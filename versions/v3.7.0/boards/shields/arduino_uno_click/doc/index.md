---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/shields/arduino_uno_click/doc/index.html
original_path: boards/shields/arduino_uno_click/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Arduino UNO click shield

## Overview

The Arduino UNO click is an extension to the Arduino UNO R3 headers.
It’s a simple shield that converts Arduino UNO R3 headers to two mikroBUS
host sockets that allow you to connect many other click shields to your
board.
In other words, the Arduino UNO click will generally be used by other
shields using the mikroBUS interface.

Two mikroBUS headers are exposed by the overlay: `mikrobus_header_1` and
`mikrobus_header_2`, each corresponding to a socket on the Arduino UNO
click shield.

The first socket (`mikrobus_header_1`) is the default socket which is
assigned the node label `mikrobus_header` in the overlay.

More information about the shield can be found at
[Arduino UNO click shield website](https://www.mikroe.com/arduino-uno-click-shield) [[1]](#id1).

## Requirements

This shield can only be used with a board which provides a configuration
for Arduino R3 connector.

The board must also define node aliases for arduino Serial,
SPI and I2C interfaces (see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

Connecting shields should use the first socket (`mikrobus_header_1`). This
socket is assigned the `mikrobus_header` node label.

## Programming

Include `--shield arduino_uno_click` when you invoke `west build` with
other mikroBUS shields. For example:

```shell
# From the root of the zephyr repository
west build -b sam_v71_xult/samv71q21 --shield arduino_uno_click --shield atmel_rf2xx_mikrobus samples/net/sockets/echo_server -- -DOVERLAY_CONFIG=overlay-802154.conf
```

## References

[[1](#id2)]

[https://www.mikroe.com/arduino-uno-click-shield](https://www.mikroe.com/arduino-uno-click-shield)
