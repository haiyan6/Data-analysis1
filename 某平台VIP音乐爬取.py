import re
import requests

# 爬虫1： 通过歌曲名构造出一个链接 请求它  得到3个值
song_name = input('请输入歌曲名:')
url1 = f'https://c.musicapp.migu.cn/v1.0/content/search_all.do?text={song_name}&pageNo=1&pageSize=20&isCopyright=1&sort=1&searchSwitch=%7B%22song%22%3A1%2C%22album%22%3A0%2C%22singer%22%3A0%2C%22tagSong%22%3A1%2C%22mvSong%22%3A0%2C%22bestShow%22%3A1%7D'
res1 = requests.get(url1)
copyrightId = re.findall('"copyrightId":"(.*?)"', res1.text)[0]
contentId = re.findall('"contentId":"(.*?)"', res1.text)[0]
albumId = re.findall('"albums":\[{"id":"(.*?)"', res1.text)[0]

# 爬虫2：通过爬虫1得到的3个值 构造出一个新的链接 请求它  得到音乐的链接
url2 = f'https://c.musicapp.migu.cn/MIGUM3.0/strategy/listen-url/v2.3?copyrightId={copyrightId}&contentId={contentId}&resourceType=2&albumId={albumId}&netType=01&toneFlag=PQ'
headers = {'channel': '0140210'}
res2 = requests.get(url2, headers=headers)
song_url = re.findall('"url":"(.*?)",', res2.text)[0]

# 爬虫3：请求爬虫2爬到的歌曲链接 把个去保存下来！
res3 = requests.get(song_url)
open(f'{song_name}.mp3', 'wb').write(res3.content)















