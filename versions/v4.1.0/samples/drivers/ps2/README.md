---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/ps2/README.html
original_path: samples/drivers/ps2/README.html
---

# PS/2 interface

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/ps2/README.rst/..)

## Overview

This sample demonstrates how to use the [PS/2 API](../../../hardware/peripherals/ps2.md#ps2-api).
Callbacks are registered that will write to the console indicating PS2 events.
These events indicate mouse configuration responses and mouse interaction.

## Building and Running

The sample can be built and executed on boards supporting PS/2.
It requires a correct fixture setup. Please connect a PS/2 mouse in order to
exercise the functionality.
For the correct execution of that sample in twister, add into boards’s
map-file next fixture settings:

```text
- fixture: fixture_connect_mouse
```

### Sample output

```shell
PS/2 test with mouse
Note: You are expected to see several interrupts
as you configure/move the mouse!
```

## See also

[PS/2 Driver APIs](../../../doxygen/html/group__ps2__interface.md)
