#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

############################################
##            ACCESS SETTINGS             ##
############################################

# The ACCESS_TOKEN required to access several parts of the API
ACCESS_TOKEN = None

# Headers which we send to the github api
HEADERS = {
    'User-Agent': 'bludger/0.1.0',
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'token {}'
}

CLONE_REPO = False

#############################################
##      REPOSITORY CREATION SETTINGS       ##
#############################################

# main switch whether to create a repository or not
# all options below this switch is dependent upon this one
# by default its false
CREATE_REPO = False

# repository name
REPO_NAME = 'myautomation'

# whether repository should be public or private
IS_PRIVATE = True

# repo slug is only valid when CREATE_REPO is set of False
# this is only when a repository already exists,
REPO_SLUG = 'user/repo'

# repository to delete
TODELETE = None

# branch
BRANCH = 'main' # or 'master'

# reponame to push
TOPUSH = None

#############################################
##            TEMPLATING ENGINE            ##
#############################################

# Settings about the templating engine
TEMPLATING = False

# Name of template
TEMPLATE_NAME = None

# command to run if a template accepts a command
COMMAND = None

#############################################
##             MONITOR MODE                ##
#############################################

# the workflow to trigger
TOTRIGGER = None

# whether to enter monitor mode or not
MONITOR = True

# whether to save logs or not
SAVE_LOGS = False

# path to save the logs, again, dependent upon the above switch
LOGS_DIR = None

# cancels a workflow
TOCANCEL = None

#############################################
##             GENERIC OPTIONS             ##
#############################################

# HTTP timeout
HTTP_TIMEOUT = 5

# debug level
DEBUG_LEVEL = 30

# whether to print out API responses
DEBUG = False