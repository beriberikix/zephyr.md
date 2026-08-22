---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/boards/espressif/ulp/lp_core/interrupt_ulp/README.html
original_path: samples/boards/espressif/ulp/lp_core/interrupt_ulp/README.html
---

# Interrupt ULP

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/espressif/ulp/lp_core/interrupt_ulp/README.rst/..)

## Overview

This sample shows how to trigger LP Core interrupt from the HP core.

## Building and Flashing

Build the sample code as follows:

```shell
west build -b esp32c6_devkitc/esp32c6/hpcore --sysbuild samples/boards/espressif/ulp/lp_core/interrupt_ulp
```

Flash it to the device with the command:

```shell
west build -b esp32c6_devkitc/esp32c6/hpcore --sysbuild samples/boards/espressif/ulp/lp_core/interrupt_ulp
west flash
```

### Sample Output

Console output on the HP core:

```shell
Triggering ULP interrupt...
Triggering ULP interrupt...
Triggering ULP interrupt...
Triggering ULP interrupt...
Triggering ULP interrupt...
```

Console output on the LP core:

```shell
LP PMU interrupt received: 0
LP PMU interrupt received: 1
LP PMU interrupt received: 2
LP PMU interrupt received: 3
LP PMU interrupt received: 4
```
