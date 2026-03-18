---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/emul__sensor_8h_source.html
original_path: doxygen/html/emul__sensor_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

6#include <[zephyr/drivers/emul.h](drivers_2emul_8h.md)>

7#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

8#include <[zephyr/drivers/sensor\_attribute\_types.h](sensor__attribute__types_8h.md)>

9

10#include <[stdint.h](stdint_8h.md)>

11

18

24

28\_\_subsystem struct emul\_sensor\_driver\_api {

30 int (\*set\_channel)(const struct emul \*target, struct sensor\_chan\_spec ch,

31 const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*value, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift);

33 int (\*get\_sample\_range)(const struct emul \*target, struct sensor\_chan\_spec ch, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*lower,

34 [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*upper, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*epsilon, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift);

36 int (\*set\_attribute)(const struct emul \*target, struct sensor\_chan\_spec ch,

37 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute, const void \*value);

39 int (\*get\_attribute\_metadata)(const struct emul \*target, struct sensor\_chan\_spec ch,

40 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*min, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*max,

41 [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*increment, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift);

42};

46

[ 54](group__sensor__emulator__backend.md#gadb7174783ab8466ab55aebb463fdfdd7)static inline bool [emul\_sensor\_backend\_is\_supported](group__sensor__emulator__backend.md#gadb7174783ab8466ab55aebb463fdfdd7)(const struct [emul](structemul.md) \*target)

55{

56 return target && target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

57}

58

[ 71](group__sensor__emulator__backend.md#gadfa5c6618361bb382e5b44dc1a03f735)static inline int [emul\_sensor\_backend\_set\_channel](group__sensor__emulator__backend.md#gadfa5c6618361bb382e5b44dc1a03f735)(const struct [emul](structemul.md) \*target,

72 struct [sensor\_chan\_spec](structsensor__chan__spec.md) ch, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*value,

73 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift)

74{

75 if (!target || !target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)) {

76 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

77 }

78

79 struct emul\_sensor\_driver\_api \*api = (struct emul\_sensor\_driver\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

80

81 if (api->set\_channel) {

82 return api->set\_channel(target, ch, value, shift);

83 }

84 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

85}

86

[ 104](group__sensor__emulator__backend.md#ga271513cf5b2b5ee28d5f37e42449ee1e)static inline int [emul\_sensor\_backend\_get\_sample\_range](group__sensor__emulator__backend.md#ga271513cf5b2b5ee28d5f37e42449ee1e)(const struct [emul](structemul.md) \*target,

105 struct [sensor\_chan\_spec](structsensor__chan__spec.md) ch, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*lower,

106 [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*upper, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*epsilon, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift)

107{

108 if (!target || !target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)) {

109 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

110 }

111

112 struct emul\_sensor\_driver\_api \*api = (struct emul\_sensor\_driver\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

113

114 if (api->get\_sample\_range) {

115 return api->get\_sample\_range(target, ch, lower, upper, epsilon, shift);

116 }

117 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

118}

119

[ 130](group__sensor__emulator__backend.md#gaec1ddd02bc6ff1c66c83ca3f3af98fa8)static inline int [emul\_sensor\_backend\_set\_attribute](group__sensor__emulator__backend.md#gaec1ddd02bc6ff1c66c83ca3f3af98fa8)(const struct [emul](structemul.md) \*target,

131 struct [sensor\_chan\_spec](structsensor__chan__spec.md) ch,

132 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute,

133 const void \*value)

134{

135 if (!target || !target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)) {

136 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

137 }

138

139 struct emul\_sensor\_driver\_api \*api = (struct emul\_sensor\_driver\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

140

141 if (api->set\_attribute == NULL) {

142 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

143 }

144 return api->set\_attribute(target, ch, attribute, value);

145}

146

[ 164](group__sensor__emulator__backend.md#ga3bf83e34c2218823386489cf4f1cd84c)static inline int [emul\_sensor\_backend\_get\_attribute\_metadata](group__sensor__emulator__backend.md#ga3bf83e34c2218823386489cf4f1cd84c)(const struct [emul](structemul.md) \*target,

165 struct [sensor\_chan\_spec](structsensor__chan__spec.md) ch,

166 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attribute,

167 [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*min, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*max,

168 [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*increment, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*shift)

169{

170 if (!target || !target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)) {

171 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

172 }

173

174 struct emul\_sensor\_driver\_api \*api = (struct emul\_sensor\_driver\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

175

176 if (api->get\_attribute\_metadata == NULL) {

177 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

178 }

179 return api->get\_attribute\_metadata(target, ch, attribute, min, max, increment, shift);

180}

181

[emul.h](drivers_2emul_8h.md)

[q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)

int32\_t q31\_t

32-bit fractional data type in 1.31 format.

**Definition** types.h:35

[emul\_sensor\_backend\_get\_sample\_range](group__sensor__emulator__backend.md#ga271513cf5b2b5ee28d5f37e42449ee1e)

static int emul\_sensor\_backend\_get\_sample\_range(const struct emul \*target, struct sensor\_chan\_spec ch, q31\_t \*lower, q31\_t \*upper, q31\_t \*epsilon, int8\_t \*shift)

Query an emulator for a channel's supported sample value range and tolerance.

**Definition** emul\_sensor.h:104

[emul\_sensor\_backend\_get\_attribute\_metadata](group__sensor__emulator__backend.md#ga3bf83e34c2218823386489cf4f1cd84c)

static int emul\_sensor\_backend\_get\_attribute\_metadata(const struct emul \*target, struct sensor\_chan\_spec ch, enum sensor\_attribute attribute, q31\_t \*min, q31\_t \*max, q31\_t \*increment, int8\_t \*shift)

Get metadata about an attribute.

**Definition** emul\_sensor.h:164

[emul\_sensor\_backend\_is\_supported](group__sensor__emulator__backend.md#gadb7174783ab8466ab55aebb463fdfdd7)

static bool emul\_sensor\_backend\_is\_supported(const struct emul \*target)

Check if a given sensor emulator supports the backend API.

**Definition** emul\_sensor.h:54

[emul\_sensor\_backend\_set\_channel](group__sensor__emulator__backend.md#gadfa5c6618361bb382e5b44dc1a03f735)

static int emul\_sensor\_backend\_set\_channel(const struct emul \*target, struct sensor\_chan\_spec ch, const q31\_t \*value, int8\_t shift)

Set an expected value for a given channel on a given sensor emulator.

**Definition** emul\_sensor.h:71

[emul\_sensor\_backend\_set\_attribute](group__sensor__emulator__backend.md#gaec1ddd02bc6ff1c66c83ca3f3af98fa8)

static int emul\_sensor\_backend\_set\_attribute(const struct emul \*target, struct sensor\_chan\_spec ch, enum sensor\_attribute attribute, const void \*value)

Set the emulator's attribute values.

**Definition** emul\_sensor.h:130

[sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b)

sensor\_attribute

Sensor attribute types.

**Definition** sensor.h:296

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[sensor\_attribute\_types.h](sensor__attribute__types_8h.md)

[stdint.h](stdint_8h.md)

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:80

[emul::backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)

const void \* backend\_api

Address of the API structure exposed by the emulator instance.

**Definition** emul.h:100

[sensor\_chan\_spec](structsensor__chan__spec.md)

Sensor Channel Specification.

**Definition** sensor.h:431

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul\_sensor.h](emul__sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
