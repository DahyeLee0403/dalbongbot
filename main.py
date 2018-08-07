from rtmbot import RtmBot
from rtmbot.core import Plugin
import time
import secret

class HelloPlugin(Plugin):
    def process_message(self, data):
        if "달봉" in data["text"]:
            self.outputs.append([data["channel"], "왈왈"])
        if "배고파" in data["text"]:
            self.outputs.append([data["channel"],"간식 멍! "])
        if "집" in data["text"]:
            self.outputs.append([data["channel"],"같이갑멍"])
        if "야" in data["text"]:
            self.outputs.append([data["channel"], "호 멍!"])
        if "몇" in dat["text"]:
            self.outputs.append([data["channel"], print(time.asctime(time.localtime(time.time())))])
config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN ,
    "ACTIVE_PLUGINS": ['main.HelloPlugin']
}
bot = RtmBot(config)
bot.start()



print('나도 달봉이 보고싶다구요!! 보여주세여(꾸벅)')
print("달봉이 사랑해~")
