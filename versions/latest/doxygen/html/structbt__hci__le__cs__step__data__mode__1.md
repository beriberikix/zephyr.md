---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__le__cs__step__data__mode__1.html
original_path: doxygen/html/structbt__hci__le__cs__step__data__mode__1.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_le\_cs\_step\_data\_mode\_1 Struct Reference

Subevent result step data format: Mode 1.
[More...](#details)

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_quality\_bit\_errors](#a0cb4198466318a7a15cbbb172c582eeb): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_quality\_aa\_check](#a8383926e95cd9d222b91704b2ca6883e): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_nadm](#a4025cf2b229ada27e258d3d519a7b1dd) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_rssi](#a1b9df39c01ab91ab225c809db5066f70) |
| union { |  |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)   [toa\_tod\_initiator](#a1365e601f422b98747f9909d3be56b60) |  |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)   [tod\_toa\_reflector](#ab3425181b2a625fcfbbfd14477d717d1) |  |
| }; |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_antenna](#afc8221a5cab14d3842590e6cac52da4d) |

## Detailed Description

Subevent result step data format: Mode 1.

## Field Documentation

## [◆ ](#a191091979aedce48549f5ca9a3b6a0f5)[union]

| union { ... } [bt\_hci\_le\_cs\_step\_data\_mode\_1](structbt__hci__le__cs__step__data__mode__1.md) |
| --- |

## [◆ ](#afc8221a5cab14d3842590e6cac52da4d)packet\_antenna

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1::packet\_antenna |
| --- |

## [◆ ](#a4025cf2b229ada27e258d3d519a7b1dd)packet\_nadm

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1::packet\_nadm |
| --- |

## [◆ ](#a8383926e95cd9d222b91704b2ca6883e)packet\_quality\_aa\_check

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1::packet\_quality\_aa\_check |
| --- |

## [◆ ](#a0cb4198466318a7a15cbbb172c582eeb)packet\_quality\_bit\_errors

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1::packet\_quality\_bit\_errors |
| --- |

## [◆ ](#a1b9df39c01ab91ab225c809db5066f70)packet\_rssi

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1::packet\_rssi |
| --- |

## [◆ ](#a1365e601f422b98747f9909d3be56b60)toa\_tod\_initiator

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_le\_cs\_step\_data\_mode\_1::toa\_tod\_initiator |
| --- |

## [◆ ](#ab3425181b2a625fcfbbfd14477d717d1)tod\_toa\_reflector

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_le\_cs\_step\_data\_mode\_1::tod\_toa\_reflector |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_le\_cs\_step\_data\_mode\_1](structbt__hci__le__cs__step__data__mode__1.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
