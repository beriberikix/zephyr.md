---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/emul__fuel__gauge_8h_source.html
original_path: doxygen/html/emul__fuel__gauge_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul\_fuel\_gauge.h

[Go to the documentation of this file.](emul__fuel__gauge_8h.md)

1/\*

2 \* Copyright (c) 2023 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_EMUL\_FUEL\_GAUGE\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_EMUL\_FUEL\_GAUGE\_H\_

14

15#include <[stdint.h](stdint_8h.md)>

16#include <[zephyr/drivers/emul.h](drivers_2emul_8h.md)>

17#include <[zephyr/drivers/fuel\_gauge.h](fuel__gauge_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

29

35\_\_subsystem struct fuel\_gauge\_emul\_driver\_api {

36 int (\*set\_battery\_charging)(const struct emul \*emul, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uV, int uA);

37 int (\*is\_battery\_cutoff)(const struct emul \*emul, bool \*cutoff);

38};

42

[ 57](group__fuel__gauge__emulator__backend.md#gab6493138c35191a58e6f28c24b97715e)\_\_syscall int [emul\_fuel\_gauge\_set\_battery\_charging](group__fuel__gauge__emulator__backend.md#gab6493138c35191a58e6f28c24b97715e)(const struct [emul](structemul.md) \*target, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uV, int uA);

58static inline int z\_impl\_emul\_fuel\_gauge\_set\_battery\_charging(const struct [emul](structemul.md) \*target,

59 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uV, int uA)

60{

61 const struct fuel\_gauge\_emul\_driver\_api \*backend\_api =

62 (const struct fuel\_gauge\_emul\_driver\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

63

64 if (backend\_api->set\_battery\_charging == 0) {

65 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

66 }

67

68 return backend\_api->set\_battery\_charging(target, uV, uA);

69}

70

[ 80](group__fuel__gauge__emulator__backend.md#gaf8326331c7470b41aa542f828b20a828)\_\_syscall int [emul\_fuel\_gauge\_is\_battery\_cutoff](group__fuel__gauge__emulator__backend.md#gaf8326331c7470b41aa542f828b20a828)(const struct [emul](structemul.md) \*target, bool \*cutoff);

81static inline int z\_impl\_emul\_fuel\_gauge\_is\_battery\_cutoff(const struct [emul](structemul.md) \*target, bool \*cutoff)

82{

83 const struct fuel\_gauge\_emul\_driver\_api \*backend\_api =

84 (const struct fuel\_gauge\_emul\_driver\_api \*)target->[backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea);

85

86 if (backend\_api->is\_battery\_cutoff == 0) {

87 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

88 }

89 return backend\_api->is\_battery\_cutoff(target, cutoff);

90}

91

92#ifdef \_\_cplusplus

93}

94#endif

95

96#include <zephyr/syscalls/emul\_fuel\_gauge.h>

97

101

102#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_EMUL\_FUEL\_GAUGE\_H\_\*/

[emul.h](drivers_2emul_8h.md)

[fuel\_gauge.h](fuel__gauge_8h.md)

[emul\_fuel\_gauge\_set\_battery\_charging](group__fuel__gauge__emulator__backend.md#gab6493138c35191a58e6f28c24b97715e)

int emul\_fuel\_gauge\_set\_battery\_charging(const struct emul \*target, uint32\_t uV, int uA)

Set charging for fuel gauge associated battery.

[emul\_fuel\_gauge\_is\_battery\_cutoff](group__fuel__gauge__emulator__backend.md#gaf8326331c7470b41aa542f828b20a828)

int emul\_fuel\_gauge\_is\_battery\_cutoff(const struct emul \*target, bool \*cutoff)

Check if the battery has been cut off.

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[emul](structemul.md)

An emulator instance - represents the target emulated device/peripheral that is interacted with throu...

**Definition** emul.h:82

[emul::backend\_api](structemul.md#ac7e90a7ff00a0c08836821c7d49b7dea)

const void \* backend\_api

Address of the API structure exposed by the emulator instance.

**Definition** emul.h:103

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul\_fuel\_gauge.h](emul__fuel__gauge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
