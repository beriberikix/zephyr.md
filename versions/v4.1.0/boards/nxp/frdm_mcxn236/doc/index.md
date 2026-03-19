---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nxp/frdm_mcxn236/doc/index.html
original_path: boards/nxp/frdm_mcxn236/doc/index.html
---

# FRDM-MCXN236

Board Overview

[![../../../../_images/frdm_mcxn236.webp](../../../../_images/frdm_mcxn236.webp)
](../../../../_images/frdm_mcxn236.webp)

FRDM-MCXN236

Name:
:   `frdm_mcxn236`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mcxn236

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_mcxn236/doc/index.rst/../..)

## Overview

FRDM-MCXN236 are compact and scalable development boards for rapid prototyping of
MCX N23X MCUs. They offer industry standard headers for easy access to the
MCUs I/Os, integrated open-standard serial interfaces, external flash memory and
an on-board MCU-Link debugger. MCX N Series are high-performance, low-power
microcontrollers with intelligent peripherals and accelerators providing multi-tasking
capabilities and performance efficiency.

## Hardware

- MCX-N236 Arm Cortex-M33 microcontroller running at 150 MHz
- 1MB dual-bank on chip Flash
- 352 KB RAM
- USB high-speed (Host/Device) with on-chip HS PHY. HS USB Type-C connectors
- 8x LP Flexcomms each supporting SPI, I2C, UART
- 2x FlexCAN with FD, 2x I3Cs, 2x SAI
- On-board MCU-Link debugger with CMSIS-DAP
- Arduino Header, FlexIO/LCD Header, SmartDMA/Camera Header, mikroBUS

For more information about the MCX-N236 SoC and FRDM-MCXN236 board, see:

- [MCX-N236 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/mcx-arm-cortex-m/mcx-n-series-microcontrollers/mcx-n23x-highly-integrated-mcus-with-on-chip-accelerators-intelligent-peripherals-and-advanced-security:MCX-N23X)
- [MCX-N236 Datasheet](https://www.nxp.com/docs/en/data-sheet/MCXN23x.pdf)
- [MCX-N236 Reference Manual](https://www.nxp.com/docs/en/reference-manual/MCXN23xRM.pdf)
- [FRDM-MCXN236 Website](https://www.nxp.com/design/design-center/development-boards-and-designs/general-purpose-mcus/frdm-development-board-for-mcx-n23x-mcus:FRDM-MCXN236)
- [FRDM-MCXN236 User Guide](https://www.nxp.com/document/guide/getting-started-with-frdm-mcxn236:GS-FRDM-MCXN236)
- [FRDM-MCXN236 Board User Manual](https://www.nxp.com/docs/en/user-manual/UM12041.pdf)
- [FRDM-MCXN236 Schematics](https://www.nxp.com/webapp/Download?colCode=SPF-90828)

### Supported Features

The FRDM-MCXN236 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| UART | on-chip | serial port-polling; serial port-interrupt |
| SPI | on-chip | spi |
| I2C | on-chip | i2c |
| I3C | on-chip | i3c |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | soc flash |
| WATCHDOG | on-chip | watchdog |
| VREF | on-chip | regulator |
| ADC | on-chip | adc |
| USBHS | on-chip | USB device |
| LPCMP | on-chip | sensor(comparator) |
| FLEXCAN | on-chip | CAN |
| FLEXIO | on-chip | flexio |
| DISPLAY | on-chip | flexio; MIPI-DBI. Tested with [NXP LCD\_PAR\_S035 TFT LCD Module](../../../shields/lcd_par_s035/doc/index.md#lcd-par-s035) |
| LPTMR | on-chip | counter |
| MRT | on-chip | counter |
| RTC | on-chip | rtc |

### Targets available

The default configuration file
[boards/nxp/frdm\_mcxn236/frdm\_mcxn236\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_mcxn236/frdm_mcxn236_defconfig)

Other hardware features are not currently supported by the port.

### Connections and IOs

The MCX-N236 SoC has 6 gpio controllers and has pinmux registers which
can be used to configure the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| P0\_PIO1\_8 | UART | UART RX |
| P1\_PIO1\_9 | UART | UART TX |

### System Clock

The MCX-N236 SoC is configured to use PLL0 running at 150MHz as a source for
the system clock.

### Serial Port

The FRDM-MCXN236 SoC has 8 FLEXCOMM interfaces for serial communication.
Flexcomm 4 is configured as UART for the console.

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
10-pin SWD connector (J12) of the board. Additionally, the jumper JP7 must
be shortened.
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
west build -b frdm_mcxn236 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxn236/mcxn236
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b frdm_mcxn236/mcxn236 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v3.6.0-4478-ge6c3a42f5f52 ***
Hello World! frdm_mcxn236/mcxn236
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
