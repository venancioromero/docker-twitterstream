import urllib2 as urllib
import oauth2 as oauth
import json,time,datetime,sys,os

TIMEOUT = int(os.environ['DOWNLOAD_TIME'])
# See Assignment 1 instructions or README for how to get these credentials
access_token_key = os.environ['ACCESS_TOKEN_KEY']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']

outputFile = "twits"
pathOutputFile = "/output/"
_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1.1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  
  init_time = time.mktime(datetime.datetime.today().timetuple())
  file = open(pathOutputFile + outputFile ,"w")
  
  for line in response:
    delta = time.mktime(datetime.datetime.today().timetuple()) - (init_time + TIMEOUT)
    if (delta > 0):
      sys.exit()
    try:
      lineObj = json.loads(line)
      if lineObj["place"] != None:
        twit=json.dumps({"lang": lineObj["lang"], "place": lineObj["place"], "text": lineObj["text"]})
        file.write(twit + "\n")
        print twit
    except:
      pass
  file.close()

if __name__ == '__main__':
  fetchsamples()