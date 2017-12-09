# coding: utf-8
from numpy import *
from slackbot.bot import respond_to

@respond_to('食べる')
def eating_func(message):
    message.reply('「朝食」「昼食」「夕食」') 
    @respond_to('朝食')
    def breakfast_func(message):
        breakfast = ["Wild Boar https://tabelog.com/tokyo/A1314/A131402/13049031/",
                     "三田おにぎり https://tabelog.com/tokyo/A1314/A131402/13191643/", 
                     "ドトールコーヒーショップ 芝公園店 https://tabelog.com/tokyo/A1314/A131402/13105053/", 
                     "ホテルヴィラフォンテーヌ田町 https://tabelog.com/tokyo/A1314/A131402/13148210/",
                     "サンマルクカフェ 田町駅前店 https://tabelog.com/tokyo/A1314/A131402/13190219/"
        ]
        breakfast = random.choice(breakfast)
        message.reply(breakfast) 
    @respond_to('昼食')
    def lunch_func(message):
        lunch = ["ラーメン二郎 三田本店 https://tabelog.com/tokyo/A1314/A131402/13006051/", 
                 "マンチズ バーガー シャック https://tabelog.com/tokyo/A1314/A131401/13121856/",
                 "イタリア食堂 TOKABO 田町センタービル店 https://tabelog.com/tokyo/A1314/A131402/13133765/",
                 "田町 大人のハンバーグ https://tabelog.com/tokyo/A1314/A131402/13091426/", 
                 "レストラン シャンクレール https://tabelog.com/tokyo/A1314/A131402/13034916/",
                 "日本料理 晴山 https://tabelog.com/tokyo/A1314/A131402/13127807/",
                 "リストランテ ラ チャウ https://tabelog.com/tokyo/A1314/A131402/13044737/",
                 "御田町 桃の木 https://tabelog.com/tokyo/A1314/A131402/13020738/"
        ]
        lunch = random.choice(lunch)
        message.reply(lunch)
    @respond_to('夕食')
    def dinner_func(message):
        dinner = ["CRAFT MEAT https://tabelog.com/tokyo/A1314/A131402/13196789/",
                  "湾岸食堂 本店 https://tabelog.com/tokyo/A1314/A131402/13013985/",
                  "ボンディ 芝浦店 https://tabelog.com/tokyo/A1314/A131402/13042261/",
                  "TOKYO CIRCUS CAFE https://tabelog.com/tokyo/A1314/A131402/13024559/",
                  "石の音 https://tabelog.com/tokyo/A1314/A131402/13120571/",
                  "うどん酒場　肉芝 https://tabelog.com/tokyo/A1314/A131402/13101737/",
                  "ホーカーズ https://tabelog.com/tokyo/A1314/A131402/13001684/",
                  "鳥一代 本店 https://tabelog.com/tokyo/A1314/A131402/13041811/",
                  "桜坊 三田店 https://tabelog.com/tokyo/A1314/A131402/13102120/",
                  "三田ばさら https://tabelog.com/tokyo/A1314/A131402/13094054/",
                  "日本酒バル ゆすら堂 https://tabelog.com/tokyo/A1314/A131402/13041811/"
        ]
        dinner = random.choice(dinner)
        message.reply(dinner)

@respond_to('遊ぶ')
def playing_func(message):
    message.reply('「映画」「スポーツ」「水族館」')
    @respond_to('映画')
    def movie_func(message):
        movie = ["T・ジョイPRINCE品川 http://tjoy-prince-shinagawa.com",
                 "TOHOシネマズ 六本木ヒルズ http://hlo.tohotheater.jp",
                 "TOHOシネマズスカラ座 http://tohotheater.jp",
                 "丸の内ピカデリー１・２ http://smt-cinema.com",
                 "キネカ大森 http://ttcg.jp"
        ]
        movie = random.choice(movie)
        message.reply(movie)
    @respond_to('スポーツ')
    def sports_func(message):
        sports = ["東京ポートボウル http://tokyoportbowl.com",
                  "品川プリンスボウリングセンター http://www.princehotels.co.jp/shinagawa/bowling/",
                  "ビリヤード&ダーツ BAGUS 銀座店 http://r.gnavi.co.jp"
        ]
        sports = random.choice(sports)
        message.reply(sports)
    @respond_to('水族館')
    def aqua_func(message):
        aquarium = ["しながわ水族館 http://aquarium.gr.jp ",
                    "アクアパーク品川 http://aqua-park.jp　"
        ]
        aquarium = random.choice(aquarium)
        message.reply(aquarium)

@respond_to('買う')
def shopping_func(message):
    message.reply('「パソコン」「洋服」')
    @respond_to('パソコン')
    def persocom_func(message):
        persocom = ["TSKUMO九十九 https://shop.tsukumo.co.jp/",
                    "マウスコンピューター http://www.mouse-jp.co.jp/"
        ]
        persocom = random.choice(persocom)
        message.reply(persocom)
    @respond_to('洋服')
    def cloth_func(message):
        cloth = ["洋服の青山 田町西口店 https://www.y-aoyama.jp/shop/?shopId=874",
                 "グランドパーク http://www.granpark.jp/about/"
        ]
        cloth = random.choice(cloth)
        message.reply(persocom)
    
@respond_to('見る')
def sightseeing_func(message):
    sightseening = ["慶應義塾大学 keio.ac.jp",
                    "東京タワー https://www.tokyotower.co.jp",
                    "芝公園 https://www.tokyo-park.or.jp/park/format/index001.html"
        ]
        sightseeing = random.choice(sightseeing)
        message.reply(sightseeing)
