---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/subsys/display/cfb/README.html
original_path: samples/subsys/display/cfb/README.html
---

# Character frame buffer

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/display/cfb/README.rst/..)

## Overview

This sample displays character strings using the Character Frame Buffer
(CFB) subsystem framework.

## Requirements

This sample requires a supported board and CFB-supporting
display, such as the [reel board](../../../../boards/phytec/reel_board/doc/index.md#reel-board).

## Building and Running

Build this sample application with the following commands:

```shell
west build -b reel_board samples/subsys/display/cfb
```

See [reel board](../../../../boards/phytec/reel_board/doc/index.md#reel-board) on how to flash the build.

## See also

[Monochrome Character Framebuffer](../../../../doxygen/html/group__monochrome__character__framebuffer.md)
