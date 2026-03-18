---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/access_8h.html
original_path: doxygen/html/access_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

access.h File Reference

Access layer APIs.
[More...](#details)

`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/settings/settings.h](settings_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/msg.h](msg_8h_source.md)>`

[Go to the source code of this file.](access_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_elem](structbt__mesh__elem.md) |
|  | Abstraction that describes a Mesh Element. [More...](structbt__mesh__elem.md#details) |
| struct | [bt\_mesh\_elem::bt\_mesh\_elem\_rt\_ctx](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md) |
|  | Mesh Element runtime information. [More...](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md#details) |
| struct | [bt\_mesh\_model\_op](structbt__mesh__model__op.md) |
|  | Model opcode handler. [More...](structbt__mesh__model__op.md#details) |
| struct | [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md) |
|  | Model publication context. [More...](structbt__mesh__model__pub.md#details) |
| struct | [bt\_mesh\_models\_metadata\_entry](structbt__mesh__models__metadata__entry.md) |
|  | Models Metadata Entry struct. [More...](structbt__mesh__models__metadata__entry.md#details) |
| struct | [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) |
|  | Model callback functions. [More...](structbt__mesh__model__cb.md#details) |
| struct | [bt\_mesh\_mod\_id\_vnd](structbt__mesh__mod__id__vnd.md) |
|  | Vendor model ID. [More...](structbt__mesh__mod__id__vnd.md#details) |
| struct | [bt\_mesh\_model](structbt__mesh__model.md) |
|  | Abstraction that describes a Mesh Model instance. [More...](structbt__mesh__model.md#details) |
| struct | [bt\_mesh\_model::bt\_mesh\_model\_rt\_ctx](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md) |
| struct | [bt\_mesh\_send\_cb](structbt__mesh__send__cb.md) |
|  | Callback structure for monitoring model message sending. [More...](structbt__mesh__send__cb.md#details) |
| struct | [bt\_mesh\_comp](structbt__mesh__comp.md) |
|  | Node Composition. [More...](structbt__mesh__comp.md#details) |
| struct | [bt\_mesh\_comp2\_record](structbt__mesh__comp2__record.md) |
|  | Composition data page 2 record. [More...](structbt__mesh__comp2__record.md#details) |
| struct | [bt\_mesh\_comp2](structbt__mesh__comp2.md) |
|  | Node Composition data page 2. [More...](structbt__mesh__comp2.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_KEY\_UNUSED\_ELT\_](#abe51f11257cf1bbb236e899e7a23acbc)(IDX, \_) |
| #define | [BT\_MESH\_ADDR\_UNASSIGNED\_ELT\_](#a421f6ac3aa620d77033a98f3d059e3ce)(IDX, \_) |
| #define | [BT\_MESH\_UUID\_UNASSIGNED\_ELT\_](#aa5b0403118f5fd434e2ca9c298aee1fd)(IDX, \_) |
| #define | [BT\_MESH\_MODEL\_KEYS\_UNUSED](#a575258fd6073a81b8037b6127f6b975a)(\_keys) |
| #define | [BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED](#a6023b10a0b89e067d68e8393155a2945)(\_grps) |
| #define | [BT\_MESH\_MODEL\_UUIDS\_UNASSIGNED](#abf60c1897454c0cbfa034bc4a3c92843)() |
| #define | [BT\_MESH\_MODEL\_RUNTIME\_INIT](#ad28c5301ea6cf93f3bf2a672043cae4e)(\_user\_data) |
| #define | [BT\_MESH\_ADDR\_IS\_UNICAST](group__bt__mesh__access.md#ga1a4694cccf834d71f0abe2a0283cb9a8)(addr) |
|  | Check if a Bluetooth Mesh address is a unicast address. |
| #define | [BT\_MESH\_ADDR\_IS\_GROUP](group__bt__mesh__access.md#gab50cc8dca6f7ffd5420ef4fb38fbe224)(addr) |
|  | Check if a Bluetooth Mesh address is a group address. |
| #define | [BT\_MESH\_ADDR\_IS\_FIXED\_GROUP](group__bt__mesh__access.md#gaff5ff58937924a1e6297aa1b20efc30f)(addr) |
|  | Check if a Bluetooth Mesh address is a fixed group address. |
| #define | [BT\_MESH\_ADDR\_IS\_VIRTUAL](group__bt__mesh__access.md#ga623eb2da2c880eec2107f36402ba6621)(addr) |
|  | Check if a Bluetooth Mesh address is a virtual address. |
| #define | [BT\_MESH\_ADDR\_IS\_RFU](group__bt__mesh__access.md#ga98ba7663259ca43cd5a38c7a9e16516d)(addr) |
|  | Check if a Bluetooth Mesh address is an RFU address. |
| #define | [BT\_MESH\_IS\_DEV\_KEY](group__bt__mesh__access.md#gac4aafa0bdd24fb51d515a62e83917936)(key) |
|  | Check if a Bluetooth Mesh key is a device key. |
| #define | [BT\_MESH\_APP\_SEG\_SDU\_MAX](group__bt__mesh__access.md#gaa620c32d1dce8e4b691b7f4270016506)   12 |
|  | Maximum size of an access message segment (in octets). |
| #define | [BT\_MESH\_APP\_UNSEG\_SDU\_MAX](group__bt__mesh__access.md#ga64eb6a94b1db9899c4f5bbf4cc88cd9f)   15 |
|  | Maximum payload size of an unsegmented access message (in octets). |
| #define | [BT\_MESH\_RX\_SEG\_MAX](group__bt__mesh__access.md#ga18756e939ec3b312eef5c3dc9fd70270)   0 |
|  | Maximum number of segments supported for incoming messages. |
| #define | [BT\_MESH\_TX\_SEG\_MAX](group__bt__mesh__access.md#ga1b2a3610ac370266578abce195e65fa2)   0 |
|  | Maximum number of segments supported for outgoing messages. |
| #define | [BT\_MESH\_TX\_SDU\_MAX](group__bt__mesh__access.md#ga86d7386603ecd89952b6d540ea4243c2) |
|  | Maximum possible payload size of an outgoing access message (in octets). |
| #define | [BT\_MESH\_RX\_SDU\_MAX](group__bt__mesh__access.md#ga36f299f2fc13892b5a7d871dad1ec9ce) |
|  | Maximum possible payload size of an incoming access message (in octets). |
| #define | [BT\_MESH\_ELEM](group__bt__mesh__access.md#ga321a5091dabd4ec4beb5396db6cabf44)(\_loc, \_mods, \_vnd\_mods) |
|  | Helper to define a mesh element within an array. |
| #define | [BT\_MESH\_MODEL\_OP\_1](group__bt__mesh__access.md#ga00915cfdff7dc0646f24d6b06e124d0d)(b0) |
| #define | [BT\_MESH\_MODEL\_OP\_2](group__bt__mesh__access.md#gaa52a40ef5972c4f34cf5ff5a10e21289)(b0, b1) |
| #define | [BT\_MESH\_MODEL\_OP\_3](group__bt__mesh__access.md#ga72d1d19701be52f5eac6af475f9b19a9)(b0, cid) |
| #define | [BT\_MESH\_LEN\_EXACT](group__bt__mesh__access.md#ga637e1be0298dc681414645867b28b59f)(len) |
|  | Macro for encoding exact message length for fixed-length messages. |
| #define | [BT\_MESH\_LEN\_MIN](group__bt__mesh__access.md#ga691ed9b3ab3ddaceda0f81c4a715ab3a)(len) |
|  | Macro for encoding minimum message length for variable-length messages. |
| #define | [BT\_MESH\_MODEL\_OP\_END](group__bt__mesh__access.md#gaf2c164506c601214c85d451747176827)   { 0, 0, NULL } |
|  | End of the opcode list. |
| #define | [BT\_MESH\_MODEL\_NO\_OPS](group__bt__mesh__access.md#gae6d55e0a27bb7c448affd312a2e11656) |
|  | Helper to define an empty opcode list. |
| #define | [BT\_MESH\_MODEL\_NONE](group__bt__mesh__access.md#gab0ad2aab95d49e5b60fe8dafd69132a4)   ((const struct [bt\_mesh\_model](structbt__mesh__model.md) []){}) |
|  | Helper to define an empty model array. |
| #define | [BT\_MESH\_MODEL\_CNT\_CB](group__bt__mesh__access.md#ga925da443eb15a4c1980d48a69388dc2c)(\_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb) |
|  | Composition data SIG model entry with callback functions with specific number of keys & groups. |
| #define | [BT\_MESH\_MODEL\_CNT\_VND\_CB](group__bt__mesh__access.md#ga32733dccd9329aa938dc0bd21cf9beae)(\_company, \_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb) |
|  | Composition data vendor model entry with callback functions with specific number of keys & groups. |
| #define | [BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)(\_id, \_op, \_pub, \_user\_data, \_cb) |
|  | Composition data SIG model entry with callback functions. |
| #define | [BT\_MESH\_MODEL\_METADATA\_CB](group__bt__mesh__access.md#ga40204b4ccaa819a487de168bcf66c98f)(\_id, \_op, \_pub, \_user\_data, \_cb, \_metadata) |
|  | Composition data SIG model entry with callback functions and metadata. |
| #define | [BT\_MESH\_MODEL\_VND\_CB](group__bt__mesh__access.md#gabe79d914990ba2721f5bb7081910e512)(\_company, \_id, \_op, \_pub, \_user\_data, \_cb) |
|  | Composition data vendor model entry with callback functions. |
| #define | [BT\_MESH\_MODEL\_VND\_METADATA\_CB](group__bt__mesh__access.md#gac62334962dcbe3a75a03ce5744b326d8)(\_company, \_id, \_op, \_pub, \_user\_data, \_cb, \_metadata) |
|  | Composition data vendor model entry with callback functions and metadata. |
| #define | [BT\_MESH\_MODEL](group__bt__mesh__access.md#gae694f5ac7ef9f0de37aaba846443586f)(\_id, \_op, \_pub, \_user\_data) |
|  | Composition data SIG model entry. |
| #define | [BT\_MESH\_MODEL\_VND](group__bt__mesh__access.md#ga3759c8c88db48be662bf2511ff514edd)(\_company, \_id, \_op, \_pub, \_user\_data) |
|  | Composition data vendor model entry. |
| #define | [BT\_MESH\_TRANSMIT](group__bt__mesh__access.md#gaff82bf652232fbce71c31f38a10577a9)(count, int\_ms) |
|  | Encode transmission count & interval steps. |
| #define | [BT\_MESH\_TRANSMIT\_COUNT](group__bt__mesh__access.md#ga62fda0d731241efbaa4827e4eb9d1795)(transmit) |
|  | Decode transmit count from a transmit value. |
| #define | [BT\_MESH\_TRANSMIT\_INT](group__bt__mesh__access.md#ga2aa21171c5677d23ad0c472291639417)(transmit) |
|  | Decode transmit interval from a transmit value. |
| #define | [BT\_MESH\_PUB\_TRANSMIT](group__bt__mesh__access.md#ga19208dea7bab9f31c2c793ef6201dd91)(count, int\_ms) |
|  | Encode Publish Retransmit count & interval steps. |
| #define | [BT\_MESH\_PUB\_TRANSMIT\_COUNT](group__bt__mesh__access.md#ga13986422dda5edce4f5fb1ce387093e3)(transmit) |
|  | Decode Publish Retransmit count from a given value. |
| #define | [BT\_MESH\_PUB\_TRANSMIT\_INT](group__bt__mesh__access.md#gaac954956dd3913dd7ad2b93a2566afd9)(transmit) |
|  | Decode Publish Retransmit interval from a given value. |
| #define | [BT\_MESH\_PUB\_MSG\_TOTAL](group__bt__mesh__access.md#ga230538bb39ac3d6c8c0327d1fad77e69)(pub) |
|  | Get total number of messages within one publication interval including initial publication. |
| #define | [BT\_MESH\_PUB\_MSG\_NUM](group__bt__mesh__access.md#ga115ee29aba3c3e985aa11d6692ca0d83)(pub) |
|  | Get message number within one publication interval. |
| #define | [BT\_MESH\_MODEL\_PUB\_DEFINE](group__bt__mesh__access.md#ga8334ff2da1f0dc3ab2fc914059c33622)(\_name, \_update, \_msg\_len) |
|  | Define a model publication context. |
| #define | [BT\_MESH\_MODELS\_METADATA\_ENTRY](group__bt__mesh__access.md#gaa2587adac719c50c311ae41c548b853c)(\_len, \_id, \_data) |
|  | Initialize a Models Metadata entry structure in a list. |
| #define | [BT\_MESH\_MODELS\_METADATA\_NONE](group__bt__mesh__access.md#ga56b518123ab47cb3ae4a249f471ae556)   NULL |
|  | Helper to define an empty Models metadata array. |
| #define | [BT\_MESH\_MODELS\_METADATA\_END](group__bt__mesh__access.md#gaab5fe51071f6e54debd9136ac6a70a49)   { 0, 0, NULL } |
|  | End of the Models Metadata list. |
| #define | [BT\_MESH\_TTL\_DEFAULT](group__bt__mesh__access.md#ga16516272b42420263b1c47c3ea16c0c8)   0xff |
|  | Special TTL value to request using configured default TTL. |
| #define | [BT\_MESH\_TTL\_MAX](group__bt__mesh__access.md#ga071e85e929589d31bf876e2e09cf2f19)   0x7f |
|  | Maximum allowed TTL value. |
| Group addresses | |
| #define | [BT\_MESH\_ADDR\_UNASSIGNED](group__bt__mesh__access.md#ga6d11790af686e6d48f08c6f1cd65317c)   0x0000 |
|  | unassigned |
| #define | [BT\_MESH\_ADDR\_ALL\_NODES](group__bt__mesh__access.md#ga27aafd100b6ccc1de060a75370184620)   0xffff |
|  | all-nodes |
| #define | [BT\_MESH\_ADDR\_RELAYS](group__bt__mesh__access.md#ga5ee81d48846de9c9c966ffe0b90ff011)   0xfffe |
|  | all-relays |
| #define | [BT\_MESH\_ADDR\_FRIENDS](group__bt__mesh__access.md#ga5d44892368bb7c1ecd205a81e66bd6f7)   0xfffd |
|  | all-friends |
| #define | [BT\_MESH\_ADDR\_PROXIES](group__bt__mesh__access.md#ga30d4975d25c2c120da1cbfadf29c098f)   0xfffc |
|  | all-proxies |
| #define | [BT\_MESH\_ADDR\_DFW\_NODES](group__bt__mesh__access.md#gabf77d8365ddc278838fa450826e43243)   0xfffb |
|  | all-directed-forwarding-nodes |
| #define | [BT\_MESH\_ADDR\_IP\_NODES](group__bt__mesh__access.md#gafd70174e5072dbbfed31156f152aeaa1)   0xfffa |
|  | all-ipt-nodes |
| #define | [BT\_MESH\_ADDR\_IP\_BR\_ROUTERS](group__bt__mesh__access.md#ga1055381438e55e953dec2e6d592ab103)   0xfff9 |
|  | all-ipt-border-routers |
| Predefined key indexes | |
| #define | [BT\_MESH\_KEY\_UNUSED](group__bt__mesh__access.md#gace23095bac3705c2f2afab749e48c02d)   0xffff |
|  | Key unused. |
| #define | [BT\_MESH\_KEY\_ANY](group__bt__mesh__access.md#ga7718cce0713be98a08420c7eab1b40ee)   0xffff |
|  | Any key index. |
| #define | [BT\_MESH\_KEY\_DEV](group__bt__mesh__access.md#gabd37f17f3f5c3bc399ad3699df282675)   0xfffe |
|  | Device key. |
| #define | [BT\_MESH\_KEY\_DEV\_LOCAL](group__bt__mesh__access.md#ga9c64b38f2a6879f4750e3e1828e8ab7a)   [BT\_MESH\_KEY\_DEV](group__bt__mesh__access.md#gabd37f17f3f5c3bc399ad3699df282675) |
|  | Local device key. |
| #define | [BT\_MESH\_KEY\_DEV\_REMOTE](group__bt__mesh__access.md#gaaa6ffb62df5d6d55c831d4d9860fc7eb)   0xfffd |
|  | Remote device key. |
| #define | [BT\_MESH\_KEY\_DEV\_ANY](group__bt__mesh__access.md#gace0a526534e31e8067daf283407533fd)   0xfffc |
|  | Any device key. |
| Foundation Models | |
| #define | [BT\_MESH\_MODEL\_ID\_CFG\_SRV](group__bt__mesh__access.md#ga004d8d1be55b2aec56abbeeca1d118d8)   0x0000 |
|  | Configuration Server. |
| #define | [BT\_MESH\_MODEL\_ID\_CFG\_CLI](group__bt__mesh__access.md#ga3f8442dcd1a110ea0d0023f50057139f)   0x0001 |
|  | Configuration Client. |
| #define | [BT\_MESH\_MODEL\_ID\_HEALTH\_SRV](group__bt__mesh__access.md#ga6416216348d7186f91175ca50bb8c903)   0x0002 |
|  | Health Server. |
| #define | [BT\_MESH\_MODEL\_ID\_HEALTH\_CLI](group__bt__mesh__access.md#gab58b85b7a77feeb579973177c12bb446)   0x0003 |
|  | Health Client. |
| #define | [BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_SRV](group__bt__mesh__access.md#ga9c7d1c5dfb87a5ce50c08747af47414f)   0x0004 |
|  | Remote Provisioning Server. |
| #define | [BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_CLI](group__bt__mesh__access.md#gaf373eb4d8af5d6bee76a821bd4d5e48c)   0x0005 |
|  | Remote Provisioning Client. |
| #define | [BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_SRV](group__bt__mesh__access.md#gacca0e355982935cfbde46a06b09a7bec)   0x000a |
|  | Private Beacon Server. |
| #define | [BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_CLI](group__bt__mesh__access.md#gab3b21cbee4e11319a6e0ba3b02b24a91)   0x000b |
|  | Private Beacon Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SAR\_CFG\_SRV](group__bt__mesh__access.md#ga1e9d8be1d2e65d2977aea0306b015258)   0x000e |
|  | SAR Configuration Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SAR\_CFG\_CLI](group__bt__mesh__access.md#gaf214eb7eef3530919432b62ff9b353c3)   0x000f |
|  | SAR Configuration Client. |
| #define | [BT\_MESH\_MODEL\_ID\_OP\_AGG\_SRV](group__bt__mesh__access.md#ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a)   0x0010 |
|  | Opcodes Aggregator Server. |
| #define | [BT\_MESH\_MODEL\_ID\_OP\_AGG\_CLI](group__bt__mesh__access.md#gabac62a77e7d2d7677af21c33c8629187)   0x0011 |
|  | Opcodes Aggregator Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_SRV](group__bt__mesh__access.md#gaec3abd6a0bd7b07a71fe5ed6a7a6931a)   0x0012 |
|  | Large Composition Data Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_CLI](group__bt__mesh__access.md#ga729d67e4183457932e4c837d65abd842)   0x0013 |
|  | Large Composition Data Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_SRV](group__bt__mesh__access.md#ga165bc198dadaa0d534ec82eb8192ebc0)   0x0014 |
|  | Solicitation PDU RPL Configuration Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_CLI](group__bt__mesh__access.md#ga6e747dd364bcfaa368e37c5f01afd530)   0x0015 |
|  | Solicitation PDU RPL Configuration Server. |
| #define | [BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_SRV](group__bt__mesh__access.md#gaddc0bd645180a57cb9cd36745b84f7a1)   0x000c |
|  | Private Proxy Server. |
| #define | [BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_CLI](group__bt__mesh__access.md#gadd36546fb2cb6d1c731f7ae7674af6a7)   0x000d |
|  | Private Proxy Client. |
| Models from the Mesh Model Specification | |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_SRV](group__bt__mesh__access.md#ga83e1ed5398d513cfeb900e41655aa4d8)   0x1000 |
|  | Generic OnOff Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_CLI](group__bt__mesh__access.md#ga4f0eee2569b518a5e4250f5b7b294fed)   0x1001 |
|  | Generic OnOff Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_SRV](group__bt__mesh__access.md#ga7f10a8332b1406c3ad628b9679e1d7cb)   0x1002 |
|  | Generic Level Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_CLI](group__bt__mesh__access.md#ga462c578845a17b20cdb3e008f74f93a6)   0x1003 |
|  | Generic Level Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_SRV](group__bt__mesh__access.md#ga004d5ec0870d47a8d37182e5b0c089a5)   0x1004 |
|  | Generic Default Transition Time Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_CLI](group__bt__mesh__access.md#gafa1c6a7d857fe13a139ce2242b4e62f5)   0x1005 |
|  | Generic Default Transition Time Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SRV](group__bt__mesh__access.md#ga09ac731fff09146ec68557f00e8294e0)   0x1006 |
|  | Generic Power OnOff Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SETUP\_SRV](group__bt__mesh__access.md#ga2a6dad18792ba7f1d81d6c9a1c65f90a)   0x1007 |
|  | Generic Power OnOff Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_CLI](group__bt__mesh__access.md#ga9f6544f7b87f39d0792ea2de13cd45f1)   0x1008 |
|  | Generic Power OnOff Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SRV](group__bt__mesh__access.md#gadd30afe63f89e9c1778e56f722fd82f9)   0x1009 |
|  | Generic Power Level Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SETUP\_SRV](group__bt__mesh__access.md#ga1ff6ec64ce3a86d1cfd00fc98e89c0a5)   0x100a |
|  | Generic Power Level Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_CLI](group__bt__mesh__access.md#ga8420454c35afc12c62ede55942f3b6d3)   0x100b |
|  | Generic Power Level Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_SRV](group__bt__mesh__access.md#gacf891135f54fb1fbb62beb812235619e)   0x100c |
|  | Generic Battery Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_CLI](group__bt__mesh__access.md#ga34bb3d4839e9685ec55f8285aac9a79f)   0x100d |
|  | Generic Battery Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SRV](group__bt__mesh__access.md#gad516f513c5c942fbfee65b85332b105e)   0x100e |
|  | Generic Location Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SETUPSRV](group__bt__mesh__access.md#ga240d1ed34b7341627773cce862f85620)   0x100f |
|  | Generic Location Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_CLI](group__bt__mesh__access.md#ga8fa01ddb1f4de4d61500bb650243390d)   0x1010 |
|  | Generic Location Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_ADMIN\_PROP\_SRV](group__bt__mesh__access.md#ga3cc6862e9c72f9282055c5cda2343c89)   0x1011 |
|  | Generic Admin Property Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_MANUFACTURER\_PROP\_SRV](group__bt__mesh__access.md#ga32e09ddfebd2e8b22da9a3102e116aae)   0x1012 |
|  | Generic Manufacturer Property Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_USER\_PROP\_SRV](group__bt__mesh__access.md#ga4b7b6a4b47e87de94ccf11ef1abd64b9)   0x1013 |
|  | Generic User Property Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_CLIENT\_PROP\_SRV](group__bt__mesh__access.md#ga20906658018ef26114d8a6656c258f62)   0x1014 |
|  | Generic Client Property Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_PROP\_CLI](group__bt__mesh__access.md#ga69455e5b1e6def3d909c4bb6e0dee9ae)   0x1015 |
|  | Generic Property Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SENSOR\_SRV](group__bt__mesh__access.md#ga3e0dcb14f46f6076e5b1b114b977f630)   0x1100 |
|  | Sensor Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SENSOR\_SETUP\_SRV](group__bt__mesh__access.md#gad10780bfc1c16866fa28de750e56bec3)   0x1101 |
|  | Sensor Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SENSOR\_CLI](group__bt__mesh__access.md#ga8f1e4ff66d388627dbe91b2f8d4ed358)   0x1102 |
|  | Sensor Client. |
| #define | [BT\_MESH\_MODEL\_ID\_TIME\_SRV](group__bt__mesh__access.md#ga93fbf1c661a75d70fdbd2a599353eb94)   0x1200 |
|  | Time Server. |
| #define | [BT\_MESH\_MODEL\_ID\_TIME\_SETUP\_SRV](group__bt__mesh__access.md#ga2725121dc8c2c21c0ee469fe4348f45f)   0x1201 |
|  | Time Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_TIME\_CLI](group__bt__mesh__access.md#ga500df90af7989794c5d72e760e5e65c6)   0x1202 |
|  | Time Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SCENE\_SRV](group__bt__mesh__access.md#gaaa5554e3d48ae101596476e6bd6caf67)   0x1203 |
|  | Scene Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SCENE\_SETUP\_SRV](group__bt__mesh__access.md#gaa3b08fc8788684abb960fa3516726264)   0x1204 |
|  | Scene Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SCENE\_CLI](group__bt__mesh__access.md#gad60472aa004a8a913aeb63ef62c45857)   0x1205 |
|  | Scene Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SCHEDULER\_SRV](group__bt__mesh__access.md#ga82b723752e240f22b9bcc8dc3dd10eb9)   0x1206 |
|  | Scheduler Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SCHEDULER\_SETUP\_SRV](group__bt__mesh__access.md#ga3dbec5a3b82cb25a142c4bc851e3fe0e)   0x1207 |
|  | Scheduler Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SCHEDULER\_CLI](group__bt__mesh__access.md#gac743b26cf7e746b16302c25e8cd56221)   0x1208 |
|  | Scheduler Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SRV](group__bt__mesh__access.md#ga16df49e84e84d0ae4a6ab5d5f3f1b2b6)   0x1300 |
|  | Light Lightness Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SETUP\_SRV](group__bt__mesh__access.md#gadb93b2ed2256a5c9c3f66237841b1bf5)   0x1301 |
|  | Light Lightness Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_CLI](group__bt__mesh__access.md#ga960055723dec7b3b366efa7c49cafc2e)   0x1302 |
|  | Light Lightness Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SRV](group__bt__mesh__access.md#gaa9a211341c5b3283b9b0e0842adef053)   0x1303 |
|  | Light CTL Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SETUP\_SRV](group__bt__mesh__access.md#ga28ac69b2dbeec70bae4bd3c0381e9e93)   0x1304 |
|  | Light CTL Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_CLI](group__bt__mesh__access.md#ga58fc8d99b746b0061177ac5d95341da1)   0x1305 |
|  | Light CTL Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_TEMP\_SRV](group__bt__mesh__access.md#gafcb1f1ea20bb78b78a9ead4bfdbe3e47)   0x1306 |
|  | Light CTL Temperature Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SRV](group__bt__mesh__access.md#gaa0ddc753a226060d014dcd368feab17e)   0x1307 |
|  | Light HSL Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SETUP\_SRV](group__bt__mesh__access.md#ga574d3ba3f629bdbffc8f15db931a263a)   0x1308 |
|  | Light HSL Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_CLI](group__bt__mesh__access.md#ga2d111a352322be8e33ba0cba0feb3f0c)   0x1309 |
|  | Light HSL Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_HUE\_SRV](group__bt__mesh__access.md#ga865952346db9336a255c71bcb5f09774)   0x130a |
|  | Light HSL Hue Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SAT\_SRV](group__bt__mesh__access.md#gae55004e70670a8711e18e9c9b3428720)   0x130b |
|  | Light HSL Saturation Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SRV](group__bt__mesh__access.md#ga29e1a90f166d88b6773d9b7ccf08e1c7)   0x130c |
|  | Light xyL Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SETUP\_SRV](group__bt__mesh__access.md#ga4addae460d6b3c0a914198695b3e31ea)   0x130d |
|  | Light xyL Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_CLI](group__bt__mesh__access.md#ga0ca4d9997e6016b5c27f42549d42a99d)   0x130e |
|  | Light xyL Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SRV](group__bt__mesh__access.md#ga789412252034939539ba45e4bf21e3e2)   0x130f |
|  | Light LC Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SETUPSRV](group__bt__mesh__access.md#ga436358740bb64d845aa4d849d462a12e)   0x1310 |
|  | Light LC Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_CLI](group__bt__mesh__access.md#gaadd48b07e1eb53df24df40b7ea412e90)   0x1311 |
|  | Light LC Client. |
| Models from the Mesh Binary Large Object Transfer Model Specification | |
| #define | [BT\_MESH\_MODEL\_ID\_BLOB\_SRV](group__bt__mesh__access.md#gae85d4cf7aad4e94582c24f79d6f60904)   0x1400 |
|  | BLOB Transfer Server. |
| #define | [BT\_MESH\_MODEL\_ID\_BLOB\_CLI](group__bt__mesh__access.md#ga17e2e59a1344e623fe9fec6e27b7f22e)   0x1401 |
|  | BLOB Transfer Client. |
| Models from the Mesh Device Firmware Update Model Specification | |
| #define | [BT\_MESH\_MODEL\_ID\_DFU\_SRV](group__bt__mesh__access.md#ga0215c2c8cd16ab6536ea243864f9604e)   0x1402 |
|  | Firmware Update Server. |
| #define | [BT\_MESH\_MODEL\_ID\_DFU\_CLI](group__bt__mesh__access.md#gaf477a37238ec577000a646af40862ee1)   0x1403 |
|  | Firmware Update Client. |
| #define | [BT\_MESH\_MODEL\_ID\_DFD\_SRV](group__bt__mesh__access.md#gaf4309dea32d05274f8f3a6ea45faba38)   0x1404 |
|  | Firmware Distribution Server. |
| #define | [BT\_MESH\_MODEL\_ID\_DFD\_CLI](group__bt__mesh__access.md#ga87d3b5cc207dc3b51e85c9594bb98cad)   0x1405 |
|  | Firmware Distribution Client. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_model\_send](group__bt__mesh__access.md#ga7cac052ef76f4b37a95343329b078e77) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, struct [net\_buf\_simple](structnet__buf__simple.md) \*msg, const struct [bt\_mesh\_send\_cb](structbt__mesh__send__cb.md) \*cb, void \*cb\_data) |
|  | Send an Access Layer message. |
| int | [bt\_mesh\_model\_publish](group__bt__mesh__access.md#ga06644f8a5fa43351328d3f3403dbad03) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Send a model publication message. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_model\_pub\_is\_retransmission](group__bt__mesh__access.md#ga1b961d45f8b7c231c698ca229115e434) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Check if a message is being retransmitted. |
| const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \* | [bt\_mesh\_model\_elem](group__bt__mesh__access.md#ga8edba04af103fb11994d4d3e558ec4fb) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod) |
|  | Get the element that a model belongs to. |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [bt\_mesh\_model\_find](group__bt__mesh__access.md#gaf0510f9511d72f1d4fd07f865753a50a) (const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \*elem, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | Find a SIG model. |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [bt\_mesh\_model\_find\_vnd](group__bt__mesh__access.md#gadfb473db4b23902a192e12d322ff1fd2) (const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \*elem, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | Find a vendor model. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_model\_in\_primary](group__bt__mesh__access.md#gaa8694fdab3f514d8051dad1cc7362ac9) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod) |
|  | Get whether the model is in the primary element of the device. |
| int | [bt\_mesh\_model\_data\_store](group__bt__mesh__access.md#gadff0895c5c34928d778fa615512b3d85) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) vnd, const char \*name, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len) |
|  | Immediately store the model's user data in persistent storage. |
| void | [bt\_mesh\_model\_data\_store\_schedule](group__bt__mesh__access.md#ga762896dd2e806b5be061b220d53ce4db) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod) |
|  | Schedule the model's user data store in persistent storage. |
| int | [bt\_mesh\_model\_extend](group__bt__mesh__access.md#gaf6356f715c8968151b8d539f2dd1880c) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*extending\_mod, const struct [bt\_mesh\_model](structbt__mesh__model.md) \*base\_mod) |
|  | Let a model extend another. |
| int | [bt\_mesh\_model\_correspond](group__bt__mesh__access.md#ga03ce9f6f9ccf734ea72beede09288923) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*corresponding\_mod, const struct [bt\_mesh\_model](structbt__mesh__model.md) \*base\_mod) |
|  | Let a model correspond to another. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_model\_is\_extended](group__bt__mesh__access.md#ga10603a5846210a397f306b227ce10c2e) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Check if model is extended by another model. |
| int | [bt\_mesh\_comp\_change\_prepare](group__bt__mesh__access.md#ga8575f680e77d86d6c85cac27985b9f3c) (void) |
|  | Indicate that the composition data will change on next bootup. |
| int | [bt\_mesh\_models\_metadata\_change\_prepare](group__bt__mesh__access.md#ga26ac86bdd32d27e0091735d98670687a) (void) |
|  | Indicate that the metadata will change on next bootup. |
| int | [bt\_mesh\_comp2\_register](group__bt__mesh__access.md#ga8445c550a47dba16e3fa6fea36d6d9fc) (const struct [bt\_mesh\_comp2](structbt__mesh__comp2.md) \*comp2) |
|  | Register composition data page 2 of the device. |

## Detailed Description

Access layer APIs.

## Macro Definition Documentation

## [◆ ](#a421f6ac3aa620d77033a98f3d059e3ce)BT\_MESH\_ADDR\_UNASSIGNED\_ELT\_

| #define BT\_MESH\_ADDR\_UNASSIGNED\_ELT\_ | ( |  | *IDX*, |
| --- | --- | --- | --- |
|  |  |  | *\_* ) |

**Value:**

[BT\_MESH\_ADDR\_UNASSIGNED](group__bt__mesh__access.md#ga6d11790af686e6d48f08c6f1cd65317c)

[BT\_MESH\_ADDR\_UNASSIGNED](group__bt__mesh__access.md#ga6d11790af686e6d48f08c6f1cd65317c)

#define BT\_MESH\_ADDR\_UNASSIGNED

unassigned

**Definition** access.h:51

## [◆ ](#abe51f11257cf1bbb236e899e7a23acbc)BT\_MESH\_KEY\_UNUSED\_ELT\_

| #define BT\_MESH\_KEY\_UNUSED\_ELT\_ | ( |  | *IDX*, |
| --- | --- | --- | --- |
|  |  |  | *\_* ) |

**Value:**

[BT\_MESH\_KEY\_UNUSED](group__bt__mesh__access.md#gace23095bac3705c2f2afab749e48c02d)

[BT\_MESH\_KEY\_UNUSED](group__bt__mesh__access.md#gace23095bac3705c2f2afab749e48c02d)

#define BT\_MESH\_KEY\_UNUSED

Key unused.

**Definition** access.h:67

## [◆ ](#a6023b10a0b89e067d68e8393155a2945)BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED

| #define BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED | ( |  | *\_grps* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ [LISTIFY](group__sys-util.md#ga81cbc0233cf73048d65b76f716653af6)(\_grps, [BT\_MESH\_ADDR\_UNASSIGNED\_ELT\_](#a421f6ac3aa620d77033a98f3d059e3ce), (,)) }

[BT\_MESH\_ADDR\_UNASSIGNED\_ELT\_](#a421f6ac3aa620d77033a98f3d059e3ce)

#define BT\_MESH\_ADDR\_UNASSIGNED\_ELT\_(IDX, \_)

**Definition** access.h:19

[LISTIFY](group__sys-util.md#ga81cbc0233cf73048d65b76f716653af6)

#define LISTIFY(LEN, F, sep,...)

Generates a sequence of code with configurable separator.

**Definition** util\_macro.h:442

## [◆ ](#a575258fd6073a81b8037b6127f6b975a)BT\_MESH\_MODEL\_KEYS\_UNUSED

| #define BT\_MESH\_MODEL\_KEYS\_UNUSED | ( |  | *\_keys* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ [LISTIFY](group__sys-util.md#ga81cbc0233cf73048d65b76f716653af6)(\_keys, [BT\_MESH\_KEY\_UNUSED\_ELT\_](#abe51f11257cf1bbb236e899e7a23acbc), (,)) }

[BT\_MESH\_KEY\_UNUSED\_ELT\_](#abe51f11257cf1bbb236e899e7a23acbc)

#define BT\_MESH\_KEY\_UNUSED\_ELT\_(IDX, \_)

**Definition** access.h:18

## [◆ ](#ad28c5301ea6cf93f3bf2a672043cae4e)BT\_MESH\_MODEL\_RUNTIME\_INIT

| #define BT\_MESH\_MODEL\_RUNTIME\_INIT | ( |  | *\_user\_data* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

.rt = &(struct bt\_mesh\_model\_rt\_ctx){ .user\_data = (\_user\_data) },

## [◆ ](#abf60c1897454c0cbfa034bc4a3c92843)BT\_MESH\_MODEL\_UUIDS\_UNASSIGNED

| #define BT\_MESH\_MODEL\_UUIDS\_UNASSIGNED | ( |  | ) |  |
| --- | --- | --- | --- | --- |

## [◆ ](#aa5b0403118f5fd434e2ca9c298aee1fd)BT\_MESH\_UUID\_UNASSIGNED\_ELT\_

| #define BT\_MESH\_UUID\_UNASSIGNED\_ELT\_ | ( |  | *IDX*, |
| --- | --- | --- | --- |
|  |  |  | *\_* ) |

**Value:**

NULL

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [access.h](access_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
