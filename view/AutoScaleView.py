from services.dao.AutoScaleSettingDao import AutoScaleSettingDao
from vo.AutoScaleSettingVO import AutoScaleSettingVO


class AutoScaleView:

    def __init__(self):
        self.assDao = AutoScaleSettingDao()

    def getSetting(self) -> AutoScaleSettingVO:
        return self.assDao.query()

    def saveSetting(self, setting = AutoScaleSettingVO()):
        return self.assDao.updateOrInsert(setting)
