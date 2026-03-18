---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/watchdog/README.html
original_path: samples/drivers/watchdog/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Watchdog

## Overview

This sample demonstrates how to use the watchdog driver API.

A typical use case for a watchdog is that the board is restarted in case some piece of code
is kept in an infinite loop.

## Building and Running

In this sample, a watchdog callback is used to handle a timeout event once. This functionality is used to request an action before the board
restarts due to a timeout event in the watchdog driver.

The watchdog peripheral is configured in the board’s `.dts` file. Make sure that the watchdog is enabled
using the configuration file in `boards` folder.

### Building and Running for ST Nucleo F091RC

The sample can be built and executed for the
[ST Nucleo F091RC](../../../boards/arm/nucleo_f091rc/doc/index.md#nucleo-f091rc-board) as follows:

```shell
west build -b nucleo_f091rc samples/drivers/watchdog
west flash
```

To build for another board, change “nucleo\_f091rc” to the name of that board and provide a corresponding devicetree overlay.

### Sample output

You should get a similar output as below:

```shell
Watchdog sample application
Attempting to test pre-reset callback
Feeding watchdog 5 times
Feeding watchdog...
Feeding watchdog...
Feeding watchdog...
Feeding watchdog...
Feeding watchdog...
Waiting for reset...
Handled things..ready to reset
```

Note

After the last message, the board will reset and the sequence will start again
