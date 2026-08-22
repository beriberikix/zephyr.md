---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structi3c__driver__config.html
original_path: doxygen/html/structi3c__driver__config.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_driver\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

This structure is common to all I3C drivers and is expected to be the first element in the object pointed to by the config field in the device structure.
[More...](#details)

`#include <[zephyr/drivers/i3c.h](i3c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [i3c\_dev\_list](structi3c__dev__list.md) | [dev\_list](#aaa79d44e949dfdfe51e3994c08837193) |
|  | I3C/I2C device list struct. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [primary\_controller\_da](#a52b9e5a36b65fbadc7fd2369ff184271) |
|  | I3C Primary Controller Dynamic Address. |

## Detailed Description

This structure is common to all I3C drivers and is expected to be the first element in the object pointed to by the config field in the device structure.

## Field Documentation

## [◆ ](#aaa79d44e949dfdfe51e3994c08837193)dev\_list

| struct [i3c\_dev\_list](structi3c__dev__list.md) i3c\_driver\_config::dev\_list |
| --- |

I3C/I2C device list struct.

## [◆ ](#a52b9e5a36b65fbadc7fd2369ff184271)primary\_controller\_da

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_driver\_config::primary\_controller\_da |
| --- |

I3C Primary Controller Dynamic Address.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i3c.h](i3c_8h_source.md)

- [i3c\_driver\_config](structi3c__driver__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
