## Deleting a repository

Deleting a repository is very simple and straightforward (provided you have correctly setup the repositories).

Simply:
```bash
./parasite.py --delete {github_username}/{repository}
```
> __WARNING:__ The `--delete/-D` switch is very powerful and has capabilities to delete any repository, so please __USE WITH CAUTION__.

## Deleting a workflow

Deleting a workflow can be done by the same switch. Deleting a workflow is equivalent to deleting that workflow config from the `.github/workflows/` folder. The slug parameter is necessary for deleting a workflow.

Run:
```bash
./parasite.py -s {github_username}/{repository} --delete config.yml
```
Done!
