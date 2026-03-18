---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__conn.html
original_path: doxygen/html/group__bt__conn.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Connection management

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Connection management.
[More...](#details)

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
| #define | [BT\_LE\_CONN\_PARAM\_INIT](#ga81de567c4c8cb691ef8b02633b42e342)(int\_min, int\_max, lat, to) |
|  | Initialize connection parameters. |
| #define | [BT\_LE\_CONN\_PARAM](#ga940d55c0d84c0cb8f09bc41074ae50d0)(int\_min, int\_max, lat, to) |
|  | Helper to declare connection parameters inline. |
| #define | [BT\_LE\_CONN\_PARAM\_DEFAULT](#ga82df8f439aeb3a156f4238deb085534a) |
|  | Default LE connection parameters: Connection Interval: 30-50 ms Latency: 0 Timeout: 4 s. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM\_INIT](#gabca56de0c82c14995738952dafb1fe2d)(\_pref\_tx\_phy, \_pref\_rx\_phy) |
|  | Initialize PHY parameters. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM](#ga39b69f0978f74b5f13f829e908b7cebb)(\_pref\_tx\_phy, \_pref\_rx\_phy) |
|  | Helper to declare PHY parameters inline. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM\_1M](#ga3ec555bb4ace5e9c7c13735820fd31de) |
|  | Only LE 1M PHY. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM\_2M](#ga633126e356658886e9fa3f3217cb4e2c) |
|  | Only LE 2M PHY. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM\_CODED](#ga4915244a6cd70995514d6dde1ee0b45f) |
|  | Only LE Coded PHY. |
| #define | [BT\_CONN\_LE\_PHY\_PARAM\_ALL](#ga02c9d7a04ccf2f043293aed7a7f767a7) |
|  | All LE PHYs. |
| #define | [BT\_CONN\_LE\_DATA\_LEN\_PARAM\_INIT](#ga98f9dab71897382cf1187259a3b5660e)(\_tx\_max\_len, \_tx\_max\_time) |
|  | Initialize transmit data length parameters. |
| #define | [BT\_CONN\_LE\_DATA\_LEN\_PARAM](#ga102b97de8689fe3fb53f9691009de87f)(\_tx\_max\_len, \_tx\_max\_time) |
|  | Helper to declare transmit data length parameters inline. |
| #define | [BT\_LE\_DATA\_LEN\_PARAM\_DEFAULT](#gaf66746d834f7556dc77659741e27e0c9) |
|  | Default LE data length parameters. |
| #define | [BT\_LE\_DATA\_LEN\_PARAM\_MAX](#ga9cc26afda3c507cb5439184fedcd61ba) |
|  | Maximum LE data length parameters. |
| #define | [BT\_CONN\_INTERVAL\_TO\_MS](#ga707cc62b12c89478aebd0488a464a776)(interval) |
|  | Convert connection interval to milliseconds. |
| #define | [BT\_CONN\_INTERVAL\_TO\_US](#ga0a5fac126005684847ee7509bb98e382)(interval) |
|  | Convert connection interval to microseconds. |
| #define | [BT\_CONN\_ROLE\_MASTER](#ga047061be4b45bcdd5c84114b01567592)   \_\_DEPRECATED\_MACRO [BT\_CONN\_ROLE\_CENTRAL](#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30) |
|  | Connection role (central or peripheral). |
| #define | [BT\_CONN\_ROLE\_SLAVE](#ga65a7e3af728d3d60f484b4f166ac9882)   \_\_DEPRECATED\_MACRO [BT\_CONN\_ROLE\_PERIPHERAL](#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0) |
| #define | [BT\_CONN\_LE\_CREATE\_PARAM\_INIT](#ga8ac93a19c34d2821c158f310879fe00d)(\_options, \_interval, \_window) |
|  | Initialize create connection parameters. |
| #define | [BT\_CONN\_LE\_CREATE\_PARAM](#gae86425d432078e2ddca260eebc2802f1)(\_options, \_interval, \_window) |
|  | Helper to declare create connection parameters inline. |
| #define | [BT\_CONN\_LE\_CREATE\_CONN](#gab4203c55c20d83256ca036148c14a00d) |
|  | Default LE create connection parameters. |
| #define | [BT\_CONN\_LE\_CREATE\_CONN\_AUTO](#gaaba7c37a5c6e98e7b62ac12bde814d5d) |
|  | Default LE create connection using filter accept list parameters. |
| #define | [BT\_CONN\_CB\_DEFINE](#ga9227880a1ae5fc373d334171e1450f00)(\_name) |
|  | Register a callback structure for connection events. |
| #define | [BT\_PASSKEY\_INVALID](#gaf638077430b418f9879ac4ddf58ef17a)   0xffffffff |
|  | Special passkey value that can be used to disable a previously set fixed passkey. |
| #define | [BT\_BR\_CONN\_PARAM\_INIT](#ga986f563bfb741c70fbee39b3948d9d8d)(role\_switch) |
|  | Initialize BR/EDR connection parameters. |
| #define | [BT\_BR\_CONN\_PARAM](#ga6f99f4adfcef36a4d738783921965ca6)(role\_switch) |
|  | Helper to declare BR/EDR connection parameters inline. |
| #define | [BT\_BR\_CONN\_PARAM\_DEFAULT](#ga5ccdbff63a430a37a8a8077d8792f706)   [BT\_BR\_CONN\_PARAM](#ga6f99f4adfcef36a4d738783921965ca6)([true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)) |
|  | Default BR/EDR connection parameters: Role switch allowed. |

| Enumerations | |
| --- | --- |
| enum | { [BT\_CONN\_LE\_PHY\_OPT\_NONE](#gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98) = 0 , [BT\_CONN\_LE\_PHY\_OPT\_CODED\_S2](#gga08eb37185a763212e65c47ab4c886ecaa42e6ff627268b9eef111375d591f9f34) = BIT(0) , [BT\_CONN\_LE\_PHY\_OPT\_CODED\_S8](#gga08eb37185a763212e65c47ab4c886ecaad1d46128ba2516810af7383e850929e0) = BIT(1) } |
|  | Connection PHY options. [More...](#ga08eb37185a763212e65c47ab4c886eca) |
| enum | [bt\_conn\_type](#gab8dde20ae75b51f1e28dbeed06001f20) {     [BT\_CONN\_TYPE\_LE](#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2) = BIT(0) , [BT\_CONN\_TYPE\_BR](#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6) = BIT(1) , [BT\_CONN\_TYPE\_SCO](#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953) = BIT(2) , [BT\_CONN\_TYPE\_ISO](#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee) = BIT(3) ,     [BT\_CONN\_TYPE\_ALL](#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836)   } |
|  | Connection Type. [More...](#gab8dde20ae75b51f1e28dbeed06001f20) |
| enum | { [BT\_CONN\_ROLE\_CENTRAL](#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30) = 0 , [BT\_CONN\_ROLE\_PERIPHERAL](#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0) = 1 } |
| enum | [bt\_conn\_state](#ga9442c1479db60e2db40a2ea6de565282) { [BT\_CONN\_STATE\_DISCONNECTED](#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587) , [BT\_CONN\_STATE\_CONNECTING](#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd) , [BT\_CONN\_STATE\_CONNECTED](#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f) , [BT\_CONN\_STATE\_DISCONNECTING](#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f) } |
| enum | [bt\_security\_t](#gaf0c56cd26c4147f6c9f0faa11fa01783) {     [BT\_SECURITY\_L0](#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e) , [BT\_SECURITY\_L1](#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b) , [BT\_SECURITY\_L2](#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a) , [BT\_SECURITY\_L3](#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631) ,     [BT\_SECURITY\_L4](#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81) , [BT\_SECURITY\_FORCE\_PAIR](#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae) = BIT(7)   } |
|  | Security level. [More...](#gaf0c56cd26c4147f6c9f0faa11fa01783) |
| enum | [bt\_security\_flag](#ga2f8712bbf3410de5cbe6ce489fe30e5e) { [BT\_SECURITY\_FLAG\_SC](#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6) = BIT(0) , [BT\_SECURITY\_FLAG\_OOB](#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198) = BIT(1) } |
|  | Security Info Flags. [More...](#ga2f8712bbf3410de5cbe6ce489fe30e5e) |
| enum | [bt\_conn\_le\_tx\_power\_phy](#ga737d8118f8aba8985292d92d0604b190) {     [BT\_CONN\_LE\_TX\_POWER\_PHY\_NONE](#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a) , [BT\_CONN\_LE\_TX\_POWER\_PHY\_1M](#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046) , [BT\_CONN\_LE\_TX\_POWER\_PHY\_2M](#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800) , [BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S8](#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2) ,     [BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S2](#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296)   } |
| enum | [bt\_conn\_auth\_keypress](#ga57465d3a61214531ddaffc2c30939043) {     [BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_STARTED](#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6) = 0x00 , [BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ENTERED](#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1) = 0x01 , [BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ERASED](#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529) = 0x02 , [BT\_CONN\_AUTH\_KEYPRESS\_CLEARED](#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da) = 0x03 ,     [BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_COMPLETED](#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8) = 0x04   } |
|  | Passkey Keypress Notification type. [More...](#ga57465d3a61214531ddaffc2c30939043) |
| enum | { [BT\_CONN\_LE\_OPT\_NONE](#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9) = 0 , [BT\_CONN\_LE\_OPT\_CODED](#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b) = BIT(0) , [BT\_CONN\_LE\_OPT\_NO\_1M](#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9) = BIT(1) } |
| enum | [bt\_security\_err](#gaa9420ff489fd5857ff076406442679ff) {     [BT\_SECURITY\_ERR\_SUCCESS](#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05) , [BT\_SECURITY\_ERR\_AUTH\_FAIL](#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7) , [BT\_SECURITY\_ERR\_PIN\_OR\_KEY\_MISSING](#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171) , [BT\_SECURITY\_ERR\_OOB\_NOT\_AVAILABLE](#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7) ,     [BT\_SECURITY\_ERR\_AUTH\_REQUIREMENT](#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae) , [BT\_SECURITY\_ERR\_PAIR\_NOT\_SUPPORTED](#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6) , [BT\_SECURITY\_ERR\_PAIR\_NOT\_ALLOWED](#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f) , [BT\_SECURITY\_ERR\_INVALID\_PARAM](#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5) ,     [BT\_SECURITY\_ERR\_KEY\_REJECTED](#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216) , [BT\_SECURITY\_ERR\_UNSPECIFIED](#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242)   } |

| Functions | |
| --- | --- |
| struct bt\_conn \* | [bt\_conn\_ref](#ga060d51eb2208de6f805b1fc0672d2d0c) (struct bt\_conn \*conn) |
|  | Increment a connection's reference count. |
| void | [bt\_conn\_unref](#ga4b18c6b22a9f02be0d7d078b2ce51ff6) (struct bt\_conn \*conn) |
|  | Decrement a connection's reference count. |
| void | [bt\_conn\_foreach](#ga5bdf8e8efc85138d3631dc1efffc3916) (enum [bt\_conn\_type](#gab8dde20ae75b51f1e28dbeed06001f20) type, void(\*func)(struct bt\_conn \*conn, void \*data), void \*data) |
|  | Iterate through all bt\_conn objects. |
| struct bt\_conn \* | [bt\_conn\_lookup\_addr\_le](#ga1bfe349efd8a7de31e9457fe439d746a) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer) |
|  | Look up an existing connection by address. |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [bt\_conn\_get\_dst](#ga77108581b8f61485ca840e4bf7a17087) (const struct bt\_conn \*conn) |
|  | Get destination (peer) address of a connection. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_conn\_index](#gad4aed76b80cc815f748ad0e84ae3d87c) (const struct bt\_conn \*conn) |
|  | Get array index of a connection. |
| int | [bt\_conn\_get\_info](#ga2de54f2ac83f0d8dca2a85a9fbfadcaa) (const struct bt\_conn \*conn, struct [bt\_conn\_info](structbt__conn__info.md) \*info) |
|  | Get connection info. |
| int | [bt\_conn\_get\_remote\_info](#ga6ea4478db6d95bd6a0d316399db36d92) (struct bt\_conn \*conn, struct [bt\_conn\_remote\_info](structbt__conn__remote__info.md) \*remote\_info) |
|  | Get connection info for the remote device. |
| int | [bt\_conn\_le\_get\_tx\_power\_level](#gaa5289154bc508444f68df7abcef18aca) (struct bt\_conn \*conn, struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) \*tx\_power\_level) |
|  | Get connection transmit power level. |
| int | [bt\_conn\_le\_enhanced\_get\_tx\_power\_level](#gaa79eada87d698f4998af876d03d7e92b) (struct bt\_conn \*conn, struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) \*tx\_power) |
|  | Get local enhanced connection transmit power level. |
| int | [bt\_conn\_le\_get\_remote\_tx\_power\_level](#ga0843a2e0b6f16ebd132a3a512cfd27a4) (struct bt\_conn \*conn, enum [bt\_conn\_le\_tx\_power\_phy](#ga737d8118f8aba8985292d92d0604b190) phy) |
|  | Get remote (peer) transmit power level. |
| int | [bt\_conn\_le\_set\_tx\_power\_report\_enable](#gaa1f38911acee0534a8a6e414018c6fb6) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) local\_enable, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) remote\_enable) |
|  | Enable transmit power reporting. |
| int | [bt\_conn\_le\_param\_update](#gab44a964725f54ed2d37de17c6e2fd3eb) (struct bt\_conn \*conn, const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param) |
|  | Update the connection parameters. |
| int | [bt\_conn\_le\_data\_len\_update](#ga8a2006f6e34b20c7e8ef65a73f431a57) (struct bt\_conn \*conn, const struct [bt\_conn\_le\_data\_len\_param](structbt__conn__le__data__len__param.md) \*param) |
|  | Update the connection transmit data length parameters. |
| int | [bt\_conn\_le\_phy\_update](#gae13ed81b1e7928f44b8fdf85995b3e58) (struct bt\_conn \*conn, const struct [bt\_conn\_le\_phy\_param](structbt__conn__le__phy__param.md) \*param) |
|  | Update the connection PHY parameters. |
| int | [bt\_conn\_disconnect](#ga14e7c852b0271781594e742ae509c5d3) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | Disconnect from a remote device or cancel pending connection. |
| int | [bt\_conn\_le\_create](#ga8d66f3e0262a51279e9fa8b3139252e6) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer, const struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) \*create\_param, const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param, struct bt\_conn \*\*conn) |
|  | Initiate an LE connection to a remote device. |
| int | [bt\_conn\_le\_create\_synced](#ga98f99c893e444d1ad1ecd9139803c0b1) (const struct bt\_le\_ext\_adv \*adv, const struct [bt\_conn\_le\_create\_synced\_param](structbt__conn__le__create__synced__param.md) \*synced\_param, const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param, struct bt\_conn \*\*conn) |
|  | Create a connection to a synced device. |
| int | [bt\_conn\_le\_create\_auto](#gaecfaf2cb44772511dbb585de8f76f09b) (const struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) \*create\_param, const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*conn\_param) |
|  | Automatically connect to remote devices in the filter accept list. |
| int | [bt\_conn\_create\_auto\_stop](#ga62dc2663b4fa39a33adb76dc9a136aa4) (void) |
|  | Stop automatic connect creation. |
| int | [bt\_le\_set\_auto\_conn](#ga8eea2211705d0691acc6ee4e0c37a47a) (const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*addr, const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \*param) |
|  | Automatically connect to remote device if it's in range. |
| int | [bt\_conn\_set\_security](#gae001f1268e1ff42c3c974c95dcb6735d) (struct bt\_conn \*conn, [bt\_security\_t](#gaf0c56cd26c4147f6c9f0faa11fa01783) sec) |
|  | Set security level for a connection. |
| [bt\_security\_t](#gaf0c56cd26c4147f6c9f0faa11fa01783) | [bt\_conn\_get\_security](#ga4b43ef0f30146808e560991a302e88ad) (const struct bt\_conn \*conn) |
|  | Get security level for a connection. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_conn\_enc\_key\_size](#gaff3e6aa16b68e5da7dab53289295545e) (const struct bt\_conn \*conn) |
|  | Get encryption key size. |
| void | [bt\_conn\_cb\_register](#ga33b35e6457af183e059078aead4562b4) (struct [bt\_conn\_cb](structbt__conn__cb.md) \*cb) |
|  | Register connection callbacks. |
| int | [bt\_conn\_cb\_unregister](#gad2f90b34390e3c3697fd455ae4ef5f31) (struct [bt\_conn\_cb](structbt__conn__cb.md) \*cb) |
|  | Unregister connection callbacks. |
| void | [bt\_set\_bondable](#ga014db594b17a3b5d7d954e64ad8de759) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable/disable bonding. |
| int | [bt\_conn\_set\_bondable](#ga4165819d12dd96e00dfa2fd6f4b95669) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set/clear the bonding flag for a given connection. |
| void | [bt\_le\_oob\_set\_sc\_flag](#gad02f8fe587efd543c0c81cace3f63d63) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Allow/disallow remote LE SC OOB data to be used for pairing. |
| void | [bt\_le\_oob\_set\_legacy\_flag](#ga978770d46d7c8af854a61261c14cb892) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Allow/disallow remote legacy OOB data to be used for pairing. |
| int | [bt\_le\_oob\_set\_legacy\_tk](#ga0f889983cfabafe826b4feb6899b95ba) (struct bt\_conn \*conn, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tk) |
|  | Set OOB Temporary Key to be used for pairing. |
| int | [bt\_le\_oob\_set\_sc\_data](#gac365f9748ad0737f09142ee1de982503) (struct bt\_conn \*conn, const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*oobd\_local, const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*oobd\_remote) |
|  | Set OOB data during LE Secure Connections (SC) pairing procedure. |
| int | [bt\_le\_oob\_get\_sc\_data](#ga096552403b5bcd0107f69eded772b1ee) (struct bt\_conn \*conn, const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*\*oobd\_local, const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*\*oobd\_remote) |
|  | Get OOB data used for LE Secure Connections (SC) pairing procedure. |
| int | [bt\_passkey\_set](#ga32c7598c086f209f9e1dee2aacbb40a1) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int passkey) |
|  | Set a fixed passkey to be used for pairing. |
| int | [bt\_conn\_auth\_cb\_register](#ga1bf13d2dfdbdf0a72f9b1c759ef23f60) (const struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) \*cb) |
|  | Register authentication callbacks. |
| int | [bt\_conn\_auth\_cb\_overlay](#ga81077385583d71c248a1eb6aab9ee86e) (struct bt\_conn \*conn, const struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) \*cb) |
|  | Overlay authentication callbacks used for a given connection. |
| int | [bt\_conn\_auth\_info\_cb\_register](#gac6684a8089ebd495b539d661cf9fd13f) (struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) \*cb) |
|  | Register authentication information callbacks. |
| int | [bt\_conn\_auth\_info\_cb\_unregister](#gac73a60b8b6b569b84fe17f707fa33f37) (struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) \*cb) |
|  | Unregister authentication information callbacks. |
| int | [bt\_conn\_auth\_passkey\_entry](#ga3906d8d3d192e8a6ad1bf6b7acc32ff0) (struct bt\_conn \*conn, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int passkey) |
|  | Reply with entered passkey. |
| int | [bt\_conn\_auth\_keypress\_notify](#ga2987a902da4f5cfe3671c60d154ced7e) (struct bt\_conn \*conn, enum [bt\_conn\_auth\_keypress](#ga57465d3a61214531ddaffc2c30939043) type) |
|  | Send Passkey Keypress Notification during pairing. |
| int | [bt\_conn\_auth\_cancel](#ga89e5fc4bcab3f5598d20a9cd8ace5f59) (struct bt\_conn \*conn) |
|  | Cancel ongoing authenticated pairing. |
| int | [bt\_conn\_auth\_passkey\_confirm](#gab8c3ecf2a3d68e54379917844a29d995) (struct bt\_conn \*conn) |
|  | Reply if passkey was confirmed to match by user. |
| int | [bt\_conn\_auth\_pairing\_confirm](#ga3e15b9deb6787d3e415bbea35c9aa91d) (struct bt\_conn \*conn) |
|  | Reply if incoming pairing was confirmed by user. |
| int | [bt\_conn\_auth\_pincode\_entry](#ga4002a1b092832807218afa8ad279ab98) (struct bt\_conn \*conn, const char \*pin) |
|  | Reply with entered PIN code. |
| struct bt\_conn \* | [bt\_conn\_create\_br](#gaf7849f332386f8903d35d6904f6c82b9) (const [bt\_addr\_t](structbt__addr__t.md) \*peer, const struct [bt\_br\_conn\_param](structbt__br__conn__param.md) \*param) |
|  | Initiate an BR/EDR connection to a remote device. |
| struct bt\_conn \* | [bt\_conn\_create\_sco](#gac270287d6764dff1963f859a51a438e4) (const [bt\_addr\_t](structbt__addr__t.md) \*peer) |
|  | Initiate an SCO connection to a remote device. |

## Detailed Description

Connection management.

## Macro Definition Documentation

## [◆ ](#ga6f99f4adfcef36a4d738783921965ca6)BT\_BR\_CONN\_PARAM

| #define BT\_BR\_CONN\_PARAM | ( |  | *role\_switch* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

((struct [bt\_br\_conn\_param](structbt__br__conn__param.md)[]) { \

BT\_BR\_CONN\_PARAM\_INIT(role\_switch) \

})

[bt\_br\_conn\_param](structbt__br__conn__param.md)

Connection parameters for BR/EDR connections.

**Definition** conn.h:1734

Helper to declare BR/EDR connection parameters inline.

Parameters
:   | role\_switch | True if role switch is allowed |
    | --- | --- |

## [◆ ](#ga5ccdbff63a430a37a8a8077d8792f706)BT\_BR\_CONN\_PARAM\_DEFAULT

| #define BT\_BR\_CONN\_PARAM\_DEFAULT   [BT\_BR\_CONN\_PARAM](#ga6f99f4adfcef36a4d738783921965ca6)([true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)) |
| --- |

`#include <[conn.h](conn_8h.md)>`

Default BR/EDR connection parameters: Role switch allowed.

## [◆ ](#ga986f563bfb741c70fbee39b3948d9d8d)BT\_BR\_CONN\_PARAM\_INIT

| #define BT\_BR\_CONN\_PARAM\_INIT | ( |  | *role\_switch* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

{ \

.allow\_role\_switch = (role\_switch), \

}

Initialize BR/EDR connection parameters.

Parameters
:   | role\_switch | True if role switch is allowed |
    | --- | --- |

## [◆ ](#ga9227880a1ae5fc373d334171e1450f00)BT\_CONN\_CB\_DEFINE

| #define BT\_CONN\_CB\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([bt\_conn\_cb](structbt__conn__cb.md), \

\_CONCAT(bt\_conn\_cb\_, \

\_name))

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[bt\_conn\_cb](structbt__conn__cb.md)

Connection callback structure.

**Definition** conn.h:957

Register a callback structure for connection events.

Parameters
:   | \_name | Name of callback structure. |
    | --- | --- |

## [◆ ](#ga707cc62b12c89478aebd0488a464a776)BT\_CONN\_INTERVAL\_TO\_MS

| #define BT\_CONN\_INTERVAL\_TO\_MS | ( |  | *interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

((interval) \* 5U / 4U)

Convert connection interval to milliseconds.

Multiply by 1.25 to get milliseconds.

Note that this may be inaccurate, as something like 7.5 ms cannot be accurately presented with integers.

## [◆ ](#ga0a5fac126005684847ee7509bb98e382)BT\_CONN\_INTERVAL\_TO\_US

| #define BT\_CONN\_INTERVAL\_TO\_US | ( |  | *interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

((interval) \* 1250U)

Convert connection interval to microseconds.

Multiply by 1250 to get microseconds.

## [◆ ](#gab4203c55c20d83256ca036148c14a00d)BT\_CONN\_LE\_CREATE\_CONN

| #define BT\_CONN\_LE\_CREATE\_CONN |
| --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

[BT\_CONN\_LE\_CREATE\_PARAM](#gae86425d432078e2ddca260eebc2802f1)([BT\_CONN\_LE\_OPT\_NONE](#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9), \

[BT\_GAP\_SCAN\_FAST\_INTERVAL](group__bt__gap__defines.md#ga747caa714962215453a966a323e77cf8), \

[BT\_GAP\_SCAN\_FAST\_INTERVAL](group__bt__gap__defines.md#ga747caa714962215453a966a323e77cf8))

[BT\_CONN\_LE\_CREATE\_PARAM](#gae86425d432078e2ddca260eebc2802f1)

#define BT\_CONN\_LE\_CREATE\_PARAM(\_options, \_interval, \_window)

Helper to declare create connection parameters inline.

**Definition** conn.h:739

[BT\_CONN\_LE\_OPT\_NONE](#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9)

@ BT\_CONN\_LE\_OPT\_NONE

Convenience value when no options are specified.

**Definition** conn.h:667

[BT\_GAP\_SCAN\_FAST\_INTERVAL](group__bt__gap__defines.md#ga747caa714962215453a966a323e77cf8)

#define BT\_GAP\_SCAN\_FAST\_INTERVAL

**Definition** gap.h:711

Default LE create connection parameters.

Scan continuously by setting scan interval equal to scan window.

## [◆ ](#gaaba7c37a5c6e98e7b62ac12bde814d5d)BT\_CONN\_LE\_CREATE\_CONN\_AUTO

| #define BT\_CONN\_LE\_CREATE\_CONN\_AUTO |
| --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

[BT\_CONN\_LE\_CREATE\_PARAM](#gae86425d432078e2ddca260eebc2802f1)([BT\_CONN\_LE\_OPT\_NONE](#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9), \

[BT\_GAP\_SCAN\_FAST\_INTERVAL](group__bt__gap__defines.md#ga747caa714962215453a966a323e77cf8), \

[BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0))

[BT\_GAP\_SCAN\_FAST\_WINDOW](group__bt__gap__defines.md#ga100e1c20813630848a1a80390e8a06a0)

#define BT\_GAP\_SCAN\_FAST\_WINDOW

**Definition** gap.h:712

Default LE create connection using filter accept list parameters.

Scan window: 30 ms. Scan interval: 60 ms.

## [◆ ](#gae86425d432078e2ddca260eebc2802f1)BT\_CONN\_LE\_CREATE\_PARAM

| #define BT\_CONN\_LE\_CREATE\_PARAM | ( |  | *\_options*, |
| --- | --- | --- | --- |
|  |  |  | *\_interval*, |
|  |  |  | *\_window* ) |

`#include <[conn.h](conn_8h.md)>`

**Value:**

((struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md)[]) { \

BT\_CONN\_LE\_CREATE\_PARAM\_INIT(\_options, \_interval, \_window) \

})

[bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md)

**Definition** conn.h:684

Helper to declare create connection parameters inline.

Parameters
:   | \_options | Create connection options. |
    | --- | --- |
    | \_interval | Create connection scan interval (N \* 0.625 ms). |
    | \_window | Create connection scan window (N \* 0.625 ms). |

## [◆ ](#ga8ac93a19c34d2821c158f310879fe00d)BT\_CONN\_LE\_CREATE\_PARAM\_INIT

| #define BT\_CONN\_LE\_CREATE\_PARAM\_INIT | ( |  | *\_options*, |
| --- | --- | --- | --- |
|  |  |  | *\_interval*, |
|  |  |  | *\_window* ) |

`#include <[conn.h](conn_8h.md)>`

**Value:**

{ \

.options = (\_options), \

.interval = (\_interval), \

.window = (\_window), \

.interval\_coded = 0, \

.window\_coded = 0, \

.timeout = 0, \

}

Initialize create connection parameters.

Parameters
:   | \_options | Create connection options. |
    | --- | --- |
    | \_interval | Create connection scan interval (N \* 0.625 ms). |
    | \_window | Create connection scan window (N \* 0.625 ms). |

## [◆ ](#ga102b97de8689fe3fb53f9691009de87f)BT\_CONN\_LE\_DATA\_LEN\_PARAM

| #define BT\_CONN\_LE\_DATA\_LEN\_PARAM | ( |  | *\_tx\_max\_len*, |
| --- | --- | --- | --- |
|  |  |  | *\_tx\_max\_time* ) |

`#include <[conn.h](conn_8h.md)>`

**Value:**

((struct [bt\_conn\_le\_data\_len\_param](structbt__conn__le__data__len__param.md)[]) { \

BT\_CONN\_LE\_DATA\_LEN\_PARAM\_INIT(\_tx\_max\_len, \_tx\_max\_time) \

})

[bt\_conn\_le\_data\_len\_param](structbt__conn__le__data__len__param.md)

Connection data length parameters for LE connections.

**Definition** conn.h:161

Helper to declare transmit data length parameters inline.

Parameters
:   | \_tx\_max\_len | Maximum Link Layer transmission payload size in bytes. |
    | --- | --- |
    | \_tx\_max\_time | Maximum Link Layer transmission payload time in us. |

## [◆ ](#ga98f9dab71897382cf1187259a3b5660e)BT\_CONN\_LE\_DATA\_LEN\_PARAM\_INIT

| #define BT\_CONN\_LE\_DATA\_LEN\_PARAM\_INIT | ( |  | *\_tx\_max\_len*, |
| --- | --- | --- | --- |
|  |  |  | *\_tx\_max\_time* ) |

`#include <[conn.h](conn_8h.md)>`

**Value:**

{ \

.tx\_max\_len = (\_tx\_max\_len), \

.tx\_max\_time = (\_tx\_max\_time), \

}

Initialize transmit data length parameters.

Parameters
:   | \_tx\_max\_len | Maximum Link Layer transmission payload size in bytes. |
    | --- | --- |
    | \_tx\_max\_time | Maximum Link Layer transmission payload time in us. |

## [◆ ](#ga39b69f0978f74b5f13f829e908b7cebb)BT\_CONN\_LE\_PHY\_PARAM

| #define BT\_CONN\_LE\_PHY\_PARAM | ( |  | *\_pref\_tx\_phy*, |
| --- | --- | --- | --- |
|  |  |  | *\_pref\_rx\_phy* ) |

`#include <[conn.h](conn_8h.md)>`

**Value:**

((struct [bt\_conn\_le\_phy\_param](structbt__conn__le__phy__param.md) []) { \

BT\_CONN\_LE\_PHY\_PARAM\_INIT(\_pref\_tx\_phy, \_pref\_rx\_phy) \

})

[bt\_conn\_le\_phy\_param](structbt__conn__le__phy__param.md)

Preferred PHY parameters for LE connections.

**Definition** conn.h:100

Helper to declare PHY parameters inline.

Parameters
:   | \_pref\_tx\_phy | Bitmask of preferred transmit PHYs. |
    | --- | --- |
    | \_pref\_rx\_phy | Bitmask of preferred receive PHYs. |

## [◆ ](#ga3ec555bb4ace5e9c7c13735820fd31de)BT\_CONN\_LE\_PHY\_PARAM\_1M

| #define BT\_CONN\_LE\_PHY\_PARAM\_1M |
| --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

[BT\_CONN\_LE\_PHY\_PARAM](#ga39b69f0978f74b5f13f829e908b7cebb)([BT\_GAP\_LE\_PHY\_1M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba53eff400720a20fe1a91da4834bad752), \

[BT\_GAP\_LE\_PHY\_1M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba53eff400720a20fe1a91da4834bad752))

[BT\_CONN\_LE\_PHY\_PARAM](#ga39b69f0978f74b5f13f829e908b7cebb)

#define BT\_CONN\_LE\_PHY\_PARAM(\_pref\_tx\_phy, \_pref\_rx\_phy)

Helper to declare PHY parameters inline.

**Definition** conn.h:123

[BT\_GAP\_LE\_PHY\_1M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba53eff400720a20fe1a91da4834bad752)

@ BT\_GAP\_LE\_PHY\_1M

LE 1M PHY.

**Definition** gap.h:740

Only LE 1M PHY.

## [◆ ](#ga633126e356658886e9fa3f3217cb4e2c)BT\_CONN\_LE\_PHY\_PARAM\_2M

| #define BT\_CONN\_LE\_PHY\_PARAM\_2M |
| --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

[BT\_CONN\_LE\_PHY\_PARAM](#ga39b69f0978f74b5f13f829e908b7cebb)([BT\_GAP\_LE\_PHY\_2M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba662049cc8293959194bcb481e1dd50a8), \

[BT\_GAP\_LE\_PHY\_2M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba662049cc8293959194bcb481e1dd50a8))

[BT\_GAP\_LE\_PHY\_2M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba662049cc8293959194bcb481e1dd50a8)

@ BT\_GAP\_LE\_PHY\_2M

LE 2M PHY.

**Definition** gap.h:742

Only LE 2M PHY.

## [◆ ](#ga02c9d7a04ccf2f043293aed7a7f767a7)BT\_CONN\_LE\_PHY\_PARAM\_ALL

| #define BT\_CONN\_LE\_PHY\_PARAM\_ALL |
| --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

[BT\_CONN\_LE\_PHY\_PARAM](#ga39b69f0978f74b5f13f829e908b7cebb)([BT\_GAP\_LE\_PHY\_1M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba53eff400720a20fe1a91da4834bad752) | \

[BT\_GAP\_LE\_PHY\_2M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba662049cc8293959194bcb481e1dd50a8) | \

[BT\_GAP\_LE\_PHY\_CODED](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba97d042e48448fdf6a9e35e5d38cb14c3), \

[BT\_GAP\_LE\_PHY\_1M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba53eff400720a20fe1a91da4834bad752) | \

[BT\_GAP\_LE\_PHY\_2M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba662049cc8293959194bcb481e1dd50a8) | \

[BT\_GAP\_LE\_PHY\_CODED](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba97d042e48448fdf6a9e35e5d38cb14c3))

[BT\_GAP\_LE\_PHY\_CODED](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba97d042e48448fdf6a9e35e5d38cb14c3)

@ BT\_GAP\_LE\_PHY\_CODED

LE Coded PHY.

**Definition** gap.h:744

All LE PHYs.

## [◆ ](#ga4915244a6cd70995514d6dde1ee0b45f)BT\_CONN\_LE\_PHY\_PARAM\_CODED

| #define BT\_CONN\_LE\_PHY\_PARAM\_CODED |
| --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

[BT\_CONN\_LE\_PHY\_PARAM](#ga39b69f0978f74b5f13f829e908b7cebb)([BT\_GAP\_LE\_PHY\_CODED](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba97d042e48448fdf6a9e35e5d38cb14c3), \

[BT\_GAP\_LE\_PHY\_CODED](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba97d042e48448fdf6a9e35e5d38cb14c3))

Only LE Coded PHY.

## [◆ ](#gabca56de0c82c14995738952dafb1fe2d)BT\_CONN\_LE\_PHY\_PARAM\_INIT

| #define BT\_CONN\_LE\_PHY\_PARAM\_INIT | ( |  | *\_pref\_tx\_phy*, |
| --- | --- | --- | --- |
|  |  |  | *\_pref\_rx\_phy* ) |

`#include <[conn.h](conn_8h.md)>`

**Value:**

{ \

.options = [BT\_CONN\_LE\_PHY\_OPT\_NONE](#gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98), \

.pref\_tx\_phy = (\_pref\_tx\_phy), \

.pref\_rx\_phy = (\_pref\_rx\_phy), \

}

[BT\_CONN\_LE\_PHY\_OPT\_NONE](#gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98)

@ BT\_CONN\_LE\_PHY\_OPT\_NONE

Convenience value when no options are specified.

**Definition** conn.h:90

Initialize PHY parameters.

Parameters
:   | \_pref\_tx\_phy | Bitmask of preferred transmit PHYs. |
    | --- | --- |
    | \_pref\_rx\_phy | Bitmask of preferred receive PHYs. |

## [◆ ](#ga047061be4b45bcdd5c84114b01567592)BT\_CONN\_ROLE\_MASTER

| #define BT\_CONN\_ROLE\_MASTER   \_\_DEPRECATED\_MACRO [BT\_CONN\_ROLE\_CENTRAL](#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30) |
| --- |

`#include <[conn.h](conn_8h.md)>`

Connection role (central or peripheral).

## [◆ ](#ga65a7e3af728d3d60f484b4f166ac9882)BT\_CONN\_ROLE\_SLAVE

| #define BT\_CONN\_ROLE\_SLAVE   \_\_DEPRECATED\_MACRO [BT\_CONN\_ROLE\_PERIPHERAL](#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0) |
| --- |

`#include <[conn.h](conn_8h.md)>`

## [◆ ](#ga940d55c0d84c0cb8f09bc41074ae50d0)BT\_LE\_CONN\_PARAM

| #define BT\_LE\_CONN\_PARAM | ( |  | *int\_min*, |
| --- | --- | --- | --- |
|  |  |  | *int\_max*, |
|  |  |  | *lat*, |
|  |  |  | *to* ) |

`#include <[conn.h](conn_8h.md)>`

**Value:**

((struct [bt\_le\_conn\_param](structbt__le__conn__param.md)[]) { \

BT\_LE\_CONN\_PARAM\_INIT(int\_min, int\_max, lat, to) \

})

[bt\_le\_conn\_param](structbt__le__conn__param.md)

Connection parameters for LE connections.

**Definition** conn.h:38

Helper to declare connection parameters inline.

Parameters
:   | int\_min | Minimum Connection Interval (N \* 1.25 ms) |
    | --- | --- |
    | int\_max | Maximum Connection Interval (N \* 1.25 ms) |
    | lat | Connection Latency |
    | to | Supervision Timeout (N \* 10 ms) |

## [◆ ](#ga82df8f439aeb3a156f4238deb085534a)BT\_LE\_CONN\_PARAM\_DEFAULT

| #define BT\_LE\_CONN\_PARAM\_DEFAULT |
| --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

[BT\_LE\_CONN\_PARAM](#ga940d55c0d84c0cb8f09bc41074ae50d0)([BT\_GAP\_INIT\_CONN\_INT\_MIN](group__bt__gap__defines.md#gadaa7f1547c4ea22936087c181d82a552), \

[BT\_GAP\_INIT\_CONN\_INT\_MAX](group__bt__gap__defines.md#ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1), \

0, 400)

[BT\_LE\_CONN\_PARAM](#ga940d55c0d84c0cb8f09bc41074ae50d0)

#define BT\_LE\_CONN\_PARAM(int\_min, int\_max, lat, to)

Helper to declare connection parameters inline.

**Definition** conn.h:67

[BT\_GAP\_INIT\_CONN\_INT\_MAX](group__bt__gap__defines.md#ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1)

#define BT\_GAP\_INIT\_CONN\_INT\_MAX

**Definition** gap.h:730

[BT\_GAP\_INIT\_CONN\_INT\_MIN](group__bt__gap__defines.md#gadaa7f1547c4ea22936087c181d82a552)

#define BT\_GAP\_INIT\_CONN\_INT\_MIN

**Definition** gap.h:729

Default LE connection parameters: Connection Interval: 30-50 ms Latency: 0 Timeout: 4 s.

## [◆ ](#ga81de567c4c8cb691ef8b02633b42e342)BT\_LE\_CONN\_PARAM\_INIT

| #define BT\_LE\_CONN\_PARAM\_INIT | ( |  | *int\_min*, |
| --- | --- | --- | --- |
|  |  |  | *int\_max*, |
|  |  |  | *lat*, |
|  |  |  | *to* ) |

`#include <[conn.h](conn_8h.md)>`

**Value:**

{ \

.interval\_min = (int\_min), \

.interval\_max = (int\_max), \

.latency = (lat), \

.timeout = (to), \

}

Initialize connection parameters.

Parameters
:   | int\_min | Minimum Connection Interval (N \* 1.25 ms) |
    | --- | --- |
    | int\_max | Maximum Connection Interval (N \* 1.25 ms) |
    | lat | Connection Latency |
    | to | Supervision Timeout (N \* 10 ms) |

## [◆ ](#gaf66746d834f7556dc77659741e27e0c9)BT\_LE\_DATA\_LEN\_PARAM\_DEFAULT

| #define BT\_LE\_DATA\_LEN\_PARAM\_DEFAULT |
| --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

[BT\_CONN\_LE\_DATA\_LEN\_PARAM](#ga102b97de8689fe3fb53f9691009de87f)([BT\_GAP\_DATA\_LEN\_DEFAULT](group__bt__gap__defines.md#ga90cfab7c375a8af6f9224a5635cbd023), \

[BT\_GAP\_DATA\_TIME\_DEFAULT](group__bt__gap__defines.md#ga245249c0b6f8ccc419f2132f76362908))

[BT\_CONN\_LE\_DATA\_LEN\_PARAM](#ga102b97de8689fe3fb53f9691009de87f)

#define BT\_CONN\_LE\_DATA\_LEN\_PARAM(\_tx\_max\_len, \_tx\_max\_time)

Helper to declare transmit data length parameters inline.

**Definition** conn.h:184

[BT\_GAP\_DATA\_TIME\_DEFAULT](group__bt__gap__defines.md#ga245249c0b6f8ccc419f2132f76362908)

#define BT\_GAP\_DATA\_TIME\_DEFAULT

Default data time.

**Definition** gap.h:802

[BT\_GAP\_DATA\_LEN\_DEFAULT](group__bt__gap__defines.md#ga90cfab7c375a8af6f9224a5635cbd023)

#define BT\_GAP\_DATA\_LEN\_DEFAULT

Default data length.

**Definition** gap.h:797

Default LE data length parameters.

## [◆ ](#ga9cc26afda3c507cb5439184fedcd61ba)BT\_LE\_DATA\_LEN\_PARAM\_MAX

| #define BT\_LE\_DATA\_LEN\_PARAM\_MAX |
| --- |

`#include <[conn.h](conn_8h.md)>`

**Value:**

[BT\_CONN\_LE\_DATA\_LEN\_PARAM](#ga102b97de8689fe3fb53f9691009de87f)([BT\_GAP\_DATA\_LEN\_MAX](group__bt__gap__defines.md#gacf5f35866d4677bd45c6e567886cabb9), \

[BT\_GAP\_DATA\_TIME\_MAX](group__bt__gap__defines.md#ga379b5d8d7f243abbc584c288cd01815f))

[BT\_GAP\_DATA\_TIME\_MAX](group__bt__gap__defines.md#ga379b5d8d7f243abbc584c288cd01815f)

#define BT\_GAP\_DATA\_TIME\_MAX

Maximum data time.

**Definition** gap.h:804

[BT\_GAP\_DATA\_LEN\_MAX](group__bt__gap__defines.md#gacf5f35866d4677bd45c6e567886cabb9)

#define BT\_GAP\_DATA\_LEN\_MAX

Maximum data length.

**Definition** gap.h:799

Maximum LE data length parameters.

## [◆ ](#gaf638077430b418f9879ac4ddf58ef17a)BT\_PASSKEY\_INVALID

| #define BT\_PASSKEY\_INVALID   0xffffffff |
| --- |

`#include <[conn.h](conn_8h.md)>`

Special passkey value that can be used to disable a previously set fixed passkey.

## Enumeration Type Documentation

## [◆ ](#ga3afc8024ddbcd3bf5a809706e39f74bc)anonymous enum

| anonymous enum |
| --- |

`#include <[conn.h](conn_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_CONN\_LE\_OPT\_NONE | Convenience value when no options are specified. |
| BT\_CONN\_LE\_OPT\_CODED | Enable LE Coded PHY.  Enable scanning on the LE Coded PHY. |
| BT\_CONN\_LE\_OPT\_NO\_1M | Disable LE 1M PHY.  Disable scanning on the LE 1M PHY.  Note  Requires [BT\_CONN\_LE\_OPT\_CODED](#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b). |

## [◆ ](#ga9c54d2e44903cf7c4e5c97e223069dbc)anonymous enum

| anonymous enum |
| --- |

`#include <[conn.h](conn_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_CONN\_ROLE\_CENTRAL |  |
| BT\_CONN\_ROLE\_PERIPHERAL |  |

## [◆ ](#ga08eb37185a763212e65c47ab4c886eca)anonymous enum

| anonymous enum |
| --- |

`#include <[conn.h](conn_8h.md)>`

Connection PHY options.

| Enumerator | |
| --- | --- |
| BT\_CONN\_LE\_PHY\_OPT\_NONE | Convenience value when no options are specified. |
| BT\_CONN\_LE\_PHY\_OPT\_CODED\_S2 | LE Coded using S=2 coding preferred when transmitting. |
| BT\_CONN\_LE\_PHY\_OPT\_CODED\_S8 | LE Coded using S=8 coding preferred when transmitting. |

## [◆ ](#ga57465d3a61214531ddaffc2c30939043)bt\_conn\_auth\_keypress

| enum [bt\_conn\_auth\_keypress](#ga57465d3a61214531ddaffc2c30939043) |
| --- |

`#include <[conn.h](conn_8h.md)>`

Passkey Keypress Notification type.

The numeric values are the same as in the Core specification for Pairing Keypress Notification PDU.

| Enumerator | |
| --- | --- |
| BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_STARTED |  |
| BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ENTERED |  |
| BT\_CONN\_AUTH\_KEYPRESS\_DIGIT\_ERASED |  |
| BT\_CONN\_AUTH\_KEYPRESS\_CLEARED |  |
| BT\_CONN\_AUTH\_KEYPRESS\_ENTRY\_COMPLETED |  |

## [◆ ](#ga737d8118f8aba8985292d92d0604b190)bt\_conn\_le\_tx\_power\_phy

| enum [bt\_conn\_le\_tx\_power\_phy](#ga737d8118f8aba8985292d92d0604b190) |
| --- |

`#include <[conn.h](conn_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_CONN\_LE\_TX\_POWER\_PHY\_NONE | Convenience macro for when no PHY is set. |
| BT\_CONN\_LE\_TX\_POWER\_PHY\_1M | LE 1M PHY. |
| BT\_CONN\_LE\_TX\_POWER\_PHY\_2M | LE 2M PHY. |
| BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S8 | LE Coded PHY using S=8 coding. |
| BT\_CONN\_LE\_TX\_POWER\_PHY\_CODED\_S2 | LE Coded PHY using S=2 coding. |

## [◆ ](#ga9442c1479db60e2db40a2ea6de565282)bt\_conn\_state

| enum [bt\_conn\_state](#ga9442c1479db60e2db40a2ea6de565282) |
| --- |

`#include <[conn.h](conn_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_CONN\_STATE\_DISCONNECTED | Channel disconnected. |
| BT\_CONN\_STATE\_CONNECTING | Channel in connecting state. |
| BT\_CONN\_STATE\_CONNECTED | Channel connected and ready for upper layer traffic on it. |
| BT\_CONN\_STATE\_DISCONNECTING | Channel in disconnecting state. |

## [◆ ](#gab8dde20ae75b51f1e28dbeed06001f20)bt\_conn\_type

| enum [bt\_conn\_type](#gab8dde20ae75b51f1e28dbeed06001f20) |
| --- |

`#include <[conn.h](conn_8h.md)>`

Connection Type.

| Enumerator | |
| --- | --- |
| BT\_CONN\_TYPE\_LE | LE Connection Type. |
| BT\_CONN\_TYPE\_BR | BR/EDR Connection Type. |
| BT\_CONN\_TYPE\_SCO | SCO Connection Type. |
| BT\_CONN\_TYPE\_ISO | ISO Connection Type. |
| BT\_CONN\_TYPE\_ALL | All Connection Type. |

## [◆ ](#gaa9420ff489fd5857ff076406442679ff)bt\_security\_err

| enum [bt\_security\_err](#gaa9420ff489fd5857ff076406442679ff) |
| --- |

`#include <[conn.h](conn_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_SECURITY\_ERR\_SUCCESS | Security procedure successful. |
| BT\_SECURITY\_ERR\_AUTH\_FAIL | Authentication failed. |
| BT\_SECURITY\_ERR\_PIN\_OR\_KEY\_MISSING | PIN or encryption key is missing. |
| BT\_SECURITY\_ERR\_OOB\_NOT\_AVAILABLE | OOB data is not available. |
| BT\_SECURITY\_ERR\_AUTH\_REQUIREMENT | The requested security level could not be reached. |
| BT\_SECURITY\_ERR\_PAIR\_NOT\_SUPPORTED | Pairing is not supported. |
| BT\_SECURITY\_ERR\_PAIR\_NOT\_ALLOWED | Pairing is not allowed. |
| BT\_SECURITY\_ERR\_INVALID\_PARAM | Invalid parameters. |
| BT\_SECURITY\_ERR\_KEY\_REJECTED | Distributed Key Rejected. |
| BT\_SECURITY\_ERR\_UNSPECIFIED | Pairing failed but the exact reason could not be specified. |

## [◆ ](#ga2f8712bbf3410de5cbe6ce489fe30e5e)bt\_security\_flag

| enum [bt\_security\_flag](#ga2f8712bbf3410de5cbe6ce489fe30e5e) |
| --- |

`#include <[conn.h](conn_8h.md)>`

Security Info Flags.

| Enumerator | |
| --- | --- |
| BT\_SECURITY\_FLAG\_SC | Paired with Secure Connections. |
| BT\_SECURITY\_FLAG\_OOB | Paired with Out of Band method. |

## [◆ ](#gaf0c56cd26c4147f6c9f0faa11fa01783)bt\_security\_t

| enum [bt\_security\_t](#gaf0c56cd26c4147f6c9f0faa11fa01783) |
| --- |

`#include <[conn.h](conn_8h.md)>`

Security level.

| Enumerator | |
| --- | --- |
| BT\_SECURITY\_L0 | Level 0: Only for BR/EDR special cases, like SDP. |
| BT\_SECURITY\_L1 | Level 1: No encryption and no authentication. |
| BT\_SECURITY\_L2 | Level 2: Encryption and no authentication (no MITM). |
| BT\_SECURITY\_L3 | Level 3: Encryption and authentication (MITM). |
| BT\_SECURITY\_L4 | Level 4: Authenticated Secure Connections and 128-bit key. |
| BT\_SECURITY\_FORCE\_PAIR | Bit to force new pairing procedure, bit-wise OR with requested security level. |

## Function Documentation

## [◆ ](#ga89e5fc4bcab3f5598d20a9cd8ace5f59)bt\_conn\_auth\_cancel()

| int bt\_conn\_auth\_cancel | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Cancel ongoing authenticated pairing.

This function allows to cancel ongoing authenticated pairing.

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#ga81077385583d71c248a1eb6aab9ee86e)bt\_conn\_auth\_cb\_overlay()

| int bt\_conn\_auth\_cb\_overlay | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) \* | *cb* ) |

`#include <[conn.h](conn_8h.md)>`

Overlay authentication callbacks used for a given connection.

This function can be used only for Bluetooth LE connections. The `CONFIG_BT_SMP` must be enabled for this function.

The authentication callbacks for a given connection cannot be overlaid if security procedures in the SMP module have already started. This function can be called only once per connection.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | cb | Callback struct. |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#ga1bf13d2dfdbdf0a72f9b1c759ef23f60)bt\_conn\_auth\_cb\_register()

| int bt\_conn\_auth\_cb\_register | ( | const struct [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Register authentication callbacks.

Register callbacks to handle authenticated pairing. Passing NULL unregisters a previous callbacks structure.

Parameters
:   | cb | Callback struct. |
    | --- | --- |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#gac6684a8089ebd495b539d661cf9fd13f)bt\_conn\_auth\_info\_cb\_register()

| int bt\_conn\_auth\_info\_cb\_register | ( | struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Register authentication information callbacks.

Register callbacks to get authenticated pairing information. Multiple registrations can be done.

Parameters
:   | cb | Callback struct. |
    | --- | --- |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#gac73a60b8b6b569b84fe17f707fa33f37)bt\_conn\_auth\_info\_cb\_unregister()

| int bt\_conn\_auth\_info\_cb\_unregister | ( | struct [bt\_conn\_auth\_info\_cb](structbt__conn__auth__info__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Unregister authentication information callbacks.

Unregister callbacks to stop getting authenticated pairing information.

Parameters
:   | cb | Callback struct. |
    | --- | --- |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#ga2987a902da4f5cfe3671c60d154ced7e)bt\_conn\_auth\_keypress\_notify()

| int bt\_conn\_auth\_keypress\_notify | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_conn\_auth\_keypress](#ga57465d3a61214531ddaffc2c30939043) | *type* ) |

`#include <[conn.h](conn_8h.md)>`

Send Passkey Keypress Notification during pairing.

This function may be called only after passkey\_entry callback from [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md "Authenticated pairing callback structure.") structure was called.

Requires `CONFIG_BT_PASSKEY_KEYPRESS` .

Parameters
:   | conn | Destination for the notification. |
    | --- | --- |
    | type | What keypress event type to send. |

See also
:   [bt\_conn\_auth\_keypress](#ga57465d3a61214531ddaffc2c30939043).

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | Improper use of the API. |
    | -ENOMEM | Failed to allocate. |
    | -ENOBUFS | Failed to allocate. |

## [◆ ](#ga3e15b9deb6787d3e415bbea35c9aa91d)bt\_conn\_auth\_pairing\_confirm()

| int bt\_conn\_auth\_pairing\_confirm | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Reply if incoming pairing was confirmed by user.

This function should be called only after pairing\_confirm callback from [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md "Authenticated pairing callback structure.") structure was called if user confirmed incoming pairing.

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#gab8c3ecf2a3d68e54379917844a29d995)bt\_conn\_auth\_passkey\_confirm()

| int bt\_conn\_auth\_passkey\_confirm | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Reply if passkey was confirmed to match by user.

This function should be called only after passkey\_confirm callback from [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md "Authenticated pairing callback structure.") structure was called.

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#ga3906d8d3d192e8a6ad1bf6b7acc32ff0)bt\_conn\_auth\_passkey\_entry()

| int bt\_conn\_auth\_passkey\_entry | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *passkey* ) |

`#include <[conn.h](conn_8h.md)>`

Reply with entered passkey.

This function should be called only after passkey\_entry callback from [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md "Authenticated pairing callback structure.") structure was called.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | passkey | Entered passkey. |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#ga4002a1b092832807218afa8ad279ab98)bt\_conn\_auth\_pincode\_entry()

| int bt\_conn\_auth\_pincode\_entry | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const char \* | *pin* ) |

`#include <[conn.h](conn_8h.md)>`

Reply with entered PIN code.

This function should be called only after PIN code callback from [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md "Authenticated pairing callback structure.") structure was called. It's for legacy 2.0 devices.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | pin | Entered PIN code. |

Returns
:   Zero on success or negative error code otherwise

## [◆ ](#ga33b35e6457af183e059078aead4562b4)bt\_conn\_cb\_register()

| void bt\_conn\_cb\_register | ( | struct [bt\_conn\_cb](structbt__conn__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Register connection callbacks.

Register callbacks to monitor the state of connections.

Parameters
:   | cb | Callback struct. Must point to memory that remains valid. |
    | --- | --- |

## [◆ ](#gad2f90b34390e3c3697fd455ae4ef5f31)bt\_conn\_cb\_unregister()

| int bt\_conn\_cb\_unregister | ( | struct [bt\_conn\_cb](structbt__conn__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Unregister connection callbacks.

Unregister the state of connections callbacks.

Parameters
:   | cb | Callback struct point to memory that remains valid. |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | If `cb` is NULL |
    | -ENOENT | if `cb` was not registered |

## [◆ ](#ga62dc2663b4fa39a33adb76dc9a136aa4)bt\_conn\_create\_auto\_stop()

| int bt\_conn\_create\_auto\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Stop automatic connect creation.

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#gaf7849f332386f8903d35d6904f6c82b9)bt\_conn\_create\_br()

| struct bt\_conn \* bt\_conn\_create\_br | ( | const [bt\_addr\_t](structbt__addr__t.md) \* | *peer*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_br\_conn\_param](structbt__br__conn__param.md) \* | *param* ) |

`#include <[conn.h](conn_8h.md)>`

Initiate an BR/EDR connection to a remote device.

Allows initiate new BR/EDR link to remote peer using its address.

The caller gets a new reference to the connection object which must be released with [bt\_conn\_unref()](#ga4b18c6b22a9f02be0d7d078b2ce51ff6) once done using the object.

Parameters
:   | peer | Remote address. |
    | --- | --- |
    | param | Initial connection parameters. |

Returns
:   Valid connection object on success or NULL otherwise.

## [◆ ](#gac270287d6764dff1963f859a51a438e4)bt\_conn\_create\_sco()

| struct bt\_conn \* bt\_conn\_create\_sco | ( | const [bt\_addr\_t](structbt__addr__t.md) \* | *peer* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Initiate an SCO connection to a remote device.

Allows initiate new SCO link to remote peer using its address.

The caller gets a new reference to the connection object which must be released with [bt\_conn\_unref()](#ga4b18c6b22a9f02be0d7d078b2ce51ff6) once done using the object.

Parameters
:   | peer | Remote address. |
    | --- | --- |

Returns
:   Valid connection object on success or NULL otherwise.

## [◆ ](#ga14e7c852b0271781594e742ae509c5d3)bt\_conn\_disconnect()

| int bt\_conn\_disconnect | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reason* ) |

`#include <[conn.h](conn_8h.md)>`

Disconnect from a remote device or cancel pending connection.

Disconnect an active connection with the specified reason code or cancel pending outgoing connection.

The disconnect reason for a normal disconnect should be: [BT\_HCI\_ERR\_REMOTE\_USER\_TERM\_CONN](hci__types_8h.md#ac0e3b44027180d7a2dedb59395c4b111 "BT_HCI_ERR_REMOTE_USER_TERM_CONN").

The following disconnect reasons are accepted:

- [BT\_HCI\_ERR\_AUTH\_FAIL](hci__types_8h.md#a070d51dd0de3288f9811f90a558c889b "BT_HCI_ERR_AUTH_FAIL")
- [BT\_HCI\_ERR\_REMOTE\_USER\_TERM\_CONN](hci__types_8h.md#ac0e3b44027180d7a2dedb59395c4b111 "BT_HCI_ERR_REMOTE_USER_TERM_CONN")
- [BT\_HCI\_ERR\_REMOTE\_LOW\_RESOURCES](hci__types_8h.md#a5eeadfb220c24b2e7f5ce3fd21e5d46a "BT_HCI_ERR_REMOTE_LOW_RESOURCES")
- [BT\_HCI\_ERR\_REMOTE\_POWER\_OFF](hci__types_8h.md#a083f1fc52300f7e47c2f8d4e50551851 "BT_HCI_ERR_REMOTE_POWER_OFF")
- [BT\_HCI\_ERR\_UNSUPP\_REMOTE\_FEATURE](hci__types_8h.md#a516751f02bd497a020783f69bcf71453 "BT_HCI_ERR_UNSUPP_REMOTE_FEATURE")
- [BT\_HCI\_ERR\_PAIRING\_NOT\_SUPPORTED](hci__types_8h.md#a059c7d5619823eddf2c541b40a6464cb "BT_HCI_ERR_PAIRING_NOT_SUPPORTED")
- [BT\_HCI\_ERR\_UNACCEPT\_CONN\_PARAM](hci__types_8h.md#a712e214942c0d151597ce04e9d0df453 "BT_HCI_ERR_UNACCEPT_CONN_PARAM")

Parameters
:   | conn | Connection to disconnect. |
    | --- | --- |
    | reason | Reason code for the disconnection. |

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#gaff3e6aa16b68e5da7dab53289295545e)bt\_conn\_enc\_key\_size()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_enc\_key\_size | ( | const struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Get encryption key size.

This function gets encryption key size. If there is no security (encryption) enabled 0 will be returned.

Parameters
:   | conn | Existing connection object. |
    | --- | --- |

Returns
:   Encryption key size.

## [◆ ](#ga5bdf8e8efc85138d3631dc1efffc3916)bt\_conn\_foreach()

| void bt\_conn\_foreach | ( | enum [bt\_conn\_type](#gab8dde20ae75b51f1e28dbeed06001f20) | *type*, |
| --- | --- | --- | --- |
|  |  | void(\* | *func*)(struct bt\_conn \*conn, void \*data), |
|  |  | void \* | *data* ) |

`#include <[conn.h](conn_8h.md)>`

Iterate through all bt\_conn objects.

Iterates trough all bt\_conn objects that are alive in the Host allocator.

To find established connections, combine this with [bt\_conn\_get\_info](#ga2de54f2ac83f0d8dca2a85a9fbfadcaa). Check that [bt\_conn\_info::state](structbt__conn__info.md#ae566e2382b69ff27314dc1dd632dbdbc "bt_conn_info::state") is [BT\_CONN\_STATE\_CONNECTED](#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f).

Thread safety: This API is thread safe, but it does not guarantee a sequentially-consistent view for objects allocated during the current invocation of this API. E.g. If preempted while allocations A then B then C happen then results may include A and C but miss B.

Parameters
:   | type | Connection Type |
    | --- | --- |
    | func | Function to call for each connection. |
    | data | Data to pass to the callback function. |

## [◆ ](#ga77108581b8f61485ca840e4bf7a17087)bt\_conn\_get\_dst()

| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* bt\_conn\_get\_dst | ( | const struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Get destination (peer) address of a connection.

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   Destination address.

## [◆ ](#ga2de54f2ac83f0d8dca2a85a9fbfadcaa)bt\_conn\_get\_info()

| int bt\_conn\_get\_info | ( | const struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_conn\_info](structbt__conn__info.md) \* | *info* ) |

`#include <[conn.h](conn_8h.md)>`

Get connection info.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | info | Connection info object. |

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#ga6ea4478db6d95bd6a0d316399db36d92)bt\_conn\_get\_remote\_info()

| int bt\_conn\_get\_remote\_info | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_conn\_remote\_info](structbt__conn__remote__info.md) \* | *remote\_info* ) |

`#include <[conn.h](conn_8h.md)>`

Get connection info for the remote device.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | remote\_info | Connection remote info object. |

Note
:   In order to retrieve the remote version (version, manufacturer and subversion) `CONFIG_BT_REMOTE_VERSION` must be enabled
:   The remote information is exchanged directly after the connection has been established. The application can be notified about when the remote information is available through the remote\_info\_available callback.

Returns
:   Zero on success or (negative) error code on failure.
:   -EBUSY The remote information is not yet available.

## [◆ ](#ga4b43ef0f30146808e560991a302e88ad)bt\_conn\_get\_security()

| [bt\_security\_t](#gaf0c56cd26c4147f6c9f0faa11fa01783) bt\_conn\_get\_security | ( | const struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Get security level for a connection.

Returns
:   Connection security level

## [◆ ](#gad4aed76b80cc815f748ad0e84ae3d87c)bt\_conn\_index()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_index | ( | const struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Get array index of a connection.

This function is used to map bt\_conn to index of an array of connections. The array has CONFIG\_BT\_MAX\_CONN elements.

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   Index of the connection object. The range of the returned value is 0..CONFIG\_BT\_MAX\_CONN-1

## [◆ ](#ga8d66f3e0262a51279e9fa8b3139252e6)bt\_conn\_le\_create()

| int bt\_conn\_le\_create | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *peer*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) \* | *create\_param*, |
|  |  | const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \* | *conn\_param*, |
|  |  | struct bt\_conn \*\* | *conn* ) |

`#include <[conn.h](conn_8h.md)>`

Initiate an LE connection to a remote device.

Allows initiate new LE link to remote peer using its address.

The caller gets a new reference to the connection object which must be released with [bt\_conn\_unref()](#ga4b18c6b22a9f02be0d7d078b2ce51ff6) once done using the object.

This uses the General Connection Establishment procedure.

The application must disable explicit scanning before initiating a new LE connection.

Parameters
:   | [in] | peer | Remote address. |
    | --- | --- | --- |
    | [in] | create\_param | Create connection parameters. |
    | [in] | conn\_param | Initial connection parameters. |
    | [out] | conn | Valid connection object on success. |

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#gaecfaf2cb44772511dbb585de8f76f09b)bt\_conn\_le\_create\_auto()

| int bt\_conn\_le\_create\_auto | ( | const struct [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md) \* | *create\_param*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \* | *conn\_param* ) |

`#include <[conn.h](conn_8h.md)>`

Automatically connect to remote devices in the filter accept list.

This uses the Auto Connection Establishment procedure. The procedure will continue until a single connection is established or the procedure is stopped through [bt\_conn\_create\_auto\_stop](#ga62dc2663b4fa39a33adb76dc9a136aa4). To establish connections to all devices in the the filter accept list the procedure should be started again in the connected callback after a new connection has been established.

Parameters
:   | create\_param | Create connection parameters |
    | --- | --- |
    | conn\_param | Initial connection parameters. |

Returns
:   Zero on success or (negative) error code on failure.
:   -ENOMEM No free connection object available.

## [◆ ](#ga98f99c893e444d1ad1ecd9139803c0b1)bt\_conn\_le\_create\_synced()

| int bt\_conn\_le\_create\_synced | ( | const struct bt\_le\_ext\_adv \* | *adv*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_conn\_le\_create\_synced\_param](structbt__conn__le__create__synced__param.md) \* | *synced\_param*, |
|  |  | const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \* | *conn\_param*, |
|  |  | struct bt\_conn \*\* | *conn* ) |

`#include <[conn.h](conn_8h.md)>`

Create a connection to a synced device.

Initiate a connection to a synced device from a Periodic Advertising with Responses (PAwR) train.

The caller gets a new reference to the connection object which must be released with [bt\_conn\_unref()](#ga4b18c6b22a9f02be0d7d078b2ce51ff6) once done using the object.

This uses the Periodic Advertising Connection Procedure.

Parameters
:   | [in] | adv | The adverting set the PAwR advertiser belongs to. |
    | --- | --- | --- |
    | [in] | synced\_param | Create connection parameters. |
    | [in] | conn\_param | Initial connection parameters. |
    | [out] | conn | Valid connection object on success. |

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#ga8a2006f6e34b20c7e8ef65a73f431a57)bt\_conn\_le\_data\_len\_update()

| int bt\_conn\_le\_data\_len\_update | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_conn\_le\_data\_len\_param](structbt__conn__le__data__len__param.md) \* | *param* ) |

`#include <[conn.h](conn_8h.md)>`

Update the connection transmit data length parameters.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | param | Updated data length parameters. |

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#gaa79eada87d698f4998af876d03d7e92b)bt\_conn\_le\_enhanced\_get\_tx\_power\_level()

| int bt\_conn\_le\_enhanced\_get\_tx\_power\_level | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) \* | *tx\_power* ) |

`#include <[conn.h](conn_8h.md)>`

Get local enhanced connection transmit power level.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | tx\_power | Transmit power level descriptor. |

Returns
:   Zero on success or (negative) error code on failure.

Return values
:   | -ENOBUFS | HCI command buffer is not available. |
    | --- | --- |

## [◆ ](#ga0843a2e0b6f16ebd132a3a512cfd27a4)bt\_conn\_le\_get\_remote\_tx\_power\_level()

| int bt\_conn\_le\_get\_remote\_tx\_power\_level | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_conn\_le\_tx\_power\_phy](#ga737d8118f8aba8985292d92d0604b190) | *phy* ) |

`#include <[conn.h](conn_8h.md)>`

Get remote (peer) transmit power level.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | phy | PHY information. |

Returns
:   Zero on success or (negative) error code on failure.

Return values
:   | -ENOBUFS | HCI command buffer is not available. |
    | --- | --- |

## [◆ ](#gaa5289154bc508444f68df7abcef18aca)bt\_conn\_le\_get\_tx\_power\_level()

| int bt\_conn\_le\_get\_tx\_power\_level | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_conn\_le\_tx\_power](structbt__conn__le__tx__power.md) \* | *tx\_power\_level* ) |

`#include <[conn.h](conn_8h.md)>`

Get connection transmit power level.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | tx\_power\_level | Transmit power level descriptor. |

Returns
:   Zero on success or (negative) error code on failure.
:   -ENOBUFS HCI command buffer is not available.

## [◆ ](#gab44a964725f54ed2d37de17c6e2fd3eb)bt\_conn\_le\_param\_update()

| int bt\_conn\_le\_param\_update | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \* | *param* ) |

`#include <[conn.h](conn_8h.md)>`

Update the connection parameters.

If the local device is in the peripheral role then updating the connection parameters will be delayed. This delay can be configured by through the `CONFIG_BT_CONN_PARAM_UPDATE_TIMEOUT` option.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | param | Updated connection parameters. |

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#gae13ed81b1e7928f44b8fdf85995b3e58)bt\_conn\_le\_phy\_update()

| int bt\_conn\_le\_phy\_update | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_conn\_le\_phy\_param](structbt__conn__le__phy__param.md) \* | *param* ) |

`#include <[conn.h](conn_8h.md)>`

Update the connection PHY parameters.

Update the preferred transmit and receive PHYs of the connection. Use [BT\_GAP\_LE\_PHY\_NONE](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20baaf7e1b40f6464a603e5116db269cacab "BT_GAP_LE_PHY_NONE") to indicate no preference.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | param | Updated connection parameters. |

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#gaa1f38911acee0534a8a6e414018c6fb6)bt\_conn\_le\_set\_tx\_power\_report\_enable()

| int bt\_conn\_le\_set\_tx\_power\_report\_enable | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *local\_enable*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *remote\_enable* ) |

`#include <[conn.h](conn_8h.md)>`

Enable transmit power reporting.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | local\_enable | Enable/disable reporting for local. |
    | remote\_enable | Enable/disable reporting for remote. |

Returns
:   Zero on success or (negative) error code on failure.

Return values
:   | -ENOBUFS | HCI command buffer is not available. |
    | --- | --- |

## [◆ ](#ga1bfe349efd8a7de31e9457fe439d746a)bt\_conn\_lookup\_addr\_le()

| struct bt\_conn \* bt\_conn\_lookup\_addr\_le | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, |
| --- | --- | --- | --- |
|  |  | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *peer* ) |

`#include <[conn.h](conn_8h.md)>`

Look up an existing connection by address.

Look up an existing connection based on the remote address.

The caller gets a new reference to the connection object which must be released with [bt\_conn\_unref()](#ga4b18c6b22a9f02be0d7d078b2ce51ff6) once done using the object.

Parameters
:   | id | Local identity (in most cases BT\_ID\_DEFAULT). |
    | --- | --- |
    | peer | Remote address. |

Returns
:   Connection object or NULL if not found.

## [◆ ](#ga060d51eb2208de6f805b1fc0672d2d0c)bt\_conn\_ref()

| struct bt\_conn \* bt\_conn\_ref | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Increment a connection's reference count.

Increment the reference count of a connection object.

Note
:   Will return NULL if the reference count is zero.

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   Connection object with incremented reference count, or NULL if the reference count is zero.

## [◆ ](#ga4165819d12dd96e00dfa2fd6f4b95669)bt\_conn\_set\_bondable()

| int bt\_conn\_set\_bondable | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[conn.h](conn_8h.md)>`

Set/clear the bonding flag for a given connection.

Set/clear the Bonding flag in the Authentication Requirements of SMP Pairing Request/Response data for a given connection.

The bonding flag for a given connection cannot be set/cleared if security procedures in the SMP module have already started. This function can be called only once per connection.

If the bonding flag is not set/cleared for a given connection, the value will depend on global configuration which is set using bt\_set\_bondable. The default value of the global configuration is defined using CONFIG\_BT\_BONDABLE Kconfig option.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | enable | Value allowing/disallowing to be bondable. |

## [◆ ](#gae001f1268e1ff42c3c974c95dcb6735d)bt\_conn\_set\_security()

| int bt\_conn\_set\_security | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [bt\_security\_t](#gaf0c56cd26c4147f6c9f0faa11fa01783) | *sec* ) |

`#include <[conn.h](conn_8h.md)>`

Set security level for a connection.

This function enable security (encryption) for a connection. If the device has bond information for the peer with sufficiently strong key encryption will be enabled. If the connection is already encrypted with sufficiently strong key this function does nothing.

If the device has no bond information for the peer and is not already paired then the pairing procedure will be initiated. Note that `sec` has no effect on the security level selected for the pairing process. The selection is instead controlled by the values of the registered [bt\_conn\_auth\_cb](structbt__conn__auth__cb.md "bt_conn_auth_cb"). If the device has bond information or is already paired and the keys are too weak then the pairing procedure will be initiated.

This function may return an error if the required level of security defined using `sec` is not possible to achieve due to local or remote device limitation (e.g., input output capabilities), or if the maximum number of paired devices has been reached.

This function may return an error if the pairing procedure has already been initiated by the local device or the peer device.

Note
:   When `CONFIG_BT_SMP_SC_ONLY` is enabled then the security level will always be level 4.
:   When `CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY` is enabled then the security level will always be level 3.
:   When [BT\_SECURITY\_FORCE\_PAIR](#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae) within `sec` is enabled then the pairing procedure will always be initiated.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | sec | Requested minimum security level. |

Returns
:   0 on success or negative error

## [◆ ](#ga4b18c6b22a9f02be0d7d078b2ce51ff6)bt\_conn\_unref()

| void bt\_conn\_unref | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Decrement a connection's reference count.

Decrement the reference count of a connection object.

Parameters
:   | conn | Connection object. |
    | --- | --- |

## [◆ ](#ga096552403b5bcd0107f69eded772b1ee)bt\_le\_oob\_get\_sc\_data()

| int bt\_le\_oob\_get\_sc\_data | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*\* | *oobd\_local*, |
|  |  | const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \*\* | *oobd\_remote* ) |

`#include <[conn.h](conn_8h.md)>`

Get OOB data used for LE Secure Connections (SC) pairing procedure.

This function allows to get OOB data during the LE SC pairing procedure that were set by the [bt\_le\_oob\_set\_sc\_data()](#gac365f9748ad0737f09142ee1de982503) API.

Note
:   The OOB data will only be available as long as the connection object associated with it is valid.

Parameters
:   | conn | Connection object |
    | --- | --- |
    | oobd\_local | Local OOB data or NULL if not set |
    | oobd\_remote | Remote OOB data or NULL if not set |

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

## [◆ ](#ga978770d46d7c8af854a61261c14cb892)bt\_le\_oob\_set\_legacy\_flag()

| void bt\_le\_oob\_set\_legacy\_flag | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Allow/disallow remote legacy OOB data to be used for pairing.

Set/clear the OOB data flag for legacy SMP Pairing Request/Response data.

Parameters
:   | enable | Value allowing/disallowing remote legacy OOB data. |
    | --- | --- |

## [◆ ](#ga0f889983cfabafe826b4feb6899b95ba)bt\_le\_oob\_set\_legacy\_tk()

| int bt\_le\_oob\_set\_legacy\_tk | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *tk* ) |

`#include <[conn.h](conn_8h.md)>`

Set OOB Temporary Key to be used for pairing.

This function allows to set OOB data for the LE legacy pairing procedure. The function should only be called in response to the oob\_data\_request() callback provided that the legacy method is user pairing.

Parameters
:   | conn | Connection object |
    | --- | --- |
    | tk | Pointer to 16 byte long TK array |

Returns
:   Zero on success or -EINVAL if NULL

## [◆ ](#gac365f9748ad0737f09142ee1de982503)bt\_le\_oob\_set\_sc\_data()

| int bt\_le\_oob\_set\_sc\_data | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \* | *oobd\_local*, |
|  |  | const struct [bt\_le\_oob\_sc\_data](structbt__le__oob__sc__data.md) \* | *oobd\_remote* ) |

`#include <[conn.h](conn_8h.md)>`

Set OOB data during LE Secure Connections (SC) pairing procedure.

This function allows to set OOB data during the LE SC pairing procedure. The function should only be called in response to the oob\_data\_request() callback provided that LE SC method is used for pairing.

The user should submit OOB data according to the information received in the callback. This may yield three different configurations: with only local OOB data present, with only remote OOB data present or with both local and remote OOB data present.

Parameters
:   | conn | Connection object |
    | --- | --- |
    | oobd\_local | Local OOB data or NULL if not present |
    | oobd\_remote | Remote OOB data or NULL if not present |

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error.

## [◆ ](#gad02f8fe587efd543c0c81cace3f63d63)bt\_le\_oob\_set\_sc\_flag()

| void bt\_le\_oob\_set\_sc\_flag | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Allow/disallow remote LE SC OOB data to be used for pairing.

Set/clear the OOB data flag for LE SC SMP Pairing Request/Response data.

Parameters
:   | enable | Value allowing/disallowing remote LE SC OOB data. |
    | --- | --- |

## [◆ ](#ga8eea2211705d0691acc6ee4e0c37a47a)bt\_le\_set\_auto\_conn()

| int bt\_le\_set\_auto\_conn | ( | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *addr*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_le\_conn\_param](structbt__le__conn__param.md) \* | *param* ) |

`#include <[conn.h](conn_8h.md)>`

Automatically connect to remote device if it's in range.

This function enables/disables automatic connection initiation. Every time the device loses the connection with peer, this connection will be re-established if connectable advertisement from peer is received.

Note
:   Auto connect is disabled during explicit scanning.

Parameters
:   | addr | Remote Bluetooth address. |
    | --- | --- |
    | param | If non-NULL, auto connect is enabled with the given parameters. If NULL, auto connect is disabled. |

Returns
:   Zero on success or error code otherwise.

## [◆ ](#ga32c7598c086f209f9e1dee2aacbb40a1)bt\_passkey\_set()

| int bt\_passkey\_set | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *passkey* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Set a fixed passkey to be used for pairing.

This API is only available when the CONFIG\_BT\_FIXED\_PASSKEY configuration option has been enabled.

Sets a fixed passkey to be used for pairing. If set, the pairing\_confirm() callback will be called for all incoming pairings.

Parameters
:   | passkey | A valid passkey (0 - 999999) or BT\_PASSKEY\_INVALID to disable a previously set fixed passkey. |
    | --- | --- |

Returns
:   0 on success or a negative error code on failure.

## [◆ ](#ga014db594b17a3b5d7d954e64ad8de759)bt\_set\_bondable()

| void bt\_set\_bondable | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn.h](conn_8h.md)>`

Enable/disable bonding.

Set/clear the Bonding flag in the Authentication Requirements of SMP Pairing Request/Response data. The initial value of this flag depends on BT\_BONDABLE Kconfig setting. For the vast majority of applications calling this function shouldn't be needed.

Parameters
:   | enable | Value allowing/disallowing to be bondable. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
