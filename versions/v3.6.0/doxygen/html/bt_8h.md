---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bt_8h.html
original_path: doxygen/html/bt_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt.h File Reference

Bluetooth L2 stack public header.
[More...](#details)

`#include <[zephyr/net/net_mgmt.h](net__mgmt_8h_source.md)>`

[Go to the source code of this file.](bt_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NET\_REQUEST\_BT\_ADVERTISE](#a2f21c722e30fba88ea8889fbf1e8e49f)   (\_NET\_BT\_BASE | [NET\_REQUEST\_BT\_CMD\_ADVERTISE](#ad8aacb4b3df6df02356939cf340bfd85a05824b9f8666281de0be14707e9b9ef1)) |
| #define | [NET\_REQUEST\_BT\_CONNECT](#aaf75ee6d31b2f16b94c392e70a57e8a0)   (\_NET\_BT\_BASE | [NET\_REQUEST\_BT\_CMD\_CONNECT](#ad8aacb4b3df6df02356939cf340bfd85a505613b3c8b9079e0b47a319bcf0de57)) |
| #define | [NET\_REQUEST\_BT\_SCAN](#a5170f730afa11a726d4369dc65039260)   (\_NET\_BT\_BASE | [NET\_REQUEST\_BT\_CMD\_SCAN](#ad8aacb4b3df6df02356939cf340bfd85ae33513ca673e9c54a8b93f1160c87bf1)) |
| #define | [NET\_EVENT\_BT\_SCAN\_RESULT](#a40a4822dcbe1890e54c67c8943584c80)   (\_NET\_BT\_EVENT | [NET\_EVENT\_BT\_CMD\_SCAN\_RESULT](#a0d85befb42a86f845b9fc1ec312d9a65ad1c9f4f1679cbc89b801ffd04b6f0033)) |
| #define | [NET\_REQUEST\_BT\_DISCONNECT](#a3798134fca04f5f7a576c215de22e6fa)   (\_NET\_BT\_BASE | [NET\_REQUEST\_BT\_CMD\_DISCONNECT](#ad8aacb4b3df6df02356939cf340bfd85aa34b01b4dd8da4bb07978604b7a9b48b)) |

| Enumerations | |
| --- | --- |
| enum | [net\_request\_bt\_cmd](#ad8aacb4b3df6df02356939cf340bfd85) { [NET\_REQUEST\_BT\_CMD\_ADVERTISE](#ad8aacb4b3df6df02356939cf340bfd85a05824b9f8666281de0be14707e9b9ef1) = 1 , [NET\_REQUEST\_BT\_CMD\_CONNECT](#ad8aacb4b3df6df02356939cf340bfd85a505613b3c8b9079e0b47a319bcf0de57) , [NET\_REQUEST\_BT\_CMD\_SCAN](#ad8aacb4b3df6df02356939cf340bfd85ae33513ca673e9c54a8b93f1160c87bf1) , [NET\_REQUEST\_BT\_CMD\_DISCONNECT](#ad8aacb4b3df6df02356939cf340bfd85aa34b01b4dd8da4bb07978604b7a9b48b) } |
| enum | [net\_event\_bt\_cmd](#a0d85befb42a86f845b9fc1ec312d9a65) { [NET\_EVENT\_BT\_CMD\_SCAN\_RESULT](#a0d85befb42a86f845b9fc1ec312d9a65ad1c9f4f1679cbc89b801ffd04b6f0033) = 1 } |

## Detailed Description

Bluetooth L2 stack public header.

## Macro Definition Documentation

## [◆ ](#a40a4822dcbe1890e54c67c8943584c80)NET\_EVENT\_BT\_SCAN\_RESULT

| #define NET\_EVENT\_BT\_SCAN\_RESULT   (\_NET\_BT\_EVENT | [NET\_EVENT\_BT\_CMD\_SCAN\_RESULT](#a0d85befb42a86f845b9fc1ec312d9a65ad1c9f4f1679cbc89b801ffd04b6f0033)) |
| --- |

## [◆ ](#a2f21c722e30fba88ea8889fbf1e8e49f)NET\_REQUEST\_BT\_ADVERTISE

| #define NET\_REQUEST\_BT\_ADVERTISE   (\_NET\_BT\_BASE | [NET\_REQUEST\_BT\_CMD\_ADVERTISE](#ad8aacb4b3df6df02356939cf340bfd85a05824b9f8666281de0be14707e9b9ef1)) |
| --- |

## [◆ ](#aaf75ee6d31b2f16b94c392e70a57e8a0)NET\_REQUEST\_BT\_CONNECT

| #define NET\_REQUEST\_BT\_CONNECT   (\_NET\_BT\_BASE | [NET\_REQUEST\_BT\_CMD\_CONNECT](#ad8aacb4b3df6df02356939cf340bfd85a505613b3c8b9079e0b47a319bcf0de57)) |
| --- |

## [◆ ](#a3798134fca04f5f7a576c215de22e6fa)NET\_REQUEST\_BT\_DISCONNECT

| #define NET\_REQUEST\_BT\_DISCONNECT   (\_NET\_BT\_BASE | [NET\_REQUEST\_BT\_CMD\_DISCONNECT](#ad8aacb4b3df6df02356939cf340bfd85aa34b01b4dd8da4bb07978604b7a9b48b)) |
| --- |

## [◆ ](#a5170f730afa11a726d4369dc65039260)NET\_REQUEST\_BT\_SCAN

| #define NET\_REQUEST\_BT\_SCAN   (\_NET\_BT\_BASE | [NET\_REQUEST\_BT\_CMD\_SCAN](#ad8aacb4b3df6df02356939cf340bfd85ae33513ca673e9c54a8b93f1160c87bf1)) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a0d85befb42a86f845b9fc1ec312d9a65)net\_event\_bt\_cmd

| enum [net\_event\_bt\_cmd](#a0d85befb42a86f845b9fc1ec312d9a65) |
| --- |

| Enumerator | |
| --- | --- |
| NET\_EVENT\_BT\_CMD\_SCAN\_RESULT |  |

## [◆ ](#ad8aacb4b3df6df02356939cf340bfd85)net\_request\_bt\_cmd

| enum [net\_request\_bt\_cmd](#ad8aacb4b3df6df02356939cf340bfd85) |
| --- |

| Enumerator | |
| --- | --- |
| NET\_REQUEST\_BT\_CMD\_ADVERTISE |  |
| NET\_REQUEST\_BT\_CMD\_CONNECT |  |
| NET\_REQUEST\_BT\_CMD\_SCAN |  |
| NET\_REQUEST\_BT\_CMD\_DISCONNECT |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [bt.h](bt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
