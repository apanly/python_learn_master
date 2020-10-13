### 数据库初始化记录

```
CREATE DATABASE `learn_master` DEFAULT COLLATE = `utf8mb4_general_ci`;
use learn_master;
CREATE TABLE `action` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '权限ID',
  `level1_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '一级菜单名称',
  `level2_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '二级菜单名称',
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '权限名',
  `url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '允许访问的链接,用特殊字符分割',
  `level1_weight` tinyint NOT NULL DEFAULT '0' COMMENT '一级菜单权重',
  `level2_weight` tinyint NOT NULL DEFAULT '0' COMMENT '二级菜单权重',
  `weight` tinyint NOT NULL DEFAULT '0' COMMENT '权重 越大排名越前面',
  `is_important` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否是重要权限',
  `status` tinyint NOT NULL DEFAULT '1' COMMENT '1 有效 0无效',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='权限表';


CREATE TABLE `app_access_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int NOT NULL DEFAULT '0' COMMENT '用户表id',
  `uname` varchar(20) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '用户表姓名',
  `referer_url` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '当前访问的refer',
  `target_url` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '访问的url',
  `query_params` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'get和post参数',
  `ua` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '访问ua',
  `ip` varchar(32) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '访问ip',
  `note` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'json格式备注字段',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入日期',
  PRIMARY KEY (`id`),
  KEY `idx_created_time` (`created_time`),
  KEY `idx_uid` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户访问日志记录表';




CREATE TABLE `app_err_log` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `request_uri` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '请求uri',
  `referer` varchar(500) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '来源url',
  `content` varchar(3000) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '日志内容',
  `ip` varchar(100) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'ip',
  `ua` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'ua信息',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_created_time` (`created_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='app错误日表';




CREATE TABLE `link` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `type` tinyint NOT NULL DEFAULT '0' COMMENT '类型',
  `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '标题',
  `url` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '网址',
  `weight` int NOT NULL DEFAULT '1' COMMENT '权重 越大越排前',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态： 1：有效  0：无效',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='网址管理';





CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '角色ID',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '角色名',
  `pid` int NOT NULL DEFAULT '0' COMMENT '父级id',
  `status` tinyint NOT NULL DEFAULT '1' COMMENT '1有效 0无效',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='角色部门表';




CREATE TABLE `role_action` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '角色权限ID',
  `role_id` int NOT NULL DEFAULT '0' COMMENT '角色ID',
  `action_id` int NOT NULL DEFAULT '0' COMMENT '权限ID',
  `status` tinyint NOT NULL DEFAULT '1' COMMENT '1有效 0无效',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_role_action_id` (`role_id`,`action_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='角色权限表';



CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '邮箱地址也是登录用户名',
  `role_id` int NOT NULL DEFAULT '0' COMMENT '人员所属部门',
  `salt` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '随机码',
  `is_root` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否是管理员 1：是 0：不是',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态 1：有效 0：无效',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户表';




CREATE TABLE `user_news` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '消息id',
  `uid` int unsigned NOT NULL DEFAULT '0' COMMENT '用户id',
  `title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '标题',
  `content` varchar(1500) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '内容',
  `status` tinyint unsigned NOT NULL DEFAULT '0' COMMENT '状态 0：未读 1：已读',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC COMMENT='用户站内消息表';





```

#### 初始化数据
```

##下面的邮箱换成你自己的就行了

INSERT INTO `user` (`id`, `name`, `email`, `role_id`, `salt`, `is_root`, `status`, `updated_time`, `created_time`)
VALUES
	(1, '即学即码工作室', 'apanly@163.com', 0, 'HRD60OnSkN4dpCDH', 1, 1, '2020-08-23 14:41:11', '2018-05-16 23:50:43');

INSERT INTO `link` (`id`, `type`, `title`, `url`, `weight`, `status`, `updated_time`, `created_time`)
VALUES
	(1, 5, '即学即码官网', 'http://www.jixuejima.cn/', 1, 1, '2020-10-13 20:05:00', '2020-08-18 14:31:23'),
	(2, 5, '即学即码博文', 'http://www.jixuejima.cn/article/index', 1, 1, '2020-10-13 20:04:56', '2020-08-18 14:31:43'),
	(3, 5, '即学即码文档中心', 'http://dcenter.jixuejima.cn/#/', 1, 1, '2020-08-18 14:32:14', '2020-08-18 14:32:14'),
	(4, 5, 'CTBox：网址收藏夹', 'http://dcenter.jixuejima.cn/#/ctbox/readme', 1, 1, '2020-10-13 20:04:27', '2020-08-18 14:32:32'),
	(5, 5, '编程浪子', 'http://www.54php.cn/', 1, 1, '2020-10-13 20:05:24', '2020-08-18 14:32:51'),
	(6, 3, 'Jobs（乔布斯）管理调度平台', 'http://dcenter.jixuejima.cn/#/flask/jobs/readme', 1, 1, '2020-10-13 20:05:58', '2020-08-18 14:33:18');


INSERT INTO `role` (`id`, `name`, `pid`, `status`, `updated_time`, `created_time`)
VALUES
	(1, '总裁办', 0, 1, '2020-08-19 01:26:04', '2020-08-19 01:16:15'),
	(2, '人事部门', 1, 1, '2020-10-13 20:21:05', '2020-08-19 01:23:19'),
	(3, '研发部门', 1, 1, '2020-08-20 01:34:08', '2020-08-20 01:33:55'),
	(4, '设计部门', 1, 1, '2020-08-20 01:37:14', '2020-08-20 01:37:14');



INSERT INTO `action` (`id`, `level1_name`, `level2_name`, `name`, `url`, `level1_weight`, `level2_weight`, `weight`, `is_important`, `status`, `updated_time`, `created_time`)
VALUES
	(1, '系统日志', '访问日志', '访问日志', '/home/log/access', 1, 60, 1, 0, 1, '2020-08-24 19:31:31', '2020-08-20 00:58:46'),
	(3, '系统日志', '错误日志', '错误日志', '/home/log/error', 1, 50, 1, 0, 1, '2020-08-24 17:52:04', '2020-08-20 01:04:24'),
	(6, '仪表盘', '首页', '首页', '/home/', 60, 1, 1, 0, 1, '2020-08-24 18:13:22', '2020-08-24 17:51:45'),
	(7, '网址之家', '网址管理', '网址管理', '/home/link/index', 55, 60, 1, 0, 1, '2020-08-24 18:05:39', '2020-08-24 17:54:40'),
	(8, '员工管理', '员工列表', '员工管理', '/home/rbac/staff/index', 50, 60, 1, 0, 1, '2020-08-24 17:55:24', '2020-08-24 17:55:24'),
	(9, '员工管理', '部门列表', '部门管理', '/home/rbac/dept/index', 50, 55, 1, 0, 1, '2020-08-24 17:56:32', '2020-08-24 17:56:32'),
	(10, '员工管理', '权限分配', '权限分配', '/home/rbac/grant/assign', 50, 50, 1, 1, 1, '2020-08-24 19:31:25', '2020-08-24 17:57:01'),
	(11, '员工管理', '权限管理', '权限管理', '/home/rbac/grant/index', 50, 45, 1, 0, 1, '2020-08-24 17:57:39', '2020-08-24 17:57:39'),
	(12, '网址之家', '网址管理', '编辑/添加', '/home/link/set', 55, 50, 1, 0, 1, '2020-08-24 18:05:25', '2020-08-24 18:05:17'),
	(13, '网址之家', '网址管理', '删除/恢复', '/home/link/ops', 55, 45, 1, 0, 1, '2020-08-24 18:09:50', '2020-08-24 18:09:50'),
	(14, '员工管理', '部门列表', '添加/编辑', '/home/rbac/dept/set', 50, 55, 1, 0, 1, '2020-08-24 18:10:34', '2020-08-24 18:10:34'),
	(15, '员工管理', '部门列表', '删除/恢复', '/home/rbac/dept/ops', 50, 55, 1, 0, 1, '2020-08-24 18:10:50', '2020-08-24 18:10:50'),
	(16, '员工管理', '员工列表', '添加/编辑', '/home/rbac/staff/set', 50, 60, 1, 0, 1, '2020-08-24 18:11:19', '2020-08-24 18:11:19'),
	(17, '员工管理', '员工列表', '删除/恢复', '/home/rbac/staff/ops', 50, 60, 1, 0, 1, '2020-08-24 18:11:38', '2020-08-24 18:11:38'),
	(18, '员工管理', '权限管理', '添加/编辑/复制', '/home/rbac/grant/set', 50, 45, 1, 0, 1, '2020-08-24 18:12:33', '2020-08-24 18:12:05'),
	(19, '员工管理', '权限管理', '删除/恢复', '/home/rbac/grant/ops', 50, 45, 1, 0, 1, '2020-08-24 18:12:27', '2020-08-24 18:12:27');


INSERT INTO `user_news` ( `uid`, `title`, `content`, `status`, `updated_time`, `created_time`)
VALUES
	(1, '欢迎使用即学即码Flask CMS V2框架', '使用教程请查看：http://dcenter.jixuejima.cn/#/flask/v2/readme~~', 0, '2020-10-11 21:52:33', '2020-10-11 21:52:33');


```
