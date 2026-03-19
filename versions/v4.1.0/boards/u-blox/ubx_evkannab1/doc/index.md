---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/u-blox/ubx_evkannab1/doc/index.html
original_path: boards/u-blox/ubx_evkannab1/doc/index.html
---

# u-blox EVK-ANNA-B11x

## Overview

The u-blox ANNA-B1 Evaluation Kit hardware is a Bluetooth low energy
module based on the Nordic Semiconductor nRF52832 ARM Cortex-M4F CPU
and has support for the following features:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy)
- RTC
- Segger RTT (RTT Console)
- SPI
- UART
- WDT

![../../../../_images/EVK-ANNA-B112.jpg](../../../../_images/EVK-ANNA-B112.jpg)

EVK ANNA-B1

More information about the ANNA-B1 module and the EVK-ANNA-B1
can be found at [ANNA-B1 product page](https://www.u-blox.com/en/product/anna-b112-open-cpu) [[1]](#id2) and
[EVK-ANNA-B1 product page](https://www.u-blox.com/en/product/evk-anna-b112) [[2]](#id4).

### Supported Features

The ubx\_evkannab1\_nrf52832 board configuration supports the
following hardware features:

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
| RADIO | on-chip | Bluetooth Low Energy |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.
See [EVK-ANNA-B1 product page](https://www.u-blox.com/en/product/evk-anna-b112) [[2]](#id4) and [ANNA-B1 Data Sheet](https://www.u-blox.com/en/docs/UBX-18011707) [[3]](#id7)
for a complete list of EVK ANNA-B1 hardware features.

### Connections and IOs

#### LED

- LED0 (red) = P0.27
- LED1 (green) = P0.25
- LED2 (blue) = P0.26

#### Push buttons

- BUTTON1 = SW1 = P0.25
- BUTTON2 = SW2 = P0.24

#### General information on module pin numbering

The numbering of the pins on the module and EVK do not follow the GPIO
numbering on the nRF52832 SoC. Please see the [ANNA-B1 Data Sheet](https://www.u-blox.com/en/docs/UBX-18011707) [[3]](#id7) for
information on how to map ANNA-B1 pins to the pin numbering on the
nRF52832 SoC.

The reason for this is the u-blox module family concept where different
modules share the same pinout and can be interchanged.

## Programming and Debugging

Applications for the `ubx_evkannab1/nrf52832` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details); however, the standard
debugging targets are not currently available.

### Flashing

Build and flash applications as usual (see
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Open a terminal program to the USB Serial Port installed when connecting
the board and listen for output.

Settings: 115200, 8N1, no flow control.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b ubx_evkannab1/nrf52832 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging boards
containing a Nordic Semiconductor chip with a Segger IC.

## Testing the LEDs and buttons in the EVK NINA-B11x

There are 2 samples that allow you to test that the buttons (switches)
and LEDs on the board are working properly with Zephyr:

```shell
samples/basic/blinky
samples/basic/button
```

You can build and flash the examples to make sure Zephyr is running
correctly on your board. The button and LED definitions can be found in
[boards/u-blox/ubx\_evkannab1/ubx\_evkannab1\_nrf52832.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/u-blox/ubx_evkannab1/ubx_evkannab1_nrf52832.dts).

Note that the buttons on the EVK-ANNA-B1 are marked SW1 and SW2, which
are named sw0 and sw1 in the dts file.
Also note that the SW1 button and the green LED are connected on HW level.

## References

[[1](#id3)]

[https://www.u-blox.com/en/product/anna-b112-open-cpu](https://www.u-blox.com/en/product/anna-b112-open-cpu)

[2]
([1](#id5),[2](#id6))

[https://www.u-blox.com/en/product/evk-anna-b112](https://www.u-blox.com/en/product/evk-anna-b112)

[3]
([1](#id8),[2](#id9))

[https://www.u-blox.com/en/docs/UBX-18011707](https://www.u-blox.com/en/docs/UBX-18011707)
