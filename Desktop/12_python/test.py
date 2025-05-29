import requests
#f 스트링을 이용해서 이강인이라는 값이 들어간 변수를 활용해주세요.
#누가 미리 만들어 놓은 기능=>내장함수=>input()
#input 값을 입력받으면 무조건 데이터 타입은 문자형
mons= "이강인"
url= "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + mons

req = requests.get(url)
print(req.text)



