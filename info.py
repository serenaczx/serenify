import requests
import re
def search_info(url, reg):
    response = requests.get(url)
    # 在响应体中搜索
    result = re.search(reg, response.text)
    if result:
        return {
            "data": result.group(),
            "location": "网页源代码"
        }
    # 在响应头中搜索
    for value in response.headers.values():
        result = re.search(reg, value)
        if result:
            return {
                "data": result.group(),
                "location": "响应头"
            }
    return None
    
if __name__ == '__main__':
    url = 'https://2995a6f6-2c9d-47df-88a4-2bd738e810c8.challenge.ctf.show/'
    reg = r'ctfshow\{.*\}'
    result = search_info(url, reg)
    print(result)