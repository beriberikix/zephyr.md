---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/stm32l1_disco/doc/index.html
original_path: boards/arm/stm32l1_disco/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ST STM32L1 Discovery

## Overview

The two generations of the STM32L1 Discovery development boards come with
an integrated ST-LINK/V2 debugger and programmer. The boards have a
24-segment LCD and a touch slider, along with two user LEDs and a user button.
Support circuitry for measuring power consumption is also available.
It also comes with a comprehensive STM32 software HAL library and various
packaged software examples.

There
are two variants of the board:

- STM32LDISCOVERY targets STM32L152RBT6, with 128K flash, 16K RAM
- 32L152CDISCOVERY targets STM32L152RCT6, with 256K flash, 32K RAM

The STM32LDISCOVERY is no longer sold, but was widely available. The current
configuration assumes only 128K flash and 16K RAM, so it builds and runs
on both variants out of the box.

![STM32LDISCOVERY](../../../../_images/stm32l1_disco.jpg)

More information about the board can be found at the [STM32LDISCOVERY website](https://www.st.com/en/evaluation-tools/32l152cdiscovery.html) [[1]](#id2).

## Hardware

The STM32 Discovery board features:

- On-board ST-LINK/V2 with selection mode switch to use the kit as a standalone
  ST-LINK/V2 (with SWD connector for programming and debugging)
- Board power supply: through USB bus or from an external 5 V supply voltage
- External application power supply: 3 V and 5 V
- Four LEDs:

  > - LD1 (red) for 3.3 V power on
  > - LD2 (red/green) for USB communication
  > - LD3 (green) for PC9 output
  > - LD4 (blue) for PC8 output
- Two push buttons (user and reset)
- Extension header for all LQFP64 I/Os for quick connection to prototyping board
  and easy probing

More information about STM32L151x can be found in the [STM32L1x reference manual](https://www.st.com/resource/en/reference_manual/cd00240193.pdf) [[2]](#id4).

### Supported Features

The Zephyr stm32l1\_disco board configuration supports the following hardware features:

Supported hardware

| Interface | Controller | Driver/component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| CLOCK | on-chip | reset and clock control |
| FLASH | on-chip | flash memory |
| WATCHDOG | on-chip | window watchdog |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |

Other hardware features are not yet supported in this Zephyr port.

The default configuration can be found in the defconfig file:
`boards/arm/stm32l1_disco/stm32l1_disco_defconfig`

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Default Zephyr Peripheral Mapping:

- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- UART\_2\_TX : PA2
- UART\_2\_RX : PA3
- I2C1\_SCL : PB6
- I2C1\_SDA : PB7
- I2C2\_SCL : PB10
- I2C2\_SDA : PB11
- SPI1\_NSS : PA4
- SPI1\_SCK : PA5
- SPI1\_MISO : PA6
- SPI1\_MOSI : PA7
- SPI2\_NSS : PB12
- SPI2\_SCK : PB13
- SPI2\_MISO : PB14
- SPI2\_MOSI : PB15

For more details please refer to [STM32L1DISCOVERY board User Manual](https://www.st.com/resource/en/user_manual/dm00027954.pdf) [[3]](#id6).

## Programming and Debugging

Applications for the `stm32l1_disco` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

STM32L1DISCOVERY board includes an ST-LINK/V2 embedded debug tool interface.
This interface is supported by the openocd version included in the Zephyr SDK.

#### Flashing an application

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32l1_disco samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32l1_disco samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/32l152cdiscovery.html](https://www.st.com/en/evaluation-tools/32l152cdiscovery.html)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/cd00240193.pdf](https://www.st.com/resource/en/reference_manual/cd00240193.pdf)

[[3](#id7)]

[https://www.st.com/resource/en/user\_manual/dm00027954.pdf](https://www.st.com/resource/en/user_manual/dm00027954.pdf)
