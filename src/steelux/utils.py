import usb.core
from steelux.models import SUPPORTED_DEVICES, USBDeviceConfig

def find_connected_mouse() -> USBDeviceConfig | None: 
    '''Finds supported SteelSeries mice connected to the system'''
    for config in SUPPORTED_DEVICES:
        dev = usb.core.find(idVendor=config.vendor_id, idProduct=config.product_id)
        if dev is not None:
            print(f"Found connected device: {config.name}")
            return config
            
    print("No supported USB device found.")
    return None
