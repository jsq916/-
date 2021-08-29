import requests


class RequestUtils():
    output = []

    def __init__(self):
        self.output = []

    def tmp(self,arg):
        print("ok")
        print(self.output)
        self.output=arg
        print(self.output)


if __name__ == "__main__":
    head = requests.head(url="http://baidu.com")
    response = requests.request("GET", url="http://baidu.com")
    print(head)
    print((((response))))
