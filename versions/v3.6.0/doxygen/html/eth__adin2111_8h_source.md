---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/eth__adin2111_8h_source.html
original_path: doxygen/html/eth__adin2111_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eth\_adin2111.h

[Go to the documentation of this file.](eth__adin2111_8h.md)

1/\*

2 \* Copyright (c) 2023 PHOENIX CONTACT Electronics GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_ADIN2111\_H\_\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_ADIN2111\_H\_\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

12#include <[zephyr/device.h](device_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 30](eth__adin2111_8h.md#a54e88cd118466a1a44ef02197fe2b59d)int [eth\_adin2111\_lock](eth__adin2111_8h.md#a54e88cd118466a1a44ef02197fe2b59d)(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout);

31

[ 41](eth__adin2111_8h.md#a72b5466138f087ac4e788bc878781c3e)int [eth\_adin2111\_unlock](eth__adin2111_8h.md#a72b5466138f087ac4e788bc878781c3e)(const struct [device](structdevice.md) \*dev);

42

[ 56](eth__adin2111_8h.md#ac768d3625f30e4a90903a3070347f38c)int [eth\_adin2111\_reg\_write](eth__adin2111_8h.md#ac768d3625f30e4a90903a3070347f38c)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

57

[ 71](eth__adin2111_8h.md#a06e40561475a7f997e706da388717414)int [eth\_adin2111\_reg\_read](eth__adin2111_8h.md#a06e40561475a7f997e706da388717414)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

72

73#ifdef \_\_cplusplus

74}

75#endif

76

77#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_ADIN2111\_H\_\_ \*/

[device.h](device_8h.md)

[eth\_adin2111\_reg\_read](eth__adin2111_8h.md#a06e40561475a7f997e706da388717414)

int eth\_adin2111\_reg\_read(const struct device \*dev, const uint16\_t reg, uint32\_t \*val)

Reads host MAC interface register over SPI.

[eth\_adin2111\_lock](eth__adin2111_8h.md#a54e88cd118466a1a44ef02197fe2b59d)

int eth\_adin2111\_lock(const struct device \*dev, k\_timeout\_t timeout)

Locks device access.

[eth\_adin2111\_unlock](eth__adin2111_8h.md#a72b5466138f087ac4e788bc878781c3e)

int eth\_adin2111\_unlock(const struct device \*dev)

Unlocks device access.

[eth\_adin2111\_reg\_write](eth__adin2111_8h.md#ac768d3625f30e4a90903a3070347f38c)

int eth\_adin2111\_reg\_write(const struct device \*dev, const uint16\_t reg, uint32\_t val)

Writes host MAC interface register over SPI.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ethernet](dir_e26e025f1b2d5c43527f6232564fe44e.md)
- [eth\_adin2111.h](eth__adin2111_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
