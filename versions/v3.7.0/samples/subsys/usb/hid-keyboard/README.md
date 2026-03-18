---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/usb/hid-keyboard/README.html
original_path: samples/subsys/usb/hid-keyboard/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# USB HID keyboard

## Overview

This sample application demonstrates the HID keyboard implementation using the
new experimental USB device stack.

## Requirements

This project requires an experimental USB device driver (UDC API) and uses the
[Input](../../../../services/input/index.md#input) API. There must be a [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) group of buttons
or keys defined at the board level that can generate input events.
At least one key is required and up to four can be used. The first three keys
are used for Num Lock, Caps Lock and Scroll Lock. The fourth key is used to
report HID keys 1, 2, 3 and the right Alt modifier at once.

The example can use up to three LEDs, configured via the devicetree alias such
as `led0`, to indicate the state of the keyboard LEDs.

## Building and Running

This sample can be built for multiple boards, in this example we will build it
for the nRF52840DK board:

```shell
west build -b nrf52840dk/nrf52840 samples/subsys/usb/hid-keyboard
west flash
```
