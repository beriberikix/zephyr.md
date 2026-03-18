---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ads114s0x_8h.html
original_path: doxygen/html/ads114s0x_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ads114s0x.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](ads114s0x_8h_source.md)

| Functions | |
| --- | --- |
| int | [ads114s0x\_gpio\_set\_output](#aae01af45d1f620e1fba7f352732cbdfe) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) initial\_value) |
| int | [ads114s0x\_gpio\_set\_input](#a772a6f07c12f310c1648351b38062dfa) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin) |
| int | [ads114s0x\_gpio\_deconfigure](#ab8dc4eec4cad38cc25aeadef3c810b0b) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin) |
| int | [ads114s0x\_gpio\_set\_pin\_value](#a92d0aa7dbfba1f6337ba1f871a328c4d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
| int | [ads114s0x\_gpio\_get\_pin\_value](#acfdec18269fb677f17ecde631e2e0eb1) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*value) |
| int | [ads114s0x\_gpio\_port\_get\_raw](#aea152628b28b208d251c7286e7ea72b9) (const struct [device](structdevice.md) \*dev, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value) |
| int | [ads114s0x\_gpio\_port\_set\_masked\_raw](#a9e285db925feafd10038c893e6544a7f) (const struct [device](structdevice.md) \*dev, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value) |
| int | [ads114s0x\_gpio\_port\_toggle\_bits](#ac59eee61e1b0dd988343461884436140) (const struct [device](structdevice.md) \*dev, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |

## Function Documentation

## [◆ ](#ab8dc4eec4cad38cc25aeadef3c810b0b)ads114s0x\_gpio\_deconfigure()

| int ads114s0x\_gpio\_deconfigure | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin* ) |

## [◆ ](#acfdec18269fb677f17ecde631e2e0eb1)ads114s0x\_gpio\_get\_pin\_value()

| int ads114s0x\_gpio\_get\_pin\_value | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *value* ) |

## [◆ ](#aea152628b28b208d251c7286e7ea72b9)ads114s0x\_gpio\_port\_get\_raw()

| int ads114s0x\_gpio\_port\_get\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \* | *value* ) |

## [◆ ](#a9e285db925feafd10038c893e6544a7f)ads114s0x\_gpio\_port\_set\_masked\_raw()

| int ads114s0x\_gpio\_port\_set\_masked\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | *mask*, |
|  |  | [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) | *value* ) |

## [◆ ](#ac59eee61e1b0dd988343461884436140)ads114s0x\_gpio\_port\_toggle\_bits()

| int ads114s0x\_gpio\_port\_toggle\_bits | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins* ) |

## [◆ ](#a772a6f07c12f310c1648351b38062dfa)ads114s0x\_gpio\_set\_input()

| int ads114s0x\_gpio\_set\_input | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin* ) |

## [◆ ](#aae01af45d1f620e1fba7f352732cbdfe)ads114s0x\_gpio\_set\_output()

| int ads114s0x\_gpio\_set\_output | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *initial\_value* ) |

## [◆ ](#a92d0aa7dbfba1f6337ba1f871a328c4d)ads114s0x\_gpio\_set\_pin\_value()

| int ads114s0x\_gpio\_set\_pin\_value | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *value* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [ads114s0x.h](ads114s0x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
