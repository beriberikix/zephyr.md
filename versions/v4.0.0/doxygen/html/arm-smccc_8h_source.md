---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm-smccc_8h_source.html
original_path: doxygen/html/arm-smccc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm-smccc.h

[Go to the documentation of this file.](arm-smccc_8h.md)

1/\*

2 \* Copyright 2020 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_SMCCC\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_SMCCC\_H\_

9

10/\*

11 \* Result from SMC/HVC call

12 \* @a0-a7 result values from registers 0 to 7

13 \*/

[ 14](structarm__smccc__res.md)struct [arm\_smccc\_res](structarm__smccc__res.md) {

[ 15](structarm__smccc__res.md#a14b8a6dd41e29f6e6be2352e9fda32c3) unsigned long [a0](structarm__smccc__res.md#a14b8a6dd41e29f6e6be2352e9fda32c3);

[ 16](structarm__smccc__res.md#a03fc5b45240f7f297e98d05cd9c9f037) unsigned long [a1](structarm__smccc__res.md#a03fc5b45240f7f297e98d05cd9c9f037);

[ 17](structarm__smccc__res.md#aff43435dfa582911ff6c162f515cf339) unsigned long [a2](structarm__smccc__res.md#aff43435dfa582911ff6c162f515cf339);

[ 18](structarm__smccc__res.md#a1e1278f6e1474ff238c1b8ed783e56b9) unsigned long [a3](structarm__smccc__res.md#a1e1278f6e1474ff238c1b8ed783e56b9);

[ 19](structarm__smccc__res.md#a79ba61e5ed6cd00d04ce7fcb9f0c1267) unsigned long [a4](structarm__smccc__res.md#a79ba61e5ed6cd00d04ce7fcb9f0c1267);

[ 20](structarm__smccc__res.md#a85f198052bbbf49f156652f8747598e1) unsigned long [a5](structarm__smccc__res.md#a85f198052bbbf49f156652f8747598e1);

[ 21](structarm__smccc__res.md#a0da7f909d80d1b859072e05790c44426) unsigned long [a6](structarm__smccc__res.md#a0da7f909d80d1b859072e05790c44426);

[ 22](structarm__smccc__res.md#a0edc6f251808d35bf3747330d06bd155) unsigned long [a7](structarm__smccc__res.md#a0edc6f251808d35bf3747330d06bd155);

23};

24

[ 25](arm-smccc_8h.md#a2443c54e127b7804b733ba18d94378ba)typedef struct [arm\_smccc\_res](structarm__smccc__res.md) [arm\_smccc\_res\_t](arm-smccc_8h.md#a2443c54e127b7804b733ba18d94378ba);

26

[ 27](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80)enum [arm\_smccc\_conduit](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80) {

[ 28](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80aad2f223e1d078eda0d631cccfb1062ff) [SMCCC\_CONDUIT\_NONE](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80aad2f223e1d078eda0d631cccfb1062ff),

[ 29](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80ab60fe907e7211885992f784a270887fb) [SMCCC\_CONDUIT\_SMC](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80ab60fe907e7211885992f784a270887fb),

[ 30](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80a8acc5857666d57a8d15ab66d6857f58d) [SMCCC\_CONDUIT\_HVC](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80a8acc5857666d57a8d15ab66d6857f58d),

31};

32

33/\*

34 \* @brief Make HVC calls

35 \*

36 \* @param a0 function identifier

37 \* @param a1-a7 parameters registers

38 \* @param res results

39 \*/

[ 40](arm-smccc_8h.md#afa839fbf56047be56c9b2d632fdcdc4e)void [arm\_smccc\_hvc](arm-smccc_8h.md#afa839fbf56047be56c9b2d632fdcdc4e)(unsigned long [a0](structarm__smccc__res.md#a14b8a6dd41e29f6e6be2352e9fda32c3), unsigned long [a1](structarm__smccc__res.md#a03fc5b45240f7f297e98d05cd9c9f037),

41 unsigned long [a2](structarm__smccc__res.md#aff43435dfa582911ff6c162f515cf339), unsigned long [a3](structarm__smccc__res.md#a1e1278f6e1474ff238c1b8ed783e56b9),

42 unsigned long [a4](structarm__smccc__res.md#a79ba61e5ed6cd00d04ce7fcb9f0c1267), unsigned long [a5](structarm__smccc__res.md#a85f198052bbbf49f156652f8747598e1),

43 unsigned long [a6](structarm__smccc__res.md#a0da7f909d80d1b859072e05790c44426), unsigned long [a7](structarm__smccc__res.md#a0edc6f251808d35bf3747330d06bd155),

44 struct [arm\_smccc\_res](structarm__smccc__res.md) \*res);

45

46/\*

47 \* @brief Make SMC calls

48 \*

49 \* @param a0 function identifier

50 \* @param a1-a7 parameters registers

51 \* @param res results

52 \*/

[ 53](arm-smccc_8h.md#a5c5b69d74ff042a8714b42d9f82b2676)void [arm\_smccc\_smc](arm-smccc_8h.md#a5c5b69d74ff042a8714b42d9f82b2676)(unsigned long [a0](structarm__smccc__res.md#a14b8a6dd41e29f6e6be2352e9fda32c3), unsigned long [a1](structarm__smccc__res.md#a03fc5b45240f7f297e98d05cd9c9f037),

54 unsigned long [a2](structarm__smccc__res.md#aff43435dfa582911ff6c162f515cf339), unsigned long [a3](structarm__smccc__res.md#a1e1278f6e1474ff238c1b8ed783e56b9),

55 unsigned long [a4](structarm__smccc__res.md#a79ba61e5ed6cd00d04ce7fcb9f0c1267), unsigned long [a5](structarm__smccc__res.md#a85f198052bbbf49f156652f8747598e1),

56 unsigned long [a6](structarm__smccc__res.md#a0da7f909d80d1b859072e05790c44426), unsigned long [a7](structarm__smccc__res.md#a0edc6f251808d35bf3747330d06bd155),

57 struct [arm\_smccc\_res](structarm__smccc__res.md) \*res);

58

59#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_SMCCC\_H\_ \*/

[arm\_smccc\_res\_t](arm-smccc_8h.md#a2443c54e127b7804b733ba18d94378ba)

struct arm\_smccc\_res arm\_smccc\_res\_t

**Definition** arm-smccc.h:25

[arm\_smccc\_conduit](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80)

arm\_smccc\_conduit

**Definition** arm-smccc.h:27

[SMCCC\_CONDUIT\_HVC](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80a8acc5857666d57a8d15ab66d6857f58d)

@ SMCCC\_CONDUIT\_HVC

**Definition** arm-smccc.h:30

[SMCCC\_CONDUIT\_NONE](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80aad2f223e1d078eda0d631cccfb1062ff)

@ SMCCC\_CONDUIT\_NONE

**Definition** arm-smccc.h:28

[SMCCC\_CONDUIT\_SMC](arm-smccc_8h.md#a3c5dbd5d749131b224b0c9f4ec75fd80ab60fe907e7211885992f784a270887fb)

@ SMCCC\_CONDUIT\_SMC

**Definition** arm-smccc.h:29

[arm\_smccc\_smc](arm-smccc_8h.md#a5c5b69d74ff042a8714b42d9f82b2676)

void arm\_smccc\_smc(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, struct arm\_smccc\_res \*res)

[arm\_smccc\_hvc](arm-smccc_8h.md#afa839fbf56047be56c9b2d632fdcdc4e)

void arm\_smccc\_hvc(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4, unsigned long a5, unsigned long a6, unsigned long a7, struct arm\_smccc\_res \*res)

[arm\_smccc\_res](structarm__smccc__res.md)

**Definition** arm-smccc.h:14

[arm\_smccc\_res::a1](structarm__smccc__res.md#a03fc5b45240f7f297e98d05cd9c9f037)

unsigned long a1

**Definition** arm-smccc.h:16

[arm\_smccc\_res::a6](structarm__smccc__res.md#a0da7f909d80d1b859072e05790c44426)

unsigned long a6

**Definition** arm-smccc.h:21

[arm\_smccc\_res::a7](structarm__smccc__res.md#a0edc6f251808d35bf3747330d06bd155)

unsigned long a7

**Definition** arm-smccc.h:22

[arm\_smccc\_res::a0](structarm__smccc__res.md#a14b8a6dd41e29f6e6be2352e9fda32c3)

unsigned long a0

**Definition** arm-smccc.h:15

[arm\_smccc\_res::a3](structarm__smccc__res.md#a1e1278f6e1474ff238c1b8ed783e56b9)

unsigned long a3

**Definition** arm-smccc.h:18

[arm\_smccc\_res::a4](structarm__smccc__res.md#a79ba61e5ed6cd00d04ce7fcb9f0c1267)

unsigned long a4

**Definition** arm-smccc.h:19

[arm\_smccc\_res::a5](structarm__smccc__res.md#a85f198052bbbf49f156652f8747598e1)

unsigned long a5

**Definition** arm-smccc.h:20

[arm\_smccc\_res::a2](structarm__smccc__res.md#aff43435dfa582911ff6c162f515cf339)

unsigned long a2

**Definition** arm-smccc.h:17

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [arm-smccc.h](arm-smccc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
