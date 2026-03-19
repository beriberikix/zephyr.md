---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ieee802154__mgmt_8h.html
original_path: doxygen/html/ieee802154__mgmt_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_mgmt.h File Reference

IEEE 802.15.4 Management interface public header.
[More...](#details)

`#include <[zephyr/net/ieee802154.h](ieee802154_8h_source.md)>`  
`#include <[zephyr/net/net_mgmt.h](net__mgmt_8h_source.md)>`

[Go to the source code of this file.](ieee802154__mgmt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ieee802154\_req\_params](structieee802154__req__params.md) |
|  | Scanning parameters. [More...](structieee802154__req__params.md#details) |
| struct | [ieee802154\_security\_params](structieee802154__security__params.md) |
|  | Security parameters. [More...](structieee802154__security__params.md#details) |

| Macros | |
| --- | --- |
| Command Macros | |
| IEEE 802.15.4 net management commands.  These IEEE 802.15.4 subsystem net management commands can be called by applications via [Network Management](group__net__mgmt.md "Network Management") macro.  All attributes and parameters are given in CPU byte order (scalars) or big endian (byte arrays) unless otherwise specified.  The following IEEE 802.15.4 MAC management service primitives are referenced in this enumeration:   - MLME-ASSOCIATE.request, see section 8.2.3 - MLME-DISASSOCIATE.request, see section 8.2.4 - MLME-SET/GET.request, see section 8.2.6 - MLME-SCAN.request, see section 8.2.11   The following IEEE 802.15.4 MAC data service primitives are referenced in this enumeration:   - MLME-DATA.request, see section 8.3.2   MAC PIB attributes (mac.../sec...): see sections 8.4.3 and 9.5. PHY PIB attributes (phy...): see section 11.3. Both are accessed through MLME-SET/GET primitives. | |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_ACK](group__ieee802154__mgmt.md#ga9fb911bed94845e723d686ded38929da)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_ACK) |
|  | Sets AckTx for all subsequent MLME-DATA (aka TX) requests. |
| #define | [NET\_REQUEST\_IEEE802154\_UNSET\_ACK](group__ieee802154__mgmt.md#gafa484eb90d0c8d3d7ef01b5a7edb2a18)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_UNSET\_ACK) |
|  | Unsets AckTx for all subsequent MLME-DATA requests. |
| #define | [NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN](group__ieee802154__mgmt.md#ga72d022935a39436e95f61cceb8001ed9)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_PASSIVE\_SCAN) |
|  | MLME-SCAN(PASSIVE, ...) request. |
| #define | [NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN](group__ieee802154__mgmt.md#gab7ad1a0db3c9a361eab52e0cf484d11b)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_ACTIVE\_SCAN) |
|  | MLME-SCAN(ACTIVE, ...) request. |
| #define | [NET\_REQUEST\_IEEE802154\_CANCEL\_SCAN](group__ieee802154__mgmt.md#gaefba66b873c90b3db1ad9bfce98ceebe)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_CANCEL\_SCAN) |
|  | Cancels an ongoing MLME-SCAN(...) command (non-standard). |
| #define | [NET\_REQUEST\_IEEE802154\_ASSOCIATE](group__ieee802154__mgmt.md#ga01e2180457cd99095e56ae3fa9f79dbf)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_ASSOCIATE) |
|  | MLME-ASSOCIATE(...) request. |
| #define | [NET\_REQUEST\_IEEE802154\_DISASSOCIATE](group__ieee802154__mgmt.md#gace7c47eba4e022f54000932814ce4edd)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_DISASSOCIATE) |
|  | MLME-DISASSOCIATE(...) request. |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_CHANNEL](group__ieee802154__mgmt.md#ga5cc7d53ae273c9977de07305efbc0ced)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_CHANNEL) |
|  | MLME-SET(phyCurrentChannel) request. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_CHANNEL](group__ieee802154__mgmt.md#gad154b4b5affb3a8a59226a241c84a14b)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_CHANNEL) |
|  | MLME-GET(phyCurrentChannel) request. |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_PAN\_ID](group__ieee802154__mgmt.md#ga9428b28728e2060586761e1f08cf983c)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_PAN\_ID) |
|  | MLME-SET(macPanId) request. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_PAN\_ID](group__ieee802154__mgmt.md#ga8a0a0c9c6b3762ebe06df860aee9431f)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_PAN\_ID) |
|  | MLME-GET(macPanId) request. |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_EXT\_ADDR](group__ieee802154__mgmt.md#gadfb408432bfd2f58eea8d695747471e9)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_EXT\_ADDR) |
|  | Sets the extended interface address (non-standard), see sections 7.1 and 8.4.3.1, in big endian byte order. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_EXT\_ADDR](group__ieee802154__mgmt.md#gaf64388508d21c5a17896c82ef1e3ac66)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_EXT\_ADDR) |
|  | like MLME-GET(macExtendedAddress) but in big endian byte order |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_SHORT\_ADDR](group__ieee802154__mgmt.md#ga9b5411f4d458421c0528e0e850c54465)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_SHORT\_ADDR) |
|  | MLME-SET(macShortAddress) request, only allowed for co-ordinators. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_SHORT\_ADDR](group__ieee802154__mgmt.md#ga60b38fa4a0a1248e5e491cd7b2b85241)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_SHORT\_ADDR) |
|  | MLME-GET(macShortAddress) request. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_TX\_POWER](group__ieee802154__mgmt.md#ga07062abc2ce8ebb326e89bee768c3638)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_TX\_POWER) |
|  | MLME-SET(phyUnicastTxPower/phyBroadcastTxPower) request (currently not distinguished). |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_TX\_POWER](group__ieee802154__mgmt.md#ga4399c84db1c15406685d218a2e1190f4)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_TX\_POWER) |
|  | MLME-GET(phyUnicastTxPower/phyBroadcastTxPower) request. |
| #define | [NET\_REQUEST\_IEEE802154\_SET\_SECURITY\_SETTINGS](group__ieee802154__mgmt.md#ga907b00f07cdbe9fe33e19ec323d56654)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_SET\_SECURITY\_SETTINGS) |
|  | Configures basic sec\* MAC PIB attributes, implies macSecurityEnabled=true. |
| #define | [NET\_REQUEST\_IEEE802154\_GET\_SECURITY\_SETTINGS](group__ieee802154__mgmt.md#ga120d2a00dd3ade6d413e1763c41075df)   (\_NET\_IEEE802154\_BASE | NET\_REQUEST\_IEEE802154\_CMD\_GET\_SECURITY\_SETTINGS) |
|  | Gets the configured sec\* attributes. |
| Event Macros | |
| IEEE 802.15.4 net management events.  These IEEE 802.15.4 subsystem net management events can be subscribed to by applications via [net\_mgmt\_init\_event\_callback](group__net__mgmt.md#gaa1d086dcdeb54412073e287129bc50e0 "net_mgmt_init_event_callback"), [net\_mgmt\_add\_event\_callback](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f "net_mgmt_add_event_callback") and [net\_mgmt\_del\_event\_callback](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946 "net_mgmt_del_event_callback"). | |
| #define | [NET\_EVENT\_IEEE802154\_SCAN\_RESULT](group__ieee802154__mgmt.md#ga0442eaa04068a7b66f9b4ae40b570470)   (\_NET\_IEEE802154\_EVENT | NET\_EVENT\_IEEE802154\_CMD\_SCAN\_RESULT) |
|  | Signals the result of the [NET\_REQUEST\_IEEE802154\_ACTIVE\_SCAN](group__ieee802154__mgmt.md#gab7ad1a0db3c9a361eab52e0cf484d11b "NET_REQUEST_IEEE802154_ACTIVE_SCAN") or [NET\_REQUEST\_IEEE802154\_PASSIVE\_SCAN](group__ieee802154__mgmt.md#ga72d022935a39436e95f61cceb8001ed9 "NET_REQUEST_IEEE802154_PASSIVE_SCAN") net management commands. |

## Detailed Description

IEEE 802.15.4 Management interface public header.

Note
:   All references to the standard in this file cite IEEE 802.15.4-2020.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154\_mgmt.h](ieee802154__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
