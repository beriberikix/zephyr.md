---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__le__cs__step__data__mode__3.html
original_path: doxygen/html/structbt__hci__le__cs__step__data__mode__3.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_le\_cs\_step\_data\_mode\_3 Struct Reference

Subevent result step data format: Mode 3.
[More...](#details)

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_quality\_bit\_errors](#a42b8bdf1fd492be1daded674e3d733d6): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_quality\_aa\_check](#ad4c30784cc2586b5b8dcfa22e7a1f8fb): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_nadm](#a9b7373e7d3faa0cb5553d4f897c94ebc) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_rssi](#a60750ac38bf019a0c7a8656ca59fc402) |
| union { |  |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)   [toa\_tod\_initiator](#a183f3ee64a4482c9d3e0f041151fdcf9) |  |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)   [tod\_toa\_reflector](#aa0f1918115a6e550d6fab17529bbb4f2) |  |
| }; |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_antenna](#ad20e9c1deba67aa5759881b52d13311d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [antenna\_permutation\_index](#a609102fc9d42fe73c09907f54526bd40) |
| struct [bt\_hci\_le\_cs\_step\_data\_tone\_info](structbt__hci__le__cs__step__data__tone__info.md) | [tone\_info](#a9ae78aa83a22f0618491871d55f2f0b9) [] |

## Detailed Description

Subevent result step data format: Mode 3.

## Field Documentation

## [◆ ](#a9ad06cb8bcbae12253a6aead552d2a82)[union]

| union { ... } [bt\_hci\_le\_cs\_step\_data\_mode\_3](structbt__hci__le__cs__step__data__mode__3.md) |
| --- |

## [◆ ](#a609102fc9d42fe73c09907f54526bd40)antenna\_permutation\_index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3::antenna\_permutation\_index |
| --- |

## [◆ ](#ad20e9c1deba67aa5759881b52d13311d)packet\_antenna

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3::packet\_antenna |
| --- |

## [◆ ](#a9b7373e7d3faa0cb5553d4f897c94ebc)packet\_nadm

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3::packet\_nadm |
| --- |

## [◆ ](#ad4c30784cc2586b5b8dcfa22e7a1f8fb)packet\_quality\_aa\_check

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3::packet\_quality\_aa\_check |
| --- |

## [◆ ](#a42b8bdf1fd492be1daded674e3d733d6)packet\_quality\_bit\_errors

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3::packet\_quality\_bit\_errors |
| --- |

## [◆ ](#a60750ac38bf019a0c7a8656ca59fc402)packet\_rssi

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3::packet\_rssi |
| --- |

## [◆ ](#a183f3ee64a4482c9d3e0f041151fdcf9)toa\_tod\_initiator

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_le\_cs\_step\_data\_mode\_3::toa\_tod\_initiator |
| --- |

## [◆ ](#aa0f1918115a6e550d6fab17529bbb4f2)tod\_toa\_reflector

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_le\_cs\_step\_data\_mode\_3::tod\_toa\_reflector |
| --- |

## [◆ ](#a9ae78aa83a22f0618491871d55f2f0b9)tone\_info

| struct [bt\_hci\_le\_cs\_step\_data\_tone\_info](structbt__hci__le__cs__step__data__tone__info.md) bt\_hci\_le\_cs\_step\_data\_mode\_3::tone\_info[] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_le\_cs\_step\_data\_mode\_3](structbt__hci__le__cs__step__data__mode__3.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
