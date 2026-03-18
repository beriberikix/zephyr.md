---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/conn_8h.html
original_path: doxygen/html/conn_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

conn.h File Reference

Bluetooth connection handling.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci_types.h](hci__types_8h_source.md)>`  
`#include <[zephyr/bluetooth/addr.h](addr_8h_source.md)>`  
`#include <[zephyr/bluetooth/gap.h](gap_8h_source.md)>`  
`#include <[zephyr/bluetooth/direction.h](direction_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](conn_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_le\_conn\_param](structbt__le__conn__param.md) |
|  | Connection parameters for LE connections. [More...](structbt__le__conn__param.md#details) |
| struct | [bt\_conn\_le\_phy\_info](structbt__conn__le__phy__info.md) |
|  | Connection PHY information for LE connections. [More...](structbt__conn__le__phy__info.md#details) |
| struct | [bt\_conn\_le\_phy\_param](structbt__conn__le__phy__param.md) |
|  | Preferred PHY parameters for LE connections. [More...](structbt__conn__le__phy__param.md#details) |
| struct | [bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md) |
|  | Connection data length information for LE connections. [More...](structbt__conn__le__data__len__info.md#details) |
| struct | [bt\_conn\_le\_data\_len\_param](structbt__conn__le__data__len__param.md) |
|  | Connection data length parameters for LE connections. [More...](structbt__conn__le__data__len__param.md#details) |
| struct | [bt\_conn\_le\_info](structbt__conn__le__info.md) |
|  | LE Connection Info Structure. [More...](structbt__conn__le__info.md#details) |
| struct | [bt\_conn\_br\_info](structbt__conn__br__info.md) |
|  | BR/EDR Connection Info Structure. [More...](structbt__conn__br__info.md#details) |
| struct | [bt\_security\_info](structbt__security__info.md) |
|  | Security Info Structure. [More...](structbt__security__info.md#details) |
| struct | [bt\_conn\_info](structbt__conn__info.md) |
|  | Connection Info Structure. [More...](structbt__conn__info.md#details) |
| struct | [bt\_conn\_le\_remote\_info](structbt__conn__le__remote__info.md) |
|  | LE Connection Remote Info Structure. [More...](structbt__conn__le__remote__info.md#details) |
| struct | [bt\_conn\_br\_remote\_info](structbt__conn__br__remote__info.md) |
|  | BR/EDR Connection Remote Info structure. [More...](structbt__conn__br__remote__info.md#details) |
| struct | [bt\_conn\_remote\_info](structbt__conn__remote__info.md) |
|  | Connection Remote Info Structure. [More...](structbt__conn__remote__info.md#details) |
| struct | [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) |
|  | LE Transmit Power Level Structure. [More...](structbt__conn__le__tx__power.md#details) |
| struct | [bt\_conn\_le\_tx\_power\_report](structbt__conn__le__tx__power__report.md) |
|  | LE Transmit Power Reporting Structure. [More...](structbt__conn__le__tx__power__report.md#details) |
| struct | [bt\_conn\_le\_path\_loss\_threshold\_report](structbt__conn__le__path__loss__threshold__report.md) |
|  | LE Path Loss Monitoring Threshold Change Report Structure. [More...](structbt__conn__le__path__loss__threshold__report.md#details) |
| struct | [bt\_conn\_le\_path\_loss\_reporting\_param](structbt__conn__le__path__loss__reporting__param.md) |
|  | LE Path Loss Monitoring Parameters Structure as defined in Core Spec. [More...](structbt__conn__le__path__loss__reporting__param.md#details) |
| struct | [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) |
| struct | [bt\_conn\_le\_create\_synced\_param](structbt__conn__le__create__synced__param.md) |
| struct | [bt\_conn\_cb](structbt__conn__cb.md) |
|  | Connection callback structure. [More...](structbt__conn__cb.md#details) |
| struct | [bt\_conn\_oob\_info](structbt__conn__oob__info.md) |
|  | Info Structure for OOB pairing. [More...](structbt__conn__oob__info.md#details) |
| struct | [bt\_conn\_pairing\_feat](structbt__conn__pairing__feat.md) |
|  | Pairing request and pairing response info structure. [More...](structbt__conn__pairing__feat.md#details) |
| struct | [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) |
|  | Authenticated pairing callback structure. [More...](structbt__conn__auth__cb.md#details) |
| struct | [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) |
|  | Authenticated pairing information callback structure. [More...](structbt__conn__auth__info__cb.md#details) |
| struct | [bt\_br\_conn\_param](structbt__br__conn__param.md) |
|  | Connection parameters for BR/EDR connections. [More...](structbt__br__conn__param.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_LE\_CONN\_PARAM\_INIT](group__bt__conn.md#ga81de567c4c8cb691ef8b02633b42e342)(int\_min, int\_max, lat, to) |
|  | Initialize connection parameters. |
| #define | [BT\_LE\_CONN\_PARAM](group__bt__conn.md#ga940d55c0d84c0cb8f09bc41074ae50d0)(int\_min, int\_max, lat, to) |
|  | Helper to declare connection parameters inline. |
| #define | [BT\_LE\_CONN\_PARAM\_DEFAULT](group__bt__conn.md#ga82df8f439aeb3a156f4238deb085534a) |
|  | Default LE connection parameters: Connection Interval: 30-50 ms Latency: 0 Timeout: 4 s. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM\_INIT](group__bt__conn.md#gabca56de0c82c14995738952dafb1fe2d)(\_pref\_tx\_phy, \_pref\_rx\_phy) |
|  | Initialize PHY parameters. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM](group__bt__conn.md#ga39b69f0978f74b5f13f829e908b7cebb)(\_pref\_tx\_phy, \_pref\_rx\_phy) |
|  | Helper to declare PHY parameters inline. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM\_1M](group__bt__conn.md#ga3ec555bb4ace5e9c7c13735820fd31de) |
|  | Only LE 1M PHY. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM\_2M](group__bt__conn.md#ga633126e356658886e9fa3f3217cb4e2c) |
|  | Only LE 2M PHY. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM\_CODED](group__bt__conn.md#ga4915244a6cd70995514d6dde1ee0b45f) |
|  | Only LE Coded PHY. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM\_ALL](group__bt__conn.md#ga02c9d7a04ccf2f043293aed7a7f767a7) |
|  | All LE PHYs. |
| #define | [BT\_CONN\_LE\_DATA\_LEN\_PARAM\_INIT](group__bt__conn.md#ga98f9dab71897382cf1187259a3b5660e)(\_tx\_max\_len, \_tx\_max\_time) |
|  | Initialize transmit data length parameters. |
| #define | [BT\_CONN\_LE\_DATA\_LEN\_PARAM](group__bt__conn.md#ga102b97de8689fe3fb53f9691009de87f)(\_tx\_max\_len, \_tx\_max\_time) |
|  | Helper to declare transmit data length parameters inline. |
| #define | [BT\_LE\_DATA\_LEN\_PARAM\_DEFAULT](group__bt__conn.md#gaf66746d834f7556dc77659741e27e0c9) |
|  | Default LE data length parameters. |
| #define | [BT\_LE\_DATA\_LEN\_PARAM\_MAX](group__bt__conn.md#ga9cc26afda3c507cb5439184fedcd61ba) |
|  | Maximum LE data length parameters. |
| #define | [BT\_CONN\_INTERVAL\_TO\_MS](group__bt__conn.md#ga707cc62b12c89478aebd0488a464a776)(interval) |
|  | Convert connection interval to milliseconds. |
| #define | [BT\_CONN\_INTERVAL\_TO\_US](group__bt__conn.md#ga0a5fac126005684847ee7509bb98e382)(interval) |
|  | Convert connection interval to microseconds. |
| #define | [BT\_CONN\_LE\_CREATE\_PARAM\_INIT](group__bt__conn.md#ga8ac93a19c34d2821c158f310879fe00d)(\_options, \_interval, \_window) |
|  | Initialize create connection parameters. |
| #define | [BT\_CONN\_LE\_CREATE\_PARAM](group__bt__conn.md#gae86425d432078e2ddca260eebc2802f1)(\_options, \_interval, \_window) |
|  | Helper to declare create connection parameters inline. |
| #define | [BT\_CONN\_LE\_CREATE\_CONN](group__bt__conn.md#gab4203c55c20d83256ca036148c14a00d) |
|  | Default LE create connection parameters. |
| #define | [BT\_CONN\_LE\_CREATE\_CONN\_AUTO](group__bt__conn.md#gaaba7c37a5c6e98e7b62ac12bde814d5d) |
|  | Default LE create connection using filter accept list parameters. |
| #define | [BT\_CONN\_CB\_DEFINE](group__bt__conn.md#ga9227880a1ae5fc373d334171e1450f00)(\_name) |
|  | Register a callback structure for connection events. |
| #define | [BT\_PASSKEY\_INVALID](group__bt__conn.md#gaf638077430b418f9879ac4ddf58ef17a)   0xffffffff |
|  | Special passkey value that can be used to disable a previously set fixed passkey. |
| #define | [BT\_BR\_CONN\_PARAM\_INIT](group__bt__conn.md#ga986f563bfb741c70fbee39b3948d9d8d)(role\_switch) |
|  | Initialize BR/EDR connection parameters. |
| #define | [BT\_BR\_CONN\_PARAM](group__bt__conn.md#ga6f99f4adfcef36a4d738783921965ca6)(role\_switch) |
|  | Helper to declare BR/EDR connection parameters inline. |
| #define | [BT\_BR\_CONN\_PARAM\_DEFAULT](group__bt__conn.md#ga5ccdbff63a430a37a8a8077d8792f706)   [BT\_BR\_CONN\_PARAM](group__bt__conn.md#ga6f99f4adfcef36a4d738783921965ca6)([true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)) |
|  | Default BR/EDR connection parameters: Role switch allowed. |

| Enumerations | |
| --- | --- |
| enum | { [BT\_CONN\_LE\_PHY\_OPT\_NONE](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98) = 0 , [BT\_CONN\_LE\_PHY\_OPT\_CODED\_S2](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaa42e6ff627268b9eef111375d591f9f34) = BIT(0) , [BT\_CONN\_LE\_PHY\_OPT\_CODED\_S8](group__bt__conn.md#gga08eb37185a763212e65c47ab4c886ecaad1d46128ba2516810af7383e850929e0) = BIT(1) } |
|  | Connection PHY options. [More...](group__bt__conn.md#ga08eb37185a763212e65c47ab4c886eca) |
| enum | [bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20) {     [BT\_CONN\_TYPE\_LE](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2) = BIT(0) , [BT\_CONN\_TYPE\_BR](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6) = BIT(1) , [BT\_CONN\_TYPE\_SCO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953) = BIT(2) , [BT\_CONN\_TYPE\_ISO](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee) = BIT(3) ,     [BT\_CONN\_TYPE\_ALL](group__bt__conn.md#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836)   } |
|  | Connection Type. [More...](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20) |
| enum | { [BT\_CONN\_ROLE\_CENTRAL](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30) = 0 , [BT\_CONN\_ROLE\_PERIPHERAL](group__bt__conn.md#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0) = 1 } |
| enum | [bt\_conn\_state](group__bt__conn.md#ga9442c1479db60e2db40a2ea6de565282) { [BT\_CONN\_STATE\_DISCONNECTED](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587) , [BT\_CONN\_STATE\_CONNECTING](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd) , [BT\_CONN\_STATE\_CONNECTED](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f) , [BT\_CONN\_STATE\_DISCONNECTING](group__bt__conn.md#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f) } |
| enum | [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) {     [BT\_SECURITY\_L0](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e) , [BT\_SECURITY\_L1](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b) , [BT\_SECURITY\_L2](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a) , [BT\_SECURITY\_L3](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631) ,     [BT\_SECURITY\_L4](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81) , [BT\_SECURITY\_FORCE\_PAIR](group__bt__conn.md#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae) = BIT(7)   } |
|  | Security level. [More...](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) |
| enum | [bt\_security\_flag](group__bt__conn.md#ga2f8712bbf3410de5cbe6ce489fe30e5e) { [BT\_SECURITY\_FLAG\_SC](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6) = BIT(0) , [BT\_SECURITY\_FLAG\_OOB](group__bt__conn.md#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198) = BIT(1) } |
|  | Security Info Flags. [More...](group__bt__conn.md#ga2f8712bbf3410de5cbe6ce489fe30e5e) |
| enum | [bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190) {     [BT\_CONN\_LE\_TX\_POWER\_PHY\_NONE](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a) , [BT\_CONN\_LE\_TX\_POWER\_PHY\_1M](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046) , [BT\_CONN\_LE\_TX\_POWER\_PHY\_2M](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800) , [BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S8](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2) ,     [BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S2](group__bt__conn.md#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296)   } |
| enum | [bt\_conn\_le\_path\_loss\_zone](group__bt__conn.md#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e) { [BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_LOW](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea17765999979bb1bac00769ea742d53d8) , [BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_MIDDLE](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea06bd101d7cc98d39403ed16719542dec) , [BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_ENTERED\_HIGH](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea19fd0c4702ca5e08c8cbfb51b34bb705) , [BT\_CONN\_LE\_PATH\_LOSS\_ZONE\_UNAVAILABLE](group__bt__conn.md#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea684ce653c5fffe9d49316d22904d3942) } |
|  | Path Loss zone that has been entered. [More...](group__bt__conn.md#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e) |
| enum | [bt\_conn\_auth\_keypress](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043) {     [BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_STARTED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6) = 0x00 , [BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ENTERED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1) = 0x01 , [BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ERASED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529) = 0x02 , [BT\_CONN\_AUTH\_KEYPRESS\_CLEARED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da) = 0x03 ,     [BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_COMPLETED](group__bt__conn.md#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8) = 0x04   } |
|  | Passkey Keypress Notification type. [More...](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043) |
| enum | { [BT\_CONN\_LE\_OPT\_NONE](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9) = 0 , [BT\_CONN\_LE\_OPT\_CODED](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b) = BIT(0) , [BT\_CONN\_LE\_OPT\_NO\_1M](group__bt__conn.md#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9) = BIT(1) } |
| enum | [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) {     [BT\_SECURITY\_ERR\_SUCCESS](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05) , [BT\_SECURITY\_ERR\_AUTH\_FAIL](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7) , [BT\_SECURITY\_ERR\_PIN\_OR\_KEY\_MISSING](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171) , [BT\_SECURITY\_ERR\_OOB\_NOT\_AVAILABLE](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7) ,     [BT\_SECURITY\_ERR\_AUTH\_REQUIREMENT](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae) , [BT\_SECURITY\_ERR\_PAIR\_NOT\_SUPPORTED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6) , [BT\_SECURITY\_ERR\_PAIR\_NOT\_ALLOWED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f) , [BT\_SECURITY\_ERR\_INVALID\_PARAM](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5) ,     [BT\_SECURITY\_ERR\_KEY\_REJECTED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216) , [BT\_SECURITY\_ERR\_UNSPECIFIED](group__bt__conn.md#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242)   } |

| Functions | |
| --- | --- |
| struct bt\_conn \* | [bt\_conn\_ref](group__bt__conn.md#ga060d51eb2208de6f805b1fc0672d2d0c) (struct bt\_conn \*conn) |
|  | Increment a connection's reference count. |
| void | [bt\_conn\_unref](group__bt__conn.md#ga4b18c6b22a9f02be0d7d078b2ce51ff6) (struct bt\_conn \*conn) |
|  | Decrement a connection's reference count. |
| void | [bt\_conn\_foreach](group__bt__conn.md#ga5bdf8e8efc85138d3631dc1efffc3916) (enum [bt\_conn\_type](group__bt__conn.md#gab8dde20ae75b51f1e28dbeed06001f20) type, void(\*func)(struct bt\_conn \*conn, void \*data), void \*data) |
|  | Iterate through all bt\_conn objects. |
| struct bt\_conn \* | [bt\_conn\_lookup\_addr\_le](group__bt__conn.md#ga1bfe349efd8a7de31e9457fe439d746a) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer) |
|  | Look up an existing connection by address. |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [bt\_conn\_get\_dst](group__bt__conn.md#ga77108581b8f61485ca840e4bf7a17087) (const struct bt\_conn \*conn) |
|  | Get destination (peer) address of a connection. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_conn\_index](group__bt__conn.md#gad4aed76b80cc815f748ad0e84ae3d87c) (const struct bt\_conn \*conn) |
|  | Get array index of a connection. |
| int | [bt\_conn\_get\_info](group__bt__conn.md#ga2de54f2ac83f0d8dca2a85a9fbfadcaa) (const struct bt\_conn \*conn, struct [bt\_conn\_info](structbt__conn__info.md) \*info) |
|  | Get connection info. |
| int | [bt\_conn\_get\_remote\_info](group__bt__conn.md#ga6ea4478db6d95bd6a0d316399db36d92) (struct bt\_conn \*conn, struct [bt\_conn\_remote\_info](structbt__conn__remote__info.md) \*remote\_info) |
|  | Get connection info for the remote device. |
| int | [bt\_conn\_le\_get\_tx\_power\_level](group__bt__conn.md#gaa5289154bc508444f68df7abcef18aca) (struct bt\_conn \*conn, struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) \*tx\_power\_level) |
|  | Get connection transmit power level. |
| int | [bt\_conn\_le\_enhanced\_get\_tx\_power\_level](group__bt__conn.md#gaa79eada87d698f4998af876d03d7e92b) (struct bt\_conn \*conn, struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) \*tx\_power) |
|  | Get local enhanced connection transmit power level. |
| int | [bt\_conn\_le\_get\_remote\_tx\_power\_level](group__bt__conn.md#ga0843a2e0b6f16ebd132a3a512cfd27a4) (struct bt\_conn \*conn, enum [bt\_conn\_le\_tx\_power\_phy](group__bt__conn.md#ga737d8118f8aba8985292d92d0604b190) phy) |
|  | Get remote (peer) transmit power level. |
| int | [bt\_conn\_le\_set\_tx\_power\_report\_enable](group__bt__conn.md#gaa1f38911acee0534a8a6e414018c6fb6) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) local\_enable, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) remote\_enable) |
|  | Enable transmit power reporting. |
| int | [bt\_conn\_le\_set\_path\_loss\_mon\_param](group__bt__conn.md#ga6be5f3bf064ba03dc2307fdd2b634637) (struct bt\_conn \*conn, const struct [bt\_conn\_le\_path\_loss\_reporting\_param](structbt__conn__le__path__loss__reporting__param.md) \*param) |
|  | Set Path Loss Monitoring Parameters. |
| int | [bt\_conn\_le\_set\_path\_loss\_mon\_enable](group__bt__conn.md#ga90ae27bcc6f71f32be56efe8ecbc165d) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable or Disable Path Loss Monitoring. |
| int | [bt\_conn\_le\_param\_update](group__bt__conn.md#gab44a964725f54ed2d37de17c6e2fd3eb) (struct bt\_conn \*conn, const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param) |
|  | Update the connection parameters. |
| int | [bt\_conn\_le\_data\_len\_update](group__bt__conn.md#ga8a2006f6e34b20c7e8ef65a73f431a57) (struct bt\_conn \*conn, const struct [bt\_conn\_le\_data\_len\_param](structbt__conn__le__data__len__param.md) \*param) |
|  | Update the connection transmit data length parameters. |
| int | [bt\_conn\_le\_phy\_update](group__bt__conn.md#gae13ed81b1e7928f44b8fdf85995b3e58) (struct bt\_conn \*conn, const struct [bt\_conn\_le\_phy\_param](structbt__conn__le__phy__param.md) \*param) |
|  | Update the connection PHY parameters. |
| int | [bt\_conn\_disconnect](group__bt__conn.md#ga14e7c852b0271781594e742ae509c5d3) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | Disconnect from a remote device or cancel pending connection. |
| int | [bt\_conn\_le\_create](group__bt__conn.md#ga8d66f3e0262a51279e9fa8b3139252e6) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer, const struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) \*create\_param, const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param, struct bt\_conn \*\*conn) |
|  | Initiate an LE connection to a remote device. |
| int | [bt\_conn\_le\_create\_synced](group__bt__conn.md#ga98f99c893e444d1ad1ecd9139803c0b1) (const struct bt\_le\_ext\_adv \*adv, const struct [bt\_conn\_le\_create\_synced\_param](structbt__conn__le__create__synced__param.md) \*synced\_param, const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param, struct bt\_conn \*\*conn) |
|  | Create a connection to a synced device. |
| int | [bt\_conn\_le\_create\_auto](group__bt__conn.md#gaecfaf2cb44772511dbb585de8f76f09b) (const struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) \*create\_param, const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param) |
|  | Automatically connect to remote devices in the filter accept list. |
| int | [bt\_conn\_create\_auto\_stop](group__bt__conn.md#ga62dc2663b4fa39a33adb76dc9a136aa4) (void) |
|  | Stop automatic connect creation. |
| int | [bt\_le\_set\_auto\_conn](group__bt__conn.md#ga8eea2211705d0691acc6ee4e0c37a47a) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param) |
|  | Automatically connect to remote device if it's in range. |
| int | [bt\_conn\_set\_security](group__bt__conn.md#gae001f1268e1ff42c3c974c95dcb6735d) (struct bt\_conn \*conn, [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) sec) |
|  | Set security level for a connection. |
| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) | [bt\_conn\_get\_security](group__bt__conn.md#ga4b43ef0f30146808e560991a302e88ad) (const struct bt\_conn \*conn) |
|  | Get security level for a connection. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_conn\_enc\_key\_size](group__bt__conn.md#gaff3e6aa16b68e5da7dab53289295545e) (const struct bt\_conn \*conn) |
|  | Get encryption key size. |
| int | [bt\_conn\_cb\_register](group__bt__conn.md#gaa9b79cd44734c1e560d6f30509be4d0b) (struct [bt\_conn\_cb](structbt__conn__cb.md) \*cb) |
|  | Register connection callbacks. |
| int | [bt\_conn\_cb\_unregister](group__bt__conn.md#gad2f90b34390e3c3697fd455ae4ef5f31) (struct [bt\_conn\_cb](structbt__conn__cb.md) \*cb) |
|  | Unregister connection callbacks. |
| static const char \* | [bt\_security\_err\_to\_str](group__bt__conn.md#ga327444a6987b8e0b573fe758d2f75886) (enum [bt\_security\_err](group__bt__conn.md#gaa9420ff489fd5857ff076406442679ff) err) |
|  | Converts a security error to string. |
| void | [bt\_set\_bondable](group__bt__conn.md#ga014db594b17a3b5d7d954e64ad8de759) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable/disable bonding. |
| int | [bt\_conn\_set\_bondable](group__bt__conn.md#ga4165819d12dd96e00dfa2fd6f4b95669) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set/clear the bonding flag for a given connection. |
| void | [bt\_le\_oob\_set\_sc\_flag](group__bt__conn.md#gad02f8fe587efd543c0c81cace3f63d63) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Allow/disallow remote LE SC OOB data to be used for pairing. |
| void | [bt\_le\_oob\_set\_legacy\_flag](group__bt__conn.md#ga978770d46d7c8af854a61261c14cb892) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Allow/disallow remote legacy OOB data to be used for pairing. |
| int | [bt\_le\_oob\_set\_legacy\_tk](group__bt__conn.md#ga0f889983cfabafe826b4feb6899b95ba) (struct bt\_conn \*conn, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tk) |
|  | Set OOB Temporary Key to be used for pairing. |
| int | [bt\_le\_oob\_set\_sc\_data](group__bt__conn.md#gac365f9748ad0737f09142ee1de982503) (struct bt\_conn \*conn, const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*oobd\_local, const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*oobd\_remote) |
|  | Set OOB data during LE Secure Connections (SC) pairing procedure. |
| int | [bt\_le\_oob\_get\_sc\_data](group__bt__conn.md#ga096552403b5bcd0107f69eded772b1ee) (struct bt\_conn \*conn, const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*\*oobd\_local, const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*\*oobd\_remote) |
|  | Get OOB data used for LE Secure Connections (SC) pairing procedure. |
| int | [bt\_passkey\_set](group__bt__conn.md#ga32c7598c086f209f9e1dee2aacbb40a1) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int passkey) |
|  | Set a fixed passkey to be used for pairing. |
| int | [bt\_conn\_auth\_cb\_register](group__bt__conn.md#ga1bf13d2dfdbdf0a72f9b1c759ef23f60) (const struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) \*cb) |
|  | Register authentication callbacks. |
| int | [bt\_conn\_auth\_cb\_overlay](group__bt__conn.md#ga81077385583d71c248a1eb6aab9ee86e) (struct bt\_conn \*conn, const struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) \*cb) |
|  | Overlay authentication callbacks used for a given connection. |
| int | [bt\_conn\_auth\_info\_cb\_register](group__bt__conn.md#gac6684a8089ebd495b539d661cf9fd13f) (struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) \*cb) |
|  | Register authentication information callbacks. |
| int | [bt\_conn\_auth\_info\_cb\_unregister](group__bt__conn.md#gac73a60b8b6b569b84fe17f707fa33f37) (struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) \*cb) |
|  | Unregister authentication information callbacks. |
| int | [bt\_conn\_auth\_passkey\_entry](group__bt__conn.md#ga3906d8d3d192e8a6ad1bf6b7acc32ff0) (struct bt\_conn \*conn, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int passkey) |
|  | Reply with entered passkey. |
| int | [bt\_conn\_auth\_keypress\_notify](group__bt__conn.md#ga2987a902da4f5cfe3671c60d154ced7e) (struct bt\_conn \*conn, enum [bt\_conn\_auth\_keypress](group__bt__conn.md#ga57465d3a61214531ddaffc2c30939043) type) |
|  | Send Passkey Keypress Notification during pairing. |
| int | [bt\_conn\_auth\_cancel](group__bt__conn.md#ga89e5fc4bcab3f5598d20a9cd8ace5f59) (struct bt\_conn \*conn) |
|  | Cancel ongoing authenticated pairing. |
| int | [bt\_conn\_auth\_passkey\_confirm](group__bt__conn.md#gab8c3ecf2a3d68e54379917844a29d995) (struct bt\_conn \*conn) |
|  | Reply if passkey was confirmed to match by user. |
| int | [bt\_conn\_auth\_pairing\_confirm](group__bt__conn.md#ga3e15b9deb6787d3e415bbea35c9aa91d) (struct bt\_conn \*conn) |
|  | Reply if incoming pairing was confirmed by user. |
| int | [bt\_conn\_auth\_pincode\_entry](group__bt__conn.md#ga4002a1b092832807218afa8ad279ab98) (struct bt\_conn \*conn, const char \*pin) |
|  | Reply with entered PIN code. |
| struct bt\_conn \* | [bt\_conn\_create\_br](group__bt__conn.md#gaf7849f332386f8903d35d6904f6c82b9) (const [bt\_addr\_t](structbt__addr__t.md) \*peer, const struct [bt\_br\_conn\_param](structbt__br__conn__param.md) \*param) |
|  | Initiate an BR/EDR connection to a remote device. |

## Detailed Description

Bluetooth connection handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [conn.h](conn_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
