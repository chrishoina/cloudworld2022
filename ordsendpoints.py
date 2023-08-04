from time import pthread_getcpuclockid
from urllib import request
import requests
import json 

url = ("https://gf641ea24ecc468-darmok.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondarmok")


happy15 = json.loads(requests.get(f"{url}/happy2015/").text) 
happy16 = json.loads(requests.get(f"{url}/happy2016/").text)
happy17 = json.loads(requests.get(f"{url}/happy2017/").text)
happy18 = json.loads(requests.get(f"{url}/happy2018/").text)
happy19 = json.loads(requests.get(f"{url}/happy2019/").text)
happy22 = json.loads(requests.get(f"{url}/happy2022/").text)

import requests
import json 

def getthedata():

    url = "https://gf641ea24ecc468-darmok.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondarmok/happy2015/?q={'country':'Switzerland'}"
    

    response = requests.get(f"{url}" + "?q={"country": "Switzerland"}")
    listofdata = []

    for thereturneditems in response.json()['items']:
        datadictionary = dict()
        
        try: 
            rank = thereturneditems['happiness_rank']
            score = thereturneditems['happiness_score)']
            listofdata.append(datadictionary)
    
        except:
            pass

    return listofdata

