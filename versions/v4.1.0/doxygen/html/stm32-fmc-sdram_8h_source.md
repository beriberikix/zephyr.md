---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32-fmc-sdram_8h_source.html
original_path: doxygen/html/stm32-fmc-sdram_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32-fmc-sdram.h

[Go to the documentation of this file.](stm32-fmc-sdram_8h.md)

1/\*

2 \* Copyright (c) 2020 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEMORY\_CONTROLLER\_STM32\_FMC\_SDRAM\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEMORY\_CONTROLLER\_STM32\_FMC\_SDRAM\_H\_

9

10/\* Number of column address bits \*/

[ 11](stm32-fmc-sdram_8h.md#a798e3829273dca48b2ed76e279df842c)#define STM32\_FMC\_SDRAM\_NC\_8 0x00000000UL

[ 12](stm32-fmc-sdram_8h.md#a807f0465db440eb86ead4b2dc4ee3a20)#define STM32\_FMC\_SDRAM\_NC\_9 0x00000001UL

[ 13](stm32-fmc-sdram_8h.md#a25a1752dcbddf9266dda6e9fa85a86b8)#define STM32\_FMC\_SDRAM\_NC\_10 0x00000002UL

[ 14](stm32-fmc-sdram_8h.md#a4ec4d6d8f42060affca0ce2db8b90006)#define STM32\_FMC\_SDRAM\_NC\_11 0x00000003UL

15

16/\* Number of row address bits \*/

[ 17](stm32-fmc-sdram_8h.md#a65c68f541a9532a731656e8a38b09359)#define STM32\_FMC\_SDRAM\_NR\_11 0x00000000UL

[ 18](stm32-fmc-sdram_8h.md#a00e460b9811e7ed63042903d8fda601a)#define STM32\_FMC\_SDRAM\_NR\_12 0x00000004UL

[ 19](stm32-fmc-sdram_8h.md#a001ca62af0f1d4721469bcadc02de257)#define STM32\_FMC\_SDRAM\_NR\_13 0x00000008UL

20

21/\* Memory data bus width. \*/

[ 22](stm32-fmc-sdram_8h.md#a477086be84f346e4e0abbe539460be77)#define STM32\_FMC\_SDRAM\_MWID\_8 0x00000000UL

[ 23](stm32-fmc-sdram_8h.md#aac6bdf6c91e01b90ff50a60778629455)#define STM32\_FMC\_SDRAM\_MWID\_16 0x00000010UL

[ 24](stm32-fmc-sdram_8h.md#a72d44331d21b2ce2bd567f846db656ce)#define STM32\_FMC\_SDRAM\_MWID\_32 0x00000020UL

25

26/\* Number of internal banks \*/

[ 27](stm32-fmc-sdram_8h.md#a984d9f441337adf77c9242a31ffcd40b)#define STM32\_FMC\_SDRAM\_NB\_2 0x00000000UL

[ 28](stm32-fmc-sdram_8h.md#a31e5eadfa58fe4235f173c06203478bc)#define STM32\_FMC\_SDRAM\_NB\_4 0x00000040UL

29

30/\* CAS Latency \*/

[ 31](stm32-fmc-sdram_8h.md#a03e122c779deae71dcaf25aca2c2a218)#define STM32\_FMC\_SDRAM\_CAS\_1 0x00000080UL

[ 32](stm32-fmc-sdram_8h.md#a6324e8027282bfedda72d9f4b801a59b)#define STM32\_FMC\_SDRAM\_CAS\_2 0x00000100UL

[ 33](stm32-fmc-sdram_8h.md#ab9a9eb595e5a7dd82678686fab8a47c0)#define STM32\_FMC\_SDRAM\_CAS\_3 0x00000180UL

34

35/\* SDRAM clock configuration \*/

[ 36](stm32-fmc-sdram_8h.md#a229b8c7b8971890fee77294c1fdd03f6)#define STM32\_FMC\_SDRAM\_SDCLK\_DISABLE 0x00000000UL

[ 37](stm32-fmc-sdram_8h.md#a2b52bf4c1070870fe0f4e6cadac5df5b)#define STM32\_FMC\_SDRAM\_SDCLK\_PERIOD\_2 0x00000800UL

[ 38](stm32-fmc-sdram_8h.md#a7e945a96afae095a45b2c26db6c3f7b0)#define STM32\_FMC\_SDRAM\_SDCLK\_PERIOD\_3 0x00000C00UL

39

40/\* Burst read \*/

[ 41](stm32-fmc-sdram_8h.md#a71fd8c4cf69851b958f2ea3c02368f82)#define STM32\_FMC\_SDRAM\_RBURST\_DISABLE 0x00000000UL

[ 42](stm32-fmc-sdram_8h.md#a39aeab5bd26a13813842a68fc0d1106a)#define STM32\_FMC\_SDRAM\_RBURST\_ENABLE 0x00001000UL

43

44/\* Read pipe \*/

[ 45](stm32-fmc-sdram_8h.md#a3a0ee21974e21ac310965b585406d525)#define STM32\_FMC\_SDRAM\_RPIPE\_0 0x00000000UL

[ 46](stm32-fmc-sdram_8h.md#a12b5689fe5b87799af5bb881bb0147e3)#define STM32\_FMC\_SDRAM\_RPIPE\_1 0x00002000UL

[ 47](stm32-fmc-sdram_8h.md#a88f8480e54b16cf83ac0d01f16819c0a)#define STM32\_FMC\_SDRAM\_RPIPE\_2 0x00004000UL

48

49#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-controller](dir_35d961eb615f3ea19ec1fece6b4faa4b.md)
- [stm32-fmc-sdram.h](stm32-fmc-sdram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
