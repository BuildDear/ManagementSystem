-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Час створення: Жов 24 2023 р., 16:28
-- Версія сервера: 10.4.28-MariaDB
-- Версія PHP: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База даних: `management`
--

-- --------------------------------------------------------

--
-- Структура таблиці `user_user`
--

CREATE TABLE `user_user` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `created` datetime(6) NOT NULL,
  `group_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `user_user`
--

INSERT INTO `user_user` (`id`, `first_name`, `last_name`, `email`, `created`, `group_id`) VALUES
(1, 'Marik', 'Mark', 'letschuka1@gmail.com', '2023-10-22 12:25:41.116396', NULL),
(2, 'Marik', 'Mark', 'letschuka2@gmail.com', '2023-10-22 12:26:29.934242', 1),
(8, 'Marta', 'Marta1', 'marta@gmail.com', '2023-10-24 14:26:54.048415', 1),
(9, 'Oleg', 'Olegovich', 'oleg@gmail.com', '2023-10-24 14:27:39.424814', 2),
(10, 'Arsen', 'Arsenovich', 'arsen@gmail.com', '2023-10-24 14:28:09.462708', 2);

--
-- Індекси збережених таблиць
--

--
-- Індекси таблиці `user_user`
--
ALTER TABLE `user_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `user_user_group_id_d81b937e_fk_user_group_id` (`group_id`);

--
-- AUTO_INCREMENT для збережених таблиць
--

--
-- AUTO_INCREMENT для таблиці `user_user`
--
ALTER TABLE `user_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Обмеження зовнішнього ключа збережених таблиць
--

--
-- Обмеження зовнішнього ключа таблиці `user_user`
--
ALTER TABLE `user_user`
  ADD CONSTRAINT `user_user_group_id_d81b937e_fk_user_group_id` FOREIGN KEY (`group_id`) REFERENCES `user_group` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
