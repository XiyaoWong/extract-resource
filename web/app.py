import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, render_template, flash

import config
from utils import main

app = Flask(__name__)
app.config.from_object(config.Config)


@app.route('/')
def index():
    author = ''
    video_url = ''
    video_name = ''
    music_url = ''
    music_name = ''
    image_url = ''
    params = request.args.to_dict()
    url = params.get('url')
    # print(url)
    if url and ('http' in url):
        data = main.get(url)
        print(data)
        author = data.get('author')
        video_url = data.get('video_url')
        video_name = data.get('video_name')
        music_name = data.get('music_name')
        music_url = data.get('music_url')
        image_url = data.get('image_url')
        flash('如果你输入的链接正确的话-成功提取的内容都会显示，否则失败。如果是抖音的话，就别试了，失败很正常')
    else:
        flash('提取失败，请检查链接是否正确，多次尝试没用就别试了~')
    return render_template('index.html',
                            author=author,
                            video_url=video_url,
                            video_name=video_name,
                            music_url=music_url,
                            music_name=music_name,
                            image_url=image_url)


if __name__ == "__main__":
    # print(app.url_map)
    app.run()