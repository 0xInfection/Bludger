#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

from os.path import pardir
from core.colors import G
import logging, sys, os
from core.requester import sendQuery

baseurl = 'https://api.github.com/repos/{}/contents/{}'

def deleteFlow(slug: str, template: str, path='.github/workflows/'):
    '''
    Creates a repository for the authenticated user
    '''
    global baseurl
    log = logging.getLogger('createRepo')

    if not slug:
        log.error('One or more required parameters got passed invalid params.')
        return None

    template = '%s.yml' % template
    wholepath = os.path.join(path, template)
    baseurl = baseurl.format(slug, wholepath)

    log.debug('Getting SHA of the file...')
    req = sendQuery("GET", baseurl, params=None)

    if req is not None:
        sha = req.json()['sha']
        log.info('Received file SHA: %s' % sha)
        log.info('Trying to delete the file: %s' % wholepath)

        payload = {
            'message'   : 'Deleting %s' % wholepath,
            'sha'       : sha
        }

        req = sendQuery("DELETE", baseurl, json=payload)

        if req is not None:
            print(G, 'Successfully deleted the workflow: %s' % wholepath)
            return True
        else:
            log.fatal('File deletion failed. Stopping all processes.')
            sys.exit(1)
