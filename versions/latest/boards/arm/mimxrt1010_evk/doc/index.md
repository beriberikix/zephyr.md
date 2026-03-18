---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/mimxrt1010_evk/doc/index.html
original_path: boards/arm/mimxrt1010_evk/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# NXP MIMXRT1010-EVK

## Overview

The i.MX RT1010 offer a new entry-point into the i.MX RT crossover processor
series by providing the lowest-cost LQFP package option, combined with the
high performance and ease-of-use known throughout the entire i.MX RT series.
This device is fully supported by NXP’s MCUXpresso Software and Tools.

![MIMXRT1010-EVK](../../../../_images/mimxrt1010_evk.jpg)

## Hardware

- MIMXRT1011DAE5A MCU
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

For more information about the MIMXRT1010 SoC and MIMXRT1010-EVK board, see
these references:

- [i.MX RT1010 Website](https://www.nxp.com/imxrt1010)
- [i.MX RT1010 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1010CEC.pdf)
- [i.MX RT1010 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1010RM)
- [MIMXRT1010-EVK Website](https://www.nxp.com/MIMXRT1010-EVK)
- [MIMXRT1010-EVK User Guide](https://www.nxp.com/webapp/Download?colCode=MIMXRT1010EVKHUG)
- [MIMXRT1010-EVK Design Files](https://www.nxp.com/webapp/Download?colCode=IMXRT1010-EVK-DESIGN-FILES)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| AT25SF128A | FLEXSPI | Enabled via flash configurationn block, which sets up FLEXSPI at boot time. |

### Supported Features

The mimxrt1010\_evk board configuration supports the hardware features listed
below. For additional features not yet supported, please also refer to the
[NXP MIMXRT1064-EVK](../../mimxrt1064_evk/doc/index.md#mimxrt1064-evk) , which is the superset board in NXP’s i.MX RT10xx family.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the mimxrt1064\_evk board may have additional features
already supported, which can also be re-used on this mimxrt1010\_evk board:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| GPIO | on-chip | gpio |
| SPI | on-chip | spi |
| I2C | on-chip | i2c |
| UART | on-chip | serial port-polling; serial port-interrupt |
| USB | on-chip | USB device |
| ADC | on-chip | adc |
| GPT | on-chip | gpt |
| TRNG | on-chip | entropy |

The default configuration can be found in the defconfig file:
`boards/arm/mimxrt1010_evk/mimxrt1010_evk_defconfig`

Other hardware features are not currently supported by the port.

### Connections and I/Os

The MIMXRT1010 SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_11 | GPIO | LED |
| GPIO\_SD\_05 | GPIO | SW4 |
| GPIO\_10 | LPUART1\_TX | UART Console |
| GPIO\_09 | LPUART1\_RX | UART Console |
| GPIO\_01 | LPI2C1\_SDA | I2C SDA |
| GPIO\_02 | LPI2C1\_CLK | I2C SCL |
| GPIO\_AD\_03 | LPSPI1\_SDI | SPI |
| GPIO\_AD\_04 | LPSPI1\_SDO | SPI |
| GPIO\_AD\_05 | LPSPI1\_PCS0 | SPI |
| GPIO\_AD\_06 | LPSPI1\_SCK | SPI |
| GPIO\_AD\_01 | ADC | ADC1 Channel 1 |
| GPIO\_AD\_02 | ADC | ADC1 Channel 2 |

### System Clock

The MIMXRT1010 SoC is configured to use SysTick as the system clock source,
running at 500MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1010 SoC has four UARTs. `LPUART1` is configured for the console,
and the remaining are not used.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe),
however the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) do not yet support programming the
external flashes on this board so you must reconfigure the board for one of the
following debug probes instead.

#### [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Attach a J-Link 10-pin connector to J55. Check that jumpers J61 and J62 are
**off** (they are on by default when boards ship from the factory) to ensure
SWD signals are disconnected from the OpenSDA microcontroller.

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console. Check that
jumpers J31 and J32 are **on** (they are on by default when boards ship from
the factory) to connect UART signals to the OpenSDA microcontroller.

Connect a USB cable from your PC to J41.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1010_evk samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW9 button), and you should
see the following message in the terminal:

```shell
Hello World! mimxrt1010_evk
```
