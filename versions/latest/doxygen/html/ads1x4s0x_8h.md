---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ads1x4s0x_8h.html
original_path: doxygen/html/ads1x4s0x_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ads1x4s0x.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](ads1x4s0x_8h_source.md)

| Functions | |
| --- | --- |
| int | [ads1x4s0x\_gpio\_set\_output](#a703c9abdb26bef488c14c20825610a6d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) initial\_value) |
| int | [ads1x4s0x\_gpio\_set\_input](#aeb9e6682f27b2c6d605cc64f92bd6b8c) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin) |
| int | [ads1x4s0x\_gpio\_deconfigure](#a18a225e3609dbfee4a2c910fb8784ab8) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin) |
| int | [ads1x4s0x\_gpio\_set\_pin\_value](#ad303897d9eaffd6c0cc8e402cb8c45ad) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
| int | [ads1x4s0x\_gpio\_get\_pin\_value](#af93b1e5324774fea17271c3e54a190e0) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*value) |
| int | [ads1x4s0x\_gpio\_port\_get\_raw](#aae6dca79ac3425a471962cc6f736eeed) (const struct [device](structdevice.md) \*dev, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value) |
| int | [ads1x4s0x\_gpio\_port\_set\_masked\_raw](#aa5f025a7f772c0787f22ced0ed761e0e) (const struct [device](structdevice.md) \*dev, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value) |
| int | [ads1x4s0x\_gpio\_port\_toggle\_bits](#a60438c9501fcece5548a1195fa3f77a0) (const struct [device](structdevice.md) \*dev, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |

## Function Documentation

## [◆ ](#a18a225e3609dbfee4a2c910fb8784ab8)ads1x4s0x\_gpio\_deconfigure()

| int ads1x4s0x\_gpio\_deconfigure | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin* ) |

## [◆ ](#af93b1e5324774fea17271c3e54a190e0)ads1x4s0x\_gpio\_get\_pin\_value()

| int ads1x4s0x\_gpio\_get\_pin\_value | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *value* ) |

## [◆ ](#aae6dca79ac3425a471962cc6f736eeed)ads1x4s0x\_gpio\_port\_get\_raw()

| int ads1x4s0x\_gpio\_port\_get\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \* | *value* ) |

## [◆ ](#aa5f025a7f772c0787f22ced0ed761e0e)ads1x4s0x\_gpio\_port\_set\_masked\_raw()

| int ads1x4s0x\_gpio\_port\_set\_masked\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | *mask*, |
|  |  | [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) | *value* ) |

## [◆ ](#a60438c9501fcece5548a1195fa3f77a0)ads1x4s0x\_gpio\_port\_toggle\_bits()

| int ads1x4s0x\_gpio\_port\_toggle\_bits | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins* ) |

## [◆ ](#aeb9e6682f27b2c6d605cc64f92bd6b8c)ads1x4s0x\_gpio\_set\_input()

| int ads1x4s0x\_gpio\_set\_input | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin* ) |

## [◆ ](#a703c9abdb26bef488c14c20825610a6d)ads1x4s0x\_gpio\_set\_output()

| int ads1x4s0x\_gpio\_set\_output | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *initial\_value* ) |

## [◆ ](#ad303897d9eaffd6c0cc8e402cb8c45ad)ads1x4s0x\_gpio\_set\_pin\_value()

| int ads1x4s0x\_gpio\_set\_pin\_value | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *value* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [ads1x4s0x.h](ads1x4s0x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
