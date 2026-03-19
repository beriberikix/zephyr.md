---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/nxp/mimxrt1170_evk/doc/index.html
original_path: boards/nxp/mimxrt1170_evk/doc/index.html
---

# MIMXRT1170-EVK/EVKB

Board Overview

[![../../../../_images/mimxrt1170_evk.jpg](../../../../_images/mimxrt1170_evk.jpg)
](../../../../_images/mimxrt1170_evk.jpg)

MIMXRT1170-EVK/EVKB

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt1176

## Overview

The dual core i.MX RT1170 runs on the Cortex-M7 core at 1 GHz and on the Cortex-M4
at 400 MHz. The i.MX RT1170 MCU offers support over a wide temperature range
and is qualified for consumer, industrial and automotive markets. Zephyr
supports the initial revision of this EVK, as well as rev EVKB.

## Hardware

- MIMXRT1176DVMAA MCU

  - 1GHz Cortex-M7 & 400Mhz Cortex-M4
  - 2MB SRAM with 512KB of TCM for Cortex-M7 and 256KB of TCM for Cortex-M4
- Memory

  - 512 Mbit SDRAM
  - 128 Mbit QSPI Flash
  - 512 Mbit Octal Flash
  - 2 Gbit raw NAND flash
  - 64 Mbit LPSPI flash
  - TF socket for SD card
- Display

  - MIPI LCD connector
- Ethernet

  - 10/100 Mbit/s Ethernet PHY
  - 10/100/1000 Mbit/s Ethernet PHY
- USB

  - USB 2.0 OTG connector
  - USB 2.0 host connector
- Audio

  - 3.5 mm audio stereo headphone jack
  - Board-mounted microphone
  - Left and right speaker out connectors
- Power

  - 5 V DC jack
- Debug

  - JTAG 20-pin connector
  - on-board debugger
- Sensor

  - FXOS8700CQ 6-axis e-compass
  - MIPI camera sensor connector
- Expansion port

  - Arduino interface
  - M.2 WIFI/BT interface
- CAN bus connector

For more information about the MIMXRT1170 SoC and MIMXRT1170-EVK board, see
these references:

