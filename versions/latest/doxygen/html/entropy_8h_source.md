---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/entropy_8h_source.html
original_path: doxygen/html/entropy_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

22

23#include <[errno.h](errno_8h.md)>

24

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/device.h](device_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 33](group__entropy__interface.md#gade7a19930b671f6924ee89f700bad2ef)#define ENTROPY\_BUSYWAIT BIT(0)

34

[ 44](group__entropy__interface.md#ga661150c9482777f98cdee794e9164b28)typedef int (\*[entropy\_get\_entropy\_t](group__entropy__interface.md#ga661150c9482777f98cdee794e9164b28))(const struct [device](structdevice.md) \*dev,

45 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

46 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

[ 53](group__entropy__interface.md#gacaa273da74b4727ea49b25d1ccd9725c)typedef int (\*[entropy\_get\_entropy\_isr\_t](group__entropy__interface.md#gacaa273da74b4727ea49b25d1ccd9725c))(const struct [device](structdevice.md) \*dev,

54 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

55 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length,

56 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

57

[ 63](structentropy__driver__api.md)\_\_subsystem struct [entropy\_driver\_api](structentropy__driver__api.md) {

[ 64](structentropy__driver__api.md#a3fd7758ed4c71ba1d64939297d06faa3) [entropy\_get\_entropy\_t](group__entropy__interface.md#ga661150c9482777f98cdee794e9164b28) [get\_entropy](structentropy__driver__api.md#a3fd7758ed4c71ba1d64939297d06faa3);

[ 65](structentropy__driver__api.md#ac0356f7fd4600377c6018414f056d766) [entropy\_get\_entropy\_isr\_t](group__entropy__interface.md#gacaa273da74b4727ea49b25d1ccd9725c) [get\_entropy\_isr](structentropy__driver__api.md#ac0356f7fd4600377c6018414f056d766);

66};

67

[ 78](group__entropy__interface.md#ga54de6cd85d5c557ca91f425944e50ce6)\_\_syscall int [entropy\_get\_entropy](group__entropy__interface.md#ga54de6cd85d5c557ca91f425944e50ce6)(const struct [device](structdevice.md) \*dev,

79 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

80 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length);

81

82static inline int z\_impl\_entropy\_get\_entropy(const struct [device](structdevice.md) \*dev,

83 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

84 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length)

85{

86 const struct [entropy\_driver\_api](structentropy__driver__api.md) \*api =

87 (const struct [entropy\_driver\_api](structentropy__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

88

89 \_\_ASSERT(api->get\_entropy != NULL,

90 "Callback pointer should not be NULL");

91 return api->get\_entropy(dev, buffer, length);

92}

93

[ 104](group__entropy__interface.md#ga71b99316bec395a7078b26e44f20fc9a)static inline int [entropy\_get\_entropy\_isr](group__entropy__interface.md#ga71b99316bec395a7078b26e44f20fc9a)(const struct [device](structdevice.md) \*dev,

105 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

106 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length,

107 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

108{

109 const struct [entropy\_driver\_api](structentropy__driver__api.md) \*api =

110 (const struct [entropy\_driver\_api](structentropy__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

111

112 if (unlikely(!api->[get\_entropy\_isr](structentropy__driver__api.md#ac0356f7fd4600377c6018414f056d766))) {

113 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

114 }

115

116 return api->[get\_entropy\_isr](structentropy__driver__api.md#ac0356f7fd4600377c6018414f056d766)(dev, buffer, length, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

117}

118

119

120#ifdef \_\_cplusplus

121}

122#endif

123

127

128#include <syscalls/entropy.h>

129

130#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ENTROPY\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[entropy\_get\_entropy](group__entropy__interface.md#ga54de6cd85d5c557ca91f425944e50ce6)

int entropy\_get\_entropy(const struct device \*dev, uint8\_t \*buffer, uint16\_t length)

Fills a buffer with entropy.

[entropy\_get\_entropy\_t](group__entropy__interface.md#ga661150c9482777f98cdee794e9164b28)

int(\* entropy\_get\_entropy\_t)(const struct device \*dev, uint8\_t \*buffer, uint16\_t length)

Callback API to get entropy.

**Definition** entropy.h:44

[entropy\_get\_entropy\_isr](group__entropy__interface.md#ga71b99316bec395a7078b26e44f20fc9a)

static int entropy\_get\_entropy\_isr(const struct device \*dev, uint8\_t \*buffer, uint16\_t length, uint32\_t flags)

Fills a buffer with entropy in a non-blocking or busy-wait manner.

**Definition** entropy.h:104

[entropy\_get\_entropy\_isr\_t](group__entropy__interface.md#gacaa273da74b4727ea49b25d1ccd9725c)

int(\* entropy\_get\_entropy\_isr\_t)(const struct device \*dev, uint8\_t \*buffer, uint16\_t length, uint32\_t flags)

Callback API to get entropy from an ISR.

**Definition** entropy.h:53

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

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

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[entropy\_driver\_api](structentropy__driver__api.md)

Entropy driver API structure.

**Definition** entropy.h:63

[entropy\_driver\_api::get\_entropy](structentropy__driver__api.md#a3fd7758ed4c71ba1d64939297d06faa3)

entropy\_get\_entropy\_t get\_entropy

**Definition** entropy.h:64

[entropy\_driver\_api::get\_entropy\_isr](structentropy__driver__api.md#ac0356f7fd4600377c6018414f056d766)

entropy\_get\_entropy\_isr\_t get\_entropy\_isr

**Definition** entropy.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [entropy.h](entropy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
