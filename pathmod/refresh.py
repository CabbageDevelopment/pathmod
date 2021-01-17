#  MIT License
#
#  Copyright (c) 2021 Sam McCormack
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
import os
import sys

sys_print = print


def print(*args, quiet=None, **kwargs):
    if not quiet:
        sys_print(*args, **kwargs)


def print_command(newline_before=True):
    if newline_before:
        print()

    print(
        f"To refresh the PATH in the current Powershell session, "
        f"run the command:\n\n"
        f"Invoke-Expression $(pathmod refresh -gq)",
        end="\n\n",
    )


def generate(quiet: bool):
    script_only = quiet
    print(
        f"Creating Powershell script to update the PATH in the current session...",
        quiet=script_only,
    )

    cmd = (
        f'$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + '
        f'[System.Environment]::GetEnvironmentVariable("Path","User")\n'
        f'Write-Output "Updated PATH in current session."\n'
        f"rm $PSCommandPath"
    )

    filename = "Update-Path.ps1"

    for i in range(2):
        try:
            if os.path.exists(filename):
                if script_only:
                    break

                print(f"Error: script already exists. Will not overwrite.")
                sys.exit(1)
            with open(filename, "w") as f:
                f.write(cmd)
                break
        except PermissionError:
            print(
                f"Don't have write permissions in '{os.getcwd()}', falling back to home directory.",
                quiet=script_only,
            )
            filename = os.path.join(os.path.expanduser("~"), filename)

    script_command = f".\\{os.path.relpath(filename)}"

    if not script_only:
        print(
            f"\nSelf-deleting Powershell script generated. "
            f"Execute the script with the command:\n\n{script_command}",
            end="\n\n",
        )
    else:
        print(script_command)
