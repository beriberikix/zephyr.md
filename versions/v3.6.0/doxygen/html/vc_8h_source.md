---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/vc_8h_source.html
original_path: doxygen/html/vc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vc.h

[Go to the documentation of this file.](vc_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_VC\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_VC\_H\_

9

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

22#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

23#include <[stdbool.h](stdbool_8h.md)>

24

25#include <[zephyr/drivers/pcie/pcie.h](drivers_2pcie_2pcie_8h.md)>

26

27/\*

28 \* 1 default VC + 7 extended VCs

29 \*/

[ 30](group__pcie__vc__host__interface.md#ga0567fabc02828372f4e901bb193c9b89)#define PCIE\_VC\_MAX\_COUNT 8U

31

[ 32](group__pcie__vc__host__interface.md#gae1ec2ec11736ed97c6e41a2d8c7f4a39)#define PCIE\_VC\_SET\_TC0 BIT(0)

[ 33](group__pcie__vc__host__interface.md#gab4d53cac004ac7b6258fbd387fc90051)#define PCIE\_VC\_SET\_TC1 BIT(1)

[ 34](group__pcie__vc__host__interface.md#ga3d0311d99240527d86e8f8452f405736)#define PCIE\_VC\_SET\_TC2 BIT(2)

[ 35](group__pcie__vc__host__interface.md#ga3122990fd5879e076346efdc706b640e)#define PCIE\_VC\_SET\_TC3 BIT(3)

[ 36](group__pcie__vc__host__interface.md#ga2259546ee27ce43dfb15ea69bdb66a7c)#define PCIE\_VC\_SET\_TC4 BIT(4)

[ 37](group__pcie__vc__host__interface.md#ga9a796b9570585c60c70fb641e0a5a733)#define PCIE\_VC\_SET\_TC5 BIT(5)

[ 38](group__pcie__vc__host__interface.md#gaf8ff3086a4a5003f303f7b17e2319c09)#define PCIE\_VC\_SET\_TC6 BIT(6)

[ 39](group__pcie__vc__host__interface.md#gacbd9b1877530539d1a14a35d35744634)#define PCIE\_VC\_SET\_TC7 BIT(7)

40

[ 41](structpcie__vctc__map.md)struct [pcie\_vctc\_map](structpcie__vctc__map.md) {

42 /\*

43 \* Map the TCs for each VC by setting bits relevantly

44 \* Note: one bit cannot be set more than once among the VCs

45 \*/

[ 46](structpcie__vctc__map.md#a93955e5b5e4ef26a81d363e8f10806fc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [vc\_tc](structpcie__vctc__map.md#a93955e5b5e4ef26a81d363e8f10806fc)[[PCIE\_VC\_MAX\_COUNT](group__pcie__vc__host__interface.md#ga0567fabc02828372f4e901bb193c9b89)];

47 /\*

48 \* Number of VCs being addressed

49 \*/

[ 50](structpcie__vctc__map.md#aa70f7e0a4f2eadcf652e8858b2fc0304) int [vc\_count](structpcie__vctc__map.md#aa70f7e0a4f2eadcf652e8858b2fc0304);

51};

52

[ 62](group__pcie__vc__host__interface.md#ga179628024fc9d651d1027833377ee9d2)int [pcie\_vc\_enable](group__pcie__vc__host__interface.md#ga179628024fc9d651d1027833377ee9d2)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf);

63

[ 69](group__pcie__vc__host__interface.md#ga89c684f7ff5e82da86df27d061a8fbd7)int [pcie\_vc\_disable](group__pcie__vc__host__interface.md#ga89c684f7ff5e82da86df27d061a8fbd7)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf);

70

[ 84](group__pcie__vc__host__interface.md#gafd4429e8c14821c685c4103f34b340c8)int [pcie\_vc\_map\_tc](group__pcie__vc__host__interface.md#gafd4429e8c14821c685c4103f34b340c8)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, struct [pcie\_vctc\_map](structpcie__vctc__map.md) \*map);

85

86

87#ifdef \_\_cplusplus

88}

89#endif

90

94

95#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_VC\_H\_ \*/

[pcie.h](drivers_2pcie_2pcie_8h.md)

[pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb)

uint32\_t pcie\_bdf\_t

A unique PCI(e) endpoint (bus, device, function).

**Definition** pcie.h:37

[PCIE\_VC\_MAX\_COUNT](group__pcie__vc__host__interface.md#ga0567fabc02828372f4e901bb193c9b89)

#define PCIE\_VC\_MAX\_COUNT

**Definition** vc.h:30

[pcie\_vc\_enable](group__pcie__vc__host__interface.md#ga179628024fc9d651d1027833377ee9d2)

int pcie\_vc\_enable(pcie\_bdf\_t bdf)

Enable PCIe Virtual Channel handling.

[pcie\_vc\_disable](group__pcie__vc__host__interface.md#ga89c684f7ff5e82da86df27d061a8fbd7)

int pcie\_vc\_disable(pcie\_bdf\_t bdf)

Disable PCIe Virtual Channel handling.

[pcie\_vc\_map\_tc](group__pcie__vc__host__interface.md#gafd4429e8c14821c685c4103f34b340c8)

int pcie\_vc\_map\_tc(pcie\_bdf\_t bdf, struct pcie\_vctc\_map \*map)

Map PCIe TC/VC.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[pcie\_vctc\_map](structpcie__vctc__map.md)

**Definition** vc.h:41

[pcie\_vctc\_map::vc\_tc](structpcie__vctc__map.md#a93955e5b5e4ef26a81d363e8f10806fc)

uint8\_t vc\_tc[8U]

**Definition** vc.h:46

[pcie\_vctc\_map::vc\_count](structpcie__vctc__map.md#aa70f7e0a4f2eadcf652e8858b2fc0304)

int vc\_count

**Definition** vc.h:50

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [vc.h](vc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
