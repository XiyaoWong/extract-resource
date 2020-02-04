import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import bilibili_cover, changya, pipigaoxiao, kuwo, kugou, quanminkge, weishi, douyin, helper


def get(url=''):

    # 根据链接判断是哪个平台
    # url = helper.get_origin_location(url)
    if 'douyin' in url:
        t = 'douyin'
    elif 'bili' in url or 'av' in url:
        t = 'bilibili_cover'
    elif 'kugou' in url:
        t = 'kugou'
    elif 'kuwo' in url:
        t = 'kuwo'
    elif 'weishi' in url:
        t = 'weishi'
    elif 'kg' in url and 'qq' in url:
        t = 'quanminkge'
    elif 'changya' in url:
        t = 'changya'
    elif 'ipp' in url:
        t = 'pipigaoxiao'
    else:
        t = ''
# ------------------------------
    # 整合返回数据
    author = ''
    video_url = ''
    video_name =  ''
    music_url = ''
    music_name = ''
    image_url = ''

    if t and url:
        if t == 'bilibili_cover':
            data = bilibili_cover.get(url)
            image_url = data.get('cover_url')
        elif t == 'changya':
            data = changya.get(url)
            author = data.get('author')
            music_name = data.get('audio_name')
            music_url = data.get('audio_url')
        elif t == 'pipigaoxiao':
            data = pipigaoxiao.get(url)
            video_url = data.get('play_url')
        elif t == 'kuwo':
            url = helper.get_origin_location(url)
            data = kuwo.get(url)
            author = data.get('author')
            music_name = data.get('song_name')
            music_url = data.get('play_url')
        elif t == 'kugou':
            data = kugou.get(url)
            author = data.get('author_name')
            music_name = data.get('song_name')
            music_url = data.get('play_url')
            image_url = data.get('img')
        elif t == 'weishi':
            url = helper.get_origin_location(url)
            data = weishi.get(url)
            video_name = data.get('title')
            video_url = data.get('play_url')
        elif t == 'quanminkge':
            data = quanminkge.get(url)
            author = data.get('singer')
            music_name = data.get('song_name')
            music_url = data.get('play_url')
            video_url = data.get('play_video')
        elif t == 'douyin':
            data = douyin.get(url)
            video_name = data.get('video_name')
            video_url = data.get('video_url')

    return {
        'author' : author,
        'video_url' : video_url,
        'video_name' :  video_name,
        'music_url' : music_url,
        'music_name' : music_name,
        'image_url' : image_url,
    }


if __name__ == "__main__":
    a = get(url='http://share.ippzone.com/pp/post/212467897747')
    print(a)