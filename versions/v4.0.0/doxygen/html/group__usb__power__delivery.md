---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__usb__power__delivery.html
original_path: doxygen/html/group__usb__power__delivery.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB Power Delivery

[Device Driver APIs](group__io__interfaces.md)

USB Power Delivery.
[More...](#details)

| Data Structures | |
| --- | --- |
| union | [pd\_header](unionpd__header.md) |
|  | Build a PD message header See Table 6-1 Message Header. [More...](unionpd__header.md#details) |
| union | [pd\_ext\_header](unionpd__ext__header.md) |
|  | Build an extended message header See Table 6-3 Extended Message Header. [More...](unionpd__ext__header.md#details) |
| union | [pd\_fixed\_supply\_pdo\_source](unionpd__fixed__supply__pdo__source.md) |
|  | Create a Fixed Supply PDO Source value See Table 6-9 Fixed Supply PDO - Source. [More...](unionpd__fixed__supply__pdo__source.md#details) |
| union | [pd\_fixed\_supply\_pdo\_sink](unionpd__fixed__supply__pdo__sink.md) |
|  | Create a Fixed Supply PDO Sink value See Table 6-14 Fixed Supply PDO - Sink. [More...](unionpd__fixed__supply__pdo__sink.md#details) |
| union | [pd\_variable\_supply\_pdo\_source](unionpd__variable__supply__pdo__source.md) |
|  | Create a Variable Supply PDO Source value See Table 6-11 Variable Supply (non-Battery) PDO - Source. [More...](unionpd__variable__supply__pdo__source.md#details) |
| union | [pd\_variable\_supply\_pdo\_sink](unionpd__variable__supply__pdo__sink.md) |
|  | Create a Variable Supply PDO Sink value See Table 6-15 Variable Supply (non-Battery) PDO - Sink. [More...](unionpd__variable__supply__pdo__sink.md#details) |
| union | [pd\_battery\_supply\_pdo\_source](unionpd__battery__supply__pdo__source.md) |
|  | Create a Battery Supply PDO Source value See Table 6-12 Battery Supply PDO - Source. [More...](unionpd__battery__supply__pdo__source.md#details) |
| union | [pd\_battery\_supply\_pdo\_sink](unionpd__battery__supply__pdo__sink.md) |
|  | Create a Battery Supply PDO Sink value See Table 6-16 Battery Supply PDO - Sink. [More...](unionpd__battery__supply__pdo__sink.md#details) |
| union | [pd\_augmented\_supply\_pdo\_source](unionpd__augmented__supply__pdo__source.md) |
|  | Create Augmented Supply PDO Source value See Table 6-13 Programmable Power Supply APDO - Source. [More...](unionpd__augmented__supply__pdo__source.md#details) |
| union | [pd\_augmented\_supply\_pdo\_sink](unionpd__augmented__supply__pdo__sink.md) |
|  | Create Augmented Supply PDO Sink value See Table 6-17 Programmable Power Supply APDO - Sink. [More...](unionpd__augmented__supply__pdo__sink.md#details) |
| union | [pd\_rdo](unionpd__rdo.md) |
|  | The Request Data Object (RDO) Shall be returned by the Sink making a request for power. [More...](unionpd__rdo.md#details) |
| struct | [pd\_msg](structpd__msg.md) |
|  | Power Delivery message. [More...](structpd__msg.md#details) |

| Macros | |
| --- | --- |
| #define | [PD\_MAX\_EXTENDED\_MSG\_LEGACY\_LEN](#ga998b67d43674778e42f6c49ec6a99af4)   26 |
|  | Maximum length of a non-Extended Message in bytes. |
| #define | [PD\_MAX\_EXTENDED\_MSG\_LEN](#gabdb041542baaf2277e054dd9e3928b16)   260 |
|  | Maximum length of an Extended Message in bytes. |
| #define | [PD\_MAX\_EXTENDED\_MSG\_CHUNK\_LEN](#gac0588f94c1792b5b8fefa6a60c1b237b)   26 |
|  | Maximum length of a Chunked Message in bytes. |
| #define | [PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MIN\_MS](#ga266725d0496981ee92b0008afe43505e)   310 |
|  | Minimum time a sink shall wait for a Source\_Capabilities message before sending a Hard Reset See Table 6-61 Time Values Parameter Name: tTypeCSinkWaitCap. |
| #define | [PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MAX\_MS](#gae32afec56f34841200188e64dc1ab9ca)   620 |
|  | Minimum time a sink shall wait for a Source\_Capabilities message before sending a Hard Reset See Table 6-61 Time Values Parameter Name: tTypeCSinkWaitCap. |
| #define | [PD\_V\_SAFE\_0V\_MAX\_MV](#gac3a939394dab5a5038801f9a6b2dcd30)   800 |
|  | VBUS maximum safe operating voltage at "zero volts". |
| #define | [PD\_V\_SAFE\_5V\_MIN\_MV](#gad4f0e12b7f0e2ccd6aee73cf1525b27c)   4750 |
|  | VBUS minimum safe operating voltage at 5V. |
| #define | [PD\_T\_SAFE\_0V\_MAX\_MS](#gad5667f26343d4601c9fd5c5e9d046802)   650 |
|  | Time to reach PD\_V\_SAFE\_0V\_MV max in milliseconds. |
| #define | [PD\_T\_SAFE\_5V\_MAX\_MS](#ga123abee7651bca30a3e6ec2956eb0563)   275 |
|  | Time to reach PD\_V\_SAFE\_5V\_MV max in milliseconds. |
| #define | [PD\_T\_TX\_TIMEOUT\_MS](#gab6c168d490983a136c184bbe3ed9e7c5)   100 |
|  | Time to wait for TCPC to complete transmit. |
| #define | [PD\_T\_HARD\_RESET\_COMPLETE\_MIN\_MS](#ga64b8c095dba137d7fe460ffe38f00ce5)   4 |
|  | Minimum time a Hard Reset must complete. |
| #define | [PD\_T\_HARD\_RESET\_COMPLETE\_MAX\_MS](#ga2748e0775b50552cc7d26cb2b2d3103d)   5 |
|  | Maximum time a Hard Reset must complete. |
| #define | [PD\_T\_SENDER\_RESPONSE\_MIN\_MS](#ga9722df85c1a842ff1661e534e88d472e)   24 |
|  | Minimum time a response must be sent from a Port Partner See Table 6-68 Time Values. |
| #define | [PD\_T\_SENDER\_RESPONSE\_NOM\_MS](#gac905bf64de8a9f5acef6f8731c11d041)   27 |
|  | Nomiminal time a response must be sent from a Port Partner See Table 6-68 Time Values. |
| #define | [PD\_T\_SENDER\_RESPONSE\_MAX\_MS](#ga4b7c238e12770841b1852a0517b12071)   30 |
|  | Maximum time a response must be sent from a Port Partner See Table 6-68 Time Values. |
| #define | [PD\_T\_SPR\_PS\_TRANSITION\_MIN\_MS](#ga4726113aa8c0100fa1a88435d3a6b1d1)   450 |
|  | Minimum SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_SPR\_PS\_TRANSITION\_NOM\_MS](#ga01a2a71da7fdbe18d07dacb687f7d295)   500 |
|  | Nominal SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_SPR\_PS\_TRANSITION\_MAX\_MS](#ga7dac8d411d8f4651b177a6495146acb0)   550 |
|  | Maximum SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_EPR\_PS\_TRANSITION\_MIN\_MS](#ga7f9a916a88c626b76963a4950878fa20)   830 |
|  | Minimum EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_EPR\_PS\_TRANSITION\_NOM\_MS](#gabcd0576899a6ce1a147bffbb0c1b517f)   925 |
|  | Nominal EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_EPR\_PS\_TRANSITION\_MAX\_MS](#gaaea48ba7ea96b304b18293c202325b0e)   1020 |
|  | Maximum EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_SINK\_REQUEST\_MIN\_MS](#ga4416cfc999de1ee2ed49ce89f54074b1)   100 |
|  | Minimum time to wait before sending another request after receiving a Wait message See Table 6-68 Time Values. |
| #define | [PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MIN\_MS](#ga890ce7af4632f8a17b399f0821aee3cf)   40 |
|  | Minimum time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values. |
| #define | [PD\_T\_CHUNKING\_NOT\_SUPPORTED\_NOM\_MS](#gad13130dbd7f6ed4276b1781c5bf2fb20)   45 |
|  | Nominal time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values. |
| #define | [PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MAX\_MS](#gaf28df42c00394f9d11dfade2cae910d4)   50 |
|  | Maximum time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values. |
| #define | [PD\_CONVERT\_BYTES\_TO\_PD\_HEADER\_COUNT](#ga953bdd1d4893bebcaeb6b4b95667fd94)(c) |
|  | Convert bytes to PD Header data object count, where a data object is 4-bytes. |
| #define | [PD\_CONVERT\_PD\_HEADER\_COUNT\_TO\_BYTES](#gad5c5b108e4b255633a52d0de48adaf71)(c) |
|  | Convert PD Header data object count to bytes. |
| #define | [SINK\_TX\_OK](#ga69f749b5c7ecf6368002aae12277ac9f)   [TC\_RP\_3A0](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c) |
|  | Collision avoidance Rp values in REV 3.0 Sink Transmit "OK". |
| #define | [SINK\_TX\_NG](#gaa3ca6814e56859792dd5524fe8cef6b1)   [TC\_RP\_1A5](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28) |
|  | Collision avoidance Rp values in REV 3.0 Sink Transmit "NO GO". |
| #define | [PD\_GET\_EXT\_HEADER](#gaf3acdb691327adef04e418d7ded3d883)(c) |
|  | Used to get extended header from the first 32-bit word of the message. |
| #define | [PDO\_MAX\_DATA\_OBJECTS](#gab1716bb587e2b162415ea21e3c8d4e74)   7 |
|  | PDO - Power Data Object RDO - Request Data Object. |
| #define | [PD\_CONVERT\_MA\_TO\_FIXED\_PDO\_CURRENT](#ga65e9aa05457df787c5be6792ce725afd)(c) |
|  | Convert milliamps to Fixed PDO Current in 10mA units. |
| #define | [PD\_CONVERT\_MV\_TO\_FIXED\_PDO\_VOLTAGE](#gad79de03a60054be13c9757d933069fe2)(v) |
|  | Convert millivolts to Fixed PDO Voltage in 50mV units. |
| #define | [PD\_CONVERT\_FIXED\_PDO\_CURRENT\_TO\_MA](#gaa0997fc5d7f26115c64f220d2ab91ef2)(c) |
|  | Convert a Fixed PDO Current from 10mA units to milliamps. |
| #define | [PD\_CONVERT\_FIXED\_PDO\_VOLTAGE\_TO\_MV](#gae9eaed8554f857d183e24b96cd69afe3)(v) |
|  | Convert a Fixed PDO Voltage from 50mV units to millivolts. |
| #define | [PD\_CONVERT\_MA\_TO\_VARIABLE\_PDO\_CURRENT](#gab3ea3b392e8fc27b4f100a99988d0ca5)(c) |
|  | Convert milliamps to Variable PDO Current in 10ma units. |
| #define | [PD\_CONVERT\_MV\_TO\_VARIABLE\_PDO\_VOLTAGE](#gae729bb9b17bc0df4201ec27f1f506921)(v) |
|  | Convert millivolts to Variable PDO Voltage in 50mV units. |
| #define | [PD\_CONVERT\_VARIABLE\_PDO\_CURRENT\_TO\_MA](#ga9cd0c218385b400b3efe34474f546203)(c) |
|  | Convert a Variable PDO Current from 10mA units to milliamps. |
| #define | [PD\_CONVERT\_VARIABLE\_PDO\_VOLTAGE\_TO\_MV](#ga4973b120261cde51c86c7b76422222fc)(v) |
|  | Convert a Variable PDO Voltage from 50mV units to millivolts. |
| #define | [PD\_CONVERT\_MW\_TO\_BATTERY\_PDO\_POWER](#ga457907a516a2cf497569ce43561fe7dd)(c) |
|  | Convert milliwatts to Battery PDO Power in 250mW units. |
| #define | [PD\_CONVERT\_MV\_TO\_BATTERY\_PDO\_VOLTAGE](#ga4832aa2b18ff84bfcf3a252361628281)(v) |
|  | Convert milliwatts to Battery PDO Voltage in 50mV units. |
| #define | [PD\_CONVERT\_BATTERY\_PDO\_POWER\_TO\_MW](#ga614dd17b2b98309a837be8e0578bb06b)(c) |
|  | Convert a Battery PDO Power from 250mW units to milliwatts. |
| #define | [PD\_CONVERT\_BATTERY\_PDO\_VOLTAGE\_TO\_MV](#ga74af9a3f10f1855d7322dc36fabdff1a)(v) |
|  | Convert a Battery PDO Voltage from 50mV units to millivolts. |
| #define | [PD\_CONVERT\_MA\_TO\_AUGMENTED\_PDO\_CURRENT](#ga1d73d5ffc7e6657dae81604ffb49b358)(c) |
|  | Convert milliamps to Augmented PDO Current in 50mA units. |
| #define | [PD\_CONVERT\_MV\_TO\_AUGMENTED\_PDO\_VOLTAGE](#ga1dd7da9850daae859d572d866c8c87e2)(v) |
|  | Convert millivolts to Augmented PDO Voltage in 100mV units. |
| #define | [PD\_CONVERT\_AUGMENTED\_PDO\_CURRENT\_TO\_MA](#ga202d52036ee2fb6d6da3594c126cf82b)(c) |
|  | Convert an Augmented PDO Current from 50mA units to milliamps. |
| #define | [PD\_CONVERT\_AUGMENTED\_PDO\_VOLTAGE\_TO\_MV](#ga8623c319b19e7444ba400c738848d9ae)(v) |
|  | Convert an Augmented PDO Voltage from 100mV units to millivolts. |
| #define | [NUM\_SOP\_STAR\_TYPES](#ga1bb5fd6bb6657399a75b095eb3442bde)   ([PD\_PACKET\_DEBUG\_PRIME\_PRIME](#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1) + 1) |
|  | Number of valid Transmit Types. |

| Enumerations | |
| --- | --- |
| enum | [pdo\_type](#ga316dca7ed0b85f1aa224d7a767896328) { [PDO\_FIXED](#gga316dca7ed0b85f1aa224d7a767896328abbc517bb47b6bdc76e44b599523e0d93) = 0 , [PDO\_BATTERY](#gga316dca7ed0b85f1aa224d7a767896328a63f4fb7a4d2f7e265fd49be07966fbaa) = 1 , [PDO\_VARIABLE](#gga316dca7ed0b85f1aa224d7a767896328a1726efca9ece0ff017cc4aaf05ce9624) = 2 , [PDO\_AUGMENTED](#gga316dca7ed0b85f1aa224d7a767896328adb8478434cc1622e98bc22f4081dff1e) = 3 } |
|  | Power Data Object Type Table 6-7 Power Data Object. [More...](#ga316dca7ed0b85f1aa224d7a767896328) |
| enum | [pd\_frs\_type](#ga48b33240e19524ea003052103d310358) { [FRS\_NOT\_SUPPORTED](#gga48b33240e19524ea003052103d310358acbf2bf3ae21ff1ea51d7fd2b823ce726) , [FRS\_DEFAULT\_USB\_POWER](#gga48b33240e19524ea003052103d310358a4cd44f89f225f8869bfd901e7ea79aed) , [FRS\_1P5A\_5V](#gga48b33240e19524ea003052103d310358acac5008ded87d7a20b0b3b272075e4c1) , [FRS\_3P0A\_5V](#gga48b33240e19524ea003052103d310358a99ab2afc15809b5e89e3fb7106be37ba) } |
|  | Fast Role Swap Required for USB Type-C current. [More...](#ga48b33240e19524ea003052103d310358) |
| enum | [pd\_rev\_type](#gab68c6b6e33449c5ceadfc9217dd7a700) { [PD\_REV10](#ggab68c6b6e33449c5ceadfc9217dd7a700a1d9b4c553f44dccdc67e4edb554557b9) = 0 , [PD\_REV20](#ggab68c6b6e33449c5ceadfc9217dd7a700a22c122b1d30a3ab96fffd5dfa6bfb9ae) = 1 , [PD\_REV30](#ggab68c6b6e33449c5ceadfc9217dd7a700af3770bcbcf6feaaab272c022d7a57c7a) = 2 } |
|  | Protocol revision. [More...](#gab68c6b6e33449c5ceadfc9217dd7a700) |
| enum | [pd\_packet\_type](#gad2df13a24f0365198d37b10af608376b) {     [PD\_PACKET\_SOP](#ggad2df13a24f0365198d37b10af608376ba0bede6a56c24b06fdf56cf1dc386bb14) = 0 , [PD\_PACKET\_SOP\_PRIME](#ggad2df13a24f0365198d37b10af608376bae3a5f99242ab24a34706170101b38ef8) = 1 , [PD\_PACKET\_PRIME\_PRIME](#ggad2df13a24f0365198d37b10af608376ba5ecd663a9eecefcf965f605125d5188c) = 2 , [PD\_PACKET\_DEBUG\_PRIME](#ggad2df13a24f0365198d37b10af608376ba63b2200ebaf016d06437f3586d15171d) = 3 ,     [PD\_PACKET\_DEBUG\_PRIME\_PRIME](#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1) = 4 , [PD\_PACKET\_TX\_HARD\_RESET](#ggad2df13a24f0365198d37b10af608376baa5cd066e86fd55727c3625cd16633f73) = 5 , [PD\_PACKET\_CABLE\_RESET](#ggad2df13a24f0365198d37b10af608376ba531ebc6013984b81e6fb550618d6b4a8) = 6 , [PD\_PACKET\_TX\_BIST\_MODE\_2](#ggad2df13a24f0365198d37b10af608376bafcd21cc6b1ae6c58b86c0619d687e8fc) = 7 ,     [PD\_PACKET\_MSG\_INVALID](#ggad2df13a24f0365198d37b10af608376ba55bb88e5955992170bee96ddbe8a7437) = 0xf   } |
|  | Power Delivery packet type See USB Type-C Port Controller Interface Specification, Revision 2.0, Version 1.2, Table 4-38 TRANSMIT Register Definition. [More...](#gad2df13a24f0365198d37b10af608376b) |
| enum | [pd\_ctrl\_msg\_type](#ga4c7862a3e953fb22534123223c942f9a) {     [PD\_CTRL\_GOOD\_CRC](#gga4c7862a3e953fb22534123223c942f9aae0895be53e5a1e54731e9608a8e0c6c9) = 1 , [PD\_CTRL\_GOTO\_MIN](#gga4c7862a3e953fb22534123223c942f9aa4ba7f63cdcbe766a34047e06145a591e) = 2 , [PD\_CTRL\_ACCEPT](#gga4c7862a3e953fb22534123223c942f9aa56df68ed627b56bbcfc20900ec5d2e5d) = 3 , [PD\_CTRL\_REJECT](#gga4c7862a3e953fb22534123223c942f9aa9dd7b559e78a99639056325a7be14d81) = 4 ,     [PD\_CTRL\_PING](#gga4c7862a3e953fb22534123223c942f9aa8177040ca8a1f71dde67fc59060c35ed) = 5 , [PD\_CTRL\_PS\_RDY](#gga4c7862a3e953fb22534123223c942f9aafc449fc3dc39f2495494507cc97f53ad) = 6 , [PD\_CTRL\_GET\_SOURCE\_CAP](#gga4c7862a3e953fb22534123223c942f9aa9324307526500683ae265e9cb0063929) = 7 , [PD\_CTRL\_GET\_SINK\_CAP](#gga4c7862a3e953fb22534123223c942f9aaaf5c221569a9108bdbc36545dcb37495) = 8 ,     [PD\_CTRL\_DR\_SWAP](#gga4c7862a3e953fb22534123223c942f9aa4aba967f7e363dbbadcc9a9ecf0c7ae4) = 9 , [PD\_CTRL\_PR\_SWAP](#gga4c7862a3e953fb22534123223c942f9aade67c4fb153e5ba87b6d6643f99260f9) = 10 , [PD\_CTRL\_VCONN\_SWAP](#gga4c7862a3e953fb22534123223c942f9aa68820e99ce9c1c73180734372e5ede2b) = 11 , [PD\_CTRL\_WAIT](#gga4c7862a3e953fb22534123223c942f9aa3b6fc49b1ae0bb343d39476350b59c90) = 12 ,     [PD\_CTRL\_SOFT\_RESET](#gga4c7862a3e953fb22534123223c942f9aadeb12ed01ec54ee55588bfb796dd0c11) = 13 , [PD\_CTRL\_DATA\_RESET](#gga4c7862a3e953fb22534123223c942f9aa03f9886881aa493fb0f9bfac16713e7a) = 14 , [PD\_CTRL\_DATA\_RESET\_COMPLETE](#gga4c7862a3e953fb22534123223c942f9aa27caca37f9522045bc8612f7536cd792) = 15 , [PD\_CTRL\_NOT\_SUPPORTED](#gga4c7862a3e953fb22534123223c942f9aabfea5fdf0263fdf4c924bd603ee7256f) = 16 ,     [PD\_CTRL\_GET\_SOURCE\_CAP\_EXT](#gga4c7862a3e953fb22534123223c942f9aab0ca2628b144d092116b461703176eaa) = 17 , [PD\_CTRL\_GET\_STATUS](#gga4c7862a3e953fb22534123223c942f9aa23287276ee22241906828515f38fedef) = 18 , [PD\_CTRL\_FR\_SWAP](#gga4c7862a3e953fb22534123223c942f9aa1c597b5f953e6e1791aa869025b98b24) = 19 , [PD\_CTRL\_GET\_PPS\_STATUS](#gga4c7862a3e953fb22534123223c942f9aab82efb96b1f8f7dae3c76e362ae1715a) = 20 ,     [PD\_CTRL\_GET\_COUNTRY\_CODES](#gga4c7862a3e953fb22534123223c942f9aa677ebc41b4b67de6ee93b5e446af702e) = 21 , [PD\_CTRL\_GET\_SINK\_CAP\_EXT](#gga4c7862a3e953fb22534123223c942f9aaaa0a5bba9a9f1573952141c4f8f77318) = 22   } |
|  | Control Message type See Table 6-5 Control Message Types. [More...](#ga4c7862a3e953fb22534123223c942f9a) |
| enum | [pd\_data\_msg\_type](#ga8239651864b4cb0e1fc89ba2d7e59462) {     [PD\_DATA\_SOURCE\_CAP](#gga8239651864b4cb0e1fc89ba2d7e59462ad9a0cf16cfa852111ea0ed3434b35dfc) = 1 , [PD\_DATA\_REQUEST](#gga8239651864b4cb0e1fc89ba2d7e59462ad9c920f987e2578b030cc08f2e69998a) = 2 , [PD\_DATA\_BIST](#gga8239651864b4cb0e1fc89ba2d7e59462a7c4bc907fb81082da05c64797854be9f) = 3 , [PD\_DATA\_SINK\_CAP](#gga8239651864b4cb0e1fc89ba2d7e59462a4cf30dcbce3fdf8076713e45d242b39a) = 4 ,     [PD\_DATA\_BATTERY\_STATUS](#gga8239651864b4cb0e1fc89ba2d7e59462ad493f01ffc4c3c164f874eb202f8adb0) = 5 , [PD\_DATA\_ALERT](#gga8239651864b4cb0e1fc89ba2d7e59462a7e3368e1c7bde4c6bb3136cb80209bb6) = 6 , [PD\_DATA\_GET\_COUNTRY\_INFO](#gga8239651864b4cb0e1fc89ba2d7e59462a83d7098236e97972cf24b900f7e5e069) = 7 , [PD\_DATA\_ENTER\_USB](#gga8239651864b4cb0e1fc89ba2d7e59462a1a0829560f9f82182f7587fd8787a846) = 8 ,     [PD\_DATA\_VENDOR\_DEF](#gga8239651864b4cb0e1fc89ba2d7e59462a881fcbc2dc5f8b1de7c97522df46242d) = 15   } |
|  | Data message type See Table 6-6 Data Message Types. [More...](#ga8239651864b4cb0e1fc89ba2d7e59462) |
| enum | [pd\_ext\_msg\_type](#ga457308d50365e0a2440e94e41a316cbf) {     [PD\_EXT\_SOURCE\_CAP](#gga457308d50365e0a2440e94e41a316cbfa51c03e44c3fe1bb59445bbc452ea7199) = 1 , [PD\_EXT\_STATUS](#gga457308d50365e0a2440e94e41a316cbfa836130da5307aed6160deadadf2f4f3f) = 2 , [PD\_EXT\_GET\_BATTERY\_CAP](#gga457308d50365e0a2440e94e41a316cbfa9c50488735d7723c3cc30f176c221e40) = 3 , [PD\_EXT\_GET\_BATTERY\_STATUS](#gga457308d50365e0a2440e94e41a316cbfa77ff801aa819461f0f5ff44546370bd7) = 4 ,     [PD\_EXT\_BATTERY\_CAP](#gga457308d50365e0a2440e94e41a316cbfae7f7b3f7233bb5cf600338b4a2c601c0) = 5 , [PD\_EXT\_GET\_MANUFACTURER\_INFO](#gga457308d50365e0a2440e94e41a316cbfac8fc4c3c64fb3eaba8cb61bd999c7033) = 6 , [PD\_EXT\_MANUFACTURER\_INFO](#gga457308d50365e0a2440e94e41a316cbfa500d77f178123eab8073058dd9308ea6) = 7 , [PD\_EXT\_SECURITY\_REQUEST](#gga457308d50365e0a2440e94e41a316cbfa0f62aa3774995018514dcd2f75ac1c1f) = 8 ,     [PD\_EXT\_SECURITY\_RESPONSE](#gga457308d50365e0a2440e94e41a316cbfad002882e8bce9cdfdb0864cd6a3e79a7) = 9 , [PD\_EXT\_FIRMWARE\_UPDATE\_REQUEST](#gga457308d50365e0a2440e94e41a316cbfa2a7b6a78cf3fd87a86f060f927b566af) = 10 , [PD\_EXT\_FIRMWARE\_UPDATE\_RESPONSE](#gga457308d50365e0a2440e94e41a316cbfa4fe2d7028fa2bdf594cb8c87ac05fe67) = 11 , [PD\_EXT\_PPS\_STATUS](#gga457308d50365e0a2440e94e41a316cbfa7d04da3fdb96eac97200d11eb2dbe083) = 12 ,     [PD\_EXT\_COUNTRY\_INFO](#gga457308d50365e0a2440e94e41a316cbfaa21adc92574ed1261b6c13df3592601b) = 13 , [PD\_EXT\_COUNTRY\_CODES](#gga457308d50365e0a2440e94e41a316cbfae69b4a8ddba29bc6cd69d50c946bc658) = 14   } |
|  | Extended message type for REV 3.0 See Table 6-48 Extended Message Types. [More...](#ga457308d50365e0a2440e94e41a316cbf) |
| enum | [usbpd\_cc\_pin](#gaee2fe2128557939404c62e8104269bbf) { [USBPD\_CC\_PIN\_1](#ggaee2fe2128557939404c62e8104269bbfa59a0ed05c4e99acebaa11080dbbe7694) = 0 , [USBPD\_CC\_PIN\_2](#ggaee2fe2128557939404c62e8104269bbfa53a0a6ba0212b9cbb407522e7f35648e) = 1 } |
|  | Active PD CC pin. [More...](#gaee2fe2128557939404c62e8104269bbf) |

| USB PD 3.1 Rev 1.6, Table 6-70 Counter Parameters | |
| --- | --- |
| #define | [PD\_N\_CAPS\_COUNT](#gac517b081df0572803efb374839846f1f)   50 |
|  | The CapsCounter is used to count the number of Source\_Capabilities Messages which have been sent by a Source at power up or after a Hard Reset. |
| #define | [PD\_N\_HARD\_RESET\_COUNT](#gae4f479f2e77066a9b870263e3580f03f)   2 |
|  | The HardResetCounter is used to retry the Hard Reset whenever there is no response from the remote device (see Section 6.6.6) Parameter Name: nHardResetCounter. |

| USB PD 3.1 Rev 1.6, Table 6-68 Time Values | |
| --- | --- |
| #define | [PD\_T\_NO\_RESPONSE\_MIN\_MS](#ga9dfd6527539e996ccc110036545e61e7)   4500 |
|  | The NoResponseTimer is used by the Policy Engine in a Source to determine that its Port Partner is not responding after a Hard Reset. |
| #define | [PD\_T\_NO\_RESPONSE\_MAX\_MS](#gaed69627505bdad8fb87c37084e2222e1)   5500 |
|  | The NoResponseTimer is used by the Policy Engine in a Source to determine that its Port Partner is not responding after a Hard Reset. |
| #define | [PD\_T\_PS\_HARD\_RESET\_MIN\_MS](#ga87d0eb341d76c01b4b355c1d5a0354a1)   25 |
|  | Min time the Source waits to ensure that the Sink has had sufficient time to process Hard Reset Signaling before turning off its power supply to VBUS Parameter Name: tPSHardReset. |
| #define | [PD\_T\_PS\_HARD\_RESET\_MAX\_MS](#ga2c4abfef3a581e19677d8f0d845a3582)   35 |
|  | Max time the Source waits to ensure that the Sink has had sufficient time to process Hard Reset Signaling before turning off its power supply to VBUS Parameter Name: tPSHardReset. |
| #define | [PD\_T\_SINK\_TX\_MIN\_MS](#gae7db10623f2ec064ef0351bb1bba51cd)   16 |
|  | Minimum time a Source waits after changing Rp from SinkTxOk to SinkTxNG before initiating an AMS by sending a Message. |
| #define | [PD\_T\_SINK\_TX\_MAX\_MS](#gadb55b3f260a17458bf479a7273fd946c)   20 |
|  | Maximum time a Source waits after changing Rp from SinkTxOk to SinkTxNG before initiating an AMS by sending a Message. |
| #define | [PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MIN\_MS](#gabe6d36578671578eddf1381f58bcc80a)   100 |
|  | Minimum time a source shall wait before sending a Source\_Capabilities message while the following is true: 1) The Port is Attached. |
| #define | [PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MAX\_MS](#ga105a9791e086ade590b6fd825fe5cded)   200 |
|  | Maximum time a source shall wait before sending a Source\_Capabilities message while the following is true: 1) The Port is Attached. |

## Detailed Description

USB Power Delivery.

## Macro Definition Documentation

## [◆ ](#ga1bb5fd6bb6657399a75b095eb3442bde)NUM\_SOP\_STAR\_TYPES

| #define NUM\_SOP\_STAR\_TYPES   ([PD\_PACKET\_DEBUG\_PRIME\_PRIME](#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1) + 1) |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Number of valid Transmit Types.

## [◆ ](#ga202d52036ee2fb6d6da3594c126cf82b)PD\_CONVERT\_AUGMENTED\_PDO\_CURRENT\_TO\_MA

| #define PD\_CONVERT\_AUGMENTED\_PDO\_CURRENT\_TO\_MA | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((c) \* 50)

Convert an Augmented PDO Current from 50mA units to milliamps.

Parameters
:   | c | Augmented PDO current in 50mA units. |
    | --- | --- |

## [◆ ](#ga8623c319b19e7444ba400c738848d9ae)PD\_CONVERT\_AUGMENTED\_PDO\_VOLTAGE\_TO\_MV

| #define PD\_CONVERT\_AUGMENTED\_PDO\_VOLTAGE\_TO\_MV | ( |  | *v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((v) \* 100)

Convert an Augmented PDO Voltage from 100mV units to millivolts.

Parameters
:   | v | Augmented PDO voltage in 100mV units. |
    | --- | --- |

## [◆ ](#ga614dd17b2b98309a837be8e0578bb06b)PD\_CONVERT\_BATTERY\_PDO\_POWER\_TO\_MW

| #define PD\_CONVERT\_BATTERY\_PDO\_POWER\_TO\_MW | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((c) \* 250)

Convert a Battery PDO Power from 250mW units to milliwatts.

Parameters
:   | c | Power in 250mW units. |
    | --- | --- |

## [◆ ](#ga74af9a3f10f1855d7322dc36fabdff1a)PD\_CONVERT\_BATTERY\_PDO\_VOLTAGE\_TO\_MV

| #define PD\_CONVERT\_BATTERY\_PDO\_VOLTAGE\_TO\_MV | ( |  | *v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((v) \* 50)

Convert a Battery PDO Voltage from 50mV units to millivolts.

Parameters
:   | v | Voltage in 50mV units. |
    | --- | --- |

## [◆ ](#ga953bdd1d4893bebcaeb6b4b95667fd94)PD\_CONVERT\_BYTES\_TO\_PD\_HEADER\_COUNT

| #define PD\_CONVERT\_BYTES\_TO\_PD\_HEADER\_COUNT | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((c) >> 2)

Convert bytes to PD Header data object count, where a data object is 4-bytes.

Parameters
:   | c | number of bytes to convert |
    | --- | --- |

## [◆ ](#gaa0997fc5d7f26115c64f220d2ab91ef2)PD\_CONVERT\_FIXED\_PDO\_CURRENT\_TO\_MA

| #define PD\_CONVERT\_FIXED\_PDO\_CURRENT\_TO\_MA | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((c) \* 10)

Convert a Fixed PDO Current from 10mA units to milliamps.

Parameters
:   | c | Fixed PDO current in 10mA units. |
    | --- | --- |

## [◆ ](#gae9eaed8554f857d183e24b96cd69afe3)PD\_CONVERT\_FIXED\_PDO\_VOLTAGE\_TO\_MV

| #define PD\_CONVERT\_FIXED\_PDO\_VOLTAGE\_TO\_MV | ( |  | *v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((v) \* 50)

Convert a Fixed PDO Voltage from 50mV units to millivolts.

Used for converting [pd\_fixed\_supply\_pdo\_source.voltage](unionpd__fixed__supply__pdo__source.md#a66f55e177b6f2bc76b392707e39fa4fe "Voltage in 50mV units.") and [pd\_fixed\_supply\_pdo\_sink.voltage](unionpd__fixed__supply__pdo__sink.md#ac47dcf98dfca90eb0e6013a3e1c5eb18 "Voltage in 50mV units.")

Parameters
:   | v | Fixed PDO voltage in 50mV units. |
    | --- | --- |

## [◆ ](#ga1d73d5ffc7e6657dae81604ffb49b358)PD\_CONVERT\_MA\_TO\_AUGMENTED\_PDO\_CURRENT

| #define PD\_CONVERT\_MA\_TO\_AUGMENTED\_PDO\_CURRENT | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((c) / 50)

Convert milliamps to Augmented PDO Current in 50mA units.

Parameters
:   | c | Current in milliamps |
    | --- | --- |

## [◆ ](#ga65e9aa05457df787c5be6792ce725afd)PD\_CONVERT\_MA\_TO\_FIXED\_PDO\_CURRENT

| #define PD\_CONVERT\_MA\_TO\_FIXED\_PDO\_CURRENT | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((c) / 10)

Convert milliamps to Fixed PDO Current in 10mA units.

Parameters
:   | c | Current in milliamps |
    | --- | --- |

## [◆ ](#gab3ea3b392e8fc27b4f100a99988d0ca5)PD\_CONVERT\_MA\_TO\_VARIABLE\_PDO\_CURRENT

| #define PD\_CONVERT\_MA\_TO\_VARIABLE\_PDO\_CURRENT | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((c) / 10)

Convert milliamps to Variable PDO Current in 10ma units.

Parameters
:   | c | Current in milliamps |
    | --- | --- |

## [◆ ](#ga1dd7da9850daae859d572d866c8c87e2)PD\_CONVERT\_MV\_TO\_AUGMENTED\_PDO\_VOLTAGE

| #define PD\_CONVERT\_MV\_TO\_AUGMENTED\_PDO\_VOLTAGE | ( |  | *v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((v) / 100)

Convert millivolts to Augmented PDO Voltage in 100mV units.

Parameters
:   | v | Voltage in millivolts |
    | --- | --- |

## [◆ ](#ga4832aa2b18ff84bfcf3a252361628281)PD\_CONVERT\_MV\_TO\_BATTERY\_PDO\_VOLTAGE

| #define PD\_CONVERT\_MV\_TO\_BATTERY\_PDO\_VOLTAGE | ( |  | *v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((v) / 50)

Convert milliwatts to Battery PDO Voltage in 50mV units.

Parameters
:   | v | Voltage in millivolts |
    | --- | --- |

## [◆ ](#gad79de03a60054be13c9757d933069fe2)PD\_CONVERT\_MV\_TO\_FIXED\_PDO\_VOLTAGE

| #define PD\_CONVERT\_MV\_TO\_FIXED\_PDO\_VOLTAGE | ( |  | *v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((v) / 50)

Convert millivolts to Fixed PDO Voltage in 50mV units.

Parameters
:   | v | Voltage in millivolts |
    | --- | --- |

## [◆ ](#gae729bb9b17bc0df4201ec27f1f506921)PD\_CONVERT\_MV\_TO\_VARIABLE\_PDO\_VOLTAGE

| #define PD\_CONVERT\_MV\_TO\_VARIABLE\_PDO\_VOLTAGE | ( |  | *v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((v) / 50)

Convert millivolts to Variable PDO Voltage in 50mV units.

Parameters
:   | v | Voltage in millivolts |
    | --- | --- |

## [◆ ](#ga457907a516a2cf497569ce43561fe7dd)PD\_CONVERT\_MW\_TO\_BATTERY\_PDO\_POWER

| #define PD\_CONVERT\_MW\_TO\_BATTERY\_PDO\_POWER | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((c) / 250)

Convert milliwatts to Battery PDO Power in 250mW units.

Parameters
:   | c | Power in milliwatts |
    | --- | --- |

## [◆ ](#gad5c5b108e4b255633a52d0de48adaf71)PD\_CONVERT\_PD\_HEADER\_COUNT\_TO\_BYTES

| #define PD\_CONVERT\_PD\_HEADER\_COUNT\_TO\_BYTES | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((c) << 2)

Convert PD Header data object count to bytes.

Parameters
:   | c | number of PD Header data objects |
    | --- | --- |

## [◆ ](#ga9cd0c218385b400b3efe34474f546203)PD\_CONVERT\_VARIABLE\_PDO\_CURRENT\_TO\_MA

| #define PD\_CONVERT\_VARIABLE\_PDO\_CURRENT\_TO\_MA | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((c) \* 10)

Convert a Variable PDO Current from 10mA units to milliamps.

Parameters
:   | c | Variable PDO current in 10mA units. |
    | --- | --- |

## [◆ ](#ga4973b120261cde51c86c7b76422222fc)PD\_CONVERT\_VARIABLE\_PDO\_VOLTAGE\_TO\_MV

| #define PD\_CONVERT\_VARIABLE\_PDO\_VOLTAGE\_TO\_MV | ( |  | *v* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((v) \* 50)

Convert a Variable PDO Voltage from 50mV units to millivolts.

Parameters
:   | v | Variable PDO voltage in 50mV units. |
    | --- | --- |

## [◆ ](#gaf3acdb691327adef04e418d7ded3d883)PD\_GET\_EXT\_HEADER

| #define PD\_GET\_EXT\_HEADER | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

**Value:**

((c) & 0xffff)

Used to get extended header from the first 32-bit word of the message.

Parameters
:   | c | first 32-bit word of the message |
    | --- | --- |

## [◆ ](#gac0588f94c1792b5b8fefa6a60c1b237b)PD\_MAX\_EXTENDED\_MSG\_CHUNK\_LEN

| #define PD\_MAX\_EXTENDED\_MSG\_CHUNK\_LEN   26 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Maximum length of a Chunked Message in bytes.

When one of both Port Partners do not support Extended Messages of Data Size greater than PD\_MAX\_EXTENDED\_MSG\_LEGACY\_LEN then the Protocol Layer supports a Chunking mechanism to break larger Messages into smaller Chunks of size PD\_MAX\_EXTENDED\_MSG\_CHUNK\_LEN. See Table 6-75 Value Parameters Parameter Name: MaxExtendedMsgChunkLen

## [◆ ](#ga998b67d43674778e42f6c49ec6a99af4)PD\_MAX\_EXTENDED\_MSG\_LEGACY\_LEN

| #define PD\_MAX\_EXTENDED\_MSG\_LEGACY\_LEN   26 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Maximum length of a non-Extended Message in bytes.

See Table 6-75 Value Parameters Parameter Name: MaxExtendedMsgLegacyLen

## [◆ ](#gabdb041542baaf2277e054dd9e3928b16)PD\_MAX\_EXTENDED\_MSG\_LEN

| #define PD\_MAX\_EXTENDED\_MSG\_LEN   260 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Maximum length of an Extended Message in bytes.

See Table 6-75 Value Parameters Parameter Name: MaxExtendedMsgLen

## [◆ ](#gac517b081df0572803efb374839846f1f)PD\_N\_CAPS\_COUNT

| #define PD\_N\_CAPS\_COUNT   50 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

The CapsCounter is used to count the number of Source\_Capabilities Messages which have been sent by a Source at power up or after a Hard Reset.

Parameter Name: nCapsCounter

## [◆ ](#gae4f479f2e77066a9b870263e3580f03f)PD\_N\_HARD\_RESET\_COUNT

| #define PD\_N\_HARD\_RESET\_COUNT   2 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

The HardResetCounter is used to retry the Hard Reset whenever there is no response from the remote device (see Section 6.6.6) Parameter Name: nHardResetCounter.

## [◆ ](#gaf28df42c00394f9d11dfade2cae910d4)PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MAX\_MS

| #define PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MAX\_MS   50 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Maximum time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values.

## [◆ ](#ga890ce7af4632f8a17b399f0821aee3cf)PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MIN\_MS

| #define PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MIN\_MS   40 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Minimum time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values.

## [◆ ](#gad13130dbd7f6ed4276b1781c5bf2fb20)PD\_T\_CHUNKING\_NOT\_SUPPORTED\_NOM\_MS

| #define PD\_T\_CHUNKING\_NOT\_SUPPORTED\_NOM\_MS   45 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Nominal time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values.

## [◆ ](#gaaea48ba7ea96b304b18293c202325b0e)PD\_T\_EPR\_PS\_TRANSITION\_MAX\_MS

| #define PD\_T\_EPR\_PS\_TRANSITION\_MAX\_MS   1020 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Maximum EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

## [◆ ](#ga7f9a916a88c626b76963a4950878fa20)PD\_T\_EPR\_PS\_TRANSITION\_MIN\_MS

| #define PD\_T\_EPR\_PS\_TRANSITION\_MIN\_MS   830 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Minimum EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

## [◆ ](#gabcd0576899a6ce1a147bffbb0c1b517f)PD\_T\_EPR\_PS\_TRANSITION\_NOM\_MS

| #define PD\_T\_EPR\_PS\_TRANSITION\_NOM\_MS   925 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Nominal EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

## [◆ ](#ga2748e0775b50552cc7d26cb2b2d3103d)PD\_T\_HARD\_RESET\_COMPLETE\_MAX\_MS

| #define PD\_T\_HARD\_RESET\_COMPLETE\_MAX\_MS   5 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Maximum time a Hard Reset must complete.

See Table 6-68 Time Values

## [◆ ](#ga64b8c095dba137d7fe460ffe38f00ce5)PD\_T\_HARD\_RESET\_COMPLETE\_MIN\_MS

| #define PD\_T\_HARD\_RESET\_COMPLETE\_MIN\_MS   4 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Minimum time a Hard Reset must complete.

See Table 6-68 Time Values

## [◆ ](#gaed69627505bdad8fb87c37084e2222e1)PD\_T\_NO\_RESPONSE\_MAX\_MS

| #define PD\_T\_NO\_RESPONSE\_MAX\_MS   5500 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

The NoResponseTimer is used by the Policy Engine in a Source to determine that its Port Partner is not responding after a Hard Reset.

Parameter Name: tNoResponseTimer

## [◆ ](#ga9dfd6527539e996ccc110036545e61e7)PD\_T\_NO\_RESPONSE\_MIN\_MS

| #define PD\_T\_NO\_RESPONSE\_MIN\_MS   4500 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

The NoResponseTimer is used by the Policy Engine in a Source to determine that its Port Partner is not responding after a Hard Reset.

Parameter Name: tNoResponseTimer

## [◆ ](#ga2c4abfef3a581e19677d8f0d845a3582)PD\_T\_PS\_HARD\_RESET\_MAX\_MS

| #define PD\_T\_PS\_HARD\_RESET\_MAX\_MS   35 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Max time the Source waits to ensure that the Sink has had sufficient time to process Hard Reset Signaling before turning off its power supply to VBUS Parameter Name: tPSHardReset.

## [◆ ](#ga87d0eb341d76c01b4b355c1d5a0354a1)PD\_T\_PS\_HARD\_RESET\_MIN\_MS

| #define PD\_T\_PS\_HARD\_RESET\_MIN\_MS   25 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Min time the Source waits to ensure that the Sink has had sufficient time to process Hard Reset Signaling before turning off its power supply to VBUS Parameter Name: tPSHardReset.

## [◆ ](#gad5667f26343d4601c9fd5c5e9d046802)PD\_T\_SAFE\_0V\_MAX\_MS

| #define PD\_T\_SAFE\_0V\_MAX\_MS   650 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Time to reach PD\_V\_SAFE\_0V\_MV max in milliseconds.

See Table 7-24 Common Source/Sink Electrical Parameters Parameter Name: tSafe0V

## [◆ ](#ga123abee7651bca30a3e6ec2956eb0563)PD\_T\_SAFE\_5V\_MAX\_MS

| #define PD\_T\_SAFE\_5V\_MAX\_MS   275 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Time to reach PD\_V\_SAFE\_5V\_MV max in milliseconds.

See Table 7-24 Common Source/Sink Electrical Parameters Parameter Name: tSafe5V

## [◆ ](#ga4b7c238e12770841b1852a0517b12071)PD\_T\_SENDER\_RESPONSE\_MAX\_MS

| #define PD\_T\_SENDER\_RESPONSE\_MAX\_MS   30 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Maximum time a response must be sent from a Port Partner See Table 6-68 Time Values.

## [◆ ](#ga9722df85c1a842ff1661e534e88d472e)PD\_T\_SENDER\_RESPONSE\_MIN\_MS

| #define PD\_T\_SENDER\_RESPONSE\_MIN\_MS   24 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Minimum time a response must be sent from a Port Partner See Table 6-68 Time Values.

## [◆ ](#gac905bf64de8a9f5acef6f8731c11d041)PD\_T\_SENDER\_RESPONSE\_NOM\_MS

| #define PD\_T\_SENDER\_RESPONSE\_NOM\_MS   27 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Nomiminal time a response must be sent from a Port Partner See Table 6-68 Time Values.

## [◆ ](#ga4416cfc999de1ee2ed49ce89f54074b1)PD\_T\_SINK\_REQUEST\_MIN\_MS

| #define PD\_T\_SINK\_REQUEST\_MIN\_MS   100 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Minimum time to wait before sending another request after receiving a Wait message See Table 6-68 Time Values.

## [◆ ](#gadb55b3f260a17458bf479a7273fd946c)PD\_T\_SINK\_TX\_MAX\_MS

| #define PD\_T\_SINK\_TX\_MAX\_MS   20 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Maximum time a Source waits after changing Rp from SinkTxOk to SinkTxNG before initiating an AMS by sending a Message.

Parameter Name: tSinkTx

## [◆ ](#gae7db10623f2ec064ef0351bb1bba51cd)PD\_T\_SINK\_TX\_MIN\_MS

| #define PD\_T\_SINK\_TX\_MIN\_MS   16 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Minimum time a Source waits after changing Rp from SinkTxOk to SinkTxNG before initiating an AMS by sending a Message.

Parameter Name: tSinkTx

## [◆ ](#ga7dac8d411d8f4651b177a6495146acb0)PD\_T\_SPR\_PS\_TRANSITION\_MAX\_MS

| #define PD\_T\_SPR\_PS\_TRANSITION\_MAX\_MS   550 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Maximum SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

## [◆ ](#ga4726113aa8c0100fa1a88435d3a6b1d1)PD\_T\_SPR\_PS\_TRANSITION\_MIN\_MS

| #define PD\_T\_SPR\_PS\_TRANSITION\_MIN\_MS   450 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Minimum SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

## [◆ ](#ga01a2a71da7fdbe18d07dacb687f7d295)PD\_T\_SPR\_PS\_TRANSITION\_NOM\_MS

| #define PD\_T\_SPR\_PS\_TRANSITION\_NOM\_MS   500 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Nominal SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values.

## [◆ ](#gab6c168d490983a136c184bbe3ed9e7c5)PD\_T\_TX\_TIMEOUT\_MS

| #define PD\_T\_TX\_TIMEOUT\_MS   100 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Time to wait for TCPC to complete transmit.

## [◆ ](#ga105a9791e086ade590b6fd825fe5cded)PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MAX\_MS

| #define PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MAX\_MS   200 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Maximum time a source shall wait before sending a Source\_Capabilities message while the following is true: 1) The Port is Attached.

2) The Source is not in an active connection with a PD Sink Port. Parameter Name: tTypeCSendSourceCap

## [◆ ](#gabe6d36578671578eddf1381f58bcc80a)PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MIN\_MS

| #define PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MIN\_MS   100 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Minimum time a source shall wait before sending a Source\_Capabilities message while the following is true: 1) The Port is Attached.

2) The Source is not in an active connection with a PD Sink Port. Parameter Name: tTypeCSendSourceCap

## [◆ ](#gae32afec56f34841200188e64dc1ab9ca)PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MAX\_MS

| #define PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MAX\_MS   620 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Minimum time a sink shall wait for a Source\_Capabilities message before sending a Hard Reset See Table 6-61 Time Values Parameter Name: tTypeCSinkWaitCap.

## [◆ ](#ga266725d0496981ee92b0008afe43505e)PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MIN\_MS

| #define PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MIN\_MS   310 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Minimum time a sink shall wait for a Source\_Capabilities message before sending a Hard Reset See Table 6-61 Time Values Parameter Name: tTypeCSinkWaitCap.

## [◆ ](#gac3a939394dab5a5038801f9a6b2dcd30)PD\_V\_SAFE\_0V\_MAX\_MV

| #define PD\_V\_SAFE\_0V\_MAX\_MV   800 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

VBUS maximum safe operating voltage at "zero volts".

See Table 7-24 Common Source/Sink Electrical Parameters Parameter Name: vSafe0V

## [◆ ](#gad4f0e12b7f0e2ccd6aee73cf1525b27c)PD\_V\_SAFE\_5V\_MIN\_MV

| #define PD\_V\_SAFE\_5V\_MIN\_MV   4750 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

VBUS minimum safe operating voltage at 5V.

See Table 7-24 Common Source/Sink Electrical Parameters Parameter Name: vSafe5V

## [◆ ](#gab1716bb587e2b162415ea21e3c8d4e74)PDO\_MAX\_DATA\_OBJECTS

| #define PDO\_MAX\_DATA\_OBJECTS   7 |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

PDO - Power Data Object RDO - Request Data Object.

Maximum number of 32-bit data objects sent in a single request

## [◆ ](#gaa3ca6814e56859792dd5524fe8cef6b1)SINK\_TX\_NG

| #define SINK\_TX\_NG   [TC\_RP\_1A5](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28) |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Collision avoidance Rp values in REV 3.0 Sink Transmit "NO GO".

## [◆ ](#ga69f749b5c7ecf6368002aae12277ac9f)SINK\_TX\_OK

| #define SINK\_TX\_OK   [TC\_RP\_3A0](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c) |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Collision avoidance Rp values in REV 3.0 Sink Transmit "OK".

## Enumeration Type Documentation

## [◆ ](#ga4c7862a3e953fb22534123223c942f9a)pd\_ctrl\_msg\_type

| enum [pd\_ctrl\_msg\_type](#ga4c7862a3e953fb22534123223c942f9a) |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Control Message type See Table 6-5 Control Message Types.

| Enumerator | |
| --- | --- |
| PD\_CTRL\_GOOD\_CRC | 0 Reserved  GoodCRC Message |
| PD\_CTRL\_GOTO\_MIN | GotoMin Message. |
| PD\_CTRL\_ACCEPT | Accept Message. |
| PD\_CTRL\_REJECT | Reject Message. |
| PD\_CTRL\_PING | Ping Message. |
| PD\_CTRL\_PS\_RDY | PS\_RDY Message. |
| PD\_CTRL\_GET\_SOURCE\_CAP | Get\_Source\_Cap Message. |
| PD\_CTRL\_GET\_SINK\_CAP | Get\_Sink\_Cap Message. |
| PD\_CTRL\_DR\_SWAP | DR\_Swap Message. |
| PD\_CTRL\_PR\_SWAP | PR\_Swap Message. |
| PD\_CTRL\_VCONN\_SWAP | VCONN\_Swap Message. |
| PD\_CTRL\_WAIT | Wait Message. |
| PD\_CTRL\_SOFT\_RESET | Soft Reset Message. |
| PD\_CTRL\_DATA\_RESET | Used for REV 3.0.  Data\_Reset Message |
| PD\_CTRL\_DATA\_RESET\_COMPLETE | Data\_Reset\_Complete Message. |
| PD\_CTRL\_NOT\_SUPPORTED | Not\_Supported Message. |
| PD\_CTRL\_GET\_SOURCE\_CAP\_EXT | Get\_Source\_Cap\_Extended Message. |
| PD\_CTRL\_GET\_STATUS | Get\_Status Message. |
| PD\_CTRL\_FR\_SWAP | FR\_Swap Message. |
| PD\_CTRL\_GET\_PPS\_STATUS | Get\_PPS\_Status Message. |
| PD\_CTRL\_GET\_COUNTRY\_CODES | Get\_Country\_Codes Message. |
| PD\_CTRL\_GET\_SINK\_CAP\_EXT | Get\_Sink\_Cap\_Extended Message. |

## [◆ ](#ga8239651864b4cb0e1fc89ba2d7e59462)pd\_data\_msg\_type

| enum [pd\_data\_msg\_type](#ga8239651864b4cb0e1fc89ba2d7e59462) |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Data message type See Table 6-6 Data Message Types.

| Enumerator | |
| --- | --- |
| PD\_DATA\_SOURCE\_CAP | 0 Reserved  Source\_Capabilities Message |
| PD\_DATA\_REQUEST | Request Message. |
| PD\_DATA\_BIST | BIST Message. |
| PD\_DATA\_SINK\_CAP | Sink Capabilities Message. |
| PD\_DATA\_BATTERY\_STATUS | 5-14 Reserved for REV 2.0 |
| PD\_DATA\_ALERT | Alert Message. |
| PD\_DATA\_GET\_COUNTRY\_INFO | Get Country Info Message. |
| PD\_DATA\_ENTER\_USB | 8-14 Reserved for REV 3.0  Enter USB message |
| PD\_DATA\_VENDOR\_DEF | Vendor Defined Message. |

## [◆ ](#ga457308d50365e0a2440e94e41a316cbf)pd\_ext\_msg\_type

| enum [pd\_ext\_msg\_type](#ga457308d50365e0a2440e94e41a316cbf) |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Extended message type for REV 3.0 See Table 6-48 Extended Message Types.

| Enumerator | |
| --- | --- |
| PD\_EXT\_SOURCE\_CAP | 0 Reserved  Source\_Capabilities\_Extended Message |
| PD\_EXT\_STATUS | Status Message. |
| PD\_EXT\_GET\_BATTERY\_CAP | Get\_Battery\_Cap Message. |
| PD\_EXT\_GET\_BATTERY\_STATUS | Get\_Battery\_Status Message. |
| PD\_EXT\_BATTERY\_CAP | Battery\_Capabilities Message. |
| PD\_EXT\_GET\_MANUFACTURER\_INFO | Get\_Manufacturer\_Info Message. |
| PD\_EXT\_MANUFACTURER\_INFO | Manufacturer\_Info Message. |
| PD\_EXT\_SECURITY\_REQUEST | Security\_Request Message. |
| PD\_EXT\_SECURITY\_RESPONSE | Security\_Response Message. |
| PD\_EXT\_FIRMWARE\_UPDATE\_REQUEST | Firmware\_Update\_Request Message. |
| PD\_EXT\_FIRMWARE\_UPDATE\_RESPONSE | Firmware\_Update\_Response Message. |
| PD\_EXT\_PPS\_STATUS | PPS\_Status Message. |
| PD\_EXT\_COUNTRY\_INFO | Country\_Codes Message. |
| PD\_EXT\_COUNTRY\_CODES | Country\_Info Message. |

## [◆ ](#ga48b33240e19524ea003052103d310358)pd\_frs\_type

| enum [pd\_frs\_type](#ga48b33240e19524ea003052103d310358) |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Fast Role Swap Required for USB Type-C current.

| Enumerator | |
| --- | --- |
| FRS\_NOT\_SUPPORTED | Fast Swap not supported. |
| FRS\_DEFAULT\_USB\_POWER | Default USB Power. |
| FRS\_1P5A\_5V | 1.5A @ 5V |
| FRS\_3P0A\_5V | 3.0A @ 5V |

## [◆ ](#gad2df13a24f0365198d37b10af608376b)pd\_packet\_type

| enum [pd\_packet\_type](#gad2df13a24f0365198d37b10af608376b) |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Power Delivery packet type See USB Type-C Port Controller Interface Specification, Revision 2.0, Version 1.2, Table 4-38 TRANSMIT Register Definition.

| Enumerator | |
| --- | --- |
| PD\_PACKET\_SOP | Port Partner message. |
| PD\_PACKET\_SOP\_PRIME | Cable Plug message. |
| PD\_PACKET\_PRIME\_PRIME | Cable Plug message far end. |
| PD\_PACKET\_DEBUG\_PRIME | Currently undefined in the PD specification. |
| PD\_PACKET\_DEBUG\_PRIME\_PRIME | Currently undefined in the PD specification. |
| PD\_PACKET\_TX\_HARD\_RESET | Hard Reset message to the Port Partner. |
| PD\_PACKET\_CABLE\_RESET | Cable Reset message to the Cable. |
| PD\_PACKET\_TX\_BIST\_MODE\_2 | BIST\_MODE\_2 message to the Port Partner. |
| PD\_PACKET\_MSG\_INVALID | USED ONLY FOR RECEPTION OF UNKNOWN MSG TYPES. |

## [◆ ](#gab68c6b6e33449c5ceadfc9217dd7a700)pd\_rev\_type

| enum [pd\_rev\_type](#gab68c6b6e33449c5ceadfc9217dd7a700) |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Protocol revision.

| Enumerator | |
| --- | --- |
| PD\_REV10 | PD revision 1.0. |
| PD\_REV20 | PD revision 2.0. |
| PD\_REV30 | PD revision 3.0. |

## [◆ ](#ga316dca7ed0b85f1aa224d7a767896328)pdo\_type

| enum [pdo\_type](#ga316dca7ed0b85f1aa224d7a767896328) |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Power Data Object Type Table 6-7 Power Data Object.

| Enumerator | |
| --- | --- |
| PDO\_FIXED | Fixed supply (Vmin = Vmax). |
| PDO\_BATTERY | Battery. |
| PDO\_VARIABLE | Variable Supply (non-Battery). |
| PDO\_AUGMENTED | Augmented Power Data Object (APDO). |

## [◆ ](#gaee2fe2128557939404c62e8104269bbf)usbpd\_cc\_pin

| enum [usbpd\_cc\_pin](#gaee2fe2128557939404c62e8104269bbf) |
| --- |

`#include <[usbc_pd.h](usbc__pd_8h.md)>`

Active PD CC pin.

| Enumerator | |
| --- | --- |
| USBPD\_CC\_PIN\_1 | PD is active on CC1. |
| USBPD\_CC\_PIN\_2 | PD is active on CC2. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
