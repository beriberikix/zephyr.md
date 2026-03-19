---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ieee802154__mgmt.html
original_path: doxygen/html/group__ieee802154__mgmt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

IEEE 802.15.4 Net Management

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md)

IEEE 802.15.4 net management library.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ieee802154\_req\_params](structieee802154__req__params.md) |
|  | Scanning parameters. [More...](structieee802154__req__params.md#details) |
| struct | [ieee802154\_security\_params](structieee802154__security__params.md) |
|  | Security parameters. [More...](structieee802154__security__params.md#details) |

| Command Macros | |
| --- | --- |
| IEEE 802.15.4 net management commands.  These IEEE 802.15.4 subsystem net management commands can be called by applications via [Network Management](group__net__mgmt.md "Network Management") macro.  All attributes and parameters are given in CPU byte order (scalars) or big endian (byte arrays) unless otherwise specified.  The following IEEE 802.15.4 MAC management service primitives are referenced in this enumeration:   - MLME-ASSOCIATE.request, see section 8.2.3 - MLME-DISASSOCIATE.request, see section 8.2.4 - MLME-SET/GET.request, see section 8.2.6 - MLME-SCAN.request, see section 8.2.11   The following IEEE 802.15.4 MAC data service primitives are referenced in this enumeration:   - MLME-DATA.request, see section 8.3.2   MAC PIB attributes (mac.../sec...): see sections 8.4.3 and 9.5. PHY PIB attributes (phy...): see section 11.3. Both are accessed through MLME-SET/GET primitives. | |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_ACK](#ga9fb911bed94845e723d686ded38929da)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_ACK) |
|  | Sets AckTx for all subsequent MLME-DATA (aka TX) requests. |
| #define | [NET\_REQUEST\_IEEE802154\_UNSET\_ACK](#gafa484eb90d0c8d3d7ef01b5a7edb2a18)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_UNSET\_ACK) |
|  | Unsets AckTx for all subsequent MLME-DATA requests. |
| #define | [NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN](#ga72d022935a39436e95f61cceb8001ed9)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_PASSIVE\_SCAN) |
|  | MLME-SCAN(PASSIVE, ...) request. |
| #define | [NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN](#gab7ad1a0db3c9a361eab52e0cf484d11b)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_ACTIVE\_SCAN) |
|  | MLME-SCAN(ACTIVE, ...) request. |
| #define | [NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN](#gaefba66b873c90b3db1ad9bfce98ceebe)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_CANCEL\_SCAN) |
|  | Cancels an ongoing MLME-SCAN(...) command (non-standard). |
| #define | [NET\_REQUEST\_IEEE802154\_ASSOCIATE](#ga01e2180457cd99095e56ae3fa9f79dbf)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_ASSOCIATE) |
|  | MLME-ASSOCIATE(...) request. |
| #define | [NET\_REQUEST\_IEEE802154\_DISASSOCIATE](#gace7c47eba4e022f54000932814ce4edd)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_DISASSOCIATE) |
|  | MLME-DISASSOCIATE(...) request. |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_CHANNEL](#ga5cc7d53ae273c9977de07305efbc0ced)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_CHANNEL) |
|  | MLME-SET(phyCurrentChannel) request. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_CHANNEL](#gad154b4b5affb3a8a59226a241c84a14b)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_CHANNEL) |
|  | MLME-GET(phyCurrentChannel) request. |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID](#ga9428b28728e2060586761e1f08cf983c)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_PAN\_ID) |
|  | MLME-SET(macPanId) request. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID](#ga8a0a0c9c6b3762ebe06df860aee9431f)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_PAN\_ID) |
|  | MLME-GET(macPanId) request. |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR](#gadfb408432bfd2f58eea8d695747471e9)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_EXT\_ADDR) |
|  | Sets the extended interface address (non-standard), see sections 7.1 and 8.4.3.1, in big endian byte order. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR](#gaf64388508d21c5a17896c82ef1e3ac66)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_EXT\_ADDR) |
|  | like MLME-GET(macExtendedAddress) but in big endian byte order |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR](#ga9b5411f4d458421c0528e0e850c54465)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_SHORT\_ADDR) |
|  | MLME-SET(macShortAddress) request, only allowed for co-ordinators. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR](#ga60b38fa4a0a1248e5e491cd7b2b85241)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_SHORT\_ADDR) |
|  | MLME-GET(macShortAddress) request. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER](#ga07062abc2ce8ebb326e89bee768c3638)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_TX\_POWER) |
|  | MLME-SET(phyUnicastTxPower/phyBroadcastTxPower) request (currently not distinguished). |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER](#ga4399c84db1c15406685d218a2e1190f4)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_TX\_POWER) |
|  | MLME-GET(phyUnicastTxPower/phyBroadcastTxPower) request. |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS](#ga907b00f07cdbe9fe33e19ec323d56654)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_SECURITY\_SETTINGS) |
|  | Configures basic sec\* MAC PIB attributes, implies macSecurityEnabled=true. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS](#ga120d2a00dd3ade6d413e1763c41075df)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_SECURITY\_SETTINGS) |
|  | Gets the configured sec\* attributes. |

| Event Macros | |
| --- | --- |
| IEEE 802.15.4 net management events.  These IEEE 802.15.4 subsystem net management events can be subscribed to by applications via [net\_mgmt\_init\_event\_callback](group__net__mgmt.md#gaa1d086dcdeb54412073e287129bc50e0 "net_mgmt_init_event_callback"), [net\_mgmt\_add\_event\_callback](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f "net_mgmt_add_event_callback") and [net\_mgmt\_del\_event\_callback](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946 "net_mgmt_del_event_callback"). | |
| #define | [NET\_EVENT\_IEEE802154\_SCAN\_RESULT](#ga0442eaa04068a7b66f9b4ae40b570470)   (\_NET\_IEEE802154\_EVENT | NET\_EVENT\_IEEE802154\_CMD\_SCAN\_RESULT) |
|  | Signals the result of the [NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN](#gab7ad1a0db3c9a361eab52e0cf484d11b) or [NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN](#ga72d022935a39436e95f61cceb8001ed9) net management commands. |

## Detailed Description

IEEE 802.15.4 net management library.

Since
:   1.0

Version
:   0.8.0

The IEEE 802.15.4 net management library provides runtime configuration features that applications can interface with directly.

Most of these commands are also accessible via shell commands. See the shell's help feature ([shell](structshell.md "Shell instance internals.")> [IEEE 802.15.4 and Thread APIs](group__ieee802154.md "IEEE 802.15.4 native and OpenThread L2, configuration, management and driver APIs.") help).

Note
:   All section, table and figure references are to the IEEE 802.15.4-2020 standard.

## Macro Definition Documentation

## [◆ ](#ga0442eaa04068a7b66f9b4ae40b570470)NET\_EVENT\_IEEE802154\_SCAN\_RESULT

| #define NET\_EVENT\_IEEE802154\_SCAN\_RESULT   (\_NET\_IEEE802154\_EVENT | NET\_EVENT\_IEEE802154\_CMD\_SCAN\_RESULT) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

Signals the result of the [NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN](#gab7ad1a0db3c9a361eab52e0cf484d11b) or [NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN](#ga72d022935a39436e95f61cceb8001ed9) net management commands.

See [ieee802154\_req\_params](structieee802154__req__params.md "ieee802154_req_params") for associated event parameters.

## [◆ ](#gab7ad1a0db3c9a361eab52e0cf484d11b)NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN

| #define NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_ACTIVE\_SCAN) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-SCAN(ACTIVE, ...) request.

See [ieee802154\_req\_params](structieee802154__req__params.md "ieee802154_req_params") for associated command parameters.

## [◆ ](#ga01e2180457cd99095e56ae3fa9f79dbf)NET\_REQUEST\_IEEE802154\_ASSOCIATE

| #define NET\_REQUEST\_IEEE802154\_ASSOCIATE   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_ASSOCIATE) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-ASSOCIATE(...) request.

## [◆ ](#gaefba66b873c90b3db1ad9bfce98ceebe)NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN

| #define NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_CANCEL\_SCAN) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

Cancels an ongoing MLME-SCAN(...) command (non-standard).

## [◆ ](#gace7c47eba4e022f54000932814ce4edd)NET\_REQUEST\_IEEE802154\_DISASSOCIATE

| #define NET\_REQUEST\_IEEE802154\_DISASSOCIATE   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_DISASSOCIATE) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-DISASSOCIATE(...) request.

## [◆ ](#gad154b4b5affb3a8a59226a241c84a14b)NET\_REQUEST\_IEEE802154\_GET\_CHANNEL

| #define NET\_REQUEST\_IEEE802154\_GET\_CHANNEL   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_CHANNEL) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-GET(phyCurrentChannel) request.

## [◆ ](#gaf64388508d21c5a17896c82ef1e3ac66)NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR

| #define NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_EXT\_ADDR) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

like MLME-GET(macExtendedAddress) but in big endian byte order

## [◆ ](#ga8a0a0c9c6b3762ebe06df860aee9431f)NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID

| #define NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_PAN\_ID) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-GET(macPanId) request.

## [◆ ](#ga120d2a00dd3ade6d413e1763c41075df)NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS

| #define NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_SECURITY\_SETTINGS) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

Gets the configured sec\* attributes.

See [ieee802154\_security\_params](structieee802154__security__params.md "ieee802154_security_params") for associated command parameters.

## [◆ ](#ga60b38fa4a0a1248e5e491cd7b2b85241)NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR

| #define NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_SHORT\_ADDR) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-GET(macShortAddress) request.

## [◆ ](#ga07062abc2ce8ebb326e89bee768c3638)NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER

| #define NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_TX\_POWER) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-SET(phyUnicastTxPower/phyBroadcastTxPower) request (currently not distinguished).

## [◆ ](#ga72d022935a39436e95f61cceb8001ed9)NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN

| #define NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_PASSIVE\_SCAN) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-SCAN(PASSIVE, ...) request.

See [ieee802154\_req\_params](structieee802154__req__params.md "ieee802154_req_params") for associated command parameters.

## [◆ ](#ga9fb911bed94845e723d686ded38929da)NET\_REQUEST\_IEEE802154\_SET\_ACK

| #define NET\_REQUEST\_IEEE802154\_SET\_ACK   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_ACK) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

Sets AckTx for all subsequent MLME-DATA (aka TX) requests.

## [◆ ](#ga5cc7d53ae273c9977de07305efbc0ced)NET\_REQUEST\_IEEE802154\_SET\_CHANNEL

| #define NET\_REQUEST\_IEEE802154\_SET\_CHANNEL   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_CHANNEL) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-SET(phyCurrentChannel) request.

## [◆ ](#gadfb408432bfd2f58eea8d695747471e9)NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR

| #define NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_EXT\_ADDR) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

Sets the extended interface address (non-standard), see sections 7.1 and 8.4.3.1, in big endian byte order.

## [◆ ](#ga9428b28728e2060586761e1f08cf983c)NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID

| #define NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_PAN\_ID) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-SET(macPanId) request.

## [◆ ](#ga907b00f07cdbe9fe33e19ec323d56654)NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS

| #define NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_SECURITY\_SETTINGS) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

Configures basic sec\* MAC PIB attributes, implies macSecurityEnabled=true.

See [ieee802154\_security\_params](structieee802154__security__params.md "ieee802154_security_params") for associated command parameters.

## [◆ ](#ga9b5411f4d458421c0528e0e850c54465)NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR

| #define NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_SHORT\_ADDR) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-SET(macShortAddress) request, only allowed for co-ordinators.

## [◆ ](#ga4399c84db1c15406685d218a2e1190f4)NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER

| #define NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_TX\_POWER) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

MLME-GET(phyUnicastTxPower/phyBroadcastTxPower) request.

## [◆ ](#gafa484eb90d0c8d3d7ef01b5a7edb2a18)NET\_REQUEST\_IEEE802154\_UNSET\_ACK

| #define NET\_REQUEST\_IEEE802154\_UNSET\_ACK   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_UNSET\_ACK) |
| --- |

`#include <[ieee802154_mgmt.h](ieee802154__mgmt_8h.md)>`

Unsets AckTx for all subsequent MLME-DATA requests.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
