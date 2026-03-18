---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__bap.html
original_path: doxygen/html/group__bt__bap.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Basic Audio Profile

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Bluetooth Basic Audio Profile (BAP).
[More...](#details)

| Topics | |
| --- | --- |
|  | [BAP Broadcast APIs](group__bt__bap__broadcast.md) |
|  | BAP Broadcast APIs. |
|  | [BAP Broadcast Sink APIs](group__bt__bap__broadcast__sink.md) |
|  | BAP Broadcast Sink APIs. |
|  | [BAP Broadcast Source APIs](group__bt__bap__broadcast__source.md) |
|  | BAP Broadcast Source APIs. |
|  | [BAP Unicast Client APIs](group__bt__bap__unicast__client.md) |
|  | [BAP Unicast Server APIs](group__bt__bap__unicast__server.md) |

| Data Structures | |
| --- | --- |
| struct | [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) |
|  | Structure storing values of fields of ASE Control Point notification. [More...](structbt__bap__ascs__rsp.md#details) |
| struct | [bt\_bap\_bass\_subgroup](structbt__bap__bass__subgroup.md) |
|  | Struct to hold subgroup specific information for the receive state. [More...](structbt__bap__bass__subgroup.md#details) |
| struct | [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) |
|  | Represents the Broadcast Audio Scan Service receive state. [More...](structbt__bap__scan__delegator__recv__state.md#details) |
| struct | [bt\_bap\_scan\_delegator\_cb](structbt__bap__scan__delegator__cb.md) |
|  | Struct to hold the Basic Audio Profile Scan Delegator callbacks. [More...](structbt__bap__scan__delegator__cb.md#details) |
| struct | [bt\_bap\_ep\_info](structbt__bap__ep__info.md) |
|  | Structure holding information of audio stream endpoint. [More...](structbt__bap__ep__info.md#details) |
| struct | [bt\_bap\_stream](structbt__bap__stream.md) |
|  | Basic Audio Profile stream structure. [More...](structbt__bap__stream.md#details) |
| struct | [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) |
|  | Stream operation. [More...](structbt__bap__stream__ops.md#details) |
| struct | [bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md) |
|  | Parameters for [bt\_bap\_scan\_delegator\_add\_src()](#ga6eb2a782d761da12d112356cfe723ff0). [More...](structbt__bap__scan__delegator__add__src__param.md#details) |
| struct | [bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md) |
|  | Parameters for [bt\_bap\_scan\_delegator\_mod\_src()](#gac022f38269742f16ff6887840ef5ba9a). [More...](structbt__bap__scan__delegator__mod__src__param.md#details) |
| struct | [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) |
|  | Struct to hold the Basic Audio Profile Broadcast Assistant callbacks. [More...](structbt__bap__broadcast__assistant__cb.md#details) |
| struct | [bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md) |
|  | Parameters for adding a source to a Broadcast Audio Scan Service server. [More...](structbt__bap__broadcast__assistant__add__src__param.md#details) |
| struct | [bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md) |
|  | Parameters for modifying a source. [More...](structbt__bap__broadcast__assistant__mod__src__param.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_BAP\_PA\_INTERVAL\_UNKNOWN](#ga357079ef00ce6f250e72a37103926c64)   0xFFFF |
|  | Value indicating that the periodic advertising interval is unknown. |
| #define | [BT\_BAP\_BIS\_SYNC\_NO\_PREF](#ga799f1417272e9b545c1e30ed4616b988)   0xFFFFFFFF |
|  | Broadcast Assistant no BIS sync preference. |
| #define | [BT\_BAP\_ASCS\_RSP](#ga8e5cd46a1428a315119e47c9cbbb9bfd)(c, [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Macro used to initialise the object storing values of ASE Control Point notification. |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_bap\_scan\_delegator\_state\_func\_t](#gaf236a87ae461ad48ec59f487780b4824)) (const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state, void \*user\_data) |
|  | Callback function for Scan Delegator receive state search functions. |
| typedef void(\* | [bt\_bap\_broadcast\_assistant\_write\_cb](#ga496c8a2f599d997a7e6e033bda5f0c36)) (struct bt\_conn \*conn, int err) |
|  | Callback function for writes. |

| Enumerations | |
| --- | --- |
| enum | [bt\_bap\_pa\_state](#gac551e9b0d53fd50f3a9e9c08447f0296) {     [BT\_BAP\_PA\_STATE\_NOT\_SYNCED](#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf) = 0x00 , [BT\_BAP\_PA\_STATE\_INFO\_REQ](#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb) = 0x01 , [BT\_BAP\_PA\_STATE\_SYNCED](#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc) = 0x02 , [BT\_BAP\_PA\_STATE\_FAILED](#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647) = 0x03 ,     [BT\_BAP\_PA\_STATE\_NO\_PAST](#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d) = 0x04   } |
|  | Periodic advertising state reported by the Scan Delegator. [More...](#gac551e9b0d53fd50f3a9e9c08447f0296) |
| enum | [bt\_bap\_big\_enc\_state](#ga5e0b0f70d247e131fa542fae16826a22) { [BT\_BAP\_BIG\_ENC\_STATE\_NO\_ENC](#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4) = 0x00 , [BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ](#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2) = 0x01 , [BT\_BAP\_BIG\_ENC\_STATE\_DEC](#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10) = 0x02 , [BT\_BAP\_BIG\_ENC\_STATE\_BAD\_CODE](#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b) = 0x03 } |
|  | Broadcast Isochronous Group encryption state reported by the Scan Delegator. [More...](#ga5e0b0f70d247e131fa542fae16826a22) |
| enum | [bt\_bap\_bass\_att\_err](#ga13e9b6d571a613d689b8ba58bae64ae3) { [BT\_BAP\_BASS\_ERR\_OPCODE\_NOT\_SUPPORTED](#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c) = 0x80 , [BT\_BAP\_BASS\_ERR\_INVALID\_SRC\_ID](#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202) = 0x81 } |
|  | Broadcast Audio Scan Service (BASS) specific ATT error codes. [More...](#ga13e9b6d571a613d689b8ba58bae64ae3) |
| enum | [bt\_bap\_ep\_state](#gaf210a91e1ff11d9bf7792ba47d1e1b4a) {     [BT\_BAP\_EP\_STATE\_IDLE](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961) = 0x00 , [BT\_BAP\_EP\_STATE\_CODEC\_CONFIGURED](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688) = 0x01 , [BT\_BAP\_EP\_STATE\_QOS\_CONFIGURED](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523) = 0x02 , [BT\_BAP\_EP\_STATE\_ENABLING](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332) = 0x03 ,     [BT\_BAP\_EP\_STATE\_STREAMING](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710) = 0x04 , [BT\_BAP\_EP\_STATE\_DISABLING](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8) = 0x05 , [BT\_BAP\_EP\_STATE\_RELEASING](#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c) = 0x06   } |
|  | Endpoint states. [More...](#gaf210a91e1ff11d9bf7792ba47d1e1b4a) |
| enum | [bt\_bap\_ascs\_rsp\_code](#ga9f7efa749c75edd32dc50503397ab9d1) {     [BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS](#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd) = 0x00 , [BT\_BAP\_ASCS\_RSP\_CODE\_NOT\_SUPPORTED](#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d) = 0x01 , [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_LENGTH](#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9) = 0x02 , [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE](#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa) = 0x03 ,     [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE\_STATE](#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5) = 0x04 , [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_DIR](#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146) = 0x05 , [BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED](#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a) = 0x06 , [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62) = 0x07 ,     [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21) = 0x08 , [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID](#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219) = 0x09 , [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED](#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7) = 0x0a , [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED](#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06) = 0x0b ,     [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_INVALID](#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06) = 0x0c , [BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM](#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb) = 0x0d , [BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED](#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a) = 0x0e   } |
|  | Response Status Code. [More...](#ga9f7efa749c75edd32dc50503397ab9d1) |
| enum | [bt\_bap\_ascs\_reason](#ga9ca1630544a336b15af8a8e8934c5a45) {     [BT\_BAP\_ASCS\_REASON\_NONE](#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd) = 0x00 , [BT\_BAP\_ASCS\_REASON\_CODEC](#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea) = 0x01 , [BT\_BAP\_ASCS\_REASON\_CODEC\_DATA](#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0) = 0x02 , [BT\_BAP\_ASCS\_REASON\_INTERVAL](#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c) = 0x03 ,     [BT\_BAP\_ASCS\_REASON\_FRAMING](#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539) = 0x04 , [BT\_BAP\_ASCS\_REASON\_PHY](#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8) = 0x05 , [BT\_BAP\_ASCS\_REASON\_SDU](#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b) = 0x06 , [BT\_BAP\_ASCS\_REASON\_RTN](#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf) = 0x07 ,     [BT\_BAP\_ASCS\_REASON\_LATENCY](#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942) = 0x08 , [BT\_BAP\_ASCS\_REASON\_PD](#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557) = 0x09 , [BT\_BAP\_ASCS\_REASON\_CIS](#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c) = 0x0a   } |
|  | Response Reasons. [More...](#ga9ca1630544a336b15af8a8e8934c5a45) |

| Functions | |
| --- | --- |
| int | [bt\_bap\_ep\_get\_info](#gaf15e5ec5bca364f6a3e7a43b1f27da68) (const struct bt\_bap\_ep \*ep, struct [bt\_bap\_ep\_info](structbt__bap__ep__info.md) \*info) |
|  | Return structure holding information of audio stream endpoint. |
| void | [bt\_bap\_stream\_cb\_register](#gab29c1e134156dceaa6c67abae9239378) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*ops) |
|  | Register Audio callbacks for a stream. |
| int | [bt\_bap\_stream\_config](#ga1e19aa4746132a2231037e82778bc402) (struct bt\_conn \*conn, struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct bt\_bap\_ep \*ep, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Configure Audio Stream. |
| int | [bt\_bap\_stream\_reconfig](#gaac84ee7b3ab5578d258848754f752546) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Reconfigure Audio Stream. |
| int | [bt\_bap\_stream\_qos](#gac878ed89242cac9a8514e8e4f1da4d9d) (struct bt\_conn \*conn, struct bt\_bap\_unicast\_group \*group) |
|  | Configure Audio Stream QoS. |
| int | [bt\_bap\_stream\_enable](#ga13a859b31b0310ec22339ec7ed0754f8) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len) |
|  | Enable Audio Stream. |
| int | [bt\_bap\_stream\_metadata](#ga0afe6c927729697e2f984cefcbc7c0f1) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len) |
|  | Change Audio Stream Metadata. |
| int | [bt\_bap\_stream\_disable](#ga0fd2bb35909fc19e3e9cff068ba9e9aa) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Disable Audio Stream. |
| int | [bt\_bap\_stream\_connect](#gaa75f2cd2c36fdaef04a62c95bec6e2e3) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Connect unicast audio stream. |
| int | [bt\_bap\_stream\_start](#ga8f2dc67c35299334d21c7dee7b8664ae) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Start Audio Stream. |
| int | [bt\_bap\_stream\_stop](#gada72bcd3951eff2bc6b70c02dcaed98b) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Stop Audio Stream. |
| int | [bt\_bap\_stream\_release](#gaaf94f1f0dda7ef356c0f9ae79b5c60e4) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Release Audio Stream. |
| int | [bt\_bap\_stream\_send](#ga63b69967aa92224a2bd9cf79eb41773e) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num) |
|  | Send data to Audio stream without timestamp. |
| int | [bt\_bap\_stream\_send\_ts](#gaa0e012446238c916abc84d6c0de89bf3) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts) |
|  | Send data to Audio stream with timestamp. |
| int | [bt\_bap\_stream\_get\_tx\_sync](#ga47eb6219d730d75ddc4f49dceac7e928) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info) |
|  | Get ISO transmission timing info for a Basic Audio Profile stream. |
| void | [bt\_bap\_scan\_delegator\_register\_cb](#ga5841f00a46c8b32bc8253d70dc05f104) (struct [bt\_bap\_scan\_delegator\_cb](structbt__bap__scan__delegator__cb.md) \*cb) |
|  | Register the callbacks for the Basic Audio Profile Scan Delegator. |
| int | [bt\_bap\_scan\_delegator\_set\_pa\_state](#ga381c1f3b386ecbdfd570eb125882161e) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id, enum [bt\_bap\_pa\_state](#gac551e9b0d53fd50f3a9e9c08447f0296) pa\_state) |
|  | Set the periodic advertising sync state to syncing. |
| int | [bt\_bap\_scan\_delegator\_set\_bis\_sync\_state](#ga7cce7e53264294abec4421364afffdbe) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bis\_synced[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]) |
|  | Set the sync state of a receive state in the server. |
| int | [bt\_bap\_scan\_delegator\_add\_src](#ga6eb2a782d761da12d112356cfe723ff0) (const struct [bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md) \*param) |
|  | Add a receive state source locally. |
| int | [bt\_bap\_scan\_delegator\_mod\_src](#gac022f38269742f16ff6887840ef5ba9a) (const struct [bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md) \*param) |
|  | Add a receive state source locally. |
| int | [bt\_bap\_scan\_delegator\_rem\_src](#ga6c240f1cdb33945197700e4fe106ef2c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id) |
|  | Remove a receive state source. |
| void | [bt\_bap\_scan\_delegator\_foreach\_state](#gab6f1a12699a9437c6575c70df33d5be0) ([bt\_bap\_scan\_delegator\_state\_func\_t](#gaf236a87ae461ad48ec59f487780b4824) func, void \*user\_data) |
|  | Iterate through all existing receive states. |
| const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \* | [bt\_bap\_scan\_delegator\_find\_state](#gabec9fd0a2966e1811fd4770855050510) ([bt\_bap\_scan\_delegator\_state\_func\_t](#gaf236a87ae461ad48ec59f487780b4824) func, void \*user\_data) |
|  | Find and return a receive state based on a compare function. |
| int | [bt\_bap\_broadcast\_assistant\_discover](#gab59c5ebc4fef28da34d8a54b1244c33b) (struct bt\_conn \*conn) |
|  | Discover Broadcast Audio Scan Service on the server. |
| int | [bt\_bap\_broadcast\_assistant\_scan\_start](#ga98ac067e66d263aa41fc6f8df6bb9126) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) start\_scan) |
|  | Scan start for BISes for a remote server. |
| int | [bt\_bap\_broadcast\_assistant\_scan\_stop](#ga76cae35df980b78a10551811050b2760) (struct bt\_conn \*conn) |
|  | Stop remote scanning for BISes for a server. |
| int | [bt\_bap\_broadcast\_assistant\_register\_cb](#gabab24c44e9833029965475ad7b149e6e) (struct [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) \*cb) |
|  | Registers the callbacks used by Broadcast Audio Scan Service client. |
| int | [bt\_bap\_broadcast\_assistant\_unregister\_cb](#ga679cdeb6e555bfc9ce20f38e493000ee) (struct [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) \*cb) |
|  | Unregisters the callbacks used by the Broadcast Audio Scan Service client. |
| int | [bt\_bap\_broadcast\_assistant\_add\_src](#gac93cb4cab33d0b937e752bc0b71cad9e) (struct bt\_conn \*conn, const struct [bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md) \*param) |
|  | Add a source on the server. |
| int | [bt\_bap\_broadcast\_assistant\_mod\_src](#gaa9c292a7dcb470926d8d7d4be699a0c7) (struct bt\_conn \*conn, const struct [bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md) \*param) |
|  | Modify a source on the server. |
| int | [bt\_bap\_broadcast\_assistant\_set\_broadcast\_code](#ga0105535992cf66e55ab2587648fb571f) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) broadcast\_code[16]) |
|  | Set a broadcast code to the specified receive state. |
| int | [bt\_bap\_broadcast\_assistant\_rem\_src](#ga09785690db551677a043fcaa2fdb7f29) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id) |
|  | Remove a source from the server. |
| int | [bt\_bap\_broadcast\_assistant\_read\_recv\_state](#ga94fce2b4346b1026d53e0b860ca7fbf2) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx) |
|  | Read the specified receive state from the server. |

## Detailed Description

Bluetooth Basic Audio Profile (BAP).

Since
:   3.0

Version
:   0.8.0

The Basic Audio Profile (BAP) allows for both unicast and broadcast Audio Stream control.

## Macro Definition Documentation

## [◆ ](#ga8e5cd46a1428a315119e47c9cbbb9bfd)BT\_BAP\_ASCS\_RSP

| #define BT\_BAP\_ASCS\_RSP | ( |  | *c*, |
| --- | --- | --- | --- |
|  |  |  | *[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)* ) |

`#include <[bap.h](bap_8h.md)>`

**Value:**

(struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md)) { .code = c, .reason = [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) }

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md)

Structure storing values of fields of ASE Control Point notification.

**Definition** bap.h:192

Macro used to initialise the object storing values of ASE Control Point notification.

Parameters
:   | c | Response Code field |
    | --- | --- |
    | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | Reason field - [bt\_bap\_ascs\_reason](#ga9ca1630544a336b15af8a8e8934c5a45) or [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354 "bt_audio_metadata_type") (see notes in [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md "bt_bap_ascs_rsp")). |

## [◆ ](#ga799f1417272e9b545c1e30ed4616b988)BT\_BAP\_BIS\_SYNC\_NO\_PREF

| #define BT\_BAP\_BIS\_SYNC\_NO\_PREF   0xFFFFFFFF |
| --- |

`#include <[bap.h](bap_8h.md)>`

Broadcast Assistant no BIS sync preference.

Value indicating that the Broadcast Assistant has no preference to which BIS the Scan Delegator syncs to

## [◆ ](#ga357079ef00ce6f250e72a37103926c64)BT\_BAP\_PA\_INTERVAL\_UNKNOWN

| #define BT\_BAP\_PA\_INTERVAL\_UNKNOWN   0xFFFF |
| --- |

`#include <[bap.h](bap_8h.md)>`

Value indicating that the periodic advertising interval is unknown.

## Typedef Documentation

## [◆ ](#ga496c8a2f599d997a7e6e033bda5f0c36)bt\_bap\_broadcast\_assistant\_write\_cb

| typedef void(\* bt\_bap\_broadcast\_assistant\_write\_cb) (struct bt\_conn \*conn, int err) |
| --- |

`#include <[bap.h](bap_8h.md)>`

Callback function for writes.

Parameters
:   | conn | The connection to the peer device. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on fail. |

## [◆ ](#gaf236a87ae461ad48ec59f487780b4824)bt\_bap\_scan\_delegator\_state\_func\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_bap\_scan\_delegator\_state\_func\_t) (const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state, void \*user\_data) |
| --- |

`#include <[bap.h](bap_8h.md)>`

Callback function for Scan Delegator receive state search functions.

Parameters
:   | recv\_state | The receive state. |
    | --- | --- |
    | user\_data | User data. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | to stop iterating. If this is used in the context of [bt\_bap\_scan\_delegator\_find\_state()](#gabec9fd0a2966e1811fd4770855050510), the recv\_state will be returned by [bt\_bap\_scan\_delegator\_find\_state()](#gabec9fd0a2966e1811fd4770855050510) |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | to continue iterating |

## Enumeration Type Documentation

## [◆ ](#ga9ca1630544a336b15af8a8e8934c5a45)bt\_bap\_ascs\_reason

| enum [bt\_bap\_ascs\_reason](#ga9ca1630544a336b15af8a8e8934c5a45) |
| --- |

`#include <[bap.h](bap_8h.md)>`

Response Reasons.

These are used if the [bt\_bap\_ascs\_rsp\_code](#ga9f7efa749c75edd32dc50503397ab9d1) value is [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62), [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21) or [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID](#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219).

| Enumerator | |
| --- | --- |
| BT\_BAP\_ASCS\_REASON\_NONE | No reason. |
| BT\_BAP\_ASCS\_REASON\_CODEC | Codec ID. |
| BT\_BAP\_ASCS\_REASON\_CODEC\_DATA | Codec configuration. |
| BT\_BAP\_ASCS\_REASON\_INTERVAL | SDU interval. |
| BT\_BAP\_ASCS\_REASON\_FRAMING | Framing. |
| BT\_BAP\_ASCS\_REASON\_PHY | PHY. |
| BT\_BAP\_ASCS\_REASON\_SDU | Maximum SDU size. |
| BT\_BAP\_ASCS\_REASON\_RTN | RTN. |
| BT\_BAP\_ASCS\_REASON\_LATENCY | Max transport latency. |
| BT\_BAP\_ASCS\_REASON\_PD | Presendation delay. |
| BT\_BAP\_ASCS\_REASON\_CIS | Invalid CIS mapping. |

## [◆ ](#ga9f7efa749c75edd32dc50503397ab9d1)bt\_bap\_ascs\_rsp\_code

| enum [bt\_bap\_ascs\_rsp\_code](#ga9f7efa749c75edd32dc50503397ab9d1) |
| --- |

`#include <[bap.h](bap_8h.md)>`

Response Status Code.

These are sent by the server to the client when a stream operation is requested.

| Enumerator | |
| --- | --- |
| BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS | Server completed operation successfully. |
| BT\_BAP\_ASCS\_RSP\_CODE\_NOT\_SUPPORTED | Server did not support operation by client. |
| BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_LENGTH | Server rejected due to invalid operation length. |
| BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE | Invalid ASE ID. |
| BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE\_STATE | Invalid ASE state. |
| BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_DIR | Invalid operation for direction. |
| BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED | Capabilities not supported by server. |
| BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED | Configuration parameters not supported by server. |
| BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED | Configuration parameters rejected by server. |
| BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID | Invalid Configuration parameters. |
| BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED | Unsupported metadata. |
| BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED | Metadata rejected by server. |
| BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_INVALID | Invalid metadata. |
| BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM | Server has insufficient resources. |
| BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED | Unspecified error. |

## [◆ ](#ga13e9b6d571a613d689b8ba58bae64ae3)bt\_bap\_bass\_att\_err

| enum [bt\_bap\_bass\_att\_err](#ga13e9b6d571a613d689b8ba58bae64ae3) |
| --- |

`#include <[bap.h](bap_8h.md)>`

Broadcast Audio Scan Service (BASS) specific ATT error codes.

| Enumerator | |
| --- | --- |
| BT\_BAP\_BASS\_ERR\_OPCODE\_NOT\_SUPPORTED | Opcode not supported. |
| BT\_BAP\_BASS\_ERR\_INVALID\_SRC\_ID | Invalid source ID supplied. |

## [◆ ](#ga5e0b0f70d247e131fa542fae16826a22)bt\_bap\_big\_enc\_state

| enum [bt\_bap\_big\_enc\_state](#ga5e0b0f70d247e131fa542fae16826a22) |
| --- |

`#include <[bap.h](bap_8h.md)>`

Broadcast Isochronous Group encryption state reported by the Scan Delegator.

| Enumerator | |
| --- | --- |
| BT\_BAP\_BIG\_ENC\_STATE\_NO\_ENC | The Broadcast Isochronous Group not encrypted. |
| BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ | The Broadcast Isochronous Group broadcast code requested. |
| BT\_BAP\_BIG\_ENC\_STATE\_DEC | The Broadcast Isochronous Group decrypted. |
| BT\_BAP\_BIG\_ENC\_STATE\_BAD\_CODE | The Broadcast Isochronous Group bad broadcast code. |

## [◆ ](#gaf210a91e1ff11d9bf7792ba47d1e1b4a)bt\_bap\_ep\_state

| enum [bt\_bap\_ep\_state](#gaf210a91e1ff11d9bf7792ba47d1e1b4a) |
| --- |

`#include <[bap.h](bap_8h.md)>`

Endpoint states.

| Enumerator | |
| --- | --- |
| BT\_BAP\_EP\_STATE\_IDLE | Audio Stream Endpoint Idle state. |
| BT\_BAP\_EP\_STATE\_CODEC\_CONFIGURED | Audio Stream Endpoint Codec Configured state. |
| BT\_BAP\_EP\_STATE\_QOS\_CONFIGURED | Audio Stream Endpoint QoS Configured state. |
| BT\_BAP\_EP\_STATE\_ENABLING | Audio Stream Endpoint Enabling state. |
| BT\_BAP\_EP\_STATE\_STREAMING | Audio Stream Endpoint Streaming state. |
| BT\_BAP\_EP\_STATE\_DISABLING | Audio Stream Endpoint Disabling state. |
| BT\_BAP\_EP\_STATE\_RELEASING | Audio Stream Endpoint Streaming state. |

## [◆ ](#gac551e9b0d53fd50f3a9e9c08447f0296)bt\_bap\_pa\_state

| enum [bt\_bap\_pa\_state](#gac551e9b0d53fd50f3a9e9c08447f0296) |
| --- |

`#include <[bap.h](bap_8h.md)>`

Periodic advertising state reported by the Scan Delegator.

| Enumerator | |
| --- | --- |
| BT\_BAP\_PA\_STATE\_NOT\_SYNCED | The periodic advertising has not been synchronized. |
| BT\_BAP\_PA\_STATE\_INFO\_REQ | Waiting for SyncInfo from Broadcast Assistant. |
| BT\_BAP\_PA\_STATE\_SYNCED | Synchronized to periodic advertising. |
| BT\_BAP\_PA\_STATE\_FAILED | Failed to synchronized to periodic advertising. |
| BT\_BAP\_PA\_STATE\_NO\_PAST | No periodic advertising sync transfer receiver from Broadcast Assistant. |

## Function Documentation

## [◆ ](#gac93cb4cab33d0b937e752bc0b71cad9e)bt\_bap\_broadcast\_assistant\_add\_src()

| int bt\_bap\_broadcast\_assistant\_add\_src | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md) \* | *param* ) |

`#include <[bap.h](bap_8h.md)>`

Add a source on the server.

Parameters
:   | conn | Connection to the server. |
    | --- | --- |
    | param | Parameter struct. |

Returns
:   Error value. 0 on success, GATT error or ERRNO on fail.

## [◆ ](#gab59c5ebc4fef28da34d8a54b1244c33b)bt\_bap\_broadcast\_assistant\_discover()

| int bt\_bap\_broadcast\_assistant\_discover | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Discover Broadcast Audio Scan Service on the server.

Warning: Only one connection can be active at any time; discovering for a new connection, will delete all previous data.

Parameters
:   | conn | The connection |
    | --- | --- |

Returns
:   int Error value. 0 on success, GATT error or ERRNO on fail.

## [◆ ](#gaa9c292a7dcb470926d8d7d4be699a0c7)bt\_bap\_broadcast\_assistant\_mod\_src()

| int bt\_bap\_broadcast\_assistant\_mod\_src | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md) \* | *param* ) |

`#include <[bap.h](bap_8h.md)>`

Modify a source on the server.

Parameters
:   | conn | Connection to the server. |
    | --- | --- |
    | param | Parameter struct. |

Returns
:   Error value. 0 on success, GATT error or ERRNO on fail.

## [◆ ](#ga94fce2b4346b1026d53e0b860ca7fbf2)bt\_bap\_broadcast\_assistant\_read\_recv\_state()

| int bt\_bap\_broadcast\_assistant\_read\_recv\_state | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *idx* ) |

`#include <[bap.h](bap_8h.md)>`

Read the specified receive state from the server.

Parameters
:   | conn | Connection to the server. |
    | --- | --- |
    | idx | The index of the receive start (0 up to the value from bt\_bap\_broadcast\_assistant\_discover\_cb) |

Returns
:   Error value. 0 on success, GATT error or ERRNO on fail.

## [◆ ](#gabab24c44e9833029965475ad7b149e6e)bt\_bap\_broadcast\_assistant\_register\_cb()

| int bt\_bap\_broadcast\_assistant\_register\_cb | ( | struct [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Registers the callbacks used by Broadcast Audio Scan Service client.

Parameters
:   | cb | The callback structure. |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | if `cb` is NULL |
    | -EALREADY | if `cb` was already registered |

## [◆ ](#ga09785690db551677a043fcaa2fdb7f29)bt\_bap\_broadcast\_assistant\_rem\_src()

| int bt\_bap\_broadcast\_assistant\_rem\_src | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src\_id* ) |

`#include <[bap.h](bap_8h.md)>`

Remove a source from the server.

Parameters
:   | conn | Connection to the server. |
    | --- | --- |
    | src\_id | Source ID of the receive state. |

Returns
:   Error value. 0 on success, GATT error or ERRNO on fail.

## [◆ ](#ga98ac067e66d263aa41fc6f8df6bb9126)bt\_bap\_broadcast\_assistant\_scan\_start()

| int bt\_bap\_broadcast\_assistant\_scan\_start | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *start\_scan* ) |

`#include <[bap.h](bap_8h.md)>`

Scan start for BISes for a remote server.

This will let the Broadcast Audio Scan Service server know that this device is actively scanning for broadcast sources. The function can optionally also start scanning, if the caller does not want to start scanning itself.

Scan results, if `start_scan` is true, is sent to the bt\_bap\_broadcast\_assistant\_scan\_cb callback.

Parameters
:   | conn | Connection to the Broadcast Audio Scan Service server. Used to let the server know that we are scanning. |
    | --- | --- |
    | start\_scan | Start scanning if true. If false, the application should enable scan itself. |

Returns
:   int Error value. 0 on success, GATT error or ERRNO on fail.

## [◆ ](#ga76cae35df980b78a10551811050b2760)bt\_bap\_broadcast\_assistant\_scan\_stop()

| int bt\_bap\_broadcast\_assistant\_scan\_stop | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Stop remote scanning for BISes for a server.

Parameters
:   | conn | Connection to the server. |
    | --- | --- |

Returns
:   int Error value. 0 on success, GATT error or ERRNO on fail.

## [◆ ](#ga0105535992cf66e55ab2587648fb571f)bt\_bap\_broadcast\_assistant\_set\_broadcast\_code()

| int bt\_bap\_broadcast\_assistant\_set\_broadcast\_code | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src\_id*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *broadcast\_code*[16] ) |

`#include <[bap.h](bap_8h.md)>`

Set a broadcast code to the specified receive state.

Parameters
:   | conn | Connection to the server. |
    | --- | --- |
    | src\_id | Source ID of the receive state. |
    | broadcast\_code | The broadcast code. |

Returns
:   Error value. 0 on success, GATT error or ERRNO on fail.

## [◆ ](#ga679cdeb6e555bfc9ce20f38e493000ee)bt\_bap\_broadcast\_assistant\_unregister\_cb()

| int bt\_bap\_broadcast\_assistant\_unregister\_cb | ( | struct [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Unregisters the callbacks used by the Broadcast Audio Scan Service client.

Parameters
:   | cb | The callback structure. |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | if `cb` is NULL |
    | -EALREADY | if `cb` was not registered |

## [◆ ](#gaf15e5ec5bca364f6a3e7a43b1f27da68)bt\_bap\_ep\_get\_info()

| int bt\_bap\_ep\_get\_info | ( | const struct bt\_bap\_ep \* | *ep*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_bap\_ep\_info](structbt__bap__ep__info.md) \* | *info* ) |

`#include <[bap.h](bap_8h.md)>`

Return structure holding information of audio stream endpoint.

Parameters
:   | ep | The audio stream endpoint object. |
    | --- | --- |
    | info | The structure object to be filled with the info. |

Return values
:   | 0 | in case of success |
    | --- | --- |
    | -EINVAL | if `ep` or `info` are NULL |

## [◆ ](#ga6eb2a782d761da12d112356cfe723ff0)bt\_bap\_scan\_delegator\_add\_src()

| int bt\_bap\_scan\_delegator\_add\_src | ( | const struct [bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Add a receive state source locally.

This will notify any connected clients about the new source. This allows them to modify and even remove it.

If `CONFIG_BT_BAP_BROADCAST_SINK` is enabled, any Broadcast Sink sources are autonomously added.

Parameters
:   | param | The parameters for adding the new source |
    | --- | --- |

Returns
:   int errno on failure, or source ID on success.

## [◆ ](#gabec9fd0a2966e1811fd4770855050510)bt\_bap\_scan\_delegator\_find\_state()

| const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \* bt\_bap\_scan\_delegator\_find\_state | ( | [bt\_bap\_scan\_delegator\_state\_func\_t](#gaf236a87ae461ad48ec59f487780b4824) | *func*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[bap.h](bap_8h.md)>`

Find and return a receive state based on a compare function.

Parameters
:   | func | The compare callback function |
    | --- | --- |
    | user\_data | User specified data that sent to the callback function |

Returns
:   The first receive state where the `func` returned true, or NULL

## [◆ ](#gab6f1a12699a9437c6575c70df33d5be0)bt\_bap\_scan\_delegator\_foreach\_state()

| void bt\_bap\_scan\_delegator\_foreach\_state | ( | [bt\_bap\_scan\_delegator\_state\_func\_t](#gaf236a87ae461ad48ec59f487780b4824) | *func*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[bap.h](bap_8h.md)>`

Iterate through all existing receive states.

Parameters
:   | func | The callback function |
    | --- | --- |
    | user\_data | User specified data that sent to the callback function |

## [◆ ](#gac022f38269742f16ff6887840ef5ba9a)bt\_bap\_scan\_delegator\_mod\_src()

| int bt\_bap\_scan\_delegator\_mod\_src | ( | const struct [bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Add a receive state source locally.

This will notify any connected clients about the new source. This allows them to modify and even remove it.

If `CONFIG_BT_BAP_BROADCAST_SINK` is enabled, any Broadcast Sink sources are autonomously modified.

Parameters
:   | param | The parameters for adding the new source |
    | --- | --- |

Returns
:   int errno on failure, or source ID on success.

## [◆ ](#ga5841f00a46c8b32bc8253d70dc05f104)bt\_bap\_scan\_delegator\_register\_cb()

| void bt\_bap\_scan\_delegator\_register\_cb | ( | struct [bt\_bap\_scan\_delegator\_cb](structbt__bap__scan__delegator__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Register the callbacks for the Basic Audio Profile Scan Delegator.

Only one set of callbacks can be registered at any one time, and calling this function multiple times will override any previously registered callbacks.

Parameters
:   | cb | Pointer to the callback struct |
    | --- | --- |

## [◆ ](#ga6c240f1cdb33945197700e4fe106ef2c)bt\_bap\_scan\_delegator\_rem\_src()

| int bt\_bap\_scan\_delegator\_rem\_src | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Remove a receive state source.

This will remove the receive state. If the receive state periodic advertising is synced, [bt\_bap\_scan\_delegator\_cb.pa\_sync\_term\_req()](structbt__bap__scan__delegator__cb.md#a5b918538cfe0edaa69155f891981eeae "Periodic advertising sync termination request.") will be called.

If `CONFIG_BT_BAP_BROADCAST_SINK` is enabled, any Broadcast Sink sources are autonomously removed.

Parameters
:   | src\_id | The source ID to remove |
    | --- | --- |

Returns
:   int Error value. 0 on success, errno on fail.

## [◆ ](#ga7cce7e53264294abec4421364afffdbe)bt\_bap\_scan\_delegator\_set\_bis\_sync\_state()

| int bt\_bap\_scan\_delegator\_set\_bis\_sync\_state | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src\_id*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *bis\_synced*[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS] ) |

`#include <[bap.h](bap_8h.md)>`

Set the sync state of a receive state in the server.

Parameters
:   | src\_id | The source id used to identify the receive state. |
    | --- | --- |
    | bis\_synced | Array of bitfields to set the BIS sync state for each subgroup. |

Returns
:   int Error value. 0 on success, ERRNO on fail.

## [◆ ](#ga381c1f3b386ecbdfd570eb125882161e)bt\_bap\_scan\_delegator\_set\_pa\_state()

| int bt\_bap\_scan\_delegator\_set\_pa\_state | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src\_id*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_bap\_pa\_state](#gac551e9b0d53fd50f3a9e9c08447f0296) | *pa\_state* ) |

`#include <[bap.h](bap_8h.md)>`

Set the periodic advertising sync state to syncing.

Set the periodic advertising sync state for a receive state to syncing, notifying Broadcast Assistants.

Parameters
:   | src\_id | The source id used to identify the receive state. |
    | --- | --- |
    | pa\_state | The Periodic Advertising sync state to set. BT\_BAP\_PA\_STATE\_NOT\_SYNCED and BT\_BAP\_PA\_STATE\_SYNCED is not necessary to provide, as they are handled internally. |

Returns
:   int Error value. 0 on success, errno on fail.

## [◆ ](#gab29c1e134156dceaa6c67abae9239378)bt\_bap\_stream\_cb\_register()

| void bt\_bap\_stream\_cb\_register | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \* | *ops* ) |

`#include <[bap.h](bap_8h.md)>`

Register Audio callbacks for a stream.

Register Audio callbacks for a stream.

Parameters
:   | stream | Stream object. |
    | --- | --- |
    | ops | Stream operations structure. |

## [◆ ](#ga1e19aa4746132a2231037e82778bc402)bt\_bap\_stream\_config()

| int bt\_bap\_stream\_config | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream*, |
|  |  | struct bt\_bap\_ep \* | *ep*, |
|  |  | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* ) |

`#include <[bap.h](bap_8h.md)>`

Configure Audio Stream.

This procedure is used by a client to configure a new stream using the remote endpoint, local capability and codec configuration.

Parameters
:   | conn | Connection object |
    | --- | --- |
    | stream | Stream object being configured |
    | ep | Remote Audio Endpoint being configured |
    | codec\_cfg | Codec configuration |

Returns
:   Allocated Audio Stream object or NULL in case of error.

## [◆ ](#gaa75f2cd2c36fdaef04a62c95bec6e2e3)bt\_bap\_stream\_connect()

| int bt\_bap\_stream\_connect | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Connect unicast audio stream.

This procedure is used by a unicast client to connect the connected isochronous stream (CIS) associated with the audio stream. If two audio streams share a CIS, then this only needs to be done once for those streams. This can only be done for streams in the QoS configured or enabled states.

The [bt\_bap\_stream\_ops.connected()](structbt__bap__stream__ops.md#a533d5ea96aa67b9b74b19c55afd43df1 "Isochronous channel connected callback.") callback will be called on the streams once this has finished.

This shall only be called for unicast streams, and only as the unicast client ( `CONFIG_BT_BAP_UNICAST_CLIENT` ).

Parameters
:   | stream | Stream object |
    | --- | --- |

Return values
:   | 0 | in case of success |
    | --- | --- |
    | -EINVAL | if the stream, endpoint, ISO channel or connection is NULL |
    | -EBADMSG | if the stream or ISO channel is in an invalid state for connection |
    | -EOPNOTSUPP | if the role of the stream is not [BT\_HCI\_ROLE\_CENTRAL](hci__types_8h.md#a150ea8f2095d8510bde3ebd65d521c29 "BT_HCI_ROLE_CENTRAL") |
    | -EALREADY | if the ISO channel is already connecting or connected |
    | -EBUSY | if another ISO channel is connecting |
    | -ENOEXEC | if otherwise rejected by the ISO layer |

## [◆ ](#ga0fd2bb35909fc19e3e9cff068ba9e9aa)bt\_bap\_stream\_disable()

| int bt\_bap\_stream\_disable | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Disable Audio Stream.

This procedure is used by a unicast client or unicast server to disable a stream.

This shall only be called for unicast streams, as broadcast streams will always be enabled once created.

Parameters
:   | stream | Stream object |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga13a859b31b0310ec22339ec7ed0754f8)bt\_bap\_stream\_enable()

| int bt\_bap\_stream\_enable | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *meta*[], |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *meta\_len* ) |

`#include <[bap.h](bap_8h.md)>`

Enable Audio Stream.

This procedure is used by a client to enable a stream.

This shall only be called for unicast streams, as broadcast streams will always be enabled once created.

Parameters
:   | stream | Stream object |
    | --- | --- |
    | meta | Metadata |
    | meta\_len | Metadata length |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga47eb6219d730d75ddc4f49dceac7e928)bt\_bap\_stream\_get\_tx\_sync()

| int bt\_bap\_stream\_get\_tx\_sync | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \* | *info* ) |

`#include <[bap.h](bap_8h.md)>`

Get ISO transmission timing info for a Basic Audio Profile stream.

Reads timing information for transmitted ISO packet on an ISO channel. The HCI\_LE\_Read\_ISO\_TX\_Sync HCI command is used to retrieve this information from the controller.

Note
:   An SDU must have already been successfully transmitted on the ISO channel for this function to return successfully. Support for sending must be supported, determined by `CONFIG_BT_AUDIO_TX` .

Parameters
:   | [in] | stream | Stream object. |
    | --- | --- | --- |
    | [out] | info | Transmit info object. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | if the stream is invalid, if the stream is not configured for sending or if it is not connected with a isochronous stream |
    | Any | return value from [bt\_iso\_chan\_get\_tx\_sync()](group__bt__iso.md#gaa3942147fdeebc36039cc35c4e984411 "Get ISO transmission timing info.") |

## [◆ ](#ga0afe6c927729697e2f984cefcbc7c0f1)bt\_bap\_stream\_metadata()

| int bt\_bap\_stream\_metadata | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *meta*[], |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *meta\_len* ) |

`#include <[bap.h](bap_8h.md)>`

Change Audio Stream Metadata.

This procedure is used by a unicast client or unicast server to change the metadata of a stream.

Parameters
:   | stream | Stream object |
    | --- | --- |
    | meta | Metadata |
    | meta\_len | Metadata length |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gac878ed89242cac9a8514e8e4f1da4d9d)bt\_bap\_stream\_qos()

| int bt\_bap\_stream\_qos | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct bt\_bap\_unicast\_group \* | *group* ) |

`#include <[bap.h](bap_8h.md)>`

Configure Audio Stream QoS.

This procedure is used by a client to configure the Quality of Service of streams in a unicast group. All streams in the group for the specified `conn` will have the Quality of Service configured. This shall only be used to configure unicast streams.

Parameters
:   | conn | Connection object |
    | --- | --- |
    | group | Unicast group object |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaac84ee7b3ab5578d258848754f752546)bt\_bap\_stream\_reconfig()

| int bt\_bap\_stream\_reconfig | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg* ) |

`#include <[bap.h](bap_8h.md)>`

Reconfigure Audio Stream.

This procedure is used by a unicast client or unicast server to reconfigure a stream to use a different local codec configuration.

This can only be done for unicast streams.

Parameters
:   | stream | Stream object being reconfigured |
    | --- | --- |
    | codec\_cfg | Codec configuration |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaaf94f1f0dda7ef356c0f9ae79b5c60e4)bt\_bap\_stream\_release()

| int bt\_bap\_stream\_release | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Release Audio Stream.

This procedure is used by a unicast client or unicast server to release a unicast stream.

Broadcast sink streams cannot be released, but can be deleted by [bt\_bap\_broadcast\_sink\_delete()](group__bt__bap__broadcast__sink.md#ga8b9d6cb409a3671654e053475ada3fda "Release a broadcast sink."). Broadcast source streams cannot be released, but can be deleted by [bt\_bap\_broadcast\_source\_delete()](group__bt__bap__broadcast__source.md#ga12e0a4856115a8eb297fe2d1fc130155 "Delete audio broadcast source.").

Parameters
:   | stream | Stream object |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga63b69967aa92224a2bd9cf79eb41773e)bt\_bap\_stream\_send()

| int bt\_bap\_stream\_send | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *seq\_num* ) |

`#include <[bap.h](bap_8h.md)>`

Send data to Audio stream without timestamp.

Send data from buffer to the stream.

Note
:   Support for sending must be supported, determined by `CONFIG_BT_AUDIO_TX` .

Parameters
:   | stream | Stream object. |
    | --- | --- |
    | buf | Buffer containing data to be sent. |
    | seq\_num | Packet Sequence number. This value shall be incremented for each call to this function and at least once per SDU interval for a specific channel. |

Returns
:   Bytes sent in case of success or negative value in case of error.

## [◆ ](#gaa0e012446238c916abc84d6c0de89bf3)bt\_bap\_stream\_send\_ts()

| int bt\_bap\_stream\_send\_ts | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *seq\_num*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *ts* ) |

`#include <[bap.h](bap_8h.md)>`

Send data to Audio stream with timestamp.

Send data from buffer to the stream.

Note
:   Support for sending must be supported, determined by `CONFIG_BT_AUDIO_TX` .

Parameters
:   | stream | Stream object. |
    | --- | --- |
    | buf | Buffer containing data to be sent. |
    | seq\_num | Packet Sequence number. This value shall be incremented for each call to this function and at least once per SDU interval for a specific channel. |
    | ts | Timestamp of the SDU in microseconds (us). This value can be used to transmit multiple SDUs in the same SDU interval in a CIG or BIG. |

Returns
:   Bytes sent in case of success or negative value in case of error.

## [◆ ](#ga8f2dc67c35299334d21c7dee7b8664ae)bt\_bap\_stream\_start()

| int bt\_bap\_stream\_start | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Start Audio Stream.

This procedure is used by a unicast client or unicast server to make a stream start streaming.

For the unicast client, this will send the receiver start ready command to the unicast server for [BT\_AUDIO\_DIR\_SOURCE](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c "BT_AUDIO_DIR_SOURCE") ASEs. The CIS is required to be connected first by [bt\_bap\_stream\_connect()](#gaa75f2cd2c36fdaef04a62c95bec6e2e3) before the command can be sent.

For the unicast server, this will execute the receiver start ready command on the unicast server for [BT\_AUDIO\_DIR\_SINK](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8 "BT_AUDIO_DIR_SINK") ASEs. If the CIS is not connected yet, the stream will go into the streaming state as soon as the CIS is connected.

This shall only be called for unicast streams.

Broadcast sinks will always be started once synchronized, and broadcast source streams shall be started with [bt\_bap\_broadcast\_source\_start()](group__bt__bap__broadcast__source.md#gac4640f5207599d51c1a63ff47f3c1d5a "Start audio broadcast source.").

Parameters
:   | stream | Stream object |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gada72bcd3951eff2bc6b70c02dcaed98b)bt\_bap\_stream\_stop()

| int bt\_bap\_stream\_stop | ( | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Stop Audio Stream.

This procedure is used by a client to make a stream stop streaming.

This shall only be called for unicast streams. Broadcast sinks cannot be stopped. Broadcast sources shall be stopped with [bt\_bap\_broadcast\_source\_stop()](group__bt__bap__broadcast__source.md#ga36a885581eec5cab8b3f652db19b9aba "Stop audio broadcast source.").

Parameters
:   | stream | Stream object |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
