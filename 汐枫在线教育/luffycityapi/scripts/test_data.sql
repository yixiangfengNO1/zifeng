-- 如果当前数据库使用了物理外键，需要先关闭原来表中的主外键约束功能
-- set FOREIGN_KEY_CHECKS=0;

-- 清空原有的课程信息表信息
truncate table fg_course_info;
-- 添加课程信息
INSERT INTO luffycity.fg_course_info (id, name, orders, is_show, is_deleted, created_time, updated_time, course_cover, course_video, course_type, level, description, pub_date, period, attachment_path, attachment_link, status, students, lessons, pub_lessons, price, recomment_home_hot, recomment_home_top, category_id, direction_id, teacher_id) VALUES
(1, '7天Typescript从入门到放弃', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-10.png', '', 0, 0, '<p>7天Typescript从入门到放弃</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 1100, 70, 15, 800.00, 0, 0, 2, 1, 1),
(2, '3天Typescript精修', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-9.png', '', 0, 0, '<p>3天Typescript精修</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 9704, 100, 100, 998.00, 1, 0, 2, 1, 2),
(3, '3天学会Vue基础', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-8.png', '', 0, 0, '<p>3天学会Vue基础</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 988, 130, 54, 500.00, 1, 0, 1, 1, 2),
(4, '算法与数据结构体系课', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-7.png', '', 0, 0, '<p>算法与数据结构体系课</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 1303, 150, 50, 998.00, 0, 1, 33, 4, 4),
(5, 'python基础入门', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-6.png', '', 0, 0, '<p>python基础入门</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 4302, 140, 30, 100.00, 0, 1, 20, 2, 4),
(6, 'javascript进阶', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-5.png', '', 0, 0, '<p>javascript进阶</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 1125, 180, 100, 1750.00, 1, 0, 5, 1, 3),
(7, '爬虫进阶之逆向工程', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-4.png', '', 0, 0, '<p>爬虫进阶之逆向工程</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 223, 145, 55, 400.00, 0, 0, 21, 2, 3),
(8, 'Kubernetes 入门到进阶实战', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-3.png', '', 0, 0, '<p>Kubernetes 入门到进阶实战</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 6074, 70, 20, 500.00, 1, 0, 50, 7, 3),
(9, 'Android 应用程序构建实战', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-2.png', '', 0, 0, '<p>Android 应用程序构建实战</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 1059, 110, 50, 550.00, 0, 0, 29, 3, 1),
(10, 'Kotlin从入门到精通', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-1.png', '', 0, 0, '<p>Kotlin从入门到精通</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 870, 120, 0, 500.00, 1, 0, 29, 3, 1),
(11, '深度学习之神经网络', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-11.png', '', 0, 0, '<p>深度学习之神经网络</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 6002, 115, 70, 80.00, 1, 0, 37, 5, 1),
(12, 'OpenCV入门到进阶', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-12.png', '', 0, 0, '<p>OpenCV入门到进阶</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 1029, 100, 70, 390.00, 0, 1, 38, 5, 2),
(13, 'Go容器化微服务系统实战', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-13.png', '', 0, 0, '<p>Go容器化微服务系统实战</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 24202, 65, 65, 399.00, 0, 0, 35, 5, 1),
(14, 'RabbitMQ精讲', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-14.png', '', 0, 0, '<p>RabbitMQ精讲</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 980, 100, 100, 710.00, 0, 0, 53, 8, 4),
(15, 'TensorFlow基础', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-15.png', '', 0, 0, '<p>RabbitMQ精讲</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 670, 220, 100, 1590.00, 0, 1, 36, 5, 2),
(16, 'ZooKeeper分布式架构搭建', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-16.png', '', 0, 0, '<p>ZooKeeper分布式架构搭建</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 90, 88, 35, 40.00, 1, 0, 35, 5, 3),
(17, '高性能MySQL调优', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-17.png', '', 0, 0, '<p>高性能MySQL调优</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 40, 300, 60, 998.00, 1, 1, 60, 10, 3),
(18, 'MySQL事务处理精选', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-18.png', '', 0, 0, '<p>MySQL事务处理精选</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 640, 65, 30, 1000.00, 1, 0, 60, 10, 1),
(19, 'MongoDB入门到进阶', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-19.png', '', 0, 0, '<p>MongoDB入门到进阶</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 11205, 86, 40, 1100.00, 0, 1, 62, 10, 3),
(20, 'Redis入门课程', 1, 1, 0, '2021-07-22 04:35:05.696823', '2021-07-22 04:35:05.696871', 'course/cover/course-20.png', '', 0, 0, '<p>Redis入门课程</p>', '2021-07-22', 7, 'luffycity-celery用法1.zip', null, 0, 120, 100, 40, 1199.00, 1, 1, 61, 10, 2);

-- 如果当前数据库使用了物理外键，开启原来表中的主外键约束功能
-- set FOREIGN_KEY_CHECKS=1;