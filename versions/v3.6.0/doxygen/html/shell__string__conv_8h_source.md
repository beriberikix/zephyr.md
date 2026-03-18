---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/shell__string__conv_8h_source.html
original_path: doxygen/html/shell__string__conv_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_string\_conv.h

[Go to the documentation of this file.](shell__string__conv_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef SHELL\_STRING\_CONV\_H\_\_

8#define SHELL\_STRING\_CONV\_H\_\_

9

10#include <[stdbool.h](stdbool_8h.md)>

11#include <[stdint.h](stdint_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 32](shell__string__conv_8h.md#a2a3fc802d8a4d13e49024ee5546d62a6)long [shell\_strtol](shell__string__conv_8h.md#a2a3fc802d8a4d13e49024ee5546d62a6)(const char \*str, int base, int \*err);

33

[ 49](shell__string__conv_8h.md#ac7928525a22e053d1dea44995c8198b9)unsigned long [shell\_strtoul](shell__string__conv_8h.md#ac7928525a22e053d1dea44995c8198b9)(const char \*str, int base, int \*err);

50

[ 66](shell__string__conv_8h.md#a635c05cc9a2e84b6438402334587d537)unsigned long long [shell\_strtoull](shell__string__conv_8h.md#a635c05cc9a2e84b6438402334587d537)(const char \*str, int base, int \*err);

67

[ 83](shell__string__conv_8h.md#aabc3fbdfdc2c3cbd4cd41dc97309aea4)bool [shell\_strtobool](shell__string__conv_8h.md#aabc3fbdfdc2c3cbd4cd41dc97309aea4)(const char \*str, int base, int \*err);

84

85#ifdef \_\_cplusplus

86}

87#endif

88

89#endif /\* SHELL\_STRING\_CONV\_H\_\_ \*/

[shell\_strtol](shell__string__conv_8h.md#a2a3fc802d8a4d13e49024ee5546d62a6)

long shell\_strtol(const char \*str, int base, int \*err)

String to long conversion with error check.

[shell\_strtoull](shell__string__conv_8h.md#a635c05cc9a2e84b6438402334587d537)

unsigned long long shell\_strtoull(const char \*str, int base, int \*err)

String to unsigned long long conversion with error check.

[shell\_strtobool](shell__string__conv_8h.md#aabc3fbdfdc2c3cbd4cd41dc97309aea4)

bool shell\_strtobool(const char \*str, int base, int \*err)

String to boolean conversion with error check.

[shell\_strtoul](shell__string__conv_8h.md#ac7928525a22e053d1dea44995c8198b9)

unsigned long shell\_strtoul(const char \*str, int base, int \*err)

String to unsigned long conversion with error check.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_string\_conv.h](shell__string__conv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
