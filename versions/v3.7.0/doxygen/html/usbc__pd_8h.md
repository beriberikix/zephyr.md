---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/usbc__pd_8h.html
original_path: doxygen/html/usbc__pd_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_pd.h File Reference

USB-C Power Delivery API used for USB-C drivers.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](usbc__pd_8h_source.md)

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
| #define | [PD\_MAX\_EXTENDED\_MSG\_LEGACY\_LEN](group__usb__power__delivery.md#ga998b67d43674778e42f6c49ec6a99af4)   26 |
|  | Maximum length of a non-Extended Message in bytes. |
| #define | [PD\_MAX\_EXTENDED\_MSG\_LEN](group__usb__power__delivery.md#gabdb041542baaf2277e054dd9e3928b16)   260 |
|  | Maximum length of an Extended Message in bytes. |
| #define | [PD\_MAX\_EXTENDED\_MSG\_CHUNK\_LEN](group__usb__power__delivery.md#gac0588f94c1792b5b8fefa6a60c1b237b)   26 |
|  | Maximum length of a Chunked Message in bytes. |
| #define | [PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MIN\_MS](group__usb__power__delivery.md#ga266725d0496981ee92b0008afe43505e)   310 |
|  | Minimum time a sink shall wait for a Source\_Capabilities message before sending a Hard Reset See Table 6-61 Time Values Parameter Name: tTypeCSinkWaitCap. |
| #define | [PD\_T\_TYPEC\_SINK\_WAIT\_CAP\_MAX\_MS](group__usb__power__delivery.md#gae32afec56f34841200188e64dc1ab9ca)   620 |
|  | Minimum time a sink shall wait for a Source\_Capabilities message before sending a Hard Reset See Table 6-61 Time Values Parameter Name: tTypeCSinkWaitCap. |
| #define | [PD\_V\_SAFE\_0V\_MAX\_MV](group__usb__power__delivery.md#gac3a939394dab5a5038801f9a6b2dcd30)   800 |
|  | VBUS maximum safe operating voltage at "zero volts". |
| #define | [PD\_V\_SAFE\_5V\_MIN\_MV](group__usb__power__delivery.md#gad4f0e12b7f0e2ccd6aee73cf1525b27c)   4750 |
|  | VBUS minimum safe operating voltage at 5V. |
| #define | [PD\_T\_SAFE\_0V\_MAX\_MS](group__usb__power__delivery.md#gad5667f26343d4601c9fd5c5e9d046802)   650 |
|  | Time to reach PD\_V\_SAFE\_0V\_MV max in milliseconds. |
| #define | [PD\_T\_SAFE\_5V\_MAX\_MS](group__usb__power__delivery.md#ga123abee7651bca30a3e6ec2956eb0563)   275 |
|  | Time to reach PD\_V\_SAFE\_5V\_MV max in milliseconds. |
| #define | [PD\_T\_TX\_TIMEOUT\_MS](group__usb__power__delivery.md#gab6c168d490983a136c184bbe3ed9e7c5)   100 |
|  | Time to wait for TCPC to complete transmit. |
| #define | [PD\_T\_HARD\_RESET\_COMPLETE\_MIN\_MS](group__usb__power__delivery.md#ga64b8c095dba137d7fe460ffe38f00ce5)   4 |
|  | Minimum time a Hard Reset must complete. |
| #define | [PD\_T\_HARD\_RESET\_COMPLETE\_MAX\_MS](group__usb__power__delivery.md#ga2748e0775b50552cc7d26cb2b2d3103d)   5 |
|  | Maximum time a Hard Reset must complete. |
| #define | [PD\_T\_SENDER\_RESPONSE\_MIN\_MS](group__usb__power__delivery.md#ga9722df85c1a842ff1661e534e88d472e)   24 |
|  | Minimum time a response must be sent from a Port Partner See Table 6-68 Time Values. |
| #define | [PD\_T\_SENDER\_RESPONSE\_NOM\_MS](group__usb__power__delivery.md#gac905bf64de8a9f5acef6f8731c11d041)   27 |
|  | Nomiminal time a response must be sent from a Port Partner See Table 6-68 Time Values. |
| #define | [PD\_T\_SENDER\_RESPONSE\_MAX\_MS](group__usb__power__delivery.md#ga4b7c238e12770841b1852a0517b12071)   30 |
|  | Maximum time a response must be sent from a Port Partner See Table 6-68 Time Values. |
| #define | [PD\_T\_SPR\_PS\_TRANSITION\_MIN\_MS](group__usb__power__delivery.md#ga4726113aa8c0100fa1a88435d3a6b1d1)   450 |
|  | Minimum SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_SPR\_PS\_TRANSITION\_NOM\_MS](group__usb__power__delivery.md#ga01a2a71da7fdbe18d07dacb687f7d295)   500 |
|  | Nominal SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_SPR\_PS\_TRANSITION\_MAX\_MS](group__usb__power__delivery.md#ga7dac8d411d8f4651b177a6495146acb0)   550 |
|  | Maximum SPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_EPR\_PS\_TRANSITION\_MIN\_MS](group__usb__power__delivery.md#ga7f9a916a88c626b76963a4950878fa20)   830 |
|  | Minimum EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_EPR\_PS\_TRANSITION\_NOM\_MS](group__usb__power__delivery.md#gabcd0576899a6ce1a147bffbb0c1b517f)   925 |
|  | Nominal EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_EPR\_PS\_TRANSITION\_MAX\_MS](group__usb__power__delivery.md#gaaea48ba7ea96b304b18293c202325b0e)   1020 |
|  | Maximum EPR Mode time for a power supply to transition to a new level See Table 6-68 Time Values. |
| #define | [PD\_T\_SINK\_REQUEST\_MIN\_MS](group__usb__power__delivery.md#ga4416cfc999de1ee2ed49ce89f54074b1)   100 |
|  | Minimum time to wait before sending another request after receiving a Wait message See Table 6-68 Time Values. |
| #define | [PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MIN\_MS](group__usb__power__delivery.md#ga890ce7af4632f8a17b399f0821aee3cf)   40 |
|  | Minimum time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values. |
| #define | [PD\_T\_CHUNKING\_NOT\_SUPPORTED\_NOM\_MS](group__usb__power__delivery.md#gad13130dbd7f6ed4276b1781c5bf2fb20)   45 |
|  | Nominal time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values. |
| #define | [PD\_T\_CHUNKING\_NOT\_SUPPORTED\_MAX\_MS](group__usb__power__delivery.md#gaf28df42c00394f9d11dfade2cae910d4)   50 |
|  | Maximum time to wait before sending a Not\_Supported message after receiving a Chunked message See Table 6-68 Time Values. |
| #define | [PD\_CONVERT\_BYTES\_TO\_PD\_HEADER\_COUNT](group__usb__power__delivery.md#ga953bdd1d4893bebcaeb6b4b95667fd94)(c) |
|  | Convert bytes to PD Header data object count, where a data object is 4-bytes. |
| #define | [PD\_CONVERT\_PD\_HEADER\_COUNT\_TO\_BYTES](group__usb__power__delivery.md#gad5c5b108e4b255633a52d0de48adaf71)(c) |
|  | Convert PD Header data object count to bytes. |
| #define | [SINK\_TX\_OK](group__usb__power__delivery.md#ga69f749b5c7ecf6368002aae12277ac9f)   [TC\_RP\_3A0](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c) |
|  | Collision avoidance Rp values in REV 3.0 Sink Transmit "OK". |
| #define | [SINK\_TX\_NG](group__usb__power__delivery.md#gaa3ca6814e56859792dd5524fe8cef6b1)   [TC\_RP\_1A5](group__usb__type__c.md#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28) |
|  | Collision avoidance Rp values in REV 3.0 Sink Transmit "NO GO". |
| #define | [PD\_GET\_EXT\_HEADER](group__usb__power__delivery.md#gaf3acdb691327adef04e418d7ded3d883)(c) |
|  | Used to get extended header from the first 32-bit word of the message. |
| #define | [PDO\_MAX\_DATA\_OBJECTS](group__usb__power__delivery.md#gab1716bb587e2b162415ea21e3c8d4e74)   7 |
|  | PDO - Power Data Object RDO - Request Data Object. |
| #define | [PD\_CONVERT\_MA\_TO\_FIXED\_PDO\_CURRENT](group__usb__power__delivery.md#ga65e9aa05457df787c5be6792ce725afd)(c) |
|  | Convert milliamps to Fixed PDO Current in 10mA units. |
| #define | [PD\_CONVERT\_MV\_TO\_FIXED\_PDO\_VOLTAGE](group__usb__power__delivery.md#gad79de03a60054be13c9757d933069fe2)(v) |
|  | Convert millivolts to Fixed PDO Voltage in 50mV units. |
| #define | [PD\_CONVERT\_FIXED\_PDO\_CURRENT\_TO\_MA](group__usb__power__delivery.md#gaa0997fc5d7f26115c64f220d2ab91ef2)(c) |
|  | Convert a Fixed PDO Current from 10mA units to milliamps. |
| #define | [PD\_CONVERT\_FIXED\_PDO\_VOLTAGE\_TO\_MV](group__usb__power__delivery.md#gae9eaed8554f857d183e24b96cd69afe3)(v) |
|  | Convert a Fixed PDO Voltage from 50mV units to millivolts. |
| #define | [PD\_CONVERT\_MA\_TO\_VARIABLE\_PDO\_CURRENT](group__usb__power__delivery.md#gab3ea3b392e8fc27b4f100a99988d0ca5)(c) |
|  | Convert milliamps to Variable PDO Current in 10ma units. |
| #define | [PD\_CONVERT\_MV\_TO\_VARIABLE\_PDO\_VOLTAGE](group__usb__power__delivery.md#gae729bb9b17bc0df4201ec27f1f506921)(v) |
|  | Convert millivolts to Variable PDO Voltage in 50mV units. |
| #define | [PD\_CONVERT\_VARIABLE\_PDO\_CURRENT\_TO\_MA](group__usb__power__delivery.md#ga9cd0c218385b400b3efe34474f546203)(c) |
|  | Convert a Variable PDO Current from 10mA units to milliamps. |
| #define | [PD\_CONVERT\_VARIABLE\_PDO\_VOLTAGE\_TO\_MV](group__usb__power__delivery.md#ga4973b120261cde51c86c7b76422222fc)(v) |
|  | Convert a Variable PDO Voltage from 50mV units to millivolts. |
| #define | [PD\_CONVERT\_MW\_TO\_BATTERY\_PDO\_POWER](group__usb__power__delivery.md#ga457907a516a2cf497569ce43561fe7dd)(c) |
|  | Convert milliwatts to Battery PDO Power in 250mW units. |
| #define | [PD\_CONVERT\_MV\_TO\_BATTERY\_PDO\_VOLTAGE](group__usb__power__delivery.md#ga4832aa2b18ff84bfcf3a252361628281)(v) |
|  | Convert milliwatts to Battery PDO Voltage in 50mV units. |
| #define | [PD\_CONVERT\_BATTERY\_PDO\_POWER\_TO\_MW](group__usb__power__delivery.md#ga614dd17b2b98309a837be8e0578bb06b)(c) |
|  | Convert a Battery PDO Power from 250mW units to milliwatts. |
| #define | [PD\_CONVERT\_BATTERY\_PDO\_VOLTAGE\_TO\_MV](group__usb__power__delivery.md#ga74af9a3f10f1855d7322dc36fabdff1a)(v) |
|  | Convert a Battery PDO Voltage from 50mV units to millivolts. |
| #define | [PD\_CONVERT\_MA\_TO\_AUGMENTED\_PDO\_CURRENT](group__usb__power__delivery.md#ga1d73d5ffc7e6657dae81604ffb49b358)(c) |
|  | Convert milliamps to Augmented PDO Current in 50mA units. |
| #define | [PD\_CONVERT\_MV\_TO\_AUGMENTED\_PDO\_VOLTAGE](group__usb__power__delivery.md#ga1dd7da9850daae859d572d866c8c87e2)(v) |
|  | Convert millivolts to Augmented PDO Voltage in 100mV units. |
| #define | [PD\_CONVERT\_AUGMENTED\_PDO\_CURRENT\_TO\_MA](group__usb__power__delivery.md#ga202d52036ee2fb6d6da3594c126cf82b)(c) |
|  | Convert an Augmented PDO Current from 50mA units to milliamps. |
| #define | [PD\_CONVERT\_AUGMENTED\_PDO\_VOLTAGE\_TO\_MV](group__usb__power__delivery.md#ga8623c319b19e7444ba400c738848d9ae)(v) |
|  | Convert an Augmented PDO Voltage from 100mV units to millivolts. |
| #define | [NUM\_SOP\_STAR\_TYPES](group__usb__power__delivery.md#ga1bb5fd6bb6657399a75b095eb3442bde)   ([PD\_PACKET\_DEBUG\_PRIME\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1) + 1) |
|  | Number of valid Transmit Types. |
| USB PD 3.1 Rev 1.6, Table 6-70 Counter Parameters | |
| #define | [PD\_N\_CAPS\_COUNT](group__usb__power__delivery.md#gac517b081df0572803efb374839846f1f)   50 |
|  | The CapsCounter is used to count the number of Source\_Capabilities Messages which have been sent by a Source at power up or after a Hard Reset. |
| #define | [PD\_N\_HARD\_RESET\_COUNT](group__usb__power__delivery.md#gae4f479f2e77066a9b870263e3580f03f)   2 |
|  | The HardResetCounter is used to retry the Hard Reset whenever there is no response from the remote device (see Section 6.6.6) Parameter Name: nHardResetCounter. |
| USB PD 3.1 Rev 1.6, Table 6-68 Time Values | |
| #define | [PD\_T\_NO\_RESPONSE\_MIN\_MS](group__usb__power__delivery.md#ga9dfd6527539e996ccc110036545e61e7)   4500 |
|  | The NoResponseTimer is used by the Policy Engine in a Source to determine that its Port Partner is not responding after a Hard Reset. |
| #define | [PD\_T\_NO\_RESPONSE\_MAX\_MS](group__usb__power__delivery.md#gaed69627505bdad8fb87c37084e2222e1)   5500 |
|  | The NoResponseTimer is used by the Policy Engine in a Source to determine that its Port Partner is not responding after a Hard Reset. |
| #define | [PD\_T\_PS\_HARD\_RESET\_MIN\_MS](group__usb__power__delivery.md#ga87d0eb341d76c01b4b355c1d5a0354a1)   25 |
|  | Min time the Source waits to ensure that the Sink has had sufficient time to process Hard Reset Signaling before turning off its power supply to VBUS Parameter Name: tPSHardReset. |
| #define | [PD\_T\_PS\_HARD\_RESET\_MAX\_MS](group__usb__power__delivery.md#ga2c4abfef3a581e19677d8f0d845a3582)   35 |
|  | Max time the Source waits to ensure that the Sink has had sufficient time to process Hard Reset Signaling before turning off its power supply to VBUS Parameter Name: tPSHardReset. |
| #define | [PD\_T\_SINK\_TX\_MIN\_MS](group__usb__power__delivery.md#gae7db10623f2ec064ef0351bb1bba51cd)   16 |
|  | Minimum time a Source waits after changing Rp from SinkTxOk to SinkTxNG before initiating an AMS by sending a Message. |
| #define | [PD\_T\_SINK\_TX\_MAX\_MS](group__usb__power__delivery.md#gadb55b3f260a17458bf479a7273fd946c)   20 |
|  | Maximum time a Source waits after changing Rp from SinkTxOk to SinkTxNG before initiating an AMS by sending a Message. |
| #define | [PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MIN\_MS](group__usb__power__delivery.md#gabe6d36578671578eddf1381f58bcc80a)   100 |
|  | Minimum time a source shall wait before sending a Source\_Capabilities message while the following is true: 1) The Port is Attached. |
| #define | [PD\_T\_TYPEC\_SEND\_SOURCE\_CAP\_MAX\_MS](group__usb__power__delivery.md#ga105a9791e086ade590b6fd825fe5cded)   200 |
|  | Maximum time a source shall wait before sending a Source\_Capabilities message while the following is true: 1) The Port is Attached. |

