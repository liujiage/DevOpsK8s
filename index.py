from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit
import logging

from services.AutoScaleService import AutoScaleService
from view.QueryView import QueryView as dv
from view.AutoScaleView import AutoScaleView
from view.AuthenticationView import AuthenticationView as auth
from vo.AutoScaleSettingVO import AutoScaleSettingVO

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, logger=True, engineio_logger=True)

'''
@Function login system
@Author Jiage
@Date 2022-02-18
'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('userid'):
        session.pop('userid')
    return render_template('login.html')


'''
@Function the first page
@Author Jiage
@Date 2022-02-18
'''


@app.route("/")
def index():
    return render_template('index.html', user=session['userid'])


'''
@Function get the cluster information 
@Author Jiage
@Date 2022-02-18
'''


@app.route("/cluster")
def cluster():
    return render_template('cluster.html')


'''
@Function get the deployment information
@Author Jiage
@Date 2022-02-18
'''


@app.route("/deploy")
def deploy():
    return render_template('deploy.html')


'''
@Function get the node information
@Author Jiage
@Date 2022-02-20
'''


@app.route("/nodes")
def nodes():
    return render_template('nodes.html')


'''
@Function get the services information
@Author Jiage
@Date 2022-02-23
'''


@app.route("/services")
def services():
    return render_template('services.html')


'''
@Function get the pod information
@Author Jiage
@Date 2022-02-23
'''


@app.route("/pods")
def pods():
    return render_template('pods.html')


'''
@Function get the node and pod status currently cpu and memory
@Author Jiage
@Date 2022-02-23
'''


@app.route("/status")
def status():
    return render_template('status.html')


'''
@Function watch currently hosts cluster usage. 
@Author Jiage
@Date 2022-02-20
'''


@app.route("/auto_scale")
def auto_scale():
    asv = AutoScaleView()
    return render_template('auto_scale.html', setting=asv.getSetting())


@app.route("/auto_scale_setting", methods=['GET', 'POST'])
def auto_scale_setting():
    asv = AutoScaleView()
    asv.saveSetting(AutoScaleSettingVO(int(request.form["miniSize"]),
                                       int(request.form["maxSize"]),
                                       int(request.form["memExc"]),
                                       request.form["deployName"]))
    return render_template('auto_scale.html', setting=asv.getSetting())


'''
@Function received requests from the client 
@Author Jiage
@Date 2022-02-20
@Data
   Json {event:{connect|query_cluster|...},data: {type of string}}
@Param event 
   connect, the client connect to service at the first time.
   query_cluster, query cluster information from K8s
'''


@socketio.on('request')
def socketRequest(msg):
    dv.socketRequest(app, msg)


@socketio.on('connect')
def socketConnect(msg):
    emit('response', {'event': 'connect', 'data': 'Connected'})


'''
@Function Intercept request, authentication. 
@Author Jiage
@Date 2022-02-20
'''
@app.before_request
def authentication():
    return auth.auth(app)

@app.before_first_request
def autoScaleBackendThread():
    # start backend thread auto scale
    thread = AutoScaleService()
    # thread.setDaemon(True)
    thread.start()


if __name__ == "__main__":
    socketio.run(app)
