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
    deluser = sys.argv[1] 
else:
    # deluser = os.environ['DELUSER']
    deluser = '11@11.com';




success = cs.delete_user(deluser)
if success:
    print('Successfully authenticated.')
else:
    print('Failed to authenticate.')
