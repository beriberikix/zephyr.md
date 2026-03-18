---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/mimxrt1060_evk/doc/index.html
original_path: boards/arm/mimxrt1060_evk/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# NXP MIMXRT1060-EVK

## Overview

The i.MX RT1060 adds to the industry’s first crossover
processor series and expands the i.MX RT series to three scalable families.

The i.MX RT1060 doubles the On-Chip SRAM to 1MB while keeping pin-to-pin
compatibility with i.MX RT1050. This series introduces additional features
ideal for real-time applications such as High-Speed GPIO, CAN FD, and
synchronous parallel NAND/NOR/PSRAM controller. The i.MX RT1060 runs on the
Arm® Cortex-M7® core up to 600 MHz.

![MIMXRT1060-EVK](../../../../_images/mimxrt1060_evk.jpg)

## Hardware

- MIMXRT1062DVL6A MCU (600 MHz, 1024 KB on-chip memory)
- Memory

  - 256 Mbit SDRAM
  - 64 Mbit QSPI Flash
  - 512 Mbit Hyper Flash
  - TF socket for SD card
- Display

  - LCD connector
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

  - FXOS8700CQ 6-axis e-compass
  - CMOS camera sensor interface
- Expansion port

  - Arduino interface
- CAN bus connector

For more information about the MIMXRT1060 SoC and MIMXRT1060-EVK board, see
these references:

