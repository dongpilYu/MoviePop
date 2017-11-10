from django.shortcuts import render, redirect

from .forms import PredictForm
from .models import Predict
import movie_serve
from bs4 import BeautifulSoup
import requests
import urllib


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj = update(obj)
            obj.num_viewers = movie_serve.predict(obj.rating_before, obj.rating_after, obj.num_news, obj.distributor)
            obj.save()

            return redirect('/')

    form = PredictForm()
    predicts = Predict.objects.order_by("-id")
    ctx = {'form': form, 'predicts': predicts}
    return render(request, 'predicts/index.html', ctx)


def refresh(request, predict_id):
    obj = Predict.objects.get(id=predict_id)
    obj = update(obj)
    obj.num_viewers = movie_serve.predict(obj.rating_before, obj.rating_after, obj.num_news, obj.distributor)
    obj.save()

    return redirect("/")


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
