---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2mdio_8h_source.html
original_path: doxygen/html/drivers_2mdio_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mdio.h

[Go to the documentation of this file.](drivers_2mdio_8h.md)

1

6

7/\*

8 \* Copyright (c) 2021 IP-Logix Inc.

9 \* Copyright 2023 NXP

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MDIO\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_MDIO\_H\_

15

22#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

23#include <[zephyr/device.h](device_8h.md)>

24#include <[errno.h](errno_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

36\_\_subsystem struct mdio\_driver\_api {

38 void (\*bus\_enable)(const struct device \*dev);

39

41 void (\*bus\_disable)(const struct device \*dev);

42

44 int (\*read)(const struct device \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad,

45 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

46

48 int (\*write)(const struct device \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad,

49 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

50

52 int (\*read\_c45)(const struct device \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad,

53 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

54

56 int (\*write\_c45)(const struct device \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad,

57 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

58};

62

[ 69](group__mdio__interface.md#ga7918fa3747d966bd62fb51ceea244c43)\_\_syscall void [mdio\_bus\_enable](group__mdio__interface.md#ga7918fa3747d966bd62fb51ceea244c43)(const struct [device](structdevice.md) \*dev);

70

71static inline void z\_impl\_mdio\_bus\_enable(const struct [device](structdevice.md) \*dev)

72{

73 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->bus\_enable != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

74 [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->bus\_enable(dev);

75 }

76}

77

[ 84](group__mdio__interface.md#gaa7562449eab35b4e3fe14ebab94540bd)\_\_syscall void [mdio\_bus\_disable](group__mdio__interface.md#gaa7562449eab35b4e3fe14ebab94540bd)(const struct [device](structdevice.md) \*dev);

85

86static inline void z\_impl\_mdio\_bus\_disable(const struct [device](structdevice.md) \*dev)

87{

88 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->bus\_disable != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

89 [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->bus\_disable(dev);

90 }

91}

92

[ 109](group__mdio__interface.md#gae056ee61011eb6e8d68254680f918434)\_\_syscall int [mdio\_read](group__mdio__interface.md#gae056ee61011eb6e8d68254680f918434)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad,

110 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

111

112static inline int z\_impl\_mdio\_read(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

113 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e))

114{

115 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->read == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

116 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

117 }

118

119 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->read(dev, prtad, regad, [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

120}

121

122

[ 139](group__mdio__interface.md#ga6a18c3d67c6dc7ef1f3f0e3780015d48)\_\_syscall int [mdio\_write](group__mdio__interface.md#ga6a18c3d67c6dc7ef1f3f0e3780015d48)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad,

140 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

141

142static inline int z\_impl\_mdio\_write(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

143 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e))

144{

145 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->write == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

146 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

147 }

148

149 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->write(dev, prtad, regad, [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

150}

151

[ 169](group__mdio__interface.md#ga93e360a1201c2bb1ddd33b94e6fce619)\_\_syscall int [mdio\_read\_c45](group__mdio__interface.md#ga93e360a1201c2bb1ddd33b94e6fce619)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

170 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

171

172static inline int z\_impl\_mdio\_read\_c45(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

173 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad,

174 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e))

175{

176 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->read\_c45 == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

177 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

178 }

179

180 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->read\_c45(dev, prtad, devad, regad, [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

181}

182

[ 200](group__mdio__interface.md#gad8868e94f7335fea3cd9fea338ef9bd5)\_\_syscall int [mdio\_write\_c45](group__mdio__interface.md#gad8868e94f7335fea3cd9fea338ef9bd5)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

201 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

202

203static inline int z\_impl\_mdio\_write\_c45(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

204 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad,

205 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e))

206{

207 if ([DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->write\_c45 == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

208 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

209 }

210

211 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(mdio, dev)->write\_c45(dev, prtad, devad, regad, [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

212}

213

214#ifdef \_\_cplusplus

215}

216#endif

217

221

222#include <zephyr/syscalls/mdio.h>

223

224#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MDIO\_H\_ \*/

[device.h](device_8h.md)

[DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)

#define DEVICE\_API\_GET(\_class, \_dev)

Expands to the pointer of a device's API for a given class.

**Definition** device.h:1350

[errno.h](errno_8h.md)

System error numbers.

[mdio\_write](group__mdio__interface.md#ga6a18c3d67c6dc7ef1f3f0e3780015d48)

int mdio\_write(const struct device \*dev, uint8\_t prtad, uint8\_t regad, uint16\_t data)

Write to MDIO bus.

[mdio\_bus\_enable](group__mdio__interface.md#ga7918fa3747d966bd62fb51ceea244c43)

void mdio\_bus\_enable(const struct device \*dev)

Enable MDIO bus.

[mdio\_read\_c45](group__mdio__interface.md#ga93e360a1201c2bb1ddd33b94e6fce619)

int mdio\_read\_c45(const struct device \*dev, uint8\_t prtad, uint8\_t devad, uint16\_t regad, uint16\_t \*data)

Read from MDIO Bus using Clause 45 access.

[mdio\_bus\_disable](group__mdio__interface.md#gaa7562449eab35b4e3fe14ebab94540bd)

void mdio\_bus\_disable(const struct device \*dev)

Disable MDIO bus and tri-state drivers.

[mdio\_write\_c45](group__mdio__interface.md#gad8868e94f7335fea3cd9fea338ef9bd5)

int mdio\_write\_c45(const struct device \*dev, uint8\_t prtad, uint8\_t devad, uint16\_t regad, uint16\_t data)

Write to MDIO bus using Clause 45 access.

[mdio\_read](group__mdio__interface.md#gae056ee61011eb6e8d68254680f918434)

int mdio\_read(const struct device \*dev, uint8\_t prtad, uint8\_t regad, uint16\_t \*data)

Read from MDIO Bus.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:520

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mdio.h](drivers_2mdio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
