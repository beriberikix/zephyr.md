---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/x_nucleo_wb05kn1/doc/index.html
original_path: boards/shields/x_nucleo_wb05kn1/doc/index.html
---

# X-NUCLEO-WB05KN1: BLE expansion board

## Overview

The X-NUCLEO-WB05KN1 is a Bluetooth Low Energy evaluation board which allows the
expansion of the STM32 Nucleo boards.
The RF module is FCC (FCC ID: YCP-MB203202) and IC certified (IC: 8976A-MB203202).

The X-NUCLEO-WB05KN1 is compatible out of the box with the Arduino UNO R3 connector.
The board interfaces with the host microcontroller via UART (default) or SPI peripheral.

![X-NUCLEO-WB05KN1](../../../../_images/x-nucleo-wb05kn1.webp)

More information about the board can be found at the
[X-NUCLEO-WB05KN1 website](https://www.st.com/en/evaluation-tools/x-nucleo-wb05kn1.html) [[1]](#id1).

## Configurations

X-NUCLEO-WB05KN1 can be utilized as a Bluetooth Low-Energy controller shield
with a UART or SPI host controller interface (HCI-UART/HCI-SPI).

The UART default settings are:

- Baudrate: 921600 bps
- 8 bits, no parity, 1 stop bit

| UART Pin | Arduino Connector Pin |
| --- | --- |
| RX | D0 |
| TX | D1 |

Note

Please, bear in mind in order to use SPI interface you need to change the shield firmware
to `DTM_SPI_WITH_UPDATER_CONTROLLER` according to the SDK provided by ST at [X-CUBE-WB05N](https://www.st.com/en/embedded-software/x-cube-wb05n.html) [[2]](#id3).

IRQ and reset pins are also necessary in addition to SPI pins.

| SPI Config Pin | Arduino Connector Pin |
| --- | --- |
| SCK | D13 |
| MISO | D12 |
| MOSI | D11 |
| CS | D10 |
| IRQ | A0 |
| RESET | D7 |

More information about X-NUCLEO-WB05KN1 can be found here:
:   - [X-NUCLEO-WB05KN1 datasheet](https://www.st.com/resource/en/datasheet/stm32wb05kn.pdf) [[3]](#id5)

## Programming

Activate the presence of the shield for the project build by adding the
`--shield x_nucleo_wb05kn1_uart` or `--shield x_nucleo_wb05kn1_spi` when you invoke
`west build` based on UART or SPI interface:

> ```shell
> west build -b your_board_name --shield x_nucleo_wb05kn1_uart your_app
> ```

or

> ```shell
> west build -b your_board_name --shield x_nucleo_wb05kn1_spi your_app
> ```

## References

[[1](#id2)]

[https://www.st.com/en/evaluation-tools/x-nucleo-wb05kn1.html](https://www.st.com/en/evaluation-tools/x-nucleo-wb05kn1.html)

[[2](#id4)]

[https://www.st.com/en/embedded-software/x-cube-wb05n.html](https://www.st.com/en/embedded-software/x-cube-wb05n.html)

[[3](#id6)]

[https://www.st.com/resource/en/datasheet/stm32wb05kn.pdf](https://www.st.com/resource/en/datasheet/stm32wb05kn.pdf)
