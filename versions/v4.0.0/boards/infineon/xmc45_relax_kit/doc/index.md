---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/infineon/xmc45_relax_kit/doc/index.html
original_path: boards/infineon/xmc45_relax_kit/doc/index.html
---

# XMC45-RELAX-KIT

Board Overview

[![../../../../_images/xmc45_relax_kit.jpg](../../../../_images/xmc45_relax_kit.jpg)
](../../../../_images/xmc45_relax_kit.jpg)

XMC45-RELAX-KIT

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   xmc4500

## Overview

The XMC4500 Relax Kit is designed to evaluate the capabilities of the XMC4500
Microcontroller. It is based on High performance ARM Cortex-M4F which can run
up to 120MHz.

### Features:

- ARM Cortex-M4F XMC4500
- 32 Mbit Quad-SPI Flash
- 4 x SPI-Master, 3x I2C, 3 x I2S, 3 x UART, 2 x CAN, 17 x ADC
- 2 pin header x1 and x2 with 80 pins
- Two buttons and two LEDs for user interaction
- Detachable on-board debugger (second XMC4500) with Segger J-Link

Details on the Relax Kit development board can be found in the [Relax Kit User Manual](https://www.infineon.com/dgdl/Board_Users_Manual_XMC4500_Relax_Kit-V1_R1.2_released.pdf?fileId=db3a30433acf32c9013adf6b97b112f9) [[1]](#id2).

### Supported Features

- The on-board 12-MHz crystal allows the device to run at its maximum operating speed of 120MHz.

The Relax Kit development board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| SYSTICK | on-chip | system clock |
| UART | on-chip | serial port |
| SPI | on-chip | spi |
| GPIO | on-chip | gpio |
| FLASH | on-chip | flash |
| ADC | on-chip | adc |
| DMA | on-chip | dma |
| PWM | on-chip | pwm |
| WATCHDOG | on-chip | watchdog |
| MDIO | on-chip | mdio |
| ETHERNET | on-chip | ethernet |
| PTP | on-chip | ethernet |
| RTC | on-chip | rtc |

More details about the supported peripherals are available in [XMC4500 TRM](https://www.infineon.com/dgdl/Infineon-xmc4500_rm_v1.6_2016-UM-v01_06-EN.pdf?fileId=db3a30433580b3710135a5f8b7bc6d13) [[2]](#id4)

The default configuration can be found in the Kconfig

[boards/infineon/xmc45\_relax\_kit/xmc45\_relax\_kit\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/xmc45_relax_kit/xmc45_relax_kit_defconfig)

Other hardware features are not currently supported by the Zephyr kernel.

## Build hello world sample

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application.

```shell
# From the root of the zephyr repository
west build -b xmc45_relax_kit samples/hello_world
```

## Programming and Debugging

### West Commands

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

> WindowsLinux
>
> ```shell
> # Do a pristine build
> west build -b xmc45_relax_kit -p always samples/hello_world
>
> west flash
> west debug
> ```
>
> ```shell
> # Do a pristine build
> west build -b xmc45_relax_kit -p always samples/hello_world
>
> west flash
> west debug
> ```

Once the gdb console starts after executing the west debug command, you may now set breakpoints and perform other standard GDB debugging.

## References

[[1](#id3)]

[https://www.infineon.com/dgdl/Board\_Users\_Manual\_XMC4500\_Relax\_Kit-V1\_R1.2\_released.pdf?fileId=db3a30433acf32c9013adf6b97b112f9](https://www.infineon.com/dgdl/Board_Users_Manual_XMC4500_Relax_Kit-V1_R1.2_released.pdf?fileId=db3a30433acf32c9013adf6b97b112f9)

[[2](#id5)]

[https://www.infineon.com/dgdl/Infineon-xmc4500\_rm\_v1.6\_2016-UM-v01\_06-EN.pdf?fileId=db3a30433580b3710135a5f8b7bc6d13](https://www.infineon.com/dgdl/Infineon-xmc4500_rm_v1.6_2016-UM-v01_06-EN.pdf?fileId=db3a30433580b3710135a5f8b7bc6d13)
