---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/zms__priv_8h_source.html
original_path: doxygen/html/zms__priv_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zms\_priv.h

[Go to the documentation of this file.](zms__priv_8h.md)

1/\* Copyright (c) 2018 Laczen

2 \* Copyright (c) 2024 BayLibre SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*

6 \* ZMS: Zephyr Memory Storage

7 \*/

8

9#ifndef \_\_ZMS\_PRIV\_H\_

10#define \_\_ZMS\_PRIV\_H\_

11

12/\*

13 \* MASKS AND SHIFT FOR ADDRESSES.

14 \* An address in zms is an uint64\_t where:

15 \* - high 4 bytes represent the sector number

16 \* - low 4 bytes represent the offset in a sector

17 \*/

[ 18](zms__priv_8h.md#a9d825de36817ea93e474a0fe0f171cd3)#define ADDR\_SECT\_MASK GENMASK64(63, 32)

[ 19](zms__priv_8h.md#a4d57ef5332dd6732dc8a774366b8c48b)#define ADDR\_SECT\_SHIFT 32

[ 20](zms__priv_8h.md#aa7e50d2939fa8059c2efd455198225fa)#define ADDR\_OFFS\_MASK GENMASK64(31, 0)

[ 21](zms__priv_8h.md#a3b4d0b06717099e5f821cd51ce759b7d)#define SECTOR\_NUM(x) FIELD\_GET(ADDR\_SECT\_MASK, x)

[ 22](zms__priv_8h.md#ae26b2c8df9b12d757a57414b38e1cac4)#define SECTOR\_OFFSET(x) FIELD\_GET(ADDR\_OFFS\_MASK, x)

23

24#if defined(CONFIG\_ZMS\_CUSTOMIZE\_BLOCK\_SIZE)

25#define ZMS\_BLOCK\_SIZE CONFIG\_ZMS\_CUSTOM\_BLOCK\_SIZE

26#else

[ 27](zms__priv_8h.md#a9b40fc34a50b2f4ac97fc64fce014f4c)#define ZMS\_BLOCK\_SIZE 32

28#endif

29

[ 30](zms__priv_8h.md#a2cc4fbfc9a8017246e5b474f5c8c6b42)#define ZMS\_LOOKUP\_CACHE\_NO\_ADDR GENMASK64(63, 0)

[ 31](zms__priv_8h.md#a488f392646447c7532b9f84b57c331b4)#define ZMS\_HEAD\_ID GENMASK(31, 0)

32

[ 33](zms__priv_8h.md#a4193db24b2497ae547992eedaa43f6b3)#define ZMS\_VERSION\_MASK GENMASK(7, 0)

[ 34](zms__priv_8h.md#a7813e55b6ff100cbce70d63cb0a7bd1d)#define ZMS\_GET\_VERSION(x) FIELD\_GET(ZMS\_VERSION\_MASK, x)

[ 35](zms__priv_8h.md#a441f6525635866111d9e859cdcc4ebef)#define ZMS\_DEFAULT\_VERSION 1

[ 36](zms__priv_8h.md#a7b8a825d1d02681d675436d0950c63a2)#define ZMS\_MAGIC\_NUMBER 0x42 /\* murmur3a hash of "ZMS" (MSB) \*/

[ 37](zms__priv_8h.md#ae002208bc578d4e4d5a26b04fc4740a6)#define ZMS\_MAGIC\_NUMBER\_MASK GENMASK(15, 8)

[ 38](zms__priv_8h.md#ab9d90629ce189b666ab05ca30f47a38d)#define ZMS\_GET\_MAGIC\_NUMBER(x) FIELD\_GET(ZMS\_MAGIC\_NUMBER\_MASK, x)

[ 39](zms__priv_8h.md#a9331265598a521b8f4abb28b5cea90f6)#define ZMS\_MIN\_ATE\_NUM 5

40

[ 41](zms__priv_8h.md#a8ce9ad0d1e436bea764bad608ec75e69)#define ZMS\_INVALID\_SECTOR\_NUM -1

[ 42](zms__priv_8h.md#a758c42a254d0e64596c35c7ac644aedc)#define ZMS\_DATA\_IN\_ATE\_SIZE 8

43

[ 48](structzms__ate.md)struct [zms\_ate](structzms__ate.md) {

[ 50](structzms__ate.md#ac96dfde8f44e1af031c11490a0add94a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc8](structzms__ate.md#ac96dfde8f44e1af031c11490a0add94a);

[ 52](structzms__ate.md#a9d5e9e8ac241b613fd2db14cc85d0323) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cycle\_cnt](structzms__ate.md#a9d5e9e8ac241b613fd2db14cc85d0323);

[ 54](structzms__ate.md#aa71a3cb51572eaaa348c3644f332fc7e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structzms__ate.md#aa71a3cb51572eaaa348c3644f332fc7e);

[ 56](structzms__ate.md#ae624bc7570e77b75fcdc0fa1d74224c8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structzms__ate.md#ae624bc7570e77b75fcdc0fa1d74224c8);

57 union {

[ 59](structzms__ate.md#a54e3d4ebd6e5eda65e56033e6e2d379b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structzms__ate.md#a54e3d4ebd6e5eda65e56033e6e2d379b)[8];

60 struct {

[ 62](structzms__ate.md#a7d623901562467778185ef61b3f9bb0f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [offset](structzms__ate.md#a7d623901562467778185ef61b3f9bb0f);

63 union {

[ 70](structzms__ate.md#a8b70dd09e10545dae52bba3eb5f167e8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data\_crc](structzms__ate.md#a8b70dd09e10545dae52bba3eb5f167e8);

[ 74](structzms__ate.md#a26388b50787341e09efb85c5c115645d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [metadata](structzms__ate.md#a26388b50787341e09efb85c5c115645d);

75 };

76 };

77 };

78} \_\_packed;

79

80#endif /\* \_\_ZMS\_PRIV\_H\_ \*/

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[zms\_ate](structzms__ate.md)

ZMS Allocation Table Entry (ATE) structure.

**Definition** zms\_priv.h:48

[zms\_ate::metadata](structzms__ate.md#a26388b50787341e09efb85c5c115645d)

uint32\_t metadata

Used to store metadata information such as storage version.

**Definition** zms\_priv.h:74

[zms\_ate::data](structzms__ate.md#a54e3d4ebd6e5eda65e56033e6e2d379b)

uint8\_t data[8]

data field used to store small sized data

**Definition** zms\_priv.h:59

[zms\_ate::offset](structzms__ate.md#a7d623901562467778185ef61b3f9bb0f)

uint32\_t offset

data offset within sector

**Definition** zms\_priv.h:62

[zms\_ate::data\_crc](structzms__ate.md#a8b70dd09e10545dae52bba3eb5f167e8)

uint32\_t data\_crc

crc for data: The data CRC is checked only when the whole data of the element is read.

**Definition** zms\_priv.h:70

[zms\_ate::cycle\_cnt](structzms__ate.md#a9d5e9e8ac241b613fd2db14cc85d0323)

uint8\_t cycle\_cnt

cycle counter for non erasable devices

**Definition** zms\_priv.h:52

[zms\_ate::len](structzms__ate.md#aa71a3cb51572eaaa348c3644f332fc7e)

uint16\_t len

data len within sector

**Definition** zms\_priv.h:54

[zms\_ate::crc8](structzms__ate.md#ac96dfde8f44e1af031c11490a0add94a)

uint8\_t crc8

crc8 check of the entry

**Definition** zms\_priv.h:50

[zms\_ate::id](structzms__ate.md#ae624bc7570e77b75fcdc0fa1d74224c8)

uint32\_t id

data id

**Definition** zms\_priv.h:56

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [fs](dir_e8230ac05e3aac2b3e0e734457f44f71.md)
- [zms](dir_142391b9069c4c871a5c68dc8690aac3.md)
- [zms\_priv.h](zms__priv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
