-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 22, 2021 at 04:16 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flaskdb3`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` varchar(500) NOT NULL,
  `description` varchar(100) NOT NULL,
  `created_at` varchar(50) NOT NULL,
  `updated_at` varchar(50) NOT NULL,
  `add_by_user` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `price`, `description`, `created_at`, `updated_at`, `add_by_user`) VALUES
(1, 'test product 1', '100', 'test product 1', '2021-08-19', '2021-08-22', 'test product 1'),
(2, 'test product 2', '200', 'test product 2', '2021-08-22', '2021-08-12', 'test product 2'),
(3, 'test product 3', '300', 'test product 3', '2021-06-02', '2021-11-25', 'test product 3'),
(4, 'test product 4', '400', 'test product 4', '2021-02-26', '2013-06-12', 'test product 4'),
(5, 'test product 5', '500', 'test product 5', '2021-06-14', '2021-05-11', 'test product 5'),
(6, 'test product 6', '600', 'test product 6', '2021-08-19', '2021-08-18', 'test product 6'),
(7, 'test product 7', '700', 'test product 7', '2021-01-05', '2021-09-21', 'test product 7'),
(8, 'test product 8', '900', 'test product 8', '2026-06-10', '2016-06-22', 'test product 8'),
(9, 'test product 9', '1000', 'test product 9', '2018-02-15', '2027-10-27', 'test product 9'),
(10, 'test product 10', '1100', 'test product 10', '2015-07-10', '2018-07-22', 'test product 10');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `UID` int(11) NOT NULL,
  `UNAME` varchar(50) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `UPASS` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UID`, `UNAME`, `EMAIL`, `UPASS`) VALUES
(1, 'Test 1', 'test@gmail.com', '123456'),
(2, 'Test 2', 'test2@gmail.com', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`UID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `UID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
