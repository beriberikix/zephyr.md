---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/inventek_eswifi/doc/index.html
original_path: boards/shields/inventek_eswifi/doc/index.html
---

# Inventek es-WIFI Shield

## Overview

The es-WIFI (embedded Serial-to-WiFi) modules are devices developed by Inventek
Systems. It integrates WIFI and optionally Bluetooth Low Energy. The es-WIFI
devices can run Cypress WICED or Inventek’s IWIN (Inventek Systems Wireless
Interoperability Network) AT commands set. The current es-WIFI driver is able
to use one of two serial interfaces: SPI or UART.

The Zephyr es-WIFI drivers was implemented using ISM43362-M3G-L44 with SPI
interface. The UART was implemented with ISM4343-WBM-L151. Besides that,
user can reprogram the modules to switch from one interface type to another
by the JTAG pin header.

### ISMART4343C-EVB

The [ISMART4343C-EVB](https://www.inventeksys.com/ismart4343-c-arduino-shield-wi-fi-2ghz-bluetooth-ble/) [[1]](#id2) is a development Kit with Arduino Uno R3 compatible
shield. It allows evaluate es-WIFI modules with SPI or UART interface. For
UART interface the [inventek\_eswifi\_arduino\_uart](https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/shields/inventek_eswifi/inventek_eswifi_arduino_uart.overlay) [[4]](#id8) must be selected. For
SPI interface the [inventek\_eswifi\_arduino\_spi](https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/shields/inventek_eswifi/inventek_eswifi_arduino_spi.overlay) [[5]](#id11) must be enabled. The EVB
can use 5V from Arduino header, if board provide it, J17 position 1-2.
Otherwise, J17 2-3 will select USB-5V. More information can be found at
[ISMART4343C-EVB Users Manual](https://www.inventeksys.com/wp-content/uploads/IoT-EVB-Users-Manual.pdf) [[2]](#id4).

Note

The Inventek’s EVBs signals are 3.3V only.

![ISMART4343C-EVB](../../../../_images/ismart4343c-evb.jpg)

### Pins Assignment of the ISMART EVBs

The below table presents signals by interface. The UART switch SW3 must be on
position 3 to enable RX/TX signals when using es-WIFI with UART firmware.

To enable full control by Arduino header user should do some manual wiring.
The signals from D3 up to D7 are not connected by default on the Inventek’s
shield. These signals marked as optional can help on development. The current
driver do not handle that signals and are simple suggestions and can be left
as is. Some arduino boards don’t have NRST pin connected to a GPIO pin. The
recommendation is bend the NRST pin and make a wire to D6. WAKE-UP signal is
available at header J26 pin 1 and shield configuration uses D7 to control that
signal, user need do a wire connecting these two terminals. On the below
image is possible see suggested wiring connections.

![ISMART4343C-EVB Wiring](../../../../_images/ismart4343c-evb-wiring.jpg)

| Arduino Connector Pin | Function | Serial Connection |
| --- | --- | --- |
| D0 | UART RX | UART |
| D1 | UART TX | UART |
| D3 | CFG-1 | UART/SPI [optional] |
| D4 | CFG-0 | UART/SPI [optional] |
| D5 | BOOT-0 | UART/SPI [optional] |
| D6 | NRST | UART/SPI [wiring] |
| D7 | WAKE-UP | UART/SPI [wiring] |
| D9 | CMD/RDY | SPI |
| D10 | SPI CS | SPI |
| D11 | SPI MOSI | SPI |
| D12 | SPI MISO | SPI |
| D13 | SPI SCK | SPI |

### Supported variations

The below table suggests shield variation accordingly with end user
application. When a standard Arduino R3 connector is available on board, user
should select the matching shield configuration based on the serial interface
(SERIAL or SPI). The inventek\_eswifi is available to allow users testing a
built-in module with dedicated <board>.overlay and <board>.defconfig files.

| Connector Standard | Shield Designation | Variation |
| --- | --- | --- |
| Without standard (overlay) | [inventek\_eswifi](https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/shields/inventek_eswifi/inventek_eswifi.overlay) [[3]](#id6) | 1 |
| Arduino by UART | [inventek\_eswifi\_arduino\_uart](https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/shields/inventek_eswifi/inventek_eswifi_arduino_uart.overlay) [[4]](#id8) | 2 |
| Arduino by SPI | [inventek\_eswifi\_arduino\_spi](https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/shields/inventek_eswifi/inventek_eswifi_arduino_spi.overlay) [[5]](#id11) | 3 |

## Requirements

This shield requires a board which provides a configuration that allows an
UART or SPI interface and two or three GPIO. (see [Shields](../../../../hardware/porting/shields.md#shields) for more
details).

Note

Some boards may already have a network interface: Check network
documentation to understand how properly configure both interfaces.
To keep simple, you can keep only the WIFI interface enabled at
Networking -> Link Layer Options. This will avoid problems running
Zephyr samples.

### Tested Boards

| Board | Disabled Interface | Variation |
| --- | --- | --- |
| ATMEL sam\_v71\_xult/samv71q21 | Ethernet | 2 , 3 |
| ST nucleo\_f767zi | Ethernet | 2 , 3 |
| ST disco\_l475\_iot1 |  |  |

Note

ST disco\_l475\_iot1 already have an ISM43362 module with IWIN SPI
firmware. It doesn’t need this shield to expose es-WIFI. It is only
used here as reference to demonstrate how configure an on-board
module.

## Sample usage

The reference sample for WIFI is [Wi-Fi shell](../../../../samples/net/wifi/shell/README.md#wifi-shell "Test Wi-Fi functionality using the Wi-Fi shell module."). It allows you to use WIFI
shell to scan local Wireless networks. With the password you can pick,
connect and send ping.

## Build and Programming

Set `--shield <shield designator>` when you invoke `west build`.

```shell
west build -b [sam_v71_xult/samv71q21 | nucleo_f767zi] --shield inventek_eswifi_arduino_uart samples/net/wifi
west flash
```

```shell
west build -b [sam_v71_xult/samv71q21 | nucleo_f767zi] --shield inventek_eswifi_arduino_spi samples/net/wifi
west flash
```

```shell
west build -b disco_l475_iot1 samples/net/wifi
west flash
```

## References

[[1](#id3)]

[https://www.inventeksys.com/ismart4343-c-arduino-shield-wi-fi-2ghz-bluetooth-ble/](https://www.inventeksys.com/ismart4343-c-arduino-shield-wi-fi-2ghz-bluetooth-ble/)

[[2](#id5)]

[https://www.inventeksys.com/wp-content/uploads/IoT-EVB-Users-Manual.pdf](https://www.inventeksys.com/wp-content/uploads/IoT-EVB-Users-Manual.pdf)

[[3](#id7)]

[https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/shields/inventek\_eswifi/inventek\_eswifi.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/shields/inventek_eswifi/inventek_eswifi.overlay)

[4]
([1](#id9),[2](#id10))

[https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/shields/inventek\_eswifi/inventek\_eswifi\_arduino\_uart.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/shields/inventek_eswifi/inventek_eswifi_arduino_uart.overlay)

[5]
([1](#id12),[2](#id13))

[https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/shields/inventek\_eswifi/inventek\_eswifi\_arduino\_spi.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/master/boards/shields/inventek_eswifi/inventek_eswifi_arduino_spi.overlay)
