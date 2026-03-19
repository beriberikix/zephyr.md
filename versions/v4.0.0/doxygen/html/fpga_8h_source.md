---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fpga_8h_source.html
original_path: doxygen/html/fpga_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fpga.h

[Go to the documentation of this file.](fpga_8h.md)

[ 1](fpga_8h.md#a02d71e7a82f446220d67664d4cc7a5c9)/\*

2 \* Copyright (c) 2021 Antmicro <www.antmicro.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_FPGA\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_FPGA\_H\_

9

10#include <[errno.h](errno_8h.md)>

11

12#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

13#include <[zephyr/sys/util.h](sys_2util_8h.md)>

14#include <[zephyr/device.h](device_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

[ 20](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1e)enum [FPGA\_status](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1e) {

21 /\* Inactive is when the FPGA cannot accept the bitstream

22 \* and will not be programmed correctly

23 \*/

[ 24](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1ea46571663477ca2df50b24cf93a5e2441) [FPGA\_STATUS\_INACTIVE](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1ea46571663477ca2df50b24cf93a5e2441),

25 /\* Active is when the FPGA can accept the bitstream and

26 \* can be programmed correctly

27 \*/

[ 28](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1eac1b036277b07dfdef1dd1c3e1a299131) [FPGA\_STATUS\_ACTIVE](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1eac1b036277b07dfdef1dd1c3e1a299131)

29};

30

31typedef enum [FPGA\_status](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1e) (\*[fpga\_api\_get\_status](fpga_8h.md#a02d71e7a82f446220d67664d4cc7a5c9))(const struct [device](structdevice.md) \*dev);

[ 32](fpga_8h.md#a9860c64bbc2cfb89df9b51da655691b6)typedef int (\*[fpga\_api\_load](fpga_8h.md#a9860c64bbc2cfb89df9b51da655691b6))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*image\_ptr,

33 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) img\_size);

[ 34](fpga_8h.md#a3c53b90b9d0b50c44c01a534c61e9212)typedef int (\*[fpga\_api\_reset](fpga_8h.md#a3c53b90b9d0b50c44c01a534c61e9212))(const struct [device](structdevice.md) \*dev);

[ 35](fpga_8h.md#af3e8ea5d443fd09352e2b63f82a459be)typedef int (\*[fpga\_api\_on](fpga_8h.md#af3e8ea5d443fd09352e2b63f82a459be))(const struct [device](structdevice.md) \*dev);

[ 36](fpga_8h.md#a872a8d75bb46de50a41b56170804ed27)typedef int (\*[fpga\_api\_off](fpga_8h.md#a872a8d75bb46de50a41b56170804ed27))(const struct [device](structdevice.md) \*dev);

[ 37](fpga_8h.md#a24fd6ce4832b960b79914f42010774aa)typedef const char \*(\*fpga\_api\_get\_info)(const struct [device](structdevice.md) \*dev);

38

[ 39](structfpga__driver__api.md)\_\_subsystem struct [fpga\_driver\_api](structfpga__driver__api.md) {

[ 40](structfpga__driver__api.md#aee587fbff9464efc2ab64c6187346d28) [fpga\_api\_get\_status](fpga_8h.md#a02d71e7a82f446220d67664d4cc7a5c9) [get\_status](structfpga__driver__api.md#aee587fbff9464efc2ab64c6187346d28);

[ 41](structfpga__driver__api.md#ab3b316a07f35610b5bb00cd6c89fa0f1) [fpga\_api\_reset](fpga_8h.md#a3c53b90b9d0b50c44c01a534c61e9212) [reset](structfpga__driver__api.md#ab3b316a07f35610b5bb00cd6c89fa0f1);

[ 42](structfpga__driver__api.md#a1a56d32b7e1c9931b7ddca9f802baecc) [fpga\_api\_load](fpga_8h.md#a9860c64bbc2cfb89df9b51da655691b6) [load](structfpga__driver__api.md#a1a56d32b7e1c9931b7ddca9f802baecc);

[ 43](structfpga__driver__api.md#a0dedc3ce6e6ac23b9907af1ebbddaa56) [fpga\_api\_on](fpga_8h.md#af3e8ea5d443fd09352e2b63f82a459be) [on](structfpga__driver__api.md#a0dedc3ce6e6ac23b9907af1ebbddaa56);

[ 44](structfpga__driver__api.md#a89de57caf9882098e9c5f42f35bff2a3) [fpga\_api\_off](fpga_8h.md#a872a8d75bb46de50a41b56170804ed27) [off](structfpga__driver__api.md#a89de57caf9882098e9c5f42f35bff2a3);

[ 45](structfpga__driver__api.md#aa2107eb303cc2e538441ba1058630ab4) [fpga\_api\_get\_info](fpga_8h.md#a24fd6ce4832b960b79914f42010774aa) [get\_info](structfpga__driver__api.md#aa2107eb303cc2e538441ba1058630ab4);

46};

47

[ 56](fpga_8h.md#a1a1e78a46df9f4bd374cf5ecc2449360)static inline enum [FPGA\_status](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1e) [fpga\_get\_status](fpga_8h.md#a1a1e78a46df9f4bd374cf5ecc2449360)(const struct [device](structdevice.md) \*dev)

57{

58 const struct [fpga\_driver\_api](structfpga__driver__api.md) \*api =

59 (const struct [fpga\_driver\_api](structfpga__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

60

61 if (api->[get\_status](structfpga__driver__api.md#aee587fbff9464efc2ab64c6187346d28) == NULL) {

62 /\* assume it can never be reprogrammed if it

63 \* doesn't support the get\_status callback

64 \*/

65 return [FPGA\_STATUS\_INACTIVE](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1ea46571663477ca2df50b24cf93a5e2441);

66 }

67

68 return api->[get\_status](structfpga__driver__api.md#aee587fbff9464efc2ab64c6187346d28)(dev);

69}

70

[ 79](fpga_8h.md#adfc8d6c24cb1b1640393017a462011c9)static inline int [fpga\_reset](fpga_8h.md#adfc8d6c24cb1b1640393017a462011c9)(const struct [device](structdevice.md) \*dev)

80{

81 const struct [fpga\_driver\_api](structfpga__driver__api.md) \*api =

82 (const struct [fpga\_driver\_api](structfpga__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

83

84 if (api->[reset](structfpga__driver__api.md#ab3b316a07f35610b5bb00cd6c89fa0f1) == NULL) {

85 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

86 }

87

88 return api->[reset](structfpga__driver__api.md#ab3b316a07f35610b5bb00cd6c89fa0f1)(dev);

89}

90

[ 101](fpga_8h.md#a1cace6c7cc44705bf861d7aa5e863e16)static inline int [fpga\_load](fpga_8h.md#a1cace6c7cc44705bf861d7aa5e863e16)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*image\_ptr,

102 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) img\_size)

103{

104 const struct [fpga\_driver\_api](structfpga__driver__api.md) \*api =

105 (const struct [fpga\_driver\_api](structfpga__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

106

107 if (api->[load](structfpga__driver__api.md#a1a56d32b7e1c9931b7ddca9f802baecc) == NULL) {

108 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

109 }

110

111 return api->[load](structfpga__driver__api.md#a1a56d32b7e1c9931b7ddca9f802baecc)(dev, image\_ptr, img\_size);

112}

113

[ 122](fpga_8h.md#ad9093bd96c6a62cd958718d1e01e3f37)static inline int [fpga\_on](fpga_8h.md#ad9093bd96c6a62cd958718d1e01e3f37)(const struct [device](structdevice.md) \*dev)

123{

124 const struct [fpga\_driver\_api](structfpga__driver__api.md) \*api =

125 (const struct [fpga\_driver\_api](structfpga__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

126

127 if (api->[on](structfpga__driver__api.md#a0dedc3ce6e6ac23b9907af1ebbddaa56) == NULL) {

128 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

129 }

130

131 return api->[on](structfpga__driver__api.md#a0dedc3ce6e6ac23b9907af1ebbddaa56)(dev);

132}

133

[ 134](fpga_8h.md#ab41c04907be508f62e8df813d633b34b)#define FPGA\_GET\_INFO\_DEFAULT "n/a"

135

[ 143](fpga_8h.md#ab887999e8728bcc335a784afbdbbee8f)static inline const char \*[fpga\_get\_info](fpga_8h.md#ab887999e8728bcc335a784afbdbbee8f)(const struct [device](structdevice.md) \*dev)

144{

145 const struct [fpga\_driver\_api](structfpga__driver__api.md) \*api =

146 (const struct [fpga\_driver\_api](structfpga__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

147

148 if (api->[get\_info](structfpga__driver__api.md#aa2107eb303cc2e538441ba1058630ab4) == NULL) {

149 return [FPGA\_GET\_INFO\_DEFAULT](fpga_8h.md#ab41c04907be508f62e8df813d633b34b);

150 }

151

152 return api->[get\_info](structfpga__driver__api.md#aa2107eb303cc2e538441ba1058630ab4)(dev);

153}

154

[ 163](fpga_8h.md#aa161c7a7006db24793c1a1ecdea25b5c)static inline int [fpga\_off](fpga_8h.md#aa161c7a7006db24793c1a1ecdea25b5c)(const struct [device](structdevice.md) \*dev)

164{

165 const struct [fpga\_driver\_api](structfpga__driver__api.md) \*api =

166 (const struct [fpga\_driver\_api](structfpga__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

167

168 if (api->[off](structfpga__driver__api.md#a89de57caf9882098e9c5f42f35bff2a3) == NULL) {

169 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

170 }

171

172 return api->[off](structfpga__driver__api.md#a89de57caf9882098e9c5f42f35bff2a3)(dev);

173}

174

175#ifdef \_\_cplusplus

176}

177#endif

178

179#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_FPGA\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[fpga\_api\_get\_status](fpga_8h.md#a02d71e7a82f446220d67664d4cc7a5c9)

enum FPGA\_status(\* fpga\_api\_get\_status)(const struct device \*dev)

**Definition** fpga.h:31

[FPGA\_status](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1e)

FPGA\_status

**Definition** fpga.h:20

[FPGA\_STATUS\_INACTIVE](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1ea46571663477ca2df50b24cf93a5e2441)

@ FPGA\_STATUS\_INACTIVE

**Definition** fpga.h:24

[FPGA\_STATUS\_ACTIVE](fpga_8h.md#a0bbacdfdac79bace1786bb2a1627bb1eac1b036277b07dfdef1dd1c3e1a299131)

@ FPGA\_STATUS\_ACTIVE

**Definition** fpga.h:28

[fpga\_get\_status](fpga_8h.md#a1a1e78a46df9f4bd374cf5ecc2449360)

static enum FPGA\_status fpga\_get\_status(const struct device \*dev)

Read the status of FPGA.

**Definition** fpga.h:56

[fpga\_load](fpga_8h.md#a1cace6c7cc44705bf861d7aa5e863e16)

static int fpga\_load(const struct device \*dev, uint32\_t \*image\_ptr, uint32\_t img\_size)

Load the bitstream and program the FPGA.

**Definition** fpga.h:101

[fpga\_api\_get\_info](fpga_8h.md#a24fd6ce4832b960b79914f42010774aa)

const char \*(\* fpga\_api\_get\_info)(const struct device \*dev)

**Definition** fpga.h:37

[fpga\_api\_reset](fpga_8h.md#a3c53b90b9d0b50c44c01a534c61e9212)

int(\* fpga\_api\_reset)(const struct device \*dev)

**Definition** fpga.h:34

[fpga\_api\_off](fpga_8h.md#a872a8d75bb46de50a41b56170804ed27)

int(\* fpga\_api\_off)(const struct device \*dev)

**Definition** fpga.h:36

[fpga\_api\_load](fpga_8h.md#a9860c64bbc2cfb89df9b51da655691b6)

int(\* fpga\_api\_load)(const struct device \*dev, uint32\_t \*image\_ptr, uint32\_t img\_size)

**Definition** fpga.h:32

[fpga\_off](fpga_8h.md#aa161c7a7006db24793c1a1ecdea25b5c)

static int fpga\_off(const struct device \*dev)

Turns off the FPGA.

**Definition** fpga.h:163

[FPGA\_GET\_INFO\_DEFAULT](fpga_8h.md#ab41c04907be508f62e8df813d633b34b)

#define FPGA\_GET\_INFO\_DEFAULT

**Definition** fpga.h:134

[fpga\_get\_info](fpga_8h.md#ab887999e8728bcc335a784afbdbbee8f)

static const char \* fpga\_get\_info(const struct device \*dev)

Returns information about the FPGA.

**Definition** fpga.h:143

[fpga\_on](fpga_8h.md#ad9093bd96c6a62cd958718d1e01e3f37)

static int fpga\_on(const struct device \*dev)

Turns on the FPGA.

**Definition** fpga.h:122

[fpga\_reset](fpga_8h.md#adfc8d6c24cb1b1640393017a462011c9)

static int fpga\_reset(const struct device \*dev)

Reset the FPGA.

**Definition** fpga.h:79

[fpga\_api\_on](fpga_8h.md#af3e8ea5d443fd09352e2b63f82a459be)

int(\* fpga\_api\_on)(const struct device \*dev)

**Definition** fpga.h:35

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[fpga\_driver\_api](structfpga__driver__api.md)

**Definition** fpga.h:39

[fpga\_driver\_api::on](structfpga__driver__api.md#a0dedc3ce6e6ac23b9907af1ebbddaa56)

fpga\_api\_on on

**Definition** fpga.h:43

[fpga\_driver\_api::load](structfpga__driver__api.md#a1a56d32b7e1c9931b7ddca9f802baecc)

fpga\_api\_load load

**Definition** fpga.h:42

[fpga\_driver\_api::off](structfpga__driver__api.md#a89de57caf9882098e9c5f42f35bff2a3)

fpga\_api\_off off

**Definition** fpga.h:44

[fpga\_driver\_api::get\_info](structfpga__driver__api.md#aa2107eb303cc2e538441ba1058630ab4)

fpga\_api\_get\_info get\_info

**Definition** fpga.h:45

[fpga\_driver\_api::reset](structfpga__driver__api.md#ab3b316a07f35610b5bb00cd6c89fa0f1)

fpga\_api\_reset reset

**Definition** fpga.h:41

[fpga\_driver\_api::get\_status](structfpga__driver__api.md#aee587fbff9464efc2ab64c6187346d28)

fpga\_api\_get\_status get\_status

**Definition** fpga.h:40

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [fpga.h](fpga_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
