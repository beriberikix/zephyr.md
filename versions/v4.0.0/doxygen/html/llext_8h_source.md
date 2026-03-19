---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/llext_8h_source.html
original_path: doxygen/html/llext_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext.h

[Go to the documentation of this file.](llext_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \* Copyright (c) 2024 Schneider Electric

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_LLEXT\_H

9#define ZEPHYR\_LLEXT\_H

10

11#include <[zephyr/sys/slist.h](slist_8h.md)>

12#include <[zephyr/llext/elf.h](llext_2elf_8h.md)>

13#include <[zephyr/llext/symbol.h](symbol_8h.md)>

14#include <[zephyr/kernel.h](kernel_8h.md)>

15#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

16#include <[stdbool.h](stdbool_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

35

[ 44](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) {

[ 45](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a4e7f671abb8e64ad6af7033a9439b7d0) [LLEXT\_MEM\_TEXT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a4e7f671abb8e64ad6af7033a9439b7d0),

[ 46](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a5e8658f79b74a0916e5d0abe8f852854) [LLEXT\_MEM\_DATA](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a5e8658f79b74a0916e5d0abe8f852854),

[ 47](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a8ad55e9d9685edd3dfc4ede21854faeb) [LLEXT\_MEM\_RODATA](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a8ad55e9d9685edd3dfc4ede21854faeb),

[ 48](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e) [LLEXT\_MEM\_BSS](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e),

[ 49](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae6ed486ed5719bf7058b2f95aa712028) [LLEXT\_MEM\_EXPORT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae6ed486ed5719bf7058b2f95aa712028),

[ 50](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a24549b7a2ee43076f5b8646e7fba5c81) [LLEXT\_MEM\_SYMTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a24549b7a2ee43076f5b8646e7fba5c81),

[ 51](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17) [LLEXT\_MEM\_STRTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17),

[ 52](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e) [LLEXT\_MEM\_SHSTRTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e),

[ 53](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a812e884e2c4a3c6430d91998b75d7974) [LLEXT\_MEM\_PREINIT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a812e884e2c4a3c6430d91998b75d7974),

[ 54](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ab119ace11d5d6ca1dca32ef4ce4cef11) [LLEXT\_MEM\_INIT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ab119ace11d5d6ca1dca32ef4ce4cef11),

[ 55](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953abfece5d78fbb60c5723eb39eb0df1c9d) [LLEXT\_MEM\_FINI](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953abfece5d78fbb60c5723eb39eb0df1c9d),

56

[ 57](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265) [LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265),

58};

59

61

62/\* Number of memory partitions used by LLEXT \*/

63#define LLEXT\_MEM\_PARTITIONS (LLEXT\_MEM\_BSS+1)

64

65struct [llext\_loader](structllext__loader.md);

67

68/\* Maximim number of dependency LLEXTs \*/

[ 69](group__llext__apis.md#ga09b483779bce7612bfaba519e1ecb9e0)#define LLEXT\_MAX\_DEPENDENCIES 8

70

[ 77](structllext.md)struct [llext](structllext.md) {

79 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_llext\_list;

80

81#ifdef CONFIG\_USERSPACE

82 struct [k\_mem\_partition](structk__mem__partition.md) mem\_parts[LLEXT\_MEM\_PARTITIONS];

83 struct [k\_mem\_domain](structk__mem__domain.md) mem\_domain;

84#endif

85

87

[ 89](structllext.md#a505e052f55e25cf10ac0431defb774ea) char [name](structllext.md#a505e052f55e25cf10ac0431defb774ea)[16];

90

[ 92](structllext.md#ae9d529433f30ed659758c9b29c9b96bd) void \*[mem](structllext.md#ae9d529433f30ed659758c9b29c9b96bd)[[LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)];

93

[ 95](structllext.md#a7556c195516041439547d891897f4a44) bool [mem\_on\_heap](structllext.md#a7556c195516041439547d891897f4a44)[[LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)];

96

[ 98](structllext.md#a47cfcb60d773a6c16d2fda8cc5011a16) size\_t [mem\_size](structllext.md#a47cfcb60d773a6c16d2fda8cc5011a16)[[LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)];

99

[ 101](structllext.md#a566e46e600e9b90f9d4b570ef007e6a6) size\_t [alloc\_size](structllext.md#a566e46e600e9b90f9d4b570ef007e6a6);

102

[ 109](structllext.md#a4f67c792a963ac124f32b2d7880f9cdf) struct [llext\_symtable](structllext__symtable.md) [sym\_tab](structllext.md#a4f67c792a963ac124f32b2d7880f9cdf);

110

[ 116](structllext.md#a76cc3ef7989f2d4bfaeedadd05738de2) struct [llext\_symtable](structllext__symtable.md) [exp\_tab](structllext.md#a76cc3ef7989f2d4bfaeedadd05738de2);

117

[ 119](structllext.md#a61c5ca5c740f5bb14791f11354b68101) unsigned int [use\_count](structllext.md#a61c5ca5c740f5bb14791f11354b68101);

120

[ 122](structllext.md#a6f93ccee334d533b5d0050fabf782780) struct [llext](structllext.md) \*[dependency](structllext.md#a6f93ccee334d533b5d0050fabf782780)[[LLEXT\_MAX\_DEPENDENCIES](group__llext__apis.md#ga09b483779bce7612bfaba519e1ecb9e0)];

123};

124

[ 130](structllext__load__param.md)struct [llext\_load\_param](structllext__load__param.md) {

[ 132](structllext__load__param.md#a3c1683b0baafc636af18df3808d08031) bool [relocate\_local](structllext__load__param.md#a3c1683b0baafc636af18df3808d08031);

[ 137](structllext__load__param.md#a5e9fdb238b8a706155a873e82e35393d) bool [pre\_located](structllext__load__param.md#a5e9fdb238b8a706155a873e82e35393d);

[ 143](structllext__load__param.md#af3d61fa83c93361e4c5292b078d51a93) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[section\_detached](structllext__load__param.md#af3d61fa83c93361e4c5292b078d51a93))(const [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) \*shdr);

144};

145

[ 147](group__llext__apis.md#ga15f6bd18c1693009be46641ce1b008c6)#define LLEXT\_LOAD\_PARAM\_DEFAULT { .relocate\_local = true, }

148

[ 155](group__llext__apis.md#gaad89b0b44cf5c9528c3f8a0ce37a8fbe)struct [llext](structllext.md) \*[llext\_by\_name](group__llext__apis.md#gaad89b0b44cf5c9528c3f8a0ce37a8fbe)(const char \*[name](structllext.md#a505e052f55e25cf10ac0431defb774ea));

156

[ 168](group__llext__apis.md#ga0faf5a335199e63a424b122b03027c98)int [llext\_iterate](group__llext__apis.md#ga0faf5a335199e63a424b122b03027c98)(int (\*fn)(struct [llext](structllext.md) \*ext, void \*arg), void \*arg);

169

[ 185](group__llext__apis.md#ga0a4c3db30bc3ec7aa8a9b0e076af7157)int [llext\_load](group__llext__apis.md#ga0a4c3db30bc3ec7aa8a9b0e076af7157)(struct [llext\_loader](structllext__loader.md) \*loader, const char \*[name](structllext.md#a505e052f55e25cf10ac0431defb774ea), struct [llext](structllext.md) \*\*ext,

186 const struct [llext\_load\_param](structllext__load__param.md) \*ldr\_parm);

187

[ 193](group__llext__apis.md#gad3df7ed4d436846504c0047166eb929e)int [llext\_unload](group__llext__apis.md#gad3df7ed4d436846504c0047166eb929e)(struct [llext](structllext.md) \*\*ext);

194

[ 196](group__llext__apis.md#ga0c27a8648deab424948eeb776a3de5ea)typedef void (\*[llext\_entry\_fn\_t](group__llext__apis.md#ga0c27a8648deab424948eeb776a3de5ea))(void \*user\_data);

197

[ 209](group__llext__apis.md#ga01c0c23dba5ff1aa9da42c7895cc7fab)int [llext\_bringup](group__llext__apis.md#ga01c0c23dba5ff1aa9da42c7895cc7fab)(struct [llext](structllext.md) \*ext);

210

[ 223](group__llext__apis.md#gae061bb6100ad394fcaca7751ff3dadba)int [llext\_teardown](group__llext__apis.md#gae061bb6100ad394fcaca7751ff3dadba)(struct [llext](structllext.md) \*ext);

224

[ 241](group__llext__apis.md#ga809f7a7976b4436dad31aa03d9ea3729)void [llext\_bootstrap](group__llext__apis.md#ga809f7a7976b4436dad31aa03d9ea3729)(struct [llext](structllext.md) \*ext, [llext\_entry\_fn\_t](group__llext__apis.md#ga0c27a8648deab424948eeb776a3de5ea) entry\_fn, void \*user\_data);

242

[ 261](group__llext__apis.md#ga201b2c853cb3ff35aaa7b891dad5464c)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [llext\_get\_fn\_table](group__llext__apis.md#ga201b2c853cb3ff35aaa7b891dad5464c)(struct [llext](structllext.md) \*ext, bool is\_init, void \*buf, size\_t size);

262

[ 275](group__llext__apis.md#gac0982fad15a62723a5cad3f7edd6ba3e)const void \*[llext\_find\_sym](group__llext__apis.md#gac0982fad15a62723a5cad3f7edd6ba3e)(const struct [llext\_symtable](structllext__symtable.md) \*sym\_table, const char \*sym\_name);

276

[ 289](group__llext__apis.md#gad50ad281c70093da99851723fc6af470)int [llext\_call\_fn](group__llext__apis.md#gad50ad281c70093da99851723fc6af470)(struct [llext](structllext.md) \*ext, const char \*sym\_name);

290

[ 304](group__llext__apis.md#ga64b13edf15b7c233b49c9c8edff884e6)int [llext\_add\_domain](group__llext__apis.md#ga64b13edf15b7c233b49c9c8edff884e6)(struct [llext](structllext.md) \*ext, struct [k\_mem\_domain](structk__mem__domain.md) \*domain);

305

[ 324](group__llext__apis.md#ga1f1a02ac08db72db8cd8a01fa91c95cb)int [arch\_elf\_relocate](group__llext__apis.md#ga1f1a02ac08db72db8cd8a01fa91c95cb)([elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) loc,

325 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) sym\_base\_addr, const char \*sym\_name, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) load\_bias);

326

[ 336](group__llext__apis.md#ga396bddb41c51415faf79e11fad44cb4e)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [llext\_find\_section](group__llext__apis.md#ga396bddb41c51415faf79e11fad44cb4e)(struct [llext\_loader](structllext__loader.md) \*loader, const char \*search\_name);

337

[ 347](group__llext__apis.md#ga3c36cb7b2337de143e9381b38e70285c)void [arch\_elf\_relocate\_local](group__llext__apis.md#ga3c36cb7b2337de143e9381b38e70285c)(struct [llext\_loader](structllext__loader.md) \*loader, struct [llext](structllext.md) \*ext,

348 const [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) \*rel, const [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) \*sym, size\_t got\_offset);

349

353

354#ifdef \_\_cplusplus

355}

356#endif

357

358#include <zephyr/syscalls/llext.h>

359

360#endif /\* ZEPHYR\_LLEXT\_H \*/

[llext\_bringup](group__llext__apis.md#ga01c0c23dba5ff1aa9da42c7895cc7fab)

int llext\_bringup(struct llext \*ext)

Calls bringup functions for an extension.

[LLEXT\_MAX\_DEPENDENCIES](group__llext__apis.md#ga09b483779bce7612bfaba519e1ecb9e0)

#define LLEXT\_MAX\_DEPENDENCIES

**Definition** llext.h:69

[llext\_load](group__llext__apis.md#ga0a4c3db30bc3ec7aa8a9b0e076af7157)

int llext\_load(struct llext\_loader \*loader, const char \*name, struct llext \*\*ext, const struct llext\_load\_param \*ldr\_parm)

Load and link an extension.

[llext\_entry\_fn\_t](group__llext__apis.md#ga0c27a8648deab424948eeb776a3de5ea)

void(\* llext\_entry\_fn\_t)(void \*user\_data)

Entry point function signature for an extension.

**Definition** llext.h:196

[llext\_iterate](group__llext__apis.md#ga0faf5a335199e63a424b122b03027c98)

int llext\_iterate(int(\*fn)(struct llext \*ext, void \*arg), void \*arg)

Iterate over all loaded extensions.

[arch\_elf\_relocate](group__llext__apis.md#ga1f1a02ac08db72db8cd8a01fa91c95cb)

int arch\_elf\_relocate(elf\_rela\_t \*rel, uintptr\_t loc, uintptr\_t sym\_base\_addr, const char \*sym\_name, uintptr\_t load\_bias)

Architecture specific opcode update function.

[llext\_get\_fn\_table](group__llext__apis.md#ga201b2c853cb3ff35aaa7b891dad5464c)

ssize\_t llext\_get\_fn\_table(struct llext \*ext, bool is\_init, void \*buf, size\_t size)

Get pointers to setup or cleanup functions for an extension.

[llext\_find\_section](group__llext__apis.md#ga396bddb41c51415faf79e11fad44cb4e)

ssize\_t llext\_find\_section(struct llext\_loader \*loader, const char \*search\_name)

Locates an ELF section in the file.

[arch\_elf\_relocate\_local](group__llext__apis.md#ga3c36cb7b2337de143e9381b38e70285c)

void arch\_elf\_relocate\_local(struct llext\_loader \*loader, struct llext \*ext, const elf\_rela\_t \*rel, const elf\_sym\_t \*sym, size\_t got\_offset)

Architecture specific function for updating addresses via relocation table.

[llext\_add\_domain](group__llext__apis.md#ga64b13edf15b7c233b49c9c8edff884e6)

int llext\_add\_domain(struct llext \*ext, struct k\_mem\_domain \*domain)

Add an extension to a memory domain.

[llext\_bootstrap](group__llext__apis.md#ga809f7a7976b4436dad31aa03d9ea3729)

void llext\_bootstrap(struct llext \*ext, llext\_entry\_fn\_t entry\_fn, void \*user\_data)

Bring up, execute, and teardown an extension.

[llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)

llext\_mem

List of memory regions stored or referenced in the LLEXT subsystem.

**Definition** llext.h:44

[llext\_by\_name](group__llext__apis.md#gaad89b0b44cf5c9528c3f8a0ce37a8fbe)

struct llext \* llext\_by\_name(const char \*name)

Find an llext by name.

[llext\_find\_sym](group__llext__apis.md#gac0982fad15a62723a5cad3f7edd6ba3e)

const void \* llext\_find\_sym(const struct llext\_symtable \*sym\_table, const char \*sym\_name)

Find the address for an arbitrary symbol.

[llext\_unload](group__llext__apis.md#gad3df7ed4d436846504c0047166eb929e)

int llext\_unload(struct llext \*\*ext)

Unload an extension.

[llext\_call\_fn](group__llext__apis.md#gad50ad281c70093da99851723fc6af470)

int llext\_call\_fn(struct llext \*ext, const char \*sym\_name)

Call a function by name.

[llext\_teardown](group__llext__apis.md#gae061bb6100ad394fcaca7751ff3dadba)

int llext\_teardown(struct llext \*ext)

Calls teardown functions for an extension.

[LLEXT\_MEM\_SYMTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a24549b7a2ee43076f5b8646e7fba5c81)

@ LLEXT\_MEM\_SYMTAB

Symbol table.

**Definition** llext.h:50

[LLEXT\_MEM\_SHSTRTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a325e4d3b4ecdbdb2fec8451fef5b582e)

@ LLEXT\_MEM\_SHSTRTAB

Section name strings.

**Definition** llext.h:52

[LLEXT\_MEM\_TEXT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a4e7f671abb8e64ad6af7033a9439b7d0)

@ LLEXT\_MEM\_TEXT

Executable code.

**Definition** llext.h:45

[LLEXT\_MEM\_DATA](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a5e8658f79b74a0916e5d0abe8f852854)

@ LLEXT\_MEM\_DATA

Initialized data.

**Definition** llext.h:46

[LLEXT\_MEM\_PREINIT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a812e884e2c4a3c6430d91998b75d7974)

@ LLEXT\_MEM\_PREINIT

Array of early setup functions.

**Definition** llext.h:53

[LLEXT\_MEM\_BSS](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a84ec2446a021fefa9e6786ad58d6986e)

@ LLEXT\_MEM\_BSS

Uninitialized data.

**Definition** llext.h:48

[LLEXT\_MEM\_RODATA](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953a8ad55e9d9685edd3dfc4ede21854faeb)

@ LLEXT\_MEM\_RODATA

Read-only data.

**Definition** llext.h:47

[LLEXT\_MEM\_INIT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ab119ace11d5d6ca1dca32ef4ce4cef11)

@ LLEXT\_MEM\_INIT

Array of setup functions.

**Definition** llext.h:54

[LLEXT\_MEM\_FINI](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953abfece5d78fbb60c5723eb39eb0df1c9d)

@ LLEXT\_MEM\_FINI

Array of cleanup functions.

**Definition** llext.h:55

[LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)

@ LLEXT\_MEM\_COUNT

Number of regions managed by LLEXT.

**Definition** llext.h:57

[LLEXT\_MEM\_STRTAB](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae0ecbbcbe2d8143f5fac4783f7157c17)

@ LLEXT\_MEM\_STRTAB

Symbol name strings.

**Definition** llext.h:51

[LLEXT\_MEM\_EXPORT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ae6ed486ed5719bf7058b2f95aa712028)

@ LLEXT\_MEM\_EXPORT

Exported symbol table.

**Definition** llext.h:49

[elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e)

struct elf64\_sym elf\_sym\_t

Machine sized symbol struct.

**Definition** elf.h:475

[elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd)

struct elf64\_shdr elf\_shdr\_t

Machine sized section header structure.

**Definition** elf.h:461

[elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea)

struct elf64\_rela elf\_rela\_t

Machine sized relocation struct with addend.

**Definition** elf.h:473

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[elf.h](llext_2elf_8h.md)

Data structures and constants defined in the ELF specification.

[slist.h](slist_8h.md)

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

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

Advanced llext\_load parameters.

**Definition** llext.h:130

[llext\_load\_param::relocate\_local](structllext__load__param.md#a3c1683b0baafc636af18df3808d08031)

bool relocate\_local

Perform local relocation.

**Definition** llext.h:132

[llext\_load\_param::pre\_located](structllext__load__param.md#a5e9fdb238b8a706155a873e82e35393d)

bool pre\_located

Use the virtual symbol addresses from the ELF, not addresses within the memory buffer,...

**Definition** llext.h:137

[llext\_load\_param::section\_detached](structllext__load__param.md#af3d61fa83c93361e4c5292b078d51a93)

bool(\* section\_detached)(const elf\_shdr\_t \*shdr)

Extensions can implement custom ELF sections to be loaded in specific memory regions,...

**Definition** llext.h:143

[llext\_loader](structllext__loader.md)

Linkable loadable extension loader context.

**Definition** loader.h:42

[llext\_symtable](structllext__symtable.md)

A symbol table.

**Definition** symbol.h:81

[llext](structllext.md)

Structure describing a linkable loadable extension.

**Definition** llext.h:77

[llext::mem\_size](structllext.md#a47cfcb60d773a6c16d2fda8cc5011a16)

size\_t mem\_size[LLEXT\_MEM\_COUNT]

Size of each stored region.

**Definition** llext.h:98

[llext::sym\_tab](structllext.md#a4f67c792a963ac124f32b2d7880f9cdf)

struct llext\_symtable sym\_tab

Table of all global symbols in the extension; used internally as part of the linking process.

**Definition** llext.h:109

[llext::name](structllext.md#a505e052f55e25cf10ac0431defb774ea)

char name[16]

Name of the llext.

**Definition** llext.h:89

[llext::alloc\_size](structllext.md#a566e46e600e9b90f9d4b570ef007e6a6)

size\_t alloc\_size

Total llext allocation size.

**Definition** llext.h:101

[llext::use\_count](structllext.md#a61c5ca5c740f5bb14791f11354b68101)

unsigned int use\_count

Extension use counter, prevents unloading while in use.

**Definition** llext.h:119

[llext::dependency](structllext.md#a6f93ccee334d533b5d0050fabf782780)

struct llext \* dependency[8]

Array of extensions, whose symbols this extension accesses.

**Definition** llext.h:122

[llext::mem\_on\_heap](structllext.md#a7556c195516041439547d891897f4a44)

bool mem\_on\_heap[LLEXT\_MEM\_COUNT]

Is the memory for this region allocated on heap?

**Definition** llext.h:95

[llext::exp\_tab](structllext.md#a76cc3ef7989f2d4bfaeedadd05738de2)

struct llext\_symtable exp\_tab

Table of symbols exported by the llext via LL\_EXTENSION\_SYMBOL.

**Definition** llext.h:116

[llext::mem](structllext.md#ae9d529433f30ed659758c9b29c9b96bd)

void \* mem[LLEXT\_MEM\_COUNT]

Lookup table of memory regions.

**Definition** llext.h:92

[symbol.h](symbol_8h.md)

Linkable loadable extension symbol definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [llext.h](llext_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
