---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__le__per__adv__param.html
original_path: doxygen/html/structbt__le__per__adv__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval\_min](#a49da44a3c0e4e866ffccffae5a9a22f7) |
|  | Minimum Periodic Advertising Interval (N \* 1.25 ms). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval\_max](#a61308cfe72ad23372dfd2a3bd2550726) |
|  | Maximum Periodic Advertising Interval (N \* 1.25 ms). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [options](#a9b80c2427171920f466601e7e8468814) |
|  | Bit-field of periodic advertising options. |

## Field Documentation

## [◆ ](#a61308cfe72ad23372dfd2a3bd2550726)interval\_max

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_param::interval\_max |
| --- |

Maximum Periodic Advertising Interval (N \* 1.25 ms).

Shall be less or equal to BT\_GAP\_PER\_ADV\_MAX\_INTERVAL and greater or equal to interval\_min.

## [◆ ](#a49da44a3c0e4e866ffccffae5a9a22f7)interval\_min

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_param::interval\_min |
| --- |

Minimum Periodic Advertising Interval (N \* 1.25 ms).

Shall be greater or equal to BT\_GAP\_PER\_ADV\_MIN\_INTERVAL and less or equal to interval\_max.

## [◆ ](#a9b80c2427171920f466601e7e8468814)options

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_per\_adv\_param::options |
| --- |

Bit-field of periodic advertising options.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
