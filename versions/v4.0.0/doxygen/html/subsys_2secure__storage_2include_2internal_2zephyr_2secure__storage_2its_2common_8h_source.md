---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_source.html
original_path: doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

common.h

[Go to the documentation of this file.](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef SECURE\_STORAGE\_ITS\_COMMON\_H

5#define SECURE\_STORAGE\_ITS\_COMMON\_H

6

10#include "[../common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md)"

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12#include <[psa/storage\_common.h](storage__common_8h.md)>

13

[ 18](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2b)typedef enum {

[ 19](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2ba8ee890874c86e0717973bc03208499bd) [SECURE\_STORAGE\_ITS\_CALLER\_PSA\_ITS](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2ba8ee890874c86e0717973bc03208499bd),

[ 20](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2badb6049a90872ae6773af2817093cce5d) [SECURE\_STORAGE\_ITS\_CALLER\_PSA\_PS](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2badb6049a90872ae6773af2817093cce5d),

[ 21](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2ba22e2c3976fbb36461f6587372ce9314b) [SECURE\_STORAGE\_ITS\_CALLER\_MBEDTLS](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2ba22e2c3976fbb36461f6587372ce9314b),

22} [secure\_storage\_its\_caller\_id\_t](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2b);

23

[ 25](structsecure__storage__its__uid__t.md)typedef struct {

[ 26](structsecure__storage__its__uid__t.md#a444f3c47521ef82e086c0c43941e23ee) [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) [uid](structsecure__storage__its__uid__t.md#a444f3c47521ef82e086c0c43941e23ee);

[ 27](structsecure__storage__its__uid__t.md#a8f581033ce88a130f3a6b04c9821294e) [secure\_storage\_its\_caller\_id\_t](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2b) [caller\_id](structsecure__storage__its__uid__t.md#a8f581033ce88a130f3a6b04c9821294e);

28} \_\_packed [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md);

29

30#endif

[storage\_common.h](storage__common_8h.md)

Common definitions of the PSA Secure Storage API.

[psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6)

uint64\_t psa\_storage\_uid\_t

UID type for identifying entries.

**Definition** storage\_common.h:23

[secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md)

The UID (caller + entry IDs) of an ITS entry.

**Definition** common.h:25

[secure\_storage\_its\_uid\_t::uid](structsecure__storage__its__uid__t.md#a444f3c47521ef82e086c0c43941e23ee)

psa\_storage\_uid\_t uid

**Definition** common.h:26

[secure\_storage\_its\_uid\_t::caller\_id](structsecure__storage__its__uid__t.md#a8f581033ce88a130f3a6b04c9821294e)

secure\_storage\_its\_caller\_id\_t caller\_id

**Definition** common.h:27

[common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md)

Common definitions of the secure storage subsystem.

[secure\_storage\_its\_caller\_id\_t](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2b)

secure\_storage\_its\_caller\_id\_t

The ID of the caller from which the ITS API call originates.

**Definition** common.h:18

[SECURE\_STORAGE\_ITS\_CALLER\_MBEDTLS](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2ba22e2c3976fbb36461f6587372ce9314b)

@ SECURE\_STORAGE\_ITS\_CALLER\_MBEDTLS

**Definition** common.h:21

[SECURE\_STORAGE\_ITS\_CALLER\_PSA\_ITS](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2ba8ee890874c86e0717973bc03208499bd)

@ SECURE\_STORAGE\_ITS\_CALLER\_PSA\_ITS

**Definition** common.h:19

[SECURE\_STORAGE\_ITS\_CALLER\_PSA\_PS](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md#a2369ff303bf323cb4e57f1b970093d2badb6049a90872ae6773af2817093cce5d)

@ SECURE\_STORAGE\_ITS\_CALLER\_PSA\_PS

**Definition** common.h:20

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [its](dir_8ffdb9b26f60d93440ec7ee1d2751029.md)
- [common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
