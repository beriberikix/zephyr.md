---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/fnmatch_8h_source.html
original_path: doxygen/html/fnmatch_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fnmatch.h

[Go to the documentation of this file.](fnmatch_8h.md)

1/\* SPDX-License-Identifier: BSD-3-Clause \*/

2

3/\* $NetBSD: fnmatch.h,v 1.12.50.1 2011/02/08 16:18:55 bouyer Exp $ \*/

4

5/\*-

6 \* Copyright (c) 1992, 1993

7 \* The Regents of the University of California. All rights reserved.

8 \*

9 \* Redistribution and use in source and binary forms, with or without

10 \* modification, are permitted provided that the following conditions

11 \* are met:

12 \* 1. Redistributions of source code must retain the above copyright

13 \* notice, this list of conditions and the following disclaimer.

14 \* 2. Redistributions in binary form must reproduce the above copyright

15 \* notice, this list of conditions and the following disclaimer in the

16 \* documentation and/or other materials provided with the distribution.

17 \* 3. Neither the name of the University nor the names of its contributors

18 \* may be used to endorse or promote products derived from this software

19 \* without specific prior written permission.

20 \*

21 \* THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND

22 \* ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE

23 \* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE

24 \* ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE

25 \* FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL

26 \* DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS

27 \* OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)

28 \* HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT

29 \* LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY

30 \* OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF

31 \* SUCH DAMAGE.

32 \*

33 \* @(#)fnmatch.h 8.1 (Berkeley) 6/2/93

34 \*/

35

36#ifndef \_FNMATCH\_H\_

37#define \_FNMATCH\_H\_

38

[ 39](fnmatch_8h.md#af2661230e0cfc9970d6cdbe01571e753)#define FNM\_NOMATCH 1 /\* Match failed. \*/

[ 40](fnmatch_8h.md#abf296e95251824c90803dd3aa374190d)#define FNM\_NOSYS 2 /\* Function not implemented. \*/

[ 41](fnmatch_8h.md#a944d56e32e8885bb5f89d654b383abf8)#define FNM\_NORES 3 /\* Out of resources \*/

42

[ 43](fnmatch_8h.md#a0c050a8a7551c2ca86560396de3d20d0)#define FNM\_NOESCAPE 0x01 /\* Disable backslash escaping. \*/

[ 44](fnmatch_8h.md#aed9e649990b20ba86e1aa7cacdc1bafe)#define FNM\_PATHNAME 0x02 /\* Slash must be matched by slash. \*/

[ 45](fnmatch_8h.md#aab98fecc02c06d6379bfcf416d6d297e)#define FNM\_PERIOD 0x04 /\* Period must be matched by period. \*/

[ 46](fnmatch_8h.md#ad41e3158a654dd4dfdab19d97745698a)#define FNM\_CASEFOLD 0x08 /\* Pattern is matched case-insensitive \*/

[ 47](fnmatch_8h.md#a94f8f78b6d024e35c971dd3ec057140c)#define FNM\_LEADING\_DIR 0x10 /\* Ignore /<tail> after Imatch. \*/

48

49#ifdef \_\_cplusplus

50extern "C" {

51#endif

52

[ 53](fnmatch_8h.md#ae8c5fe22c6e8e83faa4a413e9f07f6a0)int [fnmatch](fnmatch_8h.md#ae8c5fe22c6e8e83faa4a413e9f07f6a0)(const char \*, const char \*, int);

54

55#ifdef \_\_cplusplus

56}

57#endif

58

59#endif /\* !\_FNMATCH\_H\_ \*/

[fnmatch](fnmatch_8h.md#ae8c5fe22c6e8e83faa4a413e9f07f6a0)

int fnmatch(const char \*, const char \*, int)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [fnmatch.h](fnmatch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
