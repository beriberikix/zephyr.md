---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/nxp/mimxrt1064_evk/doc/index.html
original_path: boards/nxp/mimxrt1064_evk/doc/index.html
---

# MIMXRT1064-EVK

Board Overview

[![../../../../_images/mimxrt1064_evk.jpg](../../../../_images/mimxrt1064_evk.jpg)
](../../../../_images/mimxrt1064_evk.jpg)

MIMXRT1064-EVK

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt1064

## Overview

The i.MX RT1064 adds to the industry’s first crossover
processor series and expands the i.MX RT series to three scalable families.
The i.MX RT1064 doubles the On-Chip SRAM to 1MB while keeping pin-to-pin
compatibility with i.MX RT1050. This series introduces additional features
ideal for real-time applications such as High-Speed GPIO, CAN FD, and
synchronous parallel NAND/NOR/PSRAM controller. The i.MX RT1064 runs on the
Arm® Cortex-M7® core up to 600 MHz.

## Hardware

- MIMXRT1064DVL6A MCU (600 MHz, 1024 KB on-chip memory, 4096KB on-chip QSPI
  flash)
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

For more information about the MIMXRT1064 SoC and MIMXRT1064-EVK board, see
these references:

- [i.MX RT1064 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1064-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1064)
- [i.MX RT1064 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1064CEC.pdf)
- [i.MX RT1064 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1064RM)
- [MIMXRT1064-EVK Website](https://www.nxp.com/support/developer-resources/run-time-software/i.mx-developer-resources/mimxrt1064-evk-i.mx-rt1064-evaluation-kit:MIMXRT1064-EVK)
- [MIMXRT1064-EVK Quick Reference Guide](https://www.nxp.com/webapp/Download?colCode=IMXRT1064QSG)
- [MIMXRT1064-EVK User Guide](https://www.nxp.com/docs/en/data-sheet/MIMXRT10601064EKBHUG.pdf)
- [MIMXRT1064-EVK Schematics](https://www.nxp.com/webapp/Download?colCode=i.MXRT160EVKDS&Parent_nodeId=1537930933174731284155&Parent_pageType=product)
- [MIMXRT1064-EVK Debug Firmware](https://www.nxp.com/docs/en/application-note/AN13206.pdf)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| MT48LC16M16A2 | SEMC | Enabled via device configuration data block, which sets up SEMC at boot time |

### Supported Features

NXP considers the MIMXRT1064-EVK as the superset board for the i.MX RT10xx
family of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire RT10xx family. NXP prioritizes enabling
this board with new support for Zephyr features. The mimxrt1064\_evk board
configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| DISPLAY | on-chip | eLCDIF. Tested with [NXP RK043FN02H-CT Parallel Display](../../../shields/rk043fn02h_ct/doc/index.md#rk043fn02h-ct), and [NXP RK043FN66HS-CTG Parallel Display](../../../shields/rk043fn66hs_ctg/doc/index.md#rk043fn66hs-ctg) shields |
| VIDEO | on-chip | video, using CSI |
| FLASH | on-chip | QSPI flash |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| WATCHDOG | on-chip | watchdog |
| PWM | on-chip | pwm |
| SDHC | on-chip | disk access |
| UART | on-chip | serial port-polling; serial port-interrupt |
| ADC | on-chip | adc |
| ENET | on-chip | ethernet |
| USB | on-chip | USB device |
| CAN | on-chip | can |
| SPI | on-chip | spi |
| GPT | on-chip | gpt |
| DMA | on-chip | dma |
| HWINFO | on-chip | Unique device serial number |
| TRNG | on-chip | entropy |
| FLEXSPI | on-chip | flash programming |

The default configuration can be found in
[boards/nxp/mimxrt1064\_evk/mimxrt1064\_evk\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1064_evk/mimxrt1064_evk_defconfig)

Other hardware features are not currently supported by the port.

### Connections and I/Os

The MIMXRT1064 SoC has four pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_AD\_B0\_00 | LPSPI1\_SCK | SPI |
| GPIO\_AD\_B0\_01 | LPSPI1\_SDO | SPI |
| GPIO\_AD\_B0\_02 | LPSPI3\_SDI/LCD\_RST| SPI/LCD Display | |
| GPIO\_AD\_B0\_03 | LPSPI3\_PCS0 | SPI |
| GPIO\_AD\_B0\_05 | GPIO | SD Card |
| GPIO\_AD\_B0\_09 | GPIO/ENET\_RST | LED/Ethernet |
| GPIO\_AD\_B0\_10 | GPIO/ENET\_INT | GPIO/Ethernet |
| GPIO\_AD\_B0\_11 | GPIO | Touch Interrupt |
| GPIO\_AD\_B0\_12 | LPUART1\_TX | UART Console |
| GPIO\_AD\_B0\_13 | LPUART1\_RX | UART Console |
| GPIO\_AD\_B1\_06 | LPUART3\_TX | UART Arduino |
| GPIO\_AD\_B1\_07 | LPUART3\_RX | UART Arduino |
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
| GPIO\_SD\_B1\_05 | FLEXSPIA\_DQS | QSPI Flash |
| GPIO\_SD\_B1\_06 | FLEXSPIA\_SS0\_B | QSPI Flash |
| GPIO\_SD\_B1\_07 | FLEXSPIA\_SCLK | QSPI Flash |
| GPIO\_SD\_B1\_08 | FLEXSPIA\_DATA00 | QSPI Flash |
| GPIO\_SD\_B1\_09 | FLEXSPIA\_DATA01 | QSPI Flash |
| GPIO\_SD\_B1\_10 | FLEXSPIA\_DATA02 | QSPI Flash |
| GPIO\_SD\_B1\_11 | FLEXSPIA\_DATA03 | QSPI Flash |
| GPIO\_AD\_B1\_11 | ADC | ADC1 Channel 0 |
| GPIO\_AD\_B1\_10 | ADC | ADC1 Channel 1 |

Note

In order to use the SPI peripheral on this board, resistors R278, R279,
R280 and R281 must be populated with zero ohm resistors

### System Clock

The MIMXRT1064 SoC is configured to use SysTick as the system clock source,
running at 600MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1064 SoC has eight UARTs. `LPUART1` is configured for the console
and the remaining are not used.

## Programming and Debugging

This board supports 3 debug host tools. Please install your preferred host
tool, then follow the instructions in [Configuring a Debug Probe](#configuring-a-debug-probe) to
configure the board appropriately.

- [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) (Default, Supported by NXP)
- [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) (Supported by NXP)
- [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) (Not supported by NXP)

Once the host tool and board are configured, build and flash applications
as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more
details).

### Configuring a Debug Probe

Note

When the device transitions into low power states, the debugger may be
unable to access the chip. Use caution when enabling `CONFIG_PM`, and
if the debugger cannot flash the part, see [Troubleshooting](#troubleshooting-rt1064)

For the RT1064, J47/J48 are the SWD isolation jumpers, J42 is the DFU
mode jumper, and J21 is the 20 pin JTAG/SWD header.

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

See [Using J-Link with MIMXRT1060-EVK or MIMXRT1064-EVK](https://community.nxp.com/t5/i-MX-RT-Knowledge-Base/Using-J-Link-with-MIMXRT1060-EVK-or-MIMXRT1064-EVK/ta-p/1281149) for more
details.

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

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1064_evk samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW9 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1064_evk
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1064_evk samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1064_evk
```

### Troubleshooting

If the debug probe fails to connect with the following error, it’s possible
that the boot header in QSPI flash is invalid or corrupted. The boot header is
configured by [`CONFIG_NXP_IMXRT_BOOT_HEADER`](../../../../kconfig.md#CONFIG_NXP_IMXRT_BOOT_HEADER "CONFIG_NXP_IMXRT_BOOT_HEADER").

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
connected to the EVK properly.
