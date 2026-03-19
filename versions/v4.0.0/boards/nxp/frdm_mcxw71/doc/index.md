---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/nxp/frdm_mcxw71/doc/index.html
original_path: boards/nxp/frdm_mcxw71/doc/index.html
---

# FRDM-MCXW71

Board Overview

[![../../../../_images/frdm_mcxw71.webp](../../../../_images/frdm_mcxw71.webp)
](../../../../_images/frdm_mcxw71.webp)

FRDM-MCXW71

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxw716c

## Overview

The FRDM-MCXW71 is a compact and scalable development board for rapid
prototyping of the MCX W71 wireless MCU. It offers easy evaluation of the MCX
W71’s multiprotocol wireless support for Bluetooth LE, Zigbee, Thread and
Matter. The board includes an on-board MCU-Link debugger, industry standard
headers for easy access to the MCU’s I/Os, an accelerometer, a light sensor and
external SPI flash memory.

The MCX W71x family features a 96 MHz Arm® Cortex®-M33 core coupled with a
multiprotocol radio subsystem supporting Matter, Thread, Zigbee and Bluetooth
LE. The independent radio subsystem, with a dedicated core and memory, offloads
the main CPU, preserving it for the primary application and allowing firmware
updates to support future wireless standards.

## Hardware

- MCXW71 Arm Cortex-M33 microcontroller running up to 96 MHz
- 1MB on-chip Flash memory unit
- 128 KB TCM RAM
- On-board MCU-Link debugger with CMSIS-DAP

For more information about the MCXW71 SoC and FRDM-MCXW71 board, see:

- [MCXW71 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w71x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W71X) [[1]](#id2)
- [FRDM-MCXW71 Website](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-w71x-wireless-mcus:FRDM-MCXW71) [[2]](#id4)

### Supported Features

The `frdm_mcxw71` board target in Zephyr currently supports the following features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| PINMUX | on-chip | pinctrl |
| GPIO | on-chip | gpio |
| LPUART | on-chip | serial port-polling; serial port-interrupt |
| LPI2C | on-chip | i2c |
| LPSPI | on-chip | spi |
| FMU | on-chip | flash |
| TPM | on-chip | pwm |
| WDOG32 | on-chip | watchdog |
| LPTMR | on-chip | counter |
| BLE | on-chip | Bluetooth |
| FLEXCAN | on-chip | can |
| VREF | on-chip | regulator |
| LPADC | on-chip | adc |

## Fetch Binary Blobs

To support Bluetooth, frdm\_mcxw71 requires fetching binary blobs, which can be
achieved by running the following command:

```shell
west blobs fetch hal_nxp
```

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the MCU-Link CMSIS-DAP Onboard Debug Probe.

#### Using J-Link

There are two options. The onboard debug circuit can be updated with Segger
J-Link firmware by following the instructions in
[MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
To be able to program the firmware, you need to put the board in `DFU mode`
by shortening the jumper JP5.
The second option is to attach a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) to the
10-pin SWD connector (J12) of the board.
For both options use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J10, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxw71/mcxw716c samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.7.0-xxx-xxxx ***
Hello World! frdm_mcxw71/mcxw716c
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxw71/mcxw716c samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.7.0-xxx-xxxx ***
Hello World! frdm_mcxw71/mcxw716c
```

### Bluetooth

BLE functionality requires to fetch binary blobs, so make sure to follow
the `Fetch Binary Blobs` section first.

Two images must be written to the board: one for the host (CM33) and one for the NBU (CM3).
- To flash the application (CM33) refer to the `Flashing` section above.
- To flash the NBU, follow the instructions below:

> - Install `blhost` from NXP’s website. This is the tool that will allow you to flash the NBU.
> - Enter ISP mode. To boot the MCU in ISP mode, follow these steps:
>   :   - Disconnect the `FRDM-MCXW71` board from all power sources.
>       - Keep the `SW3` (ISP) button on the board pressed, while connecting the board to the host computer USB port.
>       - Release the `SW3` (ISP) button. The MCXW71 MCU boots in ISP mode.
>       - Reconnect any external power supply, if needed.
> - Use the following command to flash NBU file:

```shell
# On Windows
blhost.exe -p COMxx -- receive-sb-file mcxw71_nbu_ble.sb3

# On Linux
./blhost -p /dev/ttyxx -- receive-sb-file mcxw71_nbu_ble.sb3
```

Please consider changing `COMxx` on Windows or `ttyxx` on Linux to the serial port used by your board.

The NBU file can be found in : `<zephyr workspace>/modules/hal/nxp/zephyr/blobs/mcxw71/mcxw71_nbu_ble.sb3`

For more details:

### Troubleshooting

#### Using Segger SystemView and RTT

Note that when using SEGGER SystemView or RTT with this SOC, the RTT control
block address must be set manually within SystemView or the RTT Viewer. The
address provided to the tool should be the location of the `_SEGGER_RTT`
symbol, which can be found using a debugger or by examining the `zephyr.map`
file output by the linker.

The RTT control block address must be provided manually because this SOC
supports ECC RAM. If the SEGGER tooling searches the ECC RAM space for the
control block a fault will occur, provided that ECC is enabled and the RAM
segment being searched has not been initialized to a known value.

## References

[[1](#id3)]

[https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w71x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W71X](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w71x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W71X)

[[2](#id5)]

[https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-w71x-wireless-mcus:FRDM-MCXW71](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-w71x-wireless-mcus:FRDM-MCXW71)
