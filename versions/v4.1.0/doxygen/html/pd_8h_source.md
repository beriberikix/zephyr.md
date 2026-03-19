---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pd_8h_source.html
original_path: doxygen/html/pd_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd.h

[Go to the documentation of this file.](pd_8h.md)

1/\*

2 \* Copyright 2022 The Chromium OS Authors

3 \* SPDX-License-Identifier: Apache-2.0

4 \*

5 \* This is based on Linux, documentation:

6 \* https://github.com/torvalds/linux/blob/v5.19/include/dt-bindings/usb/pd.h

7 \*/

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_USBC\_PD\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_USBC\_PD\_H\_

10

11/\* Power delivery Power Data Object definitions \*/

[ 12](pd_8h.md#a6696a76fb9196a66939b81bb7288402d)#define PDO\_TYPE\_FIXED 0

[ 13](pd_8h.md#a45dd0576f017e7c246bafc798ea33b32)#define PDO\_TYPE\_BATT 1

[ 14](pd_8h.md#a017a6b931cfbb3bd2a9958f0010fcb3d)#define PDO\_TYPE\_VAR 2

[ 15](pd_8h.md#ae34a1d74ce1a88355bdca50ee5ebd5d9)#define PDO\_TYPE\_APDO 3

16

[ 17](pd_8h.md#a194c22d06729436e5e0b9e80db85d157)#define PDO\_TYPE\_SHIFT 30

[ 18](pd_8h.md#a1e9f657ac9a2a7bafa774e55ae5eb1b7)#define PDO\_TYPE\_MASK 0x3

19

[ 20](pd_8h.md#adc26e319ccbe5212476507dd6e70fbd7)#define PDO\_TYPE(t) ((t) << PDO\_TYPE\_SHIFT)

21

[ 22](pd_8h.md#ac41dc08efe8dfeeb1a9737e0b187c683)#define PDO\_VOLT\_MASK 0x3ff

[ 23](pd_8h.md#aed2ef8943d23c433e924c51939f3783a)#define PDO\_CURR\_MASK 0x3ff

[ 24](pd_8h.md#a413d2bcbc7bb4748868c665d85f01c79)#define PDO\_PWR\_MASK 0x3ff

25

[ 26](pd_8h.md#a06df29b5b810f22013ad2135cb0238ea)#define PDO\_FIXED\_DUAL\_ROLE (1 << 29) /\* Power role swap supported \*/

[ 27](pd_8h.md#a869842bccecddf1941826fba3399f735)#define PDO\_FIXED\_SUSPEND (1 << 28) /\* USB Suspend supported (Source) \*/

[ 28](pd_8h.md#ae7692e9c32e7c6ee2cf8e4c84d0752d8)#define PDO\_FIXED\_HIGHER\_CAP (1 << 28) /\* Requires more than vSafe5V (Sink) \*/

[ 29](pd_8h.md#a9e098ecbd9e7b74052fcbf302a0f6a41)#define PDO\_FIXED\_EXTPOWER (1 << 27) /\* Externally powered \*/

[ 30](pd_8h.md#a398ebc832c89bd8cbccd08b3def758dd)#define PDO\_FIXED\_USB\_COMM (1 << 26) /\* USB communications capable \*/

[ 31](pd_8h.md#a17760e6fb2761a8d14d41f1f44993c3b)#define PDO\_FIXED\_DATA\_SWAP (1 << 25) /\* Data role swap supported \*/

[ 32](pd_8h.md#a3742e41a81b5a58bba31237993e1415d)#define PDO\_FIXED\_VOLT\_SHIFT 10 /\* 50mV units \*/

[ 33](pd_8h.md#a40951b7090fb5345b9160ba9bee5ff6f)#define PDO\_FIXED\_CURR\_SHIFT 0 /\* 10mA units \*/

34

[ 35](pd_8h.md#ac084b8a13ba4b179054feb6e4cc806ee)#define PDO\_FIXED\_VOLT(mv) ((((mv) / 50) & PDO\_VOLT\_MASK) << PDO\_FIXED\_VOLT\_SHIFT)

[ 36](pd_8h.md#a565f2b493b29406d391581e23cfe7c55)#define PDO\_FIXED\_CURR(ma) ((((ma) / 10) & PDO\_CURR\_MASK) << PDO\_FIXED\_CURR\_SHIFT)

37

[ 38](pd_8h.md#a9fa615ab7f38385c21277d4e9e6a1441)#define PDO\_FIXED(mv, ma, flags) \

39 (PDO\_TYPE(PDO\_TYPE\_FIXED) | (flags) | \

40 PDO\_FIXED\_VOLT(mv) | PDO\_FIXED\_CURR(ma))

41

[ 42](pd_8h.md#ae3c4f39fb7ff5b00bdc25676af3b88f7)#define VSAFE5V 5000 /\* mv units \*/

43

[ 44](pd_8h.md#a901fc8fe941e77426090cd631f973f58)#define PDO\_BATT\_MAX\_VOLT\_SHIFT 20 /\* 50mV units \*/

[ 45](pd_8h.md#ac6cfbddae5f56f963153813597fefe36)#define PDO\_BATT\_MIN\_VOLT\_SHIFT 10 /\* 50mV units \*/

[ 46](pd_8h.md#a055085209166ac4aaf53dd3391f5755d)#define PDO\_BATT\_MAX\_PWR\_SHIFT 0 /\* 250mW units \*/

47

[ 48](pd_8h.md#add0856842113d1368e4fefc81ed4a268)#define PDO\_BATT\_MIN\_VOLT(mv) ((((mv) / 50) & PDO\_VOLT\_MASK) << PDO\_BATT\_MIN\_VOLT\_SHIFT)

[ 49](pd_8h.md#af4d54399ae043b87fd39563aca66ec76)#define PDO\_BATT\_MAX\_VOLT(mv) ((((mv) / 50) & PDO\_VOLT\_MASK) << PDO\_BATT\_MAX\_VOLT\_SHIFT)

[ 50](pd_8h.md#a13827f707f980bda4359191ba17e1f43)#define PDO\_BATT\_MAX\_POWER(mw) ((((mw) / 250) & PDO\_PWR\_MASK) << PDO\_BATT\_MAX\_PWR\_SHIFT)

51

[ 52](pd_8h.md#a37daa9cc2b8482e127d31c2f3ea4e7ed)#define PDO\_BATT(min\_mv, max\_mv, max\_mw) \

53 (PDO\_TYPE(PDO\_TYPE\_BATT) | PDO\_BATT\_MIN\_VOLT(min\_mv) | \

54 PDO\_BATT\_MAX\_VOLT(max\_mv) | PDO\_BATT\_MAX\_POWER(max\_mw))

55

[ 56](pd_8h.md#acdb43c5ba716e1c8ac98923a99c6c714)#define PDO\_VAR\_MAX\_VOLT\_SHIFT 20 /\* 50mV units \*/

[ 57](pd_8h.md#a718ca0a2cc3f17ff8cf0f4e1ba9ed6a7)#define PDO\_VAR\_MIN\_VOLT\_SHIFT 10 /\* 50mV units \*/

[ 58](pd_8h.md#afa16fcdf0864263bbe31d7f6c7370fcb)#define PDO\_VAR\_MAX\_CURR\_SHIFT 0 /\* 10mA units \*/

59

[ 60](pd_8h.md#a4e1d88119e9b14ffd5ebeafe4a04612a)#define PDO\_VAR\_MIN\_VOLT(mv) ((((mv) / 50) & PDO\_VOLT\_MASK) << PDO\_VAR\_MIN\_VOLT\_SHIFT)

[ 61](pd_8h.md#a93d66b588325ac868279a44990623a11)#define PDO\_VAR\_MAX\_VOLT(mv) ((((mv) / 50) & PDO\_VOLT\_MASK) << PDO\_VAR\_MAX\_VOLT\_SHIFT)

[ 62](pd_8h.md#afdbaa131df861f379c482e0672b97367)#define PDO\_VAR\_MAX\_CURR(ma) ((((ma) / 10) & PDO\_CURR\_MASK) << PDO\_VAR\_MAX\_CURR\_SHIFT)

63

[ 64](pd_8h.md#a359cf8ce52c69924cd2962b2a766f794)#define PDO\_VAR(min\_mv, max\_mv, max\_ma) \

65 (PDO\_TYPE(PDO\_TYPE\_VAR) | PDO\_VAR\_MIN\_VOLT(min\_mv) | \

66 PDO\_VAR\_MAX\_VOLT(max\_mv) | PDO\_VAR\_MAX\_CURR(max\_ma))

67

[ 68](pd_8h.md#aa48ea0300d5342ef46c5c56ee73bca24)#define APDO\_TYPE\_PPS 0

69

[ 70](pd_8h.md#acbed8599e3d5edf52987fde3949a1933)#define PDO\_APDO\_TYPE\_SHIFT 28 /\* Only valid value currently is 0x0 - PPS \*/

[ 71](pd_8h.md#a4abb13b016cd5d491c0c80495e24d89f)#define PDO\_APDO\_TYPE\_MASK 0x3

72

[ 73](pd_8h.md#ad52459e0b7390f0545d38c880128c636)#define PDO\_APDO\_TYPE(t) ((t) << PDO\_APDO\_TYPE\_SHIFT)

74

[ 75](pd_8h.md#a4582653b731dcaad55436deff9a4ae1f)#define PDO\_PPS\_APDO\_MAX\_VOLT\_SHIFT 17 /\* 100mV units \*/

[ 76](pd_8h.md#aaa6c1342446f4fbf7809359b1b59f168)#define PDO\_PPS\_APDO\_MIN\_VOLT\_SHIFT 8 /\* 100mV units \*/

[ 77](pd_8h.md#a5c5db3948d197b4611efde32f2374293)#define PDO\_PPS\_APDO\_MAX\_CURR\_SHIFT 0 /\* 50mA units \*/

78

[ 79](pd_8h.md#a0d66b7f12dd1750b673e9d01d5be70a3)#define PDO\_PPS\_APDO\_VOLT\_MASK 0xff

[ 80](pd_8h.md#a4d9e457e3c28050906b384bdf0a2f0d9)#define PDO\_PPS\_APDO\_CURR\_MASK 0x7f

81

[ 82](pd_8h.md#a7c1be180ef537b8104da38724e373e23)#define PDO\_PPS\_APDO\_MIN\_VOLT(mv) \

83 ((((mv) / 100) & PDO\_PPS\_APDO\_VOLT\_MASK) << PDO\_PPS\_APDO\_MIN\_VOLT\_SHIFT)

[ 84](pd_8h.md#aae9701858816813852e5bff5c814a118)#define PDO\_PPS\_APDO\_MAX\_VOLT(mv) \

85 ((((mv) / 100) & PDO\_PPS\_APDO\_VOLT\_MASK) << PDO\_PPS\_APDO\_MAX\_VOLT\_SHIFT)

[ 86](pd_8h.md#a0eaeee90e4fa809690563a92f829aef2)#define PDO\_PPS\_APDO\_MAX\_CURR(ma) \

87 ((((ma) / 50) & PDO\_PPS\_APDO\_CURR\_MASK) << PDO\_PPS\_APDO\_MAX\_CURR\_SHIFT)

88

[ 89](pd_8h.md#a48f8ae89ab76eae6f27585b389f2b33b)#define PDO\_PPS\_APDO(min\_mv, max\_mv, max\_ma) \

90 (PDO\_TYPE(PDO\_TYPE\_APDO) | PDO\_APDO\_TYPE(APDO\_TYPE\_PPS) | \

91 PDO\_PPS\_APDO\_MIN\_VOLT(min\_mv) | PDO\_PPS\_APDO\_MAX\_VOLT(max\_mv) | \

92 PDO\_PPS\_APDO\_MAX\_CURR(max\_ma))

93

94#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_USBC\_PD\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [usb-c](dir_0b553f055e45edcd5a3c9c76b7f4ae03.md)
- [pd.h](pd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
