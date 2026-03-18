---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kscan_8h_source.html
original_path: doxygen/html/kscan_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

34

[ 44](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480)typedef void (\*[kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) row,

45 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) column,

46 bool pressed);

47

55typedef int (\*kscan\_config\_t)(const struct [device](structdevice.md) \*dev,

56 [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) callback);

57typedef int (\*kscan\_disable\_callback\_t)(const struct [device](structdevice.md) \*dev);

58typedef int (\*kscan\_enable\_callback\_t)(const struct [device](structdevice.md) \*dev);

59

60\_\_subsystem struct kscan\_driver\_api {

61 kscan\_config\_t config;

62 kscan\_disable\_callback\_t disable\_callback;

63 kscan\_enable\_callback\_t enable\_callback;

64};

68

[ 79](group__kscan__interface.md#ga9caf0c1e798d610befcb9bdd4a50ddc5)\_\_syscall int [kscan\_config](group__kscan__interface.md#ga9caf0c1e798d610befcb9bdd4a50ddc5)(const struct [device](structdevice.md) \*dev,

80 [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) callback);

81

82static inline int z\_impl\_kscan\_config(const struct [device](structdevice.md) \*dev,

83 [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) callback)

84{

85 const struct kscan\_driver\_api \*api =

86 (struct kscan\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

87

88 return api->config(dev, callback);

89}

[ 97](group__kscan__interface.md#gaa1d46198ea2b36526671b0c32b3b6eab)\_\_syscall int [kscan\_enable\_callback](group__kscan__interface.md#gaa1d46198ea2b36526671b0c32b3b6eab)(const struct [device](structdevice.md) \*dev);

98

99static inline int z\_impl\_kscan\_enable\_callback(const struct [device](structdevice.md) \*dev)

100{

101 const struct kscan\_driver\_api \*api =

102 (const struct kscan\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

103

104 if (api->enable\_callback == NULL) {

105 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

106 }

107

108 return api->enable\_callback(dev);

109}

110

[ 118](group__kscan__interface.md#ga183471b229ec08d827952c7515625e28)\_\_syscall int [kscan\_disable\_callback](group__kscan__interface.md#ga183471b229ec08d827952c7515625e28)(const struct [device](structdevice.md) \*dev);

119

120static inline int z\_impl\_kscan\_disable\_callback(const struct [device](structdevice.md) \*dev)

121{

122 const struct kscan\_driver\_api \*api =

123 (const struct kscan\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

124

125 if (api->disable\_callback == NULL) {

126 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

127 }

128

129 return api->disable\_callback(dev);

130}

131

132#ifdef \_\_cplusplus

133}

134#endif

135

139

140#include <syscalls/kscan.h>

141

142#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_KB\_SCAN\_H\_ \*/

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

**Definition** kscan.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [kscan.h](kscan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
