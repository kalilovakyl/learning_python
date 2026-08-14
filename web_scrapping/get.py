import requests
res = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')
print(res.status_code)
print(res.content)
