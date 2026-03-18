---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__conn__oob__info.html
original_path: doxygen/html/structbt__conn__oob__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_oob\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Info Structure for OOB pairing.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Public Types | |
| --- | --- |
| enum | { [BT\_CONN\_OOB\_LE\_LEGACY](#a433c4a8e1efcb663ad369d018d999b0ea4c33ea839306256a198c29ea783c659b) , [BT\_CONN\_OOB\_LE\_SC](#a433c4a8e1efcb663ad369d018d999b0eacd02773beb42df3fb6cbaa2fa2abda1e) } |
|  | Type of OOB pairing method. [More...](#a433c4a8e1efcb663ad369d018d999b0e) |

| Data Fields | |
| --- | --- |
| enum bt\_conn\_oob\_info:: { ... } | [type](#aa793302d7c6c41a1b714ab219a1f14c9) |
|  | Type of OOB pairing method. |
| union { |  |
| struct { |  |
| enum | { [BT\_CONN\_OOB\_LOCAL\_ONLY](structbt__conn__oob__info_1_1_0d143143115062310336126347360141254141124170204126_1_1_0d0370572345da5e2db66fbbe9ac8ee93588533f4bf.md#a9b9715db62fd8d11ca4e8d837c86723caa45e013117ddf4acbf9c9fb832e898f4) , [BT\_CONN\_OOB\_REMOTE\_ONLY](structbt__conn__oob__info_1_1_0d143143115062310336126347360141254141124170204126_1_1_0d0370572345da5e2db66fbbe9ac8ee93588533f4bf.md#a9b9715db62fd8d11ca4e8d837c86723caab4e57ff72c0a242e51feb00e33877f5) , [BT\_CONN\_OOB\_BOTH\_PEERS](structbt__conn__oob__info_1_1_0d143143115062310336126347360141254141124170204126_1_1_0d0370572345da5e2db66fbbe9ac8ee93588533f4bf.md#a9b9715db62fd8d11ca4e8d837c86723caff99c16daa4fb26c24338954c12405d3) , [BT\_CONN\_OOB\_NO\_DATA](structbt__conn__oob__info_1_1_0d143143115062310336126347360141254141124170204126_1_1_0d0370572345da5e2db66fbbe9ac8ee93588533f4bf.md#a9b9715db62fd8d11ca4e8d837c86723cac302ce1567ab609cb29ebdca5b7f24bd) } |
|  | OOB data configuration. [More...](structbt__conn__oob__info_1_1_0d143143115062310336126347360141254141124170204126_1_1_0d0370572345da5e2db66fbbe9ac8ee93588533f4bf.md#a9b9715db62fd8d11ca4e8d837c86723c) |
| enum bt\_conn\_oob\_info:: { ... }    [oob\_config](#aa20bbff037e6878216d7dd45938bca76) |  |
|  | OOB data configuration. [More...](#aa20bbff037e6878216d7dd45938bca76) |
| }   [lesc](#ad721c4bbe51bec994362b35944579240) |
|  | LE Secure Connections OOB pairing parameters. [More...](#ad721c4bbe51bec994362b35944579240) |
| }; |  |

## Detailed Description

Info Structure for OOB pairing.

## Member Enumeration Documentation

## [◆ ](#a433c4a8e1efcb663ad369d018d999b0e)anonymous enum

| anonymous enum |
| --- |

Type of OOB pairing method.

| Enumerator | |
| --- | --- |
| BT\_CONN\_OOB\_LE\_LEGACY | LE legacy pairing. |
| BT\_CONN\_OOB\_LE\_SC | LE SC pairing. |

## Field Documentation

## [◆ ](#a1387c2dcffe2f153e856f96b2660256a)[union]

| union { ... } [bt\_conn\_oob\_info](structbt__conn__oob__info.md) |
| --- |

## [◆ ](#ad721c4bbe51bec994362b35944579240)[struct]

| struct { ... } bt\_conn\_oob\_info::lesc |
| --- |

LE Secure Connections OOB pairing parameters.

## [◆ ](#aa20bbff037e6878216d7dd45938bca76)[]

| enum { ... } bt\_conn\_oob\_info::oob\_config |
| --- |

OOB data configuration.

## [◆ ](#aa793302d7c6c41a1b714ab219a1f14c9)[]

| enum { ... } bt\_conn\_oob\_info::type |
| --- |

Type of OOB pairing method.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_oob\_info](structbt__conn__oob__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
