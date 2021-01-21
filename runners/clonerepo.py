#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

from core.colors import G
import logging, git, os, shutil
from config import ACCESS_TOKEN

cloneurl = 'https://oauth2:{}@github.com/{}.git'

def cloneRepo(slug: str, path='./custom/'):
    '''
    Clones a repository off GitHub
    '''
    global cloneurl
    rpath = os.path.join(path, slug.split('/')[1])
    log = logging.getLogger('cloneRepo')
    if os.path.exists(rpath):
        log.info('Repository already exists under the custom folder. Recloning...')
        shutil.rmtree(rpath)
    log.info('Trying to clone the repository...')
    cloneurl = cloneurl.format(ACCESS_TOKEN, slug)
    try:
        git.Repo.clone_from(cloneurl, rpath, depth=1)
        print(G, 'Repository successfully cloned under custom/ directory!')
        return True
    except Exception as e:
        log.critical('Error during cloning: %s' % e.__str__())
        return False
