-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 14, 2020 at 04:56 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `intern`
--

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `DEPT_ID` int(11) NOT NULL,
  `DEPT_NAME` varchar(100) NOT NULL,
  `DEPT_ADDRESS` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`DEPT_ID`, `DEPT_NAME`, `DEPT_ADDRESS`) VALUES
(1, 'Management', '2nd floor'),
(2, 'Software Engineer', '3rd floor'),
(3, 'HR', '1st floor'),
(4, 'Quality Assurance', '5th floor'),
(5, 'Head Office', '4th floor');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `EMP_ID` int(11) NOT NULL,
  `EMP_NAME` varchar(100) NOT NULL,
  `EMP_ADDRESS` varchar(100) NOT NULL,
  `DESIGNATION` varchar(100) NOT NULL,
  `DOB` date NOT NULL,
  `TELEPHONE` int(11) NOT NULL,
  `EMAIL` varchar(100) NOT NULL,
  `DEPT_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`EMP_ID`, `EMP_NAME`, `EMP_ADDRESS`, `DESIGNATION`, `DOB`, `TELEPHONE`, `EMAIL`, `DEPT_ID`) VALUES
(1, 'MRS.nimesha', '28/A,galle face road,Colombo', 'Senior software Engineer', '1992-02-02', 713865287, 'lahirubanukakck@gmail.com', 2),
(3, 'MR.banuka', '37/B,pethiyagoda,Gelioya', 'manager', '1995-06-19', 713965087, 'lahirubanukakck@gmail.com', 1),
(9, 'Mr.Rajana', '28/A,gelioya,Kandy', 'Software Engineer', '1992-05-02', 773647896, 'lahirukck@gmail.com', 2),
(10, 'MR.Thushan', '28/A,galle face road,Battaramulla', 'CEO', '1988-09-23', 713866789, 'Thushan.j@gmail.com', 5),
(11, 'Miss.Nayana', '28/A,galle face road,Kalutara', 'HR', '1990-05-02', 726374849, 'NAyana34@gmail.com', 3),
(12, 'MR.ASOKA', '28/A,galle face road,homagama', 'QA', '1991-02-02', 717865287, 'asoka345@gmail.com', 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`DEPT_ID`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`EMP_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `DEPT_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `EMP_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
