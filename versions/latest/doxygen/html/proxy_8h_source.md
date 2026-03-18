---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/proxy_8h_source.html
original_path: doxygen/html/proxy_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

proxy.h

[Go to the documentation of this file.](proxy_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_PROXY\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_PROXY\_H\_

12

13#include <[stdint.h](stdint_8h.md)>

14

15#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

16#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

17

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

[ 33](structbt__mesh__proxy__cb.md)struct [bt\_mesh\_proxy\_cb](structbt__mesh__proxy__cb.md) {

[ 39](structbt__mesh__proxy__cb.md#ae6f129ae511681d2f1fccafedba47918) void (\*[identity\_enabled](structbt__mesh__proxy__cb.md#ae6f129ae511681d2f1fccafedba47918))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx);

[ 45](structbt__mesh__proxy__cb.md#a207ebf7e3f1f1e732d4540af000bf2ef) void (\*[identity\_disabled](structbt__mesh__proxy__cb.md#a207ebf7e3f1f1e732d4540af000bf2ef))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx);

46};

47

[ 56](group__bt__mesh__proxy.md#ga325b71c3d7ed69952bf760c0288b28ef)#define BT\_MESH\_PROXY\_CB\_DEFINE(\_name) \

57 static const STRUCT\_SECTION\_ITERABLE( \

58 bt\_mesh\_proxy\_cb, \_CONCAT(bt\_mesh\_proxy\_cb\_, \_name))

59

[ 68](group__bt__mesh__proxy.md#ga7fb3c76f1be6943dd4a18f26e8dd18e7)int [bt\_mesh\_proxy\_identity\_enable](group__bt__mesh__proxy.md#ga7fb3c76f1be6943dd4a18f26e8dd18e7)(void);

69

[ 78](group__bt__mesh__proxy.md#gaecd529a9fd0df83b3d775d32885802f1)int [bt\_mesh\_proxy\_private\_identity\_enable](group__bt__mesh__proxy.md#gaecd529a9fd0df83b3d775d32885802f1)(void);

79

[ 88](group__bt__mesh__proxy.md#ga07d4edf80bdbc39f626f66720035c98b)int [bt\_mesh\_proxy\_connect](group__bt__mesh__proxy.md#ga07d4edf80bdbc39f626f66720035c98b)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx);

89

[ 98](group__bt__mesh__proxy.md#gaa9978d460b31412c96c6c1685729ec4f)int [bt\_mesh\_proxy\_disconnect](group__bt__mesh__proxy.md#gaa9978d460b31412c96c6c1685729ec4f)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx);

99

[ 113](group__bt__mesh__proxy.md#ga9a72515992af4f93a34a6c1aaf69d8df)int [bt\_mesh\_proxy\_solicit](group__bt__mesh__proxy.md#ga9a72515992af4f93a34a6c1aaf69d8df)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx);

114

115#ifdef \_\_cplusplus

116}

117#endif

118

122

123#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_PROXY\_H\_ \*/

[bt\_mesh\_proxy\_connect](group__bt__mesh__proxy.md#ga07d4edf80bdbc39f626f66720035c98b)

int bt\_mesh\_proxy\_connect(uint16\_t net\_idx)

Allow Proxy Client to auto connect to a network.

[bt\_mesh\_proxy\_identity\_enable](group__bt__mesh__proxy.md#ga7fb3c76f1be6943dd4a18f26e8dd18e7)

int bt\_mesh\_proxy\_identity\_enable(void)

Enable advertising with Node Identity.

[bt\_mesh\_proxy\_solicit](group__bt__mesh__proxy.md#ga9a72515992af4f93a34a6c1aaf69d8df)

int bt\_mesh\_proxy\_solicit(uint16\_t net\_idx)

Schedule advertising of Solicitation PDUs.

[bt\_mesh\_proxy\_disconnect](group__bt__mesh__proxy.md#gaa9978d460b31412c96c6c1685729ec4f)

int bt\_mesh\_proxy\_disconnect(uint16\_t net\_idx)

Disallow Proxy Client to auto connect to a network.

[bt\_mesh\_proxy\_private\_identity\_enable](group__bt__mesh__proxy.md#gaecd529a9fd0df83b3d775d32885802f1)

int bt\_mesh\_proxy\_private\_identity\_enable(void)

Enable advertising with Private Node Identity.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_proxy\_cb](structbt__mesh__proxy__cb.md)

Callbacks for the Proxy feature.

**Definition** proxy.h:33

[bt\_mesh\_proxy\_cb::identity\_disabled](structbt__mesh__proxy__cb.md#a207ebf7e3f1f1e732d4540af000bf2ef)

void(\* identity\_disabled)(uint16\_t net\_idx)

Stopped sending Node Identity beacons on the given subnet.

**Definition** proxy.h:45

[bt\_mesh\_proxy\_cb::identity\_enabled](structbt__mesh__proxy__cb.md#ae6f129ae511681d2f1fccafedba47918)

void(\* identity\_enabled)(uint16\_t net\_idx)

Started sending Node Identity beacons on the given subnet.

**Definition** proxy.h:39

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [proxy.h](proxy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
