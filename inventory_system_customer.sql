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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cust_id` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `owe` varchar(45) NOT NULL,
  PRIMARY KEY (`cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('0621','Winston Churchill','123 England','300'),('09132','ToysRUs','0912 Edinger Ave. Huntington Beach, CA 98485','100.99'),('12355','Tom Bradley','945 Nutwood Ave. Fullerton, CA 98647','0.0'),('21988','Johnny Tran','8490 Colonel Ave. Seal Beach, CA 95800','78.65'),('6849','Carolyn','123 Fake Street','45.12'),('68954','Bobby Tran','8695 Lincoln Ave. Anaheim, CA 92180','35.89'),('74568','John Doe','789 Forest Hills Dr. Lake Forest, CA 98457','44.56'),('75849','Bob Seek','2385 Pool Dr. Fullerton, CA 98457','57.65'),('78495','Tennis Shop','8183 Brookhurst St. Fountain Valley, CA 92683','300.68'),('78549','Floyd Holliday','894 College Blvd. Fullerton, CA 98456','50.00'),('78945','Jetset','567 Linhaven','13.00'),('78956','John Doe','123 Waze St. Fullerton, CA 95867','48.57'),('81400','William McCarthy','1485 Path Dr. Fullerton, CA 98576','97.45'),('85947','Bobby Tarantino','789 Harbor Blvd. Fullerton, CA 94857','155.12'),('8695','Bob Mcgyver','84956 Arts Dr. Irvine, CA 98567','32.98'),('96857','Costco','8195 Arts Dr. Fullerton, CA 94858','45.75');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
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
