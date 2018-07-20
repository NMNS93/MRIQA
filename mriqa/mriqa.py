#!/usr/bin/env python3
"""
Wrapper script for MRI quality assurance modules.
"""
import argparse
import sys
import collections

from . import uniformity
from . import rename


def command_line_parser(args):
    """Parse command line arguments,
    Args:
        args - A list containing the command line string split by spaces.
    Returns:
        A tuple containing:
        opts - A tuple in the format (argparse.Namepsace, args_list), where argparse.Namespace is
            an object containing the MRI module. args_list contains the
            remaining command line arguments to be passed on to the relevant module script.
    """
    parser = argparse.ArgumentParser(description="Run MRI Quality Assurance Protocols")
    parser.add_argument("module", type=str, help="Select MRI QA module: rename, uniformity, all")
    return parser.parse_known_args(args), parser

def main(args=None):
    """
    Call the relevant MRI QA module with the given command line arguments.
        args - A list containing command line strings split by spaces, stored in sys.argv.
    """
    # Get command line arguments
    known_args, parser = command_line_parser(args)
    opts, args = known_args

    # Create a dictionary mapping the MRI QA module name with its .main function
    MODULES = collections.OrderedDict({"rename":rename.main, "uniformity": uniformity.main})

    # If command line module given is 'all'
    if opts.module == "all":
        # Run all MRI QA modules in the order displayed in MODULES. (Rename must come first).
        for module_main in MODULES.values():
            module_main(args)
    # Else if the module given is in MODULES and run as standalone
    elif opts.module in MODULES.keys():
        MODULES[opts.module](args)
    else:
        parser.print_help(sys.stderr)
        exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
