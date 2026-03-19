---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mem__attr_8h_source.html
original_path: doxygen/html/mem__attr_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mem\_attr.h

[Go to the documentation of this file.](mem__attr_8h.md)

1/\*

2 \* Copyright (c) 2023 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_MEM\_ATTR\_H\_

8#define ZEPHYR\_INCLUDE\_MEM\_ATTR\_H\_

9

16

17#include <stddef.h>

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[zephyr/dt-bindings/memory-attr/memory-attr.h](memory-attr_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

26

27#define \_\_MEM\_ATTR zephyr\_memory\_attr

28

29#define \_FILTER(node\_id, fn) \

30 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, \_\_MEM\_ATTR), \

31 (fn(node\_id)), \

32 ())

33

35

[ 47](group__memory__attr__interface.md#ga316e41444a0db6bb78ec0c1c4bdc832b)#define DT\_MEMORY\_ATTR\_FOREACH\_STATUS\_OKAY\_NODE(fn) \

48 DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS(\_FILTER, fn)

49

[ 56](structmem__attr__region__t.md)struct [mem\_attr\_region\_t](structmem__attr__region__t.md) {

[ 58](structmem__attr__region__t.md#a84906ca493441f65f68409f1798e960e) const char \*[dt\_name](structmem__attr__region__t.md#a84906ca493441f65f68409f1798e960e);

[ 60](structmem__attr__region__t.md#a0f5363766454ed56fa00152b3bcedadd) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [dt\_addr](structmem__attr__region__t.md#a0f5363766454ed56fa00152b3bcedadd);

[ 62](structmem__attr__region__t.md#a3931b272d0e7b3ea0ced85888356a2d1) size\_t [dt\_size](structmem__attr__region__t.md#a3931b272d0e7b3ea0ced85888356a2d1);

[ 64](structmem__attr__region__t.md#ad853fe05ac7015b9229ad49a4ddbb719) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dt\_attr](structmem__attr__region__t.md#ad853fe05ac7015b9229ad49a4ddbb719);

65};

66

[ 77](group__memory__attr__interface.md#gadcf93c67fe564d65064f5f6175d7089f)size\_t [mem\_attr\_get\_regions](group__memory__attr__interface.md#gadcf93c67fe564d65064f5f6175d7089f)(const struct [mem\_attr\_region\_t](structmem__attr__region__t.md) \*\*region);

78

[ 106](group__memory__attr__interface.md#gac599eafdb0be231c0105b05eb76b657b)int [mem\_attr\_check\_buf](group__memory__attr__interface.md#gac599eafdb0be231c0105b05eb76b657b)(void \*addr, size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) attr);

107

108#ifdef \_\_cplusplus

109}

110#endif

111

113

114#endif /\* ZEPHYR\_INCLUDE\_MEM\_ATTR\_H\_ \*/

[mem\_attr\_check\_buf](group__memory__attr__interface.md#gac599eafdb0be231c0105b05eb76b657b)

int mem\_attr\_check\_buf(void \*addr, size\_t size, uint32\_t attr)

Check if a buffer has correct size and attributes.

[mem\_attr\_get\_regions](group__memory__attr__interface.md#gadcf93c67fe564d65064f5f6175d7089f)

size\_t mem\_attr\_get\_regions(const struct mem\_attr\_region\_t \*\*region)

Get the list of memory regions.

[types.h](include_2zephyr_2types_8h.md)

[memory-attr.h](memory-attr_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[mem\_attr\_region\_t](structmem__attr__region__t.md)

memory-attr region structure.

**Definition** mem\_attr.h:56

[mem\_attr\_region\_t::dt\_addr](structmem__attr__region__t.md#a0f5363766454ed56fa00152b3bcedadd)

uintptr\_t dt\_addr

Memory region physical address.

**Definition** mem\_attr.h:60

[mem\_attr\_region\_t::dt\_size](structmem__attr__region__t.md#a3931b272d0e7b3ea0ced85888356a2d1)

size\_t dt\_size

Memory region size.

**Definition** mem\_attr.h:62

[mem\_attr\_region\_t::dt\_name](structmem__attr__region__t.md#a84906ca493441f65f68409f1798e960e)

const char \* dt\_name

Memory node full name.

**Definition** mem\_attr.h:58

[mem\_attr\_region\_t::dt\_attr](structmem__attr__region__t.md#ad853fe05ac7015b9229ad49a4ddbb719)

uint32\_t dt\_attr

Memory region attributes.

**Definition** mem\_attr.h:64

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mem\_mgmt](dir_5ee27bc867ccb4004a26ac2b9a5fc96f.md)
- [mem\_attr.h](mem__attr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
