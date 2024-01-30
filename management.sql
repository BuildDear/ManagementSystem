-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Час створення: Гру 05 2023 р., 09:17
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
-- Структура таблиці `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблиці `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'managers'),
(2, 'users');

-- --------------------------------------------------------

--
-- Структура таблиці `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблиці `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add note model', 6, 'add_notemodel'),
(22, 'Can change note model', 6, 'change_notemodel'),
(23, 'Can delete note model', 6, 'delete_notemodel'),
(24, 'Can view note model', 6, 'view_notemodel'),
(25, 'Can add group model', 7, 'add_groupmodel'),
(26, 'Can change group model', 7, 'change_groupmodel'),
(27, 'Can delete group model', 7, 'delete_groupmodel'),
(28, 'Can view group model', 7, 'view_groupmodel'),
(29, 'Can add user model', 8, 'add_usermodel'),
(30, 'Can change user model', 8, 'change_usermodel'),
(31, 'Can delete user model', 8, 'delete_usermodel'),
(32, 'Can view user model', 8, 'view_usermodel'),
(33, 'Can add Token', 9, 'add_token'),
(34, 'Can change Token', 9, 'change_token'),
(35, 'Can delete Token', 9, 'delete_token'),
(36, 'Can view Token', 9, 'view_token'),
(37, 'Can add token', 10, 'add_tokenproxy'),
(38, 'Can change token', 10, 'change_tokenproxy'),
(39, 'Can delete token', 10, 'delete_tokenproxy'),
(40, 'Can view token', 10, 'view_tokenproxy');

-- --------------------------------------------------------

