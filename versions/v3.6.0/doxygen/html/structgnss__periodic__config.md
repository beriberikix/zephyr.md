---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structgnss__periodic__config.html
original_path: doxygen/html/structgnss__periodic__config.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnss\_periodic\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [GNSS Interface](group__gnss__interface.md)

GNSS periodic tracking configuration.
[More...](#details)

`#include <[gnss.h](gnss_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [active\_time\_ms](#a8255a68714bcc23af57d21639df5264b) |
|  | The time the GNSS will spend in the active state in ms. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [inactive\_time\_ms](#a87d8431b6f5e5048322533d435948136) |
|  | The time the GNSS will spend in the inactive state in ms. |

## Detailed Description

GNSS periodic tracking configuration.

Note
:   Setting either active\_time or inactive\_time to 0 will disable periodic function.

## Field Documentation

## [◆ ](#a8255a68714bcc23af57d21639df5264b)active\_time\_ms

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gnss\_periodic\_config::active\_time\_ms |
| --- |

The time the GNSS will spend in the active state in ms.

## [◆ ](#a87d8431b6f5e5048322533d435948136)inactive\_time\_ms

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gnss\_periodic\_config::inactive\_time\_ms |
| --- |

The time the GNSS will spend in the inactive state in ms.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[gnss.h](gnss_8h_source.md)

- [gnss\_periodic\_config](structgnss__periodic__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
