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

runsurl = 'https://api.github.com/repos/{}/actions/workflows/{}/runs'
baseurl = 'https://api.github.com/repos/{}/actions/runs/{}/cancel'

def cancelWorkflow(slug: str, template: str):
    '''
    Cancels a workflow run for the template supplied
    '''
    global baseurl, runsurl
    log = logging.getLogger('cancelFlow')

    if not template or not slug:
        log.error('One or more required parameters got passed invalid params.')
        return None

    template = '{}.yml'.format(template)
    runsurl = runsurl.format(slug, template)
    req = sendQuery("GET", runsurl, params=None)

    if req is not None:
        runid = req.json()['workflow_runs'][0]['id']
        baseurl = baseurl.format(slug, runid)

        req = sendQuery("POST", baseurl, json=None)
        if req is not None:
            print(G, 'Successfully requested a cancel for workflow: %s' % runid)
            return True

        else:
            log.fatal('Could not canel the workflow. Something went wrong!')
            sys.exit(1)
