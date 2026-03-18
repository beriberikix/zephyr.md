---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/fs__interface_8h_source.html
original_path: doxygen/html/fs__interface_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_interface.h

[Go to the documentation of this file.](fs__interface_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_FS\_FS\_INTERFACE\_H\_

8#define ZEPHYR\_INCLUDE\_FS\_FS\_INTERFACE\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

16#if defined(CONFIG\_FILE\_SYSTEM\_MAX\_FILE\_NAME) && (CONFIG\_FILE\_SYSTEM\_MAX\_FILE\_NAME - 0) > 0

17

18/\* No in-tree file system supports name longer than 255 characters \*/

19#if (CONFIG\_FILE\_SYSTEM\_LITTLEFS || CONFIG\_FAT\_FILESYSTEM\_ELM || \

20 CONFIG\_FILE\_SYSTEM\_EXT2) && (CONFIG\_FILE\_SYSTEM\_MAX\_FILE\_NAME > 255)

21#error "Max allowed CONFIG\_FILE\_SYSTEM\_MAX\_FILE\_NAME is 255 characters, when any in-tree FS enabled"

22#endif

23

24/\* Enabled FAT driver, without LFN, restricts name length to 12 characters \*/

25#if defined(CONFIG\_FAT\_FILESYSTEM\_ELM) && !(CONFIG\_FS\_FATFS\_LFN) && \

26 (CONFIG\_FILE\_SYSTEM\_MAX\_FILE\_NAME > 12)

27#error "CONFIG\_FILE\_SYSTEM\_MAX\_FILE\_NAME can not be > 12 if FAT is enabled without LFN"

28#endif

29

30#define MAX\_FILE\_NAME CONFIG\_FILE\_SYSTEM\_MAX\_FILE\_NAME

31

32#else

33/\* Select from enabled file systems \*/

34

35#if defined(CONFIG\_FAT\_FILESYSTEM\_ELM)

36

37#if defined(CONFIG\_FS\_FATFS\_LFN)

38#define MAX\_FILE\_NAME CONFIG\_FS\_FATFS\_MAX\_LFN

39#else /\* CONFIG\_FS\_FATFS\_LFN \*/

40#define MAX\_FILE\_NAME 12 /\* Uses 8.3 SFN \*/

41#endif /\* CONFIG\_FS\_FATFS\_LFN \*/

42

43#endif

44

45#if !defined(MAX\_FILE\_NAME) && defined(CONFIG\_FILE\_SYSTEM\_EXT2)

46#define MAX\_FILE\_NAME 255

47#endif

48

49#if !defined(MAX\_FILE\_NAME) && defined(CONFIG\_FILE\_SYSTEM\_LITTLEFS)

50#define MAX\_FILE\_NAME 255

51#endif

52

53#if !defined(MAX\_FILE\_NAME) /\* filesystem selection \*/

54/\* Use standard 8.3 when no filesystem is explicitly selected \*/

[ 55](fs__interface_8h.md#af43dedece15d018ffad8970492870bac)#define MAX\_FILE\_NAME 12

56#endif /\* filesystem selection \*/

57

58#endif /\* CONFIG\_FILE\_SYSTEM\_MAX\_FILE\_NAME \*/

59

60

61/\* Type for fs\_open flags \*/

[ 62](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027);

63

64struct [fs\_mount\_t](structfs__mount__t.md);

65

70

[ 76](structfs__file__t.md)struct [fs\_file\_t](structfs__file__t.md) {

[ 78](structfs__file__t.md#aa63d13a3c2923f1adecb55ab7e6d1bfa) void \*[filep](structfs__file__t.md#aa63d13a3c2923f1adecb55ab7e6d1bfa);

[ 80](structfs__file__t.md#af027d2f6b262d26d9d45551e4b9044e2) const struct [fs\_mount\_t](structfs__mount__t.md) \*[mp](structfs__file__t.md#af027d2f6b262d26d9d45551e4b9044e2);

[ 82](structfs__file__t.md#a9a4fbedc9df828f7ec8eb3b9734a054e) [fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027) [flags](structfs__file__t.md#a9a4fbedc9df828f7ec8eb3b9734a054e);

83};

84

[ 90](structfs__dir__t.md)struct [fs\_dir\_t](structfs__dir__t.md) {

[ 92](structfs__dir__t.md#afdd8e0b7b0c528a420c050718213d1ff) void \*[dirp](structfs__dir__t.md#afdd8e0b7b0c528a420c050718213d1ff);

[ 94](structfs__dir__t.md#a6d8e0c603a33ed4870fcd7b82e1bc0a4) const struct [fs\_mount\_t](structfs__mount__t.md) \*[mp](structfs__dir__t.md#a6d8e0c603a33ed4870fcd7b82e1bc0a4);

95};

96

100

101#ifdef \_\_cplusplus

102}

103#endif

104

105#endif /\* ZEPHYR\_INCLUDE\_FS\_FS\_INTERFACE\_H\_ \*/

[fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027)

uint8\_t fs\_mode\_t

**Definition** fs\_interface.h:62

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[fs\_dir\_t](structfs__dir__t.md)

Directory object representing an open directory.

**Definition** fs\_interface.h:90

[fs\_dir\_t::mp](structfs__dir__t.md#a6d8e0c603a33ed4870fcd7b82e1bc0a4)

const struct fs\_mount\_t \* mp

Pointer to mount point structure.

**Definition** fs\_interface.h:94

[fs\_dir\_t::dirp](structfs__dir__t.md#afdd8e0b7b0c528a420c050718213d1ff)

void \* dirp

Pointer to directory object structure.

**Definition** fs\_interface.h:92

[fs\_file\_t](structfs__file__t.md)

File object representing an open file.

**Definition** fs\_interface.h:76

[fs\_file\_t::flags](structfs__file__t.md#a9a4fbedc9df828f7ec8eb3b9734a054e)

fs\_mode\_t flags

Open/create flags.

**Definition** fs\_interface.h:82

[fs\_file\_t::filep](structfs__file__t.md#aa63d13a3c2923f1adecb55ab7e6d1bfa)

void \* filep

Pointer to file object structure.

**Definition** fs\_interface.h:78

[fs\_file\_t::mp](structfs__file__t.md#af027d2f6b262d26d9d45551e4b9044e2)

const struct fs\_mount\_t \* mp

Pointer to mount point structure.

**Definition** fs\_interface.h:80

[fs\_mount\_t](structfs__mount__t.md)

File system mount info structure.

**Definition** fs.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [fs\_interface.h](fs__interface_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
