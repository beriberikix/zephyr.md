---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__mgmt__msghdr.html
original_path: doxygen/html/structnet__mgmt__msghdr.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_mgmt\_msghdr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Core Library](group__socket__net__mgmt.md)

Each network management message is prefixed with this header.
[More...](#details)

`#include <[socket_net_mgmt.h](socket__net__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nm\_msg\_version](#a6867379b1ab13c504ee9884cc386c05e) |
|  | Network management version. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nm\_msg\_len](#ad7f4caefa6b3d8d93a480cd8210d7a4d) |
|  | Length of the data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [nm\_msg](#a09e1bc6f985b8fcc3397aa447b1d8e94) [] |
|  | The actual message data follows. |

## Detailed Description

Each network management message is prefixed with this header.

## Field Documentation

## [◆ ](#a09e1bc6f985b8fcc3397aa447b1d8e94)nm\_msg

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_mgmt\_msghdr::nm\_msg[] |
| --- |

The actual message data follows.

## [◆ ](#ad7f4caefa6b3d8d93a480cd8210d7a4d)nm\_msg\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_mgmt\_msghdr::nm\_msg\_len |
| --- |

Length of the data.

## [◆ ](#a6867379b1ab13c504ee9884cc386c05e)nm\_msg\_version

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_mgmt\_msghdr::nm\_msg\_version |
| --- |

Network management version.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket\_net\_mgmt.h](socket__net__mgmt_8h_source.md)

- [net\_mgmt\_msghdr](structnet__mgmt__msghdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
