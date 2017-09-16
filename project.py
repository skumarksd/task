import csv
import simplejson as json
import random
import datetime
import string
import sys
from dbconnect import DBConnector

class Task:

	def process(self,filename):
		db=DBConnector()
		db.dbHandle()

		user_aggregation={}

		c=0
		with open(filename) as bsvfile:
			spamreader = csv.reader(bsvfile, delimiter=',', quotechar='"')
			for row in spamreader:
				print row
				c+=1
				if c==1:
					print "headers"
					full_headers=row
					m_keys=row[:-1]
				else:

					whole_dump=json.dumps(row)
					q="insert into EventsDump (dump) value ('"+str(whole_dump)+"')";
					db.executeQuery(q)
					db.commit()

					query="""insert into Events ("""+",".join(m_keys)+""") values ('"""+"','".join(row[:-1])+"""') ON DUPLICATE KEY UPDATE is_current='"""+row[4]+"""',elapsed_seconds='"""+row[5]+"""',company_name='"""+row[6]+"""',client='"""+row[7]+"""',read_point='"""+row[8]+"""',biz_location='"""+row[9]+"""',biz_step='"""+row[10]+"""',version='"""+row[11]+"""'"""
					print query;

					db.executeQuery(query)
					db.commit()

					insert_id=db.getInsertId()

					user_data=json.loads(row[-1])
					user_data['eventsid']=str(insert_id)

					company=user_data.get('company')
					type_u=user_data.get('type')
					key_u=company+type_u

					if key_u not in user_aggregation:
						user_aggregation[key_u]=user_data

					query_user_data="""replace into UserData("""+",".join(user_data.keys())+""") values('"""+"','".join(user_data.values())+"""')"""
					print query_user_data

					db.executeQuery(query_user_data)
					db.commit()
		for key,values in user_aggregation:
			query_agg="insert into AggergatedUserData (rollup) values ('"+json.dumps(values)+"')"
			db.executeQuery(query_agg)
			db.commit()





	def createDataset(self,afile):
		
		user_data_keys=["partnerName","segmentTypeDeparture","functionalName","partnerTypeStart","bizLocationTypeStart","packagingTypeCode"]
		company_name=["CA1","CA2","CA3","CA4"]
		headers=["time","organization_id","raspberry_id","event_type","event_order","is_current","elapsed_seconds","company_name","client","read_point","biz_location","biz_step","version","user_data"]

		user_data_type=['Shipment','Storage','Manufacturer','Retailer','Grower']

		owner_name=["Ajay","Karthik","Abey","Noufal","Thomas","George"]
		afile.writerow(headers)
		org_id_list=[]
		rasp_id_list=[]

		is_current=[True,False]

		event_type=["FTStopEvent","FTInspectEvent","FTCommitEvent","FTHandoverEvent","FTStartEvent","FTClearEvent","FTEnableEvent","FTResetEvent","FTGroupEvent","FTUngroupEven","FTReadEvent","FTCheckpointEvent","FTWriteEvent"]
		
		for k in range(101,200):
			org_id_list.append(k)
			rasp_id_list.append('RB_'+str(k))
		print rasp_id_list


		for i in range(0,20000):
			towrite=[]
			t=datetime.datetime.now()
			towrite.append(t)
			towrite.append(random.choice(org_id_list))
			towrite.append(random.choice(rasp_id_list))
			towrite.append(random.choice(event_type))
			towrite.append(random.choice([0,1,2,3]))
			towrite.append(random.choice(is_current))
			towrite.append(str((i+1)*0.25)+" sec")
			towrite.append(random.choice(company_name))
			towrite.append("DW_BLORE")
			towrite.append("112 F")
			towrite.append("Bangalore")
			towrite.append("Blore_01")
			towrite.append(2)

			#for k in user_data_keys:
			user_data={}
			user_data["owner_name"]=random.choice(owner_name)+" "+random.choice(string.ascii_letters)
			user_data["company"]="CS_"+str(random.randint(0,20000))
			user_data["type"]=random.choice(user_data_type)

			for k in user_data_keys:
				user_data[k]=''
			user_data['tradeItemCountryOfOrigin']='india'
			user_data['lowTemp']=str(random.randint(0,6))
			user_data['referenceTemp']='37'
			user_data['referenceLife']='97'

			towrite.append(json.dumps(user_data))
			afile.writerow(towrite)

if __name__ == '__main__':
	obj=Task()

	try:
		type=sys.argv[1]
	except:
		type='process'

	if type=='create':
		cfile=open(sys.argv[2]+'.csv','w+')
		afile = csv.writer(cfile)

		obj.createDataset(afile)
	else:
		obj.process(sys.argv[2]+'.csv')



