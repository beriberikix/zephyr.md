---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/mimxrt1062_fmurt6/doc/index.html
original_path: boards/arm/mimxrt1062_fmurt6/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# NXP FMURT6

## Overview

The MIMXRT1062\_FMURT6 adds to the industry’s crossover
processor series and expands the i.MX RT series to three scalable families.

The i.MX RT1062 doubles the On-Chip SRAM to 1MB while keeping pin-to-pin
compatibility with i.MX RT1050. This series introduces additional features
ideal for real-time applications such as High-Speed GPIO, CAN FD, and
synchronous parallel NAND/NOR/PSRAM controller. The i.MX RT1062 runs on the
Arm® Cortex-M7® core up to 600 MHz.

![MIMXRT1062_FMURT6](../../../../_images/mimxrt1062_fmurt6.jpg)

## Hardware

- MIMXRT1062DVL6B MCU (600 MHz, 1024 KB on-chip memory)
- Memory

  - 256 Mbit SDRAM
  - 512 Mbit Hyper Flash
  - TF socket for SD card
- Ethernet

  - 10/100 Mbit/s Ethernet PHY
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
  - OpenSDA with DAPLink
- Sensor

  - BMI088 6-axis e-compass
- Expansion port

  - Arduino interface
- CAN bus connector

For more information about the MIMXRT1062 SoC and MIMXRT1062-FMURT6 board, see
these references:

