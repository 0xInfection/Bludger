#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

from core.colors import G
import logging, sys
from core.requester import sendQuery

baseurl = 'https://api.github.com/repos/{}/actions/runs/{}/cancel'

def cancelWorkflow(slug: str, runid: bool):
    '''
    Creates a repository for the authenticated user
    '''
    global baseurl
    log = logging.getLogger('triggerFlow')

    if not runid or not slug:
        log.error('One or more required parameters got passed invalid params.')
        return None

    baseurl = baseurl.format(slug, runid)

    # github REST API is extrememly buggy about the name conventions
    # between the master and main, although they are the same thing
    # useless bullshit in my opinion.
    req = sendQuery("POST", baseurl, json=None)
    if req is not None:
        print(G, 'Successfully requested a cancel for workflow: %s' % runid)
        return True

    else:
        log.fatal('Could not canel the workflow. Something went wrong!')
        sys.exit(1)
