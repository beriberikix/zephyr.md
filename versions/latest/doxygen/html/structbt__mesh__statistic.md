---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__statistic.html
original_path: doxygen/html/structbt__mesh__statistic.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_statistic Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Statistic](group__bt__mesh__stat.md)

The structure that keeps statistics of mesh frames handling.
[More...](#details)

`#include <[statistic.h](statistic_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rx\_adv](#a5c8d77c2d32964f0a54420aafff9a4e1) |
|  | All received frames passed basic validation and decryption. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rx\_loopback](#a448c73e05fd8055baaa64532275d9c69) |
|  | Received frames over loopback. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rx\_proxy](#aa86617d0c3cfa7e2ed7e10e4c3ac8b5c) |
|  | Received frames over proxy. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rx\_uknown](#af7c764c6b702957180d8b74193207a0e) |
|  | Received over unknown interface. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tx\_adv\_relay\_planned](#a1979c5798d7d015bf4cf0c30716d3e4f) |
|  | Counter of frames that were initiated to relay over advertiser bearer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tx\_adv\_relay\_succeeded](#a139484340d2bd3fae763b23e91648e0e) |
|  | Counter of frames that succeeded relaying over advertiser bearer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tx\_local\_planned](#a2c47d080eac1050422d36402a9771fa6) |
|  | Counter of frames that were initiated to send over advertiser bearer locally. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tx\_local\_succeeded](#a9da26f6d5ad7b91b69b95e4d4a70bf71) |
|  | Counter of frames that succeeded to send over advertiser bearer locally. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tx\_friend\_planned](#a0f60214d1f2480bc0025415064dd79e8) |
|  | Counter of frames that were initiated to send over friend bearer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tx\_friend\_succeeded](#aa4d83bb57f86723899bc2fe25342423d) |
|  | Counter of frames that succeeded to send over friend bearer. |

## Detailed Description

The structure that keeps statistics of mesh frames handling.

## Field Documentation

## [◆ ](#a5c8d77c2d32964f0a54420aafff9a4e1)rx\_adv

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_statistic::rx\_adv |
| --- |

All received frames passed basic validation and decryption.

Received frames over advertiser.

## [◆ ](#a448c73e05fd8055baaa64532275d9c69)rx\_loopback

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_statistic::rx\_loopback |
| --- |

Received frames over loopback.

## [◆ ](#aa86617d0c3cfa7e2ed7e10e4c3ac8b5c)rx\_proxy

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_statistic::rx\_proxy |
| --- |

Received frames over proxy.

## [◆ ](#af7c764c6b702957180d8b74193207a0e)rx\_uknown

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_statistic::rx\_uknown |
| --- |

Received over unknown interface.

## [◆ ](#a1979c5798d7d015bf4cf0c30716d3e4f)tx\_adv\_relay\_planned

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_statistic::tx\_adv\_relay\_planned |
| --- |

Counter of frames that were initiated to relay over advertiser bearer.

## [◆ ](#a139484340d2bd3fae763b23e91648e0e)tx\_adv\_relay\_succeeded

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_statistic::tx\_adv\_relay\_succeeded |
| --- |

Counter of frames that succeeded relaying over advertiser bearer.

## [◆ ](#a0f60214d1f2480bc0025415064dd79e8)tx\_friend\_planned

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_statistic::tx\_friend\_planned |
| --- |

Counter of frames that were initiated to send over friend bearer.

## [◆ ](#aa4d83bb57f86723899bc2fe25342423d)tx\_friend\_succeeded

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_statistic::tx\_friend\_succeeded |
| --- |

Counter of frames that succeeded to send over friend bearer.

## [◆ ](#a2c47d080eac1050422d36402a9771fa6)tx\_local\_planned

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_statistic::tx\_local\_planned |
| --- |

Counter of frames that were initiated to send over advertiser bearer locally.

## [◆ ](#a9da26f6d5ad7b91b69b95e4d4a70bf71)tx\_local\_succeeded

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_statistic::tx\_local\_succeeded |
| --- |

Counter of frames that succeeded to send over advertiser bearer locally.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[statistic.h](statistic_8h_source.md)

- [bt\_mesh\_statistic](structbt__mesh__statistic.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
