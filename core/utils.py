#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

import sys
import glob
import logging

def checkStatus(code: int, redir=False):
    '''
    Checks status from the HTTP status-codes
    '''
    log = logging.getLogger('checkStatus')
    if str(code).startswith('2'):
        log.debug('Action successfully completed.')
        return True
    if redir:
        if code == 302:
            log.warn('Received HTTP redirection code 302.')
            return True
    # These below have good documentation
    elif code == 304:
        log.debug('Received 304: Not modified')
    elif code == 401:
        log.error('You seem unauthorized. Double check the token supplied.')
    elif code == 403:
        log.error('We did something aweful that Github blocked us!')
    elif code == 404:
        log.error('Recevied 404: Not Found! Hmm, we tried doing something that the API doesn\'t know exists?!')
    elif code == 422:
        log.error('Invalid API query. Status 422: Unprocessable Identity. Something\'s not right.')
    else:
        log.error('Something went wrong.')
    return False


def checkTemplate(tempname: str):
    '''
    Checks if a template mentioned in argument is present in the templates/ directory
    '''
    log = logging.getLogger('checkTemplate')
    templates = glob.glob('templates/*.yml')
    log.debug('So far we have these templates: %s' % templates)
    allnames = [i.split('/')[1].split('.')[0] for i in templates]
    if tempname in allnames:
        log.debug('Template found in the templates folder!')
        return 'templates/{}.yml'.format(tempname)
    else:
        issue = 'Template %s isn\'t present in the templates folder!\n' % tempname
        issue += 'If you wish to continue, please put your config file in the templates folder and retry!'
        log.fatal(issue)
        sys.exit(1)
