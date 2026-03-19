---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/eth__nxp__enet_8h_source.html
original_path: doxygen/html/eth__nxp__enet_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eth\_nxp\_enet.h

[Go to the documentation of this file.](eth__nxp__enet_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_NXP\_ENET\_H\_\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_NXP\_ENET\_H\_\_

9

10/\*

11 \* This header is for NXP ENET driver development

12 \* and has definitions for internal implementations

13 \* not to be used by application

14 \*/

15

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/kernel.h](kernel_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

23/\*

24 \* Reasons for callback to a driver:

25 \*

26 \* Module reset: The ENET module was reset, perhaps because of power management

27 \* actions, and subdriver should reinitialize part of the module.

28 \* Interrupt: An interrupt of a type relevant to the subdriver occurred.

29 \* Interrupt enable: The driver's relevant interrupt was enabled in NVIC

30 \*/

[ 31](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47)enum [nxp\_enet\_callback\_reason](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47) {

[ 32](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47a019cb78bbe3a2ff74bd1ab1cbedb5ccd) [NXP\_ENET\_MODULE\_RESET](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47a019cb78bbe3a2ff74bd1ab1cbedb5ccd),

[ 33](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47ae355aed11d966069b2a77717fd1a46a9) [NXP\_ENET\_INTERRUPT](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47ae355aed11d966069b2a77717fd1a46a9),

[ 34](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47affa6c7124f8f9a0e3eda750287c05d18) [NXP\_ENET\_INTERRUPT\_ENABLED](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47affa6c7124f8f9a0e3eda750287c05d18),

35};

36

[ 37](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416)enum [nxp\_enet\_driver](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416) {

[ 38](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416af008b300d92db2371541464d6c577178) [NXP\_ENET\_MAC](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416af008b300d92db2371541464d6c577178),

[ 39](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416ac29234a2e347018f80a71078df4538a1) [NXP\_ENET\_MDIO](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416ac29234a2e347018f80a71078df4538a1),

[ 40](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416aa09c872026c5287cd6ae55847dcf4ebc) [NXP\_ENET\_PTP\_CLOCK](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416aa09c872026c5287cd6ae55847dcf4ebc),

41};

42

[ 43](eth__nxp__enet_8h.md#a5dd34e9d1bbe8e695995e647656cf564)extern void [nxp\_enet\_mdio\_callback](eth__nxp__enet_8h.md#a5dd34e9d1bbe8e695995e647656cf564)(const struct [device](structdevice.md) \*mdio\_dev,

44 enum [nxp\_enet\_callback\_reason](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47) event,

45 void \*data);

46

47#ifdef CONFIG\_PTP\_CLOCK\_NXP\_ENET

48extern void [nxp\_enet\_ptp\_clock\_callback](eth__nxp__enet_8h.md#ad11ef7c9660268acaccf3f39d662149a)(const struct [device](structdevice.md) \*dev,

49 enum [nxp\_enet\_callback\_reason](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47) event,

50 void \*data);

51#else

[ 52](eth__nxp__enet_8h.md#ad11ef7c9660268acaccf3f39d662149a)#define nxp\_enet\_ptp\_clock\_callback(...)

53#endif

54

55/\*

56 \* Internal implementation, inter-driver communication function

57 \*

58 \* dev: target device to call back

59 \* dev\_type: which driver to call back

60 \* event: reason/cause of callback

61 \* data: opaque data, will be interpreted based on reason and target driver

62 \*/

[ 63](eth__nxp__enet_8h.md#aa1876fb8edfa98cdb8f9f92abc48a572)extern void [nxp\_enet\_driver\_cb](eth__nxp__enet_8h.md#aa1876fb8edfa98cdb8f9f92abc48a572)(const struct [device](structdevice.md) \*dev,

64 enum [nxp\_enet\_driver](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416) dev\_type,

65 enum [nxp\_enet\_callback\_reason](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47) event,

66 void \*data);

67

68#ifdef \_\_cplusplus

69}

70#endif

71

72

73#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_NXP\_ENET\_H\_\_ \*/

[device.h](device_8h.md)

[nxp\_enet\_mdio\_callback](eth__nxp__enet_8h.md#a5dd34e9d1bbe8e695995e647656cf564)

void nxp\_enet\_mdio\_callback(const struct device \*mdio\_dev, enum nxp\_enet\_callback\_reason event, void \*data)

[nxp\_enet\_callback\_reason](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47)

nxp\_enet\_callback\_reason

**Definition** eth\_nxp\_enet.h:31

[NXP\_ENET\_MODULE\_RESET](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47a019cb78bbe3a2ff74bd1ab1cbedb5ccd)

@ NXP\_ENET\_MODULE\_RESET

**Definition** eth\_nxp\_enet.h:32

[NXP\_ENET\_INTERRUPT](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47ae355aed11d966069b2a77717fd1a46a9)

@ NXP\_ENET\_INTERRUPT

**Definition** eth\_nxp\_enet.h:33

[NXP\_ENET\_INTERRUPT\_ENABLED](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47affa6c7124f8f9a0e3eda750287c05d18)

@ NXP\_ENET\_INTERRUPT\_ENABLED

**Definition** eth\_nxp\_enet.h:34

[nxp\_enet\_driver\_cb](eth__nxp__enet_8h.md#aa1876fb8edfa98cdb8f9f92abc48a572)

void nxp\_enet\_driver\_cb(const struct device \*dev, enum nxp\_enet\_driver dev\_type, enum nxp\_enet\_callback\_reason event, void \*data)

[nxp\_enet\_ptp\_clock\_callback](eth__nxp__enet_8h.md#ad11ef7c9660268acaccf3f39d662149a)

#define nxp\_enet\_ptp\_clock\_callback(...)

**Definition** eth\_nxp\_enet.h:52

[nxp\_enet\_driver](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416)

nxp\_enet\_driver

**Definition** eth\_nxp\_enet.h:37

[NXP\_ENET\_PTP\_CLOCK](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416aa09c872026c5287cd6ae55847dcf4ebc)

@ NXP\_ENET\_PTP\_CLOCK

**Definition** eth\_nxp\_enet.h:40

[NXP\_ENET\_MDIO](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416ac29234a2e347018f80a71078df4538a1)

@ NXP\_ENET\_MDIO

**Definition** eth\_nxp\_enet.h:39

[NXP\_ENET\_MAC](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416af008b300d92db2371541464d6c577178)

@ NXP\_ENET\_MAC

**Definition** eth\_nxp\_enet.h:38

[kernel.h](kernel_8h.md)

Public kernel APIs.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ethernet](dir_e26e025f1b2d5c43527f6232564fe44e.md)
- [eth\_nxp\_enet.h](eth__nxp__enet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
