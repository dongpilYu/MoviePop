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
