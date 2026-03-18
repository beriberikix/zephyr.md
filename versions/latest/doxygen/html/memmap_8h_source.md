---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/memmap_8h_source.html
original_path: doxygen/html/memmap_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memmap.h

[Go to the documentation of this file.](memmap_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_MEMMAP\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_X86\_MEMMAP\_H\_

8

9#ifndef \_ASMLANGUAGE

10

11/\*

12 \* The "source" of the memory map refers to where we got the data to fill in

13 \* the map. Order is important: if multiple sources are available, then the

14 \* numerically HIGHEST source wins, a manually-provided map being the "best".

15 \*/

16

[ 17](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5)enum [x86\_memmap\_source](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5) {

[ 18](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a68b60d7825f63c9a7f973a5ba63b7fe9) [X86\_MEMMAP\_SOURCE\_DEFAULT](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a68b60d7825f63c9a7f973a5ba63b7fe9),

[ 19](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a7d9550deb6b27b6c720cbcb7dd48dc63) [X86\_MEMMAP\_SOURCE\_MULTIBOOT\_MEM](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a7d9550deb6b27b6c720cbcb7dd48dc63),

[ 20](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a65183e6b869d16a0b1daf4b5d0c9b3f5) [X86\_MEMMAP\_SOURCE\_MULTIBOOT\_MMAP](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a65183e6b869d16a0b1daf4b5d0c9b3f5),

[ 21](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a4718538763c5b75bb121fdeb8b2b5ffc) [X86\_MEMMAP\_SOURCE\_MANUAL](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a4718538763c5b75bb121fdeb8b2b5ffc)

22};

23

24extern enum [x86\_memmap\_source](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5) [x86\_memmap\_source](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5);

25

26/\*

27 \* For simplicity, we maintain a fixed-sized array of memory regions.

28 \*

29 \* We don't only track available RAM -- we track unavailable regions, too:

30 \* sometimes we'll be given a map with overlapping regions. We have to be

31 \* pessimistic about what is considered "available RAM" and it's easier to

32 \* keep all the regions around than it is to correct incorrect maps. It's

33 \* also handy to have the entire map intact for diagnostic purposes.

34 \*/

35

[ 36](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757ef)enum [x86\_memmap\_entry\_type](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757ef) {

37 /\*

38 \* the UNUSED entry must have a numerical 0 value, so

39 \* that partially-initialized arrays behave as expected.

40 \*/

41

[ 42](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efa7639598e6c11cde301d4aacea99b3fd6) [X86\_MEMMAP\_ENTRY\_UNUSED](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efa7639598e6c11cde301d4aacea99b3fd6), /\* this entry is unused/invalid \*/

[ 43](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efae6c7073699a49c3e74fb91c45ea24a0a) [X86\_MEMMAP\_ENTRY\_RAM](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efae6c7073699a49c3e74fb91c45ea24a0a), /\* available RAM \*/

[ 44](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efaa2f86b365795a0f0fc419121f2bdf417) [X86\_MEMMAP\_ENTRY\_ACPI](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efaa2f86b365795a0f0fc419121f2bdf417), /\* reserved for ACPI \*/

[ 45](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efa1ec11c2afcb03537e072273a6fbb2e61) [X86\_MEMMAP\_ENTRY\_NVS](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efa1ec11c2afcb03537e072273a6fbb2e61), /\* preserve during hibernation \*/

[ 46](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efa5e3f2de2b434f036b6fff8aaa63e55dd) [X86\_MEMMAP\_ENTRY\_DEFECTIVE](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efa5e3f2de2b434f036b6fff8aaa63e55dd), /\* bad memory modules \*/

[ 47](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efad26cdfad068828bce9185ebb9908b368) [X86\_MEMMAP\_ENTRY\_UNKNOWN](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efad26cdfad068828bce9185ebb9908b368) /\* unknown type, do not use \*/

48};

49

[ 50](structx86__memmap__entry.md)struct [x86\_memmap\_entry](structx86__memmap__entry.md) {

[ 51](structx86__memmap__entry.md#ac3e9625c5635d4943e8a4410ab9a0c52) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [base](structx86__memmap__entry.md#ac3e9625c5635d4943e8a4410ab9a0c52);

[ 52](structx86__memmap__entry.md#acf051142ca1ca3c6738cf8084af7fe1f) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [length](structx86__memmap__entry.md#acf051142ca1ca3c6738cf8084af7fe1f);

[ 53](structx86__memmap__entry.md#aa9fc8042ff4a001bdd5ea792c657e6bc) enum [x86\_memmap\_entry\_type](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757ef) [type](structx86__memmap__entry.md#aa9fc8042ff4a001bdd5ea792c657e6bc);

54};

55

56extern struct [x86\_memmap\_entry](structx86__memmap__entry.md) [x86\_memmap](memmap_8h.md#a8b8229cdb36bf23f8257958fda84be4b)[];

57

58/\*

59 \* We keep track of kernel memory areas (text, data, etc.) in a table for

60 \* ease of reference. There's really no reason to export this table, or to

61 \* label the members, except for diagnostic purposes.

62 \*/

63

[ 64](structx86__memmap__exclusion.md)struct [x86\_memmap\_exclusion](structx86__memmap__exclusion.md) {

[ 65](structx86__memmap__exclusion.md#a2be5b85d61e898edd8ce24df319b54e4) char \*[name](structx86__memmap__exclusion.md#a2be5b85d61e898edd8ce24df319b54e4);

[ 66](structx86__memmap__exclusion.md#aeb4aee25952808bbb8184f76c27d1ee5) void \*[start](structx86__memmap__exclusion.md#aeb4aee25952808bbb8184f76c27d1ee5); /\* address of first byte of exclusion \*/

[ 67](structx86__memmap__exclusion.md#a7ea16f8f0e3672b02cddfbcb7e402f7f) void \*[end](structx86__memmap__exclusion.md#a7ea16f8f0e3672b02cddfbcb7e402f7f); /\* one byte past end of exclusion \*/

68};

69

70extern struct [x86\_memmap\_exclusion](structx86__memmap__exclusion.md) [x86\_memmap\_exclusions](memmap_8h.md#ab1723f77a7879fd1cc4723091241d099)[];

71extern int [x86\_nr\_memmap\_exclusions](memmap_8h.md#abb046960eea27faacf7a08d18b9a57eb);

72

73#endif /\* \_ASMLANGUAGE \*/

74

75#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_MEMMAP\_H\_ \*/

[x86\_memmap](memmap_8h.md#a8b8229cdb36bf23f8257958fda84be4b)

struct x86\_memmap\_entry x86\_memmap[]

[x86\_memmap\_exclusions](memmap_8h.md#ab1723f77a7879fd1cc4723091241d099)

struct x86\_memmap\_exclusion x86\_memmap\_exclusions[]

[x86\_nr\_memmap\_exclusions](memmap_8h.md#abb046960eea27faacf7a08d18b9a57eb)

int x86\_nr\_memmap\_exclusions

[x86\_memmap\_source](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5)

x86\_memmap\_source

**Definition** memmap.h:17

[X86\_MEMMAP\_SOURCE\_MANUAL](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a4718538763c5b75bb121fdeb8b2b5ffc)

@ X86\_MEMMAP\_SOURCE\_MANUAL

**Definition** memmap.h:21

[X86\_MEMMAP\_SOURCE\_MULTIBOOT\_MMAP](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a65183e6b869d16a0b1daf4b5d0c9b3f5)

@ X86\_MEMMAP\_SOURCE\_MULTIBOOT\_MMAP

**Definition** memmap.h:20

[X86\_MEMMAP\_SOURCE\_DEFAULT](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a68b60d7825f63c9a7f973a5ba63b7fe9)

@ X86\_MEMMAP\_SOURCE\_DEFAULT

**Definition** memmap.h:18

[X86\_MEMMAP\_SOURCE\_MULTIBOOT\_MEM](memmap_8h.md#ae4f3b51d56ed1ddb36a78d0238a8bdc5a7d9550deb6b27b6c720cbcb7dd48dc63)

@ X86\_MEMMAP\_SOURCE\_MULTIBOOT\_MEM

**Definition** memmap.h:19

[x86\_memmap\_entry\_type](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757ef)

x86\_memmap\_entry\_type

**Definition** memmap.h:36

[X86\_MEMMAP\_ENTRY\_NVS](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efa1ec11c2afcb03537e072273a6fbb2e61)

@ X86\_MEMMAP\_ENTRY\_NVS

**Definition** memmap.h:45

[X86\_MEMMAP\_ENTRY\_DEFECTIVE](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efa5e3f2de2b434f036b6fff8aaa63e55dd)

@ X86\_MEMMAP\_ENTRY\_DEFECTIVE

**Definition** memmap.h:46

[X86\_MEMMAP\_ENTRY\_UNUSED](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efa7639598e6c11cde301d4aacea99b3fd6)

@ X86\_MEMMAP\_ENTRY\_UNUSED

**Definition** memmap.h:42

[X86\_MEMMAP\_ENTRY\_ACPI](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efaa2f86b365795a0f0fc419121f2bdf417)

@ X86\_MEMMAP\_ENTRY\_ACPI

**Definition** memmap.h:44

[X86\_MEMMAP\_ENTRY\_UNKNOWN](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efad26cdfad068828bce9185ebb9908b368)

@ X86\_MEMMAP\_ENTRY\_UNKNOWN

**Definition** memmap.h:47

[X86\_MEMMAP\_ENTRY\_RAM](memmap_8h.md#af5da5d5ee62dc74e3ea4bf1f5db757efae6c7073699a49c3e74fb91c45ea24a0a)

@ X86\_MEMMAP\_ENTRY\_RAM

**Definition** memmap.h:43

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[x86\_memmap\_entry](structx86__memmap__entry.md)

**Definition** memmap.h:50

[x86\_memmap\_entry::type](structx86__memmap__entry.md#aa9fc8042ff4a001bdd5ea792c657e6bc)

enum x86\_memmap\_entry\_type type

**Definition** memmap.h:53

[x86\_memmap\_entry::base](structx86__memmap__entry.md#ac3e9625c5635d4943e8a4410ab9a0c52)

uint64\_t base

**Definition** memmap.h:51

[x86\_memmap\_entry::length](structx86__memmap__entry.md#acf051142ca1ca3c6738cf8084af7fe1f)

uint64\_t length

**Definition** memmap.h:52

[x86\_memmap\_exclusion](structx86__memmap__exclusion.md)

**Definition** memmap.h:64

[x86\_memmap\_exclusion::name](structx86__memmap__exclusion.md#a2be5b85d61e898edd8ce24df319b54e4)

char \* name

**Definition** memmap.h:65

[x86\_memmap\_exclusion::end](structx86__memmap__exclusion.md#a7ea16f8f0e3672b02cddfbcb7e402f7f)

void \* end

**Definition** memmap.h:67

[x86\_memmap\_exclusion::start](structx86__memmap__exclusion.md#aeb4aee25952808bbb8184f76c27d1ee5)

void \* start

**Definition** memmap.h:66

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [memmap.h](memmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
