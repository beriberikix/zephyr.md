---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/conn__mgr__connectivity_8h_source.html
original_path: doxygen/html/conn__mgr__connectivity_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

conn\_mgr\_connectivity.h

[Go to the documentation of this file.](conn__mgr__connectivity_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_CONN\_MGR\_CONNECTIVITY\_H\_

14#define ZEPHYR\_INCLUDE\_CONN\_MGR\_CONNECTIVITY\_H\_

15

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/net/net\_if.h](net__if_8h.md)>

18#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

19#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

33

34

36

37/\* Connectivity Events \*/

38#define \_NET\_MGMT\_CONN\_LAYER NET\_MGMT\_LAYER(NET\_MGMT\_LAYER\_L2)

39#define \_NET\_MGMT\_CONN\_CODE NET\_MGMT\_LAYER\_CODE(0x207)

40#define \_NET\_MGMT\_CONN\_BASE (\_NET\_MGMT\_CONN\_LAYER | \_NET\_MGMT\_CONN\_CODE | \

41 NET\_MGMT\_EVENT\_BIT)

42#define \_NET\_MGMT\_CONN\_IF\_EVENT (NET\_MGMT\_IFACE\_BIT | \_NET\_MGMT\_CONN\_BASE)

43

44enum net\_event\_conn\_cmd {

45 NET\_EVENT\_CONN\_CMD\_IF\_TIMEOUT = 1,

46 NET\_EVENT\_CONN\_CMD\_IF\_FATAL\_ERROR,

47};

48

50

