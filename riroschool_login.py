# 원래 방과후 신청자동화 할려했는데,..
import requests

ID = input("아이디를 입력해주세요: ")
PW = input("비밀번호를 입력해주세요: ")

url = "https://{학교}.riroschool.kr/ajax.php"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "X-Requested-With" : "XMLHttpRequest",
    "Host" : "{학교}.riroschool.kr",
    "Origin" : "https://{학교}.riroschool.kr",
    "Referer" : "https://{학교}.riroschool.kr/user.php?action=signin"
}

pay_load_login = {
    "app" : "user",
    "mode" : "login",
    "userType" : "1",
    "id" : ID,
    "pw" : PW,
    "deeplink" : "",
    "redirect_link" : ""
}

session = requests.session()
response = requests.post(url, headers=headers, data=pay_load_login)

try:
    json = response.json()
    print("로그인 응답:", response.status_code)
    print("응답:", json)
except requests.exceptions.JSONDecodeError:
    print("json 디코딩 운지, 응답: ",response.text)
