---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/npcx__flash__api__ex_8h_source.html
original_path: doxygen/html/npcx__flash__api__ex_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npcx\_flash\_api\_ex.h

[Go to the documentation of this file.](npcx__flash__api__ex_8h.md)

1/\*

2 \* Copyright (c) 2023 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_ZEPHYR\_INCLUDE\_DRIVERS\_NPCX\_FLASH\_API\_EX\_H\_\_

8#define \_\_ZEPHYR\_INCLUDE\_DRIVERS\_NPCX\_FLASH\_API\_EX\_H\_\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[zephyr/drivers/flash.h](flash_8h.md)>

15

[ 16](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474)enum [flash\_npcx\_ex\_ops](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474) {

17 /\*

18 \* NPCX User Mode Access (UMA) mode execution.

19 \*

20 \* Execute a SPI transaction via User Mode Access (UMA) mode. Users can

21 \* perform a customized SPI transaction to gread or write the device's

22 \* configuration such as status registers of nor flash, power on/off,

23 \* and so on.

24 \*/

[ 25](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007) [FLASH\_NPCX\_EX\_OP\_EXEC\_UMA](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007) = [FLASH\_EX\_OP\_VENDOR\_BASE](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3),

26 /\*

27 \* NPCX Configure specific operation for Quad-SPI nor flash.

28 \*

29 \* It configures specific operation for Quad-SPI nor flash such as lock

30 \* or unlock UMA mode, set write protection pin of internal flash, and

31 \* so on.

32 \*/

[ 33](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474abbf87cdc7e9c3cdc9e6afde3c0485ec9) [FLASH\_NPCX\_EX\_OP\_SET\_QSPI\_OPER](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474abbf87cdc7e9c3cdc9e6afde3c0485ec9),

34 /\*

35 \* NPCX Get specific operation for Quad-SPI nor flash.

36 \*

37 \* It returns current specific operation for Quad-SPI nor flash.

38 \*/

[ 39](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474a46c5fff8b0ffbc480c01fed93ff8fd57) [FLASH\_NPCX\_EX\_OP\_GET\_QSPI\_OPER](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474a46c5fff8b0ffbc480c01fed93ff8fd57),

40};

41

42/\* Structures used by FLASH\_NPCX\_EX\_OP\_EXEC\_UMA \*/

