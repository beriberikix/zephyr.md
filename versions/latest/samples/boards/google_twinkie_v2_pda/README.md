---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/boards/google_twinkie_v2_pda/README.html
original_path: samples/boards/google_twinkie_v2_pda/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Twinkie Power Delivery

## Overview

This provides access to [Twinkie](../../../boards/arm/google_twinkie_v2/doc/index.md#google-twinkie-v2-board) so you can try out
the supported features.

## Building and Running

Build and flash Twinkie as follows:

```shell
west build -b google_twinkie_v2 samples/boards/google_pda
west flash
```

After flashing, the LED will start red. Putting the Twinkie in between any
usbc connection will cause the LED to turn blue. The LED will turn green instead
if the device is currently charging.
