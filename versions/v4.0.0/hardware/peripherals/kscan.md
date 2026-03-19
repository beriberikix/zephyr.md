---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/kscan.html
original_path: hardware/peripherals/kscan.html
---

# Keyboard Scan

Note

Kscan APIs are deprecated, any driver and applications should be
ported over to use [Input](../../services/input/index.md#input) instead.

## Overview

The kscan driver (keyboard scan matrix) is used for detecting a key press in a
connected matrix keyboard or any device with buttons such as joysticks.
Typically, matrix keyboards are implemented using a two-dimensional
configuration in order to sense several keys. This allows interfacing to
many keys through fewer physical pins. Keyboard matrix
drivers read the rows while applying power through the columns one at a time
with the purpose of detecting key events.
There is no correlation between the physical and electrical layout of keys.
For, example, the physical layout may be one array of 16 or fewer keys, which
may be electrically connected to a 4 x 4 array. In addition, key values are
defined by a keymap provided by the keyboard manufacturer.

## Configuration Options

Related configuration options:

- [`CONFIG_KSCAN`](../../kconfig.md#CONFIG_KSCAN "CONFIG_KSCAN")

## API Reference

[Keyboard Scan Driver APIs](../../doxygen/html/group__kscan__interface.md)

Related code samples

- [HT16K33 LED driver with keyscan](../../samples/drivers/ht16k33/README.md#ht16k33 "Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.")Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.
- [KSCAN](../../samples/drivers/kscan/README.md#kscan "Use the KSCAN API to read key presses and releases on a keyboard matrix.")Use the KSCAN API to read key presses and releases on a keyboard matrix.
