'''
Created on Oct 9, 2010

@author: ajk377
'''

import oauth2 as oauth
import time
import urlparse

def setUpRequestToken():
    # request token #
    request_token_url = "http://foursquare.com/oauth/request_token"
    
    consumer = oauth.Consumer(
        key="ZUXPQ3BFIVUFBL1M4ZIH32YKUXACXX2UHRYHIY31GKOIHW3F", 
        secret="JUWDS2GZD2XSAELLYNE5XFH2T1VESTUIPWNRHIPH2EDPVTBK")
        
    client = oauth.Client(consumer)
    resp, content = client.request(request_token_url, "GET")
    request_token = dict(urlparse.parse_qsl(content))
    
    token = oauth.Token(request_token['oauth_token'], 
                        request_token['oauth_token_secret'])
def main():
    setUpRequestToken()
if __name__ == '__main__':
    main()