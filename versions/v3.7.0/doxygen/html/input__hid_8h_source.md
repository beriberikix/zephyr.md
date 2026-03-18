---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/input__hid_8h_source.html
original_path: doxygen/html/input__hid_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_hid.h

[Go to the documentation of this file.](input__hid_8h.md)

1/\*

2 \* Copyright 2024 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_INPUT\_HID\_H\_

8#define ZEPHYR\_INCLUDE\_INPUT\_HID\_H\_

9

14

[ 26](group__input__interface.md#ga094b3ccfc2e111c4b2a000e9c2fe133c)[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [input\_to\_hid\_code](group__input__interface.md#ga094b3ccfc2e111c4b2a000e9c2fe133c)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) input\_code);

27

[ 38](group__input__interface.md#ga86ac2267d08e91bcc09c5b091042cfde)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [input\_to\_hid\_modifier](group__input__interface.md#ga86ac2267d08e91bcc09c5b091042cfde)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) input\_code);

39

41

42#endif /\* ZEPHYR\_INCLUDE\_INPUT\_HID\_H\_ \*/

[input\_to\_hid\_code](group__input__interface.md#ga094b3ccfc2e111c4b2a000e9c2fe133c)

int16\_t input\_to\_hid\_code(uint16\_t input\_code)

Convert an input code to HID code.

[input\_to\_hid\_modifier](group__input__interface.md#ga86ac2267d08e91bcc09c5b091042cfde)

uint8\_t input\_to\_hid\_modifier(uint16\_t input\_code)

Convert an input code to HID modifier.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_hid.h](input__hid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
