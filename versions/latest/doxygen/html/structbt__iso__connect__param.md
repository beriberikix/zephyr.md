---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__iso__connect__param.html
original_path: doxygen/html/structbt__iso__connect__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_connect\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO connection parameters structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_iso\_chan](structbt__iso__chan.md) \* | [iso\_chan](#ad004956584d2d065d8c0c52959f350d5) |
|  | The ISO channel to connect. |
| struct bt\_conn \* | [acl](#aba2f3838e03a1e31699a4623ba93d372) |
|  | The ACL connection. |

## Detailed Description

ISO connection parameters structure.

## Field Documentation

## [◆ ](#aba2f3838e03a1e31699a4623ba93d372)acl

| struct bt\_conn\* bt\_iso\_connect\_param::acl |
| --- |

The ACL connection.

## [◆ ](#ad004956584d2d065d8c0c52959f350d5)iso\_chan

| struct [bt\_iso\_chan](structbt__iso__chan.md)\* bt\_iso\_connect\_param::iso\_chan |
| --- |

The ISO channel to connect.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_connect\_param](structbt__iso__connect__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
