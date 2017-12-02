from django.shortcuts import render, redirect

from .forms import PredictForm
from .models import Predict
from django.shortcuts import render_to_response
from django.template import RequestContext
from bs4 import BeautifulSoup
import requests
from django.http import Http404

# Create your views here.
def index(request):

    rbX=rbY=0
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():

            from models import Serve
            obj = form.save(commit=False)
            try:
              obj = parse(obj)

            except:
                raise Http404("Wrong input")

            dict = Serve.SMOreg(obj, rbX, rbY)
            obj.audience_num=int(dict['audience_num'])
            rbX = dict['rbX']
            rbY = dict['rbY']

            print(obj.audience_num)

            if int(obj.audience_num) < 200000:
                obj.audience_num = 200000

            # feature : 7 days - 4
            #           effect - 3
            #           age, nationality, month - 3
            #           rating - 2
            # 12 features
            obj.save()

            return redirect('/')
        else :
            raise Http404("Wrong input")
    else :

        form = PredictForm()
        predicts = Predict.objects.order_by("-id")
        ctx = {'form': form, 'predicts': predicts}
        return render(request, 'predicts/index.html', ctx)


def serve(request, predict_id):
    from models import Serve
    rbX=rbY=0
    obj = Predict.objects.get(id=predict_id)
    try:
        obj = parse(obj)
    except:
        raise Http404("입력 인자가 잘못되었습니다.")

    dict = Serve.SMOreg(obj, rbX, rbY)
    print(dict['audience_num'])
    obj.audience_num = int(dict['audience_num'])

    rbX = dict['rbX']
    rbY = dict['rbY']
    if int(obj.audience_num) < 200000:
        obj.audience_num = 200000

    obj.save()

    return redirect("/")
