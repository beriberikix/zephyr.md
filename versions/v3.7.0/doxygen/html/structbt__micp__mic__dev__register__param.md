---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__micp__mic__dev__register__param.html
original_path: doxygen/html/structbt__micp__mic__dev__register__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_micp\_mic\_dev\_register\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Microphone Control Profile (MICP)](group__bt__gatt__micp.md)

Register parameters structure for Microphone Control Service.
[More...](#details)

`#include <[micp.h](micp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_aics\_register\_param](structbt__aics__register__param.md) | [aics\_param](#a7c46803c91e55e5c44e8835817e975e3) [0] |
|  | Register parameter structure for Audio Input Control Services. |
| struct [bt\_micp\_mic\_dev\_cb](structbt__micp__mic__dev__cb.md) \* | [cb](#adbb6cf96e7f1d3e48b88cd3fbc5fd71a) |
|  | Microphone Control Profile callback structure. |

## Detailed Description

Register parameters structure for Microphone Control Service.

## Field Documentation

## [◆ ](#a7c46803c91e55e5c44e8835817e975e3)aics\_param

| struct [bt\_aics\_register\_param](structbt__aics__register__param.md) bt\_micp\_mic\_dev\_register\_param::aics\_param[0] |
| --- |

Register parameter structure for Audio Input Control Services.

## [◆ ](#adbb6cf96e7f1d3e48b88cd3fbc5fd71a)cb

| struct [bt\_micp\_mic\_dev\_cb](structbt__micp__mic__dev__cb.md)\* bt\_micp\_mic\_dev\_register\_param::cb |
| --- |

Microphone Control Profile callback structure.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[micp.h](micp_8h_source.md)

- [bt\_micp\_mic\_dev\_register\_param](structbt__micp__mic__dev__register__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
