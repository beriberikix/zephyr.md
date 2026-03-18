---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sar__cfg_8h_source.html
original_path: doxygen/html/sar__cfg_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sar\_cfg.h

[Go to the documentation of this file.](sar__cfg_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef BT\_MESH\_SAR\_CFG\_H\_\_

8#define BT\_MESH\_SAR\_CFG\_H\_\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

[ 23](structbt__mesh__sar__tx.md)struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) {

[ 25](structbt__mesh__sar__tx.md#aa491eda390c1b9532e968ed566ec23c2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [seg\_int\_step](structbt__mesh__sar__tx.md#aa491eda390c1b9532e968ed566ec23c2);

26

[ 28](structbt__mesh__sar__tx.md#adaa856b561ac24c07706a04eea157183) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [unicast\_retrans\_count](structbt__mesh__sar__tx.md#adaa856b561ac24c07706a04eea157183);

29

[ 31](structbt__mesh__sar__tx.md#a1893bbeb473ebcf99db633e7f979b376) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [unicast\_retrans\_without\_prog\_count](structbt__mesh__sar__tx.md#a1893bbeb473ebcf99db633e7f979b376);

32

33 /\* SAR Unicast Retransmissions Interval Step state \*/

[ 34](structbt__mesh__sar__tx.md#a8e0ad5b5977bd4aad20bd79977a0342d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [unicast\_retrans\_int\_step](structbt__mesh__sar__tx.md#a8e0ad5b5977bd4aad20bd79977a0342d);

35

[ 37](structbt__mesh__sar__tx.md#a40a96d401f44345397bd605d6f25e04a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [unicast\_retrans\_int\_inc](structbt__mesh__sar__tx.md#a40a96d401f44345397bd605d6f25e04a);

38

[ 40](structbt__mesh__sar__tx.md#a686a6a4a7e6a7c6a532ddb8c8bad76df) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [multicast\_retrans\_count](structbt__mesh__sar__tx.md#a686a6a4a7e6a7c6a532ddb8c8bad76df);

41

[ 43](structbt__mesh__sar__tx.md#a6fec529b66c04f0828f5d5d716fd9281) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [multicast\_retrans\_int](structbt__mesh__sar__tx.md#a6fec529b66c04f0828f5d5d716fd9281);

44};

45

[ 47](structbt__mesh__sar__rx.md)struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) {

[ 49](structbt__mesh__sar__rx.md#a32a790589ddebee397d536b18518558d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [seg\_thresh](structbt__mesh__sar__rx.md#a32a790589ddebee397d536b18518558d);

50

[ 52](structbt__mesh__sar__rx.md#a5517a0f2167340cf59ef6fc72077f010) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ack\_delay\_inc](structbt__mesh__sar__rx.md#a5517a0f2167340cf59ef6fc72077f010);

53

[ 55](structbt__mesh__sar__rx.md#a70615d8df27b6f8291291b73abc57c9c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [discard\_timeout](structbt__mesh__sar__rx.md#a70615d8df27b6f8291291b73abc57c9c);

56

[ 58](structbt__mesh__sar__rx.md#ad277cc6c5d221aab7fd22581bfccd83c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_seg\_int\_step](structbt__mesh__sar__rx.md#ad277cc6c5d221aab7fd22581bfccd83c);

59

[ 61](structbt__mesh__sar__rx.md#aac228432bddf7f112ccbcb9e3d05d2ce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ack\_retrans\_count](structbt__mesh__sar__rx.md#aac228432bddf7f112ccbcb9e3d05d2ce);

62};

63

65

66#ifdef \_\_cplusplus

67}

68#endif

69

70#endif /\* BT\_MESH\_SAR\_CFG\_H\_\_ \*/

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md)

SAR Receiver Configuration state structure.

**Definition** sar\_cfg.h:47

[bt\_mesh\_sar\_rx::seg\_thresh](structbt__mesh__sar__rx.md#a32a790589ddebee397d536b18518558d)

uint8\_t seg\_thresh

SAR Segments Threshold state.

**Definition** sar\_cfg.h:49

[bt\_mesh\_sar\_rx::ack\_delay\_inc](structbt__mesh__sar__rx.md#a5517a0f2167340cf59ef6fc72077f010)

uint8\_t ack\_delay\_inc

SAR Acknowledgment Delay Increment state.

**Definition** sar\_cfg.h:52

[bt\_mesh\_sar\_rx::discard\_timeout](structbt__mesh__sar__rx.md#a70615d8df27b6f8291291b73abc57c9c)

uint8\_t discard\_timeout

SAR Discard Timeout state.

**Definition** sar\_cfg.h:55

[bt\_mesh\_sar\_rx::ack\_retrans\_count](structbt__mesh__sar__rx.md#aac228432bddf7f112ccbcb9e3d05d2ce)

uint8\_t ack\_retrans\_count

SAR Acknowledgment Retransmissions Count state.

**Definition** sar\_cfg.h:61

[bt\_mesh\_sar\_rx::rx\_seg\_int\_step](structbt__mesh__sar__rx.md#ad277cc6c5d221aab7fd22581bfccd83c)

uint8\_t rx\_seg\_int\_step

SAR Receiver Segment Interval Step state.

**Definition** sar\_cfg.h:58

[bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md)

SAR Transmitter Configuration state structure.

**Definition** sar\_cfg.h:23

[bt\_mesh\_sar\_tx::unicast\_retrans\_without\_prog\_count](structbt__mesh__sar__tx.md#a1893bbeb473ebcf99db633e7f979b376)

uint8\_t unicast\_retrans\_without\_prog\_count

SAR Unicast Retransmissions Without Progress Count state.

**Definition** sar\_cfg.h:31

[bt\_mesh\_sar\_tx::unicast\_retrans\_int\_inc](structbt__mesh__sar__tx.md#a40a96d401f44345397bd605d6f25e04a)

uint8\_t unicast\_retrans\_int\_inc

SAR Unicast Retransmissions Interval Increment state.

**Definition** sar\_cfg.h:37

[bt\_mesh\_sar\_tx::multicast\_retrans\_count](structbt__mesh__sar__tx.md#a686a6a4a7e6a7c6a532ddb8c8bad76df)

uint8\_t multicast\_retrans\_count

SAR Multicast Retransmissions Count state.

**Definition** sar\_cfg.h:40

[bt\_mesh\_sar\_tx::multicast\_retrans\_int](structbt__mesh__sar__tx.md#a6fec529b66c04f0828f5d5d716fd9281)

uint8\_t multicast\_retrans\_int

SAR Multicast Retransmissions Interval state.

**Definition** sar\_cfg.h:43

[bt\_mesh\_sar\_tx::unicast\_retrans\_int\_step](structbt__mesh__sar__tx.md#a8e0ad5b5977bd4aad20bd79977a0342d)

uint8\_t unicast\_retrans\_int\_step

**Definition** sar\_cfg.h:34

[bt\_mesh\_sar\_tx::seg\_int\_step](structbt__mesh__sar__tx.md#aa491eda390c1b9532e968ed566ec23c2)

uint8\_t seg\_int\_step

SAR Segment Interval Step state.

**Definition** sar\_cfg.h:25

[bt\_mesh\_sar\_tx::unicast\_retrans\_count](structbt__mesh__sar__tx.md#adaa856b561ac24c07706a04eea157183)

uint8\_t unicast\_retrans\_count

SAR Unicast Retransmissions Count state.

**Definition** sar\_cfg.h:28

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [sar\_cfg.h](sar__cfg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