- [i.MX RT1060 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1060-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1060)
- [i.MX RT1060 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1060RM)
- [MIMXRT1062-FMURT6 User Guide](https://docs.px4.io/master/en/)
- [MIMXRT1062-FMURT6 Schematics](https://github.com/NXPHoverGames/NXP-FMUMRT6)

### Supported Features

The mimxrt1062\_fmurt6 board configuration supports the hardware features listed
below. For additional features not yet supported, please also refer to the
[NXP MIMXRT1064-EVK](../../mimxrt1064_evk/doc/index.md#mimxrt1064-evk) , which is the superset board in NXP’s i.MX RT10xx family.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the mimxrt1064\_evk board may have additional features
already supported, which can also be re-used on this mimxrt1060\_evk board:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| DISPLAY | on-chip | display |
| FLASH | on-chip | QSPI hyper flash |
| GPIO | on-chip | gpio |
| SPI | on-chip | spi |
| I2C | on-chip | i2c |
| ADC | on-chip | adc |
| WATCHDOG | on-chip | watchdog |
| PWM | on-chip | pwm |
| UART | on-chip | serial port-polling; serial port-interrupt |
| ENET | on-chip | ethernet |
| USB | on-chip | USB device |
| CAN | on-chip | can |
| DMA | on-chip | dma |
| GPT | on-chip | gpt |
| FLEXSPI | on-chip | flash programming |

The default configuration can be found in the defconfig file:
`boards/arm/mimxrt1062_fmurt6/mimxrt1062_fmurt6_defconfig`

Other hardware features are not currently supported by the port.

### Connections and I/Os

The MIMXRT1062 SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_AD\_B1\_08 | FLEXCAN1 TX | CAN |
| GPIO\_B0\_03 | FLEXCAN1 RX | CAN |
| GPIO\_AD\_B0\_06 | PWM2A0 | PWM |
| GPIO\_EMC\_08 | PWM2A1 | PWM |
| GPIO\_EMC\_10 | PWM2A2 | PWM |
| GPIO\_AD\_B0\_09 | PWM2A3 | PWM |
| GPIO\_EMC\_31 | LPUART7\_TX | UART Console |
| GPIO\_EMC\_32 | LPUART7\_RX | UART Console |
| GPIO\_B0\_04 | LPI2C2\_SCL | I2C |
| GPIO\_B0\_05 | LPI2C2\_SDA | I2C |
| GPIO\_AD\_B1\_00 | LPI2C1\_SCL | I2C |
| GPIO\_AD\_B1\_01 | LPI2C1\_SDA | I2C |
| GPIO\_AD\_B0\_12 | LPI2C4\_SCL | I2C |
| GPIO\_AD\_B0\_13 | LPI2C4\_SDA | I2C |
| WAKEUP | GPIO | SW0 |
| GPIO\_B1\_01 | ENET\_RX\_DATA00 | Ethernet |
| GPIO\_B1\_02 | ENET\_RX\_DATA01 | Ethernet |
| GPIO\_B1\_03 | ENET\_RX\_EN | Ethernet |
| GPIO\_B0\_12 | ENET\_TX\_DATA00 | Ethernet |
| GPIO\_B0\_13 | ENET\_TX\_DATA01 | Ethernet |
| GPIO\_B0\_14 | ENET\_TX\_EN | Ethernet |
| GPIO\_B0\_15 | ENET\_REF\_CLK | Ethernet |
| GPIO\_B1\_00 | ENET\_RX\_ER | Ethernet |
| GPIO\_B1\_12 | GPIO | SD Card |
| GPIO\_B1\_14 | USDHC1\_VSELECT | SD Card |
| GPIO\_EMC\_40 | ENET\_MDC | Ethernet |
| GPIO\_B0\_01 | ENET\_MDIO | Ethernet |
| GPIO\_SD\_B0\_00 | USDHC1\_CMD | SD Card |
| GPIO\_SD\_B0\_01 | USDHC1\_CLK | SD Card |
| GPIO\_SD\_B0\_02 | USDHC1\_DATA0 | SD Card |
| GPIO\_SD\_B0\_03 | USDHC1\_DATA1 | SD Card |
| GPIO\_SD\_B0\_04 | USDHC1\_DATA2 | SD Card |
| GPIO\_SD\_B0\_05 | USDHC1\_DATA3 | SD Card |
| GPIO\_EMC\_27 | LPSPI1\_SCK | SPI |
| GPIO\_EMC\_28 | LPSPI1\_SDO | SPI |
| GPIO\_EMC\_29 | LPSPI1\_SDI | SPI |
| GPIO\_EMC\_00 | LPSPI2\_SCK | SPI |
| GPIO\_EMC\_02 | LPSPI2\_SDO | SPI |
| GPIO\_EMC\_03 | LPSPI2\_SDI | SPI |
| GPIO\_AD\_B1\_15 | LPSPI3\_SCK | SPI |
| GPIO\_AD\_B1\_14 | LPSPI3\_SDO | SPI |
| GPIO\_AD\_B1\_13 | LPSPI3\_SDI | SPI |
| GPIO\_AD\_B1\_11 | ADC | ADC1 Channel 0 |
| GPIO\_AD\_B1\_09 | ADC | ADC1 Channel 14 |
| GPIO\_AD\_B0\_15 | ADC | ADC1 Channel 4 |
| GPIO\_AD\_B1\_02 | UART2\_TX\_GPS1 | UART GPS |
| GPIO\_AD\_B1\_03 | UART2\_RX\_GPS1 | UART GPS |

### System Clock

The MIMXRT1062 SoC is configured to use SysTick as the system clock source,
running at 600MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1062 SoC has eight UARTs. `LPUART7` is configured for the console,
`LPUART8 and 2` for GPS/MAG, `LPUART3 and 4` for Telemetry and the remaining are not used.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe),
however the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) do not yet support programming the
external flashes on this board so you must reconfigure the board for one of the
following debug probes instead.

#### Using J-Link

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

For Hyperflash support on i.MxRT106x use JLink\_V780 or above.

There are two options: the onboard debug circuit can be updated with Segger
J-Link firmware, or [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) can be attached to the
FMURT6 on J23 FMU Debug Port.
Run JLink.exe and choose device / core as MIMXRT106A-ALEXA.

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console.

Connect a USB cable from your PC to PixHawk debug adapter.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

#### Using SWO

SWO can be used as a logging backend, by setting `CONFIG_LOG_BACKEND_SWO=y`.
Your SWO viewer should be configured with a CPU frequency of 132MHz, and
SWO frequency of 7500KHz.

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1062_fmurt6 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW9 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.20.0 *****
Hello World! mimxrt1062_fmurt6
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1062_fmurt6 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.20.0 *****
Hello World! mimxrt1062_fmurt6
```

### Troubleshooting

If the west flash or debug commands fail, and the command hangs while executing
runners.jlink, confirm the J-Link debug probe is configured, powered, and
connected to the FMURT6 properly.
