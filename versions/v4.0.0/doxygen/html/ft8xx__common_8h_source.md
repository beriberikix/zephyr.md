---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ft8xx__common_8h_source.html
original_path: doxygen/html/ft8xx__common_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx\_common.h

[Go to the documentation of this file.](ft8xx__common_8h.md)

1/\*

2 \* Copyright (c) 2020 Hubert Miś

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_COMMON\_H\_

13#define ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_COMMON\_H\_

14

15#include <[stdint.h](stdint_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

[ 34](group__ft8xx__common.md#ga7623499f328d820b1e84d2a3834a89a2)void [ft8xx\_wr8](group__ft8xx__common.md#ga7623499f328d820b1e84d2a3834a89a2)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data);

35

[ 42](group__ft8xx__common.md#gadfbff24d8fb246081cefbc51190b32e5)void [ft8xx\_wr16](group__ft8xx__common.md#gadfbff24d8fb246081cefbc51190b32e5)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

43

[ 50](group__ft8xx__common.md#ga3158d2c2605f66fc22bbf336d780b8bf)void [ft8xx\_wr32](group__ft8xx__common.md#ga3158d2c2605f66fc22bbf336d780b8bf)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data);

51

[ 59](group__ft8xx__common.md#gac7ed90cf4a51fc9139c49ce352a25385)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ft8xx\_rd8](group__ft8xx__common.md#gac7ed90cf4a51fc9139c49ce352a25385)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address);

60

[ 68](group__ft8xx__common.md#gad52c57f65516917792cb07f6d2f2bf71)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ft8xx\_rd16](group__ft8xx__common.md#gad52c57f65516917792cb07f6d2f2bf71)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address);

69

[ 77](group__ft8xx__common.md#ga9e78caa02181c65a5c5dac39438ca3e3)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ft8xx\_rd32](group__ft8xx__common.md#ga9e78caa02181c65a5c5dac39438ca3e3)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address);

78

82

83#ifdef \_\_cplusplus

84}

85#endif

86

87#endif /\* ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_COMMON\_H\_ \*/

[ft8xx\_wr32](group__ft8xx__common.md#ga3158d2c2605f66fc22bbf336d780b8bf)

void ft8xx\_wr32(uint32\_t address, uint32\_t data)

Write 4 bytes (32 bits) to FT8xx memory.

[ft8xx\_wr8](group__ft8xx__common.md#ga7623499f328d820b1e84d2a3834a89a2)

void ft8xx\_wr8(uint32\_t address, uint8\_t data)

Write 1 byte (8 bits) to FT8xx memory.

[ft8xx\_rd32](group__ft8xx__common.md#ga9e78caa02181c65a5c5dac39438ca3e3)

uint32\_t ft8xx\_rd32(uint32\_t address)

Read 4 bytes (32 bits) from FT8xx memory.

[ft8xx\_rd8](group__ft8xx__common.md#gac7ed90cf4a51fc9139c49ce352a25385)

uint8\_t ft8xx\_rd8(uint32\_t address)

Read 1 byte (8 bits) from FT8xx memory.

[ft8xx\_rd16](group__ft8xx__common.md#gad52c57f65516917792cb07f6d2f2bf71)

uint16\_t ft8xx\_rd16(uint32\_t address)

Read 2 bytes (16 bits) from FT8xx memory.

[ft8xx\_wr16](group__ft8xx__common.md#gadfbff24d8fb246081cefbc51190b32e5)

void ft8xx\_wr16(uint32\_t address, uint16\_t data)

Write 2 bytes (16 bits) to FT8xx memory.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx\_common.h](ft8xx__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
