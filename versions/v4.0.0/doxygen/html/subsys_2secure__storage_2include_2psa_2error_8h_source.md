---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h_source.html
original_path: doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error.h

[Go to the documentation of this file.](subsys_2secure__storage_2include_2psa_2error_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef PSA\_ERROR\_H

5#define PSA\_ERROR\_H

11#include <[stdint.h](stdint_8h.md)>

12

[ 13](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9)typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9);

14

[ 15](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1)#define PSA\_SUCCESS ((psa\_status\_t)0)

16

[ 17](subsys_2secure__storage_2include_2psa_2error_8h.md#a8bfafd6baac18ce5d3192d1de256238f)#define PSA\_ERROR\_GENERIC\_ERROR ((psa\_status\_t)-132)

[ 18](subsys_2secure__storage_2include_2psa_2error_8h.md#a4d1b8dd8526177a15a210b7afc1accb1)#define PSA\_ERROR\_NOT\_PERMITTED ((psa\_status\_t)-133)

[ 19](subsys_2secure__storage_2include_2psa_2error_8h.md#a1dcc6d130633ed5db8942257581b55dd)#define PSA\_ERROR\_NOT\_SUPPORTED ((psa\_status\_t)-134)

[ 20](subsys_2secure__storage_2include_2psa_2error_8h.md#a798df25a505ebf931f7bec1f80f1f85f)#define PSA\_ERROR\_INVALID\_ARGUMENT ((psa\_status\_t)-135)

[ 21](subsys_2secure__storage_2include_2psa_2error_8h.md#af2b34cc87edc72f3ba90071a08210d20)#define PSA\_ERROR\_ALREADY\_EXISTS ((psa\_status\_t)-139)

[ 22](subsys_2secure__storage_2include_2psa_2error_8h.md#a18646babb2ae6cbde02ea3828bbd9141)#define PSA\_ERROR\_DOES\_NOT\_EXIST ((psa\_status\_t)-140)

[ 23](subsys_2secure__storage_2include_2psa_2error_8h.md#a897a45eb206a6f6b7be7ffbe36f0d766)#define PSA\_ERROR\_INSUFFICIENT\_STORAGE ((psa\_status\_t)-142)

[ 24](subsys_2secure__storage_2include_2psa_2error_8h.md#add169a1af2707862b95fb9df91dfc37d)#define PSA\_ERROR\_STORAGE\_FAILURE ((psa\_status\_t)-146)

[ 25](subsys_2secure__storage_2include_2psa_2error_8h.md#a35927f755d232c4766de600f2c49e9f2)#define PSA\_ERROR\_INVALID\_SIGNATURE ((psa\_status\_t)-149)

[ 26](subsys_2secure__storage_2include_2psa_2error_8h.md#a9febb81a44bdeb4c6c42bf4f697b13bf)#define PSA\_ERROR\_DATA\_CORRUPT ((psa\_status\_t)-152)

27

29#endif

[stdint.h](stdint_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9)

int32\_t psa\_status\_t

**Definition** error.h:13

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [psa](dir_d06fbc62883e41d574c8881d2ac75d4f.md)
- [error.h](subsys_2secure__storage_2include_2psa_2error_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
