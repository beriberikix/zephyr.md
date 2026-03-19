---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/mbox_data/README.html
original_path: samples/drivers/mbox_data/README.html
---

# MBOX Data

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/mbox_data/README.rst/..)

## Overview

This sample demonstrates how to use the [MBOX API](../../../hardware/peripherals/mbox.md#mbox-api) in data transfer mode.
It can be used only with mbox driver which supports data transfer mode.

Sample will ping-pong up to 4 bytes of data between two cores via two mbox channels.
After each core receives data, it increments it by one and sends it back to other core.

## Building and Running

The sample can be built and executed on boards supporting MBOX with data transfer mode.

### Building the application for mimxrt1160\_evk\_cm7

```shell
# From the root of the zephyr repository
west build -b mimxrt1160_evk_cm7 --sysbuild samples/drivers/mbox_data/
west debug
```

### Building the application for mimxrt1170\_evk\_cm7

```shell
# From the root of the zephyr repository
west build -b mimxrt1170_evk_cm7 --sysbuild samples/drivers/mbox_data/
west debug
```

### Building the application for mimxrt1170\_evkb\_cm7

```shell
# From the root of the zephyr repository
west build -b mimxrt1170_evkb_cm7 --sysbuild samples/drivers/mbox_data/
west debug
```

### Building the application for lpcxpresso55s69\_cpu1

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s69_cpu1 --sysbuild samples/drivers/mbox_data/
west debug
```

### Sample Output

Open a serial terminal (minicom, putty, etc.) and connect the board with the
following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and the following message will appear on the corresponding
serial port, one is the main core another is the remote core:

```shell
*** Booting Zephyr OS build zephyr-v3.5.0-4051-g12f4f4dc8679 ***
mbox_data Client demo started
Client send (on channel 3) value: 0
Client received (on channel 2) value: 1
Client send (on channel 3) value: 2
Client received (on channel 2) value: 3
Client send (on channel 3) value: 4
...
Client received (on channel 2) value: 95
Client send (on channel 3) value: 96
Client received (on channel 2) value: 97
Client send (on channel 3) value: 98
Client received (on channel 2) value: 99
mbox_data Client demo ended
```

```shell
*** Booting Zephyr OS build zephyr-v3.5.0-4051-g12f4f4dc8679 ***
mbox_data Server demo started
Server receive (on channel 3) value: 0
Server send (on channel 2) value: 1
Server receive (on channel 3) value: 2
Server send (on channel 2) value: 3
Server receive (on channel 3) value: 4
...
Server send (on channel 2) value: 95
Server receive (on channel 3) value: 96
Server send (on channel 2) value: 97
Server receive (on channel 3) value: 98
Server send (on channel 2) value: 99
mbox_data Server demo ended.
```

## See also

[MBOX Interface](../../../doxygen/html/group__mbox__interface.md)
