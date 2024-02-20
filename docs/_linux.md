
## Table of Contents

- [ssh](#ssh)
    - [summary](#summary)
    - [required variables](#required-variables)
    - [variables](#variables)


## ssh

SSH into a server

#### Summary

SSH into a server
requires:
- HOST: The host to connect to
- USER: The user to connect as
- ARGS: [optional] Additional arguments to pass to the ssh command eg: "-i /path/to/key.pem"
- COMMAND: The command to run
#### Required Variables

- **HOST**
- **USER**
- **COMMAND**
#### Variables

- **ARGS**: `{{default "" .ARGS}}`


