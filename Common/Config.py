__author__ = 'Administrator'
import dict4ini
try:
    class Config:
        config=dict4ini.DictIni('conf.ini')
        def __init__(self):
            self.config=dict4ini.DictIni('conf.ini')
            a="ninni"
except Exception,e:
    print e

# if __name__ == '__main__':
#     d = config
#     user= d.dataBaseCon.user
#     host=d.dataBaseCon.host
#     passwd=d.dataBaseCon.passwd



