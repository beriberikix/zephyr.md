---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structgnss__satellites__callback.html
original_path: doxygen/html/structgnss__satellites__callback.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnss\_satellites\_callback Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [GNSS Interface](group__gnss__interface.md)

GNSS callback structure.
[More...](#details)

`#include <[gnss.h](gnss_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#a19e64ff2450c00080ae39528f7d07b2b) |
|  | Filter callback to GNSS data from this device if not NULL. |
| [gnss\_satellites\_callback\_t](group__gnss__interface.md#ga80cf700468d1c942cfa064368e212e6f) | [callback](#af12fc64ff9c696b5862b5adfef31269b) |
|  | Callback called when GNSS satellites is published. |

## Detailed Description

GNSS callback structure.

## Field Documentation

## [◆ ](#af12fc64ff9c696b5862b5adfef31269b)callback

| [gnss\_satellites\_callback\_t](group__gnss__interface.md#ga80cf700468d1c942cfa064368e212e6f) gnss\_satellites\_callback::callback |
| --- |

Callback called when GNSS satellites is published.

## [◆ ](#a19e64ff2450c00080ae39528f7d07b2b)dev

| const struct [device](structdevice.md)\* gnss\_satellites\_callback::dev |
| --- |

Filter callback to GNSS data from this device if not NULL.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[gnss.h](gnss_8h_source.md)

- [gnss\_satellites\_callback](structgnss__satellites__callback.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
