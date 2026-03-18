---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/task__wdt_8h_source.html
original_path: doxygen/html/task__wdt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

task\_wdt.h

[Go to the documentation of this file.](task__wdt_8h.md)

1/\*

2 \* Copyright (c) 2020 Libre Solar Technologies GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

16

17#ifndef TASK\_WDT\_H\_

18#define TASK\_WDT\_H\_

19

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

22#include <[zephyr/device.h](device_8h.md)>

23

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

[ 36](group__task__wdt__api.md#gab9b9e2dd0eb52e324806cc5090507c45)typedef void (\*[task\_wdt\_callback\_t](group__task__wdt__api.md#gab9b9e2dd0eb52e324806cc5090507c45))(int channel\_id, void \*user\_data);

37

[ 54](group__task__wdt__api.md#gafa31c31c13478669615ebf0bbdd28a0c)int [task\_wdt\_init](group__task__wdt__api.md#gafa31c31c13478669615ebf0bbdd28a0c)(const struct [device](structdevice.md) \*hw\_wdt);

55

[ 73](group__task__wdt__api.md#ga26484bd148a9e2910d9989a1d9598230)int [task\_wdt\_add](group__task__wdt__api.md#ga26484bd148a9e2910d9989a1d9598230)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reload\_period, [task\_wdt\_callback\_t](group__task__wdt__api.md#gab9b9e2dd0eb52e324806cc5090507c45) callback,

74 void \*user\_data);

75

[ 87](group__task__wdt__api.md#ga631c1243b5a00a304687cc54e2632c0d)int [task\_wdt\_delete](group__task__wdt__api.md#ga631c1243b5a00a304687cc54e2632c0d)(int channel\_id);

88

[ 101](group__task__wdt__api.md#ga00fc594cace06d6308efa1ded45a22fc)int [task\_wdt\_feed](group__task__wdt__api.md#ga00fc594cace06d6308efa1ded45a22fc)(int channel\_id);

102

103#ifdef \_\_cplusplus

104}

105#endif

106

110

111#endif /\* TASK\_WDT\_H\_ \*/

[device.h](device_8h.md)

[task\_wdt\_feed](group__task__wdt__api.md#ga00fc594cace06d6308efa1ded45a22fc)

int task\_wdt\_feed(int channel\_id)

Feed specified watchdog channel.

[task\_wdt\_add](group__task__wdt__api.md#ga26484bd148a9e2910d9989a1d9598230)

int task\_wdt\_add(uint32\_t reload\_period, task\_wdt\_callback\_t callback, void \*user\_data)

Install new timeout.

[task\_wdt\_delete](group__task__wdt__api.md#ga631c1243b5a00a304687cc54e2632c0d)

int task\_wdt\_delete(int channel\_id)

Delete task watchdog channel.

[task\_wdt\_callback\_t](group__task__wdt__api.md#gab9b9e2dd0eb52e324806cc5090507c45)

void(\* task\_wdt\_callback\_t)(int channel\_id, void \*user\_data)

Task watchdog callback.

**Definition** task\_wdt.h:36

[task\_wdt\_init](group__task__wdt__api.md#gafa31c31c13478669615ebf0bbdd28a0c)

int task\_wdt\_init(const struct device \*hw\_wdt)

Initialize task watchdog.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [task\_wdt](dir_590994245f36812650ae1f422575e718.md)
- [task\_wdt.h](task__wdt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
