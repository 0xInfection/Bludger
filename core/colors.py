#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#        Bludger        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Bludger
# https://github.com/0xInfection/Bludger

import os

if os.name != 'nt' and os.name != 'mac':
    class color:
        END  = '\033[0m'                # normal
        BOLD  = '\033[1m'               # bold
        RED  = '\033[91m'             # red
        GREEN  = '\033[92m'           # green
        ORANGE  = '\033[93m'          # orange
        BLUE  = '\033[94m'            # blue
        PURPLE  = '\033[95m'          # purple
        UNDERLINE = '\033[4m'           # underline
        CYAN  = '\033[36m'            # cyan
        GREY = '\033[97m'             # gray
        BR = '\033[97;41m'            # background red
        BG = '\033[97;42m'            # background green
        BY = '\033[97;43m'            # background yellow

    O  = '\033[1m\033[97m[!]\033[0m'  # information
    R  = '\033[1m\033[91m[-]\033[0m'  # something's not right
    GR = '\033[1m\033[93m[*]\033[0m'  # processing
    G  = '\033[1m\033[92m[+]\033[0m'  # yay!
    C  = '\033[1m\033[96m[+]\033[0m'  # done...
    P  = '\033[1m\033[95m[~]\033[0m'  # bruh, this is debug

else:
    class color:
        # no escape sequences
        END=BOLD=RED=GREEN=ORANGE=BLUE=PURPLE=UNDERLINE=CYAN=GREY=BR=BG=BY=''
    # no color values
    O = '[!]'
    R = '[-]'
    GR = '[*]'
    G = '[+]'
    C = '[+]'