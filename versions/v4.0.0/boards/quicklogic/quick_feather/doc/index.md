---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/quicklogic/quick_feather/doc/index.html
original_path: boards/quicklogic/quick_feather/doc/index.html
---

# QuickFeather

Board Overview

[![../../../../_images/feather-board.jpg](../../../../_images/feather-board.jpg)
](../../../../_images/feather-board.jpg)

QuickFeather

Vendor:
:   QuickLogic Corp.

Architecture:
:   arm

SoC:
:   quicklogic\_eos\_s3

## Overview

The QuickFeather development board is a platform with an on-board QuickLogic
EOS S3 Sensor Processing Platform.

## Hardware

- QuickLogic EOS S3 MCU Platform
- mCube MC3635 accelerometer
- Infineon DPS310 pressure sensor
- Infineon IM69D130 MEMS microphone
- 16 Mbit of on-board flash memory
- User button
- RGB LED
- Integrated battery charger

Detailed information about the board can be found in a [QuickFeather repository](https://github.com/QuickLogic-Corp/quick-feather-dev-board) [[1]](#id2).

### Supported Features

The QuickFeather configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |

The default configuration can be found in
[boards/quicklogic/quick\_feather/quick\_feather\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/quicklogic/quick_feather/quick_feather_defconfig).

### Connections and IOs

Detailed information about pinouts is available in the [schematics document](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/quickfeather-board.pdf) [[2]](#id4).

## Programming and Debugging

### Flashing

The QuickFeather platform by default boots from flash. Currently
the Zephyr port only enables loading the program directly to SRAM using either
OpenOCD and a SWD programmer or SEGGER JLink.

#### OpenOCD

In order to connect to the target a SWD programmer supported in
OpenOCD is needed. To connect to the board run:

```shell
openocd -f /path/to/swd-programmer.cfg -f tcl/board/quicklogic_quickfeather.cfg -c "init" -c "reset halt"
```

[The QuickFeather OpenOCD config](https://sourceforge.net/p/openocd/code/ci/master/tree/tcl/board/quicklogic_quickfeather.cfg) [[3]](#id6) can be found in the OpenOCD mainline repository.

#### JLink

To connect to the QuickFeather board with JLink please follow instructions
in the [QuickFeather User Guide](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/QuickFeather_UserGuide.pdf) [[4]](#id8).

### Debugging

To debug the QuickFeather board please connect to the target with either
OpenOCD or JLink and use GDB distributed in Zephyr’s SDK in *arm-zephyr-eabi/bin*
directory.

To load basic sample via GDB:

- Build the sample in an usual way:

```shell
# From the root of the zephyr repository
west build -b quick_feather samples/hello_world
```

- Connect to the target using either OpenOCD or JLink
- Connect via GDB and load an ELF file:

```shell
/path/to/zephyr-sdk/arm-zephyr-eabi/bin/arm-zephyr-eabi-gdb
target remote <port_number>
file </path/to/zephyr.elf>
load
continue
```

## References

[[1](#id3)]

[https://github.com/QuickLogic-Corp/quick-feather-dev-board](https://github.com/QuickLogic-Corp/quick-feather-dev-board)

[[2](#id5)]

[https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/quickfeather-board.pdf](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/quickfeather-board.pdf)

[[3](#id7)]

[https://sourceforge.net/p/openocd/code/ci/master/tree/tcl/board/quicklogic\_quickfeather.cfg](https://sourceforge.net/p/openocd/code/ci/master/tree/tcl/board/quicklogic_quickfeather.cfg)

[[4](#id9)]

[https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/QuickFeather\_UserGuide.pdf](https://github.com/QuickLogic-Corp/quick-feather-dev-board/blob/master/doc/QuickFeather_UserGuide.pdf)
