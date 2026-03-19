---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/params_8h_source.html
original_path: doxygen/html/params_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

params.h

[Go to the documentation of this file.](params_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\*

4 \* Permission is hereby granted, free of charge, to any person obtaining a copy

5 \* of this software and associated documentation files (the "Software"), to

6 \* deal in the Software without restriction, including without limitation the

7 \* rights to use, copy, modify, merge, publish, distribute, sublicense, and/or

8 \* sell copies of the Software, and to permit persons to whom the Software is

9 \* furnished to do so, subject to the following conditions:

10 \*

11 \* The above copyright notice and this permission notice shall be included in

12 \* all copies or substantial portions of the Software.

13 \*

14 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

15 \* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

16 \* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

17 \* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

18 \* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING

19 \* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER

20 \* DEALINGS IN THE SOFTWARE.

21 \*

22 \* Copyright (c) 2007, Keir Fraser

23 \*/

24

25#ifndef \_\_XEN\_PUBLIC\_HVM\_PARAMS\_H\_\_

26#define \_\_XEN\_PUBLIC\_HVM\_PARAMS\_H\_\_

27

28#include "[hvm\_op.h](hvm__op_8h.md)"

29

30/\*

31 \* These are not used by Xen. They are here for convenience of HVM-guest

32 \* xenbus implementations.

33 \*/

[ 34](params_8h.md#a9bce3ce400b9ffbaf311dd28a5e35b0a)#define HVM\_PARAM\_STORE\_PFN 1

[ 35](params_8h.md#a1048ebeefb4866be6781863b44026779)#define HVM\_PARAM\_STORE\_EVTCHN 2

36

37/\* Console debug shared memory ring and event channel \*/

[ 38](params_8h.md#a39fc3d97c0f343b7abf263ae5175b8ca)#define HVM\_PARAM\_CONSOLE\_PFN 17

[ 39](params_8h.md#a00e5f65cf70ae90180529027092fe410)#define HVM\_PARAM\_CONSOLE\_EVTCHN 18

40

41#endif /\* \_\_XEN\_PUBLIC\_HVM\_PARAMS\_H\_\_ \*/

[hvm\_op.h](hvm__op_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [hvm](dir_18c76ebef650877b932e646710239d41.md)
- [params.h](params_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
