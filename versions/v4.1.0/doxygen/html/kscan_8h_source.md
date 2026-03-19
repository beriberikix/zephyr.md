---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/kscan_8h_source.html
original_path: doxygen/html/kscan_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kscan.h

[Go to the documentation of this file.](kscan_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_KB\_SCAN\_H\_

17#define ZEPHYR\_INCLUDE\_DRIVERS\_KB\_SCAN\_H\_

18

19#include <[errno.h](errno_8h.md)>

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21#include <stddef.h>

22#include <[zephyr/device.h](device_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

37

[ 48](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480)typedef void (\*[kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) row,

49 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) column,

50 bool pressed);

51

60typedef int (\*kscan\_config\_t)(const struct [device](structdevice.md) \*dev,

61 [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) callback);

62typedef int (\*kscan\_disable\_callback\_t)(const struct [device](structdevice.md) \*dev);

63typedef int (\*kscan\_enable\_callback\_t)(const struct [device](structdevice.md) \*dev);

64

65\_\_subsystem struct kscan\_driver\_api {

66 kscan\_config\_t config;

67 kscan\_disable\_callback\_t disable\_callback;

68 kscan\_enable\_callback\_t enable\_callback;

69};

73

[ 85](group__kscan__interface.md#ga9caf0c1e798d610befcb9bdd4a50ddc5)\_\_syscall int [kscan\_config](group__kscan__interface.md#ga9caf0c1e798d610befcb9bdd4a50ddc5)(const struct [device](structdevice.md) \*dev,

86 [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) callback);

87

88static inline int z\_impl\_kscan\_config(const struct [device](structdevice.md) \*dev,

89 [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) callback)

90{

91 const struct kscan\_driver\_api \*api =

92 (struct kscan\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

93

94 return api->config(dev, callback);

95}

[ 104](group__kscan__interface.md#gaa1d46198ea2b36526671b0c32b3b6eab)\_\_syscall int [kscan\_enable\_callback](group__kscan__interface.md#gaa1d46198ea2b36526671b0c32b3b6eab)(const struct [device](structdevice.md) \*dev);

105

106static inline int z\_impl\_kscan\_enable\_callback(const struct [device](structdevice.md) \*dev)

107{

108 const struct kscan\_driver\_api \*api =

109 (const struct kscan\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

110

111 if (api->enable\_callback == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

112 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

113 }

114

115 return api->enable\_callback(dev);

116}

117

[ 126](group__kscan__interface.md#ga183471b229ec08d827952c7515625e28)\_\_syscall int [kscan\_disable\_callback](group__kscan__interface.md#ga183471b229ec08d827952c7515625e28)(const struct [device](structdevice.md) \*dev);

127

128static inline int z\_impl\_kscan\_disable\_callback(const struct [device](structdevice.md) \*dev)

129{

130 const struct kscan\_driver\_api \*api =

131 (const struct kscan\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

132

133 if (api->disable\_callback == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

134 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

135 }

136

137 return api->disable\_callback(dev);

138}

139

140#ifdef \_\_cplusplus

141}

142#endif

143

147

148#include <zephyr/syscalls/kscan.h>

149

150#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_KB\_SCAN\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[kscan\_disable\_callback](group__kscan__interface.md#ga183471b229ec08d827952c7515625e28)

int kscan\_disable\_callback(const struct device \*dev)

Disables callback.

[kscan\_config](group__kscan__interface.md#ga9caf0c1e798d610befcb9bdd4a50ddc5)

int kscan\_config(const struct device \*dev, kscan\_callback\_t callback)

Configure a Keyboard scan instance.

[kscan\_enable\_callback](group__kscan__interface.md#gaa1d46198ea2b36526671b0c32b3b6eab)

int kscan\_enable\_callback(const struct device \*dev)

Enables callback.

[kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480)

void(\* kscan\_callback\_t)(const struct device \*dev, uint32\_t row, uint32\_t column, bool pressed)

Keyboard scan callback called when user press/release a key on a matrix keyboard.

**Definition** kscan.h:48

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [kscan.h](kscan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
