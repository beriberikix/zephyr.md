---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/input/draw_touch_events/README.html
original_path: samples/subsys/input/draw_touch_events/README.html
---

# Draw touch events

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/input/draw_touch_events/README.rst/..)

## Overview

This sample will draw a small plus in the last touched coordinates, that way you can check
if the touch screen works for a board, examine its parameters such as inverted/swapped axes.

## Building and Running

While this is a generic sample and it should work with any boards with both display controllers
and touch controllers supported by Zephyr (provided the corresponding `/chosen node` properties
are set i.e. `zephyr,touch` and `zephyr,display`).
Below is an example on how to build the sample for [STM32F746G Discovery](../../../../boards/st/stm32f746g_disco/doc/index.md#stm32f746g_disco):

```shell
west build -b stm32f746g_disco samples/subsys/input/draw_touch_events
```

For testing purposes without the need of any hardware, the [native\_sim](../../../../boards/native/native_sim/doc/index.md#native-sim)
board is also supported and can be built as follows:

```shell
west build -b native_sim samples/subsys/input/draw_touch_events
```

## See also

[Input Event Definitions](../../../../doxygen/html/group__input__events.md)

[Display Interface](../../../../doxygen/html/group__display__interface.md)
