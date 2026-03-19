---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/debug/debugmon/README.html
original_path: samples/subsys/debug/debugmon/README.html
---

# Debug Monitor

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/debug/debugmon/README.rst/..)

## Overview

The Debug Monitor sample shows a basic configuration of debug monitor feature.

The source code shows how to:

1. Configure registers to enable degugging in debug monitor mode
2. Specify custom interrupt to be executed when entering a breakpoint

## Requirements

Your board must:

1. Support Debug Monitor feature (available on Cortex-M processors with the exception of Cortex-M0)
2. Have an LED connected via a GPIO pin (these are called “User LEDs” on many of
   Zephyr’s [Supported Boards and Shields](../../../../boards/index.md#boards)).
3. Have the LED configured using the `led0` devicetree alias.

## Building and Running

Build and flash Debug Monitor as follows, changing `reel_board` for your board:

```shell
west build -b reel_board samples/subsys/debug/debugmon
west flash
```

After flashing the board enters a breakpoint and executes debug monitor exception code.
The LED starts to blink, indicating that even though the processor spins in debug monitor
interrupt, other higher priority interrupts continue to execute.
