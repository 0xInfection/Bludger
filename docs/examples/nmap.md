## Using Nmap

### Template
The nmap template looks like:
```yml
# Template for running nmap on a target/list of targets
name: Nmap Scanner

# add your `on` trigger statement if required
on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Update the packages
        run: sudo apt-get update -y

      - name: Install nmap
        run: sudo apt-get install -y nmap

      - name: Run nmap on a set of targets
        run: |
          sudo {command}

      - name: Commit and push
        uses: stefanzweifel/git-auto-commit-action@v4.2.0
        with:
          commit_message: Commit nmap results (${{ github.sha }})
          commit_user_name: 'Nmap Runner'
          commit_user_email: 'github-actions.nmap@github.com'
```

### Notes:
Few important points the template says:
- It instructs GitHub Actions to run on `workflow_dispatch`, i.e. on manual trigger only.
- It tells the tool that it accepts a command which needs to be supplied by the `-C` or the `--command` argument.
- It commits back the generated files back to GitHub after the workflow has finished.

### Usage:
A single command does the job:
```bash
./bludger.py -n nmaprun -T nmap -C 'nmap -p 80,443 1.1.1.1/28 -T4 -oX 1.1.1.1.xml' --clone
```
Untangling things:
- Creates new repository `nmaprun`.
- Uses the template `nmap.yml`.
- Runs the command `nmap -p 80,443 1.1.1.1/28 -T4 -oX 1.1.1.1.xml`.
- Clones the repository with the resultant file after the scan has finished.

Thats it!