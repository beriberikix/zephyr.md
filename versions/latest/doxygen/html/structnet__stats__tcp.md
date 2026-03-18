---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__stats__tcp.html
original_path: doxygen/html/structnet__stats__tcp.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_tcp Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

TCP statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_stats\_bytes](structnet__stats__bytes.md) | [bytes](#af80c18bcc253133ce5f0597ac190b349) |
|  | Amount of received and sent TCP application data. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [resent](#abe567032cb4a267a984aec28c1e3cca4) |
|  | Amount of retransmitted data. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [drop](#aa549f7b6d5828009a09190fd64afa8e3) |
|  | Number of dropped packets at the TCP layer. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [recv](#ad25edb2b39a6acc8152c35ad43a5042f) |
|  | Number of received TCP segments. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [sent](#aa987bebf96000b6b4e92bfafc218759a) |
|  | Number of sent TCP segments. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [seg\_drop](#a5f045704859331918511e9c2281ac155) |
|  | Number of dropped TCP segments. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [chkerr](#a5099e174b0eafa322f0630f1f5c73a8b) |
|  | Number of TCP segments with a bad checksum. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [ackerr](#a0d40abc85776f0a9b9510a909b7f6d18) |
|  | Number of received TCP segments with a bad ACK number. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rsterr](#a471fcd5578f79ce77d20547b28503ac1) |
|  | Number of received bad TCP RST (reset) segments. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rst](#aa618cf86b962aca0f14eb9178c8ae61a) |
|  | Number of received TCP RST (reset) segments. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [rexmit](#a4a4ea6e5d87ef58b4271bd708cf39635) |
|  | Number of retransmitted TCP segments. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [conndrop](#ac557ac0d8917bc2c2dfed74126f993c8) |
|  | Number of dropped connection attempts because too few connections were available. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [connrst](#a67f55954a4c51f2b957c7d974e78c1c0) |
|  | Number of connection attempts for closed ports, triggering a RST. |

## Detailed Description

TCP statistics.

## Field Documentation

## [◆ ](#a0d40abc85776f0a9b9510a909b7f6d18)ackerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::ackerr |
| --- |

Number of received TCP segments with a bad ACK number.

## [◆ ](#af80c18bcc253133ce5f0597ac190b349)bytes

| struct [net\_stats\_bytes](structnet__stats__bytes.md) net\_stats\_tcp::bytes |
| --- |

Amount of received and sent TCP application data.

## [◆ ](#a5099e174b0eafa322f0630f1f5c73a8b)chkerr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::chkerr |
| --- |

Number of TCP segments with a bad checksum.

## [◆ ](#ac557ac0d8917bc2c2dfed74126f993c8)conndrop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::conndrop |
| --- |

Number of dropped connection attempts because too few connections were available.

## [◆ ](#a67f55954a4c51f2b957c7d974e78c1c0)connrst

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::connrst |
| --- |

Number of connection attempts for closed ports, triggering a RST.

## [◆ ](#aa549f7b6d5828009a09190fd64afa8e3)drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::drop |
| --- |

Number of dropped packets at the TCP layer.

## [◆ ](#ad25edb2b39a6acc8152c35ad43a5042f)recv

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::recv |
| --- |

Number of received TCP segments.

## [◆ ](#abe567032cb4a267a984aec28c1e3cca4)resent

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::resent |
| --- |

Amount of retransmitted data.

## [◆ ](#a4a4ea6e5d87ef58b4271bd708cf39635)rexmit

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::rexmit |
| --- |

Number of retransmitted TCP segments.

## [◆ ](#aa618cf86b962aca0f14eb9178c8ae61a)rst

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::rst |
| --- |

Number of received TCP RST (reset) segments.

## [◆ ](#a471fcd5578f79ce77d20547b28503ac1)rsterr

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::rsterr |
| --- |

Number of received bad TCP RST (reset) segments.

## [◆ ](#a5f045704859331918511e9c2281ac155)seg\_drop

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::seg\_drop |
| --- |

Number of dropped TCP segments.

## [◆ ](#aa987bebf96000b6b4e92bfafc218759a)sent

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_tcp::sent |
| --- |

Number of sent TCP segments.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_tcp](structnet__stats__tcp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
