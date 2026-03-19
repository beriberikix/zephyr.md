---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/busy__sim_8h_source.html
original_path: doxygen/html/busy__sim_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

busy\_sim.h

[Go to the documentation of this file.](busy__sim_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef BUSY\_SIM\_H\_\_

7#define BUSY\_SIM\_H\_\_

8

[ 9](busy__sim_8h.md#a6b09e8372800e740a653f45f10a3501f)typedef void (\*[busy\_sim\_cb\_t](busy__sim_8h.md#a6b09e8372800e740a653f45f10a3501f))(void);

10

[ 32](busy__sim_8h.md#a2bb7c55b7e21ee9e5f927fcecd758705)void [busy\_sim\_start](busy__sim_8h.md#a2bb7c55b7e21ee9e5f927fcecd758705)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) active\_avg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) active\_delta,

33 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idle\_avg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idle\_delta, [busy\_sim\_cb\_t](busy__sim_8h.md#a6b09e8372800e740a653f45f10a3501f) cb);

34

[ 36](busy__sim_8h.md#ae7f199942b18363936dcb11fca8d0c96)void [busy\_sim\_stop](busy__sim_8h.md#ae7f199942b18363936dcb11fca8d0c96)(void);

37

38#endif /\* BUSY\_SIM\_H\_\_ \*/

[busy\_sim\_start](busy__sim_8h.md#a2bb7c55b7e21ee9e5f927fcecd758705)

void busy\_sim\_start(uint32\_t active\_avg, uint32\_t active\_delta, uint32\_t idle\_avg, uint32\_t idle\_delta, busy\_sim\_cb\_t cb)

Start busy simulator.

[busy\_sim\_cb\_t](busy__sim_8h.md#a6b09e8372800e740a653f45f10a3501f)

void(\* busy\_sim\_cb\_t)(void)

**Definition** busy\_sim.h:9

[busy\_sim\_stop](busy__sim_8h.md#ae7f199942b18363936dcb11fca8d0c96)

void busy\_sim\_stop(void)

Stop busy simulator.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [busy\_sim.h](busy__sim_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
