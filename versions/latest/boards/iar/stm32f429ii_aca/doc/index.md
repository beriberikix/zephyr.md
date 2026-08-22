---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/iar/stm32f429ii_aca/doc/index.html
original_path: boards/iar/stm32f429ii_aca/doc/index.html
---

# STM32F429II-ACA

Board Overview

[![../../../../_images/stm32f429ii_aca.webp](../../../../_images/stm32f429ii_aca.webp)
](../../../../_images/stm32f429ii_aca.webp)

STM32F429II-ACA

Name:
:   `stm32f429ii_aca`

Vendor:
:   IAR Systems AB

Architecture:
:   arm

SoC:
:   stm32f429xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/iar/stm32f429ii_aca/doc/index.rst/../..)

## Overview

The IAR STM32F429II-ACA evaluation board features an ARM Cortex-M4 based STM32F429II MCU.
Here are some highlights of the STM32F429II-ACA board:

- STM32 microcontroller in LQFP144 package
- JTAG/SWD debugger/programmer interface
- Flexible board power supply

  - JTAG/SWD connector
  - USB HS connector
- 3x user push-buttons and 1x RESET push-button
- Open-close switch and on-auto-off switch
- 2x capacitive touch panels
- USB OTG with mini-USB connector
- Small speaker
- Trimmer potentiometer
- Nine LEDs

  - 1x power LED
  - 3x car traffic light LEDs
  - 2x pedestrian traffic light LEDs
  - 1x car interior light LED
  - 2x user LEDs

Schematics for the board can be found [here](https://iar.my.salesforce.com/sfc/p/#30000000YATY/a/Qx000000vZVh/EzlIqYKIBVXN8PN4Q8MgtowSZrR_vZarwLiNJXw7UJw) [[1]](#id2)

## Hardware

The STM32F429II-ACA evaluation board provides the following hardware components:

- STM32F429II in LQFP144 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 180 MHz max CPU frequency
- VDD from 1.8 V to 3.6 V
- 2 MB Internal Flash
- 4 Mbit External Flash
- 256+4 KB SRAM including 64-KB of core coupled memory
- GPIO with external interrupt capability
- 12-bit ADC
- 12-bit DAC
- RTC
- General Purpose Timers
- I2C
- SPI
- USB 2.0 OTG HS/FS with dedicated DMA, on-chip full-speed PHY and ULPI
- CRC calculation unit
- True random number generator
- DMA Controller

More information about STM32F429II can be found here:

- [STM32F429II on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32f429ii.html) [[2]](#id4)
- [STM32F429 Reference Manual](https://www.st.com/content/ccc/resource/technical/document/reference_manual/3d/6d/5a/66/b4/99/40/d4/DM00031020.pdf/files/DM00031020.pdf/jcr:content/translations/en.DM00031020.pdf) [[3]](#id6)

### Supported Features

The `stm32f429ii_aca` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### Default Zephyr Peripheral Mapping:

- I2C\_1\_SCL : PB8
- I2C\_1\_SDA : PB7
- I2C\_2\_SCL : PH4
- I2C\_2\_SDA : PH5
- SPI\_5\_NSS : PF6
- SPI\_5\_SCK : PF7
- SPI\_5\_MISO : PF8
- SPI\_5\_MOSI : PF9
- OTG\_HS\_ID : PB12
- OTG\_HS\_DM : PB14
- OTG\_HS\_DP : PB15

### Serial Port

By default, the STM32F429II-ACA evaluation board has no physical serial port available.
The board has up to 8 UARTs, of which none are used.

### USB Port

The STM32F429II-ACA evaluation board has a USB HS capable Mini-USB port. It is connected to the on-chip
OTG\_HS peripheral.

## Programming and Debugging

Applications for the `stm32f429ii_aca` board configuration can be built
and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

In order to flash this board using west, an external debug probe such as a Segger J-Link
has to be connected through the JTAG/SWD connector on the board.
By default, the board is set to be flashed using the jlink runner.
Alternatively, openocd, or pyocd can also be used as runners to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner pyocd
```

First, connect the STM32F429II-ACA evaluation board to your host computer using
your debug probe through the JTAG/SWD connector to prepare it for flashing.
Then build and flash your application.

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f429ii_aca samples/basic/blinky
west flash
```

LED0 should then begin to blink continuously with a 1-second delay.

## References

[[1](#id3)]

[https://iar.my.salesforce.com/sfc/p/#30000000YATY/a/Qx000000vZVh/EzlIqYKIBVXN8PN4Q8MgtowSZrR\_vZarwLiNJXw7UJw](https://iar.my.salesforce.com/sfc/p/#30000000YATY/a/Qx000000vZVh/EzlIqYKIBVXN8PN4Q8MgtowSZrR_vZarwLiNJXw7UJw)

[[2](#id5)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32f429ii.html](https://www.st.com/en/microcontrollers-microprocessors/stm32f429ii.html)

[[3](#id7)]

[https://www.st.com/content/ccc/resource/technical/document/reference\_manual/3d/6d/5a/66/b4/99/40/d4/DM00031020.pdf/files/DM00031020.pdf/jcr:content/translations/en.DM00031020.pdf](https://www.st.com/content/ccc/resource/technical/document/reference_manual/3d/6d/5a/66/b4/99/40/d4/DM00031020.pdf/files/DM00031020.pdf/jcr:content/translations/en.DM00031020.pdf)
