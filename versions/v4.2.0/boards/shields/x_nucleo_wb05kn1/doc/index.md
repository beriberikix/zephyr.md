---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/x_nucleo_wb05kn1/doc/index.html
original_path: boards/shields/x_nucleo_wb05kn1/doc/index.html
---

# X-NUCLEO-WB05KN1: BLE expansion board

## Overview

The X-NUCLEO-WB05KN1 is a Bluetooth Low Energy evaluation board which allows the
expansion of the STM32 Nucleo boards.
The RF module is FCC (FCC ID: YCP-MB203202) and IC certified (IC: 8976A-MB203202).

The X-NUCLEO-WB05KN1 is compatible out of the box with the Arduino UNO R3 connector.
The board interfaces with the host microcontroller via UART (default) or SPI peripheral.
However, the out-of-the-box firmware is not compatible with Zephyr; therefore, a controller-only
image should be flashed on the board using CN8 pin headers.
For more information about how to change the firmware, please refer to [UM3406](https://www.st.com/resource/en/user_manual/um3406-getting-started-with-the-xcubewb05n-bluetooth-low-energy-software-expansion-for-stm32cube-stmicroelectronics.pdf) [[1]](#id1) section 3.3.

Note

The [X-CUBE-WB05N](https://www.st.com/en/embedded-software/x-cube-wb05n.html) [[2]](#id3) package provided by ST contains firmware compatible with Zephyr
in the `Utilities/BLE_Transparent_Mode_STM32WB05_controller_only` directory
(`SPI` or `UART` subdirectories depending on which interface you want to use).

![X-NUCLEO-WB05KN1](../../../../_images/x-nucleo-wb05kn1.webp)

More information about the board can be found at the
[X-NUCLEO-WB05KN1 website](https://www.st.com/en/evaluation-tools/x-nucleo-wb05kn1.html) [[3]](#id5).

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

The SPI default settings are:

- Mode: Full-duplex slave
- Frame format: Motorola
- Data size: 8 bits, MSB first
- Clock Polarity: High (CPOL=1)
- Clock Phase: 2 Edge (CPHA=1)
- CS type: Software-controlled

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
:   - [X-NUCLEO-WB05KN1 datasheet](https://www.st.com/resource/en/datasheet/stm32wb05kn.pdf) [[4]](#id7)

## Programming

Activate the presence of the shield for the project build by adding the
`--shield x_nucleo_wb05kn1_uart` or `--shield x_nucleo_wb05kn1_spi` when you invoke
`west build` based on UART or SPI interface:

> ```shell
> west build -b your_board_name --shield x_nucleo_wb05kn1_uart your_app
> ```

Or

> ```shell
> west build -b your_board_name --shield x_nucleo_wb05kn1_spi your_app
> ```

## References

[[1](#id2)]

[https://www.st.com/resource/en/user\_manual/um3406-getting-started-with-the-xcubewb05n-bluetooth-low-energy-software-expansion-for-stm32cube-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um3406-getting-started-with-the-xcubewb05n-bluetooth-low-energy-software-expansion-for-stm32cube-stmicroelectronics.pdf)

[[2](#id4)]

[https://www.st.com/en/embedded-software/x-cube-wb05n.html](https://www.st.com/en/embedded-software/x-cube-wb05n.html)

[[3](#id6)]

[https://www.st.com/en/evaluation-tools/x-nucleo-wb05kn1.html](https://www.st.com/en/evaluation-tools/x-nucleo-wb05kn1.html)

[[4](#id8)]

[https://www.st.com/resource/en/datasheet/stm32wb05kn.pdf](https://www.st.com/resource/en/datasheet/stm32wb05kn.pdf)
