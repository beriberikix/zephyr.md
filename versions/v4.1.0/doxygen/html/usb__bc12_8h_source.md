---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usb__bc12_8h_source.html
original_path: doxygen/html/usb__bc12_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_bc12.h

[Go to the documentation of this file.](usb__bc12_8h.md)

1/\*

2 \* Copyright (c) 2022 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_USB\_USB\_BC12\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_USB\_USB\_BC12\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

28/\* FIXME - make these Kconfig options \*/

29

34

[ 36](group__b12__interface.md#gae32f7af00346f7baf968287eb874d880)#define BC12\_CHARGER\_VOLTAGE\_UV 5000 \* 1000

[ 48](group__b12__interface.md#ga5ebbce02f5cb47de4565ef17d57ca25a)#define BC12\_CHARGER\_MIN\_CURR\_UA 2500

[ 50](group__b12__interface.md#gaa327167a6bb6ee0c44b98faab708d1f2)#define BC12\_CHARGER\_MAX\_CURR\_UA 1500 \* 1000

51

53

61#define BC12\_CURR\_UA(val) CLAMP(val, BC12\_CHARGER\_MIN\_CURR\_UA, BC12\_CHARGER\_MAX\_CURR\_UA)

63

[ 65](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73)enum [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73) {

[ 66](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a376830bcd04da44b9a2215a6f10dcf22) [BC12\_DISCONNECTED](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a376830bcd04da44b9a2215a6f10dcf22),

[ 67](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a8be0fd9ef5bc456b25964367388e3e48) [BC12\_PORTABLE\_DEVICE](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a8be0fd9ef5bc456b25964367388e3e48),

[ 68](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a2d7dffa7a9a134e55d48bf3c699d96ef) [BC12\_CHARGING\_PORT](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a2d7dffa7a9a134e55d48bf3c699d96ef),

69};

70

[ 72](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb)enum [bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb) {

[ 74](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba55bff2c1d47018dc7d175c178c6eefe6) [BC12\_TYPE\_NONE](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba55bff2c1d47018dc7d175c178c6eefe6),

[ 76](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba4109f85b375b5dbfd2eada250fc06425) [BC12\_TYPE\_SDP](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba4109f85b375b5dbfd2eada250fc06425),

[ 78](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba6ad9973121a077d239f8db7ecd7b76f3) [BC12\_TYPE\_DCP](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba6ad9973121a077d239f8db7ecd7b76f3),

[ 80](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba2b231ba4723445006b5993431064eb9c) [BC12\_TYPE\_CDP](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba2b231ba4723445006b5993431064eb9c),

[ 82](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba08527a826ab4639e4e6a72dc54c51bb2) [BC12\_TYPE\_PROPRIETARY](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba08527a826ab4639e4e6a72dc54c51bb2),

[ 84](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba25c692e9f22c761de33f738e08bf4e30) [BC12\_TYPE\_UNKNOWN](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba25c692e9f22c761de33f738e08bf4e30),

[ 86](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba672c2ed7c64ca4f13e1eb96456585d50) [BC12\_TYPE\_COUNT](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba672c2ed7c64ca4f13e1eb96456585d50),

87};

88

[ 101](structbc12__partner__state.md)struct [bc12\_partner\_state](structbc12__partner__state.md) {

[ 102](structbc12__partner__state.md#a4da4a226fd933eea17da379687d49acf) enum [bc12\_role](structbc12__partner__state.md#a4da4a226fd933eea17da379687d49acf) [bc12\_role](structbc12__partner__state.md#a4da4a226fd933eea17da379687d49acf);

103 union {

104 struct {

[ 105](structbc12__partner__state.md#adeeb33acadfa0e1a8a57b862dfad97a1) enum [bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb) [type](structbc12__partner__state.md#adeeb33acadfa0e1a8a57b862dfad97a1);

[ 106](structbc12__partner__state.md#a3a04b815fcc4c283d342b071dda1a0da) int [current\_ua](structbc12__partner__state.md#a3a04b815fcc4c283d342b071dda1a0da);

[ 107](structbc12__partner__state.md#a1cdea094ae13acbb46fcae6f60ec3a7b) int [voltage\_uv](structbc12__partner__state.md#a1cdea094ae13acbb46fcae6f60ec3a7b);

108 };

109 struct {

[ 110](structbc12__partner__state.md#a4c1a653bd2393d79680f75afef334ac9) bool [pd\_partner\_connected](structbc12__partner__state.md#a4c1a653bd2393d79680f75afef334ac9);

111 };

112 };

113};

114

[ 125](group__b12__interface.md#gaeb039486c7826fe493e7f402212f2661)typedef void (\*[bc12\_callback\_t](group__b12__interface.md#gaeb039486c7826fe493e7f402212f2661))(const struct [device](structdevice.md) \*dev, struct [bc12\_partner\_state](structbc12__partner__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

126 void \*user\_data);

127

133\_\_subsystem struct bc12\_driver\_api {

134 int (\*set\_role)(const struct [device](structdevice.md) \*dev, enum [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73) role);

135 int (\*set\_result\_cb)(const struct [device](structdevice.md) \*dev, [bc12\_callback\_t](group__b12__interface.md#gaeb039486c7826fe493e7f402212f2661) cb, void \*user\_data);

136};

140

[ 150](group__b12__interface.md#ga2a879017d34392308d4c078178db8407)\_\_syscall int [bc12\_set\_role](group__b12__interface.md#ga2a879017d34392308d4c078178db8407)(const struct [device](structdevice.md) \*dev, enum [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73) role);

151

152static inline int z\_impl\_bc12\_set\_role(const struct [device](structdevice.md) \*dev, enum [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73) role)

153{

154 const struct bc12\_driver\_api \*api = (const struct bc12\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

155

156 return api->set\_role(dev, role);

157}

158

[ 169](group__b12__interface.md#ga0db43c4cc595cb76738cf24d97fa5228)\_\_syscall int [bc12\_set\_result\_cb](group__b12__interface.md#ga0db43c4cc595cb76738cf24d97fa5228)(const struct [device](structdevice.md) \*dev, [bc12\_callback\_t](group__b12__interface.md#gaeb039486c7826fe493e7f402212f2661) cb, void \*user\_data);

170

171static inline int z\_impl\_bc12\_set\_result\_cb(const struct [device](structdevice.md) \*dev, [bc12\_callback\_t](group__b12__interface.md#gaeb039486c7826fe493e7f402212f2661) cb,

172 void \*user\_data)

173{

174 const struct bc12\_driver\_api \*api = (const struct bc12\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

175

176 return api->set\_result\_cb(dev, cb, user\_data);

177}

178

179#ifdef \_\_cplusplus

180}

181#endif

182

186

187#include <zephyr/syscalls/usb\_bc12.h>

188

189#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_USB\_USB\_BC12\_H\_ \*/

[device.h](device_8h.md)

[bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73)

bc12\_role

BC1.2 device role.

**Definition** usb\_bc12.h:65

[bc12\_set\_result\_cb](group__b12__interface.md#ga0db43c4cc595cb76738cf24d97fa5228)

int bc12\_set\_result\_cb(const struct device \*dev, bc12\_callback\_t cb, void \*user\_data)

Register a callback for BC1.2 results.

[bc12\_set\_role](group__b12__interface.md#ga2a879017d34392308d4c078178db8407)

int bc12\_set\_role(const struct device \*dev, enum bc12\_role role)

Set the BC1.2 role.

[bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb)

bc12\_type

BC1.2 charging partner type.

**Definition** usb\_bc12.h:72

[bc12\_callback\_t](group__b12__interface.md#gaeb039486c7826fe493e7f402212f2661)

void(\* bc12\_callback\_t)(const struct device \*dev, struct bc12\_partner\_state \*state, void \*user\_data)

BC1.2 callback for charger configuration.

**Definition** usb\_bc12.h:125

[BC12\_CHARGING\_PORT](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a2d7dffa7a9a134e55d48bf3c699d96ef)

@ BC12\_CHARGING\_PORT

**Definition** usb\_bc12.h:68

[BC12\_DISCONNECTED](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a376830bcd04da44b9a2215a6f10dcf22)

@ BC12\_DISCONNECTED

**Definition** usb\_bc12.h:66

[BC12\_PORTABLE\_DEVICE](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a8be0fd9ef5bc456b25964367388e3e48)

@ BC12\_PORTABLE\_DEVICE

**Definition** usb\_bc12.h:67

[BC12\_TYPE\_PROPRIETARY](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba08527a826ab4639e4e6a72dc54c51bb2)

@ BC12\_TYPE\_PROPRIETARY

Proprietary charging port.

**Definition** usb\_bc12.h:82

[BC12\_TYPE\_UNKNOWN](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba25c692e9f22c761de33f738e08bf4e30)

@ BC12\_TYPE\_UNKNOWN

Unknown charging port, BC1.2 detection failed.

**Definition** usb\_bc12.h:84

[BC12\_TYPE\_CDP](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba2b231ba4723445006b5993431064eb9c)

@ BC12\_TYPE\_CDP

Charging Downstream Port.

**Definition** usb\_bc12.h:80

[BC12\_TYPE\_SDP](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba4109f85b375b5dbfd2eada250fc06425)

@ BC12\_TYPE\_SDP

Standard Downstream Port.

**Definition** usb\_bc12.h:76

[BC12\_TYPE\_NONE](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba55bff2c1d47018dc7d175c178c6eefe6)

@ BC12\_TYPE\_NONE

No partner connected.

**Definition** usb\_bc12.h:74

[BC12\_TYPE\_COUNT](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba672c2ed7c64ca4f13e1eb96456585d50)

@ BC12\_TYPE\_COUNT

Count of valid BC12 types.

**Definition** usb\_bc12.h:86

[BC12\_TYPE\_DCP](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba6ad9973121a077d239f8db7ecd7b76f3)

@ BC12\_TYPE\_DCP

Dedicated Charging Port.

**Definition** usb\_bc12.h:78

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[bc12\_partner\_state](structbc12__partner__state.md)

BC1.2 detected partner state.

**Definition** usb\_bc12.h:101

[bc12\_partner\_state::voltage\_uv](structbc12__partner__state.md#a1cdea094ae13acbb46fcae6f60ec3a7b)

int voltage\_uv

**Definition** usb\_bc12.h:107

[bc12\_partner\_state::current\_ua](structbc12__partner__state.md#a3a04b815fcc4c283d342b071dda1a0da)

int current\_ua

**Definition** usb\_bc12.h:106

[bc12\_partner\_state::pd\_partner\_connected](structbc12__partner__state.md#a4c1a653bd2393d79680f75afef334ac9)

bool pd\_partner\_connected

**Definition** usb\_bc12.h:110

[bc12\_partner\_state::bc12\_role](structbc12__partner__state.md#a4da4a226fd933eea17da379687d49acf)

enum bc12\_role bc12\_role

**Definition** usb\_bc12.h:102

[bc12\_partner\_state::type](structbc12__partner__state.md#adeeb33acadfa0e1a8a57b862dfad97a1)

enum bc12\_type type

**Definition** usb\_bc12.h:105

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [usb\_bc12.h](usb__bc12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
