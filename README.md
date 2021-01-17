# pathmod

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/pathmod?color=brightgreen)](https://pypi.org/project/pathmod)

## Introduction

`pathmod` is a CLI program which allows you to easily modify the PATH using the terminal on Windows. `pathmod` can persistently modify the PATH, and provides an easy way to refresh the path in the current session. 

## Requirements

You need to have Python 3.6 or higher installed. This will allow you to install `pathmod` with Python's package manager, `pip`. 

## How to install 

To install `pathmod` with `pip`:

```bash
pip install pathmod
```

After this command completes, the `pathmod` executable should be available on the PATH.

# Quick start

## User vs system PATHs

By default, `pathmod` modifies the user PATH, which does not require elevated permissions. You can use the `-s`/`--system` flag to modify the system PATH instead.

## Add

`add` is used to add an item to the PATH. 

You can use relative paths, and paths using tilde (`~`):

```powershell
# Add the current working directory to the PATH.
>> pathmod add .

# Add 'C:\Users\%USERNAME%\scripts' to the PATH.
>> pathmod add ~/scripts
```

Absolute file paths are also valid:

```powershell
>> pathmod add "C:\Program Files\my program"
```

## Prepend

`prepend` is used to prepend an item to the PATH. THis may be useful if you require items in your newly added location to be prioritised over items of the same name in other locations.

```powershell
>> pathmod prepend . 
```

## Remove

`pathmod remove` is used to remove an item from the PATH.

```powershell
>> pathmod remove .
```

As with `add` and `prepend`, this defaults to modifying the user PATH. To remove an item from the system PATH, ensure you use the `-s`/`--system` flag:

```powershell
>> pathmod remove . -s
```

## Show

`show` is used to show the items currently on the user and system PATHS. This prints the persistent values - the values which will be present in a new session - rather than the values in the current session. 

```powershell
>> pathmod show

----------------------------------------------------------------------
Path            Location
----------------------------------------------------------------------

[user]          'C:\Users\username\AppData\Local\Programs\Python\Python39\Scripts\'
[user]          'C:\Users\username\AppData\Local\Programs\Python\Python39\'
...

[system]        'C:\Windows\system32'
[system]        'C:\Windows'
...
```

## Refresh

`refresh` allows you to update the PATH in the current session. This is especially useful in terminals such as the Windows Terminal, where you would need to open a new terminal instance and be unable to migrate your tabs.

Updating the PATH directly from `pathmod` is not possible because `pathmod` cannot modify the environment of its parent process; however, a relatively easy workaround is to run the command:

```powershell
Invoke-Expression $(pathmod refresh -gq)
```

This will update the PATH in your current session so that it is equivalent to the PATH which would be used in a new session.

## Help

You can use the `--help` flag to show help info. This also works for subcommands.

# License

You may freely use, modify and redistribute this program under the terms of the MIT License. See [LICENSE](https://github.com/CabbageDevelopment/pathmod/blob/master/LICENSE).