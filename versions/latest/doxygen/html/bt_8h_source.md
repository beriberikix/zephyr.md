---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bt_8h_source.html
original_path: doxygen/html/bt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt.h

[Go to the documentation of this file.](bt_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_BT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_BT\_H\_

14

15#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21/\* Management part definitions \*/

22

23#define \_NET\_BT\_LAYER NET\_MGMT\_LAYER\_L2

24#define \_NET\_BT\_CODE 0x155

25#define \_NET\_BT\_BASE (NET\_MGMT\_IFACE\_BIT | \

26 NET\_MGMT\_LAYER(\_NET\_BT\_LAYER) | \

27 NET\_MGMT\_LAYER\_CODE(\_NET\_BT\_CODE))

28#define \_NET\_BT\_EVENT (\_NET\_BT\_BASE | NET\_MGMT\_EVENT\_BIT)

29

[ 30](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85)enum [net\_request\_bt\_cmd](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85) {

[ 31](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85a05824b9f8666281de0be14707e9b9ef1) [NET\_REQUEST\_BT\_CMD\_ADVERTISE](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85a05824b9f8666281de0be14707e9b9ef1) = 1,

[ 32](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85a505613b3c8b9079e0b47a319bcf0de57) [NET\_REQUEST\_BT\_CMD\_CONNECT](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85a505613b3c8b9079e0b47a319bcf0de57),

[ 33](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85ae33513ca673e9c54a8b93f1160c87bf1) [NET\_REQUEST\_BT\_CMD\_SCAN](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85ae33513ca673e9c54a8b93f1160c87bf1),

[ 34](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85aa34b01b4dd8da4bb07978604b7a9b48b) [NET\_REQUEST\_BT\_CMD\_DISCONNECT](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85aa34b01b4dd8da4bb07978604b7a9b48b),

35};

36

[ 37](bt_8h.md#a2f21c722e30fba88ea8889fbf1e8e49f)#define NET\_REQUEST\_BT\_ADVERTISE \

38 (\_NET\_BT\_BASE | NET\_REQUEST\_BT\_CMD\_ADVERTISE)

39

40[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_BT\_ADVERTISE](bt_8h.md#a2f21c722e30fba88ea8889fbf1e8e49f));

41

[ 42](bt_8h.md#aaf75ee6d31b2f16b94c392e70a57e8a0)#define NET\_REQUEST\_BT\_CONNECT \

43 (\_NET\_BT\_BASE | NET\_REQUEST\_BT\_CMD\_CONNECT)

44

45[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_BT\_CONNECT](bt_8h.md#aaf75ee6d31b2f16b94c392e70a57e8a0));

46

[ 47](bt_8h.md#a5170f730afa11a726d4369dc65039260)#define NET\_REQUEST\_BT\_SCAN \

48 (\_NET\_BT\_BASE | NET\_REQUEST\_BT\_CMD\_SCAN)

49

50[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_BT\_SCAN](bt_8h.md#a5170f730afa11a726d4369dc65039260));

51

[ 52](bt_8h.md#a0d85befb42a86f845b9fc1ec312d9a65)enum [net\_event\_bt\_cmd](bt_8h.md#a0d85befb42a86f845b9fc1ec312d9a65) {

[ 53](bt_8h.md#a0d85befb42a86f845b9fc1ec312d9a65ad1c9f4f1679cbc89b801ffd04b6f0033) [NET\_EVENT\_BT\_CMD\_SCAN\_RESULT](bt_8h.md#a0d85befb42a86f845b9fc1ec312d9a65ad1c9f4f1679cbc89b801ffd04b6f0033) = 1,

54};

55

[ 56](bt_8h.md#a40a4822dcbe1890e54c67c8943584c80)#define NET\_EVENT\_BT\_SCAN\_RESULT \

57 (\_NET\_BT\_EVENT | NET\_EVENT\_BT\_CMD\_SCAN\_RESULT)

58

[ 59](bt_8h.md#a3798134fca04f5f7a576c215de22e6fa)#define NET\_REQUEST\_BT\_DISCONNECT \

60 (\_NET\_BT\_BASE | NET\_REQUEST\_BT\_CMD\_DISCONNECT)

61

62[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)([NET\_REQUEST\_BT\_DISCONNECT](bt_8h.md#a3798134fca04f5f7a576c215de22e6fa));

63

64#ifdef \_\_cplusplus

65}

66#endif

67

68#endif /\* ZEPHYR\_INCLUDE\_NET\_BT\_H\_ \*/

[net\_event\_bt\_cmd](bt_8h.md#a0d85befb42a86f845b9fc1ec312d9a65)

net\_event\_bt\_cmd

**Definition** bt.h:52

[NET\_EVENT\_BT\_CMD\_SCAN\_RESULT](bt_8h.md#a0d85befb42a86f845b9fc1ec312d9a65ad1c9f4f1679cbc89b801ffd04b6f0033)

@ NET\_EVENT\_BT\_CMD\_SCAN\_RESULT

**Definition** bt.h:53

[NET\_REQUEST\_BT\_ADVERTISE](bt_8h.md#a2f21c722e30fba88ea8889fbf1e8e49f)

#define NET\_REQUEST\_BT\_ADVERTISE

**Definition** bt.h:37

[NET\_REQUEST\_BT\_DISCONNECT](bt_8h.md#a3798134fca04f5f7a576c215de22e6fa)

#define NET\_REQUEST\_BT\_DISCONNECT

**Definition** bt.h:59

[NET\_REQUEST\_BT\_SCAN](bt_8h.md#a5170f730afa11a726d4369dc65039260)

#define NET\_REQUEST\_BT\_SCAN

**Definition** bt.h:47

[NET\_REQUEST\_BT\_CONNECT](bt_8h.md#aaf75ee6d31b2f16b94c392e70a57e8a0)

#define NET\_REQUEST\_BT\_CONNECT

**Definition** bt.h:42

[net\_request\_bt\_cmd](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85)

net\_request\_bt\_cmd

**Definition** bt.h:30

[NET\_REQUEST\_BT\_CMD\_ADVERTISE](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85a05824b9f8666281de0be14707e9b9ef1)

@ NET\_REQUEST\_BT\_CMD\_ADVERTISE

**Definition** bt.h:31

[NET\_REQUEST\_BT\_CMD\_CONNECT](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85a505613b3c8b9079e0b47a319bcf0de57)

@ NET\_REQUEST\_BT\_CMD\_CONNECT

**Definition** bt.h:32

[NET\_REQUEST\_BT\_CMD\_DISCONNECT](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85aa34b01b4dd8da4bb07978604b7a9b48b)

@ NET\_REQUEST\_BT\_CMD\_DISCONNECT

**Definition** bt.h:34

[NET\_REQUEST\_BT\_CMD\_SCAN](bt_8h.md#ad8aacb4b3df6df02356939cf340bfd85ae33513ca673e9c54a8b93f1160c87bf1)

@ NET\_REQUEST\_BT\_CMD\_SCAN

**Definition** bt.h:33

[NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)

#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request)

**Definition** net\_mgmt.h:96

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [bt.h](bt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
