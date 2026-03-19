---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ambiq/apollo3p_evb/doc/index.html
original_path: boards/ambiq/apollo3p_evb/doc/index.html
---

# Apollo3 Blue Plus EVB

Board Overview

[![../../../../_images/apollo3-blue-plus-soc-eval-board.jpg](../../../../_images/apollo3-blue-plus-soc-eval-board.jpg)
](../../../../_images/apollo3-blue-plus-soc-eval-board.jpg)

Apollo3 Blue Plus EVB

Name:
:   `apollo3p_evb`

Vendor:
:   Ambiq Micro, Inc.

Architecture:
:   arm

SoC:
:   apollo3p\_blue

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ambiq/apollo3p_evb/doc/index.rst/../..)

Apollo3 Blue Plus EVB is a board by Ambiq featuring their ultra-low power Apollo3 Blue Plus SoC.

## Hardware

- Apollo3 Blue Plus SoC with up to 96 MHz operating frequency
- ARM® Cortex® M4F core
- 16 kB 2-way Associative/Direct-Mapped Cache per core
- Up to 2 MB of flash memory for code/data
- Up to 768 KB of low leakage / low power RAM for code/data
- Integrated Bluetooth 5 Low-energy controller

For more information about the Apollo3 Blue Plus SoC and Apollo3 Blue Plus EVB board:

- [Apollo3 Blue Plus Website](https://ambiq.com/apollo3-blue-plus/)
- [Apollo3 Blue Plus Datasheet](https://contentportal.ambiq.com/documents/20123/388390/Apollo3-Blue-Plus-SoC-Datasheet.pdf)
- [Apollo3 Blue Plus EVB Website](https://www.ambiq.top/en/apollo3-blue-plus-soc-eval-board)

### Supported Features

The `apollo3p_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Programming and Debugging

#### Flashing an application

Connect your device to your host computer using the JLINK USB port.
The sample application [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application, then flash it to the device:

```shell
# From the root of the zephyr repository
west build -b apollo3p_evb samples/hello_world
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
Hello World! apollo3p_evb
```
