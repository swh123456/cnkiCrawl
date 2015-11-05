# -*- coding: utf-8 -*-
from Mysql import MysqlOb

__author__ = 'Administrator'
import MySQLdb
import sys
sys.path.append("..")
import Common.dict4ini as dict4ini
import string
from cnkiCrawl.items import Cnki,Auth

mysql=MysqlOb()
class MagOper(object):
    global mysqlOb
    def UpdatePage(self,id,page):
        # global cursor
        sql='update tb_magazine set pageint=%d where id=%d'
        param=(page,id)
        n = mysqlOb.cursor.execute(sql, param)
        return n
    def UpdateState(self,id):
        sql='update tb_magazine set state=1 where id=%d'
        param=(id)
        n = mysqlOb.cursor.execute(sql, param)
        return n
    def magQue(self):
        sql='select *from tb_magazine where state=0'
        n =mysqlOb. cursor.execute(sql)
        result=mysqlOb.cursor.fetchall()
        return result
class Oper(object):
    def add(self,a):
        pass
    def delete(self,b):
        pass

class cnkiOper(Oper):
    global mysql
    def add(self,a):
        # cnki=Cnki(a)

        print mysql.config
        print mysql.host
        print mysql.user
        sql='insert into tb_cnki(name,abstracts,mystamptime) values(%s,%s,%s)'
        param=(a['title'],a['abs'],string.atoi(str(a['myStTime'])))
        print param
        n = mysql.cursor.execute(sql, param)
        return n
    def Que(self,name):
        sql='select * from tb_cnki where name=%s'
        param=(name)
        n = mysqlOb.cursor.execute(sql, param)
        result=mysqlOb.cursor.fetchall()
        id=result[n-1][1]
        return id

class AuthOper(Oper):
    global mysqlOb
    def add(self,a):
        sql='insert into tb_author_cn(cnki_id,author_name,uniq_id) values(%d,%s,%s)'
        param=(a.cnki_id,a.name,a.uniq_id)
        n = mysqlOb.cursor.execute(sql, param)
        return n









