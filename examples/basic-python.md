## Using Masscan

### Template
The masscan template has been already provided alongwith this release. The template looks like:
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

      # assumes that you have a requirements.txt file
      - name : Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install -r requirements.txt

      - name: Run the scripts
        run: {command}

      # Runs a set of commands using the runners shell
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
- It tells the tool that it accepts a command which needs to be supplied by the `-C` or the `--command` argument.
- It commits back the generated files back to GitHub after the workflow has finished.

### Usage:
Lets see a simplified usage of things:

> __NOTE:__ If you already have a repository up on github with your scripts in it, jump to the third step directly.

- Create a new repository `pythontest` and clone it locally under `custom/` folder.
    ```bash
    ./parasite.py -n pythontest --clone
    ```
- Now, put all your scripts inside the fresh cloned repository.
    ```bash
    cd custom/pythontest/
    cp ../../../some_other/directory/*.py .   # copy all your scripts rightaway
    echo 'print("Hello World")' >> hello.py   # additionally for a valid use case, we use hello.py
    echo 'print("Yo")' >> yo.py               # another demo file
    echo 'requests' >> requirements.txt       # its a good idea to keep all your dependencies in a requirements.txt file
    cd ../../
    ```
- Now its time to push these to GitHub. The below command will automatically commit the files and push it to GitHub. Note, `--push` takes in a repository name cloned under `custom/` folder.
    ```bash
    ./parasite.py --push pythontest
    ```
- Time for the actual hack. Specify your command through the `-C` switch. You can specify multiple commands using bash separators liek `&&` or semicolons `;`. Also we instruct Parasite to save the runtime logs locally in a new folder named `mypage/`.
    ```bash
    ./parasite.py -s {username}/pythontest -T basic-python -C 'python hello.py && python yo.py' --save-logs ../mypage/
    ```

Thats it! Now go ahead and check your results. Additionally if your scripts generate an output file, you can reclone the repository and checkout the output files. Parasite is as flexible as your thoughts!