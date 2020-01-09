#!/usr/bin/env python

import crowd
import os, sys, getpass
from examples import settings 

app_url =  settings.app_url
app_user = settings.app_user
app_pass = settings.app_pass

# Create the reusable Crowd object
cs = crowd.CrowdServer(app_url, app_user, app_pass)


success = cs.auth_ping()
if success:
    print(f'Crowd session created:  \n\t {cs.session.cookies}')
    
else:
    print('Auth ping failed')
