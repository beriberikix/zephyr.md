---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/emul__stub__device_8h_source.html
original_path: doxygen/html/emul__stub__device_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul\_stub\_device.h

[Go to the documentation of this file.](emul__stub__device_8h.md)

1/\*

2 \* Copyright 2023 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_EMUL\_STUB\_DEVICE\_H\_

8#define ZEPHYR\_INCLUDE\_EMUL\_STUB\_DEVICE\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/devicetree.h](devicetree_8h.md)>

12

13/\*

14 \* Needed for emulators without corresponding DEVICE\_DT\_DEFINE drivers

15 \*/

16

[ 17](structemul__stub__dev__data.md)struct [emul\_stub\_dev\_data](structemul__stub__dev__data.md) {

18 /\* Stub \*/

19};

[ 20](structemul__stub__dev__config.md)struct [emul\_stub\_dev\_config](structemul__stub__dev__config.md) {

21 /\* Stub \*/

22};

[ 23](structemul__stub__dev__api.md)struct [emul\_stub\_dev\_api](structemul__stub__dev__api.md) {

24 /\* Stub \*/

25};

26

27/\* For every instance of a DT\_DRV\_COMPAT stub out a device for that instance \*/

[ 28](emul__stub__device_8h.md#ae42dec3fd3ebdfc8ab5c1b9eabea26d0)#define EMUL\_STUB\_DEVICE(n) \

29 \_\_maybe\_unused static int emul\_init\_stub\_##n(const struct device \*dev) \

30 { \

31 ARG\_UNUSED(dev); \

32 return 0; \

33 } \

34 \

35 static struct emul\_stub\_dev\_data stub\_data\_##n; \

36 static struct emul\_stub\_dev\_config stub\_config\_##n; \

37 static struct emul\_stub\_dev\_api stub\_api\_##n; \

38 DEVICE\_DT\_INST\_DEFINE(n, &emul\_init\_stub\_##n, NULL, &stub\_data\_##n, &stub\_config\_##n, \

39 POST\_KERNEL, CONFIG\_KERNEL\_INIT\_PRIORITY\_DEVICE, &stub\_api\_##n);

40

41#endif /\* ZEPHYR\_INCLUDE\_EMUL\_STUB\_DEVICE\_H\_ \*/

[device.h](device_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[emul\_stub\_dev\_api](structemul__stub__dev__api.md)

**Definition** emul\_stub\_device.h:23

[emul\_stub\_dev\_config](structemul__stub__dev__config.md)

**Definition** emul\_stub\_device.h:20

[emul\_stub\_dev\_data](structemul__stub__dev__data.md)

**Definition** emul\_stub\_device.h:17

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul\_stub\_device.h](emul__stub__device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
