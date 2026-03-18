---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/emul__sensor_8h_source.html
original_path: doxygen/html/emul__sensor_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul\_sensor.h

[Go to the documentation of this file.](emul__sensor_8h.md)

1/\*

2 \* Copyright (c) 2023 Google LLC

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#include <[zephyr/drivers/emul.h](emul_8h.md)>

7#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

8#include <[zephyr/drivers/sensor\_attribute\_types.h](sensor__attribute__types_8h.md)>

9

10#include <[stdint.h](stdint_8h.md)>

11

18

24

28\_\_subsystem struct emul\_sensor\_backend\_api {

30 int (\*set\_channel)(const struct emul \*target, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*value,

31 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift);

33 int (\*get\_sample\_range)(const struct emul \*target, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*lower,

34 [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*upper, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*epsilon, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift);

36 int (\*set\_attribute)(const struct emul \*target, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch,

37 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute, const void \*value);

39 int (\*get\_attribute\_metadata)(const struct emul \*target, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch,

40 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*min, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*max,

41 [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*increment, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift);

42};

46

[ 54](group__sensor__emulator__backend.md#gadb7174783ab8466ab55aebb463fdfdd7)static inline bool [emul\_sensor\_backend\_is\_supported](group__sensor__emulator__backend.md#gadb7174783ab8466ab55aebb463fdfdd7)(const struct [emul](structemul.md) \*target)

55{

56 return target && target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

57}

58

[ 71](group__sensor__emulator__backend.md#ga53ecc5c20890546ee15b5ccf10945172)static inline int [emul\_sensor\_backend\_set\_channel](group__sensor__emulator__backend.md#ga53ecc5c20890546ee15b5ccf10945172)(const struct [emul](structemul.md) \*target, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch,

72 const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*value, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift)

73{

74 if (!target || !target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)) {

75 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

76 }

77

78 struct emul\_sensor\_backend\_api \*api = (struct emul\_sensor\_backend\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

79

80 if (api->set\_channel) {

81 return api->set\_channel(target, ch, value, shift);

82 }

83 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

84}

85

[ 103](group__sensor__emulator__backend.md#ga7662fbe6ebe090cacc4b1436975beeef)static inline int [emul\_sensor\_backend\_get\_sample\_range](group__sensor__emulator__backend.md#ga7662fbe6ebe090cacc4b1436975beeef)(const struct [emul](structemul.md) \*target,

104 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*lower,

105 [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*upper, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*epsilon, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift)

106{

107 if (!target || !target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)) {

108 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

109 }

110

111 struct emul\_sensor\_backend\_api \*api = (struct emul\_sensor\_backend\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

112

113 if (api->get\_sample\_range) {

114 return api->get\_sample\_range(target, ch, lower, upper, epsilon, shift);

115 }

116 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

117}

118

[ 129](group__sensor__emulator__backend.md#ga4011dd5d98c2ef63cdaccddd306c9d67)static inline int [emul\_sensor\_backend\_set\_attribute](group__sensor__emulator__backend.md#ga4011dd5d98c2ef63cdaccddd306c9d67)(const struct [emul](structemul.md) \*target,

130 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch,

131 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute,

132 const void \*value)

133{

134 if (!target || !target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)) {

135 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

136 }

137

138 struct emul\_sensor\_backend\_api \*api = (struct emul\_sensor\_backend\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

139

140 if (api->set\_attribute == NULL) {

141 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

142 }

143 return api->set\_attribute(target, ch, attribute, value);

144}

145

[ 163](group__sensor__emulator__backend.md#ga66aa2b47e79047a749b331265a66e215)static inline int [emul\_sensor\_backend\_get\_attribute\_metadata](group__sensor__emulator__backend.md#ga66aa2b47e79047a749b331265a66e215)(const struct [emul](structemul.md) \*target,

164 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) ch,

165 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute,

166 [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*min, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*max,

167 [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*increment, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift)

168{

169 if (!target || !target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)) {

170 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

171 }

172

173 struct emul\_sensor\_backend\_api \*api = (struct emul\_sensor\_backend\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

174

175 if (api->get\_attribute\_metadata == NULL) {

176 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

177 }

178 return api->get\_attribute\_metadata(target, ch, attribute, min, max, increment, shift);

179}

180

[emul.h](emul_8h.md)

[q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)

int32\_t q31\_t

32-bit fractional data type in 1.31 format.

**Definition** types.h:35

[emul\_sensor\_backend\_set\_attribute](group__sensor__emulator__backend.md#ga4011dd5d98c2ef63cdaccddd306c9d67)

static int emul\_sensor\_backend\_set\_attribute(const struct emul \*target, enum sensor\_channel ch, enum sensor\_attribute attribute, const void \*value)

Set the emulator's attribute values.

**Definition** emul\_sensor.h:129

[emul\_sensor\_backend\_set\_channel](group__sensor__emulator__backend.md#ga53ecc5c20890546ee15b5ccf10945172)

static int emul\_sensor\_backend\_set\_channel(const struct emul \*target, enum sensor\_channel ch, const q31\_t \*value, int8\_t shift)

Set an expected value for a given channel on a given sensor emulator.

**Definition** emul\_sensor.h:71

[emul\_sensor\_backend\_get\_attribute\_metadata](group__sensor__emulator__backend.md#ga66aa2b47e79047a749b331265a66e215)

static int emul\_sensor\_backend\_get\_attribute\_metadata(const struct emul \*target, enum sensor\_channel ch, enum sensor\_attribute attribute, q31\_t \*min, q31\_t \*max, q31\_t \*increment, int8\_t \*shift)

Get metadata about an attribute.

**Definition** emul\_sensor.h:163

[emul\_sensor\_backend\_get\_sample\_range](group__sensor__emulator__backend.md#ga7662fbe6ebe090cacc4b1436975beeef)

static int emul\_sensor\_backend\_get\_sample\_range(const struct emul \*target, enum sensor\_channel ch, q31\_t \*lower, q31\_t \*upper, q31\_t \*epsilon, int8\_t \*shift)

Query an emulator for a channel's supported sample value range and tolerance.

**Definition** emul\_sensor.h:103

[emul\_sensor\_backend\_is\_supported](group__sensor__emulator__backend.md#gadb7174783ab8466ab55aebb463fdfdd7)

static bool emul\_sensor\_backend\_is\_supported(const struct emul \*target)

Check if a given sensor emulator supports the backend API.

**Definition** emul\_sensor.h:54

[sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b)

sensor\_attribute

Sensor attribute types.

**Definition** sensor.h:290

[sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934)

sensor\_channel

Sensor channels.

**Definition** sensor.h:59

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[sensor\_attribute\_types.h](sensor__attribute__types_8h.md)

[stdint.h](stdint_8h.md)

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:78

[emul::backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)

const void \* backend\_api

Address of the API structure exposed by the emulator instance.

**Definition** emul.h:97

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul\_sensor.h](emul__sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
