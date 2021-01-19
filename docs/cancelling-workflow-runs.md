# Cancelling a workflow

Lets say a workflow is taking forever to complete, and you want to cancel it. It is simple. Just grab the Job ID from the output of the tool as soon it enters monitor mode.

Then:
```bash
./parasite.py -s {username}/{repository} --cancel {job_id}
```

> __NOTE:__ If you missed it, you can always head over to GitHub and manually cancel the workflow.