
import common.ConfigUtils as cf

'''
@function parse the service's config
@Author Jiage
@Date 2022-02-20
'''


def parseSampleResult(command, extendCommand="") -> str:
    conf = cf.getConfig()
    c = conf.get(command)
    sp = conf.get(cf.CUR_SSHPASS)
    # running local shell if sp is empty
    if len(sp) == 0:
        print("{0}".format(c))
        return c
    r = sp + " '" + c + extendCommand + "'"
    print("{0}".format(r))
    return r
