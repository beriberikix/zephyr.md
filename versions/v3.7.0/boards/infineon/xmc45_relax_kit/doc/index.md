---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/infineon/xmc45_relax_kit/doc/index.html
original_path: boards/infineon/xmc45_relax_kit/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# INFINEON XMC45-RELAX-KIT

## Overview

The XMC4500 Relax Kit is designed to evaluate the capabilities of the XMC4500
Microcontroller. It is based on High performance ARM Cortex-M4F which can run
up to 120MHz.

![XMC45-RELAX-KIT](../../../../_images/xmc45_relax_kit.jpg)

### Features:

- ARM Cortex-M4F XMC4500
- 32 Mbit Quad-SPI Flash
- 4 x SPI-Master, 3x I2C, 3 x I2S, 3 x UART, 2 x CAN, 17 x ADC
- 2 pin header x1 and x2 with 80 pins
- Two buttons and two LEDs for user interaction
- Detachable on-board debugger (second XMC4500) with Segger J-Link

Details on the Relax Kit development board can be found in the [Relax Kit User Manual](https://www.infineon.com/dgdl/Board_Users_Manual_XMC4500_Relax_Kit-V1_R1.2_released.pdf?fileId=db3a30433acf32c9013adf6b97b112f9).

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

More details about the supported peripherals are available in [XMC4500 TRM](https://www.infineon.com/dgdl/Infineon-xmc4500_rm_v1.6_2016-UM-v01_06-EN.pdf?fileId=db3a30433580b3710135a5f8b7bc6d13)
Other hardware features are not currently supported by the Zephyr kernel.

## Building and Flashing

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b xmc45_relax_kit samples/hello_world
west flash
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b xmc45_relax_kit samples/hello_world
west debug
```

Step through the application in your debugger.

## References
