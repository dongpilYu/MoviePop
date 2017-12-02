# MoviePop

Predict Number of Movie Viewers

![](http://i.imgur.com/js4QkxO.jpg)

## Model Info
```
  SMOreg - regression
  14 parameters
  7 days of data after release(money_num_7,show_num_7,theater_num_7,audience_num_7)
  Data of before release
```

* 1028개의 영화 (2008~2017년 영화 중 20만 관객 이상)

## Requirement
* Python 3.6.0
* Tensorflow 1.2.1
* Django 1.11.3
* BeautifulSoup 4.4.0
* numpy
* scikit-learn
* scipy


## Usage
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

이 정도면 충분하다고 생각되지만 추가적인 부분을 언급하자면
개발환경은 pycharm으로 하여 먼저 가상환경을 만들고, Django, BeautifulSoup4, numpy, scikit-learn, scipy를
설치했습니다. 장고의 경우 db에 migrate 할 것이 있는지 확인 한 후 migrate하는 작업이 필요하기
때문에 위의 Usage 순서로 하시면 됩니다.(createsuperuser는 생략 가능).
이후 runserver로 프로그램을 실행시키고 local에 접속하시면 됩니다.
또 만약 pycharm으로 확인하실 경우 Edit configuration에서 python interpreter를 재설정해주어야합니다.

입력에 있어서 사용자가 아예 잘못된 입력을 넣을 경우 예외 처리하여 장고에서 기본적으로 제공하는 page not found
페이지를 보여줍니다. 
