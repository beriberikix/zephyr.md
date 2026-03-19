---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structs_8h_source.html
original_path: doxygen/html/structs_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

structs.h

[Go to the documentation of this file.](structs_8h.md)

1/\*

2 \* Copyright (c) BayLibre SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* The purpose of this file is to provide essential/minimal architecture-

9 \* specific structure definitions to be included in generic kernel

10 \* structures.

11 \*

12 \* The following rules must be observed:

13 \* 1. arch/structs.h shall not depend on kernel.h both directly and

14 \* indirectly (i.e. it shall not include any header files that include

15 \* kernel.h in their dependency chain).

16 \* 2. kernel.h shall imply arch/structs.h via kernel\_structs.h , such that

17 \* it shall not be necessary to include arch/structs.h explicitly when

18 \* kernel.h is included.

19 \*/

20

21#ifndef ZEPHYR\_INCLUDE\_ARCH\_STRUCTS\_H\_

22#define ZEPHYR\_INCLUDE\_ARCH\_STRUCTS\_H\_

23

24#if !defined(\_ASMLANGUAGE)

25

26#if defined(CONFIG\_ARM64)

27#include <[zephyr/arch/arm64/structs.h](arm64_2structs_8h.md)>

28#elif defined(CONFIG\_RISCV)

29#include <[zephyr/arch/riscv/structs.h](riscv_2structs_8h.md)>

30#elif defined(CONFIG\_ARM)

31#include <[zephyr/arch/arm/structs.h](arm_2structs_8h.md)>

32#else

33

34/\* Default definitions when no architecture specific definitions exist. \*/

35

36/\* Per CPU architecture specifics (empty) \*/

37struct \_cpu\_arch {

38#ifdef \_\_cplusplus

39 /\* This struct will have a size 0 in C which is not allowed in C++ (it'll have a size 1). To

40 \* prevent this, we add a 1 byte dummy variable.

41 \*/

42 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dummy;

43#endif

44};

45

46#endif

47

48/\* typedefs to be used with GEN\_OFFSET\_SYM(), etc. \*/

49typedef struct \_cpu\_arch \_cpu\_arch\_t;

50

51#endif /\* \_ASMLANGUAGE \*/

52

53#endif /\* ZEPHYR\_INCLUDE\_ARCH\_STRUCTS\_H\_ \*/

[structs.h](arm64_2structs_8h.md)

[structs.h](arm_2structs_8h.md)

[structs.h](riscv_2structs_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [structs.h](structs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
