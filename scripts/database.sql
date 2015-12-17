CREATE DATABASE IF NOT EXISTS `boruvka` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */;
USE `boruvka`;


CREATE TABLE IF NOT EXISTS `AllowedSetting` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `settingId` int(10) unsigned NOT NULL,
  `value` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `settingId` (`settingId`),
  CONSTRAINT `fk_settingId_AllowedSetting` FOREIGN KEY (`settingId`) REFERENCES `Setting` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


CREATE TABLE IF NOT EXISTS `Machine` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `tokenId` int(10) unsigned DEFAULT NULL,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `description` text COLLATE utf8mb4_bin,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `fk_tokenId_Machine` (`tokenId`),
  CONSTRAINT `fk_tokenId_Machine` FOREIGN KEY (`tokenId`) REFERENCES `Token` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


CREATE TABLE IF NOT EXISTS `Setting` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


CREATE TABLE IF NOT EXISTS `Storage` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `storageLocation` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `storageLocation` (`storageLocation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


CREATE TABLE IF NOT EXISTS `Task` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `description` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `storageId` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `fk_storageId_Task` (`storageId`),
  CONSTRAINT `fk_storageId_Task` FOREIGN KEY (`storageId`) REFERENCES `Storage` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


CREATE TABLE IF NOT EXISTS `TaskMachine` (
  `taskId` int(10) unsigned NOT NULL,
  `machineId` int(10) unsigned NOT NULL,
  PRIMARY KEY (`taskId`,`machineId`),
  KEY `fk_machineId_TaskMachine` (`machineId`),
  KEY `fk_taskId_TaskMachine` (`taskId`),
  CONSTRAINT `fk_machineId_TaskMachine` FOREIGN KEY (`machineId`) REFERENCES `Machine` (`id`),
  CONSTRAINT `fk_taskId_TaskMachine` FOREIGN KEY (`taskId`) REFERENCES `Task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


CREATE TABLE IF NOT EXISTS `Token` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `value` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `expirationDate` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `value` (`value`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


CREATE TABLE IF NOT EXISTS `User` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `tokenId` int(10) unsigned DEFAULT NULL,
  `password` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `username` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`username`),
  KEY `fk_tokenId_User` (`tokenId`),
  CONSTRAINT `fk_tokenId_User` FOREIGN KEY (`tokenId`) REFERENCES `Token` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


CREATE TABLE IF NOT EXISTS `UserSetting` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userId` int(10) unsigned NOT NULL,
  `settingId` int(10) unsigned NOT NULL,
  `allowedSettingId` int(10) unsigned DEFAULT NULL,
  `value` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_userId_UserSetting` (`userId`),
  KEY `fk_settingId_UserSetting` (`settingId`),
  KEY `fk_allowedSettingId_UserSetting` (`allowedSettingId`),
  CONSTRAINT `fk_allowedSettingId_UserSetting` FOREIGN KEY (`allowedSettingId`) REFERENCES `AllowedSetting` (`id`),
  CONSTRAINT `fk_settingId_UserSetting` FOREIGN KEY (`settingId`) REFERENCES `Setting` (`id`),
  CONSTRAINT `fk_userId_UserSetting` FOREIGN KEY (`userId`) REFERENCES `User` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;