- [i.MX RT1170 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1170-crossover-mcu-family-first-ghz-mcu-with-arm-cortex-m7-and-cortex-m4-cores:i.MX-RT1170)
- [i.MX RT1170 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1170CEC.pdf)
- [i.MX RT1170 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1170RM)
- [MIMXRT1170-EVK Website](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt1170-evaluation-kit:MIMXRT1170-EVK)
- [MIMXRT1170-EVK Board Hardware User’s Guide](https://www.nxp.com/webapp/Download?colCode=MIMXRT1170EVKHUG)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| W9825G6KH SDRAM | SEMC | Enabled via device configuration data (DCD) block, which sets up the SEMC at boot time |
| IS25WP128 QSPI flash (RT1170 EVK) | FLEXSPI | Enabled via flash configuration block (FCB), which sets up the FLEXSPI at boot time. |
| W25Q512NWEIQ QSPI flash (RT1170 EVKB) | FLEXSPI | Enabled via flash configuration block (FCB), which sets up the FLEXSPI at boot time. Supported for XIP only. |

### Supported Features

NXP considers the MIMXRT1170-EVK as the superset board for the i.MX RT11xx
family of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire RT11xx family. NXP prioritizes enabling
this board with new support for Zephyr features. Note that this table
covers two boards: the RT1170 EVK (`mimxrt1170_evk//cm7/cm4`), and
RT1170 EVKB (`mimxrt1170_evk@B//cm7/cm4`)

| Interface | Controller | Driver/Component | RT1170 EVK | RT1170 EVKB |
| --- | --- | --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller | Supported | Supported |
| SYSTICK | on-chip | systick | Supported | Supported |
| GPIO | on-chip | gpio | Supported | Supported |
| COUNTER | on-chip | gpt | Supported | Supported |
| TIMER | on-chip | gpt | Supported | Supported |
| CAN | on-chip | flexcan | Supported (M7) | Supported (M7) |
| SPI | on-chip | spi | Supported (M7) | Supported |
| I2C | on-chip | i2c | Supported | Supported |
| PWM | on-chip | pwm | Supported | Supported |
| ADC | on-chip | adc | Supported (M7) | Supported (M7) |
| UART | on-chip | serial port-polling; serial port-interrupt; serial port-async | Supported | Supported |
| DMA | on-chip | dma | Supported | Supported |
| WATCHDOG | on-chip | watchdog | Supported (M7) | Supported (M7) |
| ENET | on-chip | ethernet - 10/100M | Supported (M7) | No support |
| ENET1G | on-chip | ethernet - 10/100/1000M | Supported (M7) | No support |
| SAI | on-chip | i2s | Supported | No support |
| USB | on-chip | USB Device | Supported (M7) | Supported (M7) |
| HWINFO | on-chip | Unique device serial number | Supported (M7) | Supported (M7) |
| DISPLAY | on-chip | eLCDIF; MIPI-DSI. Tested with [NXP RK055HDMIPI4M MIPI Display](../../../shields/rk055hdmipi4m/doc/index.md#rk055hdmipi4m), [NXP RK055HDMIPI4MA0 MIPI Display](../../../shields/rk055hdmipi4ma0/doc/index.md#rk055hdmipi4ma0), and [NXP G1120B0MIPI MIPI Display](../../../shields/g1120b0mipi/doc/index.md#g1120b0mipi) shields | Supported (M7) | Supported (M7) |
| ACMP | on-chip | sensor | Supported | No support |
| CAAM RNG | on-chip | entropy | Supported (M7) | No support |
| FLEXSPI | on-chip | flash programming | Supported (M7) | Supported (M7) |
| SDHC | on-chip | SD host controller | Supported (M7) | Supported (M7) |
| PIT | on-chip | pit | Supported (M7) | Supported (M7) |
| VIDEO | on-chip | CSI; MIPI CSI-2 Rx. Tested with [NXP BTB-44 OV5640 Camera Module](../../../shields/nxp_btb44_ov5640/doc/index.md#nxp-btb44-ov5640) shield | Supported (M7) | Supported (M7) |
| UART | NXP NW61x | M.2 WIFI/BT module | Unsupported | Supported (M7) |

The default configuration can be found in the defconfig files:
[boards/nxp/mimxrt1170\_evk/mimxrt1170\_evk\_mimxrt1176\_cm7\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk_mimxrt1176_cm7_defconfig)
[boards/nxp/mimxrt1170\_evk/mimxrt1170\_evk\_mimxrt1176\_cm4\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1170_evk/mimxrt1170_evk_mimxrt1176_cm4_defconfig)

### Connections and I/Os

The MIMXRT1170 SoC has six pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| WAKEUP | GPIO | SW7 |
| GPIO\_AD\_04 | GPIO | LED |
| GPIO\_AD\_24 | LPUART1\_TX | UART Console |
| GPIO\_AD\_25 | LPUART1\_RX | UART Console |
| GPIO\_LPSR\_00 | CAN3\_TX | flexcan |
| GPIO\_LPSR\_01 | CAN3\_RX | flexcan |
| GPIO\_AD\_29 | SPI1\_CS0 | spi |
| GPIO\_AD\_28 | SPI1\_CLK | spi |
| GPIO\_AD\_30 | SPI1\_SDO | spi |
| GPIO\_AD\_31 | SPI1\_SDI | spi |
| GPIO\_AD\_08 | LPI2C1\_SCL | i2c |
| GPIO\_AD\_09 | LPI2C1\_SDA | i2c |
| GPIO\_LPSR\_05 | LPI2C5\_SCL | i2c |
| GPIO\_LPSR\_04 | LPI2C5\_SDA | i2c |
| GPIO\_AD\_04 | FLEXPWM1\_PWM2 | pwm |
| GPIO\_AD\_32 | ENET\_MDC | Ethernet |
| GPIO\_AD\_33 | ENET\_MDIO | Ethernet |
| GPIO\_DISP\_B2\_02 | ENET\_TX\_DATA00 | Ethernet |
| GPIO\_DISP\_B2\_03 | ENET\_TX\_DATA01 | Ethernet |
| GPIO\_DISP\_B2\_04 | ENET\_TX\_EN | Ethernet |
| GPIO\_DISP\_B2\_05 | ENET\_REF\_CLK | Ethernet |
| GPIO\_DISP\_B2\_06 | ENET\_RX\_DATA00 | Ethernet |
| GPIO\_DISP\_B2\_07 | ENET\_RX\_DATA01 | Ethernet |
| GPIO\_DISP\_B2\_08 | ENET\_RX\_EN | Ethernet |
| GPIO\_DISP\_B2\_09 | ENET\_RX\_ER | Ethernet |
| GPIO\_AD\_17\_SAI1\_MCLK | SAI\_MCLK | SAI |
| GPIO\_AD\_21\_SAI1\_TX\_DATA00 | SAI1\_TX\_DATA | SAI |
| GPIO\_AD\_22\_SAI1\_TX\_BCLK | SAI1\_TX\_BCLK | SAI |
| GPIO\_AD\_23\_SAI1\_TX\_SYNC | SAI1\_TX\_SYNC | SAI |
| GPIO\_AD\_17\_SAI1\_MCLK | SAI1\_MCLK | SAI |
| GPIO\_AD\_20\_SAI1\_RX\_DATA00 | SAI1\_RX\_DATA00 | SAI |
| GPIO\_DISP\_B2\_10 | LPUART2\_TX | M.2 BT HCI |
| GPIO\_DISP\_B2\_11 | LPUART2\_RX | M.2 BT HCI |
| GPIO\_DISP\_B2\_12 | LPUART2\_CTS\_B | M.2 BT HCI |
| GPIO\_DISP\_B2\_13 | LPUART1\_RTS\_B | M.2 BT HCI |

## Dual Core samples

| Core | Boot Address | Comment |
| --- | --- | --- |
| Cortex M7 | 0x30000000[630K] | primary core |
| Cortex M4 | 0x20020000[96k] | boots from OCRAM |

| Memory | Address[Size] | Comment |
| --- | --- | --- |
| flexspi1 | 0x30000000[16M] | Cortex M7 flash |
| sdram0 | 0x80030000[64M] | Cortex M7 ram |
| ocram | 0x20020000[512K] | Cortex M4 “flash” |
| sram1 | 0x20000000[128K] | Cortex M4 ram |
| ocram2 | 0x200C0000[512K] | Mailbox/shared memory |

Only the first 16K of ocram2 has the correct MPU region attributes set to be
used as shared memory

### System Clock

The MIMXRT1170 SoC is configured to use SysTick as the system clock source,
running at 996MHz. When targeting the M4 core, SysTick will also be used,
running at 400MHz

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1170 SoC has 12 UARTs. `LPUART1` is configured for the console,
`LPUART2` for the Bluetooth Host Controller Interface (BT HCI), and the
remaining are not used.

### Fetch Binary Blobs

The board Bluetooth/WiFi module requires fetching some binary blob files, to do
that run the command:

```shell
west blobs fetch hal_nxp
```

Note

Only Bluetooth functionality is currently supported.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Building a Dual-Core Image

Dual core samples load the M4 core image from flash into the shared `ocram`
region. The M7 core then sets the M4 boot address to this region. The only
sample currently enabled for dual core builds is the `openamp` sample.
To flash a dual core sample, the M4 image must be flashed first, so that it is
written to flash. Then, the M7 image must be flashed. The openamp sysbuild
sample will do this automatically by setting the image order.

The secondary core can be debugged normally in single core builds
(where the target is `mimxrt1170_evk/mimxrt1176/cm4`). For dual core builds, the
secondary core should be placed into a loop, then a debugger can be attached
(see [AN13264](https://www.nxp.com/docs/en/application-note/AN13264.pdf), section 4.2.3 for more information)

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. The on-board
debugger listed below works with the LinkServer runner by default, or can be
reprogrammed with JLink firmware.

- MIMXRT1170-EVKB: [MCU-Link CMSIS-DAP Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-cmsis-onboard-debug-probe)
- MIMXRT1170-EVK: [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe)

#### Using J-Link

JLink is the default runner for this board. Install the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search path.

There are two options: the onboard debug circuit can be updated with Segger
J-Link firmware, or [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) can be attached to the
EVK. See [Using J-Link with MIMXRT1170-EVKB](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Using-J-Link-with-MIMXRT1170-EVKB/ta-p/1715138) or
[Using J-Link with MIMXRT1160-EVK or MIMXRT1170-EVK](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Using-J-Link-with-MIMXRT1160-EVK-or-MIMXRT1170-EVK/ta-p/1529760) for more details.

#### Using LinkServer

Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your
search path. LinkServer works with the default CMSIS-DAP firmware included in
the on-board debugger.

Use the `-r linkserver` option with West to use the LinkServer runner.

```shell
west flash -r linkserver
```

Alternatively, pyOCD can be used to flash and debug the board by using the
`-r pyocd` option with West. pyOCD is installed when you complete the
[Get Zephyr and install Python dependencies](../../../../develop/getting_started/index.md#gs-python-deps) step in the Getting Started Guide. The runners supported
by NXP are LinkServer and JLink. pyOCD is another potential option, but NXP
does not test or support the pyOCD runner.

### Configuring a Console

We will use the on-board debugger
microcontroller as a usb-to-serial adapter for the serial console. The following
jumper settings are default on these boards, and are required to connect the
UART signals to the USB bridge circuit:

- MIMXRT1170-EVKB: JP2 open (default)
- MIMXRT1170-EVK: J31 and J32 shorted (default)

Connect a USB cable from your PC to the on-board debugger USB port:

- MIMXRT1170-EVKB: J86
- MIMXRT1170-EVK: J11

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Before powering the board, make sure SW1 is set to 0001b

```shell
# From the root of the zephyr repository
west build -b mimxrt1170_evk/mimxrt1176/cm7 samples/hello_world
west flash
```

Power off the board, and change SW1 to 0010b. Then power on the board and
open a serial terminal, reset the board (press the SW4 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.4.0-xxxx-xxxxxxxxxxxxx *****
Hello World! mimxrt1170_evk
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1170_evk/mimxrt1176/cm7 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.4.0-xxxx-xxxxxxxxxxxxx *****
Hello World! mimxrt1170_evk
```

### ENET1G Driver

Current default of ethernet driver is to use 100M Ethernet instance ENET.
To use the 1G Ethernet instance ENET1G, include the overlay to west build with
the option `-DEXTRA_DTC_OVERLAY_FILE=nxp,enet1g.overlay` instead.
