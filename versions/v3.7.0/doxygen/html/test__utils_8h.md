---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/test__utils_8h.html
original_path: doxygen/html/test__utils_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

test\_utils.h File Reference

`#include <[zephyr/tc_util.h](tc__util_8h_source.md)>`  
`#include <tinycrypt/constants.h>`

[Go to the source code of this file.](test__utils_8h_source.md)

| Functions | |
| --- | --- |
| static void | [show\_str](#ac6d829df5f0e4fd29a01d2302366bd6a) (const char \*label, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| static void | [fatal](#a0c05eeb12526a2c168109f7e5a40d833) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) testnum, const void \*expected, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) expectedlen, const void \*computed, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) computedlen) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [check\_result](#ade1c76cc0df2be800876862b3a5941ab) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) testnum, const void \*expected, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) expectedlen, const void \*computed, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) computedlen, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) verbose) |

## Function Documentation

## [◆ ](#ade1c76cc0df2be800876862b3a5941ab)check\_result()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) check\_result | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *testnum*, | | --- | --- | --- | --- | |  |  | const void \* | *expected*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *expectedlen*, | |  |  | const void \* | *computed*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *computedlen*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *verbose* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0c05eeb12526a2c168109f7e5a40d833)fatal()

| | void fatal | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *testnum*, | | --- | --- | --- | --- | |  |  | const void \* | *expected*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *expectedlen*, | |  |  | const void \* | *computed*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *computedlen* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac6d829df5f0e4fd29a01d2302366bd6a)show\_str()

| | void show\_str | ( | const char \* | *label*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *s*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [test\_utils.h](test__utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
