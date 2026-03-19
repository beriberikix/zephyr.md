---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dhcpv4__server_8h_source.html
original_path: doxygen/html/dhcpv4__server_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dhcpv4\_server.h

[Go to the documentation of this file.](dhcpv4__server_8h.md)

1

4

5/\*

6 \* Copyright (c) 2024 Nordic Semiconductor ASA

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_DHCPV4\_SERVER\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_DHCPV4\_SERVER\_H\_

13

14#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

15#include <[zephyr/sys\_clock.h](sys__clock_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

29

31

32struct [net\_if](structnet__if.md);

33

34#define DHCPV4\_CLIENT\_ID\_MAX\_SIZE 20

35

36enum dhcpv4\_server\_addr\_state {

37 DHCPV4\_SERVER\_ADDR\_FREE,

38 DHCPV4\_SERVER\_ADDR\_RESERVED,

39 DHCPV4\_SERVER\_ADDR\_ALLOCATED,

40 DHCPV4\_SERVER\_ADDR\_DECLINED,

41};

42

43struct dhcpv4\_client\_id {

44 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buf[DHCPV4\_CLIENT\_ID\_MAX\_SIZE];

45 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len;

46};

47

48struct dhcpv4\_addr\_slot {

49 enum dhcpv4\_server\_addr\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

50 struct dhcpv4\_client\_id client\_id;

51 struct in\_addr addr;

52 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lease\_time;

53 k\_timepoint\_t expiry;

54};

55

57

[ 72](group__dhcpv4__server.md#ga2f3cc50c9428fe45540535fc66bec052)int [net\_dhcpv4\_server\_start](group__dhcpv4__server.md#ga2f3cc50c9428fe45540535fc66bec052)(struct [net\_if](structnet__if.md) \*iface, struct [in\_addr](structin__addr.md) \*base\_addr);

73

[ 84](group__dhcpv4__server.md#ga7955e5f3ff357c292a8641c0385f34e4)int [net\_dhcpv4\_server\_stop](group__dhcpv4__server.md#ga7955e5f3ff357c292a8641c0385f34e4)(struct [net\_if](structnet__if.md) \*iface);

85

[ 94](group__dhcpv4__server.md#gabd37fd84bc25525d4f1aec4df8aef8b6)typedef void (\*[net\_dhcpv4\_lease\_cb\_t](group__dhcpv4__server.md#gabd37fd84bc25525d4f1aec4df8aef8b6))(struct [net\_if](structnet__if.md) \*iface,

95 struct dhcpv4\_addr\_slot \*lease,

96 void \*user\_data);

97

[ 108](group__dhcpv4__server.md#ga636b2c71a7d5f00997cba946c31c0c00)int [net\_dhcpv4\_server\_foreach\_lease](group__dhcpv4__server.md#ga636b2c71a7d5f00997cba946c31c0c00)(struct [net\_if](structnet__if.md) \*iface,

109 [net\_dhcpv4\_lease\_cb\_t](group__dhcpv4__server.md#gabd37fd84bc25525d4f1aec4df8aef8b6) cb,

110 void \*user\_data);

111

[ 127](group__dhcpv4__server.md#ga416f4c6f173622d602aa122c5d3ca55e)typedef int (\*[net\_dhcpv4\_server\_provider\_cb\_t](group__dhcpv4__server.md#ga416f4c6f173622d602aa122c5d3ca55e))(struct [net\_if](structnet__if.md) \*iface,

128 const struct dhcpv4\_client\_id \*client\_id,

129 struct [in\_addr](structin__addr.md) \*addr,

130 void \*user\_data);

[ 137](group__dhcpv4__server.md#ga1db06c0bf6a5f79334c81472b0a37bb7)void [net\_dhcpv4\_server\_set\_provider\_cb](group__dhcpv4__server.md#ga1db06c0bf6a5f79334c81472b0a37bb7)([net\_dhcpv4\_server\_provider\_cb\_t](group__dhcpv4__server.md#ga416f4c6f173622d602aa122c5d3ca55e) cb,

138 void \*user\_data);

139

143

144#ifdef \_\_cplusplus

145}

146#endif

147

148#endif /\* ZEPHYR\_INCLUDE\_NET\_DHCPV4\_SERVER\_H\_ \*/

[net\_dhcpv4\_server\_set\_provider\_cb](group__dhcpv4__server.md#ga1db06c0bf6a5f79334c81472b0a37bb7)

void net\_dhcpv4\_server\_set\_provider\_cb(net\_dhcpv4\_server\_provider\_cb\_t cb, void \*user\_data)

Set the callback used to provide addresses to the DHCP server.

[net\_dhcpv4\_server\_start](group__dhcpv4__server.md#ga2f3cc50c9428fe45540535fc66bec052)

int net\_dhcpv4\_server\_start(struct net\_if \*iface, struct in\_addr \*base\_addr)

Start DHCPv4 server instance on an iface.

[net\_dhcpv4\_server\_provider\_cb\_t](group__dhcpv4__server.md#ga416f4c6f173622d602aa122c5d3ca55e)

int(\* net\_dhcpv4\_server\_provider\_cb\_t)(struct net\_if \*iface, const struct dhcpv4\_client\_id \*client\_id, struct in\_addr \*addr, void \*user\_data)

Callback used to let application provide an address for a given client ID.

**Definition** dhcpv4\_server.h:127

[net\_dhcpv4\_server\_foreach\_lease](group__dhcpv4__server.md#ga636b2c71a7d5f00997cba946c31c0c00)

int net\_dhcpv4\_server\_foreach\_lease(struct net\_if \*iface, net\_dhcpv4\_lease\_cb\_t cb, void \*user\_data)

Iterate over all DHCPv4 address leases on a given network interface and call callback for each lease.

[net\_dhcpv4\_server\_stop](group__dhcpv4__server.md#ga7955e5f3ff357c292a8641c0385f34e4)

int net\_dhcpv4\_server\_stop(struct net\_if \*iface)

Stop DHCPv4 server instance on an iface.

[net\_dhcpv4\_lease\_cb\_t](group__dhcpv4__server.md#gabd37fd84bc25525d4f1aec4df8aef8b6)

void(\* net\_dhcpv4\_lease\_cb\_t)(struct net\_if \*iface, struct dhcpv4\_addr\_slot \*lease, void \*user\_data)

Callback used while iterating over active DHCPv4 address leases.

**Definition** dhcpv4\_server.h:94

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:155

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[sys\_clock.h](sys__clock_8h.md)

Variables needed for system clock.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dhcpv4\_server.h](dhcpv4__server_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
