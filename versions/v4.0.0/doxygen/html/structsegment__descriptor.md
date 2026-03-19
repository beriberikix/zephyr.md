---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsegment__descriptor.html
original_path: doxygen/html/structsegment__descriptor.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

segment\_descriptor Struct Reference

`#include <[segmentation.h](segmentation_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [limit\_low](#aaec62c0ab8bb3ce1c01887ec2bc3579c) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [reserved\_task\_gate\_0](#acb81ff32dbec3821c9ba1cb423c5bb4d) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [offset\_low](#aacf357093163d9cb7c29de2cd4d74af1) |  |
| }; |  |
| union { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [segment\_selector](#ada9905938c5214787bb9a235658582dd) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [base\_low](#a22d9a7e9718d670507a0555b131079aa) |  |
| }; |  |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [base\_mid](#a9bc044fe835300da74561089217ae3b2) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [reserved\_task\_gate\_1](#a28e1c069a7afe06119ff057ecf388bd2) |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [reserved\_or\_param](#a6edf9d47468d11d8bbc2c3525217b42d):5 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [always\_0\_0](#a17006cb3ba7efd21a951e882e34b088d):3 |  |
| } |  |
| }; |  |
| union { |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [accessed](#aaa5b961b21b18d1efd9987dbfc42ad95):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [rw](#a598e508bbfbb9ed317bf6b91fd80b0e9):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [cd](#a25407a6f10ee04a42832238639e4d4ac):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [executable](#a45ebb67e9b54d4780ec42861e13531fd):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [descriptor\_type](#a95674f043c616032bf416facd6ac0469):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [dpl](#af9c72e8bd49845bf9c9bc16c2b788adf):2 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [present](#a61eda78022c10db647ce9e76a62a27a6):1 |  |
| } |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [type](#a88f41f8cda2177a6d70b9cf7c315053c):4 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [use\_other\_union](#ac9f594b7ca9e04d5a7cf8a246c73c7d5):4 |  |
| } |  |
| }; |  |
| union { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [offset\_hi](#a86d61b5de39020e207f567a5909aeaba) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [reserved\_task\_gate\_2](#a1a8678d1406de90c691a243a4562997d) |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [limit\_hi](#ad233fd87d891ca5f44b7e414c8766b05):4 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [avl](#a59e97c4fc79505fd8095d02edc01480f):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [flags\_l](#aa62f29b11de78f55aa7a829d69a07939):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [db](#a3b59b1ec549510eae9c3c2772d782e1a):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [granularity](#aebd148eac6d6e78c0a028531a76d22a8):1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [base\_hi](#a37dcfdc6eea1021d6be4f18aa26d4030) |  |
| } |  |
| }; |  |

## Field Documentation

## [◆ ](#afcc975c7e9696298dae576f8496f860c)[union]

| union { ... } [segment\_descriptor](structsegment__descriptor.md) |
| --- |

## [◆ ](#a5bc4c944d30bd45781e24232c258632e)[union]

| union { ... } [segment\_descriptor](structsegment__descriptor.md) |
| --- |

## [◆ ](#a9b1be2ff9b59bf79863f2c8aaab3fe23)[union]

| union { ... } [segment\_descriptor](structsegment__descriptor.md) |
| --- |

## [◆ ](#a5e53845ff2da5c66e8499f2d3d8617f2)[union]

| union { ... } [segment\_descriptor](structsegment__descriptor.md) |
| --- |

## [◆ ](#a0f0aa8180be0002f57b799cfa579b2d4)[union]

| union { ... } [segment\_descriptor](structsegment__descriptor.md) |
| --- |

## [◆ ](#aaa5b961b21b18d1efd9987dbfc42ad95)accessed

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::accessed |
| --- |

## [◆ ](#a17006cb3ba7efd21a951e882e34b088d)always\_0\_0

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::always\_0\_0 |
| --- |

## [◆ ](#a59e97c4fc79505fd8095d02edc01480f)avl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::avl |
| --- |

## [◆ ](#a37dcfdc6eea1021d6be4f18aa26d4030)base\_hi

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::base\_hi |
| --- |

## [◆ ](#a22d9a7e9718d670507a0555b131079aa)base\_low

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) segment\_descriptor::base\_low |
| --- |

## [◆ ](#a9bc044fe835300da74561089217ae3b2)base\_mid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::base\_mid |
| --- |

## [◆ ](#a25407a6f10ee04a42832238639e4d4ac)cd

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::cd |
| --- |

## [◆ ](#a3b59b1ec549510eae9c3c2772d782e1a)db

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::db |
| --- |

## [◆ ](#a95674f043c616032bf416facd6ac0469)descriptor\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::descriptor\_type |
| --- |

## [◆ ](#af9c72e8bd49845bf9c9bc16c2b788adf)dpl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::dpl |
| --- |

## [◆ ](#a45ebb67e9b54d4780ec42861e13531fd)executable

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::executable |
| --- |

## [◆ ](#aa62f29b11de78f55aa7a829d69a07939)flags\_l

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::flags\_l |
| --- |

## [◆ ](#aebd148eac6d6e78c0a028531a76d22a8)granularity

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::granularity |
| --- |

## [◆ ](#ad233fd87d891ca5f44b7e414c8766b05)limit\_hi

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::limit\_hi |
| --- |

## [◆ ](#aaec62c0ab8bb3ce1c01887ec2bc3579c)limit\_low

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) segment\_descriptor::limit\_low |
| --- |

## [◆ ](#a86d61b5de39020e207f567a5909aeaba)offset\_hi

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) segment\_descriptor::offset\_hi |
| --- |

## [◆ ](#aacf357093163d9cb7c29de2cd4d74af1)offset\_low

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) segment\_descriptor::offset\_low |
| --- |

## [◆ ](#a61eda78022c10db647ce9e76a62a27a6)present

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::present |
| --- |

## [◆ ](#a6edf9d47468d11d8bbc2c3525217b42d)reserved\_or\_param

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::reserved\_or\_param |
| --- |

## [◆ ](#acb81ff32dbec3821c9ba1cb423c5bb4d)reserved\_task\_gate\_0

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) segment\_descriptor::reserved\_task\_gate\_0 |
| --- |

## [◆ ](#a28e1c069a7afe06119ff057ecf388bd2)reserved\_task\_gate\_1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::reserved\_task\_gate\_1 |
| --- |

## [◆ ](#a1a8678d1406de90c691a243a4562997d)reserved\_task\_gate\_2

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) segment\_descriptor::reserved\_task\_gate\_2 |
| --- |

## [◆ ](#a598e508bbfbb9ed317bf6b91fd80b0e9)rw

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::rw |
| --- |

## [◆ ](#ada9905938c5214787bb9a235658582dd)segment\_selector

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) segment\_descriptor::segment\_selector |
| --- |

## [◆ ](#a88f41f8cda2177a6d70b9cf7c315053c)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::type |
| --- |

## [◆ ](#ac9f594b7ca9e04d5a7cf8a246c73c7d5)use\_other\_union

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) segment\_descriptor::use\_other\_union |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/arch/x86/ia32/[segmentation.h](segmentation_8h_source.md)

- [segment\_descriptor](structsegment__descriptor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
