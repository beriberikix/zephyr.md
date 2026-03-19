---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/multiboot__info_8h_source.html
original_path: doxygen/html/multiboot__info_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

multiboot\_info.h

[Go to the documentation of this file.](multiboot__info_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_MULTIBOOT\_INFO\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_X86\_MULTIBOOT\_INFO\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12/\*

13 \* Multiboot (version 1) boot information structure.

14 \*

15 \* Only fields/values of interest to Zephyr are enumerated

16 \*/

17

[ 18](structmultiboot__info.md)struct [multiboot\_info](structmultiboot__info.md) {

[ 19](structmultiboot__info.md#a33c78eb1aec2573f8293acf9a42fe2a8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structmultiboot__info.md#a33c78eb1aec2573f8293acf9a42fe2a8);

[ 20](structmultiboot__info.md#a8c88b721d871cb57a51feb5cd5fbdb6c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mem\_lower](structmultiboot__info.md#a8c88b721d871cb57a51feb5cd5fbdb6c);

[ 21](structmultiboot__info.md#a8ecb8953e55d1f6b75a3892cdc82a0b5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mem\_upper](structmultiboot__info.md#a8ecb8953e55d1f6b75a3892cdc82a0b5);

[ 22](structmultiboot__info.md#a769182fd546a2231c7cec58ea1a77789) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unused0](structmultiboot__info.md#a769182fd546a2231c7cec58ea1a77789);

[ 23](structmultiboot__info.md#aac1e78293233aa63654d4c0161820201) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmdline](structmultiboot__info.md#aac1e78293233aa63654d4c0161820201);

[ 24](structmultiboot__info.md#a2fda76c274faccbc23a2b1e1155be45d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unused1](structmultiboot__info.md#a2fda76c274faccbc23a2b1e1155be45d)[6];

[ 25](structmultiboot__info.md#a65bfac8b5152c771a4b8eadd408ca0d6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mmap\_length](structmultiboot__info.md#a65bfac8b5152c771a4b8eadd408ca0d6);

[ 26](structmultiboot__info.md#ac977f37274093fd9874d68dfb038e143) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mmap\_addr](structmultiboot__info.md#ac977f37274093fd9874d68dfb038e143);

[ 27](structmultiboot__info.md#a44d645d01d52f7ad6fc82c37b7a66e37) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unused2](structmultiboot__info.md#a44d645d01d52f7ad6fc82c37b7a66e37)[9];

[ 28](structmultiboot__info.md#a4470854aa62c829c5ada578876a68944) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fb\_addr\_lo](structmultiboot__info.md#a4470854aa62c829c5ada578876a68944);

[ 29](structmultiboot__info.md#a51ec099821903ee057a8163272da2760) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fb\_addr\_hi](structmultiboot__info.md#a51ec099821903ee057a8163272da2760);

[ 30](structmultiboot__info.md#a1a412fb3d3f792b173787a65f32450d6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fb\_pitch](structmultiboot__info.md#a1a412fb3d3f792b173787a65f32450d6);

[ 31](structmultiboot__info.md#ac0d58fbf588108f6f0109db47efeae37) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fb\_width](structmultiboot__info.md#ac0d58fbf588108f6f0109db47efeae37);

[ 32](structmultiboot__info.md#a2a23c846d241bbb1469ec8565e8b3cef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fb\_height](structmultiboot__info.md#a2a23c846d241bbb1469ec8565e8b3cef);

[ 33](structmultiboot__info.md#a0a5bc6718a8cae87416553fa6100b013) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fb\_bpp](structmultiboot__info.md#a0a5bc6718a8cae87416553fa6100b013);

[ 34](structmultiboot__info.md#a33735d95e34f7fc9588cea69efbb5075) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fb\_type](structmultiboot__info.md#a33735d95e34f7fc9588cea69efbb5075);

[ 35](structmultiboot__info.md#a7ddf1b8d00568efa22fbc11074d6fc98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fb\_color\_info](structmultiboot__info.md#a7ddf1b8d00568efa22fbc11074d6fc98)[6];

36};

37

[ 38](multiboot__info_8h.md#a8cb99862e8314c32c007eee9d2481ae1)typedef struct [multiboot\_info](structmultiboot__info.md) [multiboot\_info\_t](multiboot__info_8h.md#a8cb99862e8314c32c007eee9d2481ae1);

39

40#endif

[multiboot\_info\_t](multiboot__info_8h.md#a8cb99862e8314c32c007eee9d2481ae1)

struct multiboot\_info multiboot\_info\_t

**Definition** multiboot\_info.h:38

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[multiboot\_info](structmultiboot__info.md)

**Definition** multiboot\_info.h:18

[multiboot\_info::fb\_bpp](structmultiboot__info.md#a0a5bc6718a8cae87416553fa6100b013)

uint8\_t fb\_bpp

**Definition** multiboot\_info.h:33

[multiboot\_info::fb\_pitch](structmultiboot__info.md#a1a412fb3d3f792b173787a65f32450d6)

uint32\_t fb\_pitch

**Definition** multiboot\_info.h:30

[multiboot\_info::fb\_height](structmultiboot__info.md#a2a23c846d241bbb1469ec8565e8b3cef)

uint32\_t fb\_height

**Definition** multiboot\_info.h:32

[multiboot\_info::unused1](structmultiboot__info.md#a2fda76c274faccbc23a2b1e1155be45d)

uint32\_t unused1[6]

**Definition** multiboot\_info.h:24

[multiboot\_info::fb\_type](structmultiboot__info.md#a33735d95e34f7fc9588cea69efbb5075)

uint8\_t fb\_type

**Definition** multiboot\_info.h:34

[multiboot\_info::flags](structmultiboot__info.md#a33c78eb1aec2573f8293acf9a42fe2a8)

uint32\_t flags

**Definition** multiboot\_info.h:19

[multiboot\_info::fb\_addr\_lo](structmultiboot__info.md#a4470854aa62c829c5ada578876a68944)

uint32\_t fb\_addr\_lo

**Definition** multiboot\_info.h:28

[multiboot\_info::unused2](structmultiboot__info.md#a44d645d01d52f7ad6fc82c37b7a66e37)

uint32\_t unused2[9]

**Definition** multiboot\_info.h:27

[multiboot\_info::fb\_addr\_hi](structmultiboot__info.md#a51ec099821903ee057a8163272da2760)

uint32\_t fb\_addr\_hi

**Definition** multiboot\_info.h:29

[multiboot\_info::mmap\_length](structmultiboot__info.md#a65bfac8b5152c771a4b8eadd408ca0d6)

uint32\_t mmap\_length

**Definition** multiboot\_info.h:25

[multiboot\_info::unused0](structmultiboot__info.md#a769182fd546a2231c7cec58ea1a77789)

uint32\_t unused0

**Definition** multiboot\_info.h:22

[multiboot\_info::fb\_color\_info](structmultiboot__info.md#a7ddf1b8d00568efa22fbc11074d6fc98)

uint8\_t fb\_color\_info[6]

**Definition** multiboot\_info.h:35

[multiboot\_info::mem\_lower](structmultiboot__info.md#a8c88b721d871cb57a51feb5cd5fbdb6c)

uint32\_t mem\_lower

**Definition** multiboot\_info.h:20

[multiboot\_info::mem\_upper](structmultiboot__info.md#a8ecb8953e55d1f6b75a3892cdc82a0b5)

uint32\_t mem\_upper

**Definition** multiboot\_info.h:21

[multiboot\_info::cmdline](structmultiboot__info.md#aac1e78293233aa63654d4c0161820201)

uint32\_t cmdline

**Definition** multiboot\_info.h:23

[multiboot\_info::fb\_width](structmultiboot__info.md#ac0d58fbf588108f6f0109db47efeae37)

uint32\_t fb\_width

**Definition** multiboot\_info.h:31

[multiboot\_info::mmap\_addr](structmultiboot__info.md#ac977f37274093fd9874d68dfb038e143)

uint32\_t mmap\_addr

**Definition** multiboot\_info.h:26

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [multiboot\_info.h](multiboot__info_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
