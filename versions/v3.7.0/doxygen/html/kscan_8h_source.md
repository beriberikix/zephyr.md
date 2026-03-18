---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/kscan_8h_source.html
original_path: doxygen/html/kscan_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

36

[ 46](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480)typedef void (\*[kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) row,

47 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) column,

48 bool pressed);

49

57typedef int (\*kscan\_config\_t)(const struct [device](structdevice.md) \*dev,

58 [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) callback);

59typedef int (\*kscan\_disable\_callback\_t)(const struct [device](structdevice.md) \*dev);

60typedef int (\*kscan\_enable\_callback\_t)(const struct [device](structdevice.md) \*dev);

61

62\_\_subsystem struct kscan\_driver\_api {

63 kscan\_config\_t config;

64 kscan\_disable\_callback\_t disable\_callback;

65 kscan\_enable\_callback\_t enable\_callback;

66};

70

[ 81](group__kscan__interface.md#ga9caf0c1e798d610befcb9bdd4a50ddc5)\_\_syscall int [kscan\_config](group__kscan__interface.md#ga9caf0c1e798d610befcb9bdd4a50ddc5)(const struct [device](structdevice.md) \*dev,

82 [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) callback);

83

84static inline int z\_impl\_kscan\_config(const struct [device](structdevice.md) \*dev,

85 [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) callback)

86{

87 const struct kscan\_driver\_api \*api =

88 (struct kscan\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

89

90 return api->config(dev, callback);

91}

[ 99](group__kscan__interface.md#gaa1d46198ea2b36526671b0c32b3b6eab)\_\_syscall int [kscan\_enable\_callback](group__kscan__interface.md#gaa1d46198ea2b36526671b0c32b3b6eab)(const struct [device](structdevice.md) \*dev);

100

101static inline int z\_impl\_kscan\_enable\_callback(const struct [device](structdevice.md) \*dev)

102{

103 const struct kscan\_driver\_api \*api =

104 (const struct kscan\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

105

106 if (api->enable\_callback == NULL) {

107 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

108 }

109

110 return api->enable\_callback(dev);

111}

112

[ 120](group__kscan__interface.md#ga183471b229ec08d827952c7515625e28)\_\_syscall int [kscan\_disable\_callback](group__kscan__interface.md#ga183471b229ec08d827952c7515625e28)(const struct [device](structdevice.md) \*dev);

121

122static inline int z\_impl\_kscan\_disable\_callback(const struct [device](structdevice.md) \*dev)

123{

124 const struct kscan\_driver\_api \*api =

125 (const struct kscan\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

126

127 if (api->disable\_callback == NULL) {

128 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

129 }

130

131 return api->disable\_callback(dev);

132}

133

134#ifdef \_\_cplusplus

135}

136#endif

137

141

142#include <zephyr/syscalls/kscan.h>

143

144#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_KB\_SCAN\_H\_ \*/

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

**Definition** kscan.h:46

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [kscan.h](kscan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
