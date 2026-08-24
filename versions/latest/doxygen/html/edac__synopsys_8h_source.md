---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/edac__synopsys_8h_source.html
original_path: doxygen/html/edac__synopsys_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

edac\_synopsys.h

[Go to the documentation of this file.](edac__synopsys_8h.md)

1/\*

2 \* Copyright (c) 2025 Calian Ltd

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_EDAC\_SYNOPSYS\_H\_

8#define ZEPHYR\_DRIVERS\_EDAC\_SYNOPSYS\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12/\* Callback data provided to function passed to notify\_cb\_set \*/

[ 13](structedac__synopsys__callback__data.md)struct [edac\_synopsys\_callback\_data](structedac__synopsys__callback__data.md) {

14 /\* Number of corrected errors since last callback \*/

[ 15](structedac__synopsys__callback__data.md#a71c5e4b31f16927b483e7bd3bf8b6f32) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [corr\_err\_count](structedac__synopsys__callback__data.md#a71c5e4b31f16927b483e7bd3bf8b6f32);

16 /\* Rank number of last corrected ECC error \*/

[ 17](structedac__synopsys__callback__data.md#aece294a29dbd98a3e75f4cfb6c9c79c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [corr\_err\_rank](structedac__synopsys__callback__data.md#aece294a29dbd98a3e75f4cfb6c9c79c3);

18 /\* Bank group number of last corrected ECC error \*/

[ 19](structedac__synopsys__callback__data.md#ae6a6c090671e5bfda93b904ee9e95a2b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [corr\_err\_bg](structedac__synopsys__callback__data.md#ae6a6c090671e5bfda93b904ee9e95a2b);

20 /\* Bank number of last corrected ECC error \*/

[ 21](structedac__synopsys__callback__data.md#a749fb5929f89a63cb62fd76f4c143dba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [corr\_err\_bank](structedac__synopsys__callback__data.md#a749fb5929f89a63cb62fd76f4c143dba);

22 /\* Row number of last corrected ECC error \*/

[ 23](structedac__synopsys__callback__data.md#aa549050b7305f4e8bb15f5b849bec165) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [corr\_err\_row](structedac__synopsys__callback__data.md#aa549050b7305f4e8bb15f5b849bec165);

24 /\* Column number of last corrected ECC error \*/

[ 25](structedac__synopsys__callback__data.md#af23d5d538b8ebe722838a186c6b30909) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [corr\_err\_col](structedac__synopsys__callback__data.md#af23d5d538b8ebe722838a186c6b30909);

26 /\* Syndrome (data pattern) of last corrected ECC error \*/

[ 27](structedac__synopsys__callback__data.md#aca79f779ac263e5344dad5e12ee6d3da) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [corr\_err\_syndrome](structedac__synopsys__callback__data.md#aca79f779ac263e5344dad5e12ee6d3da);

28 /\* Syndrome ECC bits for last corrected ECC error \*/

[ 29](structedac__synopsys__callback__data.md#a73567e401a706bbf392db489afd72012) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [corr\_err\_syndrome\_ecc](structedac__synopsys__callback__data.md#a73567e401a706bbf392db489afd72012);

30 /\* Bitmask of corrected error bits in data word \*/

[ 31](structedac__synopsys__callback__data.md#a10387f0ff6db7c6a116a8ccb2ba3e7c0) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [corr\_err\_bitmask](structedac__synopsys__callback__data.md#a10387f0ff6db7c6a116a8ccb2ba3e7c0);

32 /\* Bitmask of corrected error bits in ECC word \*/

[ 33](structedac__synopsys__callback__data.md#a659a7a12f24337cc57ea121e06cbd20c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [corr\_err\_bitmask\_ecc](structedac__synopsys__callback__data.md#a659a7a12f24337cc57ea121e06cbd20c);

34

35 /\* Number of uncorrected errors since last callback \*/

[ 36](structedac__synopsys__callback__data.md#aa34f78372e80c57772ea864827a5abe1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [uncorr\_err\_count](structedac__synopsys__callback__data.md#aa34f78372e80c57772ea864827a5abe1);

37 /\* Rank number of last uncorrected ECC error \*/

[ 38](structedac__synopsys__callback__data.md#a07c6bd60a094e5b807df0bf823959a3e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uncorr\_err\_rank](structedac__synopsys__callback__data.md#a07c6bd60a094e5b807df0bf823959a3e);

39 /\* Bank group number of last uncorrected ECC error \*/

[ 40](structedac__synopsys__callback__data.md#af148757e829b0e0bfbf575521131f54b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uncorr\_err\_bg](structedac__synopsys__callback__data.md#af148757e829b0e0bfbf575521131f54b);

41 /\* Bank number of last uncorrected ECC error \*/

[ 42](structedac__synopsys__callback__data.md#a8df3545fd3f7dfa8a99dcac90e708ec2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uncorr\_err\_bank](structedac__synopsys__callback__data.md#a8df3545fd3f7dfa8a99dcac90e708ec2);

43 /\* Row number of last uncorrected ECC error \*/

[ 44](structedac__synopsys__callback__data.md#a99670584c0c09eaf2e14e6e797ec834d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [uncorr\_err\_row](structedac__synopsys__callback__data.md#a99670584c0c09eaf2e14e6e797ec834d);

45 /\* Column number of last uncorrected ECC error \*/

[ 46](structedac__synopsys__callback__data.md#a17fee6074688540133b07fb0d567857a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uncorr\_err\_col](structedac__synopsys__callback__data.md#a17fee6074688540133b07fb0d567857a);

47 /\* Syndrome (data pattern) of last uncorrected ECC error \*/

[ 48](structedac__synopsys__callback__data.md#a3c05b263247c78ac195760f6a73a30b8) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [uncorr\_err\_syndrome](structedac__synopsys__callback__data.md#a3c05b263247c78ac195760f6a73a30b8);

49 /\* Syndrome ECC bits of last uncorrected ECC error \*/

[ 50](structedac__synopsys__callback__data.md#a36d022f0de8a63581a4a2a95d923e041) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uncorr\_err\_syndrome\_ecc](structedac__synopsys__callback__data.md#a36d022f0de8a63581a4a2a95d923e041);

51};

52

53#endif /\* ZEPHYR\_DRIVERS\_EDAC\_SYNOPSYS\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[edac\_synopsys\_callback\_data](structedac__synopsys__callback__data.md)

**Definition** edac\_synopsys.h:13

[edac\_synopsys\_callback\_data::uncorr\_err\_rank](structedac__synopsys__callback__data.md#a07c6bd60a094e5b807df0bf823959a3e)

uint8\_t uncorr\_err\_rank

**Definition** edac\_synopsys.h:38

[edac\_synopsys\_callback\_data::corr\_err\_bitmask](structedac__synopsys__callback__data.md#a10387f0ff6db7c6a116a8ccb2ba3e7c0)

uint64\_t corr\_err\_bitmask

**Definition** edac\_synopsys.h:31

[edac\_synopsys\_callback\_data::uncorr\_err\_col](structedac__synopsys__callback__data.md#a17fee6074688540133b07fb0d567857a)

uint8\_t uncorr\_err\_col

**Definition** edac\_synopsys.h:46

[edac\_synopsys\_callback\_data::uncorr\_err\_syndrome\_ecc](structedac__synopsys__callback__data.md#a36d022f0de8a63581a4a2a95d923e041)

uint8\_t uncorr\_err\_syndrome\_ecc

**Definition** edac\_synopsys.h:50

[edac\_synopsys\_callback\_data::uncorr\_err\_syndrome](structedac__synopsys__callback__data.md#a3c05b263247c78ac195760f6a73a30b8)

uint64\_t uncorr\_err\_syndrome

**Definition** edac\_synopsys.h:48

[edac\_synopsys\_callback\_data::corr\_err\_bitmask\_ecc](structedac__synopsys__callback__data.md#a659a7a12f24337cc57ea121e06cbd20c)

uint8\_t corr\_err\_bitmask\_ecc

**Definition** edac\_synopsys.h:33

[edac\_synopsys\_callback\_data::corr\_err\_count](structedac__synopsys__callback__data.md#a71c5e4b31f16927b483e7bd3bf8b6f32)

uint16\_t corr\_err\_count

**Definition** edac\_synopsys.h:15

[edac\_synopsys\_callback\_data::corr\_err\_syndrome\_ecc](structedac__synopsys__callback__data.md#a73567e401a706bbf392db489afd72012)

uint8\_t corr\_err\_syndrome\_ecc

**Definition** edac\_synopsys.h:29

[edac\_synopsys\_callback\_data::corr\_err\_bank](structedac__synopsys__callback__data.md#a749fb5929f89a63cb62fd76f4c143dba)

uint8\_t corr\_err\_bank

**Definition** edac\_synopsys.h:21

[edac\_synopsys\_callback\_data::uncorr\_err\_bank](structedac__synopsys__callback__data.md#a8df3545fd3f7dfa8a99dcac90e708ec2)

uint8\_t uncorr\_err\_bank

**Definition** edac\_synopsys.h:42

[edac\_synopsys\_callback\_data::uncorr\_err\_row](structedac__synopsys__callback__data.md#a99670584c0c09eaf2e14e6e797ec834d)

uint32\_t uncorr\_err\_row

**Definition** edac\_synopsys.h:44

[edac\_synopsys\_callback\_data::uncorr\_err\_count](structedac__synopsys__callback__data.md#aa34f78372e80c57772ea864827a5abe1)

uint16\_t uncorr\_err\_count

**Definition** edac\_synopsys.h:36

[edac\_synopsys\_callback\_data::corr\_err\_row](structedac__synopsys__callback__data.md#aa549050b7305f4e8bb15f5b849bec165)

uint32\_t corr\_err\_row

**Definition** edac\_synopsys.h:23

[edac\_synopsys\_callback\_data::corr\_err\_syndrome](structedac__synopsys__callback__data.md#aca79f779ac263e5344dad5e12ee6d3da)

uint64\_t corr\_err\_syndrome

**Definition** edac\_synopsys.h:27

[edac\_synopsys\_callback\_data::corr\_err\_bg](structedac__synopsys__callback__data.md#ae6a6c090671e5bfda93b904ee9e95a2b)

uint8\_t corr\_err\_bg

**Definition** edac\_synopsys.h:19

[edac\_synopsys\_callback\_data::corr\_err\_rank](structedac__synopsys__callback__data.md#aece294a29dbd98a3e75f4cfb6c9c79c3)

uint8\_t corr\_err\_rank

**Definition** edac\_synopsys.h:17

[edac\_synopsys\_callback\_data::uncorr\_err\_bg](structedac__synopsys__callback__data.md#af148757e829b0e0bfbf575521131f54b)

uint8\_t uncorr\_err\_bg

**Definition** edac\_synopsys.h:40

[edac\_synopsys\_callback\_data::corr\_err\_col](structedac__synopsys__callback__data.md#af23d5d538b8ebe722838a186c6b30909)

uint8\_t corr\_err\_col

**Definition** edac\_synopsys.h:25

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [edac](dir_9a9baa0c528b094da145ee06d903a887.md)
- [edac\_synopsys.h](edac__synopsys_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
