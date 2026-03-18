---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/basic/threads/README.html
original_path: samples/basic/threads/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Basic thread manipulation

## Overview

This example demonstrates spawning multiple threads using
[`K_THREAD_DEFINE()`](../../../kernel/services/threads/index.md#c.K_THREAD_DEFINE "K_THREAD_DEFINE"). It spawns three threads. Each thread is then defined
at compile time using K\_THREAD\_DEFINE.

The first two each control an LED. These LEDs, `led0` and `led1`, have
loop control and timing logic controlled by separate functions.

- `blink0()` controls `led0` and has a 100ms sleep cycle
- `blink1()` controls `led1` and has a 1000ms sleep cycle

When either of these threads toggles its LED, it also pushes information into a
[FIFO](../../../kernel/services/data_passing/fifos.md#fifos-v2) identifying the thread/LED and how many times it has
been toggled.

The third thread uses `printk()` to print the information added to the
FIFO to the device console.

## Requirements

The board must have two LEDs connected via GPIO pins. These are called “User
LEDs” on many of Zephyr’s [Supported Boards](../../../boards/index.md#boards). The LEDs must be configured using the
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
