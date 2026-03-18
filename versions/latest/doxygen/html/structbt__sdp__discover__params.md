---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__sdp__discover__params.html
original_path: doxygen/html/structbt__sdp__discover__params.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_sdp\_discover\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Service Discovery Protocol (SDP)](group__bt__sdp.md)

Main user structure used in SDP discovery of remote.
[More...](#details)

`#include <[sdp.h](sdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_uuid](structbt__uuid.md) \* | [uuid](#a4c6073d7afda09be462902f5a95eaaed) |
|  | UUID (service) to be discovered on remote SDP entity. |
| [bt\_sdp\_discover\_func\_t](group__bt__sdp.md#gae5fa4166e3b909f9dcaace11b302f98f) | [func](#a650143f0733958cf1186543c3469facc) |
|  | Discover callback to be called on resolved SDP record. |
| struct [net\_buf\_pool](structnet__buf__pool.md) \* | [pool](#a6f8728e5b74211852e2ce8872c21e5fb) |
|  | Memory buffer enabled by user for SDP query results. |

## Detailed Description

Main user structure used in SDP discovery of remote.

## Field Documentation

## [◆ ](#a650143f0733958cf1186543c3469facc)func

| [bt\_sdp\_discover\_func\_t](group__bt__sdp.md#gae5fa4166e3b909f9dcaace11b302f98f) bt\_sdp\_discover\_params::func |
| --- |

Discover callback to be called on resolved SDP record.

## [◆ ](#a6f8728e5b74211852e2ce8872c21e5fb)pool

| struct [net\_buf\_pool](structnet__buf__pool.md)\* bt\_sdp\_discover\_params::pool |
| --- |

Memory buffer enabled by user for SDP query results.

## [◆ ](#a4c6073d7afda09be462902f5a95eaaed)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_sdp\_discover\_params::uuid |
| --- |

UUID (service) to be discovered on remote SDP entity.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[sdp.h](sdp_8h_source.md)

- [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
