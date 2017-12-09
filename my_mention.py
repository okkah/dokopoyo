# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from numpy import *

@respond_to('食べる')
def eating_func(message):
    message.reply('「朝食」「昼食」「夕食」の中から選択') # メンション
    @respond_to('朝食')
    def breakfast_func(message):
        breakfast = ["Wild Boar https://tabelog.com/tokyo/A1314/A131402/13049031/", "三田おにぎり https://tabelog.com/tokyo/A1314/A131402/13191643/", "ドトールコーヒーショップ 芝公園店 https://tabelog.com/tokyo/A1314/A131402/13105053/", "ホテルヴィラフォンテーヌ田町 https://tabelog.com/tokyo/A1314/A131402/13148210/", "サンマルクカフェ 田町駅前店 https://tabelog.com/tokyo/A1314/A131402/13190219/"]
        breakfast = random.choice(breakfast)
        message.reply(breakfast) # メンション
    @respond_to('昼食')
    def lunch_func(message):
        lunch = ["ラーメン二郎 三田本店 https://tabelog.com/tokyo/A1314/A131402/13006051/", "マンチズ バーガー シャック https://tabelog.com/tokyo/A1314/A131401/13121856/", "イタリア食堂 TOKABO 田町センタービル店 https://tabelog.com/tokyo/A1314/A131402/13133765/", "田町 大人のハンバーグ https://tabelog.com/tokyo/A1314/A131402/13091426/", "レストラン シャンクレール https://tabelog.com/tokyo/A1314/A131402/13034916/", "日本料理 晴山 https://tabelog.com/tokyo/A1314/A131402/13127807/", "リストランテ ラ チャウ https://tabelog.com/tokyo/A1314/A131402/13044737/", "御田町 桃の木 https://tabelog.com/tokyo/A1314/A131402/13020738/"]
        lunch = random.choice(lunch)
        message.reply(lunch) # メンション
    @respond_to('夕食')
    def dinner_func(message):
        dinner = ["CRAFT MEAT https://tabelog.com/tokyo/A1314/A131402/13196789/", "湾岸食堂 本店 https://tabelog.com/tokyo/A1314/A131402/13013985/", "ボンディ 芝浦店 https://tabelog.com/tokyo/A1314/A131402/13042261/", "TOKYO CIRCUS CAFE https://tabelog.com/tokyo/A1314/A131402/13024559/", "石の音 https://tabelog.com/tokyo/A1314/A131402/13120571/", "うどん酒場　肉芝 https://tabelog.com/tokyo/A1314/A131402/13101737/", "ホーカーズ https://tabelog.com/tokyo/A1314/A131402/13001684/", "鳥一代 本店 https://tabelog.com/tokyo/A1314/A131402/13041811/", "桜坊 三田店 https://tabelog.com/tokyo/A1314/A131402/13102120/", "三田ばさら https://tabelog.com/tokyo/A1314/A131402/13094054/", "日本酒バル ゆすら堂 https://tabelog.com/tokyo/A1314/A131402/13041811/"]
        dinner = random.choice(dinner)
        message.reply(dinner) # メンション
