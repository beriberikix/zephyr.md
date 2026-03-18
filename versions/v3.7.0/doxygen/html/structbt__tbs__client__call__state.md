---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__tbs__client__call__state.html
original_path: doxygen/html/structbt__tbs__client__call__state.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_tbs\_client\_call\_state Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Telephone Bearer Service (TBS)](group__bt__tbs.md)

Struct to hold a call state.
[More...](#details)

`#include <[tbs.h](tbs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [index](#a3d6eb4dda7adcd16c04ebbd41242c292) |
|  | Index of the call. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [state](#a3e758ad6d0b35f26f43584e50c9a9895) |
|  | State of the call (see BT\_TBS\_CALL\_STATE\_\*). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a57ed9dd726faa3c219e1c858ad6659d9) |
|  | Call flags (see BT\_TBS\_CALL\_FLAG\_\*). |

## Detailed Description

Struct to hold a call state.

## Field Documentation

## [◆ ](#a57ed9dd726faa3c219e1c858ad6659d9)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_tbs\_client\_call\_state::flags |
| --- |

Call flags (see BT\_TBS\_CALL\_FLAG\_\*).

## [◆ ](#a3d6eb4dda7adcd16c04ebbd41242c292)index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_tbs\_client\_call\_state::index |
| --- |

Index of the call.

## [◆ ](#a3e758ad6d0b35f26f43584e50c9a9895)state

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_tbs\_client\_call\_state::state |
| --- |

State of the call (see BT\_TBS\_CALL\_STATE\_\*).

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[tbs.h](tbs_8h_source.md)

- [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
