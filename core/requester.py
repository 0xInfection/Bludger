#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#       Parasite        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Parasite
# https://github.com/0xInfection/Parasite

import requests, logging
from core.utils import checkStatus
from core.logger import pheaders, pbody
from config import ACCESS_TOKEN, HEADERS, HTTP_TIMEOUT, DEBUG

logging.getLogger('urllib3').setLevel(logging.ERROR)

def sendQuery(method: str, url: str, **kwargs):
    '''
    Makes HTTP all kinds of queries
    '''
    log = logging.getLogger('sendQuery')
    log.debug('Using token: ' + ACCESS_TOKEN)

    HEADERS['Authorization'] = HEADERS.get('Authorization').format(ACCESS_TOKEN)

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
            headers=HEADERS, stream=tostream, timeout=HTTP_TIMEOUT)

        if checkStatus(req.status_code, redir=redirection):
            if DEBUG:
                pheaders(req.headers)
                pbody(req.text)
            return req

    if method.lower() == 'post':
        log.debug('Making HTTP POST query: '+ url)
        req = requests.post(url, json=kwargs['json'],
            headers=HEADERS, timeout=HTTP_TIMEOUT)

        if checkStatus(req.status_code):
            if DEBUG:
                pheaders(req.headers)
                pbody(req.text)
            return req

    if method.lower() == 'put':

        log.debug('Making HTTP PUT query: '+ url)
        req = requests.put(url, json=kwargs['json'],
            headers=HEADERS, timeout=HTTP_TIMEOUT)

        if checkStatus(req.status_code):
            if DEBUG:
                pheaders(req.headers)
                pbody(req.text)
            return req

    if method.lower() == 'delete':

        log.debug('Trying to delete: '+ url)
        req = requests.delete(url, json=kwargs['json'],
            timeout=HTTP_TIMEOUT, headers=HEADERS)

        if checkStatus(req.status_code):
            if DEBUG:
                pheaders(req.headers)
                pbody(req.text)
            return req

    return None