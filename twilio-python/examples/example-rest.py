#!/usr/bin/env python

import twilio

# Twilio REST API version
API_VERSION = '2010-04-01'

# Twilio AccountSid and AuthToken
ACCOUNT_SID = 'AC02e6fc5f949b4c1b01645d52faad168b'
ACCOUNT_TOKEN = 'd72f5917a17f3c4f4504f1c3ff2e8cbb'

# Outgoing Caller ID previously validated with Twilio
CALLER_ID = '6504540072';

# Create a Twilio REST account object using your Twilio account ID and token
account = twilio.Account(ACCOUNT_SID, ACCOUNT_TOKEN)

# ===========================================================================
# 1. Initiate a new outbound call to 415-555-1212
#    uses a HTTP POST
d = {
    'From' : CALLER_ID,
    'To' : '650-454-0072',
    'Url' : 'http://demo.twilio.com/welcome',
}
try:
    print account.request('/%s/Accounts/%s/Calls' % \
                              (API_VERSION, ACCOUNT_SID), 'POST', d)
except Exception, e:
    print e
    print e.read()

# ===========================================================================
# 2. Get a list of recent completed calls (i.e. Status = 2)
#    uses a HTTP GET
d = { 'Status':2, }
try:
    print account.request('/%s/Accounts/%s/Calls' % \
                              (API_VERSION, ACCOUNT_SID), 'GET', d)
except Exception, e:
    print e
    print e.read()

# ===========================================================================
# 3. Get a list of recent notification log entries
#    uses a HTTP GET
try:
    print account.request('/%s/Accounts/%s/Notifications' % \
                              (API_VERSION, ACCOUNT_SID), 'GET')
except Exception, e:
    print e
    print e.read()

# ===========================================================================
# 4. Get a list of audio recordings for a certain call
#    uses a HTTP GET
d = { 'CallSid':'CA0c7001f3f3f5063b7f7d96def0f1ed00', }
try:
    print account.request('/%s/Accounts/%s/Recordings' % \
                              (API_VERSION, ACCOUNT_SID), 'GET', d)
except Exception, e:
    print e
    print e.read()
    
# ===========================================================================
# 5. Delete a specific recording
#    uses a HTTP DELETE, no response is returned when using DELETE
try:
    account.request( \
        '/%s/Accounts/%s/Recordings/RE4e75a0b62a5c52e5cb96dc25fb4101d9' % \
            (API_VERSION, ACCOUNT_SID), 'DELETE')
except Exception, e:
    print e
    print e.read()
