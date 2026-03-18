---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/display/cfb/README.html
original_path: samples/subsys/display/cfb/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Character frame buffer

## Overview

This sample displays character strings using the Character Frame Buffer
(CFB) subsystem framework.

## Requirements

This sample requires a supported board and CFB-supporting
display, such as the [reel board](../../../../boards/arm/reel_board/doc/index.md#reel-board).

## Building and Running

Build this sample application with the following commands:

```shell
west build -b reel_board samples/subsys/display/cfb
```

See [reel board](../../../../boards/arm/reel_board/doc/index.md#reel-board) on how to flash the build.
