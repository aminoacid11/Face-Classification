from operator import index
import requests, lxml, re, json
from bs4 import BeautifulSoup
import os

owd = os.getcwd()
if os.path.isdir('images') is False:
    os.makedirs('images')
if os.path.isdir('images/dog') is False:
    os.makedirs('images/dog')
    os.makedirs('images/cat')
    os.makedirs('images/rabbit')
    os.makedirs('images/horse')
    os.makedirs('images/fox')
    os.makedirs('images/squirrel')
    os.makedirs('images/bear')
    os.makedirs('images/wolf')
    os.makedirs('images/monkey')
    os.makedirs('images/turtle')
    os.makedirs('images/pig')
    os.makedirs('images/deer')
    os.makedirs('images/frog')
an_face = {'강아지상':["박보검","강다니엘","백현","이종석","손예진","한효주","수지","아이유"],\
            '고양이상':["한예슬","현아","예지","조인성","하니","한소희","고아라","크리스탈"],\
            '토끼상':["나연","려욱","아이린","유나","이나은","정국","지수","한지민","도영","에스파윈터","태민"],\
            '말상':["강타","김기수","보아","제이홉","태연","이광수","소지섭","이병헌"],\
            '여우상':["서인국","가인","경리","유인나","육성재","쯔위","채령","샤이니키"],\
            '다람쥐상':["김성경","사나","문별","조보아","강미나","로꼬","레이나"],\
            "곰상":["마동석","셔누","슬기","스윙스","김윤석"],\
            "늑대상":["세훈","뷔","황인엽","김영대","서강준","구준회"],\
            "원숭이상":["박진영","빈지노","양세형","코드쿤스트","지드래곤"],\
            "거북이상":["샤이니민호","솔라","예리","유정","팔로알토"],
            "돼지상":["강소라","강호동","김준현","박나래","서현","소유","손나은"],\
            "사슴상":["김채원","렌","루한","샤이니민호","송강","윤아","차은우","태민"],\
            "개구리상":["권정열","김민주","오마이걸비니","신민아","전소민","하현우"]}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

def webscrape_images1():
    for id,animal in enumerate(an_face.keys()):
        print("1st loop",animal,"searching")
        url = "https://search.aol.com/aol/image;_ylt=Awr9Hr57TuJh5GkAKeNjCWVH?q={}+연예인&ei=UTF-8&s_it=sb_top&v_t=comsearch&imgty=photo&fr2=p%3As%2Cv%3Ai".format(animal)
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        images = soup.find_all("a", attrs={"class":"img"})
        print("images length:",len(images))
        if animal == '강아지상':
            os.chdir('images/dog')
        elif animal == '고양이상':
            os.chdir('images/cat')
        elif animal == '토끼상':
            os.chdir('images/rabbit')
        elif animal == '말상':
            os.chdir('images/horse')
        elif animal == '여우상':
            os.chdir('images/fox')
        elif animal == '다람쥐상':
            os.chdir('images/squirrel')
        elif animal == '곰상':
            os.chdir('images/bear')
        elif animal == '늑대상':
            os.chdir('images/wolf')
        elif animal == '원숭이상':
            os.chdir('images/monkey')
        elif animal == '거북이상':
            os.chdir('images/turtle')
        elif animal == '돼지상':
            os.chdir('images/pig')
        elif animal == '사슴상':
            os.chdir('images/deer')
        elif animal == '개구리상':
            os.chdir('images/frog')
        cnt = 0
        for i,image in enumerate(images):
            cnt += 1
            image_url = image["href"]
            image_res = requests.get(image_url)
            try:
                with open("{}{}.jpg".format(animal,i), "wb") as f:
                    f.write(image_res.content)
            except image_res.raise_for_status():
                continue
        os.chdir(owd)

def webscrape_images2(dog_cnt,cat_cnt,rabbit_cnt,horse_cnt,fox_cnt,squirrel_cnt,bear_cnt,wolf_cnt,monkey_cnt,turtle_cnt,pig_cnt,deer_cnt,frog_cnt):
    for idx1,names in enumerate(an_face.values()):
        for name_ind,name in enumerate(names):
            print("2nd loop",name,"searching")
            url1 = "https://search.aol.com/aol/image;_ylt=Awr9Hr57TuJh5GkAKeNjCWVH?q={}+얼굴&ei=UTF-8&s_it=sb_top&v_t=comsearch&imgty=photo&fr2=p%3As%2Cv%3Ai".format(name)
            res1 = requests.get(url1, headers=headers)
            res1.raise_for_status()
            soup1 = BeautifulSoup(res1.text, "lxml")
            face_images = soup1.find_all("a", attrs={"class":"img"})
            if idx1 == 0:
                os.chdir('images/dog')
                animal = '강아지상'
                if name_ind > 0:
                    dog_cnt += temp_cnt
                cnt = dog_cnt
            elif idx1 == 1:
                os.chdir('images/cat')
                animal = '고양이상'
                if name_ind > 0:
                    cat_cnt += temp_cnt
                cnt = cat_cnt
            elif idx1 == 2:
                os.chdir('images/rabbit')
                animal = '토끼상'
                if name_ind > 0:
                    rabbit_cnt += temp_cnt
                cnt = rabbit_cnt
            elif idx1 == 3:
                os.chdir('images/horse')
                animal = '말상'
                if name_ind > 0:
                    horse_cnt += temp_cnt
                cnt = horse_cnt
            elif idx1 == 4:
                os.chdir('images/fox')
                animal = '여우상'
                if name_ind > 0:
                    fox_cnt += temp_cnt
                cnt = fox_cnt
            elif idx1 == 5:
                os.chdir('images/squirrel')
                animal = '다람쥐상'
                if name_ind > 0:
                    squirrel_cnt += temp_cnt
                cnt = squirrel_cnt
            elif idx1 == 6:
                os.chdir('images/bear')
                animal = '곰상'
                if name_ind > 0:
                    bear_cnt += temp_cnt
                cnt = bear_cnt
            elif idx1 == 7:
                os.chdir('images/wolf')
                animal = '늑대상'
                if name_ind > 0:
                    wolf_cnt += temp_cnt
                cnt = wolf_cnt
            elif idx1 == 8:
                os.chdir('images/monkey')
                animal = '원숭이상'
                if name_ind > 0:
                    monkey_cnt += temp_cnt
                cnt = monkey_cnt
            elif idx1 == 9:
                os.chdir('images/turtle')
                animal = '거북이상'
                if name_ind > 0:
                    turtle_cnt += temp_cnt
                cnt = turtle_cnt
            elif idx1 == 10:
                os.chdir('images/pig')
                animal = '돼지상'
                if name_ind > 0:
                    pig_cnt += temp_cnt
                cnt = pig_cnt
            elif idx1 == 11:
                os.chdir('images/deer')
                animal = '사슴상'
                if name_ind > 0:
                    deer_cnt += temp_cnt
                cnt = deer_cnt
            elif idx1 == 12:
                os.chdir('images/frog')
                animal = '개구리상'
                if name_ind > 0:
                    frog_cnt += temp_cnt
                cnt = frog_cnt
            temp_cnt = 0
            print("length= ",len(face_images))
            for face_ind,face_image in enumerate(face_images):
                print(face_ind)
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
            
# webscrape_images2(36,46,36,23,40,44,21,14,38,11,26,24,34)