---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/modules/lvgl/multi_display/README.html
original_path: samples/modules/lvgl/multi_display/README.html
---

# LVGL Multi-display

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/modules/lvgl/multi_display/README.rst/..)

## Overview

A sample showcasing LVGL multi-display support in Zephyr.

By default, it runs the Music demo on the first display, and the Widgets demo on the other ones
(order as defined in the “displays” property of “zephyr,displays” compatible node in deviceTree).
Which demos are run can be changed by modifying the value of CONFIG\_LV\_Z\_DEMO\_FIRST\_DISP## and
CONFIG\_LV\_Z\_DEMO\_OTHER\_DISPS## Kconfig symbols.

- Music
  :   The music player demo shows what kind of modern, smartphone-like user interfaces can be
      created on LVGL.
- Benchmark
  :   The benchmark demo tests the performance in various cases. For example rectangle, border,
      shadow, text, image blending, image transformation, blending modes, etc.
- Stress
  :   A stress test for LVGL. It contains a lot of object creation, deletion, animations, styles
      usage, and so on. It can be used if there is any memory corruption during heavy usage or any
      memory leaks.
- Widgets
  :   Shows how the widgets look like out of the box using the built-in material theme.

More details on the demos can be found in [LVGL demos Readme](https://github.com/zephyrproject-rtos/lvgl/blob/zephyr/demos/README.md) [[1]](#id1).

## Requirements

- A board with two displays or more, ideally with 480x272 resolution or higher.

## Building and Running

This sample can be built for simulated display environment on Linux as follows:

```shell
west build -b native_sim/native/64 samples/modules/lvgl/multi_display
west build -t run
```

## References

[[1](#id2)]

[https://github.com/zephyrproject-rtos/lvgl/blob/zephyr/demos/README.md](https://github.com/zephyrproject-rtos/lvgl/blob/zephyr/demos/README.md)

## See also

[Display Interface](../../../../doxygen/html/group__display__interface.md)
