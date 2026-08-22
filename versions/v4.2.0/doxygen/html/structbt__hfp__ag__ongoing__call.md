---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__hfp__ag__ongoing__call.html
original_path: doxygen/html/structbt__hfp__ag__ongoing__call.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hfp\_ag\_ongoing\_call Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Hands Free Profile - Audio Gateway (HFP-AG)](group__bt__hfp__ag.md)

The ongoing call.
[More...](#details)

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char | [number](#a1e5800a9c0f37539d0505d3223a35e2f) [CONFIG\_BT\_HFP\_AG\_PHONE\_NUMBER\_MAX\_LEN+1] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#a26a77093f5aace7dd2d5693f4cb82189) |
| enum [bt\_hfp\_ag\_call\_dir](group__bt__hfp__ag.md#ga019020ee2ed73c218f7dadf8371bf9a6) | [dir](#a506610c17544daf8a0238a2c4d285526) |
| enum [bt\_hfp\_ag\_call\_status](group__bt__hfp__ag.md#gad2220b4a470cb3d537cf09492847568e) | [status](#ac865f464436c3e73561fa8f6fcf09947) |

## Detailed Description

The ongoing call.

Parameters
:   | [number](#a1e5800a9c0f37539d0505d3223a35e2f) | Phone number terminated with '\0' of the call. |
    | --- | --- |
    | [type](#a26a77093f5aace7dd2d5693f4cb82189) | Specify the format of the phone number. |
    | [dir](#a506610c17544daf8a0238a2c4d285526) | Call direction. |
    | [status](#ac865f464436c3e73561fa8f6fcf09947) | The status of the call. |

## Field Documentation

## [◆ ](#a506610c17544daf8a0238a2c4d285526)dir

| enum [bt\_hfp\_ag\_call\_dir](group__bt__hfp__ag.md#ga019020ee2ed73c218f7dadf8371bf9a6) bt\_hfp\_ag\_ongoing\_call::dir |
| --- |

## [◆ ](#a1e5800a9c0f37539d0505d3223a35e2f)number

| char bt\_hfp\_ag\_ongoing\_call::number[CONFIG\_BT\_HFP\_AG\_PHONE\_NUMBER\_MAX\_LEN+1] |
| --- |

## [◆ ](#ac865f464436c3e73561fa8f6fcf09947)status

| enum [bt\_hfp\_ag\_call\_status](group__bt__hfp__ag.md#gad2220b4a470cb3d537cf09492847568e) bt\_hfp\_ag\_ongoing\_call::status |
| --- |

## [◆ ](#a26a77093f5aace7dd2d5693f4cb82189)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hfp\_ag\_ongoing\_call::type |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[hfp\_ag.h](hfp__ag_8h_source.md)

- [bt\_hfp\_ag\_ongoing\_call](structbt__hfp__ag__ongoing__call.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
