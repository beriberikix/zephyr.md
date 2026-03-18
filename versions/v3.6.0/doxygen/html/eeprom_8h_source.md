---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/eeprom_8h_source.html
original_path: doxygen/html/eeprom_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <stddef.h>

28#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

29#include <[zephyr/device.h](device_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

40

45typedef int (\*eeprom\_api\_read)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

46 void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

47 size\_t len);

48

53typedef int (\*eeprom\_api\_write)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

54 const void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), size\_t len);

55

60typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) (\*eeprom\_api\_size)(const struct [device](structdevice.md) \*dev);

61

62\_\_subsystem struct eeprom\_driver\_api {

63 eeprom\_api\_read read;

64 eeprom\_api\_write write;

65 eeprom\_api\_size size;

66};

67

69

[ 80](group__eeprom__interface.md#ga92b92c8fb721f1b94038a20443d46e52)\_\_syscall int [eeprom\_read](group__eeprom__interface.md#ga92b92c8fb721f1b94038a20443d46e52)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data,

81 size\_t len);

82

83static inline int z\_impl\_eeprom\_read(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

84 void \*data, size\_t len)

85{

86 const struct eeprom\_driver\_api \*api =

87 (const struct eeprom\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

88

89 return api->read(dev, offset, data, len);

90}

91

[ 102](group__eeprom__interface.md#ga1973e8982de88f53e49154dc73461e56)\_\_syscall int [eeprom\_write](group__eeprom__interface.md#ga1973e8982de88f53e49154dc73461e56)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

103 const void \*data,

104 size\_t len);

105

106static inline int z\_impl\_eeprom\_write(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

107 const void \*data, size\_t len)

108{

109 const struct eeprom\_driver\_api \*api =

110 (const struct eeprom\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

111

112 return api->write(dev, offset, data, len);

113}

114

[ 122](group__eeprom__interface.md#ga27a1f50af8916f9291dad4a63796a707)\_\_syscall size\_t [eeprom\_get\_size](group__eeprom__interface.md#ga27a1f50af8916f9291dad4a63796a707)(const struct [device](structdevice.md) \*dev);

123

124static inline size\_t z\_impl\_eeprom\_get\_size(const struct [device](structdevice.md) \*dev)

125{

126 const struct eeprom\_driver\_api \*api =

127 (const struct eeprom\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

128

129 return api->size(dev);

130}

131

132#ifdef \_\_cplusplus

133}

134#endif

135

139

140#include <syscalls/eeprom.h>

141

142#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_EEPROM\_H\_ \*/

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

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [eeprom.h](eeprom_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
