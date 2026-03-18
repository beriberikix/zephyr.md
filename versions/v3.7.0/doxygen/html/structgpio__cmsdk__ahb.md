---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structgpio__cmsdk__ahb.html
original_path: doxygen/html/structgpio__cmsdk__ahb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_cmsdk\_ahb Struct Reference

`#include <[gpio_cmsdk_ahb.h](gpio__cmsdk__ahb_8h_source.md)>`

| Data Fields | |
| --- | --- |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [data](#accd586d346c6588ae93fc409159fa368) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dataout](#af548def1b32a28d043b4bbfdddc29662) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [reserved0](#a995563a125b425a4633f4d25ccaff0cd) [2] |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [outenableset](#ac5de9ecb2427bdf0dfc78099253ce2de) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [outenableclr](#a20babd83013581d8273570c5b63658b4) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [altfuncset](#a5f70dc42911502ff96254f44ff385caa) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [altfuncclr](#a325a85d7d5fa3830ee9a7e922bed08ae) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [intenset](#a5c79dd58c92ee471c86cf420a02a3afb) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [intenclr](#a83a77418db66bd89bae093533a168617) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [inttypeset](#abf5caf8e369d4629aabe935f63bd8f7e) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [inttypeclr](#af54ff4e5327fa86546166df38f76d3df) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [intpolset](#af76e1a0e03e7a1373a4029f9865a1abb) |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [intpolclr](#addc9f323303ed2888a047a54ff2d2092) |
| union { |  |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [intstatus](#a5bc3851b26cb0340208f4b93ef475042) |  |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [intclear](#aa3a3638d45f9dddd4f122b8081ac46cf) |  |
| }; |  |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [reserved1](#ae8c9c5c849a45f86b84b21266eaca8af) [241] |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [lb\_masked](#a1cb9a3456c4e3c7a65c5132052f4605a) [256] |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ub\_masked](#aece662b5260db9a8b43fc61ebd7a288c) [256] |

## Field Documentation

## [◆ ](#ab1490ee6715fafdce3c67a2c5990b236)[union]

| union { ... } [gpio\_cmsdk\_ahb](structgpio__cmsdk__ahb.md) |
| --- |

## [◆ ](#a325a85d7d5fa3830ee9a7e922bed08ae)altfuncclr

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::altfuncclr |
| --- |

## [◆ ](#a5f70dc42911502ff96254f44ff385caa)altfuncset

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::altfuncset |
| --- |

## [◆ ](#accd586d346c6588ae93fc409159fa368)data

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::data |
| --- |

## [◆ ](#af548def1b32a28d043b4bbfdddc29662)dataout

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::dataout |
| --- |

## [◆ ](#aa3a3638d45f9dddd4f122b8081ac46cf)intclear

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::intclear |
| --- |

## [◆ ](#a83a77418db66bd89bae093533a168617)intenclr

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::intenclr |
| --- |

## [◆ ](#a5c79dd58c92ee471c86cf420a02a3afb)intenset

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::intenset |
| --- |

## [◆ ](#addc9f323303ed2888a047a54ff2d2092)intpolclr

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::intpolclr |
| --- |

## [◆ ](#af76e1a0e03e7a1373a4029f9865a1abb)intpolset

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::intpolset |
| --- |

## [◆ ](#a5bc3851b26cb0340208f4b93ef475042)intstatus

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::intstatus |
| --- |

## [◆ ](#af54ff4e5327fa86546166df38f76d3df)inttypeclr

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::inttypeclr |
| --- |

## [◆ ](#abf5caf8e369d4629aabe935f63bd8f7e)inttypeset

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::inttypeset |
| --- |

## [◆ ](#a1cb9a3456c4e3c7a65c5132052f4605a)lb\_masked

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::lb\_masked[256] |
| --- |

## [◆ ](#a20babd83013581d8273570c5b63658b4)outenableclr

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::outenableclr |
| --- |

## [◆ ](#ac5de9ecb2427bdf0dfc78099253ce2de)outenableset

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::outenableset |
| --- |

## [◆ ](#a995563a125b425a4633f4d25ccaff0cd)reserved0

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::reserved0[2] |
| --- |

## [◆ ](#ae8c9c5c849a45f86b84b21266eaca8af)reserved1

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::reserved1[241] |
| --- |

## [◆ ](#aece662b5260db9a8b43fc61ebd7a288c)ub\_masked

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpio\_cmsdk\_ahb::ub\_masked[256] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/gpio/[gpio\_cmsdk\_ahb.h](gpio__cmsdk__ahb_8h_source.md)

- [gpio\_cmsdk\_ahb](structgpio__cmsdk__ahb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
