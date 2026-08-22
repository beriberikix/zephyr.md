---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nuvoton/numaker_m55m1/doc/index.html
original_path: boards/nuvoton/numaker_m55m1/doc/index.html
---

# NUMAKER M55M1

Board Overview

[![../../../../_images/m55m1.webp](../../../../_images/m55m1.webp)
](../../../../_images/m55m1.webp)

NUMAKER M55M1

Name:
:   `numaker_m55m1`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   m55m1xxx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/numaker_m55m1/doc/index.rst/../..)

## Overview

The NuMaker M55M1 is an Internet of Things (IoT) application focused platform
specially developed by Nuvoton. The NuMaker-M55M1 is based on the NuMicro® M55M1
series MCU with ARM® -Cortex®-M55 core.

### Features

- 32-bit Arm Cortex®-M55 M55M1H2LJAE MCU
- Core clock up to 220 MHz
- 2 MB embedded Dual Bank Flash and 1344 KB SRAM
- 128 KB DTCM and 64 KB ITCM
- USB 2.0 Full-Speed OTG / Device
- USB 1.1 Host
- Arduino UNO compatible interface
- One push-button is for reset
- Two LEDs: one is for power indication and the other is for user-defined
- On-board NU-Link2 ICE debugger/programmer with SWD connector

More information about the board can be found at the [NuMaker M55M1 User Manual](https://www.nuvoton.com/products/microcontrollers/arm-cortex-m55-mcus/m55m1-series/) [[1]](#id2).

### Supported Features

The `numaker_m55m1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

The on-board 12-MHz crystal allows the device to run at its maximum operating speed of 220 MHz.

More details about the supported peripherals are available in [M55M1 TRM](https://www.nuvoton.com/products/microcontrollers/arm-cortex-m55-mcus/m55m1-series/) [[1]](#id2)

## Building and Flashing

The `numaker_m55m1` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

On board debugger Nu-link2 can emulate UART0 as a virtual COM port over usb,
To enable this, set ISW1 DIP switch 1-3 (TXD RXD VOM) to ON.
Connect the NuMaker-M55M1 to your host computer using the USB port, then
run a serial host program to connect with your board. For example:

```shell
$ minicom -D /dev/ttyACM0
```

```shell
# From the root of the zephyr repository
west build -b numaker_m55m1 samples/hello_world
west flash
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b numaker_m55m1 samples/hello_world
west debug
```

Step through the application in your debugger.

## References

[1]
([1](#id3),[2](#id4))

[https://www.nuvoton.com/products/microcontrollers/arm-cortex-m55-mcus/m55m1-series/](https://www.nuvoton.com/products/microcontrollers/arm-cortex-m55-mcus/m55m1-series/)