"""
def update(obj):
    r = requests.get(obj.url.replace('basic', 'point'))
    soup = BeautifulSoup(r.text)

    print(soup.select(".h_movie a")[0].text)
    obj.title = soup.select(".h_movie a")[0].text

    obj.image_url = soup.select(".poster img")[0]['src']

    # 개봉 전 평점
    try:
        rating_before = ""
        for e in soup.find(id="beforePointArea").find(class_="star_score").find_all("em"):
            rating_before += e.text
        obj.rating_before = rating_before
    except:
        obj.rating_before = 5.0

    # 개봉 후 평점
    try:
        rating_after = ""
        for e in soup.find(id="netizen_point_tab_inner").find(class_="star_score").find_all("em"):
            rating_after += e.text
        obj.rating_after = rating_after
    except:
        obj.rating_after = obj.rating_before

    r = requests.get("https://search.naver.com/search.naver?where=news&query=영화+" + urllib.parse.quote(
        obj.title))
    soup = BeautifulSoup(r.text)

    # 뉴스 기사 수
    try:
        obj.num_news = soup.select(".all_my")[0].text[7:-1].replace(',', '')
    except:
        pass

    return obj
"""
def parse(obj):
    try:
        r = requests.get(obj.naver_url.replace('basic','point'))
        soup = BeautifulSoup(r.text)
    except:
        raise Http404("Parsing error")

    # title, image_url
    obj.title = soup.select(".h_movie a")[0].text
    obj.image_url = soup.select(".poster img")[0]['src']
    obj.image_url = obj.image_url.split('?type=',1)[0]

    # rating before
    try:
        before_grade = ""
        for e in soup.find(id="beforePointArea").find(class_="star_score").find_all("em"):
            before_grade += e.text
        obj.before_grade = before_grade
    except:
        obj.before_grade = 5.0

    # rating after
    try:
        after_grade = ""
        for e in soup.find(id="netizen_point_tab_inner").find(class_="star_score").find_all("em"):
            after_grade += e.text
        obj.after_grade = after_grade
    except:
        obj.after_grade = obj.before_grade

    # month, nationality, age
    obj.month = soup.select("dl.info_spec dd span:nth-of-type(4) a")[1].text[1:3]
    if soup.select("dl.info_spec dd span:nth-of-type(2) a")[0].text == "한국":
        obj.nationality = 1
    else:
        obj.nationality = 0

    if soup.select("dl.info_spec dd:nth-of-type(4) a")[0].text == "청소년 관람불가":
        obj.age = 18
    elif soup.select("dl.info_spec dd:nth-of-type(4) a")[0].text == "15세 관람가":
        obj.age = 15
    elif soup.select("dl.info_spec dd:nth-of-type(4) a")[0].text == "12세 관람가":
        obj.age = 12
    else:
        obj.age = 7

    # actor_effect, director_effect
    top_actor = ["오달수", "황정민", "송강호", "류승룡", "하정우", "이정재", "로버트 다우니 주니어", "강동원", "돈 치들", "크리스 에반스", "김윤석", "유해진", "이병헌",
                 "전지현", "제레미 레너", "스칼렛 요한슨", "심은경", "공유", "최민식", "설경구", "유아인", "사무엘 L. 잭슨", "앤 해서웨이", "곽도원",
                 "스텔란 스카스가드", "김혜수", "조진웅", "김수현", "샤이아 라보프", "손예진"]
    top_director = ["최동훈", "크리스토퍼 놀란", "윤제균", "김한민", "마이클 베이", "류승완", "이석훈", "강형철", "조스 웨던", "김성훈", "한재림", "김지운",
                    "제임스 카메론", "황동혁", "이환경", "조의석", "추창민", "나홍진", "연상호", "양우석", "크리스 벅", "제니퍼 리", "이일형", "윤종빈", "박정우",
                    "데이빗 예이츠", "마크 웹", "쉐인 블랙", "봉준호", "존 파브로"]

    r = requests.get(obj.naver_url.replace('basic', 'detail'))
    soup = BeautifulSoup(r.text)

    top_actor_count = 0
    for person in soup.select(".lst_people > li"):
        if person.select(".p_part")[0].text == "주연":
            for actor in top_actor:
                if person.select(".p_info a")[0].text == actor:
                    top_actor_count += 1
                    break
    obj.actor_effect = top_actor_count

    top_director_count = 0
    for director in top_director:
        if soup.select("dl.info_spec dd:nth-of-type(2) a")[0].text == director:
            top_director_count += 1
    obj.director_effect = top_director_count

    try:
        # 영화 진흥원 파싱
        r = requests.post("http://www.kobis.or.kr/kobis/business/mast/mvie/searchMovieDtl.do",
                          data={'code': obj.movie_code, 'sType': 'stat'})

        soup = BeautifulSoup(r.text)
    except:
        return

    screen_num_7 = 0
    show_num_7 = 0
    money_num_7 = 0
    audience_num_7 = 0
    for index, data in enumerate(soup.select(".topico tbody tr")[1:8]):
        if data.select("td")[0].text == "최근10일이전":
            if index == 0:
                try:
                    screen_num_7 += int(soup.select(".topico tbody tr")[0].select("td")[1].text.replace(',', ''))
                    show_num_7 += int(soup.select(".topico tbody tr")[0].select("td")[2].text.replace(',', ''))
                    money_num_7 += int(soup.select(".topico tbody tr")[0].select("td")[3].text.replace(',', ''))
                    audience_num_7 += int(soup.select(".topico tbody tr")[0].select("td")[4].text.replace(',', ''))
                except:
                    pass
            else:
                screen_num_7 = screen_num_7 / index * 7
                show_num_7 = show_num_7 / index * 7
                money_num_7 = money_num_7 / index * 7
                audience_num_7 = audience_num_7 / index * 7
            break
        screen_num_7 += int(data.select("td")[1].text.replace(',', ''))
        show_num_7 += int(data.select("td")[2].text.replace(',', ''))
        money_num_7 += int(data.select("td")[3].text.replace(',', ''))
        audience_num_7 += int(data.select("td")[4].text.replace(',', ''))

    # screen_num_7, show_num_7, money_num_7, audience_num_7
    obj.screen_num_7 = int(screen_num_7)
    obj.show_num_7 = int(show_num_7)
    obj.money_num_7 = int(money_num_7)
    obj.audience_num_7 = int(audience_num_7)


    return obj

