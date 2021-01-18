#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#       Parasite        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Parasite
# https://github.com/0xInfection/Parasite

from core.colors import G, GR
import time, logging
from runners.getlogs import getLogs
from core.requester import sendQuery

runsurl = 'https://api.github.com/repos/{}/actions/workflows/{}/runs'
jobsurl = 'https://api.github.com/repos/{}/actions/runs/{}/jobs'

def checkRun(slug: str, template: str, path=None):
    '''
    Checks workflow status of a template
    '''
    global runsurl, jobsurl, logsurl
    log = logging.getLogger('checkRun')

    # Pause for a few seconds for the workflow to actually trigger
    log.info('Pausing for a few seconds for the workflow to trigger...')
    time.sleep(10)

    template = '%s.yml' % template
    runsurl = runsurl.format(slug, template)

    req = sendQuery("GET", runsurl, params=None)

    if req is not None:
        # get the last workflow run
        # retry for one more time if the API doesn't give a valid response
        while True:
            if len(req.json()['workflow_runs']) == 0:
                log.warn('Waiting for workflow to trigger...')
                time.sleep(10)
                req = sendQuery("GET", runsurl, params=None)
            else:
                break

        jobid = req.json()['workflow_runs'][0]['id']
        jobsurl = jobsurl.format(slug, jobid)
        logsurl = req.json()['workflow_runs'][0]['logs_url']
        log.debug('Jobs URL: %s' % jobsurl)
        log.debug('Logs URL: %s' % logsurl)

        # continuously monitor the workflow for completion
        while True:
            req = sendQuery("GET", jobsurl, params=None)

            if req is not None:
                if req.json()['jobs'][0]['status'] == "completed":
                    print(G, 'Job seems to have successfully completed!')
                    break
                else:
                    log.debug('Workflow not completed yet.')

                    laststep = None
                    for step in req.json()['jobs'][0]['steps']:
                        if step['status'] == 'completed':
                            laststep = step['name']

                    print(GR, 'Last step executed: %s' % laststep)
                    log.debug('Pausing for 7 seconds before checking again...')
                    time.sleep(7)
                    continue

        if req.json()['jobs'][0]['conclusion'] != "success":
            log.error('Job completed but errored out!')
            log.error('Visit: %s for more information' % req.json()['jobs'][0]['html_url'])

        if path is not None:
            # fetch the logs now
            #logsurl = logsurl.format(slug, jobid)
            getLogs(logsurl, path)
