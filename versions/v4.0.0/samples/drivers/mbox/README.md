---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/mbox/README.html
original_path: samples/drivers/mbox/README.html
---

# MBOX

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/mbox/README.rst/..)

## Overview

This sample demonstrates how to use the [MBOX API](../../../hardware/peripherals/mbox.md#mbox-api).

## Building and Running

The sample can be built and executed on boards supporting MBOX.

## Building the application for nrf5340dk/nrf5340/cpuapp

```shell
# From the root of the zephyr repository
west build -b nrf5340dk/nrf5340/cpuapp --sysbuild samples/drivers/mbox/
west debug
```

Open a serial terminal (minicom, putty, etc.) and connect the board with the
following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and the following message will appear on the corresponding
serial port, one is the application (APP) core another is the network (NET)
core:

```shell
*** Booting Zephyr OS build zephyr-v3.1.0-2383-g147aee22f273  ***
Hello from APP
Pong (on channel 0)
Ping (on channel 1)
Pong (on channel 0)
Ping (on channel 1)
Ping (on channel 1)
Pong (on channel 0)
Ping (on channel 1)
Pong (on channel 0)
Ping (on channel 1)
...
```

```shell
*** Booting Zephyr OS build zephyr-v3.1.0-2383-g147aee22f273  ***
Hello from NET
Ping (on channel 0)
Pong (on channel 1)
Ping (on channel 0)
Pong (on channel 1)
```

## Building the application for the simulated nrf5340bsim

```shell
# From the root of the zephyr repository
west build -b nrf5340bsim/nrf5340/cpuapp --sysbuild samples/drivers/mbox/
```

Then you can execute your application using:

```shell
$ ./build/zephyr/zephyr.exe -nosim
# Press Ctrl+C to exit
```

You can expect a similar output as in the real HW in the invoking console.

## See also

[MBOX Interface](../../../doxygen/html/group__mbox__interface.md)
