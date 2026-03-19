---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/modules/lvgl/screen_transparency/README.html
original_path: samples/modules/lvgl/screen_transparency/README.html
---

# LVGL screen transparency

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/modules/lvgl/screen_transparency/README.rst/..)

## Overview

A sample application that demonstrates how to use LVGL to render to
screens that support transparency, like OSD overlays.

## Requirements

- A board with a display that supports `ARGB8888` color.

## Building and Running

The demo can be built as follows:

```shell
west build -b native_sim samples/modules/lvgl/screen_transparency
west build -t run
```

## See also

[Display Interface](../../../../doxygen/html/group__display__interface.md)
