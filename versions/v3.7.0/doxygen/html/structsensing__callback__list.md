---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsensing__callback__list.html
original_path: doxygen/html/structsensing__callback__list.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_callback\_list Struct Reference

[Sensing](group__sensing.md) » [Sensing Subsystem API](group__sensing__api.md)

Sensing subsystem event callback list.
[More...](#details)

`#include <[sensing.h](sensing_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sensing\_data\_event\_t](group__sensing__api.md#ga5440a8914b664209d62388183b3c89ea) | [on\_data\_event](#a7d0d7c878e338f19fd48c66cda9d04fc) |
|  | Callback function for a sensor data event. |
| void \* | [context](#a43504dbe7d484f0d0e7d33b8bb6318d4) |
|  | Associated context with on\_data\_event. |

## Detailed Description

Sensing subsystem event callback list.

## Field Documentation

## [◆ ](#a43504dbe7d484f0d0e7d33b8bb6318d4)context

| void\* sensing\_callback\_list::context |
| --- |

Associated context with on\_data\_event.

## [◆ ](#a7d0d7c878e338f19fd48c66cda9d04fc)on\_data\_event

| [sensing\_data\_event\_t](group__sensing__api.md#ga5440a8914b664209d62388183b3c89ea) sensing\_callback\_list::on\_data\_event |
| --- |

Callback function for a sensor data event.

---

The documentation for this struct was generated from the following file:

- zephyr/sensing/[sensing.h](sensing_8h_source.md)

- [sensing\_callback\_list](structsensing__callback__list.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
