import steelseries.models
import argparse

def eval_dpi(dpi: list):
    if len(dpi) > 5:
        print("ERROR: More than five DPI levels were provided.\n-> Please only specify up to 5 DPI levels.")
        return 1
    for level in dpi:
        if level % 100 != 0:
            print("ERROR: %d is not a valid DPI level\n-> HINT: DPI levels must be between 100 and 4600." % level)
            return 1
    
    return 0

def main():
    mouse = steelseries.models.aerox9wl()
    mouse.connect()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dpi",
        type=int,
        nargs="+"
    )
    
    args = parser.parse_args()

    if args.dpi:
        if eval_dpi(args.dpi) == 0:
            print("DPI settings are valid")
        else:
            print("There were problems evaluating the DPI settings.")
            exit(1)
    
    mouse.set_dpi(dpi_settings=args.dpi)
    mouse.close()
    
if __name__ == "__main__":
    main()
    