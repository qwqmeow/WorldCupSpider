/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50722
Source Host           : 192.168.2.159:3306
Source Database       : worldcup

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2018-05-14 20:36:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for history_match
-- ----------------------------
DROP TABLE IF EXISTS `history_match`;
CREATE TABLE `history_match` (
  `team_id` int(50) NOT NULL COMMENT '队伍id',
  `schedule` varchar(50) NOT NULL COMMENT '赛程',
  `match_time` varchar(50) NOT NULL COMMENT '比赛时间',
  `home_team` varchar(255) NOT NULL COMMENT '主队',
  `market` varchar(255) NOT NULL COMMENT '盘口',
  `visit_team` varchar(255) NOT NULL COMMENT '客队',
  `score` varchar(255) NOT NULL COMMENT '总比分',
  `half_score` varchar(255) NOT NULL COMMENT '半场比分',
  `result` varchar(255) NOT NULL COMMENT '比赛胜负',
  `market_trend` varchar(255) NOT NULL COMMENT '盘路',
  `bet_type1` varchar(255) NOT NULL COMMENT '上下',
  `bet_type2` varchar(255) NOT NULL COMMENT '单双',
  `goal_number` int(11) NOT NULL COMMENT '总进球数'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
