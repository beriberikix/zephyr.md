---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__sdp__discover__params.html
original_path: doxygen/html/structbt__sdp__discover__params.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| union { |  |
| const struct [bt\_uuid](structbt__uuid.md) \*   [uuid](#a4c6073d7afda09be462902f5a95eaaed) |  |
|  | UUID (service) to be discovered on remote SDP entity. [More...](#a4c6073d7afda09be462902f5a95eaaed) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [handle](#a2be942f3d0f18c56567dafa45af9c53e) |  |
|  | Service record handle. [More...](#a2be942f3d0f18c56567dafa45af9c53e) |
| }; |  |
| [bt\_sdp\_discover\_func\_t](group__bt__sdp.md#gad672a89277b276d1b702fe07302c468e) | [func](#a650143f0733958cf1186543c3469facc) |
|  | Discover callback to be called on resolved SDP record. |
| struct [net\_buf\_pool](structnet__buf__pool.md) \* | [pool](#a6f8728e5b74211852e2ce8872c21e5fb) |
|  | Memory buffer enabled by user for SDP query results. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#acec0306279408087352804fdf76560de) |
|  | Discover type. |

## Detailed Description

Main user structure used in SDP discovery of remote.

## Field Documentation

## [◆ ](#afdb1c56544bf5b97f98d79e26bbf53c0)[union]

| union { ... } [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md) |
| --- |

## [◆ ](#a650143f0733958cf1186543c3469facc)func

| [bt\_sdp\_discover\_func\_t](group__bt__sdp.md#gad672a89277b276d1b702fe07302c468e) bt\_sdp\_discover\_params::func |
| --- |

Discover callback to be called on resolved SDP record.

## [◆ ](#a2be942f3d0f18c56567dafa45af9c53e)handle

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_sdp\_discover\_params::handle |
| --- |

Service record handle.

## [◆ ](#a6f8728e5b74211852e2ce8872c21e5fb)pool

| struct [net\_buf\_pool](structnet__buf__pool.md)\* bt\_sdp\_discover\_params::pool |
| --- |

Memory buffer enabled by user for SDP query results.

## [◆ ](#acec0306279408087352804fdf76560de)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_sdp\_discover\_params::type |
| --- |

Discover type.

## [◆ ](#a4c6073d7afda09be462902f5a95eaaed)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_sdp\_discover\_params::uuid |
| --- |

UUID (service) to be discovered on remote SDP entity.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[sdp.h](sdp_8h_source.md)

- [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
