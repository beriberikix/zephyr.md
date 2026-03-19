---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/retained__mem_8h_source.html
original_path: doxygen/html/retained__mem_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

retained\_mem.h

[Go to the documentation of this file.](retained__mem_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_RETAINED\_MEM\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_RETAINED\_MEM\_

14

15#include <[stdint.h](stdint_8h.md)>

16#include <stddef.h>

17#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

18#include <[zephyr/kernel.h](kernel_8h.md)>

19#include <[zephyr/device.h](device_8h.md)>

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21#include <[zephyr/sys/math\_extras.h](math__extras_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27BUILD\_ASSERT(!(sizeof([off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)) > sizeof(size\_t)),

[ 28](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) "Size of off\_t must be equal or less than size of size\_t");

29

38

[ 44](group__retained__mem__interface.md#ga684490184eedc8d3f56b25d7b6e50a06)typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[retained\_mem\_size\_api](group__retained__mem__interface.md#ga684490184eedc8d3f56b25d7b6e50a06))(const struct [device](structdevice.md) \*dev);

45

[ 51](group__retained__mem__interface.md#ga3831f3ec0e0de7957cc6ce7da0cfbe58)typedef int (\*[retained\_mem\_read\_api](group__retained__mem__interface.md#ga3831f3ec0e0de7957cc6ce7da0cfbe58))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

52 size\_t size);

53

[ 59](group__retained__mem__interface.md#gaf6e43d230b1a606e90f3a236aeff1909)typedef int (\*[retained\_mem\_write\_api](group__retained__mem__interface.md#gaf6e43d230b1a606e90f3a236aeff1909))(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

60 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t size);

61

[ 67](group__retained__mem__interface.md#ga3fde220eceb8a45a7a42cfbb1930e27d)typedef int (\*[retained\_mem\_clear\_api](group__retained__mem__interface.md#ga3fde220eceb8a45a7a42cfbb1930e27d))(const struct [device](structdevice.md) \*dev);

68

[ 80](structretained__mem__driver__api.md)\_\_subsystem struct [retained\_mem\_driver\_api](structretained__mem__driver__api.md) {

[ 81](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619) [retained\_mem\_size\_api](group__retained__mem__interface.md#ga684490184eedc8d3f56b25d7b6e50a06) [size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619);

[ 82](structretained__mem__driver__api.md#ab68d1cdb15b79ac8d728a94305862c00) [retained\_mem\_read\_api](group__retained__mem__interface.md#ga3831f3ec0e0de7957cc6ce7da0cfbe58) [read](structretained__mem__driver__api.md#ab68d1cdb15b79ac8d728a94305862c00);

[ 83](structretained__mem__driver__api.md#abb3941c6c6465dfbc9a5f97163937526) [retained\_mem\_write\_api](group__retained__mem__interface.md#gaf6e43d230b1a606e90f3a236aeff1909) [write](structretained__mem__driver__api.md#abb3941c6c6465dfbc9a5f97163937526);

[ 84](structretained__mem__driver__api.md#ab0633d684826efcc6ace2f3d9427b406) [retained\_mem\_clear\_api](group__retained__mem__interface.md#ga3fde220eceb8a45a7a42cfbb1930e27d) [clear](structretained__mem__driver__api.md#ab0633d684826efcc6ace2f3d9427b406);

85};

86

[ 95](group__retained__mem__interface.md#gaa0b4b6db4c96054a709f803880f3091a)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [retained\_mem\_size](group__retained__mem__interface.md#gaa0b4b6db4c96054a709f803880f3091a)(const struct [device](structdevice.md) \*dev);

96

97static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) z\_impl\_retained\_mem\_size(const struct [device](structdevice.md) \*dev)

98{

99 struct [retained\_mem\_driver\_api](structretained__mem__driver__api.md) \*api = (struct [retained\_mem\_driver\_api](structretained__mem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

100

101 return api->size(dev);

102}

103

[ 114](group__retained__mem__interface.md#ga47fba21400c1f7019e7bd0e8f10662b3)\_\_syscall int [retained\_mem\_read](group__retained__mem__interface.md#ga47fba21400c1f7019e7bd0e8f10662b3)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

115 size\_t [size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619));

116

117static inline int z\_impl\_retained\_mem\_read(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

118 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t [size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619))

119{

120 struct [retained\_mem\_driver\_api](structretained__mem__driver__api.md) \*api = (struct [retained\_mem\_driver\_api](structretained__mem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

121 size\_t area\_size;

122

123 /\* Validate user-supplied parameters \*/

124 if ([size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619) == 0) {

125 return 0;

126 }

127

128 area\_size = api->size(dev);

129

130 if (offset < 0 || size > area\_size || (area\_size - [size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619)) < (size\_t)offset) {

131 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

132 }

133

134 return api->read(dev, offset, buffer, [size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619));

135}

136

[ 148](group__retained__mem__interface.md#ga1976ac945eb7c09b8dd6121926af0c6a)\_\_syscall int [retained\_mem\_write](group__retained__mem__interface.md#ga1976ac945eb7c09b8dd6121926af0c6a)(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

149 size\_t [size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619));

150

151static inline int z\_impl\_retained\_mem\_write(const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset,

152 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t [size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619))

153{

154 struct [retained\_mem\_driver\_api](structretained__mem__driver__api.md) \*api = (struct [retained\_mem\_driver\_api](structretained__mem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

155 size\_t area\_size;

156

157 /\* Validate user-supplied parameters \*/

158 if ([size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619) == 0) {

159 return 0;

160 }

161

162 area\_size = api->size(dev);

163

164 if (offset < 0 || size > area\_size || (area\_size - [size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619)) < (size\_t)offset) {

165 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

166 }

167

168 return api->write(dev, offset, buffer, [size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619));

169}

170

[ 178](group__retained__mem__interface.md#ga5962d863c21cd91e259bf47abf2154d7)\_\_syscall int [retained\_mem\_clear](group__retained__mem__interface.md#ga5962d863c21cd91e259bf47abf2154d7)(const struct [device](structdevice.md) \*dev);

179

180static inline int z\_impl\_retained\_mem\_clear(const struct [device](structdevice.md) \*dev)

181{

182 struct [retained\_mem\_driver\_api](structretained__mem__driver__api.md) \*api = (struct [retained\_mem\_driver\_api](structretained__mem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

183

184 return api->clear(dev);

185}

186

190

191#ifdef \_\_cplusplus

192}

193#endif

194

195#include <zephyr/syscalls/retained\_mem.h>

196

197#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RETAINED\_MEM\_ \*/

[device.h](device_8h.md)

[retained\_mem\_write](group__retained__mem__interface.md#ga1976ac945eb7c09b8dd6121926af0c6a)

int retained\_mem\_write(const struct device \*dev, off\_t offset, const uint8\_t \*buffer, size\_t size)

Writes data to the Retained memory area - underlying data does not need to be cleared prior to writin...

[retained\_mem\_read\_api](group__retained__mem__interface.md#ga3831f3ec0e0de7957cc6ce7da0cfbe58)

int(\* retained\_mem\_read\_api)(const struct device \*dev, off\_t offset, uint8\_t \*buffer, size\_t size)

Callback API to read from retained memory area.

**Definition** retained\_mem.h:51

[retained\_mem\_clear\_api](group__retained__mem__interface.md#ga3fde220eceb8a45a7a42cfbb1930e27d)

int(\* retained\_mem\_clear\_api)(const struct device \*dev)

Callback API to clear retained memory area (reset all data to 0x00).

**Definition** retained\_mem.h:67

[retained\_mem\_read](group__retained__mem__interface.md#ga47fba21400c1f7019e7bd0e8f10662b3)

int retained\_mem\_read(const struct device \*dev, off\_t offset, uint8\_t \*buffer, size\_t size)

Reads data from the Retained memory area.

[retained\_mem\_clear](group__retained__mem__interface.md#ga5962d863c21cd91e259bf47abf2154d7)

int retained\_mem\_clear(const struct device \*dev)

Clears data in the retained memory area by setting it to 0x00.

[retained\_mem\_size\_api](group__retained__mem__interface.md#ga684490184eedc8d3f56b25d7b6e50a06)

ssize\_t(\* retained\_mem\_size\_api)(const struct device \*dev)

Callback API to get size of retained memory area.

**Definition** retained\_mem.h:44

[retained\_mem\_size](group__retained__mem__interface.md#gaa0b4b6db4c96054a709f803880f3091a)

ssize\_t retained\_mem\_size(const struct device \*dev)

Returns the size of the retained memory area.

[retained\_mem\_write\_api](group__retained__mem__interface.md#gaf6e43d230b1a606e90f3a236aeff1909)

int(\* retained\_mem\_write\_api)(const struct device \*dev, off\_t offset, const uint8\_t \*buffer, size\_t size)

Callback API to write to retained memory area.

**Definition** retained\_mem.h:59

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[math\_extras.h](math__extras_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[retained\_mem\_driver\_api](structretained__mem__driver__api.md)

Retained memory driver API API which can be used by a device to store data in a retained memory area.

**Definition** retained\_mem.h:80

[retained\_mem\_driver\_api::size](structretained__mem__driver__api.md#a3743bda91f8700d9ae9cd06fd6780619)

retained\_mem\_size\_api size

**Definition** retained\_mem.h:81

[retained\_mem\_driver\_api::clear](structretained__mem__driver__api.md#ab0633d684826efcc6ace2f3d9427b406)

retained\_mem\_clear\_api clear

**Definition** retained\_mem.h:84

[retained\_mem\_driver\_api::read](structretained__mem__driver__api.md#ab68d1cdb15b79ac8d728a94305862c00)

retained\_mem\_read\_api read

**Definition** retained\_mem.h:82

[retained\_mem\_driver\_api::write](structretained__mem__driver__api.md#abb3941c6c6465dfbc9a5f97163937526)

retained\_mem\_write\_api write

**Definition** retained\_mem.h:83

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [retained\_mem.h](retained__mem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
