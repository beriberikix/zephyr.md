---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cy8cmbr3xxx_8h.html
original_path: doxygen/html/cy8cmbr3xxx_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cy8cmbr3xxx.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](cy8cmbr3xxx_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [cy8cmbr3xxx\_config\_data](structcy8cmbr3xxx__config__data.md) |

| Macros | |
| --- | --- |
| #define | [CY8CMBR3XXX\_EZ\_CLICK\_CONFIG\_SIZE](#a0d8534cc7dc74a6b17cf30ecb4ac1bfd)   128 |

| Functions | |
| --- | --- |
| int | [cy8cmbr3xxx\_configure](#a26da2ccc3ff92bc2c29021f66f184448) (const struct [device](structdevice.md) \*dev, const struct [cy8cmbr3xxx\_config\_data](structcy8cmbr3xxx__config__data.md) \*config\_data) |
|  | Configure the CY8CMBR3xxx device with an EZ-Click generated configuration. |

## Macro Definition Documentation

## [◆ ](#a0d8534cc7dc74a6b17cf30ecb4ac1bfd)CY8CMBR3XXX\_EZ\_CLICK\_CONFIG\_SIZE

| #define CY8CMBR3XXX\_EZ\_CLICK\_CONFIG\_SIZE   128 |
| --- |

## Function Documentation

## [◆ ](#a26da2ccc3ff92bc2c29021f66f184448)cy8cmbr3xxx\_configure()

| int cy8cmbr3xxx\_configure | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [cy8cmbr3xxx\_config\_data](structcy8cmbr3xxx__config__data.md) \* | *config\_data* ) |

Configure the CY8CMBR3xxx device with an EZ-Click generated configuration.

Parameters
:   | dev | Pointer to the input device instance |
    | --- | --- |
    | config\_data | Pointer to the configuration data for the device |

Return values
:   | 0 | if successful |
    | --- | --- |
    | <0 | if failed |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [cy8cmbr3xxx.h](cy8cmbr3xxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
