---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/qdec__nxp__tpm_8h_source.html
original_path: doxygen/html/qdec__nxp__tpm_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

qdec\_nxp\_tpm.h

[Go to the documentation of this file.](qdec__nxp__tpm_8h.md)

1/\*

2 \* Copyright (c) 2022, Prevas A/S

3 \* Copyright (c) 2025 NXP

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_QDEC\_NXP\_TPM\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_QDEC\_NXP\_TPM\_H\_

10

11#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

12

[ 13](qdec__nxp__tpm_8h.md#adab9169b39efa0b7ecbe1f5ae9c69830)enum [sensor\_attribute\_qdec\_tpm](qdec__nxp__tpm_8h.md#adab9169b39efa0b7ecbe1f5ae9c69830) {

14 /\* Number of counts per revolution \*/

[ 15](qdec__nxp__tpm_8h.md#adab9169b39efa0b7ecbe1f5ae9c69830adeea574ce5fbed87ca34dc26860428b2) [SENSOR\_ATTR\_QDEC\_MOD\_VAL](qdec__mcux_8h.md#a93f4f84af3e5a42381e9152750c46286adeea574ce5fbed87ca34dc26860428b2) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

16};

17

18#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_QDEC\_NXP\_TPM\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:372

[SENSOR\_ATTR\_QDEC\_MOD\_VAL](qdec__mcux_8h.md#a93f4f84af3e5a42381e9152750c46286adeea574ce5fbed87ca34dc26860428b2)

@ SENSOR\_ATTR\_QDEC\_MOD\_VAL

**Definition** qdec\_mcux.h:14

[sensor\_attribute\_qdec\_tpm](qdec__nxp__tpm_8h.md#adab9169b39efa0b7ecbe1f5ae9c69830)

sensor\_attribute\_qdec\_tpm

**Definition** qdec\_nxp\_tpm.h:13

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [qdec\_nxp\_tpm.h](qdec__nxp__tpm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
