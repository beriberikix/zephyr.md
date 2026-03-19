---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dt-bindings_2regulator_2npm2100_8h_source.html
original_path: doxygen/html/dt-bindings_2regulator_2npm2100_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm2100.h

[Go to the documentation of this file.](dt-bindings_2regulator_2npm2100_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_REGULATOR\_NPM2100\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_REGULATOR\_NPM2100\_H\_

9

15

20/\* Load switch selection, applies to LDOSW only \*/

[ 21](group__regulator__npm2100.md#ga569097deae5cbbae4b13e68764f25515)#define NPM2100\_REG\_LDSW\_EN 0x01U

22

23/\* DPS modes applies to BOOST only \*/

[ 24](group__regulator__npm2100.md#gafd0d56cdad7a0df1d1ae43b4c5ca76d1)#define NPM2100\_REG\_DPS\_MASK 0x03U

[ 25](group__regulator__npm2100.md#ga73809745bcafc74b0f73ece10caa559c)#define NPM2100\_REG\_DPS\_ALLOW 0x01U

[ 26](group__regulator__npm2100.md#gaa181b892021300ddee2c01eb4d61bcb9)#define NPM2100\_REG\_DPS\_ALLOWLP 0x02U

27

28/\* Operating mode \*/

[ 29](group__regulator__npm2100.md#gaa6e5ecf67d72c55453ebbcc50b92a8cc)#define NPM2100\_REG\_OPER\_MASK 0x1CU

[ 30](group__regulator__npm2100.md#gaddb187c6dc66f1b22cee829b91a598b0)#define NPM2100\_REG\_OPER\_AUTO 0x00U

[ 31](group__regulator__npm2100.md#gae908cf304e1ede24848bf481d74763af)#define NPM2100\_REG\_OPER\_HP 0x04U

[ 32](group__regulator__npm2100.md#ga3b5df0968365f29dfe99c934782ed6ca)#define NPM2100\_REG\_OPER\_LP 0x08U

[ 33](group__regulator__npm2100.md#ga65d4c68f3aaa3ea510c6f1c65dd50726)#define NPM2100\_REG\_OPER\_ULP 0x0CU

[ 34](group__regulator__npm2100.md#gab5773cc53dd1fbec770c168b8f4386f3)#define NPM2100\_REG\_OPER\_PASS 0x10U

[ 35](group__regulator__npm2100.md#ga57d61d25772852b878d630d71ebbe53d)#define NPM2100\_REG\_OPER\_NOHP 0x14U

[ 36](group__regulator__npm2100.md#ga9022ba9c129e10ef8e267c620fa69231)#define NPM2100\_REG\_OPER\_OFF 0x18U

37

38/\* Forced mode when GPIO active \*/

[ 39](group__regulator__npm2100.md#gab50fd43479c41f1cab012a182dd2ee9c)#define NPM2100\_REG\_FORCE\_MASK 0xE0U

[ 40](group__regulator__npm2100.md#ga85d8e1bfc66500cd3512c7e27bbb723c)#define NPM2100\_REG\_FORCE\_HP 0x20U

[ 41](group__regulator__npm2100.md#ga87d44a14470755cf09885c7ae78c0bd1)#define NPM2100\_REG\_FORCE\_LP 0x40U

[ 42](group__regulator__npm2100.md#gaddd2186f564d706d9eca4fccb505c779)#define NPM2100\_REG\_FORCE\_ULP 0x60U

[ 43](group__regulator__npm2100.md#ga833e247b0085d31aaa3b3a08c2e75911)#define NPM2100\_REG\_FORCE\_PASS 0x80U

[ 44](group__regulator__npm2100.md#ga648677b18c19300206a758f0c9d78f6f)#define NPM2100\_REG\_FORCE\_NOHP 0xA0U

45

47

49

50#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_REGULATOR\_NPM2100\_H\_\*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [regulator](dir_9ff35155c0210c7a7568a63cba064bf6.md)
- [npm2100.h](dt-bindings_2regulator_2npm2100_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
