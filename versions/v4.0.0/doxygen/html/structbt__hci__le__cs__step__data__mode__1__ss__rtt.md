---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__le__cs__step__data__mode__1__ss__rtt.html
original_path: doxygen/html/structbt__hci__le__cs__step__data__mode__1__ss__rtt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt Struct Reference

Subevent result step data format: Mode 1 with sounding sequence RTT support.
[More...](#details)

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_quality\_bit\_errors](#a515fde1d568a19ccf6ebefe9052866a4): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_quality\_aa\_check](#ad8f9ca9dda852b435848b988ad872797): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_nadm](#a511b281fb1c16fd7d0eaf731906a4292) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_rssi](#a5ec9c30063c09285804973008533e5cb) |
| union { |  |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)   [toa\_tod\_initiator](#a77bbcd9451360ad97813f9357e44766e) |  |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)   [tod\_toa\_reflector](#ace3843bc24616950f04150b2f86abad4) |  |
| }; |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_antenna](#abf20351ab0eaf3a7139a464f1d1a72b0) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_pct1](#a3f8ba85b776f732ebc1086a4317849a1) [4] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_pct2](#a9f969aa6fc134a9e618d07f177d2b7fd) [4] |

## Detailed Description

Subevent result step data format: Mode 1 with sounding sequence RTT support.

## Field Documentation

## [◆ ](#a799bedf4b1cdd92b38eb926ca7fb1ec5)[union]

| union { ... } [bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md) |
| --- |

## [◆ ](#abf20351ab0eaf3a7139a464f1d1a72b0)packet\_antenna

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_antenna |
| --- |

## [◆ ](#a511b281fb1c16fd7d0eaf731906a4292)packet\_nadm

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_nadm |
| --- |

## [◆ ](#a3f8ba85b776f732ebc1086a4317849a1)packet\_pct1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_pct1[4] |
| --- |

## [◆ ](#a9f969aa6fc134a9e618d07f177d2b7fd)packet\_pct2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_pct2[4] |
| --- |

## [◆ ](#ad8f9ca9dda852b435848b988ad872797)packet\_quality\_aa\_check

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_quality\_aa\_check |
| --- |

## [◆ ](#a515fde1d568a19ccf6ebefe9052866a4)packet\_quality\_bit\_errors

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_quality\_bit\_errors |
| --- |

## [◆ ](#a5ec9c30063c09285804973008533e5cb)packet\_rssi

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::packet\_rssi |
| --- |

## [◆ ](#a77bbcd9451360ad97813f9357e44766e)toa\_tod\_initiator

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::toa\_tod\_initiator |
| --- |

## [◆ ](#ace3843bc24616950f04150b2f86abad4)tod\_toa\_reflector

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt::tod\_toa\_reflector |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_le\_cs\_step\_data\_mode\_1\_ss\_rtt](structbt__hci__le__cs__step__data__mode__1__ss__rtt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
