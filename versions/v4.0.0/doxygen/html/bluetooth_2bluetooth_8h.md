---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/bluetooth_2bluetooth_8h.html
original_path: doxygen/html/bluetooth_2bluetooth_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bluetooth.h File Reference

Bluetooth subsystem core APIs.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/gap.h](gap_8h_source.md)>`  
`#include <[zephyr/bluetooth/addr.h](addr_8h_source.md)>`  
`#include <[zephyr/bluetooth/crypto.h](bluetooth_2crypto_8h_source.md)>`  
`#include <[zephyr/bluetooth/classic/classic.h](classic_8h_source.md)>`

[Go to the source code of this file.](bluetooth_2bluetooth_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md) |
| struct | [bt\_le\_ext\_adv\_connected\_info](structbt__le__ext__adv__connected__info.md) |
| struct | [bt\_le\_ext\_adv\_scanned\_info](structbt__le__ext__adv__scanned__info.md) |
| struct | [bt\_le\_per\_adv\_data\_request](structbt__le__per__adv__data__request.md) |
| struct | [bt\_le\_per\_adv\_response\_info](structbt__le__per__adv__response__info.md) |
| struct | [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md) |
| struct | [bt\_data](structbt__data.md) |
|  | Bluetooth data. [More...](structbt__data.md#details) |
| struct | [bt\_le\_adv\_param](structbt__le__adv__param.md) |
|  | LE Advertising Parameters. [More...](structbt__le__adv__param.md#details) |
| struct | [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md) |
| struct | [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md) |
| struct | [bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md) |
|  | Advertising set info structure. [More...](structbt__le__ext__adv__info.md#details) |
| struct | [bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md) |
| struct | [bt\_le\_per\_adv\_sync\_synced\_info](structbt__le__per__adv__sync__synced__info.md) |
| struct | [bt\_le\_per\_adv\_sync\_term\_info](structbt__le__per__adv__sync__term__info.md) |
| struct | [bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md) |
| struct | [bt\_le\_per\_adv\_sync\_state\_info](structbt__le__per__adv__sync__state__info.md) |
| struct | [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md) |
| struct | [bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md) |
| struct | [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md) |
|  | Advertising set info structure. [More...](structbt__le__per__adv__sync__info.md#details) |
| struct | [bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md) |
| struct | [bt\_le\_scan\_param](structbt__le__scan__param.md) |
|  | LE scan parameters. [More...](structbt__le__scan__param.md#details) |
| struct | [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md) |
|  | LE advertisement and scan response packet information. [More...](structbt__le__scan__recv__info.md#details) |
| struct | [bt\_le\_scan\_cb](structbt__le__scan__cb.md) |
|  | Listener context for (LE) scanning. [More...](structbt__le__scan__cb.md#details) |
| struct | [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) |
|  | LE Secure Connections pairing Out of Band data. [More...](structbt__le__oob__sc__data.md#details) |
| struct | [bt\_le\_oob](structbt__le__oob.md) |
|  | LE Out of Band information. [More...](structbt__le__oob.md#details) |
| struct | [bt\_bond\_info](structbt__bond__info.md) |
|  | Information about a bond with a remote device. [More...](structbt__bond__info.md#details) |
| struct | [bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md) |
| struct | [bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md) |

| Macros | |
| --- | --- |
| #define | [BT\_ID\_DEFAULT](group__bt__gap.md#gaded4b52c9bb87fd4d19b1eb9361973e5)   0 |
|  | Convenience macro for specifying the default identity. |
| #define | [BT\_DATA\_SERIALIZED\_SIZE](group__bt__gap.md#ga7357d34bf295a16d8288df3bf75e7976)(data\_len) |
|  | Bluetooth data serialized size. |
| #define | [BT\_DATA](group__bt__gap.md#ga8481217e632522e1f322de87d745f8f0)(\_type, \_data, \_data\_len) |
|  | Helper to declare elements of [bt\_data](structbt__data.md "Bluetooth data.") arrays. |
| #define | [BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)(\_type, \_bytes...) |
|  | Helper to declare elements of [bt\_data](structbt__data.md "Bluetooth data.") arrays. |
| #define | [BT\_LE\_ADV\_PARAM\_INIT](group__bt__gap.md#ga71555b857cf8c2a47c36e4dafa7accf4)(\_options, \_int\_min, \_int\_max, \_peer) |
|  | Initialize advertising parameters. |
| #define | [BT\_LE\_ADV\_PARAM](group__bt__gap.md#ga9557269dd36b624b49e76c511c3a0cc1)(\_options, \_int\_min, \_int\_max, \_peer) |
|  | Helper to declare advertising parameters inline. |
| #define | [BT\_LE\_ADV\_CONN\_DIR](group__bt__gap.md#ga1f5edc3c4cbead62e32cef8cc7b83725)(\_peer) |
| #define | [BT\_LE\_ADV\_CONN](group__bt__gap.md#gad490487b9e196526a13fe249a4c25448) |
| #define | [BT\_LE\_ADV\_CONN\_FAST\_1](group__bt__gap.md#gaa700527b1caf3bef27d96a3f91a29f69) |
|  | GAP recommended connectable advertising. |
| #define | [BT\_LE\_ADV\_CONN\_FAST\_2](group__bt__gap.md#ga684a1110a8973bc17211f6f0824beccd) |
|  | Connectable advertising with T\_GAP(adv\_fast\_interval2). |
| #define | [BT\_LE\_ADV\_CONN\_ONE\_TIME](group__bt__gap.md#gac0430ab5a40a49b3281dd6ff8a7e7378)   [BT\_LE\_ADV\_CONN\_FAST\_2](group__bt__gap.md#ga684a1110a8973bc17211f6f0824beccd) \_\_DEPRECATED\_MACRO |
| #define | [BT\_LE\_ADV\_CONN\_NAME](group__bt__gap.md#ga7b29dba3d892186897c5b4ca5adfd2e3) |
| #define | [BT\_LE\_ADV\_CONN\_NAME\_AD](group__bt__gap.md#ga213307090f1debdc783c54faf4a36740) |
| #define | [BT\_LE\_ADV\_CONN\_DIR\_LOW\_DUTY](group__bt__gap.md#gab89e033ed3fd116c94120d177dfdc839)(\_peer) |
| #define | [BT\_LE\_ADV\_NCONN](group__bt__gap.md#ga1610555bf59f1d691d640f245957fdce) |
|  | Non-connectable advertising with private address. |
| #define | [BT\_LE\_ADV\_NCONN\_NAME](group__bt__gap.md#gac1c3c47e3136ce813bb50b00a9387cb4) |
| #define | [BT\_LE\_ADV\_NCONN\_IDENTITY](group__bt__gap.md#ga6ef9fb7a469b03265c7adc99ea19a11b) |
|  | Non-connectable advertising with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e "BT_LE_ADV_OPT_USE_IDENTITY"). |
| #define | [BT\_LE\_EXT\_ADV\_CONN](group__bt__gap.md#gaeaaef4dede5d45251dfe12f329e070b7) |
|  | Connectable extended advertising. |
| #define | [BT\_LE\_EXT\_ADV\_CONN\_NAME](group__bt__gap.md#gac4880197cbe21aad78c4edf10cde95da) |
| #define | [BT\_LE\_EXT\_ADV\_SCAN](group__bt__gap.md#ga5dd57fc7f0e213db08655e631a2f314e) |
|  | Scannable extended advertising. |
| #define | [BT\_LE\_EXT\_ADV\_SCAN\_NAME](group__bt__gap.md#ga3e4abd3691e2c6d95acd21b9ca566edd) |
| #define | [BT\_LE\_EXT\_ADV\_NCONN](group__bt__gap.md#gaabc0385f6a5307b48ec43af6aae7dea6) |
|  | Non-connectable extended advertising with private address. |
| #define | [BT\_LE\_EXT\_ADV\_NCONN\_NAME](group__bt__gap.md#ga5c79af6787ccda890f485a45c931cdc8) |
| #define | [BT\_LE\_EXT\_ADV\_NCONN\_IDENTITY](group__bt__gap.md#ga7e46a64af0036c433c2e940ce7db0a05) |
|  | Non-connectable extended advertising with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e "BT_LE_ADV_OPT_USE_IDENTITY"). |
| #define | [BT\_LE\_EXT\_ADV\_CODED\_NCONN](group__bt__gap.md#ga0e911d3aafdd0c926590b3272a3da564) |
|  | Non-connectable extended advertising on coded PHY with private address. |
| #define | [BT\_LE\_EXT\_ADV\_CODED\_NCONN\_NAME](group__bt__gap.md#ga8c6027f7c0888c577f9b61a65104be05) |
| #define | [BT\_LE\_EXT\_ADV\_CODED\_NCONN\_IDENTITY](group__bt__gap.md#gac67c52693154ebbeedbb31e100513812) |
|  | Non-connectable extended advertising on coded PHY with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e "BT_LE_ADV_OPT_USE_IDENTITY"). |
| #define | [BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT](group__bt__gap.md#gaf0d4c5b05deb5466a0e29c153263b489)(\_timeout, \_n\_evts) |
|  | Helper to initialize extended advertising start parameters inline. |
| #define | [BT\_LE\_EXT\_ADV\_START\_PARAM](group__bt__gap.md#ga9b2cefbcb0a85116cadb68f6d80c6429)(\_timeout, \_n\_evts) |
|  | Helper to declare extended advertising start parameters inline. |
| #define | [BT\_LE\_EXT\_ADV\_START\_DEFAULT](group__bt__gap.md#ga8c83a6f322a479bc24a576a7f091312e)   [BT\_LE\_EXT\_ADV\_START\_PARAM](group__bt__gap.md#ga9b2cefbcb0a85116cadb68f6d80c6429)(0, 0) |
| #define | [BT\_LE\_PER\_ADV\_PARAM\_INIT](group__bt__gap.md#ga880567278a81098ae55f52f624c61041)(\_int\_min, \_int\_max, \_options) |
|  | Helper to declare periodic advertising parameters inline. |
| #define | [BT\_LE\_PER\_ADV\_PARAM](group__bt__gap.md#gaf46e54f8fcda7b65b659685bb225d243)(\_int\_min, \_int\_max, \_options) |
|  | Helper to declare periodic advertising parameters inline. |
| #define | [BT\_LE\_PER\_ADV\_DEFAULT](group__bt__gap.md#ga8f6a00faaaab2a91ac943c71ed041ac1) |
| #define | [BT\_LE\_SCAN\_OPT\_FILTER\_WHITELIST](group__bt__gap.md#ga33e84f4ccbf4d0aa2527e9fe1086e252)   \_\_DEPRECATED\_MACRO [BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3af7a25b6790b138b2b88de3c7d81cb0ae) |
| #define | [BT\_LE\_SCAN\_PARAM\_INIT](group__bt__gap.md#gac9f372ca16afb1c2f0e100c5b1b94cd5)(\_type, \_options, \_interval, \_window) |
|  | Initialize scan parameters. |
| #define | [BT\_LE\_SCAN\_PARAM](group__bt__gap.md#ga57ace75133343ba8de7fa965f452ee3d)(\_type, \_options, \_interval, \_window) |
|  | Helper to declare scan parameters inline. |
| #define | [BT\_LE\_SCAN\_ACTIVE](group__bt__gap.md#gac137ea4ce32697582a337116ffa41da5) |
|  | Helper macro to enable active scanning to discover new devices. |
| #define | [BT\_LE\_SCAN\_ACTIVE\_CONTINUOUS](group__bt__gap.md#ga9bd9701db0459c066ed7c18343f60911) |
|  | Helper macro to enable active scanning to discover new devices with window == interval. |
| #define | [BT\_LE\_SCAN\_PASSIVE](group__bt__gap.md#ga8ceaef6f0fbf4fe2d76d47e8f59aeb11) |
|  | Helper macro to enable passive scanning to discover new devices. |
| #define | [BT\_LE\_SCAN\_PASSIVE\_CONTINUOUS](group__bt__gap.md#ga8d8ccc9ea1db2c96deae1603ec1c78a3) |
|  | Helper macro to enable passive scanning to discover new devices with window==interval. |
| #define | [BT\_LE\_SCAN\_CODED\_ACTIVE](group__bt__gap.md#ga06380c4ae6289c704a143b9d192bc35f) |
|  | Helper macro to enable active scanning to discover new devices. |
| #define | [BT\_LE\_SCAN\_CODED\_PASSIVE](group__bt__gap.md#ga1e5a4589304babc6b0d49019ebcff6b0) |
|  | Helper macro to enable passive scanning to discover new devices. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_ready\_cb\_t](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb)) (int err) |
|  | Callback for notifying that Bluetooth has been enabled. |
| typedef void | [bt\_le\_scan\_cb\_t](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) rssi, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adv\_type, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback type for reporting LE scan results. |

| Enumerations | |
| --- | --- |
| enum | {     [BT\_LE\_ADV\_OPT\_NONE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea928b376123819cb0a69fbb5b35608dbf) = 0 , [BT\_LE\_ADV\_OPT\_CONNECTABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) = BIT(0) , **\_BT\_LE\_ADV\_OPT\_CONNECTABLE** = BIT(0) , [BT\_LE\_ADV\_OPT\_ONE\_TIME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2) = BIT(1) ,     **\_BT\_LE\_ADV\_OPT\_ONE\_TIME** = BIT(1) , [BT\_LE\_ADV\_OPT\_CONN](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169) = BIT(0) | BIT(1) , [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e) = BIT(2) , [BT\_LE\_ADV\_OPT\_USE\_NAME](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398) = BIT(3) ,     [BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeafd164ec5476f5e2d9aedf50032946872) = BIT(4) , [BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabdcf1c80662061fa30575e1f9fc6cf6f) = BIT(5) , [BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea807ba316edc49c8448a8ff7d497173f5) = BIT(6) , [BT\_LE\_ADV\_OPT\_FILTER\_CONN](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead5efef3d01731110dbd71d5a5dc9baaf) = BIT(7) ,     [BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea1563b053f457833d1a3d11c8dc4d394b) = BIT(8) , [BT\_LE\_ADV\_OPT\_SCANNABLE](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) = BIT(9) , [BT\_LE\_ADV\_OPT\_EXT\_ADV](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) = BIT(10) , [BT\_LE\_ADV\_OPT\_NO\_2M](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeae864aefcdfbecaffe823b9b144fe0a6b) = BIT(11) ,     [BT\_LE\_ADV\_OPT\_CODED](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1) = BIT(12) , [BT\_LE\_ADV\_OPT\_ANONYMOUS](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea185e0f884f8b0ce79625448638de8fab) = BIT(13) , [BT\_LE\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaecff4fe3ac3d1fba3f6fa76c77713859) = BIT(14) , [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeab46741616f8bfe50c4b492d1f7970779) = BIT(15) ,     [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeabd9cb02691d7e025fe3fea9a80123275) = BIT(16) , [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea89f7494620236c976bf1a76a880e2a28) = BIT(17) , [BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73) = BIT(18) , [BT\_LE\_ADV\_OPT\_USE\_NRPA](group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea22958d8539d661ad7ca8d3f1173e7e5e) = BIT(19)   } |
|  | Advertising options. [More...](group__bt__gap.md#ga654b0098c5f04a9c85a65f86b8f95dee) |
| enum | { [BT\_LE\_PER\_ADV\_OPT\_NONE](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aaa2c689d726eacfb18d87655b1f587518) = 0 , [BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa9524537e4cb726f4ff10ba93381bb27f) = BIT(1) , [BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI](group__bt__gap.md#gga592195c57b12f7224b6d07133e60fc4aa38cebc2ae885ff630b34c603e2ec6403) = BIT(2) } |
|  | Periodic Advertising options. [More...](group__bt__gap.md#ga592195c57b12f7224b6d07133e60fc4a) |
| enum | {     [BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaeeef50a544edc104b39e4ef0c9a58d6c) = 0 , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae9a88caa6a83da8b1697a6167629bf7e) = BIT(0) , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaae35a6eb572a2842e4cc2fc3677e19b53) = BIT(1) , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa9ec2b0c346c2cab7f61c2efcc8e37db2) = BIT(2) ,     [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaaaa256e560f013eb74415d817154b8f4e) = BIT(3) , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa99034652a92249e6d04065d68352020b) = BIT(4) , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa0f52e38e513ec7eefcbc5c86c36f002e) = BIT(5) , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT](group__bt__gap.md#gga9cf9b0d1941502642e50fcfc2d686bcaa5c702876d70d5eadc4df6e59d96b8320) = BIT(6)   } |
|  | Periodic advertising sync options. [More...](group__bt__gap.md#ga9cf9b0d1941502642e50fcfc2d686bca) |
| enum | {     [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aef90aceabc3f9d0b17b7f3415152fca2) = 0 , [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a2694870b7ebd2dcd0b3834367f7d7061) = BIT(0) , [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ab0725048806858083be9ab3fcd9a36ed) = BIT(1) , [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a433ae469b27e820fdfd2a1d562010991) = BIT(2) ,     [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15aed2f78d682b5fbd1adf89c2f005e4f48) = BIT(3) , [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15a3f0be549ca5cac1cfbdec2f2227e73dc) = BIT(4) , [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES](group__bt__gap.md#gga9c50ffe9d076ca7be5bdd72b91e53e15ad924f620ed6fdadbbea03f8e343b9d0c) = BIT(5)   } |
|  | Periodic Advertising Sync Transfer options. [More...](group__bt__gap.md#ga9c50ffe9d076ca7be5bdd72b91e53e15) |
| enum | {     [BT\_LE\_SCAN\_OPT\_NONE](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3aad3f19e5849b6d6813fa88257082e185) = 0 , [BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394) = BIT(0) , [BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3af7a25b6790b138b2b88de3c7d81cb0ae) = BIT(1) , [BT\_LE\_SCAN\_OPT\_CODED](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb) = BIT(2) ,     [BT\_LE\_SCAN\_OPT\_NO\_1M](group__bt__gap.md#gga5afc3803e9a80e829597375fcf2a2cf3a7ff0c79b2675e7b7512379e2cbedc0a6) = BIT(3)   } |
| enum | { [BT\_LE\_SCAN\_TYPE\_PASSIVE](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006) = 0x00 , [BT\_LE\_SCAN\_TYPE\_ACTIVE](group__bt__gap.md#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22) = 0x01 } |

| Functions | |
| --- | --- |
| int | [bt\_enable](group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b) ([bt\_ready\_cb\_t](group__bt__gap.md#ga5398783ab4a5dc854b18e37fb10774eb) cb) |
|  | Enable Bluetooth. |
| int | [bt\_disable](group__bt__gap.md#ga0a58e5a050170e84a80f8d5bb3516ec7) (void) |
|  | Disable Bluetooth. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_is\_ready](group__bt__gap.md#gaa8bf6854e7ad1fe7e0805737576e5d1a) (void) |
|  | Check if Bluetooth is ready. |
| int | [bt\_set\_name](group__bt__gap.md#gac8bb3609a3d6da69ff736809e45f5c8a) (const char \*name) |
|  | Set Bluetooth Device Name. |
| const char \* | [bt\_get\_name](group__bt__gap.md#gad922d894b25e86de3f81ce77200a13fd) (void) |
|  | Get Bluetooth Device Name. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_get\_appearance](group__bt__gap.md#ga35b76ea7ce79721e47ca4164e08b2dfb) (void) |
|  | Get local Bluetooth appearance. |
| int | [bt\_set\_appearance](group__bt__gap.md#gaf0729453790aab1bd3d52c623be3b35a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) new\_appearance) |
|  | Set local Bluetooth appearance. |
| void | [bt\_id\_get](group__bt__gap.md#ga06d0ae35cbf4382679cc3cfe612cee4d) ([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addrs, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*count) |
|  | Get the currently configured identities. |
| int | [bt\_id\_create](group__bt__gap.md#gae11eb8ad254418c38a0e8689df25a159) ([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*irk) |
|  | Create a new identity. |
| int | [bt\_id\_reset](group__bt__gap.md#gabb3353edc8a3a8d29a0370049b20cbe4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*irk) |
|  | Reset/reclaim an identity for reuse. |
| int | [bt\_id\_delete](group__bt__gap.md#gaf6cd906690a51ebed04bea4f4ef716ff) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) |
|  | Delete an identity. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bt\_data\_get\_len](group__bt__gap.md#ga3d2c6adc42eb9510734630f38d921b9a) (const struct [bt\_data](structbt__data.md) data[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_count) |
|  | Get the total size (in bytes) of a given set of [bt\_data](structbt__data.md "bt_data") structures. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bt\_data\_serialize](group__bt__gap.md#ga3c067b16468ebd17973faeded0fc83c9) (const struct [bt\_data](structbt__data.md) \*input, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*output) |
|  | Serialize a [bt\_data](structbt__data.md "bt_data") struct into an advertising structure (a flat byte array). |
| int | [bt\_le\_adv\_start](group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02) (const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param, const struct [bt\_data](structbt__data.md) \*ad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ad\_len, const struct [bt\_data](structbt__data.md) \*sd, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sd\_len) |
|  | Start advertising. |
| int | [bt\_le\_adv\_update\_data](group__bt__gap.md#ga9a406ebfefac3dd09935a4ae0e317817) (const struct [bt\_data](structbt__data.md) \*ad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ad\_len, const struct [bt\_data](structbt__data.md) \*sd, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sd\_len) |
|  | Update advertising. |
| int | [bt\_le\_adv\_stop](group__bt__gap.md#ga1776e310b9d80898e6b32d50c4fe0b49) (void) |
|  | Stop advertising. |
| int | [bt\_le\_ext\_adv\_create](group__bt__gap.md#gad02b855dd7a26e3910b247fa73f19297) (const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param, const struct [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md) \*cb, struct bt\_le\_ext\_adv \*\*adv) |
|  | Create advertising set. |
| int | [bt\_le\_ext\_adv\_start](group__bt__gap.md#gaf0f436c55482d9429f674303ae3aa815) (struct bt\_le\_ext\_adv \*adv, const struct [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md) \*param) |
|  | Start advertising with the given advertising set. |
| int | [bt\_le\_ext\_adv\_stop](group__bt__gap.md#ga1c864c4b183f9a86c9f70a11471c5b15) (struct bt\_le\_ext\_adv \*adv) |
|  | Stop advertising with the given advertising set. |
| int | [bt\_le\_ext\_adv\_set\_data](group__bt__gap.md#gad731f829b3566be3e56485b2a64f80b1) (struct bt\_le\_ext\_adv \*adv, const struct [bt\_data](structbt__data.md) \*ad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ad\_len, const struct [bt\_data](structbt__data.md) \*sd, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sd\_len) |
|  | Set an advertising set's advertising or scan response data. |
| int | [bt\_le\_ext\_adv\_update\_param](group__bt__gap.md#ga1aabdb81cb1a1841ff0fb91d849123fc) (struct bt\_le\_ext\_adv \*adv, const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param) |
|  | Update advertising parameters. |
| int | [bt\_le\_ext\_adv\_delete](group__bt__gap.md#ga62310a27f7fea925dfcf3abd7c454787) (struct bt\_le\_ext\_adv \*adv) |
|  | Delete advertising set. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_le\_ext\_adv\_get\_index](group__bt__gap.md#gaeb37d6cdd94a04b4cce8bc1e7aae70b4) (struct bt\_le\_ext\_adv \*adv) |
|  | Get array index of an advertising set. |
| int | [bt\_le\_ext\_adv\_get\_info](group__bt__gap.md#gac06c9f55cf1da46e0d64b4d9af984ecb) (const struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md) \*info) |
|  | Get advertising set info. |
| int | [bt\_le\_per\_adv\_set\_param](group__bt__gap.md#gaa72029a2759123ec776061d2e80bf3a1) (struct bt\_le\_ext\_adv \*adv, const struct [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md) \*param) |
|  | Set or update the periodic advertising parameters. |
| int | [bt\_le\_per\_adv\_set\_data](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899) (const struct bt\_le\_ext\_adv \*adv, const struct [bt\_data](structbt__data.md) \*ad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ad\_len) |
|  | Set or update the periodic advertising data. |
| int | [bt\_le\_per\_adv\_set\_subevent\_data](group__bt__gap.md#ga7de30fe5040b85bb9212e3a8fec4ac45) (const struct bt\_le\_ext\_adv \*adv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents, const struct [bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md) \*params) |
|  | Set the periodic advertising with response subevent data. |
| int | [bt\_le\_per\_adv\_start](group__bt__gap.md#ga0f23f4ed48e8679646f247ea0d687094) (struct bt\_le\_ext\_adv \*adv) |
|  | Starts periodic advertising. |
| int | [bt\_le\_per\_adv\_stop](group__bt__gap.md#ga1b15206fc552d597c12af369d48ff7d5) (struct bt\_le\_ext\_adv \*adv) |
|  | Stops periodic advertising. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_le\_per\_adv\_sync\_get\_index](group__bt__gap.md#ga8d05bd864d98b5b43595eb256e464024) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync) |
|  | Get array index of an periodic advertising sync object. |
| struct bt\_le\_per\_adv\_sync \* | [bt\_le\_per\_adv\_sync\_lookup\_index](group__bt__gap.md#ga59532b37412b1b93f81cf5cc1bab0534) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Get a periodic advertising sync object from the array index. |
| int | [bt\_le\_per\_adv\_sync\_get\_info](group__bt__gap.md#gabfaf265a48dd09ea02d114e2023c14a6) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, struct [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md) \*info) |
|  | Get periodic adv sync information. |
| struct bt\_le\_per\_adv\_sync \* | [bt\_le\_per\_adv\_sync\_lookup\_addr](group__bt__gap.md#ga83126917373c0bcaa24964dd1d8bde46) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*adv\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid) |
|  | Look up an existing periodic advertising sync object by advertiser address. |
| int | [bt\_le\_per\_adv\_sync\_create](group__bt__gap.md#ga061bf84b989b2c96ab51d2ca0debb017) (const struct [bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md) \*param, struct bt\_le\_per\_adv\_sync \*\*out\_sync) |
|  | Create a periodic advertising sync object. |
| int | [bt\_le\_per\_adv\_sync\_delete](group__bt__gap.md#gaa0c218ff3c78b26dcfaa726ee30267a6) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync) |
|  | Delete periodic advertising sync. |
| int | [bt\_le\_per\_adv\_sync\_cb\_register](group__bt__gap.md#ga4ee87bbf79e6ac844d14c3dafb2dadf4) (struct [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md) \*cb) |
|  | Register periodic advertising sync callbacks. |
| int | [bt\_le\_per\_adv\_sync\_recv\_enable](group__bt__gap.md#ga07e4510de7e72c6ed6196b3da9fb40be) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync) |
|  | Enables receiving periodic advertising reports for a sync. |
| int | [bt\_le\_per\_adv\_sync\_recv\_disable](group__bt__gap.md#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync) |
|  | Disables receiving periodic advertising reports for a sync. |
| int | [bt\_le\_per\_adv\_sync\_transfer](group__bt__gap.md#gaf81a1dd7a628d1a2f25c6b53b0679809) (const struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, const struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) service\_data) |
|  | Transfer the periodic advertising sync information to a peer device. |
| int | [bt\_le\_per\_adv\_set\_info\_transfer](group__bt__gap.md#gac96199a4e5e6cfb789c1bd1c0e67d6fe) (const struct bt\_le\_ext\_adv \*adv, const struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) service\_data) |
|  | Transfer the information about a periodic advertising set. |
| int | [bt\_le\_per\_adv\_sync\_transfer\_subscribe](group__bt__gap.md#gaa0658bd53df1d5e8e89e13330e4fd0ae) (const struct bt\_conn \*conn, const struct [bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md) \*param) |
|  | Subscribe to periodic advertising sync transfers (PASTs). |
| int | [bt\_le\_per\_adv\_sync\_transfer\_unsubscribe](group__bt__gap.md#ga08f872078045bbef4aca19761f25eeb8) (const struct bt\_conn \*conn) |
|  | Unsubscribe from periodic advertising sync transfers (PASTs). |
| int | [bt\_le\_per\_adv\_list\_add](group__bt__gap.md#ga27c4961f3c7270a7f1caeadb4107854b) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid) |
|  | Add a device to the periodic advertising list. |
| int | [bt\_le\_per\_adv\_list\_remove](group__bt__gap.md#ga100efac4a49984e06202c63c4e5955cd) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid) |
|  | Remove a device from the periodic advertising list. |
| int | [bt\_le\_per\_adv\_list\_clear](group__bt__gap.md#ga5909bd768c23a19a42a660e3b814c981) (void) |
|  | Clear the periodic advertising list. |
| int | [bt\_le\_scan\_start](group__bt__gap.md#gac5e19c26b53a08dadb8efa7ecc692ad6) (const struct [bt\_le\_scan\_param](structbt__le__scan__param.md) \*param, [bt\_le\_scan\_cb\_t](group__bt__gap.md#ga1c53d22b6e2dee38c825c58f3eeee9b4) cb) |
|  | Start (LE) scanning. |
| int | [bt\_le\_scan\_stop](group__bt__gap.md#gaa2de1a1ab523606b36a4c445fb0c3b84) (void) |
|  | Stop (LE) scanning. |
| int | [bt\_le\_scan\_cb\_register](group__bt__gap.md#ga80e870fa1de40c404c64624bef439067) (struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \*cb) |
|  | Register scanner packet callbacks. |
| void | [bt\_le\_scan\_cb\_unregister](group__bt__gap.md#gac2718f2128b3f8c79b12d760771c8378) (struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \*cb) |
|  | Unregister scanner packet callbacks. |
| int | [bt\_le\_filter\_accept\_list\_add](group__bt__gap.md#ga40f2f7fdb09aba3c5137f680e67792f0) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Add device (LE) to filter accept list. |
| int | [bt\_le\_filter\_accept\_list\_remove](group__bt__gap.md#ga0532ed768ab4f9d69c202066d2f87e66) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Remove device (LE) from filter accept list. |
| int | [bt\_le\_filter\_accept\_list\_clear](group__bt__gap.md#gac87df899d1e363c63162988157ee6d00) (void) |
|  | Clear filter accept list. |
| int | [bt\_le\_set\_chan\_map](group__bt__gap.md#gabc115fd3fff6d00ae878a31613bf70aa) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_map[5]) |
|  | Set (LE) channel map. |
| int | [bt\_le\_set\_rpa\_timeout](group__bt__gap.md#ga9ab41e118b5496c196e56b8b5d023275) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) new\_rpa\_timeout) |
|  | Set the Resolvable Private Address timeout in runtime. |
| void | [bt\_data\_parse](group__bt__gap.md#ga652eef01e5256e0d820cd1f4db877429) (struct [net\_buf\_simple](structnet__buf__simple.md) \*ad, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*func)(struct [bt\_data](structbt__data.md) \*data, void \*user\_data), void \*user\_data) |
|  | Helper for parsing advertising (or EIR or OOB) data. |
| int | [bt\_le\_oob\_get\_local](group__bt__gap.md#ga296d1adf3c9ed2f2c65bb75b887d59ee) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, struct [bt\_le\_oob](structbt__le__oob.md) \*oob) |
|  | Get local LE Out of Band (OOB) information. |
| int | [bt\_le\_ext\_adv\_oob\_get\_local](group__bt__gap.md#ga7486aab863ca497a50dacf81657f48d4) (struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_oob](structbt__le__oob.md) \*oob) |
|  | Get local LE Out of Band (OOB) information. |
| int | [bt\_unpair](group__bt__gap.md#gaceabbbe6e844650f791010e53c9df6a4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Clear pairing information. |
| void | [bt\_foreach\_bond](group__bt__gap.md#gaad380b7f8984f8522c1b79f9bdc04905) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, void(\*func)(const struct [bt\_bond\_info](structbt__bond__info.md) \*info, void \*user\_data), void \*user\_data) |
|  | Iterate through all existing bonds. |
| int | [bt\_configure\_data\_path](group__bt__gap.md#ga8046c2b06d3dad0d6c8184de492517d2) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dir, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vs\_config\_len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vs\_config) |
|  | Configure vendor data path. |
| int | [bt\_le\_per\_adv\_sync\_subevent](group__bt__gap.md#ga731f4b37a9e5cc13a6816ea23f751b0b) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, struct [bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md) \*params) |
|  | Synchronize with a subset of subevents. |
| int | [bt\_le\_per\_adv\_set\_response\_data](group__bt__gap.md#gaae6b8583f7d5457f20b03dccd146425e) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, const struct [bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md) \*params, const struct [net\_buf\_simple](structnet__buf__simple.md) \*data) |
|  | Set the data for a response slot in a specific subevent of the PAwR. |

## Detailed Description

Bluetooth subsystem core APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [bluetooth.h](bluetooth_2bluetooth_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
