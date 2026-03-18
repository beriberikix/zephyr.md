---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/log__backend__adsp__hda_8h_source.html
original_path: doxygen/html/log__backend__adsp__hda_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_adsp\_hda.h

[Go to the documentation of this file.](log__backend__adsp__hda_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LOG\_BACKEND\_ADSP\_HDA\_H\_

8#define ZEPHYR\_LOG\_BACKEND\_ADSP\_HDA\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

[ 18](log__backend__adsp__hda_8h.md#a8d50e67fece0cf916b72fcaa7c2bd11a)typedef void(\*[adsp\_hda\_log\_hook\_t](log__backend__adsp__hda_8h.md#a8d50e67fece0cf916b72fcaa7c2bd11a))([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) written);

19

[ 30](log__backend__adsp__hda_8h.md#ac9ae5b9b36f95d30643c0acf95d51e82)void [adsp\_hda\_log\_init](log__backend__adsp__hda_8h.md#ac9ae5b9b36f95d30643c0acf95d51e82)([adsp\_hda\_log\_hook\_t](log__backend__adsp__hda_8h.md#a8d50e67fece0cf916b72fcaa7c2bd11a) hook, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel);

31

32#endif /\* ZEPHYR\_LOG\_BACKEND\_ADSP\_HDA\_H\_ \*/

[adsp\_hda\_log\_hook\_t](log__backend__adsp__hda_8h.md#a8d50e67fece0cf916b72fcaa7c2bd11a)

void(\* adsp\_hda\_log\_hook\_t)(uint32\_t written)

HDA logger requires a hook for IPC messages.

**Definition** log\_backend\_adsp\_hda.h:18

[adsp\_hda\_log\_init](log__backend__adsp__hda_8h.md#ac9ae5b9b36f95d30643c0acf95d51e82)

void adsp\_hda\_log\_init(adsp\_hda\_log\_hook\_t hook, uint32\_t channel)

Initialize the Intel ADSP HDA logger.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_adsp\_hda.h](log__backend__adsp__hda_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
