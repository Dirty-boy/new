# coding=utf-8
import sys
import json

IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode

API_KEY = '8BILFNxjfXdyGi9bZH6PIXpn'
SECRET_KEY = 'UpSkNYGK1ZeF8jcO7Rxayogz8bSKMl73'


AUE = 3
FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
FORMAT = FORMATS[AUE]

CUID = "123456PYTHON"

TTS_URL = 'http://tsn.baidu.com/text2audio'


class DemoError(Exception):
    pass


"""  TOKEN start """

TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选


def fetch_token():
#     print("fetch token begin")
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()
    if (IS_PY3):
        result_str = result_str.decode()

#     print(result_str)
    result = json.loads(result_str)
#     print(result)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not SCOPE in result['scope'].split(' '):
            raise DemoError('scope is not correct')
#         print('SUCCESS WITH TOKEN: %s ; EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
        return result['access_token']
    else:
        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


def change(text: str, title, file='音频'):
    import os
    if not os.path.exists(file):
        os.mkdir(file)
    TEXT = text

    # 发音人选择, 基础音库：0为度小美，1为度小宇，3为度逍遥，4为度丫丫，
    # 精品音库：5为度小娇，103为度米朵，106为度博文，110为度小童，111为度小萌，默认为度小美
    PER = 111
    # 语速，取值0-15，默认为5中语速
    SPD = 4
    # 音调，取值0-15，默认为5中语调
    PIT = 5
    # 音量，取值0-9，默认为5中音量
    VOL = 5
    # 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
    AUE = 3

    token = fetch_token()
    tex = quote_plus(TEXT)  # 此处TEXT需要两次urlencode
    #     print(tex)
    params = {'tok': token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL, 'aue': AUE, 'cuid': CUID,
              'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数

    data = urlencode(params)
    #     print('test on Web Browser' + TTS_URL + '?' + data)

    req = Request(TTS_URL, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()

        headers = dict((name.lower(), value) for name, value in f.headers.items())

        has_error = ('content-type' not in headers.keys() or headers['content-type'].find('audio/') < 0)
    except  URLError as err:
        print('asr http response http code : ' + str(err.code))
        result_str = err.read()
        has_error = True

    save_file = "error.txt" if has_error else f'{title}.' + FORMAT
    file = file + '/'
    with open('./' + file + save_file, 'wb') as of:
        of.write(result_str)

    if has_error:
        if (IS_PY3):
            result_str = str(result_str, 'utf-8')
    #         print("tts api  error:" + result_str)

    print("result saved as :" + save_file)

strd = '''
    首先必须要声明的一点就是逻辑回归是一个受工业商业热爱，使用广泛的模型。
        1.逻辑回归对线性关系（特征与标签之间的线性关系极强的数据）的拟合效果好到丧心病狂，比如金融领域中的信用卡欺诈，评分卡制作，电商中的营销预测等等相关的数据，都是逻辑回归的强项。相对，逻辑回归在非线性数据中的效果有时候比瞎猜还不如，如果你事先知道你的数据之间的练习是非线性的，千万一定不要使用逻辑回归！！！
        2.逻辑回归计算快:对于线性数据，逻辑回归的拟合和计算都非常快，计算效率优于SVM和随机森林，亲测表示在大型数据上尤其能看出区别。
        3.逻辑回归返回的分类结果不是固定的0，1，而是以小数形式呈现的类概率数字:我们因此可以把逻辑回归返回的结果当成连续型数据来利用。比如在评分卡制作时，我们不仅需要判断客户是否会违约，还需要给出确定的”信用分“，而这个信用分的计算就需要使用类概率计算出的对数几率（概率）， 。
    总结：
        由此，我们已经了解了逻辑回归的本质，它是一个返回对数几率的在线性数据上表现优异的分类器，它主要被应用在金融领域。注意，虽然我们熟悉的逻辑回归通常被用于处理二分类问题，但逻辑回归也可以做多分类。


'''
change(strd,'音频')