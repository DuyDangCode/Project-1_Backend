from flask import request, Flask, render_template, jsonify
from predict_realtime import predictRealtime
import config
import os

app = Flask(__name__)

ALLOWED_EXTENSIONS = ['avi']
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.after_request
# def set_headers(response):
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Headers"] = "*"
#     response.headers["Access-Control-Allow-Methods"] = "*"
#     return response

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return 'No video file found'
    video = request.files['video']
    if video.filename == '':
        return 'No video selected'
    if video and allowed_file(video.filename):
        video.save('data/testing_data/video/' + video.filename)
        print(video.filename)
        return jsonify(predictRealtime(video.filename))
    return 'Invalid video file'

@app.route('/uploadvideo', methods=['POST'])
def upload2():
    # video = request.files['video']
    # video.save('data/testing_data/video/' + video.filename) 
    #return video.filename
    #return jsonify(predictRealtime(video.filename))


   
    if 'file' not in request.files:
        return 'No video file found'
        
    video = request.files['file']
    if video.filename == '':
        return 'No video selected'
    if video and allowed_file(video.filename):
        video.save('data/testing_data/video/' + video.filename)
        print(video.filename)
        return jsonify(predictRealtime(video.filename))
    return 'Invalid video file'
        
   



@app.route("/", methods=["GET"])
def home():
    return jsonify({"title":"Home"})
    #return render_template("index.html")


@app.route("/predict", methods=[ "get"])
def predict():
    return jsonify(predictRealtime())
    
    

if __name__ == "__main__":
    app.run(debug=True)