[ 54](group__conn__mgr__connectivity.md#ga5ea6e37ca9eda2b6fd8b165b8182dd38)#define NET\_EVENT\_CONN\_IF\_TIMEOUT \

55 (\_NET\_MGMT\_CONN\_IF\_EVENT | NET\_EVENT\_CONN\_CMD\_IF\_TIMEOUT)

56

[ 60](group__conn__mgr__connectivity.md#gae8f207559a7123bd2eca5ef08086d377)#define NET\_EVENT\_CONN\_IF\_FATAL\_ERROR \

61 (\_NET\_MGMT\_CONN\_IF\_EVENT | NET\_EVENT\_CONN\_CMD\_IF\_FATAL\_ERROR)

62

63

[ 67](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f)enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) {

[ 74](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f) [CONN\_MGR\_IF\_PERSISTENT](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f),

75

[ 82](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd) [CONN\_MGR\_IF\_NO\_AUTO\_CONNECT](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd),

83

[ 90](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d) [CONN\_MGR\_IF\_NO\_AUTO\_DOWN](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d),

91

93 /\* Total number of flags - must be at the end of the enum \*/

94 CONN\_MGR\_NUM\_IF\_FLAGS,

96};

97

[ 101](group__conn__mgr__connectivity.md#ga605eee24f4419b5cd6a50a0272979da7)#define CONN\_MGR\_IF\_NO\_TIMEOUT 0

102

[ 119](group__conn__mgr__connectivity.md#ga575d367c95592fd9f4ead694ff94543f)int [conn\_mgr\_if\_connect](group__conn__mgr__connectivity.md#ga575d367c95592fd9f4ead694ff94543f)(struct [net\_if](structnet__if.md) \*iface);

120

[ 135](group__conn__mgr__connectivity.md#gada2b5271b3e5dbcab629e1538b3d8eb4)int [conn\_mgr\_if\_disconnect](group__conn__mgr__connectivity.md#gada2b5271b3e5dbcab629e1538b3d8eb4)(struct [net\_if](structnet__if.md) \*iface);

136

[ 145](group__conn__mgr__connectivity.md#ga09a1169a89eac1a3291185281952ce05)bool [conn\_mgr\_if\_is\_bound](group__conn__mgr__connectivity.md#ga09a1169a89eac1a3291185281952ce05)(struct [net\_if](structnet__if.md) \*iface);

146

[ 166](group__conn__mgr__connectivity.md#ga2a2e6d7fbb7b1ed0327706a8c253d3e4)int [conn\_mgr\_if\_set\_opt](group__conn__mgr__connectivity.md#ga2a2e6d7fbb7b1ed0327706a8c253d3e4)(struct [net\_if](structnet__if.md) \*iface, int optname, const void \*optval, size\_t optlen);

167

[ 194](group__conn__mgr__connectivity.md#gaa79794ce9c773c0c3932121c931ac2d6)int [conn\_mgr\_if\_get\_opt](group__conn__mgr__connectivity.md#gaa79794ce9c773c0c3932121c931ac2d6)(struct [net\_if](structnet__if.md) \*iface, int optname, void \*optval, size\_t \*optlen);

195

[ 208](group__conn__mgr__connectivity.md#ga465c9491106cba3c9cb1cf296090612b)bool [conn\_mgr\_if\_get\_flag](group__conn__mgr__connectivity.md#ga465c9491106cba3c9cb1cf296090612b)(struct [net\_if](structnet__if.md) \*iface, enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) flag);

209

[ 223](group__conn__mgr__connectivity.md#gae86d1c808f31b8ca5e67bacbc844ef47)int [conn\_mgr\_if\_set\_flag](group__conn__mgr__connectivity.md#gae86d1c808f31b8ca5e67bacbc844ef47)(struct [net\_if](structnet__if.md) \*iface, enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) flag, bool value);

224

[ 235](group__conn__mgr__connectivity.md#gada9c37847acc604d82604351cbbb5e64)int [conn\_mgr\_if\_get\_timeout](group__conn__mgr__connectivity.md#gada9c37847acc604d82604351cbbb5e64)(struct [net\_if](structnet__if.md) \*iface);

236

[ 249](group__conn__mgr__connectivity.md#ga467ecbb330d21b8dfea3e0ce08448400)int [conn\_mgr\_if\_set\_timeout](group__conn__mgr__connectivity.md#ga467ecbb330d21b8dfea3e0ce08448400)(struct [net\_if](structnet__if.md) \*iface, int timeout);

250

254

261

[ 272](group__conn__mgr__connectivity__bulk.md#ga9e006b8b5095c223d77055fd619710c3)int [conn\_mgr\_all\_if\_up](group__conn__mgr__connectivity__bulk.md#ga9e006b8b5095c223d77055fd619710c3)(bool skip\_ignored);

273

274

[ 285](group__conn__mgr__connectivity__bulk.md#gabf6f8e5d8ce51b4c1cbf48f18a57efb2)int [conn\_mgr\_all\_if\_down](group__conn__mgr__connectivity__bulk.md#gabf6f8e5d8ce51b4c1cbf48f18a57efb2)(bool skip\_ignored);

286

[ 298](group__conn__mgr__connectivity__bulk.md#ga48e3c1b98f505af9f8ac811a25f94e1b)int [conn\_mgr\_all\_if\_connect](group__conn__mgr__connectivity__bulk.md#ga48e3c1b98f505af9f8ac811a25f94e1b)(bool skip\_ignored);

299

[ 311](group__conn__mgr__connectivity__bulk.md#ga3ce45d9040d3799e1387776257dfa8b7)int [conn\_mgr\_all\_if\_disconnect](group__conn__mgr__connectivity__bulk.md#ga3ce45d9040d3799e1387776257dfa8b7)(bool skip\_ignored);

312

316

317#ifdef \_\_cplusplus

318}

319#endif

320

321#endif /\* ZEPHYR\_INCLUDE\_CONN\_MGR\_CONNECTIVITY\_H\_ \*/

[device.h](device_8h.md)

[conn\_mgr\_all\_if\_disconnect](group__conn__mgr__connectivity__bulk.md#ga3ce45d9040d3799e1387776257dfa8b7)

int conn\_mgr\_all\_if\_disconnect(bool skip\_ignored)

Convenience function that disconnects all available ifaces that support connectivity without putting ...

[conn\_mgr\_all\_if\_connect](group__conn__mgr__connectivity__bulk.md#ga48e3c1b98f505af9f8ac811a25f94e1b)

int conn\_mgr\_all\_if\_connect(bool skip\_ignored)

Convenience function that takes all available ifaces into the admin-up state, and connects those that...

[conn\_mgr\_all\_if\_up](group__conn__mgr__connectivity__bulk.md#ga9e006b8b5095c223d77055fd619710c3)

int conn\_mgr\_all\_if\_up(bool skip\_ignored)

Convenience function that takes all available ifaces into the admin-up state.

[conn\_mgr\_all\_if\_down](group__conn__mgr__connectivity__bulk.md#gabf6f8e5d8ce51b4c1cbf48f18a57efb2)

int conn\_mgr\_all\_if\_down(bool skip\_ignored)

Convenience function that takes all available ifaces into the admin-down state.

[conn\_mgr\_if\_is\_bound](group__conn__mgr__connectivity.md#ga09a1169a89eac1a3291185281952ce05)

bool conn\_mgr\_if\_is\_bound(struct net\_if \*iface)

Check whether the provided network interface supports connectivity / has been bound to a connectivity...

[conn\_mgr\_if\_set\_opt](group__conn__mgr__connectivity.md#ga2a2e6d7fbb7b1ed0327706a8c253d3e4)

int conn\_mgr\_if\_set\_opt(struct net\_if \*iface, int optname, const void \*optval, size\_t optlen)

Set implementation-specific connectivity options.

[conn\_mgr\_if\_get\_flag](group__conn__mgr__connectivity.md#ga465c9491106cba3c9cb1cf296090612b)

bool conn\_mgr\_if\_get\_flag(struct net\_if \*iface, enum conn\_mgr\_if\_flag flag)

Check the value of connectivity flags.

[conn\_mgr\_if\_set\_timeout](group__conn__mgr__connectivity.md#ga467ecbb330d21b8dfea3e0ce08448400)

int conn\_mgr\_if\_set\_timeout(struct net\_if \*iface, int timeout)

Set the connectivity timeout for an iface.

[conn\_mgr\_if\_connect](group__conn__mgr__connectivity.md#ga575d367c95592fd9f4ead694ff94543f)

int conn\_mgr\_if\_connect(struct net\_if \*iface)

Connect interface.

[conn\_mgr\_if\_get\_opt](group__conn__mgr__connectivity.md#gaa79794ce9c773c0c3932121c931ac2d6)

int conn\_mgr\_if\_get\_opt(struct net\_if \*iface, int optname, void \*optval, size\_t \*optlen)

Get implementation-specific connectivity options.

[conn\_mgr\_if\_disconnect](group__conn__mgr__connectivity.md#gada2b5271b3e5dbcab629e1538b3d8eb4)

int conn\_mgr\_if\_disconnect(struct net\_if \*iface)

Disconnect interface.

[conn\_mgr\_if\_get\_timeout](group__conn__mgr__connectivity.md#gada9c37847acc604d82604351cbbb5e64)

int conn\_mgr\_if\_get\_timeout(struct net\_if \*iface)

Get the connectivity timeout for an iface.

[conn\_mgr\_if\_set\_flag](group__conn__mgr__connectivity.md#gae86d1c808f31b8ca5e67bacbc844ef47)

int conn\_mgr\_if\_set\_flag(struct net\_if \*iface, enum conn\_mgr\_if\_flag flag, bool value)

Set the value of a connectivity flags.

[conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f)

conn\_mgr\_if\_flag

Per-iface connectivity flags.

**Definition** conn\_mgr\_connectivity.h:67

[CONN\_MGR\_IF\_PERSISTENT](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f)

@ CONN\_MGR\_IF\_PERSISTENT

Persistent.

**Definition** conn\_mgr\_connectivity.h:74

[CONN\_MGR\_IF\_NO\_AUTO\_DOWN](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d)

@ CONN\_MGR\_IF\_NO\_AUTO\_DOWN

No auto-down.

**Definition** conn\_mgr\_connectivity.h:90

[CONN\_MGR\_IF\_NO\_AUTO\_CONNECT](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd)

@ CONN\_MGR\_IF\_NO\_AUTO\_CONNECT

No auto-connect.

**Definition** conn\_mgr\_connectivity.h:82

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [conn\_mgr\_connectivity.h](conn__mgr__connectivity_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
