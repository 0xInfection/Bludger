# Writing new templates

To level up your productivity, you should write your custom templates for your daily usage. Before going ahead, make sure you understand the basic syntax of writing GitHub Actions config files in YAML. If not, refer to the [docs](https://docs.github.com/en/free-pro-team@latest/rest/reference/actions).

Once you're comfortable, lets go ahead.

### Points:
- Wherever you mention `{command}`, you are specifying to replace that portion with your custom command which is to be specified via the `-C/--command` switch.
- You should always have the `workflow_dispatch` trigger switch in your YML file, because the tool triggers the workflow always upon manual switch.
- `{command}` can be put only in one place in your YAML file, but can accept multiple commands separated by `&&` or `;` through the `-C` switch.
- If you're planning to run the scripts daily, you should probably setup a cron.
- Make sure the template you're making has a unique name.