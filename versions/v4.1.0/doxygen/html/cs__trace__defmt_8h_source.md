---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cs__trace__defmt_8h_source.html
original_path: doxygen/html/cs__trace__defmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cs\_trace\_defmt.h

[Go to the documentation of this file.](cs__trace__defmt_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DEBUG\_CORESIGHT\_CS\_TRACE\_DEFMT\_H\_\_

8#define ZEPHYR\_INCLUDE\_DEBUG\_CORESIGHT\_CS\_TRACE\_DEFMT\_H\_\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

23

[ 30](group__cs__trace__defmt.md#gaccc05f92bfbc04b787f6f959e954115d)typedef void (\*[cs\_trace\_defmt\_cb](group__cs__trace__defmt.md#gaccc05f92bfbc04b787f6f959e954115d))([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

31

[ 33](group__cs__trace__defmt.md#gabecbf043f9f0888a0b60d2784aff55e3)#define CORESIGHT\_TRACE\_FRAME\_SIZE32 4

34

[ 36](group__cs__trace__defmt.md#ga7a31378ad5570f930cab4227a018d80d)#define CORESIGHT\_TRACE\_FRAME\_SIZE (CORESIGHT\_TRACE\_FRAME\_SIZE32 \* sizeof(uint32\_t))

37

[ 42](group__cs__trace__defmt.md#gaaeaaefe2221161691144d82c932196ca)int [cs\_trace\_defmt\_init](group__cs__trace__defmt.md#gaaeaaefe2221161691144d82c932196ca)([cs\_trace\_defmt\_cb](group__cs__trace__defmt.md#gaccc05f92bfbc04b787f6f959e954115d) cb);

43

[ 56](group__cs__trace__defmt.md#ga109bab752da74692779aa3eb96b771ba)int [cs\_trace\_defmt\_process](group__cs__trace__defmt.md#ga109bab752da74692779aa3eb96b771ba)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

57

59

60#ifdef \_\_cplusplus

61}

62#endif

63

64#endif /\* ZEPHYR\_INCLUDE\_DEBUG\_CORESIGHT\_CS\_TRACE\_DEFMT\_H\_\_ \*/

[cs\_trace\_defmt\_process](group__cs__trace__defmt.md#ga109bab752da74692779aa3eb96b771ba)

int cs\_trace\_defmt\_process(const uint8\_t \*data, size\_t len)

Decode data from the stream.

[cs\_trace\_defmt\_init](group__cs__trace__defmt.md#gaaeaaefe2221161691144d82c932196ca)

int cs\_trace\_defmt\_init(cs\_trace\_defmt\_cb cb)

Initialize Coresight Trace Deformatter.

[cs\_trace\_defmt\_cb](group__cs__trace__defmt.md#gaccc05f92bfbc04b787f6f959e954115d)

void(\* cs\_trace\_defmt\_cb)(uint32\_t id, const uint8\_t \*data, size\_t len)

Callback signature.

**Definition** cs\_trace\_defmt.h:30

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [coresight](dir_9e253c82b70fbbc4699540bacc17d458.md)
- [cs\_trace\_defmt.h](cs__trace__defmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
