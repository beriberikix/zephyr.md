---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/qdec__nxp__s32_8h_source.html
original_path: doxygen/html/qdec__nxp__s32_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

qdec\_nxp\_s32.h

[Go to the documentation of this file.](qdec__nxp__s32_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\* Logic Trigger Numbers. See Trgmux\_Ip\_Init\_PBcfg.h \*/

[ 8](qdec__nxp__s32_8h.md#a5f90d651c87f9d2967cbeb6ed14107d4)#define TRGMUX\_LOGIC\_GROUP\_0\_TRIGGER\_0 (0) /\* Logic Trigger 0 \*/

[ 9](qdec__nxp__s32_8h.md#ad58ca2f638326d20fa7d6e2f274aa781)#define TRGMUX\_LOGIC\_GROUP\_0\_TRIGGER\_1 (1) /\* Logic Trigger 1 \*/

[ 10](qdec__nxp__s32_8h.md#a5296f2a7a199ced206847e18829aa4ee)#define TRGMUX\_LOGIC\_GROUP\_1\_TRIGGER\_0 (2) /\* Logic Trigger 2 \*/

[ 11](qdec__nxp__s32_8h.md#a1f3cdaf240b7aed64a20631eff68f01b)#define TRGMUX\_LOGIC\_GROUP\_1\_TRIGGER\_1 (3) /\* Logic Trigger 3 \*/

12

13/\*-----------------------------------------------

14 \* TRGMUX HARDWARE TRIGGER INPUT

15 \* See Trgmux\_Ip\_Cfg\_Defines.h

16 \*-----------------------------------------------

17 \*/

[ 18](qdec__nxp__s32_8h.md#a61c157ef6f63440cccfdc5c5a85fd310)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN0 (60)

[ 19](qdec__nxp__s32_8h.md#ab6691aa9e2dd85d252c30c7992c0cc2d)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN1 (61)

[ 20](qdec__nxp__s32_8h.md#a703797c0a4d2b3f2f19ae67a9170c1db)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN2 (62)

[ 21](qdec__nxp__s32_8h.md#a32e367eaa554879dd6e3ddc28a524b25)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN3 (63)

[ 22](qdec__nxp__s32_8h.md#ad6aaa8c5e9d917871085993d82774d4e)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN4 (64)

[ 23](qdec__nxp__s32_8h.md#ac8531ab44c60fd98dd55774e6b54033d)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN5 (65)

[ 24](qdec__nxp__s32_8h.md#af8cd9167bfded6c453f75ddc0a5b38c8)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN6 (66)

[ 25](qdec__nxp__s32_8h.md#ad80f66c40a4b87ef0a1ca4790969f9c2)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN7 (67)

[ 26](qdec__nxp__s32_8h.md#a6ed1b02c78a353bb1e92a45190ad65b5)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN8 (68)

[ 27](qdec__nxp__s32_8h.md#ad42232cddb9dc1c2f38e1b9908fcebf4)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN9 (69)

[ 28](qdec__nxp__s32_8h.md#a9b6afac0a7eafb1c04dbfb385c6d18f1)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN10 (70)

[ 29](qdec__nxp__s32_8h.md#aa91e26818dd86f102a46a18287fde7e8)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN11 (71)

[ 30](qdec__nxp__s32_8h.md#a914e801b68356386d723ff0af1216b5d)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN12 (72)

[ 31](qdec__nxp__s32_8h.md#ad51c25c87d50d86c12c8f93c8c88460d)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN13 (73)

[ 32](qdec__nxp__s32_8h.md#a14de227e51575ec405f850632f33ace7)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN14 (74)

[ 33](qdec__nxp__s32_8h.md#a6a45b83389117d94a7f653a15457289a)#define TRGMUX\_IP\_INPUT\_SIUL2\_IN15 (75)

34

[ 35](qdec__nxp__s32_8h.md#a0482ac4e3ab453e2e0882551f32af165)#define TRGMUX\_IP\_INPUT\_LCU1\_LC0\_OUT\_I0 (105)

[ 36](qdec__nxp__s32_8h.md#a85cafa1adddad2741d57aa9a0038522f)#define TRGMUX\_IP\_INPUT\_LCU1\_LC0\_OUT\_I1 (106)

[ 37](qdec__nxp__s32_8h.md#a535b5e20ee7d59948612e7b4145af06a)#define TRGMUX\_IP\_INPUT\_LCU1\_LC0\_OUT\_I2 (107)

[ 38](qdec__nxp__s32_8h.md#ae87282218e47f09eeaa8e89d49f68f8e)#define TRGMUX\_IP\_INPUT\_LCU1\_LC0\_OUT\_I3 (108)

39

40/\*-----------------------------------------------

41 \* TRGMUX HARDWARE TRIGGER OUTPUT

42 \* See Trgmux\_Ip\_Cfg\_Defines.h

43 \*-----------------------------------------------

44 \*/

[ 45](qdec__nxp__s32_8h.md#a348fb8f222fc47542785a9d9b264f2ca)#define TRGMUX\_IP\_OUTPUT\_LCU1\_0\_INP\_I0 (144)

[ 46](qdec__nxp__s32_8h.md#a6a7b3e2d83c1daaf28863a8bee4f93cc)#define TRGMUX\_IP\_OUTPUT\_LCU1\_0\_INP\_I1 (145)

[ 47](qdec__nxp__s32_8h.md#ab7c7af569060a90b6918dc4779f222b9)#define TRGMUX\_IP\_OUTPUT\_LCU1\_0\_INP\_I2 (146)

[ 48](qdec__nxp__s32_8h.md#a36adf3458bdfd54f696e5e114dd75a21)#define TRGMUX\_IP\_OUTPUT\_LCU1\_0\_INP\_I3 (147)

49

[ 50](qdec__nxp__s32_8h.md#a2120ba38a6ca432e117e350621b30b21)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH1\_4\_IPP\_IND\_CH1 (32)

[ 51](qdec__nxp__s32_8h.md#abcef1065db27c4d5870661e64faf7fd2)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH1\_4\_IPP\_IND\_CH2 (33)

[ 52](qdec__nxp__s32_8h.md#a3c997f6ddf11c7a69ce43855bad410f4)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH1\_4\_IPP\_IND\_CH3 (34)

[ 53](qdec__nxp__s32_8h.md#ad9a1b43a14a9f22c0c36a518813a7530)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH1\_4\_IPP\_IND\_CH4 (35)

[ 54](qdec__nxp__s32_8h.md#a3c1c025a09c31c81f29c85ac89e7676d)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH5\_9\_IPP\_IND\_CH5 (36)

[ 55](qdec__nxp__s32_8h.md#ab9bfc47c3cb99c8ba5b4231b8ae6adec)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH5\_9\_IPP\_IND\_CH6 (37)

[ 56](qdec__nxp__s32_8h.md#a8672923dcb7c73d45a46e3fc8042a819)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH5\_9\_IPP\_IND\_CH7 (38)

[ 57](qdec__nxp__s32_8h.md#a5c4417fc989cc7cfd341d1b271b08ef6)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH5\_9\_IPP\_IND\_CH9 (39)

[ 58](qdec__nxp__s32_8h.md#a6479a7d5293501ec23252187bf3c53a7)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH10\_13\_IPP\_IND\_CH10 (40)

[ 59](qdec__nxp__s32_8h.md#a820b8f9c7d7e87b8e8bf69f8eb22eb9d)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH10\_13\_IPP\_IND\_CH11 (41)

[ 60](qdec__nxp__s32_8h.md#acd8405722de5780ee34fd070847e74c7)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH10\_13\_IPP\_IND\_CH12 (42)

[ 61](qdec__nxp__s32_8h.md#afd6354704670c0245ab1ef5811f181a4)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH10\_13\_IPP\_IND\_CH13 (43)

[ 62](qdec__nxp__s32_8h.md#a1f274984088ec4260544e415ef49fb8f)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH14\_15\_IPP\_IND\_CH14 (44)

[ 63](qdec__nxp__s32_8h.md#a228ce57b6b3f265f4e265f07f49111f5)#define TRGMUX\_IP\_OUTPUT\_EMIOS0\_CH14\_15\_IPP\_IND\_CH15 (45)

64

65/\*-----------------------------------------------

66 \* LCU SOURCE MUX SELECT

67 \* See Lcu\_Ip\_Cfg\_Defines.h

68 \*-----------------------------------------------

69 \*/

[ 70](qdec__nxp__s32_8h.md#a1c95e6e44fcc063050abdfb12ff4a53d)#define LCU\_IP\_MUX\_SEL\_LOGIC\_0 (0)

[ 71](qdec__nxp__s32_8h.md#a9c8968bc623e89af46b987b5a266cd7a)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_0 (1)

[ 72](qdec__nxp__s32_8h.md#a1fcbbd535dde1ee1180bbdb1939ad6fb)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_1 (2)

[ 73](qdec__nxp__s32_8h.md#a72bc02b3e8caeb349c8d083e9b355bbb)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_2 (3)

[ 74](qdec__nxp__s32_8h.md#ade15633475996e248b63c8c7bc0dd2e1)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_3 (4)

[ 75](qdec__nxp__s32_8h.md#a0749ee1d0b387050d93d4a5fd5ddbac3)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_4 (5)

[ 76](qdec__nxp__s32_8h.md#ab4150fda8780a5dfadb4e10ed2d9a6ef)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_5 (6)

[ 77](qdec__nxp__s32_8h.md#a01649444e8d4869869adb0a1497d5891)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_6 (7)

[ 78](qdec__nxp__s32_8h.md#add4bb12283b964051aadc44e91c64b4a)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_7 (8)

[ 79](qdec__nxp__s32_8h.md#adb1518b38831f5d630baa05e4318ac85)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_8 (9)

[ 80](qdec__nxp__s32_8h.md#adec9096085fb58765a665d93df7f48c8)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_9 (10)

[ 81](qdec__nxp__s32_8h.md#a6150e58658fb96c507b7f837b7e80cd2)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_10 (11)

[ 82](qdec__nxp__s32_8h.md#a5421da1bd5dda8549da581c84bbd264e)#define LCU\_IP\_MUX\_SEL\_LU\_IN\_11 (12)

[ 83](qdec__nxp__s32_8h.md#af717610f772ecd118bad267f1e7ef53a)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_0 (13)

[ 84](qdec__nxp__s32_8h.md#a806ae23bdcd235b5a8a4998dbf0645fc)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_1 (14)

[ 85](qdec__nxp__s32_8h.md#aa7ddcb1426021d8d1cc885cf8887d771)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_2 (15)

[ 86](qdec__nxp__s32_8h.md#accf4f6fa723e15466774dd08d119d530)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_3 (16)

[ 87](qdec__nxp__s32_8h.md#af248aa0bb1abd496568018bc2f831304)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_4 (17)

[ 88](qdec__nxp__s32_8h.md#a38ea3916f289680c429509fa3689e7b2)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_5 (18)

[ 89](qdec__nxp__s32_8h.md#a7d0cbe256823d47406ac5f8b9791373c)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_6 (19)

[ 90](qdec__nxp__s32_8h.md#ac24584f60b6cdb639365b0ec29c76911)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_7 (20)

[ 91](qdec__nxp__s32_8h.md#af68a610920eb13011d0ca82639938f6f)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_8 (21)

[ 92](qdec__nxp__s32_8h.md#a6f8c4425dae4f35f7ce1230cb6f6ce35)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_9 (22)

[ 93](qdec__nxp__s32_8h.md#a09da2f54cacb280bcef7bbcce0efa397)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_10 (23)

[ 94](qdec__nxp__s32_8h.md#ac5d851693a2174702cf4edf6da6d4d24)#define LCU\_IP\_MUX\_SEL\_LU\_OUT\_11 (24)

95

[ 96](qdec__nxp__s32_8h.md#a1d7a73016cff2d6bf94b31e45037c5a0)#define LCU\_IP\_IN\_0 (0)

[ 97](qdec__nxp__s32_8h.md#afd1723996331f68b68268a843c50ee0c)#define LCU\_IP\_IN\_1 (1)

[ 98](qdec__nxp__s32_8h.md#a6a2dc4f41c360fd0ad995a2191c8b40e)#define LCU\_IP\_IN\_2 (2)

[ 99](qdec__nxp__s32_8h.md#ab7e7a15a25ee912e767cd0867eaec01d)#define LCU\_IP\_IN\_3 (3)

[ 100](qdec__nxp__s32_8h.md#aaea5ffc915bd68b1e2ed8c15e428d351)#define LCU\_IP\_IN\_4 (4)

[ 101](qdec__nxp__s32_8h.md#aa6f3c25854e873cd3cd909772b913b8c)#define LCU\_IP\_IN\_5 (5)

[ 102](qdec__nxp__s32_8h.md#a545cda428781141271bb9ae2fbe9ca86)#define LCU\_IP\_IN\_6 (6)

[ 103](qdec__nxp__s32_8h.md#ab60fbbce8800af816f90f86b2cf6edc2)#define LCU\_IP\_IN\_7 (7)

[ 104](qdec__nxp__s32_8h.md#a789de245fe9fac9348075d71fac666e0)#define LCU\_IP\_IN\_8 (8)

[ 105](qdec__nxp__s32_8h.md#aa6051a5f0ad64dd49f7962b4712e9611)#define LCU\_IP\_IN\_9 (9)

[ 106](qdec__nxp__s32_8h.md#ad242f6e9c4c7d6b3ddd879f14e8efacd)#define LCU\_IP\_IN\_10 (10)

[ 107](qdec__nxp__s32_8h.md#a74ccacec42db8439d36f7749e45b2bbe)#define LCU\_IP\_IN\_11 (11)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [qdec\_nxp\_s32.h](qdec__nxp__s32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
