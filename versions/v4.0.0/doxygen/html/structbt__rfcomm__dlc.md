---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__rfcomm__dlc.html
original_path: doxygen/html/structbt__rfcomm__dlc.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_rfcomm\_dlc Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [RFCOMM](group__bt__rfcomm.md)

RFCOMM DLC structure.
[More...](#details)

`#include <[rfcomm.h](rfcomm_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_work\_delayable](structk__work__delayable.md) | [rtx\_work](#a82bcf4d9e08dba8d610e92b45abb9ac2) |
| struct [k\_fifo](structk__fifo.md) | [tx\_queue](#a194bfdb88a7fcfcf9cfee6fe878bdee8) |
| struct k\_sem | [tx\_credits](#a29b3c942a1d434214637e5d00b68fb33) |
| struct bt\_rfcomm\_session \* | [session](#af134e53ac7db47f18de810dbeacdc500) |
| struct [bt\_rfcomm\_dlc\_ops](structbt__rfcomm__dlc__ops.md) \* | [ops](#a0054c0b539b947688555b5663c585bb7) |
| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) | [required\_sec\_level](#ab298ebd444566533018eabdc5a69c8ba) |
| [bt\_rfcomm\_role\_t](group__bt__rfcomm.md#ga11f290d34ad631afaa10caf2cefd72b9) | [role](#a984c80865ff8f6b6bc19d3a978e279d0) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mtu](#a2334abbaacad9b98c2cb2c5650644854) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dlci](#a20d9d284da592d268efbecf29313aed8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [state](#ac7f484917494af6a355500cc181ed4ec) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_credit](#ac946b1f3f017a9ef50a8079aa5846df3) |
| struct [k\_thread](structk__thread.md) | [tx\_thread](#aef7415017cc80c20031804494290675d) |

## Detailed Description

RFCOMM DLC structure.

## Field Documentation

## [◆ ](#a20d9d284da592d268efbecf29313aed8)dlci

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_rfcomm\_dlc::dlci |
| --- |

## [◆ ](#a2334abbaacad9b98c2cb2c5650644854)mtu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_rfcomm\_dlc::mtu |
| --- |

## [◆ ](#a0054c0b539b947688555b5663c585bb7)ops

| struct [bt\_rfcomm\_dlc\_ops](structbt__rfcomm__dlc__ops.md)\* bt\_rfcomm\_dlc::ops |
| --- |

## [◆ ](#ab298ebd444566533018eabdc5a69c8ba)required\_sec\_level

| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) bt\_rfcomm\_dlc::required\_sec\_level |
| --- |

## [◆ ](#a984c80865ff8f6b6bc19d3a978e279d0)role

| [bt\_rfcomm\_role\_t](group__bt__rfcomm.md#ga11f290d34ad631afaa10caf2cefd72b9) bt\_rfcomm\_dlc::role |
| --- |

## [◆ ](#a82bcf4d9e08dba8d610e92b45abb9ac2)rtx\_work

| struct [k\_work\_delayable](structk__work__delayable.md) bt\_rfcomm\_dlc::rtx\_work |
| --- |

## [◆ ](#ac946b1f3f017a9ef50a8079aa5846df3)rx\_credit

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_rfcomm\_dlc::rx\_credit |
| --- |

## [◆ ](#af134e53ac7db47f18de810dbeacdc500)session

| struct bt\_rfcomm\_session\* bt\_rfcomm\_dlc::session |
| --- |

## [◆ ](#ac7f484917494af6a355500cc181ed4ec)state

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_rfcomm\_dlc::state |
| --- |

## [◆ ](#a29b3c942a1d434214637e5d00b68fb33)tx\_credits

| struct k\_sem bt\_rfcomm\_dlc::tx\_credits |
| --- |

## [◆ ](#a194bfdb88a7fcfcf9cfee6fe878bdee8)tx\_queue

| struct [k\_fifo](structk__fifo.md) bt\_rfcomm\_dlc::tx\_queue |
| --- |

## [◆ ](#aef7415017cc80c20031804494290675d)tx\_thread

| struct [k\_thread](structk__thread.md) bt\_rfcomm\_dlc::tx\_thread |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[rfcomm.h](rfcomm_8h_source.md)

- [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
