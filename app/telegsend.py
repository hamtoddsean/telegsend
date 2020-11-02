import requests,json,csv,datetime,os,time,sys
#from telebot import apihelper
import traceback#,telebot
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

#  CHAT_ID1 = -1001127170747


  
  
  
  



def send_message(text):
  token='802247903:AAHLYB3LODL0pW7kwjkf3encZGqGGuSB5GE'

  chat_id='564189421'
  api_url = "https://api.telegram.org/bot{}/".format(token)
 
  params = {'chat_id': chat_id, 'text': str(text)}
  method = 'sendMessage'
  resp = requests.post(api_url + method, params)
  return resp


if __name__=='__main__':
  v=1
  text='doing this'
  while v==1:
    v=send_message(text)
    print(v)
    time.sleep(300)
