<h1 align="center">
  <br>
  <a href="https://github.com/0xInfection/Bludger"><img src="https://image.ibb.co/cpuYoA/xsstrike-logo.png" alt="XSStrike"></a>
  <br>
  Bludger
  <br>
</h1>

<strong><p align="center">GitHub Actions at your fingertips!</p></strong>

<p align="center">
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.6+-green.svg?logo=python&style=flat-square">
  </a>
  <a href="https://twitter.com/0xInfection">
    <img src="https://img.shields.io/badge/Twitter-@0xInfection-blue.svg?logo=twitter&style=flat-square">
  </a>
  <a href="https://github.com/0xInfection/Bludger/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203%20Clause-orange.svg?logo=freebsd&style=flat-square">
  </a>
</p>
<br>
<p align="center">
  <img src="docs/images/bludger-intro.png" alt="intro" />
</p>

<p align="center">
  <a href="https://github.com/0xInfection/Bludger/wiki">Documentation</a> •
  <a href="https://github.com/0xInfection/Bludger/wiki/Usage">Usage</a> •
  <a href="#getting-started">Getting Started</a>
</p>

### About

Bludger is a GitHub Actions Automation Framework presented to you as a CLI! It leverages a powerful templating engine and the Actions REST API to perform various tasks. This enables you to make use the CI on a daily basis for heavy time-consuming tasks to game up your productivity to the next level.

Whether its parsing a dataset for research purposes or running a couple of custom scripts for your daily task, Bludger _simplifies_ everything. Its very similar to a "shell on the web", except the fact that you can easily spin up new instances/workflows with complete control over the target machine on which it is running.

### Main Features
Here are some features which it offers so far:
- [x] Powerful & extremely customisable templating engine.
- [x] Can handle automatic repository creation/cloning/deletion.
- [x] Allows you to automatically/manually create, trigger, delete or cancel workflows.
- [x] Downloading logs from a finished run.

### Getting Started
A few steps to get you quickly started
- Firstly, go ahead and [create a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) from your developer settings on GitHub. Make sure that `delete_repo`, `repo`, `user` and `workflow` scopes are checked!
- Get the toolkit.
```bash
git clone https://github.com/0xInfection/Bludger.git
cd Bludger/
```
- Put the access token in the `ACCESS_TOKEN` field in the [`config.py`](config.py) (line 7), so that it looks like:
```python
ACCESS_TOKEN = '29ab0cb8097087bca90890980980ab980bb00ac'
```
- Now you can go ahead and use it, here is the help output from the tool:
```bash
$ ./bludger.py -h

  Bludger - A GitHub Actions Automation Framework
               Version : v0.1.0

usage: ./bludger.py -n {repo_name} -A {token} [options]

Required Arguments:
  -n REPO, --new REPO   Creates a new repository with supplied name, invalid if -s is specified.
  -A TOKEN, --token TOKEN
                        GitHub personal access token to use, not required if already configured in `config.py`
  -s SLUG, --slug SLUG  Repository slug if you want to use an existing repository, invalid when -n is specified

Optional Arguments:
  -S LOGS, --save-logs LOGS
                        Destination path to save logs of the current workflow run.
  -T TEMPLATE, --template TEMPLATE
                        Configuration template to use for creating a workflow.
  -C COMMAND, --command COMMAND
                        Command to run for the specified template (if it accepts one).
  -P TOPUSH, --push TOPUSH
                        Commits and pushes a local changes to GitHub (must be present under custom/ folder).
  -D DELETE, --delete DELETE
                        Deletes something, it can be either a repository slug or a workflow template.
  -t TIMEOUT, --timeout TIMEOUT
                        HTTP timeout value in seconds (default: 5)
  -v, --verbose         Increase output verbosity, multiple -v increase verbosity
  --trigger TRIGGER     Can be used to manually trigger the workflow specified.
  --info                Display information about the tool and exit
  --no-monitor          Tells the program to not monitor the current workflow run.
  --public              Sets the visibility of a created repository as public. Valid only when -n is specified.
  --clone               Clones the repository to the current working directory.
  --cancel CANCEL       Cancels a workflow with the Run ID supplied.
  --debug               Enables debug mode & prints out HTTP API responses and headers.
```

See the [documentation] for more detailed usage of arguments and parameters. For usage examples, you can take a look at some use-cases documented within this repository. See [examples](docs/examples/).

### Contribution & License
A few ways to contribute:
- Suggest a feature
- Report a bug
- Open a pull request
- Spread the word

Bludger is licensed under the BSD 3-Clause License, see [LICENSE](LICENSE) for more information.

### Final Words
This tool was intended to make lives easier. Whether you are a guy who cannot afford a VPS to run a monitoring setup on, or someone who just wants to multitask on a wholly different level, this tool is for everyone. If you know what you're doing, an entirely new world of possibilities to level up your productivity waits ahead of you!

> Crafted with ❤️ by [@0xInfection](https://twitter.com/0xInfection)