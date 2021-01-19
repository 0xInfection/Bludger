#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#       Parasite        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Parasite
# https://github.com/0xInfection/Parasite

from core.colors import G
import logging, sys
from core.requester import sendQuery

baseurl = 'https://api.github.com/repos/{}'

def deleteRepo(slug: str):
    '''
    Creates a repository for the authenticated user
    '''
    global baseurl
    log = logging.getLogger('createRepo')

    if not slug:
        log.error('One or more required parameters got passed invalid params.')
        return None

    log.info('Trying to delete the repository: %s' % slug)
    baseurl = baseurl.format(slug)
    req = sendQuery("DELETE", baseurl, json=None)

    if req is not None:
        print(G, 'Successfully deleted the repository: %s' % slug)
        return True
    else:
        log.fatal('Repository deletion failed. Stopping all processes.')
        sys.exit(1)
