---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/eth__nxp__enet_8h_source.html
original_path: doxygen/html/eth__nxp__enet_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

[ 43](structnxp__enet__ptp__data.md)struct [nxp\_enet\_ptp\_data](structnxp__enet__ptp__data.md) {

[ 44](structnxp__enet__ptp__data.md#a236c0327117d80bcd536282240bfc039) struct [k\_sem](structk__sem.md) [ptp\_ts\_sem](structnxp__enet__ptp__data.md#a236c0327117d80bcd536282240bfc039);

[ 45](structnxp__enet__ptp__data.md#a96f125506413850d1f9099180f46be62) struct [k\_mutex](structk__mutex.md) \*[ptp\_mutex](structnxp__enet__ptp__data.md#a96f125506413850d1f9099180f46be62); /\* created in PTP driver \*/

[ 46](structnxp__enet__ptp__data.md#aebd5911593605030fad4a39d0f85dc8a) void \*[enet](structnxp__enet__ptp__data.md#aebd5911593605030fad4a39d0f85dc8a); /\* enet\_handle poiniter used by PTP driver \*/

47};

48

[ 49](eth__nxp__enet_8h.md#a5dd34e9d1bbe8e695995e647656cf564)extern void [nxp\_enet\_mdio\_callback](eth__nxp__enet_8h.md#a5dd34e9d1bbe8e695995e647656cf564)(const struct [device](structdevice.md) \*mdio\_dev,

50 enum [nxp\_enet\_callback\_reason](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47) event,

51 void \*data);

52

53#ifdef CONFIG\_PTP\_CLOCK\_NXP\_ENET

54extern void [nxp\_enet\_ptp\_clock\_callback](eth__nxp__enet_8h.md#ad11ef7c9660268acaccf3f39d662149a)(const struct [device](structdevice.md) \*dev,

55 enum [nxp\_enet\_callback\_reason](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47) event,

56 void \*data);

57#else

[ 58](eth__nxp__enet_8h.md#ad11ef7c9660268acaccf3f39d662149a)#define nxp\_enet\_ptp\_clock\_callback(...)

59#endif

60

61/\*

62 \* Internal implementation, inter-driver communication function

63 \*

64 \* dev: target device to call back

65 \* dev\_type: which driver to call back

66 \* event: reason/cause of callback

67 \* data: opaque data, will be interpreted based on reason and target driver

68 \*/

[ 69](eth__nxp__enet_8h.md#aa1876fb8edfa98cdb8f9f92abc48a572)extern void [nxp\_enet\_driver\_cb](eth__nxp__enet_8h.md#aa1876fb8edfa98cdb8f9f92abc48a572)(const struct [device](structdevice.md) \*dev,

70 enum [nxp\_enet\_driver](eth__nxp__enet_8h.md#ae3c6272946ff0e510271158ff1ab4416) dev\_type,

71 enum [nxp\_enet\_callback\_reason](eth__nxp__enet_8h.md#a91a8c6d4a482c50577ed686748f84a47) event,

72 void \*data);

73

74#ifdef \_\_cplusplus

75}

76#endif

77

78

79#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_NXP\_ENET\_H\_\_ \*/

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

**Definition** eth\_nxp\_enet.h:58

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

**Definition** device.h:510

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3070

[k\_sem](structk__sem.md)

Semaphore structure.

**Definition** kernel.h:3275

[nxp\_enet\_ptp\_data](structnxp__enet__ptp__data.md)

**Definition** eth\_nxp\_enet.h:43

[nxp\_enet\_ptp\_data::ptp\_ts\_sem](structnxp__enet__ptp__data.md#a236c0327117d80bcd536282240bfc039)

struct k\_sem ptp\_ts\_sem

**Definition** eth\_nxp\_enet.h:44

[nxp\_enet\_ptp\_data::ptp\_mutex](structnxp__enet__ptp__data.md#a96f125506413850d1f9099180f46be62)

struct k\_mutex \* ptp\_mutex

**Definition** eth\_nxp\_enet.h:45

[nxp\_enet\_ptp\_data::enet](structnxp__enet__ptp__data.md#aebd5911593605030fad4a39d0f85dc8a)

void \* enet

**Definition** eth\_nxp\_enet.h:46

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ethernet](dir_e26e025f1b2d5c43527f6232564fe44e.md)
- [eth\_nxp\_enet.h](eth__nxp__enet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
