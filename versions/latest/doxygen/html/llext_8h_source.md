---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/llext_8h_source.html
original_path: doxygen/html/llext_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext.h

[Go to the documentation of this file.](llext_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LLEXT\_H

8#define ZEPHYR\_LLEXT\_H

9

10#include <[zephyr/sys/slist.h](slist_8h.md)>

11#include <[zephyr/llext/elf.h](elf_8h.md)>

12#include <[zephyr/llext/symbol.h](symbol_8h.md)>

13#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

14#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

15#include <[stdbool.h](stdbool_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

[ 31](group__llext.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)enum [llext\_mem](group__llext.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) {

[ 32](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a4e7f671abb8e64ad6af7033a9439b7d0) [LLEXT\_MEM\_TEXT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a4e7f671abb8e64ad6af7033a9439b7d0),

[ 33](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a5e8658f79b74a0916e5d0abe8f852854) [LLEXT\_MEM\_DATA](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a5e8658f79b74a0916e5d0abe8f852854),

[ 34](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a8ad55e9d9685edd3dfc4ede21854faeb) [LLEXT\_MEM\_RODATA](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a8ad55e9d9685edd3dfc4ede21854faeb),

[ 35](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e) [LLEXT\_MEM\_BSS](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e),

[ 36](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae6ed486ed5719bf7058b2f95aa712028) [LLEXT\_MEM\_EXPORT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae6ed486ed5719bf7058b2f95aa712028),

[ 37](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a24549b7a2ee43076f5b8646e7fba5c81) [LLEXT\_MEM\_SYMTAB](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a24549b7a2ee43076f5b8646e7fba5c81),

[ 38](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17) [LLEXT\_MEM\_STRTAB](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17),

[ 39](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e) [LLEXT\_MEM\_SHSTRTAB](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e),

40

[ 41](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265) [LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265),

42};

43

[ 44](group__llext.md#ga8740e267a2d59772fde6cda3df1711f2)#define LLEXT\_MEM\_PARTITIONS (LLEXT\_MEM\_BSS+1)

45

46struct [llext\_loader](structllext__loader.md);

47

[ 51](structllext.md)struct [llext](structllext.md) {

53 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_llext\_list;

54

55#ifdef CONFIG\_USERSPACE

56 struct [k\_mem\_partition](structk__mem__partition.md) mem\_parts[[LLEXT\_MEM\_PARTITIONS](group__llext.md#ga8740e267a2d59772fde6cda3df1711f2)];

57 struct [k\_mem\_domain](structk__mem__domain.md) mem\_domain;

58#endif

59

61

[ 63](structllext.md#a505e052f55e25cf10ac0431defb774ea) char [name](structllext.md#a505e052f55e25cf10ac0431defb774ea)[16];

64

[ 66](structllext.md#ae9d529433f30ed659758c9b29c9b96bd) void \*[mem](structllext.md#ae9d529433f30ed659758c9b29c9b96bd)[[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)];

67

[ 69](structllext.md#a7556c195516041439547d891897f4a44) bool [mem\_on\_heap](structllext.md#a7556c195516041439547d891897f4a44)[[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)];

70

[ 72](structllext.md#a47cfcb60d773a6c16d2fda8cc5011a16) size\_t [mem\_size](structllext.md#a47cfcb60d773a6c16d2fda8cc5011a16)[[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)];

73

[ 75](structllext.md#a566e46e600e9b90f9d4b570ef007e6a6) size\_t [alloc\_size](structllext.md#a566e46e600e9b90f9d4b570ef007e6a6);

76

77 /\*

78 \* These are all global symbols in the extension, all of them don't

79 \* have to be exported to other extensions, but this table is needed for

80 \* faster internal linking, e.g. if the extension is built out of

81 \* several files, if any symbols are referenced between files, this

82 \* table will be used to link them.

83 \*/

[ 84](structllext.md#a4f67c792a963ac124f32b2d7880f9cdf) struct [llext\_symtable](structllext__symtable.md) [sym\_tab](structllext.md#a4f67c792a963ac124f32b2d7880f9cdf);

85

[ 87](structllext.md#a76cc3ef7989f2d4bfaeedadd05738de2) struct [llext\_symtable](structllext__symtable.md) [exp\_tab](structllext.md#a76cc3ef7989f2d4bfaeedadd05738de2);

88

[ 90](structllext.md#a61c5ca5c740f5bb14791f11354b68101) unsigned int [use\_count](structllext.md#a61c5ca5c740f5bb14791f11354b68101);

91};

92

[ 100](group__llext.md#gaad89b0b44cf5c9528c3f8a0ce37a8fbe)struct [llext](structllext.md) \*[llext\_by\_name](group__llext.md#gaad89b0b44cf5c9528c3f8a0ce37a8fbe)(const char \*[name](structllext.md#a505e052f55e25cf10ac0431defb774ea));

101

[ 113](group__llext.md#ga0faf5a335199e63a424b122b03027c98)int [llext\_iterate](group__llext.md#ga0faf5a335199e63a424b122b03027c98)(int (\*fn)(struct [llext](structllext.md) \*ext, void \*arg), void \*arg);

114

[ 121](structllext__load__param.md)struct [llext\_load\_param](structllext__load__param.md) {

[ 123](structllext__load__param.md#a3c1683b0baafc636af18df3808d08031) bool [relocate\_local](structllext__load__param.md#a3c1683b0baafc636af18df3808d08031);

124};

125

[ 126](group__llext.md#ga15f6bd18c1693009be46641ce1b008c6)#define LLEXT\_LOAD\_PARAM\_DEFAULT {.relocate\_local = true,}

127

[ 144](group__llext.md#ga93c7d7f8987bd25e3dc486943785c8a1)int [llext\_load](group__llext.md#ga93c7d7f8987bd25e3dc486943785c8a1)(struct [llext\_loader](structllext__loader.md) \*loader, const char \*name, struct [llext](structllext.md) \*\*ext,

145 struct [llext\_load\_param](structllext__load__param.md) \*ldr\_parm);

146

[ 152](group__llext.md#gad3df7ed4d436846504c0047166eb929e)int [llext\_unload](group__llext.md#gad3df7ed4d436846504c0047166eb929e)(struct [llext](structllext.md) \*\*ext);

153

[ 163](group__llext.md#ga2554c14853cc809d63deb52096423838)const void \* const [llext\_find\_sym](group__llext.md#ga2554c14853cc809d63deb52096423838)(const struct [llext\_symtable](structllext__symtable.md) \*sym\_table, const char \*sym\_name);

164

[ 177](group__llext.md#gad50ad281c70093da99851723fc6af470)int [llext\_call\_fn](group__llext.md#gad50ad281c70093da99851723fc6af470)(struct [llext](structllext.md) \*ext, const char \*sym\_name);

178

[ 191](group__llext.md#ga64b13edf15b7c233b49c9c8edff884e6)int [llext\_add\_domain](group__llext.md#ga64b13edf15b7c233b49c9c8edff884e6)(struct [llext](structllext.md) \*ext, struct [k\_mem\_domain](structk__mem__domain.md) \*domain);

192

[ 206](group__llext.md#gad3ced43229d6f68622d71e5bc7234ca2)void [arch\_elf\_relocate](group__llext.md#gad3ced43229d6f68622d71e5bc7234ca2)([elf\_rela\_t](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) opaddr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) opval);

207

[ 215](group__llext.md#ga396bddb41c51415faf79e11fad44cb4e)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [llext\_find\_section](group__llext.md#ga396bddb41c51415faf79e11fad44cb4e)(struct [llext\_loader](structllext__loader.md) \*loader, const char \*search\_name);

216

[ 225](group__llext.md#ga437e19a2132007a3f9636e349a233d36)void [arch\_elf\_relocate\_local](group__llext.md#ga437e19a2132007a3f9636e349a233d36)(struct [llext\_loader](structllext__loader.md) \*loader, struct [llext](structllext.md) \*ext,

226 [elf\_rela\_t](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, size\_t got\_offset);

227

231

232#ifdef \_\_cplusplus

233}

234#endif

235

236#endif /\* ZEPHYR\_LLEXT\_H \*/

[elf.h](elf_8h.md)

[elf\_rela\_t](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea)

struct elf64\_rela elf\_rela\_t

**Definition** elf.h:451

[llext\_iterate](group__llext.md#ga0faf5a335199e63a424b122b03027c98)

int llext\_iterate(int(\*fn)(struct llext \*ext, void \*arg), void \*arg)

Iterate overall registered llext instances.

[llext\_find\_sym](group__llext.md#ga2554c14853cc809d63deb52096423838)

const void \*const llext\_find\_sym(const struct llext\_symtable \*sym\_table, const char \*sym\_name)

Find the address for an arbitrary symbol name.

[llext\_find\_section](group__llext.md#ga396bddb41c51415faf79e11fad44cb4e)

ssize\_t llext\_find\_section(struct llext\_loader \*loader, const char \*search\_name)

Find an ELF section.

[arch\_elf\_relocate\_local](group__llext.md#ga437e19a2132007a3f9636e349a233d36)

void arch\_elf\_relocate\_local(struct llext\_loader \*loader, struct llext \*ext, elf\_rela\_t \*rel, size\_t got\_offset)

Architecture specific function for updating addresses via relocation table.

[llext\_add\_domain](group__llext.md#ga64b13edf15b7c233b49c9c8edff884e6)

int llext\_add\_domain(struct llext \*ext, struct k\_mem\_domain \*domain)

Add the known memory partitions of the extension to a memory domain.

[LLEXT\_MEM\_PARTITIONS](group__llext.md#ga8740e267a2d59772fde6cda3df1711f2)

#define LLEXT\_MEM\_PARTITIONS

**Definition** llext.h:44

[llext\_mem](group__llext.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)

llext\_mem

List of ELF regions that are stored or referenced in the llext.

**Definition** llext.h:31

[llext\_load](group__llext.md#ga93c7d7f8987bd25e3dc486943785c8a1)

int llext\_load(struct llext\_loader \*loader, const char \*name, struct llext \*\*ext, struct llext\_load\_param \*ldr\_parm)

Load and link an extension.

[llext\_by\_name](group__llext.md#gaad89b0b44cf5c9528c3f8a0ce37a8fbe)

struct llext \* llext\_by\_name(const char \*name)

Find an llext by name.

[arch\_elf\_relocate](group__llext.md#gad3ced43229d6f68622d71e5bc7234ca2)

void arch\_elf\_relocate(elf\_rela\_t \*rel, uintptr\_t opaddr, uintptr\_t opval)

Architecture specific function for updating op codes given a relocation.

[llext\_unload](group__llext.md#gad3df7ed4d436846504c0047166eb929e)

int llext\_unload(struct llext \*\*ext)

Unload an extension.

[llext\_call\_fn](group__llext.md#gad50ad281c70093da99851723fc6af470)

int llext\_call\_fn(struct llext \*ext, const char \*sym\_name)

Call a function by name.

[LLEXT\_MEM\_SYMTAB](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a24549b7a2ee43076f5b8646e7fba5c81)

@ LLEXT\_MEM\_SYMTAB

**Definition** llext.h:37

[LLEXT\_MEM\_SHSTRTAB](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e)

@ LLEXT\_MEM\_SHSTRTAB

**Definition** llext.h:39

[LLEXT\_MEM\_TEXT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a4e7f671abb8e64ad6af7033a9439b7d0)

@ LLEXT\_MEM\_TEXT

**Definition** llext.h:32

[LLEXT\_MEM\_DATA](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a5e8658f79b74a0916e5d0abe8f852854)

@ LLEXT\_MEM\_DATA

**Definition** llext.h:33

[LLEXT\_MEM\_BSS](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e)

@ LLEXT\_MEM\_BSS

**Definition** llext.h:35

[LLEXT\_MEM\_RODATA](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a8ad55e9d9685edd3dfc4ede21854faeb)

@ LLEXT\_MEM\_RODATA

**Definition** llext.h:34

[LLEXT\_MEM\_COUNT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)

@ LLEXT\_MEM\_COUNT

**Definition** llext.h:41

[LLEXT\_MEM\_STRTAB](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17)

@ LLEXT\_MEM\_STRTAB

**Definition** llext.h:38

[LLEXT\_MEM\_EXPORT](group__llext.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae6ed486ed5719bf7058b2f95aa712028)

@ LLEXT\_MEM\_EXPORT

**Definition** llext.h:36

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[slist.h](slist_8h.md)

[stdbool.h](stdbool_8h.md)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[k\_mem\_domain](structk__mem__domain.md)

Memory Domain.

**Definition** mem\_domain.h:80

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

[llext\_load\_param](structllext__load__param.md)

llext loader parameters

**Definition** llext.h:121

[llext\_load\_param::relocate\_local](structllext__load__param.md#a3c1683b0baafc636af18df3808d08031)

bool relocate\_local

Should local relocation be performed.

**Definition** llext.h:123

[llext\_loader](structllext__loader.md)

Linkable loadable extension loader context.

**Definition** loader.h:29

[llext\_symtable](structllext__symtable.md)

A symbol table.

**Definition** symbol.h:60

[llext](structllext.md)

Linkable loadable extension.

**Definition** llext.h:51

[llext::mem\_size](structllext.md#a47cfcb60d773a6c16d2fda8cc5011a16)

size\_t mem\_size[LLEXT\_MEM\_COUNT]

Size of each stored section.

**Definition** llext.h:72

[llext::sym\_tab](structllext.md#a4f67c792a963ac124f32b2d7880f9cdf)

struct llext\_symtable sym\_tab

**Definition** llext.h:84

[llext::name](structllext.md#a505e052f55e25cf10ac0431defb774ea)

char name[16]

Name of the llext.

**Definition** llext.h:63

[llext::alloc\_size](structllext.md#a566e46e600e9b90f9d4b570ef007e6a6)

size\_t alloc\_size

Total llext allocation size.

**Definition** llext.h:75

[llext::use\_count](structllext.md#a61c5ca5c740f5bb14791f11354b68101)

unsigned int use\_count

Extension use counter, prevents unloading while in use.

**Definition** llext.h:90

[llext::mem\_on\_heap](structllext.md#a7556c195516041439547d891897f4a44)

bool mem\_on\_heap[LLEXT\_MEM\_COUNT]

Is the memory for this section allocated on heap?

**Definition** llext.h:69

[llext::exp\_tab](structllext.md#a76cc3ef7989f2d4bfaeedadd05738de2)

struct llext\_symtable exp\_tab

Exported symbols from the llext, may be linked against by other llext.

**Definition** llext.h:87

[llext::mem](structllext.md#ae9d529433f30ed659758c9b29c9b96bd)

void \* mem[LLEXT\_MEM\_COUNT]

Lookup table of llext memory regions.

**Definition** llext.h:66

[symbol.h](symbol_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [llext.h](llext_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
