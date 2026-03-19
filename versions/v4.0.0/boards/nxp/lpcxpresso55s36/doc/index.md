---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/nxp/lpcxpresso55s36/doc/index.html
original_path: boards/nxp/lpcxpresso55s36/doc/index.html
---

# LPCXpresso55S36

Board Overview

[![../../../../_images/lpcxpresso55S36.jpg](../../../../_images/lpcxpresso55S36.jpg)
](../../../../_images/lpcxpresso55S36.jpg)

LPCXpresso55S36

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   lpc55s36

## Overview

The LPCXpresso55S36 board provides the ideal platform for evaluation
of the LPC55S3x/LPC553x MCU family, based on the Arm® Cortex®-M33
architecture. Arduino® UNO compatible shield connectors are included,
with additional expansion ports around the Arduino footprint, along
with a PMod/host interface port and MikroElektronika Click module
site.

## Hardware

- LPC55S36 Arm® Cortex®-M33 microcontroller running at up to 150 MHz
- 256 KB flash and 96 KB SRAM on-chip
- LPC-Link2 debug high speed USB probe with VCOM port
- I2C and SPI USB bridging to the LPC device via LPC-Link2 probe
- MikroElektronika Click expansion option
- LPCXpresso expansion connectors compatible with Arduino UNO
- PMod compatible expansion / host connector
- Reset, ISP, wake, and user buttons for easy testing of software functionality
- Tri-color LED
- Full-speed USB device / host port
- High-speed USB device / host port
- UART header for external serial to USB cable
- CAN Transceiver
- Stereo audio codec with in/out line

For more information about the LPC55S36 SoC and LPCXPresso55S36 board, see:

- [LPC55S36 SoC Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/general-purpose-mcus/lpc5500-cortex-m33/lpc553x-s3x-advanced-analog-armcortex-m33-based-mcu-family:LPC553x)
- [LPC55S36 Datasheet](https://www.nxp.com/docs/en/data-sheet/LPC553x.pdf)
- [LPC55S36 User Manual](https://www.nxp.com/docs/en/reference-manual/LPC553xRM.pdf)
- [LPCXpresso55S36 Website](https://www.nxp.com/design/development-boards/lpcxpresso-boards/development-board-for-the-lpc553x-family-of-mcus:LPCXpresso55S36)
- [LPCXpresso55S36 User Manual](https://www.nxp.com/docs/en/user-manual/LPCXpresso55S36UM.pdf)
- [LPCXpresso55S36 Development Board Design Files](https://www.nxp.com/webapp/Download?colCode=LPCXPRESSO5536_EVK-DESIGN-FILES)

### Supported Features

NXP considers the LPCXpresso55S36 as a superset board for the LPC55(S)3x
family of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire LPC55(S)3x family. NXP prioritizes enabling
this board with new support for Zephyr features. The lpcxpresso55s36 board
configuration supports the hardware features below. Another similar superset
board is the [LPCXPRESSO55S69](../../lpcxpresso55s69/doc/index.md#lpcxpresso55s69), and that board may have additional features
already supported, which can also be re-used on this lpcxpresso55s36 board:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| IOCON | on-chip | pinmux |
| GPIO | on-chip | gpio |
| USART | on-chip | serial port-polling; serial port-interrupt |
| CLOCK | on-chip | clock\_control |
| CAN | on-chip | canbus |
| IAP | on-chip | flash |
| PWM | on-chip | pwm |
| USB FS | on-chip | USB Full Speed device |
| DAC | on-chip | dac |

Other hardware features are not currently enabled.

Currently available targets for this board are:

- *lpcxpresso55s36*

### Connections and IOs

The LPC55S36 SoC has IOCON registers, which can be used to configure
the functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_17 | GPIO | USR SW3 |
| PIO0\_22 | GPIO | GREEN LED |
| PIO0\_28 | GPIO | RED LED |
| PIO0\_29 | USART | USART RX |
| PIO0\_30 | USART | USART TX |
| PIO1\_11 | GPIO | BLUE\_LED |
| PIO1\_18 | GPIO | Wakeup SW1 |
| PIO1\_20 | FLEXPPWM0\_PWM0\_A | pwm |
| PIO1\_17 | FLEXPPWM0\_PWM0\_B | pwm |
| PIO1\_6 | FLEXPPWM0\_PWM1\_A | pwm |
| PIO1\_22 | FLEXPPWM0\_PWM1\_B | pwm |
| PIO1\_8 | FLEXPPWM0\_PWM2\_A | pwm |
| PIO1\_4 | FLEXPPWM0\_PWM2\_B | pwm |
| PIO1\_21 | FLEXPPWM1\_PWM0\_A | pwm |
| PIO0\_3 | FLEXPPWM1\_PWM0\_B | pwm |
| PIO1\_23 | FLEXPPWM1\_PWM1\_A | pwm |
| PIO0\_21 | FLEXPPWM1\_PWM1\_B | pwm |
| PIO1\_25 | FLEXPPWM1\_PWM2\_A | pwm |
| PIO0\_31 | FLEXPPWM1\_PWM2\_B | pwm |
| PIO1\_2 | CAN0\_TXD | CAN TX |
| PIO1\_3 | CAN0\_RXD | CAN RX |
| PIO0\_22 | USB0\_VBUS | USBFS VBUS |

### System Clock

The LPC55S36 SoC is configured to use PLL1 clocked from the external 24MHz
crystal, running at 144MHz as a source for the system clock. When the flash
controller is enabled, the core clock will be reduced to 96MHz. Other sources for the system clock are
provided in the SOC, depending on your system requirements.

### Serial Port

The LPC55S36 SoC has 8 FLEXCOMM interfaces for serial
communication. One is configured as USART for the console and the
remaining are not used.

## Programming and Debugging

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the integrated [MCU-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-onboard-debug-probe)
in the CMSIS-DAP mode. To use this probe with Zephyr, you need to install the
[LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your search path.
Then, use the `linkserver` runner option to flash and debug the board. Refer
to the detailed overview about [Application Debugging](../../../../develop/debug/index.md#application-debugging) for additional
information.

The integrated MCU-Link hardware can also be used as a J-Link probe with a
firmware update, as described in [MCU-Link JLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#mcu-link-jlink-onboard-debug-probe).
The [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) should be available in this case.

### Configuring a Console

Connect a USB cable from your PC to J1 (LINK2), and use the serial
terminal of your choice (minicom, putty, etc.) with the following
settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s36 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v2.2.0 *****
Hello World! lpcxpresso55s36
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s36 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS zephyr-v2.2.0 *****
Hello World! lpcxpresso55s36
```
