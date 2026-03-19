---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structxen__domctl__createdomain.html
original_path: doxygen/html/structxen__domctl__createdomain.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xen\_domctl\_createdomain Struct Reference

`#include <[domctl.h](public_2domctl_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ssidref](#a06ffb30e51c2784838fd952407ebb8f9) |
| [xen\_domain\_handle\_t](xen_8h.md#a7be3933d71db9ec81444793055b5d9be) | [handle](#adaf41563368b9860936fb65a2877c9da) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a95075979e76ce83d0f6ed6db93441fc9) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [iommu\_opts](#a1b2e3e39c70e95ea46faf8ec10b2fb7c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_vcpus](#acd79a2c45cdf4d7ff413b385d9709681) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_evtchn\_port](#a2ce51b652bac61a08190a101a3743b68) |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [max\_grant\_frames](#aba5536e3e28cd164779ac6bced9f6eba) |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [max\_maptrack\_frames](#acde0ef87527498de29d38e885bfb822d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [grant\_opts](#a6fa7844107a90f97afead3f17ce91c49) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vmtrace\_size](#a6b9bd817c7df997e5f6585868da7d4bd) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cpupool\_id](#ac2ef8f072975509418de8ef126f2a65a) |
| struct xen\_arch\_domainconfig | [arch](#a63186466661618e0f70ac2f2d37f8953) |

## Field Documentation

## [◆ ](#a63186466661618e0f70ac2f2d37f8953)arch

| struct xen\_arch\_domainconfig xen\_domctl\_createdomain::arch |
| --- |

## [◆ ](#ac2ef8f072975509418de8ef126f2a65a)cpupool\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_createdomain::cpupool\_id |
| --- |

## [◆ ](#a95075979e76ce83d0f6ed6db93441fc9)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_createdomain::flags |
| --- |

## [◆ ](#a6fa7844107a90f97afead3f17ce91c49)grant\_opts

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_createdomain::grant\_opts |
| --- |

## [◆ ](#adaf41563368b9860936fb65a2877c9da)handle

| [xen\_domain\_handle\_t](xen_8h.md#a7be3933d71db9ec81444793055b5d9be) xen\_domctl\_createdomain::handle |
| --- |

## [◆ ](#a1b2e3e39c70e95ea46faf8ec10b2fb7c)iommu\_opts

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_createdomain::iommu\_opts |
| --- |

## [◆ ](#a2ce51b652bac61a08190a101a3743b68)max\_evtchn\_port

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_createdomain::max\_evtchn\_port |
| --- |

## [◆ ](#aba5536e3e28cd164779ac6bced9f6eba)max\_grant\_frames

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) xen\_domctl\_createdomain::max\_grant\_frames |
| --- |

## [◆ ](#acde0ef87527498de29d38e885bfb822d)max\_maptrack\_frames

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) xen\_domctl\_createdomain::max\_maptrack\_frames |
| --- |

## [◆ ](#acd79a2c45cdf4d7ff413b385d9709681)max\_vcpus

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_createdomain::max\_vcpus |
| --- |

## [◆ ](#a06ffb30e51c2784838fd952407ebb8f9)ssidref

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_createdomain::ssidref |
| --- |

## [◆ ](#a6b9bd817c7df997e5f6585868da7d4bd)vmtrace\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_createdomain::vmtrace\_size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[domctl.h](public_2domctl_8h_source.md)

- [xen\_domctl\_createdomain](structxen__domctl__createdomain.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
