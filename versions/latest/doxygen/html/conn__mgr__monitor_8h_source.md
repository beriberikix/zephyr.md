---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/conn__mgr__monitor_8h_source.html
original_path: doxygen/html/conn__mgr__monitor_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

conn\_mgr\_monitor.h

[Go to the documentation of this file.](conn__mgr__monitor_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_CONN\_MGR\_H\_

8#define ZEPHYR\_INCLUDE\_CONN\_MGR\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#if defined(CONFIG\_NET\_CONNECTION\_MANAGER) || defined(\_\_DOXYGEN\_\_)

15

22

23struct [net\_if](structnet__if.md);

24struct [net\_l2](structnet__l2.md);

25

[ 30](group__conn__mgr.md#gacdde95f41f32e7a829d8cd3a6d0e2277)void [conn\_mgr\_mon\_resend\_status](group__conn__mgr.md#gacdde95f41f32e7a829d8cd3a6d0e2277)(void);

31

[ 43](group__conn__mgr.md#ga7bad393c43a24df7a03176830b05b288)void [conn\_mgr\_ignore\_iface](group__conn__mgr.md#ga7bad393c43a24df7a03176830b05b288)(struct [net\_if](structnet__if.md) \*iface);

44

[ 58](group__conn__mgr.md#gacc8735b835dea9b31531fcca9fe8a979)void [conn\_mgr\_watch\_iface](group__conn__mgr.md#gacc8735b835dea9b31531fcca9fe8a979)(struct [net\_if](structnet__if.md) \*iface);

59

[ 67](group__conn__mgr.md#gada16a88ec2c1db71fc39782b0696dac2)bool [conn\_mgr\_is\_iface\_ignored](group__conn__mgr.md#gada16a88ec2c1db71fc39782b0696dac2)(struct [net\_if](structnet__if.md) \*iface);

68

[ 76](group__conn__mgr.md#ga6bd1ee46dc2e3dae554fce49e82c6187)void [conn\_mgr\_ignore\_l2](group__conn__mgr.md#ga6bd1ee46dc2e3dae554fce49e82c6187)(const struct [net\_l2](structnet__l2.md) \*l2);

77

[ 85](group__conn__mgr.md#gad96056478dcbcb568dd2ef8d5d2ad50b)void [conn\_mgr\_watch\_l2](group__conn__mgr.md#gad96056478dcbcb568dd2ef8d5d2ad50b)(const struct [net\_l2](structnet__l2.md) \*l2);

86

90

91#else

92

93#define conn\_mgr\_mon\_resend\_status(...)

94#define conn\_mgr\_ignore\_iface(...)

95#define conn\_mgr\_watch\_iface(...)

96#define conn\_mgr\_ignore\_l2(...)

97#define conn\_mgr\_watch\_l2(...)

98

99#endif /\* CONFIG\_NET\_CONNECTION\_MANAGER \*/

100

101#ifdef \_\_cplusplus

102}

103#endif

104

105#endif /\* ZEPHYR\_INCLUDE\_CONN\_MGR\_H\_ \*/

[conn\_mgr\_ignore\_l2](group__conn__mgr.md#ga6bd1ee46dc2e3dae554fce49e82c6187)

void conn\_mgr\_ignore\_l2(const struct net\_l2 \*l2)

Mark an L2 to be ignored by conn\_mgr.

[conn\_mgr\_ignore\_iface](group__conn__mgr.md#ga7bad393c43a24df7a03176830b05b288)

void conn\_mgr\_ignore\_iface(struct net\_if \*iface)

Mark an iface to be ignored by conn\_mgr.

[conn\_mgr\_watch\_iface](group__conn__mgr.md#gacc8735b835dea9b31531fcca9fe8a979)

void conn\_mgr\_watch\_iface(struct net\_if \*iface)

Watch (stop ignoring) an iface.

[conn\_mgr\_mon\_resend\_status](group__conn__mgr.md#gacdde95f41f32e7a829d8cd3a6d0e2277)

void conn\_mgr\_mon\_resend\_status(void)

Resend either NET\_L4\_CONNECTED or NET\_L4\_DISCONNECTED depending on whether connectivity is currently ...

[conn\_mgr\_watch\_l2](group__conn__mgr.md#gad96056478dcbcb568dd2ef8d5d2ad50b)

void conn\_mgr\_watch\_l2(const struct net\_l2 \*l2)

Watch (stop ignoring) an L2.

[conn\_mgr\_is\_iface\_ignored](group__conn__mgr.md#gada16a88ec2c1db71fc39782b0696dac2)

bool conn\_mgr\_is\_iface\_ignored(struct net\_if \*iface)

Check whether the provided iface is currently ignored.

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

[net\_l2](structnet__l2.md)

Network L2 structure.

**Definition** net\_l2.h:55

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [conn\_mgr\_monitor.h](conn__mgr__monitor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
