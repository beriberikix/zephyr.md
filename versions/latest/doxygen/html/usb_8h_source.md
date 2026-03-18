---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usb_8h_source.html
original_path: doxygen/html/usb_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb.h

[Go to the documentation of this file.](usb_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_USB\_USB\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_USB\_USB\_H\_

8

9/\* Ideally we'd generate this enum to match what's coming out of the YAML,

10 \* however, we dont have a good way to know how to name such an enum from

11 \* the generation point of view, so for now we just hand code the enum. This

12 \* enum is expected to match the order in the yaml (dts/bindings/usb/usb.yaml)

13 \*/

14

[ 15](usb_8h.md#ac343e285b07073790285bba59e3500bf)enum [dt\_usb\_maximum\_speed](usb_8h.md#ac343e285b07073790285bba59e3500bf) {

[ 16](usb_8h.md#ac343e285b07073790285bba59e3500bfaf5e69c61df9ae69910b5509564f91828) [DT\_USB\_MAXIMUM\_SPEED\_LOW\_SPEED](usb_8h.md#ac343e285b07073790285bba59e3500bfaf5e69c61df9ae69910b5509564f91828),

[ 17](usb_8h.md#ac343e285b07073790285bba59e3500bfac7256cb721aa6d6ae982314e13c5667e) [DT\_USB\_MAXIMUM\_SPEED\_FULL\_SPEED](usb_8h.md#ac343e285b07073790285bba59e3500bfac7256cb721aa6d6ae982314e13c5667e),

[ 18](usb_8h.md#ac343e285b07073790285bba59e3500bfab1b5b72e016a50503f9ff2661965340b) [DT\_USB\_MAXIMUM\_SPEED\_HIGH\_SPEED](usb_8h.md#ac343e285b07073790285bba59e3500bfab1b5b72e016a50503f9ff2661965340b),

[ 19](usb_8h.md#ac343e285b07073790285bba59e3500bfa98ef9ffd2b88d0780f79d258945e4f0d) [DT\_USB\_MAXIMUM\_SPEED\_SUPER\_SPEED](usb_8h.md#ac343e285b07073790285bba59e3500bfa98ef9ffd2b88d0780f79d258945e4f0d),

20};

21

22#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_USB\_USB\_H\_ \*/

[dt\_usb\_maximum\_speed](usb_8h.md#ac343e285b07073790285bba59e3500bf)

dt\_usb\_maximum\_speed

**Definition** usb.h:15

[DT\_USB\_MAXIMUM\_SPEED\_SUPER\_SPEED](usb_8h.md#ac343e285b07073790285bba59e3500bfa98ef9ffd2b88d0780f79d258945e4f0d)

@ DT\_USB\_MAXIMUM\_SPEED\_SUPER\_SPEED

**Definition** usb.h:19

[DT\_USB\_MAXIMUM\_SPEED\_HIGH\_SPEED](usb_8h.md#ac343e285b07073790285bba59e3500bfab1b5b72e016a50503f9ff2661965340b)

@ DT\_USB\_MAXIMUM\_SPEED\_HIGH\_SPEED

**Definition** usb.h:18

[DT\_USB\_MAXIMUM\_SPEED\_FULL\_SPEED](usb_8h.md#ac343e285b07073790285bba59e3500bfac7256cb721aa6d6ae982314e13c5667e)

@ DT\_USB\_MAXIMUM\_SPEED\_FULL\_SPEED

**Definition** usb.h:17

[DT\_USB\_MAXIMUM\_SPEED\_LOW\_SPEED](usb_8h.md#ac343e285b07073790285bba59e3500bfaf5e69c61df9ae69910b5509564f91828)

@ DT\_USB\_MAXIMUM\_SPEED\_LOW\_SPEED

**Definition** usb.h:16

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [usb](dir_b73aae62b1ec6442c36a8e8be819fb7c.md)
- [usb.h](usb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
