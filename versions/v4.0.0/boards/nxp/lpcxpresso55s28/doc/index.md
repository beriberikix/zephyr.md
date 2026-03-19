---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/nxp/lpcxpresso55s28/doc/index.html
original_path: boards/nxp/lpcxpresso55s28/doc/index.html
---

# LPCXpresso55S28

Board Overview

[![../../../../_images/LPC55S28-EVK.jpg](../../../../_images/LPC55S28-EVK.jpg)
](../../../../_images/LPC55S28-EVK.jpg)

LPCXpresso55S28

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   lpc55s28

## Overview

The LPCXpresso55S28 development board provides the ideal platform for evaluation
of and development with the LPC552x/S2x MCU based on the Arm® Cortex®-M33
architecture. The board includes a high-performance onboard debug probe, audio
subsystem and accelerometer, with several options for adding off-the-shelf
add-on boards for networking, sensors, displays, and other interfaces.

## Hardware

- LPC55S28 Arm® Cortex®-M33 microcontroller running at up to 150 MHz
- 512 KB flash and 256 KB SRAM on-chip
- Onboard, high-speed USB, Link2 debug probe with CMSIS-DAP and SEGGER J-Link
  protocol options
- UART and SPI port bridging from LPC55S28 target to USB via the onboard debug
  probe
- Hardware support for external debug probe
- 3 x user LEDs, plus Reset, ISP (3) and user buttons
- Micro SD card slot (4-bit SDIO)
- NXP MMA8652FCR1 accelerometer
- Stereo audio codec with line in/out
- High and full speed USB ports with micro A/B connector for host or device
  functionality
- MikroEletronika Click expansion option
- LPCXpresso-V3 expansion option compatible with Arduino UNO
- PMod compatible expansion / host connector

For more information about the LPC55S28 SoC and LPCXPresso55S28 board, see:

- [LPC55S28 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc552x-s2x-mainstream-arm-cortex-m33-based-microcontroller-family:LPC552x-S2x)
- [LPC55S28 Datasheet](https://www.nxp.com/docs/en/nxp/data-sheets/LPC55S2x_LPC552x_DS.pdf)
- [LPC55S28 User Manual](https://www.nxp.com/webapp/Download?colCode=UM11126)
- [LPCXpresso55S28 Website](https://www.nxp.com/design/software/development-software/lpcxpresso55s28-development-board:LPC55S28-EVK)
- [LPCXpresso55S28 User Manual](https://www.nxp.com/webapp/Download?colCode=UM11158)
- [LPCXpresso55S28 Development Board Design Files](https://www.nxp.com/webapp/Download?colCode=LPCXpresso55S69-DS)

### Supported Features

The lpcxpresso55s28 board configuration supports the hardware features listed
below. For additional features not yet supported, please also refer to the
[LPCXPRESSO55S69](../../lpcxpresso55s69/doc/index.md#lpcxpresso55s69) , which is the superset board in NXP’s LPC55xx series.
NXP prioritizes enabling the superset board with NXP’s Full Platform Support for
Zephyr. Therefore, the lpcxpresso55s69 board may have additional features
already supported, which can also be re-used on this lpcxpresso55s28 board:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| IOCON | on-chip | pinmux |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| USART | on-chip | serial port-polling; serial port-interrupt |
| WWDT | on-chip | windowed watchdog timer |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| RNG | on-chip | entropy; random |
| IAP | on-chip | flash programming |

Other hardware features are not currently enabled.

The default configuration file
[boards/nxp/lpcxpresso55s28/lpcxpresso55s28\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/lpcxpresso55s28/lpcxpresso55s28_defconfig)

### Connections and IOs

The LPC55S28 SoC has IOCON registers, which can be used to configure
the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_26 | SPI | SPI MOSI |
| PIO0\_29 | USART | USART RX |
| PIO0\_30 | USART | USART TX |
| PIO1\_1 | SPI | SPI SSEL |
| PIO1\_2 | SPI | SPI SCK |
| PIO1\_3 | SPI | SPI MISO |
| PIO1\_4 | GPIO | RED LED |
| PIO1\_6 | GPIO | BLUE\_LED |
| PIO1\_7 | GPIO | GREEN LED |
| PIO1\_20 | I2C | I2C SCL |
| PIO1\_21 | I2C | I2C SDA |

### System Clock

The LPC55S28 SoC is configured to use PLL1 clocked from the external 24MHz
crystal, running at 144MHz as a source for the system clock. When the flash
controller is enabled, the core clock will be reduced to 96MHz. The application
may reconfigure clocks after initialization, provided that the core clock is
always set to 96MHz when flash programming operations are performed.

### Serial Port

The LPC55S28 SoC has 8 FLEXCOMM interfaces for serial communication. One is
configured as USART for the console and the remaining are not used.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This
board is configured by default to use the LPC-Link2 CMSIS-DAP Onboard
Debug Probe.

### Configuring a Console

Connect a USB cable from your PC to P6, and use the serial terminal of your
choice (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s28 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v2.4.0 *****
Hello World! lpcxpresso55s28
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s28 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS zephyr-v2.4.0 *****
Hello World! lpcxpresso55s28
```
