---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adafruit/nrf52_adafruit_feather/doc/index.html
original_path: boards/adafruit/nrf52_adafruit_feather/doc/index.html
---

# nRF52 Adafruit Feather

Board Overview

[![../../../../_images/nrf52_adafruit_feather.jpg](../../../../_images/nrf52_adafruit_feather.jpg)
](../../../../_images/nrf52_adafruit_feather.jpg)

nRF52 Adafruit Feather

Name:
:   `nrf52_adafruit_feather`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   nrf52832

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/nrf52_adafruit_feather/doc/index.rst/../..)

## Overview

The nRF52 Adafruit Bluefruit Feather hardware provides
support for the Nordic Semiconductor nRF52832 ARM Cortex-M4F CPU and
the following devices:

- NVIC
- RTC
- UART
- GPIO
- FLASH
- RADIO (Bluetooth Low Energy)
- Segger RTT (RTT Console)

More information about the board and its features can be found at the
[Adafruit Feather nRF52 Bluefruit Learning Guide](https://learn.adafruit.com/bluefruit-nrf52-feather-learning-guide/introduction) [[1]](#id2). The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[4]](#id9)
contains the processor’s information and the datasheet.

## Hardware

- nRF52832 ARM Cortex-M4F processor at 64 MHz
- 32.768 kHz crystal oscillator
- 512 KiB flash memory and 64 KiB of SRAM
- Battery connector and charger for 3.7 V lithium polymer batteries
- Charging indicator LED
- 2 User LEDs
- Reset button
- SWD connector
- USB serial converter

### Supported Features

The `nrf52_adafruit_feather` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The [Adafruit Feather nRF52 Bluefruit Learning Guide](https://learn.adafruit.com/bluefruit-nrf52-feather-learning-guide/introduction) [[1]](#id2) has detailed
information about the board including [pinouts](https://cdn-learn.adafruit.com/assets/assets/000/046/210/original/Feather_NRF52_Pinout_v1.2.pdf?1504807075) [[3]](#id7) and the [schematic](https://learn.adafruit.com/assets/39913) [[2]](#id5).

#### LED

- LED0 (red) = P0.17
- LED1 (blue) = P0.19

#### Push buttons

- DFU = SW0 = P0.20
- RESET = SW1 = P0.21/reset

## Programming and Debugging

The `nrf52_adafruit_feather` board is available in two different versions:

- [Adafruit Feather nRF52 Pro with myNewt Bootloader](https://www.adafruit.com/product/3574) [[6]](#id13)
  :   This board version is the recommended one to use. It has the SWD header
      already populated and comes with the Mynewt serial bootloader installed by
      default.
- [Adafruit Feather nRF52 Bluefruit LE](https://www.adafruit.com/product/3406) [[5]](#id11)
  :   This board is identical to the board above, but the SWD header is not
      populated and ships with an Arduino friendly bootloader. To be able to work
      with this version a 2\*5pin 0.5” SWD header (e.g. [Adafruit SWD connector](https://www.adafruit.com/product/752) [[7]](#id15))
      needs to be soldered.

Applications for the `nrf52_adafruit_feather` board configuration can be
built, flashed, and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

### Flashing

Flashing Zephyr onto the `nrf52_adafruit_feather` board requires an external
J-Link programmer. The programmer is attached to the X1 SWD header.

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b nrf52_adafruit_feather samples/hello_world
   ```
2. Connect the Adafruit nRF52 Feather to your host computer using USB
3. Run your favorite terminal program to listen for output.

   ```shell
   $ minicom -D <tty_device> -b 115200
   ```

   Replace `<tty_device>` with the port where the nRF52 Adafruit Feather
   board can be found. For example, under Linux, `/dev/ttyUSB0`.
4. Flash the image:

   ```shell
   west build -b nrf52_adafruit_feather samples/hello_world
   west flash
   ```

   You should see “Hello World! nrf52\_adafruit\_feather” in your terminal.

### Debugging

The `nrf52_adafruit_feather` board does not have an on-board J-Link debug IC
as some nRF5x development boards, however, instructions from the
[Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page also apply to this board, with the additional step
of connecting an external debugger.

## Testing the LEDs and buttons on the nRF52 Adafruit Feather

There are several samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")
- [Fade LED](../../../../samples/basic/fade_led/README.md#fade-led "Fade an LED using the PWM API.")
- [PWM Blinky](../../../../samples/basic/blinky_pwm/README.md#pwm-blinky "Blink an LED using the PWM API.")
- [Basic thread manipulation](../../../../samples/basic/threads/README.md#multi-thread-blinky "Spawn multiple threads that blink LEDs and print information to the console.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/adafruit/nrf52\_adafruit\_feather/board.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/nrf52_adafruit_feather/board.h).

## References

[1]
([1](#id3),[2](#id4))

[https://learn.adafruit.com/bluefruit-nrf52-feather-learning-guide/introduction](https://learn.adafruit.com/bluefruit-nrf52-feather-learning-guide/introduction)

[[2](#id6)]

[https://learn.adafruit.com/assets/39913](https://learn.adafruit.com/assets/39913)

[[3](#id8)]

[https://cdn-learn.adafruit.com/assets/assets/000/046/210/original/Feather\_NRF52\_Pinout\_v1.2.pdf?1504807075](https://cdn-learn.adafruit.com/assets/assets/000/046/210/original/Feather_NRF52_Pinout_v1.2.pdf?1504807075)

[[4](#id10)]

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)

[[5](#id12)]

[https://www.adafruit.com/product/3406](https://www.adafruit.com/product/3406)

[[6](#id14)]

[https://www.adafruit.com/product/3574](https://www.adafruit.com/product/3574)

[[7](#id16)]

[https://www.adafruit.com/product/752](https://www.adafruit.com/product/752)