--
-- Структура таблиці `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-12-05 07:00:44.962994', '1', 'managers', 1, '[{\"added\": {}}]', 3, 5),
(2, '2023-12-05 07:00:59.749449', '7', 'manager@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Custom_user_groups\", \"Groups\"]}}]', 8, 5),
(3, '2023-12-05 07:01:13.733454', '2', 'users', 1, '[{\"added\": {}}]', 3, 5),
(4, '2023-12-05 07:01:43.204837', '6', 'user@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 8, 5);

-- --------------------------------------------------------

--
-- Структура таблиці `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'groupmodel'),
(6, 'accounts', 'notemodel'),
(8, 'accounts', 'usermodel'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(9, 'authtoken', 'token'),
(10, 'authtoken', 'tokenproxy'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Структура таблиці `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-11-30 09:01:31.720134'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-11-30 09:01:31.839511'),
(3, 'auth', '0001_initial', '2023-11-30 09:01:32.292090'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-11-30 09:01:32.401797'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-11-30 09:01:32.426627'),
(6, 'auth', '0004_alter_user_username_opts', '2023-11-30 09:01:32.455552'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-11-30 09:01:32.483475'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-11-30 09:01:32.496440'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-11-30 09:01:32.530671'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-11-30 09:01:32.553261'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-11-30 09:01:32.576122'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-11-30 09:01:32.635961'),
(13, 'auth', '0011_update_proxy_permissions', '2023-11-30 09:01:32.659900'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-11-30 09:01:32.683971'),
(15, 'accounts', '0001_initial', '2023-11-30 09:01:33.519289'),
(16, 'admin', '0001_initial', '2023-11-30 09:01:33.690826'),
(17, 'admin', '0002_logentry_remove_auto_add', '2023-11-30 09:01:33.711707'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2023-11-30 09:01:33.731685'),
(19, 'authtoken', '0001_initial', '2023-11-30 09:01:33.897630'),
(20, 'authtoken', '0002_auto_20160226_1747', '2023-11-30 09:01:33.963980'),
(21, 'authtoken', '0003_tokenproxy', '2023-11-30 09:01:33.972466'),
(22, 'sessions', '0001_initial', '2023-11-30 09:01:34.030275'),
(23, 'accounts', '0002_groupmodel_created', '2023-11-30 19:15:39.758075'),
(24, 'accounts', '0003_remove_groupmodel_note_notemodel_group', '2023-11-30 19:45:25.852562'),
(25, 'accounts', '0004_usermodel_is_staff', '2023-12-04 22:13:20.187544');

-- --------------------------------------------------------

--
-- Структура таблиці `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('gxrcfoudo27947m3j1e03o2oy257ge9v', '.eJxVjEEOwiAQRe_C2hAoUhiX7nsGMgyDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERIE6_W0R6cN1BumO9NUmtrssc5a7Ig3Y5tcTP6-H-HRTs5VszabZmiIbBGSalmR0yMpAyKluHCrwlP2Qk57IejRkz6wxwzgoTePH-AAPMOHo:1rAQD5:rulEgL7pmzytfn1AlwBrIoBTJ9OXmxPd9jEonCf1djM', '2023-12-19 07:51:15.761778');

-- --------------------------------------------------------

--
-- Структура таблиці `note`
--

CREATE TABLE `note` (
  `id` bigint(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `created` datetime(6) NOT NULL,
  `group_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `note`
--

INSERT INTO `note` (`id`, `name`, `description`, `created`, `group_id`) VALUES
(2, 'video', 'birthday', '2023-11-30 19:47:01.514418', 1),
(3, 'drink', 'beerrr', '2023-12-01 20:07:17.614006', 1),
(4, 'video', 'I will record', '2023-12-02 09:48:43.005196', 2),
(5, 'breakfest', 'Beer, whiskey, vine', '2023-12-02 09:49:56.074486', 2),
(6, 'dinner', 'only protein', '2023-12-02 09:52:11.221638', 2),
(7, 'evening', 'train, sleep, repeat', '2023-12-02 09:53:00.968704', 2),
(8, 'somee', 'somee', '2023-12-02 11:43:17.635541', 4);

-- --------------------------------------------------------

--
-- Структура таблиці `user`
--

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `created` datetime(6) NOT NULL,
  `is_manager` tinyint(1) NOT NULL,
  `group_id` bigint(20) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `user`
--

INSERT INTO `user` (`id`, `password`, `last_login`, `is_superuser`, `first_name`, `last_name`, `email`, `created`, `is_manager`, `group_id`, `is_staff`) VALUES
(4, '123', '2023-12-02 11:44:11.880085', 0, 'Маркіян', 'Лещука', 'letschuka111@gmail.com', '2023-12-02 11:43:55.321410', 1, 1, 0),
(5, '12345', '2023-12-05 07:00:11.050136', 1, 'Marik', 'Manager', 'less@gmail.com', '2023-12-04 22:13:48.308607', 1, 1, 1),
(6, 'pbkdf2_sha256$600000$G0psVIqSRV5f2ctox6EO1M$mZ9Sl1wR3u52d+GMOIk/4BVM8hUlIvKOu5rKeaj0lbs=', '2023-12-05 06:57:17.000000', 0, 'User', 'Mark', 'user@gmail.com', '2023-12-05 06:39:17.900699', 0, 2, 0),
(7, 'pbkdf2_sha256$600000$GebvD4nsZRxQh2zsYonw2T$uweiLTaUrglk65tKHhZSHwCmwUv2OEN9TLoZJDT9WGc=', '2023-12-05 07:38:41.817727', 1, 'Manager', 'Mark', 'manager@gmail.com', '2023-12-05 06:40:35.449369', 1, 1, 0),
(8, 'pbkdf2_sha256$600000$sf4F8lHo66aG92VkJdhslW$vK5WSHpdH8yLptsCKjO/Lx4bMIUq1/5SrqnCtAG6VP0=', '2023-12-05 07:38:59.636687', 1, 'Supermanager', '', 'supermanager@gmail.com', '2023-12-05 07:15:59.942702', 1, NULL, 1),
(9, 'pbkdf2_sha256$600000$Uayf3m0vBwK84z3BKCyvC5$+7OnJhKGm3vhvguJXEOaE9N7aVc5Neg2hx3qw9Zqxe4=', '2023-12-05 07:51:15.756794', 0, 'User', 'User1', 'user1@gmail.com', '2023-12-05 07:17:31.049001', 0, 1, 0);

-- --------------------------------------------------------

--
-- Структура таблиці `user_group`
--

CREATE TABLE `user_group` (
  `id` bigint(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` varchar(20) NOT NULL,
  `created` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `user_group`
--

INSERT INTO `user_group` (`id`, `name`, `description`, `created`) VALUES
(1, 'school', 'birthday', '2023-11-30 19:15:39.722169'),
(2, 'arsen_patty', 'best !!!', '2023-11-30 19:15:39.722169'),
(3, 'sport', 'math and algo !!!', '2023-11-30 19:16:36.340077'),
(4, 'python', 'someee', '2023-12-02 11:42:57.025976');

-- --------------------------------------------------------

--
-- Структура таблиці `user_groups`
--

CREATE TABLE `user_groups` (
  `id` bigint(20) NOT NULL,
  `usermodel_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп даних таблиці `user_groups`
--

INSERT INTO `user_groups` (`id`, `usermodel_id`, `group_id`) VALUES
(2, 6, 2),
(1, 7, 1);

-- --------------------------------------------------------

--
-- Структура таблиці `user_user_permissions`
--

CREATE TABLE `user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `usermodel_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Індекси збережених таблиць
--

--
-- Індекси таблиці `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Індекси таблиці `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Індекси таблиці `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Індекси таблиці `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Індекси таблиці `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_user_id` (`user_id`);

--
-- Індекси таблиці `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Індекси таблиці `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Індекси таблиці `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Індекси таблиці `note`
--
ALTER TABLE `note`
  ADD PRIMARY KEY (`id`),
  ADD KEY `note_group_id_786fecd4_fk_user_group_id` (`group_id`);

--
-- Індекси таблиці `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `user_group_id_50ce08ac_fk_user_group_id` (`group_id`);

--
-- Індекси таблиці `user_group`
--
ALTER TABLE `user_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Індекси таблиці `user_groups`
--
ALTER TABLE `user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_groups_usermodel_id_group_id_b92f3245_uniq` (`usermodel_id`,`group_id`),
  ADD KEY `user_groups_group_id_b76f8aba_fk_auth_group_id` (`group_id`);

--
-- Індекси таблиці `user_user_permissions`
--
ALTER TABLE `user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_user_permissions_usermodel_id_permission_id_a6d6add3_uniq` (`usermodel_id`,`permission_id`),
  ADD KEY `user_user_permission_permission_id_9deb68a3_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT для збережених таблиць
--

--
-- AUTO_INCREMENT для таблиці `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблиці `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблиці `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT для таблиці `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблиці `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблиці `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT для таблиці `note`
--
ALTER TABLE `note`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблиці `user`
--
ALTER TABLE `user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT для таблиці `user_group`
--
ALTER TABLE `user_group`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблиці `user_groups`
--
ALTER TABLE `user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблиці `user_user_permissions`
--
ALTER TABLE `user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Обмеження зовнішнього ключа збережених таблиць
--

--
-- Обмеження зовнішнього ключа таблиці `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Обмеження зовнішнього ключа таблиці `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Обмеження зовнішнього ключа таблиці `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Обмеження зовнішнього ключа таблиці `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Обмеження зовнішнього ключа таблиці `note`
--
ALTER TABLE `note`
  ADD CONSTRAINT `note_group_id_786fecd4_fk_user_group_id` FOREIGN KEY (`group_id`) REFERENCES `user_group` (`id`);

--
-- Обмеження зовнішнього ключа таблиці `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_group_id_50ce08ac_fk_user_group_id` FOREIGN KEY (`group_id`) REFERENCES `user_group` (`id`);

--
-- Обмеження зовнішнього ключа таблиці `user_groups`
--
ALTER TABLE `user_groups`
  ADD CONSTRAINT `user_groups_group_id_b76f8aba_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_groups_usermodel_id_edcb1e77_fk_user_id` FOREIGN KEY (`usermodel_id`) REFERENCES `user` (`id`);

--
-- Обмеження зовнішнього ключа таблиці `user_user_permissions`
--
ALTER TABLE `user_user_permissions`
  ADD CONSTRAINT `user_user_permission_permission_id_9deb68a3_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_user_permissions_usermodel_id_261a7b99_fk_user_id` FOREIGN KEY (`usermodel_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
