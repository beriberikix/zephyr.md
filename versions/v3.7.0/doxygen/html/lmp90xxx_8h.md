---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/lmp90xxx_8h.html
original_path: doxygen/html/lmp90xxx_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lmp90xxx.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](lmp90xxx_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LMP90XXX\_GPIO\_MAX](#a4d1a76d266a648aa9ea4f831a37b2f78)   6 |

| Functions | |
| --- | --- |
| int | [lmp90xxx\_gpio\_set\_output](#a1e17998cc9fcded05d18c5bf15ee4289) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin) |
| int | [lmp90xxx\_gpio\_set\_input](#a8a0f64db753e7d5d789563b1521cb795) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin) |
| int | [lmp90xxx\_gpio\_set\_pin\_value](#a0d516dc704a18efde862c5eef73d571c) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
| int | [lmp90xxx\_gpio\_get\_pin\_value](#a8ac7fc5e8fb30e4789f40ecaf4c37a3e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*value) |
| int | [lmp90xxx\_gpio\_port\_get\_raw](#a43342a79e50eb313a17e7c81aeda86e5) (const struct [device](structdevice.md) \*dev, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value) |
| int | [lmp90xxx\_gpio\_port\_set\_masked\_raw](#a1b16f4a754035047e4fb614905203a97) (const struct [device](structdevice.md) \*dev, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value) |
| int | [lmp90xxx\_gpio\_port\_set\_bits\_raw](#adff5b68dbf1ac67c274f77de7b72e64e) (const struct [device](structdevice.md) \*dev, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
| int | [lmp90xxx\_gpio\_port\_clear\_bits\_raw](#a3fc83c28427940e410f11558fa8208ad) (const struct [device](structdevice.md) \*dev, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
| int | [lmp90xxx\_gpio\_port\_toggle\_bits](#a0a1d236bdb7e1a1a0ab472963a61627e) (const struct [device](structdevice.md) \*dev, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |

## Macro Definition Documentation

## [◆ ](#a4d1a76d266a648aa9ea4f831a37b2f78)LMP90XXX\_GPIO\_MAX

| #define LMP90XXX\_GPIO\_MAX   6 |
| --- |

## Function Documentation

## [◆ ](#a8ac7fc5e8fb30e4789f40ecaf4c37a3e)lmp90xxx\_gpio\_get\_pin\_value()

| int lmp90xxx\_gpio\_get\_pin\_value | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *value* ) |

## [◆ ](#a3fc83c28427940e410f11558fa8208ad)lmp90xxx\_gpio\_port\_clear\_bits\_raw()

| int lmp90xxx\_gpio\_port\_clear\_bits\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins* ) |

## [◆ ](#a43342a79e50eb313a17e7c81aeda86e5)lmp90xxx\_gpio\_port\_get\_raw()

| int lmp90xxx\_gpio\_port\_get\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \* | *value* ) |

## [◆ ](#adff5b68dbf1ac67c274f77de7b72e64e)lmp90xxx\_gpio\_port\_set\_bits\_raw()

| int lmp90xxx\_gpio\_port\_set\_bits\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins* ) |

## [◆ ](#a1b16f4a754035047e4fb614905203a97)lmp90xxx\_gpio\_port\_set\_masked\_raw()

| int lmp90xxx\_gpio\_port\_set\_masked\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | *mask*, |
|  |  | [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) | *value* ) |

## [◆ ](#a0a1d236bdb7e1a1a0ab472963a61627e)lmp90xxx\_gpio\_port\_toggle\_bits()

| int lmp90xxx\_gpio\_port\_toggle\_bits | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins* ) |

## [◆ ](#a8a0f64db753e7d5d789563b1521cb795)lmp90xxx\_gpio\_set\_input()

| int lmp90xxx\_gpio\_set\_input | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin* ) |

## [◆ ](#a1e17998cc9fcded05d18c5bf15ee4289)lmp90xxx\_gpio\_set\_output()

| int lmp90xxx\_gpio\_set\_output | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin* ) |

## [◆ ](#a0d516dc704a18efde862c5eef73d571c)lmp90xxx\_gpio\_set\_pin\_value()

| int lmp90xxx\_gpio\_set\_pin\_value | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *value* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [lmp90xxx.h](lmp90xxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
