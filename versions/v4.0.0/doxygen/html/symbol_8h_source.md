---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/symbol_8h_source.html
original_path: doxygen/html/symbol_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

symbol.h

[Go to the documentation of this file.](symbol_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LLEXT\_SYMBOL\_H

8#define ZEPHYR\_LLEXT\_SYMBOL\_H

9

10#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12#include <stddef.h>

13#include <[stdint.h](stdint_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

31

[ 42](structllext__const__symbol.md)struct [llext\_const\_symbol](structllext__const__symbol.md) {

47 union {

[ 49](structllext__const__symbol.md#a8e18aab091d8aa99b94eed2e215400f9) const char \*const [name](structllext__const__symbol.md#a8e18aab091d8aa99b94eed2e215400f9);

50

[ 52](structllext__const__symbol.md#afe01c08dff4f9334a95a9be23aede72b) const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [slid](structllext__const__symbol.md#afe01c08dff4f9334a95a9be23aede72b);

53 };

54

[ 56](structllext__const__symbol.md#ac0bb3e3c67e91f790a1284f3ebc260b2) const void \*const [addr](structllext__const__symbol.md#ac0bb3e3c67e91f790a1284f3ebc260b2);

57};

58BUILD\_ASSERT(sizeof(struct [llext\_const\_symbol](structllext__const__symbol.md)) == 2 \* sizeof([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)));

59

[ 67](structllext__symbol.md)struct [llext\_symbol](structllext__symbol.md) {

[ 69](structllext__symbol.md#ae827718e18c718002eeb0cc3a3ae0ab3) const char \*[name](structllext__symbol.md#ae827718e18c718002eeb0cc3a3ae0ab3);

70

[ 72](structllext__symbol.md#ae9d19614618dc3c000f3c4e71dbda5ac) void \*[addr](structllext__symbol.md#ae9d19614618dc3c000f3c4e71dbda5ac);

73};

74

75

[ 81](structllext__symtable.md)struct [llext\_symtable](structllext__symtable.md) {

[ 83](structllext__symtable.md#a1e65bbdadb52a27b60e835994357cca1) size\_t [sym\_cnt](structllext__symtable.md#a1e65bbdadb52a27b60e835994357cca1);

84

[ 86](structllext__symtable.md#ac03152f3cb9d1881feed1d840dd024d9) struct [llext\_symbol](structllext__symbol.md) \*[syms](structllext__symtable.md#ac03152f3cb9d1881feed1d840dd024d9);

87};

88

89

91#ifdef LL\_EXTENSION\_BUILD

92/\* Extension build: add exported symbols to llext table \*/

93#define Z\_LL\_EXTENSION\_SYMBOL(x) \

94 static const struct llext\_const\_symbol \

95 Z\_GENERIC\_SECTION(".exported\_sym") \_\_used \

96 \_\_llext\_sym\_ ## x = { \

97 .name = STRINGIFY(x), .addr = (const void \*)&x, \

98 }

99#else

100/\* No-op when not building an extension \*/

101#define Z\_LL\_EXTENSION\_SYMBOL(x)

102#endif

104

[ 116](group__llext__symbols.md#ga2e05a6082a3ee50fbc74e14a48056626)#define LL\_EXTENSION\_SYMBOL(x) Z\_LL\_EXTENSION\_SYMBOL(x)

117

119#if defined(LL\_EXTENSION\_BUILD)

120/\* Extension build: EXPORT\_SYMBOL maps to LL\_EXTENSION\_SYMBOL \*/

121#define Z\_EXPORT\_SYMBOL(x) Z\_LL\_EXTENSION\_SYMBOL(x)

122#elif defined(CONFIG\_LLEXT\_EXPORT\_BUILTINS\_BY\_SLID)

123/\* SLID-enabled LLEXT application: export symbols, names in separate section \*/

124#define Z\_EXPORT\_SYMBOL(x) \

125 static const char Z\_GENERIC\_SECTION("llext\_exports\_strtab") \_\_used \

126 \_\_llext\_sym\_name\_ ## x[] = STRINGIFY(x); \

127 static const STRUCT\_SECTION\_ITERABLE(llext\_const\_symbol, \

128 \_\_llext\_sym\_ ## x) = { \

129 .name = \_\_llext\_sym\_name\_ ## x, .addr = (const void \*)&x, \

130 }

131#elif defined(CONFIG\_LLEXT)

132/\* LLEXT application: export symbols \*/

133#define Z\_EXPORT\_SYMBOL(x) \

134 static const STRUCT\_SECTION\_ITERABLE(llext\_const\_symbol, \

135 \_\_llext\_sym\_ ## x) = { \

136 .name = STRINGIFY(x), .addr = (const void \*)&x, \

137 }

138#else

139/\* No extension support in this build \*/

140#define Z\_EXPORT\_SYMBOL(x)

141#endif

143

[ 155](group__llext__symbols.md#ga0188531646d69e784eccf85bd4fb34aa)#define EXPORT\_SYMBOL(x) Z\_EXPORT\_SYMBOL(x)

156

160

161#ifdef \_\_cplusplus

162}

163#endif

164

165

166#endif /\* ZEPHYR\_LLEXT\_SYMBOL\_H \*/

[stdint.h](stdint_8h.md)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[llext\_const\_symbol](structllext__const__symbol.md)

Constant symbols are unchangeable named memory addresses.

**Definition** symbol.h:42

[llext\_const\_symbol::name](structllext__const__symbol.md#a8e18aab091d8aa99b94eed2e215400f9)

const char \*const name

Name of symbol.

**Definition** symbol.h:49

[llext\_const\_symbol::addr](structllext__const__symbol.md#ac0bb3e3c67e91f790a1284f3ebc260b2)

const void \*const addr

Address of symbol.

**Definition** symbol.h:56

[llext\_const\_symbol::slid](structllext__const__symbol.md#afe01c08dff4f9334a95a9be23aede72b)

const uintptr\_t slid

Symbol Link Identifier.

**Definition** symbol.h:52

[llext\_symbol](structllext__symbol.md)

Symbols are named memory addresses.

**Definition** symbol.h:67

[llext\_symbol::name](structllext__symbol.md#ae827718e18c718002eeb0cc3a3ae0ab3)

const char \* name

Name of symbol.

**Definition** symbol.h:69

[llext\_symbol::addr](structllext__symbol.md#ae9d19614618dc3c000f3c4e71dbda5ac)

void \* addr

Address of symbol.

**Definition** symbol.h:72

[llext\_symtable](structllext__symtable.md)

A symbol table.

**Definition** symbol.h:81

[llext\_symtable::sym\_cnt](structllext__symtable.md#a1e65bbdadb52a27b60e835994357cca1)

size\_t sym\_cnt

Number of symbols in the table.

**Definition** symbol.h:83

[llext\_symtable::syms](structllext__symtable.md#ac03152f3cb9d1881feed1d840dd024d9)

struct llext\_symbol \* syms

Array of symbols.

**Definition** symbol.h:86

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [symbol.h](symbol_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
