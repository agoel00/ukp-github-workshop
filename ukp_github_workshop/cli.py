"""CLI interface for ukp_github_workshop project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import argparse
from ukp_github_workshop.fibonacci import Fibonacci
def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m ukp_github_workshop` and `$ ukp_github_workshop `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    ##### YOUR CODE HERE #####
    parser = argparse.ArgumentParser()
    parser.add_argument('n')
    args = parser.parse_args()
    obj = Fibonacci()
    print(f"The {args.n}-th Fibonacci number is {obj.fib(int(args.n))}")
    ##########################
