#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

import logging, sys
from config import COMMAND

def getTemplate(template: str):
    '''
    Takes in a template for processing
    '''
    log = logging.getLogger('templating')
    log.debug('Processing template: %s' % template)

    with open(template, 'r') as rf:
        tempstr = rf.read()
        # if the template takes in command
        if r'{command}' in tempstr.__repr__():
            log.debug('It seems that this template %s takes in commands.' % template)
            if not COMMAND:
                log.fatal('Template contains a commnd directive but user specified none!')
                sys.exit(1)
            tempstr = tempstr.format(command=COMMAND)

    return tempstr

