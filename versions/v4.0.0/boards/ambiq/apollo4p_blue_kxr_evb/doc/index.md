---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/ambiq/apollo4p_blue_kxr_evb/doc/index.html
original_path: boards/ambiq/apollo4p_blue_kxr_evb/doc/index.html
---

# Apollo4 Blue Plus KXR EVB

Board Overview

[![../../../../_images/apollo4-blue-plus-kxr-soc-eval-board.jpg](../../../../_images/apollo4-blue-plus-kxr-soc-eval-board.jpg)
](../../../../_images/apollo4-blue-plus-kxr-soc-eval-board.jpg)

Apollo4 Blue Plus KXR EVB

Vendor:
:   Ambiq Micro, Inc.

Architecture:
:   arm

SoC:
:   apollo4p\_blue

Apollo4 Blue Plus KXR EVB is a board by Ambiq featuring their ultra-low power Apollo4 Blue Plus SoC.

## Hardware

- Apollo4 Blue Plus SoC with upto 192 MHz operating frequency
- ARM® Cortex® M4F core
- 64 kB 2-way Associative/Direct-Mapped Cache per core
- Up to 2 MB of non-volatile memory (NVM) for code/data
- Up to 2.75 MB of low leakage / low power RAM for code/data
- 384 kB Tightly Coupled RAM
- 384 kB Extended RAM
- Bluetooth 5.1 Low Energy

For more information about the Apollo4 Blue Plus SoC and Apollo4 Blue Plus KXR EVB board:

- [Apollo4 Blue Plus Website](https://ambiq.com/apollo4-blue-plus/)
- [Apollo4 Blue Plus Datasheet](https://contentportal.ambiq.com/documents/20123/388410/Apollo4-Blue-Plus-SoC-Datasheet.pdf)
- [Apollo4 Blue Plus KXR EVB Website](https://www.ambiq.top/en/apollo4-blue-plus-kxr-soc-eval-board)

### Supported Features

The Apollo4 Blue Plus KXR EVB board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| MPU | on-chip | memory protection unit |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| STIMER | on-chip | stimer |
| GPIO | on-chip | gpio |
| UART | on-chip | serial |
| WDT | on-chip | watchdog |
| SPI(M) | on-chip | spi |
| I2C(M) | on-chip | i2c |
| CLOCK | on-chip | clock\_control |
| RADIO | on-chip | bluetooth |

The default configuration can be found in
[boards/ambiq/apollo4p\_blue\_kxr\_evb/apollo4p\_blue\_kxr\_evb\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ambiq/apollo4p_blue_kxr_evb/apollo4p_blue_kxr_evb_defconfig)

### Programming and Debugging

#### Flashing an application

Connect your device to your host computer using the JLINK USB port.
The sample application [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application, then flash it to the device:

```shell
# From the root of the zephyr repository
west build -b apollo4p_blue_kxr_evb samples/hello_world
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
Hello World! apollo4p_blue_kxr_evb
```
