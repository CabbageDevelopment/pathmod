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
from argparse import ArgumentParser

argparser = ArgumentParser()

argparser.add_argument(
    "path",
    nargs="*",
    help="The path to add to the PATH",
)
argparser.add_argument(
    "-d",
    "--dry-run",
    action="store_true",
    help="Print the command which would be run, but don't execute it",
)
argparser.add_argument(
    "-s",
    "--system",
    action="store_true",
    help="Whether to add to the system PATH; requires elevated permissions in your shell",
)
argparser.add_argument(
    "-p",
    "--prepend",
    action="store_true",
    help="Prepend the new item to the PATH, instead of appending. This ensures that files in the newly added location "
    "have priority over those in other locations on the PATH",
)
argparser.add_argument(
    "-r",
    "--remove",
    action="store_true",
    help="Remove an item from the path",
)
argparser.add_argument(
    "-f",
    "--force",
    action="store_true",
    help="Add to the PATH, even if the location does not exist or is already added to the PATH",
)
argparser.add_argument(
    "--show",
    action="store_true",
    help="Show the items on the PATH",
)
argparser.add_argument(
    "-g",
    "--generate-script",
    action="store_true",
    help="Generate a Powershell script which updates the PATH in the current session",
)
argparser.add_argument(
    "-pso",
    "--print-script-only",
    action="store_true",
    help="Only print the command required to run the Powershell "
    "script generated with the '--generate-script' parameter",
)

args = argparser.parse_args()
