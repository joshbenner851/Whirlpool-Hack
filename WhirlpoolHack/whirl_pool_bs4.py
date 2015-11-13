import urllib.request
import urllib.parse
import json
from time import sleep
from bs4 import BeautifulSoup

#api string for whirlpool
url2 = 'https://api-mc360.spindance.com/api/v1/device/payment'
#washing machine api dictionary requirements
values = {'machine_id' : 'SYS0007373',
          'user_acct_userid' : '12345',
          'payment_amount' : 0,
          'access_token' : '9A012D08-235B-4917-BA9E-6FF48332ED7D'}
#twitterurl = "https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi"

teams = []
scores = [[0,0]]
count =0
values2 = {'machine_id' : 'SYS0007325',
           'user_acct_userid': '54321',
           'payment_amount': 0,
           'access_token': '9A012D08-235B-4917-BA9E-6FF48332ED7D'}
'''values2['payment_amount'] = 50
data = urllib.parse.urlencode(values2)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url2, data)
response = urllib.request.urlopen(req)
the_page = response.read()
'''
def Washer(scores):
    '''calculates pennies to send to washing machine'''
    values['payment_amount'] = scores[0]*25
    setWashers(values)
    #values['access_token'] = 'SYS0007325'
    values2['payment_amount'] = scores[1]*25
    setWashers(values2)
    
def setWashers(values):
    '''makes a post call to the whirlpool api to set the time '''
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') # data should be bytes
    req = urllib.request.Request(url2, data)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    
while(count<40):
    if(count<1):
        urlz = str(input("enter a url"))
    url = urllib.request.urlopen(urlz)
    soup = BeautifulSoup(url)
    if(count<1):
        teams.append([soup.findAll('span',{"class":"home"})[0].text,soup.findAll('span',{"class":"away"})[0].text])
    x = soup.findAll('div',{"class":"hidden-scores"})[0]
    print(x)
    soup2 = BeautifulSoup(str(x))
    #parsing through the span tag to search for all homes tag, getting text
    sco = [soup2.findAll('span',{"class":"home"})[0].text,soup2.findAll('span',{"class":"away"})[0].text]
    #if getting the new list isn't different from the last, don't do anything
    if(sco!=scores[-1]):
        scores.append(sco)
        difference = (int(scores[-1][0]) - int(scores[-2][0]),int(scores[-1][1]) - int(scores[-2][1]))
        print("difference was : " , difference)
        Washer(difference)
        count+=1
        print(teams, " ",  scores)
    #print(int(scores[-1][0]) - int(scores[-2][0]))

Id = []
sleep(2)
print(scores)


'''
def gametostring(score):
    for x in range(len(score)):
        print(Id[x][1] + " " + str(score[x][0]) + " - " + Id[x][2] + " " +  str(score[x][1]))
    #values['payment_amount'] = 250
        
gametostring(game_master)
print("hello")
'''

'''
for x in range(0,5):
    Id.append([str(mydict["games"][x]["id"]),mydict["games"][x]["home"]["name"],mydict["games"][x]["away"]["name"]])
    #Id.append(members)
    
    #if(!mydict["games"][x]["title"][0,3]
    #print(mydict["games"][x]["home"]["name"] + " vs " ,mydict["games"][x]["away"]["name"])
#values['payment_amount'] = (int(mydict["date"].split("-")[-1])//5)*25
#print(Id)
'''
