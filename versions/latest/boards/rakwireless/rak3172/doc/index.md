---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/rakwireless/rak3172/doc/index.html
original_path: boards/rakwireless/rak3172/doc/index.html
---

# RAK3172

Board Overview

[![../../../../_images/rak3172.webp](../../../../_images/rak3172.webp)
](../../../../_images/rak3172.webp)

RAK3172

Name:
:   `rak3172`

Vendor:
:   RAKwireless Technology Limited

Architecture:
:   arm

SoC:
:   stm32wle5xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/rakwireless/rak3172/doc/index.rst/../..)

## Overview

RAK3172 is a WisDuo LPWAN module which integrating a STM32WLE5CC chip.
The breakout board has the RAK3172 as its core and with soldered to the
antenna connector.

## Hardware

The breakout board footprint allows RAK3172 stamp module pins to be transferred to 2.54 mm headers.
It is designed to easy access to the pins on the board and simplify the evaluation of the RAK3172
module.

- RAK3172 STM32WLE5CC Module with LPWAN single-core Cortex®-M4 at 48 MHz
- 256-Kbyte Flash memory and 64-Kbyte SRAM
- RF transceiver LoRa® modulations
- Hardware encryption AES256-bit and a True random number generator
- SMA connectors for the LORA antenna
- I/O ports:

  > - UART
  > - I2C
  > - SPI
  > - SWD

![RAK3172-pinout](../../../../_images/pinout.webp)

For more information about the RAK3172 stamp module:

- [WisDuo RAK3172 Website](https://docs.rakwireless.com/Product-Categories/WisDuo/RAK3172-Module/Overview/#product-description) [[1]](#id2)
- [STM32WLE5CC on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32wle5cc.html) [[2]](#id4)

### Supported Features

The `rak3172` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Programming and Debugging

The RAK3172 board can be debugged and flashed with an external debug probe connected
to the SWD pins.
It can also be flashed via [pyOCD](https://github.com/pyocd/pyOCD) [[3]](#id6), but have to install an additional pack to support STM32WL.

```shell
$ pyocd pack --update
$ pyocd pack --install stm32wl
```

#### Flashing an application

Connect the board to your host computer and build and flash an application.
The sample application [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application, then flash it to the device:

```shell
# From the root of the zephyr repository
west build -b rak3172 samples/hello_world
west flash
```

Run a serial terminal to connect with your board. By default, `usart1` is
accessible via the USB to TTL converter.

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

```shell
Hello World! rak3172/stm32wle5xx
```

## References

[[1](#id3)]

[https://docs.rakwireless.com/Product-Categories/WisDuo/RAK3172-Module/Overview/#product-description](https://docs.rakwireless.com/Product-Categories/WisDuo/RAK3172-Module/Overview/#product-description)

[[2](#id5)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32wle5cc.html](https://www.st.com/en/microcontrollers-microprocessors/stm32wle5cc.html)

[[3](#id7)]

[https://github.com/pyocd/pyOCD](https://github.com/pyocd/pyOCD)
