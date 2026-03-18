---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/arduino/due/doc/index.html
original_path: boards/arduino/due/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Arduino Due

## Overview

The arduino\_due board configuration is used by Zephyr applications
that run on the Arduino Due board. It provides support for the Atmel
SAM3X8E ARM Cortex-M3 CPU and the following devices:

- Nested Vectored Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)
- Serial Port over USB (ATMEL\_SAM3)

More information about the board can be found at the [Arduino Due website](https://www.arduino.cc/en/Main/ArduinoBoardDue).
The [Atmel SAM3X8E Datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A_Datasheet.pdf) has the information and the datasheet about
the processor.

Note

This configuration is not supported by Arduino.

![Arduino Due](../../../../_images/arduino_due.jpg)

## Hardware

### Supported Features

The arduino\_due board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| SYSTICK | on-chip | system clock |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| Watchdog | on-chip | watchdog |

Other hardware features are not currently supported by the Zephyr kernel.
See [Arduino Due website](https://www.arduino.cc/en/Main/ArduinoBoardDue) and [Atmel SAM3X8E Datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-11057-32-bit-Cortex-M3-Microcontroller-SAM3X-SAM3A_Datasheet.pdf) for a complete
list of Arduino Due board hardware features.

The default configuration can be found in the Kconfig
[boards/arduino/due/arduino\_due\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/due/arduino_due_defconfig).

Note

For I2C, pull-up resistors are required for using SCL1 and SDA1 (near IO13).

### Interrupt Controller

There are 15 fixed exceptions including exceptions 12 (debug monitor) and 15
(SYSTICK) that behave more as interrupts than exceptions. In addition, there can
be a variable number of IRQs. Exceptions 7-10 and 13 are reserved. They don’t
need handlers.

A Cortex-M3/4-based board uses vectored exceptions. This means each exception
calls a handler directly from the vector table.

Handlers are provided for exceptions 1-6, 11-12, and 14-15. The table here
identifies the handlers used for each exception.

| Exc# | Name | Remarks | Used by Zephyr Kernel |
| --- | --- | --- | --- |
| 1 | Reset |  | system initialization |
| 2 | NMI |  | system fatal error |
| 3 | Hard fault |  | system fatal error |
| 4 | MemManage | MPU fault | system fatal error |
| 5 | Bus |  | system fatal error |
| 6 | Usage fault | undefined instruction, or switch attempt to ARM mode | system fatal error |
| 11 | SVC |  | system calls, kernel run-time exceptions, and IRQ offloading |
| 12 | Debug monitor |  | system fatal error |
| 14 | PendSV |  | context switch |
| 15 | SYSTICK |  | system clock |

Note

After a reset, all exceptions have a priority of 0. Interrupts cannot run
at priority 0 for the interrupt locking mechanism and exception handling
to function properly.

### System Clock

Arduino Due has two external oscillators/resonators. The slow clock is
32.768 kHz, and the main clock is 12 MHz. The processor can set up PLL to drive
the master clock, which can be set as high as 84 MHz.

### Serial Port

The Atmel SAM3X8E processor has a single UART that is used by the SAM-BA
bootloader. This UART has only two wires for RX/TX and does not have flow
control (CTS/RTS) or FIFO. The RX/TX pins are connected to the ATmega16U2,
which provides USB-to-TTL serial function. The Zephyr console output, by
default, is utilizing this controller.

## Programming and Debugging

### Flashing

#### BOSSA Tool

Flashing the Zephyr kernel onto Arduino Due requires the [bossa tool](https://github.com/shumatech/BOSSA).

There are GUI and command line versions of the bossa tool. The following
section provides the steps to build the command line version. Please
refer to the bossa tool’s README file on how to build the GUI version.

To build the bossa tool, follow these steps:

1. Checkout the bossa tool’s code from the repository.

   ```shell
   $ git clone https://github.com/shumatech/BOSSA.git
   $ cd BOSSA
   ```
2. Checkout the arduino branch. The code on the master branch does not
   work with Arduino Due.

   ```shell
   $ git checkout arduino
   ```
3. Build the command line version of the bossa tool.

   ```shell
   $ make bin/bossac
   ```
4. The resulting binary is available at `bin/bossac`.

#### Flashing an Application to Arduino Due

Applications for the `arduino_due` board configuration can be built
and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application. After
building the application, press the Reset button before running the
flash command, so the board will boot into the SAM-BA bootloader and
be prepared to receive the new program.

```shell
# From the root of the zephyr repository
west build -b arduino_due samples/hello_world
west flash
```

After flashing the application, run your favorite terminal program to
listen for output. For example, under Linux, the terminal should be
`/dev/ttyACM0`. For example:

```shell
$ sudo minicom -D /dev/ttyACM0 -o
```

The -o option tells minicom not to send the modem initialization
string.

Now press the Reset button and you should see “Hello World! arduino\_due” in your terminal.

Note

Make sure your terminal program is closed before flashing the binary image,
or it will interfere with the flashing process.

## References