| Enumerations | |
| --- | --- |
| enum | [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) { [PDO\_FIXED](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328abbc517bb47b6bdc76e44b599523e0d93) = 0 , [PDO\_BATTERY](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328a63f4fb7a4d2f7e265fd49be07966fbaa) = 1 , [PDO\_VARIABLE](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328a1726efca9ece0ff017cc4aaf05ce9624) = 2 , [PDO\_AUGMENTED](group__usb__power__delivery.md#gga316dca7ed0b85f1aa224d7a767896328adb8478434cc1622e98bc22f4081dff1e) = 3 } |
|  | Power Data Object Type Table 6-7 Power Data Object. [More...](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) |
| enum | [pd\_frs\_type](group__usb__power__delivery.md#ga48b33240e19524ea003052103d310358) { [FRS\_NOT\_SUPPORTED](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358acbf2bf3ae21ff1ea51d7fd2b823ce726) , [FRS\_DEFAULT\_USB\_POWER](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358a4cd44f89f225f8869bfd901e7ea79aed) , [FRS\_1P5A\_5V](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358acac5008ded87d7a20b0b3b272075e4c1) , [FRS\_3P0A\_5V](group__usb__power__delivery.md#gga48b33240e19524ea003052103d310358a99ab2afc15809b5e89e3fb7106be37ba) } |
|  | Fast Role Swap Required for USB Type-C current. [More...](group__usb__power__delivery.md#ga48b33240e19524ea003052103d310358) |
| enum | [pd\_rev\_type](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700) { [PD\_REV10](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700a1d9b4c553f44dccdc67e4edb554557b9) = 0 , [PD\_REV20](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700a22c122b1d30a3ab96fffd5dfa6bfb9ae) = 1 , [PD\_REV30](group__usb__power__delivery.md#ggab68c6b6e33449c5ceadfc9217dd7a700af3770bcbcf6feaaab272c022d7a57c7a) = 2 } |
|  | Protocol revision. [More...](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700) |
| enum | [pd\_packet\_type](group__usb__power__delivery.md#gad2df13a24f0365198d37b10af608376b) {     [PD\_PACKET\_SOP](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba0bede6a56c24b06fdf56cf1dc386bb14) = 0 , [PD\_PACKET\_SOP\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376bae3a5f99242ab24a34706170101b38ef8) = 1 , [PD\_PACKET\_PRIME\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba5ecd663a9eecefcf965f605125d5188c) = 2 , [PD\_PACKET\_DEBUG\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba63b2200ebaf016d06437f3586d15171d) = 3 ,     [PD\_PACKET\_DEBUG\_PRIME\_PRIME](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1) = 4 , [PD\_PACKET\_TX\_HARD\_RESET](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376baa5cd066e86fd55727c3625cd16633f73) = 5 , [PD\_PACKET\_CABLE\_RESET](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba531ebc6013984b81e6fb550618d6b4a8) = 6 , [PD\_PACKET\_TX\_BIST\_MODE\_2](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376bafcd21cc6b1ae6c58b86c0619d687e8fc) = 7 ,     [PD\_PACKET\_MSG\_INVALID](group__usb__power__delivery.md#ggad2df13a24f0365198d37b10af608376ba55bb88e5955992170bee96ddbe8a7437) = 0xf   } |
|  | Power Delivery packet type See USB Type-C Port Controller Interface Specification, Revision 2.0, Version 1.2, Table 4-38 TRANSMIT Register Definition. [More...](group__usb__power__delivery.md#gad2df13a24f0365198d37b10af608376b) |
| enum | [pd\_ctrl\_msg\_type](group__usb__power__delivery.md#ga4c7862a3e953fb22534123223c942f9a) {     [PD\_CTRL\_GOOD\_CRC](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aae0895be53e5a1e54731e9608a8e0c6c9) = 1 , [PD\_CTRL\_GOTO\_MIN](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa4ba7f63cdcbe766a34047e06145a591e) = 2 , [PD\_CTRL\_ACCEPT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa56df68ed627b56bbcfc20900ec5d2e5d) = 3 , [PD\_CTRL\_REJECT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa9dd7b559e78a99639056325a7be14d81) = 4 ,     [PD\_CTRL\_PING](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa8177040ca8a1f71dde67fc59060c35ed) = 5 , [PD\_CTRL\_PS\_RDY](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aafc449fc3dc39f2495494507cc97f53ad) = 6 , [PD\_CTRL\_GET\_SOURCE\_CAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa9324307526500683ae265e9cb0063929) = 7 , [PD\_CTRL\_GET\_SINK\_CAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aaaf5c221569a9108bdbc36545dcb37495) = 8 ,     [PD\_CTRL\_DR\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa4aba967f7e363dbbadcc9a9ecf0c7ae4) = 9 , [PD\_CTRL\_PR\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aade67c4fb153e5ba87b6d6643f99260f9) = 10 , [PD\_CTRL\_VCONN\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa68820e99ce9c1c73180734372e5ede2b) = 11 , [PD\_CTRL\_WAIT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa3b6fc49b1ae0bb343d39476350b59c90) = 12 ,     [PD\_CTRL\_SOFT\_RESET](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aadeb12ed01ec54ee55588bfb796dd0c11) = 13 , [PD\_CTRL\_DATA\_RESET](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa03f9886881aa493fb0f9bfac16713e7a) = 14 , [PD\_CTRL\_DATA\_RESET\_COMPLETE](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa27caca37f9522045bc8612f7536cd792) = 15 , [PD\_CTRL\_NOT\_SUPPORTED](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aabfea5fdf0263fdf4c924bd603ee7256f) = 16 ,     [PD\_CTRL\_GET\_SOURCE\_CAP\_EXT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aab0ca2628b144d092116b461703176eaa) = 17 , [PD\_CTRL\_GET\_STATUS](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa23287276ee22241906828515f38fedef) = 18 , [PD\_CTRL\_FR\_SWAP](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa1c597b5f953e6e1791aa869025b98b24) = 19 , [PD\_CTRL\_GET\_PPS\_STATUS](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aab82efb96b1f8f7dae3c76e362ae1715a) = 20 ,     [PD\_CTRL\_GET\_COUNTRY\_CODES](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aa677ebc41b4b67de6ee93b5e446af702e) = 21 , [PD\_CTRL\_GET\_SINK\_CAP\_EXT](group__usb__power__delivery.md#gga4c7862a3e953fb22534123223c942f9aaaa0a5bba9a9f1573952141c4f8f77318) = 22   } |
|  | Control Message type See Table 6-5 Control Message Types. [More...](group__usb__power__delivery.md#ga4c7862a3e953fb22534123223c942f9a) |
| enum | [pd\_data\_msg\_type](group__usb__power__delivery.md#ga8239651864b4cb0e1fc89ba2d7e59462) {     [PD\_DATA\_SOURCE\_CAP](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad9a0cf16cfa852111ea0ed3434b35dfc) = 1 , [PD\_DATA\_REQUEST](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad9c920f987e2578b030cc08f2e69998a) = 2 , [PD\_DATA\_BIST](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a7c4bc907fb81082da05c64797854be9f) = 3 , [PD\_DATA\_SINK\_CAP](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a4cf30dcbce3fdf8076713e45d242b39a) = 4 ,     [PD\_DATA\_BATTERY\_STATUS](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462ad493f01ffc4c3c164f874eb202f8adb0) = 5 , [PD\_DATA\_ALERT](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a7e3368e1c7bde4c6bb3136cb80209bb6) = 6 , [PD\_DATA\_GET\_COUNTRY\_INFO](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a83d7098236e97972cf24b900f7e5e069) = 7 , [PD\_DATA\_ENTER\_USB](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a1a0829560f9f82182f7587fd8787a846) = 8 ,     [PD\_DATA\_VENDOR\_DEF](group__usb__power__delivery.md#gga8239651864b4cb0e1fc89ba2d7e59462a881fcbc2dc5f8b1de7c97522df46242d) = 15   } |
|  | Data message type See Table 6-6 Data Message Types. [More...](group__usb__power__delivery.md#ga8239651864b4cb0e1fc89ba2d7e59462) |
| enum | [pd\_ext\_msg\_type](group__usb__power__delivery.md#ga457308d50365e0a2440e94e41a316cbf) {     [PD\_EXT\_SOURCE\_CAP](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa51c03e44c3fe1bb59445bbc452ea7199) = 1 , [PD\_EXT\_STATUS](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa836130da5307aed6160deadadf2f4f3f) = 2 , [PD\_EXT\_GET\_BATTERY\_CAP](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa9c50488735d7723c3cc30f176c221e40) = 3 , [PD\_EXT\_GET\_BATTERY\_STATUS](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa77ff801aa819461f0f5ff44546370bd7) = 4 ,     [PD\_EXT\_BATTERY\_CAP](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfae7f7b3f7233bb5cf600338b4a2c601c0) = 5 , [PD\_EXT\_GET\_MANUFACTURER\_INFO](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfac8fc4c3c64fb3eaba8cb61bd999c7033) = 6 , [PD\_EXT\_MANUFACTURER\_INFO](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa500d77f178123eab8073058dd9308ea6) = 7 , [PD\_EXT\_SECURITY\_REQUEST](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa0f62aa3774995018514dcd2f75ac1c1f) = 8 ,     [PD\_EXT\_SECURITY\_RESPONSE](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfad002882e8bce9cdfdb0864cd6a3e79a7) = 9 , [PD\_EXT\_FIRMWARE\_UPDATE\_REQUEST](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa2a7b6a78cf3fd87a86f060f927b566af) = 10 , [PD\_EXT\_FIRMWARE\_UPDATE\_RESPONSE](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa4fe2d7028fa2bdf594cb8c87ac05fe67) = 11 , [PD\_EXT\_PPS\_STATUS](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfa7d04da3fdb96eac97200d11eb2dbe083) = 12 ,     [PD\_EXT\_COUNTRY\_INFO](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfaa21adc92574ed1261b6c13df3592601b) = 13 , [PD\_EXT\_COUNTRY\_CODES](group__usb__power__delivery.md#gga457308d50365e0a2440e94e41a316cbfae69b4a8ddba29bc6cd69d50c946bc658) = 14   } |
|  | Extended message type for REV 3.0 See Table 6-48 Extended Message Types. [More...](group__usb__power__delivery.md#ga457308d50365e0a2440e94e41a316cbf) |
| enum | [usbpd\_cc\_pin](group__usb__power__delivery.md#gaee2fe2128557939404c62e8104269bbf) { [USBPD\_CC\_PIN\_1](group__usb__power__delivery.md#ggaee2fe2128557939404c62e8104269bbfa59a0ed05c4e99acebaa11080dbbe7694) = 0 , [USBPD\_CC\_PIN\_2](group__usb__power__delivery.md#ggaee2fe2128557939404c62e8104269bbfa53a0a6ba0212b9cbb407522e7f35648e) = 1 } |
|  | Active PD CC pin. [More...](group__usb__power__delivery.md#gaee2fe2128557939404c62e8104269bbf) |

## Detailed Description

USB-C Power Delivery API used for USB-C drivers.

The information in this file was taken from the USB PD Specification Revision 3.0, Version 2.0

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [usbc\_pd.h](usbc__pd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
