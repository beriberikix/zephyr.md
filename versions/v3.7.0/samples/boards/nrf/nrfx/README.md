---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/nrf/nrfx/README.html
original_path: samples/boards/nrf/nrfx/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nrfx use example

## Overview

This sample demonstrates the usage of nrfx library in Zephyr.
GPIOTE and DPPI/PPI are used as examples of nrfx drivers.

The code shows how to initialize the GPIOTE interrupt in Zephyr
so that the nrfx\_gpiote driver can use it. Additionally, it shows
how the DPPI/PPI subsystem can be used to connect tasks and events of
nRF peripherals, enabling those peripherals to interact with each
other without any intervention from the CPU.

Zephyr GPIO driver is disabled to prevent it from registering its own handler
for the GPIOTE interrupt. Button 1 is configured to create an event when pushed.
This calls the `button_handler()` callback and triggers the LED 1 pin OUT task.
LED is then toggled.

Please note that no debouncing mechanism is used for the button, so it may
happen that one press results in multiple events. And because the event-task
connection is handled in hardware, for very fast coming events, toggling of
the LED may sometimes be even unnoticeable.

## Requirements

This sample has been tested on the NordicSemiconductor nRF9160 DK
(nrf9160dk/nrf9160) and nRF52840 DK (nrf52840dk/nrf52840) boards.

## Building and Running

The code can be found in [samples/boards/nrf/nrfx](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/boards/nrf/nrfx).

To build and flash the application:

```shell
west build -b nrf9160dk/nrf9160 samples/boards/nrf/nrfx
west flash
```

Push Button 1 to toggle the LED 1.

Connect to the serial port - notice that each time the button is pressed,
the `button_handler()` function is called.

See [nrfx\_repository](https://github.com/NordicSemiconductor/nrfx) for more information about nrfx.
