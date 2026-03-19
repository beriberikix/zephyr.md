---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/fs__loader_8h_source.html
original_path: doxygen/html/fs__loader_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_loader.h

[Go to the documentation of this file.](fs__loader_8h.md)

1/\*

2 \* Copyright (c) 2024 BayLibre SAS

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LLEXT\_FS\_LOADER\_H

8#define ZEPHYR\_LLEXT\_FS\_LOADER\_H

9

10#include <[zephyr/llext/loader.h](loader_8h.md)>

11#include <[zephyr/fs/fs.h](fs_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

24

[ 28](structllext__fs__loader.md)struct [llext\_fs\_loader](structllext__fs__loader.md) {

[ 30](structllext__fs__loader.md#a33f0ba96f4437d74faff6cb78c2188cb) struct [llext\_loader](structllext__loader.md) [loader](structllext__fs__loader.md#a33f0ba96f4437d74faff6cb78c2188cb);

31

33 bool is\_open;

34 const char \*name;

35 struct [fs\_file\_t](structfs__file__t.md) file;

37};

38

40int llext\_fs\_prepare(struct [llext\_loader](structllext__loader.md) \*ldr);

41int llext\_fs\_read(struct [llext\_loader](structllext__loader.md) \*ldr, void \*buf, size\_t len);

42int llext\_fs\_seek(struct [llext\_loader](structllext__loader.md) \*ldr, size\_t pos);

43void llext\_fs\_finalize(struct [llext\_loader](structllext__loader.md) \*ldr);

45

[ 51](group__llext__loader__apis.md#ga25a394fb7f7f93cfe3ab92d8ed4a6bff)#define LLEXT\_FS\_LOADER(\_filename) \

52 { \

53 .loader = \

54 { \

55 .prepare = llext\_fs\_prepare, \

56 .read = llext\_fs\_read, \

57 .seek = llext\_fs\_seek, \

58 .peek = NULL, \

59 .finalize = llext\_fs\_finalize, \

60 }, \

61 .is\_open = false, \

62 .name = (\_filename), \

63 }

64

68

69#ifdef \_\_cplusplus

70}

71#endif

72

73#endif /\* ZEPHYR\_LLEXT\_FS\_LOADER\_H \*/

[fs.h](fs_8h.md)

[loader.h](loader_8h.md)

LLEXT ELF loader context types.

[fs\_file\_t](structfs__file__t.md)

File object representing an open file.

**Definition** fs\_interface.h:76

[llext\_fs\_loader](structllext__fs__loader.md)

Implementation of llext\_loader that reads from a filesystem.

**Definition** fs\_loader.h:28

[llext\_fs\_loader::loader](structllext__fs__loader.md#a33f0ba96f4437d74faff6cb78c2188cb)

struct llext\_loader loader

Extension loader.

**Definition** fs\_loader.h:30

[llext\_loader](structllext__loader.md)

Linkable loadable extension loader context.

**Definition** loader.h:42

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [fs\_loader.h](fs__loader_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
