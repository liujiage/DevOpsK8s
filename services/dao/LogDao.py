from abc import ABC

from common.StrUtils import isEmpty, isAnyEmpty
from common.TimeUtils import getTimeStr
from services.dao.SqliteDao import SqliteDao
from vo.LogVO import LogVO

'''
@Author Jiage
@Date 2021-09-09
@Function query and save deploys log 
'''
class LogDao(SqliteDao):

    '''
    @Author Jiage
    @Date 2021-09-08
    @Function query deploys log
    '''

    def query(self, value=None) -> list:
        records = self.fetch(
            'select id,create_time,user_name,service_name,version,nodes,port from deploy_log order by create_time desc limit 500')
        res = []
        if isEmpty(records): return res;
        for record in records:
            res.append(LogVO(id=record[0], createTime=record[1], userName=record[2], serviceName=record[3], version=record[4], nodes=record[5], port=record[6]))
        return res

    '''
    @Author Jiage
    @Date 2021-09-08
    @Function Save data into the database as a log
    '''

    def updateOrInsert(self, value: LogVO) -> int:
        print("'%s' - ,'%s' - ,'%s' - ,'%s' - ,'%s' - ,'%s' - ,'%s')" % (
                value.id, value.createTime, value.userName, value.serviceName,
                value.version, value.nodes, value.port))
        # get and check value
        value = self.__getValueWithCheck(value)
        if value is None: return 0
        return self.execute(
            "insert into deploy_log(id,create_time,user_name,service_name,version,nodes,port) "
            "values('%s','%s','%s','%s','%s','%s','%s')" % (
                value.id, value.createTime, value.userName, value.serviceName,
                value.version, value.nodes, value.port))

    '''
    @Author Jiage
    @Date 2021-09-08
    @Function get and check data prepare to insert it into the database as a log
    '''

    def __getValueWithCheck(self, value: LogVO):
        if isAnyEmpty(
                [value, value.userName, value.serviceName, value.version,
                 value.nodes, value.port]): return None
        value.createTime = getTimeStr()
        value.id = value.createTime + "-" + value.userName + "-" + value.serviceName + "-" + value.version
        return value
