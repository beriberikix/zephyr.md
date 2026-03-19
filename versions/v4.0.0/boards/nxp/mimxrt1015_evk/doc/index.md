---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/nxp/mimxrt1015_evk/doc/index.html
original_path: boards/nxp/mimxrt1015_evk/doc/index.html
---

# MIMXRT1015-EVK

Board Overview

[![../../../../_images/mimxrt1015_evk.jpg](../../../../_images/mimxrt1015_evk.jpg)
](../../../../_images/mimxrt1015_evk.jpg)

MIMXRT1015-EVK

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt1015

## Overview

The i.MX RT1015 expands the i.MX RT crossover processor families by providing
high-performance feature set in low-cost LQFP packages, further simplifying
board design and layout for customers. The i.MX RT1015 runs on the Arm®
Cortex®-M7 core at 500 MHz.

## Hardware

- MIMXRT1015DAF5A MCU
- Memory

  - 128 Mbit QSPI Flash
- Connectivity

  - Micro USB host and OTG connectors
  - Arduino interface
- Audio

  - Audio Codec
  - 4-pole audio headphone jack
  - External speaker connection
  - Microphone
- Debug

  - JTAG 10-pin connector
  - OpenSDA with DAPLink

For more information about the MIMXRT1015 SoC and MIMXRT1015-EVK board, see
these references:

- [i.MX RT1015 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1015-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1015)
- [i.MX RT1015 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1015CEC.pdf)
- [i.MX RT1015 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1015RM)
- [MIMXRT1015-EVK Website](https://www.nxp.com/support/developer-resources/run-time-software/i.mx-developer-resources/i.mx-rt1015-evaluation-kit:MIMXRT1015-EVK)
- [MIMXRT1015-EVK Quick Reference Guide](https://www.nxp.com/webapp/Download?colCode=IMXRT1015QSG)
- [MIMXRT1015-EVK Design Files](https://www.nxp.com/webapp/Download?colCode=MIMXRT1015-EVK-REVB-DS)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| AT25SF128A | FLEXSPI | Enabled via flash configurationn block, which sets up FLEXSPI at boot time. |

### Supported Features

The mimxrt1015\_evk board configuration supports the hardware features listed
below. For additional features not yet supported, please also refer to the
[MIMXRT1064-EVK](../../mimxrt1064_evk/doc/index.md#mimxrt1064_evk) , which is the superset board in NXP’s i.MX RT10xx family.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the mimxrt1064\_evk board may have additional features
already supported, which can also be re-used on this mimxrt1015\_evk board:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| UART | on-chip | serial port-polling; serial port-interrupt |
| USB | on-chip | USB device |
| ADC | on-chip | ADC |
| GPT | on-chip | gpt |
| TRNG | on-chip | entropy |

The default configuration can be found in
[boards/nxp/mimxrt1015\_evk/mimxrt1015\_evk\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1015_evk/mimxrt1015_evk_defconfig)

Other hardware features are not currently supported by the port.

### Connections and I/Os

The MIMXRT1015 SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_AD\_B0\_05 | GPIO | LED |
| GPIO\_EMC\_09 | GPIO | SW4 |
| GPIO\_AD\_B0\_06 | LPUART1\_TX | UART Console |
| GPIO\_AD\_B0\_07 | LPUART1\_RX | UART Console |
| GPIO\_EMC\_32 | LPUART4\_TX | UART Console |
| GPIO\_EMC\_33 | LPUART4\_RX | UART Console |
| GPIO\_AD\_B1\_15 | LPI2C1\_SDA | I2C SDA |
| GPIO\_AD\_B1\_14 | LPI2C1\_CLK | I2C SCL |
| GPIO\_AD\_B0\_10 | LPSPI1\_SCK | SPI |
| GPIO\_AD\_B0\_11 | LPSPI1\_PCS0 | SPI |
| GPIO\_AD\_B0\_12 | LPSPI1\_SDO | SPI |
| GPIO\_AD\_B0\_13 | LPSPI1\_SDI | SPI |
| GPIO\_AD\_B0\_14 | ADC | ADC1 Channel 1 |
| GPIO\_AD\_B1\_13 | ADC | ADC1 Channel 13 |

### System Clock

The MIMXRT1015 SoC is configured to use SysTick as the system clock source,
running at 500MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1015 SoC has four UARTs. `LPUART1` is configured for the console,
and the remaining are not used.

## Programming and Debugging

This board supports 3 debug host tools. Please install your preferred host
tool, then follow the instructions in [Configuring a Debug Probe](#configuring-a-debug-probe) to
configure the board appropriately.

- [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) (Default, Supported by NXP)
- [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) (Supported by NXP)
- [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) (Not supported by NXP)

Once the host tool and board are configured, build and flash applications
as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more
details).

### Configuring a Debug Probe

For the RT1015, J47/J48 are the SWD isolation jumpers, J42 is the DFU
mode jumper, and J34 is the 10 pin JTAG/SWD header.

A debug probe is used for both flashing and debugging the board. This board has
an [LPC-LINK2 Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpc-link2-onboard-debug-probe). The default firmware present on this
probe is the [LPC-Link2 DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpclink2-daplink-onboard-debug-probe).

Based on the host tool installed, please use the following instructions
to setup your debug probe:

- [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools):
  [Using J-Link with LPC-Link2 Probe](#using-j-link-with-lpc-link2-probe)
- [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools):
  [Using CMSIS-DAP with LPC-Link2 Probe](#using-cmsis-dap-with-lpc-link2-probe)
- [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools):
  [Using CMSIS-DAP with LPC-Link2 Probe](#using-cmsis-dap-with-lpc-link2-probe)

#### Using CMSIS-DAP with LPC-Link2 Probe

1. Follow the instructions provided at
   [LPC-LINK2 CMSIS DAP Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpclink2-cmsis-onboard-debug-probe) to reprogram the default debug
   probe firmware on this board.
2. Ensure the SWD isolation jumpers are populated

#### Using J-Link with LPC-Link2 Probe

There are two options: the onboard debug circuit can be updated with Segger
J-Link firmware, or a [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) can be attached to the
EVK.

To update the onboard debug circuit, please do the following:

1. Switch the power source for the EVK to a different source than the
   debug USB, as the J-Link firmware does not power the EVK via the
   debug USB.
2. Follow the instructions provided at
   [LPC-Link2 J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpclink2-jlink-onboard-debug-probe) to reprogram the default debug
   probe firmware on this board.
3. Ensure the SWD isolation jumpers are populated.

To attach an external J-Link probe, ensure the SWD isolation jumpers are
removed, then connect the probe to the external JTAG/SWD header

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console. Check that
jumpers J45 and J46 are **on** (they are on by default when boards ship from
the factory) to connect UART signals to the OpenSDA microcontroller.

Connect a USB cable from your PC to J41.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1015_evk samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW9 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1-1297-g312d75f2459e *****
Hello World! mimxrt1015_evk
```
