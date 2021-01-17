#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#       Parasite        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Parasite
# https://github.com/0xInfection/Parasite

import requests, logging, urllib3

from core.utils import checkStatus
from config import ACCESS_TOKEN, HEADERS, HTTP_TIMEOUT

logging.getLogger('urllib3').setLevel(logging.ERROR)

def sendQuery(method: str, url: str, **kwargs):
    '''
    Makes HTTP all kinds of queries
    '''
    log = logging.getLogger('sendQuery')
    log.debug('Using token: ' + ACCESS_TOKEN)

    HEADERS['Authorization'] = HEADERS.get('Authorization').format(ACCESS_TOKEN)

    if method.lower() == 'get':
        log.debug('Making HTTP GET query: ' + url)
        req = requests.get(url, params=kwargs['params'],
            headers=HEADERS, timeout=HTTP_TIMEOUT)
        if checkStatus(req.status_code):
            return req

    if method.lower() == 'post':
        log.debug('Making HTTP POST query: '+ url)
        req = requests.post(url, json=kwargs['json'],
            headers=HEADERS, timeout=HTTP_TIMEOUT)

        if checkStatus(req.status_code):
            return req

    if method.lower() == 'put':
        log.debug('Making HTTP PUT query: '+ url)
        req = requests.put(url, json=kwargs['json'],
            headers=HEADERS, timeout=HTTP_TIMEOUT)
        if checkStatus(req.status_code):
            return req

    if method.lower() == 'stream':
        log.debug('Trying to download the file: '+ url)
        req = requests.get(url, stream=True,
            timeout=HTTP_TIMEOUT)
        if checkStatus(req.status_code):
            return req

    if method.lower() == 'delete':
        log.debug('Trying to delete: '+ url)
        req = requests.delete(url, json=kwargs['json'],
            timeout=HTTP_TIMEOUT, headers=HEADERS)
        if checkStatus(req.status_code):
            return req

    return None