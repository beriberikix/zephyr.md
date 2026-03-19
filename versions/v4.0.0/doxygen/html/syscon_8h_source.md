---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/syscon_8h_source.html
original_path: doxygen/html/syscon_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

syscon.h

[Go to the documentation of this file.](syscon_8h.md)

1/\*

2 \* Copyright (c) 2021 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SYSCON\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_SYSCON\_H\_

14

21

22#include <[errno.h](errno_8h.md)>

23

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <[zephyr/device.h](device_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 36](group__syscon__interface.md#ga51cf97235e40c0fa63d5c91fcee62819)typedef int (\*[syscon\_api\_get\_base](group__syscon__interface.md#ga51cf97235e40c0fa63d5c91fcee62819))(const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*addr);

37

[ 43](group__syscon__interface.md#gab23dbb591174dcb5944ce534c851eea8)typedef int (\*[syscon\_api\_read\_reg](group__syscon__interface.md#gab23dbb591174dcb5944ce534c851eea8))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

44

[ 50](group__syscon__interface.md#ga1939885e191dbf49ef1698425085ee56)typedef int (\*[syscon\_api\_write\_reg](group__syscon__interface.md#ga1939885e191dbf49ef1698425085ee56))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

51

[ 57](group__syscon__interface.md#gae09207fe29a18f32f9e52a77c8c1695f)typedef int (\*[syscon\_api\_get\_size](group__syscon__interface.md#gae09207fe29a18f32f9e52a77c8c1695f))(const struct [device](structdevice.md) \*dev, size\_t \*size);

58

[ 62](structsyscon__driver__api.md)\_\_subsystem struct [syscon\_driver\_api](structsyscon__driver__api.md) {

[ 63](structsyscon__driver__api.md#a385dd8412ad8d45aee167a1da63af337) [syscon\_api\_read\_reg](group__syscon__interface.md#gab23dbb591174dcb5944ce534c851eea8) [read](structsyscon__driver__api.md#a385dd8412ad8d45aee167a1da63af337);

[ 64](structsyscon__driver__api.md#a525b35b755468c2247febee9e5b784ab) [syscon\_api\_write\_reg](group__syscon__interface.md#ga1939885e191dbf49ef1698425085ee56) [write](structsyscon__driver__api.md#a525b35b755468c2247febee9e5b784ab);

[ 65](structsyscon__driver__api.md#a27746b1b7f15a228f2c7a3a1e3f4c305) [syscon\_api\_get\_base](group__syscon__interface.md#ga51cf97235e40c0fa63d5c91fcee62819) [get\_base](structsyscon__driver__api.md#a27746b1b7f15a228f2c7a3a1e3f4c305);

[ 66](structsyscon__driver__api.md#a3fd953872c44e99e574d4e048ac7a755) [syscon\_api\_get\_size](group__syscon__interface.md#gae09207fe29a18f32f9e52a77c8c1695f) [get\_size](structsyscon__driver__api.md#a3fd953872c44e99e574d4e048ac7a755);

67};

68

[ 76](group__syscon__interface.md#ga14c9c3bb09cec4c297a22f1ec751ceff)\_\_syscall int [syscon\_get\_base](group__syscon__interface.md#ga14c9c3bb09cec4c297a22f1ec751ceff)(const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*addr);

77

78static inline int z\_impl\_syscon\_get\_base(const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*addr)

79{

80 const struct [syscon\_driver\_api](structsyscon__driver__api.md) \*api = (const struct [syscon\_driver\_api](structsyscon__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

81

82 if (api == NULL) {

83 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

84 }

85

86 return api->get\_base(dev, addr);

87}

88

89

[ 101](group__syscon__interface.md#ga2b912d694cce403011212b83e98a7426)\_\_syscall int [syscon\_read\_reg](group__syscon__interface.md#ga2b912d694cce403011212b83e98a7426)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

102

103static inline int z\_impl\_syscon\_read\_reg(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val)

104{

105 const struct [syscon\_driver\_api](structsyscon__driver__api.md) \*api = (const struct [syscon\_driver\_api](structsyscon__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

106

107 if (api == NULL) {

108 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

109 }

110

111 return api->read(dev, reg, val);

112}

113

114

[ 126](group__syscon__interface.md#gad38b74cf372f8cdeb0439d6524af7da8)\_\_syscall int [syscon\_write\_reg](group__syscon__interface.md#gad38b74cf372f8cdeb0439d6524af7da8)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

127

128static inline int z\_impl\_syscon\_write\_reg(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

129{

130 const struct [syscon\_driver\_api](structsyscon__driver__api.md) \*api = (const struct [syscon\_driver\_api](structsyscon__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

131

132 if (api == NULL) {

133 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

134 }

135

136 return api->write(dev, reg, val);

137}

138

[ 146](group__syscon__interface.md#ga431adee943fe536fc0c4abe7e169bdf5)\_\_syscall int [syscon\_get\_size](group__syscon__interface.md#ga431adee943fe536fc0c4abe7e169bdf5)(const struct [device](structdevice.md) \*dev, size\_t \*size);

147

148static inline int z\_impl\_syscon\_get\_size(const struct [device](structdevice.md) \*dev, size\_t \*size)

149{

150 const struct [syscon\_driver\_api](structsyscon__driver__api.md) \*api = (const struct [syscon\_driver\_api](structsyscon__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

151

152 return api->get\_size(dev, size);

153}

154

158

159#ifdef \_\_cplusplus

160}

161#endif

162

163#include <zephyr/syscalls/syscon.h>

164

165#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SYSCON\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[syscon\_get\_base](group__syscon__interface.md#ga14c9c3bb09cec4c297a22f1ec751ceff)

int syscon\_get\_base(const struct device \*dev, uintptr\_t \*addr)

Get the syscon base address.

[syscon\_api\_write\_reg](group__syscon__interface.md#ga1939885e191dbf49ef1698425085ee56)

int(\* syscon\_api\_write\_reg)(const struct device \*dev, uint16\_t reg, uint32\_t val)

API template to write a single register.

**Definition** syscon.h:50

[syscon\_read\_reg](group__syscon__interface.md#ga2b912d694cce403011212b83e98a7426)

int syscon\_read\_reg(const struct device \*dev, uint16\_t reg, uint32\_t \*val)

Read from syscon register.

[syscon\_get\_size](group__syscon__interface.md#ga431adee943fe536fc0c4abe7e169bdf5)

int syscon\_get\_size(const struct device \*dev, size\_t \*size)

Get the size of the syscon register in bytes.

[syscon\_api\_get\_base](group__syscon__interface.md#ga51cf97235e40c0fa63d5c91fcee62819)

int(\* syscon\_api\_get\_base)(const struct device \*dev, uintptr\_t \*addr)

API template to get the base address of the syscon region.

**Definition** syscon.h:36

[syscon\_api\_read\_reg](group__syscon__interface.md#gab23dbb591174dcb5944ce534c851eea8)

int(\* syscon\_api\_read\_reg)(const struct device \*dev, uint16\_t reg, uint32\_t \*val)

API template to read a single register.

**Definition** syscon.h:43

[syscon\_write\_reg](group__syscon__interface.md#gad38b74cf372f8cdeb0439d6524af7da8)

int syscon\_write\_reg(const struct device \*dev, uint16\_t reg, uint32\_t val)

Write to syscon register.

[syscon\_api\_get\_size](group__syscon__interface.md#gae09207fe29a18f32f9e52a77c8c1695f)

int(\* syscon\_api\_get\_size)(const struct device \*dev, size\_t \*size)

API template to get the size of the syscon register.

**Definition** syscon.h:57

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

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

[syscon\_driver\_api](structsyscon__driver__api.md)

System Control (syscon) register driver API.

**Definition** syscon.h:62

[syscon\_driver\_api::get\_base](structsyscon__driver__api.md#a27746b1b7f15a228f2c7a3a1e3f4c305)

syscon\_api\_get\_base get\_base

**Definition** syscon.h:65

[syscon\_driver\_api::read](structsyscon__driver__api.md#a385dd8412ad8d45aee167a1da63af337)

syscon\_api\_read\_reg read

**Definition** syscon.h:63

[syscon\_driver\_api::get\_size](structsyscon__driver__api.md#a3fd953872c44e99e574d4e048ac7a755)

syscon\_api\_get\_size get\_size

**Definition** syscon.h:66

[syscon\_driver\_api::write](structsyscon__driver__api.md#a525b35b755468c2247febee9e5b784ab)

syscon\_api\_write\_reg write

**Definition** syscon.h:64

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [syscon.h](syscon_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
