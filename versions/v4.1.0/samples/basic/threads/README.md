---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/basic/threads/README.html
original_path: samples/basic/threads/README.html
---

# Basic thread manipulation

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/basic/threads/README.rst/..)

## Overview

This example demonstrates spawning multiple threads using
[`K_THREAD_DEFINE()`](../../../doxygen/html/group__thread__apis.md#gab3ced58648ca35788a40676e8478ecd2). It spawns three threads. Each thread is then defined
at compile time using K\_THREAD\_DEFINE.

The first two each control an LED. These LEDs, `led0` and `led1`, have
loop control and timing logic controlled by separate functions.

- `blink0()` controls `led0` and has a 100ms sleep cycle
- `blink1()` controls `led1` and has a 1000ms sleep cycle

When either of these threads toggles its LED, it also pushes information into a
[FIFO](../../../kernel/services/data_passing/fifos.md#fifos-v2) identifying the thread/LED and how many times it has
been toggled.

The third thread uses [`printk()`](../../../doxygen/html/printk_8h.md#a768a7dff8592b69f327a08f96b00fa54) to print the information added to the
FIFO to the device console.

## Requirements

The board must have two LEDs connected via GPIO pins. These are called “User
LEDs” on many of Zephyr’s [Supported Boards and Shields](../../../boards/index.md#boards). The LEDs must be configured using the
`led0` and `led1` [devicetree](../../../build/dts/index.md#dt-guide) aliases, usually in the
[BOARD.dts file](../../../build/dts/intro-input-output.md#devicetree-in-out-files).

You will see one of these errors if you try to build this sample for an
unsupported board:

```text
Unsupported board: led0 devicetree alias is not defined
Unsupported board: led1 devicetree alias is not defined
```

## Building

For example, to build this sample for [96Boards Carbon](../../../boards/96boards/carbon/doc/stm32f401xe.md#b-carbon-board):

```shell
west build -b 96b_carbon/stm32f401xe samples/basic/threads
west flash
```

Change `96b_carbon/stm32f401xe` appropriately for other supported boards.

## See also

[GPIO Driver APIs](../../../doxygen/html/group__gpio__interface.md)

[Thread APIs](../../../doxygen/html/group__thread__apis.md)
