---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2common_2sys__io_8h_source.html
original_path: doxygen/html/arch_2common_2sys__io_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_io.h

[Go to the documentation of this file.](arch_2common_2sys__io_8h.md)

1/\*

2 \* Copyright (c) 2015, Wind River Systems, Inc.

3 \* Copyright (c) 2017, Oticon A/S

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8/\* Memory mapped registers I/O functions in non-arch-specific C code \*/

9

10#ifndef ZEPHYR\_INCLUDE\_ARCH\_COMMON\_SYS\_IO\_H\_

11#define ZEPHYR\_INCLUDE\_ARCH\_COMMON\_SYS\_IO\_H\_

12

13#ifndef \_ASMLANGUAGE

14

15#include <[zephyr/toolchain.h](toolchain_8h.md)>

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17#include <[zephyr/sys/sys\_io.h](sys_2sys__io_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 23](arch_2common_2sys__io_8h.md#a51f9740fef1b1bb2abc93126ca2646ae)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_read8](arch_2arm_2cortex__a__r_2sys__io_8h.md#a51f9740fef1b1bb2abc93126ca2646ae)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

24{

25 return \*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)addr;

26}

27

[ 28](arch_2common_2sys__io_8h.md#adf3b7a8a798d7497661d54d705a078fc)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write8](arch_2arm_2cortex__a__r_2sys__io_8h.md#adf3b7a8a798d7497661d54d705a078fc)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

29{

30 \*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)addr = data;

31}

32

[ 33](arch_2common_2sys__io_8h.md#ad8daa7da2671ca845272861859463567)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_read16](arch_2arm_2cortex__a__r_2sys__io_8h.md#ad8daa7da2671ca845272861859463567)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

34{

35 return \*(volatile [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*)addr;

36}

37

[ 38](arch_2common_2sys__io_8h.md#a5cae8f8c0ea3749985e80f6ca85b1b13)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write16](arch_2arm_2cortex__a__r_2sys__io_8h.md#a5cae8f8c0ea3749985e80f6ca85b1b13)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

39{

40 \*(volatile [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*)addr = data;

41}

42

[ 43](arch_2common_2sys__io_8h.md#a62f6066146f924b75015ae976b27866a)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_read32](arch_2arm_2cortex__a__r_2sys__io_8h.md#a62f6066146f924b75015ae976b27866a)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

44{

45 return \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr;

46}

47

[ 48](arch_2common_2sys__io_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write32](arch_2arm_2cortex__a__r_2sys__io_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

49{

50 \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr = data;

51}

52

[ 53](arch_2common_2sys__io_8h.md#ae20bb8c275dcc157c1be9b232d00ff9d)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_read64](arch_2arm_2cortex__a__r_2sys__io_8h.md#ae20bb8c275dcc157c1be9b232d00ff9d)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

54{

55 return \*(volatile [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*)addr;

56}

57

[ 58](arch_2common_2sys__io_8h.md#a00285d93d1c8951641510e2071d46b40)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write64](arch_2arm64_2sys__io_8h.md#a00285d93d1c8951641510e2071d46b40)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) data, [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

59{

60 \*(volatile [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*)addr = data;

61}

62

63#ifdef \_\_cplusplus

64}

65#endif

66

67#endif /\* \_ASMLANGUAGE \*/

68

69#endif /\* ZEPHYR\_INCLUDE\_ARCH\_COMMON\_SYS\_IO\_H\_ \*/

[sys\_write64](arch_2arm64_2sys__io_8h.md#a00285d93d1c8951641510e2071d46b40)

static ALWAYS\_INLINE void sys\_write64(uint64\_t data, mem\_addr\_t addr)

**Definition** sys\_io.h:95

[sys\_write32](arch_2arm_2cortex__a__r_2sys__io_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)

static ALWAYS\_INLINE void sys\_write32(uint32\_t data, mem\_addr\_t addr)

**Definition** sys\_io.h:69

[sys\_read8](arch_2arm_2cortex__a__r_2sys__io_8h.md#a51f9740fef1b1bb2abc93126ca2646ae)

static ALWAYS\_INLINE uint8\_t sys\_read8(mem\_addr\_t addr)

**Definition** sys\_io.h:27

[sys\_write16](arch_2arm_2cortex__a__r_2sys__io_8h.md#a5cae8f8c0ea3749985e80f6ca85b1b13)

static ALWAYS\_INLINE void sys\_write16(uint16\_t data, mem\_addr\_t addr)

**Definition** sys\_io.h:53

[sys\_read32](arch_2arm_2cortex__a__r_2sys__io_8h.md#a62f6066146f924b75015ae976b27866a)

static ALWAYS\_INLINE uint32\_t sys\_read32(mem\_addr\_t addr)

**Definition** sys\_io.h:59

[sys\_read16](arch_2arm_2cortex__a__r_2sys__io_8h.md#ad8daa7da2671ca845272861859463567)

static ALWAYS\_INLINE uint16\_t sys\_read16(mem\_addr\_t addr)

**Definition** sys\_io.h:43

[sys\_write8](arch_2arm_2cortex__a__r_2sys__io_8h.md#adf3b7a8a798d7497661d54d705a078fc)

static ALWAYS\_INLINE void sys\_write8(uint8\_t data, mem\_addr\_t addr)

**Definition** sys\_io.h:37

[sys\_read64](arch_2arm_2cortex__a__r_2sys__io_8h.md#ae20bb8c275dcc157c1be9b232d00ff9d)

static ALWAYS\_INLINE uint64\_t sys\_read64(mem\_addr\_t addr)

**Definition** sys\_io.h:75

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

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

[sys\_io.h](sys_2sys__io_8h.md)

[mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d)

uintptr\_t mem\_addr\_t

**Definition** sys\_io.h:21

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [common](dir_7cbd25c8850fe30be392200e83a608be.md)
- [sys\_io.h](arch_2common_2sys__io_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
