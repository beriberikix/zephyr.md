---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/init_8h_source.html
original_path: doxygen/html/init_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

13#include <[zephyr/sys/util.h](util_8h.md)>

14#include <[zephyr/toolchain.h](toolchain_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

49

50struct [device](structdevice.md);

51

[ 59](unioninit__function.md)union [init\_function](unioninit__function.md) {

[ 66](unioninit__function.md#a147196ff078175284385ce2eb1448498) int (\*[sys](unioninit__function.md#a147196ff078175284385ce2eb1448498))(void);

[ 75](unioninit__function.md#a074d663e90ecb3e3ffcd0b9f5f16eb08) int (\*[dev](unioninit__function.md#a074d663e90ecb3e3ffcd0b9f5f16eb08))(const struct [device](structdevice.md) \*[dev](unioninit__function.md#a074d663e90ecb3e3ffcd0b9f5f16eb08));

76#ifdef CONFIG\_DEVICE\_MUTABLE

85 int (\*dev\_rw)(struct [device](structdevice.md) \*[dev](unioninit__function.md#a074d663e90ecb3e3ffcd0b9f5f16eb08));

86#endif

87};

88

[ 103](structinit__entry.md)struct [init\_entry](structinit__entry.md) {

[ 105](structinit__entry.md#a2b2155a753096b51e80a1ef7752d05fb) union [init\_function](unioninit__function.md) [init\_fn](structinit__entry.md#a2b2155a753096b51e80a1ef7752d05fb);

110 union {

[ 111](structinit__entry.md#af03b5e4991da3a75059bc4b254a3e21e) const struct [device](structdevice.md) \*[dev](structinit__entry.md#af03b5e4991da3a75059bc4b254a3e21e);

112#ifdef CONFIG\_DEVICE\_MUTABLE

113 struct [device](structdevice.md) \*dev\_rw;

114#endif

115 };

116};

117

119

120/\* Helper definitions to evaluate level equality \*/

121#define Z\_INIT\_EARLY\_EARLY 1

122#define Z\_INIT\_PRE\_KERNEL\_1\_PRE\_KERNEL\_1 1

123#define Z\_INIT\_PRE\_KERNEL\_2\_PRE\_KERNEL\_2 1

124#define Z\_INIT\_POST\_KERNEL\_POST\_KERNEL 1

125#define Z\_INIT\_APPLICATION\_APPLICATION 1

126#define Z\_INIT\_SMP\_SMP 1

127

128/\* Init level ordinals \*/

129#define Z\_INIT\_ORD\_EARLY 0

130#define Z\_INIT\_ORD\_PRE\_KERNEL\_1 1

131#define Z\_INIT\_ORD\_PRE\_KERNEL\_2 2

132#define Z\_INIT\_ORD\_POST\_KERNEL 3

133#define Z\_INIT\_ORD\_APPLICATION 4

134#define Z\_INIT\_ORD\_SMP 5

135

141#define Z\_INIT\_ENTRY\_NAME(init\_id) \_CONCAT(\_\_init\_, init\_id)

142

150#define Z\_INIT\_ENTRY\_SECTION(level, prio, sub\_prio) \

151 \_\_attribute\_\_((\_\_section\_\_( \

152 ".z\_init\_" #level STRINGIFY(prio)"\_" STRINGIFY(sub\_prio)"\_")))

153

155

[ 164](group__sys__init.md#ga3025b426a99f8351d4b483205f437e48)#define INIT\_LEVEL\_ORD(level) \

165 COND\_CODE\_1(Z\_INIT\_EARLY\_##level, (Z\_INIT\_ORD\_EARLY), \

166 (COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_1\_##level, (Z\_INIT\_ORD\_PRE\_KERNEL\_1), \

167 (COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_2\_##level, (Z\_INIT\_ORD\_PRE\_KERNEL\_2), \

168 (COND\_CODE\_1(Z\_INIT\_POST\_KERNEL\_##level, (Z\_INIT\_ORD\_POST\_KERNEL), \

169 (COND\_CODE\_1(Z\_INIT\_APPLICATION\_##level, (Z\_INIT\_ORD\_APPLICATION), \

170 (COND\_CODE\_1(Z\_INIT\_SMP\_##level, (Z\_INIT\_ORD\_SMP), \

171 (ZERO\_OR\_COMPILE\_ERROR(0)))))))))))))

172

[ 189](group__sys__init.md#gaf507cc0613add8113c41896bd631254f)#define SYS\_INIT(init\_fn, level, prio) \

190 SYS\_INIT\_NAMED(init\_fn, init\_fn, level, prio)

191

[ 205](group__sys__init.md#gae862feb31eb4628b8ec95b471e5d4c54)#define SYS\_INIT\_NAMED(name, init\_fn\_, level, prio) \

206 static const Z\_DECL\_ALIGN(struct init\_entry) \

207 Z\_INIT\_ENTRY\_SECTION(level, prio, 0) \_\_used \_\_noasan \

208 Z\_INIT\_ENTRY\_NAME(name) = {{ (init\_fn\_) }, { NULL } }

209

211

212#ifdef \_\_cplusplus

213}

214#endif

215

216#endif /\* ZEPHYR\_INCLUDE\_INIT\_H\_ \*/

[stdint.h](stdint_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[init\_entry](structinit__entry.md)

Structure to store initialization entry information.

**Definition** init.h:103

[init\_entry::init\_fn](structinit__entry.md#a2b2155a753096b51e80a1ef7752d05fb)

union init\_function init\_fn

Initialization function.

**Definition** init.h:105

[init\_entry::dev](structinit__entry.md#af03b5e4991da3a75059bc4b254a3e21e)

const struct device \* dev

**Definition** init.h:111

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[init\_function](unioninit__function.md)

Initialization function for init entries.

**Definition** init.h:59

[init\_function::dev](unioninit__function.md#a074d663e90ecb3e3ffcd0b9f5f16eb08)

int(\* dev)(const struct device \*dev)

Device initialization function.

**Definition** init.h:75

[init\_function::sys](unioninit__function.md#a147196ff078175284385ce2eb1448498)

int(\* sys)(void)

System initialization function.

**Definition** init.h:66

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [init.h](init_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
