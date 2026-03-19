---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32__flash__api__extensions_8h_source.html
original_path: doxygen/html/stm32__flash__api__extensions_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_flash\_api\_extensions.h

[Go to the documentation of this file.](stm32__flash__api__extensions_8h.md)

1/\*

2 \* Copyright (c) 2023 Google Inc

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_STM32\_FLASH\_API\_EXTENSIONS\_H\_\_

8#define \_\_ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_STM32\_FLASH\_API\_EXTENSIONS\_H\_\_

9

10#include <[zephyr/drivers/flash.h](flash_8h.md)>

11

[ 12](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8)enum [stm32\_ex\_ops](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8) {

13 /\*

14 \* STM32 sector write protection control.

15 \*

16 \* As an input this operation takes a structure with two sector masks,

17 \* first mask is used to enable protection on sectors, while second mask

18 \* is used to do the opposite. If both masks are 0, then protection will

19 \* remain unchanged. If same sector is set on both masks, protection

20 \* will be enabled.

21 \*

22 \* As an output, sector mask with enabled protection is returned.

23 \* Input can be NULL if we only want to get protected sectors.

24 \* Output can be NULL if not needed.

25 \*/

[ 26](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe) [FLASH\_STM32\_EX\_OP\_SECTOR\_WP](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe) = [FLASH\_EX\_OP\_VENDOR\_BASE](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3),

27 /\*

28 \* STM32 sector readout protection control.

29 \*

30 \* As an input this operation takes structure with information about

31 \* desired RDP state. As an output the status after applying changes

32 \* is returned.

33 \*/

[ 34](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0) [FLASH\_STM32\_EX\_OP\_RDP](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0),

35 /\*

36 \* STM32 block option register.

37 \*

38 \* This operation causes option register to be locked until next boot.

39 \* After calling, it's not possible to change option bytes (WP, RDP,

40 \* user bytes).

41 \*/

[ 42](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903) [FLASH\_STM32\_EX\_OP\_BLOCK\_OPTION\_REG](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903),

43 /\*

44 \* STM32 block control register.

45 \*

46 \* This operation causes control register to be locked until next boot.

47 \* After calling, it's not possible to perform basic operation like

48 \* erasing or writing.

49 \*/

[ 50](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096) [FLASH\_STM32\_EX\_OP\_BLOCK\_CONTROL\_REG](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096),

51 /\*

52 \* STM32 option bytes read.

53 \*

54 \* Read the option bytes content, out takes a \*uint32\_t, in is unused.

55 \*/

[ 56](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a778e98df945314508cb9c2c266e6f02a) [FLASH\_STM32\_EX\_OP\_OPTB\_READ](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a778e98df945314508cb9c2c266e6f02a),

57 /\*

58 \* STM32 option bytes write.

59 \*

60 \* Write the option bytes content, in takes the new value, out is

61 \* unused. Note that the new value only takes effect after the device

62 \* is restarted.

63 \*/

[ 64](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a40f2e65d83c8ef8144c2ba3072cb4a85) [FLASH\_STM32\_EX\_OP\_OPTB\_WRITE](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a40f2e65d83c8ef8144c2ba3072cb4a85),

65};

66

67#if defined(CONFIG\_FLASH\_STM32\_WRITE\_PROTECT)

68struct flash\_stm32\_ex\_op\_sector\_wp\_in {

69 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) enable\_mask;

70 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) disable\_mask;

71};

72

73struct flash\_stm32\_ex\_op\_sector\_wp\_out {

74 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) protected\_mask;

75};

76#endif /\* CONFIG\_FLASH\_STM32\_WRITE\_PROTECT \*/

77

78#if defined(CONFIG\_FLASH\_STM32\_READOUT\_PROTECTION)

79struct flash\_stm32\_ex\_op\_rdp {

80 bool enable;

81 bool permanent;

82};

83#endif /\* CONFIG\_FLASH\_STM32\_READOUT\_PROTECTION \*/

84

85#endif /\* \_\_ZEPHYR\_INCLUDE\_DRIVERS\_FLASH\_STM32\_FLASH\_API\_EXTENSIONS\_H\_\_ \*/

[flash.h](flash_8h.md)

Public API for FLASH drivers.

[FLASH\_EX\_OP\_VENDOR\_BASE](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3)

#define FLASH\_EX\_OP\_VENDOR\_BASE

**Definition** flash.h:670

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[stm32\_ex\_ops](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8)

stm32\_ex\_ops

**Definition** stm32\_flash\_api\_extensions.h:12

[FLASH\_STM32\_EX\_OP\_OPTB\_WRITE](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a40f2e65d83c8ef8144c2ba3072cb4a85)

@ FLASH\_STM32\_EX\_OP\_OPTB\_WRITE

**Definition** stm32\_flash\_api\_extensions.h:64

[FLASH\_STM32\_EX\_OP\_BLOCK\_OPTION\_REG](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903)

@ FLASH\_STM32\_EX\_OP\_BLOCK\_OPTION\_REG

**Definition** stm32\_flash\_api\_extensions.h:42

[FLASH\_STM32\_EX\_OP\_OPTB\_READ](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a778e98df945314508cb9c2c266e6f02a)

@ FLASH\_STM32\_EX\_OP\_OPTB\_READ

**Definition** stm32\_flash\_api\_extensions.h:56

[FLASH\_STM32\_EX\_OP\_SECTOR\_WP](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe)

@ FLASH\_STM32\_EX\_OP\_SECTOR\_WP

**Definition** stm32\_flash\_api\_extensions.h:26

[FLASH\_STM32\_EX\_OP\_BLOCK\_CONTROL\_REG](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096)

@ FLASH\_STM32\_EX\_OP\_BLOCK\_CONTROL\_REG

**Definition** stm32\_flash\_api\_extensions.h:50

[FLASH\_STM32\_EX\_OP\_RDP](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0)

@ FLASH\_STM32\_EX\_OP\_RDP

**Definition** stm32\_flash\_api\_extensions.h:34

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash](dir_b5b0d43e6264d65db716db62f9858e50.md)
- [stm32\_flash\_api\_extensions.h](stm32__flash__api__extensions_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
