---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/task_wdt/README.html
original_path: samples/subsys/task_wdt/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Task watchdog

## Overview

This sample allows to test the [task watchdog](../../../services/task_wdt/index.md#task-wdt-api) subsystem.

## Building and Running

It should be possible to build and run the task watchdog sample on almost any
board. If a hardware watchdog is defined in the devicetree, it is used as a
fallback. Otherwise the task watchdog will run independently.

### Building and Running for ST Nucleo L073RZ

The sample can be built and executed for the
[ST Nucleo L073RZ](../../../boards/arm/nucleo_l073rz/doc/index.md#nucleo-l073rz-board) as follows:

```shell
west build -b nucleo_l073rz samples/subsys/task_wdt
west flash
```

For other boards just replace the board name.

### Sample output

The following output is printed and continuously repeated (after each
reset):

```shell
Task watchdog sample application.
Main thread still alive...
Control thread started.
Main thread still alive...
Main thread still alive...
Main thread still alive...
Control thread getting stuck...
Main thread still alive...
Task watchdog channel 1 callback, thread: control
Resetting device...
```
