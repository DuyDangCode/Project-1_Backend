from flask import request, Flask, render_template, jsonify, send_from_directory
from predict_realtime import predictRealtime
import config
import os


app = Flask(__name__)

ALLOWED_EXTENSIONS = ['avi', 'mp4']


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/v1/videos', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return 'No video file found'
    video = request.files['video']
    if video.filename == '':
        return 'No video selected'
    if video and allowed_file(video.filename):

        # ext = video.filename.split(".")[-1]
        # filename = f"download_video.{ext}"

        filename = video.filename
        video.save('data/testing_data/video/' + filename)
        print(filename)
        result, t = predictRealtime(filename)
        # predictString = predictRealtime(video.filename)

        # clip = moviepy.VideoFileClip('data/testing_data/video/' + video.filename)
        # clip.write_videofile('data/saved_video_mp4/' + video.filename.replace(".avi", ".mp4"))
        # clip.close()
        # return send_from_directory('data/saved_video_mp4/', video.filename.replace(".avi", ".mp4"))
        return jsonify({"result": result, "time": t})
    return 'Invalid video file'


@app.route("/", methods=["GET"])
def home():
    return jsonify({"title": "Home"})
    # return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
