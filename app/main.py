from flask import Flask, render_template, request, redirect, url_for
import requests, csv, os, json
from youtu import get_video
from waitress import serve
PATH = os.getenv("APP_PATH", "/home/repente/prog/python/projects/YouTubeLink/app")

app = Flask(__name__)


def load_csv(path):
    result = []
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            result.append(row)
    return result

def query_video(youtube_url):
    def convert_second_to_hours(second):
        import time
        return time.strftime('%H:%M:%S', time.gmtime(second))

    video = {}
    try:
        video = get_video( youtube_url )
    except json.decoder.JSONDecodeError as err:
        print("Error: ",err)
    return video




@app.context_processor
def utility_processor():

    def convert_second_to_hours(seconds):
        import time
        return time.strftime('%H:%M:%S', time.gmtime(seconds))

    return dict(convert_second_to_hours=convert_second_to_hours,)

@app.route("/", methods = ["GET"])
def index():
    data = {"title": "Скачать видео ютуб"}
    return render_template("download_link.html", data = data), 200


@app.route("/", methods = ["POST"])
def handler_post():
    data = {}
    param = request.form.to_dict()
    data['title'] = param.setdefault("title", "Скачать видео ютуб")
    data['video'] = query_video(param['link'])
    data['error'] = True if not data['video'] else False

    # if data['video']:
        # import pdb;pdb.set_trace()
    return render_template("download_link.html", data = data), 200


@app.route("/site-map", methods = ["GET"])
def site_map():
    data = {"title":"Карта сайта"}
    # data['active'] = 'active'
    data["keys"] = load_csv(PATH + "/data/keys.csv")
    return render_template("site-map.html", data = data), 200


@app.route("/<query>", methods = ["GET"])
def key_query(query):
    data = {}
    keys = load_csv(PATH + "/data/keys.csv")
    search = list(filter(lambda x : x[-1] == query, keys))
    if search:
        data = {"title":search[0][0]}
        return render_template("download_link.html", data = data), 200
    return render_template("404.html", data = data), 404



if __name__ == '__main__':
    if os.getenv("APP_PATH", False):
        serve(app, host='0.0.0.0', port=5000)
    else:
        app.run(port=5010, host='0.0.0.0', debug=True)