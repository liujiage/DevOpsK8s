import unittest
import configparser
import common.ConfigUtils as cf

class MyTestCase(unittest.TestCase):
    def test_something(self):
        config = configparser.RawConfigParser()
        config.read('../resources/config.properties')
        config_dict = dict(config.items("SHELL_CONFIG"))
        print(config_dict)
        print(config_dict.get('pre.deploy.service'))

    def test_config(self):
        confs = cf.getConfig()
        dds = confs.get(cf.CUR_DEPLOY_SERVICE)
        dcf = confs.get(cf.CUR_SERVICE_CONFIG_FOLDER)
        dps = confs.get(cf.CUR_SSHPASS)
        print("ddf: {0}, dcf: {1}, dps: {2} ".format(dds, dcf, dps))


if __name__ == '__main__':
    unittest.main()
