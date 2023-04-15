from importlib import reload
import openai
import requests

import logging
from datetime import datetime


logging.basicConfig(level=logging.DEBUG)
openai.organization = "org-RGPsZEgYBS5gNP6gO5p6r2QY"
openai.api_key = "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"


def analyze_birthday(birth1, gender1, birth2, gender2, question):
    lang_type = "ko"

    # birth1 = "1967-1-26 22:21"
    lat1 = 35.8714354
    lng1 = 128.601445
    # gender1 = "man"
    knowTime1 = True

    resp = requests.get(
    f"https://rur5ab9i95.execute-api.ap-northeast-2.amazonaws.com/dev/basic_characters_each?birth={birth1}&lat={lat1}&lng={lng1}&gender={gender1}&knowTime={knowTime1}&lang_type={lang_type}"
    )
    parsed1 = resp.json()
    print(f"parsed1:{parsed1}")
    print()
    my_char1 = parsed1["일반_기본_성격"]["대표적_기질"]["나의대표적기질"]
    my_char2 = parsed1["일반_기본_성격"]["능동성과_피동성"]
    my_char3 = parsed1["일반_기본_성격"]["삶의방식과_가치관"]["대표격_1"]
    my_char4 = parsed1["일반_기본_성격"]["삶의방식과_가치관"]["대표격_2"]
    my_char5 = parsed1["일반_기본_성격"]["삶의방식과_가치관"]["대표격_3"]
    my_char = my_char1 + my_char2 + my_char3 + my_char4 + my_char5
    # 생일과 성별을 분석하는 코드 작성하기
    # ...

    # birth2 = "1966-8-2 12:21"
    lat2 = 35.8714354
    lng2 = 128.601445
    # gender2 = "woman"
    knowTime2 = True


    resp2 = requests.get(
    f"https://rur5ab9i95.execute-api.ap-northeast-2.amazonaws.com/dev/basic_characters_each?birth={birth2}&lat={lat2}&lng={lng2}&gender={gender2}&knowTime={knowTime2}&lang_type={lang_type}"
    )
    parsed2 = resp2.json()

    partner_char1 = parsed2["일반_기본_성격"]["대표적_기질"]["나의대표적기질"]
    partner_char2 = parsed2["일반_기본_성격"]["능동성과_피동성"]
    partner_char3 = parsed2["일반_기본_성격"]["삶의방식과_가치관"]["대표격_1"]
    partner_char4 = parsed2["일반_기본_성격"]["삶의방식과_가치관"]["대표격_2"]
    partner_char5 = parsed2["일반_기본_성격"]["삶의방식과_가치관"]["대표격_3"]

    partner_char = partner_char1 + partner_char2 + partner_char3 + partner_char4 + partner_char5

    # parsed2["일반_기본_성격"] #["대표적_기질"]["나의대표적기질"]
    print(partner_char)

    sdf = ""

    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    return gen(question, my_char, partner_char)


def gen(question, my_char, partner_char):
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
       messages=[
            {"role": "system", "content": f"나의 성격은 {my_char}. 상대방 성격은 {partner_char}."},
            {"role": "user", "content": f"{question}"},
#             {"role": "assistant", "content": f"{sdf}"},
#             {"role": "user", "content": user_message}
        ]
    )
    print(f"result:{result}")
    print(result['choices'][0]['message']['content'].encode('utf-8').decode('utf-8'))

    return  {
        "my_char": my_char,
       "partner_char": partner_char,
        "result": result['choices'][0]['message']['content'].encode('utf-8').decode('utf-8'),
    }


