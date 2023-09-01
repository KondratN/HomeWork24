# create database mysqldb;
# создание базы данных use mysqldb;  выбор базы данных
# create table mycomputer(  создание таблицы мой компьютер в базе данных
# id int primary key auto_increment, firm varchar(20) not null, year_prod
# varchar(20), store_count int );
# insert into mycomputer(firm, year_prod, store_count) values('Samsung', '2023', 5),
# ('Dell', '2022', 10), ('Apple', 2020, 20), ('Huawei', 2023, 1), ('Asus', null, null), ('Xiaomi', 2021, 8);
#  select * from mycomputer  вывод таблицы mycomputer с условием
#  where firm is not null and year_prod is not null;
# select firm, year_prod from mycomputer
# where store_count > 0;
