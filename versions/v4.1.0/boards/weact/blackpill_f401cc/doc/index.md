---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/weact/blackpill_f401cc/doc/index.html
original_path: boards/weact/blackpill_f401cc/doc/index.html
---

# Black Pill V1.2

Board Overview

[![../../../../_images/blackpill-v3.jpg](../../../../_images/blackpill-v3.jpg)
](../../../../_images/blackpill-v3.jpg)

Black Pill V1.2

Name:
:   `blackpill_f401cc`

Vendor:
:   WeAct Studio

Architecture:
:   arm

SoC:
:   stm32f401xc

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/weact/blackpill_f401cc/doc/index.rst/../..)

## Overview

The WeAct Black Pill V1.2 Board is an extremely low cost and bare-bones
development board featuring the STM32F401CC, see [STM32F401CC website](https://www.st.com/en/microcontrollers/stm32f401cc.html) [[5]](#id10).
This is the 48-pin variant of the STM32F401x series,
see [STM32F401x reference manual](https://www.st.com/resource/en/reference_manual/dm00096844.pdf) [[6]](#id12). More info about the board available
[here](https://stm32-base.org/boards/STM32F401CCU6-WeAct-Black-Pill-V1.2.html) [[3]](#id6) and on [WeAct Github](https://github.com/WeActStudio/WeActStudio.MiniSTM32F4x1) [[2]](#id4).

## Hardware

The STM32F401CC based Black Pill V3.0+ Board provides the following
hardware components:

- STM32F401CCU6 in UFQFPN48 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 84 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 256 KB Flash
- 64 KB SRAM
- GPIO with external interrupt capability
- 1x12-bit, 2.4 MSPS ADC with 16 channels
- DMA Controller
- Up to 11 Timers (six 16-bit, two 32-bit, two watchdog timers and a SysTick timer)
- USART/UART (3)
- I2C (3)
- SPI/I2S (5)
- SDIO
- USB 2.0 full-speed device/host/OTG controller with on-chip PHY
- CRC calculation unit
- 96-bit unique ID
- RTC

### Supported Features

The `blackpill_f401cc` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

#### Available pins:

![Black Pill V1.2 Pinout](../../../../_images/Blackpill_Pinout.jpg)

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PA9/PA10
- I2C1 SCL/SDA : PB8/PB9
- SPI1 CS/SCK/MISO/MOSI : PA4/PA5/PA6/PA7 (Routed to footprint for external flash)
- PWM\_4\_CH1 : PB6
- PWM\_4\_CH2 : PB7
- ADC\_1 : PA1
- USER\_PB : PA0
- USER\_LED : PC13

#### Clock Sources

The board has two external oscillators. The frequency of the slow clock (LSE) is
32.768 kHz. The frequency of the main clock (HSE) is 25 MHz.

The default configuration sources the system clock from the PLL, which is
derived from HSE, and is set at 84MHz, which is the maximum possible frequency
to achieve a stable USB clock (42MHz).

## Programming and Debugging

There are 2 main entry points for flashing STM32F4X SoCs, one using the ROM
bootloader, and another by using the SWD debug port (which requires additional
hardware). Flashing using the ROM bootloader requires a special activation
pattern, which can be triggered by using the BOOT0 pin.

### Flashing

#### Installing dfu-util

It is recommended to use at least v0.8 of [dfu-util](http://dfu-util.sourceforge.net/build.html) [[4]](#id8). The package available in
debian/ubuntu can be quite old, so you might have to build dfu-util from source.

There is also a Windows version which works, but you may have to install the
right USB drivers with a tool like [Zadig](https://zadig.akeo.ie/) [[1]](#id2).

#### Flashing an Application

Connect a USB-C cable and the board should power ON. Force the board into DFU mode
by keeping the BOOT0 switch pressed while pressing and releasing the NRST switch.

The dfu-util runner is supported on this board and so a sample can be built and
tested easily.

```shell
# From the root of the zephyr repository
west build -b blackpill_f401cc samples/basic/blinky
west flash
```

### Debugging

The board can be debugged by installing the included 100 mil (0.1 inch) header,
and attaching an SWD debugger to the 3V3 (3.3V), GND, SCK, and DIO
pins on that header.

## References

[[1](#id3)]

[https://zadig.akeo.ie/](https://zadig.akeo.ie/)

[[2](#id5)]

[https://github.com/WeActStudio/WeActStudio.MiniSTM32F4x1](https://github.com/WeActStudio/WeActStudio.MiniSTM32F4x1)

[[3](#id7)]

[https://stm32-base.org/boards/STM32F401CCU6-WeAct-Black-Pill-V1.2.html](https://stm32-base.org/boards/STM32F401CCU6-WeAct-Black-Pill-V1.2.html)

[[4](#id9)]

[http://dfu-util.sourceforge.net/build.html](http://dfu-util.sourceforge.net/build.html)

[[5](#id11)]

[https://www.st.com/en/microcontrollers/stm32f401cc.html](https://www.st.com/en/microcontrollers/stm32f401cc.html)

[[6](#id13)]

[https://www.st.com/resource/en/reference\_manual/dm00096844.pdf](https://www.st.com/resource/en/reference_manual/dm00096844.pdf)
