---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/ps2/README.html
original_path: samples/drivers/ps2/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# PS/2 interface

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
