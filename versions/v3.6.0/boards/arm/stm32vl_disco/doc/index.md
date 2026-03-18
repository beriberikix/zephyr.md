---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/stm32vl_disco/doc/index.html
original_path: boards/arm/stm32vl_disco/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ST STM32VL Discovery

## Overview

The STM32 Discovery series comes in many varieties, in this case the “Value
Line” STM32F100x SoC series is showcased. Like other Discovery board, an
integrated ST-LINK debugger and programmer is included (V1), but the only
included I/O devices are two user LEDs and one user button.

![STM32VLDISCOVERY](../../../../_images/stm32vl_disco.jpg)

More information about the board can be found at the [STM32VLDISCOVERY website](https://www.st.com/en/evaluation-tools/stm32vldiscovery.html) [[1]](#id2).

## Hardware

The STM32 Discovery board features:

- On-board ST-LINK/V1 with selection mode switch to use the kit as a standalone
  ST-LINK/V1 (with SWD connector for programming and debugging)
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

More information about the STM32F100x can be found in the
[STM32F100x reference manual](https://www.st.com/resource/en/reference_manual/cd00246267.pdf) [[2]](#id4) and the [STM32F100x data sheet](https://www.st.com/resource/en/datasheet/stm32f100cb.pdf) [[3]](#id6).

### Supported Features

The Zephyr stm32vl\_disco board configuration supports the following hardware features:

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
| ADC | on-chip | adc |

Other hardware features are not yet supported in this Zephyr port.

The default configuration can be found in the defconfig file:
`boards/arm/stm32vl_disco/stm32vl_disco_defconfig`

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
- UART\_3\_TX : PB10
- UART\_3\_RX : PB11
- SPI1\_NSS : PA4
- SPI1\_SCK : PA5
- SPI1\_MISO : PA6
- SPI1\_MOSI : PA7
- SPI2\_NSS : PB12
- SPI2\_SCK : PB13
- SPI2\_MISO : PB14
- SPI2\_MOSI : PB15
- I2C1\_SCL : PB6
- I2C1\_SDA : PB7
- I2C2\_SCL : PB10
- I2C2\_SDA : PB11

For more details please refer to [STM32VLDISCOVERY board User Manual](https://www.st.com/resource/en/user_manual/cd00267113.pdf) [[4]](#id8).

## Programming and Debugging

Applications for the `stm32vl_disco` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

STM32VLDISCOVERY board includes an ST-LINK/V1 embedded debug tool interface.
This interface is supported by the openocd version included in the Zephyr SDK.

#### Flashing an application

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32vl_disco samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32vl_disco samples/basic/blinky
west debug
```

### USB mass storage issues

The ST-LINK/V1 includes a buggy USB mass storage gadget. To connect to the
ST-LINK from Linux, you might need to ignore the device using modprobe
configuration parameters:

```shell
$ echo "options usb-storage quirks=483:3744:i" | sudo tee /etc/modprobe.d/local.conf
$ sudo modprobe -r usb-storage
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/stm32vldiscovery.html](https://www.st.com/en/evaluation-tools/stm32vldiscovery.html)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/cd00246267.pdf](https://www.st.com/resource/en/reference_manual/cd00246267.pdf)

[[3](#id7)]

[https://www.st.com/resource/en/datasheet/stm32f100cb.pdf](https://www.st.com/resource/en/datasheet/stm32f100cb.pdf)

[[4](#id9)]

[https://www.st.com/resource/en/user\_manual/cd00267113.pdf](https://www.st.com/resource/en/user_manual/cd00267113.pdf)
