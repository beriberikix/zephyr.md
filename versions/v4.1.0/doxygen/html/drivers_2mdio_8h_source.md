---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2mdio_8h_source.html
original_path: doxygen/html/drivers_2mdio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

73 const struct mdio\_driver\_api \*api =

74 (const struct mdio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

75

76 if (api->bus\_enable != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

77 api->bus\_enable(dev);

78 }

79}

80

[ 87](group__mdio__interface.md#gaa7562449eab35b4e3fe14ebab94540bd)\_\_syscall void [mdio\_bus\_disable](group__mdio__interface.md#gaa7562449eab35b4e3fe14ebab94540bd)(const struct [device](structdevice.md) \*dev);

88

89static inline void z\_impl\_mdio\_bus\_disable(const struct [device](structdevice.md) \*dev)

90{

91 const struct mdio\_driver\_api \*api =

92 (const struct mdio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

93

94 if (api->bus\_disable != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

95 api->bus\_disable(dev);

96 }

97}

98

[ 115](group__mdio__interface.md#gae056ee61011eb6e8d68254680f918434)\_\_syscall int [mdio\_read](group__mdio__interface.md#gae056ee61011eb6e8d68254680f918434)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad,

116 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

117

118static inline int z\_impl\_mdio\_read(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

119 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data)

120{

121 const struct mdio\_driver\_api \*api =

122 (const struct mdio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

123

124 if (api->read == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

125 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

126 }

127

128 return api->read(dev, prtad, regad, data);

129}

130

131

[ 148](group__mdio__interface.md#ga6a18c3d67c6dc7ef1f3f0e3780015d48)\_\_syscall int [mdio\_write](group__mdio__interface.md#ga6a18c3d67c6dc7ef1f3f0e3780015d48)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad,

149 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

150

151static inline int z\_impl\_mdio\_write(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

152 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

153{

154 const struct mdio\_driver\_api \*api =

155 (const struct mdio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

156

157 if (api->write == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

158 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

159 }

160

161 return api->write(dev, prtad, regad, data);

162}

163

[ 181](group__mdio__interface.md#ga93e360a1201c2bb1ddd33b94e6fce619)\_\_syscall int [mdio\_read\_c45](group__mdio__interface.md#ga93e360a1201c2bb1ddd33b94e6fce619)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

182 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

183

184static inline int z\_impl\_mdio\_read\_c45(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

185 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad,

186 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data)

187{

188 const struct mdio\_driver\_api \*api =

189 (const struct mdio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

190

191 if (api->read\_c45 == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

192 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

193 }

194

195 return api->read\_c45(dev, prtad, devad, regad, data);

196}

197

[ 215](group__mdio__interface.md#gad8868e94f7335fea3cd9fea338ef9bd5)\_\_syscall int [mdio\_write\_c45](group__mdio__interface.md#gad8868e94f7335fea3cd9fea338ef9bd5)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

216 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

217

218static inline int z\_impl\_mdio\_write\_c45(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

219 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad,

220 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

221{

222 const struct mdio\_driver\_api \*api =

223 (const struct mdio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

224

225 if (api->write\_c45 == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

226 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

227 }

228

229 return api->write\_c45(dev, prtad, devad, regad, data);

230}

231

232#ifdef \_\_cplusplus

233}

234#endif

235

239

240#include <zephyr/syscalls/mdio.h>

241

242#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MDIO\_H\_ \*/

[device.h](device_8h.md)

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

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mdio.h](drivers_2mdio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
