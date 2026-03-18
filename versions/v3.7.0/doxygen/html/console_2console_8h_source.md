---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/console_2console_8h_source.html
original_path: doxygen/html/console_2console_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

console.h

[Go to the documentation of this file.](console_2console_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_CONSOLE\_CONSOLE\_H\_

8#define ZEPHYR\_INCLUDE\_CONSOLE\_CONSOLE\_H\_

9

10#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

11#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

12#include <[zephyr/kernel.h](kernel_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

24

[ 35](group__console__api.md#ga0bf949437e32d17992435003cf8b46b5)int [console\_init](group__console__api.md#ga0bf949437e32d17992435003cf8b46b5)(void);

36

[ 48](group__console__api.md#ga27785534c14d4098822db2b870b7d81d)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [console\_read](group__console__api.md#ga27785534c14d4098822db2b870b7d81d)(void \*dummy, void \*buf, size\_t size);

49

[ 60](group__console__api.md#ga204fd795daf9ef6b1f2803547747545e)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [console\_write](group__console__api.md#ga204fd795daf9ef6b1f2803547747545e)(void \*dummy, const void \*buf, size\_t size);

61

[ 75](group__console__api.md#ga2ba36eb1081cd0b98aa43216ccd6fbd5)int [console\_getchar](group__console__api.md#ga2ba36eb1081cd0b98aa43216ccd6fbd5)(void);

76

[ 84](group__console__api.md#ga7bd842f1cda6c8218cb1d41420e4de49)int [console\_putchar](group__console__api.md#ga7bd842f1cda6c8218cb1d41420e4de49)(char c);

85

[ 93](group__console__api.md#gacd13267df8567c63f2285ce0e1cbbc20)void [console\_getline\_init](group__console__api.md#gacd13267df8567c63f2285ce0e1cbbc20)(void);

94

[ 111](group__console__api.md#ga3454f5b84d38d46a6c2bbf7fd6baa815)char \*[console\_getline](group__console__api.md#ga3454f5b84d38d46a6c2bbf7fd6baa815)(void);

112

113#ifdef \_\_cplusplus

114}

115#endif

116

120

121#endif /\* ZEPHYR\_INCLUDE\_CONSOLE\_CONSOLE\_H\_ \*/

[console\_init](group__console__api.md#ga0bf949437e32d17992435003cf8b46b5)

int console\_init(void)

Initialize console device.

[console\_write](group__console__api.md#ga204fd795daf9ef6b1f2803547747545e)

ssize\_t console\_write(void \*dummy, const void \*buf, size\_t size)

Write data to console.

[console\_read](group__console__api.md#ga27785534c14d4098822db2b870b7d81d)

ssize\_t console\_read(void \*dummy, void \*buf, size\_t size)

Read data from console.

[console\_getchar](group__console__api.md#ga2ba36eb1081cd0b98aa43216ccd6fbd5)

int console\_getchar(void)

Get next char from console input buffer.

[console\_getline](group__console__api.md#ga3454f5b84d38d46a6c2bbf7fd6baa815)

char \* console\_getline(void)

Get next line from console input buffer.

[console\_putchar](group__console__api.md#ga7bd842f1cda6c8218cb1d41420e4de49)

int console\_putchar(char c)

Output a char to console (buffered).

[console\_getline\_init](group__console__api.md#gacd13267df8567c63f2285ce0e1cbbc20)

void console\_getline\_init(void)

Initialize console\_getline() call.

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [console](dir_2f086bf88c9e3ffd4c7c065f4bf7757c.md)
- [console.h](console_2console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
