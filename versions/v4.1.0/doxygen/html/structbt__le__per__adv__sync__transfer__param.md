---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__le__per__adv__sync__transfer__param.html
original_path: doxygen/html/structbt__le__per__adv__sync__transfer__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_sync\_transfer\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [skip](#a840e7cfac3a2947e5128d704067aaf7e) |
|  | Maximum event skip. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timeout](#a5bfa84c6bdacdf8893a0951a5ce71fc6) |
|  | Synchronization timeout (N \* 10 ms). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [options](#a0b3ee6df1b409e64a064ffb6ac632cce) |
|  | Periodic Advertising Sync Transfer options. |

## Field Documentation

## [◆ ](#a0b3ee6df1b409e64a064ffb6ac632cce)options

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_per\_adv\_sync\_transfer\_param::options |
| --- |

Periodic Advertising Sync Transfer options.

## [◆ ](#a840e7cfac3a2947e5128d704067aaf7e)skip

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_sync\_transfer\_param::skip |
| --- |

Maximum event skip.

The number of periodic advertising packets that can be skipped after a successful receive.

## [◆ ](#a5bfa84c6bdacdf8893a0951a5ce71fc6)timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_sync\_transfer\_param::timeout |
| --- |

Synchronization timeout (N \* 10 ms).

Synchronization timeout for the periodic advertising sync. Range 0x000A to 0x4000 (100 ms to 163840 ms)

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
