import os
import requests

def restart():
    answer = str(input("Do you want to start over? y/n ")).lower()
    if answer == "y" or answer =="n":
        if answer == "n":
            print("k. bye!")
            return  # return 으로 함수 종료 시켜 for문의 break를 쓸 필요가 없다.
        elif answer == "y":
        main() #함수내에서도 다른 함수나 자체의 함수를 부를 수도 있다 이를 재귀함수(호출) 라고 부른다.
    else:
        print("That's not a valid answer")
        restart()


def main():
    os.system('clear')
    print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
    urls = str(input()).lower().split(",")
    for url in urls:
        url = url.strip()
        if "." not in url:
        print(url, "is not a valid URL.")
        else:
        if "http" not in url:
            url = f"http://{url}"
        try:
            request = requests.get(url)
            if request.status_code == 200:
            print(url,"is up!")
            else:
            print(url, "is down!")
        except:
            print(url, "is down!")
    restart()


main()