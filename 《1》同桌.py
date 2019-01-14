import random
import string
import time
import hashlib
import urllib.parse
import urllib.request
import json
import requests

appid = 2110540682
appkey = "62RBGB9EyzFZ7sIZ"
base_url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"

def smart_chat(question):
    params = {
        "app_id": 2110540682 ,
        "session": "1000",
        "question": question,
        "time_stamp": time.time(),
        # "time_stamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
        "nonce_str": "".join(random.sample(string.ascii_letters + string.digits, 10))
    }
    params["sign"] = get_sign(params, appkey)
    return do_http_post(base_url, params)

def get_sign(params, appkey):
    # True 降序 False升序默认升序
    keys = sorted(params, reverse=False)
    # print(sorted(params.items(), key=operator.itemgetter(0), reverse=False))
    str_ = ""
    for key in keys:
        str_ += (key + "=" + urllib.parse.quote(str(params.get(key))) + "&")
    # print(str_)
    str_ += ("app_key" + "=" + appkey)
    # 构造MD5
    md = hashlib.md5()
    md.update(str_.encode("utf-8"))
    # print(md.hexdigest())
    sign = md.hexdigest().upper()
    return sign

def do_http_post(url, params):
    data = urllib.parse.urlencode(params).encode("utf-8")
    result_obj = urllib.request.urlopen(url, data)
    # r = requests.post(url, data=params)
    # print(r.json())
    return json.loads(result_obj.read().decode("utf-8"))["data"]["answer"]

def test_run():
    while True:
        question = input(f"小可爱:")
        print(f"马二哈:{smart_chat(question)}")

test_run()