- [i.MX RT1060 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1060-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1060)
- [i.MX RT1060 Datasheet](https://www.nxp.com/docs/en/nxp/data-sheets/IMXRT1060CEC.pdf)
- [i.MX RT1060 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1060RM)
- [MIMXRT1060-EVK Website](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt1060-evaluation-kit:MIMXRT1060-EVKB)
- [MIMXRT1060-EVK User Guide](https://www.nxp.com/webapp/Download?colCode=MIMXRT10601064EKBHUG)
- [MIMXRT1060-EVK Schematics](https://www.nxp.com/webapp/Download?colCode=MIMXRT1060-EVK-DESIGNFILE-A3)
- [MIMXRT1060-EVK Debug Firmware](https://www.nxp.com/docs/en/application-note/AN13206.pdf)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| IS25WP064AJBLE | SEMC | Enabled via device configuration data block, which sets up SEMC at boot time |
| IS42S16160J | FLEXSPI | Enabled via flash configurationn block, which sets up FLEXSPI at boot time. |

### Supported Features

The mimxrt1060\_evk board configuration supports the hardware features listed
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
| FLASH | on-chip | QSPI flash |
| GPIO | on-chip | gpio |
| SPI | on-chip | spi |
| I2C | on-chip | i2c |
| WATCHDOG | on-chip | watchdog |
| SDHC | on-chip | disk access |
| UART | on-chip | serial port-polling; serial port-interrupt |
| ENET | on-chip | ethernet |
| USB | on-chip | USB device |
| CAN | on-chip | can |
| DMA | on-chip | dma |
| ADC | on-chip | adc |
| SAI | on-chip | i2s |
| GPT | on-chip | gpt |
| TRNG | on-chip | entropy |
| FLEXSPI | on-chip | flash programming |

The default configuration can be found in the defconfig file:
`boards/arm/mimxrt1060_evk/mimxrt1060_evk_defconfig`

Other hardware features are not currently supported by the port.

### Connections and I/Os

The MIMXRT1060 SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_AD\_B0\_00 | LPSPI1\_SCK | SPI |
| GPIO\_AD\_B0\_01 | LPSPI1\_SDO | SPI |
| GPIO\_AD\_B0\_02 | LPSPI3\_SDI/LCD\_RST| SPI/LCD Display | |
| GPIO\_AD\_B0\_03 | LPSPI3\_PCS0 | SPI |
| GPIO\_AD\_B0\_05 | GPIO | SD Card |
| GPIO\_AD\_B0\_09 | GPIO/ENET\_RST | LED |
| GPIO\_AD\_B0\_10 | GPIO/ENET\_INT | GPIO/Ethernet |
| GPIO\_AD\_B0\_11 | GPIO | Touch Interrupt |
| GPIO\_AD\_B0\_12 | LPUART1\_TX | UART Console |
| GPIO\_AD\_B0\_13 | LPUART1\_RX | UART Console |
| GPIO\_AD\_B1\_00 | LPI2C1\_SCL | I2C |
| GPIO\_AD\_B1\_01 | LPI2C1\_SDA | I2C |
| GPIO\_AD\_B1\_06 | LPUART3\_TX | UART BT HCI |
| GPIO\_AD\_B1\_07 | LPUART3\_RX | UART BT HCI |
| WAKEUP | GPIO | SW0 |
| GPIO\_B0\_00 | LCD\_CLK | LCD Display |
| GPIO\_B0\_01 | LCD\_ENABLE | LCD Display |
| GPIO\_B0\_02 | LCD\_HSYNC | LCD Display |
| GPIO\_B0\_03 | LCD\_VSYNC | LCD Display |
| GPIO\_B0\_04 | LCD\_DATA00 | LCD Display |
| GPIO\_B0\_05 | LCD\_DATA01 | LCD Display |
| GPIO\_B0\_06 | LCD\_DATA02 | LCD Display |
| GPIO\_B0\_07 | LCD\_DATA03 | LCD Display |
| GPIO\_B0\_08 | LCD\_DATA04 | LCD Display |
| GPIO\_B0\_09 | LCD\_DATA05 | LCD Display |
| GPIO\_B0\_10 | LCD\_DATA06 | LCD Display |
| GPIO\_B0\_11 | LCD\_DATA07 | LCD Display |
| GPIO\_B0\_12 | LCD\_DATA08 | LCD Display |
| GPIO\_B0\_13 | LCD\_DATA09 | LCD Display |
| GPIO\_B0\_14 | LCD\_DATA10 | LCD Display |
| GPIO\_B0\_15 | LCD\_DATA11 | LCD Display |
| GPIO\_B1\_00 | LCD\_DATA12 | LCD Display |
| GPIO\_B1\_01 | LCD\_DATA13 | LCD Display |
| GPIO\_B1\_02 | LCD\_DATA14 | LCD Display |
| GPIO\_B1\_03 | LCD\_DATA15 | LCD Display |
| GPIO\_B1\_04 | ENET\_RX\_DATA00 | Ethernet |
| GPIO\_B1\_05 | ENET\_RX\_DATA01 | Ethernet |
| GPIO\_B1\_06 | ENET\_RX\_EN | Ethernet |
| GPIO\_B1\_07 | ENET\_TX\_DATA00 | Ethernet |
| GPIO\_B1\_08 | ENET\_TX\_DATA01 | Ethernet |
| GPIO\_B1\_09 | ENET\_TX\_EN | Ethernet |
| GPIO\_B1\_10 | ENET\_REF\_CLK | Ethernet |
| GPIO\_B1\_11 | ENET\_RX\_ER | Ethernet |
| GPIO\_B1\_12 | GPIO | SD Card |
| GPIO\_B1\_14 | USDHC1\_VSELECT | SD Card |
| GPIO\_B1\_15 | BACKLIGHT\_CTL | LCD Display |
| GPIO\_EMC\_40 | ENET\_MDC | Ethernet |
| GPIO\_EMC\_41 | ENET\_MDIO | Ethernet |
| GPIO\_AD\_B0\_09 | ENET\_RST | Ethernet |
| GPIO\_AD\_B0\_10 | ENET\_INT | Ethernet |
| GPIO\_SD\_B0\_00 | USDHC1\_CMD/LPSPI1\_SCK | SD Card/SPI | |
| GPIO\_SD\_B0\_01 | USDHC1\_CLK/LPSPI1\_PCS0 | SD Card/SPI | |
| GPIO\_SD\_B0\_02 | USDHC1\_DATA0/LPSPI1\_SDO | SD Card/SPI | |
| GPIO\_SD\_B0\_03 | USDHC1\_DATA1/LPSPI1\_SDI | SD Card/SPI | |
| GPIO\_SD\_B0\_04 | USDHC1\_DATA2 | SD Card |
| GPIO\_SD\_B0\_05 | USDHC1\_DATA3 | SD Card |
| GPIO\_AD\_B1\_11 | ADC | ADC1 Channel 0 |
| GPIO\_AD\_B1\_10 | ADC | ADC1 Channel 15 |
| GPIO\_AD\_B1\_09 | SAI1\_MCLK | I2S |
| GPIO\_AD\_B1\_12 | SAI1\_RX | I2S |
| GPIO\_AD\_B1\_13 | SAI1\_TX | I2S |
| GPIO\_AD\_B1\_14 | SAI1\_TX\_BCLK | I2S |
| GPIO\_AD\_B1\_15 | SAI1\_TX\_SYNC | I2S |
| GPIO\_AD\_B1\_02 | 1588\_EVENT2\_OUT | 1588 |
| GPIO\_AD\_B1\_03 | 1588\_EVENT2\_IN | 1588 |

Note

In order to use the SPI peripheral on this board, resistors R278, R279,
R280 and R281 must be populated with zero ohm resistors.

### System Clock

The MIMXRT1060 SoC is configured to use SysTick as the system clock source,
running at 600MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1060 SoC has eight UARTs. `LPUART1` is configured for the console,
`LPUART3` for the Bluetooth Host Controller Interface (BT HCI), and the
remaining are not used.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe),
however the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) do not yet support programming the
external flashes on this board so you must reconfigure the board for one of the
following debug probes instead.

> 1. Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your search path.
> 2. To update the debug firmware, please follow the instructions on MIMXRT1060-EVK Debug Firmware

#### Using J-Link

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

There are two options: the onboard debug circuit can be updated with Segger
J-Link firmware, or [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) can be attached to the
EVK. See [Using J-Link with MIMXRT1060-EVK or MIMXRT1064-EVK](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Using-J-Link-with-MIMXRT1060-EVK-or-MIMXRT1064-EVK/ta-p/1281149) or
[Using J-Link with MIMXRT1060-EVKB](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Using-J-Link-with-MIMXRT1060-EVKB/ta-p/1452717) for more details.

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

#### Using SWO

SWO can be used as a logging backend, by setting `CONFIG_LOG_BACKEND_SWO=y`.
Your SWO viewer should be configured with a CPU frequency of 132MHz, and
SWO frequency of 7500KHz.

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1060_evk samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW9 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1060_evk
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1060_evk samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1060_evk
```

### Troubleshooting

If the debug probe fails to connect with the following error, it’s possible
that the boot header in QSPI flash is invalid or corrupted. The boot header is
configured by [`CONFIG_NXP_IMX_RT_BOOT_HEADER`](../../../../kconfig.md#CONFIG_NXP_IMX_RT_BOOT_HEADER "CONFIG_NXP_IMX_RT_BOOT_HEADER").

```shell
Remote debugging using :2331
Remote communication error.  Target disconnected.: Connection reset by peer.
"monitor" command not supported by this target.
"monitor" command not supported by this target.
You can't do that when your target is `exec'
(gdb) Could not connect to target.
Please check power, connection and settings.
```

You can fix it by erasing and reprogramming the QSPI flash with the following
steps:

1. Set the SW7 DIP switches to ON-OFF-ON-OFF to prevent booting from QSPI flash.
2. Reset by pressing SW9
3. Run `west debug` or `west flash` again with a known working Zephyr
   application.
4. Set the SW7 DIP switches to OFF-OFF-ON-OFF to boot from QSPI flash.
5. Reset by pressing SW9

If the west flash or debug commands fail, and the command hangs while executing
runners.jlink, confirm the J-Link debug probe is configured, powered, and
connected to the EVK properly. See [Using J-Link](#using-j-link-rt1060) for more details.

### Experimental ENET Driver

Current default ethernet driver is eth\_mcux, with binding nxp,kinetis-ethernet. There is a new
driver with binding nxp,enet, which is experimental and undergoing development, but will have
enhanced capability, such as not hardcoding code for only one phy in the driver like eth\_mcux.

To build for this EVK with the new driver, include the experimental overlay to west build with
the option -DEXTRA\_DTC\_OVERLAY\_FILE=nxp,enet-experimental.overlay.
