-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 22, 2023 at 07:16 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `1collegeasspy`
--

-- --------------------------------------------------------

--
-- Table structure for table `assigntb`
--

CREATE TABLE `assigntb` (
  `id` bigint(250) NOT NULL,
  `AssignmentName` varchar(250) NOT NULL,
  `SubjectName` varchar(250) NOT NULL,
  `LastDate` varchar(250) NOT NULL,
  `Degree` varchar(250) NOT NULL,
  `Department` varchar(250) NOT NULL,
  `Year` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `Regno` varchar(250) NOT NULL,
  `AssFile` varchar(500) NOT NULL,
  `Status` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `Regno` varchar(250) NOT NULL,
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Phone` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `Degree` varchar(250) NOT NULL,
  `Department` varchar(250) NOT NULL,
  `Year` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`Regno`, `Name`, `Gender`, `Age`, `Email`, `Phone`, `Address`, `Degree`, `Department`, `Year`) VALUES
('20UBC609', 'Sebastin Benadict Joshwa D', 'male', '20', 'joshwadsb@gmail.com', '8883166011', 'No. 438, Valayampatti, Sivagangai   District', 'bca', 'it', '3');

-- --------------------------------------------------------

--
-- Table structure for table `temptb`
--

CREATE TABLE `temptb` (
  `AssignmentName` varchar(250) NOT NULL,
  `Regno` varchar(250) NOT NULL,
  `FileName` varchar(250) NOT NULL,
  `Regno1` varchar(250) NOT NULL,
  `FileName1` varchar(250) NOT NULL,
  `Similarity` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `assigntb`
--
ALTER TABLE `assigntb`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `assigntb`
--
ALTER TABLE `assigntb`
  MODIFY `id` bigint(250) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
