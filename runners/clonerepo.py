#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#       Parasite        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Parasite
# https://github.com/0xInfection/Parasite

from core.colors import G
import logging, git
from config import ACCESS_TOKEN

cloneurl = 'https://oauth2:{}@github.com/{}.git'

def cloneRepo(slug: str, path='./'):
    '''
    Clones a repository off GitHub
    '''
    global cloneurl
    log = logging.getLogger('cloneRepo')
    log.info('Trying to clone the repository...')
    cloneurl = cloneurl.format(ACCESS_TOKEN, slug)
    try:
        git.Repo.clone_from(cloneurl, path)
        print(G, 'Repository successfully cloned!')
        return True
    except Exception as e:
        log.critical('Error during cloning:', e.__str__())
        return False