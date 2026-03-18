---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/stm32f030_demo/doc/index.html
original_path: boards/arm/stm32f030_demo/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# STM32F030 DEMO BOARD

This board has the bare minimum components required to power on
the STM32F030F4P6 MCU. Most of the GPIOs on the STM32 SoC have
been exposed in the external headers with silk screen labels
that match the SoC’s pin names.

For practical use, you’ll need to add additional components
and circuits using a breadboard, for example.

![STM32F030 DEMO BOARD](../../../../_images/stm32f030_demo.jpg)

More information about the board can be found at the [stm32-base.org website](https://stm32-base.org/boards/STM32F030F4P6-STM32F030-DEMO-BOARD-V1.1) [[1]](#id1).

More information about STM32F030F4P6 can be found here:

- [STM32F030 reference manual](https://www.st.com/resource/en/reference_manual/dm00091010.pdf) [[2]](#id3)
- [STM32F030 data sheet](https://www.st.com/resource/en/datasheet/stm32f030f4.pdf) [[3]](#id5)

## Hardware

- STM32F030F4P6 ARM Cortex-M0 processor, frequency up to 48 MHz
- 16 KiB of flash memory and 4 KiB of RAM
- 8 MHz quartz crystal
- 1 user LED
- One reset button
- 2-way jumper (BOOT0)
- Serial (1x4 male dupont (2.54mm))
- SWD (1x4 male dupont (2.54mm))
- USB port (power only)

### Supported Features

The Zephyr stm32f030\_demo board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| WATCHDOG | on-chip | independent watchdog |
| die-temp | on-chip | die temperature sensor |

Other hardware features are not yet supported on this Zephyr porting.

The default configuration can be found in the defconfig file:
`boards/arm/stm32f030_demo/stm32f030_demo_defconfig`

### Pin Mapping

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PA9/PA10
- LED : PA4

## Programming and Debugging

Applications for the `stm32f030_demo` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board can be flashed by using ST-LINKV2 in-circuit debugger and programmer.
This interface is supported by the openocd version included in the Zephyr SDK.

#### Flashing an application to STM32F030 DEMO BOARD

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f030_demo samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32f030_demo samples/basic/blinky
west debug
```

## References

[[1](#id2)]

[https://stm32-base.org/boards/STM32F030F4P6-STM32F030-DEMO-BOARD-V1.1](https://stm32-base.org/boards/STM32F030F4P6-STM32F030-DEMO-BOARD-V1.1)

[[2](#id4)]

[https://www.st.com/resource/en/reference\_manual/dm00091010.pdf](https://www.st.com/resource/en/reference_manual/dm00091010.pdf)

[[3](#id6)]

[https://www.st.com/resource/en/datasheet/stm32f030f4.pdf](https://www.st.com/resource/en/datasheet/stm32f030f4.pdf)
