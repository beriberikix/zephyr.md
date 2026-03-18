---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structi3c__driver__data.html
original_path: doxygen/html/structi3c__driver__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_driver\_data Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

This structure is common to all I3C drivers and is expected to be the first element in the driver's struct driver\_data declaration.
[More...](#details)

`#include <[i3c.h](i3c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [i3c\_config\_controller](structi3c__config__controller.md) | [ctrl\_config](#a00fc23f3b070cdfce304c015b4409cbb) |
|  | Controller Configuration. |
| struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) | [attached\_dev](#ae64e0be2d004d67900c11adf46630901) |
|  | Attached I3C/I2C devices and addresses. |

## Detailed Description

This structure is common to all I3C drivers and is expected to be the first element in the driver's struct driver\_data declaration.

## Field Documentation

## [◆ ](#ae64e0be2d004d67900c11adf46630901)attached\_dev

| struct [i3c\_dev\_attached\_list](structi3c__dev__attached__list.md) i3c\_driver\_data::attached\_dev |
| --- |

Attached I3C/I2C devices and addresses.

## [◆ ](#a00fc23f3b070cdfce304c015b4409cbb)ctrl\_config

| struct [i3c\_config\_controller](structi3c__config__controller.md) i3c\_driver\_data::ctrl\_config |
| --- |

Controller Configuration.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i3c.h](i3c_8h_source.md)

- [i3c\_driver\_data](structi3c__driver__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
