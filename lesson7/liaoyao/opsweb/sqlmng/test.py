#!/usr/bin/python
#-\*-coding: utf-8-\*-

''' 建表语句
CREATE TABLE IF NOT EXISTS `mytable1`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `myname` VARCHAR(10) NOT NULL,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

import MySQLdb

# 待审核/执行的sql语句（需包含目标数据库的地址、端口 等参数）
sql='/* --user=root;--password=123456;--host=10.10.10.90;--port=3306;--enable-execute; */\
inception_magic_start;\
use inc_test;\
insert into mytable1 (myname) values ("xianyu1"),("xianyu2");\
insert into mytable1 (myname) values ("xianyu1"),("xianyu2");\
delete from mytable1 where id=1;\
inception_magic_commit;'
try:
    conn=MySQLdb.connect(host='10.10.10.90',user='',passwd='',db='',port=6669,use_unicode=True,charset="utf8")  # inception的地址、端口等
    cur=conn.cursor()
    ret=cur.execute(sql)
    result=cur.fetchall()
    num_fields = len(cur.description) 
    field_names = [i[0] for i in cur.description]
    print result
    '''
    for row in result:
        print row[0], "|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",
        row[5],"|",row[6],"|",row[7],"|",row[8],"|",row[9],"|",row[10]
    '''
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

