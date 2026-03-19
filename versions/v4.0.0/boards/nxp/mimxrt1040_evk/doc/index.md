---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/nxp/mimxrt1040_evk/doc/index.html
original_path: boards/nxp/mimxrt1040_evk/doc/index.html
---

# MIMXRT1040-EVK

Board Overview

[![../../../../_images/mimxrt1040_evk.jpg](../../../../_images/mimxrt1040_evk.jpg)
](../../../../_images/mimxrt1040_evk.jpg)

MIMXRT1040-EVK

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   mimxrt1042

## Overview

i.MX RT1040 crossover MCUs add additional flexibility with new packages and an
extended temperature range up to 125° C. The i.MX RT1040 MCU has a compact
9x9 mm package, as well as the 11x11 mm package that supports implementing a
2-layer PCB design. The i.MX RT1040 MCUs run on the Arm® Cortex®-M7 core at
600 MHz.

## Hardware

- MIMXRT1042XJM5B MCU (600 MHz, 512 KB TCM)
- Memory

  - 256 MBit SDRAM (Winbond W9825G6KH)
  - 64 Mbit QSPI Flash (Winbond W25Q64JVSSIQ)
- Display

  - LCD connector
  - Touch connector
- Ethernet

  - 10/100 Mbit/s Ethernet PHY
- USB

  - USB 2.0 OTG connector
- Audio

  - 3.5 mm audio stereo headphone jack
  - Board-mounted microphone
- Power

  - 5 V DC jack
- Debug

  - JTAG 20-pin connector
  - OpenSDA with DAPLink
- Expansion port

  - Arduino interface
- CAN bus connector

For more information about the MIMXRT1040 SoC and MIMXRT1040-EVK board, see
these references:

