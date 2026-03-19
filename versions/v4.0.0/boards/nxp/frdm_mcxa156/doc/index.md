---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/nxp/frdm_mcxa156/doc/index.html
original_path: boards/nxp/frdm_mcxa156/doc/index.html
---

# FRDM-MCXA156

Board Overview

[![../../../../_images/frdm_mcxa156.webp](../../../../_images/frdm_mcxa156.webp)
](../../../../_images/frdm_mcxa156.webp)

FRDM-MCXA156

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxa156

## Overview

FRDM-MCXA156 are compact and scalable development boards for rapid prototyping of
MCX A15X MCUs. They offer industry standard headers for easy access to the
MCUs I/Os, integrated open-standard serial interfaces, external flash memory and
an on-board MCU-Link debugger. MCX N Series are high-performance, low-power
microcontrollers with intelligent peripherals and accelerators providing multi-tasking
capabilities and performance efficiency.

## Hardware

- MCX-A156 Arm Cortex-M33 microcontroller running at 96 MHz
- 1MB dual-bank on chip Flash
- 128 KB RAM
- USB high-speed (Host/Device) with on-chip HS PHY. HS USB Type-C connectors
- 2x FlexCAN with FD, 2x I3Cs, 2x SAI
- On-board MCU-Link debugger with CMSIS-DAP
- Arduino Header, FlexIO/LCD Header, SmartDMA/Camera Header, mikroBUS

For more information about the MCX-A156 SoC and FRDM-MCXA156 board, see:

- [MCX-A156 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-a-series-microcontrollers/mcx-a13x-14x-15x-mcus-with-arm-cortex-m33-scalable-device-options-low-power-and-intelligent-peripherals:MCX-A13X-A14X-A15X)
- [MCX-A156 Datasheet](https://www.nxp.com/docs/en/data-sheet/MCXAP100M96FS6.pdf)
- [MCX-A156 Reference Manual](https://www.nxp.com/webapp/Download?colCode=MCXAP100M96FS6RM)
- [FRDM-MCXA156 Website](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-a144-5-6-a154-5-6-mcus:FRDM-MCXA156)
- [FRDM-MCXA156 User Guide](https://www.nxp.com/document/guide/getting-started-with-frdm-mcxa156:GS-FRDM-MCXA156)
- [FRDM-MCXA156 Board User Manual](https://www.nxp.com/docs/en/user-manual/UM12121.pdf)
- [FRDM-MCXA156 Schematics](https://www.nxp.com/webapp/Download?colCode=SPF-90841)

### Supported Features

The FRDM-MCXA156 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| UART | on-chip | serial port-polling; serial port-interrupt |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | soc flash |

### Targets available

The default configuration file
[boards/nxp/frdm\_mcxa156/frdm\_mcxa156\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxa156/frdm_mcxa156_defconfig)

Other hardware features are not currently supported by the port.

### Connections and IOs

The MCX-A156 SoC has 5 gpio controllers and has pinmux registers which
can be used to configure the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_2 | UART | UART RX |
| PIO0\_3 | UART | UART TX |

### System Clock

The MCX-A156 SoC is configured to use FRO running at 96MHz as a source for
the system clock.

### Serial Port

The FRDM-MCXA156 SoC has 5 LPUART interfaces for serial communication.
LPUART 0 is configured as UART for the console.

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
short jumper JP5.

#### Using J-Link

There are two options. The onboard debug circuit can be updated with Segger
J-Link firmware by following the instructions in
[MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
To be able to program the firmware, you need to put the board in `DFU mode`
by shortening the jumper JP5.
The second option is to attach a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) to the
10-pin SWD connector (J24) of the board. Additionally, the jumper JP7 must
be shortened.
For both options use the `-r jlink` option with west to use the jlink runner.

```shell
west flash -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J21, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxa156 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxa156/mcxa156
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxa156/mcxa156 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxa156/mcxa156
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
