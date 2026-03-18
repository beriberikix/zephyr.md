---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/modules/lvgl/demos/README.html
original_path: samples/modules/lvgl/demos/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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

More details can be found in [LVGL demos Readme](https://github.com/zephyrproject-rtos/lvgl/blob/zephyr/demos/README.md).

## Requirements

- A board with display, ideally with 480x272 resolution or higher.
- A pointer input device: touchpad, mouse, or touch screen capable display, compatible with [`zephyr,lvgl-pointer-input`](../../../../build/dts/api/bindings/input/zephyr%2Clvgl-pointer-input.md#std-dtcompatible-zephyr-lvgl-pointer-input).

Note that other input devices types are not demonstrated in these demos, namely keyboards, keypads ([`zephyr,lvgl-keypad-input`](../../../../build/dts/api/bindings/input/zephyr%2Clvgl-keypad-input.md#std-dtcompatible-zephyr-lvgl-keypad-input)), rotary encoders ([`zephyr,lvgl-encoder-input`](../../../../build/dts/api/bindings/input/zephyr%2Clvgl-encoder-input.md#std-dtcompatible-zephyr-lvgl-encoder-input)) and hardware buttons ([`zephyr,lvgl-button-input`](../../../../build/dts/api/bindings/input/zephyr%2Clvgl-button-input.md#std-dtcompatible-zephyr-lvgl-button-input)).

## Building and Running

Example building for [NXP MIMXRT1060-EVK](../../../../boards/nxp/mimxrt1060_evk/doc/index.md#mimxrt1060-evk):

```shell
# From the root of the zephyr repository
west build -b mimxrt1060_evk samples/modules/lvgl/demos
west flash
```

These demos can be built for simulated display environment as follows:

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

Alternatively, if building from a 64-bit host machine, the previous target
board argument may also be replaced by `native_sim/native/64`.

## References
