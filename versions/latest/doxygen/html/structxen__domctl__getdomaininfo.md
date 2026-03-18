---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structxen__domctl__getdomaininfo.html
original_path: doxygen/html/structxen__domctl__getdomaininfo.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xen\_domctl\_getdomaininfo Struct Reference

`#include <[domctl.h](public_2domctl_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) | [domain](#a5e7d88b68cadb01f8c07d684a0ad3830) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pad1](#a3d95e5632a072051d23f1d55600412c6) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#ae65559d31f31c04f77c12a54341eaff7) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [tot\_pages](#a1a16010642a6d39c66a6c7f9198e4ed4) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [max\_pages](#a9bd68dbcd962f6f9e9cb8bd59b61098a) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [outstanding\_pages](#a0886d0cc1989df57ca01dd5b5182b864) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [shr\_pages](#a9b174ea0accd536124987c67ff0ebec6) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [paged\_pages](#a9dd6c1d2a3b79cb3f40f471e943a17fe) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [shared\_info\_frame](#a454dbc861570f637283e1c5e063f9f9f) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [cpu\_time](#aa9f8baa2443b101cbed57d2779f0b0d3) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nr\_online\_vcpus](#a31cfa87a2ef46d2f25b886b0bd05b4d4) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_vcpu\_id](#ad1357c297623c4244d14efbae6d4f0f0) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ssidref](#abb8a0270095249a351777b54f747786f) |
| [xen\_domain\_handle\_t](xen_8h.md#a7be3933d71db9ec81444793055b5d9be) | [handle](#aadfc1b75adac22b197228a2107e6e310) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cpupool](#a13c6ae340f7f8b9b79bb3b62ace156b8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [gpaddr\_bits](#a5c4df1039ec53351693fa880577e39a5) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pad2](#a6f304fc43fc449e21c6fc3591944c1c8) [7] |
| struct xen\_arch\_domainconfig | [arch\_config](#a5b8ed09273407167af2dc9b62da61cd3) |

## Field Documentation

## [◆ ](#a5b8ed09273407167af2dc9b62da61cd3)arch\_config

| struct xen\_arch\_domainconfig xen\_domctl\_getdomaininfo::arch\_config |
| --- |

## [◆ ](#aa9f8baa2443b101cbed57d2779f0b0d3)cpu\_time

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) xen\_domctl\_getdomaininfo::cpu\_time |
| --- |

## [◆ ](#a13c6ae340f7f8b9b79bb3b62ace156b8)cpupool

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_getdomaininfo::cpupool |
| --- |

## [◆ ](#a5e7d88b68cadb01f8c07d684a0ad3830)domain

| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) xen\_domctl\_getdomaininfo::domain |
| --- |

## [◆ ](#ae65559d31f31c04f77c12a54341eaff7)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_getdomaininfo::flags |
| --- |

## [◆ ](#a5c4df1039ec53351693fa880577e39a5)gpaddr\_bits

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xen\_domctl\_getdomaininfo::gpaddr\_bits |
| --- |

## [◆ ](#aadfc1b75adac22b197228a2107e6e310)handle

| [xen\_domain\_handle\_t](xen_8h.md#a7be3933d71db9ec81444793055b5d9be) xen\_domctl\_getdomaininfo::handle |
| --- |

## [◆ ](#a9bd68dbcd962f6f9e9cb8bd59b61098a)max\_pages

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) xen\_domctl\_getdomaininfo::max\_pages |
| --- |

## [◆ ](#ad1357c297623c4244d14efbae6d4f0f0)max\_vcpu\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_getdomaininfo::max\_vcpu\_id |
| --- |

## [◆ ](#a31cfa87a2ef46d2f25b886b0bd05b4d4)nr\_online\_vcpus

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_getdomaininfo::nr\_online\_vcpus |
| --- |

## [◆ ](#a0886d0cc1989df57ca01dd5b5182b864)outstanding\_pages

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) xen\_domctl\_getdomaininfo::outstanding\_pages |
| --- |

## [◆ ](#a3d95e5632a072051d23f1d55600412c6)pad1

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) xen\_domctl\_getdomaininfo::pad1 |
| --- |

## [◆ ](#a6f304fc43fc449e21c6fc3591944c1c8)pad2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xen\_domctl\_getdomaininfo::pad2[7] |
| --- |

## [◆ ](#a9dd6c1d2a3b79cb3f40f471e943a17fe)paged\_pages

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) xen\_domctl\_getdomaininfo::paged\_pages |
| --- |

## [◆ ](#a454dbc861570f637283e1c5e063f9f9f)shared\_info\_frame

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) xen\_domctl\_getdomaininfo::shared\_info\_frame |
| --- |

## [◆ ](#a9b174ea0accd536124987c67ff0ebec6)shr\_pages

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) xen\_domctl\_getdomaininfo::shr\_pages |
| --- |

## [◆ ](#abb8a0270095249a351777b54f747786f)ssidref

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xen\_domctl\_getdomaininfo::ssidref |
| --- |

## [◆ ](#a1a16010642a6d39c66a6c7f9198e4ed4)tot\_pages

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) xen\_domctl\_getdomaininfo::tot\_pages |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[domctl.h](public_2domctl_8h_source.md)

- [xen\_domctl\_getdomaininfo](structxen__domctl__getdomaininfo.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
