SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `user_test`
-- ----------------------------
DROP TABLE IF EXISTS `user_test`;
CREATE TABLE `user_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `user_name` varchar(20) NOT NULL COMMENT '用户名',
  `pass_word` varchar(50) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `user_test`
-- ----------------------------
BEGIN;
INSERT INTO `user_test` VALUES ('1', 'wangkun', 'wangkun123', '17621749522'), ('2', 'vayne', 'vayne123', '18326559547');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
