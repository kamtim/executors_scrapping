import requests

# return captcha because api is not public

r = requests.get('https://youdo.com/api/executors/executors/?category=teaching&subcategorycode=english&page=1&station=&city=&isonline=false&isonlyvalidated=falsehttps://youdo.com/api/executors/executors/?category=teaching&subcategorycode=english&page=1&station=&city=&isonline=false&isonlyvalidated=false')
print(r.text)