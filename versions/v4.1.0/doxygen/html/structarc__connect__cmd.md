---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structarc__connect__cmd.html
original_path: doxygen/html/structarc__connect__cmd.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_connect\_cmd Struct Reference

`#include <[arc_connect.h](arc__connect_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [cmd](#a83c7cc807f7e5f8593574715cc60fb4d):8 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [param](#a6c03654eda9c5074ea9012cfa8bb18a3):16 |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [pad](#afc0086f899ec7e4ea7ae5ea33a6971cf):8 |  |
| } |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [val](#afb90551e0d8ad5acb910559dabff1471) |  |
| }; |  |

## Field Documentation

## [◆ ](#a4db3c4fced89c13ac6219e3614fefe2e)[union]

| union { ... } [arc\_connect\_cmd](structarc__connect__cmd.md) |
| --- |

## [◆ ](#a83c7cc807f7e5f8593574715cc60fb4d)cmd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arc\_connect\_cmd::cmd |
| --- |

## [◆ ](#afc0086f899ec7e4ea7ae5ea33a6971cf)pad

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arc\_connect\_cmd::pad |
| --- |

## [◆ ](#a6c03654eda9c5074ea9012cfa8bb18a3)param

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arc\_connect\_cmd::param |
| --- |

## [◆ ](#afb90551e0d8ad5acb910559dabff1471)val

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arc\_connect\_cmd::val |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/arch/arc/v2/[arc\_connect.h](arc__connect_8h_source.md)

- [arc\_connect\_cmd](structarc__connect__cmd.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
