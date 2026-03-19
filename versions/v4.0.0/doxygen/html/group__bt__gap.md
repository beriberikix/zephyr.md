---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__gap.html
original_path: doxygen/html/group__bt__gap.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Generic Access Profile (GAP)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Generic Access Profile (GAP).
[More...](#details)

| Topics | |
| --- | --- |
|  | [Defines and Assigned Numbers](group__bt__gap__defines.md) |
|  | Bluetooth Generic Access Profile defines and Assigned Numbers. |

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
| struct | [bt\_br\_discovery\_result](structbt__br__discovery__result.md) |
|  | BR/EDR discovery result structure. [More...](structbt__br__discovery__result.md#details) |
| struct | [bt\_br\_discovery\_param](structbt__br__discovery__param.md) |
|  | BR/EDR discovery parameters. [More...](structbt__br__discovery__param.md#details) |
| struct | [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md) |
| struct | [bt\_br\_oob](structbt__br__oob.md) |

| Macros | |
| --- | --- |
| #define | [BT\_ID\_DEFAULT](#gaded4b52c9bb87fd4d19b1eb9361973e5)   0 |
|  | Convenience macro for specifying the default identity. |
| #define | [BT\_DATA\_SERIALIZED\_SIZE](#ga7357d34bf295a16d8288df3bf75e7976)(data\_len) |
|  | Bluetooth data serialized size. |
| #define | [BT\_DATA](#ga8481217e632522e1f322de87d745f8f0)(\_type, \_data, \_data\_len) |
|  | Helper to declare elements of [bt\_data](structbt__data.md "Bluetooth data.") arrays. |
| #define | [BT\_DATA\_BYTES](#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)(\_type, \_bytes...) |
|  | Helper to declare elements of [bt\_data](structbt__data.md "Bluetooth data.") arrays. |
| #define | [BT\_LE\_ADV\_PARAM\_INIT](#ga71555b857cf8c2a47c36e4dafa7accf4)(\_options, \_int\_min, \_int\_max, \_peer) |
|  | Initialize advertising parameters. |
| #define | [BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)(\_options, \_int\_min, \_int\_max, \_peer) |
|  | Helper to declare advertising parameters inline. |
| #define | [BT\_LE\_ADV\_CONN\_DIR](#ga1f5edc3c4cbead62e32cef8cc7b83725)(\_peer) |
| #define | [BT\_LE\_ADV\_CONN](#gad490487b9e196526a13fe249a4c25448) |
| #define | [BT\_LE\_ADV\_CONN\_FAST\_1](#gaa700527b1caf3bef27d96a3f91a29f69) |
|  | GAP recommended connectable advertising. |
| #define | [BT\_LE\_ADV\_CONN\_FAST\_2](#ga684a1110a8973bc17211f6f0824beccd) |
|  | Connectable advertising with T\_GAP(adv\_fast\_interval2). |
| #define | [BT\_LE\_ADV\_CONN\_ONE\_TIME](#gac0430ab5a40a49b3281dd6ff8a7e7378)   [BT\_LE\_ADV\_CONN\_FAST\_2](#ga684a1110a8973bc17211f6f0824beccd) \_\_DEPRECATED\_MACRO |
| #define | [BT\_LE\_ADV\_CONN\_NAME](#ga7b29dba3d892186897c5b4ca5adfd2e3) |
| #define | [BT\_LE\_ADV\_CONN\_NAME\_AD](#ga213307090f1debdc783c54faf4a36740) |
| #define | [BT\_LE\_ADV\_CONN\_DIR\_LOW\_DUTY](#gab89e033ed3fd116c94120d177dfdc839)(\_peer) |
| #define | [BT\_LE\_ADV\_NCONN](#ga1610555bf59f1d691d640f245957fdce) |
|  | Non-connectable advertising with private address. |
| #define | [BT\_LE\_ADV\_NCONN\_NAME](#gac1c3c47e3136ce813bb50b00a9387cb4) |
| #define | [BT\_LE\_ADV\_NCONN\_IDENTITY](#ga6ef9fb7a469b03265c7adc99ea19a11b) |
|  | Non-connectable advertising with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e). |
| #define | [BT\_LE\_EXT\_ADV\_CONN](#gaeaaef4dede5d45251dfe12f329e070b7) |
|  | Connectable extended advertising. |
| #define | [BT\_LE\_EXT\_ADV\_CONN\_NAME](#gac4880197cbe21aad78c4edf10cde95da) |
| #define | [BT\_LE\_EXT\_ADV\_SCAN](#ga5dd57fc7f0e213db08655e631a2f314e) |
|  | Scannable extended advertising. |
| #define | [BT\_LE\_EXT\_ADV\_SCAN\_NAME](#ga3e4abd3691e2c6d95acd21b9ca566edd) |
| #define | [BT\_LE\_EXT\_ADV\_NCONN](#gaabc0385f6a5307b48ec43af6aae7dea6) |
|  | Non-connectable extended advertising with private address. |
| #define | [BT\_LE\_EXT\_ADV\_NCONN\_NAME](#ga5c79af6787ccda890f485a45c931cdc8) |
| #define | [BT\_LE\_EXT\_ADV\_NCONN\_IDENTITY](#ga7e46a64af0036c433c2e940ce7db0a05) |
|  | Non-connectable extended advertising with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e). |
| #define | [BT\_LE\_EXT\_ADV\_CODED\_NCONN](#ga0e911d3aafdd0c926590b3272a3da564) |
|  | Non-connectable extended advertising on coded PHY with private address. |
| #define | [BT\_LE\_EXT\_ADV\_CODED\_NCONN\_NAME](#ga8c6027f7c0888c577f9b61a65104be05) |
| #define | [BT\_LE\_EXT\_ADV\_CODED\_NCONN\_IDENTITY](#gac67c52693154ebbeedbb31e100513812) |
|  | Non-connectable extended advertising on coded PHY with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e). |
| #define | [BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT](#gaf0d4c5b05deb5466a0e29c153263b489)(\_timeout, \_n\_evts) |
|  | Helper to initialize extended advertising start parameters inline. |
| #define | [BT\_LE\_EXT\_ADV\_START\_PARAM](#ga9b2cefbcb0a85116cadb68f6d80c6429)(\_timeout, \_n\_evts) |
|  | Helper to declare extended advertising start parameters inline. |
| #define | [BT\_LE\_EXT\_ADV\_START\_DEFAULT](#ga8c83a6f322a479bc24a576a7f091312e)   [BT\_LE\_EXT\_ADV\_START\_PARAM](#ga9b2cefbcb0a85116cadb68f6d80c6429)(0, 0) |
| #define | [BT\_LE\_PER\_ADV\_PARAM\_INIT](#ga880567278a81098ae55f52f624c61041)(\_int\_min, \_int\_max, \_options) |
|  | Helper to declare periodic advertising parameters inline. |
| #define | [BT\_LE\_PER\_ADV\_PARAM](#gaf46e54f8fcda7b65b659685bb225d243)(\_int\_min, \_int\_max, \_options) |
|  | Helper to declare periodic advertising parameters inline. |
| #define | [BT\_LE\_PER\_ADV\_DEFAULT](#ga8f6a00faaaab2a91ac943c71ed041ac1) |
| #define | [BT\_LE\_SCAN\_OPT\_FILTER\_WHITELIST](#ga33e84f4ccbf4d0aa2527e9fe1086e252)   \_\_DEPRECATED\_MACRO [BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST](#gga5afc3803e9a80e829597375fcf2a2cf3af7a25b6790b138b2b88de3c7d81cb0ae) |
| #define | [BT\_LE\_SCAN\_PARAM\_INIT](#gac9f372ca16afb1c2f0e100c5b1b94cd5)(\_type, \_options, \_interval, \_window) |
|  | Initialize scan parameters. |
| #define | [BT\_LE\_SCAN\_PARAM](#ga57ace75133343ba8de7fa965f452ee3d)(\_type, \_options, \_interval, \_window) |
|  | Helper to declare scan parameters inline. |
| #define | [BT\_LE\_SCAN\_ACTIVE](#gac137ea4ce32697582a337116ffa41da5) |
|  | Helper macro to enable active scanning to discover new devices. |
| #define | [BT\_LE\_SCAN\_ACTIVE\_CONTINUOUS](#ga9bd9701db0459c066ed7c18343f60911) |
|  | Helper macro to enable active scanning to discover new devices with window == interval. |
| #define | [BT\_LE\_SCAN\_PASSIVE](#ga8ceaef6f0fbf4fe2d76d47e8f59aeb11) |
|  | Helper macro to enable passive scanning to discover new devices. |
| #define | [BT\_LE\_SCAN\_PASSIVE\_CONTINUOUS](#ga8d8ccc9ea1db2c96deae1603ec1c78a3) |
|  | Helper macro to enable passive scanning to discover new devices with window==interval. |
| #define | [BT\_LE\_SCAN\_CODED\_ACTIVE](#ga06380c4ae6289c704a143b9d192bc35f) |
|  | Helper macro to enable active scanning to discover new devices. |
| #define | [BT\_LE\_SCAN\_CODED\_PASSIVE](#ga1e5a4589304babc6b0d49019ebcff6b0) |
|  | Helper macro to enable passive scanning to discover new devices. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_ready\_cb\_t](#ga5398783ab4a5dc854b18e37fb10774eb)) (int err) |
|  | Callback for notifying that Bluetooth has been enabled. |
| typedef void | [bt\_le\_scan\_cb\_t](#ga1c53d22b6e2dee38c825c58f3eeee9b4)(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) rssi, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adv\_type, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback type for reporting LE scan results. |

| Enumerations | |
| --- | --- |
| enum | {     [BT\_LE\_ADV\_OPT\_NONE](#gga654b0098c5f04a9c85a65f86b8f95deea928b376123819cb0a69fbb5b35608dbf) = 0 , [BT\_LE\_ADV\_OPT\_CONNECTABLE](#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) = BIT(0) , **\_BT\_LE\_ADV\_OPT\_CONNECTABLE** = BIT(0) , [BT\_LE\_ADV\_OPT\_ONE\_TIME](#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2) = BIT(1) ,     **\_BT\_LE\_ADV\_OPT\_ONE\_TIME** = BIT(1) , [BT\_LE\_ADV\_OPT\_CONN](#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169) = BIT(0) | BIT(1) , [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e) = BIT(2) , [BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398) = BIT(3) ,     [BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY](#gga654b0098c5f04a9c85a65f86b8f95deeafd164ec5476f5e2d9aedf50032946872) = BIT(4) , [BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA](#gga654b0098c5f04a9c85a65f86b8f95deeabdcf1c80662061fa30575e1f9fc6cf6f) = BIT(5) , [BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ](#gga654b0098c5f04a9c85a65f86b8f95deea807ba316edc49c8448a8ff7d497173f5) = BIT(6) , [BT\_LE\_ADV\_OPT\_FILTER\_CONN](#gga654b0098c5f04a9c85a65f86b8f95deead5efef3d01731110dbd71d5a5dc9baaf) = BIT(7) ,     [BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ](#gga654b0098c5f04a9c85a65f86b8f95deea1563b053f457833d1a3d11c8dc4d394b) = BIT(8) , [BT\_LE\_ADV\_OPT\_SCANNABLE](#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) = BIT(9) , [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) = BIT(10) , [BT\_LE\_ADV\_OPT\_NO\_2M](#gga654b0098c5f04a9c85a65f86b8f95deeae864aefcdfbecaffe823b9b144fe0a6b) = BIT(11) ,     [BT\_LE\_ADV\_OPT\_CODED](#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1) = BIT(12) , [BT\_LE\_ADV\_OPT\_ANONYMOUS](#gga654b0098c5f04a9c85a65f86b8f95deea185e0f884f8b0ce79625448638de8fab) = BIT(13) , [BT\_LE\_ADV\_OPT\_USE\_TX\_POWER](#gga654b0098c5f04a9c85a65f86b8f95deeaecff4fe3ac3d1fba3f6fa76c77713859) = BIT(14) , [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37](#gga654b0098c5f04a9c85a65f86b8f95deeab46741616f8bfe50c4b492d1f7970779) = BIT(15) ,     [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38](#gga654b0098c5f04a9c85a65f86b8f95deeabd9cb02691d7e025fe3fea9a80123275) = BIT(16) , [BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39](#gga654b0098c5f04a9c85a65f86b8f95deea89f7494620236c976bf1a76a880e2a28) = BIT(17) , [BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73) = BIT(18) , [BT\_LE\_ADV\_OPT\_USE\_NRPA](#gga654b0098c5f04a9c85a65f86b8f95deea22958d8539d661ad7ca8d3f1173e7e5e) = BIT(19)   } |
|  | Advertising options. [More...](#ga654b0098c5f04a9c85a65f86b8f95dee) |
| enum | { [BT\_LE\_PER\_ADV\_OPT\_NONE](#gga592195c57b12f7224b6d07133e60fc4aaa2c689d726eacfb18d87655b1f587518) = 0 , [BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER](#gga592195c57b12f7224b6d07133e60fc4aa9524537e4cb726f4ff10ba93381bb27f) = BIT(1) , [BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI](#gga592195c57b12f7224b6d07133e60fc4aa38cebc2ae885ff630b34c603e2ec6403) = BIT(2) } |
|  | Periodic Advertising options. [More...](#ga592195c57b12f7224b6d07133e60fc4a) |
| enum | {     [BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE](#gga9cf9b0d1941502642e50fcfc2d686bcaaeeef50a544edc104b39e4ef0c9a58d6c) = 0 , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST](#gga9cf9b0d1941502642e50fcfc2d686bcaae9a88caa6a83da8b1697a6167629bf7e) = BIT(0) , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED](#gga9cf9b0d1941502642e50fcfc2d686bcaae35a6eb572a2842e4cc2fc3677e19b53) = BIT(1) , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE](#gga9cf9b0d1941502642e50fcfc2d686bcaa9ec2b0c346c2cab7f61c2efcc8e37db2) = BIT(2) ,     [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA](#gga9cf9b0d1941502642e50fcfc2d686bcaaaa256e560f013eb74415d817154b8f4e) = BIT(3) , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US](#gga9cf9b0d1941502642e50fcfc2d686bcaa99034652a92249e6d04065d68352020b) = BIT(4) , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US](#gga9cf9b0d1941502642e50fcfc2d686bcaa0f52e38e513ec7eefcbc5c86c36f002e) = BIT(5) , [BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT](#gga9cf9b0d1941502642e50fcfc2d686bcaa5c702876d70d5eadc4df6e59d96b8320) = BIT(6)   } |
|  | Periodic advertising sync options. [More...](#ga9cf9b0d1941502642e50fcfc2d686bca) |
| enum | {     [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE](#gga9c50ffe9d076ca7be5bdd72b91e53e15aef90aceabc3f9d0b17b7f3415152fca2) = 0 , [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA](#gga9c50ffe9d076ca7be5bdd72b91e53e15a2694870b7ebd2dcd0b3834367f7d7061) = BIT(0) , [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US](#gga9c50ffe9d076ca7be5bdd72b91e53e15ab0725048806858083be9ab3fcd9a36ed) = BIT(1) , [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US](#gga9c50ffe9d076ca7be5bdd72b91e53e15a433ae469b27e820fdfd2a1d562010991) = BIT(2) ,     [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE](#gga9c50ffe9d076ca7be5bdd72b91e53e15aed2f78d682b5fbd1adf89c2f005e4f48) = BIT(3) , [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED](#gga9c50ffe9d076ca7be5bdd72b91e53e15a3f0be549ca5cac1cfbdec2f2227e73dc) = BIT(4) , [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES](#gga9c50ffe9d076ca7be5bdd72b91e53e15ad924f620ed6fdadbbea03f8e343b9d0c) = BIT(5)   } |
|  | Periodic Advertising Sync Transfer options. [More...](#ga9c50ffe9d076ca7be5bdd72b91e53e15) |
| enum | {     [BT\_LE\_SCAN\_OPT\_NONE](#gga5afc3803e9a80e829597375fcf2a2cf3aad3f19e5849b6d6813fa88257082e185) = 0 , [BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394) = BIT(0) , [BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST](#gga5afc3803e9a80e829597375fcf2a2cf3af7a25b6790b138b2b88de3c7d81cb0ae) = BIT(1) , [BT\_LE\_SCAN\_OPT\_CODED](#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb) = BIT(2) ,     [BT\_LE\_SCAN\_OPT\_NO\_1M](#gga5afc3803e9a80e829597375fcf2a2cf3a7ff0c79b2675e7b7512379e2cbedc0a6) = BIT(3)   } |
| enum | { [BT\_LE\_SCAN\_TYPE\_PASSIVE](#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006) = 0x00 , [BT\_LE\_SCAN\_TYPE\_ACTIVE](#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22) = 0x01 } |

| Functions | |
| --- | --- |
| int | [bt\_enable](#gac45d16bfe21c3c38e834c293e5ebc42b) ([bt\_ready\_cb\_t](#ga5398783ab4a5dc854b18e37fb10774eb) cb) |
|  | Enable Bluetooth. |
| int | [bt\_disable](#ga0a58e5a050170e84a80f8d5bb3516ec7) (void) |
|  | Disable Bluetooth. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_is\_ready](#gaa8bf6854e7ad1fe7e0805737576e5d1a) (void) |
|  | Check if Bluetooth is ready. |
| int | [bt\_set\_name](#gac8bb3609a3d6da69ff736809e45f5c8a) (const char \*name) |
|  | Set Bluetooth Device Name. |
| const char \* | [bt\_get\_name](#gad922d894b25e86de3f81ce77200a13fd) (void) |
|  | Get Bluetooth Device Name. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_get\_appearance](#ga35b76ea7ce79721e47ca4164e08b2dfb) (void) |
|  | Get local Bluetooth appearance. |
| int | [bt\_set\_appearance](#gaf0729453790aab1bd3d52c623be3b35a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) new\_appearance) |
|  | Set local Bluetooth appearance. |
| void | [bt\_id\_get](#ga06d0ae35cbf4382679cc3cfe612cee4d) ([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addrs, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*count) |
|  | Get the currently configured identities. |
| int | [bt\_id\_create](#gae11eb8ad254418c38a0e8689df25a159) ([bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*irk) |
|  | Create a new identity. |
| int | [bt\_id\_reset](#gabb3353edc8a3a8d29a0370049b20cbe4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*irk) |
|  | Reset/reclaim an identity for reuse. |
| int | [bt\_id\_delete](#gaf6cd906690a51ebed04bea4f4ef716ff) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) |
|  | Delete an identity. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bt\_data\_get\_len](#ga3d2c6adc42eb9510734630f38d921b9a) (const struct [bt\_data](structbt__data.md) data[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_count) |
|  | Get the total size (in bytes) of a given set of [bt\_data](structbt__data.md "bt_data") structures. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bt\_data\_serialize](#ga3c067b16468ebd17973faeded0fc83c9) (const struct [bt\_data](structbt__data.md) \*input, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*output) |
|  | Serialize a [bt\_data](structbt__data.md "bt_data") struct into an advertising structure (a flat byte array). |
| int | [bt\_le\_adv\_start](#gad2e3caef88d52d720e8e4d21df767b02) (const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param, const struct [bt\_data](structbt__data.md) \*ad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ad\_len, const struct [bt\_data](structbt__data.md) \*sd, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sd\_len) |
|  | Start advertising. |
| int | [bt\_le\_adv\_update\_data](#ga9a406ebfefac3dd09935a4ae0e317817) (const struct [bt\_data](structbt__data.md) \*ad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ad\_len, const struct [bt\_data](structbt__data.md) \*sd, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sd\_len) |
|  | Update advertising. |
| int | [bt\_le\_adv\_stop](#ga1776e310b9d80898e6b32d50c4fe0b49) (void) |
|  | Stop advertising. |
| int | [bt\_le\_ext\_adv\_create](#gad02b855dd7a26e3910b247fa73f19297) (const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param, const struct [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md) \*cb, struct bt\_le\_ext\_adv \*\*adv) |
|  | Create advertising set. |
| int | [bt\_le\_ext\_adv\_start](#gaf0f436c55482d9429f674303ae3aa815) (struct bt\_le\_ext\_adv \*adv, const struct [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md) \*param) |
|  | Start advertising with the given advertising set. |
| int | [bt\_le\_ext\_adv\_stop](#ga1c864c4b183f9a86c9f70a11471c5b15) (struct bt\_le\_ext\_adv \*adv) |
|  | Stop advertising with the given advertising set. |
| int | [bt\_le\_ext\_adv\_set\_data](#gad731f829b3566be3e56485b2a64f80b1) (struct bt\_le\_ext\_adv \*adv, const struct [bt\_data](structbt__data.md) \*ad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ad\_len, const struct [bt\_data](structbt__data.md) \*sd, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sd\_len) |
|  | Set an advertising set's advertising or scan response data. |
| int | [bt\_le\_ext\_adv\_update\_param](#ga1aabdb81cb1a1841ff0fb91d849123fc) (struct bt\_le\_ext\_adv \*adv, const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \*param) |
|  | Update advertising parameters. |
| int | [bt\_le\_ext\_adv\_delete](#ga62310a27f7fea925dfcf3abd7c454787) (struct bt\_le\_ext\_adv \*adv) |
|  | Delete advertising set. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_le\_ext\_adv\_get\_index](#gaeb37d6cdd94a04b4cce8bc1e7aae70b4) (struct bt\_le\_ext\_adv \*adv) |
|  | Get array index of an advertising set. |
| int | [bt\_le\_ext\_adv\_get\_info](#gac06c9f55cf1da46e0d64b4d9af984ecb) (const struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md) \*info) |
|  | Get advertising set info. |
| int | [bt\_le\_per\_adv\_set\_param](#gaa72029a2759123ec776061d2e80bf3a1) (struct bt\_le\_ext\_adv \*adv, const struct [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md) \*param) |
|  | Set or update the periodic advertising parameters. |
| int | [bt\_le\_per\_adv\_set\_data](#gafd0e7ccca93a8347a4ca6cca88e77899) (const struct bt\_le\_ext\_adv \*adv, const struct [bt\_data](structbt__data.md) \*ad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ad\_len) |
|  | Set or update the periodic advertising data. |
| int | [bt\_le\_per\_adv\_set\_subevent\_data](#ga7de30fe5040b85bb9212e3a8fec4ac45) (const struct bt\_le\_ext\_adv \*adv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents, const struct [bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md) \*params) |
|  | Set the periodic advertising with response subevent data. |
| int | [bt\_le\_per\_adv\_start](#ga0f23f4ed48e8679646f247ea0d687094) (struct bt\_le\_ext\_adv \*adv) |
|  | Starts periodic advertising. |
| int | [bt\_le\_per\_adv\_stop](#ga1b15206fc552d597c12af369d48ff7d5) (struct bt\_le\_ext\_adv \*adv) |
|  | Stops periodic advertising. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_le\_per\_adv\_sync\_get\_index](#ga8d05bd864d98b5b43595eb256e464024) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync) |
|  | Get array index of an periodic advertising sync object. |
| struct bt\_le\_per\_adv\_sync \* | [bt\_le\_per\_adv\_sync\_lookup\_index](#ga59532b37412b1b93f81cf5cc1bab0534) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Get a periodic advertising sync object from the array index. |
| int | [bt\_le\_per\_adv\_sync\_get\_info](#gabfaf265a48dd09ea02d114e2023c14a6) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, struct [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md) \*info) |
|  | Get periodic adv sync information. |
| struct bt\_le\_per\_adv\_sync \* | [bt\_le\_per\_adv\_sync\_lookup\_addr](#ga83126917373c0bcaa24964dd1d8bde46) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*adv\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid) |
|  | Look up an existing periodic advertising sync object by advertiser address. |
| int | [bt\_le\_per\_adv\_sync\_create](#ga061bf84b989b2c96ab51d2ca0debb017) (const struct [bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md) \*param, struct bt\_le\_per\_adv\_sync \*\*out\_sync) |
|  | Create a periodic advertising sync object. |
| int | [bt\_le\_per\_adv\_sync\_delete](#gaa0c218ff3c78b26dcfaa726ee30267a6) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync) |
|  | Delete periodic advertising sync. |
| int | [bt\_le\_per\_adv\_sync\_cb\_register](#ga4ee87bbf79e6ac844d14c3dafb2dadf4) (struct [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md) \*cb) |
|  | Register periodic advertising sync callbacks. |
| int | [bt\_le\_per\_adv\_sync\_recv\_enable](#ga07e4510de7e72c6ed6196b3da9fb40be) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync) |
|  | Enables receiving periodic advertising reports for a sync. |
| int | [bt\_le\_per\_adv\_sync\_recv\_disable](#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync) |
|  | Disables receiving periodic advertising reports for a sync. |
| int | [bt\_le\_per\_adv\_sync\_transfer](#gaf81a1dd7a628d1a2f25c6b53b0679809) (const struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, const struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) service\_data) |
|  | Transfer the periodic advertising sync information to a peer device. |
| int | [bt\_le\_per\_adv\_set\_info\_transfer](#gac96199a4e5e6cfb789c1bd1c0e67d6fe) (const struct bt\_le\_ext\_adv \*adv, const struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) service\_data) |
|  | Transfer the information about a periodic advertising set. |
| int | [bt\_le\_per\_adv\_sync\_transfer\_subscribe](#gaa0658bd53df1d5e8e89e13330e4fd0ae) (const struct bt\_conn \*conn, const struct [bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md) \*param) |
|  | Subscribe to periodic advertising sync transfers (PASTs). |
| int | [bt\_le\_per\_adv\_sync\_transfer\_unsubscribe](#ga08f872078045bbef4aca19761f25eeb8) (const struct bt\_conn \*conn) |
|  | Unsubscribe from periodic advertising sync transfers (PASTs). |
| int | [bt\_le\_per\_adv\_list\_add](#ga27c4961f3c7270a7f1caeadb4107854b) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid) |
|  | Add a device to the periodic advertising list. |
| int | [bt\_le\_per\_adv\_list\_remove](#ga100efac4a49984e06202c63c4e5955cd) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sid) |
|  | Remove a device from the periodic advertising list. |
| int | [bt\_le\_per\_adv\_list\_clear](#ga5909bd768c23a19a42a660e3b814c981) (void) |
|  | Clear the periodic advertising list. |
| int | [bt\_le\_scan\_start](#gac5e19c26b53a08dadb8efa7ecc692ad6) (const struct [bt\_le\_scan\_param](structbt__le__scan__param.md) \*param, [bt\_le\_scan\_cb\_t](#ga1c53d22b6e2dee38c825c58f3eeee9b4) cb) |
|  | Start (LE) scanning. |
| int | [bt\_le\_scan\_stop](#gaa2de1a1ab523606b36a4c445fb0c3b84) (void) |
|  | Stop (LE) scanning. |
| int | [bt\_le\_scan\_cb\_register](#ga80e870fa1de40c404c64624bef439067) (struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \*cb) |
|  | Register scanner packet callbacks. |
| void | [bt\_le\_scan\_cb\_unregister](#gac2718f2128b3f8c79b12d760771c8378) (struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \*cb) |
|  | Unregister scanner packet callbacks. |
| int | [bt\_le\_filter\_accept\_list\_add](#ga40f2f7fdb09aba3c5137f680e67792f0) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Add device (LE) to filter accept list. |
| int | [bt\_le\_filter\_accept\_list\_remove](#ga0532ed768ab4f9d69c202066d2f87e66) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Remove device (LE) from filter accept list. |
| int | [bt\_le\_filter\_accept\_list\_clear](#gac87df899d1e363c63162988157ee6d00) (void) |
|  | Clear filter accept list. |
| int | [bt\_le\_set\_chan\_map](#gabc115fd3fff6d00ae878a31613bf70aa) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chan\_map[5]) |
|  | Set (LE) channel map. |
| int | [bt\_le\_set\_rpa\_timeout](#ga9ab41e118b5496c196e56b8b5d023275) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) new\_rpa\_timeout) |
|  | Set the Resolvable Private Address timeout in runtime. |
| void | [bt\_data\_parse](#ga652eef01e5256e0d820cd1f4db877429) (struct [net\_buf\_simple](structnet__buf__simple.md) \*ad, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*func)(struct [bt\_data](structbt__data.md) \*data, void \*user\_data), void \*user\_data) |
|  | Helper for parsing advertising (or EIR or OOB) data. |
| int | [bt\_le\_oob\_get\_local](#ga296d1adf3c9ed2f2c65bb75b887d59ee) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, struct [bt\_le\_oob](structbt__le__oob.md) \*oob) |
|  | Get local LE Out of Band (OOB) information. |
| int | [bt\_le\_ext\_adv\_oob\_get\_local](#ga7486aab863ca497a50dacf81657f48d4) (struct bt\_le\_ext\_adv \*adv, struct [bt\_le\_oob](structbt__le__oob.md) \*oob) |
|  | Get local LE Out of Band (OOB) information. |
| int | [bt\_unpair](#gaceabbbe6e844650f791010e53c9df6a4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr) |
|  | Clear pairing information. |
| void | [bt\_foreach\_bond](#gaad380b7f8984f8522c1b79f9bdc04905) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, void(\*func)(const struct [bt\_bond\_info](structbt__bond__info.md) \*info, void \*user\_data), void \*user\_data) |
|  | Iterate through all existing bonds. |
| int | [bt\_configure\_data\_path](#ga8046c2b06d3dad0d6c8184de492517d2) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dir, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vs\_config\_len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vs\_config) |
|  | Configure vendor data path. |
| int | [bt\_le\_per\_adv\_sync\_subevent](#ga731f4b37a9e5cc13a6816ea23f751b0b) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, struct [bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md) \*params) |
|  | Synchronize with a subset of subevents. |
| int | [bt\_le\_per\_adv\_set\_response\_data](#gaae6b8583f7d5457f20b03dccd146425e) (struct bt\_le\_per\_adv\_sync \*per\_adv\_sync, const struct [bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md) \*params, const struct [net\_buf\_simple](structnet__buf__simple.md) \*data) |
|  | Set the data for a response slot in a specific subevent of the PAwR. |
| int | [bt\_br\_discovery\_start](#ga9760190192dde5c498ec96628468be8d) (const struct [bt\_br\_discovery\_param](structbt__br__discovery__param.md) \*param, struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \*results, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Start BR/EDR discovery. |
| int | [bt\_br\_discovery\_stop](#ga567c71b49399fe7e1a5593edbf005e3a) (void) |
|  | Stop BR/EDR discovery. |
| void | [bt\_br\_discovery\_cb\_register](#ga430de0ad30da7322c5353941f1f6a133) (struct [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md) \*cb) |
|  | Register discovery packet callbacks. |
| void | [bt\_br\_discovery\_cb\_unregister](#ga25ab96ac005237aee739bf32fc1aac94) (struct [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md) \*cb) |
|  | Unregister discovery packet callbacks. |
| int | [bt\_br\_oob\_get\_local](#ga2ec860d06c45098624b106b59fbab634) (struct [bt\_br\_oob](structbt__br__oob.md) \*oob) |
|  | Get BR/EDR local Out Of Band information. |
| int | [bt\_br\_set\_discoverable](#gad3b9075cc9bab5c1ae37514a6dfe555c) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable/disable set controller in discoverable state. |
| int | [bt\_br\_set\_connectable](#ga80aed18a099948bef8f3649ad537e541) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable/disable set controller in connectable state. |

## Detailed Description

Generic Access Profile (GAP).

Since
:   1.0

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga8481217e632522e1f322de87d745f8f0)BT\_DATA

| #define BT\_DATA | ( |  | *\_type*, |
| --- | --- | --- | --- |
|  |  |  | *\_data*, |
|  |  |  | *\_data\_len* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

{ \

.type = (\_type), \

.data\_len = (\_data\_len), \

.data = (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_data), \

}

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Helper to declare elements of [bt\_data](structbt__data.md "Bluetooth data.") arrays.

This macro is mainly for creating an array of struct [bt\_data](structbt__data.md "Bluetooth data.") elements which is then passed to e.g. [bt\_le\_adv\_start()](#gad2e3caef88d52d720e8e4d21df767b02).

Parameters
:   | \_type | Type of advertising data field |
    | --- | --- |
    | \_data | Pointer to the data field payload |
    | \_data\_len | Number of bytes behind the \_data pointer |

## [◆ ](#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)BT\_DATA\_BYTES

| #define BT\_DATA\_BYTES | ( |  | *\_type*, |
| --- | --- | --- | --- |
|  |  |  | *\_bytes...* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_DATA](#ga8481217e632522e1f322de87d745f8f0)(\_type, (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) []) { \_bytes }), \

sizeof(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) []) { \_bytes }))

[BT\_DATA](#ga8481217e632522e1f322de87d745f8f0)

#define BT\_DATA(\_type, \_data, \_data\_len)

Helper to declare elements of bt\_data arrays.

**Definition** bluetooth.h:472

Helper to declare elements of [bt\_data](structbt__data.md "Bluetooth data.") arrays.

This macro is mainly for creating an array of struct [bt\_data](structbt__data.md "Bluetooth data.") elements which is then passed to e.g. [bt\_le\_adv\_start()](#gad2e3caef88d52d720e8e4d21df767b02).

Parameters
:   | \_type | Type of advertising data field |
    | --- | --- |
    | \_bytes | Variable number of single-byte parameters |

## [◆ ](#ga7357d34bf295a16d8288df3bf75e7976)BT\_DATA\_SERIALIZED\_SIZE

| #define BT\_DATA\_SERIALIZED\_SIZE | ( |  | *data\_len* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

((data\_len) + 2)

Bluetooth data serialized size.

Get the size of a serialized [bt\_data](structbt__data.md "bt_data") given its data length.

Size of 'AD Structure'->'Length' field, equal to 1. Size of 'AD Structure'->'Data'->'AD Type' field, equal to 1. Size of 'AD Structure'->'Data'->'AD Data' field, equal to data\_len.

See Core Specification Version 5.4 Vol. 3 Part C, 11, Figure 11.1.

## [◆ ](#gaded4b52c9bb87fd4d19b1eb9361973e5)BT\_ID\_DEFAULT

| #define BT\_ID\_DEFAULT   0 |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Convenience macro for specifying the default identity.

This helps make the code more readable, especially when only one identity is supported.

## [◆ ](#gad490487b9e196526a13fe249a4c25448)BT\_LE\_ADV\_CONN

| #define BT\_LE\_ADV\_CONN |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_CONNECTABLE](#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3), [BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), NULL) \

\_\_DEPRECATED\_MACRO

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60)

#define BT\_GAP\_ADV\_FAST\_INT\_MIN\_2

**Definition** gap.h:726

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb)

#define BT\_GAP\_ADV\_FAST\_INT\_MAX\_2

**Definition** gap.h:727

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)

#define BT\_LE\_ADV\_PARAM(\_options, \_int\_min, \_int\_max, \_peer)

Helper to declare advertising parameters inline.

**Definition** bluetooth.h:965

[BT\_LE\_ADV\_OPT\_CONNECTABLE](#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3)

@ BT\_LE\_ADV\_OPT\_CONNECTABLE

Advertise as connectable.

**Definition** bluetooth.h:545

**[Deprecated](deprecated.md#_deprecated000001)**
:   This is a convenience macro for [BT\_LE\_ADV\_OPT\_CONNECTABLE](#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3), which is deprecated. Please use [BT\_LE\_ADV\_CONN\_FAST\_1](#gaa700527b1caf3bef27d96a3f91a29f69) or [BT\_LE\_ADV\_CONN\_FAST\_2](#ga684a1110a8973bc17211f6f0824beccd) instead.

## [◆ ](#ga1f5edc3c4cbead62e32cef8cc7b83725)BT\_LE\_ADV\_CONN\_DIR

| #define BT\_LE\_ADV\_CONN\_DIR | ( |  | *\_peer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_CONN](#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169), 0, 0, \_peer)

[BT\_LE\_ADV\_OPT\_CONN](#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169)

@ BT\_LE\_ADV\_OPT\_CONN

Connectable advertising.

**Definition** bluetooth.h:603

## [◆ ](#gab89e033ed3fd116c94120d177dfdc839)BT\_LE\_ADV\_CONN\_DIR\_LOW\_DUTY

| #define BT\_LE\_ADV\_CONN\_DIR\_LOW\_DUTY | ( |  | *\_peer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_CONN](#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169) | [BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY](#gga654b0098c5f04a9c85a65f86b8f95deeafd164ec5476f5e2d9aedf50032946872), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), [BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), \_peer)

[BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY](#gga654b0098c5f04a9c85a65f86b8f95deeafd164ec5476f5e2d9aedf50032946872)

@ BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY

Low duty cycle directed advertising.

**Definition** bluetooth.h:649

## [◆ ](#gaa700527b1caf3bef27d96a3f91a29f69)BT\_LE\_ADV\_CONN\_FAST\_1

| #define BT\_LE\_ADV\_CONN\_FAST\_1 |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_CONN](#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169), [BT\_GAP\_ADV\_FAST\_INT\_MIN\_1](group__bt__gap__defines.md#ga397a52fe616416665b46a2bc454c2e11), [BT\_GAP\_ADV\_FAST\_INT\_MAX\_1](group__bt__gap__defines.md#ga13acf16d3d8edd39636bb10df752775a), \

NULL)

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_1](group__bt__gap__defines.md#ga13acf16d3d8edd39636bb10df752775a)

#define BT\_GAP\_ADV\_FAST\_INT\_MAX\_1

**Definition** gap.h:725

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_1](group__bt__gap__defines.md#ga397a52fe616416665b46a2bc454c2e11)

#define BT\_GAP\_ADV\_FAST\_INT\_MIN\_1

**Definition** gap.h:724

GAP recommended connectable advertising.

This is the recommended default for when a person is likely to be waiting the device to connect or be discovered.

Use a longer interval to conserve battery at the cost of responsiveness. Consider entering a lower power state with longer intervals after a timeout.

GAP recommends advertisers use this "when user-initiated". The application developer decides what this means. It can by any time the user interacts with the device, a press on a dedicated Bluetooth wakeup button, or anything in-between.

This is the recommended setting for limited discoverable mode.

See Bluetooth Core Specification:

- 3.C.A "Timers and Constants", T\_GAP(adv\_fast\_interval1)
- 3.C.9.3.11 "Connection Establishment Timing parameters"

## [◆ ](#ga684a1110a8973bc17211f6f0824beccd)BT\_LE\_ADV\_CONN\_FAST\_2

| #define BT\_LE\_ADV\_CONN\_FAST\_2 |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_CONN](#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169), [BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), [BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), \

NULL)

Connectable advertising with T\_GAP(adv\_fast\_interval2).

The advertising interval corresponds to what was offered as [BT\_LE\_ADV\_CONN](#gad490487b9e196526a13fe249a4c25448) in Zephyr 3.6 and earlier, but unlike [BT\_LE\_ADV\_CONN](#gad490487b9e196526a13fe249a4c25448), the host does not automatically resume the advertiser after it results in a connection.

See Bluetooth Core Specification:

- 3.C.A "Timers and Constants", T\_GAP(adv\_fast\_interval1)
- 3.C.9.3.11 "Connection Establishment Timing parameters"

## [◆ ](#ga7b29dba3d892186897c5b4ca5adfd2e3)BT\_LE\_ADV\_CONN\_NAME

| #define BT\_LE\_ADV\_CONN\_NAME |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_CONNECTABLE](#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) | \

[BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), NULL) \

\_\_DEPRECATED\_MACRO

[BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398)

@ BT\_LE\_ADV\_OPT\_USE\_NAME

Advertise using GAP device name.

**Definition** bluetooth.h:641

**[Deprecated](deprecated.md#_deprecated000002)**
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

## [◆ ](#ga213307090f1debdc783c54faf4a36740)BT\_LE\_ADV\_CONN\_NAME\_AD

| #define BT\_LE\_ADV\_CONN\_NAME\_AD |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_CONNECTABLE](#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) | \

[BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398) | \

[BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), NULL) \

\_\_DEPRECATED\_MACRO

[BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73)

@ BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD

Put GAP device name into advert data.

**Definition** bluetooth.h:772

**[Deprecated](deprecated.md#_deprecated000003)**
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

## [◆ ](#gac0430ab5a40a49b3281dd6ff8a7e7378)BT\_LE\_ADV\_CONN\_ONE\_TIME

| #define BT\_LE\_ADV\_CONN\_ONE\_TIME   [BT\_LE\_ADV\_CONN\_FAST\_2](#ga684a1110a8973bc17211f6f0824beccd) \_\_DEPRECATED\_MACRO |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

## [◆ ](#ga1610555bf59f1d691d640f245957fdce)BT\_LE\_ADV\_NCONN

| #define BT\_LE\_ADV\_NCONN |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)(0, [BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), NULL)

Non-connectable advertising with private address.

## [◆ ](#ga6ef9fb7a469b03265c7adc99ea19a11b)BT\_LE\_ADV\_NCONN\_IDENTITY

| #define BT\_LE\_ADV\_NCONN\_IDENTITY |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), \

NULL)

[BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e)

@ BT\_LE\_ADV\_OPT\_USE\_IDENTITY

Advertise using identity address.

**Definition** bluetooth.h:615

Non-connectable advertising with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e).

## [◆ ](#gac1c3c47e3136ce813bb50b00a9387cb4)BT\_LE\_ADV\_NCONN\_NAME

| #define BT\_LE\_ADV\_NCONN\_NAME |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), NULL) \

\_\_DEPRECATED\_MACRO

**[Deprecated](deprecated.md#_deprecated000004)**
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Non-connectable advertising with [BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398)

## [◆ ](#ga9557269dd36b624b49e76c511c3a0cc1)BT\_LE\_ADV\_PARAM

| #define BT\_LE\_ADV\_PARAM | ( |  | *\_options*, |
| --- | --- | --- | --- |
|  |  |  | *\_int\_min*, |
|  |  |  | *\_int\_max*, |
|  |  |  | *\_peer* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

((const struct [bt\_le\_adv\_param](structbt__le__adv__param.md)[]) { \

BT\_LE\_ADV\_PARAM\_INIT(\_options, \_int\_min, \_int\_max, \_peer) \

})

[bt\_le\_adv\_param](structbt__le__adv__param.md)

LE Advertising Parameters.

**Definition** bluetooth.h:790

Helper to declare advertising parameters inline.

Parameters
:   | \_options | Advertising Options |
    | --- | --- |
    | \_int\_min | Minimum advertising interval |
    | \_int\_max | Maximum advertising interval |
    | \_peer | Peer address, set to NULL for undirected advertising or address of peer for directed advertising. |

## [◆ ](#ga71555b857cf8c2a47c36e4dafa7accf4)BT\_LE\_ADV\_PARAM\_INIT

| #define BT\_LE\_ADV\_PARAM\_INIT | ( |  | *\_options*, |
| --- | --- | --- | --- |
|  |  |  | *\_int\_min*, |
|  |  |  | *\_int\_max*, |
|  |  |  | *\_peer* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

{ \

.id = [BT\_ID\_DEFAULT](#gaded4b52c9bb87fd4d19b1eb9361973e5), \

.sid = 0, \

.secondary\_max\_skip = 0, \

.options = (\_options), \

.interval\_min = (\_int\_min), \

.interval\_max = (\_int\_max), \

.peer = (\_peer), \

}

[BT\_ID\_DEFAULT](#gaded4b52c9bb87fd4d19b1eb9361973e5)

#define BT\_ID\_DEFAULT

Convenience macro for specifying the default identity.

**Definition** bluetooth.h:49

Initialize advertising parameters.

Parameters
:   | \_options | Advertising Options |
    | --- | --- |
    | \_int\_min | Minimum advertising interval |
    | \_int\_max | Maximum advertising interval |
    | \_peer | Peer address, set to NULL for undirected advertising or address of peer for directed advertising. |

## [◆ ](#ga0e911d3aafdd0c926590b3272a3da564)BT\_LE\_EXT\_ADV\_CODED\_NCONN

| #define BT\_LE\_EXT\_ADV\_CODED\_NCONN |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) | \

[BT\_LE\_ADV\_OPT\_CODED](#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), \

NULL)

[BT\_LE\_ADV\_OPT\_CODED](#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1)

@ BT\_LE\_ADV\_OPT\_CODED

Advertise on the LE Coded PHY (Long Range).

**Definition** bluetooth.h:736

[BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab)

@ BT\_LE\_ADV\_OPT\_EXT\_ADV

Advertise with extended advertising.

**Definition** bluetooth.h:708

Non-connectable extended advertising on coded PHY with private address.

## [◆ ](#gac67c52693154ebbeedbb31e100513812)BT\_LE\_EXT\_ADV\_CODED\_NCONN\_IDENTITY

| #define BT\_LE\_EXT\_ADV\_CODED\_NCONN\_IDENTITY |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) | [BT\_LE\_ADV\_OPT\_CODED](#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1) | \

[BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), NULL)

Non-connectable extended advertising on coded PHY with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e).

## [◆ ](#ga8c6027f7c0888c577f9b61a65104be05)BT\_LE\_EXT\_ADV\_CODED\_NCONN\_NAME

| #define BT\_LE\_EXT\_ADV\_CODED\_NCONN\_NAME |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) | [BT\_LE\_ADV\_OPT\_CODED](#gga654b0098c5f04a9c85a65f86b8f95deead01c4962a350d3218ba0cabd713708b1) | \

[BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), NULL) \

\_\_DEPRECATED\_MACRO

**[Deprecated](deprecated.md#_deprecated000008)**
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Non-connectable extended advertising on coded PHY with [BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398)

## [◆ ](#gaeaaef4dede5d45251dfe12f329e070b7)BT\_LE\_EXT\_ADV\_CONN

| #define BT\_LE\_EXT\_ADV\_CONN |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) | [BT\_LE\_ADV\_OPT\_CONN](#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169), [BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), NULL)

Connectable extended advertising.

## [◆ ](#gac4880197cbe21aad78c4edf10cde95da)BT\_LE\_EXT\_ADV\_CONN\_NAME

| #define BT\_LE\_EXT\_ADV\_CONN\_NAME |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) | \

[BT\_LE\_ADV\_OPT\_CONNECTABLE](#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) | \

[BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), \

NULL) \

\_\_DEPRECATED\_MACRO

**[Deprecated](deprecated.md#_deprecated000005)**
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Connectable extended advertising with [BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398)

## [◆ ](#gaabc0385f6a5307b48ec43af6aae7dea6)BT\_LE\_EXT\_ADV\_NCONN

| #define BT\_LE\_EXT\_ADV\_NCONN |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), NULL)

Non-connectable extended advertising with private address.

## [◆ ](#ga7e46a64af0036c433c2e940ce7db0a05)BT\_LE\_EXT\_ADV\_NCONN\_IDENTITY

| #define BT\_LE\_EXT\_ADV\_NCONN\_IDENTITY |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) | \

[BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), NULL)

Non-connectable extended advertising with [BT\_LE\_ADV\_OPT\_USE\_IDENTITY](#gga654b0098c5f04a9c85a65f86b8f95deea407cf5ae358d3c00dd7e47dfaad3ec6e).

## [◆ ](#ga5c79af6787ccda890f485a45c931cdc8)BT\_LE\_EXT\_ADV\_NCONN\_NAME

| #define BT\_LE\_EXT\_ADV\_NCONN\_NAME |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) | \

[BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), \

NULL) \

\_\_DEPRECATED\_MACRO

**[Deprecated](deprecated.md#_deprecated000007)**
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Non-connectable extended advertising with [BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398)

## [◆ ](#ga5dd57fc7f0e213db08655e631a2f314e)BT\_LE\_EXT\_ADV\_SCAN

| #define BT\_LE\_EXT\_ADV\_SCAN |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) | \

[BT\_LE\_ADV\_OPT\_SCANNABLE](#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), \

NULL)

[BT\_LE\_ADV\_OPT\_SCANNABLE](#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9)

@ BT\_LE\_ADV\_OPT\_SCANNABLE

Support scan response data.

**Definition** bluetooth.h:686

Scannable extended advertising.

## [◆ ](#ga3e4abd3691e2c6d95acd21b9ca566edd)BT\_LE\_EXT\_ADV\_SCAN\_NAME

| #define BT\_LE\_EXT\_ADV\_SCAN\_NAME |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_ADV\_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)([BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) | \

[BT\_LE\_ADV\_OPT\_SCANNABLE](#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) | \

[BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398), \

[BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60), \

[BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb), \

NULL) \

\_\_DEPRECATED\_MACRO

**[Deprecated](deprecated.md#_deprecated000006)**
:   This macro will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)

Scannable extended advertising with [BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398)

## [◆ ](#ga8c83a6f322a479bc24a576a7f091312e)BT\_LE\_EXT\_ADV\_START\_DEFAULT

| #define BT\_LE\_EXT\_ADV\_START\_DEFAULT   [BT\_LE\_EXT\_ADV\_START\_PARAM](#ga9b2cefbcb0a85116cadb68f6d80c6429)(0, 0) |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

## [◆ ](#ga9b2cefbcb0a85116cadb68f6d80c6429)BT\_LE\_EXT\_ADV\_START\_PARAM

| #define BT\_LE\_EXT\_ADV\_START\_PARAM | ( |  | *\_timeout*, |
| --- | --- | --- | --- |
|  |  |  | *\_n\_evts* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

((const struct [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md)[]) { \

BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT((\_timeout), (\_n\_evts)) \

})

[bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md)

**Definition** bluetooth.h:1298

Helper to declare extended advertising start parameters inline.

Parameters
:   | \_timeout | Advertiser timeout |
    | --- | --- |
    | \_n\_evts | Number of advertising events |

## [◆ ](#gaf0d4c5b05deb5466a0e29c153263b489)BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT

| #define BT\_LE\_EXT\_ADV\_START\_PARAM\_INIT | ( |  | *\_timeout*, |
| --- | --- | --- | --- |
|  |  |  | *\_n\_evts* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

{ \

.timeout = (\_timeout), \

.num\_events = (\_n\_evts), \

}

Helper to initialize extended advertising start parameters inline.

Parameters
:   | \_timeout | Advertiser timeout |
    | --- | --- |
    | \_n\_evts | Number of advertising events |

## [◆ ](#ga8f6a00faaaab2a91ac943c71ed041ac1)BT\_LE\_PER\_ADV\_DEFAULT

| #define BT\_LE\_PER\_ADV\_DEFAULT |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_PER\_ADV\_PARAM](#gaf46e54f8fcda7b65b659685bb225d243)([BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN](group__bt__gap__defines.md#gab51898ce46ee9ae468ed7ffc1d117321), \

[BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX](group__bt__gap__defines.md#gaa618da2a7c217527b0d962315caa1c22), \

[BT\_LE\_PER\_ADV\_OPT\_NONE](#gga592195c57b12f7224b6d07133e60fc4aaa2c689d726eacfb18d87655b1f587518))

[BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX](group__bt__gap__defines.md#gaa618da2a7c217527b0d962315caa1c22)

#define BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX

**Definition** gap.h:735

[BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN](group__bt__gap__defines.md#gab51898ce46ee9ae468ed7ffc1d117321)

#define BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN

**Definition** gap.h:734

[BT\_LE\_PER\_ADV\_PARAM](#gaf46e54f8fcda7b65b659685bb225d243)

#define BT\_LE\_PER\_ADV\_PARAM(\_int\_min, \_int\_max, \_options)

Helper to declare periodic advertising parameters inline.

**Definition** bluetooth.h:1213

[BT\_LE\_PER\_ADV\_OPT\_NONE](#gga592195c57b12f7224b6d07133e60fc4aaa2c689d726eacfb18d87655b1f587518)

@ BT\_LE\_PER\_ADV\_OPT\_NONE

Convenience value when no options are specified.

**Definition** bluetooth.h:861

## [◆ ](#gaf46e54f8fcda7b65b659685bb225d243)BT\_LE\_PER\_ADV\_PARAM

| #define BT\_LE\_PER\_ADV\_PARAM | ( |  | *\_int\_min*, |
| --- | --- | --- | --- |
|  |  |  | *\_int\_max*, |
|  |  |  | *\_options* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

((struct [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md)[]) { \

BT\_LE\_PER\_ADV\_PARAM\_INIT(\_int\_min, \_int\_max, \_options) \

})

[bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md)

**Definition** bluetooth.h:878

Helper to declare periodic advertising parameters inline.

Parameters
:   | \_int\_min | Minimum periodic advertising interval |
    | --- | --- |
    | \_int\_max | Maximum periodic advertising interval |
    | \_options | Periodic advertising properties bitfield. |

## [◆ ](#ga880567278a81098ae55f52f624c61041)BT\_LE\_PER\_ADV\_PARAM\_INIT

| #define BT\_LE\_PER\_ADV\_PARAM\_INIT | ( |  | *\_int\_min*, |
| --- | --- | --- | --- |
|  |  |  | *\_int\_max*, |
|  |  |  | *\_options* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

{ \

.interval\_min = (\_int\_min), \

.interval\_max = (\_int\_max), \

.options = (\_options), \

}

Helper to declare periodic advertising parameters inline.

Parameters
:   | \_int\_min | Minimum periodic advertising interval |
    | --- | --- |
    | \_int\_max | Maximum periodic advertising interval |
    | \_options | Periodic advertising properties bitfield. |

## [◆ ](#gac137ea4ce32697582a337116ffa41da5)BT\_LE\_SCAN\_ACTIVE

| #define BT\_LE\_SCAN\_ACTIVE |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_SCAN\_PARAM](#ga57ace75133343ba8de7fa965f452ee3d)([BT\_LE\_SCAN\_TYPE\_ACTIVE](#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22), \

[BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394), \

[BT\_GAP\_SCAN\_FAST\_INTERVAL](group__bt__gap__defines.md#ga747caa714962215453a966a323e77cf8), \

[BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0))

[BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0)

#define BT\_GAP\_SCAN\_FAST\_WINDOW

**Definition** gap.h:719

[BT\_GAP\_SCAN\_FAST\_INTERVAL](group__bt__gap__defines.md#ga747caa714962215453a966a323e77cf8)

#define BT\_GAP\_SCAN\_FAST\_INTERVAL

**Definition** gap.h:718

[BT\_LE\_SCAN\_PARAM](#ga57ace75133343ba8de7fa965f452ee3d)

#define BT\_LE\_SCAN\_PARAM(\_type, \_options, \_interval, \_window)

Helper to declare scan parameters inline.

**Definition** bluetooth.h:2305

[BT\_LE\_SCAN\_TYPE\_ACTIVE](#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22)

@ BT\_LE\_SCAN\_TYPE\_ACTIVE

Scan and request additional information from advertisers.

**Definition** bluetooth.h:2151

[BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394)

@ BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE

Filter duplicates.

**Definition** bluetooth.h:2122

Helper macro to enable active scanning to discover new devices.

## [◆ ](#ga9bd9701db0459c066ed7c18343f60911)BT\_LE\_SCAN\_ACTIVE\_CONTINUOUS

| #define BT\_LE\_SCAN\_ACTIVE\_CONTINUOUS |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_SCAN\_PARAM](#ga57ace75133343ba8de7fa965f452ee3d)([BT\_LE\_SCAN\_TYPE\_ACTIVE](#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22), \

[BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394), \

[BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN](group__bt__gap__defines.md#gae9356673ee78d9abb27891738344513a), \

[BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0))

[BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN](group__bt__gap__defines.md#gae9356673ee78d9abb27891738344513a)

#define BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN

**Definition** gap.h:717

Helper macro to enable active scanning to discover new devices with window == interval.

Continuous scanning should be used to maximize the chances of receiving advertising packets.

## [◆ ](#ga06380c4ae6289c704a143b9d192bc35f)BT\_LE\_SCAN\_CODED\_ACTIVE

| #define BT\_LE\_SCAN\_CODED\_ACTIVE |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_SCAN\_PARAM](#ga57ace75133343ba8de7fa965f452ee3d)([BT\_LE\_SCAN\_TYPE\_ACTIVE](#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22), \

[BT\_LE\_SCAN\_OPT\_CODED](#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb) | \

[BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394), \

[BT\_GAP\_SCAN\_FAST\_INTERVAL](group__bt__gap__defines.md#ga747caa714962215453a966a323e77cf8), \

[BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0))

[BT\_LE\_SCAN\_OPT\_CODED](#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb)

@ BT\_LE\_SCAN\_OPT\_CODED

Enable scan on coded PHY (Long Range).

**Definition** bluetooth.h:2128

Helper macro to enable active scanning to discover new devices.

Include scanning on Coded PHY in addition to 1M PHY.

## [◆ ](#ga1e5a4589304babc6b0d49019ebcff6b0)BT\_LE\_SCAN\_CODED\_PASSIVE

| #define BT\_LE\_SCAN\_CODED\_PASSIVE |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_SCAN\_PARAM](#ga57ace75133343ba8de7fa965f452ee3d)([BT\_LE\_SCAN\_TYPE\_PASSIVE](#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006), \

[BT\_LE\_SCAN\_OPT\_CODED](#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb) | \

[BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394), \

[BT\_GAP\_SCAN\_FAST\_INTERVAL](group__bt__gap__defines.md#ga747caa714962215453a966a323e77cf8), \

[BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0))

[BT\_LE\_SCAN\_TYPE\_PASSIVE](#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006)

@ BT\_LE\_SCAN\_TYPE\_PASSIVE

Scan without requesting additional information from advertisers.

**Definition** bluetooth.h:2142

Helper macro to enable passive scanning to discover new devices.

Include scanning on Coded PHY in addition to 1M PHY.

This macro should be used if information required for device identification (e.g., UUID) are known to be placed in Advertising Data.

## [◆ ](#ga33e84f4ccbf4d0aa2527e9fe1086e252)BT\_LE\_SCAN\_OPT\_FILTER\_WHITELIST

| #define BT\_LE\_SCAN\_OPT\_FILTER\_WHITELIST   \_\_DEPRECATED\_MACRO [BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST](#gga5afc3803e9a80e829597375fcf2a2cf3af7a25b6790b138b2b88de3c7d81cb0ae) |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

## [◆ ](#ga57ace75133343ba8de7fa965f452ee3d)BT\_LE\_SCAN\_PARAM

| #define BT\_LE\_SCAN\_PARAM | ( |  | *\_type*, |
| --- | --- | --- | --- |
|  |  |  | *\_options*, |
|  |  |  | *\_interval*, |
|  |  |  | *\_window* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

((struct [bt\_le\_scan\_param](structbt__le__scan__param.md)[]) { \

BT\_LE\_SCAN\_PARAM\_INIT(\_type, \_options, \_interval, \_window) \

})

[bt\_le\_scan\_param](structbt__le__scan__param.md)

LE scan parameters.

**Definition** bluetooth.h:2155

Helper to declare scan parameters inline.

Parameters
:   | \_type | Scan Type, BT\_LE\_SCAN\_TYPE\_ACTIVE or BT\_LE\_SCAN\_TYPE\_PASSIVE. |
    | --- | --- |
    | \_options | Scan options |
    | \_interval | Scan Interval (N \* 0.625 ms) |
    | \_window | Scan Window (N \* 0.625 ms) |

## [◆ ](#gac9f372ca16afb1c2f0e100c5b1b94cd5)BT\_LE\_SCAN\_PARAM\_INIT

| #define BT\_LE\_SCAN\_PARAM\_INIT | ( |  | *\_type*, |
| --- | --- | --- | --- |
|  |  |  | *\_options*, |
|  |  |  | *\_interval*, |
|  |  |  | *\_window* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

{ \

.type = (\_type), \

.options = (\_options), \

.interval = (\_interval), \

.window = (\_window), \

.timeout = 0, \

.interval\_coded = 0, \

.window\_coded = 0, \

}

Initialize scan parameters.

Parameters
:   | \_type | Scan Type, BT\_LE\_SCAN\_TYPE\_ACTIVE or BT\_LE\_SCAN\_TYPE\_PASSIVE. |
    | --- | --- |
    | \_options | Scan options |
    | \_interval | Scan Interval (N \* 0.625 ms) |
    | \_window | Scan Window (N \* 0.625 ms) |

## [◆ ](#ga8ceaef6f0fbf4fe2d76d47e8f59aeb11)BT\_LE\_SCAN\_PASSIVE

| #define BT\_LE\_SCAN\_PASSIVE |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_SCAN\_PARAM](#ga57ace75133343ba8de7fa965f452ee3d)([BT\_LE\_SCAN\_TYPE\_PASSIVE](#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006), \

[BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394), \

[BT\_GAP\_SCAN\_FAST\_INTERVAL](group__bt__gap__defines.md#ga747caa714962215453a966a323e77cf8), \

[BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0))

Helper macro to enable passive scanning to discover new devices.

This macro should be used if information required for device identification (e.g., UUID) are known to be placed in Advertising Data.

## [◆ ](#ga8d8ccc9ea1db2c96deae1603ec1c78a3)BT\_LE\_SCAN\_PASSIVE\_CONTINUOUS

| #define BT\_LE\_SCAN\_PASSIVE\_CONTINUOUS |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

**Value:**

[BT\_LE\_SCAN\_PARAM](#ga57ace75133343ba8de7fa965f452ee3d)([BT\_LE\_SCAN\_TYPE\_PASSIVE](#gga2383d7ea529bcaadb727dd11ecbe5f9aa731c507ed451eb6f8f8372849185b006), \

[BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE](#gga5afc3803e9a80e829597375fcf2a2cf3a0af65ac48e068f7e6f1815cb151d4394), \

[BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN](group__bt__gap__defines.md#gae9356673ee78d9abb27891738344513a), \

[BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0))

Helper macro to enable passive scanning to discover new devices with window==interval.

This macro should be used if information required for device identification (e.g., UUID) are known to be placed in Advertising Data.

## Typedef Documentation

## [◆ ](#ga1c53d22b6e2dee38c825c58f3eeee9b4)bt\_le\_scan\_cb\_t

| typedef void bt\_le\_scan\_cb\_t(const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) rssi, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adv\_type, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Callback type for reporting LE scan results.

A function of this type is given to the [bt\_le\_scan\_start()](#gac5e19c26b53a08dadb8efa7ecc692ad6) function and will be called for any discovered LE device.

Parameters
:   | addr | Advertiser LE address and type. |
    | --- | --- |
    | rssi | Strength of advertiser signal. |
    | adv\_type | Type of advertising response from advertiser. Uses the BT\_GAP\_ADV\_TYPE\_\* values. |
    | buf | Buffer containing advertiser data. |

## [◆ ](#ga5398783ab4a5dc854b18e37fb10774eb)bt\_ready\_cb\_t

| typedef void(\* bt\_ready\_cb\_t) (int err) |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Callback for notifying that Bluetooth has been enabled.

Parameters
:   | err | zero on success or (negative) error code otherwise. |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#ga654b0098c5f04a9c85a65f86b8f95dee)anonymous enum

| anonymous enum |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Advertising options.

| Enumerator | |
| --- | --- |
| BT\_LE\_ADV\_OPT\_NONE | Convenience value when no options are specified. |
| BT\_LE\_ADV\_OPT\_CONNECTABLE | Advertise as connectable.  **[Deprecated](deprecated.md#_deprecated000009)**  Use [BT\_LE\_ADV\_OPT\_CONN](#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169) instead.  Advertise as connectable. If not connectable then the type of advertising is determined by providing scan response data. The advertiser address is determined by the type of advertising and/or enabling privacy   ``` CONFIG_BT_PRIVACY ```   .  Starting connectable advertising preallocates a connection object. If this fails, the API returns `-ENOMEM`.  When an advertiser set results in a connection creation, the controller automatically disables that advertising set.  If the advertising set was started with [bt\_le\_adv\_start](#gad2e3caef88d52d720e8e4d21df767b02) without [BT\_LE\_ADV\_OPT\_ONE\_TIME](#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2), the host will attempt to resume the advertiser under some conditions. |
| BT\_LE\_ADV\_OPT\_ONE\_TIME | Advertise one time.  **[Deprecated](deprecated.md#_deprecated000010)**  Use [BT\_LE\_ADV\_OPT\_CONN](#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169) instead.  Don't try to resume connectable advertising after a connection. This option is only meaningful when used together with BT\_LE\_ADV\_OPT\_CONNECTABLE. If set the advertising will be stopped when [bt\_le\_adv\_stop()](#ga1776e310b9d80898e6b32d50c4fe0b49) is called or when an incoming (peripheral) connection happens. If this option is not set the stack will take care of keeping advertising enabled even as connections occur. If Advertising directed or the advertiser was started with [bt\_le\_ext\_adv\_start](#gaf0f436c55482d9429f674303ae3aa815) then this behavior is the default behavior and this flag has no effect. |
| BT\_LE\_ADV\_OPT\_CONN | Connectable advertising.  Starting connectable advertising preallocates a connection object. If this fails, the API returns `-ENOMEM`.  The advertising set stops immediately after it creates a connection. This happens automatically in the controller.  Note  To continue advertising after a connection is created, the application should listen for the [bt\_conn\_cb::connected](structbt__conn__cb.md#ab3618150bfeea9492095ba27ce978c69 "bt_conn_cb::connected") event and start the advertising set again. Note that the advertiser cannot be started when all connection objects are in use. In that case, defer starting the advertiser until [bt\_conn\_cb::recycled](structbt__conn__cb.md#a1bd8d99988ad0ae3f79aad3d03fcbd8b "bt_conn_cb::recycled"). To continue after a disconnection, listen for [bt\_conn\_cb::recycled](structbt__conn__cb.md#a1bd8d99988ad0ae3f79aad3d03fcbd8b "bt_conn_cb::recycled"). |
| BT\_LE\_ADV\_OPT\_USE\_IDENTITY | Advertise using identity address.  Advertise using the identity address as the advertiser address.  Warning  This will compromise the privacy of the device, so care must be taken when using this option.  Note  The address used for advertising will not be the same as returned by [bt\_le\_oob\_get\_local](#ga296d1adf3c9ed2f2c65bb75b887d59ee), instead [bt\_id\_get](#ga06d0ae35cbf4382679cc3cfe612cee4d) should be used to get the LE address. |
| BT\_LE\_ADV\_OPT\_USE\_NAME | Advertise using GAP device name.  **[Deprecated](deprecated.md#_deprecated000011)**  This option will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)  Include the GAP device name automatically when advertising. By default the GAP device name is put at the end of the scan response data. When advertising using [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) and not [BT\_LE\_ADV\_OPT\_SCANNABLE](#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) then it will be put at the end of the advertising data. If the GAP device name does not fit into advertising data it will be converted to a shortened name if possible. [BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD](#gga654b0098c5f04a9c85a65f86b8f95deea0a9642077d93cf9c0eb42f64a9e34e73) can be used to force the device name to appear in the advertising data of an advert with scan response data.  The application can set the device name itself by including the following in the advertising data.  BT\_DATA(BT\_DATA\_NAME\_COMPLETE, name, sizeof(name) - 1) |
| BT\_LE\_ADV\_OPT\_DIR\_MODE\_LOW\_DUTY | Low duty cycle directed advertising.  Use low duty directed advertising mode, otherwise high duty mode will be used. |
| BT\_LE\_ADV\_OPT\_DIR\_ADDR\_RPA | Directed advertising to privacy-enabled peer.  Enable use of Resolvable Private Address (RPA) as the target address in directed advertisements. This is required if the remote device is privacy-enabled and supports address resolution of the target address in directed advertisement. It is the responsibility of the application to check that the remote device supports address resolution of directed advertisements by reading its Central Address Resolution characteristic. |
| BT\_LE\_ADV\_OPT\_FILTER\_SCAN\_REQ | Use filter accept list to filter devices that can request scan response data. |
| BT\_LE\_ADV\_OPT\_FILTER\_CONN | Use filter accept list to filter devices that can connect. |
| BT\_LE\_ADV\_OPT\_NOTIFY\_SCAN\_REQ | Notify the application when a scan response data has been sent to an active scanner. |
| BT\_LE\_ADV\_OPT\_SCANNABLE | Support scan response data.  When used together with [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) then this option cannot be used together with the [BT\_LE\_ADV\_OPT\_CONN](#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169) option. When used together with [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) then scan response data must be set. |
| BT\_LE\_ADV\_OPT\_EXT\_ADV | Advertise with extended advertising.  This options enables extended advertising in the advertising set. In extended advertising the advertising set will send a small header packet on the three primary advertising channels. This small header points to the advertising data packet that will be sent on one of the 37 secondary advertising channels. The advertiser will send primary advertising on LE 1M PHY, and secondary advertising on LE 2M PHY. Connections will be established on LE 2M PHY.  Without this option the advertiser will send advertising data on the three primary advertising channels.  Note  Enabling this option requires extended advertising support in the peer devices scanning for advertisement packets.  This cannot be used with [bt\_le\_adv\_start()](#gad2e3caef88d52d720e8e4d21df767b02). |
| BT\_LE\_ADV\_OPT\_NO\_2M | Disable use of LE 2M PHY on the secondary advertising channel.  Disabling the use of LE 2M PHY could be necessary if scanners don't support the LE 2M PHY. The advertiser will send primary advertising on LE 1M PHY, and secondary advertising on LE 1M PHY. Connections will be established on LE 1M PHY.  Note  Cannot be set if BT\_LE\_ADV\_OPT\_CODED is set.  Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab). |
| BT\_LE\_ADV\_OPT\_CODED | Advertise on the LE Coded PHY (Long Range).  The advertiser will send both primary and secondary advertising on the LE Coded PHY. This gives the advertiser increased range with the trade-off of lower data rate and higher power consumption. Connections will be established on LE Coded PHY.  Note  Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) |
| BT\_LE\_ADV\_OPT\_ANONYMOUS | Advertise without a device address (identity or RPA).  Note  Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) |
| BT\_LE\_ADV\_OPT\_USE\_TX\_POWER | Advertise with transmit power.  Note  Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) |
| BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_37 | Disable advertising on channel index 37. |
| BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_38 | Disable advertising on channel index 38. |
| BT\_LE\_ADV\_OPT\_DISABLE\_CHAN\_39 | Disable advertising on channel index 39. |
| BT\_LE\_ADV\_OPT\_FORCE\_NAME\_IN\_AD | Put GAP device name into advert data.  **[Deprecated](deprecated.md#_deprecated000012)**  This option will be removed in the near future, see [https://github.com/zephyrproject-rtos/zephyr/issues/71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686)  Will place the GAP device name into the advertising data rather than the scan response data.  Note  Requires [BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398) |
| BT\_LE\_ADV\_OPT\_USE\_NRPA | Advertise using a Non-Resolvable Private Address.  A new NRPA is set when updating the advertising parameters.  This is an advanced feature; most users will want to enable   ``` CONFIG_BT_EXT_ADV ```   instead.  Note  Not implemented when  ``` CONFIG_BT_PRIVACY ```  .  Mutually exclusive with BT\_LE\_ADV\_OPT\_USE\_IDENTITY. |

## [◆ ](#ga9cf9b0d1941502642e50fcfc2d686bca)anonymous enum

| anonymous enum |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Periodic advertising sync options.

| Enumerator | |
| --- | --- |
| BT\_LE\_PER\_ADV\_SYNC\_OPT\_NONE | Convenience value when no options are specified. |
| BT\_LE\_PER\_ADV\_SYNC\_OPT\_USE\_PER\_ADV\_LIST | Use the periodic advertising list to sync with advertiser.  When this option is set, the address and SID of the parameters are ignored. |
| BT\_LE\_PER\_ADV\_SYNC\_OPT\_REPORTING\_INITIALLY\_DISABLED | Disables periodic advertising reports.  No advertisement reports will be handled until enabled. |
| BT\_LE\_PER\_ADV\_SYNC\_OPT\_FILTER\_DUPLICATE | Filter duplicate Periodic Advertising reports. |
| BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOA | Sync with Angle of Arrival (AoA) constant tone extension. |
| BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_1US | Sync with Angle of Departure (AoD) 1 us constant tone extension. |
| BT\_LE\_PER\_ADV\_SYNC\_OPT\_DONT\_SYNC\_AOD\_2US | Sync with Angle of Departure (AoD) 2 us constant tone extension. |
| BT\_LE\_PER\_ADV\_SYNC\_OPT\_SYNC\_ONLY\_CONST\_TONE\_EXT | Do not sync to packets without a constant tone extension. |

## [◆ ](#ga9c50ffe9d076ca7be5bdd72b91e53e15)anonymous enum

| anonymous enum |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Periodic Advertising Sync Transfer options.

| Enumerator | |
| --- | --- |
| BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_NONE | Convenience value when no options are specified. |
| BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOA | No Angle of Arrival (AoA).  Do not sync with Angle of Arrival (AoA) constant tone extension |
| BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_1US | No Angle of Departure (AoD) 1 us.  Do not sync with Angle of Departure (AoD) 1 us constant tone extension |
| BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_NO\_AOD\_2US | No Angle of Departure (AoD) 2.  Do not sync with Angle of Departure (AoD) 2 us constant tone extension |
| BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_SYNC\_ONLY\_CTE | Only sync to packets with constant tone extension. |
| BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED | Sync to received PAST packets but don't generate sync reports.  This option must not be set at the same time as [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES](#gga9c50ffe9d076ca7be5bdd72b91e53e15ad924f620ed6fdadbbea03f8e343b9d0c). |
| BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_FILTER\_DUPLICATES | Sync to received PAST packets and generate sync reports with duplicate filtering.  This option must not be set at the same time as [BT\_LE\_PER\_ADV\_SYNC\_TRANSFER\_OPT\_REPORTING\_INITIALLY\_DISABLED](#gga9c50ffe9d076ca7be5bdd72b91e53e15a3f0be549ca5cac1cfbdec2f2227e73dc). |

## [◆ ](#ga5afc3803e9a80e829597375fcf2a2cf3)anonymous enum

| anonymous enum |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_LE\_SCAN\_OPT\_NONE | Convenience value when no options are specified. |
| BT\_LE\_SCAN\_OPT\_FILTER\_DUPLICATE | Filter duplicates. |
| BT\_LE\_SCAN\_OPT\_FILTER\_ACCEPT\_LIST | Filter using filter accept list. |
| BT\_LE\_SCAN\_OPT\_CODED | Enable scan on coded PHY (Long Range). |
| BT\_LE\_SCAN\_OPT\_NO\_1M | Disable scan on 1M phy.  Note  Requires [BT\_LE\_SCAN\_OPT\_CODED](#gga5afc3803e9a80e829597375fcf2a2cf3a16f171c649dd090333e9822a92b4bbdb). |

## [◆ ](#ga2383d7ea529bcaadb727dd11ecbe5f9a)anonymous enum

| anonymous enum |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_LE\_SCAN\_TYPE\_PASSIVE | Scan without requesting additional information from advertisers. |
| BT\_LE\_SCAN\_TYPE\_ACTIVE | Scan and request additional information from advertisers.  Using this scan type will automatically send scan requests to all devices. Scan responses are received in the same manner and using the same callbacks as advertising reports. |

## [◆ ](#ga592195c57b12f7224b6d07133e60fc4a)anonymous enum

| anonymous enum |
| --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Periodic Advertising options.

| Enumerator | |
| --- | --- |
| BT\_LE\_PER\_ADV\_OPT\_NONE | Convenience value when no options are specified. |
| BT\_LE\_PER\_ADV\_OPT\_USE\_TX\_POWER | Advertise with transmit power.  Note  Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) |
| BT\_LE\_PER\_ADV\_OPT\_INCLUDE\_ADI | Advertise with included AdvDataInfo (ADI).  Note  Requires [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) |

## Function Documentation

## [◆ ](#ga430de0ad30da7322c5353941f1f6a133)bt\_br\_discovery\_cb\_register()

| void bt\_br\_discovery\_cb\_register | ( | struct [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[classic.h](classic_8h.md)>`

Register discovery packet callbacks.

Adds the callback structure to the list of callback structures that monitors inquiry activity.

This callback will be called for all inquiry activity, regardless of what API was used to start the discovery.

Parameters
:   | cb | Callback struct. Must point to memory that remains valid. |
    | --- | --- |

## [◆ ](#ga25ab96ac005237aee739bf32fc1aac94)bt\_br\_discovery\_cb\_unregister()

| void bt\_br\_discovery\_cb\_unregister | ( | struct [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[classic.h](classic_8h.md)>`

Unregister discovery packet callbacks.

Remove the callback structure from the list of discovery callbacks.

Parameters
:   | cb | Callback struct. Must point to memory that remains valid. |
    | --- | --- |

## [◆ ](#ga9760190192dde5c498ec96628468be8d)bt\_br\_discovery\_start()

| int bt\_br\_discovery\_start | ( | const struct [bt\_br\_discovery\_param](structbt__br__discovery__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \* | *results*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count* ) |

`#include <[classic.h](classic_8h.md)>`

Start BR/EDR discovery.

Start BR/EDR discovery (inquiry) and provide results through the specified callback. The discovery results will be notified through callbacks registered by [bt\_br\_discovery\_cb\_register](#ga430de0ad30da7322c5353941f1f6a133). If more inquiry results were received during session than fits in provided result storage, only ones with highest RSSI will be reported.

Parameters
:   | param | Discovery parameters. |
    | --- | --- |
    | results | Storage for discovery results. |
    | count | Number of results in storage. Valid range: 1-255. |

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error

## [◆ ](#ga567c71b49399fe7e1a5593edbf005e3a)bt\_br\_discovery\_stop()

| int bt\_br\_discovery\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[classic.h](classic_8h.md)>`

Stop BR/EDR discovery.

Stops ongoing BR/EDR discovery. If discovery was stopped by this call results won't be reported

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

## [◆ ](#ga2ec860d06c45098624b106b59fbab634)bt\_br\_oob\_get\_local()

| int bt\_br\_oob\_get\_local | ( | struct [bt\_br\_oob](structbt__br__oob.md) \* | *oob* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[classic.h](classic_8h.md)>`

Get BR/EDR local Out Of Band information.

This function allows to get local controller information that are useful for Out Of Band pairing or connection creation process.

Parameters
:   | oob | Out Of Band information |
    | --- | --- |

## [◆ ](#ga80aed18a099948bef8f3649ad537e541)bt\_br\_set\_connectable()

| int bt\_br\_set\_connectable | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[classic.h](classic_8h.md)>`

Enable/disable set controller in connectable state.

Allows make local controller to be connectable. It means the controller start listen to devices requests on PAGE SCAN channel. If disabled also resets discoverability if was set.

Parameters
:   | enable | Value allowing/disallowing controller to be connectable. |
    | --- | --- |

Returns
:   Negative if fail set to requested state or requested state has been already set. Zero if done successfully.

## [◆ ](#gad3b9075cc9bab5c1ae37514a6dfe555c)bt\_br\_set\_discoverable()

| int bt\_br\_set\_discoverable | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[classic.h](classic_8h.md)>`

Enable/disable set controller in discoverable state.

Allows make local controller to listen on INQUIRY SCAN channel and responds to devices making general inquiry. To enable this state it's mandatory to first be in connectable state.

Parameters
:   | enable | Value allowing/disallowing controller to become discoverable. |
    | --- | --- |

Returns
:   Negative if fail set to requested state or requested state has been already set. Zero if done successfully.

## [◆ ](#ga8046c2b06d3dad0d6c8184de492517d2)bt\_configure\_data\_path()

| int bt\_configure\_data\_path | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dir*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *vs\_config\_len*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *vs\_config* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Configure vendor data path.

Request the Controller to configure the data transport path in a given direction between the Controller and the Host.

Parameters
:   | dir | Direction to be configured, BT\_HCI\_DATAPATH\_DIR\_HOST\_TO\_CTLR or BT\_HCI\_DATAPATH\_DIR\_CTLR\_TO\_HOST |
    | --- | --- |
    | id | Vendor specific logical transport channel ID, range [BT\_HCI\_DATAPATH\_ID\_VS..BT\_HCI\_DATAPATH\_ID\_VS\_END] |
    | vs\_config\_len | Length of additional vendor specific configuration data |
    | vs\_config | Pointer to additional vendor specific configuration data |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga3d2c6adc42eb9510734630f38d921b9a)bt\_data\_get\_len()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_data\_get\_len | ( | const struct [bt\_data](structbt__data.md) | *data*[], |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_count* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Get the total size (in bytes) of a given set of [bt\_data](structbt__data.md "bt_data") structures.

Parameters
:   | [in] | data | Array of [bt\_data](structbt__data.md "bt_data") structures. |
    | --- | --- | --- |
    | [in] | data\_count | Number of [bt\_data](structbt__data.md "bt_data") structures in `data`. |

Returns
:   Size of the concatenated data, built from the [bt\_data](structbt__data.md "bt_data") structure set.

## [◆ ](#ga652eef01e5256e0d820cd1f4db877429)bt\_data\_parse()

| void bt\_data\_parse | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *ad*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | *func*)(struct [bt\_data](structbt__data.md) \*data, void \*user\_data), |
|  |  | void \* | *user\_data* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Helper for parsing advertising (or EIR or OOB) data.

A helper for parsing the basic data types used for Extended Inquiry Response (EIR), Advertising Data (AD), and OOB data blocks. The most common scenario is to call this helper on the advertising data received in the callback that was given to [bt\_le\_scan\_start()](#gac5e19c26b53a08dadb8efa7ecc692ad6).

Warning
:   This helper function will consume ad when parsing. The user should make a copy if the original data is to be used afterwards

Parameters
:   | ad | Advertising data as given to the [bt\_le\_scan\_cb\_t](#ga1c53d22b6e2dee38c825c58f3eeee9b4) callback. |
    | --- | --- |
    | func | Callback function which will be called for each element that's found in the data. The callback should return true to continue parsing, or false to stop parsing. |
    | user\_data | User data to be passed to the callback. |

## [◆ ](#ga3c067b16468ebd17973faeded0fc83c9)bt\_data\_serialize()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_data\_serialize | ( | const struct [bt\_data](structbt__data.md) \* | *input*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *output* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Serialize a [bt\_data](structbt__data.md "bt_data") struct into an advertising structure (a flat byte array).

The data are formatted according to the Bluetooth Core Specification v. 5.4, vol. 3, part C, 11.

Parameters
:   | [in] | input | Single [bt\_data](structbt__data.md "bt_data") structure to read from. |
    | --- | --- | --- |
    | [out] | output | Buffer large enough to store the advertising structure in `input`. The size of it must be at least the size of the input->data\_len + 2 (for the type and the length). |

Returns
:   Number of bytes written in `output`.

## [◆ ](#ga0a58e5a050170e84a80f8d5bb3516ec7)bt\_disable()

| int bt\_disable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Disable Bluetooth.

Disable Bluetooth. Can't be called before bt\_enable has completed.

This API will clear all configured identities and keys that are not persistently stored with

```
CONFIG_BT_SETTINGS
```

. These can be restored with [settings\_load()](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648 "Load serialized items from registered persistence sources.") before reenabling the stack.

This API does *not* clear previously registered callbacks like [bt\_le\_scan\_cb\_register](#ga80e870fa1de40c404c64624bef439067), [bt\_conn\_cb\_register](group__bt__conn.md#gaa9b79cd44734c1e560d6f30509be4d0b "bt_conn_cb_register") AND [bt\_br\_discovery\_cb\_register](#ga430de0ad30da7322c5353941f1f6a133). That is, the application shall not re-register them when the Bluetooth subsystem is re-enabled later.

Close and release HCI resources. Result is architecture dependent.

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gac45d16bfe21c3c38e834c293e5ebc42b)bt\_enable()

| int bt\_enable | ( | [bt\_ready\_cb\_t](#ga5398783ab4a5dc854b18e37fb10774eb) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Enable Bluetooth.

Enable Bluetooth. Must be the called before any calls that require communication with the local Bluetooth hardware.

When

```
CONFIG_BT_SETTINGS
```

is enabled, the application must load the Bluetooth settings after this API call successfully completes before Bluetooth APIs can be used. Loading the settings before calling this function is insufficient. Bluetooth settings can be loaded with [settings\_load()](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648 "Load serialized items from registered persistence sources.") or [settings\_load\_subtree()](group__settings.md#gab80e8a21c80243359b652386f7ce2424 "Load limited set of serialized items from registered persistence sources.") with argument "bt". The latter selectively loads only Bluetooth settings and is recommended if [settings\_load()](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648 "Load serialized items from registered persistence sources.") has been called earlier.

Parameters
:   | cb | Callback to notify completion or NULL to perform the enabling synchronously. The callback is called from the system workqueue. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gaad380b7f8984f8522c1b79f9bdc04905)bt\_foreach\_bond()

| void bt\_foreach\_bond | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, |
| --- | --- | --- | --- |
|  |  | void(\* | *func*)(const struct [bt\_bond\_info](structbt__bond__info.md) \*info, void \*user\_data), |
|  |  | void \* | *user\_data* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Iterate through all existing bonds.

Parameters
:   | id | Local identity (mostly just BT\_ID\_DEFAULT). |
    | --- | --- |
    | func | Function to call for each bond. |
    | user\_data | Data to pass to the callback function. |

## [◆ ](#ga35b76ea7ce79721e47ca4164e08b2dfb)bt\_get\_appearance()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_get\_appearance | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Get local Bluetooth appearance.

Bluetooth Appearance is a description of the external appearance of a device in terms of an Appearance Value.

See also
:   [https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf](https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf)

Returns
:   Appearance Value of local Bluetooth host.

## [◆ ](#gad922d894b25e86de3f81ce77200a13fd)bt\_get\_name()

| const char \* bt\_get\_name | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Get Bluetooth Device Name.

Get Bluetooth GAP Device Name.

Returns
:   Bluetooth Device Name

## [◆ ](#gae11eb8ad254418c38a0e8689df25a159)bt\_id\_create()

| int bt\_id\_create | ( | [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *irk* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Create a new identity.

Create a new identity using the given address and IRK. This function can be called before calling [bt\_enable()](#gac45d16bfe21c3c38e834c293e5ebc42b). However, the new identity will only be stored persistently in flash when this API is used after [bt\_enable()](#gac45d16bfe21c3c38e834c293e5ebc42b). The reason is that the persistent settings are loaded after [bt\_enable()](#gac45d16bfe21c3c38e834c293e5ebc42b) and would therefore cause potential conflicts with the stack blindly overwriting what's stored in flash. The identity will also not be written to flash in case a pre-defined address is provided, since in such a situation the app clearly has some place it got the address from and will be able to repeat the procedure on every power cycle, i.e. it would be redundant to also store the information in flash.

Generating random static address or random IRK is not supported when calling this function before [bt\_enable()](#gac45d16bfe21c3c38e834c293e5ebc42b).

If the application wants to have the stack randomly generate identities and store them in flash for later recovery, the way to do it would be to first initialize the stack (using bt\_enable), then call [settings\_load()](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648 "Load serialized items from registered persistence sources."), and after that check with [bt\_id\_get()](#ga06d0ae35cbf4382679cc3cfe612cee4d) how many identities were recovered. If an insufficient amount of identities were recovered the app may then call [bt\_id\_create()](#gae11eb8ad254418c38a0e8689df25a159) to create new ones.

If supported by the HCI driver (indicated by setting

```
CONFIG_BT_HCI_SET_PUBLIC_ADDR
```

), the first call to this function can be used to set the controller's public identity address. This call must happen before calling [bt\_enable()](#gac45d16bfe21c3c38e834c293e5ebc42b). Subsequent calls always add/generate random static addresses.

Parameters
:   | addr | Address to use for the new identity. If NULL or initialized to BT\_ADDR\_LE\_ANY the stack will generate a new random static address for the identity and copy it to the given parameter upon return from this function (in case the parameter was non-NULL). |
    | --- | --- |
    | irk | Identity Resolving Key (16 bytes) to be used with this identity. If set to all zeroes or NULL, the stack will generate a random IRK for the identity and copy it back to the parameter upon return from this function (in case the parameter was non-NULL). If privacy  ``` CONFIG_BT_PRIVACY ```  is not enabled this parameter must be NULL. |

Returns
:   Identity identifier (>= 0) in case of success, or a negative error code on failure.

## [◆ ](#gaf6cd906690a51ebed04bea4f4ef716ff)bt\_id\_delete()

| int bt\_id\_delete | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Delete an identity.

When given a valid identity this function will disconnect any connections created using it, remove any pairing keys or other data associated with it, and then flag is as deleted, so that it can not be used for any operations. To take back into use the slot the identity was occupying the [bt\_id\_reset()](#gabb3353edc8a3a8d29a0370049b20cbe4) API needs to be used.

Note
:   the default identity (BT\_ID\_DEFAULT) cannot be deleted, i.e. this API will return an error if asked to do that.

Parameters
:   | id | Existing identity identifier. |
    | --- | --- |

Returns
:   0 in case of success, or a negative error code on failure.

## [◆ ](#ga06d0ae35cbf4382679cc3cfe612cee4d)bt\_id\_get()

| void bt\_id\_get | ( | [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addrs*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *count* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Get the currently configured identities.

Returns an array of the currently configured identity addresses. To make sure all available identities can be retrieved, the number of elements in the *addrs* array should be CONFIG\_BT\_ID\_MAX. The identity identifier that some APIs expect (such as advertising parameters) is simply the index of the identity in the *addrs* array.

If *addrs* is passed as NULL, then returned *count* contains the count of all available identities that can be retrieved with a subsequent call to this function with non-NULL *addrs* parameter.

Note
:   Deleted identities may show up as [BT\_ADDR\_LE\_ANY](group__bt__addr.md#ga17e9efacd50c682b2f709c217e920d48 "BT_ADDR_LE_ANY") in the returned array.

Parameters
:   | addrs | Array where to store the configured identities. |
    | --- | --- |
    | count | Should be initialized to the array size. Once the function returns it will contain the number of returned identities. |

## [◆ ](#gabb3353edc8a3a8d29a0370049b20cbe4)bt\_id\_reset()

| int bt\_id\_reset | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, |
| --- | --- | --- | --- |
|  |  | [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *irk* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Reset/reclaim an identity for reuse.

The semantics of the *addr* and *irk* parameters of this function are the same as with [bt\_id\_create()](#gae11eb8ad254418c38a0e8689df25a159). The difference is the first *id* parameter that needs to be an existing identity (if it doesn't exist this function will return an error). When given an existing identity this function will disconnect any connections created using it, remove any pairing keys or other data associated with it, and then create a new identity in the same slot, based on the *addr* and *irk* parameters.

Note
:   the default identity (BT\_ID\_DEFAULT) cannot be reset, i.e. this API will return an error if asked to do that.

Parameters
:   | id | Existing identity identifier. |
    | --- | --- |
    | addr | Address to use for the new identity. If NULL or initialized to BT\_ADDR\_LE\_ANY the stack will generate a new static random address for the identity and copy it to the given parameter upon return from this function (in case the parameter was non-NULL). |
    | irk | Identity Resolving Key (16 bytes) to be used with this identity. If set to all zeroes or NULL, the stack will generate a random IRK for the identity and copy it back to the parameter upon return from this function (in case the parameter was non-NULL). If privacy  ``` CONFIG_BT_PRIVACY ```  is not enabled this parameter must be NULL. |

Returns
:   Identity identifier (>= 0) in case of success, or a negative error code on failure.

## [◆ ](#gaa8bf6854e7ad1fe7e0805737576e5d1a)bt\_is\_ready()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_is\_ready | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Check if Bluetooth is ready.

Returns
:   true when Bluetooth is ready, false otherwise

## [◆ ](#gad2e3caef88d52d720e8e4d21df767b02)bt\_le\_adv\_start()

| int bt\_le\_adv\_start | ( | const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_data](structbt__data.md) \* | *ad*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *ad\_len*, |
|  |  | const struct [bt\_data](structbt__data.md) \* | *sd*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *sd\_len* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Start advertising.

Set advertisement data, scan response data, advertisement parameters and start advertising.

When the advertisement parameter peer address has been set the advertising will be directed to the peer. In this case advertisement data and scan response data parameters are ignored. If the mode is high duty cycle the timeout will be [BT\_GAP\_ADV\_HIGH\_DUTY\_CYCLE\_MAX\_TIMEOUT](group__bt__gap__defines.md#gabe483d4dd601b11ac3eea570c962b1ec "BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT").

This function cannot be used with [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) in the `param.options`. For extended advertising, the bt\_le\_ext\_adv\_\* functions must be used.

Parameters
:   | param | Advertising parameters. |
    | --- | --- |
    | ad | Data to be used in advertisement packets. |
    | ad\_len | Number of elements in ad |
    | sd | Data to be used in scan response packets. |
    | sd\_len | Number of elements in sd |

Returns
:   Zero on success or (negative) error code otherwise.
:   -ENOMEM No free connection objects available for connectable advertiser.
:   -ECONNREFUSED When connectable advertising is requested and there is already maximum number of connections established in the controller. This error code is only guaranteed when using Zephyr controller, for other controllers code returned in this case may be -EIO.

## [◆ ](#ga1776e310b9d80898e6b32d50c4fe0b49)bt\_le\_adv\_stop()

| int bt\_le\_adv\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Stop advertising.

Stops ongoing advertising.

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga9a406ebfefac3dd09935a4ae0e317817)bt\_le\_adv\_update\_data()

| int bt\_le\_adv\_update\_data | ( | const struct [bt\_data](structbt__data.md) \* | *ad*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *ad\_len*, |
|  |  | const struct [bt\_data](structbt__data.md) \* | *sd*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *sd\_len* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Update advertising.

Update advertisement and scan response data.

Parameters
:   | ad | Data to be used in advertisement packets. |
    | --- | --- |
    | ad\_len | Number of elements in ad |
    | sd | Data to be used in scan response packets. |
    | sd\_len | Number of elements in sd |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gad02b855dd7a26e3910b247fa73f19297)bt\_le\_ext\_adv\_create()

| int bt\_le\_ext\_adv\_create | ( | const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md) \* | *cb*, |
|  |  | struct bt\_le\_ext\_adv \*\* | *adv* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Create advertising set.

Create a new advertising set and set advertising parameters. Advertising parameters can be updated with [bt\_le\_ext\_adv\_update\_param](#ga1aabdb81cb1a1841ff0fb91d849123fc).

Parameters
:   | [in] | param | Advertising parameters. |
    | --- | --- | --- |
    | [in] | cb | Callback struct to notify about advertiser activity. Can be NULL. Must point to valid memory during the lifetime of the advertising set. |
    | [out] | adv | Valid advertising set object on success. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga62310a27f7fea925dfcf3abd7c454787)bt\_le\_ext\_adv\_delete()

| int bt\_le\_ext\_adv\_delete | ( | struct bt\_le\_ext\_adv \* | *adv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Delete advertising set.

Delete advertising set. This will free up the advertising set and make it possible to create a new advertising set.

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gaeb37d6cdd94a04b4cce8bc1e7aae70b4)bt\_le\_ext\_adv\_get\_index()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_ext\_adv\_get\_index | ( | struct bt\_le\_ext\_adv \* | *adv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Get array index of an advertising set.

This function is used to map bt\_adv to index of an array of advertising sets. The array has CONFIG\_BT\_EXT\_ADV\_MAX\_ADV\_SET elements.

Parameters
:   | adv | Advertising set. |
    | --- | --- |

Returns
:   Index of the advertising set object. The range of the returned value is 0..CONFIG\_BT\_EXT\_ADV\_MAX\_ADV\_SET-1

## [◆ ](#gac06c9f55cf1da46e0d64b4d9af984ecb)bt\_le\_ext\_adv\_get\_info()

| int bt\_le\_ext\_adv\_get\_info | ( | const struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_le\_ext\_adv\_info](structbt__le__ext__adv__info.md) \* | *info* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Get advertising set info.

Parameters
:   | adv | Advertising set object |
    | --- | --- |
    | info | Advertising set info object |

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#ga7486aab863ca497a50dacf81657f48d4)bt\_le\_ext\_adv\_oob\_get\_local()

| int bt\_le\_ext\_adv\_oob\_get\_local | ( | struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_le\_oob](structbt__le__oob.md) \* | *oob* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Get local LE Out of Band (OOB) information.

This function allows to get local information that are useful for Out of Band pairing or connection creation.

If privacy

```
CONFIG_BT_PRIVACY
```

is enabled this will result in generating new Resolvable Private Address (RPA) that is valid for

```
CONFIG_BT_RPA_TIMEOUT
```

seconds. This address will be used by the advertising set.

Note
:   When generating OOB information for multiple advertising set all OOB information needs to be generated at the same time.
:   If privacy is enabled the RPA cannot be refreshed in the following cases:

    - Creating a connection in progress, wait for the connected callback.

Parameters
:   | [in] | adv | The advertising set object |
    | --- | --- | --- |
    | [out] | oob | LE OOB information |

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

## [◆ ](#gad731f829b3566be3e56485b2a64f80b1)bt\_le\_ext\_adv\_set\_data()

| int bt\_le\_ext\_adv\_set\_data | ( | struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_data](structbt__data.md) \* | *ad*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *ad\_len*, |
|  |  | const struct [bt\_data](structbt__data.md) \* | *sd*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *sd\_len* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Set an advertising set's advertising or scan response data.

Set advertisement data or scan response data. If the advertising set is currently advertising then the advertising data will be updated in subsequent advertising events.

When both [BT\_LE\_ADV\_OPT\_EXT\_ADV](#gga654b0098c5f04a9c85a65f86b8f95deeae33ae9d8e43cce82e47fa73999d415ab) and [BT\_LE\_ADV\_OPT\_SCANNABLE](#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) are enabled then advertising data is ignored. When [BT\_LE\_ADV\_OPT\_SCANNABLE](#gga654b0098c5f04a9c85a65f86b8f95deeae60eafe69ef10b84f61a1f4accf789c9) is not enabled then scan response data is ignored.

If the advertising set has been configured to send advertising data on the primary advertising channels then the maximum data length is [BT\_GAP\_ADV\_MAX\_ADV\_DATA\_LEN](group__bt__gap__defines.md#ga39ab5040c9471631486da7dbebd9c36f "BT_GAP_ADV_MAX_ADV_DATA_LEN") bytes. If the advertising set has been configured for extended advertising, then the maximum data length is defined by the controller with the maximum possible of [BT\_GAP\_ADV\_MAX\_EXT\_ADV\_DATA\_LEN](group__bt__gap__defines.md#ga53af114e4925482739dc50dc84c2f641 "BT_GAP_ADV_MAX_EXT_ADV_DATA_LEN") bytes.

Note
:   Not all scanners support extended data length advertising data.
:   When updating the advertising data while advertising the advertising data and scan response data length must be smaller or equal to what can be fit in a single advertising packet. Otherwise the advertiser must be stopped.

Parameters
:   | adv | Advertising set object. |
    | --- | --- |
    | ad | Data to be used in advertisement packets. |
    | ad\_len | Number of elements in ad |
    | sd | Data to be used in scan response packets. |
    | sd\_len | Number of elements in sd |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gaf0f436c55482d9429f674303ae3aa815)bt\_le\_ext\_adv\_start()

| int bt\_le\_ext\_adv\_start | ( | struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md) \* | *param* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Start advertising with the given advertising set.

If the advertiser is limited by either the timeout or number of advertising events the application will be notified by the advertiser sent callback once the limit is reached. If the advertiser is limited by both the timeout and the number of advertising events then the limit that is reached first will stop the advertiser.

Parameters
:   | adv | Advertising set object. |
    | --- | --- |
    | param | Advertise start parameters. |

## [◆ ](#ga1c864c4b183f9a86c9f70a11471c5b15)bt\_le\_ext\_adv\_stop()

| int bt\_le\_ext\_adv\_stop | ( | struct bt\_le\_ext\_adv \* | *adv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Stop advertising with the given advertising set.

Stop advertising with a specific advertising set. When using this function the advertising sent callback will not be called.

Parameters
:   | adv | Advertising set object. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga1aabdb81cb1a1841ff0fb91d849123fc)bt\_le\_ext\_adv\_update\_param()

| int bt\_le\_ext\_adv\_update\_param | ( | struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_le\_adv\_param](structbt__le__adv__param.md) \* | *param* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Update advertising parameters.

Update the advertising parameters. The function will return an error if the advertiser set is currently advertising. Stop the advertising set before calling this function.

Note
:   When changing the option [BT\_LE\_ADV\_OPT\_USE\_NAME](#gga654b0098c5f04a9c85a65f86b8f95deea2dbc9ec77d6de134d96a7bd3d9256398) then [bt\_le\_ext\_adv\_set\_data](#gad731f829b3566be3e56485b2a64f80b1) needs to be called in order to update the advertising data and scan response data.

Parameters
:   | adv | Advertising set object. |
    | --- | --- |
    | param | Advertising parameters. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga40f2f7fdb09aba3c5137f680e67792f0)bt\_le\_filter\_accept\_list\_add()

| int bt\_le\_filter\_accept\_list\_add | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Add device (LE) to filter accept list.

Add peer device LE address to the filter accept list.

Note
:   The filter accept list cannot be modified when an LE role is using the filter accept list, i.e advertiser or scanner using a filter accept list or automatic connecting to devices using filter accept list.

Parameters
:   | addr | Bluetooth LE identity address. |
    | --- | --- |

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

## [◆ ](#gac87df899d1e363c63162988157ee6d00)bt\_le\_filter\_accept\_list\_clear()

| int bt\_le\_filter\_accept\_list\_clear | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Clear filter accept list.

Clear all devices from the filter accept list.

Note
:   The filter accept list cannot be modified when an LE role is using the filter accept list, i.e advertiser or scanner using a filter accept list or automatic connecting to devices using filter accept list.

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

## [◆ ](#ga0532ed768ab4f9d69c202066d2f87e66)bt\_le\_filter\_accept\_list\_remove()

| int bt\_le\_filter\_accept\_list\_remove | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Remove device (LE) from filter accept list.

Remove peer device LE address from the filter accept list.

Note
:   The filter accept list cannot be modified when an LE role is using the filter accept list, i.e advertiser or scanner using a filter accept list or automatic connecting to devices using filter accept list.

Parameters
:   | addr | Bluetooth LE identity address. |
    | --- | --- |

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

## [◆ ](#ga296d1adf3c9ed2f2c65bb75b887d59ee)bt\_le\_oob\_get\_local()

| int bt\_le\_oob\_get\_local | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_le\_oob](structbt__le__oob.md) \* | *oob* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Get local LE Out of Band (OOB) information.

This function allows to get local information that are useful for Out of Band pairing or connection creation.

If privacy

```
CONFIG_BT_PRIVACY
```

is enabled this will result in generating new Resolvable Private Address (RPA) that is valid for

```
CONFIG_BT_RPA_TIMEOUT
```

seconds. This address will be used for advertising started by [bt\_le\_adv\_start](#gad2e3caef88d52d720e8e4d21df767b02), active scanning and connection creation.

Note
:   If privacy is enabled the RPA cannot be refreshed in the following cases:

    - Creating a connection in progress, wait for the connected callback. In addition when extended advertising

      ```
      CONFIG_BT_EXT_ADV
      ```

      is not enabled or not supported by the controller:
    - Advertiser is enabled using a Random Static Identity Address for a different local identity.
    - The local identity conflicts with the local identity used by other roles.

Parameters
:   | [in] | id | Local identity, in most cases BT\_ID\_DEFAULT. |
    | --- | --- | --- |
    | [out] | oob | LE OOB information |

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

## [◆ ](#ga27c4961f3c7270a7f1caeadb4107854b)bt\_le\_per\_adv\_list\_add()

| int bt\_le\_per\_adv\_list\_add | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *sid* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Add a device to the periodic advertising list.

Add peer device LE address to the periodic advertising list. This will make it possibly to automatically create a periodic advertising sync to this device.

Parameters
:   | addr | Bluetooth LE identity address. |
    | --- | --- |
    | sid | The advertising set ID. This value is obtained from the [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md "bt_le_scan_recv_info") in the scan callback. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga5909bd768c23a19a42a660e3b814c981)bt\_le\_per\_adv\_list\_clear()

| int bt\_le\_per\_adv\_list\_clear | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Clear the periodic advertising list.

Clears the entire periodic advertising list.

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga100efac4a49984e06202c63c4e5955cd)bt\_le\_per\_adv\_list\_remove()

| int bt\_le\_per\_adv\_list\_remove | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *sid* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Remove a device from the periodic advertising list.

Removes peer device LE address from the periodic advertising list.

Parameters
:   | addr | Bluetooth LE identity address. |
    | --- | --- |
    | sid | The advertising set ID. This value is obtained from the [bt\_le\_scan\_recv\_info](structbt__le__scan__recv__info.md "bt_le_scan_recv_info") in the scan callback. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gafd0e7ccca93a8347a4ca6cca88e77899)bt\_le\_per\_adv\_set\_data()

| int bt\_le\_per\_adv\_set\_data | ( | const struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_data](structbt__data.md) \* | *ad*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *ad\_len* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Set or update the periodic advertising data.

The periodic advertisement data can only be set or updated on an extended advertisement set which is neither scannable, connectable nor anonymous.

Parameters
:   | adv | Advertising set object. |
    | --- | --- |
    | ad | Advertising data. |
    | ad\_len | Advertising data length. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gac96199a4e5e6cfb789c1bd1c0e67d6fe)bt\_le\_per\_adv\_set\_info\_transfer()

| int bt\_le\_per\_adv\_set\_info\_transfer | ( | const struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | const struct bt\_conn \* | *conn*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *service\_data* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Transfer the information about a periodic advertising set.

This will allow another device to quickly synchronize to periodic advertising set from this device.

Parameters
:   | adv | The periodic advertising set to transfer info of. |
    | --- | --- |
    | conn | The peer device that will receive the information. |
    | service\_data | Application service data provided to the remote host. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gaa72029a2759123ec776061d2e80bf3a1)bt\_le\_per\_adv\_set\_param()

| int bt\_le\_per\_adv\_set\_param | ( | struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md) \* | *param* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Set or update the periodic advertising parameters.

The periodic advertising parameters can only be set or updated on an extended advertisement set which is neither scannable, connectable nor anonymous.

Parameters
:   | adv | Advertising set object. |
    | --- | --- |
    | param | Advertising parameters. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gaae6b8583f7d5457f20b03dccd146425e)bt\_le\_per\_adv\_set\_response\_data()

| int bt\_le\_per\_adv\_set\_response\_data | ( | struct bt\_le\_per\_adv\_sync \* | *per\_adv\_sync*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md) \* | *params*, |
|  |  | const struct [net\_buf\_simple](structnet__buf__simple.md) \* | *data* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Set the data for a response slot in a specific subevent of the PAwR.

This function is called by the application to set the response data. The data for a response slot shall be transmitted only once.

Parameters
:   | per\_adv\_sync | The periodic advertising sync object. |
    | --- | --- |
    | params | Parameters. |
    | data | The response data to send. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga7de30fe5040b85bb9212e3a8fec4ac45)bt\_le\_per\_adv\_set\_subevent\_data()

| int bt\_le\_per\_adv\_set\_subevent\_data | ( | const struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_subevents*, |
|  |  | const struct [bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md) \* | *params* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Set the periodic advertising with response subevent data.

Set the data for one or more subevents of a Periodic Advertising with Responses Advertiser in reply data request.

Precondition
:   There are `num_subevents` elements in `params`.
:   The controller has requested data for the subevents in `params`.

Parameters
:   | adv | The extended advertiser the PAwR train belongs to. |
    | --- | --- |
    | num\_subevents | The number of subevents to set data for. |
    | params | Subevent parameters. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga0f23f4ed48e8679646f247ea0d687094)bt\_le\_per\_adv\_start()

| int bt\_le\_per\_adv\_start | ( | struct bt\_le\_ext\_adv \* | *adv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Starts periodic advertising.

Enabling the periodic advertising can be done independently of extended advertising, but both periodic advertising and extended advertising shall be enabled before any periodic advertising data is sent. The periodic advertising and extended advertising can be enabled in any order.

Once periodic advertising has been enabled, it will continue advertising until [bt\_le\_per\_adv\_stop()](#ga1b15206fc552d597c12af369d48ff7d5) has been called, or if the advertising set is deleted by [bt\_le\_ext\_adv\_delete()](#ga62310a27f7fea925dfcf3abd7c454787). Calling [bt\_le\_ext\_adv\_stop()](#ga1c864c4b183f9a86c9f70a11471c5b15) will not stop the periodic advertising.

Parameters
:   | adv | Advertising set object. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga1b15206fc552d597c12af369d48ff7d5)bt\_le\_per\_adv\_stop()

| int bt\_le\_per\_adv\_stop | ( | struct bt\_le\_ext\_adv \* | *adv* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Stops periodic advertising.

Disabling the periodic advertising can be done independently of extended advertising. Disabling periodic advertising will not disable extended advertising.

Parameters
:   | adv | Advertising set object. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga4ee87bbf79e6ac844d14c3dafb2dadf4)bt\_le\_per\_adv\_sync\_cb\_register()

| int bt\_le\_per\_adv\_sync\_cb\_register | ( | struct [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Register periodic advertising sync callbacks.

Adds the callback structure to the list of callback structures for periodic advertising syncs.

This callback will be called for all periodic advertising sync activity, such as synced, terminated and when data is received.

Parameters
:   | cb | Callback struct. Must point to memory that remains valid. |
    | --- | --- |

Return values
:   | 0 | Success. |
    | --- | --- |
    | -EEXIST | if `cb` was already registered. |

## [◆ ](#ga061bf84b989b2c96ab51d2ca0debb017)bt\_le\_per\_adv\_sync\_create()

| int bt\_le\_per\_adv\_sync\_create | ( | const struct [bt\_le\_per\_adv\_sync\_param](structbt__le__per__adv__sync__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct bt\_le\_per\_adv\_sync \*\* | *out\_sync* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Create a periodic advertising sync object.

Create a periodic advertising sync object that can try to synchronize to periodic advertising reports from an advertiser. Scan shall either be disabled or extended scan shall be enabled.

This function does not timeout, and will continue to look for an advertiser until it either finds it or [bt\_le\_per\_adv\_sync\_delete()](#gaa0c218ff3c78b26dcfaa726ee30267a6) is called. It is thus suggested to implement a timeout when using this, if it is expected to find the advertiser within a reasonable timeframe.

Parameters
:   | [in] | param | Periodic advertising sync parameters. |
    | --- | --- | --- |
    | [out] | out\_sync | Periodic advertising sync object on. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gaa0c218ff3c78b26dcfaa726ee30267a6)bt\_le\_per\_adv\_sync\_delete()

| int bt\_le\_per\_adv\_sync\_delete | ( | struct bt\_le\_per\_adv\_sync \* | *per\_adv\_sync* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Delete periodic advertising sync.

Delete the periodic advertising sync object. Can be called regardless of the state of the sync. If the syncing is currently syncing, the syncing is cancelled. If the sync has been established, it is terminated. The periodic advertising sync object will be invalidated afterwards.

If the state of the sync object is syncing, then a new periodic advertising sync object may not be created until the controller has finished canceling this object.

Parameters
:   | per\_adv\_sync | The periodic advertising sync object. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga8d05bd864d98b5b43595eb256e464024)bt\_le\_per\_adv\_sync\_get\_index()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_sync\_get\_index | ( | struct bt\_le\_per\_adv\_sync \* | *per\_adv\_sync* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Get array index of an periodic advertising sync object.

This function is get the index of an array of periodic advertising sync objects. The array has CONFIG\_BT\_PER\_ADV\_SYNC\_MAX elements.

Parameters
:   | per\_adv\_sync | The periodic advertising sync object. |
    | --- | --- |

Returns
:   Index of the periodic advertising sync object. The range of the returned value is 0..CONFIG\_BT\_PER\_ADV\_SYNC\_MAX-1

## [◆ ](#gabfaf265a48dd09ea02d114e2023c14a6)bt\_le\_per\_adv\_sync\_get\_info()

| int bt\_le\_per\_adv\_sync\_get\_info | ( | struct bt\_le\_per\_adv\_sync \* | *per\_adv\_sync*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_le\_per\_adv\_sync\_info](structbt__le__per__adv__sync__info.md) \* | *info* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Get periodic adv sync information.

Parameters
:   | per\_adv\_sync | Periodic advertising sync object. |
    | --- | --- |
    | info | Periodic advertising sync info object |

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#ga83126917373c0bcaa24964dd1d8bde46)bt\_le\_per\_adv\_sync\_lookup\_addr()

| struct bt\_le\_per\_adv\_sync \* bt\_le\_per\_adv\_sync\_lookup\_addr | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *adv\_addr*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *sid* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Look up an existing periodic advertising sync object by advertiser address.

Parameters
:   | adv\_addr | Advertiser address. |
    | --- | --- |
    | sid | The advertising set ID. |

Returns
:   Periodic advertising sync object or NULL if not found.

## [◆ ](#ga59532b37412b1b93f81cf5cc1bab0534)bt\_le\_per\_adv\_sync\_lookup\_index()

| struct bt\_le\_per\_adv\_sync \* bt\_le\_per\_adv\_sync\_lookup\_index | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Get a periodic advertising sync object from the array index.

This function is to get the periodic advertising sync object from the array index. The array has CONFIG\_BT\_PER\_ADV\_SYNC\_MAX elements.

Parameters
:   | index | The index of the periodic advertising sync object. The range of the index value is 0..CONFIG\_BT\_PER\_ADV\_SYNC\_MAX-1 |
    | --- | --- |

Returns
:   The periodic advertising sync object of the array index or NULL if invalid index.

## [◆ ](#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)bt\_le\_per\_adv\_sync\_recv\_disable()

| int bt\_le\_per\_adv\_sync\_recv\_disable | ( | struct bt\_le\_per\_adv\_sync \* | *per\_adv\_sync* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Disables receiving periodic advertising reports for a sync.

If the sync report receiving is already disabled, -EALREADY is returned.

Parameters
:   | per\_adv\_sync | The periodic advertising sync object. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga07e4510de7e72c6ed6196b3da9fb40be)bt\_le\_per\_adv\_sync\_recv\_enable()

| int bt\_le\_per\_adv\_sync\_recv\_enable | ( | struct bt\_le\_per\_adv\_sync \* | *per\_adv\_sync* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Enables receiving periodic advertising reports for a sync.

If the sync is already receiving the reports, -EALREADY is returned.

Parameters
:   | per\_adv\_sync | The periodic advertising sync object. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga731f4b37a9e5cc13a6816ea23f751b0b)bt\_le\_per\_adv\_sync\_subevent()

| int bt\_le\_per\_adv\_sync\_subevent | ( | struct bt\_le\_per\_adv\_sync \* | *per\_adv\_sync*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_le\_per\_adv\_sync\_subevent\_params](structbt__le__per__adv__sync__subevent__params.md) \* | *params* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Synchronize with a subset of subevents.

Until this command is issued, the subevent(s) the controller is synchronized to is unspecified.

Parameters
:   | per\_adv\_sync | The periodic advertising sync object. |
    | --- | --- |
    | params | Parameters. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaf81a1dd7a628d1a2f25c6b53b0679809)bt\_le\_per\_adv\_sync\_transfer()

| int bt\_le\_per\_adv\_sync\_transfer | ( | const struct bt\_le\_per\_adv\_sync \* | *per\_adv\_sync*, |
| --- | --- | --- | --- |
|  |  | const struct bt\_conn \* | *conn*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *service\_data* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Transfer the periodic advertising sync information to a peer device.

This will allow another device to quickly synchronize to the same periodic advertising train that this device is currently synced to.

Parameters
:   | per\_adv\_sync | The periodic advertising sync to transfer. |
    | --- | --- |
    | conn | The peer device that will receive the sync information. |
    | service\_data | Application service data provided to the remote host. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gaa0658bd53df1d5e8e89e13330e4fd0ae)bt\_le\_per\_adv\_sync\_transfer\_subscribe()

| int bt\_le\_per\_adv\_sync\_transfer\_subscribe | ( | const struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_le\_per\_adv\_sync\_transfer\_param](structbt__le__per__adv__sync__transfer__param.md) \* | *param* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Subscribe to periodic advertising sync transfers (PASTs).

Sets the parameters and allow other devices to transfer periodic advertising syncs.

Parameters
:   | conn | The connection to set the parameters for. If NULL default parameters for all connections will be set. Parameters set for specific connection will always have precedence. |
    | --- | --- |
    | param | The periodic advertising sync transfer parameters. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga08f872078045bbef4aca19761f25eeb8)bt\_le\_per\_adv\_sync\_transfer\_unsubscribe()

| int bt\_le\_per\_adv\_sync\_transfer\_unsubscribe | ( | const struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Unsubscribe from periodic advertising sync transfers (PASTs).

Remove the parameters that allow other devices to transfer periodic advertising syncs.

Parameters
:   | conn | The connection to remove the parameters for. If NULL default parameters for all connections will be removed. Unsubscribing for a specific device, will still allow other devices to transfer periodic advertising syncs. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga80e870fa1de40c404c64624bef439067)bt\_le\_scan\_cb\_register()

| int bt\_le\_scan\_cb\_register | ( | struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Register scanner packet callbacks.

Adds the callback structure to the list of callback structures that monitors scanner activity.

This callback will be called for all scanner activity, regardless of what API was used to start the scanner.

Parameters
:   | cb | Callback struct. Must point to memory that remains valid. |
    | --- | --- |

Return values
:   | 0 | Success. |
    | --- | --- |
    | -EEXIST | if `cb` was already registered. |

## [◆ ](#gac2718f2128b3f8c79b12d760771c8378)bt\_le\_scan\_cb\_unregister()

| void bt\_le\_scan\_cb\_unregister | ( | struct [bt\_le\_scan\_cb](structbt__le__scan__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Unregister scanner packet callbacks.

Remove the callback structure from the list of scanner callbacks.

Parameters
:   | cb | Callback struct. Must point to memory that remains valid. |
    | --- | --- |

## [◆ ](#gac5e19c26b53a08dadb8efa7ecc692ad6)bt\_le\_scan\_start()

| int bt\_le\_scan\_start | ( | const struct [bt\_le\_scan\_param](structbt__le__scan__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | [bt\_le\_scan\_cb\_t](#ga1c53d22b6e2dee38c825c58f3eeee9b4) | *cb* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Start (LE) scanning.

Start LE scanning with given parameters and provide results through the specified callback.

Note
:   The LE scanner by default does not use the Identity Address of the local device when

    ```
    CONFIG_BT_PRIVACY
    ```

    is disabled. This is to prevent the active scanner from disclosing the identity information when requesting additional information from advertisers. In order to enable directed advertiser reports then

    ```
    CONFIG_BT_SCAN_WITH_IDENTITY
    ```

    must be enabled.
:   Setting the param.timeout parameter is not supported when

    ```
    CONFIG_BT_PRIVACY
    ```

    is enabled, when the param.type is [BT\_LE\_SCAN\_TYPE\_ACTIVE](#gga2383d7ea529bcaadb727dd11ecbe5f9aaf202213813092ba298cd046aed687f22). Supplying a non-zero timeout will result in an -EINVAL error code.

Parameters
:   | param | Scan parameters. |
    | --- | --- |
    | cb | Callback to notify scan results. May be NULL if callback registration through [bt\_le\_scan\_cb\_register](#ga80e870fa1de40c404c64624bef439067) is preferred. |

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

Return values
:   | -EBUSY | if the scanner is already being started in a different thread. |
    | --- | --- |

## [◆ ](#gaa2de1a1ab523606b36a4c445fb0c3b84)bt\_le\_scan\_stop()

| int bt\_le\_scan\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Stop (LE) scanning.

Stops ongoing LE scanning.

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

## [◆ ](#gabc115fd3fff6d00ae878a31613bf70aa)bt\_le\_set\_chan\_map()

| int bt\_le\_set\_chan\_map | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *chan\_map*[5] | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Set (LE) channel map.

Parameters
:   | chan\_map | Channel map. |
    | --- | --- |

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

## [◆ ](#ga9ab41e118b5496c196e56b8b5d023275)bt\_le\_set\_rpa\_timeout()

| int bt\_le\_set\_rpa\_timeout | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *new\_rpa\_timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Set the Resolvable Private Address timeout in runtime.

The new RPA timeout value will be used for the next RPA rotation and all subsequent rotations until another override is scheduled with this API.

Initially, the if

```
CONFIG_BT_RPA_TIMEOUT
```

is used as the RPA timeout.

This symbol is linkable if

```
CONFIG_BT_RPA_TIMEOUT_DYNAMIC
```

is enabled.

Parameters
:   | new\_rpa\_timeout | Resolvable Private Address timeout in seconds |
    | --- | --- |

Return values
:   | 0 | Success. |
    | --- | --- |
    | -EINVAL | RPA timeout value is invalid. Valid range is 1s - 3600s. |

## [◆ ](#gaf0729453790aab1bd3d52c623be3b35a)bt\_set\_appearance()

| int bt\_set\_appearance | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *new\_appearance* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Set local Bluetooth appearance.

Automatically preserves the new appearance across reboots if

```
CONFIG_BT_SETTINGS
```

is enabled.

This symbol is linkable if

```
CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC
```

is enabled.

Parameters
:   | new\_appearance | Appearance Value |
    | --- | --- |

Return values
:   | 0 | Success. |
    | --- | --- |
    | other | Persistent storage failed. Appearance was not updated. |

## [◆ ](#gac8bb3609a3d6da69ff736809e45f5c8a)bt\_set\_name()

| int bt\_set\_name | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Set Bluetooth Device Name.

Set Bluetooth GAP Device Name.

When advertising with device name in the advertising data the name should be updated by calling [bt\_le\_adv\_update\_data](#ga9a406ebfefac3dd09935a4ae0e317817) or [bt\_le\_ext\_adv\_set\_data](#gad731f829b3566be3e56485b2a64f80b1).

Note
:   Requires

    ```
    CONFIG_BT_DEVICE_NAME_DYNAMIC
    ```

    .

See also
:   ```
    CONFIG_BT_DEVICE_NAME_MAX
    ```

    .

Parameters
:   | name | New name |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gaceabbbe6e844650f791010e53c9df6a4)bt\_unpair()

| int bt\_unpair | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, |
| --- | --- | --- | --- |
|  |  | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr* ) |

`#include <[bluetooth.h](bluetooth_2bluetooth_8h.md)>`

Clear pairing information.

Parameters
:   | id | Local identity (mostly just BT\_ID\_DEFAULT). |
    | --- | --- |
    | addr | Remote address, NULL or BT\_ADDR\_LE\_ANY to clear all remote devices. |

Returns
:   0 on success or negative error value on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
