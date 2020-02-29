-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: inventory_system
-- ------------------------------------------------------
-- Server version	8.0.17

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
  `wo_number` varchar(7) NOT NULL,
  `status` varchar(10) NOT NULL,
  `company` varchar(45) NOT NULL,
  `date_recv` date DEFAULT NULL,
  `eta` date DEFAULT NULL,
  PRIMARY KEY (`wo_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Shows data for all open work orders';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_in_progress`
--

LOCK TABLES `work_in_progress` WRITE;
/*!40000 ALTER TABLE `work_in_progress` DISABLE KEYS */;
INSERT INTO `work_in_progress` VALUES ('00001','Receiving','Target',NULL,NULL),('00002','Assembly','Best Buy',NULL,NULL),('00003','Testing','Walmart',NULL,NULL),('00004','Shipping','Microcenter',NULL,NULL),('00005','Assembly','Microcenter',NULL,NULL),('00006','Testing','Best Buy',NULL,NULL),('00007','Testing','Walmart',NULL,NULL);
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

-- Dump completed on 2020-02-29 14:12:45
