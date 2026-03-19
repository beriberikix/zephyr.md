---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sip__svc__agilex__smc_8h_source.html
original_path: doxygen/html/sip__svc__agilex__smc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc\_agilex\_smc.h

[Go to the documentation of this file.](sip__svc__agilex__smc_8h.md)

1/\*

2 \* Copyright (c) 2022-2023, Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SIP\_SVC\_AGILEX\_SMC\_H\_

8#define ZEPHYR\_INCLUDE\_SIP\_SVC\_AGILEX\_SMC\_H\_

9

15

16/\* @brief SMC return status

17 \*/

18

[ 19](sip__svc__agilex__smc_8h.md#abca52daa3ed42c3acacd0a2f27a64c8b)#define SMC\_STATUS\_INVALID 0xFFFFFFFF

[ 20](sip__svc__agilex__smc_8h.md#aff7de6199219a46e9c177557a55b20ad)#define SMC\_STATUS\_OKAY 0

[ 21](sip__svc__agilex__smc_8h.md#a8959eae5cbbe690922a6aa35c3e6ad19)#define SMC\_STATUS\_BUSY 1

[ 22](sip__svc__agilex__smc_8h.md#a2350309516a2c57ec3250a53305d0627)#define SMC\_STATUS\_REJECT 2

[ 23](sip__svc__agilex__smc_8h.md#a1b99b2307df8b02a1f3dd36614077269)#define SMC\_STATUS\_NO\_RESPONSE 3

[ 24](sip__svc__agilex__smc_8h.md#a0f21a71f1245c31ef3a3a468901a7fe3)#define SMC\_STATUS\_ERROR 4

25

26/\* @brief SMC Intel Header at a1

27 \*

28 \* bit

29 \* 7: 0 Transaction ID

30 \* 59: 8 Reserved

31 \* 63:60 Version

32 \*/

[ 33](sip__svc__agilex__smc_8h.md#a149c807c9429c49b48febb7493ded05a)#define SMC\_PLAT\_PROTO\_VER 0x0

34

[ 35](sip__svc__agilex__smc_8h.md#aaf01ecddc145b991b1437dc4ccd88854)#define SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_OFFSET 0

[ 36](sip__svc__agilex__smc_8h.md#a8fe58b94720ef6bb2cb46351c9e3da8f)#define SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_MASK 0xFF

37

[ 38](sip__svc__agilex__smc_8h.md#ae9827c60ec0c0e0d62167672b443d136)#define SMC\_PLAT\_PROTO\_HEADER\_VER\_OFFSET 60

[ 39](sip__svc__agilex__smc_8h.md#a14cf7302d786ab126a18abbd0e757fed)#define SMC\_PLAT\_PROTO\_HEADER\_VER\_MASK 0xF

40

[ 41](sip__svc__agilex__smc_8h.md#a0ac21d31ae06d1fa1fd86253526baff2)#define SMC\_PLAT\_PROTO\_HEADER \

42 ((SMC\_PLAT\_PROTO\_VER & SMC\_PLAT\_PROTO\_HEADER\_VER\_MASK) << SMC\_PLAT\_PROTO\_HEADER\_VER\_OFFSET)

43

[ 44](sip__svc__agilex__smc_8h.md#aee5f5ecdeb83631a3114593e2e487a43)#define SMC\_PLAT\_PROTO\_HEADER\_SET\_TRANS\_ID(header, trans\_id) \

45 (header) &= \

46 ~(SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_MASK << SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_OFFSET); \

47 (header) |= (((trans\_id)&SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_MASK) \

48 << SMC\_PLAT\_PROTO\_HEADER\_TRANS\_ID\_OFFSET);

49

50/\* @brief SYNC SMC Function IDs

51 \*/

52

[ 53](sip__svc__agilex__smc_8h.md#afa8c0dca448e2074bfc6abeaffd26464)#define SMC\_FUNC\_ID\_GET\_SVC\_VERSION 0xC2000400

[ 54](sip__svc__agilex__smc_8h.md#afcaee0b300ae5fbe475c51c1d20b8e48)#define SMC\_FUNC\_ID\_REG\_READ 0xC2000401

[ 55](sip__svc__agilex__smc_8h.md#ab619bffd89340c1d72f3786d2c8d326b)#define SMC\_FUNC\_ID\_REG\_WRITE 0xC2000402

[ 56](sip__svc__agilex__smc_8h.md#ad56834ca5734a3d105e6810cb4821406)#define SMC\_FUNC\_ID\_REG\_UPDATE 0xC2000403

[ 57](sip__svc__agilex__smc_8h.md#a382037b06541eb54757b3ad9fd7df8a4)#define SMC\_FUNC\_ID\_SET\_HPS\_BRIDGES 0xC2000404

[ 58](sip__svc__agilex__smc_8h.md#abf081ba2e3a8039b42c40f8a7135c113)#define SMC\_FUNC\_ID\_RSU\_UPDATE\_ADDR 0xC2000405

59

60/\* @brief ASYNC SMC Function IDs

61 \*/

62

[ 63](sip__svc__agilex__smc_8h.md#a98d77f81a2b07bcf8305e28e0be1e4c4)#define SMC\_FUNC\_ID\_MAILBOX\_SEND\_COMMAND 0xC2000420

[ 64](sip__svc__agilex__smc_8h.md#ac26572cb1321697ff33adcd471e27874)#define SMC\_FUNC\_ID\_MAILBOX\_POLL\_RESPONSE 0xC2000421

65

66/\* @brief SDM mailbox CANCEL command

67 \*/

[ 68](sip__svc__agilex__smc_8h.md#a0a1d2a2c6a290c6b293fa71cd04975fb)#define MAILBOX\_CANCEL\_COMMAND 0x03

69

70#endif /\* ZEPHYR\_INCLUDE\_SIP\_SVC\_AGILEX\_SMC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sip\_svc](dir_be59f4c2e7724c8d2ef47362c82e9052.md)
- [sip\_svc\_agilex\_smc.h](sip__svc__agilex__smc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
