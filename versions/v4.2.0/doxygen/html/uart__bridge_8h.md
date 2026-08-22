---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/uart__bridge_8h.html
original_path: doxygen/html/uart__bridge_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_bridge.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](uart__bridge_8h_source.md)

| Functions | |
| --- | --- |
| void | [uart\_bridge\_settings\_update](#a05e43f34092fbbe84c868e6ec8966313) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*bridge\_dev) |
|  | Update the hardware port settings on a uart bridge. |

## Function Documentation

## [◆ ](#a05e43f34092fbbe84c868e6ec8966313)uart\_bridge\_settings\_update()

| void uart\_bridge\_settings\_update | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *bridge\_dev* ) |

Update the hardware port settings on a uart bridge.

If dev is part bridge\_dev, then the dev uart configuration are applied to the other device in the uart bridge. This allows propagating the settings from a USB CDC-ACM port to a hardware UART.

If dev is not part of bridge\_dev then the function is a no-op.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart](dir_eceb547fc512cd90b0f2ab20ab1dbc9a.md)
- [uart\_bridge.h](uart__bridge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
