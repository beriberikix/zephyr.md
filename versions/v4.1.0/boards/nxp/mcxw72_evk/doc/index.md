---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nxp/mcxw72_evk/doc/index.html
original_path: boards/nxp/mcxw72_evk/doc/index.html
---

# MCXW72-EVK

Board Overview

[![../../../../_images/mcxw72_evk.webp](../../../../_images/mcxw72_evk.webp)
](../../../../_images/mcxw72_evk.webp)

MCXW72-EVK

Name:
:   `mcxw72_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxw727c

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mcxw72_evk/doc/index.rst/../..)

## Overview

The MCXW72-EVK

The MCX W72x family features a 96 MHz Arm® Cortex®-M33 core coupled with a
multiprotocol radio subsystem supporting Matter, Thread, Zigbee and
Bluetooth LE. The independent radio subsystem, with a dedicated core and
memory, offloads the main CPU, preserving it for the primary application and
allowing firmware updates to support future wireless standards.

## Hardware

- MCXW72 Arm Cortex-M33 microcontroller running up to 96 MHz
- 2MB on-chip Flash memory unit
- 256 KB TCM RAM
- On-board MCU-Link debugger with CMSIS-DAP

For more information about the MCXW72 SoC and MCXW72-EVK board, see:

- [MCXW72 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w72x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W72X) [[1]](#id2)
- [MCXW72-EVK Website](#mcxw72-evk-website)

### Supported Features

The `mcxw72_evk` board in Zephyr currently supports the following features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| PINMUX | on-chip | pinctrl |
| GPIO | on-chip | gpio |
| LPUART | on-chip | serial port-polling; serial port-interrupt |
| TPM | on-chip | pwm |
| LPTMR | on-chip | counter |
| SPI | on-chip | spi |
| FLEXCAN | on-chip | can |
| ADC | on-chip | adc |
| I2C | on-chip | i2c |

## Fetch Binary Blobs

To support Bluetooth, mcxw72\_evk requires fetching binary blobs, which can be
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

#### Using LinkServer

Linkserver is the default runner for this board, and supports the factory
default MCU-Link firmware. Follow the instructions in
[MCU-Link CMSIS-DAP Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-cmsis-onboard-debug-probe) to reprogram the default MCU-Link
firmware. This only needs to be done if the default onboard debug circuit
firmware was changed. To put the board in `DFU mode` to program the firmware,
short jumper JP20.

#### Using J-Link

There are two options. The onboard debug circuit can be updated with Segger
J-Link firmware by following the instructions in
[MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
To be able to program the firmware, you need to put the board in `DFU mode`
by shortening the jumper JP20.
The second option is to attach a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) to the
10-pin SWD connector (J16) of the board.
For both options use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J14, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mcxw72_evk/mcxw727c/cpu0 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.7.0-xxx-xxxx ***
Hello World! mcxw72_evk/mcxw727c/cpu0
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mcxw72_evk/mcxw727c/cpu0 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.7.0-xxx-xxxx ***
Hello World! mcxw72_evk/mcxw727c/cpu0
```

### Bluetooth

BLE functionality requires to fetch binary blobs, so make sure to follow
the `Fetch Binary Blobs` section first.

Two images must be written to the board: one for the host (CM33 core0) and one for the NBU (CM33 core1).
- To flash the application (CM33) refer to the `Flashing` section above.
- To flash the NBU, follow the instructions below:

```shell
JLinkExe -device MCXW727C_CORE1 -if SWD -speed 4000 -autoconnect 1
J-Link>loadbin <path to nbu blob file> 0x0
```

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

[https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w72x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W72X](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-w-series-microcontrollers/mcx-w72x-secure-and-ultra-low-power-mcus-for-matter-thread-zigbee-and-bluetooth-le:MCX-W72X)
