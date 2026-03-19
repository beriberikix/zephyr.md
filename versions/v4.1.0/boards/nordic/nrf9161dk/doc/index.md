---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/nordic/nrf9161dk/doc/index.html
original_path: boards/nordic/nrf9161dk/doc/index.html
---

# nRF9161 DK

## Overview

The nRF9161 DK (PCA10153) is a single-board development kit for evaluation and
development on the nRF9161 SiP for DECT NR+ and LTE-M/NB-IoT with GNSS. The `nrf9161dk/nrf9161`
board configuration provides support for the Nordic Semiconductor nRF9161 ARM
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

More information about the board can be found at the
[nRF9161 DK website](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF9161-DK) [[2]](#id3). [nRF9161 Product Specification](https://docs.nordicsemi.com/bundle/ps_nrf9161/page/nRF9161_html5_keyfeatures.html) [[3]](#id6)
contains the processor’s information and the datasheet.

## Hardware

nRF9161 DK has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 32 MHz.

### Supported Features

The `nrf9161dk/nrf9161` board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| FLASH | external | spi |
| GPIO | on-chip | gpio |
| GPIO | external | i2c |
| I2C(M) | on-chip | i2c |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| RTC | on-chip | system clock |
| RTT | nRF53 | console |
| SPI(M/S) | on-chip | spi |
| SPU | on-chip | system protection |
| UARTE | on-chip | serial |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.
See [nRF9161 DK website](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF9161-DK) [[2]](#id3) and [nRF9161 Product Specification](https://docs.nordicsemi.com/bundle/ps_nrf9161/page/nRF9161_html5_keyfeatures.html) [[3]](#id6)
for a complete list of nRF9161 DK board hardware features.

### Connections and IOs

#### LED

- LED1 (green) = P0.0
- LED2 (green) = P0.1
- LED3 (green) = P0.4
- LED4 (green) = P0.5

#### Push buttons and Switches

- BUTTON1 = P0.8
- BUTTON2 = P0.9
- SWITCH1 = P0.18
- SWITCH2 = P0.19
- BOOT = SW5 = boot/reset

### Security components

- Implementation Defined Attribution Unit ([IDAU](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau) [[1]](#id1)). The IDAU is implemented
  with the System Protection Unit and is used to define secure and non-secure
  memory maps. By default, all of the memory space (Flash, SRAM, and
  peripheral address space) is defined to be secure accessible only.
- Secure boot.

## Programming and Debugging

`nrf9161dk/nrf9161` supports the Armv8m Security Extension, and by default boots
in the Secure state.

### Building Secure/Non-Secure Zephyr applications with Arm® TrustZone®

The process requires the following steps:

1. Build the Secure Zephyr application using `-DBOARD=nrf9161dk/nrf9161` and
   `CONFIG_TRUSTED_EXECUTION_SECURE=y` in the application project configuration file.
2. Build the Non-Secure Zephyr application using `-DBOARD=nrf9161dk/nrf9161/ns`.
3. Merge the two binaries together.

When building a Secure/Non-Secure application, the Secure application will
have to set the IDAU (SPU) configuration to allow Non-Secure access to all
CPU resources utilized by the Non-Secure application firmware. SPU
configuration shall take place before jumping to the Non-Secure application.

### Building a Secure only application

Build the Zephyr app in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run)), using `-DBOARD=nrf9161dk/nrf9161`.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the nRF9161 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b nrf9161dk/nrf9161 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## Testing the LEDs and buttons in the nRF9161 DK

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/nordic/nrf9161dk/nrf9161dk\_nrf9161\_common.dtsi](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nordic/nrf9161dk/nrf9161dk_nrf9161_common.dtsi).

## References

[[1](#id2)]

[https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau](https://developer.arm.com/docs/100690/latest/attribution-units-sau-and-idau)

[2]
([1](#id4),[2](#id5))

[https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF9161-DK](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF9161-DK)

[3]
([1](#id7),[2](#id8))

[https://docs.nordicsemi.com/bundle/ps\_nrf9161/page/nRF9161\_html5\_keyfeatures.html](https://docs.nordicsemi.com/bundle/ps_nrf9161/page/nRF9161_html5_keyfeatures.html)
