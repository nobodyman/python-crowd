#!/usr/bin/env python

import crowd
import os, sys, getpass
from examples import settings 

app_url =  settings.app_url
app_user = settings.app_user
app_pass = settings.app_pass

# Create the reusable Crowd object
cs = crowd.CrowdServer(app_url, app_user, app_pass)

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = os.environ['USER']

password = getpass.getpass(prompt='Enter password for %s: ' % username)

success = cs.auth_user(username, password)
if success:
    print('Successfully authenticated.')
else:
    print('Failed to authenticate.')
