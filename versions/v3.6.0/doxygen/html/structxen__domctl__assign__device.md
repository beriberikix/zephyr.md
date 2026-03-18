---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structxen__domctl__assign__device.html
original_path: doxygen/html/structxen__domctl__assign__device.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xen\_domctl\_assign\_device Struct Reference

`#include <[domctl.h](public_2domctl_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dev](#afd889f5732c896690b4dd13a763d4fb2) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a306ada0659d7ef8434773efd8cdb594e) |
| union { |  |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [machine\_sbdf](#a87fea9d75ecd8d4c161550fd5a28105a) |  |
| }   [pci](#a1d44b15c0e80e2a0082eccce83af549a) |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [size](#a10c7d5368170e054c54a8b1cc69c8515) |  |
| [path](#a2f714f8a4580fa956bb707b6f27fc26f) |  |
| }   [dt](#a508c528eacf758fed230d5b17fc9a801) |
| } | [u](#a76fde5e4eb3713c1db5dba8924e627a1) |

## Field Documentation

## [◆ ](#afd889f5732c896690b4dd13a763d4fb2)dev

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_assign\_device::dev |
| --- |

## [◆ ](#a508c528eacf758fed230d5b17fc9a801)[struct]

| struct { ... } xen\_domctl\_assign\_device::dt |
| --- |

## [◆ ](#a306ada0659d7ef8434773efd8cdb594e)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_assign\_device::flags |
| --- |

## [◆ ](#a87fea9d75ecd8d4c161550fd5a28105a)machine\_sbdf

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_assign\_device::machine\_sbdf |
| --- |

## [◆ ](#a2f714f8a4580fa956bb707b6f27fc26f)path

| xen\_domctl\_assign\_device::path |
| --- |

## [◆ ](#a1d44b15c0e80e2a0082eccce83af549a)[struct]

| struct { ... } xen\_domctl\_assign\_device::pci |
| --- |

## [◆ ](#a10c7d5368170e054c54a8b1cc69c8515)size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_assign\_device::size |
| --- |

## [◆ ](#a76fde5e4eb3713c1db5dba8924e627a1)[union]

| union { ... } xen\_domctl\_assign\_device::u |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[domctl.h](public_2domctl_8h_source.md)

- [xen\_domctl\_assign\_device](structxen__domctl__assign__device.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
