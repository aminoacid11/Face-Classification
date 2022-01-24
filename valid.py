from operator import index
import requests, lxml, re, json
from bs4 import BeautifulSoup
import os

owd = os.getcwd()
if os.path.isdir('images') is False:
    os.makedirs('images')
if os.path.isdir('images/valid') is False:
    os.makedirs('images/valid')
    os.makedirs('images/valid/dog')
    os.makedirs('images/valid/cat')
    os.makedirs('images/valid/rabbit')
    os.makedirs('images/valid/horse')
    os.makedirs('images/valid/fox')
    os.makedirs('images/valid/squirrel')
    os.makedirs('images/valid/bear')
    os.makedirs('images/valid/wolf')
    os.makedirs('images/valid/monkey')
    os.makedirs('images/valid/turtle')
    os.makedirs('images/valid/pig')
    os.makedirs('images/valid/deer')
    os.makedirs('images/valid/frog')

val_face = {'강아지상':['아이즈원권은비','오마이걸효정','워너원박지훈','박하나','선예'],\
            '고양이상':['시우민','황민현','지코'],\
            '토끼상':['워너원박지훈','아이콘바비','nct도영','권은비','강지영','강예서','박소담','배두나','산다라박'],\
            '말상':['세븐틴도겸','exo레이','박정민','nct헨드리'],\
            '여우상':['인피니트김성규','뉴이스트민현','아스트로문빈','러블리즈지수','슈퍼주니어예성','세븐틴원우'],\
            '다람쥐상':['오마이걸승희','비투비이민혁','더보이즈큐','차선우'],\
            "곰상":['b1a4신우','비투비임현식','nct천러','엑소카이','nct해찬'],\
            "늑대상":['설현','수루이치','올리비아혜','더보이즈주연'],\
            "원숭이상":['이재명','정은지','신하균'],\
            "거북이상":['박규희','nct유타','세븐틴정한','공유','김소혜','위키미키리나'],
            "돼지상":['성훈','화사','김신영','한혜연','장성규','허가윤'],\
            "사슴상":['위너김진우','nct성찬','nct윈윈','nct재민'],\
            "개구리상":['뽀구미','아이즈원김민주']}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

def valid_webscrape1():
    dog_cnt,cat_cnt,rabbit_cnt,horse_cnt,fox_cnt,squirrel_cnt,bear_cnt,wolf_cnt,monkey_cnt,turtle_cnt,pig_cnt,deer_cnt,frog_cnt = 0,0,0,0,0,0,0,0,0,0,0,0,0
    for idx1,names in enumerate(val_face.values()):
        for name_ind,name in enumerate(names):
            print("2nd loop",name,"searching")
            url1 = "https://search.aol.com/aol/image;_ylt=Awr9Hr57TuJh5GkAKeNjCWVH?q={}+얼굴&ei=UTF-8&s_it=sb_top&v_t=comsearch&imgty=photo&fr2=p%3As%2Cv%3Ai".format(name)
            res1 = requests.get(url1, headers=headers)
            res1.raise_for_status()
            soup1 = BeautifulSoup(res1.text, "lxml")
            face_images = soup1.find_all("a", attrs={"class":"img"})
            if idx1 == 0:
                os.chdir('images/valid/dog')
                animal = '강아지상'
                if name_ind > 0:
                    dog_cnt += temp_cnt
                cnt = dog_cnt
            elif idx1 == 1:
                os.chdir('images/valid/cat')
                animal = '고양이상'
                if name_ind > 0:
                    cat_cnt += temp_cnt
                cnt = cat_cnt
            elif idx1 == 2:
                os.chdir('images/valid/rabbit')
                animal = '토끼상'
                if name_ind > 0:
                    rabbit_cnt += temp_cnt
                cnt = rabbit_cnt
            elif idx1 == 3:
                os.chdir('images/valid/horse')
                animal = '말상'
                if name_ind > 0:
                    horse_cnt += temp_cnt
                cnt = horse_cnt
            elif idx1 == 4:
                os.chdir('images/valid/fox')
                animal = '여우상'
                if name_ind > 0:
                    fox_cnt += temp_cnt
                cnt = fox_cnt
            elif idx1 == 5:
                os.chdir('images/valid/squirrel')
                animal = '다람쥐상'
                if name_ind > 0:
                    squirrel_cnt += temp_cnt
                cnt = squirrel_cnt
            elif idx1 == 6:
                os.chdir('images/valid/bear')
                animal = '곰상'
                if name_ind > 0:
                    bear_cnt += temp_cnt
                cnt = bear_cnt
            elif idx1 == 7:
                os.chdir('images/valid/wolf')
                animal = '늑대상'
                if name_ind > 0:
                    wolf_cnt += temp_cnt
                cnt = wolf_cnt
            elif idx1 == 8:
                os.chdir('images/valid/monkey')
                animal = '원숭이상'
                if name_ind > 0:
                    monkey_cnt += temp_cnt
                cnt = monkey_cnt
            elif idx1 == 9:
                os.chdir('images/valid/turtle')
                animal = '거북이상'
                if name_ind > 0:
                    turtle_cnt += temp_cnt
                cnt = turtle_cnt
            elif idx1 == 10:
                os.chdir('images/valid/pig')
                animal = '돼지상'
                if name_ind > 0:
                    pig_cnt += temp_cnt
                cnt = pig_cnt
            elif idx1 == 11:
                os.chdir('images/valid/deer')
                animal = '사슴상'
                if name_ind > 0:
                    deer_cnt += temp_cnt
                cnt = deer_cnt
            elif idx1 == 12:
                os.chdir('images/valid/frog')
                animal = '개구리상'
                if name_ind > 0:
                    frog_cnt += temp_cnt
                cnt = frog_cnt
            temp_cnt = 0
            print("length= ",len(face_images))
            for face_image in face_images:
                temp_cnt += 1
                cnt += 1
                face_image_url = face_image["href"]
                face_image_res = requests.get(face_image_url)
                try:
                    with open("{}{}.jpg".format(animal,cnt), "wb") as f:
                        f.write(face_image_res.content)
                except face_image_res.raise_for_status():
                    continue
            os.chdir(owd)

# valid_webscrape1()