/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50722
Source Host           : 192.168.2.159:3306
Source Database       : worldcup

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2018-05-14 20:36:09
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for team_data
-- ----------------------------
DROP TABLE IF EXISTS `team_data`;
CREATE TABLE `team_data` (
  `id` int(4) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `team_name` varchar(60) NOT NULL DEFAULT '' COMMENT '球队名称',
  `team_id` int(4) NOT NULL DEFAULT '0' COMMENT '球队编码',
  `create_year` varchar(20) NOT NULL DEFAULT '0' COMMENT '成立时间',
  `coach` varchar(255) NOT NULL DEFAULT '' COMMENT '主教练',
  `city` varchar(255) NOT NULL DEFAULT '' COMMENT '球队所在城市',
  `country` varchar(255) NOT NULL DEFAULT '' COMMENT '国家',
  `league` varchar(255) NOT NULL DEFAULT '' COMMENT '联赛',
  `intro` text COMMENT '球队介绍',
  `website` varchar(255) NOT NULL DEFAULT '' COMMENT '官网地址',
  `team_member` text COMMENT '成员',
  `img_url` varchar(255) NOT NULL DEFAULT '' COMMENT '图片地址',
  `match_place` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`,`team_id`),
  KEY `team_data_team_id` (`team_id`),
  KEY `team_data_name` (`team_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
