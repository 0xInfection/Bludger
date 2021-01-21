#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#       Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

from core.colors import G
import logging, base64
from core.requester import sendQuery

baseurl = 'https://api.github.com/repos/{}/contents/{}'

def commitFile(file: str, path: str, repo: str):
    '''
    Commits a file to the GitHub Repository
    '''
    global baseurl
    log = logging.getLogger('commitFile')

    if path is not None:
        path = '.github/workflows/{}.yml'.format(path)
        log.debug('Target file to create: %s' % path)
    else:
        path = '.github/workflows/{}.yml'.format('default')
        with open('templates/default.yml', 'r') as rf:
            file = rf.read()

    baseurl = baseurl.format(repo, path)

    log.debug('Encoding the file to base64.')
    file64 = base64.b64encode(file.encode('ascii'))
    file64msg = file64.decode('ascii')

    log.debug('Content to commit: %s' % file64msg)

    payload = {
        "content"   : file64msg,
        "message"   : 'Added workflow file',
    }

    log.debug('Trying to create the file...')
    req = sendQuery("PUT", baseurl, json=payload)

    if req is not None:
        print(G, 'File successfully committed to GitHub: %s' % path)
        return True

    return False