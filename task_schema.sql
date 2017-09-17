-- MySQL dump 10.13  Distrib 5.6.25, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: data_engg_task
-- ------------------------------------------------------
-- Server version	5.6.25-0ubuntu0.15.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AggergatedUserData`
--

DROP TABLE IF EXISTS `AggergatedUserData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AggergatedUserData` (
  `UUID` int(11) NOT NULL AUTO_INCREMENT,
  `rollup` longtext NOT NULL,
  PRIMARY KEY (`UUID`)
) ENGINE=InnoDB AUTO_INCREMENT=18046 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Events`
--

DROP TABLE IF EXISTS `Events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Events` (
  `time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `organization_id` int(11) NOT NULL,
  `raspberry_id` varchar(20) NOT NULL,
  `event_order` int(11) NOT NULL,
  `is_current` tinyint(1) NOT NULL,
  `elapsed_seconds` varchar(20) NOT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `client` varchar(20) DEFAULT NULL,
  `read_point` varchar(20) DEFAULT NULL,
  `biz_location` varchar(20) DEFAULT NULL,
  `biz_step` varchar(20) DEFAULT NULL,
  `version` int(11) NOT NULL,
  `event_type` enum('FTStopEvent','FTInspectEvent','FTCommitEvent','FTHandoverEvent','FTStartEvent','FTClearEvent','FTEnableEvent','FTResetEvent','FTGroupEvent','FTUngroupEven','FTReadEvent','FTCheckpointEvent','FTWriteEvent') NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`time`,`organization_id`,`raspberry_id`,`event_type`,`event_order`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20003 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `EventsDump`
--

DROP TABLE IF EXISTS `EventsDump`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EventsDump` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dump` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40003 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `UserData`
--

DROP TABLE IF EXISTS `UserData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserData` (
  `owner_name` varchar(50) NOT NULL,
  `company` varchar(50) NOT NULL,
  `type` enum('Shipment','Storage','Manufacturer','Retailer','Grower') NOT NULL,
  `partnerName` varchar(50) DEFAULT NULL,
  `segmentTypeDeparture` varchar(50) DEFAULT NULL,
  `functionalName` varchar(50) DEFAULT NULL,
  `partnerTypeStart` varchar(50) DEFAULT NULL,
  `bizLocationTypeStart` varchar(50) DEFAULT NULL,
  `packagingTypeCode` varchar(50) DEFAULT NULL,
  `tradeItemCountryOfOrigin` varchar(50) NOT NULL,
  `lowTemp` int(11) NOT NULL,
  `referenceTemp` int(11) NOT NULL,
  `referenceLife` int(11) DEFAULT NULL,
  `eventsid` int(11) NOT NULL,
  PRIMARY KEY (`owner_name`,`company`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-17  7:28:24
