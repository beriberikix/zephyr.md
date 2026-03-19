---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__le__cs__step__data__mode__3__ss__rtt.html
original_path: doxygen/html/structbt__hci__le__cs__step__data__mode__3__ss__rtt.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt Struct Reference

Subevent result step data format: Mode 3 with sounding sequence RTT support.
[More...](#details)

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_quality\_bit\_errors](#af5d8a8559400b45066bdac86fbdac411): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_quality\_aa\_check](#a657ec3570e3ad6b2ddab87bada231587): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_nadm](#a9d2428083c401d931520addde0af54fd) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_rssi](#adc4fe32bc6b7515e5bf1055f19f1a2bd) |
| union { |  |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)   [toa\_tod\_initiator](#ae2181a568ed6da32d3f60ba6d271c64f) |  |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)   [tod\_toa\_reflector](#ada4d52f54f1efa804a812c65edd8f125) |  |
| }; |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_antenna](#a9ce412ad8b18a9315b858cf1fe2a466a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_pct1](#aada8b3ff1bb0d0b9eccb846da173b3f4) [4] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_pct2](#afdebbafc06475dde12aaed73d2180f96) [4] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [antenna\_permutation\_index](#ac4067e27caa12cf9f8c6525bf6a72973) |
| struct [bt\_hci\_le\_cs\_step\_data\_tone\_info](structbt__hci__le__cs__step__data__tone__info.md) | [tone\_info](#aea13fc3e16092dcede9fb46ea719f21c) [] |

## Detailed Description

Subevent result step data format: Mode 3 with sounding sequence RTT support.

## Field Documentation

## [◆ ](#ac112c9cad8388984ccd6e83ca4457b4e)[union]

| union { ... } [bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md) |
| --- |

## [◆ ](#ac4067e27caa12cf9f8c6525bf6a72973)antenna\_permutation\_index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::antenna\_permutation\_index |
| --- |

## [◆ ](#a9ce412ad8b18a9315b858cf1fe2a466a)packet\_antenna

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_antenna |
| --- |

## [◆ ](#a9d2428083c401d931520addde0af54fd)packet\_nadm

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_nadm |
| --- |

## [◆ ](#aada8b3ff1bb0d0b9eccb846da173b3f4)packet\_pct1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_pct1[4] |
| --- |

## [◆ ](#afdebbafc06475dde12aaed73d2180f96)packet\_pct2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_pct2[4] |
| --- |

## [◆ ](#a657ec3570e3ad6b2ddab87bada231587)packet\_quality\_aa\_check

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_quality\_aa\_check |
| --- |

## [◆ ](#af5d8a8559400b45066bdac86fbdac411)packet\_quality\_bit\_errors

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_quality\_bit\_errors |
| --- |

## [◆ ](#adc4fe32bc6b7515e5bf1055f19f1a2bd)packet\_rssi

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::packet\_rssi |
| --- |

## [◆ ](#ae2181a568ed6da32d3f60ba6d271c64f)toa\_tod\_initiator

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::toa\_tod\_initiator |
| --- |

## [◆ ](#ada4d52f54f1efa804a812c65edd8f125)tod\_toa\_reflector

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::tod\_toa\_reflector |
| --- |

## [◆ ](#aea13fc3e16092dcede9fb46ea719f21c)tone\_info

| struct [bt\_hci\_le\_cs\_step\_data\_tone\_info](structbt__hci__le__cs__step__data__tone__info.md) bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt::tone\_info[] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_le\_cs\_step\_data\_mode\_3\_ss\_rtt](structbt__hci__le__cs__step__data__mode__3__ss__rtt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
