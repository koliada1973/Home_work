import requests

# response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

# print(response.text)
# print(response.status_code)
# print(response.json())

# print(f"__attrs__: ", response.__attrs__)
# print(f"_content: ", response._content)
# print(f"status_code: ", response.status_code)
# print(f"headers: ", response.headers)
# print(f"content: ", response.content)
# print(f"url: ", response.url)
# print(requests.__version__)

# response = requests.get("https://www.ukrposhta.ua/files/shares/out/postindex.zip?_gl=1*16zufvm*_gcl_au*MTA5Nzk5MjUyNy4xNzUzMTI1MDQy*_ga*MTIyMTI2MzY2OS4xNzUzMTI1MDQz*_ga_6400KY4HRY*czE3NTQxMjEyMjAkbzMkZzAkdDE3NTQxMjEyMjAkajYwJGwwJGgw&_ga=2.190588777.332186593.1754121221-1221263669.1753125043")
response = requests.get("https://www.ukrposhta.ua/files/shares/out/postindex.zip")
print(f"__attrs__: ", response.__attrs__)
# print(f"encoding: ", response._content)