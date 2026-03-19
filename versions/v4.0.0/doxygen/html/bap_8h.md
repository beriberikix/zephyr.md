---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/bap_8h.html
original_path: doxygen/html/bap_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bap.h File Reference

Header for Bluetooth BAP.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h_source.md)>`  
`#include <[zephyr/bluetooth/addr.h](addr_8h_source.md)>`  
`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/bluetooth/iso.h](iso_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](bap_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) |
|  | QoS configuration structure. [More...](structbt__bap__qos__cfg.md#details) |
| struct | [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) |
|  | Audio Stream Quality of Service Preference structure. [More...](structbt__bap__qos__cfg__pref.md#details) |
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
| struct | [bt\_bap\_unicast\_server\_register\_param](structbt__bap__unicast__server__register__param.md) |
|  | Structure for registering Unicast Server. [More...](structbt__bap__unicast__server__register__param.md#details) |
| struct | [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) |
|  | Unicast Server callback structure. [More...](structbt__bap__unicast__server__cb.md#details) |
| struct | [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md) |
|  | Parameter struct for each stream in the unicast group. [More...](structbt__bap__unicast__group__stream__param.md#details) |
| struct | [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) |
|  | Parameter struct for the unicast group functions. [More...](structbt__bap__unicast__group__stream__pair__param.md#details) |
| struct | [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) |
|  | Parameters for the creating unicast groups with [bt\_bap\_unicast\_group\_create()](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21 "Create unicast group."). [More...](structbt__bap__unicast__group__param.md#details) |
| struct | [bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md) |
|  | Unicast Client callback structure. [More...](structbt__bap__unicast__client__cb.md#details) |
| struct | [bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md) |
|  | Codec ID structure for a Broadcast Audio Source Endpoint (BASE). [More...](structbt__bap__base__codec__id.md#details) |
| struct | [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) |
|  | BIS structure for each BIS in a Broadcast Audio Source Endpoint (BASE) subgroup. [More...](structbt__bap__base__subgroup__bis.md#details) |
| struct | [bt\_bap\_broadcast\_source\_stream\_param](structbt__bap__broadcast__source__stream__param.md) |
|  | Broadcast Source stream parameters. [More...](structbt__bap__broadcast__source__stream__param.md#details) |
| struct | [bt\_bap\_broadcast\_source\_subgroup\_param](structbt__bap__broadcast__source__subgroup__param.md) |
|  | Broadcast Source subgroup parameters. [More...](structbt__bap__broadcast__source__subgroup__param.md#details) |
| struct | [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) |
|  | Broadcast Source create parameters. [More...](structbt__bap__broadcast__source__param.md#details) |
| struct | [bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md) |
|  | Broadcast Audio Sink callback structure. [More...](structbt__bap__broadcast__sink__cb.md#details) |
| struct | [bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md) |
|  | Parameters for [bt\_bap\_scan\_delegator\_add\_src()](group__bt__bap.md#ga6eb2a782d761da12d112356cfe723ff0 "Add a receive state source locally."). [More...](structbt__bap__scan__delegator__add__src__param.md#details) |
| struct | [bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md) |
|  | Parameters for [bt\_bap\_scan\_delegator\_mod\_src()](group__bt__bap.md#gac022f38269742f16ff6887840ef5ba9a "Add a receive state source locally."). [More...](structbt__bap__scan__delegator__mod__src__param.md#details) |
| struct | [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) |
|  | Struct to hold the Basic Audio Profile Broadcast Assistant callbacks. [More...](structbt__bap__broadcast__assistant__cb.md#details) |
| struct | [bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md) |
|  | Parameters for adding a source to a Broadcast Audio Scan Service server. [More...](structbt__bap__broadcast__assistant__add__src__param.md#details) |
| struct | [bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md) |
|  | Parameters for modifying a source. [More...](structbt__bap__broadcast__assistant__mod__src__param.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_BAP\_INVALID\_BROADCAST\_ID](group__bt__bap.md#ga83cfb2a817e0db6d78c300dc5dea2d8a)   0xFFFFFFFFU |
|  | An invalid Broadcast ID. |
| #define | [BT\_BAP\_BASS\_VALID\_BIT\_BITFIELD](group__bt__bap.md#ga91adb24c76c0d14757c5eec0146caebb)(\_bis\_bitfield) |
|  | Check if a BAP BASS BIS\_Sync bitfield is valid. |
| #define | [BT\_BAP\_QOS\_CFG](group__bt__bap.md#ga7bd804c68e67d0b4bfe391d80d33a6c7)(\_interval, \_framing, \_phy, \_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare elements of [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md "QoS configuration structure."). |
| #define | [BT\_BAP\_QOS\_CFG\_UNFRAMED](group__bt__bap.md#gae578c78a10df4d1e4e6d1781ca48e1f5)(\_interval, \_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare Input Unframed [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md "QoS configuration structure."). |
| #define | [BT\_BAP\_QOS\_CFG\_FRAMED](group__bt__bap.md#gaa91c55ca2de3ddf09620948fd4914b14)(\_interval, \_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare Input Framed [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md "QoS configuration structure."). |
| #define | [BT\_BAP\_QOS\_CFG\_PREF](group__bt__bap.md#ga7a3fc7cb21be45276cf50846c076101d)(\_unframed\_supported, \_phy, \_rtn, \_latency, \_pd\_min, \_pd\_max, \_pref\_pd\_min, \_pref\_pd\_max) |
|  | Helper to declare elements of [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md "bt_bap_qos_cfg_pref"). |
| #define | [BT\_BAP\_PA\_INTERVAL\_UNKNOWN](group__bt__bap.md#ga357079ef00ce6f250e72a37103926c64)   0xFFFF |
|  | Value indicating that the periodic advertising interval is unknown. |
| #define | [BT\_BAP\_BIS\_SYNC\_NO\_PREF](group__bt__bap.md#ga799f1417272e9b545c1e30ed4616b988)   0xFFFFFFFF |
|  | Broadcast Assistant no BIS sync preference. |
| #define | [BT\_BAP\_BIS\_SYNC\_FAILED](group__bt__bap.md#ga2a2e4a06f6e39360458fe2e4d0b66833)   0xFFFFFFFF |
|  | BIS sync value indicating that the BIG sync has failed for any reason. |
| #define | [BT\_BAP\_ASCS\_RSP](group__bt__bap.md#ga8e5cd46a1428a315119e47c9cbbb9bfd)(c, [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Macro used to initialise the object storing values of ASE Control Point notification. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_bap\_ep\_func\_t](group__bt__bap__unicast__server.md#gab571883c431267fc9a9f892de3c864f1)) (struct bt\_bap\_ep \*ep, void \*user\_data) |
|  | The callback function called for each endpoint. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_bap\_scan\_delegator\_state\_func\_t](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824)) (const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \*recv\_state, void \*user\_data) |
|  | Callback function for Scan Delegator receive state search functions. |
| typedef void(\* | [bt\_bap\_broadcast\_assistant\_write\_cb](group__bt__bap.md#ga496c8a2f599d997a7e6e033bda5f0c36)) (struct bt\_conn \*conn, int err) |
|  | Callback function for writes. |

| Enumerations | |
| --- | --- |
| enum | [bt\_bap\_qos\_cfg\_framing](group__bt__bap.md#ga37a5f9d7198739eef8bde6764da30de9) { [BT\_BAP\_QOS\_CFG\_FRAMING\_UNFRAMED](group__bt__bap.md#gga37a5f9d7198739eef8bde6764da30de9afe1ffd5db8e36f8082a2ef7545e04a94) = 0x00 , [BT\_BAP\_QOS\_CFG\_FRAMING\_FRAMED](group__bt__bap.md#gga37a5f9d7198739eef8bde6764da30de9a406ad3527d9d92e4e8b213fe52794298) = 0x01 } |
|  | QoS Framing. [More...](group__bt__bap.md#ga37a5f9d7198739eef8bde6764da30de9) |
| enum | { [BT\_BAP\_QOS\_CFG\_1M](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28) = BIT(0) , [BT\_BAP\_QOS\_CFG\_2M](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147) = BIT(1) , [BT\_BAP\_QOS\_CFG\_CODED](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73) = BIT(2) } |
|  | QoS Preferred PHY. [More...](group__bt__bap.md#ga5e8ebf4db88f94f44828bb6f41e81d44) |
| enum | [bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296) {     [BT\_BAP\_PA\_STATE\_NOT\_SYNCED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296a7b1fefef1bf427344367c56a706abadf) = 0x00 , [BT\_BAP\_PA\_STATE\_INFO\_REQ](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296acc9d79f4d27718862abebe50c734badb) = 0x01 , [BT\_BAP\_PA\_STATE\_SYNCED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aae1dc286b9c767730625900d7eea8cdc) = 0x02 , [BT\_BAP\_PA\_STATE\_FAILED](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aab516ef505a91f77e998154fd4068647) = 0x03 ,     [BT\_BAP\_PA\_STATE\_NO\_PAST](group__bt__bap.md#ggac551e9b0d53fd50f3a9e9c08447f0296aefea9fc8ccf288ca58eb0d000f9dc36d) = 0x04   } |
|  | Periodic advertising state reported by the Scan Delegator. [More...](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296) |
| enum | [bt\_bap\_big\_enc\_state](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) { [BT\_BAP\_BIG\_ENC\_STATE\_NO\_ENC](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab04f102f7a4b5f2c7c35475ce83859e4) = 0x00 , [BT\_BAP\_BIG\_ENC\_STATE\_BCODE\_REQ](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22a27fa0c62c91f8be8f4097a0e89d219d2) = 0x01 , [BT\_BAP\_BIG\_ENC\_STATE\_DEC](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ac641a3260e65459163c60687b198cb10) = 0x02 , [BT\_BAP\_BIG\_ENC\_STATE\_BAD\_CODE](group__bt__bap.md#gga5e0b0f70d247e131fa542fae16826a22ab5e7b18243a162522e6f95a2f0fa796b) = 0x03 } |
|  | Broadcast Isochronous Group encryption state reported by the Scan Delegator. [More...](group__bt__bap.md#ga5e0b0f70d247e131fa542fae16826a22) |
| enum | [bt\_bap\_bass\_att\_err](group__bt__bap.md#ga13e9b6d571a613d689b8ba58bae64ae3) { [BT\_BAP\_BASS\_ERR\_OPCODE\_NOT\_SUPPORTED](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1b201d26c590e98968d6db728401fd5c) = 0x80 , [BT\_BAP\_BASS\_ERR\_INVALID\_SRC\_ID](group__bt__bap.md#gga13e9b6d571a613d689b8ba58bae64ae3a1df885fd6ebbec48636452d87238a202) = 0x81 } |
|  | Broadcast Audio Scan Service (BASS) specific ATT error codes. [More...](group__bt__bap.md#ga13e9b6d571a613d689b8ba58bae64ae3) |
| enum | [bt\_bap\_ep\_state](group__bt__bap.md#gaf210a91e1ff11d9bf7792ba47d1e1b4a) {     [BT\_BAP\_EP\_STATE\_IDLE](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa3e03502c3e461df70bd404363f74c961) = 0x00 , [BT\_BAP\_EP\_STATE\_CODEC\_CONFIGURED](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa6585721b9bfbb744b0a27b5d7a6f5688) = 0x01 , [BT\_BAP\_EP\_STATE\_QOS\_CONFIGURED](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa76cd25c523b1fc0500db9fb40f303523) = 0x02 , [BT\_BAP\_EP\_STATE\_ENABLING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa187f373140139caa320d593061e7c332) = 0x03 ,     [BT\_BAP\_EP\_STATE\_STREAMING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aae15bf7ad5a2e44401d15ff62aee85710) = 0x04 , [BT\_BAP\_EP\_STATE\_DISABLING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa7b7a407f002502aced74e408c1278ae8) = 0x05 , [BT\_BAP\_EP\_STATE\_RELEASING](group__bt__bap.md#ggaf210a91e1ff11d9bf7792ba47d1e1b4aa70282dfd43920dc4758fb3251604863c) = 0x06   } |
|  | Endpoint states. [More...](group__bt__bap.md#gaf210a91e1ff11d9bf7792ba47d1e1b4a) |
| enum | [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) {     [BT\_BAP\_ASCS\_RSP\_CODE\_SUCCESS](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ae6e8ebcfc2578eefec11cb9e8222eafd) = 0x00 , [BT\_BAP\_ASCS\_RSP\_CODE\_NOT\_SUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a54515d30244888af19711f153b942d2d) = 0x01 , [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_LENGTH](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad43b45076cbb1ec36af8a4e5126d4bb9) = 0x02 , [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a635bf6ad106e80e4e64ce3153fd668aa) = 0x03 ,     [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_ASE\_STATE](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a11bc72f67d626889c24cd54f412730b5) = 0x04 , [BT\_BAP\_ASCS\_RSP\_CODE\_INVALID\_DIR](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a64417c64d67fa73fa8430b6f4255e146) = 0x05 , [BT\_BAP\_ASCS\_RSP\_CODE\_CAP\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a96278dcde41d37b6e9fd2a926c9ff16a) = 0x06 , [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a5a0230629bffc7659ec8127169a90b62) = 0x07 ,     [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1af587ec0a8b72fd9a7379aa173a8beb21) = 0x08 , [BT\_BAP\_ASCS\_RSP\_CODE\_CONF\_INVALID](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a7f2a361b595dad7bc0e7f354bf6a1219) = 0x09 , [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_UNSUPPORTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ad604f01d7a964fc8ae55dc76a5a8e0a7) = 0x0a , [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_REJECTED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9945d6001d365d759023fc233514ed06) = 0x0b ,     [BT\_BAP\_ASCS\_RSP\_CODE\_METADATA\_INVALID](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a3ef9532dbd19abc90a89305d67f82e06) = 0x0c , [BT\_BAP\_ASCS\_RSP\_CODE\_NO\_MEM](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1a9676a2e7fc5e417cbae2cea663204ccb) = 0x0d , [BT\_BAP\_ASCS\_RSP\_CODE\_UNSPECIFIED](group__bt__bap.md#gga9f7efa749c75edd32dc50503397ab9d1ac6c03bd8827040ce48905c58ea7d423a) = 0x0e   } |
|  | Response Status Code. [More...](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) |
| enum | [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) {     [BT\_BAP\_ASCS\_REASON\_NONE](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1d4794f987bab3c784955ac10e1cdcdd) = 0x00 , [BT\_BAP\_ASCS\_REASON\_CODEC](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8923f9c27858f27fd3799367cf525aea) = 0x01 , [BT\_BAP\_ASCS\_REASON\_CODEC\_DATA](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a69c9d998626ccb2a6963dd2dfd68cbb0) = 0x02 , [BT\_BAP\_ASCS\_REASON\_INTERVAL](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45ae297b097cc8fbb5f161c0d8c44c6623c) = 0x03 ,     [BT\_BAP\_ASCS\_REASON\_FRAMING](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a458cd637ba37015e2598990f9f248539) = 0x04 , [BT\_BAP\_ASCS\_REASON\_PHY](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a8eda92a6782649f2a42f0021095a54a8) = 0x05 , [BT\_BAP\_ASCS\_REASON\_SDU](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a731ac5962c8a8685c3f40884c1b67d0b) = 0x06 , [BT\_BAP\_ASCS\_REASON\_RTN](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45acc839aadf0d60ce8eb086271397b94cf) = 0x07 ,     [BT\_BAP\_ASCS\_REASON\_LATENCY](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a904156d246f97189820c9de93fb90942) = 0x08 , [BT\_BAP\_ASCS\_REASON\_PD](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a1fdcf3a40ed30b7aa63e1df573a2d557) = 0x09 , [BT\_BAP\_ASCS\_REASON\_CIS](group__bt__bap.md#gga9ca1630544a336b15af8a8e8934c5a45a93bc6ab73f6088bceea03c6f8e71854c) = 0x0a   } |
|  | Response Reasons. [More...](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) |

| Functions | |
| --- | --- |
| int | [bt\_bap\_ep\_get\_info](group__bt__bap.md#gaf15e5ec5bca364f6a3e7a43b1f27da68) (const struct bt\_bap\_ep \*ep, struct [bt\_bap\_ep\_info](structbt__bap__ep__info.md) \*info) |
|  | Return structure holding information of audio stream endpoint. |
| void | [bt\_bap\_stream\_cb\_register](group__bt__bap.md#gab29c1e134156dceaa6c67abae9239378) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*ops) |
|  | Register Audio callbacks for a stream. |
| int | [bt\_bap\_stream\_config](group__bt__bap.md#ga1e19aa4746132a2231037e82778bc402) (struct bt\_conn \*conn, struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct bt\_bap\_ep \*ep, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Configure Audio Stream. |
| int | [bt\_bap\_stream\_reconfig](group__bt__bap.md#gaac84ee7b3ab5578d258848754f752546) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Reconfigure Audio Stream. |
| int | [bt\_bap\_stream\_qos](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d) (struct bt\_conn \*conn, struct bt\_bap\_unicast\_group \*[group](structgroup.md)) |
|  | Configure Audio Stream QoS. |
| int | [bt\_bap\_stream\_enable](group__bt__bap.md#ga13a859b31b0310ec22339ec7ed0754f8) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len) |
|  | Enable Audio Stream. |
| int | [bt\_bap\_stream\_metadata](group__bt__bap.md#ga0afe6c927729697e2f984cefcbc7c0f1) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len) |
|  | Change Audio Stream Metadata. |
| int | [bt\_bap\_stream\_disable](group__bt__bap.md#ga0fd2bb35909fc19e3e9cff068ba9e9aa) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Disable Audio Stream. |
| int | [bt\_bap\_stream\_connect](group__bt__bap.md#gaa75f2cd2c36fdaef04a62c95bec6e2e3) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Connect unicast audio stream. |
| int | [bt\_bap\_stream\_start](group__bt__bap.md#ga8f2dc67c35299334d21c7dee7b8664ae) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Start Audio Stream. |
| int | [bt\_bap\_stream\_stop](group__bt__bap.md#gada72bcd3951eff2bc6b70c02dcaed98b) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Stop Audio Stream. |
| int | [bt\_bap\_stream\_release](group__bt__bap.md#gaaf94f1f0dda7ef356c0f9ae79b5c60e4) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream) |
|  | Release Audio Stream. |
| int | [bt\_bap\_stream\_send](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num) |
|  | Send data to Audio stream without timestamp. |
| int | [bt\_bap\_stream\_send\_ts](group__bt__bap.md#gaa0e012446238c916abc84d6c0de89bf3) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts) |
|  | Send data to Audio stream with timestamp. |
| int | [bt\_bap\_stream\_get\_tx\_sync](group__bt__bap.md#ga47eb6219d730d75ddc4f49dceac7e928) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info) |
|  | Get ISO transmission timing info for a Basic Audio Profile stream. |
| int | [bt\_bap\_unicast\_server\_register](group__bt__bap__unicast__server.md#gab3ea6014854e6290f058c87e866c3191) (const struct [bt\_bap\_unicast\_server\_register\_param](structbt__bap__unicast__server__register__param.md) \*param) |
|  | Register the Unicast Server. |
| int | [bt\_bap\_unicast\_server\_unregister](group__bt__bap__unicast__server.md#ga6ef3b9e877ffdc04cc48fda6713a0209) (void) |
|  | Unregister the Unicast Server. |
| int | [bt\_bap\_unicast\_server\_register\_cb](group__bt__bap__unicast__server.md#ga7669133936bc13f7ab38817db9ce69c0) (const struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) \*cb) |
|  | Register unicast server callbacks. |
| int | [bt\_bap\_unicast\_server\_unregister\_cb](group__bt__bap__unicast__server.md#gadf984f12bdeadcfc814dc2fc770cb7bf) (const struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) \*cb) |
|  | Unregister unicast server callbacks. |
| void | [bt\_bap\_unicast\_server\_foreach\_ep](group__bt__bap__unicast__server.md#ga4614a504d47cf732b09d4f22302d3239) (struct bt\_conn \*conn, [bt\_bap\_ep\_func\_t](group__bt__bap__unicast__server.md#gab571883c431267fc9a9f892de3c864f1) func, void \*user\_data) |
|  | Iterate through all endpoints of the given connection. |
| int | [bt\_bap\_unicast\_server\_config\_ase](group__bt__bap__unicast__server.md#ga6e71c34a21091f222d3478f4fad95319) (struct bt\_conn \*conn, struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*qos\_pref) |
|  | Initialize and configure a new ASE. |
| int | [bt\_bap\_unicast\_group\_create](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21) (struct [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) \*param, struct bt\_bap\_unicast\_group \*\*unicast\_group) |
|  | Create unicast group. |
| int | [bt\_bap\_unicast\_group\_reconfig](group__bt__bap__unicast__client.md#gacd684504c8127ff4f8d038cc06718e5e) (struct bt\_bap\_unicast\_group \*unicast\_group, const struct [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) \*param) |
|  | Reconfigure unicast group. |
| int | [bt\_bap\_unicast\_group\_add\_streams](group__bt__bap__unicast__client.md#ga9cc792cd1eaaa79d56f3df0e2341cbf6) (struct bt\_bap\_unicast\_group \*unicast\_group, struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) params[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_param) |
|  | Add streams to a unicast group as a unicast client. |
| int | [bt\_bap\_unicast\_group\_delete](group__bt__bap__unicast__client.md#ga34dbdce6133f8366df453ec937fb47d2) (struct bt\_bap\_unicast\_group \*unicast\_group) |
|  | Delete audio unicast group. |
| int | [bt\_bap\_unicast\_client\_register\_cb](group__bt__bap__unicast__client.md#gade70f04ae1a828b43b3b44fa8933f674) (struct [bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md) \*cb) |
|  | Register unicast client callbacks. |
| int | [bt\_bap\_unicast\_client\_discover](group__bt__bap__unicast__client.md#gacef9c88f66762e8de19303d20dafa0bb) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
|  | Discover remote capabilities and endpoints. |
| const struct bt\_bap\_base \* | [bt\_bap\_base\_get\_base\_from\_ad](group__bt__bap__broadcast.md#ga29423a39d76ad16f0586d82a23c07ba7) (const struct [bt\_data](structbt__data.md) \*ad) |
|  | Generate a pointer to a BASE from periodic advertising data. |
| int | [bt\_bap\_base\_get\_size](group__bt__bap__broadcast.md#ga539f92b71ec34f0551ef6240d83b972e) (const struct bt\_bap\_base \*base) |
|  | Get the size of a BASE. |
| int | [bt\_bap\_base\_get\_pres\_delay](group__bt__bap__broadcast.md#gaf91f45bcf7df2f368c5abeb116b65dd0) (const struct bt\_bap\_base \*base) |
|  | Get the presentation delay value of a BASE. |
| int | [bt\_bap\_base\_get\_subgroup\_count](group__bt__bap__broadcast.md#gadcae0230168564da1ee8b3c577ce27d7) (const struct bt\_bap\_base \*base) |
|  | Get the subgroup count of a BASE. |
| int | [bt\_bap\_base\_get\_bis\_indexes](group__bt__bap__broadcast.md#ga6deab5a8b7a16ddf0c3685d4003694e1) (const struct bt\_bap\_base \*base, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bis\_indexes) |
|  | Get all BIS indexes of a BASE. |
| int | [bt\_bap\_base\_foreach\_subgroup](group__bt__bap__broadcast.md#ga5e6e0b758409cbdde93c0f648ef5e5e8) (const struct bt\_bap\_base \*base, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*func)(const struct bt\_bap\_base\_subgroup \*subgroup, void \*user\_data), void \*user\_data) |
|  | Iterate on all subgroups in the BASE. |
| int | [bt\_bap\_base\_get\_subgroup\_codec\_id](group__bt__bap__broadcast.md#gae75e05a002dee8336eb066ae8231ea0c) (const struct bt\_bap\_base\_subgroup \*subgroup, struct [bt\_bap\_base\_codec\_id](structbt__bap__base__codec__id.md) \*codec\_id) |
|  | Get the codec ID of a subgroup. |
| int | [bt\_bap\_base\_get\_subgroup\_codec\_data](group__bt__bap__broadcast.md#ga10e2e32dc2802ba55d55c77148331f6a) (const struct bt\_bap\_base\_subgroup \*subgroup, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
|  | Get the codec configuration data of a subgroup. |
| int | [bt\_bap\_base\_get\_subgroup\_codec\_meta](group__bt__bap__broadcast.md#gafb9d9544f38c7ad2613fff1679eb1f0c) (const struct bt\_bap\_base\_subgroup \*subgroup, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*meta) |
|  | Get the codec metadata of a subgroup. |
| int | [bt\_bap\_base\_subgroup\_codec\_to\_codec\_cfg](group__bt__bap__broadcast.md#ga920e3409f1978b803bcf6bc8d05ac8f6) (const struct bt\_bap\_base\_subgroup \*subgroup, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Store subgroup codec data in a [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs"). |
| int | [bt\_bap\_base\_get\_subgroup\_bis\_count](group__bt__bap__broadcast.md#ga051e1f8aa2faf3ba7a973356138fd2d3) (const struct bt\_bap\_base\_subgroup \*subgroup) |
|  | Get the BIS count of a subgroup. |
| int | [bt\_bap\_base\_subgroup\_get\_bis\_indexes](group__bt__bap__broadcast.md#ga37df3bf1e18d2d8e9388541217b2e366) (const struct bt\_bap\_base\_subgroup \*subgroup, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bis\_indexes) |
|  | Get all BIS indexes of a subgroup. |
| int | [bt\_bap\_base\_subgroup\_foreach\_bis](group__bt__bap__broadcast.md#ga4f85ee43984cb2f3139b41da7b9b1aee) (const struct bt\_bap\_base\_subgroup \*subgroup, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*func)(const struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) \*bis, void \*user\_data), void \*user\_data) |
|  | Iterate on all BIS in the subgroup. |
| int | [bt\_bap\_base\_subgroup\_bis\_codec\_to\_codec\_cfg](group__bt__bap__broadcast.md#gaa5cb191df7807ea87f1fba1871ca8ebe) (const struct [bt\_bap\_base\_subgroup\_bis](structbt__bap__base__subgroup__bis.md) \*bis, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Store BIS codec configuration data in a [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs"). |
| int | [bt\_bap\_broadcast\_source\_create](group__bt__bap__broadcast__source.md#gacdebfc435eebd47cf9cd05099a5f78e0) (struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) \*param, struct bt\_bap\_broadcast\_source \*\*source) |
|  | Create audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_reconfig](group__bt__bap__broadcast__source.md#gabecaa9db7be5cb03ed997ba478878d40) (struct bt\_bap\_broadcast\_source \*source, struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) \*param) |
|  | Reconfigure audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_update\_metadata](group__bt__bap__broadcast__source.md#gaff2cfdadbff3ebe1e2efb660dee56f02) (struct bt\_bap\_broadcast\_source \*source, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len) |
|  | Modify the metadata of an audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_start](group__bt__bap__broadcast__source.md#gac4640f5207599d51c1a63ff47f3c1d5a) (struct bt\_bap\_broadcast\_source \*source, struct bt\_le\_ext\_adv \*adv) |
|  | Start audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_stop](group__bt__bap__broadcast__source.md#ga36a885581eec5cab8b3f652db19b9aba) (struct bt\_bap\_broadcast\_source \*source) |
|  | Stop audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_delete](group__bt__bap__broadcast__source.md#ga12e0a4856115a8eb297fe2d1fc130155) (struct bt\_bap\_broadcast\_source \*source) |
|  | Delete audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_get\_base](group__bt__bap__broadcast__source.md#gafe07e4c6962858500fcf66415a173be8) (struct bt\_bap\_broadcast\_source \*source, struct [net\_buf\_simple](structnet__buf__simple.md) \*base\_buf) |
|  | Get the Broadcast Audio Stream Endpoint of a broadcast source. |
| int | [bt\_bap\_broadcast\_sink\_register\_cb](group__bt__bap__broadcast__sink.md#ga1b83ead634d990e954f233d0208c5a85) (struct [bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md) \*cb) |
|  | Register Broadcast sink callbacks. |
| int | [bt\_bap\_broadcast\_sink\_create](group__bt__bap__broadcast__sink.md#ga0637d1957db70ad39e0608ed07e75166) (struct bt\_le\_per\_adv\_sync \*pa\_sync, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) broadcast\_id, struct bt\_bap\_broadcast\_sink \*\*sink) |
|  | Create a Broadcast Sink from a periodic advertising sync. |
| int | [bt\_bap\_broadcast\_sink\_sync](group__bt__bap__broadcast__sink.md#gacadebb5ce8aab5f5b8f1ff7e0fa57805) (struct bt\_bap\_broadcast\_sink \*sink, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) indexes\_bitfield, struct [bt\_bap\_stream](structbt__bap__stream.md) \*streams[], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) broadcast\_code[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)]) |
|  | Sync to a broadcaster's audio. |
| int | [bt\_bap\_broadcast\_sink\_stop](group__bt__bap__broadcast__sink.md#ga1020b21bfb4195aeb5823197145b1fe9) (struct bt\_bap\_broadcast\_sink \*sink) |
|  | Stop audio broadcast sink. |
| int | [bt\_bap\_broadcast\_sink\_delete](group__bt__bap__broadcast__sink.md#ga8b9d6cb409a3671654e053475ada3fda) (struct bt\_bap\_broadcast\_sink \*sink) |
|  | Release a broadcast sink. |
| int | [bt\_bap\_scan\_delegator\_register](group__bt__bap.md#ga7632ab444dbf99387871f7d0c90b11ba) (struct [bt\_bap\_scan\_delegator\_cb](structbt__bap__scan__delegator__cb.md) \*cb) |
|  | Register the Basic Audio Profile Scan Delegator and BASS. |
| int | [bt\_bap\_scan\_delegator\_unregister](group__bt__bap.md#ga6f52e58767303ded16cb6289f094895a) (void) |
|  | unregister the Basic Audio Profile Scan Delegator and BASS. |
| int | [bt\_bap\_scan\_delegator\_set\_pa\_state](group__bt__bap.md#ga381c1f3b386ecbdfd570eb125882161e) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id, enum [bt\_bap\_pa\_state](group__bt__bap.md#gac551e9b0d53fd50f3a9e9c08447f0296) pa\_state) |
|  | Set the periodic advertising sync state to syncing. |
| int | [bt\_bap\_scan\_delegator\_set\_bis\_sync\_state](group__bt__bap.md#ga7cce7e53264294abec4421364afffdbe) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bis\_synced[CONFIG\_BT\_BAP\_BASS\_MAX\_SUBGROUPS]) |
|  | Set the sync state of a receive state in the server. |
| int | [bt\_bap\_scan\_delegator\_add\_src](group__bt__bap.md#ga6eb2a782d761da12d112356cfe723ff0) (const struct [bt\_bap\_scan\_delegator\_add\_src\_param](structbt__bap__scan__delegator__add__src__param.md) \*param) |
|  | Add a receive state source locally. |
| int | [bt\_bap\_scan\_delegator\_mod\_src](group__bt__bap.md#gac022f38269742f16ff6887840ef5ba9a) (const struct [bt\_bap\_scan\_delegator\_mod\_src\_param](structbt__bap__scan__delegator__mod__src__param.md) \*param) |
|  | Add a receive state source locally. |
| int | [bt\_bap\_scan\_delegator\_rem\_src](group__bt__bap.md#ga6c240f1cdb33945197700e4fe106ef2c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id) |
|  | Remove a receive state source. |
| void | [bt\_bap\_scan\_delegator\_foreach\_state](group__bt__bap.md#gab6f1a12699a9437c6575c70df33d5be0) ([bt\_bap\_scan\_delegator\_state\_func\_t](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824) func, void \*user\_data) |
|  | Iterate through all existing receive states. |
| const struct [bt\_bap\_scan\_delegator\_recv\_state](structbt__bap__scan__delegator__recv__state.md) \* | [bt\_bap\_scan\_delegator\_find\_state](group__bt__bap.md#gabec9fd0a2966e1811fd4770855050510) ([bt\_bap\_scan\_delegator\_state\_func\_t](group__bt__bap.md#gaf236a87ae461ad48ec59f487780b4824) func, void \*user\_data) |
|  | Find and return a receive state based on a compare function. |
| int | [bt\_bap\_broadcast\_assistant\_discover](group__bt__bap.md#gab59c5ebc4fef28da34d8a54b1244c33b) (struct bt\_conn \*conn) |
|  | Discover Broadcast Audio Scan Service on the server. |
| int | [bt\_bap\_broadcast\_assistant\_scan\_start](group__bt__bap.md#ga98ac067e66d263aa41fc6f8df6bb9126) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) start\_scan) |
|  | Scan start for BISes for a remote server. |
| int | [bt\_bap\_broadcast\_assistant\_scan\_stop](group__bt__bap.md#ga76cae35df980b78a10551811050b2760) (struct bt\_conn \*conn) |
|  | Stop remote scanning for BISes for a server. |
| int | [bt\_bap\_broadcast\_assistant\_register\_cb](group__bt__bap.md#gabab24c44e9833029965475ad7b149e6e) (struct [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) \*cb) |
|  | Registers the callbacks used by Broadcast Audio Scan Service client. |
| int | [bt\_bap\_broadcast\_assistant\_unregister\_cb](group__bt__bap.md#ga679cdeb6e555bfc9ce20f38e493000ee) (struct [bt\_bap\_broadcast\_assistant\_cb](structbt__bap__broadcast__assistant__cb.md) \*cb) |
|  | Unregisters the callbacks used by the Broadcast Audio Scan Service client. |
| int | [bt\_bap\_broadcast\_assistant\_add\_src](group__bt__bap.md#gac93cb4cab33d0b937e752bc0b71cad9e) (struct bt\_conn \*conn, const struct [bt\_bap\_broadcast\_assistant\_add\_src\_param](structbt__bap__broadcast__assistant__add__src__param.md) \*param) |
|  | Add a source on the server. |
| int | [bt\_bap\_broadcast\_assistant\_mod\_src](group__bt__bap.md#gaa9c292a7dcb470926d8d7d4be699a0c7) (struct bt\_conn \*conn, const struct [bt\_bap\_broadcast\_assistant\_mod\_src\_param](structbt__bap__broadcast__assistant__mod__src__param.md) \*param) |
|  | Modify a source on the server. |
| int | [bt\_bap\_broadcast\_assistant\_set\_broadcast\_code](group__bt__bap.md#gabcec07689c13a996bcb9d2d417347dbb) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) broadcast\_code[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)]) |
|  | Set a broadcast code to the specified receive state. |
| int | [bt\_bap\_broadcast\_assistant\_rem\_src](group__bt__bap.md#ga09785690db551677a043fcaa2fdb7f29) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_id) |
|  | Remove a source from the server. |
| int | [bt\_bap\_broadcast\_assistant\_read\_recv\_state](group__bt__bap.md#ga94fce2b4346b1026d53e0b860ca7fbf2) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx) |
|  | Read the specified receive state from the server. |

## Detailed Description

Header for Bluetooth BAP.

Copyright (c) 2020 Bose Corporation Copyright (c) 2021-2024 Nordic Semiconductor ASA

SPDX-License-Identifier: Apache-2.0

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [bap.h](bap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
