---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/conn__mgr__monitor_8h_source.html
original_path: doxygen/html/conn__mgr__monitor_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

11

12#ifndef ZEPHYR\_INCLUDE\_CONN\_MGR\_H\_

13#define ZEPHYR\_INCLUDE\_CONN\_MGR\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19#if defined(CONFIG\_NET\_CONNECTION\_MANAGER) || defined(\_\_DOXYGEN\_\_)

20

27

28struct [net\_if](structnet__if.md);

29struct [net\_l2](structnet__l2.md);

30

[ 35](group__conn__mgr.md#gacdde95f41f32e7a829d8cd3a6d0e2277)void [conn\_mgr\_mon\_resend\_status](group__conn__mgr.md#gacdde95f41f32e7a829d8cd3a6d0e2277)(void);

36

[ 48](group__conn__mgr.md#ga7bad393c43a24df7a03176830b05b288)void [conn\_mgr\_ignore\_iface](group__conn__mgr.md#ga7bad393c43a24df7a03176830b05b288)(struct [net\_if](structnet__if.md) \*iface);

49

[ 63](group__conn__mgr.md#gacc8735b835dea9b31531fcca9fe8a979)void [conn\_mgr\_watch\_iface](group__conn__mgr.md#gacc8735b835dea9b31531fcca9fe8a979)(struct [net\_if](structnet__if.md) \*iface);

64

[ 72](group__conn__mgr.md#gada16a88ec2c1db71fc39782b0696dac2)bool [conn\_mgr\_is\_iface\_ignored](group__conn__mgr.md#gada16a88ec2c1db71fc39782b0696dac2)(struct [net\_if](structnet__if.md) \*iface);

73

[ 81](group__conn__mgr.md#ga6bd1ee46dc2e3dae554fce49e82c6187)void [conn\_mgr\_ignore\_l2](group__conn__mgr.md#ga6bd1ee46dc2e3dae554fce49e82c6187)(const struct [net\_l2](structnet__l2.md) \*l2);

82

[ 90](group__conn__mgr.md#gad96056478dcbcb568dd2ef8d5d2ad50b)void [conn\_mgr\_watch\_l2](group__conn__mgr.md#gad96056478dcbcb568dd2ef8d5d2ad50b)(const struct [net\_l2](structnet__l2.md) \*l2);

91

95

96#else

97

98#define conn\_mgr\_mon\_resend\_status(...)

99#define conn\_mgr\_ignore\_iface(...)

100#define conn\_mgr\_watch\_iface(...)

101#define conn\_mgr\_ignore\_l2(...)

102#define conn\_mgr\_watch\_l2(...)

103

104#endif /\* CONFIG\_NET\_CONNECTION\_MANAGER \*/

105

106#ifdef \_\_cplusplus

107}

108#endif

109

110#endif /\* ZEPHYR\_INCLUDE\_CONN\_MGR\_H\_ \*/

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

**Definition** net\_if.h:678

[net\_l2](structnet__l2.md)

Network L2 structure.

**Definition** net\_l2.h:55

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [conn\_mgr\_monitor.h](conn__mgr__monitor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
