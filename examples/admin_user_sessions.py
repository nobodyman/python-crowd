#!/usr/bin/env python

import crowd
import os, sys, getpass
from examples import settings 

app_url =  settings.app_url
app_user = settings.app_user
app_pass = settings.app_pass

# Create the reusable Crowd object
cs = crowd.CrowdServer(app_url, app_user, app_pass)


users = cs.get_user_sessions("1")
if users:
    print(f'got user list:  \n\t {users}')
    
else:
    print('failed')
