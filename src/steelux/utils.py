import usb.core
from steelux.mice import SUPPORTED_DEVICES, USBDeviceConfig

def find_connected_mouse() -> tuple[Optional[usb.core.Device], Optional[USBDeviceConfig]]: 
    '''Finds supported SteelSeries mice connected to the system'''
    for config in SUPPORTED_DEVICES:
        dev = usb.core.find(idVendor=config.vendor_id, idProduct=config.product_id)
        if dev is not None:
            print(f"Found connected device: {config.name}")
            return dev, config
            
    print("No supported USB device found.")
    return None, None
