---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structvcpu__time__info.html
original_path: doxygen/html/structvcpu__time__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vcpu\_time\_info Struct Reference

`#include <[xen.h](xen_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [version](#a82f016f109904dd5effa7c87c8cc35fb) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pad0](#a20339e02cb0bd2993e6d4a293c6f8d3b) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [tsc\_timestamp](#a3bcf2b4d3f246bef1f1c90ceeef6c774) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [system\_time](#a8963a462f7e7ab7f3833d43adc60e06f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tsc\_to\_system\_mul](#a11b2973a6d58b5cfa31a3306d1a9ff84) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tsc\_shift](#af7d9bee0e8e4eab21b4388f60b4febb7) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [pad1](#a871e2e15e0a3707c4662456b62d14677) [3] |

## Field Documentation

## [◆ ](#a20339e02cb0bd2993e6d4a293c6f8d3b)pad0

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vcpu\_time\_info::pad0 |
| --- |

## [◆ ](#a871e2e15e0a3707c4662456b62d14677)pad1

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) vcpu\_time\_info::pad1[3] |
| --- |

## [◆ ](#a8963a462f7e7ab7f3833d43adc60e06f)system\_time

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) vcpu\_time\_info::system\_time |
| --- |

## [◆ ](#af7d9bee0e8e4eab21b4388f60b4febb7)tsc\_shift

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) vcpu\_time\_info::tsc\_shift |
| --- |

## [◆ ](#a3bcf2b4d3f246bef1f1c90ceeef6c774)tsc\_timestamp

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) vcpu\_time\_info::tsc\_timestamp |
| --- |

## [◆ ](#a11b2973a6d58b5cfa31a3306d1a9ff84)tsc\_to\_system\_mul

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vcpu\_time\_info::tsc\_to\_system\_mul |
| --- |

## [◆ ](#a82f016f109904dd5effa7c87c8cc35fb)version

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vcpu\_time\_info::version |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[xen.h](xen_8h_source.md)

- [vcpu\_time\_info](structvcpu__time__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
