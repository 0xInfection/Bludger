## Downloading and Parsing Datasets

Lets take a look at an example where we will download, parse and analyse a large dataset for research purposes. In this example we'll be using a small dataset, the UDP mDNS dataset from Rapid7 SonarDB.

> Link: https://opendata.rapid7.com/sonar.udp/2020-12-11-1607672419-udp_mdns_5353.csv.gz

### Template
You can write your own template for this, but for now, we'll use the `basic-python.yml` template:
```yml
# Template for basic python automation
name: Custom Python Automation

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Setup python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name : Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ ! -f requirements.txt ]; then echo "Skipping requirements.txt step"; else python -m pip install -r requirements.txt; fi

      - name: Run the scripts
        run: {command}

      - name: Commit and push
        uses: stefanzweifel/git-auto-commit-action@v4.2.0
        with:
          commit_message: Commit output files
          commit_user_name: 'Basic Python'
          commit_user_email: 'github-actions.python@github.com'
```

### Notes:
Few important points the template says:
- It instructs GitHub Actions to run only on `workflow_dispatch`, i.e. on manual trigger.
- It downloads the dataset and extracts it, displaying the first 5 lines of the resultant output file.
- It tells the tool that it accepts a command which needs to be supplied by the `-C` or the `--command` argument.
- It commits back the generated files back to GitHub after the workflow has finished.

### Usage:
- First off lets create a simple python script to read our csv dataset.
    ```python
    import csv, sys

    filename = sys.argv[1]
    fields, rows = list(), list()

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
        print("Total no. of rows: %d" % csvreader.line_num)

    print('Field names are:' + ', '.join(field for field in fields))
    print('\nFirst 5 rows are:\n')

    for row in rows[:5]:
        for col in row:
            print("%10s" % col)
        print('\n')
    ```
    The python script accepts the name of the csv file as the first argument, and gives us the total no.
    of rows, field names and then displays the first 5 rows. Lets name it `parse.py`.

    Now push the script to github (you can manually do it or see [here](basic-python.md) for more details on how to do it).

- Now, lets go ahead and run the template:
    ```bash
    ./parasite.py -s {user}/{repository} -T basic-python -C 'wget -q https://opendata.rapid7.com/sonar.udp/2020-12-11-1607672419-udp_mdns_5353.csv.gz && gzip -dkv 2020-12-11-1607672419-udp_mdns_5353.csv.gz && python parse.py 2020-12-11-1607672419-udp_mdns_5353.csv' --save-logs ../logsdir/
    ```
    The following things happened here:
    - We instructed parasite to use the `{user}/{repository}`.
    - We used the basic-python.yml template.
    - The command can be broken down:
        - Downloads the dataset from the URL - https://opendata.rapid7.com/sonar.udp/2020-12-11-1607672419-udp_mdns_5353.csv.gz using wget.
        - Extracts the dataset using gzip.
        - Runs the script `parse.py` on the dataset.
    - Lastly, saves the logs to the directory `../logsdir/`.

Thats it, you can view the result of the files from the logs itself!