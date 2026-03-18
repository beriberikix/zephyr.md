---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__le__per__adv__sync__term__info.html
original_path: doxygen/html/structbt__le__per__adv__sync__term__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_term\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [addr](#a2b76ccd5e4c9933f2c05db2ec5b8e2fc) |
|  | Advertiser LE address and type. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a7a5f2ecccaf698bad86f10d9a7d16189) |
|  | Advertiser SID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reason](#a429b8b665eacbfe9db013a571b829bac) |
|  | Cause of periodic advertising termination. |

## Field Documentation

## [◆ ](#a2b76ccd5e4c9933f2c05db2ec5b8e2fc)addr

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_le\_per\_adv\_sync\_term\_info::addr |
| --- |

Advertiser LE address and type.

## [◆ ](#a429b8b665eacbfe9db013a571b829bac)reason

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_term\_info::reason |
| --- |

Cause of periodic advertising termination.

## [◆ ](#a7a5f2ecccaf698bad86f10d9a7d16189)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_term\_info::sid |
| --- |

Advertiser SID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
