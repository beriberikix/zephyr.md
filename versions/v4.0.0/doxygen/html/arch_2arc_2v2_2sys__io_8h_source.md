---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2arc_2v2_2sys__io_8h_source.html
original_path: doxygen/html/arch_2arc_2v2_2sys__io_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_io.h

[Go to the documentation of this file.](arch_2arc_2v2_2sys__io_8h.md)

1/\*

2 \* Copyright (c) 2015 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_SYS\_IO\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_SYS\_IO\_H\_

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

23/\* Implementation of sys\_io.h's documented functions \*/

24

25static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 26](arch_2arc_2v2_2sys__io_8h.md#a4eb1822b6af401aef41646d01f900733) void [sys\_out8](arch_2arc_2v2_2sys__io_8h.md#a4eb1822b6af401aef41646d01f900733)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

27{

28 z\_arc\_v2\_aux\_reg\_write(port, data);

29}

30

31static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 32](arch_2arc_2v2_2sys__io_8h.md#a38e2ce31ef09cb5d903da6f0fbd7b174) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_in8](arch_2arc_2v2_2sys__io_8h.md#a38e2ce31ef09cb5d903da6f0fbd7b174)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

33{

34 return ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))(z\_arc\_v2\_aux\_reg\_read(port) & 0x000000ff);

35}

36

37static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 38](arch_2arc_2v2_2sys__io_8h.md#a8700f40b9c9951083b9a729b7e50f47d) void [sys\_out16](arch_2arc_2v2_2sys__io_8h.md#a8700f40b9c9951083b9a729b7e50f47d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

39{

40 z\_arc\_v2\_aux\_reg\_write(port, data);

41}

42

43static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 44](arch_2arc_2v2_2sys__io_8h.md#ab9823ccf71d78cbb0316e9c335081f6d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_in16](arch_2arc_2v2_2sys__io_8h.md#ab9823ccf71d78cbb0316e9c335081f6d)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

45{

46 return ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))(z\_arc\_v2\_aux\_reg\_read(port) & 0x0000ffff);

47}

48

