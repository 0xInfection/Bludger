## Using Masscan

### Template
The masscan template has been already provided alongwith this release. The template looks like:
```yml
# Template for running masscan on a target/list of targets
name: Masscan FTW!

# add your `on` trigger statement
on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Update the packages
        run: sudo apt-get update -y

      - name: Install masscan
        run: sudo apt-get install -y masscan

      - name: Run masscan on a set of targets
        run: |
          sudo {command}

      - name: Commit and push
        uses: stefanzweifel/git-auto-commit-action@v4.2.0
        with:
          commit_message: Commit masscan results (${{ github.sha }})
          commit_user_name: 'Masscan Runner'
          commit_user_email: 'github-actions.masscan@github.com'
```

### Notes:
Few important points the template says:
- It instructs GitHub Actions to run only on `workflow_dispatch`, i.e. on manual trigger.
- It tells the tool that it accepts a command which needs to be supplied by the `-C` or the `--command` argument.
- It commits back the generated files back to GitHub after the workflow has finished.

### Usage:
A single command does the job:
```bash
./parasite.py -n massrun -T masscan -C 'masscan --rate 1000 1.1.1.1/28 -p 1-1024 -oJ 1.1.1.1.json' --save-logs your/preferred/dir/ --clone
```
Untangling things:
- Creates new repository `massrun`.
- Uses the template `masscan.yml`.
- Runs command `masscan --rate 1000 1.1.1.1/28 -p 1-1024 -oJ 1.1.1.1.json`.
- Saves the logs to `your/preferred/dir/`.
- Clones the resultant repository after the scan has finished.

Thats it!