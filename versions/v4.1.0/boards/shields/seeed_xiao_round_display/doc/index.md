---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/seeed_xiao_round_display/doc/index.html
original_path: boards/shields/seeed_xiao_round_display/doc/index.html
---

# Seeed Studio XIAO Round Display

## Overview

Seeed Studio Round Display for XIAO is an expansion board compatible with all
XIAO development boards. It features a fully covered touch screen on one side,
designed as a 39mm disc. It contains onboard RTC, charge chip, TF card slot
within its compact size, perfect for interactive displays in smart home,
wearables and more.

More information can be found on [the Getting Started page](https://wiki.seeedstudio.com/get_start_round_display/)

![Seeed Studio XIAO Round Display](../../../../_images/seeed_xiao_round_display.webp)

Seeed Studio XIAO Round Display (Credit: Seeed Studio)

## Programming

Set `--shield seeed_xiao_round_display` when you invoke `west build`.

### LVGL Basic Sample

For example:

```shell
# From the root of the zephyr repository
west build -b xiao_ble/nrf52840 --shield seeed_xiao_round_display samples/subsys/display/lvgl
```
