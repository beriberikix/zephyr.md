---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/init_8h_source.html
original_path: doxygen/html/init_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

init.h

[Go to the documentation of this file.](init_8h.md)

1/\*

2 \* Copyright (c) 2015 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_INIT\_H\_

8#define ZEPHYR\_INCLUDE\_INIT\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <stddef.h>

12

13#include <[zephyr/sys/util.h](sys_2util_8h.md)>

14#include <[zephyr/toolchain.h](toolchain_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

49

50struct [device](structdevice.md);

51

[ 66](structinit__entry.md)struct [init\_entry](structinit__entry.md) {

[ 71](structinit__entry.md#ac0b2a7ee85ad51e462b557bcb3faf6b9) int (\*[init\_fn](structinit__entry.md#ac0b2a7ee85ad51e462b557bcb3faf6b9))(void);

[ 76](structinit__entry.md#af03b5e4991da3a75059bc4b254a3e21e) const struct [device](structdevice.md) \*[dev](structinit__entry.md#af03b5e4991da3a75059bc4b254a3e21e);

77};

78

80

81/\* Helper definitions to evaluate level equality \*/

82#define Z\_INIT\_EARLY\_EARLY 1

83#define Z\_INIT\_PRE\_KERNEL\_1\_PRE\_KERNEL\_1 1

84#define Z\_INIT\_PRE\_KERNEL\_2\_PRE\_KERNEL\_2 1

85#define Z\_INIT\_POST\_KERNEL\_POST\_KERNEL 1

86#define Z\_INIT\_APPLICATION\_APPLICATION 1

87#define Z\_INIT\_SMP\_SMP 1

88

89/\* Init level ordinals \*/

90#define Z\_INIT\_ORD\_EARLY 0

91#define Z\_INIT\_ORD\_PRE\_KERNEL\_1 1

92#define Z\_INIT\_ORD\_PRE\_KERNEL\_2 2

93#define Z\_INIT\_ORD\_POST\_KERNEL 3

94#define Z\_INIT\_ORD\_APPLICATION 4

95#define Z\_INIT\_ORD\_SMP 5

96

102#define Z\_INIT\_ENTRY\_NAME(init\_id) \_CONCAT(\_\_init\_, init\_id)

103

111#define Z\_INIT\_ENTRY\_SECTION(level, prio, sub\_prio) \

112 \_\_attribute\_\_((\_\_section\_\_( \

113 ".z\_init\_" #level "\_P\_" STRINGIFY(prio) "\_SUB\_" STRINGIFY(sub\_prio)"\_")))

114

116

[ 125](group__sys__init.md#ga3025b426a99f8351d4b483205f437e48)#define INIT\_LEVEL\_ORD(level) \

126 COND\_CODE\_1(Z\_INIT\_EARLY\_##level, (Z\_INIT\_ORD\_EARLY), \

127 (COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_1\_##level, (Z\_INIT\_ORD\_PRE\_KERNEL\_1), \

128 (COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_2\_##level, (Z\_INIT\_ORD\_PRE\_KERNEL\_2), \

129 (COND\_CODE\_1(Z\_INIT\_POST\_KERNEL\_##level, (Z\_INIT\_ORD\_POST\_KERNEL), \

130 (COND\_CODE\_1(Z\_INIT\_APPLICATION\_##level, (Z\_INIT\_ORD\_APPLICATION), \

131 (COND\_CODE\_1(Z\_INIT\_SMP\_##level, (Z\_INIT\_ORD\_SMP), \

132 (ZERO\_OR\_COMPILE\_ERROR(0)))))))))))))

133

[ 150](group__sys__init.md#gaf507cc0613add8113c41896bd631254f)#define SYS\_INIT(init\_fn, level, prio) \

151 SYS\_INIT\_NAMED(init\_fn, init\_fn, level, prio)

152

[ 166](group__sys__init.md#gae862feb31eb4628b8ec95b471e5d4c54)#define SYS\_INIT\_NAMED(name, init\_fn\_, level, prio) \

167 static const Z\_DECL\_ALIGN(struct init\_entry) \

168 Z\_INIT\_ENTRY\_SECTION(level, prio, 0) \_\_used \_\_noasan \

169 Z\_INIT\_ENTRY\_NAME(name) = {.init\_fn = (init\_fn\_), .dev = NULL} \

170

171

172

173#ifdef \_\_cplusplus

174}

175#endif

176

177#endif /\* ZEPHYR\_INCLUDE\_INIT\_H\_ \*/

[stdint.h](stdint_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[init\_entry](structinit__entry.md)

Structure to store initialization entry information.

**Definition** init.h:66

[init\_entry::init\_fn](structinit__entry.md#ac0b2a7ee85ad51e462b557bcb3faf6b9)

int(\* init\_fn)(void)

If the init function belongs to a SYS\_INIT, this field stored the initialization function,...

**Definition** init.h:71

[init\_entry::dev](structinit__entry.md#af03b5e4991da3a75059bc4b254a3e21e)

const struct device \* dev

If the init entry belongs to a device, this fields stores a reference to it, otherwise it is set to N...

**Definition** init.h:76

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [init.h](init_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