[ 43](structnpcx__ex__ops__uma__in.md)struct [npcx\_ex\_ops\_uma\_in](structnpcx__ex__ops__uma__in.md) {

[ 44](structnpcx__ex__ops__uma__in.md#a891172574f487bcfbcbbed20cd340998) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [opcode](structnpcx__ex__ops__uma__in.md#a891172574f487bcfbcbbed20cd340998);

[ 45](structnpcx__ex__ops__uma__in.md#a67c765977abd17095e4589604dfe43b0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[tx\_buf](structnpcx__ex__ops__uma__in.md#a67c765977abd17095e4589604dfe43b0);

[ 46](structnpcx__ex__ops__uma__in.md#add76f25d7adf905d4d4ba3b6f4b977e6) size\_t [tx\_count](structnpcx__ex__ops__uma__in.md#add76f25d7adf905d4d4ba3b6f4b977e6);

[ 47](structnpcx__ex__ops__uma__in.md#a4fe44cf0e3b09193700a72b62b78f544) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [addr](structnpcx__ex__ops__uma__in.md#a4fe44cf0e3b09193700a72b62b78f544);

[ 48](structnpcx__ex__ops__uma__in.md#a3c950c4208da78e2908a116ea3eedd5f) size\_t [addr\_count](structnpcx__ex__ops__uma__in.md#a3c950c4208da78e2908a116ea3eedd5f);

[ 49](structnpcx__ex__ops__uma__in.md#a7c36c34ffe3f6c69e9229efdc41da87c) size\_t [rx\_count](structnpcx__ex__ops__uma__in.md#a7c36c34ffe3f6c69e9229efdc41da87c);

50};

51

[ 52](structnpcx__ex__ops__uma__out.md)struct [npcx\_ex\_ops\_uma\_out](structnpcx__ex__ops__uma__out.md) {

[ 53](structnpcx__ex__ops__uma__out.md#a9be2364b1328eedc07e0123d774dbba7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[rx\_buf](structnpcx__ex__ops__uma__out.md#a9be2364b1328eedc07e0123d774dbba7);

54};

55

56/\* Structures used by FLASH\_NPCX\_EX\_OP\_SET\_QSPI\_OPER \*/

[ 57](structnpcx__ex__ops__qspi__oper__in.md)struct [npcx\_ex\_ops\_qspi\_oper\_in](structnpcx__ex__ops__qspi__oper__in.md) {

[ 58](structnpcx__ex__ops__qspi__oper__in.md#afc12bebd886ba71fc9431cedf0765c24) bool [enable](structnpcx__ex__ops__qspi__oper__in.md#afc12bebd886ba71fc9431cedf0765c24);

[ 59](structnpcx__ex__ops__qspi__oper__in.md#a0b9c9407bb320396d73f30ae4a8b55f1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mask](structnpcx__ex__ops__qspi__oper__in.md#a0b9c9407bb320396d73f30ae4a8b55f1);

60};

61

62/\* Structures used by FLASH\_NPCX\_EX\_OP\_GET\_QSPI\_OPER \*/

[ 63](structnpcx__ex__ops__qspi__oper__out.md)struct [npcx\_ex\_ops\_qspi\_oper\_out](structnpcx__ex__ops__qspi__oper__out.md) {

[ 64](structnpcx__ex__ops__qspi__oper__out.md#aa77f1bdcc00e1f3cc7a66cc150ab5686) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [oper](structnpcx__ex__ops__qspi__oper__out.md#aa77f1bdcc00e1f3cc7a66cc150ab5686);

65};

66

67/\* Specific NPCX QSPI devices control bits \*/

[ 68](npcx__flash__api__ex_8h.md#abfe13897bc1ad3a19d7cf4f52cc86c7b)#define NPCX\_EX\_OP\_LOCK\_UMA BIT(0) /\* Lock/Unlock UMA mode \*/

[ 69](npcx__flash__api__ex_8h.md#af33c593f223dc4ebd2d2b2745cd20951)#define NPCX\_EX\_OP\_INT\_FLASH\_WP BIT(1) /\* Issue write protection of internal flash \*/

70

71#ifdef \_\_cplusplus

72}

73#endif

74

75#endif /\* \_\_ZEPHYR\_INCLUDE\_DRIVERS\_NPCX\_FLASH\_API\_EX\_H\_\_ \*/

[flash.h](flash_8h.md)

Public API for FLASH drivers.

[FLASH\_EX\_OP\_VENDOR\_BASE](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3)

#define FLASH\_EX\_OP\_VENDOR\_BASE

**Definition** flash.h:630

[flash\_npcx\_ex\_ops](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474)

flash\_npcx\_ex\_ops

**Definition** npcx\_flash\_api\_ex.h:16

[FLASH\_NPCX\_EX\_OP\_GET\_QSPI\_OPER](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474a46c5fff8b0ffbc480c01fed93ff8fd57)

@ FLASH\_NPCX\_EX\_OP\_GET\_QSPI\_OPER

**Definition** npcx\_flash\_api\_ex.h:39

[FLASH\_NPCX\_EX\_OP\_SET\_QSPI\_OPER](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474abbf87cdc7e9c3cdc9e6afde3c0485ec9)

@ FLASH\_NPCX\_EX\_OP\_SET\_QSPI\_OPER

**Definition** npcx\_flash\_api\_ex.h:33

[FLASH\_NPCX\_EX\_OP\_EXEC\_UMA](npcx__flash__api__ex_8h.md#ad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007)

@ FLASH\_NPCX\_EX\_OP\_EXEC\_UMA

**Definition** npcx\_flash\_api\_ex.h:25

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[npcx\_ex\_ops\_qspi\_oper\_in](structnpcx__ex__ops__qspi__oper__in.md)

**Definition** npcx\_flash\_api\_ex.h:57

[npcx\_ex\_ops\_qspi\_oper\_in::mask](structnpcx__ex__ops__qspi__oper__in.md#a0b9c9407bb320396d73f30ae4a8b55f1)

uint32\_t mask

**Definition** npcx\_flash\_api\_ex.h:59

[npcx\_ex\_ops\_qspi\_oper\_in::enable](structnpcx__ex__ops__qspi__oper__in.md#afc12bebd886ba71fc9431cedf0765c24)

bool enable

**Definition** npcx\_flash\_api\_ex.h:58

[npcx\_ex\_ops\_qspi\_oper\_out](structnpcx__ex__ops__qspi__oper__out.md)

**Definition** npcx\_flash\_api\_ex.h:63

[npcx\_ex\_ops\_qspi\_oper\_out::oper](structnpcx__ex__ops__qspi__oper__out.md#aa77f1bdcc00e1f3cc7a66cc150ab5686)

uint32\_t oper

**Definition** npcx\_flash\_api\_ex.h:64

[npcx\_ex\_ops\_uma\_in](structnpcx__ex__ops__uma__in.md)

**Definition** npcx\_flash\_api\_ex.h:43

[npcx\_ex\_ops\_uma\_in::addr\_count](structnpcx__ex__ops__uma__in.md#a3c950c4208da78e2908a116ea3eedd5f)

size\_t addr\_count

**Definition** npcx\_flash\_api\_ex.h:48

[npcx\_ex\_ops\_uma\_in::addr](structnpcx__ex__ops__uma__in.md#a4fe44cf0e3b09193700a72b62b78f544)

uint32\_t addr

**Definition** npcx\_flash\_api\_ex.h:47

[npcx\_ex\_ops\_uma\_in::tx\_buf](structnpcx__ex__ops__uma__in.md#a67c765977abd17095e4589604dfe43b0)

uint8\_t \* tx\_buf

**Definition** npcx\_flash\_api\_ex.h:45

[npcx\_ex\_ops\_uma\_in::rx\_count](structnpcx__ex__ops__uma__in.md#a7c36c34ffe3f6c69e9229efdc41da87c)

size\_t rx\_count

**Definition** npcx\_flash\_api\_ex.h:49

[npcx\_ex\_ops\_uma\_in::opcode](structnpcx__ex__ops__uma__in.md#a891172574f487bcfbcbbed20cd340998)

uint8\_t opcode

**Definition** npcx\_flash\_api\_ex.h:44

[npcx\_ex\_ops\_uma\_in::tx\_count](structnpcx__ex__ops__uma__in.md#add76f25d7adf905d4d4ba3b6f4b977e6)

size\_t tx\_count

**Definition** npcx\_flash\_api\_ex.h:46

[npcx\_ex\_ops\_uma\_out](structnpcx__ex__ops__uma__out.md)

**Definition** npcx\_flash\_api\_ex.h:52

[npcx\_ex\_ops\_uma\_out::rx\_buf](structnpcx__ex__ops__uma__out.md#a9be2364b1328eedc07e0123d774dbba7)

uint8\_t \* rx\_buf

**Definition** npcx\_flash\_api\_ex.h:53

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash](dir_b5b0d43e6264d65db716db62f9858e50.md)
- [npcx\_flash\_api\_ex.h](npcx__flash__api__ex_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
