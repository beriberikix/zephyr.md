---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32__flash__api__extensions_8h_source.html
original_path: doxygen/html/stm32__flash__api__extensions_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

7#include <[zephyr/drivers/flash.h](flash_8h.md)>

8

[ 9](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8)enum [stm32\_ex\_ops](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8) {

10 /\*

11 \* STM32 sector write protection control.

12 \*

13 \* As an input this operation takes a structure with two sector masks,

14 \* first mask is used to enable protection on sectors, while second mask

15 \* is used to do the opposite. If both masks are 0, then protection will

16 \* remain unchanged. If same sector is set on both masks, protection

17 \* will be enabled.

18 \*

19 \* As an output, sector mask with enabled protection is returned.

20 \* Input can be NULL if we only want to get protected sectors.

21 \* Output can be NULL if not needed.

22 \*/

[ 23](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe) [FLASH\_STM32\_EX\_OP\_SECTOR\_WP](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe) = [FLASH\_EX\_OP\_VENDOR\_BASE](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3),

24 /\*

25 \* STM32 sector readout protection control.

26 \*

27 \* As an input this operation takes structure with information about

28 \* desired RDP state. As an output the status after applying changes

29 \* is returned.

30 \*/

[ 31](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0) [FLASH\_STM32\_EX\_OP\_RDP](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0),

32 /\*

33 \* STM32 block option register.

34 \*

35 \* This operation causes option register to be locked until next boot.

36 \* After calling, it's not possible to change option bytes (WP, RDP,

37 \* user bytes).

38 \*/

[ 39](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903) [FLASH\_STM32\_EX\_OP\_BLOCK\_OPTION\_REG](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903),

40 /\*

41 \* STM32 block control register.

42 \*

43 \* This operation causes control register to be locked until next boot.

44 \* After calling, it's not possible to perform basic operation like

45 \* erasing or writing.

46 \*/

[ 47](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096) [FLASH\_STM32\_EX\_OP\_BLOCK\_CONTROL\_REG](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096),

48};

49

50#if defined(CONFIG\_FLASH\_STM32\_WRITE\_PROTECT)

51struct flash\_stm32\_ex\_op\_sector\_wp\_in {

52 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) enable\_mask;

53 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) disable\_mask;

54};

55

56struct flash\_stm32\_ex\_op\_sector\_wp\_out {

57 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) protected\_mask;

58};

59#endif /\* CONFIG\_FLASH\_STM32\_WRITE\_PROTECT \*/

60

61#if defined(CONFIG\_FLASH\_STM32\_READOUT\_PROTECTION)

62struct flash\_stm32\_ex\_op\_rdp {

63 bool enable;

64 bool permanent;

65};

66#endif /\* CONFIG\_FLASH\_STM32\_READOUT\_PROTECTION \*/

[flash.h](flash_8h.md)

Public API for FLASH drivers.

[FLASH\_EX\_OP\_VENDOR\_BASE](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3)

#define FLASH\_EX\_OP\_VENDOR\_BASE

**Definition** flash.h:471

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[stm32\_ex\_ops](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8)

stm32\_ex\_ops

**Definition** stm32\_flash\_api\_extensions.h:9

[FLASH\_STM32\_EX\_OP\_BLOCK\_OPTION\_REG](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a59b3b9a3b0eaee9cd4435f452855b903)

@ FLASH\_STM32\_EX\_OP\_BLOCK\_OPTION\_REG

**Definition** stm32\_flash\_api\_extensions.h:39

[FLASH\_STM32\_EX\_OP\_SECTOR\_WP](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8a7bde6043879f1a6139da11679b4455fe)

@ FLASH\_STM32\_EX\_OP\_SECTOR\_WP

**Definition** stm32\_flash\_api\_extensions.h:23

[FLASH\_STM32\_EX\_OP\_BLOCK\_CONTROL\_REG](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8aab8109cdf28181ef0dbb9d1e3b93b096)

@ FLASH\_STM32\_EX\_OP\_BLOCK\_CONTROL\_REG

**Definition** stm32\_flash\_api\_extensions.h:47

[FLASH\_STM32\_EX\_OP\_RDP](stm32__flash__api__extensions_8h.md#a95b012159eb95cd62859a6d5c4d862b8ae1b013a96c3a64b0d3e677b4bce954a0)

@ FLASH\_STM32\_EX\_OP\_RDP

**Definition** stm32\_flash\_api\_extensions.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash](dir_b5b0d43e6264d65db716db62f9858e50.md)
- [stm32\_flash\_api\_extensions.h](stm32__flash__api__extensions_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
