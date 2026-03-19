---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/smp__dummy_8h_source.html
original_path: doxygen/html/smp__dummy_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_dummy.h

[Go to the documentation of this file.](smp__dummy_8h.md)

1/\*

2 \* Copyright Runtime.io 2018. All rights reserved.

3 \* Copyright Laird Connectivity 2021-2022. All rights reserved.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

11#ifndef ZEPHYR\_INCLUDE\_MGMT\_MCUMGR\_TRANSPORT\_DUMMY\_H\_

12#define ZEPHYR\_INCLUDE\_MGMT\_MCUMGR\_TRANSPORT\_DUMMY\_H\_

13

14#include <[zephyr/kernel.h](kernel_8h.md)>

15#include <[zephyr/net\_buf.h](net__buf_8h.md)>

16#include <[zephyr/mgmt/mcumgr/mgmt/mgmt.h](mgmt_8h.md)>

17#include <[zephyr/mgmt/mcumgr/transport/serial.h](serial_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 26](smp__dummy_8h.md#ad9b3c7f35e4fa24fe863145a687f53db)void [smp\_dummy\_clear\_state](smp__dummy_8h.md#ad9b3c7f35e4fa24fe863145a687f53db)(void);

27

[ 34](smp__dummy_8h.md#a8bf3d0c12669c2cf5370eb7e148f10c2)void [dummy\_mcumgr\_add\_data](smp__dummy_8h.md#a8bf3d0c12669c2cf5370eb7e148f10c2)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_size);

35

[ 42](smp__dummy_8h.md#aa744df8e85bdb93cff2322b215164e9a)struct [net\_buf](structnet__buf.md) \*[smp\_dummy\_get\_outgoing](smp__dummy_8h.md#aa744df8e85bdb93cff2322b215164e9a)(void);

43

[ 53](smp__dummy_8h.md#a501596f79e8cf48fa1bb07484966fe53)bool [smp\_dummy\_wait\_for\_data](smp__dummy_8h.md#a501596f79e8cf48fa1bb07484966fe53)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_time\_s);

54

[ 58](smp__dummy_8h.md#ab5a47cd08e9467c969cbee9c85dcfe8a)void [smp\_dummy\_add\_data](smp__dummy_8h.md#ab5a47cd08e9467c969cbee9c85dcfe8a)(void);

59

[ 65](smp__dummy_8h.md#ab09b0ae8ed526252b4900e77afa57dc5)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [smp\_dummy\_get\_send\_pos](smp__dummy_8h.md#ab09b0ae8ed526252b4900e77afa57dc5)(void);

66

[ 72](smp__dummy_8h.md#a71158b7a935497506a6cc9e2f40a2b1e)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [smp\_dummy\_get\_receive\_pos](smp__dummy_8h.md#a71158b7a935497506a6cc9e2f40a2b1e)(void);

73

[ 82](smp__dummy_8h.md#a5440421e4994119fc98ec119706e4dd9)int [smp\_dummy\_tx\_pkt](smp__dummy_8h.md#a5440421e4994119fc98ec119706e4dd9)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), int [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

83

[ 87](smp__dummy_8h.md#adde2de8dc7895bda0e5d72a961dfba78)void [smp\_dummy\_enable](smp__dummy_8h.md#adde2de8dc7895bda0e5d72a961dfba78)(void);

88

[ 92](smp__dummy_8h.md#a57d38b86c8b826ef1d49bcae0565b772)void [smp\_dummy\_disable](smp__dummy_8h.md#a57d38b86c8b826ef1d49bcae0565b772)(void);

93

[ 99](smp__dummy_8h.md#a364817f12c377c6538867c6118d071c6)bool [smp\_dummy\_get\_status](smp__dummy_8h.md#a364817f12c377c6538867c6118d071c6)(void);

100

101#ifdef \_\_cplusplus

102}

103#endif

104

105#endif /\* ZEPHYR\_INCLUDE\_MGMT\_MCUMGR\_TRANSPORT\_DUMMY\_H\_ \*/

[kernel.h](kernel_8h.md)

Public kernel APIs.

[mgmt.h](mgmt_8h.md)

[net\_buf.h](net__buf_8h.md)

Buffer management.

[serial.h](serial_8h.md)

[smp\_dummy\_get\_status](smp__dummy_8h.md#a364817f12c377c6538867c6118d071c6)

bool smp\_dummy\_get\_status(void)

Returns status on if the dummy SMP system is active.

[smp\_dummy\_wait\_for\_data](smp__dummy_8h.md#a501596f79e8cf48fa1bb07484966fe53)

bool smp\_dummy\_wait\_for\_data(uint32\_t wait\_time\_s)

Waits for a period of time for outgoing SMPC data to be ready and returns either when a full message ...

[smp\_dummy\_tx\_pkt](smp__dummy_8h.md#a5440421e4994119fc98ec119706e4dd9)

int smp\_dummy\_tx\_pkt(const uint8\_t \*data, int len)

Converts input data to go out through the internal SMPC buffer.

[smp\_dummy\_disable](smp__dummy_8h.md#a57d38b86c8b826ef1d49bcae0565b772)

void smp\_dummy\_disable(void)

Disables the dummy SMP module (will not process sent/received data).

[smp\_dummy\_get\_receive\_pos](smp__dummy_8h.md#a71158b7a935497506a6cc9e2f40a2b1e)

uint16\_t smp\_dummy\_get\_receive\_pos(void)

Gets current receive buffer position.

[dummy\_mcumgr\_add\_data](smp__dummy_8h.md#a8bf3d0c12669c2cf5370eb7e148f10c2)

void dummy\_mcumgr\_add\_data(uint8\_t \*data, uint16\_t data\_size)

Adds SMPC data to the internal buffer to be processed.

[smp\_dummy\_get\_outgoing](smp__dummy_8h.md#aa744df8e85bdb93cff2322b215164e9a)

struct net\_buf \* smp\_dummy\_get\_outgoing(void)

Processes a single line (fragment) coming from the mcumgr response to be used in tests.

[smp\_dummy\_get\_send\_pos](smp__dummy_8h.md#ab09b0ae8ed526252b4900e77afa57dc5)

uint16\_t smp\_dummy\_get\_send\_pos(void)

Gets current send buffer position.

[smp\_dummy\_add\_data](smp__dummy_8h.md#ab5a47cd08e9467c969cbee9c85dcfe8a)

void smp\_dummy\_add\_data(void)

Calls dummy\_mcumgr\_add\_data with the internal SMPC receive buffer.

[smp\_dummy\_clear\_state](smp__dummy_8h.md#ad9b3c7f35e4fa24fe863145a687f53db)

void smp\_dummy\_clear\_state(void)

Clears internal dummy SMP state and resets semaphore.

[smp\_dummy\_enable](smp__dummy_8h.md#adde2de8dc7895bda0e5d72a961dfba78)

void smp\_dummy\_enable(void)

Enabled the dummy SMP module (will process sent/received data).

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_buf::data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** net\_buf.h:1032

[net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)

uint16\_t len

Length of the data behind the data pointer.

**Definition** net\_buf.h:1035

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [smp\_dummy.h](smp__dummy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
