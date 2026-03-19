---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/shell__fprintf_8h_source.html
original_path: doxygen/html/shell__fprintf_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_fprintf.h

[Go to the documentation of this file.](shell__fprintf_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SHELL\_FPRINTF\_H\_

8#define ZEPHYR\_INCLUDE\_SHELL\_FPRINTF\_H\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12#include <stddef.h>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 18](shell__fprintf_8h.md#a2ea67ad2a9eeffdcfbfe460e4cfe6b34)typedef void (\*[shell\_fprintf\_fwrite](shell__fprintf_8h.md#a2ea67ad2a9eeffdcfbfe460e4cfe6b34))(const void \*user\_ctx,

19 const char \*data,

20 size\_t length);

21

[ 22](structshell__fprintf__control__block.md)struct [shell\_fprintf\_control\_block](structshell__fprintf__control__block.md) {

[ 23](structshell__fprintf__control__block.md#a3070be7874707be797997210ce8cf8c3) size\_t [buffer\_cnt](structshell__fprintf__control__block.md#a3070be7874707be797997210ce8cf8c3);

[ 24](structshell__fprintf__control__block.md#a70f4ae1d5268a35d009e97d267b44e2f) bool [autoflush](structshell__fprintf__control__block.md#a70f4ae1d5268a35d009e97d267b44e2f);

25};

26

[ 29](structshell__fprintf.md)struct [shell\_fprintf](structshell__fprintf.md) {

[ 30](structshell__fprintf.md#a60eb48520fa96fccdfe7a9f4a32729f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buffer](structshell__fprintf.md#a60eb48520fa96fccdfe7a9f4a32729f7);

[ 31](structshell__fprintf.md#a0055b09fb33072e035fca20a4dfd6d15) size\_t [buffer\_size](structshell__fprintf.md#a0055b09fb33072e035fca20a4dfd6d15);

[ 32](structshell__fprintf.md#a8add85184dda7c002e7265baebe2112b) [shell\_fprintf\_fwrite](shell__fprintf_8h.md#a2ea67ad2a9eeffdcfbfe460e4cfe6b34) [fwrite](structshell__fprintf.md#a8add85184dda7c002e7265baebe2112b);

[ 33](structshell__fprintf.md#ab1920b62893c411baea3e1ff35816185) const void \*[user\_ctx](structshell__fprintf.md#ab1920b62893c411baea3e1ff35816185);

[ 34](structshell__fprintf.md#a1bc59eaff9fe7e19c5b6db965c08bb67) struct [shell\_fprintf\_control\_block](structshell__fprintf__control__block.md) \*[ctrl\_blk](structshell__fprintf.md#a1bc59eaff9fe7e19c5b6db965c08bb67);

35};

36

47#define Z\_SHELL\_FPRINTF\_DEFINE(\_name, \_user\_ctx, \_buf, \_size, \

48 \_autoflush, \_fwrite) \

49 static struct shell\_fprintf\_control\_block \

50 \_name##\_shell\_fprintf\_ctx = { \

51 .autoflush = \_autoflush, \

52 .buffer\_cnt = 0 \

53 }; \

54 static const struct shell\_fprintf \_name = { \

55 .buffer = \_buf, \

56 .buffer\_size = \_size, \

57 .fwrite = \_fwrite, \

58 .user\_ctx = \_user\_ctx, \

59 .ctrl\_blk = &\_name##\_shell\_fprintf\_ctx \

60 }

61

69void z\_shell\_fprintf\_fmt(const struct [shell\_fprintf](group__shell__api.md#ga1fd1671311b112f0c87ab2dafd801105) \*sh\_fprintf,

70 char const \*fmt, va\_list args);

71

77void z\_shell\_fprintf\_buffer\_flush(const struct [shell\_fprintf](group__shell__api.md#ga1fd1671311b112f0c87ab2dafd801105) \*sh\_fprintf);

78

79#ifdef \_\_cplusplus

80}

81#endif

82

83#endif /\* ZEPHYR\_INCLUDE\_SHELL\_FPRINTF\_H\_ \*/

[shell\_fprintf](group__shell__api.md#ga1fd1671311b112f0c87ab2dafd801105)

#define shell\_fprintf(sh, color, fmt,...)

**Definition** shell.h:1074

[kernel.h](kernel_8h.md)

Public kernel APIs.

[shell\_fprintf\_fwrite](shell__fprintf_8h.md#a2ea67ad2a9eeffdcfbfe460e4cfe6b34)

void(\* shell\_fprintf\_fwrite)(const void \*user\_ctx, const char \*data, size\_t length)

**Definition** shell\_fprintf.h:18

[stdbool.h](stdbool_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[shell\_fprintf\_control\_block](structshell__fprintf__control__block.md)

**Definition** shell\_fprintf.h:22

[shell\_fprintf\_control\_block::buffer\_cnt](structshell__fprintf__control__block.md#a3070be7874707be797997210ce8cf8c3)

size\_t buffer\_cnt

**Definition** shell\_fprintf.h:23

[shell\_fprintf\_control\_block::autoflush](structshell__fprintf__control__block.md#a70f4ae1d5268a35d009e97d267b44e2f)

bool autoflush

**Definition** shell\_fprintf.h:24

[shell\_fprintf](structshell__fprintf.md)

fprintf context

**Definition** shell\_fprintf.h:29

[shell\_fprintf::buffer\_size](structshell__fprintf.md#a0055b09fb33072e035fca20a4dfd6d15)

size\_t buffer\_size

**Definition** shell\_fprintf.h:31

[shell\_fprintf::ctrl\_blk](structshell__fprintf.md#a1bc59eaff9fe7e19c5b6db965c08bb67)

struct shell\_fprintf\_control\_block \* ctrl\_blk

**Definition** shell\_fprintf.h:34

[shell\_fprintf::buffer](structshell__fprintf.md#a60eb48520fa96fccdfe7a9f4a32729f7)

uint8\_t \* buffer

**Definition** shell\_fprintf.h:30

[shell\_fprintf::fwrite](structshell__fprintf.md#a8add85184dda7c002e7265baebe2112b)

shell\_fprintf\_fwrite fwrite

**Definition** shell\_fprintf.h:32

[shell\_fprintf::user\_ctx](structshell__fprintf.md#ab1920b62893c411baea3e1ff35816185)

const void \* user\_ctx

**Definition** shell\_fprintf.h:33

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_fprintf.h](shell__fprintf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
