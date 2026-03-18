---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/emul__bc12_8h_source.html
original_path: doxygen/html/emul__bc12_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul\_bc12.h

[Go to the documentation of this file.](emul__bc12_8h.md)

1/\*

2 \* Copyright (c) 2022 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_USB\_EMUL\_BC12\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_USB\_EMUL\_BC12\_H\_

14

15#include <[zephyr/drivers/emul.h](drivers_2emul_8h.md)>

16#include <[zephyr/drivers/usb/usb\_bc12.h](usb__bc12_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

28

34\_\_subsystem struct bc12\_emul\_driver\_api {

35 int (\*set\_charging\_partner)(const struct emul \*emul, enum [bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb) partner\_type);

36 int (\*set\_pd\_partner)(const struct emul \*emul, bool connected);

37};

41

[ 56](group__b12__emulator__backend.md#gaca0e62f2f8a5ec3135523fa3a1308034)static inline int [bc12\_emul\_set\_charging\_partner](group__b12__emulator__backend.md#gaca0e62f2f8a5ec3135523fa3a1308034)(const struct [emul](structemul.md) \*target,

57 enum [bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb) partner\_type)

58{

59 const struct bc12\_emul\_driver\_api \*backend\_api =

60 (const struct bc12\_emul\_driver\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

61

62 return backend\_api->set\_charging\_partner(target, partner\_type);

63}

64

[ 80](group__b12__emulator__backend.md#gaa71771a3199aef043fe313f09f3bb4f2)static inline int [bc12\_emul\_set\_pd\_partner](group__b12__emulator__backend.md#gaa71771a3199aef043fe313f09f3bb4f2)(const struct [emul](structemul.md) \*target, bool connected)

81{

82 const struct bc12\_emul\_driver\_api \*backend\_api =

83 (const struct bc12\_emul\_driver\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

84

85 return backend\_api->set\_pd\_partner(target, connected);

86}

87

88#ifdef \_\_cplusplus

89}

90#endif

91

95

96#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_USB\_EMUL\_BC12\_H\_ \*/

[emul.h](drivers_2emul_8h.md)

[bc12\_emul\_set\_pd\_partner](group__b12__emulator__backend.md#gaa71771a3199aef043fe313f09f3bb4f2)

static int bc12\_emul\_set\_pd\_partner(const struct emul \*target, bool connected)

Set the portable device partner state.

**Definition** emul\_bc12.h:80

[bc12\_emul\_set\_charging\_partner](group__b12__emulator__backend.md#gaca0e62f2f8a5ec3135523fa3a1308034)

static int bc12\_emul\_set\_charging\_partner(const struct emul \*target, enum bc12\_type partner\_type)

Set the charging partner type connected to the BC1.2 device.

**Definition** emul\_bc12.h:56

[bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb)

bc12\_type

BC1.2 charging partner type.

**Definition** usb\_bc12.h:72

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:80

[emul::backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)

const void \* backend\_api

Address of the API structure exposed by the emulator instance.

**Definition** emul.h:100

[usb\_bc12.h](usb__bc12_8h.md)

Public APIs for the USB BC1.2 battery charging detect drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [emul\_bc12.h](emul__bc12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
