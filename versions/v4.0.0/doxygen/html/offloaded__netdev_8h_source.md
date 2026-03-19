---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/offloaded__netdev_8h_source.html
original_path: doxygen/html/offloaded__netdev_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

offloaded\_netdev.h

[Go to the documentation of this file.](offloaded__netdev_8h.md)

1

6

7/\*

8 \* Copyright (c) 2022 Nordic Semiconductor ASA

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_OFFLOADED\_NETDEV\_H\_

14#define ZEPHYR\_INCLUDE\_OFFLOADED\_NETDEV\_H\_

15

16#include <[zephyr/kernel.h](kernel_8h.md)>

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18#include <[stdbool.h](stdbool_8h.md)>

19#include <[zephyr/net/net\_if.h](net__if_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

33

[ 35](group__offloaded__netdev.md#gac1980977f6da3ace33ede7949d43f81f)enum [offloaded\_net\_if\_types](group__offloaded__netdev.md#gac1980977f6da3ace33ede7949d43f81f) {

[ 37](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa46a984d855ea5731207274149b12de1d) [L2\_OFFLOADED\_NET\_IF\_TYPE\_UNKNOWN](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa46a984d855ea5731207274149b12de1d),

38

[ 40](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa532f2d2684118c1c7e78064b5bd7920a) [L2\_OFFLOADED\_NET\_IF\_TYPE\_ETHERNET](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa532f2d2684118c1c7e78064b5bd7920a),

41

[ 43](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa85328162750725aae17aa0d84a4dab21) [L2\_OFFLOADED\_NET\_IF\_TYPE\_MODEM](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa85328162750725aae17aa0d84a4dab21),

44

[ 46](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24) [L2\_OFFLOADED\_NET\_IF\_TYPE\_WIFI](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24),

47};

48

[ 53](structoffloaded__if__api.md)struct [offloaded\_if\_api](structoffloaded__if__api.md) {

[ 58](structoffloaded__if__api.md#a24cc2bd70d18075731be617955e3e1a8) struct net\_if\_api [iface\_api](structoffloaded__if__api.md#a24cc2bd70d18075731be617955e3e1a8);

59

[ 61](structoffloaded__if__api.md#aadf471a8e3ae22f3294df1cab090a7a3) int (\*[enable](structoffloaded__if__api.md#aadf471a8e3ae22f3294df1cab090a7a3))(const struct [net\_if](structnet__if.md) \*iface, bool [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

62

64 enum [offloaded\_net\_if\_types](group__offloaded__netdev.md#gac1980977f6da3ace33ede7949d43f81f) (\*[get\_type](structoffloaded__if__api.md#a5ae87a9ed455f62958e1f2fa8cb715e7))(void);

65};

66

67/\* Ensure offloaded\_if\_api is compatible with net\_if\_api \*/

68BUILD\_ASSERT(offsetof(struct [offloaded\_if\_api](structoffloaded__if__api.md), iface\_api) == 0);

69

[ 77](group__offloaded__netdev.md#gad1076eacf1b1e82f70759f9b54937ced)static inline bool [net\_off\_is\_wifi\_offloaded](group__offloaded__netdev.md#gad1076eacf1b1e82f70759f9b54937ced)(struct [net\_if](structnet__if.md) \*iface)

78{

79 const struct [offloaded\_if\_api](structoffloaded__if__api.md) \*api = (const struct [offloaded\_if\_api](structoffloaded__if__api.md) \*)

80 [net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)(iface)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

81

82 return api->[get\_type](structoffloaded__if__api.md#a5ae87a9ed455f62958e1f2fa8cb715e7) && api->[get\_type](structoffloaded__if__api.md#a5ae87a9ed455f62958e1f2fa8cb715e7)() == [L2\_OFFLOADED\_NET\_IF\_TYPE\_WIFI](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24);

83}

84

88

89#ifdef \_\_cplusplus

90}

91#endif

92

93#endif /\* ZEPHYR\_INCLUDE\_OFFLOADED\_NETDEV\_H\_ \*/

[net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)

static const struct device \* net\_if\_get\_device(struct net\_if \*iface)

Get an network interface's device.

**Definition** net\_if.h:944

[offloaded\_net\_if\_types](group__offloaded__netdev.md#gac1980977f6da3ace33ede7949d43f81f)

offloaded\_net\_if\_types

Types of offloaded netdev L2.

**Definition** offloaded\_netdev.h:35

[net\_off\_is\_wifi\_offloaded](group__offloaded__netdev.md#gad1076eacf1b1e82f70759f9b54937ced)

static bool net\_off\_is\_wifi\_offloaded(struct net\_if \*iface)

Check if the offloaded network interface supports Wi-Fi.

**Definition** offloaded\_netdev.h:77

[L2\_OFFLOADED\_NET\_IF\_TYPE\_UNKNOWN](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa46a984d855ea5731207274149b12de1d)

@ L2\_OFFLOADED\_NET\_IF\_TYPE\_UNKNOWN

Unknown, device hasn't register a type.

**Definition** offloaded\_netdev.h:37

[L2\_OFFLOADED\_NET\_IF\_TYPE\_ETHERNET](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa532f2d2684118c1c7e78064b5bd7920a)

@ L2\_OFFLOADED\_NET\_IF\_TYPE\_ETHERNET

Ethernet devices.

**Definition** offloaded\_netdev.h:40

[L2\_OFFLOADED\_NET\_IF\_TYPE\_MODEM](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fa85328162750725aae17aa0d84a4dab21)

@ L2\_OFFLOADED\_NET\_IF\_TYPE\_MODEM

Modem.

**Definition** offloaded\_netdev.h:43

[L2\_OFFLOADED\_NET\_IF\_TYPE\_WIFI](group__offloaded__netdev.md#ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24)

@ L2\_OFFLOADED\_NET\_IF\_TYPE\_WIFI

IEEE 802.11 Wi-Fi.

**Definition** offloaded\_netdev.h:46

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[stdbool.h](stdbool_8h.md)

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

[offloaded\_if\_api](structoffloaded__if__api.md)

Extended net\_if\_api for offloaded ifaces/network devices, allowing handling of admin up/down state ch...

**Definition** offloaded\_netdev.h:53

[offloaded\_if\_api::iface\_api](structoffloaded__if__api.md#a24cc2bd70d18075731be617955e3e1a8)

struct net\_if\_api iface\_api

The net\_if\_api must be placed in first position in this struct so that we are compatible with network...

**Definition** offloaded\_netdev.h:58

[offloaded\_if\_api::get\_type](structoffloaded__if__api.md#a5ae87a9ed455f62958e1f2fa8cb715e7)

enum offloaded\_net\_if\_types(\* get\_type)(void)

Types of offloaded net device.

**Definition** offloaded\_netdev.h:64

[offloaded\_if\_api::enable](structoffloaded__if__api.md#aadf471a8e3ae22f3294df1cab090a7a3)

int(\* enable)(const struct net\_if \*iface, bool state)

Enable or disable the device (in response to admin state change).

**Definition** offloaded\_netdev.h:61

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [offloaded\_netdev.h](offloaded__netdev_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
