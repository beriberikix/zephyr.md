---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/display/cfb/README.html
original_path: samples/subsys/display/cfb/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Character frame buffer

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
