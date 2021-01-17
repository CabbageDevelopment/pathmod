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
import time

import click

from pathmod import pathutils
from pathmod.cli import root


def add_options(options):
    def wrapper(func):
        for option in reversed(options):
            func = option(func)
        return func

    return wrapper


dry_run = click.option(
    "-d",
    "--dry-run",
    is_flag=True,
    help="Dry-run: only print the command which will be used",
)

system = click.option(
    "-s",
    "--system",
    is_flag=True,
    help="[Requires elevated shell] Modify the system PATH, rather than the user PATH",
)

force = click.option(
    "-f",
    "--force",
    is_flag=True,
    help="Proceed even if the location does not exist or is already on the PATH",
)


@root.command("add", help="Add (append) a location to the PATH")
@click.argument("location")
@add_options([dry_run, system, force])
def append(location: str, dry_run: bool, system: bool, force: bool):
    pathutils.modify_path(
        location,
        prepend=False,
        remove=False,
        dry_run=dry_run,
        system=system,
        force=force,
    )


@root.command("prepend", help="Prepend a location to the PATH")
@click.argument("location")
@add_options([dry_run, system, force])
def prepend(location: str, dry_run: bool, system: bool, force: bool):
    pathutils.modify_path(
        location,
        prepend=True,
        remove=False,
        dry_run=dry_run,
        system=system,
        force=force,
    )


@root.command("remove", help="Remove a location from the PATH")
@click.argument("location")
@add_options([dry_run, system])
def remove(location: str, dry_run: bool, system: bool):
    pathutils.modify_path(
        location,
        remove=True,
        system=system,
        prepend=False,
        force=False,
        dry_run=dry_run,
    )


@root.command("refresh", help="Refresh the PATH in the current session")
@click.option(
    "-g",
    "--generate",
    is_flag=True,
    help="Generate Powershell script to update the current session",
)
@click.option(
    "-q",
    "--quiet",
    is_flag=True,
    help="Only print the command needed to execute the Powershell script",
)
def refresh(generate: bool, quiet: bool):
    from pathmod import refresh

    if generate:
        refresh.generate(quiet=quiet)
    else:
        refresh.print_command()


@root.command("show", help="Show the current PATH")
def show():
    user = pathutils.get_current_path(user=True)
    system = pathutils.get_current_path(user=False)

    print()
    h = "-" * 70
    print(h)
    print(f"Path\t\tLocation")
    print(h, end="\n\n")

    for i in user:
        print(f"[user]   \t'{i}'")

    print()
    for i in system:
        print(f"[system]\t'{i}'")

    print()
