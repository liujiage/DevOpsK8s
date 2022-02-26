import os
import common.ConfigUtils as cf
from services.ParseService import parseSampleResult
from flask_socketio import SocketIO, emit
import subprocess

from services.dao.LogDao import LogDao


class QueryView:
    logDao = LogDao()

    '''
    @Function call the api from kubectl cluster
    @Author Jiage
    @Date 2022-02-20
    '''

    @staticmethod
    def socketRequest(app, msg):
        event = msg['event']
        data = msg['data']
        cmd, response_event = None, None
        if event == 'connect':
            app.logger.info('the client connecting and send message is ' + data)
        elif event == 'query_cluster':
            app.logger.info('the client sending query_cluster event, the message is ' + data)
            cmd = parseSampleResult(command=cf.CUR_CLUSTER_SERVICE)
            response_event = "log-cluster"
        elif event == 'query_nodes':
            app.logger.info('the client sending query_nodes event, the message is ' + data)
            cmd = parseSampleResult(command=cf.CUR_NODES_SERVICE)
            response_event = "log-nodes"
        elif event == 'query_deploy':
            app.logger.info('the client sending query_deploy event, the message is ' + data)
            cmd = parseSampleResult(command=cf.CUR_DEPLOY_SERVICE)
            response_event = "log-deploy"
        elif event == 'query_services':
            app.logger.info('the client sending query_services event, the message is ' + data)
            cmd = parseSampleResult(command=cf.CUR_SERVICES_SERVICE)
            response_event = "log-services"
        elif event == 'query_pods':
            app.logger.info('the client sending query_pods event, the message is ' + data)
            cmd = parseSampleResult(command=cf.CUR_PODS_SERVICE)
            response_event = "log-pods"
        elif event == 'query_status':
            app.logger.info('the client sending query_status event, the message is ' + data)
            cmd = parseSampleResult(command=cf.CUR_STATUS_SERVICE)
            response_event = "log-status"
        else:
            app.logger.error('Error, received a wrong request!')
        if cmd is not None:
            with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=50, universal_newlines=True) as p:
                for line in iter(p.stdout.readline, ""):
                    print(line)
                    emit('response', {'event': response_event, 'data':
                        line.replace("[0;32m", "").replace("[0;33m", "").replace("[0m", "")})
