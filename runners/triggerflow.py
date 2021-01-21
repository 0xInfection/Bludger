#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

import time
from core.colors import G
import logging, sys
from core.requester import sendQuery

baseurl = 'https://api.github.com/repos/{}/actions/workflows/{}/dispatches'

def triggerWorkflow(slug: str, template: bool):
    '''
    Creates a workflow run for the authenticated user
    '''
    global baseurl
    log = logging.getLogger('triggerFlow')

    if not template or not slug:
        log.error('One or more required parameters got passed invalid params.')
        return None

    template = '{}.yml'.format(template)
    baseurl = baseurl.format(slug, template)

    payload = {
        "ref" : "master"
    }
    log.debug('Sending payload: %s' % payload)

    # pause for a few seconds, otheriwse github api gives out a 404
    log.warning("Pausing for a few seconds to prevent race condition between API endpoints...")
    time.sleep(10)

    # github REST API is extrememly buggy about the name conventions
    # between the master and main, although they are the same thing
    # useless bullshit in my opinion.
    req = sendQuery("POST", baseurl, json=payload)
    if req is not None:
        print(G, 'Successfully triggered a workflow for: %s' % template)
        return True

    else:
        log.critical('Couldn\'t trigger a workflow! Ref seems to be messing up.')
        log.info('Retrying the request with different ref: master')
        # retry the request using ref as master instead of main
        # usually returns a 422 unprocessable identity
        payload = {
            "ref" : "main"
        }
        log.debug('Sending payload: %s' % payload)

        req = sendQuery("POST", baseurl, json=payload)
        if req is not None:
            print(G, 'Successfully triggered a workflow for: %s' % template)
            return True
        else:
            log.fatal('Could not trigger a workflow. Something went wrong!')
            sys.exit(1)
