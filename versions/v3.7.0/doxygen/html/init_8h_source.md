---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/init_8h_source.html
original_path: doxygen/html/init_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

154

155/\* Designated initializers where added to C in C99. There were added to

156 \* C++ 20 years later in a much more restricted form. C99 allows many

157 \* variations: out of order, mix of designated and not, overlap,

158 \* override,... but C++ allows none of these. See differences detailed

159 \* in the P0329R0.pdf C++ proposal.

160 \* Note \_\_STDC\_VERSION\_\_ is undefined when compiling C++.

161 \*/

162#if defined(\_\_STDC\_VERSION\_\_) && (\_\_STDC\_VERSION\_\_) < 201100

163

164/\* Anonymous unions require C11. Some pre-C11 gcc versions have early

165 \* support for anonymous unions but they require these braces when

166 \* combined with C99 designated initializers, see longer discussion in

167 \* #69411.

168 \* These braces are compatible with any C version but not with C++20.

169 \*/

170# define Z\_INIT\_SYS\_INIT\_DEV\_NULL { .dev = NULL }

171

172#else

173

174/\* When using -std=c++20 or higher, g++ (v12.2.0) reject braces for

175 \* initializing anonymous unions because it is technically a mix of

176 \* designated and not designated initializers which is not allowed in

177 \* C++. Interestingly, the \_same\_ g++ version does accept the braces above

178 \* when using -std=c++17 or lower!

179 \* The tests/lib/cpp/cxx/ added by commit 3d9c428d57bf invoke the C++

180 \* compiler with a range of different `-std=...` parameters without needing

181 \* any manual configuration.

182 \*/

183# define Z\_INIT\_SYS\_INIT\_DEV\_NULL .dev = NULL

184

185#endif

186

188

[ 197](group__sys__init.md#ga3025b426a99f8351d4b483205f437e48)#define INIT\_LEVEL\_ORD(level) \

198 COND\_CODE\_1(Z\_INIT\_EARLY\_##level, (Z\_INIT\_ORD\_EARLY), \

199 (COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_1\_##level, (Z\_INIT\_ORD\_PRE\_KERNEL\_1), \

200 (COND\_CODE\_1(Z\_INIT\_PRE\_KERNEL\_2\_##level, (Z\_INIT\_ORD\_PRE\_KERNEL\_2), \

201 (COND\_CODE\_1(Z\_INIT\_POST\_KERNEL\_##level, (Z\_INIT\_ORD\_POST\_KERNEL), \

202 (COND\_CODE\_1(Z\_INIT\_APPLICATION\_##level, (Z\_INIT\_ORD\_APPLICATION), \

203 (COND\_CODE\_1(Z\_INIT\_SMP\_##level, (Z\_INIT\_ORD\_SMP), \

204 (ZERO\_OR\_COMPILE\_ERROR(0)))))))))))))

205

[ 222](group__sys__init.md#gaf507cc0613add8113c41896bd631254f)#define SYS\_INIT(init\_fn, level, prio) \

223 SYS\_INIT\_NAMED(init\_fn, init\_fn, level, prio)

224

[ 238](group__sys__init.md#gae862feb31eb4628b8ec95b471e5d4c54)#define SYS\_INIT\_NAMED(name, init\_fn\_, level, prio) \

239 static const Z\_DECL\_ALIGN(struct init\_entry) \

240 Z\_INIT\_ENTRY\_SECTION(level, prio, 0) \_\_used \_\_noasan \

241 Z\_INIT\_ENTRY\_NAME(name) = {.init\_fn = {.sys = (init\_fn\_)}, \

242 Z\_INIT\_SYS\_INIT\_DEV\_NULL}

243

245

246#ifdef \_\_cplusplus

247}

248#endif

249

250#endif /\* ZEPHYR\_INCLUDE\_INIT\_H\_ \*/

[stdint.h](stdint_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

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
