from flask import Flask, redirect, url_for, render_template, Response, request
from camera import Video
app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/success/<name>')
# def success(name):
#    return 'welcome1 %s' % name

# @app.route('/success2/<name>')
# def success2(name):
#    return 'welcome sot %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success2',name = user))

if __name__ == '__main__':
   app.run(debug = True)