---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/loader_8h_source.html
original_path: doxygen/html/loader_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

loader.h

[Go to the documentation of this file.](loader_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LLEXT\_LOADER\_H

8#define ZEPHYR\_LLEXT\_LOADER\_H

9

10#include <[zephyr/llext/elf.h](llext_2elf_8h.md)>

11#include <stddef.h>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

28

29#include <[zephyr/llext/llext.h](llext_8h.md)>

30

32struct llext\_elf\_sect\_map; /\* defined in llext\_priv.h \*/

34

[ 48](group__llext__loader__apis.md#ga8e04f364aef19cf45843cc97cc702f24)enum [llext\_storage\_type](group__llext__loader__apis.md#ga8e04f364aef19cf45843cc97cc702f24) {

[ 55](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6) [LLEXT\_STORAGE\_TEMPORARY](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6),

[ 62](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0) [LLEXT\_STORAGE\_PERSISTENT](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0),

[ 70](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b) [LLEXT\_STORAGE\_WRITABLE](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b),

71};

72

[ 80](structllext__loader.md)struct [llext\_loader](structllext__loader.md) {

[ 88](structllext__loader.md#a3034e439e3c55a2ed874cf2db6aba46e) int (\*[prepare](structllext__loader.md#a3034e439e3c55a2ed874cf2db6aba46e))(struct [llext\_loader](structllext__loader.md) \*ldr);

89

[ 102](structllext__loader.md#a29a16df55b72bc299b338036437f53e0) int (\*[read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0))(struct [llext\_loader](structllext__loader.md) \*ldr, void \*out, size\_t len);

103

[ 115](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d) int (\*[seek](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d))(struct [llext\_loader](structllext__loader.md) \*ldr, size\_t pos);

116

[ 127](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6) void \*(\*peek)(struct [llext\_loader](structllext__loader.md) \*ldr, size\_t pos);

128

[ 134](structllext__loader.md#a7c0ea7bce0a56ccf98e120a52e362b37) void (\*[finalize](structllext__loader.md#a7c0ea7bce0a56ccf98e120a52e362b37))(struct [llext\_loader](structllext__loader.md) \*ldr);

135

[ 139](structllext__loader.md#a1b82b69501e174b6a0f24ef356abbf16) enum [llext\_storage\_type](group__llext__loader__apis.md#ga8e04f364aef19cf45843cc97cc702f24) [storage](structllext__loader.md#a1b82b69501e174b6a0f24ef356abbf16);

140

142 [elf\_ehdr\_t](group__llext__elf.md#gab39a1763256a6b9ccccf8b89836cd192) hdr;

143 [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) sects[[LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)];

144 struct llext\_elf\_sect\_map \*sect\_map;

146};

147

149static inline int llext\_prepare(struct [llext\_loader](structllext__loader.md) \*l)

150{

151 if (l->[prepare](structllext__loader.md#a3034e439e3c55a2ed874cf2db6aba46e)) {

152 return l->[prepare](structllext__loader.md#a3034e439e3c55a2ed874cf2db6aba46e)(l);

153 }

154

155 return 0;

156}

157

158static inline int llext\_read(struct [llext\_loader](structllext__loader.md) \*l, void \*buf, size\_t len)

159{

160 return l->[read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0)(l, buf, len);

161}

162

163static inline int llext\_seek(struct [llext\_loader](structllext__loader.md) \*l, size\_t pos)

164{

165 return l->[seek](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d)(l, pos);

166}

167

168static inline void \*llext\_peek(struct [llext\_loader](structllext__loader.md) \*l, size\_t pos)

169{

170 if (l->[peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)) {

171 return l->[peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)(l, pos);

172 }

173

174 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

175}

176

177static inline void llext\_finalize(struct [llext\_loader](structllext__loader.md) \*l)

178{

179 if (l->[finalize](structllext__loader.md#a7c0ea7bce0a56ccf98e120a52e362b37)) {

180 l->[finalize](structllext__loader.md#a7c0ea7bce0a56ccf98e120a52e362b37)(l);

181 }

182}

183/\* @endcond \*/

184

188

189#ifdef \_\_cplusplus

190}

191#endif

192

193#endif /\* ZEPHYR\_LLEXT\_LOADER\_H \*/

[LLEXT\_MEM\_COUNT](group__llext__apis.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)

@ LLEXT\_MEM\_COUNT

Number of regions managed by LLEXT.

**Definition** llext.h:57

[elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd)

struct elf64\_shdr elf\_shdr\_t

Machine sized section header structure.

**Definition** elf.h:463

[elf\_ehdr\_t](group__llext__elf.md#gab39a1763256a6b9ccccf8b89836cd192)

struct elf64\_ehdr elf\_ehdr\_t

Dynamic features currently not used by LLEXT.

**Definition** elf.h:461

[llext\_storage\_type](group__llext__loader__apis.md#ga8e04f364aef19cf45843cc97cc702f24)

llext\_storage\_type

Storage type for the ELF data to be loaded.

**Definition** loader.h:48

[LLEXT\_STORAGE\_TEMPORARY](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6)

@ LLEXT\_STORAGE\_TEMPORARY

ELF data is only available during llext\_load(); even if the loader supports directly accessing the me...

**Definition** loader.h:55

[LLEXT\_STORAGE\_WRITABLE](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b)

@ LLEXT\_STORAGE\_WRITABLE

ELF data is stored in a writable memory buffer that is guaranteed to be always accessible for as long...

**Definition** loader.h:70

[LLEXT\_STORAGE\_PERSISTENT](group__llext__loader__apis.md#gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0)

@ LLEXT\_STORAGE\_PERSISTENT

ELF data is stored in a read-only buffer that is guaranteed to be always accessible for as long as th...

**Definition** loader.h:62

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[elf.h](llext_2elf_8h.md)

Data structures and constants defined in the ELF specification.

[llext.h](llext_8h.md)

Support for linkable loadable extensions.

[llext\_loader](structllext__loader.md)

Linkable loadable extension loader context.

**Definition** loader.h:80

[llext\_loader::storage](structllext__loader.md#a1b82b69501e174b6a0f24ef356abbf16)

enum llext\_storage\_type storage

Storage type of the underlying data accessed by this loader.

**Definition** loader.h:139

[llext\_loader::seek](structllext__loader.md#a2376c3774af219972e164b0ee8a6bb6d)

int(\* seek)(struct llext\_loader \*ldr, size\_t pos)

Function to seek to a new absolute location in the stream.

**Definition** loader.h:115

[llext\_loader::read](structllext__loader.md#a29a16df55b72bc299b338036437f53e0)

int(\* read)(struct llext\_loader \*ldr, void \*out, size\_t len)

Function to read (copy) from the loader.

**Definition** loader.h:102

[llext\_loader::prepare](structllext__loader.md#a3034e439e3c55a2ed874cf2db6aba46e)

int(\* prepare)(struct llext\_loader \*ldr)

Optional function to prepare the loader for loading extension.

**Definition** loader.h:88

[llext\_loader::finalize](structllext__loader.md#a7c0ea7bce0a56ccf98e120a52e362b37)

void(\* finalize)(struct llext\_loader \*ldr)

Optional function to clean after the extension has been loaded or error occurred.

**Definition** loader.h:134

[llext\_loader::peek](structllext__loader.md#af5452f4b4f1099379d110c1bcd7773f6)

void \*(\* peek)(struct llext\_loader \*ldr, size\_t pos)

Optional function to peek at an absolute location in the ELF.

**Definition** loader.h:127

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [loader.h](loader_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
