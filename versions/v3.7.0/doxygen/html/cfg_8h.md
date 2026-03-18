---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/cfg_8h.html
original_path: doxygen/html/cfg_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cfg.h File Reference

Runtime configuration APIs.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`

[Go to the source code of this file.](cfg_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_KR\_NORMAL](group__bt__mesh__cfg.md#ga5b3af48dfe15948654b7791d7a684ba8)   0x00 |
| #define | [BT\_MESH\_KR\_PHASE\_1](group__bt__mesh__cfg.md#ga139d621ce45ea87b4d8a15fc2b29dbe3)   0x01 |
| #define | [BT\_MESH\_KR\_PHASE\_2](group__bt__mesh__cfg.md#gaff6e8f59719f341ab681268e421b1612)   0x02 |
| #define | [BT\_MESH\_KR\_PHASE\_3](group__bt__mesh__cfg.md#gab0e65cdc2b152d3b84615223fdaebb2e)   0x03 |
| #define | [BT\_MESH\_RELAY\_DISABLED](group__bt__mesh__cfg.md#gaafd10319da7d2f938207b8fd6de02dbc)   [BT\_MESH\_FEATURE\_DISABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_RELAY\_ENABLED](group__bt__mesh__cfg.md#gae5d235a7c182a8add961d7ce344f87aa)   [BT\_MESH\_FEATURE\_ENABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_RELAY\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gabbbbddd31c2a92256fe2f7a7520e76f7)   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| #define | [BT\_MESH\_BEACON\_DISABLED](group__bt__mesh__cfg.md#ga8fa3d0ac3cb9f69464c4068ca61689b9)   [BT\_MESH\_FEATURE\_DISABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_BEACON\_ENABLED](group__bt__mesh__cfg.md#ga01235217559423b93d7e6cf2236278f0)   [BT\_MESH\_FEATURE\_ENABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_PRIV\_BEACON\_DISABLED](group__bt__mesh__cfg.md#ga2645fd9e2aed6de7806e7ac5afd1af10)   [BT\_MESH\_FEATURE\_DISABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_PRIV\_BEACON\_ENABLED](group__bt__mesh__cfg.md#ga1f72ffadff83f30943df88cd1ddcbee8)   [BT\_MESH\_FEATURE\_ENABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_GATT\_PROXY\_DISABLED](group__bt__mesh__cfg.md#ga3fe3e68efd25a3a03a041b978435fd7b)   [BT\_MESH\_FEATURE\_DISABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_GATT\_PROXY\_ENABLED](group__bt__mesh__cfg.md#ga77f4438624aae49ea2bb66437c9623f7)   [BT\_MESH\_FEATURE\_ENABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_GATT\_PROXY\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gaecec3747198a29dd10185e3755e660f8)   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| #define | [BT\_MESH\_PRIV\_GATT\_PROXY\_DISABLED](group__bt__mesh__cfg.md#ga475302ad8ba5589c7ea95da36f18948e)   [BT\_MESH\_FEATURE\_DISABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_PRIV\_GATT\_PROXY\_ENABLED](group__bt__mesh__cfg.md#gac73cdadfd9c9417a051739bce59960a7)   [BT\_MESH\_FEATURE\_ENABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_PRIV\_GATT\_PROXY\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#ga66b4ed203ecbc9a70620b5adff04110f)   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| #define | [BT\_MESH\_FRIEND\_DISABLED](group__bt__mesh__cfg.md#ga29fe48989e760438f2c5241110134c8c)   [BT\_MESH\_FEATURE\_DISABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_FRIEND\_ENABLED](group__bt__mesh__cfg.md#gaa23bba212dc1b322651723ca20f497a3)   [BT\_MESH\_FEATURE\_ENABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_FRIEND\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#ga35f85e6a9c085cdad4f70b8e60d0b027)   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| #define | [BT\_MESH\_NODE\_IDENTITY\_STOPPED](group__bt__mesh__cfg.md#ga9a83214cdbd34ac1d4bc644136523bd9)   [BT\_MESH\_FEATURE\_DISABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_NODE\_IDENTITY\_RUNNING](group__bt__mesh__cfg.md#ga86e88acc6fdcc26a9cea4415daad016c)   [BT\_MESH\_FEATURE\_ENABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_NODE\_IDENTITY\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#ga7ffe6722b12a8663518b4e17349e4da5)   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) { [BT\_MESH\_FEATURE\_DISABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) , [BT\_MESH\_FEATURE\_ENABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) , [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) } |
|  | Bluetooth Mesh feature states. [More...](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) |

| Functions | |
| --- | --- |
| void | [bt\_mesh\_beacon\_set](group__bt__mesh__cfg.md#ga15de1cdc964628b6f001ef893021ce6e) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) beacon) |
|  | Enable or disable sending of the Secure Network Beacon. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_beacon\_enabled](group__bt__mesh__cfg.md#ga479c14f6b0d4a08ddf5b160fa9267844) (void) |
|  | Get the current Secure Network Beacon state. |
| int | [bt\_mesh\_priv\_beacon\_set](group__bt__mesh__cfg.md#ga1afc5ec210bbc6090ada922ddf75e284) (enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) priv\_beacon) |
|  | Enable or disable sending of the Mesh Private beacon. |
| enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) | [bt\_mesh\_priv\_beacon\_get](group__bt__mesh__cfg.md#ga2c8dc9ee5c3862790efd2a74a1ef6873) (void) |
|  | Get the current Mesh Private beacon state. |
| void | [bt\_mesh\_priv\_beacon\_update\_interval\_set](group__bt__mesh__cfg.md#ga01abb07d27edef40ffff4da968065c1d) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval) |
|  | Set the current Mesh Private beacon update interval. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_priv\_beacon\_update\_interval\_get](group__bt__mesh__cfg.md#gafe3d54c1546b03cebbecaf762ae87781) (void) |
|  | Get the current Mesh Private beacon update interval. |
| int | [bt\_mesh\_default\_ttl\_set](group__bt__mesh__cfg.md#gaafea57625c9fdba535431cc92dadd162) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) default\_ttl) |
|  | Set the default TTL value. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_default\_ttl\_get](group__bt__mesh__cfg.md#gaa97f63f5b3167c672fa1a0d8c8fe9ab7) (void) |
|  | Get the current default TTL value. |
| int | [bt\_mesh\_od\_priv\_proxy\_get](group__bt__mesh__cfg.md#ga256d00139ca40eb99303fef766a3add7) (void) |
|  | Get the current Mesh On-Demand Private Proxy state. |
| int | [bt\_mesh\_od\_priv\_proxy\_set](group__bt__mesh__cfg.md#ga26023b727e1b180263b22d0ade145f81) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) on\_demand\_proxy) |
|  | Set state of Mesh On-Demand Private Proxy. |
| void | [bt\_mesh\_net\_transmit\_set](group__bt__mesh__cfg.md#gaa652e4f1460f62252065ac21854ab3f6) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xmit) |
|  | Set the Network Transmit parameters. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_net\_transmit\_get](group__bt__mesh__cfg.md#ga08b336fa1a4a721ac9b10fbb75e4af6b) (void) |
|  | Get the current Network Transmit parameters. |
| int | [bt\_mesh\_relay\_set](group__bt__mesh__cfg.md#gad8d6773753b80540b2aaa982c1ec8c03) (enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) relay, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xmit) |
|  | Configure the Relay feature. |
| enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) | [bt\_mesh\_relay\_get](group__bt__mesh__cfg.md#gadb41d2f78a490aa81b5640bb7ff5a5ce) (void) |
|  | Get the current Relay feature state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_relay\_retransmit\_get](group__bt__mesh__cfg.md#gaf9abf4bcba55d273a7e6e8ee42c521a9) (void) |
|  | Get the current Relay Retransmit parameters. |
| int | [bt\_mesh\_gatt\_proxy\_set](group__bt__mesh__cfg.md#gaac543b57580f9ac8dff36c0ce1196144) (enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) gatt\_proxy) |
|  | Enable or disable the GATT Proxy feature. |
| enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) | [bt\_mesh\_gatt\_proxy\_get](group__bt__mesh__cfg.md#ga8457f222211bc812106b2dccc87b1abe) (void) |
|  | Get the current GATT Proxy state. |
| int | [bt\_mesh\_priv\_gatt\_proxy\_set](group__bt__mesh__cfg.md#ga346244dcc70afe3a85e85c28c56b4f49) (enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) priv\_gatt\_proxy) |
|  | Enable or disable the Private GATT Proxy feature. |
| enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) | [bt\_mesh\_priv\_gatt\_proxy\_get](group__bt__mesh__cfg.md#ga037375c99abb492d30378deca183071d) (void) |
|  | Get the current Private GATT Proxy state. |
| int | [bt\_mesh\_friend\_set](group__bt__mesh__cfg.md#ga74b79bc6a15c35ef399e7d5f7c4d26e6) (enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) friendship) |
|  | Enable or disable the Friend feature. |
| enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) | [bt\_mesh\_friend\_get](group__bt__mesh__cfg.md#gac7b1f1208659c80956e6dab6ac0ebc47) (void) |
|  | Get the current Friend state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_add](group__bt__mesh__cfg__subnet.md#ga6a6ba6ac1dcbe5f6cfce9bbf38c1851f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16]) |
|  | Add a Subnet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_update](group__bt__mesh__cfg__subnet.md#ga47236f48940303be27fa6af4797424c2) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16]) |
|  | Update the given Subnet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_del](group__bt__mesh__cfg__subnet.md#gaec9d827d5f026b473f3ac88988d3c842) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Delete a Subnet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_subnet\_exists](group__bt__mesh__cfg__subnet.md#gad48780acaae085350a8b48d033717bfa) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Check whether a Subnet is known. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_kr\_phase\_set](group__bt__mesh__cfg__subnet.md#gaef15af43e74e3c71590c63c5f1e3ea55) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*phase) |
|  | Set the Subnet's Key Refresh phase. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_kr\_phase\_get](group__bt__mesh__cfg__subnet.md#gad251907892150649f3f1ae6b4112cd84) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*phase) |
|  | Get the Subnet's Key Refresh phase. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_node\_id\_set](group__bt__mesh__cfg__subnet.md#ga59bf9f022665edc0ad03267e4bd16632) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) node\_id) |
|  | Set the Node Identity state of the Subnet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_node\_id\_get](group__bt__mesh__cfg__subnet.md#ga683d1f9abe82649a774b3d53dcaced8e) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) \*node\_id) |
|  | Get the Node Identity state of the Subnet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_priv\_node\_id\_set](group__bt__mesh__cfg__subnet.md#ga5aa3e7f6b64e1b8b98f9737606d5d1ec) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) priv\_node\_id) |
|  | Set the Private Node Identity state of the Subnet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_priv\_node\_id\_get](group__bt__mesh__cfg__subnet.md#ga555b4a7127869355fdf6040b8d14f999) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) \*priv\_node\_id) |
|  | Get the Private Node Identity state of the Subnet. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_mesh\_subnets\_get](group__bt__mesh__cfg__subnet.md#ga0fd04bff5423a36b013089a4ba351d67) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idxs[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) skip) |
|  | Get a list of all known Subnet indexes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_app\_key\_add](group__bt__mesh__cfg__app.md#ga0110ef750489af49a156a259c5a95c9b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16]) |
|  | Add an Application key. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_app\_key\_update](group__bt__mesh__cfg__app.md#ga5ae73ef766f0e1c38c0414c0a34e4053) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16]) |
|  | Update an Application key. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_app\_key\_del](group__bt__mesh__cfg__app.md#gaa0e80a19c14d47808fc11459bf5ea2eb) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Delete an Application key. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_app\_key\_exists](group__bt__mesh__cfg__app.md#ga42c46a936e589460225a1fa69598a1ac) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx) |
|  | Check if an Application key is known. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_mesh\_app\_keys\_get](group__bt__mesh__cfg__app.md#gad7a949a0a814f6c9a26816c076d8b92a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idxs[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) skip) |
|  | Get a list of all known Application key indexes. |

## Detailed Description

Runtime configuration APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [cfg.h](cfg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
