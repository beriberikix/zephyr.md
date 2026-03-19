---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32-fmc-nor-psram_8h_source.html
original_path: doxygen/html/stm32-fmc-nor-psram_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32-fmc-nor-psram.h

[Go to the documentation of this file.](stm32-fmc-nor-psram_8h.md)

1/\*

2 \* Copyright (c) 2022 Georgij Cernysiov

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEMORY\_CONTROLLER\_STM32\_FMC\_SRAM\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEMORY\_CONTROLLER\_STM32\_FMC\_SRAM\_H\_

9

10/\* Data Address Bus Multiplexing \*/

[ 11](stm32-fmc-nor-psram_8h.md#ab49545823d378c30d0b2054275dd5316)#define STM32\_FMC\_DATA\_ADDRESS\_MUX\_DISABLE 0x00000000UL

[ 12](stm32-fmc-nor-psram_8h.md#a7318079a6d6cf395a48d8a9b3b573965)#define STM32\_FMC\_DATA\_ADDRESS\_MUX\_ENABLE 0x00000002UL

13

14/\* Memory Type \*/

[ 15](stm32-fmc-nor-psram_8h.md#ae41ef04358fa9521f97c47a72bbb1c86)#define STM32\_FMC\_MEMORY\_TYPE\_SRAM 0x00000000UL

[ 16](stm32-fmc-nor-psram_8h.md#a11c633811ebce988518c1aafc828eb23)#define STM32\_FMC\_MEMORY\_TYPE\_PSRAM 0x00000004UL

[ 17](stm32-fmc-nor-psram_8h.md#a61a73700a6c8e70fde4530e4f3db90be)#define STM32\_FMC\_MEMORY\_TYPE\_NOR 0x00000008UL

18

19/\* NORSRAM Data Width \*/

[ 20](stm32-fmc-nor-psram_8h.md#a806afc07795847549ae10e20228de965)#define STM32\_FMC\_NORSRAM\_MEM\_BUS\_WIDTH\_8 0x00000000UL

[ 21](stm32-fmc-nor-psram_8h.md#add91fa155ec311548bd135b230ef2915)#define STM32\_FMC\_NORSRAM\_MEM\_BUS\_WIDTH\_16 0x00000010UL

[ 22](stm32-fmc-nor-psram_8h.md#a582648a2c62410d398b13e519ec37baf)#define STM32\_FMC\_NORSRAM\_MEM\_BUS\_WIDTH\_32 0x00000020UL

23

24/\* Burst Access Mode \*/

[ 25](stm32-fmc-nor-psram_8h.md#a527403ad639bbd6c5680d56de37c4e4e)#define STM32\_FMC\_BURST\_ACCESS\_MODE\_DISABLE 0x00000000UL

[ 26](stm32-fmc-nor-psram_8h.md#a75ba9ce1a097c82d7f9527b4b8a08928)#define STM32\_FMC\_BURST\_ACCESS\_MODE\_ENABLE 0x00000100UL

27

28/\* Wait Signal Polarity \*/

[ 29](stm32-fmc-nor-psram_8h.md#af6b0ada2448b137cab429b6a47a5b516)#define STM32\_FMC\_WAIT\_SIGNAL\_POLARITY\_LOW 0x00000000UL

[ 30](stm32-fmc-nor-psram_8h.md#a88b374fdbb484ab559e56c415c2c12ca)#define STM32\_FMC\_WAIT\_SIGNAL\_POLARITY\_HIGH 0x00000200UL

31

32/\* Wait Timing \*/

[ 33](stm32-fmc-nor-psram_8h.md#add819f0ba699002506392a0bd9f91337)#define STM32\_FMC\_WAIT\_TIMING\_BEFORE\_WS 0x00000000UL

[ 34](stm32-fmc-nor-psram_8h.md#ae1788e8b88e3e22547aa9aa8948f6570)#define STM32\_FMC\_WAIT\_TIMING\_DURING\_WS 0x00000800UL

35

36/\* Write Operation \*/

[ 37](stm32-fmc-nor-psram_8h.md#aca93e3b2ae199989d555125c4acf334f)#define STM32\_FMC\_WRITE\_OPERATION\_DISABLE 0x00000000UL

[ 38](stm32-fmc-nor-psram_8h.md#aa17046722e4d9583d2d6b2142d5e8026)#define STM32\_FMC\_WRITE\_OPERATION\_ENABLE 0x00001000UL

39

40/\* Wait Signal \*/

[ 41](stm32-fmc-nor-psram_8h.md#a18e24d58c88346b52f9602c6d7017e8d)#define STM32\_FMC\_WAIT\_SIGNAL\_DISABLE 0x00000000UL

[ 42](stm32-fmc-nor-psram_8h.md#a6e5fb677427ede2899684fdcce7e1500)#define STM32\_FMC\_WAIT\_SIGNAL\_ENABLE 0x00002000UL

43

44/\* Extended Mode \*/

[ 45](stm32-fmc-nor-psram_8h.md#aab24ca64ba4b6065108d29b699bff5e0)#define STM32\_FMC\_EXTENDED\_MODE\_DISABLE 0x00000000UL

[ 46](stm32-fmc-nor-psram_8h.md#a86b2a55f428d5413f6d7ea4d3263da6d)#define STM32\_FMC\_EXTENDED\_MODE\_ENABLE 0x00004000UL

47

48/\* Asynchronous Wait \*/

[ 49](stm32-fmc-nor-psram_8h.md#a32371c9989a20cb2fdbc354af6839637)#define STM32\_FMC\_ASYNCHRONOUS\_WAIT\_DISABLE 0x00000000UL

[ 50](stm32-fmc-nor-psram_8h.md#a49857e48048dcc5758dad37507d501c8)#define STM32\_FMC\_ASYNCHRONOUS\_WAIT\_ENABLE 0x00008000UL

51

52/\* Write Burst \*/

[ 53](stm32-fmc-nor-psram_8h.md#aca6157135cdd3caa7c26d7f90bd324db)#define STM32\_FMC\_WRITE\_BURST\_DISABLE 0x00000000UL

[ 54](stm32-fmc-nor-psram_8h.md#ab87a4ac9a4a867920569ba3a48df4967)#define STM32\_FMC\_WRITE\_BURST\_ENABLE 0x00080000UL

55

56/\* Continuous Clock \*/

[ 57](stm32-fmc-nor-psram_8h.md#aeafacbe30f5a783ab9df44da90d095be)#define STM32\_FMC\_CONTINUOUS\_CLOCK\_SYNC\_ONLY 0x00000000UL

[ 58](stm32-fmc-nor-psram_8h.md#a505d16591d41726a4012a51de973c2aa)#define STM32\_FMC\_CONTINUOUS\_CLOCK\_SYNC\_ASYNC 0x00100000UL

59

60/\* Write FIFO \*/

61/\* Not every SoC can disable FIFO, refer to reference manual \*/

[ 62](stm32-fmc-nor-psram_8h.md#ab203835e4cff8a22243715cd93a9194f)#define STM32\_FMC\_WRITE\_FIFO\_DISABLE 0x00200000UL

[ 63](stm32-fmc-nor-psram_8h.md#a1f68faf14d41d1f272302b0e88b879da)#define STM32\_FMC\_WRITE\_FIFO\_ENABLE 0x00000000UL

64

65/\* Page Size \*/

[ 66](stm32-fmc-nor-psram_8h.md#a1455eadceb4c7fe93775bd25b7d73bc4)#define STM32\_FMC\_PAGE\_SIZE\_NONE 0x00000000UL

[ 67](stm32-fmc-nor-psram_8h.md#ab218cd22286f68b776becba79b429179)#define STM32\_FMC\_PAGE\_SIZE\_128 0x00010000UL

[ 68](stm32-fmc-nor-psram_8h.md#a1c2636c154fc9fd120f8cd4663e8cf7e)#define STM32\_FMC\_PAGE\_SIZE\_256 0x00020000UL

[ 69](stm32-fmc-nor-psram_8h.md#a93eef275a4b8a11a5167ef94085e21fa)#define STM32\_FMC\_PAGE\_SIZE\_512 0x00030000UL

[ 70](stm32-fmc-nor-psram_8h.md#ad6476a3ef69c624fb9046d1cae4d26fa)#define STM32\_FMC\_PAGE\_SIZE\_1024 0x00040000UL

71

72/\* Access Mode \*/

[ 73](stm32-fmc-nor-psram_8h.md#a4733d2c4e687c821921f710c1154e9b5)#define STM32\_FMC\_ACCESS\_MODE\_A 0x00000000UL

[ 74](stm32-fmc-nor-psram_8h.md#a58dff9715cadd3b5ce6236f253578e9f)#define STM32\_FMC\_ACCESS\_MODE\_B 0x10000000UL

[ 75](stm32-fmc-nor-psram_8h.md#a4fd51f5975ad4abe6e94a4696a372475)#define STM32\_FMC\_ACCESS\_MODE\_C 0x20000000UL

[ 76](stm32-fmc-nor-psram_8h.md#ab5715e383c55c6660e1b7da618eed346)#define STM32\_FMC\_ACCESS\_MODE\_D 0x30000000UL

77

78#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEMORY\_CONTROLLER\_STM32\_FMC\_SRAM\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-controller](dir_35d961eb615f3ea19ec1fece6b4faa4b.md)
- [stm32-fmc-nor-psram.h](stm32-fmc-nor-psram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
