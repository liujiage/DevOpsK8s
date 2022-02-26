from abc import ABC

from common.StrUtils import isEmpty, isAnyEmpty
from common.TimeUtils import getTimeStr
from services.dao.SqliteDao import SqliteDao
from vo.AutoScaleSettingVO import AutoScaleSettingVO
from vo.LogVO import LogVO

'''
@Author Jiage
@Date 2022-02-09
@Function query auto scale and update scale
'''


class AutoScaleSettingDao(SqliteDao):
    '''
    @Author Jiage
    @Date 2022-02-08
    @Function query deploys log
    '''

    def query(self, value=None) -> AutoScaleSettingVO:
        records = self.fetch(
            'select mini_size,max_size,mem_exc,deploy_name from auto_scale_setting')
        ass = AutoScaleSettingVO()
        if isEmpty(records): return ass
        record = records[0]
        ass.miniSize = record[0]
        ass.maxSize = record[1]
        ass.memExc = record[2]
        ass.deployName = record[3]
        return ass

    '''
    @Author Jiage
    @Date 2022-02-08
    @Function Save data into the database as a log
    '''

    def updateOrInsert(self, value: AutoScaleSettingVO) -> int:
        print("'%d' - ,'%d' - ,'%d', - '%s')" % (value.miniSize, value.maxSize, value.memExc, value.deployName))
        # first delete data
        self.execute("delete from auto_scale_setting")
        self.execute(
            "insert into auto_scale_setting(mini_size,max_size,mem_exc,deploy_name) "
            "values('%d','%d','%d', '%s')" % (value.miniSize, value.maxSize, value.memExc, value.deployName))
        return 1


