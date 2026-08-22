---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/samples/boards/espressif/ulp/lp_core/echo_ulp/README.html
original_path: samples/boards/espressif/ulp/lp_core/echo_ulp/README.html
---

# Echo ULP

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/espressif/ulp/lp_core/echo_ulp/README.rst/..)

## Overview

This sample application demonstrates how to use poll-based APIs from the Zephyr
UART driver subsystem. It reads characters from the LP UART using
[`uart_poll_in()`](../../../../../../doxygen/html/group__uart__polling.md#gae81ac8cc976a20d774cfbda09e9c983d) and echoes them back using [`uart_poll_out()`](../../../../../../doxygen/html/group__uart__polling.md#ga06ba27ba772a7a18462b8cdbc7f9353c).

## Building and Flashing

Build the sample code as follows:

```shell
west build -b esp32c6_devkitc/esp32c6/hpcore --sysbuild samples/boards/espressif/ulp/lp_core/echo_ulp
```

Flash it to the device with the command:

```shell
west build -b esp32c6_devkitc/esp32c6/hpcore --sysbuild samples/boards/espressif/ulp/lp_core/echo_ulp
west flash
```

### Sample Output

```shell
UART echo example started. Type something...
```
