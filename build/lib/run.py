import steelux.mice
import steelux.utils
import argparse

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
    
    args = parse_args()
    
    # Find a mouse connected to the system and retrieve handle & config
    mouse_handle, mouse_config  = steelux.utils.find_connected_mouse()

    # No supported mouse found. Exit.
    if mouse_handle is None and mouse_config is None:
        exit(1)

    # TODO: Should everything be handled inside of the object, or initiated from main?
    mouse = steelux.mice.SteelSeriesMouse(
        config=mouse_config,
        handle=mouse_handle,
        cli_args=args
    )

    # Enter "main loop" (It's not a loop, ik...)
    if args.dpi:
        mouse.set_dpi(dpi_list=args.dpi)
    
    # Close mouse in any event
    mouse.close()
    
if __name__ == "__main__":
    main()