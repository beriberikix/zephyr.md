---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/ubx_evkninab1_nrf52832/doc/index.html
original_path: boards/arm/ubx_evkninab1_nrf52832/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# u-blox EVK NINA-B11x

## Overview

The u-blox NINA-B1 Evaluation Kit hardware is a Bluetooth
low energy module based on the Nordic Semiconductor nRF52832
ARM Cortex-M4F CPU and has support for the following features:

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

![../../../../_images/EVK-NINA-B1.jpg](../../../../_images/EVK-NINA-B1.jpg)

EVK NINA-B1

More information about the NINA-B1 module and the EVK NINA-B1
can be found at [NINA-B1 product page](https://www.u-blox.com/en/product/nina-b1-series-open-cpu) [[1]](#id2) and
[EVK-NINA-B1 product page](https://www.u-blox.com/en/product/evk-nina-b1) [[2]](#id4).

### Supported Features

The ubx\_evkninab1\_nrf52832 board configuration supports the
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

Note

Most Arduino interfaces are supported. Arduino pins
D5 and D8 are not available, so arduino\_gpio is
disabled. On the EVK-NINA-B1, these pins are
assigned to SWDIO and SWDCLK, respectively.

Other hardware features have not been enabled yet for this board.
See [EVK-NINA-B1 product page](https://www.u-blox.com/en/product/evk-nina-b1) [[2]](#id4) and [NINA-B1 Data Sheet](https://www.u-blox.com/en/docs/UBX-15019243) [[3]](#id7)
for a complete list of EVK NINA-B1 hardware features.

### Connections and IOs

#### LED

- LED0 (red) = P0.08
- LED1 (green) = P0.16
- LED2 (blue) = P0.18

#### Push buttons

- BUTTON1 = SW1 = P0.16
- BUTTON2 = SW2 = P0.30

#### General information on module pin numbering

The numbering of the pins on the module and EVK do not follow the GPIO
numbering on the nRF52832 SoC. Please see the [NINA-B1 Data Sheet](https://www.u-blox.com/en/docs/UBX-15019243) [[3]](#id7) for
information on how to map NINA-B1 pins to the pin numbering on the
nRF52832 SoC.

The reason for this is the u-blox module family concept where different
modules share the same pinout and can be interchanged, see
[NINA module family Nested design](https://www.u-blox.com/en/docs/UBX-17065600) [[4]](#id10).

## Programming and Debugging

Applications for the `ubx_evkninab1_nrf52832` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details); however, the standard
debugging targets are not currently available.

### Flashing

Build and flash applications as usual (see
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

Open a terminal program to the USB Serial Port installed when connecting
the board and listen for output.

Settings: 115200, 8N1, no flow control.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b ubx_evkninab1_nrf52832 samples/hello_world
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
[boards/arm/ubx\_evkninab1\_nrf52832/ubx\_evkninab1\_nrf52832.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/ubx_evkninab1_nrf52832/ubx_evkninab1_nrf52832.dts).

Note that the buttons on the EVK-NINA-B1 are marked SW1 and SW2, which
are named sw0 and sw1 in the dts file.
Also note that the SW1 button and the green LED are connected on HW level.

## References

[[1](#id3)]

[https://www.u-blox.com/en/product/nina-b1-series-open-cpu](https://www.u-blox.com/en/product/nina-b1-series-open-cpu)

[2]
([1](#id5),[2](#id6))

[https://www.u-blox.com/en/product/evk-nina-b1](https://www.u-blox.com/en/product/evk-nina-b1)

[3]
([1](#id8),[2](#id9))

[https://www.u-blox.com/en/docs/UBX-15019243](https://www.u-blox.com/en/docs/UBX-15019243)

[[4](#id11)]

[https://www.u-blox.com/en/docs/UBX-17065600](https://www.u-blox.com/en/docs/UBX-17065600)
