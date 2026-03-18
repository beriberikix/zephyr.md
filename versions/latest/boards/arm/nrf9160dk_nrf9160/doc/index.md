---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/nrf9160dk_nrf9160/doc/index.html
original_path: boards/arm/nrf9160dk_nrf9160/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nRF9160 DK

## Overview

The nRF9160 DK (PCA10090) is a single-board development kit for evaluation and
development on the nRF9160 SiP for LTE-M and NB-IoT. The nrf9160dk\_nrf9160
board configuration provides support for the Nordic Semiconductor nRF9160 ARM
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

![nRF9160 DK](../../../../_images/nrf9160dk_nrf9160.jpg)

nRF9160 DK (Credit: Nordic Semiconductor)

More information about the board can be found at the
[nRF9160 DK website](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF9160-DK) [[2]](#id4). The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[3]](#id7)
contains the processor’s information and the datasheet.

## Hardware

nRF9160 DK has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 32 MHz.

### Supported Features

The nrf9160dk\_nrf9160 board configuration supports the following
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

#### Additional hardware in v0.14.0+

Starting from v0.14.0, additional hardware is available on the DK:

- External flash memory (MX25R6435F, 64 Mb)
- I/O expander (PCAL6408A) that can be used to interface LEDs, slide switches,
  and buttons

To use this additional hardware, specify the revision of the board that
should be used when building your application (for more information, see
[Building for a board revision](../../../../develop/application/index.md#application-board-version)). For example, to build for nRF9160 DK v1.0.0:

Using west:

```shell
west build -b nrf9160dk_nrf9160@1.0.0
```

Using CMake and ninja:

```shell
mkdir build && cd build
cmake -GNinja -DBOARD=nrf9160dk_nrf9160@1.0.0 ..
ninja
```

Remember to also enable routing for this additional hardware in the firmware for
[nRF9160 DK - nRF52840](../../nrf9160dk_nrf52840/doc/index.md#nrf9160dk-nrf52840) (see [Board controller firmware](../../nrf9160dk_nrf52840/doc/index.md#nrf9160dk-board-controller-firmware)).

Other hardware features have not been enabled yet for this board.
See [nRF9160 DK website](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF9160-DK) [[2]](#id4) and [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[3]](#id7)
for a complete list of nRF9160 DK board hardware features.

### Connections and IOs

#### LED

- LED1 (green) = P0.2
- LED2 (green) = P0.3
- LED3 (green) = P0.4
- LED4 (green) = P0.5

#### Push buttons and Switches

- BUTTON1 = P0.6
- BUTTON2 = P0.7
- SWITCH1 = P0.8
- SWITCH2 = P0.9
- BOOT = SW5 = boot/reset

### Security components

- Implementation Defined Attribution Unit ([IDAU](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau) [[1]](#id2)). The IDAU is implemented
  with the System Protection Unit and is used to define secure and non-secure
  memory maps. By default, all of the memory space (Flash, SRAM, and
  peripheral address space) is defined to be secure accessible only.
- Secure boot.

## Programming and Debugging

nrf9160dk\_nrf9160 supports the Armv8m Security Extension, and by default boots
in the Secure state.

### Building Secure/Non-Secure Zephyr applications with Arm® TrustZone®

Applications on the nRF9160 may contain a Secure and a Non-Secure firmware
image. The Secure image can be built using either Zephyr or
[Trusted Firmware M](https://www.trustedfirmware.org/projects/tf-m/) [[4]](#id10) (TF-M). Non-Secure firmware images are always built
using Zephyr. The two alternatives are described below.

Note

By default the Secure image for nRF9160 is built using TF-M.

#### Building the Secure firmware using Zephyr

The process requires the following steps:

1. Build the Secure Zephyr application using `-DBOARD=nrf9160dk_nrf9160` and
   `CONFIG_TRUSTED_EXECUTION_SECURE=y` in the application project configuration file.
2. Build the Non-Secure Zephyr application using `-DBOARD=nrf9160dk_nrf9160_ns`.
3. Merge the two binaries together.

#### Building the Secure firmware with TF-M

The process to build the Secure firmware image using TF-M and the Non-Secure
firmware image using Zephyr requires the following action:

1. Build the Non-Secure Zephyr application
   using `-DBOARD=nrf9160dk_nrf9160_ns`.
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
and [Run an Application](../../../../develop/application/index.md#application-run)), using `-DBOARD=nrf9160dk_nrf9160`.

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

Replace `<tty_device>` with the port where the nRF9160 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b nrf9160dk_nrf9160 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## Testing the LEDs and buttons in the nRF9160 DK

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/arm/nrf9160dk\_nrf9160/nrf9160dk\_nrf9160\_common.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/nrf9160dk_nrf9160/nrf9160dk_nrf9160_common.dtsi).

## References

[[1](#id3)]

[https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau)

[2]
([1](#id5),[2](#id6))

[https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF9160-DK](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF9160-DK)

[3]
([1](#id8),[2](#id9))

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)

[[4](#id11)]

[https://www.trustedfirmware.org/projects/tf-m/](https://www.trustedfirmware.org/projects/tf-m/)
