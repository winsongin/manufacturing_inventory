-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: inventory_system
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `work_in_progress`
--

DROP TABLE IF EXISTS `work_in_progress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `work_in_progress` (
  `wo_number` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  `date_recv` varchar(45) NOT NULL,
  `eta` varchar(45) NOT NULL,
  `cust_id` varchar(45) NOT NULL,
  `price` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  PRIMARY KEY (`wo_number`),
  KEY `cust_id_idx` (`cust_id`),
  CONSTRAINT `cust_id` FOREIGN KEY (`cust_id`) REFERENCES `customer` (`cust_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_in_progress`
--

LOCK TABLES `work_in_progress` WRITE;
/*!40000 ALTER TABLE `work_in_progress` DISABLE KEYS */;
INSERT INTO `work_in_progress` VALUES ('1','Shipping','03/24/2020, 11:42:14','03/24/2020, 13:42:14','85947','7.75','789 Harbor Blvd. Fullerton, CA 94857'),('10','Shipping','04/07/2020, 14:15:45','04/07/2020, 16:15:45','0621','300','123 England'),('2','Shipping','03/24/2020, 11:44:09','03/24/2020, 13:44:09','78956','4.56','123 Waze St. Fullerton, CA 95867'),('3','Shipping','03/24/2020, 11:45:40','03/24/2020, 13:45:40','21988','8.58','8490 Colonel Ave. Seal Beach, CA 95800'),('4','Shipping','03/24/2020, 11:48:06','03/24/2020, 13:48:06','8695','75.69','84956 Arts Dr. Irvine, CA 98567'),('5','Shipping','03/24/2020, 11:49:59','03/24/2020, 13:49:59','81400','73.20','1485 Path Dr. Fullerton, CA 98576'),('6','Shipping','03/24/2020, 11:51:12','03/24/2020, 13:51:12','96857','8.57','8195 Arts Dr. Fullerton, CA 94858'),('8','Shipping','04/07/2020, 00:27:14','04/07/2020, 02:27:14','78945','500','567 Linhaven'),('9','Shipping','04/07/2020, 00:30:42','04/07/2020, 02:30:42','6849','200','123 Fake Street');
/*!40000 ALTER TABLE `work_in_progress` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-07 18:24:46
