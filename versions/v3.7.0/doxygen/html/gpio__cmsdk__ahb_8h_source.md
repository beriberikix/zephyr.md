---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gpio__cmsdk__ahb_8h_source.html
original_path: doxygen/html/gpio__cmsdk__ahb_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_cmsdk\_ahb.h

[Go to the documentation of this file.](gpio__cmsdk__ahb_8h.md)

1/\*

2 \* Copyright (c) 2016 Linaro Limited.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_CMSDK\_AHB\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_CMSDK\_AHB\_H\_

8

9#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

15/\* ARM LTD CMSDK AHB General Purpose Input/Output (GPIO) \*/

[ 16](structgpio__cmsdk__ahb.md)struct [gpio\_cmsdk\_ahb](structgpio__cmsdk__ahb.md) {

17 /\* Offset: 0x000 (r/w) data register \*/

[ 18](structgpio__cmsdk__ahb.md#accd586d346c6588ae93fc409159fa368) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data](structgpio__cmsdk__ahb.md#accd586d346c6588ae93fc409159fa368);

19 /\* Offset: 0x004 (r/w) data output latch register \*/

[ 20](structgpio__cmsdk__ahb.md#af548def1b32a28d043b4bbfdddc29662) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dataout](structgpio__cmsdk__ahb.md#af548def1b32a28d043b4bbfdddc29662);

[ 21](structgpio__cmsdk__ahb.md#a995563a125b425a4633f4d25ccaff0cd) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved0](structgpio__cmsdk__ahb.md#a995563a125b425a4633f4d25ccaff0cd)[2];

22 /\* Offset: 0x010 (r/w) output enable set register \*/

[ 23](structgpio__cmsdk__ahb.md#ac5de9ecb2427bdf0dfc78099253ce2de) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [outenableset](structgpio__cmsdk__ahb.md#ac5de9ecb2427bdf0dfc78099253ce2de);

24 /\* Offset: 0x014 (r/w) output enable clear register \*/

[ 25](structgpio__cmsdk__ahb.md#a20babd83013581d8273570c5b63658b4) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [outenableclr](structgpio__cmsdk__ahb.md#a20babd83013581d8273570c5b63658b4);

26 /\* Offset: 0x018 (r/w) alternate function set register \*/

[ 27](structgpio__cmsdk__ahb.md#a5f70dc42911502ff96254f44ff385caa) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [altfuncset](structgpio__cmsdk__ahb.md#a5f70dc42911502ff96254f44ff385caa);

28 /\* Offset: 0x01c (r/w) alternate function clear register \*/

[ 29](structgpio__cmsdk__ahb.md#a325a85d7d5fa3830ee9a7e922bed08ae) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [altfuncclr](structgpio__cmsdk__ahb.md#a325a85d7d5fa3830ee9a7e922bed08ae);

30 /\* Offset: 0x020 (r/w) interrupt enable set register \*/

[ 31](structgpio__cmsdk__ahb.md#a5c79dd58c92ee471c86cf420a02a3afb) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [intenset](structgpio__cmsdk__ahb.md#a5c79dd58c92ee471c86cf420a02a3afb);

32 /\* Offset: 0x024 (r/w) interrupt enable clear register \*/

[ 33](structgpio__cmsdk__ahb.md#a83a77418db66bd89bae093533a168617) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [intenclr](structgpio__cmsdk__ahb.md#a83a77418db66bd89bae093533a168617);

34 /\* Offset: 0x028 (r/w) interrupt type set register \*/

[ 35](structgpio__cmsdk__ahb.md#abf5caf8e369d4629aabe935f63bd8f7e) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [inttypeset](structgpio__cmsdk__ahb.md#abf5caf8e369d4629aabe935f63bd8f7e);

36 /\* Offset: 0x02c (r/w) interrupt type clear register \*/

[ 37](structgpio__cmsdk__ahb.md#af54ff4e5327fa86546166df38f76d3df) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [inttypeclr](structgpio__cmsdk__ahb.md#af54ff4e5327fa86546166df38f76d3df);

38 /\* Offset: 0x030 (r/w) interrupt polarity set register \*/

[ 39](structgpio__cmsdk__ahb.md#af76e1a0e03e7a1373a4029f9865a1abb) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [intpolset](structgpio__cmsdk__ahb.md#af76e1a0e03e7a1373a4029f9865a1abb);

40 /\* Offset: 0x034 (r/w) interrupt polarity clear register \*/

[ 41](structgpio__cmsdk__ahb.md#addc9f323303ed2888a047a54ff2d2092) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [intpolclr](structgpio__cmsdk__ahb.md#addc9f323303ed2888a047a54ff2d2092);

42 union {

43 /\* Offset: 0x038 (r/ ) interrupt status register \*/

[ 44](structgpio__cmsdk__ahb.md#a5bc3851b26cb0340208f4b93ef475042) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [intstatus](structgpio__cmsdk__ahb.md#a5bc3851b26cb0340208f4b93ef475042);

45 /\* Offset: 0x038 ( /w) interrupt clear register \*/

[ 46](structgpio__cmsdk__ahb.md#aa3a3638d45f9dddd4f122b8081ac46cf) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [intclear](structgpio__cmsdk__ahb.md#aa3a3638d45f9dddd4f122b8081ac46cf);

47 };

[ 48](structgpio__cmsdk__ahb.md#ae8c9c5c849a45f86b84b21266eaca8af) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved1](structgpio__cmsdk__ahb.md#ae8c9c5c849a45f86b84b21266eaca8af)[241];

49 /\* Offset: 0x400 - 0x7fc lower byte masked access register (r/w) \*/

[ 50](structgpio__cmsdk__ahb.md#a1cb9a3456c4e3c7a65c5132052f4605a) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [lb\_masked](structgpio__cmsdk__ahb.md#a1cb9a3456c4e3c7a65c5132052f4605a)[256];

51 /\* Offset: 0x800 - 0xbfc upper byte masked access register (r/w) \*/

[ 52](structgpio__cmsdk__ahb.md#aece662b5260db9a8b43fc61ebd7a288c) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ub\_masked](structgpio__cmsdk__ahb.md#aece662b5260db9a8b43fc61ebd7a288c)[256];

53};

54

55#ifdef \_\_cplusplus

56}

57#endif

58

59#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_CMSDK\_AHB\_H\_ \*/

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[gpio\_cmsdk\_ahb](structgpio__cmsdk__ahb.md)

**Definition** gpio\_cmsdk\_ahb.h:16

[gpio\_cmsdk\_ahb::lb\_masked](structgpio__cmsdk__ahb.md#a1cb9a3456c4e3c7a65c5132052f4605a)

volatile uint32\_t lb\_masked[256]

**Definition** gpio\_cmsdk\_ahb.h:50

[gpio\_cmsdk\_ahb::outenableclr](structgpio__cmsdk__ahb.md#a20babd83013581d8273570c5b63658b4)

volatile uint32\_t outenableclr

**Definition** gpio\_cmsdk\_ahb.h:25

[gpio\_cmsdk\_ahb::altfuncclr](structgpio__cmsdk__ahb.md#a325a85d7d5fa3830ee9a7e922bed08ae)

volatile uint32\_t altfuncclr

**Definition** gpio\_cmsdk\_ahb.h:29

[gpio\_cmsdk\_ahb::intstatus](structgpio__cmsdk__ahb.md#a5bc3851b26cb0340208f4b93ef475042)

volatile uint32\_t intstatus

**Definition** gpio\_cmsdk\_ahb.h:44

[gpio\_cmsdk\_ahb::intenset](structgpio__cmsdk__ahb.md#a5c79dd58c92ee471c86cf420a02a3afb)

volatile uint32\_t intenset

**Definition** gpio\_cmsdk\_ahb.h:31

[gpio\_cmsdk\_ahb::altfuncset](structgpio__cmsdk__ahb.md#a5f70dc42911502ff96254f44ff385caa)

volatile uint32\_t altfuncset

**Definition** gpio\_cmsdk\_ahb.h:27

[gpio\_cmsdk\_ahb::intenclr](structgpio__cmsdk__ahb.md#a83a77418db66bd89bae093533a168617)

volatile uint32\_t intenclr

**Definition** gpio\_cmsdk\_ahb.h:33

[gpio\_cmsdk\_ahb::reserved0](structgpio__cmsdk__ahb.md#a995563a125b425a4633f4d25ccaff0cd)

volatile uint32\_t reserved0[2]

**Definition** gpio\_cmsdk\_ahb.h:21

[gpio\_cmsdk\_ahb::intclear](structgpio__cmsdk__ahb.md#aa3a3638d45f9dddd4f122b8081ac46cf)

volatile uint32\_t intclear

**Definition** gpio\_cmsdk\_ahb.h:46

[gpio\_cmsdk\_ahb::inttypeset](structgpio__cmsdk__ahb.md#abf5caf8e369d4629aabe935f63bd8f7e)

volatile uint32\_t inttypeset

**Definition** gpio\_cmsdk\_ahb.h:35

[gpio\_cmsdk\_ahb::outenableset](structgpio__cmsdk__ahb.md#ac5de9ecb2427bdf0dfc78099253ce2de)

volatile uint32\_t outenableset

**Definition** gpio\_cmsdk\_ahb.h:23

[gpio\_cmsdk\_ahb::data](structgpio__cmsdk__ahb.md#accd586d346c6588ae93fc409159fa368)

volatile uint32\_t data

**Definition** gpio\_cmsdk\_ahb.h:18

[gpio\_cmsdk\_ahb::intpolclr](structgpio__cmsdk__ahb.md#addc9f323303ed2888a047a54ff2d2092)

volatile uint32\_t intpolclr

**Definition** gpio\_cmsdk\_ahb.h:41

[gpio\_cmsdk\_ahb::reserved1](structgpio__cmsdk__ahb.md#ae8c9c5c849a45f86b84b21266eaca8af)

volatile uint32\_t reserved1[241]

**Definition** gpio\_cmsdk\_ahb.h:48

[gpio\_cmsdk\_ahb::ub\_masked](structgpio__cmsdk__ahb.md#aece662b5260db9a8b43fc61ebd7a288c)

volatile uint32\_t ub\_masked[256]

**Definition** gpio\_cmsdk\_ahb.h:52

[gpio\_cmsdk\_ahb::dataout](structgpio__cmsdk__ahb.md#af548def1b32a28d043b4bbfdddc29662)

volatile uint32\_t dataout

**Definition** gpio\_cmsdk\_ahb.h:20

[gpio\_cmsdk\_ahb::inttypeclr](structgpio__cmsdk__ahb.md#af54ff4e5327fa86546166df38f76d3df)

volatile uint32\_t inttypeclr

**Definition** gpio\_cmsdk\_ahb.h:37

[gpio\_cmsdk\_ahb::intpolset](structgpio__cmsdk__ahb.md#af76e1a0e03e7a1373a4029f9865a1abb)

volatile uint32\_t intpolset

**Definition** gpio\_cmsdk\_ahb.h:39

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_cmsdk\_ahb.h](gpio__cmsdk__ahb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
