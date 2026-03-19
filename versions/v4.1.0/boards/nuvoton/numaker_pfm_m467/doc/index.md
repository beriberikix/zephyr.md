---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nuvoton/numaker_pfm_m467/doc/index.html
original_path: boards/nuvoton/numaker_pfm_m467/doc/index.html
---

# NUMAKER PFM M467

Board Overview

[![../../../../_images/pfm_m467.jpeg](../../../../_images/pfm_m467.jpeg)
](../../../../_images/pfm_m467.jpeg)

NUMAKER PFM M467

Name:
:   `numaker_pfm_m467`

Vendor:
:   Nuvoton Technology Corporation

Architecture:
:   arm

SoC:
:   m467

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nuvoton/numaker_pfm_m467/doc/index.rst/../..)

## Overview

The NuMaker PFM M467 is an Internet of Things (IoT) application focused platform
specially developed by Nuvoton. The PFM-M467 is based on the NuMicro® M467
Ethernet series MCU with ARM® -Cortex®-M4F core.

### Features:

- 32-bit Arm Cortex®-M4 M467HJHAE MCU
- Core clock up to 200 MHz
- 1024 KB embedded Dual Bank Flash and 512 KB SRAM
- Ethernet (IP101GR) for network application
- USB 2.0 High-Speed OTG / Host / Device
- USB 1.1 Full-Speed OTG / Host / Device
- External SPI Flash (Winbond W25Q20) which can be regarded as ROM module
- MicroSD Card slot for T-Flash
- Arduino UNO compatible interface
- Three push-buttons: one is for reset and the other two are for user-defined
- Four LEDs: one is for power indication and the other three are for user-defined
- On-board NU-Link2 ICE debugger/programmer with SWD connector

More information about the board can be found at the [PFM M467 User Manual](https://www.nuvoton.com/export/resource-files/UM_NuMaker-PFM-M467_User_Manual_EN_Rev1.01.pdf) [[1]](#id2).

### Supported Features

The `numaker_pfm_m467` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

The on-board 12-MHz crystal allows the device to run at its maximum operating speed of 200MHz.

More details about the supported peripherals are available in [M460 TRM](https://www.nuvoton.com/export/resource-files/TRM_M460_Series_EN_Rev1.01.pdf) [[2]](#id4)

## Building and Flashing

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

On board debugger Nu-link2 can emulate UART0 as a virtual COM port over usb,
To enable this, set ISW1 DIP switch 1-3 (TXD RXD VOM) to ON.
Connect the PFM M467 IoT to your host computer using the USB port, then
run a serial host program to connect with your board. For example:

```shell
$ minicom -D /dev/ttyACM0
```

```shell
# From the root of the zephyr repository
west build -b numaker_pfm_m467 samples/hello_world
west flash
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b numaker_pfm_m467 samples/hello_world
west debug
```

Step through the application in your debugger.

## References

[[1](#id3)]

[https://www.nuvoton.com/export/resource-files/UM\_NuMaker-PFM-M467\_User\_Manual\_EN\_Rev1.01.pdf](https://www.nuvoton.com/export/resource-files/UM_NuMaker-PFM-M467_User_Manual_EN_Rev1.01.pdf)

[[2](#id5)]

[https://www.nuvoton.com/export/resource-files/TRM\_M460\_Series\_EN\_Rev1.01.pdf](https://www.nuvoton.com/export/resource-files/TRM_M460_Series_EN_Rev1.01.pdf)
