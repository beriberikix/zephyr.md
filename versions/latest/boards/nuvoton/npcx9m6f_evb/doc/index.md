---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/nuvoton/npcx9m6f_evb/doc/index.html
original_path: boards/nuvoton/npcx9m6f_evb/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Nuvoton NPCX9M6F\_EVB

## Overview

The NPCX9M6F\_EVB kit is a development platform to evaluate the
Nuvoton NPCX9 series microcontrollers. This board needs to be mated with
part number NPCX996F.

![NPCX9M6F Evaluation Board](../../../../_images/npcx9m6f_evb.jpg)

## Hardware

- ARM Cortex-M4F Processor
- 256 KB RAM and 64 KB boot ROM
- ADC & GPIO headers
- UART0 and UART1
- FAN PWM interface
- Jtag interface
- Intel Modular Embedded Controller Card (MECC) headers

### Supported Features

The following features are supported:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| ADC | on-chip | adc controller |
| CLOCK | on-chip | reset and clock control |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c port/controller |
| PINMUX | on-chip | pinmux |
| PM | on-chip | power management |
| PSL | on-chip | power switch logic |
| PWM | on-chip | pulse width modulator |
| TACH | on-chip | tachometer sensor |
| UART | on-chip | serial port-polling; serial port-interrupt |
| WDT | on-chip | watchdog |

Other hardware features are not currently supported by Zephyr (at the moment)

The default configuration can be found in the defconfig file:
[boards/nuvoton/npcx9m6f\_evb/npcx9m6f\_evb\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nuvoton/npcx9m6f_evb/npcx9m6f_evb_defconfig)

### Connections and IOs

Nuvoton to provide the schematic for this board.

### System Clock

The NPCX9M6F MCU is configured to use the 90Mhz internal oscillator with the
on-chip PLL to generate a resulting EC clock rate of 15 MHz. See Processor clock
control register (chapter 4 in user manual)

### Serial Port

UART1 is configured for serial logs.

## Programming and Debugging

This board comes with a Cortex ETM port which facilitates tracing and debugging
using a single physical connection. In addition, it comes with sockets for
JTAG-only sessions.

### Flashing

If the correct IDC headers are installed, this board supports both J-TAG and
also the ChromiumOS servo.

To flash using Servo V2, μServo, or Servo V4 (CCD), see the
[Chromium EC Flashing Documentation](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board) [[1]](#id1) for more information.

To flash with J-TAG, install the drivers for your programmer, for example:
SEGGER J-link’s drivers are at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

```shell
# From the root of the zephyr repository
west build -b npcx9m6f_evb samples/basic/blinky
west flash
```

### Debugging

Use JTAG/SWD with a J-Link

## References

[[1](#id2)]

[https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board](https://chromium.googlesource.com/chromiumos/platform/ec#Flashing-via-the-servo-debug-board)
