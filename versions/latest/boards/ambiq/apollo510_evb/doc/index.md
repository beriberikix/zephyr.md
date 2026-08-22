---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ambiq/apollo510_evb/doc/index.html
original_path: boards/ambiq/apollo510_evb/doc/index.html
---

# Apollo510 SOC Evaluation Board

Board Overview

[![../../../../_images/apollo510-soc-eval-board.jpg](../../../../_images/apollo510-soc-eval-board.jpg)
](../../../../_images/apollo510-soc-eval-board.jpg)

Apollo510 SOC Evaluation Board

Name:
:   `apollo510_evb`

Vendor:
:   Ambiq Micro, Inc.

Architecture:
:   arm

SoC:
:   apollo510

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ambiq/apollo510_evb/doc/index.rst/../..)

Apollo510 EVB is a board by Ambiq featuring their ultra-low power Apollo510 SoC.

## Hardware

- Apollo510 SoC with up to 250 MHz operating frequency
- ARM® Cortex® M55 core
- 64 kB Instruction Cache and 64 kB Data Cache
- Up to 4 MB of non-volatile memory (NVM) for code/data
- Up to 3 MB of low leakage / low power RAM for code/data
- 256 kB Instruction Tightly Coupled RAM (ITCM)
- 512 kB Data Tightly Coupled RAM (DTCM)

For more information about the Apollo510 SoC and Apollo510 EVB board:

- [Apollo510 Website](https://ambiq.com/apollo510/)
- [Apollo510 Datasheet](https://contentportal.ambiq.com/documents/20123/2877485/Apollo510-SoC-Datasheet.pdf)
- [Apollo510 EVB Website](Formoreinformation,pleasereachouttoSalesandFAE.)

### Supported Features

The `apollo510_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Programming and Debugging

The `apollo510_evb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

#### Flashing an application

Connect your device to your host computer using the JLINK USB port.
The sample application [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application, then flash it to the device:

```shell
# From the root of the zephyr repository
west build -b apollo510_evb samples/hello_world
west flash
```

Note

`west flash` requires [SEGGER J-Link software](https://www.segger.com/downloads/jlink) and [pylink](https://github.com/Square/pylink) Python module
to be installed on you host computer.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should be able to see on the corresponding Serial Port
the following message:

```shell
Hello World! apollo510_evb
```
