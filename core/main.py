#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

from runners.deleteflow import deleteFlow
from core.options import *
import logging, config
from core.utils import checkTemplate
from runners.deleterepo import deleteRepo
from runners.cancelflow import cancelWorkflow
from runners.pushrepo import pushRepo
from core.templating import getTemplate
from runners.commitfile import commitFile
from runners.createrepo import createRepo
from runners.checkrun import checkRun
from runners.clonerepo import cloneRepo
from runners.triggerflow import triggerWorkflow
from core.logger import CustomFormatter, calcLogLevel

def kickOff():
    '''
    Binds the entire framework into one
    '''
    formatter = CustomFormatter()
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(fmt=formatter)
    logging.root.addHandler(hdlr=handler)
    logging.root.setLevel(level=calcLogLevel(args))
    log = logging.getLogger('main')

    if not config.ACCESS_TOKEN:
        log.critical('You have to supply an access token via -A or the config.py file for this tool to work!')
        sys.exit(1)

    reposlug = config.REPO_SLUG

    if config.CREATE_REPO:
        xname = createRepo(config.REPO_NAME, config.IS_PRIVATE)

        if xname is not None:
            reposlug = xname

    # lets start off by just creating a config file
    if config.TEMPLATING:
        temdir = checkTemplate(config.TEMPLATE_NAME)
        configfile = getTemplate(temdir)

        if commitFile(configfile, config.TEMPLATE_NAME, reposlug):
            # lets trigger a workflow
            triggerWorkflow(reposlug, config.TEMPLATE_NAME)

            if not config.MONITOR:
                info = 'Cool, GitHub should\'ve started building on your template rightaway. '
                info += 'Visit https://github.com/%s/actions/ to see it actually running!' % reposlug
                print(G, info)

            else:
                log.info('Entering monitor mode...')

                if config.SAVE_LOGS:
                    checkRun(reposlug, config.TEMPLATE_NAME, path=config.LOGS_DIR)
                else:
                    checkRun(reposlug, config.TEMPLATE_NAME)

        else:
            log.fatal('Dang, something went wrong while committing the file.')
            sys.exit(1)

    if config.TOTRIGGER:
        triggerWorkflow(reposlug, config.TOTRIGGER)
        if config.MONITOR:
            log.info('Entering monitor mode...')
            if config.SAVE_LOGS:
                checkRun(reposlug, config.TOTRIGGER, path=config.LOGS_DIR)
            else:
                checkRun(reposlug, config.TOTRIGGER)

    if config.TOCANCEL:
        cancelWorkflow(reposlug, config.TOCANCEL)

    if config.CLONE_REPO:
        cloneRepo(reposlug)

    if config.TOPUSH:
        pushRepo(config.TOPUSH)

    if config.TODELETE:
        # we know its a repository
        if '/' in config.TODELETE:
            deleteRepo(config.TODELETE)
        # we know it is a file
        else:
            deleteFlow(reposlug, config.TODELETE)