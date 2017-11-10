# MoviePop

Predict Number of Movie Viewers

![](http://i.imgur.com/js4QkxO.jpg)

## Model Info
```
movie_data.xlsx - All Data
dataset.csv - Training DataSet
movie_parse.py - Parse Naver Movie Data
movie_train.py - Train Model
movie_serve.py - Serve Model
```

* 1028개의 영화 (2008~2017년 영화 중 20만 관객 이상)
* 개봉 전 평점, 개봉 후 평점, 네이버 뉴스 기사 개수, 4대 배급사 유무
* 개봉하지 않은 영화일 경우 개봉 전 평점=개봉 후 평점
* batch_size=500, layer=4. shape=128, step=5001 
* xavier_initializer + AdamOptimizer

## Requirement
* Python 3.6.0
* Tensorflow 1.2.1
* Django 1.11.3
* BeautifulSoup 4.4.0


## Usage
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```