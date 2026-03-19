---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm_2cortex__a__r_2mpu_8h_source.html
original_path: doxygen/html/arm_2cortex__a__r_2mpu_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpu.h

[Go to the documentation of this file.](arm_2cortex__a__r_2mpu_8h.md)

1/\* SPDX-License-Identifier: Apache-2.0

2 \*

3 \* Copyright (c) 2019 Lexmark International, Inc.

4 \*/

5#ifndef ARCH\_ARM\_CORTEX\_R\_MPU\_H

6#define ARCH\_ARM\_CORTEX\_R\_MPU\_H 1

7

[ 8](arm_2cortex__a__r_2mpu_8h.md#a33905dca89aa5b5bb9aa9518094b8b80)#define MPU\_RBAR\_ADDR\_Msk (~0x1f)

[ 9](arm_2cortex__a__r_2mpu_8h.md#af6c4850fc33a5f13a42cf25dbce72646)#define MPU\_RASR\_ENABLE\_Msk (1)

10

[ 11](arm_2cortex__a__r_2mpu_8h.md#ad90549193db0d2b7e70d3d52cb902710)#define MPU\_RASR\_SIZE\_Pos 1U

[ 12](arm_2cortex__a__r_2mpu_8h.md#a222e237e51f20d0e8a8c249295e77298)#define MPU\_RASR\_SIZE\_Msk (0x1FUL << MPU\_RASR\_SIZE\_Pos)

13

[ 14](arm_2cortex__a__r_2mpu_8h.md#a4d090ef632d2ba3a6ae4078c2594d6d3)#define MPU\_TYPE\_DREGION\_Pos 8U

[ 15](arm_2cortex__a__r_2mpu_8h.md#a3a5d2e6871b1518dca61e28b18aec6cb)#define MPU\_TYPE\_DREGION\_Msk (0xFFUL << MPU\_TYPE\_DREGION\_Pos)

16

[ 17](arm_2cortex__a__r_2mpu_8h.md#aa02d0a5dd8b96fb9500cb5f31c9ea67b)#define MPU\_RASR\_XN\_Pos 12

[ 18](arm_2cortex__a__r_2mpu_8h.md#a4f8afc5cc7fca2ada211f8b09c76802e)#define MPU\_RASR\_XN\_Msk (1UL << MPU\_RASR\_XN\_Pos)

19

[ 20](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)#define MPU\_RASR\_AP\_Pos 8

[ 21](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)#define MPU\_RASR\_AP\_Msk (0x7UL << MPU\_RASR\_AP\_Pos)

22

[ 23](arm_2cortex__a__r_2mpu_8h.md#a340f1c91469c5bb4ee91bc29ad21c631)#define MPU\_RASR\_TEX\_Pos 3

[ 24](arm_2cortex__a__r_2mpu_8h.md#a94f4b4a368986c1955b92743046a1f4e)#define MPU\_RASR\_TEX\_Msk (0x7UL << MPU\_RASR\_TEX\_Pos)

25

[ 26](arm_2cortex__a__r_2mpu_8h.md#a1820e125a5aa584cd49ede44c742985c)#define MPU\_RASR\_S\_Pos 2

[ 27](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361)#define MPU\_RASR\_S\_Msk (1UL << MPU\_RASR\_S\_Pos)

28

[ 29](arm_2cortex__a__r_2mpu_8h.md#a3a1631f2c85c66ead1d6d4cea9c16a52)#define MPU\_RASR\_C\_Pos 1

[ 30](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1)#define MPU\_RASR\_C\_Msk (1UL << MPU\_RASR\_C\_Pos)

31

[ 32](arm_2cortex__a__r_2mpu_8h.md#ae9ea3c456f66c56040a2e55793c63cf5)#define MPU\_RASR\_B\_Pos 0

[ 33](arm_2cortex__a__r_2mpu_8h.md#af97de2b86316d5b29931fc6f70b3cba1)#define MPU\_RASR\_B\_Msk (1UL << MPU\_RASR\_B\_Pos)

34

35#if defined(CONFIG\_CPU\_CORTEX\_R4) || defined(CONFIG\_CPU\_CORTEX\_R5) || defined(CONFIG\_CPU\_CORTEX\_R8)

36#define ARM\_MPU\_REGION\_SIZE\_32B ((uint8\_t)0x04U)

37#define ARM\_MPU\_REGION\_SIZE\_64B ((uint8\_t)0x05U)

38#define ARM\_MPU\_REGION\_SIZE\_128B ((uint8\_t)0x06U)

39#endif

40

[ 41](arm_2cortex__a__r_2mpu_8h.md#ad9d8775a432b076a44a93cbf725e8619)#define ARM\_MPU\_REGION\_SIZE\_256B ((uint8\_t)0x07U)

[ 42](arm_2cortex__a__r_2mpu_8h.md#a79a3000f14a4d30b77e513c4db53cbe5)#define ARM\_MPU\_REGION\_SIZE\_512B ((uint8\_t)0x08U)

[ 43](arm_2cortex__a__r_2mpu_8h.md#ae5bf2b5255a76ff6b62dfaed01580e9d)#define ARM\_MPU\_REGION\_SIZE\_1KB ((uint8\_t)0x09U)

[ 44](arm_2cortex__a__r_2mpu_8h.md#ad4d916f22b3737207c55b8d0d165caee)#define ARM\_MPU\_REGION\_SIZE\_2KB ((uint8\_t)0x0aU)

[ 45](arm_2cortex__a__r_2mpu_8h.md#a0612fe51de2b25b49692290d072d829c)#define ARM\_MPU\_REGION\_SIZE\_4KB ((uint8\_t)0x0bU)

[ 46](arm_2cortex__a__r_2mpu_8h.md#a4ce38a1ed6641648a2d2a66f48dbcb24)#define ARM\_MPU\_REGION\_SIZE\_8KB ((uint8\_t)0x0cU)

[ 47](arm_2cortex__a__r_2mpu_8h.md#af7a1b511ea419cb40777e0eaf32cc7e2)#define ARM\_MPU\_REGION\_SIZE\_16KB ((uint8\_t)0x0dU)

[ 48](arm_2cortex__a__r_2mpu_8h.md#a4d0d0ebcc97c9f24618808b66847056a)#define ARM\_MPU\_REGION\_SIZE\_32KB ((uint8\_t)0x0eU)

[ 49](arm_2cortex__a__r_2mpu_8h.md#ad0c79b123d9c7954c48fda30ef25b609)#define ARM\_MPU\_REGION\_SIZE\_64KB ((uint8\_t)0x0fU)

[ 50](arm_2cortex__a__r_2mpu_8h.md#a362c22f584b2822b8f451e356cba39d4)#define ARM\_MPU\_REGION\_SIZE\_128KB ((uint8\_t)0x10U)

[ 51](arm_2cortex__a__r_2mpu_8h.md#ac489a9c4e5b9cdf9acd7748c9616499b)#define ARM\_MPU\_REGION\_SIZE\_256KB ((uint8\_t)0x11U)

[ 52](arm_2cortex__a__r_2mpu_8h.md#a074f11c22a2c6e4deaf1e8f78717730d)#define ARM\_MPU\_REGION\_SIZE\_512KB ((uint8\_t)0x12U)

[ 53](arm_2cortex__a__r_2mpu_8h.md#aa2f3cf8222d50742ff33c94b7c8b3612)#define ARM\_MPU\_REGION\_SIZE\_1MB ((uint8\_t)0x13U)

[ 54](arm_2cortex__a__r_2mpu_8h.md#a2109105e7e283d5a5cf88772b776e441)#define ARM\_MPU\_REGION\_SIZE\_2MB ((uint8\_t)0x14U)

[ 55](arm_2cortex__a__r_2mpu_8h.md#a5d38b84546726a09a19c28f8de770b11)#define ARM\_MPU\_REGION\_SIZE\_4MB ((uint8\_t)0x15U)

[ 56](arm_2cortex__a__r_2mpu_8h.md#a62bebf6281c66f54f1d35ca43429c631)#define ARM\_MPU\_REGION\_SIZE\_8MB ((uint8\_t)0x16U)

[ 57](arm_2cortex__a__r_2mpu_8h.md#af3f56fa6ceeede9a0106d7f98b27a31e)#define ARM\_MPU\_REGION\_SIZE\_16MB ((uint8\_t)0x17U)

[ 58](arm_2cortex__a__r_2mpu_8h.md#a8b5fabd9bb7508e14e1bae69529a5853)#define ARM\_MPU\_REGION\_SIZE\_32MB ((uint8\_t)0x18U)

[ 59](arm_2cortex__a__r_2mpu_8h.md#a8fb3e1bb94b66387331a84c5c488286a)#define ARM\_MPU\_REGION\_SIZE\_64MB ((uint8\_t)0x19U)

[ 60](arm_2cortex__a__r_2mpu_8h.md#ae8fd2daf98ba641d02ff7ca3978a3ad9)#define ARM\_MPU\_REGION\_SIZE\_128MB ((uint8\_t)0x1aU)

[ 61](arm_2cortex__a__r_2mpu_8h.md#acce8e377f172943311b6268118bfcfdf)#define ARM\_MPU\_REGION\_SIZE\_256MB ((uint8\_t)0x1bU)

[ 62](arm_2cortex__a__r_2mpu_8h.md#a55ee4d5868b59de98bad7107243c2a95)#define ARM\_MPU\_REGION\_SIZE\_512MB ((uint8\_t)0x1cU)

[ 63](arm_2cortex__a__r_2mpu_8h.md#ac8d05ede24fdfca60537ca47f86dce1d)#define ARM\_MPU\_REGION\_SIZE\_1GB ((uint8\_t)0x1dU)

[ 64](arm_2cortex__a__r_2mpu_8h.md#a8f5d28ac5a55d84a4d0cf271e06bbb19)#define ARM\_MPU\_REGION\_SIZE\_2GB ((uint8\_t)0x1eU)

[ 65](arm_2cortex__a__r_2mpu_8h.md#ace58a7f0428b94180b8e61e29564f408)#define ARM\_MPU\_REGION\_SIZE\_4GB ((uint8\_t)0x1fU)

66

67#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [mpu.h](arm_2cortex__a__r_2mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
