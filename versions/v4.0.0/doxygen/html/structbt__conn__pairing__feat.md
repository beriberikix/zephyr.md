---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__conn__pairing__feat.html
original_path: doxygen/html/structbt__conn__pairing__feat.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_pairing\_feat Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Pairing request and pairing response info structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [io\_capability](#a68005cea273c8e76c086502001b258b0) |
|  | IO Capability, Core Spec. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [oob\_data\_flag](#afb03164960db62b4b4cf70d3f0134099) |
|  | OOB data flag, Core Spec. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [auth\_req](#af9a977b1e0f9d4eada26a82d92eaec54) |
|  | AuthReq, Core Spec. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_enc\_key\_size](#abe1d7d4bd9f4b551a2d0c69adc75bd40) |
|  | Maximum Encryption Key Size, Core Spec. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [init\_key\_dist](#a70adc125b875348ec8d273dea3b470d8) |
|  | Initiator Key Distribution/Generation, Core Spec. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [resp\_key\_dist](#a49f9f02e232e91f7f7a530aa7f226cba) |
|  | Responder Key Distribution/Generation, Core Spec. |

## Detailed Description

Pairing request and pairing response info structure.

This structure is the same for both smp\_pairing\_req and smp\_pairing\_rsp and a subset of the packet data, except for the initial Code octet. It is documented in Core Spec. Vol. 3, Part H, 3.5.1 and 3.5.2.

## Field Documentation

## [◆ ](#af9a977b1e0f9d4eada26a82d92eaec54)auth\_req

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_pairing\_feat::auth\_req |
| --- |

AuthReq, Core Spec.

Vol 3, Part H, 3.5.1, Fig. 3.3

## [◆ ](#a70adc125b875348ec8d273dea3b470d8)init\_key\_dist

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_pairing\_feat::init\_key\_dist |
| --- |

Initiator Key Distribution/Generation, Core Spec.

Vol 3, Part H, 3.6.1, Fig. 3.11

## [◆ ](#a68005cea273c8e76c086502001b258b0)io\_capability

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_pairing\_feat::io\_capability |
| --- |

IO Capability, Core Spec.

Vol 3, Part H, 3.5.1, Table 3.4

## [◆ ](#abe1d7d4bd9f4b551a2d0c69adc75bd40)max\_enc\_key\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_pairing\_feat::max\_enc\_key\_size |
| --- |

Maximum Encryption Key Size, Core Spec.

Vol 3, Part H, 3.5.1

## [◆ ](#afb03164960db62b4b4cf70d3f0134099)oob\_data\_flag

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_pairing\_feat::oob\_data\_flag |
| --- |

OOB data flag, Core Spec.

Vol 3, Part H, 3.5.1, Table 3.5

## [◆ ](#a49f9f02e232e91f7f7a530aa7f226cba)resp\_key\_dist

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_pairing\_feat::resp\_key\_dist |
| --- |

Responder Key Distribution/Generation, Core Spec.

Vol 3, Part H 3.6.1, Fig. 3.11

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_pairing\_feat](structbt__conn__pairing__feat.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
