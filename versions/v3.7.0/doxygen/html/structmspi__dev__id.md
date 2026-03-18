---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmspi__dev__id.html
original_path: doxygen/html/structmspi__dev__id.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_dev\_id Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI Configure API](group__mspi__configure__api.md)

MSPI device ID The controller can identify its devices and determine whether the access is allowed in a multiple device scheme.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [gpio\_dt\_spec](structgpio__dt__spec.md) | [ce](#ac79d41731c8599f23b666f78cdb58bf0) |
|  | device gpio ce |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dev\_idx](#aab54e4f449d4cfb87c5c6f0ccd1d7bfb) |
|  | device index on DT |

## Detailed Description

MSPI device ID The controller can identify its devices and determine whether the access is allowed in a multiple device scheme.

## Field Documentation

## [◆ ](#ac79d41731c8599f23b666f78cdb58bf0)ce

| struct [gpio\_dt\_spec](structgpio__dt__spec.md) mspi\_dev\_id::ce |
| --- |

device gpio ce

## [◆ ](#aab54e4f449d4cfb87c5c6f0ccd1d7bfb)dev\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mspi\_dev\_id::dev\_idx |
| --- |

device index on DT

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_dev\_id](structmspi__dev__id.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
