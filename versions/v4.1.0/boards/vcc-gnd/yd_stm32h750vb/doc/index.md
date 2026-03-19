---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/vcc-gnd/yd_stm32h750vb/doc/index.html
original_path: boards/vcc-gnd/yd_stm32h750vb/doc/index.html
---

# YD-STM32H750VB

Board Overview

[![../../../../_images/yd_stm32h750vb.png](../../../../_images/yd_stm32h750vb.png)
](../../../../_images/yd_stm32h750vb.png)

YD-STM32H750VB

Name:
:   `yd_stm32h750vb`

Vendor:
:   VCC-GND Studio

Architecture:
:   arm

SoC:
:   stm32h750xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/vcc-gnd/yd_stm32h750vb/doc/index.rst/../..)

## Overview

The YD-STM32H750VB development board is a complete demonstration and development
platform for Arm® Cortex®-M7 core-based STM32H750VBT6 microcontroller, with
128Kbytes of Flash memory and 1 Mbytes of SRAM.

More information about STM32H750 can be found here:

- [STM32H750 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32h750-value-line.html) [[3]](#id6)
- [STM32H750xx reference manual](https://www.st.com/resource/en/reference_manual/rm0433-stm32h742-stm32h743753-and-stm32h750-value-line-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) [[4]](#id8)
- [STM32H750xx datasheet](https://www.st.com/resource/en/datasheet/stm32h750vb.pdf) [[5]](#id10)

### Supported Features

The `yd_stm32h750vb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- LED\_1 : PA13 (SWDIO)
- LED\_2 : PA14 (SWCLK)
- LED\_3 : PA15
- LED\_4 : PB4
- KEY : PB3

### System Clock

The STM32H750VB System Clock can be driven by an internal or external oscillator,
as well as by the main PLL clock. By default, the System clock
is driven by the PLL clock at 480MHz. PLL clock is feed by a 25MHz high speed external clock.

### Flashing

There are 2 main entry points for flashing STM32H750VB SoCs, one using the ROM
bootloader, and another by using the SWD debug port (which requires additional
hardware such as ST-Link). Flashing using the ROM bootloader requires a special activation
pattern, which can be triggered by using the BOOT0 button.

#### Installing dfu-util

It is recommended to use at least v0.8 of [dfu-util](http://dfu-util.sourceforge.net/build.html) [[2]](#id4). The package available in
debian/ubuntu can be quite old, so you might have to build dfu-util from source.

There is also a Windows version which works, but you may have to install the
right USB drivers with a tool like [Zadig](https://zadig.akeo.ie/) [[1]](#id2).

#### Flashing an application to YD-STM32H750VB

Connect a USB-C cable and the board should power ON. Force the board into DFU mode
by keeping the BOOT0 switch pressed while pressing and releasing the RST switch.

The dfu-util runner is supported on this board and so a sample can be built and
tested easily.

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b yd_stm32h750vb samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b yd_stm32h750vb samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://zadig.akeo.ie/](https://zadig.akeo.ie/)

[[2](#id5)]

[http://dfu-util.sourceforge.net/build.html](http://dfu-util.sourceforge.net/build.html)

[[3](#id7)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32h750-value-line.html](https://www.st.com/en/microcontrollers-microprocessors/stm32h750-value-line.html)

[[4](#id9)]

[https://www.st.com/resource/en/reference\_manual/rm0433-stm32h742-stm32h743753-and-stm32h750-value-line-advanced-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0433-stm32h742-stm32h743753-and-stm32h750-value-line-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

[[5](#id11)]

[https://www.st.com/resource/en/datasheet/stm32h750vb.pdf](https://www.st.com/resource/en/datasheet/stm32h750vb.pdf)
