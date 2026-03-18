---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structgnss__info.html
original_path: doxygen/html/structgnss__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnss\_info Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [GNSS Interface](group__gnss__interface.md)

GNSS info data structure.
[More...](#details)

`#include <[gnss.h](gnss_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [satellites\_cnt](#a81160955c4b9d3a746280d88a74f07eb) |
|  | Number of satellites being tracked. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [hdop](#a7e82c952ac5a1727b816f6fe30ce4ad8) |
|  | Horizontal dilution of precision in 1/1000. |
| enum [gnss\_fix\_status](group__gnss__interface.md#ga15536308e2229a45493d06e8b61e63d9) | [fix\_status](#a718e95833c4d07ad530669035ca21f8c) |
|  | The fix status. |
| enum [gnss\_fix\_quality](group__gnss__interface.md#gacf5a3464c487ae7609d526c73ccc758a) | [fix\_quality](#a54396dd23fd05185bcb1104ee529984e) |
|  | The fix quality. |

## Detailed Description

GNSS info data structure.

## Field Documentation

## [◆ ](#a54396dd23fd05185bcb1104ee529984e)fix\_quality

| enum [gnss\_fix\_quality](group__gnss__interface.md#gacf5a3464c487ae7609d526c73ccc758a) gnss\_info::fix\_quality |
| --- |

The fix quality.

## [◆ ](#a718e95833c4d07ad530669035ca21f8c)fix\_status

| enum [gnss\_fix\_status](group__gnss__interface.md#ga15536308e2229a45493d06e8b61e63d9) gnss\_info::fix\_status |
| --- |

The fix status.

## [◆ ](#a7e82c952ac5a1727b816f6fe30ce4ad8)hdop

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) gnss\_info::hdop |
| --- |

Horizontal dilution of precision in 1/1000.

## [◆ ](#a81160955c4b9d3a746280d88a74f07eb)satellites\_cnt

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) gnss\_info::satellites\_cnt |
| --- |

Number of satellites being tracked.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[gnss.h](gnss_8h_source.md)

- [gnss\_info](structgnss__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
