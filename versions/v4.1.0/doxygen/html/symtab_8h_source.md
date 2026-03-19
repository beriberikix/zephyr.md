---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/symtab_8h_source.html
original_path: doxygen/html/symtab_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

symtab.h

[Go to the documentation of this file.](symtab_8h.md)

1/\*

2 \* Copyright (c) 2024 Meta Platforms

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DEBUG\_SYMTAB\_H\_

8#define ZEPHYR\_INCLUDE\_DEBUG\_SYMTAB\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

25

26struct z\_symtab\_entry {

27 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset;

28 const char \*const name;

29};

30

34

[ 35](structsymtab__info.md)struct [symtab\_info](structsymtab__info.md) {

36 /\* Absolute address of the first symbol \*/

[ 37](structsymtab__info.md#a86d6af07f0ddb6c95ee6db63307a0783) const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [first\_addr](structsymtab__info.md#a86d6af07f0ddb6c95ee6db63307a0783);

38 /\* Number of symbol entries \*/

[ 39](structsymtab__info.md#a8d2bb0574287422a94c5d6074cfda066) const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [length](structsymtab__info.md#a8d2bb0574287422a94c5d6074cfda066);

40 /\* Symbol entries \*/

[ 41](structsymtab__info.md#a69ad14fd05738735036cab84ddad02bc) const struct z\_symtab\_entry \*const [entries](structsymtab__info.md#a69ad14fd05738735036cab84ddad02bc);

42};

43

[ 49](group__symtab__apis.md#ga2f1c4fa3cc113c2e5f47c5bbcd337e32)const struct [symtab\_info](structsymtab__info.md) \*[symtab\_get](group__symtab__apis.md#ga2f1c4fa3cc113c2e5f47c5bbcd337e32)(void);

50

[ 60](group__symtab__apis.md#gac5927cf3f4e0bf3e1b27b397290e44c5)const char \*[symtab\_find\_symbol\_name](group__symtab__apis.md#gac5927cf3f4e0bf3e1b27b397290e44c5)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*offset);

61

65

66#ifdef \_\_cplusplus

67}

68#endif

69

70#endif /\* ZEPHYR\_INCLUDE\_DEBUG\_SYMTAB\_H\_ \*/

[symtab\_get](group__symtab__apis.md#ga2f1c4fa3cc113c2e5f47c5bbcd337e32)

const struct symtab\_info \* symtab\_get(void)

Get the pointer to the symbol table.

[symtab\_find\_symbol\_name](group__symtab__apis.md#gac5927cf3f4e0bf3e1b27b397290e44c5)

const char \* symtab\_find\_symbol\_name(uintptr\_t addr, uint32\_t \*offset)

Find the symbol name with a binary search.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[symtab\_info](structsymtab__info.md)

**Definition** symtab.h:35

[symtab\_info::entries](structsymtab__info.md#a69ad14fd05738735036cab84ddad02bc)

const struct z\_symtab\_entry \*const entries

**Definition** symtab.h:41

[symtab\_info::first\_addr](structsymtab__info.md#a86d6af07f0ddb6c95ee6db63307a0783)

const uintptr\_t first\_addr

**Definition** symtab.h:37

[symtab\_info::length](structsymtab__info.md#a8d2bb0574287422a94c5d6074cfda066)

const uint32\_t length

**Definition** symtab.h:39

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [symtab.h](symtab_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