- [i.MX RT1040 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt1040-crossover-mcu-with-arm-cortex-m7-core:i.MX-RT1040)
- [i.MX RT1040 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT1040CEC.pdf)
- [i.MX RT1040 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT1040RM)
- [MIMXRT1040-EVK Website](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt1040-evaluation-kit:MIMXRT1040-EVK)
- [MIMXRT1040-EVK User Guide](https://www.nxp.com/webapp/Download?colCode=MIMXRT1040-EVKUM)
- [MIMXRT1040-EVK Design Files](https://www.nxp.com/webapp/Download?colCode=MIMXRT1040-EVK-DESIGNFILES)

### External Memory

This platform has the following external memories:

| Device | Controller | Status |
| --- | --- | --- |
| W9825G6KH | SEMC | Enabled via device configuration data block, which sets up SEMC at boot time |
| W25Q64JVSSIQ | FLEXSPI | Enabled via flash configurationn block, which sets up FLEXSPI at boot time. Supported for XIP only. |

### Supported Features

The mimxrt1040\_evk board configuration supports the hardware features listed
below. For additional features not yet supported, please also refer to the
[MIMXRT1064-EVK](../../mimxrt1064_evk/doc/index.md#mimxrt1064_evk) , which is the superset board in NXP’s i.MX RT10xx family.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the mimxrt1064\_evk board may have additional features
already supported, which can also be re-used on this mimxrt1040\_evk board:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| GPIO | on-chip | gpio |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PWM | on-chip | pwm |
| ADC | on-chip | adc |
| SPI | on-chip | spi |
| DMA | on-chip | dma |
| I2C | on-chip | i2c |
| GPT | on-chip | gpt |
| DISPLAY | on-chip | eLCDIF. Tested with [NXP RK043FN02H-CT Parallel Display](../../../shields/rk043fn02h_ct/doc/index.md#rk043fn02h-ct), and [NXP RK043FN66HS-CTG Parallel Display](../../../shields/rk043fn66hs_ctg/doc/index.md#rk043fn66hs-ctg) shields |
| UART | NXP NW61x | M.2 WIFI/BT module |

The default configuration can be found in
[boards/nxp/mimxrt1040\_evk/mimxrt1040\_evk\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt1040_evk/mimxrt1040_evk_defconfig)

Other hardware features are not currently supported by the port.

### Connections and IOs

The MIMXRT1040 SoC has five pairs of pinmux/gpio controllers.

| Name | Function | Usage |
| --- | --- | --- |
| GPIO\_AD\_B0\_12 | LPUART1\_TX | UART Console |
| GPIO\_AD\_B0\_13 | LPUART1\_RX | UART Console |
| WAKEUP | GPIO | SW0 |
| GPIO\_AD\_B0\_08 | GPIO | User LD1 |
| GPIO\_AD\_B0\_10 | FLEXPWM1 PWM3A | PWM Output |
| GPIO\_AD\_B0\_14 | ADC0 IN3 | ADC0 Input |
| GPIO\_AD\_B0\_15 | ADC0 IN4 | ADC0 Input |
| GPIO\_SD\_B0\_02 | LPSPI1\_SDO | SPI Output |
| GPIO\_SD\_B0\_03 | LPSPI1\_SDI | SPI Input |
| GPIO\_SD\_B0\_00 | LPSPI1\_SCK | SPI Clock |
| GPIO\_SD\_B0\_00 | LPSPI1\_SCK | SPI Clock |
| GPIO\_AD\_B1\_00 | LPI2C1\_SCL | I2C Clock |
| GPIO\_AD\_B1\_01 | LPI2C1\_SDA | I2C Data |
| GPIO\_AD\_B1\_06 | LPUART3\_TX | M.2 BT HCI |
| GPIO\_AD\_B1\_07 | LPUART3\_RX | M.2 BT HCI |
| GPIO\_AD\_B1\_04 | LPUART3\_CTS\_b | M.2 BT HCI |
| GPIO\_AD\_B1\_05 | LPUART3\_RTS\_b | M.2 BT HCI |

Note

In order to use the SPI peripheral on this board, resistors R350, R346,
and R360 must be populated with zero ohm resistors.

### System Clock

The MIMXRT1040 SoC is configured to use SysTick as the system clock source,
running at 600MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution

### Serial Port

The MIMXRT1040 SoC has eight UARTs. `LPUART1` is configured for the console,
`LPUART3` for the Bluetooth Host Controller Interface (BT HCI),
and the remaining UARTs are not used.

### Fetch Binary Blobs

The board Bluetooth/WiFi module requires fetching some binary blob files, to do
that run the command:

```shell
west blobs fetch hal_nxp
```

Note

Only Bluetooth functionality is currently supported.

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

For the RT1040, J9/J10 are the SWD isolation jumpers, J12 is the DFU
mode jumper, and J2 is the 20 pin JTAG/SWD header.

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
jumpers J11 and J13 are **on** (they are on by default when boards ship from
the factory) to connect UART signals to the OpenSDA microcontroller.

Connect a USB cable from your PC to J1.

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
west build -b mimxrt1040_evk samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS Booting Zephyr OS build v3.3.0-rc3-66 *****
Hello World! mimxrt1040_evk
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b mimxrt1040_evk samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS Booting Zephyr OS build v3.3.0-rc3-66 *****
Hello World! mimxrt1040_evk
```

### Troubleshooting

#### USER\_LED D8

The MIMXRT1040-EVK board ships with the wireless module in the M.2 connector,
and with jumper J80 shorted. This causes a conflict with the USER\_LED D8,
and the LED will not turn off. Samples and applications using USER\_LED D8,
like blinky, require removal of J80 jumper.

#### Boot Header

If the debug probe fails to connect with the following error, it’s possible
that the boot header in QSPI is invalid or corrupted. The boot header is
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

You can fix it by erasing and reprogramming the QSPI with the following
steps:

1. Set the SW4 DIP switches to OFF-OFF-OFF-ON to boot into the ROM bootloader.
2. Reset by pressing SW1
3. Run `west debug` or `west flash` again with a known working Zephyr
   application.
4. Set the SW4 DIP switches to OFF-OFF-ON-OFF to boot from QSPI.
5. Reset by pressing SW1

#### Bluetooth Module

For Murate 2EL M.2 Mdoule, the following hardware rework needs to be applied,
Solder 0 ohm resistors for R96, and R93.
Remove resistors from R497, R498, R456 and R457.

And due to pin conflict issue, the PCM interface of Bluetooth module cannot be supported.

For the debugger fails to connect with the following error, please refer to the next section.

#### WiFi Module

If the debugger fails to connect with the following error, it’s possible
the M.2 WiFi module is interfering with the debug signals

```shell
Remote debugging using :2331
Remote communication error.  Target disconnected.: Connection reset by peer.
"monitor" command not supported by this target.
"monitor" command not supported by this target.
You can't do that when your target is `exec'
(gdb) Could not connect to target.
Please check power, connection and settings.
```

To resolve this, you may remove the M.2 WiFi module from the board when
flashing or debugging it, or remove jumper J80.
