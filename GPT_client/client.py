"""
Create ChatGPT serverr
"""
import sys

# Custom libraries
from default_library.utils import (validate_args)
from default_library.configuration import DataConfiguration
from resource.gui import gui

def main() -> int:
    """
    Run main function
    """
    # args = sys.argv
    args = ["", "LOCAL"]
    validate_args(args=args)
    environment = args[1].upper()
    config = DataConfiguration(environment=environment)
    gui.start(config)
    return 0
# End mian method


if __name__ == "__main__":
    result_code = main()
    SystemExit(result_code)