---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/emul__bbram_8h_source.html
original_path: doxygen/html/emul__bbram_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul\_bbram.h

[Go to the documentation of this file.](emul__bbram_8h.md)

1/\*

2 \* Copyright 2024 Google LLC

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef INCLUDE\_ZEPHYR\_DRIVERS\_EMUL\_BBRAM\_H\_

7#define INCLUDE\_ZEPHYR\_DRIVERS\_EMUL\_BBRAM\_H\_

8

9#include <[zephyr/drivers/emul.h](drivers_2emul_8h.md)>

10

11#include <[stdint.h](stdint_8h.md)>

12

19

25

26\_\_subsystem struct emul\_bbram\_driver\_api {

28 int (\*set\_data)(const struct emul \*target, size\_t offset, size\_t count,

29 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

31 int (\*get\_data)(const struct emul \*target, size\_t offset, size\_t count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

32};

33

37

[ 49](group__bbram__emulator__backend.md#gaeff1fa9acd765323778c42a4c3424c0b)static inline int [emul\_bbram\_backend\_set\_data](group__bbram__emulator__backend.md#gaeff1fa9acd765323778c42a4c3424c0b)(const struct [emul](structemul.md) \*target, size\_t offset,

50 size\_t count, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structemul.md#a82f3fcaf221cd329ef1b6cb93cc7c8e6))

51{

52 if (target == NULL || target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea) == NULL) {

53 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

54 }

55

56 struct emul\_bbram\_driver\_api \*api = (struct emul\_bbram\_driver\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

57

58 if (api->set\_data == NULL) {

59 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

60 }

61

62 return api->set\_data(target, offset, count, data);

63}

64

[ 76](group__bbram__emulator__backend.md#ga92942f1ebe6905ad3cfe389824af5914)static inline int [emul\_bbram\_backend\_get\_data](group__bbram__emulator__backend.md#ga92942f1ebe6905ad3cfe389824af5914)(const struct [emul](structemul.md) \*target, size\_t offset,

77 size\_t count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

78{

79 if (target == NULL || target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea) == NULL) {

80 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

81 }

82

83 struct emul\_bbram\_driver\_api \*api = (struct emul\_bbram\_driver\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

84

85 if (api->get\_data == NULL) {

86 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

87 }

88

89 return api->get\_data(target, offset, count, data);

90}

91

95

96#endif /\* INCLUDE\_ZEPHYR\_DRIVERS\_EMUL\_BBRAM\_H\_ \*/

[emul.h](drivers_2emul_8h.md)

[emul\_bbram\_backend\_get\_data](group__bbram__emulator__backend.md#ga92942f1ebe6905ad3cfe389824af5914)

static int emul\_bbram\_backend\_get\_data(const struct emul \*target, size\_t offset, size\_t count, uint8\_t \*data)

Get the expected data in the bbram region.

**Definition** emul\_bbram.h:76

[emul\_bbram\_backend\_set\_data](group__bbram__emulator__backend.md#gaeff1fa9acd765323778c42a4c3424c0b)

static int emul\_bbram\_backend\_set\_data(const struct emul \*target, size\_t offset, size\_t count, const uint8\_t \*data)

Set the expected data in the bbram region.

**Definition** emul\_bbram.h:49

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:80

[emul::data](structemul.md#a82f3fcaf221cd329ef1b6cb93cc7c8e6)

void \* data

Emulator-specific data.

**Definition** emul.h:88

[emul::backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)

const void \* backend\_api

Address of the API structure exposed by the emulator instance.

**Definition** emul.h:100

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul\_bbram.h](emul__bbram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
