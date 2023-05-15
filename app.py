from flask import request, Flask, render_template, jsonify, send_from_directory
from predict_realtime import predictRealtime
import config
import os
import moviepy.editor as moviepy

app = Flask(__name__)

ALLOWED_EXTENSIONS = ['avi', 'mp4']

predictString = "Nothing"
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.after_request
# def set_headers(response):
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Headers"] = "*"
#     response.headers["Access-Control-Allow-Methods"] = "*"
#     return response

# @app.route('/uploadvideo', methods=['POST'])
# def sentPredictString():
#     if 'video' not in request.files:
#         return 'No video file found'
#     video = request.files['video']
#     if video.filename == '':
#         return 'No video selected'
#     if video and allowed_file(video.filename):
#         video.save('data/testing_data/video/' + video.filename)
#         print(video.filename)
#         return jsonify(predictRealtime(video.filename))
#     return 'Invalid video file'

@app.route('/uploadvideo', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return 'No video file found'
    video = request.files['video']
    if video.filename == '':
        return 'No video selected'
    if video and allowed_file(video.filename):
        video.save('data/testing_data/video/' + video.filename)
        print(video.filename)
        # predictString = predictRealtime(video.filename)
        
        # clip = moviepy.VideoFileClip('data/testing_data/video/' + video.filename)
        # clip.write_videofile('data/saved_video_mp4/' + video.filename.replace(".avi", ".mp4"))
        # clip.close()
        # return send_from_directory('data/saved_video_mp4/', video.filename.replace(".avi", ".mp4"))
        return predictRealtime(video.filename)
    return 'Invalid video file'



        


@app.route("/", methods=["GET"])
def home():
    return jsonify({"title":"Home"})
    #return render_template("index.html")


@app.route("/predict", methods=[ "get"])
def predict():
    return predictString
    
    

if __name__ == "__main__":
    app.run(debug=True)