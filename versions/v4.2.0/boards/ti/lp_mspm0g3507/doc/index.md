---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ti/lp_mspm0g3507/doc/index.html
original_path: boards/ti/lp_mspm0g3507/doc/index.html
---

# MSPM0G3507 Launchpad

Board Overview

[![../../../../_images/lp_mspm0g3507.webp](../../../../_images/lp_mspm0g3507.webp)
](../../../../_images/lp_mspm0g3507.webp)

MSPM0G3507 Launchpad

Name:
:   `lp_mspm0g3507`

Vendor:
:   Texas Instruments

Architecture:
:   arm

SoC:
:   mspm0g3507

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/lp_mspm0g3507/doc/index.rst/../..)

## Overview

MSPM0G350x microcontrollers (MCUs) are part of the MSP highly integrated, ultra-low-power 32-bit MCU
family based on the enhanced Arm® Cortex®-M0+ 32-bit core platform operating at up to 80-MHz frequency.
These cost-optimized MCUs offer high-performance analog peripheral integration, support extended temperature
ranges from -40°C to 125°C, and operate with supply voltages ranging from 1.62 V to 3.6 V.

The MSPM0G350x devices provide up to 128KB embedded flash program memory with built-in error correction
code (ECC) and up to 32KB SRAM with a hardware parity option. These MCUs also incorporate a
memory protection unit, 7-channel DMA, math accelerator, and a variety of peripherals including

- Analog.

  - Two 12-bit 4-Msps ADCs.
  - Configurable internal shared voltage reference.
  - One 12-bit 1-Msps DAC.
  - Three high speed comparators with built-in reference DACs.
  - Two zero-drift zero-crossover op-amps with programmable gain.
- Digital.

  - Two 16-bit advanced control timers.
  - Five general-purpose timers.

    - One 16-bit general-purpose timer for QEI interface.
    - One 32-bit high resolution general-purpose timer.
    - Two 16-bit timers with deadband support and up to 12 PWM Channels.
  - Two windowed-watchdog timers.
  - One RTC with alarm and calendar modes.
- Data Integrity and Encryption.

  - One AES HW accelerator capable of CTR, CBC, and ECB modes.
  - One Cyclic Redundancy Check (CRC) accelerator.
  - One True Random Number Generator (TRNG).
- Communication.

  - Four UARTs, one with support for advanced modes such as LIN and Manchester.
  - Two I2C supporting SMBUS/PMBUS and speeds up to FM+ (1Mbits/s).
  - Two SPI, one with max speed 32Mbits/s.
  - One CAN interface supporting CAN 2.0 A or B and CAN-FD.

![MSPM0G3507 LaunchPad development board](../../../../_images/lp_mspm0g35071.webp)

Zephyr uses the `lp_mspm0g3507` board for building LP\_MSPM0G3507

## Features:

- Onboard XDS110 debug probe
- EnergyTrace technology available for ultra-low-power debugging
- 2 buttons, 1 LED and 1 RGB LED for user interaction
- Temperature sensor circuit
- Light sensor circuit
- External OPA2365 (default buffer mode) for ADC (up to 4 Msps) evaluation
- Onboard 32.768-kHz and 40-MHz crystals
- RC filter for ADC input (unpopulated by default)

Details on the MSPM0G3507 LaunchPad can be found on the [TI LP\_MSPM0G3507 Product Page](https://www.ti.com/tool/LP-MSPM0G3507).

### Supported Features

The `lp_mspm0g3507` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Building and Flashing

### Building

Follow the [Getting Started Guide](../../../../develop/getting_started/index.md#getting-started) instructions for Zephyr application development.

For example, to build the blinky application for the MSPM0G3507 LaunchPad:

```shell
# From the root of the zephyr repository
west build -b lp_mspm0g3507 samples/hello_world
```

The resulting `zephyr.bin` binary in the build directory can be flashed onto
MSPM0G3507 LaunchPad using the steps mentioned below.

### Flashing

Open OCD is used to program the flash memory on the devices. It may be necessary in
earlier versions to use a branch of open OCD onto the device.

Before OpenOCD is public, one can clone [This Repo](https://github.com/openocd-org/openocd.git),
and then this can be built with

```shell
$ cd <cloned_OPENOCD_dir>
$ ./bootstrap (when building from the git repository)
$ ./configure
$ make
$ sudo make install
```

Then after the build, it is possible to flash the device by passing additional arguments to the flash command

```shell
$ west flash --openocd <path to cloned dir>/src/openocd --openocd-search <path to cloned dir>/tcl
```

Flashing using JLINK

```shell
$ west flash --runner jlink
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b lp_mspm0g3507 samples/hello_world
west debug
```

## References

TI MSPM0 MCU Page:
:   [https://www.ti.com/microcontrollers-mcus-processors/arm-based-microcontrollers/arm-cortex-m0-mcus/overview.html](https://www.ti.com/microcontrollers-mcus-processors/arm-based-microcontrollers/arm-cortex-m0-mcus/overview.html)

TI MSPM0G3507 Product Page:
:   [https://www.ti.com/product/MSPM0G3507](https://www.ti.com/product/MSPM0G3507)

TI MSPM0 SDK:
:   [https://www.ti.com/tool/MSPM0-SDK](https://www.ti.com/tool/MSPM0-SDK)
