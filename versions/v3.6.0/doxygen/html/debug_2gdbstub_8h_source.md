---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/debug_2gdbstub_8h_source.html
original_path: doxygen/html/debug_2gdbstub_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gdbstub.h

[Go to the documentation of this file.](debug_2gdbstub_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DEBUG\_GDBSTUB\_H\_

8#define ZEPHYR\_INCLUDE\_DEBUG\_GDBSTUB\_H\_

9

10/\* Map from CPU exceptions to GDB \*/

[ 11](debug_2gdbstub_8h.md#a34e3537cdca807d30b24ce76ab1e503c)#define GDB\_EXCEPTION\_INVALID\_INSTRUCTION 4UL

[ 12](debug_2gdbstub_8h.md#af97b5ae81a45e635e69c613b4e2fa9f4)#define GDB\_EXCEPTION\_BREAKPOINT 5UL

[ 13](debug_2gdbstub_8h.md#a37ea8e51fd123a434d6d221280cedca2)#define GDB\_EXCEPTION\_MEMORY\_FAULT 7UL

[ 14](debug_2gdbstub_8h.md#ad65b407f7c8d6d44ab5886866ee2d9da)#define GDB\_EXCEPTION\_DIVIDE\_ERROR 8UL

[ 15](debug_2gdbstub_8h.md#a94da0c93f951fc608c76a525251a9d3a)#define GDB\_EXCEPTION\_INVALID\_MEMORY 11UL

[ 16](debug_2gdbstub_8h.md#acc588c5509a9cf55df485b90dff54ba4)#define GDB\_EXCEPTION\_OVERFLOW 16UL

17

18/\* Access permissions for memory regions \*/

[ 19](debug_2gdbstub_8h.md#a02b9a9d5f33f9ee43bfdd0e68a9a6462)#define GDB\_MEM\_REGION\_NO\_ACCESS 0UL

[ 20](debug_2gdbstub_8h.md#a8a7f81403bcc747817792171bf502d1a)#define GDB\_MEM\_REGION\_READ BIT(0)

[ 21](debug_2gdbstub_8h.md#adb7926e4055fc3ffd94da16c9f0a97b6)#define GDB\_MEM\_REGION\_WRITE BIT(1)

22

[ 23](debug_2gdbstub_8h.md#a083549c8b9db7f28536481e33d362479)#define GDB\_MEM\_REGION\_RO \

24 (GDB\_MEM\_REGION\_READ)

25

[ 26](debug_2gdbstub_8h.md#a386751baaedc3e607a37a473a88bb05a)#define GDB\_MEM\_REGION\_RW \

27 (GDB\_MEM\_REGION\_READ | GDB\_MEM\_REGION\_WRITE)

28

[ 30](structgdb__mem__region.md)struct [gdb\_mem\_region](structgdb__mem__region.md) {

[ 32](structgdb__mem__region.md#a463465123fd373996a857b38c71474b3) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [start](structgdb__mem__region.md#a463465123fd373996a857b38c71474b3);

33

[ 35](structgdb__mem__region.md#a16001ef766b3c5775c1d1b2c59575b74) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [end](structgdb__mem__region.md#a16001ef766b3c5775c1d1b2c59575b74);

36

[ 38](structgdb__mem__region.md#ad8ae6acf6950428a9846a25fb0219eeb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [attributes](structgdb__mem__region.md#ad8ae6acf6950428a9846a25fb0219eeb);

39

[ 41](structgdb__mem__region.md#aa714bde657eb3572367a924298dd927f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [alignment](structgdb__mem__region.md#aa714bde657eb3572367a924298dd927f);

42};

43

52extern const struct [gdb\_mem\_region](structgdb__mem__region.md) [gdb\_mem\_region\_array](debug_2gdbstub_8h.md#a9d01831c656bae3ee4592ccb45456295)[];

53

59extern const size\_t [gdb\_mem\_num\_regions](debug_2gdbstub_8h.md#a439e80da6ae6e5388f9a78744d0978d1);

60

[ 74](debug_2gdbstub_8h.md#ab392b604a2edf4bea077eb7fa02079e1)size\_t [gdb\_bin2hex](debug_2gdbstub_8h.md#ab392b604a2edf4bea077eb7fa02079e1)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen,

75 char \*hex, size\_t hexlen);

76

77

[ 89](debug_2gdbstub_8h.md#add890d2dc6e197a2b94c45c4de94c8b1)bool [gdb\_mem\_can\_read](debug_2gdbstub_8h.md#add890d2dc6e197a2b94c45c4de94c8b1)(const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, const size\_t len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*align);

90

[ 102](debug_2gdbstub_8h.md#aac6c53353a4751d835028c6fd9906d19)bool [gdb\_mem\_can\_write](debug_2gdbstub_8h.md#aac6c53353a4751d835028c6fd9906d19)(const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr, const size\_t len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*align);

103

104#endif

[gdb\_mem\_num\_regions](debug_2gdbstub_8h.md#a439e80da6ae6e5388f9a78744d0978d1)

const size\_t gdb\_mem\_num\_regions

Number of Memory Regions.

[gdb\_mem\_region\_array](debug_2gdbstub_8h.md#a9d01831c656bae3ee4592ccb45456295)

const struct gdb\_mem\_region gdb\_mem\_region\_array[]

Memory region descriptions used for GDB memory access.

[gdb\_mem\_can\_write](debug_2gdbstub_8h.md#aac6c53353a4751d835028c6fd9906d19)

bool gdb\_mem\_can\_write(const uintptr\_t addr, const size\_t len, uint8\_t \*align)

Check if a memory block can be written into.

[gdb\_bin2hex](debug_2gdbstub_8h.md#ab392b604a2edf4bea077eb7fa02079e1)

size\_t gdb\_bin2hex(const uint8\_t \*buf, size\_t buflen, char \*hex, size\_t hexlen)

Convert a binary array into string representation.

[gdb\_mem\_can\_read](debug_2gdbstub_8h.md#add890d2dc6e197a2b94c45c4de94c8b1)

bool gdb\_mem\_can\_read(const uintptr\_t addr, const size\_t len, uint8\_t \*align)

Check if a memory block can be read.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[gdb\_mem\_region](structgdb__mem__region.md)

Describe one memory region.

**Definition** gdbstub.h:30

[gdb\_mem\_region::end](structgdb__mem__region.md#a16001ef766b3c5775c1d1b2c59575b74)

uintptr\_t end

End address of a memory region.

**Definition** gdbstub.h:35

[gdb\_mem\_region::start](structgdb__mem__region.md#a463465123fd373996a857b38c71474b3)

uintptr\_t start

Start address of a memory region.

**Definition** gdbstub.h:32

[gdb\_mem\_region::alignment](structgdb__mem__region.md#aa714bde657eb3572367a924298dd927f)

uint8\_t alignment

Read/write alignment, 0 if using default alignment.

**Definition** gdbstub.h:41

[gdb\_mem\_region::attributes](structgdb__mem__region.md#ad8ae6acf6950428a9846a25fb0219eeb)

uint16\_t attributes

Memory region attributes.

**Definition** gdbstub.h:38

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [gdbstub.h](debug_2gdbstub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
