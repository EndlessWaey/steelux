import time
import usb.core
import usb.util

class aerox9wl(object):

    def __init__(self):
        self.dev = None
        self.PID = 0x1858
        self.VID = 0x1038
        self.DPI_INTERFACE = 3

    def close(self):
        '''Close the handle to the usb device'''
        if self.dev:
            cfg = self.dev[0]

            for intf in cfg:
                print("Reattaching kernel driver for %d" % intf.bInterfaceNumber)
                ret = self.dev.attach_kernel_driver(intf.bInterfaceNumber)
                if ret is None:
                    print("\tSuccessfully reattached Linux Kernel Driver")
    
    def connect(self):
        '''Finds and connects to the mouse'''
        try:
            self.dev = usb.core.find(idVendor=self.VID, idProduct=self.PID)
            if self.dev is None:
                print("Couldn't find device")
                exit(1)
            else:
                print("Device Found: \n\tVendor:  %X\n\tProduct: %X" % (self.dev.idVendor, self.dev.idProduct) )
        except USBerror as e:
            print(e)
            exit(1)

    def _release_from_kernel(self):
        '''Releases all interfaces that are currently claimed by Linix Kernel Drivers'''
        cfg = self.dev[0]
        print("Releasing all interfaces currently claimed by a kernel driver...")

        for intf in cfg:
            if self.dev.is_kernel_driver_active(intf.bInterfaceNumber):
                print("Interface %d is claimed" % intf.bInterfaceNumber )
                print("\tAttempting to release interface")
                ret = self.dev.detach_kernel_driver(intf.bInterfaceNumber)
                if ret is None:
                    print("\tSuccessfully released the interface")

    def _claim_interface(self, interface: int):
        '''Claims an interface on the device'''
        usb.util.claim_interface(self.dev, interface)
    
    def _release_interface(self, interface: int):
        '''Releases a claimed interface'''
        usb.util.release_interface(self.dev, interface)

    def set_dpi(self, dpi_settings: list):
        '''Sets the DPI on the mouse'''

        dpi_settings.sort()

        for i, val in enumerate(dpi_settings):
            val = int(val / 100)
            if val == 1:
                val-=1
            elif  8 <= val <= 13:
                val+=1
            elif 14 <= val <= 18:
                val+=2
            elif 19 <= val <= 24:
                val+=3
            elif 25 <= val <= 29:
                val+=4
            elif val == 30:
                val+=5
            elif 31 <= val <= 36:
                val+=6
            elif 37 <= val <= 41: 
                val+=7
            elif 42 <= val <= 46:
                val+=8
            val = format(val, '02x')
            dpi_settings[i] = val


        len_orig = format(len(dpi_settings), '02x')

        if len(dpi_settings) < 5:
            
            dpi_settings_delta = 5 - len(dpi_settings)
            print("Less than 5 DPI levels specified, filling up remaining space with zeros...")
            
            while dpi_settings_delta != 0:
                dpi_settings.append('00')
                dpi_settings_delta-=1
            
        
        dpi_string = ''.join(dpi_settings)
        
        print(f"Prepared the following DPI values: {dpi_string}")
        
        self._release_from_kernel()
        self._claim_interface(interface=self.DPI_INTERFACE)
        
        bmRequestType = 0x21
        bRequest      = 0x09
        report_type   = 0x02
        report_id     = 0x00
        wValue        = 0x0200
        wIndex        = self.DPI_INTERFACE
        payload       = bytes.fromhex("6d" + len_orig + "00" + dpi_string + "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        
        try:
            print("Trying to send DPI payload")
            bytes_sent = self.dev.ctrl_transfer(
                bmRequestType=bmRequestType,
                bRequest=bRequest,
                wValue=wValue,
                wIndex=wIndex,
                data_or_wLength=payload
            )
            print(f"Successfully sent {bytes_sent} bytes.")
        except usb.core.USBError as e:
            print(f"Control Transfer failed: {e}")
        
        payload = bytes.fromhex("51000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        
        try:
            bytes_sent = self.dev.ctrl_transfer(
                bmRequestType=bmRequestType,
                bRequest=bRequest,
                wValue=wValue,
                wIndex=wIndex,
                data_or_wLength=payload
            )
            print(f"Successfully sent {bytes_sent} bytes.")
        except usb.core.USBError as e:
            print(f"Control Transfer failed: {e}")
        finally:
            self._release_interface(interface=self.DPI_INTERFACE)
            print("Released DPI Interface %d" % self.DPI_INTERFACE)
            