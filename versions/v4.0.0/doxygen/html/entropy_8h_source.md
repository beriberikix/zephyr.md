---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/entropy_8h_source.html
original_path: doxygen/html/entropy_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

entropy.h

[Go to the documentation of this file.](entropy_8h.md)

1

6

7/\*

8 \* Copyright (c) 2016 ARM Ltd.

9 \* Copyright (c) 2017 Intel Corporation

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ENTROPY\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_ENTROPY\_H\_

15

24

25#include <[errno.h](errno_8h.md)>

26

27#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

28#include <[zephyr/device.h](device_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

[ 35](group__entropy__interface.md#gade7a19930b671f6924ee89f700bad2ef)#define ENTROPY\_BUSYWAIT BIT(0)

36

[ 46](group__entropy__interface.md#ga661150c9482777f98cdee794e9164b28)typedef int (\*[entropy\_get\_entropy\_t](group__entropy__interface.md#ga661150c9482777f98cdee794e9164b28))(const struct [device](structdevice.md) \*dev,

47 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

48 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

[ 55](group__entropy__interface.md#gacaa273da74b4727ea49b25d1ccd9725c)typedef int (\*[entropy\_get\_entropy\_isr\_t](group__entropy__interface.md#gacaa273da74b4727ea49b25d1ccd9725c))(const struct [device](structdevice.md) \*dev,

56 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

57 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length,

58 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

59

[ 65](structentropy__driver__api.md)\_\_subsystem struct [entropy\_driver\_api](structentropy__driver__api.md) {

[ 66](structentropy__driver__api.md#a3fd7758ed4c71ba1d64939297d06faa3) [entropy\_get\_entropy\_t](group__entropy__interface.md#ga661150c9482777f98cdee794e9164b28) [get\_entropy](structentropy__driver__api.md#a3fd7758ed4c71ba1d64939297d06faa3);

[ 67](structentropy__driver__api.md#ac0356f7fd4600377c6018414f056d766) [entropy\_get\_entropy\_isr\_t](group__entropy__interface.md#gacaa273da74b4727ea49b25d1ccd9725c) [get\_entropy\_isr](structentropy__driver__api.md#ac0356f7fd4600377c6018414f056d766);

68};

69

[ 80](group__entropy__interface.md#ga54de6cd85d5c557ca91f425944e50ce6)\_\_syscall int [entropy\_get\_entropy](group__entropy__interface.md#ga54de6cd85d5c557ca91f425944e50ce6)(const struct [device](structdevice.md) \*dev,

81 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

82 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

83

84static inline int z\_impl\_entropy\_get\_entropy(const struct [device](structdevice.md) \*dev,

85 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

86 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length)

87{

88 const struct [entropy\_driver\_api](structentropy__driver__api.md) \*api =

89 (const struct [entropy\_driver\_api](structentropy__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

90

91 \_\_ASSERT(api->get\_entropy != NULL,

92 "Callback pointer should not be NULL");

93 return api->get\_entropy(dev, buffer, length);

94}

95

[ 106](group__entropy__interface.md#ga71b99316bec395a7078b26e44f20fc9a)static inline int [entropy\_get\_entropy\_isr](group__entropy__interface.md#ga71b99316bec395a7078b26e44f20fc9a)(const struct [device](structdevice.md) \*dev,

107 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

108 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length,

109 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

110{

111 const struct [entropy\_driver\_api](structentropy__driver__api.md) \*api =

112 (const struct [entropy\_driver\_api](structentropy__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

113

114 if (unlikely(!api->[get\_entropy\_isr](structentropy__driver__api.md#ac0356f7fd4600377c6018414f056d766))) {

115 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

116 }

117

118 return api->[get\_entropy\_isr](structentropy__driver__api.md#ac0356f7fd4600377c6018414f056d766)(dev, buffer, length, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

119}

120

121

122#ifdef \_\_cplusplus

123}

124#endif

125

129

130#include <zephyr/syscalls/entropy.h>

131

132#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ENTROPY\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[entropy\_get\_entropy](group__entropy__interface.md#ga54de6cd85d5c557ca91f425944e50ce6)

int entropy\_get\_entropy(const struct device \*dev, uint8\_t \*buffer, uint16\_t length)

Fills a buffer with entropy.

[entropy\_get\_entropy\_t](group__entropy__interface.md#ga661150c9482777f98cdee794e9164b28)

int(\* entropy\_get\_entropy\_t)(const struct device \*dev, uint8\_t \*buffer, uint16\_t length)

Callback API to get entropy.

**Definition** entropy.h:46

[entropy\_get\_entropy\_isr](group__entropy__interface.md#ga71b99316bec395a7078b26e44f20fc9a)

static int entropy\_get\_entropy\_isr(const struct device \*dev, uint8\_t \*buffer, uint16\_t length, uint32\_t flags)

Fills a buffer with entropy in a non-blocking or busy-wait manner.

**Definition** entropy.h:106

[entropy\_get\_entropy\_isr\_t](group__entropy__interface.md#gacaa273da74b4727ea49b25d1ccd9725c)

int(\* entropy\_get\_entropy\_isr\_t)(const struct device \*dev, uint8\_t \*buffer, uint16\_t length, uint32\_t flags)

Callback API to get entropy from an ISR.

**Definition** entropy.h:55

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[entropy\_driver\_api](structentropy__driver__api.md)

Entropy driver API structure.

**Definition** entropy.h:65

[entropy\_driver\_api::get\_entropy](structentropy__driver__api.md#a3fd7758ed4c71ba1d64939297d06faa3)

entropy\_get\_entropy\_t get\_entropy

**Definition** entropy.h:66

[entropy\_driver\_api::get\_entropy\_isr](structentropy__driver__api.md#ac0356f7fd4600377c6018414f056d766)

entropy\_get\_entropy\_isr\_t get\_entropy\_isr

**Definition** entropy.h:67

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [entropy.h](entropy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
