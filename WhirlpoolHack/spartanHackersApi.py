import urllib.parse, urllib.request, json
url = input("Please enter the URL you want to shorten (including http://): ")
params = {
    "login" : "spartahack",
    "apiKey" : "R_87c01471ca8b478d9c0c06f168ff39c0",
    "URI" : url
    }
data = urllib.parse.urlencode(params)
data = data.encode('utf-8')
bitly_url = "http://api.bitly.com/v3/shorten?"
request = urllib.request.Request(bitly_url, data)

try:
    response_object = urllib.request.urlopen(request)
    response_text = response_object.read().decode()
    response_json = json.loads(response_text)

    response_data = response_json["data"]
    shortened_url = response_data["url"]
    print("The shortened URL is: ", shortened_url)
    print(response_data)
except:
    print("API reading error")

