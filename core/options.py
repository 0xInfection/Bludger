#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

import logging, sys
import argparse, config
from core.colors import C, color
from core.info import (
    __version__,
    __author__,
    __username__,
    __license__,
    __homepage__,
    __about__,
    __copyright__
)

print('''
  %s%sBludger %s- %sA GitHub Actions Automation Framework
               %sVersion : v%s%s
''' % (color.BOLD, color.CYAN, color.GREY, color.BLUE, color.RED, __version__, color.END))

log = logging.getLogger('options')

parser = argparse.ArgumentParser(usage='./bludger.py -n {repo_name} -A {token} [options]')
parser._action_groups.pop()

required = parser.add_argument_group('Required Arguments')
optional = parser.add_argument_group('Optional Arguments')

# Required arguments - either of these are required
required.add_argument('-n', '--new', dest='repo',
                help='Creates a new repository with supplied name, invalid if -s is specified.')
required.add_argument('-A', '--token', dest='token',
                help='GitHub personal access token to use, not required if already configured in `config.py`')
required.add_argument('-s', '--slug', dest='slug',
                help='Repository slug if you want to use an existing repository, invalid when -n is specified')

# Optional arguments
optional.add_argument('-S', '--save-logs', dest='logs',
                help='Destination path to save logs of the current workflow run.')
optional.add_argument('-T', '--template', dest='template',
                help='Configuration template to use for creating a workflow.')
optional.add_argument('-C', '--command', dest='command',
                help='Command to run for the specified template (if it accepts one).')
optional.add_argument('-P', '--push', dest='topush',
                help='Commits and pushes a local changes to GitHub (must be present under custom/ folder).')
optional.add_argument('-D', '--delete', dest='delete',
                help='Deletes something, it can be either a repository slug or a workflow template.')
optional.add_argument('-t', '--timeout', dest='timeout', type=int,
                help='HTTP timeout value in seconds (default: 5)')
optional.add_argument('-v', '--verbose', dest='verbose', action='count',
                help='Increase output verbosity, multiple -v increase verbosity')
optional.add_argument('--trigger', dest='trigger',
                help='Can be used to manually trigger the workflow specified.')
optional.add_argument('--info', dest='version', action='store_true',
                help='Display information about the tool and exit')
optional.add_argument('--no-monitor', dest='nomonitor', action='store_true',
                help='Tells the program to not monitor the current workflow run.')
optional.add_argument('--public', dest='public', action='store_true',
                help='Sets the visibility of a created repository as public. Valid only when -n is specified.')
optional.add_argument('--clone', dest='clone', action='store_true',
                help='Clones the repository to the current working directory.')
optional.add_argument('--cancel', dest='cancel',
                help='Cancels the last workflow run for a specific configuration.')
optional.add_argument('--debug', dest='debug', action='store_true',
                help='Enables debug mode & prints out HTTP API responses and headers.')

args = parser.parse_args()


if not len(sys.argv) > 1:
    parser.print_help()
    sys.exit(0)

if args.version:
    print(C, color.BOLD+'About:'+color.END+' %s' % __about__)
    print(C, color.BOLD+'Author:'+color.END+' %s (@%s)' % (__author__, __username__))
    print(C, color.BOLD+'Homepage:'+color.END+' %s' % __homepage__)
    print(C, color.BOLD+'Version:'+color.END+' %s' % __version__)
    print(C, color.BOLD+'License:'+color.END+' %s' % __license__)
    print(C, color.BOLD+'Copyright:'+color.END+' %s' % __copyright__)
    sys.exit(0)

if args.repo:
    if args.slug:
        log.fatal('Invalid optiion -s associated with -n. Exiting.')
        sys.exit(1)
    else:
        config.CREATE_REPO = True
        config.REPO_NAME = args.repo

if args.debug:
    config.DEBUG = True

if args.public:
    config.IS_PRIVATE = False

if args.cancel:
    config.TOCANCEL = args.cancel

if args.slug:
    config.REPO_SLUG = args.slug

if args.token:
    config.ACCESS_TOKEN = args.token

if args.topush:
    config.TOPUSH = args.topush

if args.logs:
    config.SAVE_LOGS = True
    config.LOGS_DIR = args.logs

if args.template:
    config.TEMPLATING = True
    config.TEMPLATE_NAME = args.template

if args.command:
    config.COMMAND = args.command

if args.timeout:
    config.HTTP_TIMEOUT = args.timeout

if args.clone:
    config.CLONE_REPO = args.clone

if args.nomonitor:
    config.MONITOR = False

if args.delete:
    config.TODELETE = args.delete

if args.trigger:
    config.TOTRIGGER = args.trigger
