---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gap_8h.html
original_path: doxygen/html/gap_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gap.h File Reference

Bluetooth Generic Access Profile defines and Assigned Numbers.
[More...](#details)

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/bluetooth/byteorder.h](bluetooth_2byteorder_8h_source.md)>`

[Go to the source code of this file.](gap_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BT\_GAP\_ADV\_MAX\_ADV\_DATA\_LEN](group__bt__gap__defines.md#ga39ab5040c9471631486da7dbebd9c36f)   31 |
|  | Maximum advertising data length. |
| #define | [BT\_GAP\_ADV\_MAX\_EXT\_ADV\_DATA\_LEN](group__bt__gap__defines.md#ga53af114e4925482739dc50dc84c2f641)   1650 |
|  | Maximum extended advertising data length. |
| #define | [BT\_GAP\_TX\_POWER\_INVALID](group__bt__gap__defines.md#ga61ccce819d75313cb2ee58309ed4b275)   0x7f |
| #define | [BT\_GAP\_RSSI\_INVALID](group__bt__gap__defines.md#ga64b5c5e429dadf1e875984f69cd399dc)   0x7f |
| #define | [BT\_GAP\_SID\_INVALID](group__bt__gap__defines.md#ga103af3e3142473be8897cd2647dca915)   0xff |
| #define | [BT\_GAP\_NO\_TIMEOUT](group__bt__gap__defines.md#ga9d6b2af6b96eab6356ded93c54301ef6)   0x0000 |
| #define | [BT\_GAP\_ADV\_HIGH\_DUTY\_CYCLE\_MAX\_TIMEOUT](group__bt__gap__defines.md#gabe483d4dd601b11ac3eea570c962b1ec)   128 |
| #define | [BT\_GAP\_DATA\_LEN\_DEFAULT](group__bt__gap__defines.md#ga90cfab7c375a8af6f9224a5635cbd023)   0x001b /\* 27 bytes \*/ |
|  | Default data length. |
| #define | [BT\_GAP\_DATA\_LEN\_MAX](group__bt__gap__defines.md#gacf5f35866d4677bd45c6e567886cabb9)   0x00fb /\* 251 bytes \*/ |
|  | Maximum data length. |
| #define | [BT\_GAP\_DATA\_TIME\_DEFAULT](group__bt__gap__defines.md#ga245249c0b6f8ccc419f2132f76362908)   0x0148 /\* 328 us \*/ |
|  | Default data time. |
| #define | [BT\_GAP\_DATA\_TIME\_MAX](group__bt__gap__defines.md#ga379b5d8d7f243abbc584c288cd01815f)   0x4290 /\* 17040 us \*/ |
|  | Maximum data time. |
| #define | [BT\_GAP\_SID\_MAX](group__bt__gap__defines.md#gafa6f803fe3ada07030fb1f2f725940c4)   0x0F |
|  | Maximum advertising set number. |
| #define | [BT\_GAP\_PER\_ADV\_MAX\_SKIP](group__bt__gap__defines.md#gaf92b229c47309a7a5e99047f28b860e7)   0x01F3 |
|  | Maximum number of consecutive periodic advertisement events that can be skipped after a successful receive. |
| #define | [BT\_GAP\_PER\_ADV\_MIN\_TIMEOUT](group__bt__gap__defines.md#ga17d8ae7e98f6a1dfead4f8ecb75f9645)   0x000A /\* 100 ms \*/ |
|  | Minimum Periodic Advertising Timeout (N \* 10 ms). |
| #define | [BT\_GAP\_PER\_ADV\_MAX\_TIMEOUT](group__bt__gap__defines.md#gad6674199f615fa6ecaeb1fe9d099e04c)   0x4000 /\* 163.84 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
|  | Maximum Periodic Advertising Timeout (N \* 10 ms). |
| #define | [BT\_GAP\_PER\_ADV\_MIN\_INTERVAL](group__bt__gap__defines.md#ga07e21fdeb8a0a0b967690898bef2f7aa)   0x0006 /\* 7.5 ms \*/ |
|  | Minimum Periodic Advertising Interval (N \* 1.25 ms). |
| #define | [BT\_GAP\_PER\_ADV\_MAX\_INTERVAL](group__bt__gap__defines.md#ga80bf3f1fb6f34a2c4363687149c365bd)   0xFFFF /\* 81.91875 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
|  | Maximum Periodic Advertising Interval (N \* 1.25 ms). |
| #define | [BT\_GAP\_PER\_ADV\_INTERVAL\_TO\_MS](group__bt__gap__defines.md#ga450799e76dd71888ed3a045f68f58908)(interval) |
|  | Convert periodic advertising interval (N \* 1.25 ms) to milliseconds. |
| #define | [BT\_LE\_SUPP\_FEAT\_40\_ENCODE](group__bt__gap__defines.md#ga799f6cb9dd02b9995ed76fbe97be3eb3)(w64) |
|  | Encode 40 least significant bits of 64-bit LE Supported Features into array values in little-endian format. |
| #define | [BT\_LE\_SUPP\_FEAT\_32\_ENCODE](group__bt__gap__defines.md#ga7aa92098e33840ff02cb8c0435637094)(w64) |
|  | Encode 4 least significant bytes of 64-bit LE Supported Features into 4 bytes long array of values in little-endian format. |
| #define | [BT\_LE\_SUPP\_FEAT\_24\_ENCODE](group__bt__gap__defines.md#gab8739c92f8d50b796539a21027c3b6eb)(w64) |
|  | Encode 3 least significant bytes of 64-bit LE Supported Features into 3 bytes long array of values in little-endian format. |
| #define | [BT\_LE\_SUPP\_FEAT\_16\_ENCODE](group__bt__gap__defines.md#ga3c29ad99d6a6e020148590381ab08b17)(w64) |
|  | Encode 2 least significant bytes of 64-bit LE Supported Features into 2 bytes long array of values in little-endian format. |
| #define | [BT\_LE\_SUPP\_FEAT\_8\_ENCODE](group__bt__gap__defines.md#ga8fac302925ac3ef8982630e6a0ec13af)(w64) |
|  | Encode the least significant byte of 64-bit LE Supported Features into single byte long array. |
| #define | [BT\_LE\_SUPP\_FEAT\_VALIDATE](group__bt__gap__defines.md#ga86266eaf452dfaf82f097992e01397c8)(w64) |
|  | Validate whether LE Supported Features value does not use bits that are reserved for future use. |
| Company Identifiers (see Bluetooth Assigned Numbers) | |
| #define | [BT\_COMP\_ID\_LF](group__bt__gap__defines.md#ga6bbf21c05f24d2c2c710be9bcf05af5f)   0x05f1 |
|  | The Linux Foundation. |
| EIR/AD data type definitions | |
| #define | [BT\_DATA\_FLAGS](group__bt__gap__defines.md#ga396b92d418fcb8263895e420b9df3df2)   0x01 |
|  | AD flags. |
| #define | [BT\_DATA\_UUID16\_SOME](group__bt__gap__defines.md#ga6c725bd3d31c159a4d046561dbca38ba)   0x02 |
|  | 16-bit UUID, more available |
| #define | [BT\_DATA\_UUID16\_ALL](group__bt__gap__defines.md#ga0d55063b9ad321b5c530a0012337df8a)   0x03 |
|  | 16-bit UUID, all listed |
| #define | [BT\_DATA\_UUID32\_SOME](group__bt__gap__defines.md#ga2486a6748490ba57e442ca15223482ef)   0x04 |
|  | 32-bit UUID, more available |
| #define | [BT\_DATA\_UUID32\_ALL](group__bt__gap__defines.md#gaaf825c3e4686e572a35ddd46ee6fe2e8)   0x05 |
|  | 32-bit UUID, all listed |
| #define | [BT\_DATA\_UUID128\_SOME](group__bt__gap__defines.md#ga5c4f7fc1b93c611e95f735330fba243b)   0x06 |
|  | 128-bit UUID, more available |
| #define | [BT\_DATA\_UUID128\_ALL](group__bt__gap__defines.md#gaafcade3dbbcb4005f4590e994f91884b)   0x07 |
|  | 128-bit UUID, all listed |
| #define | [BT\_DATA\_NAME\_SHORTENED](group__bt__gap__defines.md#gafc509b33a8d2dd9124f6893eadbe1662)   0x08 |
|  | Shortened name. |
| #define | [BT\_DATA\_NAME\_COMPLETE](group__bt__gap__defines.md#gab94a7c5689d296acf47f976538056ab5)   0x09 |
|  | Complete name. |
| #define | [BT\_DATA\_TX\_POWER](group__bt__gap__defines.md#ga4988c17578c4cf76fcdd9d44e1c931b0)   0x0a |
|  | Tx Power. |
| #define | [BT\_DATA\_DEVICE\_CLASS](group__bt__gap__defines.md#ga152c3028a2befcc4caf40aa6590c80b7)   0x0d |
|  | Class of Device. |
| #define | [BT\_DATA\_SIMPLE\_PAIRING\_HASH\_C192](group__bt__gap__defines.md#ga053c8bb0aedd01b3dd3f6154f4b49999)   0x0e |
|  | Simple Pairing Hash C-192. |
| #define | [BT\_DATA\_SIMPLE\_PAIRING\_RAND\_C192](group__bt__gap__defines.md#ga280f1f96c5204960fe034c9ddaf194ec)   0x0f |
|  | Simple Pairing Randomizer R-192. |
| #define | [BT\_DATA\_DEVICE\_ID](group__bt__gap__defines.md#gac9402c597e5b4497f4bcd22d5177cc23)   0x10 |
|  | Device ID (Profile). |
| #define | [BT\_DATA\_SM\_TK\_VALUE](group__bt__gap__defines.md#ga5014acb2fe8e76b855b55bf98abe6d05)   0x10 |
|  | Security Manager TK Value. |
| #define | [BT\_DATA\_SM\_OOB\_FLAGS](group__bt__gap__defines.md#gaa12c742d1c955036aa3f55e84df69890)   0x11 |
|  | Security Manager OOB Flags. |
| #define | [BT\_DATA\_PERIPHERAL\_INT\_RANGE](group__bt__gap__defines.md#gabcf872eafc60c21287f6be63174dc7c8)   0x12 |
|  | Peripheral Connection Interval Range. |
| #define | [BT\_DATA\_SOLICIT16](group__bt__gap__defines.md#ga2ad4d2ec2ff29c0aad5159de12d3f741)   0x14 |
|  | Solicit UUIDs, 16-bit. |
| #define | [BT\_DATA\_SOLICIT128](group__bt__gap__defines.md#ga217df3f70846e86fa09e5605d5acd291)   0x15 |
|  | Solicit UUIDs, 128-bit. |
| #define | [BT\_DATA\_SVC\_DATA16](group__bt__gap__defines.md#ga76990dda919688b369decaf9d3606b32)   0x16 |
|  | Service data, 16-bit UUID. |
| #define | [BT\_DATA\_PUB\_TARGET\_ADDR](group__bt__gap__defines.md#gacb867f0436d38c5c80e3426ca6247a46)   0x17 |
|  | Public Target Address. |
| #define | [BT\_DATA\_RAND\_TARGET\_ADDR](group__bt__gap__defines.md#ga3d9097d8f53213ccafc152c51ad6fdbd)   0x18 |
|  | Random Target Address. |
| #define | [BT\_DATA\_GAP\_APPEARANCE](group__bt__gap__defines.md#ga67fc721da05758b7d7a36aecaa035fac)   0x19 |
|  | GAP appearance. |
| #define | [BT\_DATA\_ADV\_INT](group__bt__gap__defines.md#ga6fd8c0f32bbcb97aaafee51fda0b601e)   0x1a |
|  | Advertising Interval. |
| #define | [BT\_DATA\_LE\_BT\_DEVICE\_ADDRESS](group__bt__gap__defines.md#gad9e8a273239fa160a6b2797ef5563a94)   0x1b |
|  | LE Bluetooth Device Address. |
| #define | [BT\_DATA\_LE\_ROLE](group__bt__gap__defines.md#ga255c7cb16eb24b95fa0f531fc4574273)   0x1c |
|  | LE Role. |
| #define | [BT\_DATA\_SIMPLE\_PAIRING\_HASH](group__bt__gap__defines.md#ga324f91521eacd1e9d579c9d52d02eb06)   0x1d |
|  | Simple Pairing Hash C256. |
| #define | [BT\_DATA\_SIMPLE\_PAIRING\_RAND](group__bt__gap__defines.md#gad7e7dd2d3a972e53f9e5e80627bd07e6)   0x1e |
|  | Simple Pairing Randomizer R256. |
| #define | [BT\_DATA\_SOLICIT32](group__bt__gap__defines.md#ga76e7e8971ed841b87fda08793a00b14f)   0x1f |
|  | Solicit UUIDs, 32-bit. |
| #define | [BT\_DATA\_SVC\_DATA32](group__bt__gap__defines.md#ga7d411a723ff2f038c3b7a1e09c88cb3d)   0x20 |
|  | Service data, 32-bit UUID. |
| #define | [BT\_DATA\_SVC\_DATA128](group__bt__gap__defines.md#gaa53847910515d9488b490f17a4fdf0d1)   0x21 |
|  | Service data, 128-bit UUID. |
| #define | [BT\_DATA\_LE\_SC\_CONFIRM\_VALUE](group__bt__gap__defines.md#ga883dda02c157f0de8157b1c5f66aafd0)   0x22 |
|  | LE SC Confirmation Value. |
| #define | [BT\_DATA\_LE\_SC\_RANDOM\_VALUE](group__bt__gap__defines.md#gacbc31c67684e3c68481501cf89f9ec68)   0x23 |
|  | LE SC Random Value. |
| #define | [BT\_DATA\_URI](group__bt__gap__defines.md#ga3c6a5903cc4a46aaf0b30a0de0179403)   0x24 |
|  | URI. |
| #define | [BT\_DATA\_INDOOR\_POS](group__bt__gap__defines.md#ga0f29f9d8f5a336af430f0a603e87e995)   0x25 |
|  | Indoor Positioning. |
| #define | [BT\_DATA\_TRANS\_DISCOVER\_DATA](group__bt__gap__defines.md#ga8e9ccc669ee545152b2d9b3120692d55)   0x26 |
|  | Transport Discovery Data. |
| #define | [BT\_DATA\_LE\_SUPPORTED\_FEATURES](group__bt__gap__defines.md#ga207bc1e5405a4fd3f39863a2cb304ebc)   0x27 |
|  | LE Supported Features. |
| #define | [BT\_DATA\_CHANNEL\_MAP\_UPDATE\_IND](group__bt__gap__defines.md#gae3eb96c0f127b6417d7cad288faaaceb)   0x28 |
|  | Channel Map Update Indication. |
| #define | [BT\_DATA\_MESH\_PROV](group__bt__gap__defines.md#gafc5984d58b0b54ee824dd83bc78dfbe9)   0x29 |
|  | Mesh Provisioning PDU. |
| #define | [BT\_DATA\_MESH\_MESSAGE](group__bt__gap__defines.md#gac351c67ab58520b796fa713602d9f602)   0x2a |
|  | Mesh Networking PDU. |
| #define | [BT\_DATA\_MESH\_BEACON](group__bt__gap__defines.md#ga59cc479be1f6c61a4a47aa6f479fe67a)   0x2b |
|  | Mesh Beacon. |
| #define | [BT\_DATA\_BIG\_INFO](group__bt__gap__defines.md#ga16feb94cd09c04d020450f61646f5486)   0x2c |
|  | BIGInfo. |
| #define | [BT\_DATA\_BROADCAST\_CODE](group__bt__gap__defines.md#ga72d2e55819db593a6db77579ebfe1e9d)   0x2d |
|  | Broadcast Code. |
| #define | [BT\_DATA\_CSIS\_RSI](group__bt__gap__defines.md#ga122da4184d606ae140f8a311aaebeedd)   0x2e |
|  | CSIS Random Set ID type. |
| #define | [BT\_DATA\_ADV\_INT\_LONG](group__bt__gap__defines.md#gad4ac2e0de80dddcacc4ca6d25765eebd)   0x2f |
|  | Advertising Interval long. |
| #define | [BT\_DATA\_BROADCAST\_NAME](group__bt__gap__defines.md#ga7d781791bc85fe3c7ea839ff617ee6e7)   0x30 |
|  | Broadcast Name. |
| #define | [BT\_DATA\_ENCRYPTED\_AD\_DATA](group__bt__gap__defines.md#ga41d5c898144e89b6035f92ff506f38a3)   0x31 |
|  | Encrypted Advertising Data. |
| #define | [BT\_DATA\_PAWR\_TIMING\_INFO](group__bt__gap__defines.md#ga14a8b1cf9d6c1c9749443a012731d39c)   0x32 |
|  | Periodic Advertising Response Timing Info. |
| #define | [BT\_DATA\_ESL](group__bt__gap__defines.md#ga90c7a1175148f3a56b04dc0b29525a4d)   0x34 |
|  | Electronic Shelf Label Profile. |
| #define | [BT\_DATA\_3D\_INFO](group__bt__gap__defines.md#gaecab0c77f9f912c16c264e7eaf2e4707)   0x3D |
|  | 3D Information Data |
| #define | [BT\_DATA\_MANUFACTURER\_DATA](group__bt__gap__defines.md#ga63b846807bff632b1cdd49b1e46e63b4)   0xff |
|  | Manufacturer Specific Data. |
| #define | [BT\_LE\_AD\_LIMITED](group__bt__gap__defines.md#ga36191ee000a2098fd679c398b31e0906)   0x01 |
|  | Limited Discoverable. |
| #define | [BT\_LE\_AD\_GENERAL](group__bt__gap__defines.md#ga13d9b4a24e2a8b58402bfb21f8b782c8)   0x02 |
|  | General Discoverable. |
| #define | [BT\_LE\_AD\_NO\_BREDR](group__bt__gap__defines.md#gabf5725f481cb73cbd974f3653c904bc9)   0x04 |
|  | BR/EDR not supported. |
| Appearance Values | |
| Last Modified on 2023-01-05 | |
| #define | [BT\_APPEARANCE\_UNKNOWN](group__bt__gap__defines.md#gafd1c9ca638a362a01897792e5a00a0c5)   0x0000 |
|  | Generic Unknown. |
| #define | [BT\_APPEARANCE\_GENERIC\_PHONE](group__bt__gap__defines.md#gae7061e78f960563af6e1b3dea71655a9)   0x0040 |
|  | Generic Phone. |
| #define | [BT\_APPEARANCE\_GENERIC\_COMPUTER](group__bt__gap__defines.md#ga6b74ad86efc0e9a745f2c9e64079b1cd)   0x0080 |
|  | Generic Computer. |
| #define | [BT\_APPEARANCE\_COMPUTER\_DESKTOP\_WORKSTATION](group__bt__gap__defines.md#ga1aa0565ca7e00e3a1aa8968e0a7f1bef)   0x0081 |
|  | Desktop Workstation. |
| #define | [BT\_APPEARANCE\_COMPUTER\_SERVER\_CLASS](group__bt__gap__defines.md#gab71a3c3f836561ac7bd8e52f5e01c769)   0x0082 |
|  | Server-class Computer. |
| #define | [BT\_APPEARANCE\_COMPUTER\_LAPTOP](group__bt__gap__defines.md#ga55ce2ad96a153ed6bdfd841276145c28)   0x0083 |
|  | Laptop. |
| #define | [BT\_APPEARANCE\_COMPUTER\_HANDHELD\_PCPDA](group__bt__gap__defines.md#gab64312ea16f03c5998db4429b194b8b0)   0x0084 |
|  | Handheld PC/PDA (clamshell). |
| #define | [BT\_APPEARANCE\_COMPUTER\_PALMSIZE\_PCPDA](group__bt__gap__defines.md#ga9340ed60911fc7c5aab7d317b6925c10)   0x0085 |
|  | Palm­size PC/PDA. |
| #define | [BT\_APPEARANCE\_COMPUTER\_WEARABLE\_COMPUTER](group__bt__gap__defines.md#ga7c6667ba4c68dec380a548ba9530c110)   0x0086 |
|  | Wearable computer (watch size). |
| #define | [BT\_APPEARANCE\_COMPUTER\_TABLET](group__bt__gap__defines.md#ga11bc881cb5f88956edbf2bb2fe5b358c)   0x0087 |
|  | Tablet. |
| #define | [BT\_APPEARANCE\_COMPUTER\_DOCKING\_STATION](group__bt__gap__defines.md#ga36187d2651d08c4b3e17c36565a2d3c9)   0x0088 |
|  | Docking Station. |
| #define | [BT\_APPEARANCE\_COMPUTER\_ALL\_IN\_ONE](group__bt__gap__defines.md#gaa4d962ad8661c28ed48f5cf8cd75ad6e)   0x0089 |
|  | All in One. |
| #define | [BT\_APPEARANCE\_COMPUTER\_BLADE\_SERVER](group__bt__gap__defines.md#ga53e8eff26f2020b1fc89b21684e54698)   0x008A |
|  | Blade Server. |
| #define | [BT\_APPEARANCE\_COMPUTER\_CONVERTIBLE](group__bt__gap__defines.md#ga073dca362cabfd2a07cdc1cb787a0f58)   0x008B |
|  | Convertible. |
| #define | [BT\_APPEARANCE\_COMPUTER\_DETACHABLE](group__bt__gap__defines.md#ga8f35f76cc9de4170006669d6e9e7d72a)   0x008C |
|  | Detachable. |
| #define | [BT\_APPEARANCE\_COMPUTER\_IOT\_GATEWAY](group__bt__gap__defines.md#ga6ae353795476853bc3be2196ed220aa7)   0x008D |
|  | IoT Gateway. |
| #define | [BT\_APPEARANCE\_COMPUTER\_MINI\_PC](group__bt__gap__defines.md#ga3c47c11f56eabec15e960662c64f6fcb)   0x008E |
|  | Mini PC. |
| #define | [BT\_APPEARANCE\_COMPUTER\_STICK\_PC](group__bt__gap__defines.md#gabb53daf3eb4ac9ba0cbb1614056ee214)   0x008F |
|  | Stick PC. |
| #define | [BT\_APPEARANCE\_GENERIC\_WATCH](group__bt__gap__defines.md#ga0c512fd6aa5d35e78f02176073f5f121)   0x00C0 |
|  | Generic Watch. |
| #define | [BT\_APPEARANCE\_SPORTS\_WATCH](group__bt__gap__defines.md#gaca9cc93d768145ec3d87b88740954b50)   0x00C1 |
|  | Sports Watch. |
| #define | [BT\_APPEARANCE\_SMARTWATCH](group__bt__gap__defines.md#gaa5662d4a544b034243faa45245a9728b)   0x00C2 |
|  | Smartwatch. |
| #define | [BT\_APPEARANCE\_GENERIC\_CLOCK](group__bt__gap__defines.md#ga100d26d6b9e9a3af925d64c0b006c6bd)   0x0100 |
|  | Generic Clock. |
| #define | [BT\_APPEARANCE\_GENERIC\_DISPLAY](group__bt__gap__defines.md#ga0a21cb58861a48875002af38ee82ac08)   0x0140 |
|  | Generic Display. |
| #define | [BT\_APPEARANCE\_GENERIC\_REMOTE](group__bt__gap__defines.md#ga0b47897768b27d26b8687dd2ab28703b)   0x0180 |
|  | Generic Remote Control. |
| #define | [BT\_APPEARANCE\_GENERIC\_EYEGLASSES](group__bt__gap__defines.md#gab2b5f6385662519a2ece8fb654a6194b)   0x01C0 |
|  | Generic Eye-glasses. |
| #define | [BT\_APPEARANCE\_GENERIC\_TAG](group__bt__gap__defines.md#gaca6d810977e6da1a3174ee2b6b36662d)   0x0200 |
|  | Generic Tag. |
| #define | [BT\_APPEARANCE\_GENERIC\_KEYRING](group__bt__gap__defines.md#gaf73b11c4dbf366a854b4c68e802e3c1c)   0x0240 |
|  | Generic Keyring. |
| #define | [BT\_APPEARANCE\_GENERIC\_MEDIA\_PLAYER](group__bt__gap__defines.md#ga17e94209c0c96b5ca039b1613de0d05e)   0x0280 |
|  | Generic Media Player. |
| #define | [BT\_APPEARANCE\_GENERIC\_BARCODE\_SCANNER](group__bt__gap__defines.md#gadca19a01611ca83e18156bb540dd96c1)   0x02C0 |
|  | Generic Barcode Scanner. |
| #define | [BT\_APPEARANCE\_GENERIC\_THERMOMETER](group__bt__gap__defines.md#ga2e0fde88d83e1f4533d69c8dc472255f)   0x0300 |
|  | Generic Thermometer. |
| #define | [BT\_APPEARANCE\_THERMOMETER\_EAR](group__bt__gap__defines.md#ga54283061a207491dcfced899c0fc3008)   0x0301 |
|  | Ear Thermometer. |
| #define | [BT\_APPEARANCE\_GENERIC\_HEART\_RATE](group__bt__gap__defines.md#gac5bdf195b81215932848151d765e84d6)   0x0340 |
|  | Generic Heart Rate Sensor. |
| #define | [BT\_APPEARANCE\_HEART\_RATE\_BELT](group__bt__gap__defines.md#ga895f6570a09f3eee8d821eca57cdeb03)   0x0341 |
|  | Heart Rate Belt. |
| #define | [BT\_APPEARANCE\_GENERIC\_BLOOD\_PRESSURE](group__bt__gap__defines.md#ga3ab7a9595e00208a9e6a56dca99b56c2)   0x0380 |
|  | Generic Blood Pressure. |
| #define | [BT\_APPEARANCE\_BLOOD\_PRESSURE\_ARM](group__bt__gap__defines.md#ga55c3e67d27c8fd8ae06880ccdd9259ce)   0x0381 |
|  | Arm Blood Pressure. |
| #define | [BT\_APPEARANCE\_BLOOD\_PRESSURE\_WRIST](group__bt__gap__defines.md#ga89684ca0544a400293b663cdf0063cfa)   0x0382 |
|  | Wrist Blood Pressure. |
| #define | [BT\_APPEARANCE\_GENERIC\_HID](group__bt__gap__defines.md#gaf2050baedf0863ec37177dd2ef872d39)   0x03C0 |
|  | Generic Human Interface Device. |
| #define | [BT\_APPEARANCE\_HID\_KEYBOARD](group__bt__gap__defines.md#gaa74af272423a80d5489ed8cf6c3ee66c)   0x03C1 |
|  | Keyboard. |
| #define | [BT\_APPEARANCE\_HID\_MOUSE](group__bt__gap__defines.md#ga3b6ba8ffe424db08583186c448e37149)   0x03C2 |
|  | Mouse. |
| #define | [BT\_APPEARANCE\_HID\_JOYSTICK](group__bt__gap__defines.md#ga2f9f15df2260a1307f5142f37437bf0c)   0x03C3 |
|  | Joystick. |
| #define | [BT\_APPEARANCE\_HID\_GAMEPAD](group__bt__gap__defines.md#ga770336524e74d106cb18354f9dbfad76)   0x03C4 |
|  | Gamepad. |
| #define | [BT\_APPEARANCE\_HID\_DIGITIZER\_TABLET](group__bt__gap__defines.md#gacac11dcb96ab60963a1118e171a731de)   0x03C5 |
|  | Digitizer Tablet. |
| #define | [BT\_APPEARANCE\_HID\_CARD\_READER](group__bt__gap__defines.md#gaa03c3b4d7ea8211748316146afab8bd4)   0x03C6 |
|  | Card Reader. |
| #define | [BT\_APPEARANCE\_HID\_DIGITAL\_PEN](group__bt__gap__defines.md#ga002a1d7965b23ec62c8a196f4e5452d9)   0x03C7 |
|  | Digital Pen. |
| #define | [BT\_APPEARANCE\_HID\_BARCODE\_SCANNER](group__bt__gap__defines.md#gaf88f83afd454fe88dd7146e10ef6d35e)   0x03C8 |
|  | Barcode Scanner. |
| #define | [BT\_APPEARANCE\_HID\_TOUCHPAD](group__bt__gap__defines.md#gaee207f9434bce7d0f7e096bf3b37a01c)   0x03C9 |
|  | Touchpad. |
| #define | [BT\_APPEARANCE\_HID\_PRESENTATION\_REMOTE](group__bt__gap__defines.md#gae415dd9e8d620dfd1981719f4ed2d796)   0x03CA |
|  | Presentation Remote. |
| #define | [BT\_APPEARANCE\_GENERIC\_GLUCOSE](group__bt__gap__defines.md#ga209645f7445873beb50c388cc82aff2a)   0x0400 |
|  | Generic Glucose Meter. |
| #define | [BT\_APPEARANCE\_GENERIC\_WALKING](group__bt__gap__defines.md#ga9cf19d97db0c4c5b8473b72809b51d42)   0x0440 |
|  | Generic Running Walking Sensor. |
| #define | [BT\_APPEARANCE\_WALKING\_IN\_SHOE](group__bt__gap__defines.md#gad748f5dc2e0622353d6159c3a3e4241b)   0x0441 |
|  | In-Shoe Running Walking Sensor. |
| #define | [BT\_APPEARANCE\_WALKING\_ON\_SHOE](group__bt__gap__defines.md#ga0a4541459ba8b41a3938c5b8d35b1c8c)   0x0442 |
|  | On-Shoe Running Walking Sensor. |
| #define | [BT\_APPEARANCE\_WALKING\_ON\_HIP](group__bt__gap__defines.md#gad211a7e2f11dc7effe3ba28e8c4f7092)   0x0443 |
|  | On-Hip Running Walking Sensor. |
| #define | [BT\_APPEARANCE\_GENERIC\_CYCLING](group__bt__gap__defines.md#ga7a0463b9b0df37bce80cada38b10ee54)   0x0480 |
|  | Generic Cycling. |
| #define | [BT\_APPEARANCE\_CYCLING\_COMPUTER](group__bt__gap__defines.md#ga3e81dce23c3d005a9b48ff83c7b8f896)   0x0481 |
|  | Cycling Computer. |
| #define | [BT\_APPEARANCE\_CYCLING\_SPEED](group__bt__gap__defines.md#ga16fb08fa70272252ab6b2d3a5aec485a)   0x0482 |
|  | Speed Sensor. |
| #define | [BT\_APPEARANCE\_CYCLING\_CADENCE](group__bt__gap__defines.md#ga71dc370aad015e88fce7c3e758c647ed)   0x0483 |
|  | Cadence Sensor. |
| #define | [BT\_APPEARANCE\_CYCLING\_POWER](group__bt__gap__defines.md#ga02fd9566d9b932aeaa1163d312fbc4d8)   0x0484 |
|  | Power Sensor. |
| #define | [BT\_APPEARANCE\_CYCLING\_SPEED\_CADENCE](group__bt__gap__defines.md#ga48d8f2a285795785f8f51ce220d46371)   0x0485 |
|  | Speed and Cadence Sensor. |
| #define | [BT\_APPEARANCE\_GENERIC\_CONTROL\_DEVICE](group__bt__gap__defines.md#ga5e16df5eefcae8556dfc387135e2b1b6)   0x04C0 |
|  | Generic Control Device. |
| #define | [BT\_APPEARANCE\_CONTROL\_SWITCH](group__bt__gap__defines.md#gac53247d00e3da69595274e0b94fa670f)   0x04C1 |
|  | Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_MULTI\_SWITCH](group__bt__gap__defines.md#gad30c40df58e160128893e545a11ab44c)   0x04C2 |
|  | Multi-switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_BUTTON](group__bt__gap__defines.md#ga52dfd2858663b7ab624f0c4b08cee7dc)   0x04C3 |
|  | Button. |
| #define | [BT\_APPEARANCE\_CONTROL\_SLIDER](group__bt__gap__defines.md#gaa849d890c000defcaf29893296c86cc5)   0x04C4 |
|  | Slider. |
| #define | [BT\_APPEARANCE\_CONTROL\_ROTARY\_SWITCH](group__bt__gap__defines.md#ga946b6a8bb49bf0b5cd3ded93ee8dfe89)   0x04C5 |
|  | Rotary Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_TOUCH\_PANEL](group__bt__gap__defines.md#ga4d5763288557e7b7f6da0f3e9831171d)   0x04C6 |
|  | Touch Panel. |
| #define | [BT\_APPEARANCE\_CONTROL\_SINGLE\_SWITCH](group__bt__gap__defines.md#ga979ca0f4febeaa55daec07e2b3b0179e)   0x04C7 |
|  | Single Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_DOUBLE\_SWITCH](group__bt__gap__defines.md#gac1c80dbb8aaa327b6125bf632692c3be)   0x04C8 |
|  | Double Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_TRIPLE\_SWITCH](group__bt__gap__defines.md#gaa532fd1bd67c2c5b72822704a62df143)   0x04C9 |
|  | Triple Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_BATTERY\_SWITCH](group__bt__gap__defines.md#gaea669671a53b3df5b1aa4c43e5bde9b9)   0x04CA |
|  | Battery Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_ENERGY\_HARVESTING\_SWITCH](group__bt__gap__defines.md#gadec2907a822e302d5027f162ef9ce4b6)   0x04CB |
|  | Energy Harvesting Switch. |
| #define | [BT\_APPEARANCE\_CONTROL\_PUSH\_BUTTON](group__bt__gap__defines.md#ga9bb358864e1388cc00502b5586ec581f)   0x04CC |
|  | Push Button. |
| #define | [BT\_APPEARANCE\_GENERIC\_NETWORK\_DEVICE](group__bt__gap__defines.md#gac4727ec720344ece687256ac517800e7)   0x0500 |
|  | Generic Network Device. |
| #define | [BT\_APPEARANCE\_NETWORK\_ACCESS\_POINT](group__bt__gap__defines.md#ga265ba959769d56f42ff621a20e193aba)   0x0501 |
|  | Access Point. |
| #define | [BT\_APPEARANCE\_NETWORK\_MESH\_DEVICE](group__bt__gap__defines.md#gadcc3d795579a731ae03ade14d5193408)   0x0502 |
|  | Mesh Device. |
| #define | [BT\_APPEARANCE\_NETWORK\_MESH\_PROXY](group__bt__gap__defines.md#gad4c5f5840a8caba73d55b0138e506bd0)   0x0503 |
|  | Mesh Network Proxy. |
| #define | [BT\_APPEARANCE\_GENERIC\_SENSOR](group__bt__gap__defines.md#gab3241fe012482e716c3f18e2962ca15d)   0x0540 |
|  | Generic Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_MOTION](group__bt__gap__defines.md#gab49b84183136e9b65ba2e1f5490a79ed)   0x0541 |
|  | Motion Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_AIR\_QUALITY](group__bt__gap__defines.md#gaacb0779499ad4aaa83f0b6303460caf8)   0x0542 |
|  | Air quality Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_TEMPERATURE](group__bt__gap__defines.md#ga5e072a902bf145dc2b00dbd1c8a64b52)   0x0543 |
|  | Temperature Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_HUMIDITY](group__bt__gap__defines.md#ga2deff206602e1e0784af9456ef8abd5b)   0x0544 |
|  | Humidity Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_LEAK](group__bt__gap__defines.md#ga2cbac5e931080f1f5cb3c9bb4c73e9d8)   0x0545 |
|  | Leak Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_SMOKE](group__bt__gap__defines.md#gaeedc0612f8ca171aec061cf02ee907e4)   0x0546 |
|  | Smoke Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_OCCUPANCY](group__bt__gap__defines.md#ga8e8b7834c82c42a0076300aca20c2d35)   0x0547 |
|  | Occupancy Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_CONTACT](group__bt__gap__defines.md#gac71e281cf1b8d1b6535623ec34c7d63f)   0x0548 |
|  | Contact Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_CARBON\_MONOXIDE](group__bt__gap__defines.md#ga0e60b365f871c17c0015ffcf8bc1646e)   0x0549 |
|  | Carbon Monoxide Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_CARBON\_DIOXIDE](group__bt__gap__defines.md#ga34ed8c9aefe34d5030209f073c9ecd24)   0x054A |
|  | Carbon Dioxide Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_AMBIENT\_LIGHT](group__bt__gap__defines.md#ga622508f9b051ed0320700b01967f6446)   0x054B |
|  | Ambient Light Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_ENERGY](group__bt__gap__defines.md#gaca0cfcd560fa4133c0bc62a61d2874c7)   0x054C |
|  | Energy Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_COLOR\_LIGHT](group__bt__gap__defines.md#ga8106142ddb6445e7462137e032e50854)   0x054D |
|  | Color Light Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_RAIN](group__bt__gap__defines.md#ga380da83e3a69de3fd5091cdc89f7fcbc)   0x054E |
|  | Rain Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_FIRE](group__bt__gap__defines.md#ga425115e6c251a9c493c98d79f659077d)   0x054F |
|  | Fire Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_WIND](group__bt__gap__defines.md#gaa710c0666d8b5bf1e1230672cbbf55fa)   0x0550 |
|  | Wind Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_PROXIMITY](group__bt__gap__defines.md#ga6d3447e24d5d75051b81998fd9ad8bfe)   0x0551 |
|  | Proximity Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_MULTI](group__bt__gap__defines.md#gaeec9666dbdb31e9302a25aaa536f3180)   0x0552 |
|  | Multi-Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_FLUSH\_MOUNTED](group__bt__gap__defines.md#gaf9a9c0191ec175d14061058cf3da163c)   0x0553 |
|  | Flush Mounted Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_CEILING\_MOUNTED](group__bt__gap__defines.md#gadfb6808db5a7060316b724c24c8ceaf8)   0x0554 |
|  | Ceiling Mounted Sensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_WALL\_MOUNTED](group__bt__gap__defines.md#gae564900f0517d393ceffcca8d27f6e45)   0x0555 |
|  | Wall Mounted Sensor. |
| #define | [BT\_APPEARANCE\_MULTISENSOR](group__bt__gap__defines.md#ga90237753920702380321e9f858344741)   0x0556 |
|  | Multisensor. |
| #define | [BT\_APPEARANCE\_SENSOR\_ENERGY\_METER](group__bt__gap__defines.md#ga7238d3a45f9e62f0189db9d7eeac4d15)   0x0557 |
|  | Energy Meter. |
| #define | [BT\_APPEARANCE\_SENSOR\_FLAME\_DETECTOR](group__bt__gap__defines.md#gaae8f95ef639cb7d5e97063eed710a07d)   0x0558 |
|  | Flame Detector. |
| #define | [BT\_APPEARANCE\_SENSOR\_VEHICLE\_TIRE\_PRESSURE](group__bt__gap__defines.md#ga4d0877a3cd9b7efebbaa5fd8a988a2a3)   0x0559 |
|  | Vehicle Tire Pressure Sensor. |
| #define | [BT\_APPEARANCE\_GENERIC\_LIGHT\_FIXTURES](group__bt__gap__defines.md#gae01be867f730c06b59fcb03289ae66d7)   0x0580 |
|  | Generic Light Fixtures. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_WALL](group__bt__gap__defines.md#gae1b2b535754f9cdc24c4a6cee63ef5cb)   0x0581 |
|  | Wall Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_CEILING](group__bt__gap__defines.md#ga2d77fb5f5ed9a43771186ecc5693da8f)   0x0582 |
|  | Ceiling Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOR](group__bt__gap__defines.md#ga57bb461b0ddd045d21d7fbd3843fbabb)   0x0583 |
|  | Floor Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_CABINET](group__bt__gap__defines.md#gadc48840b6590a89593a5d17fbdb1e9e9)   0x0584 |
|  | Cabinet Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_DESK](group__bt__gap__defines.md#ga2f37bf95ea6057b999bbf2cf94016e5d)   0x0585 |
|  | Desk Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_TROFFER](group__bt__gap__defines.md#gaa57b538ecad380ad77354e0cd9576e5b)   0x0586 |
|  | Troffer Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_PENDANT](group__bt__gap__defines.md#ga336147b54406237e25d8cf9ed152928b)   0x0587 |
|  | Pendant Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_IN\_GROUND](group__bt__gap__defines.md#ga583b7432ba6ac4cc078d3a069e3a54e1)   0x0588 |
|  | In-ground Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_FLOOD](group__bt__gap__defines.md#gab41f8b6f1ff0f624bb6666ef2ac6dab3)   0x0589 |
|  | Flood Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_UNDERWATER](group__bt__gap__defines.md#ga83f50305a23250e5e2cef5004762e122)   0x058A |
|  | Underwater Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_BOLLARD\_WITH](group__bt__gap__defines.md#ga20a7b241f292475d70626a38d983886c)   0x058B |
|  | Bollard with Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_PATHWAY](group__bt__gap__defines.md#ga7c5811bd50d9f78e67e3e56faa432aae)   0x058C |
|  | Pathway Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_GARDEN](group__bt__gap__defines.md#ga348e64ffe0f3d6301dd8c911f70ead68)   0x058D |
|  | Garden Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_POLE\_TOP](group__bt__gap__defines.md#ga0da0cbeebd2b20bf28dfc06def016068)   0x058E |
|  | Pole-top Light. |
| #define | [BT\_APPEARANCE\_SPOT\_LIGHT](group__bt__gap__defines.md#ga58e1989c99b5a223a318a716d62f6e2b)   0x058F |
|  | Spotlight. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_LINEAR](group__bt__gap__defines.md#ga5388daf123e629d6f7a0b9af13fbc366)   0x0590 |
|  | Linear Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_STREET](group__bt__gap__defines.md#gac938fb03553d2d3c27b50af2a9a1ac48)   0x0591 |
|  | Street Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_SHELVES](group__bt__gap__defines.md#ga1bf2889f7a8a7ae363bc1d4355ee8d65)   0x0592 |
|  | Shelves Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_BAY](group__bt__gap__defines.md#ga8f98c2d32664a6e03ebc2a43ae1eb52a)   0x0593 |
|  | Bay Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_EMERGENCY\_EXIT](group__bt__gap__defines.md#ga3f687f994ffff2ce70b81a992195d210)   0x0594 |
|  | Emergency Exit Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_CONTROLLER](group__bt__gap__defines.md#ga35a90a4e3bfef7b0cfec0d5fa7b36c4a)   0x0595 |
|  | Light Controller. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_DRIVER](group__bt__gap__defines.md#gac2b6de99b4e87f7c40063ba844c75ead)   0x0596 |
|  | Light Driver. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_BULB](group__bt__gap__defines.md#ga8325830f2c977dc238a9ca1b9837803e)   0x0597 |
|  | Bulb. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_LOW\_BAY](group__bt__gap__defines.md#gafc924bbc1b6aff0130c2be3d5fe59e33)   0x0598 |
|  | Low-bay Light. |
| #define | [BT\_APPEARANCE\_LIGHT\_FIXTURES\_HIGH\_BAY](group__bt__gap__defines.md#ga738e87008c6a64450bb7ec22dbcdd113)   0x0599 |
|  | High-bay Light. |
| #define | [BT\_APPEARANCE\_GENERIC\_FAN](group__bt__gap__defines.md#ga82cc89321c4f4ffbf3ef25eff624943c)   0x05C0 |
|  | Generic Fan. |
| #define | [BT\_APPEARANCE\_FAN\_CEILING](group__bt__gap__defines.md#ga8cd83cd08846ac276cc65f31333ee62e)   0x05C1 |
|  | Ceiling Fan. |
| #define | [BT\_APPEARANCE\_FAN\_AXIAL](group__bt__gap__defines.md#ga32dd73ffa211d632617018aa510b89c4)   0x05C2 |
|  | Axial Fan. |
| #define | [BT\_APPEARANCE\_FAN\_EXHAUST](group__bt__gap__defines.md#ga1e842c97b90678908f4d18c86c1227c2)   0x05C3 |
|  | Exhaust Fan. |
| #define | [BT\_APPEARANCE\_FAN\_PEDESTAL](group__bt__gap__defines.md#ga2e54f8de862435f2dbd7f56b98615c84)   0x05C4 |
|  | Pedestal Fan. |
| #define | [BT\_APPEARANCE\_FAN\_DESK](group__bt__gap__defines.md#gaa9e17b8b5e06d2fb365bf152e0cbef5d)   0x05C5 |
|  | Desk Fan. |
| #define | [BT\_APPEARANCE\_FAN\_WALL](group__bt__gap__defines.md#ga498be79799cb778c9df6629411fe32ad)   0x05C6 |
|  | Wall Fan. |
| #define | [BT\_APPEARANCE\_GENERIC\_HVAC](group__bt__gap__defines.md#gaf1f01946f6acadcaf719d3d7cc06e55f)   0x0600 |
|  | Generic HVAC. |
| #define | [BT\_APPEARANCE\_HVAC\_THERMOSTAT](group__bt__gap__defines.md#ga33055b50c10bfc713b18823fca525488)   0x0601 |
|  | Thermostat. |
| #define | [BT\_APPEARANCE\_HVAC\_HUMIDIFIER](group__bt__gap__defines.md#gaf55f3f3f07cc78509e7fe19cea6cea4e)   0x0602 |
|  | Humidifier. |
| #define | [BT\_APPEARANCE\_HVAC\_DEHUMIDIFIER](group__bt__gap__defines.md#gaa3b96e44638048b8891a2dece29f4b3f)   0x0603 |
|  | De-humidifier. |
| #define | [BT\_APPEARANCE\_HVAC\_HEATER](group__bt__gap__defines.md#gacef9145f435d10cbf5a775b9a2c9b756)   0x0604 |
|  | Heater. |
| #define | [BT\_APPEARANCE\_HVAC\_RADIATOR](group__bt__gap__defines.md#gad90f108f3d33d68e27ac545cdb520f18)   0x0605 |
|  | Radiator. |
| #define | [BT\_APPEARANCE\_HVAC\_BOILER](group__bt__gap__defines.md#gacc28a1bc1a809c574019455de4ac9d0b)   0x0606 |
|  | Boiler. |
| #define | [BT\_APPEARANCE\_HVAC\_HEAT\_PUMP](group__bt__gap__defines.md#gaead4ebeabb8855111ab9080aca4e035a)   0x0607 |
|  | Heat Pump. |
| #define | [BT\_APPEARANCE\_HVAC\_INFRARED\_HEATER](group__bt__gap__defines.md#ga50c5df52d8471fc8e1dc65e31079566d)   0x0608 |
|  | Infrared Heater. |
| #define | [BT\_APPEARANCE\_HVAC\_RADIANT\_PANEL\_HEATER](group__bt__gap__defines.md#gad43d27ff96a7fba1ed7d5e20ebd472d9)   0x0609 |
|  | Radiant Panel Heater. |
| #define | [BT\_APPEARANCE\_HVAC\_FAN\_HEATER](group__bt__gap__defines.md#ga2a044c3369ed48d216707f6e6a541a23)   0x060A |
|  | Fan Heater. |
| #define | [BT\_APPEARANCE\_HVAC\_AIR\_CURTAIN](group__bt__gap__defines.md#ga182ade4b2c8f4705ba132248e504bb95)   0x060B |
|  | Air Curtain. |
| #define | [BT\_APPEARANCE\_GENERIC\_AIR\_CONDITIONING](group__bt__gap__defines.md#gaa13ae6496d47df2be0a0692a28806007)   0x0640 |
|  | Generic Air Conditioning. |
| #define | [BT\_APPEARANCE\_GENERIC\_HUMIDIFIER](group__bt__gap__defines.md#ga0b552243744bc598467421555e935cd0)   0x0680 |
|  | Generic Humidifier. |
| #define | [BT\_APPEARANCE\_GENERIC\_HEATING](group__bt__gap__defines.md#ga8ea92ea92ca4e2bad4e5e2baba1271dd)   0x06C0 |
|  | Generic Heating. |
| #define | [BT\_APPEARANCE\_HEATING\_RADIATOR](group__bt__gap__defines.md#ga05b0b91c74aed5bc73a92f336bdae33a)   0x06C1 |
|  | Radiator. |
| #define | [BT\_APPEARANCE\_HEATING\_BOILER](group__bt__gap__defines.md#gac1abc9ae0b8ede2197720ea9e67b692e)   0x06C2 |
|  | Boiler. |
| #define | [BT\_APPEARANCE\_HEATING\_HEAT\_PUMP](group__bt__gap__defines.md#ga99537968fdc7e680d922ca309fba7678)   0x06C3 |
|  | Heat Pump. |
| #define | [BT\_APPEARANCE\_HEATING\_INFRARED\_HEATER](group__bt__gap__defines.md#ga8e40496a351c7ec5ea836805925f1e13)   0x06C4 |
|  | Infrared Heater. |
| #define | [BT\_APPEARANCE\_HEATING\_RADIANT\_PANEL\_HEATER](group__bt__gap__defines.md#ga46fe051c7e50492dba5ae824e154cf69)   0x06C5 |
|  | Radiant Panel Heater. |
| #define | [BT\_APPEARANCE\_HEATING\_FAN\_HEATER](group__bt__gap__defines.md#ga995ca18db114ea062df0d76c9e241937)   0x06C6 |
|  | Fan Heater. |
| #define | [BT\_APPEARANCE\_HEATING\_AIR\_CURTAIN](group__bt__gap__defines.md#gac74bc8e109f5d9b4c0988ee6378ed471)   0x06C7 |
|  | Air Curtain. |
| #define | [BT\_APPEARANCE\_GENERIC\_ACCESS\_CONTROL](group__bt__gap__defines.md#gac856a99a5db04dc20229a6e60a18d310)   0x0700 |
|  | Generic Access Control. |
| #define | [BT\_APPEARANCE\_CONTROL\_ACCESS\_DOOR](group__bt__gap__defines.md#ga8e21f7df9d789b7c3aa6f7dab500df8c)   0x0701 |
|  | Access Door. |
| #define | [BT\_APPEARANCE\_CONTROL\_GARAGE\_DOOR](group__bt__gap__defines.md#ga39134568b56c1d33e6567c893eb441f1)   0x0702 |
|  | Garage Door. |
| #define | [BT\_APPEARANCE\_CONTROL\_EMERGENCY\_EXIT\_DOOR](group__bt__gap__defines.md#ga2b6c7987ee4040216a385e665ff92321)   0x0703 |
|  | Emergency Exit Door. |
| #define | [BT\_APPEARANCE\_CONTROL\_ACCESS\_LOCK](group__bt__gap__defines.md#gac2f588b6202e9d6140ec682cfe45f65d)   0x0704 |
|  | Access Lock. |
| #define | [BT\_APPEARANCE\_CONTROL\_ELEVATOR](group__bt__gap__defines.md#ga321d63ead349c0a83ef289bd2e4efb33)   0x0705 |
|  | Elevator. |
| #define | [BT\_APPEARANCE\_CONTROL\_WINDOW](group__bt__gap__defines.md#gaedc6415432862889e7f002fc9ef46b74)   0x0706 |
|  | Window. |
| #define | [BT\_APPEARANCE\_CONTROL\_ENTRANCE\_GATE](group__bt__gap__defines.md#gab2a476a90f20576c0a1784fdc1e5e633)   0x0707 |
|  | Entrance Gate. |
| #define | [BT\_APPEARANCE\_CONTROL\_DOOR\_LOCK](group__bt__gap__defines.md#ga29d07ce1101740b5f6f980660e405278)   0x0708 |
|  | Door Lock. |
| #define | [BT\_APPEARANCE\_CONTROL\_LOCKER](group__bt__gap__defines.md#ga824236ba19c7f54d06b9abcd7df8c767)   0x0709 |
|  | Locker. |
| #define | [BT\_APPEARANCE\_GENERIC\_MOTORIZED\_DEVICE](group__bt__gap__defines.md#ga414b202e93d1db533853093d66603720)   0x0740 |
|  | Generic Motorized Device. |
| #define | [BT\_APPEARANCE\_MOTORIZED\_GATE](group__bt__gap__defines.md#ga376ef909868a5c273b71d1c372755707)   0x0741 |
|  | Motorized Gate. |
| #define | [BT\_APPEARANCE\_MOTORIZED\_AWNING](group__bt__gap__defines.md#ga338de5523abf3fd81e913f3cdb4a31b6)   0x0742 |
|  | Awning. |
| #define | [BT\_APPEARANCE\_MOTORIZED\_BLINDS\_OR\_SHADES](group__bt__gap__defines.md#gaaa39c48ed2d6edd5650743b82154462b)   0x0743 |
|  | Blinds or Shades. |
| #define | [BT\_APPEARANCE\_MOTORIZED\_CURTAINS](group__bt__gap__defines.md#ga53f6a4df5ccc2117525952be2e174ddc)   0x0744 |
|  | Curtains. |
| #define | [BT\_APPEARANCE\_MOTORIZED\_SCREEN](group__bt__gap__defines.md#ga5f32cab5c7a155fffbe0c33cadfef31a)   0x0745 |
|  | Screen. |
| #define | [BT\_APPEARANCE\_GENERIC\_POWER\_DEVICE](group__bt__gap__defines.md#gadae82e45d9aafd34cafd3f0e793b1b24)   0x0780 |
|  | Generic Power Device. |
| #define | [BT\_APPEARANCE\_POWER\_OUTLET](group__bt__gap__defines.md#gad9efd19e2c95525a3972c8b0f0417449)   0x0781 |
|  | Power Outlet. |
| #define | [BT\_APPEARANCE\_POWER\_STRIP](group__bt__gap__defines.md#ga2c5bd38d4eeb1aad2d29b004390a6d18)   0x0782 |
|  | Power Strip. |
| #define | [BT\_APPEARANCE\_POWER\_PLUG](group__bt__gap__defines.md#ga0d9aadc19f5f5f484769b225164866e4)   0x0783 |
|  | Plug. |
| #define | [BT\_APPEARANCE\_POWER\_SUPPLY](group__bt__gap__defines.md#ga07acce808c9cf2b5e84aacd65e8f256d)   0x0784 |
|  | Power Supply. |
| #define | [BT\_APPEARANCE\_POWER\_LED\_DRIVER](group__bt__gap__defines.md#ga31842298741c822dcebba942453975c6)   0x0785 |
|  | LED Driver. |
| #define | [BT\_APPEARANCE\_POWER\_FLUORESCENT\_LAMP\_GEAR](group__bt__gap__defines.md#ga7de26016aa039e3e72ddd61653e1c1d8)   0x0786 |
|  | Fluorescent Lamp Gear. |
| #define | [BT\_APPEARANCE\_POWER\_HID\_LAMP\_GEAR](group__bt__gap__defines.md#ga6396b1d813c9764bdfe92c4f2ba961b1)   0x0787 |
|  | HID Lamp Gear. |
| #define | [BT\_APPEARANCE\_POWER\_CHARGE\_CASE](group__bt__gap__defines.md#ga5d6b28b9660d2357e2af2bf0ceab9c18)   0x0788 |
|  | Charge Case. |
| #define | [BT\_APPEARANCE\_POWER\_POWER\_BANK](group__bt__gap__defines.md#gab6a5ac3941a5707f052126810a7f22e0)   0x0789 |
|  | Power Bank. |
| #define | [BT\_APPEARANCE\_GENERIC\_LIGHT\_SOURCE](group__bt__gap__defines.md#gacb3340c5193588eea2d42fe1bef443d0)   0x07C0 |
|  | Generic Light Source. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_INCANDESCENT\_BULB](group__bt__gap__defines.md#gafed8531ffde21d0ad6e8d477d64496f0)   0x07C1 |
|  | Incandescent Light Bulb. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_LAMP](group__bt__gap__defines.md#ga66bf91b8a25ac88a0fd6ab9456201de1)   0x07C2 |
|  | LED Lamp. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_HID\_LAMP](group__bt__gap__defines.md#ga1babd2989112bafb5819235fe5b6c556)   0x07C3 |
|  | HID Lamp. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_FLUORESCENT\_LAMP](group__bt__gap__defines.md#ga39957a77aa54255ab3a06441e422e7e3)   0x07C4 |
|  | Fluorescent Lamp. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_LED\_ARRAY](group__bt__gap__defines.md#ga242d324cf5cf33e4edd5cf33e8c3c89b)   0x07C5 |
|  | LED Array. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_MULTICOLOR\_LED\_ARRAY](group__bt__gap__defines.md#ga8449006920ed1fdd562c702ee2e16a21)   0x07C6 |
|  | Multi-Color LED Array. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_LOW\_VOLTAGE\_HALOGEN](group__bt__gap__defines.md#gaf47bce54f4ae1915cd64c3c2d254e353)   0x07C7 |
|  | Low voltage halogen. |
| #define | [BT\_APPEARANCE\_LIGHT\_SOURCE\_OLED](group__bt__gap__defines.md#gaed4400a94dae4f536a456cc55eb6f6d5)   0x07C8 |
|  | Organic light emitting diode. |
| #define | [BT\_APPEARANCE\_GENERIC\_WINDOW\_COVERING](group__bt__gap__defines.md#ga1e70d961fca2719243c866464132684c)   0x0800 |
|  | Generic Window Covering. |
| #define | [BT\_APPEARANCE\_WINDOW\_SHADES](group__bt__gap__defines.md#ga37614ae63c8287bc4bd0c9a5bf00502e)   0x0801 |
|  | Window Shades. |
| #define | [BT\_APPEARANCE\_WINDOW\_BLINDS](group__bt__gap__defines.md#ga717efaeab0329ded066567761b9983a7)   0x0802 |
|  | Window Blinds. |
| #define | [BT\_APPEARANCE\_WINDOW\_AWNING](group__bt__gap__defines.md#ga9945bb52a9ee3268efda7d5e05421e12)   0x0803 |
|  | Window Awning. |
| #define | [BT\_APPEARANCE\_WINDOW\_CURTAIN](group__bt__gap__defines.md#ga20352e58e6cec63efbb6beaa75c0e330)   0x0804 |
|  | Window Curtain. |
| #define | [BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SHUTTER](group__bt__gap__defines.md#ga7ead13b128fbc50be3f5c101fb1383cb)   0x0805 |
|  | Exterior Shutter. |
| #define | [BT\_APPEARANCE\_WINDOW\_EXTERIOR\_SCREEN](group__bt__gap__defines.md#ga0a0b87095177af0560a540e545c97f42)   0x0806 |
|  | Exterior Screen. |
| #define | [BT\_APPEARANCE\_GENERIC\_AUDIO\_SINK](group__bt__gap__defines.md#ga32bb0f06096ce5259676a31342b9f0d9)   0x0840 |
|  | Generic Audio Sink. |
| #define | [BT\_APPEARANCE\_AUDIO\_SINK\_STANDALONE\_SPEAKER](group__bt__gap__defines.md#gabcb109c4660a177494329faf353406f4)   0x0841 |
|  | Standalone Speaker. |
| #define | [BT\_APPEARANCE\_AUDIO\_SINK\_SOUNDBAR](group__bt__gap__defines.md#ga93e3a858b2efabea72a8855a28ad21c2)   0x0842 |
|  | Soundbar. |
| #define | [BT\_APPEARANCE\_AUDIO\_SINK\_BOOKSHELF\_SPEAKER](group__bt__gap__defines.md#ga666aed968e9a0f9566edcc1bcba0bfbd)   0x0843 |
|  | Bookshelf Speaker. |
| #define | [BT\_APPEARANCE\_AUDIO\_SINK\_STANDMOUNTED\_SPEAKER](group__bt__gap__defines.md#ga6b3ddddf1de7d95a15aa6194ddc656ee)   0x0844 |
|  | Standmounted Speaker. |
| #define | [BT\_APPEARANCE\_AUDIO\_SINK\_SPEAKERPHONE](group__bt__gap__defines.md#gadd82602d251aa555a06123ef0388d1b1)   0x0845 |
|  | Speakerphone. |
| #define | [BT\_APPEARANCE\_GENERIC\_AUDIO\_SOURCE](group__bt__gap__defines.md#gac85b90f2585044d0efa61191dba3c596)   0x0880 |
|  | Generic Audio Source. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_MICROPHONE](group__bt__gap__defines.md#ga6dd1354de34ed79702d9d7878d859fcb)   0x0881 |
|  | Microphone. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_ALARM](group__bt__gap__defines.md#gaa8d5a95cb181e27efb2409d5dce3da57)   0x0882 |
|  | Alarm. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_BELL](group__bt__gap__defines.md#ga748b4fa86145f3950069ed44cde8cacb)   0x0883 |
|  | Bell. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_HORN](group__bt__gap__defines.md#ga3415afbd526b29b5bbafc1ac889bd371)   0x0884 |
|  | Horn. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_DEVICE](group__bt__gap__defines.md#ga35ecc1a1051379010123582c82e9b31c)   0x0885 |
|  | Broadcasting Device. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_SERVICE\_DESK](group__bt__gap__defines.md#ga48fc37d769211cba1e6121e670b02e25)   0x0886 |
|  | Service Desk. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_KIOSK](group__bt__gap__defines.md#ga6ad3ee00ed05c8a7ed182df5c82a5af4)   0x0887 |
|  | Kiosk. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_BROADCASTING\_ROOM](group__bt__gap__defines.md#gaad0fe38e5246c55cc562729448b9f390)   0x0888 |
|  | Broadcasting Room. |
| #define | [BT\_APPEARANCE\_AUDIO\_SOURCE\_AUDITORIUM](group__bt__gap__defines.md#gac8ab0549f83c9d6b68dc4dd75cfe7b1e)   0x0889 |
|  | Auditorium. |
| #define | [BT\_APPEARANCE\_GENERIC\_MOTORIZED\_VEHICLE](group__bt__gap__defines.md#ga49328394fd7505da9476d4d62ae60c03)   0x08C0 |
|  | Generic Motorized Vehicle. |
| #define | [BT\_APPEARANCE\_VEHICLE\_CAR](group__bt__gap__defines.md#ga6257291ed3e6d09ce6197e2081b36d04)   0x08C1 |
|  | Car. |
| #define | [BT\_APPEARANCE\_VEHICLE\_LARGE\_GOODS](group__bt__gap__defines.md#ga31ff643e1efccffd9ba73c793f63837c)   0x08C2 |
|  | Large Goods Vehicle. |
| #define | [BT\_APPEARANCE\_VEHICLE\_TWO\_WHEELED](group__bt__gap__defines.md#ga68ade931a12e5d9e9863decad3d8de9e)   0x08C3 |
|  | 2-Wheeled Vehicle |
| #define | [BT\_APPEARANCE\_VEHICLE\_MOTORBIKE](group__bt__gap__defines.md#gaa71eaa4fd0eef66a794475cb44aaf397)   0x08C4 |
|  | Motorbike. |
| #define | [BT\_APPEARANCE\_VEHICLE\_SCOOTER](group__bt__gap__defines.md#gae082982b90d94404b69c57987d8a2c5a)   0x08C5 |
|  | Scooter. |
| #define | [BT\_APPEARANCE\_VEHICLE\_MOPED](group__bt__gap__defines.md#ga18b0231dbd97d8871f685774f9e1b4e1)   0x08C6 |
|  | Moped. |
| #define | [BT\_APPEARANCE\_VEHICLE\_THREE\_WHEELED](group__bt__gap__defines.md#ga8159dfd6933a2a5fdb2c72da9623bc2e)   0x08C7 |
|  | 3-Wheeled Vehicle |
| #define | [BT\_APPEARANCE\_VEHICLE\_LIGHT](group__bt__gap__defines.md#gac22a0476760c42eb8f00b36b74361c5e)   0x08C8 |
|  | Light Vehicle. |
| #define | [BT\_APPEARANCE\_VEHICLE\_QUAD\_BIKE](group__bt__gap__defines.md#ga03e3660bdc2e439126f2f8df8ea335ee)   0x08C9 |
|  | Quad Bike. |
| #define | [BT\_APPEARANCE\_VEHICLE\_MINIBUS](group__bt__gap__defines.md#ga0cf473bbf07d4576ab9f0116ca48f161)   0x08CA |
|  | Minibus. |
| #define | [BT\_APPEARANCE\_VEHICLE\_BUS](group__bt__gap__defines.md#ga0da02a18987c653a3232c28a3e4908f7)   0x08CB |
|  | Bus. |
| #define | [BT\_APPEARANCE\_VEHICLE\_TROLLEY](group__bt__gap__defines.md#gabde7af9f7c25d56f5fb9643398273526)   0x08CC |
|  | Trolley. |
| #define | [BT\_APPEARANCE\_VEHICLE\_AGRICULTURAL](group__bt__gap__defines.md#gaa149e56e4b4a1b6dde821fbdac3d9c32)   0x08CD |
|  | Agricultural Vehicle. |
| #define | [BT\_APPEARANCE\_VEHICLE\_CAMPER\_OR\_CARAVAN](group__bt__gap__defines.md#gafcb3909bf61bb130f8c0a217e69477b8)   0x08CE |
|  | Camper/Caravan. |
| #define | [BT\_APPEARANCE\_VEHICLE\_RECREATIONAL](group__bt__gap__defines.md#ga9366a994d42c88490313380d419b2a8e)   0x08CF |
|  | Recreational Vehicle/Motor Home. |
| #define | [BT\_APPEARANCE\_GENERIC\_DOMESTIC\_APPLIANCE](group__bt__gap__defines.md#gac08b31ff9b618b19e4c1b43ae2056b5f)   0x0900 |
|  | Generic Domestic Appliance. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_REFRIGERATOR](group__bt__gap__defines.md#gad02c3dc8fa1321b14ee70264a36c4950)   0x0901 |
|  | Refrigerator. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_FREEZER](group__bt__gap__defines.md#ga6ec2458a171142a5e22ec339d23a5a0c)   0x0902 |
|  | Freezer. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_OVEN](group__bt__gap__defines.md#ga7a48c5a07e677167ae10412ed2c1040b)   0x0903 |
|  | Oven. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_MICROWAVE](group__bt__gap__defines.md#gabaac12b866cd29547165331333e8be3d)   0x0904 |
|  | Microwave. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_TOASTER](group__bt__gap__defines.md#ga5b0d9632cb2ed4afd856f05a1e857394)   0x0905 |
|  | Toaster. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_WASHING\_MACHINE](group__bt__gap__defines.md#ga1febcada2c95105648831094a4de6a8d)   0x0906 |
|  | Washing Machine. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_DRYER](group__bt__gap__defines.md#gaac26996e0de10b16e24900a08c1098f5)   0x0907 |
|  | Dryer. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_COFFEE\_MAKER](group__bt__gap__defines.md#gac601c74c6132decf13527bdacbc5a08b)   0x0908 |
|  | Coffee maker. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_IRON](group__bt__gap__defines.md#gaeb66941a8e8b38ed0ea47305da157e24)   0x0909 |
|  | Clothes iron. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_CURLING\_IRON](group__bt__gap__defines.md#ga6a9885e9a2133c0732d056ecd63313ad)   0x090A |
|  | Curling iron. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_HAIR\_DRYER](group__bt__gap__defines.md#ga15be0164f5883558fb61c9cb9679b78f)   0x090B |
|  | Hair dryer. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_VACUUM\_CLEANER](group__bt__gap__defines.md#ga46d5f18bb8c764c43af97fddcec4a1ec)   0x090C |
|  | Vacuum cleaner. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_ROBOTIC\_VACUUM\_CLEANER](group__bt__gap__defines.md#ga423e85d0816a4bd0205f4d8188e6c406)   0x090D |
|  | Robotic vacuum cleaner. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_RICE\_COOKER](group__bt__gap__defines.md#ga78511e0ef7d509deeba65352e7f81ad8)   0x090E |
|  | Rice cooker. |
| #define | [BT\_APPEARANCE\_APPLIANCE\_CLOTHES\_STEAMER](group__bt__gap__defines.md#ga0292c6123b655964311d0e6027b5af20)   0x090F |
|  | Clothes steamer. |
| #define | [BT\_APPEARANCE\_GENERIC\_WEARABLE\_AUDIO\_DEVICE](group__bt__gap__defines.md#gabad761094a16873dcebbc6238825d84b)   0x0940 |
|  | Generic Wearable Audio Device. |
| #define | [BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_EARBUD](group__bt__gap__defines.md#gab480735e2ba8db23d2668ea3a2137214)   0x0941 |
|  | Earbud. |
| #define | [BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADSET](group__bt__gap__defines.md#ga8bd98ba3a4c1cbf8dbf8235d9ad0f943)   0x0942 |
|  | Headset. |
| #define | [BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_HEADPHONES](group__bt__gap__defines.md#gae420044380309abba1b9570d26735315)   0x0943 |
|  | Headphones. |
| #define | [BT\_APPEARANCE\_WEARABLE\_AUDIO\_DEVICE\_NECK\_BAND](group__bt__gap__defines.md#ga59ea8ff5efec7a19bce8440e7ae78a1e)   0x0944 |
|  | Neck Band. |
| #define | [BT\_APPEARANCE\_GENERIC\_AIRCRAFT](group__bt__gap__defines.md#ga24c9bcf9646ec5049abf310b31ab355e)   0x0980 |
|  | Generic Aircraft. |
| #define | [BT\_APPEARANCE\_AIRCRAFT\_LIGHT](group__bt__gap__defines.md#ga6f1d2fb56f53ac5317b024d7487b8742)   0x0981 |
|  | Light Aircraft. |
| #define | [BT\_APPEARANCE\_AIRCRAFT\_MICROLIGHT](group__bt__gap__defines.md#gad2d0b1c4b710e50127049ec4cd299396)   0x0982 |
|  | Microlight. |
| #define | [BT\_APPEARANCE\_AIRCRAFT\_PARAGLIDER](group__bt__gap__defines.md#ga6f827322066333fe926f0912099e6903)   0x0983 |
|  | Paraglider. |
| #define | [BT\_APPEARANCE\_AIRCRAFT\_LARGE\_PASSENGER](group__bt__gap__defines.md#gae7be5c3bf9ad97e34d6c62bb791c39c0)   0x0984 |
|  | Large Passenger Aircraft. |
| #define | [BT\_APPEARANCE\_GENERIC\_AV\_EQUIPMENT](group__bt__gap__defines.md#gadb3b07d6c3d3f679b15069fdd8d4e1ee)   0x09C0 |
|  | Generic AV Equipment. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_AMPLIFIER](group__bt__gap__defines.md#ga7294c7b26ac8da3b9800c91ec824ad22)   0x09C1 |
|  | Amplifier. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_RECEIVER](group__bt__gap__defines.md#gac826e2e5326d1aa5fdd7ebf55fe395e6)   0x09C2 |
|  | Receiver. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_RADIO](group__bt__gap__defines.md#gad60d1a387a1c62218baa3044e5acc3db)   0x09C3 |
|  | Radio. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_TUNER](group__bt__gap__defines.md#ga7ccf41932861fa5f33d12060a12d5aa7)   0x09C4 |
|  | Tuner. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_TURNTABLE](group__bt__gap__defines.md#ga69417cb3e9c434e751483328d6134cdf)   0x09C5 |
|  | Turntable. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_CD\_PLAYER](group__bt__gap__defines.md#ga6c9ad45a9b22a94ae0cce16bfe749a33)   0x09C6 |
|  | CD Player. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_DVD\_PLAYER](group__bt__gap__defines.md#ga02681af8d755c701d9caef3f89a5c35a)   0x09C7 |
|  | DVD Player. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_BLURAY\_PLAYER](group__bt__gap__defines.md#ga1394bc80927fb8db4eef1786111c65c7)   0x09C8 |
|  | Bluray Player. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_OPTICAL\_DISC\_PLAYER](group__bt__gap__defines.md#gaa01c862bff9aaaad09ed925da60fcb25)   0x09C9 |
|  | Optical Disc Player. |
| #define | [BT\_APPEARANCE\_AV\_EQUIPMENT\_SET\_TOP\_BOX](group__bt__gap__defines.md#gad0ac86cf291b781b772fa9e85dda283a)   0x09CA |
|  | Set-Top Box. |
| #define | [BT\_APPEARANCE\_GENERIC\_DISPLAY\_EQUIPMENT](group__bt__gap__defines.md#ga44b70b2f515416baf686b1e127ef4375)   0x0A00 |
|  | Generic Display Equipment. |
| #define | [BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_TELEVISION](group__bt__gap__defines.md#ga9a6684aa8677575625e049fa0da2c26c)   0x0A01 |
|  | Television. |
| #define | [BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_MONITOR](group__bt__gap__defines.md#gabbcb0fbbeb6423052db9d5e04410499c)   0x0A02 |
|  | Monitor. |
| #define | [BT\_APPEARANCE\_DISPLAY\_EQUIPMENT\_PROJECTOR](group__bt__gap__defines.md#gaa98f5139c99b46515746fb76e9ae7f9b)   0x0A03 |
|  | Projector. |
| #define | [BT\_APPEARANCE\_GENERIC\_HEARING\_AID](group__bt__gap__defines.md#gadb5595a41edf5974e03649a675618b7b)   0x0A40 |
|  | Generic Hearing aid. |
| #define | [BT\_APPEARANCE\_HEARING\_AID\_IN\_EAR](group__bt__gap__defines.md#ga28cc6555937d9d5a9e8ae0079fc8a534)   0x0A41 |
|  | In-ear hearing aid. |
| #define | [BT\_APPEARANCE\_HEARING\_AID\_BEHIND\_EAR](group__bt__gap__defines.md#ga1fa6231e14dcfa90a5518e61f0e4e302)   0x0A42 |
|  | Behind-ear hearing aid. |
| #define | [BT\_APPEARANCE\_HEARING\_AID\_COCHLEAR\_IMPLANT](group__bt__gap__defines.md#ga82ba79bd9fd04a3fbdb6d8b4e35e3877)   0x0A43 |
|  | Cochlear Implant. |
| #define | [BT\_APPEARANCE\_GENERIC\_GAMING](group__bt__gap__defines.md#gaca727b215a8277d921c0a3bfeccb3f14)   0x0A80 |
|  | Generic Gaming. |
| #define | [BT\_APPEARANCE\_HOME\_VIDEO\_GAME\_CONSOLE](group__bt__gap__defines.md#ga8fbaf0fced0cce12e08c4a516351b166)   0x0A81 |
|  | Home Video Game Console. |
| #define | [BT\_APPEARANCE\_PORTABLE\_HANDHELD\_CONSOLE](group__bt__gap__defines.md#ga39ad633d1795af4546bd930d0e799447)   0x0A82 |
|  | Portable handheld console. |
| #define | [BT\_APPEARANCE\_GENERIC\_SIGNAGE](group__bt__gap__defines.md#gabc243c7449804749704c1862db286eab)   0x0AC0 |
|  | Generic Signage. |
| #define | [BT\_APPEARANCE\_SIGNAGE\_DIGITAL](group__bt__gap__defines.md#gace31a591ef3b5f0812e4cbf417a2205a)   0x0AC1 |
|  | Digital Signage. |
| #define | [BT\_APPEARANCE\_SIGNAGE\_ELECTRONIC\_LABEL](group__bt__gap__defines.md#gaa4674b06751edf98fa88ede568a68ad4)   0x0AC2 |
|  | Electronic Label. |
| #define | [BT\_APPEARANCE\_GENERIC\_PULSE\_OXIMETER](group__bt__gap__defines.md#ga93ee753bf3b8819239041c065eaf024f)   0x0C40 |
|  | Generic Pulse Oximeter. |
| #define | [BT\_APPEARANCE\_PULSE\_OXIMETER\_FINGERTIP](group__bt__gap__defines.md#ga8a298130c73299b6079dae3065954c0c)   0x0C41 |
|  | Fingertip Pulse Oximeter. |
| #define | [BT\_APPEARANCE\_PULSE\_OXIMETER\_WRIST](group__bt__gap__defines.md#gaebcadd5c37e6d87903e2cb97e03aeb7d)   0x0C42 |
|  | Wrist Worn Pulse Oximeter. |
| #define | [BT\_APPEARANCE\_GENERIC\_WEIGHT\_SCALE](group__bt__gap__defines.md#ga1aec23cd4f531a57260c7c8faf9caf40)   0x0C80 |
|  | Generic Weight Scale. |
| #define | [BT\_APPEARANCE\_GENERIC\_PERSONAL\_MOBILITY\_DEVICE](group__bt__gap__defines.md#ga7387d717c77b38374e981991278aeb1c)   0x0CC0 |
|  | Generic Personal Mobility Device. |
| #define | [BT\_APPEARANCE\_MOBILITY\_POWERED\_WHEELCHAIR](group__bt__gap__defines.md#ga7966ec64cafe708fe94a7c323fbe3713)   0x0CC1 |
|  | Powered Wheelchair. |
| #define | [BT\_APPEARANCE\_MOBILITY\_SCOOTER](group__bt__gap__defines.md#ga21f21a73f355ffaa408376ca4fc802a8)   0x0CC2 |
|  | Mobility Scooter. |
| #define | [BT\_APPEARANCE\_CONTINUOUS\_GLUCOSE\_MONITOR](group__bt__gap__defines.md#gab77dd4cfe254df84cbe0b8d45247e198)   0x0D00 |
|  | Continuous Glucose Monitor. |
| #define | [BT\_APPEARANCE\_GENERIC\_INSULIN\_PUMP](group__bt__gap__defines.md#ga481169a27fab19628f81a68af31d543c)   0x0D40 |
|  | Generic Insulin Pump. |
| #define | [BT\_APPEARANCE\_INSULIN\_PUMP\_DURABLE](group__bt__gap__defines.md#ga63512439364307259010bededf7bfd8b)   0x0D41 |
|  | Insulin Pump, durable pump. |
| #define | [BT\_APPEARANCE\_INSULIN\_PUMP\_PATCH](group__bt__gap__defines.md#ga0979695247b96321e5a8b6869d09227a)   0x0D44 |
|  | Insulin Pump, patch pump. |
| #define | [BT\_APPEARANCE\_INSULIN\_PEN](group__bt__gap__defines.md#ga1562514d0182e8862edad570b7a346e6)   0x0D48 |
|  | Insulin Pen. |
| #define | [BT\_APPEARANCE\_GENERIC\_MEDICATION\_DELIVERY](group__bt__gap__defines.md#ga08453eebe2ae8f53deddaa64a029c2b5)   0x0D80 |
|  | Generic Medication Delivery. |
| #define | [BT\_APPEARANCE\_GENERIC\_SPIROMETER](group__bt__gap__defines.md#ga1332c44cc3371fa9006993d03ba4ae12)   0x0DC0 |
|  | Generic Spirometer. |
| #define | [BT\_APPEARANCE\_SPIROMETER\_HANDHELD](group__bt__gap__defines.md#ga42b9d596efb757b209f080a8c33f3723)   0x0DC1 |
|  | Handheld Spirometer. |
| #define | [BT\_APPEARANCE\_GENERIC\_OUTDOOR\_SPORTS](group__bt__gap__defines.md#ga0d39ca2892bd96013b8c82111eecc1cb)   0x1440 |
|  | Generic Outdoor Sports Activity. |
| #define | [BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION](group__bt__gap__defines.md#ga30c97d6f5bff1a4a67e4f59eb4d49d2d)   0x1441 |
|  | Location Display. |
| #define | [BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_AND\_NAV](group__bt__gap__defines.md#ga52b6c51c9afcbbba12d9d3cae824f4a7)   0x1442 |
|  | Location and Navigation Display. |
| #define | [BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD](group__bt__gap__defines.md#gadf053353789183d1b1c3ca13ad98559f)   0x1443 |
|  | Location Pod. |
| #define | [BT\_APPEARANCE\_OUTDOOR\_SPORTS\_LOCATION\_POD\_AND\_NAV](group__bt__gap__defines.md#ga8fbc7782099e724febb712ee108e8cba)   0x1444 |
|  | Location and Navigation Pod. |
| Defined GAP timers | |
| #define | [BT\_GAP\_SCAN\_FAST\_INTERVAL\_MIN](group__bt__gap__defines.md#gae9356673ee78d9abb27891738344513a)   0x0030 /\* 30 ms \*/ |
| #define | [BT\_GAP\_SCAN\_FAST\_INTERVAL](group__bt__gap__defines.md#ga747caa714962215453a966a323e77cf8)   0x0060 /\* 60 ms \*/ |
| #define | [BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0)   0x0030 /\* 30 ms \*/ |
| #define | [BT\_GAP\_SCAN\_SLOW\_INTERVAL\_1](group__bt__gap__defines.md#ga1acb5143221e9f94af4d5dc3a9eab125)   0x0800 /\* 1.28 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_SCAN\_SLOW\_WINDOW\_1](group__bt__gap__defines.md#ga29a1a15bfbe035f439c48d1db96db392)   0x0012 /\* 11.25 ms \*/ |
| #define | [BT\_GAP\_SCAN\_SLOW\_INTERVAL\_2](group__bt__gap__defines.md#ga38455c10880fddac0a1b4303a642e44d)   0x1000 /\* 2.56 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_SCAN\_SLOW\_WINDOW\_2](group__bt__gap__defines.md#gaa809fd8143c2805768874195ac24936f)   0x0012 /\* 11.25 ms \*/ |
| #define | [BT\_GAP\_ADV\_FAST\_INT\_MIN\_1](group__bt__gap__defines.md#ga397a52fe616416665b46a2bc454c2e11)   0x0030 /\* 30 ms \*/ |
| #define | [BT\_GAP\_ADV\_FAST\_INT\_MAX\_1](group__bt__gap__defines.md#ga13acf16d3d8edd39636bb10df752775a)   0x0060 /\* 60 ms \*/ |
| #define | [BT\_GAP\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga9573e6bcdae3aae9d51c0becbbd7ac60)   0x00a0 /\* 100 ms \*/ |
| #define | [BT\_GAP\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#gaebc3ce60836522d883f664227a3ffcfb)   0x00f0 /\* 150 ms \*/ |
| #define | [BT\_GAP\_ADV\_SLOW\_INT\_MIN](group__bt__gap__defines.md#ga647f70c07c15f11287b735cbaad2a326)   0x0640 /\* 1 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_ADV\_SLOW\_INT\_MAX](group__bt__gap__defines.md#gadecbfb823bbb6ffdd48be02df2f05f87)   0x0780 /\* 1.2 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_1](group__bt__gap__defines.md#gafd724ebc809044574283c5547beda824)   0x0018 /\* 30 ms \*/ |
| #define | [BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_1](group__bt__gap__defines.md#ga849315b0b724af6017b910e78db0cfae)   0x0030 /\* 60 ms \*/ |
| #define | [BT\_GAP\_PER\_ADV\_FAST\_INT\_MIN\_2](group__bt__gap__defines.md#ga61eb4d6d65f1dd9c475a6f2f44b27957)   0x0050 /\* 100 ms \*/ |
| #define | [BT\_GAP\_PER\_ADV\_FAST\_INT\_MAX\_2](group__bt__gap__defines.md#ga264134294d8378d6e7d2bc52d4e0af1c)   0x0078 /\* 150 ms \*/ |
| #define | [BT\_GAP\_PER\_ADV\_SLOW\_INT\_MIN](group__bt__gap__defines.md#gab51898ce46ee9ae468ed7ffc1d117321)   0x0320 /\* 1 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_PER\_ADV\_SLOW\_INT\_MAX](group__bt__gap__defines.md#gaa618da2a7c217527b0d962315caa1c22)   0x03C0 /\* 1.2 [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) \*/ |
| #define | [BT\_GAP\_INIT\_CONN\_INT\_MIN](group__bt__gap__defines.md#gadaa7f1547c4ea22936087c181d82a552)   0x0018 /\* 30 ms \*/ |
| #define | [BT\_GAP\_INIT\_CONN\_INT\_MAX](group__bt__gap__defines.md#ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1)   0x0028 /\* 50 ms \*/ |

| Enumerations | |
| --- | --- |
| enum | { [BT\_GAP\_LE\_PHY\_NONE](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20baaf7e1b40f6464a603e5116db269cacab) = 0 , [BT\_GAP\_LE\_PHY\_1M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba53eff400720a20fe1a91da4834bad752) = BIT(0) , [BT\_GAP\_LE\_PHY\_2M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba662049cc8293959194bcb481e1dd50a8) = BIT(1) , [BT\_GAP\_LE\_PHY\_CODED](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba97d042e48448fdf6a9e35e5d38cb14c3) = BIT(2) } |
|  | LE PHY types. [More...](group__bt__gap__defines.md#ga7dc8e89251aa575e28331e05775ba20b) |
| enum | {     [BT\_GAP\_ADV\_TYPE\_ADV\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eaf4d48e46c1da164e876e4ded28470c82) = 0x00 , [BT\_GAP\_ADV\_TYPE\_ADV\_DIRECT\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea05b182a44fea67f52015cbfb4d775be8) = 0x01 , [BT\_GAP\_ADV\_TYPE\_ADV\_SCAN\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eae48316c135886d9f6d20f7bdba0858c1) = 0x02 , [BT\_GAP\_ADV\_TYPE\_ADV\_NONCONN\_IND](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3eabb587b376bd6511881d6b70ceaa2af56) = 0x03 ,     [BT\_GAP\_ADV\_TYPE\_SCAN\_RSP](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea5387de0177d3a9da9fd0c44ca30c7018) = 0x04 , [BT\_GAP\_ADV\_TYPE\_EXT\_ADV](group__bt__gap__defines.md#ggab5a881b0cb1df3cf98de07a14e818c3ea09292ffe2f0b76b8761fcaad6fbf9ba8) = 0x05   } |
|  | Advertising PDU types. [More...](group__bt__gap__defines.md#gab5a881b0cb1df3cf98de07a14e818c3e) |
| enum | {     [BT\_GAP\_ADV\_PROP\_CONNECTABLE](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711baf843db0752f3360ccb1a02c456ca9e5e) = BIT(0) , [BT\_GAP\_ADV\_PROP\_SCANNABLE](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba6c5ea1b8392783568b568c74f9f17571) = BIT(1) , [BT\_GAP\_ADV\_PROP\_DIRECTED](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba4595d3a3ea30bd4cd51ba4f1c4ab7de9) = BIT(2) , [BT\_GAP\_ADV\_PROP\_SCAN\_RESPONSE](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711ba55258ac9a7b355db87aeec5d443718f7) = BIT(3) ,     [BT\_GAP\_ADV\_PROP\_EXT\_ADV](group__bt__gap__defines.md#ggabf1a0417a549ec0a97263c2d990e711baeda2301e9eb191e742375e54bb765684) = BIT(4)   } |
|  | Advertising PDU properties. [More...](group__bt__gap__defines.md#gabf1a0417a549ec0a97263c2d990e711b) |
| enum | { [BT\_GAP\_CTE\_AOA](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966a8a82746ee64ffbcc62e79fdd8e0e30a0) = 0x00 , [BT\_GAP\_CTE\_AOD\_1US](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966aa8587383f9ea245e8c279fdd63417a19) = 0x01 , [BT\_GAP\_CTE\_AOD\_2US](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966a2385af24a5a82f4d799674443b92e966) = 0x02 , [BT\_GAP\_CTE\_NONE](group__bt__gap__defines.md#ggad30b9b6f60a1491bac4aa2c355072966aec9324d8e0997e1ace59895e168087e8) = 0xFF } |
|  | Constant Tone Extension (CTE) types. [More...](group__bt__gap__defines.md#gad30b9b6f60a1491bac4aa2c355072966) |
| enum | {     [BT\_GAP\_SCA\_UNKNOWN](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bace5a2d3f9fcb1a8913203ee6f437b910) = 0 , [BT\_GAP\_SCA\_251\_500](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba96900858c146259fc41af27b4cb62247) = 0 , [BT\_GAP\_SCA\_151\_250](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bab19b506bc13aad6af3dba925153f4e7d) = 1 , [BT\_GAP\_SCA\_101\_150](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba7f41d38c1a2125bd7c4d1765c8fbee73) = 2 ,     [BT\_GAP\_SCA\_76\_100](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6baa4011892d3409238f668c87626587bfd) = 3 , [BT\_GAP\_SCA\_51\_75](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba999a15d6ed8c860af7323af1b4d86fe9) = 4 , [BT\_GAP\_SCA\_31\_50](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba5fa53f708753d67bd6ec4f54b164b005) = 5 , [BT\_GAP\_SCA\_21\_30](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6ba164fe8b7df50d8e393373153a1f70d1d) = 6 ,     [BT\_GAP\_SCA\_0\_20](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bab8fd607ccdc30216fd90d4c6f568b9f6) = 7   } |
|  | Peripheral sleep clock accuracy (SCA) in ppm (parts per million). [More...](group__bt__gap__defines.md#gafa0d8b6c50823ebb6bd38340efbb5a6b) |

## Detailed Description

Bluetooth Generic Access Profile defines and Assigned Numbers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [gap.h](gap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
