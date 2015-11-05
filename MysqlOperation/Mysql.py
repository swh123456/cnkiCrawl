import MySQLdb
import sys
sys.path.append("..")
from Common import dict4ini

__author__ = 'Administrator'
class MysqlOb(object):
    def __init__(self):
        self.config=dict4ini.DictIni('C:/Users/Administrator/Desktop/conf.ini')
        self.host=self.config.dataBaseCon.host
        self.user=self.config.dataBaseCon.user
        self.passwd=self.config.dataBaseCon.passwd
        self.db=self.config.dataBaseCon.db
        self.port=self.config.dataBaseCon.port
        self.conn=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=self.port,charset='utf8')
        self.cursor=self.conn.cursor()

