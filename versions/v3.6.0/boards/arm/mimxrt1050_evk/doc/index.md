---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/mimxrt1050_evk/doc/index.html
original_path: boards/arm/mimxrt1050_evk/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# NXP MIMXRT1050-EVK

## Overview

The i.MX RT1050 is a new processor family featuring NXP’s advanced
implementation of the ARM Cortex-M7 Core. It provides high CPU performance and
real-time response.

The i.MX RT1050 provides various memory interfaces, including SDRAM, Raw NAND
FLASH, NOR FLASH, SD/eMMC, Quad SPI, HyperBus and a wide range of other
interfaces for connecting peripherals, such as WLAN, Bluetooth™, GPS, displays,
and camera sensors. As with other i.MX processors, i.MX RT1050 also has rich
audio and video features, including LCD display, basic 2D graphics, camera
interface, SPDIF, and I2S audio interface.

The following document refers to the discontinued MIMXRT1050-EVK board. For the
MIMXRT1050-EVKB board, refer to [Board Revisions](#board-revisions) section.

![MIMXRT1050-EVK](../../../../_images/mimxrt1050_evk.jpg)

## Hardware

- MIMXRT1052DVL6A MCU (600 MHz, 512 KB TCM)
- Memory

  - 256 KB SDRAM
  - 64 Mbit QSPI Flash
  - 512 Mbit Hyper Flash
- Display

  - LCD connector
  - Touch connector
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

For more information about the MIMXRT1050 SoC and MIMXRT1050-EVK board, see
these references:

- [i.MX RT1050 Website](https://www.nxp.com/products/microcontrollers-and-processors/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1050-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1050)
- [i.MX RT1050 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1050CEC.pdf)
- [i.MX RT1050 Reference Manual](https://www.nxp.com/docs/en/reference-manual/IMXRT1050RM.pdf)
- [MIMXRT1050-EVK Website](https://www.nxp.com/products/microcontrollers-and-processors/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1050-evaluation-kit:MIMXRT1050-EVK)
- [MIMXRT1050-EVK User Guide](https://www.nxp.com/webapp/Download?colCode=IMXRT1050EVKBHUG)
- [MIMXRT1050-EVK Schematics](https://www.nxp.com/webapp/Download?colCode=MIMXRT1050-EVK-DESIGNFILES)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| IS42S16160J | SEMC | Enabled via device configuration data block, which sets up SEMC at boot time |
| S26KS512SDPBHI020 | FLEXSPI | Enabled via flash configurationn block, which sets up FLEXSPI at boot time. |

### Supported Features

The mimxrt1050\_evk board configuration supports the hardware features listed
below. For additional features not yet supported, please also refer to the
[NXP MIMXRT1064-EVK](../../mimxrt1064_evk/doc/index.md#mimxrt1064-evk) , which is the superset board in NXP’s i.MX RT10xx family.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the mimxrt1064\_evk board may have additional features
already supported, which can also be re-used on this mimxrt1050\_evk board:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| DISPLAY | on-chip | display |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SDHC | on-chip | disk access |
| SPI | on-chip | spi |
| UART | on-chip | serial port-polling; serial port-interrupt |
| ENET | on-chip | ethernet |
| USB | on-chip | USB device |
| ADC | on-chip | adc |
| GPT | on-chip | gpt |
| TRNG | on-chip | entropy |
| FLEXSPI | on-chip | flash programming |

The default configuration can be found in the defconfig file:

> `boards/arm/mimxrt1050_evk/mimxrt1050_evk_defconfig`

Other hardware features are not currently supported by the port.

### Connections and IOs

The MIMXRT1050 SoC has five pairs of pinmux/gpio controllers.

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
| GPIO\_AD\_B1\_11 | ADC | ADC1 channel 0 |
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
| GPIO\_AD\_B1\_02 | 1588\_EVENT2\_OUT | 1588 |
| GPIO\_AD\_B1\_03 | 1588\_EVENT2\_IN | 1588 |

Note

In order to use the SPI peripheral on this board, resistors R278,
R279, R280, and R281 must be populated with zero ohm resistors

### System Clock

The MIMXRT1050 SoC is configured to use SysTick as the system clock source,
running at 600MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1050 SoC has eight UARTs. `LPUART1` is configured for the console,
`LPUART3` for the Bluetooth Host Controller Interface (BT HCI), and the
remaining are not used.

### USB

The RT1050 SoC has two USB OTG (USBOTG) controllers that supports both
device and host functions through its micro USB connectors.
Only USB device function is supported in Zephyr at the moment.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe),
however the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) do not yet support programming the
external flashes on this board so you must reconfigure the board for one of the
following debug probes instead.

#### Using LinkServer

Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your
search path. LinkServer works with the default CMSIS-DAP firmware included in
the on-board debugger.

Linkserver is the default runner. You may also se the `-r linkserver` option
with West to use the LinkServer runner.

```shell
west flash
west debug
```

#### JLink (on-board): [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Follow the instructions in [OpenSDA J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-jlink-onboard-debug-probe) to program
the [OpenSDA J-Link MIMXRT1050-EVK-Hyperflash Firmware](https://www.segger.com/downloads/jlink/OpenSDA_MIMXRT1050-EVK-Hyperflash). Check that jumpers
J32 and J33 are **on** (they are on by default when boards ship from the
factory) to ensure SWD signals are connected to the OpenSDA microcontroller.

Follow the instructions in [Enable QSPI flash support in SEGGER JLink](https://wiki.segger.com/i.MXRT1050#QSPI_flash)
in order to support your EVK if you have modified it to boot from QSPI NOR
flash as specified by NXP AN12108.

#### External JLink [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe)

Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search
path.

Attach a J-Link 20-pin connector to J21. Check that jumpers J32 and J33 are
**off** (they are on by default when boards ship from the factory) to ensure
SWD signals are disconnected from the OpenSDA microcontroller.

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console. Check that
jumpers J30 and J31 are **on** (they are on by default when boards ship from
the factory) to connect UART signals to the OpenSDA microcontroller.

Connect a USB cable from your PC to J28.

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
west build -b mimxrt1050_evk samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW4 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1050_evk
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1050_evk samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1050_evk
```

### Troubleshooting

If the debug probe fails to connect with the following error, it’s possible
that the boot header in HyperFlash is invalid or corrupted. The boot header is
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

You can fix it by erasing and reprogramming the HyperFlash with the following
steps:

1. Set the SW7 DIP switches to ON-ON-ON-OFF to prevent booting from HyperFlash.
2. Reset by pressing SW4
3. Run `west debug` or `west flash` again with a known working Zephyr
   application.
4. Set the SW7 DIP switches to OFF-ON-ON-OFF to boot from HyperFlash.
5. Reset by pressing SW4

## Board Revisions

The original MIMXRT1050-EVK (rev A0) board was updated with a newer
MIMXRT1050-EVKB (rev A1) board, with these major hardware differences:

- SoC changed from MIMXRT1052DVL6**A** to MIMXRT1052DVL6**B**
- Hardware bug fixes for: power, interfaces, and memory
- Arduino headers included

For more details, please see the following [NXP i.MXRT1050 A0 to A1 Migration Guide](https://www.nxp.com/docs/en/nxp/application-notes/AN12146.pdf).

Current Zephyr build supports the new MIMXRT1050-EVKB

### Experimental ENET Driver

Current default ethernet driver is eth\_mcux, with binding nxp,kinetis-ethernet. There is a new
driver with binding nxp,enet, which is experimental and undergoing development, but will have
enhanced capability, such as not hardcoding code for only one phy in the driver like eth\_mcux.

To build for this EVK with the new driver, include the experimental overlay to west build with
the option -DEXTRA\_DTC\_OVERLAY\_FILE=nxp,enet-experimental.overlay.
