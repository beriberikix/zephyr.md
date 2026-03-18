---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sys-io-common_8h_source.html
original_path: doxygen/html/sys-io-common_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys-io-common.h

[Go to the documentation of this file.](sys-io-common_8h.md)

1/\*

2 \* Copyright (c) 2021 Synopsys.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_SYS\_IO\_COMMON\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_SYS\_IO\_COMMON\_H\_

9

10#ifndef \_ASMLANGUAGE

11

12#include <[zephyr/toolchain.h](toolchain_8h.md)>

13#include <[zephyr/sys/sys\_io.h](sys_2sys__io_8h.md)>

14#include <[zephyr/arch/arc/v2/aux\_regs.h](aux__regs_8h.md)>

15

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17#include <stddef.h>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 23](sys-io-common_8h.md#a51f9740fef1b1bb2abc93126ca2646ae)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_read8](sys-io-common_8h.md#a51f9740fef1b1bb2abc93126ca2646ae)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

24{

25 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value;

26

27 compiler\_barrier();

28 value = \*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)addr;

29 compiler\_barrier();

30

31 return value;

32}

33

[ 34](sys-io-common_8h.md#adf3b7a8a798d7497661d54d705a078fc)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write8](sys-io-common_8h.md#adf3b7a8a798d7497661d54d705a078fc)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

35{

36 compiler\_barrier();

37 \*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)addr = data;

38 compiler\_barrier();

39}

40

[ 41](sys-io-common_8h.md#ad8daa7da2671ca845272861859463567)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_read16](sys-io-common_8h.md#ad8daa7da2671ca845272861859463567)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

42{

43 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value;

44

45 compiler\_barrier();

46 value = \*(volatile [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*)addr;

47 compiler\_barrier();

48

49 return value;

50}

51

[ 52](sys-io-common_8h.md#a5cae8f8c0ea3749985e80f6ca85b1b13)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write16](sys-io-common_8h.md#a5cae8f8c0ea3749985e80f6ca85b1b13)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

53{

54 compiler\_barrier();

55 \*(volatile [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*)addr = data;

56 compiler\_barrier();

57}

58

[ 59](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

60{

61 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value;

62

63 compiler\_barrier();

64 value = \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr;

65 compiler\_barrier();

66

67 return value;

68}

69

[ 70](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr)

71{

72 compiler\_barrier();

73 \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)addr = data;

74 compiler\_barrier();

75}

76

77#ifdef \_\_cplusplus

78}

79#endif

80

81#endif /\* \_ASMLANGUAGE \*/

82

83#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_SYS\_IO\_COMMON\_H\_ \*/

[aux\_regs.h](aux__regs_8h.md)

ARCv2 auxiliary registers definitions.

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)

static ALWAYS\_INLINE void sys\_write32(uint32\_t data, mem\_addr\_t addr)

**Definition** sys-io-common.h:70

[sys\_read8](sys-io-common_8h.md#a51f9740fef1b1bb2abc93126ca2646ae)

static ALWAYS\_INLINE uint8\_t sys\_read8(mem\_addr\_t addr)

**Definition** sys-io-common.h:23

[sys\_write16](sys-io-common_8h.md#a5cae8f8c0ea3749985e80f6ca85b1b13)

static ALWAYS\_INLINE void sys\_write16(uint16\_t data, mem\_addr\_t addr)

**Definition** sys-io-common.h:52

[sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)

static ALWAYS\_INLINE uint32\_t sys\_read32(mem\_addr\_t addr)

**Definition** sys-io-common.h:59

[sys\_read16](sys-io-common_8h.md#ad8daa7da2671ca845272861859463567)

static ALWAYS\_INLINE uint16\_t sys\_read16(mem\_addr\_t addr)

**Definition** sys-io-common.h:41

[sys\_write8](sys-io-common_8h.md#adf3b7a8a798d7497661d54d705a078fc)

static ALWAYS\_INLINE void sys\_write8(uint8\_t data, mem\_addr\_t addr)

**Definition** sys-io-common.h:34

[sys\_io.h](sys_2sys__io_8h.md)

[mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d)

uintptr\_t mem\_addr\_t

**Definition** sys\_io.h:21

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [sys-io-common.h](sys-io-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
