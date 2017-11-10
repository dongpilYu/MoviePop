import openpyxl
from bs4 import BeautifulSoup
import requests
import urllib

excel_document = openpyxl.load_workbook('movie_data.xlsx', data_only=True)
sheet = excel_document.get_sheet_by_name('sheet0')

for i in range(4, 1032):
    idx = 'B' + str(i)
    r = requests.get("https://search.naver.com/search.naver?query=영화+" + urllib.parse.quote(sheet[idx].value))
    soup = BeautifulSoup(r.text)
    try:
        if soup.find(id="dss_h_movie_info_opendate_content").text[:4] == sheet['H' + str(i)].value[:4]:
            url = soup.find(class_="sh_movie_link").get("href").replace('basic', 'point')
            r2 = requests.get(url)
            soup2 = BeautifulSoup(r2.text)

            # 개봉 전 평점
            score = ""
            for e2 in soup2.find(id="beforePointArea").find(class_="star_score").find_all("em"):
                score += e2.text
            sheet['Z' + str(i)].value = score

            # 개봉 후 평점
            score2 = ""
            for e2 in soup2.find(id="netizen_point_tab_inner").find(class_="star_score").find_all("em"):
                score2 += e2.text
            sheet['AA' + str(i)].value = score2

            # 주연 배우 3명
            actor = 'W'
            for e2 in soup2.select(".info_spec dd")[2].select("a"):
                if e2.text == "더보기":
                    continue
                sheet[actor + str(i)].value = e2.text
                actor = chr(ord(actor) + 1)
        else:
            print(sheet[idx].value)
    except:
        print(sheet[idx].value)

    # 개봉 전 3개월 이내 뉴스기사 개수
    try:
        year = sheet['I' + str(i)].value
        month = sheet['J' + str(i)].value
        if int(month) < 4:
            year = str(int(year) - 1)
            month = str(int(month) + 12 - 3)
        else:
            month = "0" + str(int(month) - 3)

        r2 = requests.get("https://search.naver.com/search.naver?where=news&query=영화+" + urllib.parse.quote(
            sheet[idx].value) + "&ie=utf8&pd=3&ds=" + year + "." + month + "." + sheet['K' + str(i)].value + "&de=" +
                          sheet['H' + str(i)].value.replace('-', '.'))
        soup2 = BeautifulSoup(r2.text)
        sheet['AB' + str(i)].value = soup2.select(".all_my")[0].text[7:-1].replace(',', '')
    except:
        print(sheet[idx].value)

excel_document.save('movie_data.xlsx')
