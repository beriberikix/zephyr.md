---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/usb/device_next/usb_device.html
original_path: connectivity/usb/device_next/usb_device.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# New experimental USB device support

## Overview

The new USB device support is experimental. It consists of [USB device controller (UDC) driver API](api/udc.md#udc-api)
and [USB device stack (next) API](api/usbd.md#usbd-api). The new device stack brings support for multiple device
controllers, support for multiple configurations, and dynamic registration of
class instances to a configuration at runtime. The stack also provides a specific
class API that should be used to implement the functions (classes).
It will replace [USB device support](../device/usb_device.md#usb-device-stack).

If you would like to play around with the new device support, or the new USB
support in general, please try [USB shell](../../../samples/subsys/usb/shell/README.md#usb-shell "Use shell commands to interact with USB device stack.") sample. The sample is mainly to help
test the capabilities of the stack and correct implementation of the USB controller
drivers.

## Supported USB classes

### Bluetooth HCI USB transport layer

See [Bluetooth: HCI USB](../../../samples/bluetooth/hci_usb/README.md#bluetooth-hci-usb-sample) sample for reference.
To build the sample for the new device support, set the configuration
`-DCONF_FILE=usbd_next_prj.conf` either directly or via `west`.

### CDC ACM

CDC ACM implementation has support for multiple instances.
Description from [CDC ACM](../device/usb_device.md#usb-device-cdc-acm) also applies to the new implementation.
See [USB CDC-ACM](../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample for reference.
To build the sample for the new device support, set the configuration
`-DCONF_FILE=usbd_next_prj.conf` either directly or via `west`.

### Mass Storage Class

See [USB Mass Storage](../../../samples/subsys/usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.") sample for reference.
To build the sample for the new device support, set the configuration
`-DCONF_FILE=usbd_next_prj.conf` either directly or via `west`.

### Networking

At the moment only CDC ECM class is implemented and has support for multiple instances.
It provides a virtual Ethernet connection between the remote (USB host) and
Zephyr network support.

See [zperf: Network Traffic Generator](../../../samples/net/zperf/README.md#zperf "Use the zperf shell utility to evaluate network bandwidth.") for reference.
To build the sample for the new device support, set the configuration overlay file
`-DDEXTRA_CONF_FILE=overlay-usbd_next_ecm.conf` and devicetree overlay file
`-DDTC_OVERLAY_FILE="usbd_next_ecm.overlay` either directly or via `west`.
