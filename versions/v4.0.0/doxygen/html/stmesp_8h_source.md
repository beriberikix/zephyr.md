---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stmesp_8h_source.html
original_path: doxygen/html/stmesp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stmesp.h

[Go to the documentation of this file.](stmesp_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MISC\_CORESIGHT\_STMESP\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_MISC\_CORESIGHT\_STMESP\_H\_

9

10#include <[zephyr/devicetree.h](devicetree_8h.md)>

11

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

26typedef struct {

27 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) G\_DMTS[2];

28 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) G\_DM[2];

29 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) G\_DTS[2];

30 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) G\_D[2];

31 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) RESERVED0[16];

32 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) G\_FLAGTS[2];

33 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) G\_FLAG[2];

34 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) G\_TRIGTS[2];

35 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) G\_TRIG[2];

36 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) I\_DMTS[2];

37 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) I\_DM[2];

38 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) I\_DTS[2];

39 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) I\_D[2];

40 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) RESERVED1[16];

41 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) I\_FLAGTS[2];

42 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) I\_FLAG[2];

43 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) I\_TRIGTS[2];

44 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) I\_TRIG[2];

45} STMESP\_Type;

46

56static inline volatile void \*\_stmesp\_get\_data\_reg(STMESP\_Type \*reg, bool ts,

57 bool marked, bool guaranteed)

58{

59 if (ts) {

60 if (guaranteed) {

61 if (marked) {

62 return &reg->G\_DMTS[0];

63 } else {

64 return &reg->G\_DTS[0];

65 }

66 } else {

67 if (marked) {

68 return &reg->I\_DMTS[0];

69 } else {

70 return &reg->I\_DTS[0];

71 }

72 }

73 } else {

74 if (guaranteed) {

75 if (marked) {

76 return &reg->G\_DM[0];

77 } else {

78 return &reg->G\_D[0];

79 }

80 } else {

81 if (marked) {

82 return &reg->I\_DM[0];

83 } else {

84 return &reg->I\_D[0];

85 }

86 }

87 }

88}

89

91

[ 99](group__stmsp__interface.md#ga2ffcc08b7d5c32c90b5d24982c0f6349)static inline void [stmesp\_flag](group__stmsp__interface.md#ga2ffcc08b7d5c32c90b5d24982c0f6349)(STMESP\_Type \*reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, bool ts, bool guaranteed)

100{

101 if (ts) {

102 if (guaranteed) {

103 reg->G\_FLAGTS[0] = data;

104 } else {

105 reg->I\_FLAGTS[0] = data;

106 }

107 } else {

108 if (guaranteed) {

109 reg->G\_FLAG[0] = data;

110 } else {

111 reg->I\_FLAG[0] = data;

112 }

113 }

114}

115

[ 124](group__stmsp__interface.md#ga4af9486d77c93a55f221c7647d69a9f2)static inline void [stmesp\_data8](group__stmsp__interface.md#ga4af9486d77c93a55f221c7647d69a9f2)(STMESP\_Type \*reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, bool ts,

125 bool marked, bool guaranteed)

126{

127 \*(volatile [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)\_stmesp\_get\_data\_reg(reg, ts, marked, guaranteed) = data;

128}

129

[ 138](group__stmsp__interface.md#gaef1918a9d15d8da34fb5f2d7a11ff5fd)static inline void [stmesp\_data16](group__stmsp__interface.md#gaef1918a9d15d8da34fb5f2d7a11ff5fd)(STMESP\_Type \*reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, bool ts,

139 bool marked, bool guaranteed)

140{

141 \*(volatile [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*)\_stmesp\_get\_data\_reg(reg, ts, marked, guaranteed) = data;

142}

143

[ 152](group__stmsp__interface.md#gaa7885c5a7620e46a532dbf405bfc6034)static inline void [stmesp\_data32](group__stmsp__interface.md#gaa7885c5a7620e46a532dbf405bfc6034)(STMESP\_Type \*reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, bool ts,

153 bool marked, bool guaranteed)

154{

155 \*(volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)\_stmesp\_get\_data\_reg(reg, ts, marked, guaranteed) = data;

156}

157

[ 169](group__stmsp__interface.md#ga4350f5d201e3591221a932aa9fc3e94d)static inline int [stmesp\_get\_port](group__stmsp__interface.md#ga4350f5d201e3591221a932aa9fc3e94d)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx, STMESP\_Type \*\*port)

170

171{

172 /\* Check if index is within STM ports \*/

173 if ((port == NULL) ||

174 (idx >= ([DT\_REG\_SIZE](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(stmesp)) / sizeof(STMESP\_Type)))) {

175 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

176 }

177

178 STMESP\_Type \*const base = (STMESP\_Type \*const)[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(stmesp));

179

180 \*port = &base[idx];

181

182 return 0;

183}

184

185#ifdef \_\_cplusplus

186}

187#endif

188

192

193#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MISC\_CORESIGHT\_STMESP\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2433

[DT\_REG\_SIZE](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)

#define DT\_REG\_SIZE(node\_id)

Get a node's (only) register block size.

**Definition** devicetree.h:2454

[stmesp\_flag](group__stmsp__interface.md#ga2ffcc08b7d5c32c90b5d24982c0f6349)

static void stmesp\_flag(STMESP\_Type \*reg, uint32\_t data, bool ts, bool guaranteed)

Write flag to STMESP.

**Definition** stmesp.h:99

[stmesp\_get\_port](group__stmsp__interface.md#ga4350f5d201e3591221a932aa9fc3e94d)

static int stmesp\_get\_port(uint32\_t idx, STMESP\_Type \*\*port)

Return address of a STM extended stimulus port.

**Definition** stmesp.h:169

[stmesp\_data8](group__stmsp__interface.md#ga4af9486d77c93a55f221c7647d69a9f2)

static void stmesp\_data8(STMESP\_Type \*reg, uint8\_t data, bool ts, bool marked, bool guaranteed)

Write 8 bit data to STMESP.

**Definition** stmesp.h:124

[stmesp\_data32](group__stmsp__interface.md#gaa7885c5a7620e46a532dbf405bfc6034)

static void stmesp\_data32(STMESP\_Type \*reg, uint32\_t data, bool ts, bool marked, bool guaranteed)

Write 32 bit data to STMESP.

**Definition** stmesp.h:152

[stmesp\_data16](group__stmsp__interface.md#gaef1918a9d15d8da34fb5f2d7a11ff5fd)

static void stmesp\_data16(STMESP\_Type \*reg, uint16\_t data, bool ts, bool marked, bool guaranteed)

Write 16 bit data to STMESP.

**Definition** stmesp.h:138

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [coresight](dir_027ea40c83108e8cf62d53228a00b8a9.md)
- [stmesp.h](stmesp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
