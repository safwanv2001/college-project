/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - chatbot
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`chatbot` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `chatbot`;

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `assign` */

insert  into `assign`(`assign_id`,`staff_id`,`subject_id`) values 
(7,3,10),
(9,3,11),
(16,13,9);

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `a_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `attendance` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `hour` int(11) DEFAULT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `attendance` */

insert  into `attendance`(`a_id`,`student_id`,`subject_id`,`attendance`,`date`,`hour`) values 
(1,28,9,'1','2022-06-08',1),
(2,28,9,'0','2022-06-10',2),
(3,28,9,'1','2022-05-08',1),
(4,28,9,'1','2022-06-10',1);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`user_type`) values 
(1,'admin','jdtce','admin'),
(3,'remya arun','remya12','staff'),
(13,'ninu','ninu','staff'),
(27,'basheer','basheer','parent'),
(28,'abdulla','basheer','student');

/*Table structure for table `mark` */

DROP TABLE IF EXISTS `mark`;

CREATE TABLE `mark` (
  `mark_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `mark` varchar(50) DEFAULT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`mark_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `mark` */

insert  into `mark`(`mark_id`,`staff_id`,`subject_id`,`student_id`,`mark`,`date`) values 
(5,3,8,9,'90','2022-05-25'),
(6,3,8,12,'90','2022-05-25'),
(7,13,9,9,'00','2022-05-25'),
(8,13,9,12,'08','2022-05-25'),
(9,13,9,28,'90','2022-06-07'),
(10,13,9,28,'100','2022-06-08'),
(11,3,10,28,'90','2022-06-09'),
(12,3,11,28,'90','2022-06-09');

/*Table structure for table `mentor` */

DROP TABLE IF EXISTS `mentor`;

CREATE TABLE `mentor` (
  `mentor_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`mentor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `mentor` */

insert  into `mentor`(`mentor_id`,`staff_lid`) values 
(1,3),
(3,13);

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `n_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `notification` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`n_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`n_id`,`date`,`notification`) values 
(1,'2022-05-27','hi'),
(2,'2022-06-08','hellloooooo');

/*Table structure for table `parent` */

DROP TABLE IF EXISTS `parent`;

CREATE TABLE `parent` (
  `parent_id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_lid` int(11) DEFAULT NULL,
  `f_name` varchar(50) DEFAULT NULL,
  `l_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `student_id` int(10) NOT NULL,
  PRIMARY KEY (`parent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `parent` */

insert  into `parent`(`parent_id`,`parent_lid`,`f_name`,`l_name`,`place`,`post`,`pin`,`phone`,`email`,`student_id`) values 
(3,27,'basheer','abdulla','nadakkavu','nadakkavu',673005,9808989809,'safwanv2001@gmail.com',28);

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_rid` int(11) DEFAULT NULL,
  `f_name` varchar(50) DEFAULT NULL,
  `l_name` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`staff_rid`,`f_name`,`l_name`,`gender`,`dob`,`place`,`post`,`pin`,`phone`,`email`) values 
(2,3,'remya','arun','female','2022-05-01','kannadikkal','kannadikkal',673001,9898989898,'remya@gmail.com'),
(3,13,'ninu','mol','female','8888-08-09','gsahuh','hkb',673001,9897767565,'ninu@gmail.com');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_lid` int(11) DEFAULT NULL,
  `f_name` varchar(50) DEFAULT NULL,
  `l_name` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `semester` int(11) DEFAULT NULL,
  `phone` bigint(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`student_id`,`student_lid`,`f_name`,`l_name`,`gender`,`dob`,`place`,`post`,`pin`,`semester`,`phone`,`email`) values 
(14,28,'abdulla','basheer','Male','2022-05-01','nadakkavu','nadakkavu',673005,1,9808989809,'remya arun');

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `semester` int(11) DEFAULT NULL,
  `subject` varchar(50) DEFAULT NULL,
  `subject_code` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`subject_id`,`semester`,`subject`,`subject_code`) values 
(9,1,'chemistry1','1003'),
(10,1,'workshop','1009'),
(11,1,'mathematics','1001');

/*Table structure for table `timetable` */

DROP TABLE IF EXISTS `timetable`;

CREATE TABLE `timetable` (
  `t_id` int(11) NOT NULL AUTO_INCREMENT,
  `sem` int(11) DEFAULT NULL,
  `timetable` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`t_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `timetable` */

insert  into `timetable`(`t_id`,`sem`,`timetable`) values 
(1,1,'ScreenShot_20220425112028.jpeg'),
(2,6,'Default.jpg'),
(3,2,'Default.jpg'),
(4,3,'Default.jpg'),
(5,4,'Default.jpg'),
(6,5,'Default.jpg');

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `work_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `work` text,
  `Assigned_date` varchar(50) DEFAULT NULL,
  `Submission_date` varchar(50) DEFAULT NULL,
  `Subject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`work_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `work` */

insert  into `work`(`work_id`,`staff_id`,`work`,`Assigned_date`,`Submission_date`,`Subject_id`) values 
(3,13,'hello','2022-06-07','22-06-2022',9);

/*Table structure for table `workreport` */

DROP TABLE IF EXISTS `workreport`;

CREATE TABLE `workreport` (
  `work_rid` int(11) NOT NULL AUTO_INCREMENT,
  `work_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `report` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`work_rid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `workreport` */

insert  into `workreport`(`work_rid`,`work_id`,`student_id`,`report`,`date`) values 
(2,3,28,'storage_emulated_0_WhatsApp_Media_WhatsApp_Video_VID-20220607-WA0036.mp4','2022-06-08');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
