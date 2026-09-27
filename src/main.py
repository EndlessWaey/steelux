import steelux.models
import steelux.utils
import argparse

def eval_dpi(dpi: list):
    '''Evaluate the provided DPI settings. TODO: Move this to utils.'''
    if len(dpi) > 5:
        print("ERROR: More than five DPI levels were provided.\n-> Please only specify up to 5 DPI levels.")
        return 1
    for level in dpi:
        if level % 100 != 0:
            print("ERROR: %d is not a valid DPI level\n-> HINT: DPI levels must be between 100 and 4600." % level)
            return 1
    
    return 0

def parse_args():
    '''Parse the CLI Arguments and options passed with SteeLux'''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dpi",
        type=int,
        nargs="+"
    )
    
    return parser.parse_args()

def main():
    
    # Find a mouse connected to the system.
    connected_mouse = steelux.utils.find_connected_mouse()

    # No supported mouse found. Exit.
    if connected_mouse is None:
        exit(1)

    mouse = steelux.models.Aerox9WL()
    mouse.connect()
    
    args = parse_args()

    if args.dpi:
        if eval_dpi(args.dpi) == 0:
            print("DPI settings are valid")
            mouse.set_dpi(dpi_settings=args.dpi)
        else:
            print("There were problems evaluating the DPI settings.")
            exit(1)
    
    # Close mouse in any event
    mouse.close()
    
if __name__ == "__main__":
    main()
    