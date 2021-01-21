#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#       Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

import logging, os, zipfile, io, re
from core.colors import G
from core.requester import sendQuery

def getLogs(url: str, path: str):
    '''
    Grabs the logs for a run and saves it to a directory
    '''
    log = logging.getLogger('createRepo')

    if not url and not path:
        log.error('One or more required parameters got passed invalid params.')
        return None

    if not os.path.exists(path):
        log.error('Path %s doesn\'t exist on your filesystem.' % path)
        log.info('Creating the dir: %s' % path)
        os.makedirs(path)

    log.info('Trying to download the logs...')
    req = sendQuery("GET", url, redirection=True, stream=True, params=None)
    if req is not None:
        try:
            filename = re.search(r'(?i)filename=([^;]+)', req.headers['content-disposition'])
            log.info('Inflating the zipped logs: %s' % filename.group(1))

            zipf = zipfile.ZipFile(io.BytesIO(req.content))
            zipf.extractall(path)

            print(G, 'Successfully saved all logs to: %s' % path)

        except Exception as e:
            log.error('Error: %s' % e.__str__())

    return None
