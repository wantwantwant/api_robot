import optparse
import time
import apiutil  # 这里我上端代码独立生成一个文件“apiutil.py"，所以要导入一下
import json

app_key ="62RBGB9EyzFZ7sIZ"
app_id = 2110540682
questionS = '在吗？'


def anso(questionS):
    str_question = questionS
    session = 10000
    ai_obj = apiutil.AiPlat(app_id, app_key)

    rsp = ai_obj.getNlpTextChat(session, str_question)
    if rsp['ret'] == 0:
        ask = (rsp['data'])['answer']
        return (ask)
    else:
        print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))


if __name__ == '__main__':
    while True:
        questionS = input(f"Rose:")
        print(f"Jack：{anso(questionS)}")

anso(questionS)
