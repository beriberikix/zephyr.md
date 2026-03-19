---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structgnss__data__callback.html
original_path: doxygen/html/structgnss__data__callback.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnss\_data\_callback Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [GNSS Interface](group__gnss__interface.md)

GNSS callback structure.
[More...](#details)

`#include <[gnss.h](gnss_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#afdf273ceed2d2038b6415840f9ecdd7b) |
|  | Filter callback to GNSS data from this device if not NULL. |
| [gnss\_data\_callback\_t](group__gnss__interface.md#ga025c965369275ad8e5ab5ad44c14a23b) | [callback](#a07e9c7fd6192fd5b58ff37aabdbff11e) |
|  | Callback called when GNSS data is published. |

## Detailed Description

GNSS callback structure.

## Field Documentation

## [◆ ](#a07e9c7fd6192fd5b58ff37aabdbff11e)callback

| [gnss\_data\_callback\_t](group__gnss__interface.md#ga025c965369275ad8e5ab5ad44c14a23b) gnss\_data\_callback::callback |
| --- |

Callback called when GNSS data is published.

## [◆ ](#afdf273ceed2d2038b6415840f9ecdd7b)dev

| const struct [device](structdevice.md)\* gnss\_data\_callback::dev |
| --- |

Filter callback to GNSS data from this device if not NULL.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[gnss.h](gnss_8h_source.md)

- [gnss\_data\_callback](structgnss__data__callback.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
