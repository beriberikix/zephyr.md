---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/modules/lvgl/demos/README.html
original_path: samples/modules/lvgl/demos/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# LVGL demos

## Overview

A sample showcasing upstream LVGL demos.

- Music
  :   The music player demo shows what kind of modern, smartphone-like user interfaces can be created on LVGL.
- Benchmark
  :   The benchmark demo tests the performance in various cases. For example rectangle, border, shadow, text, image blending, image transformation, blending modes, etc.
- Stress
  :   A stress test for LVGL. It contains a lot of object creation, deletion, animations, styles usage, and so on. It can be used if there is any memory corruption during heavy usage or any memory leaks.
- Widgets
  :   Shows how the widgets look like out of the box using the built-in material theme.

## Requirements

- A board with display, ideally with 480x272 resolution or higher.

## Building and Running

These demos can be built as follows:

```shell
west build -b native_sim samples/modules/lvgl/demos -- -DCONFIG_LV_Z_DEMO_MUSIC=y
west build -t run
```

```shell
west build -b native_sim samples/modules/lvgl/demos -- -DCONFIG_LV_Z_DEMO_BENCHMARK=y
west build -t run
```

```shell
west build -b native_sim samples/modules/lvgl/demos -- -DCONFIG_LV_Z_DEMO_STRESS=y
west build -t run
```

```shell
west build -b native_sim samples/modules/lvgl/demos -- -DCONFIG_LV_Z_DEMO_WIDGETS=y
west build -t run
```
