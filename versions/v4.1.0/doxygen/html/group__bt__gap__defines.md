---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__gap__defines.html
original_path: doxygen/html/group__bt__gap__defines.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Defines and Assigned Numbers

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Bluetooth Generic Access Profile defines and Assigned Numbers.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_GAP\_ADV\_MAX\_ADV\_DATA\_LEN](#ga39ab5040c9471631486da7dbebd9c36f)   31 |
|  | Maximum advertising data length. |
| #define | [BT\_GAP\_ADV\_MAX\_EXT\_ADV\_DATA\_LEN](#ga53af114e4925482739dc50dc84c2f641)   1650 |
|  | Maximum extended advertising data length. |
| #define | [BT\_GAP\_TX\_POWER\_INVALID](#ga61ccce819d75313cb2ee58309ed4b275)   0x7f |
| #define | [BT\_GAP\_RSSI\_INVALID](#ga64b5c5e429dadf1e875984f69cd399dc)   0x7f |
| #define | [BT\_GAP\_SID\_INVALID](#ga103af3e3142473be8897cd2647dca915)   0xff |
| #define | [BT\_GAP\_NO\_TIMEOUT](#ga9d6b2af6b96eab6356ded93c54301ef6)   0x0000 |
| #define | [BT\_GAP\_ADV\_HIGH\_DUTY\_CYCLE\_MAX\_TIMEOUT](#gabe483d4dd601b11ac3eea570c962b1ec)   128 |
| #define | [BT\_GAP\_DATA\_LEN\_DEFAULT](#ga90cfab7c375a8af6f9224a5635cbd023)   0x001b /\* 27 bytes \*/ |
|  | Default data length. |
| #define | [BT\_GAP\_DATA\_LEN\_MAX](#gacf5f35866d4677bd45c6e567886cabb9)   0x00fb /\* 251 bytes \*/ |
|  | Maximum data length. |
| #define | [BT\_GAP\_DATA\_TIME\_DEFAULT](#ga245249c0b6f8ccc419f2132f76362908)   0x0148 /\* 328 us \*/ |
|  | Default data time. |
| #define | [BT\_GAP\_DATA\_TIME\_MAX](#ga379b5d8d7f243abbc584c288cd01815f)   0x4290 /\* 17040 us \*/ |
|  | Maximum data time. |
| #define | [BT\_GAP\_SID\_MAX](#gafa6f803fe3ada07030fb1f2f725940c4)   0x0F |
|  | Maximum advertising set number. |
| #define | [BT\_GAP\_PER\_ADV\_MAX\_SKIP](#gaf92b229c47309a7a5e99047f28b860e7)   0x01F3 |
|  | Maximum number of consecutive periodic advertisement events that can be skipped after a successful receive. |
| #define | [BT\_GAP\_PER\_ADV\_MIN\_TIMEOUT](#ga17d8ae7e98f6a1dfead4f8ecb75f9645)   0x000A /\* 100 ms \*/ |
|  | Minimum Periodic Advertising Timeout (N \* 10 ms). |
| #define | [BT\_GAP\_PER\_ADV\_MAX\_TIMEOUT](#gad6674199f615fa6ecaeb1fe9d099e04c)   0x4000 /\* 163.84 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
|  | Maximum Periodic Advertising Timeout (N \* 10 ms). |
| #define | [BT\_GAP\_PER\_ADV\_MIN\_INTERVAL](#ga07e21fdeb8a0a0b967690898bef2f7aa)   0x0006 /\* 7.5 ms \*/ |
|  | Minimum Periodic Advertising Interval (N \* 1.25 ms). |
| #define | [BT\_GAP\_PER\_ADV\_MAX\_INTERVAL](#ga80bf3f1fb6f34a2c4363687149c365bd)   0xFFFF /\* 81.91875 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
|  | Maximum Periodic Advertising Interval (N \* 1.25 ms). |
| #define | [BT\_GAP\_ADV\_INTERVAL\_TO\_US](#ga6e10b5311c785ad7eea10743987c0f27)(\_interval) |
|  | Convert periodic advertising interval (N \* 0.625 ms) to microseconds. |
| #define | [BT\_GAP\_ADV\_INTERVAL\_TO\_MS](#ga7261e64328e433d333d88d3a4cad21de)(\_interval) |
|  | Convert periodic advertising interval (N \* 0.625 ms) to milliseconds. |
| #define | [BT\_GAP\_ISO\_INTERVAL\_TO\_US](#ga4feca4664259c43121c2ff481d9ee611)(\_interval) |
|  | Convert isochronous interval (N \* 1.25 ms) to microseconds. |
| #define | [BT\_GAP\_ISO\_INTERVAL\_TO\_MS](#ga46c1e49ca3285ed9fc1b4ac593a25cd3)(\_interval) |
|  | Convert isochronous interval (N \* 1.25 ms) to milliseconds. |
| #define | [BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_US](#ga63587ef565ccde477b9c6f03faf778a5)(\_interval) |
|  | Convert periodic advertising interval (N \* 1.25 ms) to microseconds \*. |
| #define | [BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_MS](#gac240015012694df3557679d99da6c1a9)(\_interval) |
|  | Convert periodic advertising interval (N \* 1.25 ms) to milliseconds. |
| #define | [BT\_GAP\_US\_TO\_ADV\_INTERVAL](#gac79626389f62bb7b3e5b5f6d3a5eaf2b)(\_interval) |
|  | Convert microseconds to advertising interval units (0.625 ms). |
| #define | [BT\_GAP\_MS\_TO\_ADV\_INTERVAL](#gaef9c34f229f1b8b06d3e6cd44a1014ef)(\_interval) |
|  | Convert milliseconds to advertising interval units (0.625 ms). |
| #define | [BT\_GAP\_US\_TO\_PER\_ADV\_INTERVAL](#ga5a9da01507b4356c2ad6f8309257f2ce)(\_interval) |
|  | Convert microseconds to periodic advertising interval units (1.25 ms). |
| #define | [BT\_GAP\_MS\_TO\_PER\_ADV\_INTERVAL](#ga15ec0bc7c9bab797d6c5595269a33ea4)(\_interval) |
|  | Convert milliseconds to periodic advertising interval units (1.25 ms). |
| #define | [BT\_GAP\_MS\_TO\_PER\_ADV\_SYNC\_TIMEOUT](#ga242a6a4e3dd138073c01bc600c9642eb)(\_timeout) |
|  | Convert milliseconds to periodic advertising sync timeout units (10 ms). |
| #define | [BT\_GAP\_US\_TO\_PER\_ADV\_SYNC\_TIMEOUT](#gaf33284a372b21e24c53deb5e3a6a91aa)(\_timeout) |
|  | Convert microseconds to periodic advertising sync timeout units (10 ms). |
| #define | [BT\_GAP\_US\_TO\_SCAN\_INTERVAL](#gab65e489c4a799774f6511c6ce5b65ea2)(\_interval) |
|  | Convert microseconds to scan interval units (0.625 ms). |
| #define | [BT\_GAP\_MS\_TO\_SCAN\_INTERVAL](#gad18c4a9774014081833905fc9e03fb15)(\_interval) |
|  | Convert milliseconds to scan interval units (0.625 ms). |
| #define | [BT\_GAP\_US\_TO\_SCAN\_WINDOW](#gaac5d0ec82d9730b793960c0470ac6342)(\_window) |
|  | Convert microseconds to scan window units (0.625 ms). |
| #define | [BT\_GAP\_MS\_TO\_SCAN\_WINDOW](#ga5204f7e42b4e33eb8ae4ae71b82a4c88)(\_window) |
|  | Convert milliseconds to scan window units (0.625 ms). |
| #define | [BT\_GAP\_US\_TO\_CONN\_INTERVAL](#gab12ba919a5a389b4c342d142d3a9ce6e)(\_interval) |
|  | Convert microseconds to connection interval units (1.25 ms). |
| #define | [BT\_GAP\_MS\_TO\_CONN\_INTERVAL](#ga75985e2c444da7b2426cc746c9781c8c)(\_interval) |
|  | Convert milliseconds to connection interval units (1.25 ms). |
| #define | [BT\_GAP\_MS\_TO\_CONN\_TIMEOUT](#ga24f79cacceeea262987f3cdaf2ef6bc3)(\_timeout) |
|  | Convert milliseconds to connection supervision timeout units (10 ms). |
| #define | [BT\_GAP\_US\_TO\_CONN\_TIMEOUT](#ga317a60f9edb371fef180130282805539)(\_timeout) |
|  | Convert microseconds to connection supervision timeout units (10 ms). |
| #define | [BT\_GAP\_US\_TO\_CONN\_EVENT\_LEN](#ga8905e22b1864021b77367c228b8bff48)(\_event\_len) |
|  | Convert milliseconds to connection event length units (0.625). |
| #define | [BT\_GAP\_MS\_TO\_CONN\_EVENT\_LEN](#gaa3703cccd343dbb6418fdeb47a718eb5)(\_event\_len) |
|  | Convert milliseconds to connection event length units (0.625). |
| #define | [BT\_LE\_SUPP\_FEAT\_40\_ENCODE](#ga799f6cb9dd02b9995ed76fbe97be3eb3)(w64) |
|  | Encode 40 least significant bits of 64-bit LE Supported Features into array values in little-endian format. |
| #define | [BT\_LE\_SUPP\_FEAT\_32\_ENCODE](#ga7aa92098e33840ff02cb8c0435637094)(w64) |
|  | Encode 4 least significant bytes of 64-bit LE Supported Features into 4 bytes long array of values in little-endian format. |
| #define | [BT\_LE\_SUPP\_FEAT\_24\_ENCODE](#gab8739c92f8d50b796539a21027c3b6eb)(w64) |
|  | Encode 3 least significant bytes of 64-bit LE Supported Features into 3 bytes long array of values in little-endian format. |
| #define | [BT\_LE\_SUPP\_FEAT\_16\_ENCODE](#ga3c29ad99d6a6e020148590381ab08b17)(w64) |
|  | Encode 2 least significant bytes of 64-bit LE Supported Features into 2 bytes long array of values in little-endian format. |
| #define | [BT\_LE\_SUPP\_FEAT\_8\_ENCODE](#ga8fac302925ac3ef8982630e6a0ec13af)(w64) |
|  | Encode the least significant byte of 64-bit LE Supported Features into single byte long array. |
| #define | [BT\_LE\_SUPP\_FEAT\_VALIDATE](#ga86266eaf452dfaf82f097992e01397c8)(w64) |
|  | Validate whether LE Supported Features value does not use bits that are reserved for future use. |

| Enumerations | |
| --- | --- |
| enum | {     [BT\_GAP\_LE\_PHY\_NONE](#gga7dc8e89251aa575e28331e05775ba20baaf7e1b40f6464a603e5116db269cacab) = 0 , [BT\_GAP\_LE\_PHY\_1M](#gga7dc8e89251aa575e28331e05775ba20ba53eff400720a20fe1a91da4834bad752) = BIT(0) , [BT\_GAP\_LE\_PHY\_2M](#gga7dc8e89251aa575e28331e05775ba20ba662049cc8293959194bcb481e1dd50a8) = BIT(1) , [BT\_GAP\_LE\_PHY\_CODED](#gga7dc8e89251aa575e28331e05775ba20ba97d042e48448fdf6a9e35e5d38cb14c3) = BIT(2) ,     [BT\_GAP\_LE\_PHY\_CODED\_S8](#gga7dc8e89251aa575e28331e05775ba20ba47ca63851d4380aad42a0a37a17f020d) = BIT(3) , [BT\_GAP\_LE\_PHY\_CODED\_S2](#gga7dc8e89251aa575e28331e05775ba20ba23fc74a635a05d082b0033b3f152592b) = BIT(4)   } |
|  | LE PHY types. [More...](#ga7dc8e89251aa575e28331e05775ba20b) |
| enum | {     [BT\_GAP\_ADV\_TYPE\_ADV\_IND](#ggab5a881b0cb1df3cf98de07a14e818c3eaf4d48e46c1da164e876e4ded28470c82) = 0x00 , [BT\_GAP\_ADV\_TYPE\_ADV\_DIRECT\_IND](#ggab5a881b0cb1df3cf98de07a14e818c3ea05b182a44fea67f52015cbfb4d775be8) = 0x01 , [BT\_GAP\_ADV\_TYPE\_ADV\_SCAN\_IND](#ggab5a881b0cb1df3cf98de07a14e818c3eae48316c135886d9f6d20f7bdba0858c1) = 0x02 , [BT\_GAP\_ADV\_TYPE\_ADV\_NONCONN\_IND](#ggab5a881b0cb1df3cf98de07a14e818c3eabb587b376bd6511881d6b70ceaa2af56) = 0x03 ,     [BT\_GAP\_ADV\_TYPE\_SCAN\_RSP](#ggab5a881b0cb1df3cf98de07a14e818c3ea5387de0177d3a9da9fd0c44ca30c7018) = 0x04 , [BT\_GAP\_ADV\_TYPE\_EXT\_ADV](#ggab5a881b0cb1df3cf98de07a14e818c3ea09292ffe2f0b76b8761fcaad6fbf9ba8) = 0x05   } |
|  | Advertising PDU types. [More...](#gab5a881b0cb1df3cf98de07a14e818c3e) |
| enum | {     [BT\_GAP\_ADV\_PROP\_CONNECTABLE](#ggabf1a0417a549ec0a97263c2d990e711baf843db0752f3360ccb1a02c456ca9e5e) = BIT(0) , [BT\_GAP\_ADV\_PROP\_SCANNABLE](#ggabf1a0417a549ec0a97263c2d990e711ba6c5ea1b8392783568b568c74f9f17571) = BIT(1) , [BT\_GAP\_ADV\_PROP\_DIRECTED](#ggabf1a0417a549ec0a97263c2d990e711ba4595d3a3ea30bd4cd51ba4f1c4ab7de9) = BIT(2) , [BT\_GAP\_ADV\_PROP\_SCAN\_RESPONSE](#ggabf1a0417a549ec0a97263c2d990e711ba55258ac9a7b355db87aeec5d443718f7) = BIT(3) ,     [BT\_GAP\_ADV\_PROP\_EXT\_ADV](#ggabf1a0417a549ec0a97263c2d990e711baeda2301e9eb191e742375e54bb765684) = BIT(4)   } |
|  | Advertising PDU properties. [More...](#gabf1a0417a549ec0a97263c2d990e711b) |
| enum | { [BT\_GAP\_CTE\_AOA](#ggad30b9b6f60a1491bac4aa2c355072966a8a82746ee64ffbcc62e79fdd8e0e30a0) = 0x00 , [BT\_GAP\_CTE\_AOD\_1US](#ggad30b9b6f60a1491bac4aa2c355072966aa8587383f9ea245e8c279fdd63417a19) = 0x01 , [BT\_GAP\_CTE\_AOD\_2US](#ggad30b9b6f60a1491bac4aa2c355072966a2385af24a5a82f4d799674443b92e966) = 0x02 , [BT\_GAP\_CTE\_NONE](#ggad30b9b6f60a1491bac4aa2c355072966aec9324d8e0997e1ace59895e168087e8) = 0xFF } |
|  | Constant Tone Extension (CTE) types. [More...](#gad30b9b6f60a1491bac4aa2c355072966) |
| enum | {     [BT\_GAP\_SCA\_UNKNOWN](#ggafa0d8b6c50823ebb6bd38340efbb5a6bace5a2d3f9fcb1a8913203ee6f437b910) = 0 , [BT\_GAP\_SCA\_251\_500](#ggafa0d8b6c50823ebb6bd38340efbb5a6ba96900858c146259fc41af27b4cb62247) = 0 , [BT\_GAP\_SCA\_151\_250](#ggafa0d8b6c50823ebb6bd38340efbb5a6bab19b506bc13aad6af3dba925153f4e7d) = 1 , [BT\_GAP\_SCA\_101\_150](#ggafa0d8b6c50823ebb6bd38340efbb5a6ba7f41d38c1a2125bd7c4d1765c8fbee73) = 2 ,     [BT\_GAP\_SCA\_76\_100](#ggafa0d8b6c50823ebb6bd38340efbb5a6baa4011892d3409238f668c87626587bfd) = 3 , [BT\_GAP\_SCA\_51\_75](#ggafa0d8b6c50823ebb6bd38340efbb5a6ba999a15d6ed8c860af7323af1b4d86fe9) = 4 , [BT\_GAP\_SCA\_31\_50](#ggafa0d8b6c50823ebb6bd38340efbb5a6ba5fa53f708753d67bd6ec4f54b164b005) = 5 , [BT\_GAP\_SCA\_21\_30](#ggafa0d8b6c50823ebb6bd38340efbb5a6ba164fe8b7df50d8e393373153a1f70d1d) = 6 ,     [BT\_GAP\_SCA\_0\_20](#ggafa0d8b6c50823ebb6bd38340efbb5a6bab8fd607ccdc30216fd90d4c6f568b9f6) = 7   } |
|  | Peripheral sleep clock accuracy (SCA) in ppm (parts per million). [More...](#gafa0d8b6c50823ebb6bd38340efbb5a6b) |

| Company Identifiers (see Bluetooth Assigned Numbers) | |
| --- | --- |
| #define | [BT\_COMP\_ID\_LF](#ga6bbf21c05f24d2c2c710be9bcf05af5f)   0x05f1 |
|  | The Linux Foundation. |

| EIR/AD data type definitions | |
| --- | --- |
| #define | [BT\_DATA\_FLAGS](#ga396b92d418fcb8263895e420b9df3df2)   0x01 |
|  | AD flags. |
| #define | [BT\_DATA\_UUID16\_SOME](#ga6c725bd3d31c159a4d046561dbca38ba)   0x02 |
|  | 16-bit UUID, more available |
| #define | [BT\_DATA\_UUID16\_ALL](#ga0d55063b9ad321b5c530a0012337df8a)   0x03 |
|  | 16-bit UUID, all listed |
| #define | [BT\_DATA\_UUID32\_SOME](#ga2486a6748490ba57e442ca15223482ef)   0x04 |
|  | 32-bit UUID, more available |
| #define | [BT\_DATA\_UUID32\_ALL](#gaaf825c3e4686e572a35ddd46ee6fe2e8)   0x05 |
|  | 32-bit UUID, all listed |
| #define | [BT\_DATA\_UUID128\_SOME](#ga5c4f7fc1b93c611e95f735330fba243b)   0x06 |
|  | 128-bit UUID, more available |
| #define | [BT\_DATA\_UUID128\_ALL](#gaafcade3dbbcb4005f4590e994f91884b)   0x07 |
|  | 128-bit UUID, all listed |
| #define | [BT\_DATA\_NAME\_SHORTENED](#gafc509b33a8d2dd9124f6893eadbe1662)   0x08 |
|  | Shortened name. |
| #define | [BT\_DATA\_NAME\_COMPLETE](#gab94a7c5689d296acf47f976538056ab5)   0x09 |
|  | Complete name. |
| #define | [BT\_DATA\_TX\_POWER](#ga4988c17578c4cf76fcdd9d44e1c931b0)   0x0a |
|  | Tx Power. |
| #define | [BT\_DATA\_DEVICE\_CLASS](#ga152c3028a2befcc4caf40aa6590c80b7)   0x0d |
|  | Class of Device. |
| #define | [BT\_DATA\_SIMPLE\_PAIRING\_HASH\_C192](#ga053c8bb0aedd01b3dd3f6154f4b49999)   0x0e |
|  | Simple Pairing Hash C-192. |
| #define | [BT\_DATA\_SIMPLE\_PAIRING\_RAND\_C192](#ga280f1f96c5204960fe034c9ddaf194ec)   0x0f |
|  | Simple Pairing Randomizer R-192. |
| #define | [BT\_DATA\_DEVICE\_ID](#gac9402c597e5b4497f4bcd22d5177cc23)   0x10 |
|  | Device ID (Profile). |
| #define | [BT\_DATA\_SM\_TK\_VALUE](#ga5014acb2fe8e76b855b55bf98abe6d05)   0x10 |
|  | Security Manager TK Value. |
| #define | [BT\_DATA\_SM\_OOB\_FLAGS](#gaa12c742d1c955036aa3f55e84df69890)   0x11 |
|  | Security Manager OOB Flags. |
| #define | [BT\_DATA\_PERIPHERAL\_INT\_RANGE](#gabcf872eafc60c21287f6be63174dc7c8)   0x12 |
|  | Peripheral Connection Interval Range. |
| #define | [BT\_DATA\_SOLICIT16](#ga2ad4d2ec2ff29c0aad5159de12d3f741)   0x14 |
|  | Solicit UUIDs, 16-bit. |
| #define | [BT\_DATA\_SOLICIT128](#ga217df3f70846e86fa09e5605d5acd291)   0x15 |
|  | Solicit UUIDs, 128-bit. |
| #define | [BT\_DATA\_SVC\_DATA16](#ga76990dda919688b369decaf9d3606b32)   0x16 |
|  | Service data, 16-bit UUID. |
| #define | [BT\_DATA\_PUB\_TARGET\_ADDR](#gacb867f0436d38c5c80e3426ca6247a46)   0x17 |
|  | Public Target Address. |
| #define | [BT\_DATA\_RAND\_TARGET\_ADDR](#ga3d9097d8f53213ccafc152c51ad6fdbd)   0x18 |
|  | Random Target Address. |
| #define | [BT\_DATA\_GAP\_APPEARANCE](#ga67fc721da05758b7d7a36aecaa035fac)   0x19 |
|  | GAP appearance. |
| #define | [BT\_DATA\_ADV\_INT](#ga6fd8c0f32bbcb97aaafee51fda0b601e)   0x1a |
|  | Advertising Interval. |
| #define | [BT\_DATA\_LE\_BT\_DEVICE\_ADDRESS](#gad9e8a273239fa160a6b2797ef5563a94)   0x1b |
|  | LE Bluetooth Device Address. |
| #define | [BT\_DATA\_LE\_ROLE](#ga255c7cb16eb24b95fa0f531fc4574273)   0x1c |
|  | LE Role. |
| #define | [BT\_DATA\_SIMPLE\_PAIRING\_HASH](#ga324f91521eacd1e9d579c9d52d02eb06)   0x1d |
|  | Simple Pairing Hash C256. |
| #define | [BT\_DATA\_SIMPLE\_PAIRING\_RAND](#gad7e7dd2d3a972e53f9e5e80627bd07e6)   0x1e |
|  | Simple Pairing Randomizer R256. |
| #define | [BT\_DATA\_SOLICIT32](#ga76e7e8971ed841b87fda08793a00b14f)   0x1f |
|  | Solicit UUIDs, 32-bit. |
| #define | [BT\_DATA\_SVC\_DATA32](#ga7d411a723ff2f038c3b7a1e09c88cb3d)   0x20 |
|  | Service data, 32-bit UUID. |
| #define | [BT\_DATA\_SVC\_DATA128](#gaa53847910515d9488b490f17a4fdf0d1)   0x21 |
|  | Service data, 128-bit UUID. |
| #define | [BT\_DATA\_LE\_SC\_CONFIRM\_VALUE](#ga883dda02c157f0de8157b1c5f66aafd0)   0x22 |
|  | LE SC Confirmation Value. |
| #define | [BT\_DATA\_LE\_SC\_RANDOM\_VALUE](#gacbc31c67684e3c68481501cf89f9ec68)   0x23 |
|  | LE SC Random Value. |
| #define | [BT\_DATA\_URI](#ga3c6a5903cc4a46aaf0b30a0de0179403)   0x24 |
|  | URI. |
| #define | [BT\_DATA\_INDOOR\_POS](#ga0f29f9d8f5a336af430f0a603e87e995)   0x25 |
|  | Indoor Positioning. |
| #define | [BT\_DATA\_TRANS\_DISCOVER\_DATA](#ga8e9ccc669ee545152b2d9b3120692d55)   0x26 |
|  | Transport Discovery Data. |
| #define | [BT\_DATA\_LE\_SUPPORTED\_FEATURES](#ga207bc1e5405a4fd3f39863a2cb304ebc)   0x27 |
|  | LE Supported Features. |
| #define | [BT\_DATA\_CHANNEL\_MAP\_UPDATE\_IND](#gae3eb96c0f127b6417d7cad288faaaceb)   0x28 |
|  | Channel Map Update Indication. |
| #define | [BT\_DATA\_MESH\_PROV](#gafc5984d58b0b54ee824dd83bc78dfbe9)   0x29 |
|  | Mesh Provisioning PDU. |
| #define | [BT\_DATA\_MESH\_MESSAGE](#gac351c67ab58520b796fa713602d9f602)   0x2a |
|  | Mesh Networking PDU. |
| #define | [BT\_DATA\_MESH\_BEACON](#ga59cc479be1f6c61a4a47aa6f479fe67a)   0x2b |
|  | Mesh Beacon. |
| #define | [BT\_DATA\_BIG\_INFO](#ga16feb94cd09c04d020450f61646f5486)   0x2c |
|  | BIGInfo. |
| #define | [BT\_DATA\_BROADCAST\_CODE](#ga72d2e55819db593a6db77579ebfe1e9d)   0x2d |
|  | Broadcast Code. |
| #define | [BT\_DATA\_CSIS\_RSI](#ga122da4184d606ae140f8a311aaebeedd)   0x2e |
|  | CSIS Random Set ID type. |
| #define | [BT\_DATA\_ADV\_INT\_LONG](#gad4ac2e0de80dddcacc4ca6d25765eebd)   0x2f |
|  | Advertising Interval long. |
| #define | [BT\_DATA\_BROADCAST\_NAME](#ga7d781791bc85fe3c7ea839ff617ee6e7)   0x30 |
|  | Broadcast Name. |
| #define | [BT\_DATA\_ENCRYPTED\_AD\_DATA](#ga41d5c898144e89b6035f92ff506f38a3)   0x31 |
|  | Encrypted Advertising Data. |
| #define | [BT\_DATA\_PAWR\_TIMING\_INFO](#ga14a8b1cf9d6c1c9749443a012731d39c)   0x32 |
|  | Periodic Advertising Response Timing Info. |
| #define | [BT\_DATA\_ESL](#ga90c7a1175148f3a56b04dc0b29525a4d)   0x34 |
|  | Electronic Shelf Label Profile. |
| #define | [BT\_DATA\_3D\_INFO](#gaecab0c77f9f912c16c264e7eaf2e4707)   0x3D |
|  | 3D Information Data |
| #define | [BT\_DATA\_MANUFACTURER\_DATA](#ga63b846807bff632b1cdd49b1e46e63b4)   0xff |
|  | Manufacturer Specific Data. |
| #define | [BT\_LE\_AD\_LIMITED](#ga36191ee000a2098fd679c398b31e0906)   0x01 |
|  | Limited Discoverable. |
| #define | [BT\_LE\_AD\_GENERAL](#ga13d9b4a24e2a8b58402bfb21f8b782c8)   0x02 |
|  | General Discoverable. |
| #define | [BT\_LE\_AD\_NO\_BREDR](#gabf5725f481cb73cbd974f3653c904bc9)   0x04 |
|  | BR/EDR not supported. |

| Appearance Values | |
| --- | --- |
| Last Modified on 2023-01-05 | |
| #define | [BT\_APPEARANCE\_UNKNOWN](#gafd1c9ca638a362a01897792e5a00a0c5)   0x0000 |
|  | Generic Unknown. |
| #define | [BT\_APPEARANCE\_GENERIC\_PHONE](#gae7061e78f960563af6e1b3dea71655a9)   0x0040 |
|  | Generic Phone. |
| #define | [BT\_APPEARANCE\_GENERIC\_COMPUTER](#ga6b74ad86efc0e9a745f2c9e64079b1cd)   0x0080 |
|  | Generic Computer. |
| #define | [BT\_APPEARANCE\_COMPUTER\_DESKTOP\_WORKSTATION](#ga1aa0565ca7e00e3a1aa8968e0a7f1bef)   0x0081 |
|  | Desktop Workstation. |
| #define | [BT\_APPEARANCE\_COMPUTER\_SERVER\_CLASS](#gab71a3c3f836561ac7bd8e52f5e01c769)   0x0082 |
|  | Server-class Computer. |
| #define | [BT\_APPEARANCE\_COMPUTER\_LAPTOP](#ga55ce2ad96a153ed6bdfd841276145c28)   0x0083 |
|  | Laptop. |
| #define | [BT\_APPEARANCE\_COMPUTER\_HANDHELD\_PCPDA](#gab64312ea16f03c5998db4429b194b8b0)   0x0084 |
|  | Handheld PC/PDA (clamshell). |
| #define | [BT\_APPEARANCE\_COMPUTER\_PALMSIZE\_PCPDA](#ga9340ed60911fc7c5aab7d317b6925c10)   0x0085 |
|  | Palm­size PC/PDA. |
| #define | [BT\_APPEARANCE\_COMPUTER\_WEARABLE\_COMPUTER](#ga7c6667ba4c68dec380a548ba9530c110)   0x0086 |
|  | Wearable computer (watch size). |
| #define | [BT\_APPEARANCE\_COMPUTER\_TABLET](#ga11bc881cb5f88956edbf2bb2fe5b358c)   0x0087 |
|  | Tablet. |
| #define | [BT\_APPEARANCE\_COMPUTER\_DOCKING\_STATION](#ga36187d2651d08c4b3e17c36565a2d3c9)   0x0088 |
|  | Docking Station. |
| #define | [BT\_APPEARANCE\_COMPUTER\_ALL\_IN\_ONE](#gaa4d962ad8661c28ed48f5cf8cd75ad6e)   0x0089 |
|  | All in One. |
| #define | [BT\_APPEARANCE\_COMPUTER\_BLADE\_SERVER](#ga53e8eff26f2020b1fc89b21684e54698)   0x008A |
|  | Blade Server. |
| #define | [BT\_APPEARANCE\_COMPUTER\_CONVERTIBLE](#ga073dca362cabfd2a07cdc1cb787a0f58)   0x008B |
|  | Convertible. |
| #define | [BT\_APPEARANCE\_COMPUTER\_DETACHABLE](#ga8f35f76cc9de4170006669d6e9e7d72a)   0x008C |
|  | Detachable. |
| #define | [BT\_APPEARANCE\_COMPUTER\_IOT\_GATEWAY](#ga6ae353795476853bc3be2196ed220aa7)   0x008D |
|  | IoT Gateway. |
| #define | [BT\_APPEARANCE\_COMPUTER\_MINI\_PC](#ga3c47c11f56eabec15e960662c64f6fcb)   0x008E |
|  | Mini PC. |
| #define | [BT\_APPEARANCE\_COMPUTER\_STICK\_PC](#gabb53daf3eb4ac9ba0cbb1614056ee214)   0x008F |
|  | Stick PC. |
| #define | [BT\_APPEARANCE\_GENERIC\_WATCH](#ga0c512fd6aa5d35e78f02176073f5f121)   0x00C0 |
|  | Generic Watch. |
| #define | [BT\_APPEARANCE\_SPORTS\_WATCH](#gaca9cc93d768145ec3d87b88740954b50)   0x00C1 |
|  | Sports Watch. |
| #define | [BT\_APPEARANCE\_SMARTWATCH](#gaa5662d4a544b034243faa45245a9728b)   0x00C2 |
|  | Smartwatch. |
| #define | [BT\_APPEARANCE\_GENERIC\_CLOCK](#ga100d26d6b9e9a3af925d64c0b006c6bd)   0x0100 |
|  | Generic Clock. |
| #define | [BT\_APPEARANCE\_GENERIC\_DISPLAY](#ga0a21cb58861a48875002af38ee82ac08)   0x0140 |
|  | Generic Display. |
| #define | [BT\_APPEARANCE\_GENERIC\_REMOTE](#ga0b47897768b27d26b8687dd2ab28703b)   0x0180 |
|  | Generic Remote Control. |
| #define | [BT\_APPEARANCE\_GENERIC\_EYEGLASSES](#gab2b5f6385662519a2ece8fb654a6194b)   0x01C0 |
|  | Generic Eye-glasses. |
| #define | [BT\_APPEARANCE\_GENERIC\_TAG](#gaca6d810977e6da1a3174ee2b6b36662d)   0x0200 |
|  | Generic Tag. |
| #define | [BT\_APPEARANCE\_GENERIC\_KEYRING](#gaf73b11c4dbf366a854b4c68e802e3c1c)   0x0240 |
|  | Generic Keyring. |
| #define | [BT\_APPEARANCE\_GENERIC\_MEDIA\_PLAYER](#ga17e94209c0c96b5ca039b1613de0d05e)   0x0280 |
|  | Generic Media Player. |
| #define | [BT\_APPEARANCE\_GENERIC\_BARCODE\_SCANNER](#gadca19a01611ca83e18156bb540dd96c1)   0x02C0 |
|  | Generic Barcode Scanner. |
| #define | [BT\_APPEARANCE\_GENERIC\_THERMOMETER](#ga2e0fde88d83e1f4533d69c8dc472255f)   0x0300 |
|  | Generic Thermometer. |
| #define | [BT\_APPEARANCE\_THERMOMETER\_EAR](#ga54283061a207491dcfced899c0fc3008)   0x0301 |
|  | Ear Thermometer. |
| #define | [BT\_APPEARANCE\_GENERIC\_HEART\_RATE](#gac5bdf195b81215932848151d765e84d6)   0x0340 |
|  | Generic Heart Rate Sensor. |
| #define | [BT\_APPEARANCE\_HEART\_RATE\_BELT](#ga895f6570a09f3eee8d821eca57cdeb03)   0x0341 |
|  | Heart Rate Belt. |
| #define | [BT\_APPEARANCE\_GENERIC\_BLOOD\_PRESSURE](#ga3ab7a9595e00208a9e6a56dca99b56c2)   0x0380 |
|  | Generic Blood Pressure. |
| #define | [BT\_APPEARANCE\_BLOOD\_PRESSURE\_ARM](#ga55c3e67d27c8fd8ae06880ccdd9259ce)   0x0381 |
|  | Arm Blood Pressure. |
| #define | [BT\_APPEARANCE\_BLOOD\_PRESSURE\_WRIST](#ga89684ca0544a400293b663cdf0063cfa)   0x0382 |
|  | Wrist Blood Pressure. |
| #define | [BT\_APPEARANCE\_GENERIC\_HID](#gaf2050baedf0863ec37177dd2ef872d39)   0x03C0 |
|  | Generic Human Interface Device. |
| #define | [BT\_APPEARANCE\_HID\_KEYBOARD](#gaa74af272423a80d5489ed8cf6c3ee66c)   0x03C1 |
|  | Keyboard. |
| #define | [BT\_APPEARANCE\_HID\_MOUSE](#ga3b6ba8ffe424db08583186c448e37149)   0x03C2 |
|  | Mouse. |
| #define | [BT\_APPEARANCE\_HID\_JOYSTICK](#ga2f9f15df2260a1307f5142f37437bf0c)   0x03C3 |
|  | Joystick. |
| #define | [BT\_APPEARANCE\_HID\_GAMEPAD](#ga770336524e74d106cb18354f9dbfad76)   0x03C4 |
|  | Gamepad. |
| #define | [BT\_APPEARANCE\_HID\_DIGITIZER\_TABLET](#gacac11dcb96ab60963a1118e171a731de)   0x03C5 |
|  | Digitizer Tablet. |
| #define | [BT\_APPEARANCE\_HID\_CARD\_READER](#gaa03c3b4d7ea8211748316146afab8bd4)   0x03C6 |
|  | Card Reader. |
| #define | [BT\_APPEARANCE\_HID\_DIGITAL\_PEN](#ga002a1d7965b23ec62c8a196f4e5452d9)   0x03C7 |
|  | Digital Pen. |
| #define | [BT\_APPEARANCE\_HID\_BARCODE\_SCANNER](#gaf88f83afd454fe88dd7146e10ef6d35e)   0x03C8 |
|  | Barcode Scanner. |
| #define | [BT\_APPEARANCE\_HID\_TOUCHPAD](#gaee207f9434bce7d0f7e096bf3b37a01c)   0x03C9 |
|  | Touchpad. |
| #define | [BT\_APPEARANCE\_HID\_PRESENTATION\_REMOTE](#gae415dd9e8d620dfd1981719f4ed2d796)   0x03CA |
|  | Presentation Remote. |
| #define | [BT\_APPEARANCE\_GENERIC\_GLUCOSE](#ga209645f7445873beb50c388cc82aff2a)   0x0400 |
|  | Generic Glucose Meter. |
| #define | [BT\_APPEARANCE\_GENERIC\_WALKING](#ga9cf19d97db0c4c5b8473b72809b51d42)   0x0440 |
|  | Generic Running Walking Sensor. |
| #define | [BT\_APPEARANCE\_WALKING\_IN\_SHOE](#gad748f5dc2e0622353d6159c3a3e4241b)   0x0441 |
|  | In-Shoe Running Walking Sensor. |
| #define | [BT\_APPEARANCE\_WALKING\_ON\_SHOE](#ga0a4541459ba8b41a3938c5b8d35b1c8c)   0x0442 |
|  | On-Shoe Running Walking Sensor. |
| #define | [BT\_APPEARANCE\_WALKING\_ON\_HIP](#gad211a7e2f11dc7effe3ba28e8c4f7092)   0x0443 |
|  | On-Hip Running Walking Sensor. |
| #define | [BT\_APPEARANCE\_GENERIC\_CYCLING](#ga7a0463b9b0df37bce80cada38b10ee54)   0x0480 |
|  | Generic Cycling. |
| #define | [BT\_APPEARANCE\_CYCLING\_COMPUTER](#ga3e81dce23c3d005a9b48ff83c7b8f896)   0x0481 |
|  | Cycling Computer. |
| #define | [BT\_APPEARANCE\_CYCLING\_SPEED](#ga16fb08fa70272252ab6b2d3a5aec485a)   0x0482 |
|  | Speed Sensor. |
| #define | [BT\_APPEARANCE\_CYCLING\_CADENCE](#ga71dc370aad015e88fce7c3e758c647ed)   0x0483 |
|  | Cadence Sensor. |
| #define | [BT\_APPEARANCE\_CYCLING\_POWER](#ga02fd9566d9b932aeaa1163d312fbc4d8)   0x0484 |
|  | Power Sensor. |
| #define | [BT\_APPEARANCE\_CYCLING\_SPEED\_CADENCE](#ga48d8f2a285795785f8f51ce220d46371)   0x0485 |
|  | Speed and Cadence Sensor. |
| #define | [BT\_APPEARANCE\_GENERIC\_CONTROL\_DEVICE](#ga5e16df5eefcae8556dfc387135e2b1b6)   0x04C0 |
|  | Generic Control Device. |
| #define | [BT\_APPEARANCE\_CONTROL\_SWITCH](#gac53247d00e3da69595274e0b94fa670f)   0x04C1 |
|  | Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_MULTI\_SWITCH](#gad30c40df58e160128893e545a11ab44c)   0x04C2 |
|  | Multi-switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_BUTTON](#ga52dfd2858663b7ab624f0c4b08cee7dc)   0x04C3 |
|  | Button. |
| #define | [BT\_APPEARANCE\_CONTROL\_SLIDER](#gaa849d890c000defcaf29893296c86cc5)   0x04C4 |
|  | Slider. |
| #define | [BT\_APPEARANCE\_CONTROL\_ROTARY\_SWITCH](#ga946b6a8bb49bf0b5cd3ded93ee8dfe89)   0x04C5 |
|  | Rotary Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_TOUCH\_PANEL](#ga4d5763288557e7b7f6da0f3e9831171d)   0x04C6 |
|  | Touch Panel. |
| #define | [BT\_APPEARANCE\_CONTROL\_SINGLE\_SWITCH](#ga979ca0f4febeaa55daec07e2b3b0179e)   0x04C7 |
|  | Single Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_DOUBLE\_SWITCH](#gac1c80dbb8aaa327b6125bf632692c3be)   0x04C8 |
|  | Double Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_TRIPLE\_SWITCH](#gaa532fd1bd67c2c5b72822704a62df143)   0x04C9 |
|  | Triple Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_BATTERY\_SWITCH](#gaea669671a53b3df5b1aa4c43e5bde9b9)   0x04CA |
|  | Battery Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_ENERGY\_HARVESTING\_SWITCH](#gadec2907a822e302d5027f162ef9ce4b6)   0x04CB |
|  | Energy Harvesting Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_PUSH\_BUTTON](#ga9bb358864e1388cc00502b5586ec581f)   0x04CC |
|  | Push Button. |
| #define | [BT\_APPEARANCE\_GENERIC\_NETWORK\_DEVICE](#gac4727ec720344ece687256ac517800e7)   0x0500 |
|  | Generic Network Device. |
| #define | [BT\_APPEARANCE\_NETWORK\_ACCESS\_POINT](#ga265ba959769d56f42ff621a20e193aba)   0x0501 |
|  | Access Point. |
| #define | [BT\_APPEARANCE\_NETWORK\_MESH\_DEVICE](#gadcc3d795579a731ae03ade14d5193408)   0x0502 |
|  | Mesh Device. |
| #define | [BT\_APPEARANCE\_NETWORK\_MESH\_PROXY](#gad4c5f5840a8caba73d55b0138e506bd0)   0x0503 |
|  | Mesh Network Proxy. |
| #define | [BT\_APPEARANCE\_GENERIC\_SENSOR](#gab3241fe012482e716c3f18e2962ca15d)   0x0540 |
|  | Generic Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_MOTION](#gab49b84183136e9b65ba2e1f5490a79ed)   0x0541 |
|  | Motion Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_AIR\_QUALITY](#gaacb0779499ad4aaa83f0b6303460caf8)   0x0542 |
|  | Air quality Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_TEMPERATURE](#ga5e072a902bf145dc2b00dbd1c8a64b52)   0x0543 |
|  | Temperature Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_HUMIDITY](#ga2deff206602e1e0784af9456ef8abd5b)   0x0544 |
|  | Humidity Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_LEAK](#ga2cbac5e931080f1f5cb3c9bb4c73e9d8)   0x0545 |
|  | Leak Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_SMOKE](#gaeedc0612f8ca171aec061cf02ee907e4)   0x0546 |
|  | Smoke Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_OCCUPANCY](#ga8e8b7834c82c42a0076300aca20c2d35)   0x0547 |
|  | Occupancy Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_CONTACT](#gac71e281cf1b8d1b6535623ec34c7d63f)   0x0548 |
|  | Contact Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_CARBON\_MONOXIDE](#ga0e60b365f871c17c0015ffcf8bc1646e)   0x0549 |
|  | Carbon Monoxide Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_CARBON\_DIOXIDE](#ga34ed8c9aefe34d5030209f073c9ecd24)   0x054A |
|  | Carbon Dioxide Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_AMBIENT\_LIGHT](#ga622508f9b051ed0320700b01967f6446)   0x054B |
|  | Ambient Light Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_ENERGY](#gaca0cfcd560fa4133c0bc62a61d2874c7)   0x054C |
|  | Energy Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_COLOR\_LIGHT](#ga8106142ddb6445e7462137e032e50854)   0x054D |
|  | Color Light Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_RAIN](#ga380da83e3a69de3fd5091cdc89f7fcbc)   0x054E |
|  | Rain Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_FIRE](#ga425115e6c251a9c493c98d79f659077d)   0x054F |
|  | Fire Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_WIND](#gaa710c0666d8b5bf1e1230672cbbf55fa)   0x0550 |
|  | Wind Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_PROXIMITY](#ga6d3447e24d5d75051b81998fd9ad8bfe)   0x0551 |
|  | Proximity Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_MULTI](#gaeec9666dbdb31e9302a25aaa536f3180)   0x0552 |
|  | Multi-Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_FLUSH\_MOUNTED](#gaf9a9c0191ec175d14061058cf3da163c)   0x0553 |
|  | Flush Mounted Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_CEILING\_MOUNTED](#gadfb6808db5a7060316b724c24c8ceaf8)   0x0554 |
|  | Ceiling Mounted Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_WALL\_MOUNTED](#gae564900f0517d393ceffcca8d27f6e45)   0x0555 |
|  | Wall Mounted Sensor. |
| #define | [BT\_APPEARANCE\_MULTISENSOR](#ga90237753920702380321e9f858344741)   0x0556 |
|  | Multisensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_ENERGY\_METER](#ga7238d3a45f9e62f0189db9d7eeac4d15)   0x0557 |
|  | Energy Meter. |
| #define | [BT\_APPEARANCE\_SENSOR\_FLAME\_DETECTOR](#gaae8f95ef639cb7d5e97063eed710a07d)   0x0558 |
|  | Flame Detector. |
| #define | [BT\_APPEARANCE\_SENSOR\_VEHICLE\_TIRE\_PRESSURE](#ga4d0877a3cd9b7efebbaa5fd8a988a2a3)   0x0559 |
|  | Vehicle Tire Pressure Sensor. |
| #define | [BT\_APPEARANCE\_GENERIC\_LIGHT\_FIXTURES](#gae01be867f730c06b59fcb03289ae66d7)   0x0580 |
|  | Generic Light Fixtures. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_WALL](#gae1b2b535754f9cdc24c4a6cee63ef5cb)   0x0581 |
|  | Wall Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_CEILING](#ga2d77fb5f5ed9a43771186ecc5693da8f)   0x0582 |
|  | Ceiling Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOR](#ga57bb461b0ddd045d21d7fbd3843fbabb)   0x0583 |
|  | Floor Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_CABINET](#gadc48840b6590a89593a5d17fbdb1e9e9)   0x0584 |
|  | Cabinet Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_DESK](#ga2f37bf95ea6057b999bbf2cf94016e5d)   0x0585 |
|  | Desk Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_TROFFER](#gaa57b538ecad380ad77354e0cd9576e5b)   0x0586 |
|  | Troffer Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_PENDANT](#ga336147b54406237e25d8cf9ed152928b)   0x0587 |
|  | Pendant Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_IN\_GROUND](#ga583b7432ba6ac4cc078d3a069e3a54e1)   0x0588 |
|  | In-ground Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOD](#gab41f8b6f1ff0f624bb6666ef2ac6dab3)   0x0589 |
|  | Flood Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_UNDERWATER](#ga83f50305a23250e5e2cef5004762e122)   0x058A |
|  | Underwater Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_BOLLARD\_WITH](#ga20a7b241f292475d70626a38d983886c)   0x058B |
|  | Bollard with Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_PATHWAY](#ga7c5811bd50d9f78e67e3e56faa432aae)   0x058C |
|  | Pathway Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_GARDEN](#ga348e64ffe0f3d6301dd8c911f70ead68)   0x058D |
|  | Garden Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_POLE\_TOP](#ga0da0cbeebd2b20bf28dfc06def016068)   0x058E |
|  | Pole-top Light. |
| #define | [BT\_APPEARANCE\_SPOT\_LIGHT](#ga58e1989c99b5a223a318a716d62f6e2b)   0x058F |
|  | Spotlight. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_LINEAR](#ga5388daf123e629d6f7a0b9af13fbc366)   0x0590 |
|  | Linear Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_STREET](#gac938fb03553d2d3c27b50af2a9a1ac48)   0x0591 |
|  | Street Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_SHELVES](#ga1bf2889f7a8a7ae363bc1d4355ee8d65)   0x0592 |
|  | Shelves Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_BAY](#ga8f98c2d32664a6e03ebc2a43ae1eb52a)   0x0593 |
|  | Bay Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_EMERGENCY\_EXIT](#ga3f687f994ffff2ce70b81a992195d210)   0x0594 |
|  | Emergency Exit Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_CONTROLLER](#ga35a90a4e3bfef7b0cfec0d5fa7b36c4a)   0x0595 |
|  | Light Controller. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_DRIVER](#gac2b6de99b4e87f7c40063ba844c75ead)   0x0596 |
|  | Light Driver. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_BULB](#ga8325830f2c977dc238a9ca1b9837803e)   0x0597 |
|  | Bulb. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_LOW\_BAY](#gafc924bbc1b6aff0130c2be3d5fe59e33)   0x0598 |
|  | Low-bay Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_HIGH\_BAY](#ga738e87008c6a64450bb7ec22dbcdd113)   0x0599 |
|  | High-bay Light. |
| #define | [BT\_APPEARANCE\_GENERIC\_FAN](#ga82cc89321c4f4ffbf3ef25eff624943c)   0x05C0 |
|  | Generic Fan. |
| #define | [BT\_APPEARANCE\_FAN\_CEILING](#ga8cd83cd08846ac276cc65f31333ee62e)   0x05C1 |
|  | Ceiling Fan. |
| #define | [BT\_APPEARANCE\_FAN\_AXIAL](#ga32dd73ffa211d632617018aa510b89c4)   0x05C2 |
|  | Axial Fan. |
| #define | [BT\_APPEARANCE\_FAN\_EXHAUST](#ga1e842c97b90678908f4d18c86c1227c2)   0x05C3 |
|  | Exhaust Fan. |
| #define | [BT\_APPEARANCE\_FAN\_PEDESTAL](#ga2e54f8de862435f2dbd7f56b98615c84)   0x05C4 |
|  | Pedestal Fan. |
| #define | [BT\_APPEARANCE\_FAN\_DESK](#gaa9e17b8b5e06d2fb365bf152e0cbef5d)   0x05C5 |
|  | Desk Fan. |
| #define | [BT\_APPEARANCE\_FAN\_WALL](#ga498be79799cb778c9df6629411fe32ad)   0x05C6 |
|  | Wall Fan. |
| #define | [BT\_APPEARANCE\_GENERIC\_HVAC](#gaf1f01946f6acadcaf719d3d7cc06e55f)   0x0600 |
|  | Generic HVAC. |
| #define | [BT\_APPEARANCE\_HVAC\_THERMOSTAT](#ga33055b50c10bfc713b18823fca525488)   0x0601 |
|  | Thermostat. |
| #define | [BT\_APPEARANCE\_HVAC\_HUMIDIFIER](#gaf55f3f3f07cc78509e7fe19cea6cea4e)   0x0602 |
|  | Humidifier. |
| #define | [BT\_APPEARANCE\_HVAC\_DEHUMIDIFIER](#gaa3b96e44638048b8891a2dece29f4b3f)   0x0603 |
|  | De-humidifier. |
| #define | [BT\_APPEARANCE\_HVAC\_HEATER](#gacef9145f435d10cbf5a775b9a2c9b756)   0x0604 |
|  | Heater. |
| #define | [BT\_APPEARANCE\_HVAC\_RADIATOR](#gad90f108f3d33d68e27ac545cdb520f18)   0x0605 |
|  | Radiator. |
| #define | [BT\_APPEARANCE\_HVAC\_BOILER](#gacc28a1bc1a809c574019455de4ac9d0b)   0x0606 |
|  | Boiler. |
| #define | [BT\_APPEARANCE\_HVAC\_HEAT\_PUMP](#gaead4ebeabb8855111ab9080aca4e035a)   0x0607 |
|  | Heat Pump. |
| #define | [BT\_APPEARANCE\_HVAC\_INFRARED\_HEATER](#ga50c5df52d8471fc8e1dc65e31079566d)   0x0608 |
|  | Infrared Heater. |
| #define | [BT\_APPEARANCE\_HVAC\_RADIANT\_PANEL\_HEATER](#gad43d27ff96a7fba1ed7d5e20ebd472d9)   0x0609 |
|  | Radiant Panel Heater. |
| #define | [BT\_APPEARANCE\_HVAC\_FAN\_HEATER](#ga2a044c3369ed48d216707f6e6a541a23)   0x060A |
|  | Fan Heater. |
| #define | [BT\_APPEARANCE\_HVAC\_AIR\_CURTAIN](#ga182ade4b2c8f4705ba132248e504bb95)   0x060B |
|  | Air Curtain. |
| #define | [BT\_APPEARANCE\_GENERIC\_AIR\_CONDITIONING](#gaa13ae6496d47df2be0a0692a28806007)   0x0640 |
|  | Generic Air Conditioning. |
| #define | [BT\_APPEARANCE\_GENERIC\_HUMIDIFIER](#ga0b552243744bc598467421555e935cd0)   0x0680 |
|  | Generic Humidifier. |
| #define | [BT\_APPEARANCE\_GENERIC\_HEATING](#ga8ea92ea92ca4e2bad4e5e2baba1271dd)   0x06C0 |
|  | Generic Heating. |
| #define | [BT\_APPEARANCE\_HEATING\_RADIATOR](#ga05b0b91c74aed5bc73a92f336bdae33a)   0x06C1 |
|  | Radiator. |
| #define | [BT\_APPEARANCE\_HEATING\_BOILER](#gac1abc9ae0b8ede2197720ea9e67b692e)   0x06C2 |
|  | Boiler. |
| #define | [BT\_APPEARANCE\_HEATING\_HEAT\_PUMP](#ga99537968fdc7e680d922ca309fba7678)   0x06C3 |
|  | Heat Pump. |
| #define | [BT\_APPEARANCE\_HEATING\_INFRARED\_HEATER](#ga8e40496a351c7ec5ea836805925f1e13)   0x06C4 |
|  | Infrared Heater. |
| #define | [BT\_APPEARANCE\_HEATING\_RADIANT\_PANEL\_HEATER](#ga46fe051c7e50492dba5ae824e154cf69)   0x06C5 |
|  | Radiant Panel Heater. |
| #define | [BT\_APPEARANCE\_HEATING\_FAN\_HEATER](#ga995ca18db114ea062df0d76c9e241937)   0x06C6 |
|  | Fan Heater. |
| #define | [BT\_APPEARANCE\_HEATING\_AIR\_CURTAIN](#gac74bc8e109f5d9b4c0988ee6378ed471)   0x06C7 |
|  | Air Curtain. |
| #define | [BT\_APPEARANCE\_GENERIC\_ACCESS\_CONTROL](#gac856a99a5db04dc20229a6e60a18d310)   0x0700 |
|  | Generic Access Control. |
| #define | [BT\_APPEARANCE\_CONTROL\_ACCESS\_DOOR](#ga8e21f7df9d789b7c3aa6f7dab500df8c)   0x0701 |
|  | Access Door. |
| #define | [BT\_APPEARANCE\_CONTROL\_GARAGE\_DOOR](#ga39134568b56c1d33e6567c893eb441f1)   0x0702 |
|  | Garage Door. |
| #define | [BT\_APPEARANCE\_CONTROL\_EMERGENCY\_EXIT\_DOOR](#ga2b6c7987ee4040216a385e665ff92321)   0x0703 |
|  | Emergency Exit Door. |
| #define | [BT\_APPEARANCE\_CONTROL\_ACCESS\_LOCK](#gac2f588b6202e9d6140ec682cfe45f65d)   0x0704 |
|  | Access Lock. |
| #define | [BT\_APPEARANCE\_CONTROL\_ELEVATOR](#ga321d63ead349c0a83ef289bd2e4efb33)   0x0705 |
|  | Elevator. |
| #define | [BT\_APPEARANCE\_CONTROL\_WINDOW](#gaedc6415432862889e7f002fc9ef46b74)   0x0706 |
|  | Window. |
| #define | [BT\_APPEARANCE\_CONTROL\_ENTRANCE\_GATE](#gab2a476a90f20576c0a1784fdc1e5e633)   0x0707 |
|  | Entrance Gate. |
| #define | [BT\_APPEARANCE\_CONTROL\_DOOR\_LOCK](#ga29d07ce1101740b5f6f980660e405278)   0x0708 |
|  | Door Lock. |
| #define | [BT\_APPEARANCE\_CONTROL\_LOCKER](#ga824236ba19c7f54d06b9abcd7df8c767)   0x0709 |
|  | Locker. |
| #define | [BT\_APPEARANCE\_GENERIC\_MOTORIZED\_DEVICE](#ga414b202e93d1db533853093d66603720)   0x0740 |
|  | Generic Motorized Device. |
| #define | [BT\_APPEARANCE\_MOTORIZED\_GATE](#ga376ef909868a5c273b71d1c372755707)   0x0741 |
|  | Motorized Gate. |
| #define | [BT\_APPEARANCE\_MOTORIZED\_AWNING](#ga338de5523abf3fd81e913f3cdb4a31b6)   0x0742 |
|  | Awning. |
| #define | [BT\_APPEARANCE\_MOTORIZED\_BLINDS\_OR\_SHADES](#gaaa39c48ed2d6edd5650743b82154462b)   0x0743 |
|  | Blinds or Shades. |
| #define | [BT\_APPEARANCE\_MOTORIZED\_CURTAINS](#ga53f6a4df5ccc2117525952be2e174ddc)   0x0744 |
|  | Curtains. |
| #define | [BT\_APPEARANCE\_MOTORIZED\_SCREEN](#ga5f32cab5c7a155fffbe0c33cadfef31a)   0x0745 |
|  | Screen. |
| #define | [BT\_APPEARANCE\_GENERIC\_POWER\_DEVICE](#gadae82e45d9aafd34cafd3f0e793b1b24)   0x0780 |
|  | Generic Power Device. |
| #define | [BT\_APPEARANCE\_POWER\_OUTLET](#gad9efd19e2c95525a3972c8b0f0417449)   0x0781 |
|  | Power Outlet. |
| #define | [BT\_APPEARANCE\_POWER\_STRIP](#ga2c5bd38d4eeb1aad2d29b004390a6d18)   0x0782 |
|  | Power Strip. |
| #define | [BT\_APPEARANCE\_POWER\_PLUG](#ga0d9aadc19f5f5f484769b225164866e4)   0x0783 |
|  | Plug. |
| #define | [BT\_APPEARANCE\_POWER\_SUPPLY](#ga07acce808c9cf2b5e84aacd65e8f256d)   0x0784 |
|  | Power Supply. |
| #define | [BT\_APPEARANCE\_POWER\_LED\_DRIVER](#ga31842298741c822dcebba942453975c6)   0x0785 |
|  | LED Driver. |
| #define | [BT\_APPEARANCE\_POWER\_FLUORESCENT\_LAMP\_GEAR](#ga7de26016aa039e3e72ddd61653e1c1d8)   0x0786 |
|  | Fluorescent Lamp Gear. |
| #define | [BT\_APPEARANCE\_POWER\_HID\_LAMP\_GEAR](#ga6396b1d813c9764bdfe92c4f2ba961b1)   0x0787 |
|  | HID Lamp Gear. |
| #define | [BT\_APPEARANCE\_POWER\_CHARGE\_CASE](#ga5d6b28b9660d2357e2af2bf0ceab9c18)   0x0788 |
|  | Charge Case. |
| #define | [BT\_APPEARANCE\_POWER\_POWER\_BANK](#gab6a5ac3941a5707f052126810a7f22e0)   0x0789 |
|  | Power Bank. |
| #define | [BT\_APPEARANCE\_GENERIC\_LIGHT\_SOURCE](#gacb3340c5193588eea2d42fe1bef443d0)   0x07C0 |
|  | Generic Light Source. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_INCANDESCENT\_BULB](#gafed8531ffde21d0ad6e8d477d64496f0)   0x07C1 |
|  | Incandescent Light Bulb. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_LAMP](#ga66bf91b8a25ac88a0fd6ab9456201de1)   0x07C2 |
|  | LED Lamp. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_HID\_LAMP](#ga1babd2989112bafb5819235fe5b6c556)   0x07C3 |
|  | HID Lamp. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_FLUORESCENT\_LAMP](#ga39957a77aa54255ab3a06441e422e7e3)   0x07C4 |
|  | Fluorescent Lamp. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_ARRAY](#ga242d324cf5cf33e4edd5cf33e8c3c89b)   0x07C5 |
|  | LED Array. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_MULTICOLOR\_LED\_ARRAY](#ga8449006920ed1fdd562c702ee2e16a21)   0x07C6 |
|  | Multi-Color LED Array. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_LOW\_VOLTAGE\_HALOGEN](#gaf47bce54f4ae1915cd64c3c2d254e353)   0x07C7 |
|  | Low voltage halogen. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_OLED](#gaed4400a94dae4f536a456cc55eb6f6d5)   0x07C8 |
|  | Organic light emitting diode. |
| #define | [BT\_APPEARANCE\_GENERIC\_WINDOW\_COVERING](#ga1e70d961fca2719243c866464132684c)   0x0800 |
|  | Generic Window Covering. |
| #define | [BT\_APPEARANCE\_WINDOW\_SHADES](#ga37614ae63c8287bc4bd0c9a5bf00502e)   0x0801 |
|  | Window Shades. |
| #define | [BT\_APPEARANCE\_WINDOW\_BLINDS](#ga717efaeab0329ded066567761b9983a7)   0x0802 |
|  | Window Blinds. |
| #define | [BT\_APPEARANCE\_WINDOW\_AWNING](#ga9945bb52a9ee3268efda7d5e05421e12)   0x0803 |
|  | Window Awning. |
| #define | [BT\_APPEARANCE\_WINDOW\_CURTAIN](#ga20352e58e6cec63efbb6beaa75c0e330)   0x0804 |
|  | Window Curtain. |
| #define | [BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SHUTTER](#ga7ead13b128fbc50be3f5c101fb1383cb)   0x0805 |
|  | Exterior Shutter. |
| #define | [BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SCREEN](#ga0a0b87095177af0560a540e545c97f42)   0x0806 |
|  | Exterior Screen. |
| #define | [BT\_APPEARANCE\_GENERIC\_AUDIO\_SINK](#ga32bb0f06096ce5259676a31342b9f0d9)   0x0840 |
|  | Generic Audio Sink. |
| #define | [BT\_APPEARANCE\_AUDIO\_SINK\_STANDALONE\_SPEAKER](#gabcb109c4660a177494329faf353406f4)   0x0841 |
|  | Standalone Speaker. |
| #define | [BT\_APPEARANCE\_AUDIO\_SINK\_SOUNDBAR](#ga93e3a858b2efabea72a8855a28ad21c2)   0x0842 |
|  | Soundbar. |
| #define | [BT\_APPEARANCE\_AUDIO\_SINK\_BOOKSHELF\_SPEAKER](#ga666aed968e9a0f9566edcc1bcba0bfbd)   0x0843 |
|  | Bookshelf Speaker. |
| #define | [BT\_APPEARANCE\_AUDIO\_SINK\_STANDMOUNTED\_SPEAKER](#ga6b3ddddf1de7d95a15aa6194ddc656ee)   0x0844 |
|  | Standmounted Speaker. |
| #define | [BT\_APPEARANCE\_AUDIO\_SINK\_SPEAKERPHONE](#gadd82602d251aa555a06123ef0388d1b1)   0x0845 |
|  | Speakerphone. |
| #define | [BT\_APPEARANCE\_GENERIC\_AUDIO\_SOURCE](#gac85b90f2585044d0efa61191dba3c596)   0x0880 |
|  | Generic Audio Source. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_MICROPHONE](#ga6dd1354de34ed79702d9d7878d859fcb)   0x0881 |
|  | Microphone. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_ALARM](#gaa8d5a95cb181e27efb2409d5dce3da57)   0x0882 |
|  | Alarm. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_BELL](#ga748b4fa86145f3950069ed44cde8cacb)   0x0883 |
|  | Bell. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_HORN](#ga3415afbd526b29b5bbafc1ac889bd371)   0x0884 |
|  | Horn. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_DEVICE](#ga35ecc1a1051379010123582c82e9b31c)   0x0885 |
|  | Broadcasting Device. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_SERVICE\_DESK](#ga48fc37d769211cba1e6121e670b02e25)   0x0886 |
|  | Service Desk. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_KIOSK](#ga6ad3ee00ed05c8a7ed182df5c82a5af4)   0x0887 |
|  | Kiosk. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_ROOM](#gaad0fe38e5246c55cc562729448b9f390)   0x0888 |
|  | Broadcasting Room. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_AUDITORIUM](#gac8ab0549f83c9d6b68dc4dd75cfe7b1e)   0x0889 |
|  | Auditorium. |
| #define | [BT\_APPEARANCE\_GENERIC\_MOTORIZED\_VEHICLE](#ga49328394fd7505da9476d4d62ae60c03)   0x08C0 |
|  | Generic Motorized Vehicle. |
| #define | [BT\_APPEARANCE\_VEHICLE\_CAR](#ga6257291ed3e6d09ce6197e2081b36d04)   0x08C1 |
|  | Car. |
| #define | [BT\_APPEARANCE\_VEHICLE\_LARGE\_GOODS](#ga31ff643e1efccffd9ba73c793f63837c)   0x08C2 |
|  | Large Goods Vehicle. |
| #define | [BT\_APPEARANCE\_VEHICLE\_TWO\_WHEELED](#ga68ade931a12e5d9e9863decad3d8de9e)   0x08C3 |
|  | 2-Wheeled Vehicle |
| #define | [BT\_APPEARANCE\_VEHICLE\_MOTORBIKE](#gaa71eaa4fd0eef66a794475cb44aaf397)   0x08C4 |
|  | Motorbike. |
| #define | [BT\_APPEARANCE\_VEHICLE\_SCOOTER](#gae082982b90d94404b69c57987d8a2c5a)   0x08C5 |
|  | Scooter. |
| #define | [BT\_APPEARANCE\_VEHICLE\_MOPED](#ga18b0231dbd97d8871f685774f9e1b4e1)   0x08C6 |
|  | Moped. |
| #define | [BT\_APPEARANCE\_VEHICLE\_THREE\_WHEELED](#ga8159dfd6933a2a5fdb2c72da9623bc2e)   0x08C7 |
|  | 3-Wheeled Vehicle |
| #define | [BT\_APPEARANCE\_VEHICLE\_LIGHT](#gac22a0476760c42eb8f00b36b74361c5e)   0x08C8 |
|  | Light Vehicle. |
| #define | [BT\_APPEARANCE\_VEHICLE\_QUAD\_BIKE](#ga03e3660bdc2e439126f2f8df8ea335ee)   0x08C9 |
|  | Quad Bike. |
| #define | [BT\_APPEARANCE\_VEHICLE\_MINIBUS](#ga0cf473bbf07d4576ab9f0116ca48f161)   0x08CA |
|  | Minibus. |
| #define | [BT\_APPEARANCE\_VEHICLE\_BUS](#ga0da02a18987c653a3232c28a3e4908f7)   0x08CB |
|  | Bus. |
| #define | [BT\_APPEARANCE\_VEHICLE\_TROLLEY](#gabde7af9f7c25d56f5fb9643398273526)   0x08CC |
|  | Trolley. |
| #define | [BT\_APPEARANCE\_VEHICLE\_AGRICULTURAL](#gaa149e56e4b4a1b6dde821fbdac3d9c32)   0x08CD |
|  | Agricultural Vehicle. |
| #define | [BT\_APPEARANCE\_VEHICLE\_CAMPER\_OR\_CARAVAN](#gafcb3909bf61bb130f8c0a217e69477b8)   0x08CE |
|  | Camper/Caravan. |
| #define | [BT\_APPEARANCE\_VEHICLE\_RECREATIONAL](#ga9366a994d42c88490313380d419b2a8e)   0x08CF |
|  | Recreational Vehicle/Motor Home. |
| #define | [BT\_APPEARANCE\_GENERIC\_DOMESTIC\_APPLIANCE](#gac08b31ff9b618b19e4c1b43ae2056b5f)   0x0900 |
|  | Generic Domestic Appliance. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_REFRIGERATOR](#gad02c3dc8fa1321b14ee70264a36c4950)   0x0901 |
|  | Refrigerator. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_FREEZER](#ga6ec2458a171142a5e22ec339d23a5a0c)   0x0902 |
|  | Freezer. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_OVEN](#ga7a48c5a07e677167ae10412ed2c1040b)   0x0903 |
|  | Oven. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_MICROWAVE](#gabaac12b866cd29547165331333e8be3d)   0x0904 |
|  | Microwave. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_TOASTER](#ga5b0d9632cb2ed4afd856f05a1e857394)   0x0905 |
|  | Toaster. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_WASHING\_MACHINE](#ga1febcada2c95105648831094a4de6a8d)   0x0906 |
|  | Washing Machine. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_DRYER](#gaac26996e0de10b16e24900a08c1098f5)   0x0907 |
|  | Dryer. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_COFFEE\_MAKER](#gac601c74c6132decf13527bdacbc5a08b)   0x0908 |
|  | Coffee maker. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_IRON](#gaeb66941a8e8b38ed0ea47305da157e24)   0x0909 |
|  | Clothes iron. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_CURLING\_IRON](#ga6a9885e9a2133c0732d056ecd63313ad)   0x090A |
|  | Curling iron. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_HAIR\_DRYER](#ga15be0164f5883558fb61c9cb9679b78f)   0x090B |
|  | Hair dryer. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_VACUUM\_CLEANER](#ga46d5f18bb8c764c43af97fddcec4a1ec)   0x090C |
|  | Vacuum cleaner. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_ROBOTIC\_VACUUM\_CLEANER](#ga423e85d0816a4bd0205f4d8188e6c406)   0x090D |
|  | Robotic vacuum cleaner. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_RICE\_COOKER](#ga78511e0ef7d509deeba65352e7f81ad8)   0x090E |
|  | Rice cooker. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_STEAMER](#ga0292c6123b655964311d0e6027b5af20)   0x090F |
|  | Clothes steamer. |
| #define | [BT\_APPEARANCE\_GENERIC\_WEARABLE\_AUDIO\_DEVICE](#gabad761094a16873dcebbc6238825d84b)   0x0940 |
|  | Generic Wearable Audio Device. |
| #define | [BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_EARBUD](#gab480735e2ba8db23d2668ea3a2137214)   0x0941 |
|  | Earbud. |
| #define | [BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADSET](#ga8bd98ba3a4c1cbf8dbf8235d9ad0f943)   0x0942 |
|  | Headset. |
| #define | [BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADPHONES](#gae420044380309abba1b9570d26735315)   0x0943 |
|  | Headphones. |
| #define | [BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_NECK\_BAND](#ga59ea8ff5efec7a19bce8440e7ae78a1e)   0x0944 |
|  | Neck Band. |
| #define | [BT\_APPEARANCE\_GENERIC\_AIRCRAFT](#ga24c9bcf9646ec5049abf310b31ab355e)   0x0980 |
|  | Generic Aircraft. |
| #define | [BT\_APPEARANCE\_AIRCRAFT\_LIGHT](#ga6f1d2fb56f53ac5317b024d7487b8742)   0x0981 |
|  | Light Aircraft. |
| #define | [BT\_APPEARANCE\_AIRCRAFT\_MICROLIGHT](#gad2d0b1c4b710e50127049ec4cd299396)   0x0982 |
|  | Microlight. |
| #define | [BT\_APPEARANCE\_AIRCRAFT\_PARAGLIDER](#ga6f827322066333fe926f0912099e6903)   0x0983 |
|  | Paraglider. |
| #define | [BT\_APPEARANCE\_AIRCRAFT\_LARGE\_PASSENGER](#gae7be5c3bf9ad97e34d6c62bb791c39c0)   0x0984 |
|  | Large Passenger Aircraft. |
| #define | [BT\_APPEARANCE\_GENERIC\_AV\_EQUIPMENT](#gadb3b07d6c3d3f679b15069fdd8d4e1ee)   0x09C0 |
|  | Generic AV Equipment. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_AMPLIFIER](#ga7294c7b26ac8da3b9800c91ec824ad22)   0x09C1 |
|  | Amplifier. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_RECEIVER](#gac826e2e5326d1aa5fdd7ebf55fe395e6)   0x09C2 |
|  | Receiver. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_RADIO](#gad60d1a387a1c62218baa3044e5acc3db)   0x09C3 |
|  | Radio. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_TUNER](#ga7ccf41932861fa5f33d12060a12d5aa7)   0x09C4 |
|  | Tuner. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_TURNTABLE](#ga69417cb3e9c434e751483328d6134cdf)   0x09C5 |
|  | Turntable. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_CD\_PLAYER](#ga6c9ad45a9b22a94ae0cce16bfe749a33)   0x09C6 |
|  | CD Player. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_DVD\_PLAYER](#ga02681af8d755c701d9caef3f89a5c35a)   0x09C7 |
|  | DVD Player. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_BLURAY\_PLAYER](#ga1394bc80927fb8db4eef1786111c65c7)   0x09C8 |
|  | Bluray Player. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_OPTICAL\_DISC\_PLAYER](#gaa01c862bff9aaaad09ed925da60fcb25)   0x09C9 |
|  | Optical Disc Player. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_SET\_TOP\_BOX](#gad0ac86cf291b781b772fa9e85dda283a)   0x09CA |
|  | Set-Top Box. |
| #define | [BT\_APPEARANCE\_GENERIC\_DISPLAY\_EQUIPMENT](#ga44b70b2f515416baf686b1e127ef4375)   0x0A00 |
|  | Generic Display Equipment. |
| #define | [BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_TELEVISION](#ga9a6684aa8677575625e049fa0da2c26c)   0x0A01 |
|  | Television. |
| #define | [BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_MONITOR](#gabbcb0fbbeb6423052db9d5e04410499c)   0x0A02 |
|  | Monitor. |
| #define | [BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_PROJECTOR](#gaa98f5139c99b46515746fb76e9ae7f9b)   0x0A03 |
|  | Projector. |
| #define | [BT\_APPEARANCE\_GENERIC\_HEARING\_AID](#gadb5595a41edf5974e03649a675618b7b)   0x0A40 |
|  | Generic Hearing aid. |
| #define | [BT\_APPEARANCE\_HEARING\_AID\_IN\_EAR](#ga28cc6555937d9d5a9e8ae0079fc8a534)   0x0A41 |
|  | In-ear hearing aid. |
| #define | [BT\_APPEARANCE\_HEARING\_AID\_BEHIND\_EAR](#ga1fa6231e14dcfa90a5518e61f0e4e302)   0x0A42 |
|  | Behind-ear hearing aid. |
| #define | [BT\_APPEARANCE\_HEARING\_AID\_COCHLEAR\_IMPLANT](#ga82ba79bd9fd04a3fbdb6d8b4e35e3877)   0x0A43 |
|  | Cochlear Implant. |
| #define | [BT\_APPEARANCE\_GENERIC\_GAMING](#gaca727b215a8277d921c0a3bfeccb3f14)   0x0A80 |
|  | Generic Gaming. |
| #define | [BT\_APPEARANCE\_HOME\_VIDEO\_GAME\_CONSOLE](#ga8fbaf0fced0cce12e08c4a516351b166)   0x0A81 |
|  | Home Video Game Console. |
| #define | [BT\_APPEARANCE\_PORTABLE\_HANDHELD\_CONSOLE](#ga39ad633d1795af4546bd930d0e799447)   0x0A82 |
|  | Portable handheld console. |
| #define | [BT\_APPEARANCE\_GENERIC\_SIGNAGE](#gabc243c7449804749704c1862db286eab)   0x0AC0 |
|  | Generic Signage. |
| #define | [BT\_APPEARANCE\_SIGNAGE\_DIGITAL](#gace31a591ef3b5f0812e4cbf417a2205a)   0x0AC1 |
|  | Digital Signage. |
| #define | [BT\_APPEARANCE\_SIGNAGE\_ELECTRONIC\_LABEL](#gaa4674b06751edf98fa88ede568a68ad4)   0x0AC2 |
|  | Electronic Label. |
| #define | [BT\_APPEARANCE\_GENERIC\_PULSE\_OXIMETER](#ga93ee753bf3b8819239041c065eaf024f)   0x0C40 |
|  | Generic Pulse Oximeter. |
| #define | [BT\_APPEARANCE\_PULSE\_OXIMETER\_FINGERTIP](#ga8a298130c73299b6079dae3065954c0c)   0x0C41 |
|  | Fingertip Pulse Oximeter. |
| #define | [BT\_APPEARANCE\_PULSE\_OXIMETER\_WRIST](#gaebcadd5c37e6d87903e2cb97e03aeb7d)   0x0C42 |
|  | Wrist Worn Pulse Oximeter. |
| #define | [BT\_APPEARANCE\_GENERIC\_WEIGHT\_SCALE](#ga1aec23cd4f531a57260c7c8faf9caf40)   0x0C80 |
|  | Generic Weight Scale. |
| #define | [BT\_APPEARANCE\_GENERIC\_PERSONAL\_MOBILITY\_DEVICE](#ga7387d717c77b38374e981991278aeb1c)   0x0CC0 |
|  | Generic Personal Mobility Device. |
| #define | [BT\_APPEARANCE\_MOBILITY\_POWERED\_WHEELCHAIR](#ga7966ec64cafe708fe94a7c323fbe3713)   0x0CC1 |
|  | Powered Wheelchair. |
| #define | [BT\_APPEARANCE\_MOBILITY\_SCOOTER](#ga21f21a73f355ffaa408376ca4fc802a8)   0x0CC2 |
|  | Mobility Scooter. |
| #define | [BT\_APPEARANCE\_CONTINUOUS\_GLUCOSE\_MONITOR](#gab77dd4cfe254df84cbe0b8d45247e198)   0x0D00 |
|  | Continuous Glucose Monitor. |
| #define | [BT\_APPEARANCE\_GENERIC\_INSULIN\_PUMP](#ga481169a27fab19628f81a68af31d543c)   0x0D40 |
|  | Generic Insulin Pump. |
| #define | [BT\_APPEARANCE\_INSULIN\_PUMP\_DURABLE](#ga63512439364307259010bededf7bfd8b)   0x0D41 |
|  | Insulin Pump, durable pump. |
| #define | [BT\_APPEARANCE\_INSULIN\_PUMP\_PATCH](#ga0979695247b96321e5a8b6869d09227a)   0x0D44 |
|  | Insulin Pump, patch pump. |
| #define | [BT\_APPEARANCE\_INSULIN\_PEN](#ga1562514d0182e8862edad570b7a346e6)   0x0D48 |
|  | Insulin Pen. |
| #define | [BT\_APPEARANCE\_GENERIC\_MEDICATION\_DELIVERY](#ga08453eebe2ae8f53deddaa64a029c2b5)   0x0D80 |
|  | Generic Medication Delivery. |
| #define | [BT\_APPEARANCE\_GENERIC\_SPIROMETER](#ga1332c44cc3371fa9006993d03ba4ae12)   0x0DC0 |
|  | Generic Spirometer. |
| #define | [BT\_APPEARANCE\_SPIROMETER\_HANDHELD](#ga42b9d596efb757b209f080a8c33f3723)   0x0DC1 |
|  | Handheld Spirometer. |
| #define | [BT\_APPEARANCE\_GENERIC\_OUTDOOR\_SPORTS](#ga0d39ca2892bd96013b8c82111eecc1cb)   0x1440 |
|  | Generic Outdoor Sports Activity. |
| #define | [BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION](#ga30c97d6f5bff1a4a67e4f59eb4d49d2d)   0x1441 |
|  | Location Display. |
| #define | [BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_AND\_NAV](#ga52b6c51c9afcbbba12d9d3cae824f4a7)   0x1442 |
|  | Location and Navigation Display. |
| #define | [BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD](#gadf053353789183d1b1c3ca13ad98559f)   0x1443 |
|  | Location Pod. |
| #define | [BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD\_AND\_NAV](#ga8fbc7782099e724febb712ee108e8cba)   0x1444 |
|  | Location and Navigation Pod. |

| Defined GAP timers | |
| --- | --- |
| #define | [BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN](#gae9356673ee78d9abb27891738344513a)   0x0030 /\* 30 ms \*/ |
| #define | [BT\_GAP\_SCAN\_FAST\_INTERVAL](#ga747caa714962215453a966a323e77cf8)   0x0060 /\* 60 ms \*/ |
| #define | [BT\_GAP\_SCAN\_FAST\_WINDOW](#ga100e1c20813630848a1a80390e8a06a0)   0x0030 /\* 30 ms \*/ |
| #define | [BT\_GAP\_SCAN\_SLOW\_INTERVAL\_1](#ga1acb5143221e9f94af4d5dc3a9eab125)   0x0800 /\* 1.28 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_SCAN\_SLOW\_WINDOW\_1](#ga29a1a15bfbe035f439c48d1db96db392)   0x0012 /\* 11.25 ms \*/ |
| #define | [BT\_GAP\_SCAN\_SLOW\_INTERVAL\_2](#ga38455c10880fddac0a1b4303a642e44d)   0x1000 /\* 2.56 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_SCAN\_SLOW\_WINDOW\_2](#gaa809fd8143c2805768874195ac24936f)   0x0012 /\* 11.25 ms \*/ |
| #define | [BT\_GAP\_ADV\_FAST\_INT\_MIN\_1](#ga397a52fe616416665b46a2bc454c2e11)   0x0030 /\* 30 ms \*/ |
| #define | [BT\_GAP\_ADV\_FAST\_INT\_MAX\_1](#ga13acf16d3d8edd39636bb10df752775a)   0x0060 /\* 60 ms \*/ |
| #define | [BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](#ga9573e6bcdae3aae9d51c0becbbd7ac60)   0x00a0 /\* 100 ms \*/ |
| #define | [BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](#gaebc3ce60836522d883f664227a3ffcfb)   0x00f0 /\* 150 ms \*/ |
| #define | [BT\_GAP\_ADV\_SLOW\_INT\_MIN](#ga647f70c07c15f11287b735cbaad2a326)   0x0640 /\* 1 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_ADV\_SLOW\_INT\_MAX](#gadecbfb823bbb6ffdd48be02df2f05f87)   0x0780 /\* 1.2 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_1](#gafd724ebc809044574283c5547beda824)   0x0018 /\* 30 ms \*/ |
| #define | [BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_1](#ga849315b0b724af6017b910e78db0cfae)   0x0030 /\* 60 ms \*/ |
| #define | [BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_2](#ga61eb4d6d65f1dd9c475a6f2f44b27957)   0x0050 /\* 100 ms \*/ |
| #define | [BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_2](#ga264134294d8378d6e7d2bc52d4e0af1c)   0x0078 /\* 150 ms \*/ |
| #define | [BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN](#gab51898ce46ee9ae468ed7ffc1d117321)   0x0320 /\* 1 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX](#gaa618da2a7c217527b0d962315caa1c22)   0x03C0 /\* 1.2 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_INIT\_CONN\_INT\_MIN](#gadaa7f1547c4ea22936087c181d82a552)   0x0018 /\* 30 ms \*/ |
| #define | [BT\_GAP\_INIT\_CONN\_INT\_MAX](#ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1)   0x0028 /\* 50 ms \*/ |

## Detailed Description

Bluetooth Generic Access Profile defines and Assigned Numbers.

## Macro Definition Documentation

## [◆ ](#gae7be5c3bf9ad97e34d6c62bb791c39c0)BT\_APPEARANCE\_AIRCRAFT\_LARGE\_PASSENGER

| #define BT\_APPEARANCE\_AIRCRAFT\_LARGE\_PASSENGER   0x0984 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Large Passenger Aircraft.

## [◆ ](#ga6f1d2fb56f53ac5317b024d7487b8742)BT\_APPEARANCE\_AIRCRAFT\_LIGHT

| #define BT\_APPEARANCE\_AIRCRAFT\_LIGHT   0x0981 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Light Aircraft.

## [◆ ](#gad2d0b1c4b710e50127049ec4cd299396)BT\_APPEARANCE\_AIRCRAFT\_MICROLIGHT

| #define BT\_APPEARANCE\_AIRCRAFT\_MICROLIGHT   0x0982 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Microlight.

## [◆ ](#ga6f827322066333fe926f0912099e6903)BT\_APPEARANCE\_AIRCRAFT\_PARAGLIDER

| #define BT\_APPEARANCE\_AIRCRAFT\_PARAGLIDER   0x0983 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Paraglider.

## [◆ ](#gaeb66941a8e8b38ed0ea47305da157e24)BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_IRON

| #define BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_IRON   0x0909 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Clothes iron.

## [◆ ](#ga0292c6123b655964311d0e6027b5af20)BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_STEAMER

| #define BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_STEAMER   0x090F |
| --- |

`#include <[gap.h](gap_8h.md)>`

Clothes steamer.

## [◆ ](#gac601c74c6132decf13527bdacbc5a08b)BT\_APPEARANCE\_APPLIANCE\_COFFEE\_MAKER

| #define BT\_APPEARANCE\_APPLIANCE\_COFFEE\_MAKER   0x0908 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Coffee maker.

## [◆ ](#ga6a9885e9a2133c0732d056ecd63313ad)BT\_APPEARANCE\_APPLIANCE\_CURLING\_IRON

| #define BT\_APPEARANCE\_APPLIANCE\_CURLING\_IRON   0x090A |
| --- |

`#include <[gap.h](gap_8h.md)>`

Curling iron.

## [◆ ](#gaac26996e0de10b16e24900a08c1098f5)BT\_APPEARANCE\_APPLIANCE\_DRYER

| #define BT\_APPEARANCE\_APPLIANCE\_DRYER   0x0907 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Dryer.

## [◆ ](#ga6ec2458a171142a5e22ec339d23a5a0c)BT\_APPEARANCE\_APPLIANCE\_FREEZER

| #define BT\_APPEARANCE\_APPLIANCE\_FREEZER   0x0902 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Freezer.

## [◆ ](#ga15be0164f5883558fb61c9cb9679b78f)BT\_APPEARANCE\_APPLIANCE\_HAIR\_DRYER

| #define BT\_APPEARANCE\_APPLIANCE\_HAIR\_DRYER   0x090B |
| --- |

`#include <[gap.h](gap_8h.md)>`

Hair dryer.

## [◆ ](#gabaac12b866cd29547165331333e8be3d)BT\_APPEARANCE\_APPLIANCE\_MICROWAVE

| #define BT\_APPEARANCE\_APPLIANCE\_MICROWAVE   0x0904 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Microwave.

## [◆ ](#ga7a48c5a07e677167ae10412ed2c1040b)BT\_APPEARANCE\_APPLIANCE\_OVEN

| #define BT\_APPEARANCE\_APPLIANCE\_OVEN   0x0903 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Oven.

## [◆ ](#gad02c3dc8fa1321b14ee70264a36c4950)BT\_APPEARANCE\_APPLIANCE\_REFRIGERATOR

| #define BT\_APPEARANCE\_APPLIANCE\_REFRIGERATOR   0x0901 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Refrigerator.

## [◆ ](#ga78511e0ef7d509deeba65352e7f81ad8)BT\_APPEARANCE\_APPLIANCE\_RICE\_COOKER

| #define BT\_APPEARANCE\_APPLIANCE\_RICE\_COOKER   0x090E |
| --- |

`#include <[gap.h](gap_8h.md)>`

Rice cooker.

## [◆ ](#ga423e85d0816a4bd0205f4d8188e6c406)BT\_APPEARANCE\_APPLIANCE\_ROBOTIC\_VACUUM\_CLEANER

| #define BT\_APPEARANCE\_APPLIANCE\_ROBOTIC\_VACUUM\_CLEANER   0x090D |
| --- |

`#include <[gap.h](gap_8h.md)>`

Robotic vacuum cleaner.

## [◆ ](#ga5b0d9632cb2ed4afd856f05a1e857394)BT\_APPEARANCE\_APPLIANCE\_TOASTER

| #define BT\_APPEARANCE\_APPLIANCE\_TOASTER   0x0905 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Toaster.

## [◆ ](#ga46d5f18bb8c764c43af97fddcec4a1ec)BT\_APPEARANCE\_APPLIANCE\_VACUUM\_CLEANER

| #define BT\_APPEARANCE\_APPLIANCE\_VACUUM\_CLEANER   0x090C |
| --- |

`#include <[gap.h](gap_8h.md)>`

Vacuum cleaner.

## [◆ ](#ga1febcada2c95105648831094a4de6a8d)BT\_APPEARANCE\_APPLIANCE\_WASHING\_MACHINE

| #define BT\_APPEARANCE\_APPLIANCE\_WASHING\_MACHINE   0x0906 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Washing Machine.

## [◆ ](#ga666aed968e9a0f9566edcc1bcba0bfbd)BT\_APPEARANCE\_AUDIO\_SINK\_BOOKSHELF\_SPEAKER

| #define BT\_APPEARANCE\_AUDIO\_SINK\_BOOKSHELF\_SPEAKER   0x0843 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Bookshelf Speaker.

## [◆ ](#ga93e3a858b2efabea72a8855a28ad21c2)BT\_APPEARANCE\_AUDIO\_SINK\_SOUNDBAR

| #define BT\_APPEARANCE\_AUDIO\_SINK\_SOUNDBAR   0x0842 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Soundbar.

## [◆ ](#gadd82602d251aa555a06123ef0388d1b1)BT\_APPEARANCE\_AUDIO\_SINK\_SPEAKERPHONE

| #define BT\_APPEARANCE\_AUDIO\_SINK\_SPEAKERPHONE   0x0845 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Speakerphone.

## [◆ ](#gabcb109c4660a177494329faf353406f4)BT\_APPEARANCE\_AUDIO\_SINK\_STANDALONE\_SPEAKER

| #define BT\_APPEARANCE\_AUDIO\_SINK\_STANDALONE\_SPEAKER   0x0841 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Standalone Speaker.

## [◆ ](#ga6b3ddddf1de7d95a15aa6194ddc656ee)BT\_APPEARANCE\_AUDIO\_SINK\_STANDMOUNTED\_SPEAKER

| #define BT\_APPEARANCE\_AUDIO\_SINK\_STANDMOUNTED\_SPEAKER   0x0844 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Standmounted Speaker.

## [◆ ](#gaa8d5a95cb181e27efb2409d5dce3da57)BT\_APPEARANCE\_AUDIO\_SOURCE\_ALARM

| #define BT\_APPEARANCE\_AUDIO\_SOURCE\_ALARM   0x0882 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Alarm.

## [◆ ](#gac8ab0549f83c9d6b68dc4dd75cfe7b1e)BT\_APPEARANCE\_AUDIO\_SOURCE\_AUDITORIUM

| #define BT\_APPEARANCE\_AUDIO\_SOURCE\_AUDITORIUM   0x0889 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Auditorium.

## [◆ ](#ga748b4fa86145f3950069ed44cde8cacb)BT\_APPEARANCE\_AUDIO\_SOURCE\_BELL

| #define BT\_APPEARANCE\_AUDIO\_SOURCE\_BELL   0x0883 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Bell.

## [◆ ](#ga35ecc1a1051379010123582c82e9b31c)BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_DEVICE

| #define BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_DEVICE   0x0885 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Broadcasting Device.

## [◆ ](#gaad0fe38e5246c55cc562729448b9f390)BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_ROOM

| #define BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_ROOM   0x0888 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Broadcasting Room.

## [◆ ](#ga3415afbd526b29b5bbafc1ac889bd371)BT\_APPEARANCE\_AUDIO\_SOURCE\_HORN

| #define BT\_APPEARANCE\_AUDIO\_SOURCE\_HORN   0x0884 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Horn.

## [◆ ](#ga6ad3ee00ed05c8a7ed182df5c82a5af4)BT\_APPEARANCE\_AUDIO\_SOURCE\_KIOSK

| #define BT\_APPEARANCE\_AUDIO\_SOURCE\_KIOSK   0x0887 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Kiosk.

## [◆ ](#ga6dd1354de34ed79702d9d7878d859fcb)BT\_APPEARANCE\_AUDIO\_SOURCE\_MICROPHONE

| #define BT\_APPEARANCE\_AUDIO\_SOURCE\_MICROPHONE   0x0881 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Microphone.

## [◆ ](#ga48fc37d769211cba1e6121e670b02e25)BT\_APPEARANCE\_AUDIO\_SOURCE\_SERVICE\_DESK

| #define BT\_APPEARANCE\_AUDIO\_SOURCE\_SERVICE\_DESK   0x0886 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Service Desk.

## [◆ ](#ga7294c7b26ac8da3b9800c91ec824ad22)BT\_APPEARANCE\_AV\_EQUIPMENT\_AMPLIFIER

| #define BT\_APPEARANCE\_AV\_EQUIPMENT\_AMPLIFIER   0x09C1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Amplifier.

## [◆ ](#ga1394bc80927fb8db4eef1786111c65c7)BT\_APPEARANCE\_AV\_EQUIPMENT\_BLURAY\_PLAYER

| #define BT\_APPEARANCE\_AV\_EQUIPMENT\_BLURAY\_PLAYER   0x09C8 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Bluray Player.

## [◆ ](#ga6c9ad45a9b22a94ae0cce16bfe749a33)BT\_APPEARANCE\_AV\_EQUIPMENT\_CD\_PLAYER

| #define BT\_APPEARANCE\_AV\_EQUIPMENT\_CD\_PLAYER   0x09C6 |
| --- |

`#include <[gap.h](gap_8h.md)>`

CD Player.

## [◆ ](#ga02681af8d755c701d9caef3f89a5c35a)BT\_APPEARANCE\_AV\_EQUIPMENT\_DVD\_PLAYER

| #define BT\_APPEARANCE\_AV\_EQUIPMENT\_DVD\_PLAYER   0x09C7 |
| --- |

`#include <[gap.h](gap_8h.md)>`

DVD Player.

## [◆ ](#gaa01c862bff9aaaad09ed925da60fcb25)BT\_APPEARANCE\_AV\_EQUIPMENT\_OPTICAL\_DISC\_PLAYER

| #define BT\_APPEARANCE\_AV\_EQUIPMENT\_OPTICAL\_DISC\_PLAYER   0x09C9 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Optical Disc Player.

## [◆ ](#gad60d1a387a1c62218baa3044e5acc3db)BT\_APPEARANCE\_AV\_EQUIPMENT\_RADIO

| #define BT\_APPEARANCE\_AV\_EQUIPMENT\_RADIO   0x09C3 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Radio.

## [◆ ](#gac826e2e5326d1aa5fdd7ebf55fe395e6)BT\_APPEARANCE\_AV\_EQUIPMENT\_RECEIVER

| #define BT\_APPEARANCE\_AV\_EQUIPMENT\_RECEIVER   0x09C2 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Receiver.

## [◆ ](#gad0ac86cf291b781b772fa9e85dda283a)BT\_APPEARANCE\_AV\_EQUIPMENT\_SET\_TOP\_BOX

| #define BT\_APPEARANCE\_AV\_EQUIPMENT\_SET\_TOP\_BOX   0x09CA |
| --- |

`#include <[gap.h](gap_8h.md)>`

Set-Top Box.

## [◆ ](#ga7ccf41932861fa5f33d12060a12d5aa7)BT\_APPEARANCE\_AV\_EQUIPMENT\_TUNER

| #define BT\_APPEARANCE\_AV\_EQUIPMENT\_TUNER   0x09C4 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Tuner.

## [◆ ](#ga69417cb3e9c434e751483328d6134cdf)BT\_APPEARANCE\_AV\_EQUIPMENT\_TURNTABLE

| #define BT\_APPEARANCE\_AV\_EQUIPMENT\_TURNTABLE   0x09C5 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Turntable.

## [◆ ](#ga55c3e67d27c8fd8ae06880ccdd9259ce)BT\_APPEARANCE\_BLOOD\_PRESSURE\_ARM

| #define BT\_APPEARANCE\_BLOOD\_PRESSURE\_ARM   0x0381 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Arm Blood Pressure.

## [◆ ](#ga89684ca0544a400293b663cdf0063cfa)BT\_APPEARANCE\_BLOOD\_PRESSURE\_WRIST

| #define BT\_APPEARANCE\_BLOOD\_PRESSURE\_WRIST   0x0382 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Wrist Blood Pressure.

## [◆ ](#gaa4d962ad8661c28ed48f5cf8cd75ad6e)BT\_APPEARANCE\_COMPUTER\_ALL\_IN\_ONE

| #define BT\_APPEARANCE\_COMPUTER\_ALL\_IN\_ONE   0x0089 |
| --- |

`#include <[gap.h](gap_8h.md)>`

All in One.

## [◆ ](#ga53e8eff26f2020b1fc89b21684e54698)BT\_APPEARANCE\_COMPUTER\_BLADE\_SERVER

| #define BT\_APPEARANCE\_COMPUTER\_BLADE\_SERVER   0x008A |
| --- |

`#include <[gap.h](gap_8h.md)>`

Blade Server.

## [◆ ](#ga073dca362cabfd2a07cdc1cb787a0f58)BT\_APPEARANCE\_COMPUTER\_CONVERTIBLE

| #define BT\_APPEARANCE\_COMPUTER\_CONVERTIBLE   0x008B |
| --- |

`#include <[gap.h](gap_8h.md)>`

Convertible.

## [◆ ](#ga1aa0565ca7e00e3a1aa8968e0a7f1bef)BT\_APPEARANCE\_COMPUTER\_DESKTOP\_WORKSTATION

| #define BT\_APPEARANCE\_COMPUTER\_DESKTOP\_WORKSTATION   0x0081 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Desktop Workstation.

## [◆ ](#ga8f35f76cc9de4170006669d6e9e7d72a)BT\_APPEARANCE\_COMPUTER\_DETACHABLE

| #define BT\_APPEARANCE\_COMPUTER\_DETACHABLE   0x008C |
| --- |

`#include <[gap.h](gap_8h.md)>`

Detachable.

## [◆ ](#ga36187d2651d08c4b3e17c36565a2d3c9)BT\_APPEARANCE\_COMPUTER\_DOCKING\_STATION

| #define BT\_APPEARANCE\_COMPUTER\_DOCKING\_STATION   0x0088 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Docking Station.

## [◆ ](#gab64312ea16f03c5998db4429b194b8b0)BT\_APPEARANCE\_COMPUTER\_HANDHELD\_PCPDA

| #define BT\_APPEARANCE\_COMPUTER\_HANDHELD\_PCPDA   0x0084 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Handheld PC/PDA (clamshell).

## [◆ ](#ga6ae353795476853bc3be2196ed220aa7)BT\_APPEARANCE\_COMPUTER\_IOT\_GATEWAY

| #define BT\_APPEARANCE\_COMPUTER\_IOT\_GATEWAY   0x008D |
| --- |

`#include <[gap.h](gap_8h.md)>`

IoT Gateway.

## [◆ ](#ga55ce2ad96a153ed6bdfd841276145c28)BT\_APPEARANCE\_COMPUTER\_LAPTOP

| #define BT\_APPEARANCE\_COMPUTER\_LAPTOP   0x0083 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Laptop.

## [◆ ](#ga3c47c11f56eabec15e960662c64f6fcb)BT\_APPEARANCE\_COMPUTER\_MINI\_PC

| #define BT\_APPEARANCE\_COMPUTER\_MINI\_PC   0x008E |
| --- |

`#include <[gap.h](gap_8h.md)>`

Mini PC.

## [◆ ](#ga9340ed60911fc7c5aab7d317b6925c10)BT\_APPEARANCE\_COMPUTER\_PALMSIZE\_PCPDA

| #define BT\_APPEARANCE\_COMPUTER\_PALMSIZE\_PCPDA   0x0085 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Palm­size PC/PDA.

## [◆ ](#gab71a3c3f836561ac7bd8e52f5e01c769)BT\_APPEARANCE\_COMPUTER\_SERVER\_CLASS

| #define BT\_APPEARANCE\_COMPUTER\_SERVER\_CLASS   0x0082 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Server-class Computer.

## [◆ ](#gabb53daf3eb4ac9ba0cbb1614056ee214)BT\_APPEARANCE\_COMPUTER\_STICK\_PC

| #define BT\_APPEARANCE\_COMPUTER\_STICK\_PC   0x008F |
| --- |

`#include <[gap.h](gap_8h.md)>`

Stick PC.

## [◆ ](#ga11bc881cb5f88956edbf2bb2fe5b358c)BT\_APPEARANCE\_COMPUTER\_TABLET

| #define BT\_APPEARANCE\_COMPUTER\_TABLET   0x0087 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Tablet.

## [◆ ](#ga7c6667ba4c68dec380a548ba9530c110)BT\_APPEARANCE\_COMPUTER\_WEARABLE\_COMPUTER

| #define BT\_APPEARANCE\_COMPUTER\_WEARABLE\_COMPUTER   0x0086 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Wearable computer (watch size).

## [◆ ](#gab77dd4cfe254df84cbe0b8d45247e198)BT\_APPEARANCE\_CONTINUOUS\_GLUCOSE\_MONITOR

| #define BT\_APPEARANCE\_CONTINUOUS\_GLUCOSE\_MONITOR   0x0D00 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Continuous Glucose Monitor.

## [◆ ](#ga8e21f7df9d789b7c3aa6f7dab500df8c)BT\_APPEARANCE\_CONTROL\_ACCESS\_DOOR

| #define BT\_APPEARANCE\_CONTROL\_ACCESS\_DOOR   0x0701 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Access Door.

## [◆ ](#gac2f588b6202e9d6140ec682cfe45f65d)BT\_APPEARANCE\_CONTROL\_ACCESS\_LOCK

| #define BT\_APPEARANCE\_CONTROL\_ACCESS\_LOCK   0x0704 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Access Lock.

## [◆ ](#gaea669671a53b3df5b1aa4c43e5bde9b9)BT\_APPEARANCE\_CONTROL\_BATTERY\_SWITCH

| #define BT\_APPEARANCE\_CONTROL\_BATTERY\_SWITCH   0x04CA |
| --- |

`#include <[gap.h](gap_8h.md)>`

Battery Switch.

## [◆ ](#ga52dfd2858663b7ab624f0c4b08cee7dc)BT\_APPEARANCE\_CONTROL\_BUTTON

| #define BT\_APPEARANCE\_CONTROL\_BUTTON   0x04C3 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Button.

## [◆ ](#ga29d07ce1101740b5f6f980660e405278)BT\_APPEARANCE\_CONTROL\_DOOR\_LOCK

| #define BT\_APPEARANCE\_CONTROL\_DOOR\_LOCK   0x0708 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Door Lock.

## [◆ ](#gac1c80dbb8aaa327b6125bf632692c3be)BT\_APPEARANCE\_CONTROL\_DOUBLE\_SWITCH

| #define BT\_APPEARANCE\_CONTROL\_DOUBLE\_SWITCH   0x04C8 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Double Switch.

## [◆ ](#ga321d63ead349c0a83ef289bd2e4efb33)BT\_APPEARANCE\_CONTROL\_ELEVATOR

| #define BT\_APPEARANCE\_CONTROL\_ELEVATOR   0x0705 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Elevator.

## [◆ ](#ga2b6c7987ee4040216a385e665ff92321)BT\_APPEARANCE\_CONTROL\_EMERGENCY\_EXIT\_DOOR

| #define BT\_APPEARANCE\_CONTROL\_EMERGENCY\_EXIT\_DOOR   0x0703 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Emergency Exit Door.

## [◆ ](#gadec2907a822e302d5027f162ef9ce4b6)BT\_APPEARANCE\_CONTROL\_ENERGY\_HARVESTING\_SWITCH

| #define BT\_APPEARANCE\_CONTROL\_ENERGY\_HARVESTING\_SWITCH   0x04CB |
| --- |

`#include <[gap.h](gap_8h.md)>`

Energy Harvesting Switch.

## [◆ ](#gab2a476a90f20576c0a1784fdc1e5e633)BT\_APPEARANCE\_CONTROL\_ENTRANCE\_GATE

| #define BT\_APPEARANCE\_CONTROL\_ENTRANCE\_GATE   0x0707 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Entrance Gate.

## [◆ ](#ga39134568b56c1d33e6567c893eb441f1)BT\_APPEARANCE\_CONTROL\_GARAGE\_DOOR

| #define BT\_APPEARANCE\_CONTROL\_GARAGE\_DOOR   0x0702 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Garage Door.

## [◆ ](#ga824236ba19c7f54d06b9abcd7df8c767)BT\_APPEARANCE\_CONTROL\_LOCKER

| #define BT\_APPEARANCE\_CONTROL\_LOCKER   0x0709 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Locker.

## [◆ ](#gad30c40df58e160128893e545a11ab44c)BT\_APPEARANCE\_CONTROL\_MULTI\_SWITCH

| #define BT\_APPEARANCE\_CONTROL\_MULTI\_SWITCH   0x04C2 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Multi-switch.

## [◆ ](#ga9bb358864e1388cc00502b5586ec581f)BT\_APPEARANCE\_CONTROL\_PUSH\_BUTTON

| #define BT\_APPEARANCE\_CONTROL\_PUSH\_BUTTON   0x04CC |
| --- |

`#include <[gap.h](gap_8h.md)>`

Push Button.

## [◆ ](#ga946b6a8bb49bf0b5cd3ded93ee8dfe89)BT\_APPEARANCE\_CONTROL\_ROTARY\_SWITCH

| #define BT\_APPEARANCE\_CONTROL\_ROTARY\_SWITCH   0x04C5 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Rotary Switch.

## [◆ ](#ga979ca0f4febeaa55daec07e2b3b0179e)BT\_APPEARANCE\_CONTROL\_SINGLE\_SWITCH

| #define BT\_APPEARANCE\_CONTROL\_SINGLE\_SWITCH   0x04C7 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Single Switch.

## [◆ ](#gaa849d890c000defcaf29893296c86cc5)BT\_APPEARANCE\_CONTROL\_SLIDER

| #define BT\_APPEARANCE\_CONTROL\_SLIDER   0x04C4 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Slider.

## [◆ ](#gac53247d00e3da69595274e0b94fa670f)BT\_APPEARANCE\_CONTROL\_SWITCH

| #define BT\_APPEARANCE\_CONTROL\_SWITCH   0x04C1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Switch.

## [◆ ](#ga4d5763288557e7b7f6da0f3e9831171d)BT\_APPEARANCE\_CONTROL\_TOUCH\_PANEL

| #define BT\_APPEARANCE\_CONTROL\_TOUCH\_PANEL   0x04C6 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Touch Panel.

## [◆ ](#gaa532fd1bd67c2c5b72822704a62df143)BT\_APPEARANCE\_CONTROL\_TRIPLE\_SWITCH

| #define BT\_APPEARANCE\_CONTROL\_TRIPLE\_SWITCH   0x04C9 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Triple Switch.

## [◆ ](#gaedc6415432862889e7f002fc9ef46b74)BT\_APPEARANCE\_CONTROL\_WINDOW

| #define BT\_APPEARANCE\_CONTROL\_WINDOW   0x0706 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Window.

## [◆ ](#ga71dc370aad015e88fce7c3e758c647ed)BT\_APPEARANCE\_CYCLING\_CADENCE

| #define BT\_APPEARANCE\_CYCLING\_CADENCE   0x0483 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Cadence Sensor.

## [◆ ](#ga3e81dce23c3d005a9b48ff83c7b8f896)BT\_APPEARANCE\_CYCLING\_COMPUTER

| #define BT\_APPEARANCE\_CYCLING\_COMPUTER   0x0481 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Cycling Computer.

## [◆ ](#ga02fd9566d9b932aeaa1163d312fbc4d8)BT\_APPEARANCE\_CYCLING\_POWER

| #define BT\_APPEARANCE\_CYCLING\_POWER   0x0484 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Power Sensor.

## [◆ ](#ga16fb08fa70272252ab6b2d3a5aec485a)BT\_APPEARANCE\_CYCLING\_SPEED

| #define BT\_APPEARANCE\_CYCLING\_SPEED   0x0482 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Speed Sensor.

## [◆ ](#ga48d8f2a285795785f8f51ce220d46371)BT\_APPEARANCE\_CYCLING\_SPEED\_CADENCE

| #define BT\_APPEARANCE\_CYCLING\_SPEED\_CADENCE   0x0485 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Speed and Cadence Sensor.

## [◆ ](#gabbcb0fbbeb6423052db9d5e04410499c)BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_MONITOR

| #define BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_MONITOR   0x0A02 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Monitor.

## [◆ ](#gaa98f5139c99b46515746fb76e9ae7f9b)BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_PROJECTOR

| #define BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_PROJECTOR   0x0A03 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Projector.

## [◆ ](#ga9a6684aa8677575625e049fa0da2c26c)BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_TELEVISION

| #define BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_TELEVISION   0x0A01 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Television.

## [◆ ](#ga32dd73ffa211d632617018aa510b89c4)BT\_APPEARANCE\_FAN\_AXIAL

| #define BT\_APPEARANCE\_FAN\_AXIAL   0x05C2 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Axial Fan.

## [◆ ](#ga8cd83cd08846ac276cc65f31333ee62e)BT\_APPEARANCE\_FAN\_CEILING

| #define BT\_APPEARANCE\_FAN\_CEILING   0x05C1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Ceiling Fan.

## [◆ ](#gaa9e17b8b5e06d2fb365bf152e0cbef5d)BT\_APPEARANCE\_FAN\_DESK

| #define BT\_APPEARANCE\_FAN\_DESK   0x05C5 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Desk Fan.

## [◆ ](#ga1e842c97b90678908f4d18c86c1227c2)BT\_APPEARANCE\_FAN\_EXHAUST

| #define BT\_APPEARANCE\_FAN\_EXHAUST   0x05C3 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Exhaust Fan.

## [◆ ](#ga2e54f8de862435f2dbd7f56b98615c84)BT\_APPEARANCE\_FAN\_PEDESTAL

| #define BT\_APPEARANCE\_FAN\_PEDESTAL   0x05C4 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Pedestal Fan.

## [◆ ](#ga498be79799cb778c9df6629411fe32ad)BT\_APPEARANCE\_FAN\_WALL

| #define BT\_APPEARANCE\_FAN\_WALL   0x05C6 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Wall Fan.

## [◆ ](#gac856a99a5db04dc20229a6e60a18d310)BT\_APPEARANCE\_GENERIC\_ACCESS\_CONTROL

| #define BT\_APPEARANCE\_GENERIC\_ACCESS\_CONTROL   0x0700 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Access Control.

## [◆ ](#gaa13ae6496d47df2be0a0692a28806007)BT\_APPEARANCE\_GENERIC\_AIR\_CONDITIONING

| #define BT\_APPEARANCE\_GENERIC\_AIR\_CONDITIONING   0x0640 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Air Conditioning.

## [◆ ](#ga24c9bcf9646ec5049abf310b31ab355e)BT\_APPEARANCE\_GENERIC\_AIRCRAFT

| #define BT\_APPEARANCE\_GENERIC\_AIRCRAFT   0x0980 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Aircraft.

## [◆ ](#ga32bb0f06096ce5259676a31342b9f0d9)BT\_APPEARANCE\_GENERIC\_AUDIO\_SINK

| #define BT\_APPEARANCE\_GENERIC\_AUDIO\_SINK   0x0840 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Audio Sink.

## [◆ ](#gac85b90f2585044d0efa61191dba3c596)BT\_APPEARANCE\_GENERIC\_AUDIO\_SOURCE

| #define BT\_APPEARANCE\_GENERIC\_AUDIO\_SOURCE   0x0880 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Audio Source.

## [◆ ](#gadb3b07d6c3d3f679b15069fdd8d4e1ee)BT\_APPEARANCE\_GENERIC\_AV\_EQUIPMENT

| #define BT\_APPEARANCE\_GENERIC\_AV\_EQUIPMENT   0x09C0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic AV Equipment.

## [◆ ](#gadca19a01611ca83e18156bb540dd96c1)BT\_APPEARANCE\_GENERIC\_BARCODE\_SCANNER

| #define BT\_APPEARANCE\_GENERIC\_BARCODE\_SCANNER   0x02C0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Barcode Scanner.

## [◆ ](#ga3ab7a9595e00208a9e6a56dca99b56c2)BT\_APPEARANCE\_GENERIC\_BLOOD\_PRESSURE

| #define BT\_APPEARANCE\_GENERIC\_BLOOD\_PRESSURE   0x0380 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Blood Pressure.

## [◆ ](#ga100d26d6b9e9a3af925d64c0b006c6bd)BT\_APPEARANCE\_GENERIC\_CLOCK

| #define BT\_APPEARANCE\_GENERIC\_CLOCK   0x0100 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Clock.

## [◆ ](#ga6b74ad86efc0e9a745f2c9e64079b1cd)BT\_APPEARANCE\_GENERIC\_COMPUTER

| #define BT\_APPEARANCE\_GENERIC\_COMPUTER   0x0080 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Computer.

## [◆ ](#ga5e16df5eefcae8556dfc387135e2b1b6)BT\_APPEARANCE\_GENERIC\_CONTROL\_DEVICE

| #define BT\_APPEARANCE\_GENERIC\_CONTROL\_DEVICE   0x04C0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Control Device.

## [◆ ](#ga7a0463b9b0df37bce80cada38b10ee54)BT\_APPEARANCE\_GENERIC\_CYCLING

| #define BT\_APPEARANCE\_GENERIC\_CYCLING   0x0480 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Cycling.

## [◆ ](#ga0a21cb58861a48875002af38ee82ac08)BT\_APPEARANCE\_GENERIC\_DISPLAY

| #define BT\_APPEARANCE\_GENERIC\_DISPLAY   0x0140 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Display.

## [◆ ](#ga44b70b2f515416baf686b1e127ef4375)BT\_APPEARANCE\_GENERIC\_DISPLAY\_EQUIPMENT

| #define BT\_APPEARANCE\_GENERIC\_DISPLAY\_EQUIPMENT   0x0A00 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Display Equipment.

## [◆ ](#gac08b31ff9b618b19e4c1b43ae2056b5f)BT\_APPEARANCE\_GENERIC\_DOMESTIC\_APPLIANCE

| #define BT\_APPEARANCE\_GENERIC\_DOMESTIC\_APPLIANCE   0x0900 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Domestic Appliance.

## [◆ ](#gab2b5f6385662519a2ece8fb654a6194b)BT\_APPEARANCE\_GENERIC\_EYEGLASSES

| #define BT\_APPEARANCE\_GENERIC\_EYEGLASSES   0x01C0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Eye-glasses.

## [◆ ](#ga82cc89321c4f4ffbf3ef25eff624943c)BT\_APPEARANCE\_GENERIC\_FAN

| #define BT\_APPEARANCE\_GENERIC\_FAN   0x05C0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Fan.

## [◆ ](#gaca727b215a8277d921c0a3bfeccb3f14)BT\_APPEARANCE\_GENERIC\_GAMING

| #define BT\_APPEARANCE\_GENERIC\_GAMING   0x0A80 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Gaming.

## [◆ ](#ga209645f7445873beb50c388cc82aff2a)BT\_APPEARANCE\_GENERIC\_GLUCOSE

| #define BT\_APPEARANCE\_GENERIC\_GLUCOSE   0x0400 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Glucose Meter.

## [◆ ](#gadb5595a41edf5974e03649a675618b7b)BT\_APPEARANCE\_GENERIC\_HEARING\_AID

| #define BT\_APPEARANCE\_GENERIC\_HEARING\_AID   0x0A40 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Hearing aid.

## [◆ ](#gac5bdf195b81215932848151d765e84d6)BT\_APPEARANCE\_GENERIC\_HEART\_RATE

| #define BT\_APPEARANCE\_GENERIC\_HEART\_RATE   0x0340 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Heart Rate Sensor.

## [◆ ](#ga8ea92ea92ca4e2bad4e5e2baba1271dd)BT\_APPEARANCE\_GENERIC\_HEATING

| #define BT\_APPEARANCE\_GENERIC\_HEATING   0x06C0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Heating.

## [◆ ](#gaf2050baedf0863ec37177dd2ef872d39)BT\_APPEARANCE\_GENERIC\_HID

| #define BT\_APPEARANCE\_GENERIC\_HID   0x03C0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Human Interface Device.

## [◆ ](#ga0b552243744bc598467421555e935cd0)BT\_APPEARANCE\_GENERIC\_HUMIDIFIER

| #define BT\_APPEARANCE\_GENERIC\_HUMIDIFIER   0x0680 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Humidifier.

## [◆ ](#gaf1f01946f6acadcaf719d3d7cc06e55f)BT\_APPEARANCE\_GENERIC\_HVAC

| #define BT\_APPEARANCE\_GENERIC\_HVAC   0x0600 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic HVAC.

## [◆ ](#ga481169a27fab19628f81a68af31d543c)BT\_APPEARANCE\_GENERIC\_INSULIN\_PUMP

| #define BT\_APPEARANCE\_GENERIC\_INSULIN\_PUMP   0x0D40 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Insulin Pump.

## [◆ ](#gaf73b11c4dbf366a854b4c68e802e3c1c)BT\_APPEARANCE\_GENERIC\_KEYRING

| #define BT\_APPEARANCE\_GENERIC\_KEYRING   0x0240 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Keyring.

## [◆ ](#gae01be867f730c06b59fcb03289ae66d7)BT\_APPEARANCE\_GENERIC\_LIGHT\_FIXTURES

| #define BT\_APPEARANCE\_GENERIC\_LIGHT\_FIXTURES   0x0580 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Light Fixtures.

## [◆ ](#gacb3340c5193588eea2d42fe1bef443d0)BT\_APPEARANCE\_GENERIC\_LIGHT\_SOURCE

| #define BT\_APPEARANCE\_GENERIC\_LIGHT\_SOURCE   0x07C0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Light Source.

## [◆ ](#ga17e94209c0c96b5ca039b1613de0d05e)BT\_APPEARANCE\_GENERIC\_MEDIA\_PLAYER

| #define BT\_APPEARANCE\_GENERIC\_MEDIA\_PLAYER   0x0280 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Media Player.

## [◆ ](#ga08453eebe2ae8f53deddaa64a029c2b5)BT\_APPEARANCE\_GENERIC\_MEDICATION\_DELIVERY

| #define BT\_APPEARANCE\_GENERIC\_MEDICATION\_DELIVERY   0x0D80 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Medication Delivery.

## [◆ ](#ga414b202e93d1db533853093d66603720)BT\_APPEARANCE\_GENERIC\_MOTORIZED\_DEVICE

| #define BT\_APPEARANCE\_GENERIC\_MOTORIZED\_DEVICE   0x0740 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Motorized Device.

## [◆ ](#ga49328394fd7505da9476d4d62ae60c03)BT\_APPEARANCE\_GENERIC\_MOTORIZED\_VEHICLE

| #define BT\_APPEARANCE\_GENERIC\_MOTORIZED\_VEHICLE   0x08C0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Motorized Vehicle.

## [◆ ](#gac4727ec720344ece687256ac517800e7)BT\_APPEARANCE\_GENERIC\_NETWORK\_DEVICE

| #define BT\_APPEARANCE\_GENERIC\_NETWORK\_DEVICE   0x0500 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Network Device.

## [◆ ](#ga0d39ca2892bd96013b8c82111eecc1cb)BT\_APPEARANCE\_GENERIC\_OUTDOOR\_SPORTS

| #define BT\_APPEARANCE\_GENERIC\_OUTDOOR\_SPORTS   0x1440 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Outdoor Sports Activity.

## [◆ ](#ga7387d717c77b38374e981991278aeb1c)BT\_APPEARANCE\_GENERIC\_PERSONAL\_MOBILITY\_DEVICE

| #define BT\_APPEARANCE\_GENERIC\_PERSONAL\_MOBILITY\_DEVICE   0x0CC0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Personal Mobility Device.

## [◆ ](#gae7061e78f960563af6e1b3dea71655a9)BT\_APPEARANCE\_GENERIC\_PHONE

| #define BT\_APPEARANCE\_GENERIC\_PHONE   0x0040 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Phone.

## [◆ ](#gadae82e45d9aafd34cafd3f0e793b1b24)BT\_APPEARANCE\_GENERIC\_POWER\_DEVICE

| #define BT\_APPEARANCE\_GENERIC\_POWER\_DEVICE   0x0780 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Power Device.

## [◆ ](#ga93ee753bf3b8819239041c065eaf024f)BT\_APPEARANCE\_GENERIC\_PULSE\_OXIMETER

| #define BT\_APPEARANCE\_GENERIC\_PULSE\_OXIMETER   0x0C40 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Pulse Oximeter.

## [◆ ](#ga0b47897768b27d26b8687dd2ab28703b)BT\_APPEARANCE\_GENERIC\_REMOTE

| #define BT\_APPEARANCE\_GENERIC\_REMOTE   0x0180 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Remote Control.

## [◆ ](#gab3241fe012482e716c3f18e2962ca15d)BT\_APPEARANCE\_GENERIC\_SENSOR

| #define BT\_APPEARANCE\_GENERIC\_SENSOR   0x0540 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Sensor.

## [◆ ](#gabc243c7449804749704c1862db286eab)BT\_APPEARANCE\_GENERIC\_SIGNAGE

| #define BT\_APPEARANCE\_GENERIC\_SIGNAGE   0x0AC0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Signage.

## [◆ ](#ga1332c44cc3371fa9006993d03ba4ae12)BT\_APPEARANCE\_GENERIC\_SPIROMETER

| #define BT\_APPEARANCE\_GENERIC\_SPIROMETER   0x0DC0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Spirometer.

## [◆ ](#gaca6d810977e6da1a3174ee2b6b36662d)BT\_APPEARANCE\_GENERIC\_TAG

| #define BT\_APPEARANCE\_GENERIC\_TAG   0x0200 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Tag.

## [◆ ](#ga2e0fde88d83e1f4533d69c8dc472255f)BT\_APPEARANCE\_GENERIC\_THERMOMETER

| #define BT\_APPEARANCE\_GENERIC\_THERMOMETER   0x0300 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Thermometer.

## [◆ ](#ga9cf19d97db0c4c5b8473b72809b51d42)BT\_APPEARANCE\_GENERIC\_WALKING

| #define BT\_APPEARANCE\_GENERIC\_WALKING   0x0440 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Running Walking Sensor.

## [◆ ](#ga0c512fd6aa5d35e78f02176073f5f121)BT\_APPEARANCE\_GENERIC\_WATCH

| #define BT\_APPEARANCE\_GENERIC\_WATCH   0x00C0 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Watch.

## [◆ ](#gabad761094a16873dcebbc6238825d84b)BT\_APPEARANCE\_GENERIC\_WEARABLE\_AUDIO\_DEVICE

| #define BT\_APPEARANCE\_GENERIC\_WEARABLE\_AUDIO\_DEVICE   0x0940 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Wearable Audio Device.

## [◆ ](#ga1aec23cd4f531a57260c7c8faf9caf40)BT\_APPEARANCE\_GENERIC\_WEIGHT\_SCALE

| #define BT\_APPEARANCE\_GENERIC\_WEIGHT\_SCALE   0x0C80 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Weight Scale.

## [◆ ](#ga1e70d961fca2719243c866464132684c)BT\_APPEARANCE\_GENERIC\_WINDOW\_COVERING

| #define BT\_APPEARANCE\_GENERIC\_WINDOW\_COVERING   0x0800 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Window Covering.

## [◆ ](#ga1fa6231e14dcfa90a5518e61f0e4e302)BT\_APPEARANCE\_HEARING\_AID\_BEHIND\_EAR

| #define BT\_APPEARANCE\_HEARING\_AID\_BEHIND\_EAR   0x0A42 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Behind-ear hearing aid.

## [◆ ](#ga82ba79bd9fd04a3fbdb6d8b4e35e3877)BT\_APPEARANCE\_HEARING\_AID\_COCHLEAR\_IMPLANT

| #define BT\_APPEARANCE\_HEARING\_AID\_COCHLEAR\_IMPLANT   0x0A43 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Cochlear Implant.

## [◆ ](#ga28cc6555937d9d5a9e8ae0079fc8a534)BT\_APPEARANCE\_HEARING\_AID\_IN\_EAR

| #define BT\_APPEARANCE\_HEARING\_AID\_IN\_EAR   0x0A41 |
| --- |

`#include <[gap.h](gap_8h.md)>`

In-ear hearing aid.

## [◆ ](#ga895f6570a09f3eee8d821eca57cdeb03)BT\_APPEARANCE\_HEART\_RATE\_BELT

| #define BT\_APPEARANCE\_HEART\_RATE\_BELT   0x0341 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Heart Rate Belt.

## [◆ ](#gac74bc8e109f5d9b4c0988ee6378ed471)BT\_APPEARANCE\_HEATING\_AIR\_CURTAIN

| #define BT\_APPEARANCE\_HEATING\_AIR\_CURTAIN   0x06C7 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Air Curtain.

## [◆ ](#gac1abc9ae0b8ede2197720ea9e67b692e)BT\_APPEARANCE\_HEATING\_BOILER

| #define BT\_APPEARANCE\_HEATING\_BOILER   0x06C2 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Boiler.

## [◆ ](#ga995ca18db114ea062df0d76c9e241937)BT\_APPEARANCE\_HEATING\_FAN\_HEATER

| #define BT\_APPEARANCE\_HEATING\_FAN\_HEATER   0x06C6 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Fan Heater.

## [◆ ](#ga99537968fdc7e680d922ca309fba7678)BT\_APPEARANCE\_HEATING\_HEAT\_PUMP

| #define BT\_APPEARANCE\_HEATING\_HEAT\_PUMP   0x06C3 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Heat Pump.

## [◆ ](#ga8e40496a351c7ec5ea836805925f1e13)BT\_APPEARANCE\_HEATING\_INFRARED\_HEATER

| #define BT\_APPEARANCE\_HEATING\_INFRARED\_HEATER   0x06C4 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Infrared Heater.

## [◆ ](#ga46fe051c7e50492dba5ae824e154cf69)BT\_APPEARANCE\_HEATING\_RADIANT\_PANEL\_HEATER

| #define BT\_APPEARANCE\_HEATING\_RADIANT\_PANEL\_HEATER   0x06C5 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Radiant Panel Heater.

## [◆ ](#ga05b0b91c74aed5bc73a92f336bdae33a)BT\_APPEARANCE\_HEATING\_RADIATOR

| #define BT\_APPEARANCE\_HEATING\_RADIATOR   0x06C1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Radiator.

## [◆ ](#gaf88f83afd454fe88dd7146e10ef6d35e)BT\_APPEARANCE\_HID\_BARCODE\_SCANNER

| #define BT\_APPEARANCE\_HID\_BARCODE\_SCANNER   0x03C8 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Barcode Scanner.

## [◆ ](#gaa03c3b4d7ea8211748316146afab8bd4)BT\_APPEARANCE\_HID\_CARD\_READER

| #define BT\_APPEARANCE\_HID\_CARD\_READER   0x03C6 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Card Reader.

## [◆ ](#ga002a1d7965b23ec62c8a196f4e5452d9)BT\_APPEARANCE\_HID\_DIGITAL\_PEN

| #define BT\_APPEARANCE\_HID\_DIGITAL\_PEN   0x03C7 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Digital Pen.

## [◆ ](#gacac11dcb96ab60963a1118e171a731de)BT\_APPEARANCE\_HID\_DIGITIZER\_TABLET

| #define BT\_APPEARANCE\_HID\_DIGITIZER\_TABLET   0x03C5 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Digitizer Tablet.

## [◆ ](#ga770336524e74d106cb18354f9dbfad76)BT\_APPEARANCE\_HID\_GAMEPAD

| #define BT\_APPEARANCE\_HID\_GAMEPAD   0x03C4 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Gamepad.

## [◆ ](#ga2f9f15df2260a1307f5142f37437bf0c)BT\_APPEARANCE\_HID\_JOYSTICK

| #define BT\_APPEARANCE\_HID\_JOYSTICK   0x03C3 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Joystick.

## [◆ ](#gaa74af272423a80d5489ed8cf6c3ee66c)BT\_APPEARANCE\_HID\_KEYBOARD

| #define BT\_APPEARANCE\_HID\_KEYBOARD   0x03C1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Keyboard.

## [◆ ](#ga3b6ba8ffe424db08583186c448e37149)BT\_APPEARANCE\_HID\_MOUSE

| #define BT\_APPEARANCE\_HID\_MOUSE   0x03C2 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Mouse.

## [◆ ](#gae415dd9e8d620dfd1981719f4ed2d796)BT\_APPEARANCE\_HID\_PRESENTATION\_REMOTE

| #define BT\_APPEARANCE\_HID\_PRESENTATION\_REMOTE   0x03CA |
| --- |

`#include <[gap.h](gap_8h.md)>`

Presentation Remote.

## [◆ ](#gaee207f9434bce7d0f7e096bf3b37a01c)BT\_APPEARANCE\_HID\_TOUCHPAD

| #define BT\_APPEARANCE\_HID\_TOUCHPAD   0x03C9 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Touchpad.

## [◆ ](#ga8fbaf0fced0cce12e08c4a516351b166)BT\_APPEARANCE\_HOME\_VIDEO\_GAME\_CONSOLE

| #define BT\_APPEARANCE\_HOME\_VIDEO\_GAME\_CONSOLE   0x0A81 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Home Video Game Console.

## [◆ ](#ga182ade4b2c8f4705ba132248e504bb95)BT\_APPEARANCE\_HVAC\_AIR\_CURTAIN

| #define BT\_APPEARANCE\_HVAC\_AIR\_CURTAIN   0x060B |
| --- |

`#include <[gap.h](gap_8h.md)>`

Air Curtain.

## [◆ ](#gacc28a1bc1a809c574019455de4ac9d0b)BT\_APPEARANCE\_HVAC\_BOILER

| #define BT\_APPEARANCE\_HVAC\_BOILER   0x0606 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Boiler.

## [◆ ](#gaa3b96e44638048b8891a2dece29f4b3f)BT\_APPEARANCE\_HVAC\_DEHUMIDIFIER

| #define BT\_APPEARANCE\_HVAC\_DEHUMIDIFIER   0x0603 |
| --- |

`#include <[gap.h](gap_8h.md)>`

De-humidifier.

## [◆ ](#ga2a044c3369ed48d216707f6e6a541a23)BT\_APPEARANCE\_HVAC\_FAN\_HEATER

| #define BT\_APPEARANCE\_HVAC\_FAN\_HEATER   0x060A |
| --- |

`#include <[gap.h](gap_8h.md)>`

Fan Heater.

## [◆ ](#gaead4ebeabb8855111ab9080aca4e035a)BT\_APPEARANCE\_HVAC\_HEAT\_PUMP

| #define BT\_APPEARANCE\_HVAC\_HEAT\_PUMP   0x0607 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Heat Pump.

## [◆ ](#gacef9145f435d10cbf5a775b9a2c9b756)BT\_APPEARANCE\_HVAC\_HEATER

| #define BT\_APPEARANCE\_HVAC\_HEATER   0x0604 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Heater.

## [◆ ](#gaf55f3f3f07cc78509e7fe19cea6cea4e)BT\_APPEARANCE\_HVAC\_HUMIDIFIER

| #define BT\_APPEARANCE\_HVAC\_HUMIDIFIER   0x0602 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Humidifier.

## [◆ ](#ga50c5df52d8471fc8e1dc65e31079566d)BT\_APPEARANCE\_HVAC\_INFRARED\_HEATER

| #define BT\_APPEARANCE\_HVAC\_INFRARED\_HEATER   0x0608 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Infrared Heater.

## [◆ ](#gad43d27ff96a7fba1ed7d5e20ebd472d9)BT\_APPEARANCE\_HVAC\_RADIANT\_PANEL\_HEATER

| #define BT\_APPEARANCE\_HVAC\_RADIANT\_PANEL\_HEATER   0x0609 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Radiant Panel Heater.

## [◆ ](#gad90f108f3d33d68e27ac545cdb520f18)BT\_APPEARANCE\_HVAC\_RADIATOR

| #define BT\_APPEARANCE\_HVAC\_RADIATOR   0x0605 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Radiator.

## [◆ ](#ga33055b50c10bfc713b18823fca525488)BT\_APPEARANCE\_HVAC\_THERMOSTAT

| #define BT\_APPEARANCE\_HVAC\_THERMOSTAT   0x0601 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Thermostat.

## [◆ ](#ga1562514d0182e8862edad570b7a346e6)BT\_APPEARANCE\_INSULIN\_PEN

| #define BT\_APPEARANCE\_INSULIN\_PEN   0x0D48 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Insulin Pen.

## [◆ ](#ga63512439364307259010bededf7bfd8b)BT\_APPEARANCE\_INSULIN\_PUMP\_DURABLE

| #define BT\_APPEARANCE\_INSULIN\_PUMP\_DURABLE   0x0D41 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Insulin Pump, durable pump.

## [◆ ](#ga0979695247b96321e5a8b6869d09227a)BT\_APPEARANCE\_INSULIN\_PUMP\_PATCH

| #define BT\_APPEARANCE\_INSULIN\_PUMP\_PATCH   0x0D44 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Insulin Pump, patch pump.

## [◆ ](#ga8f98c2d32664a6e03ebc2a43ae1eb52a)BT\_APPEARANCE\_LIGHT\_FIXTURES\_BAY

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_BAY   0x0593 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Bay Light.

## [◆ ](#ga20a7b241f292475d70626a38d983886c)BT\_APPEARANCE\_LIGHT\_FIXTURES\_BOLLARD\_WITH

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_BOLLARD\_WITH   0x058B |
| --- |

`#include <[gap.h](gap_8h.md)>`

Bollard with Light.

## [◆ ](#ga8325830f2c977dc238a9ca1b9837803e)BT\_APPEARANCE\_LIGHT\_FIXTURES\_BULB

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_BULB   0x0597 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Bulb.

## [◆ ](#gadc48840b6590a89593a5d17fbdb1e9e9)BT\_APPEARANCE\_LIGHT\_FIXTURES\_CABINET

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_CABINET   0x0584 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Cabinet Light.

## [◆ ](#ga2d77fb5f5ed9a43771186ecc5693da8f)BT\_APPEARANCE\_LIGHT\_FIXTURES\_CEILING

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_CEILING   0x0582 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Ceiling Light.

## [◆ ](#ga35a90a4e3bfef7b0cfec0d5fa7b36c4a)BT\_APPEARANCE\_LIGHT\_FIXTURES\_CONTROLLER

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_CONTROLLER   0x0595 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Light Controller.

## [◆ ](#ga2f37bf95ea6057b999bbf2cf94016e5d)BT\_APPEARANCE\_LIGHT\_FIXTURES\_DESK

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_DESK   0x0585 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Desk Light.

## [◆ ](#gac2b6de99b4e87f7c40063ba844c75ead)BT\_APPEARANCE\_LIGHT\_FIXTURES\_DRIVER

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_DRIVER   0x0596 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Light Driver.

## [◆ ](#ga3f687f994ffff2ce70b81a992195d210)BT\_APPEARANCE\_LIGHT\_FIXTURES\_EMERGENCY\_EXIT

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_EMERGENCY\_EXIT   0x0594 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Emergency Exit Light.

## [◆ ](#gab41f8b6f1ff0f624bb6666ef2ac6dab3)BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOD

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOD   0x0589 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Flood Light.

## [◆ ](#ga57bb461b0ddd045d21d7fbd3843fbabb)BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOR

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOR   0x0583 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Floor Light.

## [◆ ](#ga348e64ffe0f3d6301dd8c911f70ead68)BT\_APPEARANCE\_LIGHT\_FIXTURES\_GARDEN

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_GARDEN   0x058D |
| --- |

`#include <[gap.h](gap_8h.md)>`

Garden Light.

## [◆ ](#ga738e87008c6a64450bb7ec22dbcdd113)BT\_APPEARANCE\_LIGHT\_FIXTURES\_HIGH\_BAY

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_HIGH\_BAY   0x0599 |
| --- |

`#include <[gap.h](gap_8h.md)>`

High-bay Light.

## [◆ ](#ga583b7432ba6ac4cc078d3a069e3a54e1)BT\_APPEARANCE\_LIGHT\_FIXTURES\_IN\_GROUND

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_IN\_GROUND   0x0588 |
| --- |

`#include <[gap.h](gap_8h.md)>`

In-ground Light.

## [◆ ](#ga5388daf123e629d6f7a0b9af13fbc366)BT\_APPEARANCE\_LIGHT\_FIXTURES\_LINEAR

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_LINEAR   0x0590 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Linear Light.

## [◆ ](#gafc924bbc1b6aff0130c2be3d5fe59e33)BT\_APPEARANCE\_LIGHT\_FIXTURES\_LOW\_BAY

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_LOW\_BAY   0x0598 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Low-bay Light.

## [◆ ](#ga7c5811bd50d9f78e67e3e56faa432aae)BT\_APPEARANCE\_LIGHT\_FIXTURES\_PATHWAY

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_PATHWAY   0x058C |
| --- |

`#include <[gap.h](gap_8h.md)>`

Pathway Light.

## [◆ ](#ga336147b54406237e25d8cf9ed152928b)BT\_APPEARANCE\_LIGHT\_FIXTURES\_PENDANT

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_PENDANT   0x0587 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Pendant Light.

## [◆ ](#ga0da0cbeebd2b20bf28dfc06def016068)BT\_APPEARANCE\_LIGHT\_FIXTURES\_POLE\_TOP

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_POLE\_TOP   0x058E |
| --- |

`#include <[gap.h](gap_8h.md)>`

Pole-top Light.

## [◆ ](#ga1bf2889f7a8a7ae363bc1d4355ee8d65)BT\_APPEARANCE\_LIGHT\_FIXTURES\_SHELVES

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_SHELVES   0x0592 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Shelves Light.

## [◆ ](#gac938fb03553d2d3c27b50af2a9a1ac48)BT\_APPEARANCE\_LIGHT\_FIXTURES\_STREET

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_STREET   0x0591 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Street Light.

## [◆ ](#gaa57b538ecad380ad77354e0cd9576e5b)BT\_APPEARANCE\_LIGHT\_FIXTURES\_TROFFER

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_TROFFER   0x0586 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Troffer Light.

## [◆ ](#ga83f50305a23250e5e2cef5004762e122)BT\_APPEARANCE\_LIGHT\_FIXTURES\_UNDERWATER

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_UNDERWATER   0x058A |
| --- |

`#include <[gap.h](gap_8h.md)>`

Underwater Light.

## [◆ ](#gae1b2b535754f9cdc24c4a6cee63ef5cb)BT\_APPEARANCE\_LIGHT\_FIXTURES\_WALL

| #define BT\_APPEARANCE\_LIGHT\_FIXTURES\_WALL   0x0581 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Wall Light.

## [◆ ](#ga39957a77aa54255ab3a06441e422e7e3)BT\_APPEARANCE\_LIGHT\_SOURCE\_FLUORESCENT\_LAMP

| #define BT\_APPEARANCE\_LIGHT\_SOURCE\_FLUORESCENT\_LAMP   0x07C4 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Fluorescent Lamp.

## [◆ ](#ga1babd2989112bafb5819235fe5b6c556)BT\_APPEARANCE\_LIGHT\_SOURCE\_HID\_LAMP

| #define BT\_APPEARANCE\_LIGHT\_SOURCE\_HID\_LAMP   0x07C3 |
| --- |

`#include <[gap.h](gap_8h.md)>`

HID Lamp.

## [◆ ](#gafed8531ffde21d0ad6e8d477d64496f0)BT\_APPEARANCE\_LIGHT\_SOURCE\_INCANDESCENT\_BULB

| #define BT\_APPEARANCE\_LIGHT\_SOURCE\_INCANDESCENT\_BULB   0x07C1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Incandescent Light Bulb.

## [◆ ](#ga242d324cf5cf33e4edd5cf33e8c3c89b)BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_ARRAY

| #define BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_ARRAY   0x07C5 |
| --- |

`#include <[gap.h](gap_8h.md)>`

LED Array.

## [◆ ](#ga66bf91b8a25ac88a0fd6ab9456201de1)BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_LAMP

| #define BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_LAMP   0x07C2 |
| --- |

`#include <[gap.h](gap_8h.md)>`

LED Lamp.

## [◆ ](#gaf47bce54f4ae1915cd64c3c2d254e353)BT\_APPEARANCE\_LIGHT\_SOURCE\_LOW\_VOLTAGE\_HALOGEN

| #define BT\_APPEARANCE\_LIGHT\_SOURCE\_LOW\_VOLTAGE\_HALOGEN   0x07C7 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Low voltage halogen.

## [◆ ](#ga8449006920ed1fdd562c702ee2e16a21)BT\_APPEARANCE\_LIGHT\_SOURCE\_MULTICOLOR\_LED\_ARRAY

| #define BT\_APPEARANCE\_LIGHT\_SOURCE\_MULTICOLOR\_LED\_ARRAY   0x07C6 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Multi-Color LED Array.

## [◆ ](#gaed4400a94dae4f536a456cc55eb6f6d5)BT\_APPEARANCE\_LIGHT\_SOURCE\_OLED

| #define BT\_APPEARANCE\_LIGHT\_SOURCE\_OLED   0x07C8 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Organic light emitting diode.

## [◆ ](#ga7966ec64cafe708fe94a7c323fbe3713)BT\_APPEARANCE\_MOBILITY\_POWERED\_WHEELCHAIR

| #define BT\_APPEARANCE\_MOBILITY\_POWERED\_WHEELCHAIR   0x0CC1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Powered Wheelchair.

## [◆ ](#ga21f21a73f355ffaa408376ca4fc802a8)BT\_APPEARANCE\_MOBILITY\_SCOOTER

| #define BT\_APPEARANCE\_MOBILITY\_SCOOTER   0x0CC2 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Mobility Scooter.

## [◆ ](#ga338de5523abf3fd81e913f3cdb4a31b6)BT\_APPEARANCE\_MOTORIZED\_AWNING

| #define BT\_APPEARANCE\_MOTORIZED\_AWNING   0x0742 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Awning.

## [◆ ](#gaaa39c48ed2d6edd5650743b82154462b)BT\_APPEARANCE\_MOTORIZED\_BLINDS\_OR\_SHADES

| #define BT\_APPEARANCE\_MOTORIZED\_BLINDS\_OR\_SHADES   0x0743 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Blinds or Shades.

## [◆ ](#ga53f6a4df5ccc2117525952be2e174ddc)BT\_APPEARANCE\_MOTORIZED\_CURTAINS

| #define BT\_APPEARANCE\_MOTORIZED\_CURTAINS   0x0744 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Curtains.

## [◆ ](#ga376ef909868a5c273b71d1c372755707)BT\_APPEARANCE\_MOTORIZED\_GATE

| #define BT\_APPEARANCE\_MOTORIZED\_GATE   0x0741 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Motorized Gate.

## [◆ ](#ga5f32cab5c7a155fffbe0c33cadfef31a)BT\_APPEARANCE\_MOTORIZED\_SCREEN

| #define BT\_APPEARANCE\_MOTORIZED\_SCREEN   0x0745 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Screen.

## [◆ ](#ga90237753920702380321e9f858344741)BT\_APPEARANCE\_MULTISENSOR

| #define BT\_APPEARANCE\_MULTISENSOR   0x0556 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Multisensor.

## [◆ ](#ga265ba959769d56f42ff621a20e193aba)BT\_APPEARANCE\_NETWORK\_ACCESS\_POINT

| #define BT\_APPEARANCE\_NETWORK\_ACCESS\_POINT   0x0501 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Access Point.

## [◆ ](#gadcc3d795579a731ae03ade14d5193408)BT\_APPEARANCE\_NETWORK\_MESH\_DEVICE

| #define BT\_APPEARANCE\_NETWORK\_MESH\_DEVICE   0x0502 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Mesh Device.

## [◆ ](#gad4c5f5840a8caba73d55b0138e506bd0)BT\_APPEARANCE\_NETWORK\_MESH\_PROXY

| #define BT\_APPEARANCE\_NETWORK\_MESH\_PROXY   0x0503 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Mesh Network Proxy.

## [◆ ](#ga30c97d6f5bff1a4a67e4f59eb4d49d2d)BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION

| #define BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION   0x1441 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Location Display.

## [◆ ](#ga52b6c51c9afcbbba12d9d3cae824f4a7)BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_AND\_NAV

| #define BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_AND\_NAV   0x1442 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Location and Navigation Display.

## [◆ ](#gadf053353789183d1b1c3ca13ad98559f)BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD

| #define BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD   0x1443 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Location Pod.

## [◆ ](#ga8fbc7782099e724febb712ee108e8cba)BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD\_AND\_NAV

| #define BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD\_AND\_NAV   0x1444 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Location and Navigation Pod.

## [◆ ](#ga39ad633d1795af4546bd930d0e799447)BT\_APPEARANCE\_PORTABLE\_HANDHELD\_CONSOLE

| #define BT\_APPEARANCE\_PORTABLE\_HANDHELD\_CONSOLE   0x0A82 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Portable handheld console.

## [◆ ](#ga5d6b28b9660d2357e2af2bf0ceab9c18)BT\_APPEARANCE\_POWER\_CHARGE\_CASE

| #define BT\_APPEARANCE\_POWER\_CHARGE\_CASE   0x0788 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Charge Case.

## [◆ ](#ga7de26016aa039e3e72ddd61653e1c1d8)BT\_APPEARANCE\_POWER\_FLUORESCENT\_LAMP\_GEAR

| #define BT\_APPEARANCE\_POWER\_FLUORESCENT\_LAMP\_GEAR   0x0786 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Fluorescent Lamp Gear.

## [◆ ](#ga6396b1d813c9764bdfe92c4f2ba961b1)BT\_APPEARANCE\_POWER\_HID\_LAMP\_GEAR

| #define BT\_APPEARANCE\_POWER\_HID\_LAMP\_GEAR   0x0787 |
| --- |

`#include <[gap.h](gap_8h.md)>`

HID Lamp Gear.

## [◆ ](#ga31842298741c822dcebba942453975c6)BT\_APPEARANCE\_POWER\_LED\_DRIVER

| #define BT\_APPEARANCE\_POWER\_LED\_DRIVER   0x0785 |
| --- |

`#include <[gap.h](gap_8h.md)>`

LED Driver.

## [◆ ](#gad9efd19e2c95525a3972c8b0f0417449)BT\_APPEARANCE\_POWER\_OUTLET

| #define BT\_APPEARANCE\_POWER\_OUTLET   0x0781 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Power Outlet.

## [◆ ](#ga0d9aadc19f5f5f484769b225164866e4)BT\_APPEARANCE\_POWER\_PLUG

| #define BT\_APPEARANCE\_POWER\_PLUG   0x0783 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Plug.

## [◆ ](#gab6a5ac3941a5707f052126810a7f22e0)BT\_APPEARANCE\_POWER\_POWER\_BANK

| #define BT\_APPEARANCE\_POWER\_POWER\_BANK   0x0789 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Power Bank.

## [◆ ](#ga2c5bd38d4eeb1aad2d29b004390a6d18)BT\_APPEARANCE\_POWER\_STRIP

| #define BT\_APPEARANCE\_POWER\_STRIP   0x0782 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Power Strip.

## [◆ ](#ga07acce808c9cf2b5e84aacd65e8f256d)BT\_APPEARANCE\_POWER\_SUPPLY

| #define BT\_APPEARANCE\_POWER\_SUPPLY   0x0784 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Power Supply.

## [◆ ](#ga8a298130c73299b6079dae3065954c0c)BT\_APPEARANCE\_PULSE\_OXIMETER\_FINGERTIP

| #define BT\_APPEARANCE\_PULSE\_OXIMETER\_FINGERTIP   0x0C41 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Fingertip Pulse Oximeter.

## [◆ ](#gaebcadd5c37e6d87903e2cb97e03aeb7d)BT\_APPEARANCE\_PULSE\_OXIMETER\_WRIST

| #define BT\_APPEARANCE\_PULSE\_OXIMETER\_WRIST   0x0C42 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Wrist Worn Pulse Oximeter.

## [◆ ](#gaacb0779499ad4aaa83f0b6303460caf8)BT\_APPEARANCE\_SENSOR\_AIR\_QUALITY

| #define BT\_APPEARANCE\_SENSOR\_AIR\_QUALITY   0x0542 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Air quality Sensor.

## [◆ ](#ga622508f9b051ed0320700b01967f6446)BT\_APPEARANCE\_SENSOR\_AMBIENT\_LIGHT

| #define BT\_APPEARANCE\_SENSOR\_AMBIENT\_LIGHT   0x054B |
| --- |

`#include <[gap.h](gap_8h.md)>`

Ambient Light Sensor.

## [◆ ](#ga34ed8c9aefe34d5030209f073c9ecd24)BT\_APPEARANCE\_SENSOR\_CARBON\_DIOXIDE

| #define BT\_APPEARANCE\_SENSOR\_CARBON\_DIOXIDE   0x054A |
| --- |

`#include <[gap.h](gap_8h.md)>`

Carbon Dioxide Sensor.

## [◆ ](#ga0e60b365f871c17c0015ffcf8bc1646e)BT\_APPEARANCE\_SENSOR\_CARBON\_MONOXIDE

| #define BT\_APPEARANCE\_SENSOR\_CARBON\_MONOXIDE   0x0549 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Carbon Monoxide Sensor.

## [◆ ](#gadfb6808db5a7060316b724c24c8ceaf8)BT\_APPEARANCE\_SENSOR\_CEILING\_MOUNTED

| #define BT\_APPEARANCE\_SENSOR\_CEILING\_MOUNTED   0x0554 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Ceiling Mounted Sensor.

## [◆ ](#ga8106142ddb6445e7462137e032e50854)BT\_APPEARANCE\_SENSOR\_COLOR\_LIGHT

| #define BT\_APPEARANCE\_SENSOR\_COLOR\_LIGHT   0x054D |
| --- |

`#include <[gap.h](gap_8h.md)>`

Color Light Sensor.

## [◆ ](#gac71e281cf1b8d1b6535623ec34c7d63f)BT\_APPEARANCE\_SENSOR\_CONTACT

| #define BT\_APPEARANCE\_SENSOR\_CONTACT   0x0548 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Contact Sensor.

## [◆ ](#gaca0cfcd560fa4133c0bc62a61d2874c7)BT\_APPEARANCE\_SENSOR\_ENERGY

| #define BT\_APPEARANCE\_SENSOR\_ENERGY   0x054C |
| --- |

`#include <[gap.h](gap_8h.md)>`

Energy Sensor.

## [◆ ](#ga7238d3a45f9e62f0189db9d7eeac4d15)BT\_APPEARANCE\_SENSOR\_ENERGY\_METER

| #define BT\_APPEARANCE\_SENSOR\_ENERGY\_METER   0x0557 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Energy Meter.

## [◆ ](#ga425115e6c251a9c493c98d79f659077d)BT\_APPEARANCE\_SENSOR\_FIRE

| #define BT\_APPEARANCE\_SENSOR\_FIRE   0x054F |
| --- |

`#include <[gap.h](gap_8h.md)>`

Fire Sensor.

## [◆ ](#gaae8f95ef639cb7d5e97063eed710a07d)BT\_APPEARANCE\_SENSOR\_FLAME\_DETECTOR

| #define BT\_APPEARANCE\_SENSOR\_FLAME\_DETECTOR   0x0558 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Flame Detector.

## [◆ ](#gaf9a9c0191ec175d14061058cf3da163c)BT\_APPEARANCE\_SENSOR\_FLUSH\_MOUNTED

| #define BT\_APPEARANCE\_SENSOR\_FLUSH\_MOUNTED   0x0553 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Flush Mounted Sensor.

## [◆ ](#ga2deff206602e1e0784af9456ef8abd5b)BT\_APPEARANCE\_SENSOR\_HUMIDITY

| #define BT\_APPEARANCE\_SENSOR\_HUMIDITY   0x0544 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Humidity Sensor.

## [◆ ](#ga2cbac5e931080f1f5cb3c9bb4c73e9d8)BT\_APPEARANCE\_SENSOR\_LEAK

| #define BT\_APPEARANCE\_SENSOR\_LEAK   0x0545 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Leak Sensor.

## [◆ ](#gab49b84183136e9b65ba2e1f5490a79ed)BT\_APPEARANCE\_SENSOR\_MOTION

| #define BT\_APPEARANCE\_SENSOR\_MOTION   0x0541 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Motion Sensor.

## [◆ ](#gaeec9666dbdb31e9302a25aaa536f3180)BT\_APPEARANCE\_SENSOR\_MULTI

| #define BT\_APPEARANCE\_SENSOR\_MULTI   0x0552 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Multi-Sensor.

## [◆ ](#ga8e8b7834c82c42a0076300aca20c2d35)BT\_APPEARANCE\_SENSOR\_OCCUPANCY

| #define BT\_APPEARANCE\_SENSOR\_OCCUPANCY   0x0547 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Occupancy Sensor.

## [◆ ](#ga6d3447e24d5d75051b81998fd9ad8bfe)BT\_APPEARANCE\_SENSOR\_PROXIMITY

| #define BT\_APPEARANCE\_SENSOR\_PROXIMITY   0x0551 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Proximity Sensor.

## [◆ ](#ga380da83e3a69de3fd5091cdc89f7fcbc)BT\_APPEARANCE\_SENSOR\_RAIN

| #define BT\_APPEARANCE\_SENSOR\_RAIN   0x054E |
| --- |

`#include <[gap.h](gap_8h.md)>`

Rain Sensor.

## [◆ ](#gaeedc0612f8ca171aec061cf02ee907e4)BT\_APPEARANCE\_SENSOR\_SMOKE

| #define BT\_APPEARANCE\_SENSOR\_SMOKE   0x0546 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Smoke Sensor.

## [◆ ](#ga5e072a902bf145dc2b00dbd1c8a64b52)BT\_APPEARANCE\_SENSOR\_TEMPERATURE

| #define BT\_APPEARANCE\_SENSOR\_TEMPERATURE   0x0543 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Temperature Sensor.

## [◆ ](#ga4d0877a3cd9b7efebbaa5fd8a988a2a3)BT\_APPEARANCE\_SENSOR\_VEHICLE\_TIRE\_PRESSURE

| #define BT\_APPEARANCE\_SENSOR\_VEHICLE\_TIRE\_PRESSURE   0x0559 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Vehicle Tire Pressure Sensor.

## [◆ ](#gae564900f0517d393ceffcca8d27f6e45)BT\_APPEARANCE\_SENSOR\_WALL\_MOUNTED

| #define BT\_APPEARANCE\_SENSOR\_WALL\_MOUNTED   0x0555 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Wall Mounted Sensor.

## [◆ ](#gaa710c0666d8b5bf1e1230672cbbf55fa)BT\_APPEARANCE\_SENSOR\_WIND

| #define BT\_APPEARANCE\_SENSOR\_WIND   0x0550 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Wind Sensor.

## [◆ ](#gace31a591ef3b5f0812e4cbf417a2205a)BT\_APPEARANCE\_SIGNAGE\_DIGITAL

| #define BT\_APPEARANCE\_SIGNAGE\_DIGITAL   0x0AC1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Digital Signage.

## [◆ ](#gaa4674b06751edf98fa88ede568a68ad4)BT\_APPEARANCE\_SIGNAGE\_ELECTRONIC\_LABEL

| #define BT\_APPEARANCE\_SIGNAGE\_ELECTRONIC\_LABEL   0x0AC2 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Electronic Label.

## [◆ ](#gaa5662d4a544b034243faa45245a9728b)BT\_APPEARANCE\_SMARTWATCH

| #define BT\_APPEARANCE\_SMARTWATCH   0x00C2 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Smartwatch.

## [◆ ](#ga42b9d596efb757b209f080a8c33f3723)BT\_APPEARANCE\_SPIROMETER\_HANDHELD

| #define BT\_APPEARANCE\_SPIROMETER\_HANDHELD   0x0DC1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Handheld Spirometer.

## [◆ ](#gaca9cc93d768145ec3d87b88740954b50)BT\_APPEARANCE\_SPORTS\_WATCH

| #define BT\_APPEARANCE\_SPORTS\_WATCH   0x00C1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Sports Watch.

## [◆ ](#ga58e1989c99b5a223a318a716d62f6e2b)BT\_APPEARANCE\_SPOT\_LIGHT

| #define BT\_APPEARANCE\_SPOT\_LIGHT   0x058F |
| --- |

`#include <[gap.h](gap_8h.md)>`

Spotlight.

## [◆ ](#ga54283061a207491dcfced899c0fc3008)BT\_APPEARANCE\_THERMOMETER\_EAR

| #define BT\_APPEARANCE\_THERMOMETER\_EAR   0x0301 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Ear Thermometer.

## [◆ ](#gafd1c9ca638a362a01897792e5a00a0c5)BT\_APPEARANCE\_UNKNOWN

| #define BT\_APPEARANCE\_UNKNOWN   0x0000 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Generic Unknown.

## [◆ ](#gaa149e56e4b4a1b6dde821fbdac3d9c32)BT\_APPEARANCE\_VEHICLE\_AGRICULTURAL

| #define BT\_APPEARANCE\_VEHICLE\_AGRICULTURAL   0x08CD |
| --- |

`#include <[gap.h](gap_8h.md)>`

Agricultural Vehicle.

## [◆ ](#ga0da02a18987c653a3232c28a3e4908f7)BT\_APPEARANCE\_VEHICLE\_BUS

| #define BT\_APPEARANCE\_VEHICLE\_BUS   0x08CB |
| --- |

`#include <[gap.h](gap_8h.md)>`

Bus.

## [◆ ](#gafcb3909bf61bb130f8c0a217e69477b8)BT\_APPEARANCE\_VEHICLE\_CAMPER\_OR\_CARAVAN

| #define BT\_APPEARANCE\_VEHICLE\_CAMPER\_OR\_CARAVAN   0x08CE |
| --- |

`#include <[gap.h](gap_8h.md)>`

Camper/Caravan.

## [◆ ](#ga6257291ed3e6d09ce6197e2081b36d04)BT\_APPEARANCE\_VEHICLE\_CAR

| #define BT\_APPEARANCE\_VEHICLE\_CAR   0x08C1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Car.

## [◆ ](#ga31ff643e1efccffd9ba73c793f63837c)BT\_APPEARANCE\_VEHICLE\_LARGE\_GOODS

| #define BT\_APPEARANCE\_VEHICLE\_LARGE\_GOODS   0x08C2 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Large Goods Vehicle.

## [◆ ](#gac22a0476760c42eb8f00b36b74361c5e)BT\_APPEARANCE\_VEHICLE\_LIGHT

| #define BT\_APPEARANCE\_VEHICLE\_LIGHT   0x08C8 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Light Vehicle.

## [◆ ](#ga0cf473bbf07d4576ab9f0116ca48f161)BT\_APPEARANCE\_VEHICLE\_MINIBUS

| #define BT\_APPEARANCE\_VEHICLE\_MINIBUS   0x08CA |
| --- |

`#include <[gap.h](gap_8h.md)>`

Minibus.

## [◆ ](#ga18b0231dbd97d8871f685774f9e1b4e1)BT\_APPEARANCE\_VEHICLE\_MOPED

| #define BT\_APPEARANCE\_VEHICLE\_MOPED   0x08C6 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Moped.

## [◆ ](#gaa71eaa4fd0eef66a794475cb44aaf397)BT\_APPEARANCE\_VEHICLE\_MOTORBIKE

| #define BT\_APPEARANCE\_VEHICLE\_MOTORBIKE   0x08C4 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Motorbike.

## [◆ ](#ga03e3660bdc2e439126f2f8df8ea335ee)BT\_APPEARANCE\_VEHICLE\_QUAD\_BIKE

| #define BT\_APPEARANCE\_VEHICLE\_QUAD\_BIKE   0x08C9 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Quad Bike.

## [◆ ](#ga9366a994d42c88490313380d419b2a8e)BT\_APPEARANCE\_VEHICLE\_RECREATIONAL

| #define BT\_APPEARANCE\_VEHICLE\_RECREATIONAL   0x08CF |
| --- |

`#include <[gap.h](gap_8h.md)>`

Recreational Vehicle/Motor Home.

## [◆ ](#gae082982b90d94404b69c57987d8a2c5a)BT\_APPEARANCE\_VEHICLE\_SCOOTER

| #define BT\_APPEARANCE\_VEHICLE\_SCOOTER   0x08C5 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Scooter.

## [◆ ](#ga8159dfd6933a2a5fdb2c72da9623bc2e)BT\_APPEARANCE\_VEHICLE\_THREE\_WHEELED

| #define BT\_APPEARANCE\_VEHICLE\_THREE\_WHEELED   0x08C7 |
| --- |

`#include <[gap.h](gap_8h.md)>`

3-Wheeled Vehicle

## [◆ ](#gabde7af9f7c25d56f5fb9643398273526)BT\_APPEARANCE\_VEHICLE\_TROLLEY

| #define BT\_APPEARANCE\_VEHICLE\_TROLLEY   0x08CC |
| --- |

`#include <[gap.h](gap_8h.md)>`

Trolley.

## [◆ ](#ga68ade931a12e5d9e9863decad3d8de9e)BT\_APPEARANCE\_VEHICLE\_TWO\_WHEELED

| #define BT\_APPEARANCE\_VEHICLE\_TWO\_WHEELED   0x08C3 |
| --- |

`#include <[gap.h](gap_8h.md)>`

2-Wheeled Vehicle

## [◆ ](#gad748f5dc2e0622353d6159c3a3e4241b)BT\_APPEARANCE\_WALKING\_IN\_SHOE

| #define BT\_APPEARANCE\_WALKING\_IN\_SHOE   0x0441 |
| --- |

`#include <[gap.h](gap_8h.md)>`

In-Shoe Running Walking Sensor.

## [◆ ](#gad211a7e2f11dc7effe3ba28e8c4f7092)BT\_APPEARANCE\_WALKING\_ON\_HIP

| #define BT\_APPEARANCE\_WALKING\_ON\_HIP   0x0443 |
| --- |

`#include <[gap.h](gap_8h.md)>`

On-Hip Running Walking Sensor.

## [◆ ](#ga0a4541459ba8b41a3938c5b8d35b1c8c)BT\_APPEARANCE\_WALKING\_ON\_SHOE

| #define BT\_APPEARANCE\_WALKING\_ON\_SHOE   0x0442 |
| --- |

`#include <[gap.h](gap_8h.md)>`

On-Shoe Running Walking Sensor.

## [◆ ](#gab480735e2ba8db23d2668ea3a2137214)BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_EARBUD

| #define BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_EARBUD   0x0941 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Earbud.

## [◆ ](#gae420044380309abba1b9570d26735315)BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADPHONES

| #define BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADPHONES   0x0943 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Headphones.

## [◆ ](#ga8bd98ba3a4c1cbf8dbf8235d9ad0f943)BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADSET

| #define BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADSET   0x0942 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Headset.

## [◆ ](#ga59ea8ff5efec7a19bce8440e7ae78a1e)BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_NECK\_BAND

| #define BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_NECK\_BAND   0x0944 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Neck Band.

## [◆ ](#ga9945bb52a9ee3268efda7d5e05421e12)BT\_APPEARANCE\_WINDOW\_AWNING

| #define BT\_APPEARANCE\_WINDOW\_AWNING   0x0803 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Window Awning.

## [◆ ](#ga717efaeab0329ded066567761b9983a7)BT\_APPEARANCE\_WINDOW\_BLINDS

| #define BT\_APPEARANCE\_WINDOW\_BLINDS   0x0802 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Window Blinds.

## [◆ ](#ga20352e58e6cec63efbb6beaa75c0e330)BT\_APPEARANCE\_WINDOW\_CURTAIN

| #define BT\_APPEARANCE\_WINDOW\_CURTAIN   0x0804 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Window Curtain.

## [◆ ](#ga0a0b87095177af0560a540e545c97f42)BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SCREEN

| #define BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SCREEN   0x0806 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Exterior Screen.

## [◆ ](#ga7ead13b128fbc50be3f5c101fb1383cb)BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SHUTTER

| #define BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SHUTTER   0x0805 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Exterior Shutter.

## [◆ ](#ga37614ae63c8287bc4bd0c9a5bf00502e)BT\_APPEARANCE\_WINDOW\_SHADES

| #define BT\_APPEARANCE\_WINDOW\_SHADES   0x0801 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Window Shades.

## [◆ ](#ga6bbf21c05f24d2c2c710be9bcf05af5f)BT\_COMP\_ID\_LF

| #define BT\_COMP\_ID\_LF   0x05f1 |
| --- |

`#include <[gap.h](gap_8h.md)>`

The Linux Foundation.

## [◆ ](#gaecab0c77f9f912c16c264e7eaf2e4707)BT\_DATA\_3D\_INFO

| #define BT\_DATA\_3D\_INFO   0x3D |
| --- |

`#include <[gap.h](gap_8h.md)>`

3D Information Data

## [◆ ](#ga6fd8c0f32bbcb97aaafee51fda0b601e)BT\_DATA\_ADV\_INT

| #define BT\_DATA\_ADV\_INT   0x1a |
| --- |

`#include <[gap.h](gap_8h.md)>`

Advertising Interval.

## [◆ ](#gad4ac2e0de80dddcacc4ca6d25765eebd)BT\_DATA\_ADV\_INT\_LONG

| #define BT\_DATA\_ADV\_INT\_LONG   0x2f |
| --- |

`#include <[gap.h](gap_8h.md)>`

Advertising Interval long.

## [◆ ](#ga16feb94cd09c04d020450f61646f5486)BT\_DATA\_BIG\_INFO

| #define BT\_DATA\_BIG\_INFO   0x2c |
| --- |

`#include <[gap.h](gap_8h.md)>`

BIGInfo.

## [◆ ](#ga72d2e55819db593a6db77579ebfe1e9d)BT\_DATA\_BROADCAST\_CODE

| #define BT\_DATA\_BROADCAST\_CODE   0x2d |
| --- |

`#include <[gap.h](gap_8h.md)>`

Broadcast Code.

## [◆ ](#ga7d781791bc85fe3c7ea839ff617ee6e7)BT\_DATA\_BROADCAST\_NAME

| #define BT\_DATA\_BROADCAST\_NAME   0x30 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Broadcast Name.

## [◆ ](#gae3eb96c0f127b6417d7cad288faaaceb)BT\_DATA\_CHANNEL\_MAP\_UPDATE\_IND

| #define BT\_DATA\_CHANNEL\_MAP\_UPDATE\_IND   0x28 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Channel Map Update Indication.

## [◆ ](#ga122da4184d606ae140f8a311aaebeedd)BT\_DATA\_CSIS\_RSI

| #define BT\_DATA\_CSIS\_RSI   0x2e |
| --- |

`#include <[gap.h](gap_8h.md)>`

CSIS Random Set ID type.

## [◆ ](#ga152c3028a2befcc4caf40aa6590c80b7)BT\_DATA\_DEVICE\_CLASS

| #define BT\_DATA\_DEVICE\_CLASS   0x0d |
| --- |

`#include <[gap.h](gap_8h.md)>`

Class of Device.

## [◆ ](#gac9402c597e5b4497f4bcd22d5177cc23)BT\_DATA\_DEVICE\_ID

| #define BT\_DATA\_DEVICE\_ID   0x10 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Device ID (Profile).

## [◆ ](#ga41d5c898144e89b6035f92ff506f38a3)BT\_DATA\_ENCRYPTED\_AD\_DATA

| #define BT\_DATA\_ENCRYPTED\_AD\_DATA   0x31 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Encrypted Advertising Data.

## [◆ ](#ga90c7a1175148f3a56b04dc0b29525a4d)BT\_DATA\_ESL

| #define BT\_DATA\_ESL   0x34 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Electronic Shelf Label Profile.

## [◆ ](#ga396b92d418fcb8263895e420b9df3df2)BT\_DATA\_FLAGS

| #define BT\_DATA\_FLAGS   0x01 |
| --- |

`#include <[gap.h](gap_8h.md)>`

AD flags.

## [◆ ](#ga67fc721da05758b7d7a36aecaa035fac)BT\_DATA\_GAP\_APPEARANCE

| #define BT\_DATA\_GAP\_APPEARANCE   0x19 |
| --- |

`#include <[gap.h](gap_8h.md)>`

GAP appearance.

## [◆ ](#ga0f29f9d8f5a336af430f0a603e87e995)BT\_DATA\_INDOOR\_POS

| #define BT\_DATA\_INDOOR\_POS   0x25 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Indoor Positioning.

## [◆ ](#gad9e8a273239fa160a6b2797ef5563a94)BT\_DATA\_LE\_BT\_DEVICE\_ADDRESS

| #define BT\_DATA\_LE\_BT\_DEVICE\_ADDRESS   0x1b |
| --- |

`#include <[gap.h](gap_8h.md)>`

LE Bluetooth Device Address.

## [◆ ](#ga255c7cb16eb24b95fa0f531fc4574273)BT\_DATA\_LE\_ROLE

| #define BT\_DATA\_LE\_ROLE   0x1c |
| --- |

`#include <[gap.h](gap_8h.md)>`

LE Role.

## [◆ ](#ga883dda02c157f0de8157b1c5f66aafd0)BT\_DATA\_LE\_SC\_CONFIRM\_VALUE

| #define BT\_DATA\_LE\_SC\_CONFIRM\_VALUE   0x22 |
| --- |

`#include <[gap.h](gap_8h.md)>`

LE SC Confirmation Value.

## [◆ ](#gacbc31c67684e3c68481501cf89f9ec68)BT\_DATA\_LE\_SC\_RANDOM\_VALUE

| #define BT\_DATA\_LE\_SC\_RANDOM\_VALUE   0x23 |
| --- |

`#include <[gap.h](gap_8h.md)>`

LE SC Random Value.

## [◆ ](#ga207bc1e5405a4fd3f39863a2cb304ebc)BT\_DATA\_LE\_SUPPORTED\_FEATURES

| #define BT\_DATA\_LE\_SUPPORTED\_FEATURES   0x27 |
| --- |

`#include <[gap.h](gap_8h.md)>`

LE Supported Features.

## [◆ ](#ga63b846807bff632b1cdd49b1e46e63b4)BT\_DATA\_MANUFACTURER\_DATA

| #define BT\_DATA\_MANUFACTURER\_DATA   0xff |
| --- |

`#include <[gap.h](gap_8h.md)>`

Manufacturer Specific Data.

## [◆ ](#ga59cc479be1f6c61a4a47aa6f479fe67a)BT\_DATA\_MESH\_BEACON

| #define BT\_DATA\_MESH\_BEACON   0x2b |
| --- |

`#include <[gap.h](gap_8h.md)>`

Mesh Beacon.

## [◆ ](#gac351c67ab58520b796fa713602d9f602)BT\_DATA\_MESH\_MESSAGE

| #define BT\_DATA\_MESH\_MESSAGE   0x2a |
| --- |

`#include <[gap.h](gap_8h.md)>`

Mesh Networking PDU.

## [◆ ](#gafc5984d58b0b54ee824dd83bc78dfbe9)BT\_DATA\_MESH\_PROV

| #define BT\_DATA\_MESH\_PROV   0x29 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Mesh Provisioning PDU.

## [◆ ](#gab94a7c5689d296acf47f976538056ab5)BT\_DATA\_NAME\_COMPLETE

| #define BT\_DATA\_NAME\_COMPLETE   0x09 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Complete name.

## [◆ ](#gafc509b33a8d2dd9124f6893eadbe1662)BT\_DATA\_NAME\_SHORTENED

| #define BT\_DATA\_NAME\_SHORTENED   0x08 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Shortened name.

## [◆ ](#ga14a8b1cf9d6c1c9749443a012731d39c)BT\_DATA\_PAWR\_TIMING\_INFO

| #define BT\_DATA\_PAWR\_TIMING\_INFO   0x32 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Periodic Advertising Response Timing Info.

## [◆ ](#gabcf872eafc60c21287f6be63174dc7c8)BT\_DATA\_PERIPHERAL\_INT\_RANGE

| #define BT\_DATA\_PERIPHERAL\_INT\_RANGE   0x12 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Peripheral Connection Interval Range.

## [◆ ](#gacb867f0436d38c5c80e3426ca6247a46)BT\_DATA\_PUB\_TARGET\_ADDR

| #define BT\_DATA\_PUB\_TARGET\_ADDR   0x17 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Public Target Address.

## [◆ ](#ga3d9097d8f53213ccafc152c51ad6fdbd)BT\_DATA\_RAND\_TARGET\_ADDR

| #define BT\_DATA\_RAND\_TARGET\_ADDR   0x18 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Random Target Address.

## [◆ ](#ga324f91521eacd1e9d579c9d52d02eb06)BT\_DATA\_SIMPLE\_PAIRING\_HASH

| #define BT\_DATA\_SIMPLE\_PAIRING\_HASH   0x1d |
| --- |

`#include <[gap.h](gap_8h.md)>`

Simple Pairing Hash C256.

## [◆ ](#ga053c8bb0aedd01b3dd3f6154f4b49999)BT\_DATA\_SIMPLE\_PAIRING\_HASH\_C192

| #define BT\_DATA\_SIMPLE\_PAIRING\_HASH\_C192   0x0e |
| --- |

`#include <[gap.h](gap_8h.md)>`

Simple Pairing Hash C-192.

## [◆ ](#gad7e7dd2d3a972e53f9e5e80627bd07e6)BT\_DATA\_SIMPLE\_PAIRING\_RAND

| #define BT\_DATA\_SIMPLE\_PAIRING\_RAND   0x1e |
| --- |

`#include <[gap.h](gap_8h.md)>`

Simple Pairing Randomizer R256.

## [◆ ](#ga280f1f96c5204960fe034c9ddaf194ec)BT\_DATA\_SIMPLE\_PAIRING\_RAND\_C192

| #define BT\_DATA\_SIMPLE\_PAIRING\_RAND\_C192   0x0f |
| --- |

`#include <[gap.h](gap_8h.md)>`

Simple Pairing Randomizer R-192.

## [◆ ](#gaa12c742d1c955036aa3f55e84df69890)BT\_DATA\_SM\_OOB\_FLAGS

| #define BT\_DATA\_SM\_OOB\_FLAGS   0x11 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Security Manager OOB Flags.

## [◆ ](#ga5014acb2fe8e76b855b55bf98abe6d05)BT\_DATA\_SM\_TK\_VALUE

| #define BT\_DATA\_SM\_TK\_VALUE   0x10 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Security Manager TK Value.

## [◆ ](#ga217df3f70846e86fa09e5605d5acd291)BT\_DATA\_SOLICIT128

| #define BT\_DATA\_SOLICIT128   0x15 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Solicit UUIDs, 128-bit.

## [◆ ](#ga2ad4d2ec2ff29c0aad5159de12d3f741)BT\_DATA\_SOLICIT16

| #define BT\_DATA\_SOLICIT16   0x14 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Solicit UUIDs, 16-bit.

## [◆ ](#ga76e7e8971ed841b87fda08793a00b14f)BT\_DATA\_SOLICIT32

| #define BT\_DATA\_SOLICIT32   0x1f |
| --- |

`#include <[gap.h](gap_8h.md)>`

Solicit UUIDs, 32-bit.

## [◆ ](#gaa53847910515d9488b490f17a4fdf0d1)BT\_DATA\_SVC\_DATA128

| #define BT\_DATA\_SVC\_DATA128   0x21 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Service data, 128-bit UUID.

## [◆ ](#ga76990dda919688b369decaf9d3606b32)BT\_DATA\_SVC\_DATA16

| #define BT\_DATA\_SVC\_DATA16   0x16 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Service data, 16-bit UUID.

## [◆ ](#ga7d411a723ff2f038c3b7a1e09c88cb3d)BT\_DATA\_SVC\_DATA32

| #define BT\_DATA\_SVC\_DATA32   0x20 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Service data, 32-bit UUID.

## [◆ ](#ga8e9ccc669ee545152b2d9b3120692d55)BT\_DATA\_TRANS\_DISCOVER\_DATA

| #define BT\_DATA\_TRANS\_DISCOVER\_DATA   0x26 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Transport Discovery Data.

## [◆ ](#ga4988c17578c4cf76fcdd9d44e1c931b0)BT\_DATA\_TX\_POWER

| #define BT\_DATA\_TX\_POWER   0x0a |
| --- |

`#include <[gap.h](gap_8h.md)>`

Tx Power.

## [◆ ](#ga3c6a5903cc4a46aaf0b30a0de0179403)BT\_DATA\_URI

| #define BT\_DATA\_URI   0x24 |
| --- |

`#include <[gap.h](gap_8h.md)>`

URI.

## [◆ ](#gaafcade3dbbcb4005f4590e994f91884b)BT\_DATA\_UUID128\_ALL

| #define BT\_DATA\_UUID128\_ALL   0x07 |
| --- |

`#include <[gap.h](gap_8h.md)>`

128-bit UUID, all listed

## [◆ ](#ga5c4f7fc1b93c611e95f735330fba243b)BT\_DATA\_UUID128\_SOME

| #define BT\_DATA\_UUID128\_SOME   0x06 |
| --- |

`#include <[gap.h](gap_8h.md)>`

128-bit UUID, more available

## [◆ ](#ga0d55063b9ad321b5c530a0012337df8a)BT\_DATA\_UUID16\_ALL

| #define BT\_DATA\_UUID16\_ALL   0x03 |
| --- |

`#include <[gap.h](gap_8h.md)>`

16-bit UUID, all listed

## [◆ ](#ga6c725bd3d31c159a4d046561dbca38ba)BT\_DATA\_UUID16\_SOME

| #define BT\_DATA\_UUID16\_SOME   0x02 |
| --- |

`#include <[gap.h](gap_8h.md)>`

16-bit UUID, more available

## [◆ ](#gaaf825c3e4686e572a35ddd46ee6fe2e8)BT\_DATA\_UUID32\_ALL

| #define BT\_DATA\_UUID32\_ALL   0x05 |
| --- |

`#include <[gap.h](gap_8h.md)>`

32-bit UUID, all listed

## [◆ ](#ga2486a6748490ba57e442ca15223482ef)BT\_DATA\_UUID32\_SOME

| #define BT\_DATA\_UUID32\_SOME   0x04 |
| --- |

`#include <[gap.h](gap_8h.md)>`

32-bit UUID, more available

## [◆ ](#ga13acf16d3d8edd39636bb10df752775a)BT\_GAP\_ADV\_FAST\_INT\_MAX\_1

| #define BT\_GAP\_ADV\_FAST\_INT\_MAX\_1   0x0060 /\* 60 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#gaebc3ce60836522d883f664227a3ffcfb)BT\_GAP\_ADV\_FAST\_INT\_MAX\_2

| #define BT\_GAP\_ADV\_FAST\_INT\_MAX\_2   0x00f0 /\* 150 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga397a52fe616416665b46a2bc454c2e11)BT\_GAP\_ADV\_FAST\_INT\_MIN\_1

| #define BT\_GAP\_ADV\_FAST\_INT\_MIN\_1   0x0030 /\* 30 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga9573e6bcdae3aae9d51c0becbbd7ac60)BT\_GAP\_ADV\_FAST\_INT\_MIN\_2

| #define BT\_GAP\_ADV\_FAST\_INT\_MIN\_2   0x00a0 /\* 100 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#gabe483d4dd601b11ac3eea570c962b1ec)BT\_GAP\_ADV\_HIGH\_DUTY\_CYCLE\_MAX\_TIMEOUT

| #define BT\_GAP\_ADV\_HIGH\_DUTY\_CYCLE\_MAX\_TIMEOUT   128 |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga7261e64328e433d333d88d3a4cad21de)BT\_GAP\_ADV\_INTERVAL\_TO\_MS

| #define BT\_GAP\_ADV\_INTERVAL\_TO\_MS | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

([BT\_GAP\_ADV\_INTERVAL\_TO\_US](#ga6e10b5311c785ad7eea10743987c0f27)(\_interval) / [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27))

[BT\_GAP\_ADV\_INTERVAL\_TO\_US](#ga6e10b5311c785ad7eea10743987c0f27)

#define BT\_GAP\_ADV\_INTERVAL\_TO\_US(\_interval)

Convert periodic advertising interval (N \* 0.625 ms) to microseconds.

**Definition** gap.h:841

[USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)

#define USEC\_PER\_MSEC

number of microseconds per millisecond

**Definition** sys\_clock.h:89

Convert periodic advertising interval (N \* 0.625 ms) to milliseconds.

Value range of `_interval` is [BT\_LE\_ADV\_INTERVAL\_MIN](hci__types_8h.md#ac89392b0484164812b77360d15d9984b "BT_LE_ADV_INTERVAL_MIN") to [BT\_LE\_ADV\_INTERVAL\_MAX](hci__types_8h.md#a6479fb2c964155cfcdd3cc48c3a45618 "BT_LE_ADV_INTERVAL_MAX")

Note
:   When intervals cannot be represented in milliseconds, this will round down. For example [BT\_GAP\_ADV\_INTERVAL\_TO\_MS(0x0021)](#ga7261e64328e433d333d88d3a4cad21de) will become 20 ms instead of 20.625 ms

## [◆ ](#ga6e10b5311c785ad7eea10743987c0f27)BT\_GAP\_ADV\_INTERVAL\_TO\_US

| #define BT\_GAP\_ADV\_INTERVAL\_TO\_US | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))((\_interval) \* 625U))

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Convert periodic advertising interval (N \* 0.625 ms) to microseconds.

Value range of `_interval` is [BT\_LE\_ADV\_INTERVAL\_MIN](hci__types_8h.md#ac89392b0484164812b77360d15d9984b "BT_LE_ADV_INTERVAL_MIN") to [BT\_LE\_ADV\_INTERVAL\_MAX](hci__types_8h.md#a6479fb2c964155cfcdd3cc48c3a45618 "BT_LE_ADV_INTERVAL_MAX")

## [◆ ](#ga39ab5040c9471631486da7dbebd9c36f)BT\_GAP\_ADV\_MAX\_ADV\_DATA\_LEN

| #define BT\_GAP\_ADV\_MAX\_ADV\_DATA\_LEN   31 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Maximum advertising data length.

## [◆ ](#ga53af114e4925482739dc50dc84c2f641)BT\_GAP\_ADV\_MAX\_EXT\_ADV\_DATA\_LEN

| #define BT\_GAP\_ADV\_MAX\_EXT\_ADV\_DATA\_LEN   1650 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Maximum extended advertising data length.

Note
:   The maximum advertising data length that can be sent by an extended advertiser is defined by the controller.

## [◆ ](#gadecbfb823bbb6ffdd48be02df2f05f87)BT\_GAP\_ADV\_SLOW\_INT\_MAX

| #define BT\_GAP\_ADV\_SLOW\_INT\_MAX   0x0780 /\* 1.2 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga647f70c07c15f11287b735cbaad2a326)BT\_GAP\_ADV\_SLOW\_INT\_MIN

| #define BT\_GAP\_ADV\_SLOW\_INT\_MIN   0x0640 /\* 1 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga90cfab7c375a8af6f9224a5635cbd023)BT\_GAP\_DATA\_LEN\_DEFAULT

| #define BT\_GAP\_DATA\_LEN\_DEFAULT   0x001b /\* 27 bytes \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

Default data length.

## [◆ ](#gacf5f35866d4677bd45c6e567886cabb9)BT\_GAP\_DATA\_LEN\_MAX

| #define BT\_GAP\_DATA\_LEN\_MAX   0x00fb /\* 251 bytes \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

Maximum data length.

## [◆ ](#ga245249c0b6f8ccc419f2132f76362908)BT\_GAP\_DATA\_TIME\_DEFAULT

| #define BT\_GAP\_DATA\_TIME\_DEFAULT   0x0148 /\* 328 us \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

Default data time.

## [◆ ](#ga379b5d8d7f243abbc584c288cd01815f)BT\_GAP\_DATA\_TIME\_MAX

| #define BT\_GAP\_DATA\_TIME\_MAX   0x4290 /\* 17040 us \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

Maximum data time.

## [◆ ](#ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1)BT\_GAP\_INIT\_CONN\_INT\_MAX

| #define BT\_GAP\_INIT\_CONN\_INT\_MAX   0x0028 /\* 50 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#gadaa7f1547c4ea22936087c181d82a552)BT\_GAP\_INIT\_CONN\_INT\_MIN

| #define BT\_GAP\_INIT\_CONN\_INT\_MIN   0x0018 /\* 30 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga46c1e49ca3285ed9fc1b4ac593a25cd3)BT\_GAP\_ISO\_INTERVAL\_TO\_MS

| #define BT\_GAP\_ISO\_INTERVAL\_TO\_MS | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

([BT\_GAP\_ISO\_INTERVAL\_TO\_US](#ga4feca4664259c43121c2ff481d9ee611)(\_interval) / [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27))

[BT\_GAP\_ISO\_INTERVAL\_TO\_US](#ga4feca4664259c43121c2ff481d9ee611)

#define BT\_GAP\_ISO\_INTERVAL\_TO\_US(\_interval)

Convert isochronous interval (N \* 1.25 ms) to microseconds.

**Definition** gap.h:858

Convert isochronous interval (N \* 1.25 ms) to milliseconds.

Value range of `_interval` is [BT\_HCI\_ISO\_INTERVAL\_MIN](hci__types_8h.md#a9d5e85ae1380fa85bae9d7e5e67aa0ae "BT_HCI_ISO_INTERVAL_MIN") to [BT\_HCI\_ISO\_INTERVAL\_MAX](hci__types_8h.md#aaadbec2cc6adc2bb14d7117396023d06 "BT_HCI_ISO_INTERVAL_MAX")

Note
:   When intervals cannot be represented in milliseconds, this will round down. For example [BT\_GAP\_ISO\_INTERVAL\_TO\_MS(0x0005)](#ga46c1e49ca3285ed9fc1b4ac593a25cd3) will become 6 ms instead of 6.25 ms

## [◆ ](#ga4feca4664259c43121c2ff481d9ee611)BT\_GAP\_ISO\_INTERVAL\_TO\_US

| #define BT\_GAP\_ISO\_INTERVAL\_TO\_US | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))((\_interval) \* 1250U))

Convert isochronous interval (N \* 1.25 ms) to microseconds.

Value range of `_interval` is [BT\_HCI\_ISO\_INTERVAL\_MIN](hci__types_8h.md#a9d5e85ae1380fa85bae9d7e5e67aa0ae "BT_HCI_ISO_INTERVAL_MIN") to [BT\_HCI\_ISO\_INTERVAL\_MAX](hci__types_8h.md#aaadbec2cc6adc2bb14d7117396023d06 "BT_HCI_ISO_INTERVAL_MAX")

## [◆ ](#gaef9c34f229f1b8b06d3e6cd44a1014ef)BT\_GAP\_MS\_TO\_ADV\_INTERVAL

| #define BT\_GAP\_MS\_TO\_ADV\_INTERVAL | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

([BT\_GAP\_US\_TO\_ADV\_INTERVAL](#gac79626389f62bb7b3e5b5f6d3a5eaf2b)((\_interval) \* [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)))

[BT\_GAP\_US\_TO\_ADV\_INTERVAL](#gac79626389f62bb7b3e5b5f6d3a5eaf2b)

#define BT\_GAP\_US\_TO\_ADV\_INTERVAL(\_interval)

Convert microseconds to advertising interval units (0.625 ms).

**Definition** gap.h:894

Convert milliseconds to advertising interval units (0.625 ms).

Value range of `_interval` is 20 to 1024

Note
:   If `_interval` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_MS\_TO\_ADV\_INTERVAL(21)](#gaef9c34f229f1b8b06d3e6cd44a1014ef) will become 20.625 milliseconds

## [◆ ](#gaa3703cccd343dbb6418fdeb47a718eb5)BT\_GAP\_MS\_TO\_CONN\_EVENT\_LEN

| #define BT\_GAP\_MS\_TO\_CONN\_EVENT\_LEN | ( |  | *\_event\_len* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

([BT\_GAP\_US\_TO\_CONN\_EVENT\_LEN](#ga8905e22b1864021b77367c228b8bff48)((\_event\_len) \* [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)))

[BT\_GAP\_US\_TO\_CONN\_EVENT\_LEN](#ga8905e22b1864021b77367c228b8bff48)

#define BT\_GAP\_US\_TO\_CONN\_EVENT\_LEN(\_event\_len)

Convert milliseconds to connection event length units (0.625).

**Definition** gap.h:1043

Convert milliseconds to connection event length units (0.625).

Value range of `_event_len` is 0 to 40959.375

Note
:   If `_event_len` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_MS\_TO\_CONN\_EVENT\_LEN(21)](#gaa3703cccd343dbb6418fdeb47a718eb5) will become 20.625 milliseconds

## [◆ ](#ga75985e2c444da7b2426cc746c9781c8c)BT\_GAP\_MS\_TO\_CONN\_INTERVAL

| #define BT\_GAP\_MS\_TO\_CONN\_INTERVAL | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

([BT\_GAP\_US\_TO\_CONN\_INTERVAL](#gab12ba919a5a389b4c342d142d3a9ce6e)((\_interval) \* [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)))

[BT\_GAP\_US\_TO\_CONN\_INTERVAL](#gab12ba919a5a389b4c342d142d3a9ce6e)

#define BT\_GAP\_US\_TO\_CONN\_INTERVAL(\_interval)

Convert microseconds to connection interval units (1.25 ms).

**Definition** gap.h:1002

Convert milliseconds to connection interval units (1.25 ms).

Value range of `_interval` is 7.5 to 4000

Note
:   If `_interval` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_MS\_TO\_CONN\_INTERVAL(21)](#ga75985e2c444da7b2426cc746c9781c8c) will become 20 milliseconds

## [◆ ](#ga24f79cacceeea262987f3cdaf2ef6bc3)BT\_GAP\_MS\_TO\_CONN\_TIMEOUT

| #define BT\_GAP\_MS\_TO\_CONN\_TIMEOUT | ( |  | *\_timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))((\_timeout) / 10U))

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

Convert milliseconds to connection supervision timeout units (10 ms).

Value range of `_timeout` is 100 to 32000

Note
:   If `_timeout` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_MS\_TO\_CONN\_TIMEOUT(4005)](#ga24f79cacceeea262987f3cdaf2ef6bc3) will become 4000 milliseconds

## [◆ ](#ga15ec0bc7c9bab797d6c5595269a33ea4)BT\_GAP\_MS\_TO\_PER\_ADV\_INTERVAL

| #define BT\_GAP\_MS\_TO\_PER\_ADV\_INTERVAL | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

([BT\_GAP\_US\_TO\_PER\_ADV\_INTERVAL](#ga5a9da01507b4356c2ad6f8309257f2ce)((\_interval) \* [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)))

[BT\_GAP\_US\_TO\_PER\_ADV\_INTERVAL](#ga5a9da01507b4356c2ad6f8309257f2ce)

#define BT\_GAP\_US\_TO\_PER\_ADV\_INTERVAL(\_interval)

Convert microseconds to periodic advertising interval units (1.25 ms).

**Definition** gap.h:915

Convert milliseconds to periodic advertising interval units (1.25 ms).

Value range of `_interval` is 7.5 to 81918.75

Note
:   If `_interval` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_MS\_TO\_PER\_ADV\_INTERVAL(11)](#ga15ec0bc7c9bab797d6c5595269a33ea4) will become 10 milliseconds

## [◆ ](#ga242a6a4e3dd138073c01bc600c9642eb)BT\_GAP\_MS\_TO\_PER\_ADV\_SYNC\_TIMEOUT

| #define BT\_GAP\_MS\_TO\_PER\_ADV\_SYNC\_TIMEOUT | ( |  | *\_timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))((\_timeout) / 10U))

Convert milliseconds to periodic advertising sync timeout units (10 ms).

Value range of `_timeout` is 100 to 163840

Note
:   If `_timeout` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_MS\_TO\_PER\_ADV\_SYNC\_TIMEOUT(4005)](#ga242a6a4e3dd138073c01bc600c9642eb) will become 4000 milliseconds

## [◆ ](#gad18c4a9774014081833905fc9e03fb15)BT\_GAP\_MS\_TO\_SCAN\_INTERVAL

| #define BT\_GAP\_MS\_TO\_SCAN\_INTERVAL | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

([BT\_GAP\_US\_TO\_SCAN\_INTERVAL](#gab65e489c4a799774f6511c6ce5b65ea2)((\_interval) \* [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)))

[BT\_GAP\_US\_TO\_SCAN\_INTERVAL](#gab65e489c4a799774f6511c6ce5b65ea2)

#define BT\_GAP\_US\_TO\_SCAN\_INTERVAL(\_interval)

Convert microseconds to scan interval units (0.625 ms).

**Definition** gap.h:958

Convert milliseconds to scan interval units (0.625 ms).

Value range of `_interval` is 2.5 to 40959.375 if `CONFIG_BT_EXT_ADV` else 2500 to 10240

Note
:   If `_interval` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_MS\_TO\_SCAN\_INTERVAL(21)](#gad18c4a9774014081833905fc9e03fb15) will become 20.625 milliseconds

## [◆ ](#ga5204f7e42b4e33eb8ae4ae71b82a4c88)BT\_GAP\_MS\_TO\_SCAN\_WINDOW

| #define BT\_GAP\_MS\_TO\_SCAN\_WINDOW | ( |  | *\_window* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

([BT\_GAP\_US\_TO\_SCAN\_WINDOW](#gaac5d0ec82d9730b793960c0470ac6342)((\_window) \* [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)))

[BT\_GAP\_US\_TO\_SCAN\_WINDOW](#gaac5d0ec82d9730b793960c0470ac6342)

#define BT\_GAP\_US\_TO\_SCAN\_WINDOW(\_window)

Convert microseconds to scan window units (0.625 ms).

**Definition** gap.h:981

Convert milliseconds to scan window units (0.625 ms).

Value range of `_window` is 2.5 to 40959.375 if `CONFIG_BT_EXT_ADV` else 2500 to 10240

Note
:   If `_window` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_MS\_TO\_SCAN\_WINDOW(21)](#ga5204f7e42b4e33eb8ae4ae71b82a4c88) will become 20.625 milliseconds

## [◆ ](#ga9d6b2af6b96eab6356ded93c54301ef6)BT\_GAP\_NO\_TIMEOUT

| #define BT\_GAP\_NO\_TIMEOUT   0x0000 |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga849315b0b724af6017b910e78db0cfae)BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_1

| #define BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_1   0x0030 /\* 60 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga264134294d8378d6e7d2bc52d4e0af1c)BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_2

| #define BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_2   0x0078 /\* 150 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#gafd724ebc809044574283c5547beda824)BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_1

| #define BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_1   0x0018 /\* 30 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga61eb4d6d65f1dd9c475a6f2f44b27957)BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_2

| #define BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_2   0x0050 /\* 100 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#gac240015012694df3557679d99da6c1a9)BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_MS

| #define BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_MS | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

([BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_US](#ga63587ef565ccde477b9c6f03faf778a5)(\_interval) / [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27))

[BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_US](#ga63587ef565ccde477b9c6f03faf778a5)

#define BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_US(\_interval)

Convert periodic advertising interval (N \* 1.25 ms) to microseconds \*.

**Definition** gap.h:875

Convert periodic advertising interval (N \* 1.25 ms) to milliseconds.

Note
:   When intervals cannot be represented in milliseconds, this will round down. For example [BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_MS(0x0009)](#gac240015012694df3557679d99da6c1a9) will become 11 ms instead of 11.25 ms

## [◆ ](#ga63587ef565ccde477b9c6f03faf778a5)BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_US

| #define BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_US | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))((\_interval) \* 1250U))

Convert periodic advertising interval (N \* 1.25 ms) to microseconds \*.

Value range of `_interval` is [BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MIN](hci__types_8h.md#a04f870ac03c1baca22ab5d984354f3bf "BT_HCI_LE_PER_ADV_INTERVAL_MIN") to [BT\_HCI\_LE\_PER\_ADV\_INTERVAL\_MAX](hci__types_8h.md#a2f2216a88cf77ccac1c9a2f6c5820746 "BT_HCI_LE_PER_ADV_INTERVAL_MAX")

## [◆ ](#ga80bf3f1fb6f34a2c4363687149c365bd)BT\_GAP\_PER\_ADV\_MAX\_INTERVAL

| #define BT\_GAP\_PER\_ADV\_MAX\_INTERVAL   0xFFFF /\* 81.91875 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

Maximum Periodic Advertising Interval (N \* 1.25 ms).

## [◆ ](#gaf92b229c47309a7a5e99047f28b860e7)BT\_GAP\_PER\_ADV\_MAX\_SKIP

| #define BT\_GAP\_PER\_ADV\_MAX\_SKIP   0x01F3 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Maximum number of consecutive periodic advertisement events that can be skipped after a successful receive.

## [◆ ](#gad6674199f615fa6ecaeb1fe9d099e04c)BT\_GAP\_PER\_ADV\_MAX\_TIMEOUT

| #define BT\_GAP\_PER\_ADV\_MAX\_TIMEOUT   0x4000 /\* 163.84 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

Maximum Periodic Advertising Timeout (N \* 10 ms).

## [◆ ](#ga07e21fdeb8a0a0b967690898bef2f7aa)BT\_GAP\_PER\_ADV\_MIN\_INTERVAL

| #define BT\_GAP\_PER\_ADV\_MIN\_INTERVAL   0x0006 /\* 7.5 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

Minimum Periodic Advertising Interval (N \* 1.25 ms).

## [◆ ](#ga17d8ae7e98f6a1dfead4f8ecb75f9645)BT\_GAP\_PER\_ADV\_MIN\_TIMEOUT

| #define BT\_GAP\_PER\_ADV\_MIN\_TIMEOUT   0x000A /\* 100 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

Minimum Periodic Advertising Timeout (N \* 10 ms).

## [◆ ](#gaa618da2a7c217527b0d962315caa1c22)BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX

| #define BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX   0x03C0 /\* 1.2 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#gab51898ce46ee9ae468ed7ffc1d117321)BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN

| #define BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN   0x0320 /\* 1 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga64b5c5e429dadf1e875984f69cd399dc)BT\_GAP\_RSSI\_INVALID

| #define BT\_GAP\_RSSI\_INVALID   0x7f |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga747caa714962215453a966a323e77cf8)BT\_GAP\_SCAN\_FAST\_INTERVAL

| #define BT\_GAP\_SCAN\_FAST\_INTERVAL   0x0060 /\* 60 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#gae9356673ee78d9abb27891738344513a)BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN

| #define BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN   0x0030 /\* 30 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga100e1c20813630848a1a80390e8a06a0)BT\_GAP\_SCAN\_FAST\_WINDOW

| #define BT\_GAP\_SCAN\_FAST\_WINDOW   0x0030 /\* 30 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga1acb5143221e9f94af4d5dc3a9eab125)BT\_GAP\_SCAN\_SLOW\_INTERVAL\_1

| #define BT\_GAP\_SCAN\_SLOW\_INTERVAL\_1   0x0800 /\* 1.28 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga38455c10880fddac0a1b4303a642e44d)BT\_GAP\_SCAN\_SLOW\_INTERVAL\_2

| #define BT\_GAP\_SCAN\_SLOW\_INTERVAL\_2   0x1000 /\* 2.56 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga29a1a15bfbe035f439c48d1db96db392)BT\_GAP\_SCAN\_SLOW\_WINDOW\_1

| #define BT\_GAP\_SCAN\_SLOW\_WINDOW\_1   0x0012 /\* 11.25 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#gaa809fd8143c2805768874195ac24936f)BT\_GAP\_SCAN\_SLOW\_WINDOW\_2

| #define BT\_GAP\_SCAN\_SLOW\_WINDOW\_2   0x0012 /\* 11.25 ms \*/ |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#ga103af3e3142473be8897cd2647dca915)BT\_GAP\_SID\_INVALID

| #define BT\_GAP\_SID\_INVALID   0xff |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#gafa6f803fe3ada07030fb1f2f725940c4)BT\_GAP\_SID\_MAX

| #define BT\_GAP\_SID\_MAX   0x0F |
| --- |

`#include <[gap.h](gap_8h.md)>`

Maximum advertising set number.

## [◆ ](#ga61ccce819d75313cb2ee58309ed4b275)BT\_GAP\_TX\_POWER\_INVALID

| #define BT\_GAP\_TX\_POWER\_INVALID   0x7f |
| --- |

`#include <[gap.h](gap_8h.md)>`

## [◆ ](#gac79626389f62bb7b3e5b5f6d3a5eaf2b)BT\_GAP\_US\_TO\_ADV\_INTERVAL

| #define BT\_GAP\_US\_TO\_ADV\_INTERVAL | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))((\_interval) / 625U))

Convert microseconds to advertising interval units (0.625 ms).

Value range of `_interval` is 20000 to 1024000

Note
:   If `_interval` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_US\_TO\_ADV\_INTERVAL(21000)](#gac79626389f62bb7b3e5b5f6d3a5eaf2b) will become 20625 microseconds

## [◆ ](#ga8905e22b1864021b77367c228b8bff48)BT\_GAP\_US\_TO\_CONN\_EVENT\_LEN

| #define BT\_GAP\_US\_TO\_CONN\_EVENT\_LEN | ( |  | *\_event\_len* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))((\_event\_len) / 625U))

Convert milliseconds to connection event length units (0.625).

Value range of `_event_len` is 0 to 40959375

Note
:   If `_event_len` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_US\_TO\_CONN\_EVENT\_LEN(21000)](#ga8905e22b1864021b77367c228b8bff48) will become 20625 milliseconds

## [◆ ](#gab12ba919a5a389b4c342d142d3a9ce6e)BT\_GAP\_US\_TO\_CONN\_INTERVAL

| #define BT\_GAP\_US\_TO\_CONN\_INTERVAL | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))((\_interval) / 1250U))

Convert microseconds to connection interval units (1.25 ms).

Value range of `_interval` is 7500 to 4000000

Note
:   If `_interval` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_US\_TO\_CONN\_INTERVAL(21000)](#gab12ba919a5a389b4c342d142d3a9ce6e) will become 20000 microseconds

## [◆ ](#ga317a60f9edb371fef180130282805539)BT\_GAP\_US\_TO\_CONN\_TIMEOUT

| #define BT\_GAP\_US\_TO\_CONN\_TIMEOUT | ( |  | *\_timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

([BT\_GAP\_MS\_TO\_CONN\_TIMEOUT](#ga24f79cacceeea262987f3cdaf2ef6bc3)((\_timeout) / [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)))

[BT\_GAP\_MS\_TO\_CONN\_TIMEOUT](#ga24f79cacceeea262987f3cdaf2ef6bc3)

#define BT\_GAP\_MS\_TO\_CONN\_TIMEOUT(\_timeout)

Convert milliseconds to connection supervision timeout units (10 ms).

**Definition** gap.h:1023

Convert microseconds to connection supervision timeout units (10 ms).

Value range of `_timeout` is 100000 to 32000000

Note
:   If `_timeout` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_MS\_TO\_CONN\_TIMEOUT(4005000)](#ga24f79cacceeea262987f3cdaf2ef6bc3) will become 4000000 microseconds

## [◆ ](#ga5a9da01507b4356c2ad6f8309257f2ce)BT\_GAP\_US\_TO\_PER\_ADV\_INTERVAL

| #define BT\_GAP\_US\_TO\_PER\_ADV\_INTERVAL | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))((\_interval) / 1250U))

Convert microseconds to periodic advertising interval units (1.25 ms).

Value range of `_interval` is 7500 to 81918750

Note
:   If `_interval` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_US\_TO\_PER\_ADV\_INTERVAL(11000)](#ga5a9da01507b4356c2ad6f8309257f2ce) will become 10000 microseconds

## [◆ ](#gaf33284a372b21e24c53deb5e3a6a91aa)BT\_GAP\_US\_TO\_PER\_ADV\_SYNC\_TIMEOUT

| #define BT\_GAP\_US\_TO\_PER\_ADV\_SYNC\_TIMEOUT | ( |  | *\_timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

([BT\_GAP\_MS\_TO\_PER\_ADV\_SYNC\_TIMEOUT](#ga242a6a4e3dd138073c01bc600c9642eb)((\_timeout) / [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)))

[BT\_GAP\_MS\_TO\_PER\_ADV\_SYNC\_TIMEOUT](#ga242a6a4e3dd138073c01bc600c9642eb)

#define BT\_GAP\_MS\_TO\_PER\_ADV\_SYNC\_TIMEOUT(\_timeout)

Convert milliseconds to periodic advertising sync timeout units (10 ms).

**Definition** gap.h:936

Convert microseconds to periodic advertising sync timeout units (10 ms).

Value range of `_timeout` is 100000 to 163840000

Note
:   If `_timeout` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_MS\_TO\_PER\_ADV\_SYNC\_TIMEOUT(4005000)](#ga242a6a4e3dd138073c01bc600c9642eb) will become 4000000 microseconds

## [◆ ](#gab65e489c4a799774f6511c6ce5b65ea2)BT\_GAP\_US\_TO\_SCAN\_INTERVAL

| #define BT\_GAP\_US\_TO\_SCAN\_INTERVAL | ( |  | *\_interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))((\_interval) / 625U))

Convert microseconds to scan interval units (0.625 ms).

Value range of `_interval` is 2500 to 40959375 if `CONFIG_BT_EXT_ADV` else 2500 to 10240000

Note
:   If `_interval` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_US\_TO\_SCAN\_INTERVAL(21000)](#gab65e489c4a799774f6511c6ce5b65ea2) will become 20625 microseconds

## [◆ ](#gaac5d0ec82d9730b793960c0470ac6342)BT\_GAP\_US\_TO\_SCAN\_WINDOW

| #define BT\_GAP\_US\_TO\_SCAN\_WINDOW | ( |  | *\_window* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))((\_window) / 625U))

Convert microseconds to scan window units (0.625 ms).

Value range of `_window` is 2500 to 40959375 if `CONFIG_BT_EXT_ADV` else 2500 to 10240000

Note
:   If `_window` is not a multiple of the unit, it will round down to nearest. For example [BT\_GAP\_US\_TO\_SCAN\_WINDOW(21000)](#gaac5d0ec82d9730b793960c0470ac6342) will become 20625 microseconds

## [◆ ](#ga13d9b4a24e2a8b58402bfb21f8b782c8)BT\_LE\_AD\_GENERAL

| #define BT\_LE\_AD\_GENERAL   0x02 |
| --- |

`#include <[gap.h](gap_8h.md)>`

General Discoverable.

## [◆ ](#ga36191ee000a2098fd679c398b31e0906)BT\_LE\_AD\_LIMITED

| #define BT\_LE\_AD\_LIMITED   0x01 |
| --- |

`#include <[gap.h](gap_8h.md)>`

Limited Discoverable.

## [◆ ](#gabf5725f481cb73cbd974f3653c904bc9)BT\_LE\_AD\_NO\_BREDR

| #define BT\_LE\_AD\_NO\_BREDR   0x04 |
| --- |

`#include <[gap.h](gap_8h.md)>`

BR/EDR not supported.

## [◆ ](#ga3c29ad99d6a6e020148590381ab08b17)BT\_LE\_SUPP\_FEAT\_16\_ENCODE

| #define BT\_LE\_SUPP\_FEAT\_16\_ENCODE | ( |  | *w64* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)(w64)

[BT\_BYTES\_LIST\_LE16](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)

#define BT\_BYTES\_LIST\_LE16(\_v)

Encode 16-bit value into array values in little-endian format.

**Definition** byteorder.h:36

Encode 2 least significant bytes of 64-bit LE Supported Features into 2 bytes long array of values in little-endian format.

Helper macro to encode 64-bit LE Supported Features value into advertising data. The macro encodes 3 least significant bytes into advertising data. Other 6 bytes are not encoded.

Example of how to encode the 0x000000DFF00DF00D into advertising data.

[BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)([BT\_DATA\_LE\_SUPPORTED\_FEATURES](#ga207bc1e5405a4fd3f39863a2cb304ebc), [BT\_LE\_SUPP\_FEAT\_16\_ENCODE](#ga3c29ad99d6a6e020148590381ab08b17)(0x000000DFF00DF00D))

[BT\_DATA\_LE\_SUPPORTED\_FEATURES](#ga207bc1e5405a4fd3f39863a2cb304ebc)

#define BT\_DATA\_LE\_SUPPORTED\_FEATURES

LE Supported Features.

**Definition** gap.h:77

[BT\_LE\_SUPP\_FEAT\_16\_ENCODE](#ga3c29ad99d6a6e020148590381ab08b17)

#define BT\_LE\_SUPP\_FEAT\_16\_ENCODE(w64)

Encode 2 least significant bytes of 64-bit LE Supported Features into 2 bytes long array of values in...

**Definition** gap.h:1162

[BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)

#define BT\_DATA\_BYTES(\_type, \_bytes...)

Helper to declare elements of bt\_data arrays.

**Definition** bluetooth.h:488

Parameters
:   | w64 | LE Supported Features value (64-bits) |
    | --- | --- |

Returns
:   The comma separated values for LE Supported Features value that may be used directly as an argument for [BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2 "BT_DATA_BYTES").

## [◆ ](#gab8739c92f8d50b796539a21027c3b6eb)BT\_LE\_SUPP\_FEAT\_24\_ENCODE

| #define BT\_LE\_SUPP\_FEAT\_24\_ENCODE | ( |  | *w64* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_LE24](group__bt__byteorder.md#ga68d63372c0b7e981d7ae715250c42261)(w64)

[BT\_BYTES\_LIST\_LE24](group__bt__byteorder.md#ga68d63372c0b7e981d7ae715250c42261)

#define BT\_BYTES\_LIST\_LE24(\_v)

Encode 24-bit value into array values in little-endian format.

**Definition** byteorder.h:50

Encode 3 least significant bytes of 64-bit LE Supported Features into 3 bytes long array of values in little-endian format.

Helper macro to encode 64-bit LE Supported Features value into advertising data. The macro encodes 3 least significant bytes into advertising data. Other 5 bytes are not encoded.

Example of how to encode the 0x000000DFF00DF00D into advertising data.

[BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)([BT\_DATA\_LE\_SUPPORTED\_FEATURES](#ga207bc1e5405a4fd3f39863a2cb304ebc), [BT\_LE\_SUPP\_FEAT\_24\_ENCODE](#gab8739c92f8d50b796539a21027c3b6eb)(0x000000DFF00DF00D))

[BT\_LE\_SUPP\_FEAT\_24\_ENCODE](#gab8739c92f8d50b796539a21027c3b6eb)

#define BT\_LE\_SUPP\_FEAT\_24\_ENCODE(w64)

Encode 3 least significant bytes of 64-bit LE Supported Features into 3 bytes long array of values in...

**Definition** gap.h:1141

Parameters
:   | w64 | LE Supported Features value (64-bits) |
    | --- | --- |

Returns
:   The comma separated values for LE Supported Features value that may be used directly as an argument for [BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2 "BT_DATA_BYTES").

## [◆ ](#ga7aa92098e33840ff02cb8c0435637094)BT\_LE\_SUPP\_FEAT\_32\_ENCODE

| #define BT\_LE\_SUPP\_FEAT\_32\_ENCODE | ( |  | *w64* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_LE32](group__bt__byteorder.md#ga0bf0275f0eea70eb5ae6002edeb1b812)(w64)

[BT\_BYTES\_LIST\_LE32](group__bt__byteorder.md#ga0bf0275f0eea70eb5ae6002edeb1b812)

#define BT\_BYTES\_LIST\_LE32(\_v)

Encode 32-bit value into array values in little-endian format.

**Definition** byteorder.h:64

Encode 4 least significant bytes of 64-bit LE Supported Features into 4 bytes long array of values in little-endian format.

Helper macro to encode 64-bit LE Supported Features value into advertising data. The macro encodes 4 least significant bytes into advertising data. Other 4 bytes are not encoded.

Example of how to encode the 0x000000DFF00DF00D into advertising data.

[BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)([BT\_DATA\_LE\_SUPPORTED\_FEATURES](#ga207bc1e5405a4fd3f39863a2cb304ebc), [BT\_LE\_SUPP\_FEAT\_32\_ENCODE](#ga7aa92098e33840ff02cb8c0435637094)(0x000000DFF00DF00D))

[BT\_LE\_SUPP\_FEAT\_32\_ENCODE](#ga7aa92098e33840ff02cb8c0435637094)

#define BT\_LE\_SUPP\_FEAT\_32\_ENCODE(w64)

Encode 4 least significant bytes of 64-bit LE Supported Features into 4 bytes long array of values in...

**Definition** gap.h:1120

Parameters
:   | w64 | LE Supported Features value (64-bits) |
    | --- | --- |

Returns
:   The comma separated values for LE Supported Features value that may be used directly as an argument for [BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2 "BT_DATA_BYTES").

## [◆ ](#ga799f6cb9dd02b9995ed76fbe97be3eb3)BT\_LE\_SUPP\_FEAT\_40\_ENCODE

| #define BT\_LE\_SUPP\_FEAT\_40\_ENCODE | ( |  | *w64* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

[BT\_BYTES\_LIST\_LE40](group__bt__byteorder.md#gadd963cf0f7898e5e143b5d2fd79839ef)(w64)

[BT\_BYTES\_LIST\_LE40](group__bt__byteorder.md#gadd963cf0f7898e5e143b5d2fd79839ef)

#define BT\_BYTES\_LIST\_LE40(\_v)

Encode 40-bit value into array values in little-endian format.

**Definition** byteorder.h:78

Encode 40 least significant bits of 64-bit LE Supported Features into array values in little-endian format.

Helper macro to encode 40 least significant bits of 64-bit LE Supported Features value into advertising data. The number of bits that are encoded is a number of LE Supported Features defined by BT 5.3 Core specification.

Example of how to encode the 0x000000DFF00DF00D into advertising data.

[BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)([BT\_DATA\_LE\_SUPPORTED\_FEATURES](#ga207bc1e5405a4fd3f39863a2cb304ebc), [BT\_LE\_SUPP\_FEAT\_40\_ENCODE](#ga799f6cb9dd02b9995ed76fbe97be3eb3)(0x000000DFF00DF00D))

[BT\_LE\_SUPP\_FEAT\_40\_ENCODE](#ga799f6cb9dd02b9995ed76fbe97be3eb3)

#define BT\_LE\_SUPP\_FEAT\_40\_ENCODE(w64)

Encode 40 least significant bits of 64-bit LE Supported Features into array values in little-endian f...

**Definition** gap.h:1100

Parameters
:   | w64 | LE Supported Features value (64-bits) |
    | --- | --- |

Returns
:   The comma separated values for LE Supported Features value that may be used directly as an argument for [BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2 "BT_DATA_BYTES").

## [◆ ](#ga8fac302925ac3ef8982630e6a0ec13af)BT\_LE\_SUPP\_FEAT\_8\_ENCODE

| #define BT\_LE\_SUPP\_FEAT\_8\_ENCODE | ( |  | *w64* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

(((w64) >> 0) & 0xFF)

Encode the least significant byte of 64-bit LE Supported Features into single byte long array.

Helper macro to encode 64-bit LE Supported Features value into advertising data. The macro encodes the least significant byte into advertising data. Other 7 bytes are not encoded.

Example of how to encode the 0x000000DFF00DF00D into advertising data.

[BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2)([BT\_DATA\_LE\_SUPPORTED\_FEATURES](#ga207bc1e5405a4fd3f39863a2cb304ebc), [BT\_LE\_SUPP\_FEAT\_8\_ENCODE](#ga8fac302925ac3ef8982630e6a0ec13af)(0x000000DFF00DF00D))

[BT\_LE\_SUPP\_FEAT\_8\_ENCODE](#ga8fac302925ac3ef8982630e6a0ec13af)

#define BT\_LE\_SUPP\_FEAT\_8\_ENCODE(w64)

Encode the least significant byte of 64-bit LE Supported Features into single byte long array.

**Definition** gap.h:1183

Parameters
:   | w64 | LE Supported Features value (64-bits) |
    | --- | --- |

Returns
:   The value of least significant byte of LE Supported Features value that may be used directly as an argument for [BT\_DATA\_BYTES](group__bt__gap.md#ga4c51f9b7a3a4e84abb4df3f1f714c6e2 "BT_DATA_BYTES").

## [◆ ](#ga86266eaf452dfaf82f097992e01397c8)BT\_LE\_SUPP\_FEAT\_VALIDATE

| #define BT\_LE\_SUPP\_FEAT\_VALIDATE | ( |  | *w64* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gap.h](gap_8h.md)>`

**Value:**

BUILD\_ASSERT(!((w64) & (~[BIT64\_MASK](group__sys-util.md#ga1a138896caafcb2429a6483ea7412d12)(40))), \

"RFU bit in LE Supported Features are not zeros.")

[BIT64\_MASK](group__sys-util.md#ga1a138896caafcb2429a6483ea7412d12)

#define BIT64\_MASK(n)

64-bit bit mask with bits 0 through n-1 (inclusive) set, or 0 if n is 0.

**Definition** util\_macro.h:74

Validate whether LE Supported Features value does not use bits that are reserved for future use.

Helper macro to check if `w64` has zeros as bits 40-63. The macro is compliant with BT 5.3 Core Specification where bits 0-40 has assigned values. In case of invalid value, build time error is reported.

## Enumeration Type Documentation

## [◆ ](#gafa0d8b6c50823ebb6bd38340efbb5a6b)anonymous enum

| anonymous enum |
| --- |

`#include <[gap.h](gap_8h.md)>`

Peripheral sleep clock accuracy (SCA) in ppm (parts per million).

| Enumerator | |
| --- | --- |
| BT\_GAP\_SCA\_UNKNOWN | Unknown. |
| BT\_GAP\_SCA\_251\_500 | 251 ppm to 500 ppm |
| BT\_GAP\_SCA\_151\_250 | 151 ppm to 250 ppm |
| BT\_GAP\_SCA\_101\_150 | 101 ppm to 150 ppm |
| BT\_GAP\_SCA\_76\_100 | 76 ppm to 100 ppm |
| BT\_GAP\_SCA\_51\_75 | 51 ppm to 75 ppm |
| BT\_GAP\_SCA\_31\_50 | 31 ppm to 50 ppm |
| BT\_GAP\_SCA\_21\_30 | 21 ppm to 30 ppm |
| BT\_GAP\_SCA\_0\_20 | 0 ppm to 20 ppm |

## [◆ ](#gab5a881b0cb1df3cf98de07a14e818c3e)anonymous enum

| anonymous enum |
| --- |

`#include <[gap.h](gap_8h.md)>`

Advertising PDU types.

| Enumerator | |
| --- | --- |
| BT\_GAP\_ADV\_TYPE\_ADV\_IND | Scannable and connectable advertising. |
| BT\_GAP\_ADV\_TYPE\_ADV\_DIRECT\_IND | Directed connectable advertising. |
| BT\_GAP\_ADV\_TYPE\_ADV\_SCAN\_IND | Non-connectable and scannable advertising. |
| BT\_GAP\_ADV\_TYPE\_ADV\_NONCONN\_IND | Non-connectable and non-scannable advertising. |
| BT\_GAP\_ADV\_TYPE\_SCAN\_RSP | Additional advertising data requested by an active scanner. |
| BT\_GAP\_ADV\_TYPE\_EXT\_ADV | Extended advertising, see advertising properties. |

## [◆ ](#gad30b9b6f60a1491bac4aa2c355072966)anonymous enum

| anonymous enum |
| --- |

`#include <[gap.h](gap_8h.md)>`

Constant Tone Extension (CTE) types.

| Enumerator | |
| --- | --- |
| BT\_GAP\_CTE\_AOA | Angle of Arrival. |
| BT\_GAP\_CTE\_AOD\_1US | Angle of Departure with 1 us slots. |
| BT\_GAP\_CTE\_AOD\_2US | Angle of Departure with 2 us slots. |
| BT\_GAP\_CTE\_NONE | No extensions. |

## [◆ ](#ga7dc8e89251aa575e28331e05775ba20b)anonymous enum

| anonymous enum |
| --- |

`#include <[gap.h](gap_8h.md)>`

LE PHY types.

| Enumerator | |
| --- | --- |
| BT\_GAP\_LE\_PHY\_NONE | Convenience macro for when no PHY is set. |
| BT\_GAP\_LE\_PHY\_1M | LE 1M PHY. |
| BT\_GAP\_LE\_PHY\_2M | LE 2M PHY. |
| BT\_GAP\_LE\_PHY\_CODED | LE Coded PHY, coding scheme not specified. |
| BT\_GAP\_LE\_PHY\_CODED\_S8 | LE Coded S=8 PHY.  Only used for advertising reports when Kconfig BT\_EXT\_ADV\_CODING\_SELECTION is enabled. |
| BT\_GAP\_LE\_PHY\_CODED\_S2 | LE Coded S=2 PHY.  Only used for advertising reports when Kconfig BT\_EXT\_ADV\_CODING\_SELECTION is enabled. |

## [◆ ](#gabf1a0417a549ec0a97263c2d990e711b)anonymous enum

| anonymous enum |
| --- |

`#include <[gap.h](gap_8h.md)>`

Advertising PDU properties.

| Enumerator | |
| --- | --- |
| BT\_GAP\_ADV\_PROP\_CONNECTABLE | Connectable advertising. |
| BT\_GAP\_ADV\_PROP\_SCANNABLE | Scannable advertising. |
| BT\_GAP\_ADV\_PROP\_DIRECTED | Directed advertising. |
| BT\_GAP\_ADV\_PROP\_SCAN\_RESPONSE | Additional advertising data requested by an active scanner. |
| BT\_GAP\_ADV\_PROP\_EXT\_ADV | Extended advertising. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
