#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

import logging, sys
from core.colors import G
from core.requester import sendQuery

baseurl = 'https://api.github.com/user/repos'

def createRepo(reponame: str, isprivate: bool):
    '''
    Creates a repository for the authenticated user
    '''
    log = logging.getLogger('createRepo')

    if not reponame or not isprivate:
        log.error('One or more required parameters got passed invalid params.')
        return None

    log.info('Trying to create the repository...')

    payload = {
        "name"          : reponame,
        "description"   : "My Custom Automation Setup",
        "private"       : isprivate,
    }

    req = sendQuery("POST", baseurl, json=payload)
    if req is not None:
        print(G, 'Successfully created: %s' % req.json()['html_url'])
        log.debug('Repo ID: ' + str(req.json()['id']) + ' | Repo URL: ' + req.json()['html_url'])
        return req.json()['full_name']
    else:
        log.info('Another repository with the same name already exists on your account! Deleting it with --delete flag and trying again.')
        log.fatal('Repository creation failed. Stopping all processes.')
        sys.exit(1)
