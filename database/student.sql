CREATE DATABASE  IF NOT EXISTS `face_recognizer` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `face_recognizer`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: face_recognizer
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `fname` varchar(20) NOT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `contact` varchar(45) DEFAULT NULL,
  `user_name` varchar(45) NOT NULL,
  `securityQ` varchar(45) DEFAULT NULL,
  `securityA` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES ('abc','abc','123','abc','Your Birth Place','abc','123'),('cde','cde','456','cde','Your Birth Place','cde','456'),('Rudra','Jain','123','rudra','Your Birth Place','Bhopal','123'),('Rudra','Jain','123','rudra@gmail.com','Your Birth Place','Bhopal','123');
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Dep` varchar(45) DEFAULT NULL,
  `course` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `Semester` varchar(45) DEFAULT NULL,
  `Student_id` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Batch` varchar(45) DEFAULT NULL,
  `Roll` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `Dob` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Teacher` varchar(45) DEFAULT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('  CSE  ','  B.Tech  ','   2023-24   ','   6th  ','01','Rudra Jain','Batch-1','01','Male','08/07/2003','rudra@gmail.com','12345678','Indore','abc','Yes'),('  CSE  ','  B.Tech  ','   2023-24   ','   6th  ','10','Yash Jhalwar','Batch-2','10','Male','25/09/2003','Yash23@gmail.com','123465798','Indore','abc','Yes'),('  CSE  ','  B.Tech  ','   2023-24   ','   6th  ','2','Vitthal Magarde','Batch-2','2','Male','08/07/2003','vitthal@gmail.com','123456789','Indore','abc','Yes'),('  CSE  ','  B.Tech  ','   2023-24   ','   6th  ','3','Shivang ','Batch-2','3','Male','08/07/2003','shivang@gmail.com','123456789','Indore','abc','Yes'),('  CSE  ','  B.Tech  ','   2023-24   ','   6th  ','5','Varsha','Batch-2','5','Female','08/07/2003','yash@gmail.com','123456789','Indore','abc','Yes'),('  CSE  ','  B.Tech  ','   2023-24   ','   6th  ','6','yash','Batch-2','6','Male','08/07/2003','yash@gmail.com','123456789','Indore','abc','Yes'),('  CSE  ','  B.Tech  ','   2023-24   ','   6th  ','7','Saloni','Batch-1','7','Female','08/07/2003','saloni@gmail.com','123456789','Indore','abc','Yes'),('  CSE  ','  B.Tech  ','   2023-24   ','   6th  ','8','Vidhi Batheja','Batch-1','8','Female','18/09/2003','vidhi123@gmail.com','123456798','Indore','abc','Yes'),('  CSE  ','  B.Tech  ','   2023-24   ','   6th  ','9','Vijay','Batch-2','9','Male','18/09/2003','Vijay23@gmail.com','123456798','Indore','abc','Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-02 17:01:49
