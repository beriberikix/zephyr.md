---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/usb/device/api/usb_device.html
original_path: connectivity/usb/device/api/usb_device.html
---

# USB device stack API

## API reference

There are two ways to transmit data, using the ‘low’ level read/write API or
the ‘high’ level transfer API.

Low level API
:   To transmit data to the host, the class driver should call usb\_write().
    Upon completion the registered endpoint callback will be called. Before
    sending another packet the class driver should wait for the completion of
    the previous write. When data is received, the registered endpoint callback
    is called. usb\_read() should be used for retrieving the received data.
    For CDC ACM sample driver this happens via the OUT bulk endpoint handler
    (cdc\_acm\_bulk\_out) mentioned in the endpoint array (cdc\_acm\_ep\_data).

High level API
:   The usb\_transfer method can be used to transfer data to/from the host. The
    transfer API will automatically split the data transmission into one or more
    USB transaction(s), depending endpoint max packet size. The class driver does
    not have to implement endpoint callback and should set this callback to the
    generic usb\_transfer\_ep\_callback.

[USB Device Core API](../../../../doxygen/html/group____usb__device__core__api.md)

Related code samples

- [Console over USB CDC ACM](../../../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.")Output "Hello World!" to the console over USB CDC ACM.
- [HCI H4 over USB](../../../../samples/bluetooth/hci_usb_h4/README.md#bluetooth_hci_usb_h4 "Turn a Zephyr board into a USB H4 Bluetooth dongle (Linux/BlueZ only).")Turn a Zephyr board into a USB H4 Bluetooth dongle (Linux/BlueZ only).
- [HCI USB](../../../../samples/bluetooth/hci_usb/README.md#bluetooth_hci_usb "Turn a Zephyr board into a USB Bluetooth dongle (compatible with all operating systems).")Turn a Zephyr board into a USB Bluetooth dongle (compatible with all operating systems).
- [USB Audio headset](../../../../samples/subsys/usb/audio/headset/README.md#usb-audio-headset "Implement a USB Audio headset device with audio IN/OUT loopback.")Implement a USB Audio headset device with audio IN/OUT loopback.
- [USB Audio microphone & headphones](../../../../samples/subsys/usb/audio/headphones_microphone/README.md#usb-audio-headphones-microphone "Implement a USB Audio microphone + headphones device with audio IN/OUT loopback.")Implement a USB Audio microphone + headphones device with audio IN/OUT loopback.
- [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.")Use USB CDC-ACM driver to implement a serial port echo.
- [USB DFU (Device Firmware Upgrade)](../../../../samples/subsys/usb/dfu/README.md#usb-dfu "Implement device firmware upgrade using the USB DFU class driver.")Implement device firmware upgrade using the USB DFU class driver.
- [USB HID mouse](../../../../samples/subsys/usb/hid-mouse/README.md#usb-hid-mouse "Implement a basic HID mouse device.")Implement a basic HID mouse device.
- [USB Mass Storage](../../../../samples/subsys/usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.")Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.
- [USB testing application](../../../../samples/subsys/usb/testusb/README.md#testusb-app "Test USB device drivers using a loopback function.")Test USB device drivers using a loopback function.
- [WebUSB](../../../../samples/subsys/usb/webusb/README.md#webusb "Receive and echo data from a web page using WebUSB API.")Receive and echo data from a web page using WebUSB API.
