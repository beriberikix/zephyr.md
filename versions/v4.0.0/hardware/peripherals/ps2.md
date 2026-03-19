---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/ps2.html
original_path: hardware/peripherals/ps2.html
---

# PS/2

## Overview

The PS/2 connector first hit the market in 1987 on
IBM’s desktop PC line of the same name before
becoming an industry-wide standard for mouse and
keyboard connections. Starting around 2007, USB
superseded PS/2 and is the modern peripheral device
connection standard. For legacy support on boards
with a PS/2 connector, Zephyr provides these PS/2 driver APIs.

## Configuration Options

Related configuration options:

- [`CONFIG_PS2`](../../kconfig.md#CONFIG_PS2 "CONFIG_PS2")

## API Reference

[PS/2 Driver APIs](../../doxygen/html/group__ps2__interface.md)

Related code samples

- [PS/2 interface](../../samples/drivers/ps2/README.md#ps2 "Communicate with a PS/2 mouse.")Communicate with a PS/2 mouse.
