---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsim7080__sms.html
original_path: doxygen/html/structsim7080__sms.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sim7080\_sms Struct Reference

Buffer structure for sms.
[More...](#details)

`#include <[simcom-sim7080.h](simcom-sim7080_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [first\_octet](#a8c41c51b2bfaea343b5340ba8c02b56a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tp\_pid](#aaaa3957cf7e0597dfbf309da0b64b54f) |
| enum [sim7080\_sms\_stat](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eb) | [stat](#a9dc5291721c65a949a8d351b2408a253) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [index](#abd559c83ec2896660cffbe8df1be687b) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [year](#afdb63d3e307c3368149f6d0183541379) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [month](#a3db8a08ab147d1765eec75a0b93f3cb7) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [day](#a30773852fece821bd82fc97e02667bd9) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [hour](#af207e345f8c024258c5c011a28ad28c0) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [minute](#a705e0cbd5654677e6b99cd6ed22767be) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [second](#a343f290be0f3ca62618c47ff7e54cda2) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [timezone](#ac5a04784c883710d8794bf4762bb9078) |  |
| } | [time](#af97df12fbebedf53af7cd4e505fe9342) |
| char | [data](#a7dd5c165eafbf70f3e1f01efa71bf640) [160+1] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_len](#af9aeb3cb06325e0d1e52db6d78567feb) |

## Detailed Description

Buffer structure for sms.

## Field Documentation

## [◆ ](#a7dd5c165eafbf70f3e1f01efa71bf640)data

| char sim7080\_sms::data[160+1] |
| --- |

## [◆ ](#af9aeb3cb06325e0d1e52db6d78567feb)data\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sim7080\_sms::data\_len |
| --- |

## [◆ ](#a30773852fece821bd82fc97e02667bd9)day

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sim7080\_sms::day |
| --- |

## [◆ ](#a8c41c51b2bfaea343b5340ba8c02b56a)first\_octet

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sim7080\_sms::first\_octet |
| --- |

## [◆ ](#af207e345f8c024258c5c011a28ad28c0)hour

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sim7080\_sms::hour |
| --- |

## [◆ ](#abd559c83ec2896660cffbe8df1be687b)index

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sim7080\_sms::index |
| --- |

## [◆ ](#a705e0cbd5654677e6b99cd6ed22767be)minute

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sim7080\_sms::minute |
| --- |

## [◆ ](#a3db8a08ab147d1765eec75a0b93f3cb7)month

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sim7080\_sms::month |
| --- |

## [◆ ](#a343f290be0f3ca62618c47ff7e54cda2)second

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sim7080\_sms::second |
| --- |

## [◆ ](#a9dc5291721c65a949a8d351b2408a253)stat

| enum [sim7080\_sms\_stat](simcom-sim7080_8h.md#a04f3c0bce4f7d2b35762dc92f0aa20eb) sim7080\_sms::stat |
| --- |

## [◆ ](#af97df12fbebedf53af7cd4e505fe9342)[struct]

| struct { ... } sim7080\_sms::time |
| --- |

## [◆ ](#ac5a04784c883710d8794bf4762bb9078)timezone

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sim7080\_sms::timezone |
| --- |

## [◆ ](#aaaa3957cf7e0597dfbf309da0b64b54f)tp\_pid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sim7080\_sms::tp\_pid |
| --- |

## [◆ ](#afdb63d3e307c3368149f6d0183541379)year

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sim7080\_sms::year |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/modem/[simcom-sim7080.h](simcom-sim7080_8h_source.md)

- [sim7080\_sms](structsim7080__sms.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
