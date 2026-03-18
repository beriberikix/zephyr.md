---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/symbol_8h_source.html
original_path: doxygen/html/symbol_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

23

[ 31](structllext__const__symbol.md)struct [llext\_const\_symbol](structllext__const__symbol.md) {

[ 33](structllext__const__symbol.md#a8e18aab091d8aa99b94eed2e215400f9) const char \*const [name](structllext__const__symbol.md#a8e18aab091d8aa99b94eed2e215400f9);

34

[ 36](structllext__const__symbol.md#ac0bb3e3c67e91f790a1284f3ebc260b2) const void \*const [addr](structllext__const__symbol.md#ac0bb3e3c67e91f790a1284f3ebc260b2);

37};

38

[ 46](structllext__symbol.md)struct [llext\_symbol](structllext__symbol.md) {

[ 48](structllext__symbol.md#ae827718e18c718002eeb0cc3a3ae0ab3) const char \*[name](structllext__symbol.md#ae827718e18c718002eeb0cc3a3ae0ab3);

49

[ 51](structllext__symbol.md#ae9d19614618dc3c000f3c4e71dbda5ac) void \*[addr](structllext__symbol.md#ae9d19614618dc3c000f3c4e71dbda5ac);

52};

53

54

[ 60](structllext__symtable.md)struct [llext\_symtable](structllext__symtable.md) {

[ 62](structllext__symtable.md#a1e65bbdadb52a27b60e835994357cca1) size\_t [sym\_cnt](structllext__symtable.md#a1e65bbdadb52a27b60e835994357cca1);

63

[ 65](structllext__symtable.md#ac03152f3cb9d1881feed1d840dd024d9) struct [llext\_symbol](structllext__symbol.md) \*[syms](structllext__symtable.md#ac03152f3cb9d1881feed1d840dd024d9);

66};

67

68

[ 77](group__llext__symbols.md#ga0188531646d69e784eccf85bd4fb34aa)#define EXPORT\_SYMBOL(x) \

78 static const STRUCT\_SECTION\_ITERABLE(llext\_const\_symbol, x ## \_sym) = { \

79 .name = STRINGIFY(x), .addr = &x, \

80 }

81

[ 82](group__llext__symbols.md#ga2e05a6082a3ee50fbc74e14a48056626)#define LL\_EXTENSION\_SYMBOL(x) \

83 struct llext\_symbol Z\_GENERIC\_SECTION(".exported\_sym") \_\_used \

84 symbol\_##x = {STRINGIFY(x), &x}

85

[ 94](group__llext__symbols.md#ga0cb660137c5768a1335f0970a5efb16b)#define EXPORT\_SYSCALL(x) EXPORT\_SYMBOL(z\_impl\_ ## x)

95

99

100#ifdef \_\_cplusplus

101}

102#endif

103

104

105#endif /\* ZEPHYR\_LLEXT\_SYMBOL\_H \*/

[llext\_const\_symbol](structllext__const__symbol.md)

Constant symbols are unchangeable named memory addresses.

**Definition** symbol.h:31

[llext\_const\_symbol::name](structllext__const__symbol.md#a8e18aab091d8aa99b94eed2e215400f9)

const char \*const name

Name of symbol.

**Definition** symbol.h:33

[llext\_const\_symbol::addr](structllext__const__symbol.md#ac0bb3e3c67e91f790a1284f3ebc260b2)

const void \*const addr

Address of symbol.

**Definition** symbol.h:36

[llext\_symbol](structllext__symbol.md)

Symbols are named memory addresses.

**Definition** symbol.h:46

[llext\_symbol::name](structllext__symbol.md#ae827718e18c718002eeb0cc3a3ae0ab3)

const char \* name

Name of symbol.

**Definition** symbol.h:48

[llext\_symbol::addr](structllext__symbol.md#ae9d19614618dc3c000f3c4e71dbda5ac)

void \* addr

Address of symbol.

**Definition** symbol.h:51

[llext\_symtable](structllext__symtable.md)

A symbol table.

**Definition** symbol.h:60

[llext\_symtable::sym\_cnt](structllext__symtable.md#a1e65bbdadb52a27b60e835994357cca1)

size\_t sym\_cnt

Number of symbols in the table.

**Definition** symbol.h:62

[llext\_symtable::syms](structllext__symtable.md#ac03152f3cb9d1881feed1d840dd024d9)

struct llext\_symbol \* syms

Array of symbols.

**Definition** symbol.h:65

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [symbol.h](symbol_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
