---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/kscan/README.html
original_path: samples/drivers/kscan/README.html
---

# KSCAN

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/kscan/README.rst/..)

## Overview

This sample demonstrates how to use the [KSCAN API](../../../hardware/peripherals/kscan.md#kscan-api).
Callbacks are registered that will write to the console indicating KSCAN events.
These events indicate key presses and releases.

## Building and Running

The sample can be built and executed on boards supporting a Keyboard Matrix.
It requires a correct fixture setup. Please connect a Keyboard Matrix to
exercise the functionality (you need to obtain the right keymap from the vendor
because they vary across different manufactures).
For the correct execution of that sample in twister, add into boards’s
map-file next fixture settings:

```text
- fixture: fixture_connect_keyboard
```

### Sample output

```shell
KSCAN test with a Keyboard matrix
Note: You are expected to see several callbacks
as you press and release keys!
```

## See also

[Keyboard Scan Driver APIs](../../../doxygen/html/group__kscan__interface.md)

[Timer APIs](../../../doxygen/html/group__timer__apis.md)
