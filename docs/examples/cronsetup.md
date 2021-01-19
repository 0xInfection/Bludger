## Using Crons

### Template
The cron template has been already provided alongwith this release. The template looks like:
```yml
name: The cron to run

on:
  # runs daily at 00:00 UTC
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name : Run your scripts
        run: |
          {command}

      - name: Commit and push
        uses: stefanzweifel/git-auto-commit-action@v4.2.0
        with:
          commit_message: Added cron results
          commit_user_name: 'Cron builder'
          commit_user_email: 'github-actions.cron@github.com'
```

### Notes:
Few important points the template says:
- It instructs GitHub Actions to run only on `workflow_dispatch`, i.e. on manual trigger.
- It has the cron switch, means it will also run according to the cron timing.
- It tells the tool that it accepts a command which needs to be supplied by the `-C` or the `--command` argument.
- It commits back the generated files back to GitHub after the workflow has finished.

### Usage:
Lets see a simplified usage of things. In this case, we'll setup a cron to ping hackerone.com on ICMP. Lets type off the one in all command:
```bash
./parasite.py -n crontest -T cron -C 'ping -c 4 hackerone.com'
```

Thats it!