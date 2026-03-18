---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/nuvoton/numaker_pfm_m467/doc/index.html
original_path: boards/nuvoton/numaker_pfm_m467/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# NUVOTON NUMAKER PFM M467

## Overview

The NuMaker PFM M467 is an Internet of Things (IoT) application focused platform
specially developed by Nuvoton. The PFM-M467 is based on the NuMicro® M467
Ethernet series MCU with ARM® -Cortex®-M4F core.

[![PFM-M467](../../../../_images/pfm_m467.jpeg)](../../../../_images/pfm_m467.jpeg)

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

More information about the board can be found at the [PFM M467 User Manual](https://www.nuvoton.com/export/resource-files/UM_NuMaker-PFM-M467_User_Manual_EN_Rev1.01.pdf).

### Supported Features

- The on-board 12-MHz crystal allows the device to run at its maximum operating speed of 200MHz.

The development board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| SYSTICK | on-chip | system clock |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |

Other hardware features are not yet supported on Zephyr porting.

More details about the supported peripherals are available in [M460 TRM](https://www.nuvoton.com/export/resource-files/TRM_M460_Series_EN_Rev1.01.pdf)
Other hardware features are not currently supported by the Zephyr kernel.

## Building and Flashing

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

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

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b numaker_pfm_m467 samples/hello_world
west debug
```

Step through the application in your debugger.

## References
