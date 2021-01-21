#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

import requests, logging, config
from core.utils import checkStatus
from core.logger import pheaders, pbody

logging.getLogger('urllib3').setLevel(logging.ERROR)

def sendQuery(method: str, url: str, **kwargs):
    '''
    Makes HTTP all kinds of queries
    '''
    log = logging.getLogger('sendQuery')
    log.debug('Using token: %s' % config.ACCESS_TOKEN)

    HEADERS = config.HEADERS
    HEADERS['Authorization'] = HEADERS.get('Authorization').format(config.ACCESS_TOKEN)

    if method.lower() == 'get':
        redirection = False
        tostream = False
        try:
            redirection = kwargs['redirection']
        except KeyError:
            pass

        try:
            tostream = kwargs['stream']
        except KeyError:
            pass

        log.debug('Making HTTP GET query: ' + url)

        req = requests.get(url, params=kwargs['params'],
            headers=HEADERS, stream=tostream, timeout=config.HTTP_TIMEOUT)

        if config.DEBUG:
            pheaders(req.headers)
            pbody(req.text)

        if checkStatus(req.status_code, redir=redirection):
            return req
        else:
            log.critical('Error received: %s' % req.json())

    if method.lower() == 'post':
        log.debug('Making HTTP POST query: '+ url)
        req = requests.post(url, json=kwargs['json'],
            headers=HEADERS, timeout=config.HTTP_TIMEOUT)

        if config.DEBUG:
            pheaders(req.headers)
            pbody(req.text)

        if checkStatus(req.status_code):
            return req
        else:
            log.critical('Error received: %s' % req.json())

    if method.lower() == 'put':

        log.debug('Making HTTP PUT query: '+ url)
        req = requests.put(url, json=kwargs['json'],
            headers=HEADERS, timeout=config.HTTP_TIMEOUT)

        if config.DEBUG:
            pheaders(req.headers)
            pbody(req.text)

        if checkStatus(req.status_code):
            return req
        else:
            log.critical('Error received: %s' % req.json())

    if method.lower() == 'delete':

        log.debug('Trying to delete: '+ url)
        req = requests.delete(url, json=kwargs['json'],
            timeout=config.HTTP_TIMEOUT, headers=HEADERS)

        if config.DEBUG:
            pheaders(req.headers)
            pbody(req.text)

        if checkStatus(req.status_code):
            return req
        else:
            log.critical('Error received: %s' % req.json())

    return None