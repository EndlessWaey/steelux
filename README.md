# Change the DPI levels on your Steel Series Aerox 9 WL! (On Linux)

That's pretty much it. This program will enable you to _finally_ change the DPI levels on your SteelSeries Aerox 9 WL gaming mouse. I created this primarily for myself, but thought that other people might also find this useful/interesting.

Please note that I'm not really a programmer. I dabble into programming here and there, but I'm nowhere near being adept at it, so don't expect high quality standards in code. Since I wanted this to be a learning experience, the code was created without the help of AI.

I'd be more than happy to make this a community project, so feel free to modify the code and propose changes.

# Usage

Clone the repo and create a virtual environment with pyusb installed. Also install "libusb" on your distro, which is what pyusb uses in the background. In addition, you will also require write-access to your mouse. I'm planning to make this a feature in the software going into the future, but for now you will have to manually "own" the mouse through shell commands. I've crafted the following one-liner which works rather decently:

```sh
sudo chown root:$USER $(lsusb | grep "1038:1858" | awk '{print "/dev/bus/usb/"$2"/"$4}' | sed 's/://g')
```

> "1038" and "1858" are the Vendor/Product IDs of the mouse respectively.

Finally, you may run "main.py" with the `--dpi` option and the desired DPI levels as arguments (Up to five). Please note: The highest DPI that is currently supported is 4000.

Example of setting the DPI:

```sh
python main.py --dpi 1200 1600 2000 2400
```

This will set 4 DPI Levels:

1. 1200 DPI
2. 1600 DPI
3. 2000 DPI
4. 2400 DPI

> I've only tested direct multiples of hundred up until now and tried to ensure that you can't in fact set anything that _is not a multiple of 100_. But again, I'm not a good programmer.

# Future plans

First and foremost, I want to make the program a bit more "silent" as it currently dumps A LOT of text to your terminal when executing. For debugging puposes, I will add an option for verbosity.

The code could also use some refactoring here and there. My primary concern was to get this runnning, not to make it particularly readable. This needs some changes, I am aware.

Add more functionalities. Rather obvious, but wouldn't it be nice to also query the battery status? I for one would love that, especially since the battery live on my particular model isn't anything to write home about to speak quite frankly. Afterwards, I would try to add options for changing the keybindings and lighting effects.

Oh, and of course I also want to document all the steps I took to create this project, maybe even with a video.