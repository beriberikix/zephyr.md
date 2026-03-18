---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/display/cfb_custom_font/README.html
original_path: samples/subsys/display/cfb_custom_font/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Custom fonts

## Overview

A simple example showing how to generate Character Framebuffer (CFB)
font headers automatically at build time.

This example generates a font with font elements for 6 sided dice from
a PNG image, and then uses the generated header (`cfb_font_dice.h`)
to show the font elements on the display of a supported board.

The source code for this sample application can be found at:
[samples/subsys/display/cfb\_custom\_font](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/display/cfb_custom_font).

## Building and Running

There are different configuration files in the cfb\_custom\_font
directory:

- `prj.conf`
  Generic config file, normally you should use this.
- `boards/reel_board.conf`
  This overlay config enables support for SSD16XX display controller
  on the reel\_board.

Example building for the reel\_board with SSD16XX display support:

```shell
west build -b reel_board samples/subsys/display/cfb_custom_font
west flash
```
