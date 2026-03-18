---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/eeprom_8h_source.html
original_path: doxygen/html/eeprom_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eeprom.h

[Go to the documentation of this file.](eeprom_8h.md)

1/\*

2 \* Copyright (c) 2019 Vestas Wind Systems A/S

3 \*

4 \* Heavily based on drivers/flash.h which is:

5 \* Copyright (c) 2017 Nordic Semiconductor ASA

6 \* Copyright (c) 2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

15

16#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_EEPROM\_H\_

17#define ZEPHYR\_INCLUDE\_DRIVERS\_EEPROM\_H\_

18

27

28#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

29#include <stddef.h>

30#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

31#include <[zephyr/device.h](device_8h.md)>

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

42

47typedef int (\*eeprom\_api\_read)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

48 void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

49 size\_t len);

50

55typedef int (\*eeprom\_api\_write)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

56 const void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), size\_t len);

57

62typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) (\*eeprom\_api\_size)(const struct [device](structdevice.md) \*dev);

63

64\_\_subsystem struct eeprom\_driver\_api {

65 eeprom\_api\_read read;

66 eeprom\_api\_write write;

67 eeprom\_api\_size size;

68};

69

71

[ 82](group__eeprom__interface.md#ga92b92c8fb721f1b94038a20443d46e52)\_\_syscall int [eeprom\_read](group__eeprom__interface.md#ga92b92c8fb721f1b94038a20443d46e52)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data,

83 size\_t len);

84

85static inline int z\_impl\_eeprom\_read(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

86 void \*data, size\_t len)

87{

88 const struct eeprom\_driver\_api \*api =

89 (const struct eeprom\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

90

91 return api->read(dev, offset, data, len);

92}

93

[ 104](group__eeprom__interface.md#ga1973e8982de88f53e49154dc73461e56)\_\_syscall int [eeprom\_write](group__eeprom__interface.md#ga1973e8982de88f53e49154dc73461e56)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

105 const void \*data,

106 size\_t len);

107

108static inline int z\_impl\_eeprom\_write(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

109 const void \*data, size\_t len)

110{

111 const struct eeprom\_driver\_api \*api =

112 (const struct eeprom\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

113

114 return api->write(dev, offset, data, len);

115}

116

[ 124](group__eeprom__interface.md#ga27a1f50af8916f9291dad4a63796a707)\_\_syscall size\_t [eeprom\_get\_size](group__eeprom__interface.md#ga27a1f50af8916f9291dad4a63796a707)(const struct [device](structdevice.md) \*dev);

125

126static inline size\_t z\_impl\_eeprom\_get\_size(const struct [device](structdevice.md) \*dev)

127{

128 const struct eeprom\_driver\_api \*api =

129 (const struct eeprom\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

130

131 return api->size(dev);

132}

133

134#ifdef \_\_cplusplus

135}

136#endif

137

141

142#include <zephyr/syscalls/eeprom.h>

143

144#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_EEPROM\_H\_ \*/

[device.h](device_8h.md)

[eeprom\_write](group__eeprom__interface.md#ga1973e8982de88f53e49154dc73461e56)

int eeprom\_write(const struct device \*dev, off\_t offset, const void \*data, size\_t len)

Write data to EEPROM.

[eeprom\_get\_size](group__eeprom__interface.md#ga27a1f50af8916f9291dad4a63796a707)

size\_t eeprom\_get\_size(const struct device \*dev)

Get the size of the EEPROM in bytes.

[eeprom\_read](group__eeprom__interface.md#ga92b92c8fb721f1b94038a20443d46e52)

int eeprom\_read(const struct device \*dev, off\_t offset, void \*data, size\_t len)

Read data from EEPROM.

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)

Size of off\_t must be equal or less than size of size\_t

**Definition** retained\_mem.h:28

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [eeprom.h](eeprom_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
