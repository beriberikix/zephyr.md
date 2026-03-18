---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2mdio_8h_source.html
original_path: doxygen/html/drivers_2mdio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

76 return api->bus\_enable(dev);

77}

78

[ 85](group__mdio__interface.md#gaa7562449eab35b4e3fe14ebab94540bd)\_\_syscall void [mdio\_bus\_disable](group__mdio__interface.md#gaa7562449eab35b4e3fe14ebab94540bd)(const struct [device](structdevice.md) \*dev);

86

87static inline void z\_impl\_mdio\_bus\_disable(const struct [device](structdevice.md) \*dev)

88{

89 const struct mdio\_driver\_api \*api =

90 (const struct mdio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

91

92 return api->bus\_disable(dev);

93}

94

[ 111](group__mdio__interface.md#gae056ee61011eb6e8d68254680f918434)\_\_syscall int [mdio\_read](group__mdio__interface.md#gae056ee61011eb6e8d68254680f918434)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad,

112 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

113

114static inline int z\_impl\_mdio\_read(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

115 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data)

116{

117 const struct mdio\_driver\_api \*api =

118 (const struct mdio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

119

120 if (api->read == NULL) {

121 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

122 }

123

124 return api->read(dev, prtad, regad, data);

125}

126

127

[ 144](group__mdio__interface.md#ga6a18c3d67c6dc7ef1f3f0e3780015d48)\_\_syscall int [mdio\_write](group__mdio__interface.md#ga6a18c3d67c6dc7ef1f3f0e3780015d48)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad,

145 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

146

147static inline int z\_impl\_mdio\_write(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

148 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

149{

150 const struct mdio\_driver\_api \*api =

151 (const struct mdio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

152

153 if (api->write == NULL) {

154 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

155 }

156

157 return api->write(dev, prtad, regad, data);

158}

159

[ 177](group__mdio__interface.md#ga93e360a1201c2bb1ddd33b94e6fce619)\_\_syscall int [mdio\_read\_c45](group__mdio__interface.md#ga93e360a1201c2bb1ddd33b94e6fce619)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

178 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

179

180static inline int z\_impl\_mdio\_read\_c45(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

181 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad,

182 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data)

183{

184 const struct mdio\_driver\_api \*api =

185 (const struct mdio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

186

187 if (api->read\_c45 == NULL) {

188 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

189 }

190

191 return api->read\_c45(dev, prtad, devad, regad, data);

192}

193

[ 211](group__mdio__interface.md#gad8868e94f7335fea3cd9fea338ef9bd5)\_\_syscall int [mdio\_write\_c45](group__mdio__interface.md#gad8868e94f7335fea3cd9fea338ef9bd5)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

212 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

213

214static inline int z\_impl\_mdio\_write\_c45(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad,

215 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad,

216 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

217{

218 const struct mdio\_driver\_api \*api =

219 (const struct mdio\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

220

221 if (api->write\_c45 == NULL) {

222 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

223 }

224

225 return api->write\_c45(dev, prtad, devad, regad, data);

226}

227

228#ifdef \_\_cplusplus

229}

230#endif

231

235

236#include <syscalls/mdio.h>

237

238#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MDIO\_H\_ \*/

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

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mdio.h](drivers_2mdio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