49static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 50](arch_2arc_2v2_2sys__io_8h.md#ae60822b265f38b57b70a2925996aaa88) void [sys\_out32](arch_2arc_2v2_2sys__io_8h.md#ae60822b265f38b57b70a2925996aaa88)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

51{

52 z\_arc\_v2\_aux\_reg\_write(port, data);

53}

54

55static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 56](arch_2arc_2v2_2sys__io_8h.md#af89948c04bd432f5fa14319f29d06968) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_in32](arch_2arc_2v2_2sys__io_8h.md#af89948c04bd432f5fa14319f29d06968)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port)

57{

58 return z\_arc\_v2\_aux\_reg\_read(port);

59}

60

61static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 62](arch_2arc_2v2_2sys__io_8h.md#ab74f07a31f01e5866d397e91b012abf7) void [sys\_io\_set\_bit](arch_2arc_2v2_2sys__io_8h.md#ab74f07a31f01e5866d397e91b012abf7)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, unsigned int bit)

63{

64 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg = 0;

65

66 \_\_asm\_\_ volatile("lr %1, [%0]\n"

67 "bset %1, %1, %2\n"

68 "sr %1, [%0];\n\t"

69 :

70 : "ir" (port),

71 "r" (reg), "ir" (bit)

72 : "memory", "cc");

73}

74

75static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 76](arch_2arc_2v2_2sys__io_8h.md#a6a6ece8db6858d64378c6cce47a64238) void [sys\_io\_clear\_bit](arch_2arc_2v2_2sys__io_8h.md#a6a6ece8db6858d64378c6cce47a64238)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, unsigned int bit)

77{

78 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg = 0;

79

80 \_\_asm\_\_ volatile("lr %1, [%0]\n"

81 "bclr %1, %1, %2\n"

82 "sr %1, [%0];\n\t"

83 :

84 : "ir" (port),

85 "r" (reg), "ir" (bit)

86 : "memory", "cc");

87}

88

89static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 90](arch_2arc_2v2_2sys__io_8h.md#a1593f7afecfc05001fc47d1d75ee895d) int [sys\_io\_test\_bit](arch_2arc_2v2_2sys__io_8h.md#a1593f7afecfc05001fc47d1d75ee895d)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, unsigned int bit)

91{

92 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status = \_ARC\_V2\_STATUS32;

93 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg = 0;

94 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

95

96 \_\_asm\_\_ volatile("lr %2, [%1]\n"

97 "btst %2, %3\n"

98 "lr %0, [%4];\n\t"

99 : "=r" (ret)

100 : "ir" (port),

101 "r" (reg), "ir" (bit), "i" (status)

102 : "memory", "cc");

103

104 return !(ret & \_ARC\_V2\_STATUS32\_Z);

105}

106

107static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 108](arch_2arc_2v2_2sys__io_8h.md#a070e38b330fc6402de5aae6192abd41b) int [sys\_io\_test\_and\_set\_bit](arch_2arc_2v2_2sys__io_8h.md#a070e38b330fc6402de5aae6192abd41b)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, unsigned int bit)

109{

110 int ret;

111

112 ret = [sys\_io\_test\_bit](arch_2arc_2v2_2sys__io_8h.md#a1593f7afecfc05001fc47d1d75ee895d)(port, bit);

113 [sys\_io\_set\_bit](arch_2arc_2v2_2sys__io_8h.md#ab74f07a31f01e5866d397e91b012abf7)(port, bit);

114

115 return ret;

116}

117

118static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

[ 119](arch_2arc_2v2_2sys__io_8h.md#a41953bee114b3317cd7bcdfbad4738b9) int [sys\_io\_test\_and\_clear\_bit](arch_2arc_2v2_2sys__io_8h.md#a41953bee114b3317cd7bcdfbad4738b9)([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port, unsigned int bit)

120{

121 int ret;

122

123 ret = [sys\_io\_test\_bit](arch_2arc_2v2_2sys__io_8h.md#a1593f7afecfc05001fc47d1d75ee895d)(port, bit);

124 [sys\_io\_clear\_bit](arch_2arc_2v2_2sys__io_8h.md#a6a6ece8db6858d64378c6cce47a64238)(port, bit);

125

126 return ret;

127}

128

129#ifdef \_\_cplusplus

130}

131#endif

132

133#endif /\* \_ASMLANGUAGE \*/

134

135#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_SYS\_IO\_H\_ \*/

[sys\_io\_test\_and\_set\_bit](arch_2arc_2v2_2sys__io_8h.md#a070e38b330fc6402de5aae6192abd41b)

static ALWAYS\_INLINE int sys\_io\_test\_and\_set\_bit(io\_port\_t port, unsigned int bit)

**Definition** sys\_io.h:108

[sys\_io\_test\_bit](arch_2arc_2v2_2sys__io_8h.md#a1593f7afecfc05001fc47d1d75ee895d)

static ALWAYS\_INLINE int sys\_io\_test\_bit(io\_port\_t port, unsigned int bit)

**Definition** sys\_io.h:90

[sys\_in8](arch_2arc_2v2_2sys__io_8h.md#a38e2ce31ef09cb5d903da6f0fbd7b174)

static ALWAYS\_INLINE uint8\_t sys\_in8(io\_port\_t port)

**Definition** sys\_io.h:32

[sys\_io\_test\_and\_clear\_bit](arch_2arc_2v2_2sys__io_8h.md#a41953bee114b3317cd7bcdfbad4738b9)

static ALWAYS\_INLINE int sys\_io\_test\_and\_clear\_bit(io\_port\_t port, unsigned int bit)

**Definition** sys\_io.h:119

[sys\_out8](arch_2arc_2v2_2sys__io_8h.md#a4eb1822b6af401aef41646d01f900733)

static ALWAYS\_INLINE void sys\_out8(uint8\_t data, io\_port\_t port)

**Definition** sys\_io.h:26

[sys\_io\_clear\_bit](arch_2arc_2v2_2sys__io_8h.md#a6a6ece8db6858d64378c6cce47a64238)

static ALWAYS\_INLINE void sys\_io\_clear\_bit(io\_port\_t port, unsigned int bit)

**Definition** sys\_io.h:76

[sys\_out16](arch_2arc_2v2_2sys__io_8h.md#a8700f40b9c9951083b9a729b7e50f47d)

static ALWAYS\_INLINE void sys\_out16(uint16\_t data, io\_port\_t port)

**Definition** sys\_io.h:38

[sys\_io\_set\_bit](arch_2arc_2v2_2sys__io_8h.md#ab74f07a31f01e5866d397e91b012abf7)

static ALWAYS\_INLINE void sys\_io\_set\_bit(io\_port\_t port, unsigned int bit)

**Definition** sys\_io.h:62

[sys\_in16](arch_2arc_2v2_2sys__io_8h.md#ab9823ccf71d78cbb0316e9c335081f6d)

static ALWAYS\_INLINE uint16\_t sys\_in16(io\_port\_t port)

**Definition** sys\_io.h:44

[sys\_out32](arch_2arc_2v2_2sys__io_8h.md#ae60822b265f38b57b70a2925996aaa88)

static ALWAYS\_INLINE void sys\_out32(uint32\_t data, io\_port\_t port)

**Definition** sys\_io.h:50

[sys\_in32](arch_2arc_2v2_2sys__io_8h.md#af89948c04bd432f5fa14319f29d06968)

static ALWAYS\_INLINE uint32\_t sys\_in32(io\_port\_t port)

**Definition** sys\_io.h:56

[aux\_regs.h](aux__regs_8h.md)

ARCv2 auxiliary registers definitions.

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

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

[sys\_io.h](sys_2sys__io_8h.md)

[io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86)

uint32\_t io\_port\_t

**Definition** sys\_io.h:19

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [sys\_io.h](arch_2arc_2v2_2sys__io_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
