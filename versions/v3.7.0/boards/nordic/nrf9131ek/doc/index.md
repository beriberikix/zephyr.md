---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/nordic/nrf9131ek/doc/index.html
original_path: boards/nordic/nrf9131ek/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nRF9131 EK

## Overview

The nRF9131 EK (PCA10165) is a single-board evaluation kit for the nRF9131 SiP
for DECT NR+ and LTE-M/NB-IoT with GNSS.
The `nrf9131ek/nrf9131` board configuration provides support for the Nordic Semiconductor nRF9131 ARM
Cortex-M33F CPU with ARMv8-M Security Extension and the following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RTC
- Segger RTT (RTT Console)
- SPI
- UARTE
- WDT
- IDAU

![nRF9131 EK](../../../../_images/nrf9131ek_nrf9131.webp)

nRF9131 EK (Credit: Nordic Semiconductor)

The [Nordic Semiconductor TechDocs](https://docs.nordicsemi.com/) [[2]](#id4) will soon
contain the processor’s information and the datasheet.

## Hardware

nRF9131 EK has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 32 MHz.

### Supported Features

The `nrf9131ek/nrf9131` board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C(M) | on-chip | i2c |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| SPU | on-chip | system protection |
| UARTE | on-chip | serial |
| WDT | on-chip | watchdog |

### Connections and IOs

#### LED

- LED (red) = P0.29
- LED (green) = P0.30
- LED (blue) = P0.31

#### Push buttons and Switches

- BUTTON = P0.28
- RESET

### Security components

- Implementation Defined Attribution Unit ([IDAU](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau) [[1]](#id2)). The IDAU is implemented
  with the System Protection Unit and is used to define secure and non-secure
  memory maps. By default, all of the memory space (Flash, SRAM, and
  peripheral address space) is defined to be secure accessible only.
- Secure boot.

## Programming and Debugging

`nrf9131ek/nrf9131` supports the Armv8m Security Extension, and by default boots
in the Secure state.

### Building Secure/Non-Secure Zephyr applications with Arm® TrustZone®

Applications on the nRF9131 may contain a Secure and a Non-Secure firmware
image. The Secure image can be built using either Zephyr or
[Trusted Firmware M](https://www.trustedfirmware.org/projects/tf-m/) [[3]](#id6) (TF-M). Non-Secure firmware images are always built
using Zephyr. The two alternatives are described below.

Note

By default the Secure image for nRF9131 is built using TF-M.

#### Building the Secure firmware using Zephyr

The process requires the following steps:

1. Build the Secure Zephyr application using `-DBOARD=nrf9131ek/nrf9131` and
   `CONFIG_TRUSTED_EXECUTION_SECURE=y` in the application project configuration file.
2. Build the Non-Secure Zephyr application using `-DBOARD=nrf9131ek/nrf9131/ns`.
3. Merge the two binaries together.

#### Building the Secure firmware with TF-M

The process to build the Secure firmware image using TF-M and the Non-Secure
firmware image using Zephyr requires the following action:

1. Build the Non-Secure Zephyr application
   using `-DBOARD=nrf9131ek/nrf9131/ns`.
   To invoke the building of TF-M the Zephyr build system requires the
   Kconfig option `BUILD_WITH_TFM` to be enabled, which is done by
   default when building Zephyr as a Non-Secure application.
   The Zephyr build system will perform the following steps automatically:

   > - Build the Non-Secure firmware image as a regular Zephyr application
   > - Build a TF-M (secure) firmware image
   > - Merge the output binaries together
   > - Optionally build a bootloader image (MCUboot)

Note

Depending on the TF-M configuration, an application DTS overlay may be
required, to adjust the Non-Secure image Flash and SRAM starting address
and sizes.

When building a Secure/Non-Secure application, the Secure application will
have to set the IDAU (SPU) configuration to allow Non-Secure access to all
CPU resources utilized by the Non-Secure application firmware. SPU
configuration shall take place before jumping to the Non-Secure application.

### Building a Secure only application

Build the Zephyr app in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run)), using `-DBOARD=nrf9131ek/nrf9131`.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the nRF9131 EK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b nrf9131ek/nrf9131 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## Testing the LEDs and buttons in the nRF9131 EK

There are 2 samples that allow you to test that the button and LED on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/nordic/nrf9131ek/nrf9131ek\_nrf9131\_common.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf9131ek/nrf9131ek_nrf9131_common.dtsi).

## References

[[1](#id3)]

[https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau)

[[2](#id5)]

[https://docs.nordicsemi.com/](https://docs.nordicsemi.com/)

[[3](#id7)]

[https://www.trustedfirmware.org/projects/tf-m/](https://www.trustedfirmware.org/projects/tf-m/)
