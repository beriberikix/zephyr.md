---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/npcx__flash__api__ex_8h.html
original_path: doxygen/html/npcx__flash__api__ex_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npcx\_flash\_api\_ex.h File Reference

`#include <[zephyr/drivers/flash.h](flash_8h_source.md)>`

[Go to the source code of this file.](npcx__flash__api__ex_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [npcx\_ex\_ops\_uma\_in](structnpcx__ex__ops__uma__in.md) |
| struct | [npcx\_ex\_ops\_uma\_out](structnpcx__ex__ops__uma__out.md) |
| struct | [npcx\_ex\_ops\_qspi\_oper\_in](structnpcx__ex__ops__qspi__oper__in.md) |
| struct | [npcx\_ex\_ops\_qspi\_oper\_out](structnpcx__ex__ops__qspi__oper__out.md) |

| Macros | |
| --- | --- |
| #define | [NPCX\_EX\_OP\_LOCK\_UMA](#abfe13897bc1ad3a19d7cf4f52cc86c7b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* Lock/Unlock UMA mode \*/ |
| #define | [NPCX\_EX\_OP\_INT\_FLASH\_WP](#af33c593f223dc4ebd2d2b2745cd20951)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* Issue write protection of internal flash \*/ |

| Enumerations | |
| --- | --- |
| enum | [flash\_npcx\_ex\_ops](#ad4f93f7272e825355875d0fb05351474) { [FLASH\_NPCX\_EX\_OP\_EXEC\_UMA](#ad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007) = FLASH\_EX\_OP\_VENDOR\_BASE , [FLASH\_NPCX\_EX\_OP\_SET\_QSPI\_OPER](#ad4f93f7272e825355875d0fb05351474abbf87cdc7e9c3cdc9e6afde3c0485ec9) , [FLASH\_NPCX\_EX\_OP\_GET\_QSPI\_OPER](#ad4f93f7272e825355875d0fb05351474a46c5fff8b0ffbc480c01fed93ff8fd57) } |

## Macro Definition Documentation

## [◆ ](#af33c593f223dc4ebd2d2b2745cd20951)NPCX\_EX\_OP\_INT\_FLASH\_WP

| #define NPCX\_EX\_OP\_INT\_FLASH\_WP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* Issue write protection of internal flash \*/ |
| --- |

## [◆ ](#abfe13897bc1ad3a19d7cf4f52cc86c7b)NPCX\_EX\_OP\_LOCK\_UMA

| #define NPCX\_EX\_OP\_LOCK\_UMA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* Lock/Unlock UMA mode \*/ |
| --- |

## Enumeration Type Documentation

## [◆ ](#ad4f93f7272e825355875d0fb05351474)flash\_npcx\_ex\_ops

| enum [flash\_npcx\_ex\_ops](#ad4f93f7272e825355875d0fb05351474) |
| --- |

| Enumerator | |
| --- | --- |
| FLASH\_NPCX\_EX\_OP\_EXEC\_UMA |  |
| FLASH\_NPCX\_EX\_OP\_SET\_QSPI\_OPER |  |
| FLASH\_NPCX\_EX\_OP\_GET\_QSPI\_OPER |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash](dir_b5b0d43e6264d65db716db62f9858e50.md)
- [npcx\_flash\_api\_ex.h](npcx__flash__api__ex_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
