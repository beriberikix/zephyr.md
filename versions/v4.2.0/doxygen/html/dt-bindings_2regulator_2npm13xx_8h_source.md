---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/dt-bindings_2regulator_2npm13xx_8h_source.html
original_path: doxygen/html/dt-bindings_2regulator_2npm13xx_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm13xx.h

[Go to the documentation of this file.](dt-bindings_2regulator_2npm13xx_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_REGULATOR\_NPM13XX\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_REGULATOR\_NPM13XX\_H\_

9

15

20/\* Buck modes \*/

[ 21](group__regulator__npm13xx.md#gaa6a9106d64b5c69eb0bcd8a49f7395cf)#define NPM13XX\_BUCK\_MODE\_AUTO 0x00U

[ 22](group__regulator__npm13xx.md#ga04f737111a1c0f78e14679764a10273d)#define NPM13XX\_BUCK\_MODE\_PWM 0x01U

[ 23](group__regulator__npm13xx.md#gabcc7d0fb606c6bbfa7a73a555e16b40c)#define NPM13XX\_BUCK\_MODE\_PFM 0x04U

24

25/\* LDSW / LDO modes \*/

[ 26](group__regulator__npm13xx.md#ga4a7899bf6566240cb5488aee91d6a660)#define NPM13XX\_LDSW\_MODE\_LDO 0x02U

[ 27](group__regulator__npm13xx.md#gaf3b3cd08075c1f5852408a50c98c0278)#define NPM13XX\_LDSW\_MODE\_LDSW 0x03U

28

29/\* GPIO control configuration \*/

[ 30](group__regulator__npm13xx.md#gaca83ea4645a3529feef3c6d0494123a5)#define NPM13XX\_GPIO\_CHAN\_NONE 0x00U

[ 31](group__regulator__npm13xx.md#ga489b934362bcc80189ae6cb58a753d30)#define NPM13XX\_GPIO\_CHAN\_0 0x01U

[ 32](group__regulator__npm13xx.md#ga2c2eca66af7e59189c6db79f937d265a)#define NPM13XX\_GPIO\_CHAN\_1 0x02U

[ 33](group__regulator__npm13xx.md#gaed068808f742637fadee82eee4e30a1e)#define NPM13XX\_GPIO\_CHAN\_2 0x03U

[ 34](group__regulator__npm13xx.md#gad9e0eaf56c8789eb7edbdca0775402ee)#define NPM13XX\_GPIO\_CHAN\_3 0x04U

[ 35](group__regulator__npm13xx.md#gaaab0ba89f22f93480c18f79d17f8a9d0)#define NPM13XX\_GPIO\_CHAN\_4 0x05U

36

38

40

41#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_REGULATOR\_NPM13XX\_H\_\*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [regulator](dir_9ff35155c0210c7a7568a63cba064bf6.md)
- [npm13xx.h](dt-bindings_2regulator_2npm13xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
