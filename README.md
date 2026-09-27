# SteeLux

> **DISCLAIMER:** This project is neither affiliated with, nor endorsed by SteelSeries. I've created this project as an alternative to the native SteelSeries Software that is offered for Windows.

A software for configuring SteelSeries mice on Linux. 

**EARLY DEVELOPMENT NOTICE:** This project is still in _very early development_. However, I felt like there's no reason in keeping it all to myself until I am happy with it. There's always something to gain by getting feedback and aid early on I believe.

Got a SteelSeries Mouse but can't change a damn setting because you don't want to use up storage for MicroSlop Windows? I've been in a similar situation and so I started creating this piece of software, primarily to be able to change the five DPI levels on my SteelSeries mouse. Eventhough this feature is already implemented, I'm planning to do more yet: Lighting, button re-mapping, polling rate... you name it. Currently, only the SteelSeries Aerox 9 WL is supported, because that's the mouse I own myself. Supporting more devices will be a major community effort for which I will have to rely on help from fellow SteelSeries users. See the FAQ for how you may support the project!

# Supported devices

Since I only own one SteelSeries mouse, this list isn't really a list yet. But who knows in what ways it may grow one day?

| Name | Supported since (ver) | Contributor | Website |
| ---- | --- | --- | --- |
| SteelSeries Aeorx 9 WL | Development | EndlessWaey | [Link](https://steelseries.com/de-de/gaming-mice/aerox-9?color=black) |   

# Usage Example (Development only)

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

# FAQ

**Why does the code suck so much?**

The simple and truthful answer is that I'm not really programmer. I work in IT amd dabble into scripting here and there, but am more versed in maintaining infrastructure. This project is a learning experience for me, so I'm still learning! Also: You may always provide feedback or make your own modifications! I would appreciate it a lot.

**"I wish my mouse was also supported"**

I'd also like that. The more the merrier, so they say! Fortunately, the more traction this project gains, the higher the chance of people contributing information on their yet unsupported hardware. Feel free to open an Issue for a missing device, such as a mouse. Maybe someone has the required time and skills to work it out and make a contribution. Or maybe you could also try to work it out yourself and make your own contribution to the project?

**How did you get started with reverse engineering a USB mouse?**

I started out watching other people do it for different hardware on YouTube. Everyone approached it slightly differently and most of them also linked to external resources. When I stumbled over something I didn't understand (such as the clusterfuck that is the HID-Protocol), I would start my own research. One step at a time.

**Is support for other operating systems such as Windows or MacOS planned?**

No, at least not on my part. I'm definitely not against expanding support onto other operating systems, but my primary concern is support for Linux. If someone would like to bring support to another OS, they are more than free to do so by forking the project or creating a separate branch that could theoretically be merged one day. After all: It's Open-Source!

**"Ok cool, how can I contribute?"**

Thought you'd _never_ ask!

Everything goes, basically. In essence, **every one may contribute by:**

- **Improving the code:** Improve the overall quality of the code or simply propose changes / provide constructive feedback so I may implement it myself. I'm not a good programmer (yet) and wish to learn as much as possible from this project.
- **Provide USB-Dumps:** Having quality code is nice 'n everything, but it's of little use when the program only supports like 1-3 devices. If you own a device that's currently unsupported, please feel free to provide a USB-Dump that includes different configurations for the respective device. _A guide on how to create such a dump will follow in the future..._
- **Documentation:** The backbone of every IT-Project and dreaded by everyone. Personally, I like documenting stuff, but it depends on the type of documentation really. I get why some people feel it to be quite jarring at times.

# Future plans

- First and foremost, I want to make the program a bit more "silent" as it currently dumps A LOT of text to your terminal when executing. For debugging puposes, I will add an option for verbosity.
- The code could also use some refactoring here and there. My priary concern was to get this runnning, not to make it particularly readable. This needs some changes, I am aware.
- Add more functionalities. Rather obvious, but wouldn't it be nice to also query the battery status? I for one would love that, especially since the battery live on my particular model isn't anything to write home about to speak quite frankly. Afterwards, I would try to add options for changing the keybindings and lighting effects.
- Oh, and of course I also want to document all the steps I took to create this project, maybe even with a video.