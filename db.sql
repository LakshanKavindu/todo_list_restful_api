
use id20353168_todo_db;
CREATE TABLE `new_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `todoname` varchar(45) DEFAULT NULL,
  `is_deleted` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

insert into new_table ('username','todoname','is_deleted') values("nipun","do react",0);
insert into new_table ('username','todoname','is_deleted') values("gattu","do react and vanilla js",0);
insert into new_table ('username','todoname','is_deleted') values("charuka","do shiny stuff",0);


alter table new_table add is_done int default 0;