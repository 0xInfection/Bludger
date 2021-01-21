#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

from git import Repo
from core.colors import G
import logging, os, sys

def pushRepo(mdir: str, path='./custom/'):
    '''
    Clones a repository off GitHub
    '''
    global cloneurl

    log = logging.getLogger('cloneRepo')
    rpath = os.path.join(path, mdir)

    if not os.path.exists(rpath):
        log.critical('Repository to push doesn\'t exist!')
        sys.exit(1)

    log.info('Trying to commit files in the repository...')

    os.chdir(rpath)
    os.system('git config user.email "python.automation@bludger.github"')
    os.system('git config user.name "bludger.automation"')

    try:
        repo = Repo('.')
        repo.git.add('.')
        repo.index.commit('Updated with new files')

        origin = repo.remote(name='origin')
        origin.push()

        print(G, 'Successfully pushed changes to %s' % origin.__str__())

    except Exception as err:
        log.critical('Something terrible happened: %s' % err.__str__())
        sys.exit(1)