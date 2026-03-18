---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/nxp/mimxrt1020_evk/doc/index.html
original_path: boards/nxp/mimxrt1020_evk/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# NXP MIMXRT1020-EVK

## Overview

The i.MX RT1020 expands the i.MX RT crossover processor families by providing
high-performance feature set in low-cost LQFP packages, further simplifying
board design and layout for customers. The i.MX RT1020 runs on the Arm®
Cortex®-M7 core at 500 MHz.

![MIMXRT1020-EVK](../../../../_images/mimxrt1020_evk.jpg)

## Hardware

- MIMXRT1021DAG5A MCU
- Memory

  - 256 Mbit SDRAM
  - 64 Mbit QSPI Flash
  - TF socket for SD card
- Connectivity

  - 10/100 Mbit/s Ethernet PHY
  - Micro USB host and OTG connectors
  - CAN transceivers
  - Arduino interface
- Audio

  - Audio Codec
  - 4-pole audio headphone jack
  - Microphone
  - External speaker connection
- Power

  - 5 V DC jack
- Debug

  - JTAG 20-pin connector
  - OpenSDA with DAPLink

For more information about the MIMXRT1020 SoC and MIMXRT1020-EVK board, see
these references:

- [i.MX RT1020 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1020-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1020)
- [i.MX RT1020 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1020CEC.pdf)
- [i.MX RT1020 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1020RM)
- [MIMXRT1020-EVK Website](https://www.nxp.com/support/developer-resources/run-time-software/i.mx-developer-resources/i.mx-rt1020-evaluation-kit:MIMXRT1020-EVK)
- [MIMXRT1020-EVK User Guide](https://www.nxp.com/webapp/Download?colCode=MIMXRT1020EVKHUG)
- [MIMXRT1020-EVK Design Files](https://www.nxp.com/webapp/Download?colCode=MIMXRT1020-EVK-Design-Files)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| MT48LC16M16A2P | SEMC | Enabled via device configuration data block, which sets up SEMC at boot time |
| IS25LP064A | FLEXSPI | Enabled via flash configurationn block, which sets up FLEXSPI at boot time |

### Supported Features

The mimxrt1020\_evk board configuration supports the hardware features listed
below. For additional features not yet supported, please also refer to the
[NXP MIMXRT1064-EVK](../../mimxrt1064_evk/doc/index.md#mimxrt1064-evk) , which is the superset board in NXP’s i.MX RT10xx family.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the mimxrt1064\_evk board may have additional features
already supported, which can also be re-used on this mimxrt1020\_evk board:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| FLASH | on-chip | QSPI flash |
| GPIO | on-chip | gpio |
| SPI | on-chip | spi |
| I2C | on-chip | i2c |
| SDHC | on-chip | disk access |
| UART | on-chip | serial port-polling; serial port-interrupt |
| ENET | on-chip | ethernet |
| USB | on-chip | USB device |
| ADC | on-chip | adc |
| GPT | on-chip | gpt |
| TRNG | on-chip | entropy |
| FLEXSPI | on-chip | flash programming |

The default configuration can be found in
[boards/nxp/mimxrt1020\_evk/mimxrt1020\_evk\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1020_evk/mimxrt1020_evk_defconfig)

Other hardware features are not currently supported by the port.

### Connections and I/Os

The MIMXRT1020 SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_AD\_B0\_05 | GPIO | LED |
| GPIO\_AD\_B0\_06 | LPUART1\_TX | UART Console |
| GPIO\_AD\_B0\_07 | LPUART1\_RX | UART Console |
| GPIO\_AD\_B1\_08 | LPUART2\_TX | UART BT HCI |
| GPIO\_AD\_B1\_09 | LPUART2\_RX | UART BT HCI |
| GPIO\_AD\_B1\_14 | LPI2C1\_SCL | I2C |
| GPIO\_AD\_B1\_15 | LPI2C1\_SDA | I2C |
| GPIO\_SD\_B1\_02 | LPI2C4\_SCL | I2C |
| GPIO\_SD\_B1\_03 | LPI2C4\_SDA | I2C |
| WAKEUP | GPIO | SW0 |
| GPIO\_AD\_B0\_04 | ENET\_RST | Ethernet |
| GPIO\_AD\_B0\_08 | ENET\_REF\_CLK | Ethernet |
| GPIO\_AD\_B0\_09 | ENET\_RX\_DATA01 | Ethernet |
| GPIO\_AD\_B0\_10 | ENET\_RX\_DATA00/LPSPI1\_SCK | Ethernet/SPI | |
| GPIO\_AD\_B0\_11 | ENET\_RX\_EN/LPSPI1\_PCS0 | Ethernet/SPI | |
| GPIO\_AD\_B0\_12 | ENET\_RX\_ER/LPSPI1\_SDO | Ethernet/SPI | |
| GPIO\_AD\_B0\_13 | ENET\_TX\_EN/LPSPI1\_SDI | Ethernet/SPI | |
| GPIO\_AD\_B0\_14 | ENET\_TX\_DATA00 | Ethernet |
| GPIO\_AD\_B0\_15 | ENET\_TX\_DATA01 | Ethernet |
| GPIO\_AD\_B1\_06 | ENET\_INT | Ethernet |
| GPIO\_EMC\_41 | ENET\_MDC | Ethernet |
| GPIO\_EMC\_40 | ENET\_MDIO | Ethernet |
| GPIO\_AD\_B1\_07 | USDHC1\_VSELECT | SD Card |
| GPIO\_SD\_B0\_02 | USDHC1\_CMD | SD Card |
| GPIO\_SD\_B0\_03 | USDHC1\_CLK | SD Card |
| GPIO\_SD\_B0\_04 | USDHC1\_DATA0 | SD Card |
| GPIO\_SD\_B0\_05 | USDHC1\_DATA1 | SD Card |
| GPIO\_SD\_B0\_00 | USDHC1\_DATA2 | SD Card |
| GPIO\_SD\_B0\_01 | USDHC1\_DATA3 | SD Card |
| GPIO\_SD\_B0\_06 | USDHC1\_CD\_B | SD Card |
| GPIO\_AD\_B1\_10 | ADC | ADC1 Channel 10 |
| GPIO\_AD\_B1\_11 | ADC | ADC1 Channel 11 |

### System Clock

The MIMXRT1020 SoC is configured to use SysTick as the system clock source,
running at 500MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1020 SoC has eight UARTs. `LPUART1` is configured for the console,
`LPUART2` for the Bluetooth Host Controller Interface (BT HCI), and the
remaining are not used.

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

For the RT1020, J47/J48 are the SWD isolation jumpers, J42 is the DFU
mode jumper, and J16 is the 20 pin JTAG/SWD header.

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
jumpers J25 and J26 are **on** (they are on by default when boards ship from
the factory) to connect UART signals to the OpenSDA microcontroller.

Connect a USB cable from your PC to J23.

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
west build -b mimxrt1020_evk samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW5 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1020_evk
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1020_evk samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1020_evk
```
