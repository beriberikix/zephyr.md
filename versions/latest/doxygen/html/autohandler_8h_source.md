---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/autohandler_8h_source.html
original_path: doxygen/html/autohandler_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

autohandler.h

[Go to the documentation of this file.](autohandler_8h.md)

1/\*

2 \* Copyright (c) 2024 Vogl Electronic GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

18

19#ifndef ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_AUTOHANDLER\_H\_

20#define ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_AUTOHANDLER\_H\_

21

22#include <[zephyr/mgmt/hawkbit/hawkbit.h](hawkbit_2hawkbit_8h.md)>

23

[ 32](group__hawkbit__autohandler.md#ga41865255aa3020a34816c23ae7977f20)void [hawkbit\_autohandler](group__hawkbit__autohandler.md#ga41865255aa3020a34816c23ae7977f20)(bool auto\_reschedule);

33

[ 45](group__hawkbit__autohandler.md#ga6d13b3d7b9a61d06a6eaa346189a08c6)enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) [hawkbit\_autohandler\_wait](group__hawkbit__autohandler.md#ga6d13b3d7b9a61d06a6eaa346189a08c6)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events, [k\_timeout\_t](structk__timeout__t.md) timeout);

46

[ 52](group__hawkbit__autohandler.md#gabc27308bb974d6e0b9650476243e5e9a)int [hawkbit\_autohandler\_cancel](group__hawkbit__autohandler.md#gabc27308bb974d6e0b9650476243e5e9a)(void);

53

[ 67](group__hawkbit__autohandler.md#ga47fe3e9cd227fd4da332e9eeff81f991)int [hawkbit\_autohandler\_set\_delay](group__hawkbit__autohandler.md#ga47fe3e9cd227fd4da332e9eeff81f991)([k\_timeout\_t](structk__timeout__t.md) timeout, bool if\_bigger);

68

72

73#endif /\* ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_AUTOHANDLER\_H\_ \*/

[hawkbit\_autohandler](group__hawkbit__autohandler.md#ga41865255aa3020a34816c23ae7977f20)

void hawkbit\_autohandler(bool auto\_reschedule)

Runs hawkBit probe and hawkBit update automatically.

[hawkbit\_autohandler\_set\_delay](group__hawkbit__autohandler.md#ga47fe3e9cd227fd4da332e9eeff81f991)

int hawkbit\_autohandler\_set\_delay(k\_timeout\_t timeout, bool if\_bigger)

Set the delay for the next run of the autohandler.

[hawkbit\_autohandler\_wait](group__hawkbit__autohandler.md#ga6d13b3d7b9a61d06a6eaa346189a08c6)

enum hawkbit\_response hawkbit\_autohandler\_wait(uint32\_t events, k\_timeout\_t timeout)

Wait for the autohandler to finish.

[hawkbit\_autohandler\_cancel](group__hawkbit__autohandler.md#gabc27308bb974d6e0b9650476243e5e9a)

int hawkbit\_autohandler\_cancel(void)

Cancel the run of the hawkBit autohandler.

[hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b)

hawkbit\_response

Response message from hawkBit.

**Definition** hawkbit.h:33

[hawkbit.h](hawkbit_2hawkbit_8h.md)

hawkBit main header file

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [hawkbit](dir_a48dfaa3f142fb7c063e17169510ae85.md)
- [autohandler.h](autohandler_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
