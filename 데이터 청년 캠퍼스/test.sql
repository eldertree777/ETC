create table tashu_using_status(
    대여스테이션 smallint unsigned not null,
    대여일시 bigint unsigned,
    반납스테이션 smallint unsigned,
    반납일시 bigint unsigned,
    이동거리 int unsigned,
    회원구분 enum('0', '1', '2')
);