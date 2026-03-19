---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/usb/device_next/api/udc.html
original_path: connectivity/usb/device_next/api/udc.html
---

# USB device controller (UDC) driver API

The USB device controller driver API is described in
[include/zephyr/drivers/usb/udc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/usb/udc.h) and referred to
as the `UDC driver` API.

UDC driver API is experimental and is subject to change without notice.
It is a replacement for [USB device controller driver API](../../device/api/usb_dc.md#usb-dc-api). If you wish to port an existing
driver to UDC driver API, or add a new driver, please use
[drivers/usb/udc/udc\_skeleton.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/udc_skeleton.c) as a starting point.

## API reference

[USB device controller driver API](../../../../doxygen/html/group__udc__api.md)

[Buffer macros and definitions used in USB device support](../../../../doxygen/html/group__udc__buf.md)
