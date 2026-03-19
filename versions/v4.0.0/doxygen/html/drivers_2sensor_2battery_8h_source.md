---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2sensor_2battery_8h_source.html
original_path: doxygen/html/drivers_2sensor_2battery_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

battery.h

[Go to the documentation of this file.](drivers_2sensor_2battery_8h.md)

1/\*

2 \* Copyright 2024 Embeint Inc

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_BATTERY\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_BATTERY\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[errno.h](errno_8h.md)>

12

13#include <[zephyr/devicetree.h](devicetree_8h.md)>

14#include <[zephyr/math/interpolation.h](interpolation_8h.md)>

15#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

26

27/\* Battery chemistry enumeration.

28 \* Value names must match those from dts/bindings/battery.yaml

29 \*/

[ 30](group__battery__apis.md#gaf7ee6b6e85da9f31231cac577428de01)enum [battery\_chemistry](group__battery__apis.md#gaf7ee6b6e85da9f31231cac577428de01) {

[ 31](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a52bae762c2ef4ca140c1e7f89440b007) [BATTERY\_CHEMISTRY\_UNKNOWN](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a52bae762c2ef4ca140c1e7f89440b007) = 0,

[ 32](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a00f07b177e6246e139b469386064698f) [BATTERY\_CHEMISTRY\_NICKEL\_CADMIUM](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a00f07b177e6246e139b469386064698f),

[ 33](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a377834c71930068b6a822d4afd2112f4) [BATTERY\_CHEMISTRY\_NICKEL\_METAL\_HYDRIDE](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a377834c71930068b6a822d4afd2112f4),

[ 34](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a450162d694da85864af48712cb05badd) [BATTERY\_CHEMISTRY\_LITHIUM\_ION](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a450162d694da85864af48712cb05badd),

[ 35](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01ab21f5e769426047924d83e5301b8a19f) [BATTERY\_CHEMISTRY\_LITHIUM\_ION\_POLYMER](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01ab21f5e769426047924d83e5301b8a19f),

[ 36](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a951b3bea1c503ce6f1d78e8cc1ed9e37) [BATTERY\_CHEMISTRY\_LITHIUM\_ION\_IRON\_PHOSPHATE](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a951b3bea1c503ce6f1d78e8cc1ed9e37),

[ 37](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a30cd5d02bb416248b9380ab953836e96) [BATTERY\_CHEMISTRY\_LITHIUM\_ION\_MANGANESE\_OXIDE](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a30cd5d02bb416248b9380ab953836e96),

38};

39

40/\* Length of open circuit voltage table \*/

[ 41](group__battery__apis.md#ga02de0e4f76b8e5804b82cd397c13ef86)#define BATTERY\_OCV\_TABLE\_LEN 11

42

[ 48](group__battery__apis.md#gae2c365581f7c8c71e1ec31b223545711)#define BATTERY\_CHEMISTRY\_DT\_GET(node\_id) \

49 UTIL\_CAT(BATTERY\_CHEMISTRY\_, DT\_STRING\_UPPER\_TOKEN\_OR(node\_id, device\_chemistry, UNKNOWN))

50

[ 57](group__battery__apis.md#ga833bf8bf88136fd277a69fb41ad0fb7f)#define BATTERY\_OCV\_TABLE\_DT\_GET(node\_id, table) \

58 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, table), \

59 ({DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, table, DT\_PROP\_BY\_IDX, (,))}), ({-1}))

60

[ 69](group__battery__apis.md#gaea81fb0c63b85654005b6f65521c3345)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [battery\_soc\_lookup](group__battery__apis.md#gaea81fb0c63b85654005b6f65521c3345)(const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ocv\_table[[BATTERY\_OCV\_TABLE\_LEN](group__battery__apis.md#ga02de0e4f76b8e5804b82cd397c13ef86)],

70 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) voltage\_uv)

71{

72 static const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) soc\_axis[[BATTERY\_OCV\_TABLE\_LEN](group__battery__apis.md#ga02de0e4f76b8e5804b82cd397c13ef86)] = {

73 0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};

74

75 /\* Convert voltage to SoC \*/

76 return [linear\_interpolate](interpolation_8h.md#a8abbb1799796222b39a051819bd19a2a)(ocv\_table, soc\_axis, [BATTERY\_OCV\_TABLE\_LEN](group__battery__apis.md#ga02de0e4f76b8e5804b82cd397c13ef86), voltage\_uv);

77}

78

82

83#ifdef \_\_cplusplus

84}

85#endif

86

87#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_BATTERY\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[errno.h](errno_8h.md)

System error numbers.

[BATTERY\_OCV\_TABLE\_LEN](group__battery__apis.md#ga02de0e4f76b8e5804b82cd397c13ef86)

#define BATTERY\_OCV\_TABLE\_LEN

**Definition** battery.h:41

[battery\_soc\_lookup](group__battery__apis.md#gaea81fb0c63b85654005b6f65521c3345)

static int32\_t battery\_soc\_lookup(const int32\_t ocv\_table[11], uint32\_t voltage\_uv)

Convert an OCV table and battery voltage to a charge percentage.

**Definition** battery.h:69

[battery\_chemistry](group__battery__apis.md#gaf7ee6b6e85da9f31231cac577428de01)

battery\_chemistry

**Definition** battery.h:30

[BATTERY\_CHEMISTRY\_NICKEL\_CADMIUM](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a00f07b177e6246e139b469386064698f)

@ BATTERY\_CHEMISTRY\_NICKEL\_CADMIUM

**Definition** battery.h:32

[BATTERY\_CHEMISTRY\_LITHIUM\_ION\_MANGANESE\_OXIDE](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a30cd5d02bb416248b9380ab953836e96)

@ BATTERY\_CHEMISTRY\_LITHIUM\_ION\_MANGANESE\_OXIDE

**Definition** battery.h:37

[BATTERY\_CHEMISTRY\_NICKEL\_METAL\_HYDRIDE](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a377834c71930068b6a822d4afd2112f4)

@ BATTERY\_CHEMISTRY\_NICKEL\_METAL\_HYDRIDE

**Definition** battery.h:33

[BATTERY\_CHEMISTRY\_LITHIUM\_ION](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a450162d694da85864af48712cb05badd)

@ BATTERY\_CHEMISTRY\_LITHIUM\_ION

**Definition** battery.h:34

[BATTERY\_CHEMISTRY\_UNKNOWN](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a52bae762c2ef4ca140c1e7f89440b007)

@ BATTERY\_CHEMISTRY\_UNKNOWN

**Definition** battery.h:31

[BATTERY\_CHEMISTRY\_LITHIUM\_ION\_IRON\_PHOSPHATE](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a951b3bea1c503ce6f1d78e8cc1ed9e37)

@ BATTERY\_CHEMISTRY\_LITHIUM\_ION\_IRON\_PHOSPHATE

**Definition** battery.h:36

[BATTERY\_CHEMISTRY\_LITHIUM\_ION\_POLYMER](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01ab21f5e769426047924d83e5301b8a19f)

@ BATTERY\_CHEMISTRY\_LITHIUM\_ION\_POLYMER

**Definition** battery.h:35

[interpolation.h](interpolation_8h.md)

Provide linear interpolation functions.

[linear\_interpolate](interpolation_8h.md#a8abbb1799796222b39a051819bd19a2a)

static int32\_t linear\_interpolate(const int32\_t \*x\_axis, const int32\_t \*y\_axis, uint8\_t len, int32\_t x)

Perform a linear interpolation across an arbitrary curve.

**Definition** interpolation.h:37

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [battery.h](drivers_2sensor_2battery_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
