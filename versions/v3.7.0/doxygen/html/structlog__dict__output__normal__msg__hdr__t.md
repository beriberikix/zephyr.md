---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structlog__dict__output__normal__msg__hdr__t.html
original_path: doxygen/html/structlog__dict__output__normal__msg__hdr__t.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_dict\_output\_normal\_msg\_hdr\_t Struct Reference

Output header for one dictionary based log message.
[More...](#details)

`#include <[log_output_dict.h](log__output__dict_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#a5c2916995965e12d5504d5f9ae3ea04f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [domain](#ac70bc70b6c59d6905b86ddb94f0f8f11):4 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [level](#a41b40465b8d86d25cfdf61fd8067c60f):4 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [package\_len](#a207adee5780cc0c33adc4a3e9b28d2ed):16 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [data\_len](#a7fb4f8934358565646f35c20238a1289):16 |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [source](#a6570a840284fee5b84dacc746ce838fc) |
| [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) | [timestamp](#adb10537b51af8632dd9d9e18e18f15e4) |

## Detailed Description

Output header for one dictionary based log message.

## Field Documentation

## [◆ ](#a7fb4f8934358565646f35c20238a1289)data\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_dict\_output\_normal\_msg\_hdr\_t::data\_len |
| --- |

## [◆ ](#ac70bc70b6c59d6905b86ddb94f0f8f11)domain

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_dict\_output\_normal\_msg\_hdr\_t::domain |
| --- |

## [◆ ](#a41b40465b8d86d25cfdf61fd8067c60f)level

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_dict\_output\_normal\_msg\_hdr\_t::level |
| --- |

## [◆ ](#a207adee5780cc0c33adc4a3e9b28d2ed)package\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_dict\_output\_normal\_msg\_hdr\_t::package\_len |
| --- |

## [◆ ](#a6570a840284fee5b84dacc746ce838fc)source

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) log\_dict\_output\_normal\_msg\_hdr\_t::source |
| --- |

## [◆ ](#adb10537b51af8632dd9d9e18e18f15e4)timestamp

| [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) log\_dict\_output\_normal\_msg\_hdr\_t::timestamp |
| --- |

## [◆ ](#a5c2916995965e12d5504d5f9ae3ea04f)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_dict\_output\_normal\_msg\_hdr\_t::type |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_output\_dict.h](log__output__dict_8h_source.md)

- [log\_dict\_output\_normal\_msg\_hdr\_t](structlog__dict__output__normal__msg__hdr__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
