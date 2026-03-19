---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__mesh__access.html
original_path: doxygen/html/group__bt__mesh__access.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Access layer

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Access layer.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_elem](structbt__mesh__elem.md) |
|  | Abstraction that describes a Mesh Element. [More...](structbt__mesh__elem.md#details) |
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
| #define | [BT\_MESH\_ADDR\_IS\_UNICAST](#ga1a4694cccf834d71f0abe2a0283cb9a8)(addr) |
|  | Check if a Bluetooth Mesh address is a unicast address. |
| #define | [BT\_MESH\_ADDR\_IS\_GROUP](#gab50cc8dca6f7ffd5420ef4fb38fbe224)(addr) |
|  | Check if a Bluetooth Mesh address is a group address. |
| #define | [BT\_MESH\_ADDR\_IS\_FIXED\_GROUP](#gaff5ff58937924a1e6297aa1b20efc30f)(addr) |
|  | Check if a Bluetooth Mesh address is a fixed group address. |
| #define | [BT\_MESH\_ADDR\_IS\_VIRTUAL](#ga623eb2da2c880eec2107f36402ba6621)(addr) |
|  | Check if a Bluetooth Mesh address is a virtual address. |
| #define | [BT\_MESH\_ADDR\_IS\_RFU](#ga98ba7663259ca43cd5a38c7a9e16516d)(addr) |
|  | Check if a Bluetooth Mesh address is an RFU address. |
| #define | [BT\_MESH\_IS\_DEV\_KEY](#gac4aafa0bdd24fb51d515a62e83917936)(key) |
|  | Check if a Bluetooth Mesh key is a device key. |
| #define | [BT\_MESH\_APP\_SEG\_SDU\_MAX](#gaa620c32d1dce8e4b691b7f4270016506)   12 |
|  | Maximum size of an access message segment (in octets). |
| #define | [BT\_MESH\_APP\_UNSEG\_SDU\_MAX](#ga64eb6a94b1db9899c4f5bbf4cc88cd9f)   15 |
|  | Maximum payload size of an unsegmented access message (in octets). |
| #define | [BT\_MESH\_RX\_SEG\_MAX](#ga18756e939ec3b312eef5c3dc9fd70270)   0 |
|  | Maximum number of segments supported for incoming messages. |
| #define | [BT\_MESH\_TX\_SEG\_MAX](#ga1b2a3610ac370266578abce195e65fa2)   0 |
|  | Maximum number of segments supported for outgoing messages. |
| #define | [BT\_MESH\_TX\_SDU\_MAX](#ga86d7386603ecd89952b6d540ea4243c2) |
|  | Maximum possible payload size of an outgoing access message (in octets). |
| #define | [BT\_MESH\_RX\_SDU\_MAX](#ga36f299f2fc13892b5a7d871dad1ec9ce) |
|  | Maximum possible payload size of an incoming access message (in octets). |
| #define | [BT\_MESH\_ELEM](#ga321a5091dabd4ec4beb5396db6cabf44)(\_loc, \_mods, \_vnd\_mods) |
|  | Helper to define a mesh element within an array. |
| #define | [BT\_MESH\_MODEL\_OP\_1](#ga00915cfdff7dc0646f24d6b06e124d0d)(b0) |
| #define | [BT\_MESH\_MODEL\_OP\_2](#gaa52a40ef5972c4f34cf5ff5a10e21289)(b0, b1) |
| #define | [BT\_MESH\_MODEL\_OP\_3](#ga72d1d19701be52f5eac6af475f9b19a9)(b0, cid) |
| #define | [BT\_MESH\_LEN\_EXACT](#ga637e1be0298dc681414645867b28b59f)(len) |
|  | Macro for encoding exact message length for fixed-length messages. |
| #define | [BT\_MESH\_LEN\_MIN](#ga691ed9b3ab3ddaceda0f81c4a715ab3a)(len) |
|  | Macro for encoding minimum message length for variable-length messages. |
| #define | [BT\_MESH\_MODEL\_OP\_END](#gaf2c164506c601214c85d451747176827)   { 0, 0, NULL } |
|  | End of the opcode list. |
| #define | [BT\_MESH\_MODEL\_NO\_OPS](#gae6d55e0a27bb7c448affd312a2e11656) |
|  | Helper to define an empty opcode list. |
| #define | [BT\_MESH\_MODEL\_NONE](#gab0ad2aab95d49e5b60fe8dafd69132a4)   ((const struct [bt\_mesh\_model](structbt__mesh__model.md) []){}) |
|  | Helper to define an empty model array. |
| #define | [BT\_MESH\_MODEL\_CNT\_CB](#ga925da443eb15a4c1980d48a69388dc2c)(\_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb) |
|  | Composition data SIG model entry with callback functions with specific number of keys & groups. |
| #define | [BT\_MESH\_MODEL\_CNT\_VND\_CB](#ga32733dccd9329aa938dc0bd21cf9beae)(\_company, \_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb) |
|  | Composition data vendor model entry with callback functions with specific number of keys & groups. |
| #define | [BT\_MESH\_MODEL\_CB](#gac062c101b7310020e11a527de9c40d3a)(\_id, \_op, \_pub, \_user\_data, \_cb) |
|  | Composition data SIG model entry with callback functions. |
| #define | [BT\_MESH\_MODEL\_METADATA\_CB](#ga40204b4ccaa819a487de168bcf66c98f)(\_id, \_op, \_pub, \_user\_data, \_cb, \_metadata) |
|  | Composition data SIG model entry with callback functions and metadata. |
| #define | [BT\_MESH\_MODEL\_VND\_CB](#gabe79d914990ba2721f5bb7081910e512)(\_company, \_id, \_op, \_pub, \_user\_data, \_cb) |
|  | Composition data vendor model entry with callback functions. |
| #define | [BT\_MESH\_MODEL\_VND\_METADATA\_CB](#gac62334962dcbe3a75a03ce5744b326d8)(\_company, \_id, \_op, \_pub, \_user\_data, \_cb, \_metadata) |
|  | Composition data vendor model entry with callback functions and metadata. |
| #define | [BT\_MESH\_MODEL](#gae694f5ac7ef9f0de37aaba846443586f)(\_id, \_op, \_pub, \_user\_data) |
|  | Composition data SIG model entry. |
| #define | [BT\_MESH\_MODEL\_VND](#ga3759c8c88db48be662bf2511ff514edd)(\_company, \_id, \_op, \_pub, \_user\_data) |
|  | Composition data vendor model entry. |
| #define | [BT\_MESH\_TRANSMIT](#gaff82bf652232fbce71c31f38a10577a9)(count, int\_ms) |
|  | Encode transmission count & interval steps. |
| #define | [BT\_MESH\_TRANSMIT\_COUNT](#ga62fda0d731241efbaa4827e4eb9d1795)(transmit) |
|  | Decode transmit count from a transmit value. |
| #define | [BT\_MESH\_TRANSMIT\_INT](#ga2aa21171c5677d23ad0c472291639417)(transmit) |
|  | Decode transmit interval from a transmit value. |
| #define | [BT\_MESH\_PUB\_TRANSMIT](#ga19208dea7bab9f31c2c793ef6201dd91)(count, int\_ms) |
|  | Encode Publish Retransmit count & interval steps. |
| #define | [BT\_MESH\_PUB\_TRANSMIT\_COUNT](#ga13986422dda5edce4f5fb1ce387093e3)(transmit) |
|  | Decode Publish Retransmit count from a given value. |
| #define | [BT\_MESH\_PUB\_TRANSMIT\_INT](#gaac954956dd3913dd7ad2b93a2566afd9)(transmit) |
|  | Decode Publish Retransmit interval from a given value. |
| #define | [BT\_MESH\_PUB\_MSG\_TOTAL](#ga230538bb39ac3d6c8c0327d1fad77e69)(pub) |
|  | Get total number of messages within one publication interval including initial publication. |
| #define | [BT\_MESH\_PUB\_MSG\_NUM](#ga115ee29aba3c3e985aa11d6692ca0d83)(pub) |
|  | Get message number within one publication interval. |
| #define | [BT\_MESH\_MODEL\_PUB\_DEFINE](#ga8334ff2da1f0dc3ab2fc914059c33622)(\_name, \_update, \_msg\_len) |
|  | Define a model publication context. |
| #define | [BT\_MESH\_MODELS\_METADATA\_ENTRY](#gaa2587adac719c50c311ae41c548b853c)(\_len, \_id, \_data) |
|  | Initialize a Models Metadata entry structure in a list. |
| #define | [BT\_MESH\_MODELS\_METADATA\_NONE](#ga56b518123ab47cb3ae4a249f471ae556)   NULL |
|  | Helper to define an empty Models metadata array. |
| #define | [BT\_MESH\_MODELS\_METADATA\_END](#gaab5fe51071f6e54debd9136ac6a70a49)   { 0, 0, NULL } |
|  | End of the Models Metadata list. |
| #define | [BT\_MESH\_TTL\_DEFAULT](#ga16516272b42420263b1c47c3ea16c0c8)   0xff |
|  | Special TTL value to request using configured default TTL. |
| #define | [BT\_MESH\_TTL\_MAX](#ga071e85e929589d31bf876e2e09cf2f19)   0x7f |
|  | Maximum allowed TTL value. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_model\_send](#ga7cac052ef76f4b37a95343329b078e77) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model, struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, struct [net\_buf\_simple](structnet__buf__simple.md) \*msg, const struct [bt\_mesh\_send\_cb](structbt__mesh__send__cb.md) \*cb, void \*cb\_data) |
|  | Send an Access Layer message. |
| int | [bt\_mesh\_model\_publish](#ga06644f8a5fa43351328d3f3403dbad03) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Send a model publication message. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_model\_pub\_is\_retransmission](#ga1b961d45f8b7c231c698ca229115e434) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Check if a message is being retransmitted. |
| const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \* | [bt\_mesh\_model\_elem](#ga8edba04af103fb11994d4d3e558ec4fb) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod) |
|  | Get the element that a model belongs to. |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [bt\_mesh\_model\_find](#gaf0510f9511d72f1d4fd07f865753a50a) (const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \*elem, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | Find a SIG model. |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [bt\_mesh\_model\_find\_vnd](#gadfb473db4b23902a192e12d322ff1fd2) (const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \*elem, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) company, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | Find a vendor model. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_model\_in\_primary](#gaa8694fdab3f514d8051dad1cc7362ac9) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod) |
|  | Get whether the model is in the primary element of the device. |
| int | [bt\_mesh\_model\_data\_store](#gadff0895c5c34928d778fa615512b3d85) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) vnd, const char \*name, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len) |
|  | Immediately store the model's user data in persistent storage. |
| void | [bt\_mesh\_model\_data\_store\_schedule](#ga762896dd2e806b5be061b220d53ce4db) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*mod) |
|  | Schedule the model's user data store in persistent storage. |
| int | [bt\_mesh\_model\_extend](#gaf6356f715c8968151b8d539f2dd1880c) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*extending\_mod, const struct [bt\_mesh\_model](structbt__mesh__model.md) \*base\_mod) |
|  | Let a model extend another. |
| int | [bt\_mesh\_model\_correspond](#ga03ce9f6f9ccf734ea72beede09288923) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*corresponding\_mod, const struct [bt\_mesh\_model](structbt__mesh__model.md) \*base\_mod) |
|  | Let a model correspond to another. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_model\_is\_extended](#ga10603a5846210a397f306b227ce10c2e) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model) |
|  | Check if model is extended by another model. |
| int | [bt\_mesh\_comp\_change\_prepare](#ga8575f680e77d86d6c85cac27985b9f3c) (void) |
|  | Indicate that the composition data will change on next bootup. |
| int | [bt\_mesh\_models\_metadata\_change\_prepare](#ga26ac86bdd32d27e0091735d98670687a) (void) |
|  | Indicate that the metadata will change on next bootup. |
| int | [bt\_mesh\_comp2\_register](#ga8445c550a47dba16e3fa6fea36d6d9fc) (const struct [bt\_mesh\_comp2](structbt__mesh__comp2.md) \*comp2) |
|  | Register composition data page 2 of the device. |

| Group addresses | |
| --- | --- |
| #define | [BT\_MESH\_ADDR\_UNASSIGNED](#ga6d11790af686e6d48f08c6f1cd65317c)   0x0000 |
|  | unassigned |
| #define | [BT\_MESH\_ADDR\_ALL\_NODES](#ga27aafd100b6ccc1de060a75370184620)   0xffff |
|  | all-nodes |
| #define | [BT\_MESH\_ADDR\_RELAYS](#ga5ee81d48846de9c9c966ffe0b90ff011)   0xfffe |
|  | all-relays |
| #define | [BT\_MESH\_ADDR\_FRIENDS](#ga5d44892368bb7c1ecd205a81e66bd6f7)   0xfffd |
|  | all-friends |
| #define | [BT\_MESH\_ADDR\_PROXIES](#ga30d4975d25c2c120da1cbfadf29c098f)   0xfffc |
|  | all-proxies |
| #define | [BT\_MESH\_ADDR\_DFW\_NODES](#gabf77d8365ddc278838fa450826e43243)   0xfffb |
|  | all-directed-forwarding-nodes |
| #define | [BT\_MESH\_ADDR\_IP\_NODES](#gafd70174e5072dbbfed31156f152aeaa1)   0xfffa |
|  | all-ipt-nodes |
| #define | [BT\_MESH\_ADDR\_IP\_BR\_ROUTERS](#ga1055381438e55e953dec2e6d592ab103)   0xfff9 |
|  | all-ipt-border-routers |

| Predefined key indexes | |
| --- | --- |
| #define | [BT\_MESH\_KEY\_UNUSED](#gace23095bac3705c2f2afab749e48c02d)   0xffff |
|  | Key unused. |
| #define | [BT\_MESH\_KEY\_ANY](#ga7718cce0713be98a08420c7eab1b40ee)   0xffff |
|  | Any key index. |
| #define | [BT\_MESH\_KEY\_DEV](#gabd37f17f3f5c3bc399ad3699df282675)   0xfffe |
|  | Device key. |
| #define | [BT\_MESH\_KEY\_DEV\_LOCAL](#ga9c64b38f2a6879f4750e3e1828e8ab7a)   [BT\_MESH\_KEY\_DEV](#gabd37f17f3f5c3bc399ad3699df282675) |
|  | Local device key. |
| #define | [BT\_MESH\_KEY\_DEV\_REMOTE](#gaaa6ffb62df5d6d55c831d4d9860fc7eb)   0xfffd |
|  | Remote device key. |
| #define | [BT\_MESH\_KEY\_DEV\_ANY](#gace0a526534e31e8067daf283407533fd)   0xfffc |
|  | Any device key. |

| Foundation Models | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_ID\_CFG\_SRV](#ga004d8d1be55b2aec56abbeeca1d118d8)   0x0000 |
|  | Configuration Server. |
| #define | [BT\_MESH\_MODEL\_ID\_CFG\_CLI](#ga3f8442dcd1a110ea0d0023f50057139f)   0x0001 |
|  | Configuration Client. |
| #define | [BT\_MESH\_MODEL\_ID\_HEALTH\_SRV](#ga6416216348d7186f91175ca50bb8c903)   0x0002 |
|  | Health Server. |
| #define | [BT\_MESH\_MODEL\_ID\_HEALTH\_CLI](#gab58b85b7a77feeb579973177c12bb446)   0x0003 |
|  | Health Client. |
| #define | [BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_SRV](#ga9c7d1c5dfb87a5ce50c08747af47414f)   0x0004 |
|  | Remote Provisioning Server. |
| #define | [BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_CLI](#gaf373eb4d8af5d6bee76a821bd4d5e48c)   0x0005 |
|  | Remote Provisioning Client. |
| #define | [BT\_MESH\_MODEL\_ID\_BRG\_CFG\_SRV](#ga599d00e9d63ade6ed1a6803579c1e16e)   0x0008 |
|  | Bridge Configuration Sever. |
| #define | [BT\_MESH\_MODEL\_ID\_BRG\_CFG\_CLI](#ga9c776b4befd21c15f4867d906f631257)   0x0009 |
|  | Bridge Configuration Client. |
| #define | [BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_SRV](#gacca0e355982935cfbde46a06b09a7bec)   0x000a |
|  | Private Beacon Server. |
| #define | [BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_CLI](#gab3b21cbee4e11319a6e0ba3b02b24a91)   0x000b |
|  | Private Beacon Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SAR\_CFG\_SRV](#ga1e9d8be1d2e65d2977aea0306b015258)   0x000e |
|  | SAR Configuration Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SAR\_CFG\_CLI](#gaf214eb7eef3530919432b62ff9b353c3)   0x000f |
|  | SAR Configuration Client. |
| #define | [BT\_MESH\_MODEL\_ID\_OP\_AGG\_SRV](#ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a)   0x0010 |
|  | Opcodes Aggregator Server. |
| #define | [BT\_MESH\_MODEL\_ID\_OP\_AGG\_CLI](#gabac62a77e7d2d7677af21c33c8629187)   0x0011 |
|  | Opcodes Aggregator Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_SRV](#gaec3abd6a0bd7b07a71fe5ed6a7a6931a)   0x0012 |
|  | Large Composition Data Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_CLI](#ga729d67e4183457932e4c837d65abd842)   0x0013 |
|  | Large Composition Data Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_SRV](#ga165bc198dadaa0d534ec82eb8192ebc0)   0x0014 |
|  | Solicitation PDU RPL Configuration Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_CLI](#ga6e747dd364bcfaa368e37c5f01afd530)   0x0015 |
|  | Solicitation PDU RPL Configuration Server. |
| #define | [BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_SRV](#gaddc0bd645180a57cb9cd36745b84f7a1)   0x000c |
|  | Private Proxy Server. |
| #define | [BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_CLI](#gadd36546fb2cb6d1c731f7ae7674af6a7)   0x000d |
|  | Private Proxy Client. |

| Models from the Mesh Model Specification | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_SRV](#ga83e1ed5398d513cfeb900e41655aa4d8)   0x1000 |
|  | Generic OnOff Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_CLI](#ga4f0eee2569b518a5e4250f5b7b294fed)   0x1001 |
|  | Generic OnOff Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_SRV](#ga7f10a8332b1406c3ad628b9679e1d7cb)   0x1002 |
|  | Generic Level Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_CLI](#ga462c578845a17b20cdb3e008f74f93a6)   0x1003 |
|  | Generic Level Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_SRV](#ga004d5ec0870d47a8d37182e5b0c089a5)   0x1004 |
|  | Generic Default Transition Time Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_CLI](#gafa1c6a7d857fe13a139ce2242b4e62f5)   0x1005 |
|  | Generic Default Transition Time Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SRV](#ga09ac731fff09146ec68557f00e8294e0)   0x1006 |
|  | Generic Power OnOff Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SETUP\_SRV](#ga2a6dad18792ba7f1d81d6c9a1c65f90a)   0x1007 |
|  | Generic Power OnOff Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_CLI](#ga9f6544f7b87f39d0792ea2de13cd45f1)   0x1008 |
|  | Generic Power OnOff Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SRV](#gadd30afe63f89e9c1778e56f722fd82f9)   0x1009 |
|  | Generic Power Level Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SETUP\_SRV](#ga1ff6ec64ce3a86d1cfd00fc98e89c0a5)   0x100a |
|  | Generic Power Level Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_CLI](#ga8420454c35afc12c62ede55942f3b6d3)   0x100b |
|  | Generic Power Level Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_SRV](#gacf891135f54fb1fbb62beb812235619e)   0x100c |
|  | Generic Battery Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_CLI](#ga34bb3d4839e9685ec55f8285aac9a79f)   0x100d |
|  | Generic Battery Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SRV](#gad516f513c5c942fbfee65b85332b105e)   0x100e |
|  | Generic Location Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SETUPSRV](#ga240d1ed34b7341627773cce862f85620)   0x100f |
|  | Generic Location Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_CLI](#ga8fa01ddb1f4de4d61500bb650243390d)   0x1010 |
|  | Generic Location Client. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_ADMIN\_PROP\_SRV](#ga3cc6862e9c72f9282055c5cda2343c89)   0x1011 |
|  | Generic Admin Property Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_MANUFACTURER\_PROP\_SRV](#ga32e09ddfebd2e8b22da9a3102e116aae)   0x1012 |
|  | Generic Manufacturer Property Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_USER\_PROP\_SRV](#ga4b7b6a4b47e87de94ccf11ef1abd64b9)   0x1013 |
|  | Generic User Property Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_CLIENT\_PROP\_SRV](#ga20906658018ef26114d8a6656c258f62)   0x1014 |
|  | Generic Client Property Server. |
| #define | [BT\_MESH\_MODEL\_ID\_GEN\_PROP\_CLI](#ga69455e5b1e6def3d909c4bb6e0dee9ae)   0x1015 |
|  | Generic Property Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SENSOR\_SRV](#ga3e0dcb14f46f6076e5b1b114b977f630)   0x1100 |
|  | Sensor Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SENSOR\_SETUP\_SRV](#gad10780bfc1c16866fa28de750e56bec3)   0x1101 |
|  | Sensor Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SENSOR\_CLI](#ga8f1e4ff66d388627dbe91b2f8d4ed358)   0x1102 |
|  | Sensor Client. |
| #define | [BT\_MESH\_MODEL\_ID\_TIME\_SRV](#ga93fbf1c661a75d70fdbd2a599353eb94)   0x1200 |
|  | Time Server. |
| #define | [BT\_MESH\_MODEL\_ID\_TIME\_SETUP\_SRV](#ga2725121dc8c2c21c0ee469fe4348f45f)   0x1201 |
|  | Time Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_TIME\_CLI](#ga500df90af7989794c5d72e760e5e65c6)   0x1202 |
|  | Time Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SCENE\_SRV](#gaaa5554e3d48ae101596476e6bd6caf67)   0x1203 |
|  | Scene Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SCENE\_SETUP\_SRV](#gaa3b08fc8788684abb960fa3516726264)   0x1204 |
|  | Scene Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SCENE\_CLI](#gad60472aa004a8a913aeb63ef62c45857)   0x1205 |
|  | Scene Client. |
| #define | [BT\_MESH\_MODEL\_ID\_SCHEDULER\_SRV](#ga82b723752e240f22b9bcc8dc3dd10eb9)   0x1206 |
|  | Scheduler Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SCHEDULER\_SETUP\_SRV](#ga3dbec5a3b82cb25a142c4bc851e3fe0e)   0x1207 |
|  | Scheduler Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_SCHEDULER\_CLI](#gac743b26cf7e746b16302c25e8cd56221)   0x1208 |
|  | Scheduler Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SRV](#ga16df49e84e84d0ae4a6ab5d5f3f1b2b6)   0x1300 |
|  | Light Lightness Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SETUP\_SRV](#gadb93b2ed2256a5c9c3f66237841b1bf5)   0x1301 |
|  | Light Lightness Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_CLI](#ga960055723dec7b3b366efa7c49cafc2e)   0x1302 |
|  | Light Lightness Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SRV](#gaa9a211341c5b3283b9b0e0842adef053)   0x1303 |
|  | Light CTL Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SETUP\_SRV](#ga28ac69b2dbeec70bae4bd3c0381e9e93)   0x1304 |
|  | Light CTL Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_CLI](#ga58fc8d99b746b0061177ac5d95341da1)   0x1305 |
|  | Light CTL Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_TEMP\_SRV](#gafcb1f1ea20bb78b78a9ead4bfdbe3e47)   0x1306 |
|  | Light CTL Temperature Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SRV](#gaa0ddc753a226060d014dcd368feab17e)   0x1307 |
|  | Light HSL Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SETUP\_SRV](#ga574d3ba3f629bdbffc8f15db931a263a)   0x1308 |
|  | Light HSL Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_CLI](#ga2d111a352322be8e33ba0cba0feb3f0c)   0x1309 |
|  | Light HSL Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_HUE\_SRV](#ga865952346db9336a255c71bcb5f09774)   0x130a |
|  | Light HSL Hue Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SAT\_SRV](#gae55004e70670a8711e18e9c9b3428720)   0x130b |
|  | Light HSL Saturation Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SRV](#ga29e1a90f166d88b6773d9b7ccf08e1c7)   0x130c |
|  | Light xyL Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SETUP\_SRV](#ga4addae460d6b3c0a914198695b3e31ea)   0x130d |
|  | Light xyL Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_CLI](#ga0ca4d9997e6016b5c27f42549d42a99d)   0x130e |
|  | Light xyL Client. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SRV](#ga789412252034939539ba45e4bf21e3e2)   0x130f |
|  | Light LC Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SETUPSRV](#ga436358740bb64d845aa4d849d462a12e)   0x1310 |
|  | Light LC Setup Server. |
| #define | [BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_CLI](#gaadd48b07e1eb53df24df40b7ea412e90)   0x1311 |
|  | Light LC Client. |

| Models from the Mesh Binary Large Object Transfer Model Specification | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_ID\_BLOB\_SRV](#gae85d4cf7aad4e94582c24f79d6f60904)   0x1400 |
|  | BLOB Transfer Server. |
| #define | [BT\_MESH\_MODEL\_ID\_BLOB\_CLI](#ga17e2e59a1344e623fe9fec6e27b7f22e)   0x1401 |
|  | BLOB Transfer Client. |

| Models from the Mesh Device Firmware Update Model Specification | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_ID\_DFU\_SRV](#ga0215c2c8cd16ab6536ea243864f9604e)   0x1402 |
|  | Firmware Update Server. |
| #define | [BT\_MESH\_MODEL\_ID\_DFU\_CLI](#gaf477a37238ec577000a646af40862ee1)   0x1403 |
|  | Firmware Update Client. |
| #define | [BT\_MESH\_MODEL\_ID\_DFD\_SRV](#gaf4309dea32d05274f8f3a6ea45faba38)   0x1404 |
|  | Firmware Distribution Server. |
| #define | [BT\_MESH\_MODEL\_ID\_DFD\_CLI](#ga87d3b5cc207dc3b51e85c9594bb98cad)   0x1405 |
|  | Firmware Distribution Client. |

## Detailed Description

Access layer.

## Macro Definition Documentation

## [◆ ](#ga27aafd100b6ccc1de060a75370184620)BT\_MESH\_ADDR\_ALL\_NODES

| #define BT\_MESH\_ADDR\_ALL\_NODES   0xffff |
| --- |

`#include <[access.h](access_8h.md)>`

all-nodes

## [◆ ](#gabf77d8365ddc278838fa450826e43243)BT\_MESH\_ADDR\_DFW\_NODES

| #define BT\_MESH\_ADDR\_DFW\_NODES   0xfffb |
| --- |

`#include <[access.h](access_8h.md)>`

all-directed-forwarding-nodes

## [◆ ](#ga5d44892368bb7c1ecd205a81e66bd6f7)BT\_MESH\_ADDR\_FRIENDS

| #define BT\_MESH\_ADDR\_FRIENDS   0xfffd |
| --- |

`#include <[access.h](access_8h.md)>`

all-friends

## [◆ ](#ga1055381438e55e953dec2e6d592ab103)BT\_MESH\_ADDR\_IP\_BR\_ROUTERS

| #define BT\_MESH\_ADDR\_IP\_BR\_ROUTERS   0xfff9 |
| --- |

`#include <[access.h](access_8h.md)>`

all-ipt-border-routers

## [◆ ](#gafd70174e5072dbbfed31156f152aeaa1)BT\_MESH\_ADDR\_IP\_NODES

| #define BT\_MESH\_ADDR\_IP\_NODES   0xfffa |
| --- |

`#include <[access.h](access_8h.md)>`

all-ipt-nodes

## [◆ ](#gaff5ff58937924a1e6297aa1b20efc30f)BT\_MESH\_ADDR\_IS\_FIXED\_GROUP

| #define BT\_MESH\_ADDR\_IS\_FIXED\_GROUP | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

((addr) >= 0xff00 && (addr) < 0xffff)

Check if a Bluetooth Mesh address is a fixed group address.

## [◆ ](#gab50cc8dca6f7ffd5420ef4fb38fbe224)BT\_MESH\_ADDR\_IS\_GROUP

| #define BT\_MESH\_ADDR\_IS\_GROUP | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

((addr) >= 0xc000 && (addr) < 0xff00)

Check if a Bluetooth Mesh address is a group address.

## [◆ ](#ga98ba7663259ca43cd5a38c7a9e16516d)BT\_MESH\_ADDR\_IS\_RFU

| #define BT\_MESH\_ADDR\_IS\_RFU | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

((addr) >= 0xff00 && (addr) <= 0xfff8)

Check if a Bluetooth Mesh address is an RFU address.

## [◆ ](#ga1a4694cccf834d71f0abe2a0283cb9a8)BT\_MESH\_ADDR\_IS\_UNICAST

| #define BT\_MESH\_ADDR\_IS\_UNICAST | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

((addr) && (addr) < 0x8000)

Check if a Bluetooth Mesh address is a unicast address.

## [◆ ](#ga623eb2da2c880eec2107f36402ba6621)BT\_MESH\_ADDR\_IS\_VIRTUAL

| #define BT\_MESH\_ADDR\_IS\_VIRTUAL | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

((addr) >= 0x8000 && (addr) < 0xc000)

Check if a Bluetooth Mesh address is a virtual address.

## [◆ ](#ga30d4975d25c2c120da1cbfadf29c098f)BT\_MESH\_ADDR\_PROXIES

| #define BT\_MESH\_ADDR\_PROXIES   0xfffc |
| --- |

`#include <[access.h](access_8h.md)>`

all-proxies

## [◆ ](#ga5ee81d48846de9c9c966ffe0b90ff011)BT\_MESH\_ADDR\_RELAYS

| #define BT\_MESH\_ADDR\_RELAYS   0xfffe |
| --- |

`#include <[access.h](access_8h.md)>`

all-relays

## [◆ ](#ga6d11790af686e6d48f08c6f1cd65317c)BT\_MESH\_ADDR\_UNASSIGNED

| #define BT\_MESH\_ADDR\_UNASSIGNED   0x0000 |
| --- |

`#include <[access.h](access_8h.md)>`

unassigned

## [◆ ](#gaa620c32d1dce8e4b691b7f4270016506)BT\_MESH\_APP\_SEG\_SDU\_MAX

| #define BT\_MESH\_APP\_SEG\_SDU\_MAX   12 |
| --- |

`#include <[access.h](access_8h.md)>`

Maximum size of an access message segment (in octets).

## [◆ ](#ga64eb6a94b1db9899c4f5bbf4cc88cd9f)BT\_MESH\_APP\_UNSEG\_SDU\_MAX

| #define BT\_MESH\_APP\_UNSEG\_SDU\_MAX   15 |
| --- |

`#include <[access.h](access_8h.md)>`

Maximum payload size of an unsegmented access message (in octets).

## [◆ ](#ga321a5091dabd4ec4beb5396db6cabf44)BT\_MESH\_ELEM

| #define BT\_MESH\_ELEM | ( |  | *\_loc*, |
| --- | --- | --- | --- |
|  |  |  | *\_mods*, |
|  |  |  | *\_vnd\_mods* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

{ \

.rt = &(struct bt\_mesh\_elem\_rt\_ctx) { 0 }, \

.loc = (\_loc), \

.model\_count = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_mods), \

.vnd\_model\_count = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_vnd\_mods), \

.models = (\_mods), \

.vnd\_models = (\_vnd\_mods), \

}

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:120

Helper to define a mesh element within an array.

In case the element has no SIG or Vendor models the helper macro BT\_MESH\_MODEL\_NONE can be given instead.

Parameters
:   | \_loc | Location Descriptor. |
    | --- | --- |
    | \_mods | Array of models. |
    | \_vnd\_mods | Array of vendor models. |

## [◆ ](#gac4aafa0bdd24fb51d515a62e83917936)BT\_MESH\_IS\_DEV\_KEY

| #define BT\_MESH\_IS\_DEV\_KEY | ( |  | *key* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

(key == [BT\_MESH\_KEY\_DEV\_LOCAL](#ga9c64b38f2a6879f4750e3e1828e8ab7a) || \

key == [BT\_MESH\_KEY\_DEV\_REMOTE](#gaaa6ffb62df5d6d55c831d4d9860fc7eb))

[BT\_MESH\_KEY\_DEV\_LOCAL](#ga9c64b38f2a6879f4750e3e1828e8ab7a)

#define BT\_MESH\_KEY\_DEV\_LOCAL

Local device key.

**Definition** access.h:70

[BT\_MESH\_KEY\_DEV\_REMOTE](#gaaa6ffb62df5d6d55c831d4d9860fc7eb)

#define BT\_MESH\_KEY\_DEV\_REMOTE

Remote device key.

**Definition** access.h:71

Check if a Bluetooth Mesh key is a device key.

## [◆ ](#ga7718cce0713be98a08420c7eab1b40ee)BT\_MESH\_KEY\_ANY

| #define BT\_MESH\_KEY\_ANY   0xffff |
| --- |

`#include <[access.h](access_8h.md)>`

Any key index.

## [◆ ](#gabd37f17f3f5c3bc399ad3699df282675)BT\_MESH\_KEY\_DEV

| #define BT\_MESH\_KEY\_DEV   0xfffe |
| --- |

`#include <[access.h](access_8h.md)>`

Device key.

## [◆ ](#gace0a526534e31e8067daf283407533fd)BT\_MESH\_KEY\_DEV\_ANY

| #define BT\_MESH\_KEY\_DEV\_ANY   0xfffc |
| --- |

`#include <[access.h](access_8h.md)>`

Any device key.

## [◆ ](#ga9c64b38f2a6879f4750e3e1828e8ab7a)BT\_MESH\_KEY\_DEV\_LOCAL

| #define BT\_MESH\_KEY\_DEV\_LOCAL   [BT\_MESH\_KEY\_DEV](#gabd37f17f3f5c3bc399ad3699df282675) |
| --- |

`#include <[access.h](access_8h.md)>`

Local device key.

## [◆ ](#gaaa6ffb62df5d6d55c831d4d9860fc7eb)BT\_MESH\_KEY\_DEV\_REMOTE

| #define BT\_MESH\_KEY\_DEV\_REMOTE   0xfffd |
| --- |

`#include <[access.h](access_8h.md)>`

Remote device key.

## [◆ ](#gace23095bac3705c2f2afab749e48c02d)BT\_MESH\_KEY\_UNUSED

| #define BT\_MESH\_KEY\_UNUSED   0xffff |
| --- |

`#include <[access.h](access_8h.md)>`

Key unused.

## [◆ ](#ga637e1be0298dc681414645867b28b59f)BT\_MESH\_LEN\_EXACT

| #define BT\_MESH\_LEN\_EXACT | ( |  | *len* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

(-len)

Macro for encoding exact message length for fixed-length messages.

## [◆ ](#ga691ed9b3ab3ddaceda0f81c4a715ab3a)BT\_MESH\_LEN\_MIN

| #define BT\_MESH\_LEN\_MIN | ( |  | *len* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

(len)

Macro for encoding minimum message length for variable-length messages.

## [◆ ](#gae694f5ac7ef9f0de37aaba846443586f)BT\_MESH\_MODEL

| #define BT\_MESH\_MODEL | ( |  | *\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_op*, |
|  |  |  | *\_pub*, |
|  |  |  | *\_user\_data* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](#gac062c101b7310020e11a527de9c40d3a)(\_id, \_op, \_pub, \_user\_data, NULL)

[BT\_MESH\_MODEL\_CB](#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:495

Composition data SIG model entry.

This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

Parameters
:   | \_id | Model ID. |
    | --- | --- |
    | \_op | Array of model opcode handlers. |
    | \_pub | Model publish parameters. |
    | \_user\_data | User data for the model. |

## [◆ ](#gac062c101b7310020e11a527de9c40d3a)BT\_MESH\_MODEL\_CB

| #define BT\_MESH\_MODEL\_CB | ( |  | *\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_op*, |
|  |  |  | *\_pub*, |
|  |  |  | *\_user\_data*, |
|  |  |  | *\_cb* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CNT\_CB](#ga925da443eb15a4c1980d48a69388dc2c)(\_id, \_op, \_pub, \_user\_data, \

CONFIG\_BT\_MESH\_MODEL\_KEY\_COUNT, \

CONFIG\_BT\_MESH\_MODEL\_GROUP\_COUNT, \_cb)

[BT\_MESH\_MODEL\_CNT\_CB](#ga925da443eb15a4c1980d48a69388dc2c)

#define BT\_MESH\_MODEL\_CNT\_CB(\_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb)

Composition data SIG model entry with callback functions with specific number of keys & groups.

**Definition** access.h:436

Composition data SIG model entry with callback functions.

This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

Parameters
:   | \_id | Model ID. |
    | --- | --- |
    | \_op | Array of model opcode handlers. |
    | \_pub | Model publish parameters. |
    | \_user\_data | User data for the model. |
    | \_cb | Callback structure, or NULL to keep no callbacks. |

## [◆ ](#ga925da443eb15a4c1980d48a69388dc2c)BT\_MESH\_MODEL\_CNT\_CB

| #define BT\_MESH\_MODEL\_CNT\_CB | ( |  | *\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_op*, |
|  |  |  | *\_pub*, |
|  |  |  | *\_user\_data*, |
|  |  |  | *\_keys*, |
|  |  |  | *\_grps*, |
|  |  |  | *\_cb* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

{ \

.id = (\_id), \

[BT\_MESH\_MODEL\_RUNTIME\_INIT](access_8h.md#ad28c5301ea6cf93f3bf2a672043cae4e)(\_user\_data) \

.pub = \_pub, \

.keys = ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) []) [BT\_MESH\_MODEL\_KEYS\_UNUSED](access_8h.md#a575258fd6073a81b8037b6127f6b975a)(\_keys), \

.keys\_cnt = \_keys, \

.groups = ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) []) [BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED](access_8h.md#a6023b10a0b89e067d68e8393155a2945)(\_grps), \

.groups\_cnt = \_grps, \

BT\_MESH\_MODEL\_UUIDS\_UNASSIGNED() \

.op = \_op, \

.cb = \_cb, \

}

[BT\_MESH\_MODEL\_KEYS\_UNUSED](access_8h.md#a575258fd6073a81b8037b6127f6b975a)

#define BT\_MESH\_MODEL\_KEYS\_UNUSED(\_keys)

**Definition** access.h:21

[BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED](access_8h.md#a6023b10a0b89e067d68e8393155a2945)

#define BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED(\_grps)

**Definition** access.h:23

[BT\_MESH\_MODEL\_RUNTIME\_INIT](access_8h.md#ad28c5301ea6cf93f3bf2a672043cae4e)

#define BT\_MESH\_MODEL\_RUNTIME\_INIT(\_user\_data)

**Definition** access.h:33

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

Composition data SIG model entry with callback functions with specific number of keys & groups.

This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

Parameters
:   | \_id | Model ID. |
    | --- | --- |
    | \_op | Array of model opcode handlers. |
    | \_pub | Model publish parameters. |
    | \_user\_data | User data for the model. |
    | \_keys | Number of keys that can be bound to the model. Shall not exceed  ``` CONFIG_BT_MESH_MODEL_KEY_COUNT ```  . |
    | \_grps | Number of addresses that the model can be subscribed to. Shall not exceed  ``` CONFIG_BT_MESH_MODEL_GROUP_COUNT ```  . |
    | \_cb | Callback structure, or NULL to keep no callbacks. |

## [◆ ](#ga32733dccd9329aa938dc0bd21cf9beae)BT\_MESH\_MODEL\_CNT\_VND\_CB

| #define BT\_MESH\_MODEL\_CNT\_VND\_CB | ( |  | *\_company*, |
| --- | --- | --- | --- |
|  |  |  | *\_id*, |
|  |  |  | *\_op*, |
|  |  |  | *\_pub*, |
|  |  |  | *\_user\_data*, |
|  |  |  | *\_keys*, |
|  |  |  | *\_grps*, |
|  |  |  | *\_cb* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

{ \

.vnd.company = (\_company), \

.vnd.id = (\_id), \

BT\_MESH\_MODEL\_RUNTIME\_INIT(\_user\_data) \

.op = \_op, \

.pub = \_pub, \

.keys = ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) []) [BT\_MESH\_MODEL\_KEYS\_UNUSED](access_8h.md#a575258fd6073a81b8037b6127f6b975a)(\_keys), \

.keys\_cnt = \_keys, \

.groups = ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) []) [BT\_MESH\_MODEL\_GROUPS\_UNASSIGNED](access_8h.md#a6023b10a0b89e067d68e8393155a2945)(\_grps), \

.groups\_cnt = \_grps, \

BT\_MESH\_MODEL\_UUIDS\_UNASSIGNED() \

.cb = \_cb, \

}

Composition data vendor model entry with callback functions with specific number of keys & groups.

This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

Parameters
:   | \_company | Company ID. |
    | --- | --- |
    | \_id | Model ID. |
    | \_op | Array of model opcode handlers. |
    | \_pub | Model publish parameters. |
    | \_user\_data | User data for the model. |
    | \_keys | Number of keys that can be bound to the model. Shall not exceed  ``` CONFIG_BT_MESH_MODEL_KEY_COUNT ```  . |
    | \_grps | Number of addresses that the model can be subscribed to. Shall not exceed  ``` CONFIG_BT_MESH_MODEL_GROUP_COUNT ```  . |
    | \_cb | Callback structure, or NULL to keep no callbacks. |

## [◆ ](#ga17e2e59a1344e623fe9fec6e27b7f22e)BT\_MESH\_MODEL\_ID\_BLOB\_CLI

| #define BT\_MESH\_MODEL\_ID\_BLOB\_CLI   0x1401 |
| --- |

`#include <[access.h](access_8h.md)>`

BLOB Transfer Client.

## [◆ ](#gae85d4cf7aad4e94582c24f79d6f60904)BT\_MESH\_MODEL\_ID\_BLOB\_SRV

| #define BT\_MESH\_MODEL\_ID\_BLOB\_SRV   0x1400 |
| --- |

`#include <[access.h](access_8h.md)>`

BLOB Transfer Server.

## [◆ ](#ga9c776b4befd21c15f4867d906f631257)BT\_MESH\_MODEL\_ID\_BRG\_CFG\_CLI

| #define BT\_MESH\_MODEL\_ID\_BRG\_CFG\_CLI   0x0009 |
| --- |

`#include <[access.h](access_8h.md)>`

Bridge Configuration Client.

## [◆ ](#ga599d00e9d63ade6ed1a6803579c1e16e)BT\_MESH\_MODEL\_ID\_BRG\_CFG\_SRV

| #define BT\_MESH\_MODEL\_ID\_BRG\_CFG\_SRV   0x0008 |
| --- |

`#include <[access.h](access_8h.md)>`

Bridge Configuration Sever.

## [◆ ](#ga3f8442dcd1a110ea0d0023f50057139f)BT\_MESH\_MODEL\_ID\_CFG\_CLI

| #define BT\_MESH\_MODEL\_ID\_CFG\_CLI   0x0001 |
| --- |

`#include <[access.h](access_8h.md)>`

Configuration Client.

## [◆ ](#ga004d8d1be55b2aec56abbeeca1d118d8)BT\_MESH\_MODEL\_ID\_CFG\_SRV

| #define BT\_MESH\_MODEL\_ID\_CFG\_SRV   0x0000 |
| --- |

`#include <[access.h](access_8h.md)>`

Configuration Server.

## [◆ ](#ga87d3b5cc207dc3b51e85c9594bb98cad)BT\_MESH\_MODEL\_ID\_DFD\_CLI

| #define BT\_MESH\_MODEL\_ID\_DFD\_CLI   0x1405 |
| --- |

`#include <[access.h](access_8h.md)>`

Firmware Distribution Client.

## [◆ ](#gaf4309dea32d05274f8f3a6ea45faba38)BT\_MESH\_MODEL\_ID\_DFD\_SRV

| #define BT\_MESH\_MODEL\_ID\_DFD\_SRV   0x1404 |
| --- |

`#include <[access.h](access_8h.md)>`

Firmware Distribution Server.

## [◆ ](#gaf477a37238ec577000a646af40862ee1)BT\_MESH\_MODEL\_ID\_DFU\_CLI

| #define BT\_MESH\_MODEL\_ID\_DFU\_CLI   0x1403 |
| --- |

`#include <[access.h](access_8h.md)>`

Firmware Update Client.

## [◆ ](#ga0215c2c8cd16ab6536ea243864f9604e)BT\_MESH\_MODEL\_ID\_DFU\_SRV

| #define BT\_MESH\_MODEL\_ID\_DFU\_SRV   0x1402 |
| --- |

`#include <[access.h](access_8h.md)>`

Firmware Update Server.

## [◆ ](#ga3cc6862e9c72f9282055c5cda2343c89)BT\_MESH\_MODEL\_ID\_GEN\_ADMIN\_PROP\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_ADMIN\_PROP\_SRV   0x1011 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Admin Property Server.

## [◆ ](#ga34bb3d4839e9685ec55f8285aac9a79f)BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_CLI

| #define BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_CLI   0x100d |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Battery Client.

## [◆ ](#gacf891135f54fb1fbb62beb812235619e)BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_BATTERY\_SRV   0x100c |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Battery Server.

## [◆ ](#ga20906658018ef26114d8a6656c258f62)BT\_MESH\_MODEL\_ID\_GEN\_CLIENT\_PROP\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_CLIENT\_PROP\_SRV   0x1014 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Client Property Server.

## [◆ ](#gafa1c6a7d857fe13a139ce2242b4e62f5)BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_CLI

| #define BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_CLI   0x1005 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Default Transition Time Client.

## [◆ ](#ga004d5ec0870d47a8d37182e5b0c089a5)BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_DEF\_TRANS\_TIME\_SRV   0x1004 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Default Transition Time Server.

## [◆ ](#ga462c578845a17b20cdb3e008f74f93a6)BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_CLI

| #define BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_CLI   0x1003 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Level Client.

## [◆ ](#ga7f10a8332b1406c3ad628b9679e1d7cb)BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_LEVEL\_SRV   0x1002 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Level Server.

## [◆ ](#ga8fa01ddb1f4de4d61500bb650243390d)BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_CLI

| #define BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_CLI   0x1010 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Location Client.

## [◆ ](#ga240d1ed34b7341627773cce862f85620)BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SETUPSRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SETUPSRV   0x100f |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Location Setup Server.

## [◆ ](#gad516f513c5c942fbfee65b85332b105e)BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_LOCATION\_SRV   0x100e |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Location Server.

## [◆ ](#ga32e09ddfebd2e8b22da9a3102e116aae)BT\_MESH\_MODEL\_ID\_GEN\_MANUFACTURER\_PROP\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_MANUFACTURER\_PROP\_SRV   0x1012 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Manufacturer Property Server.

## [◆ ](#ga4f0eee2569b518a5e4250f5b7b294fed)BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_CLI

| #define BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_CLI   0x1001 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic OnOff Client.

## [◆ ](#ga83e1ed5398d513cfeb900e41655aa4d8)BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_ONOFF\_SRV   0x1000 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic OnOff Server.

## [◆ ](#ga8420454c35afc12c62ede55942f3b6d3)BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_CLI

| #define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_CLI   0x100b |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Power Level Client.

## [◆ ](#ga1ff6ec64ce3a86d1cfd00fc98e89c0a5)BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SETUP\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SETUP\_SRV   0x100a |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Power Level Setup Server.

## [◆ ](#gadd30afe63f89e9c1778e56f722fd82f9)BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_LEVEL\_SRV   0x1009 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Power Level Server.

## [◆ ](#ga9f6544f7b87f39d0792ea2de13cd45f1)BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_CLI

| #define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_CLI   0x1008 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Power OnOff Client.

## [◆ ](#ga2a6dad18792ba7f1d81d6c9a1c65f90a)BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SETUP\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SETUP\_SRV   0x1007 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Power OnOff Setup Server.

## [◆ ](#ga09ac731fff09146ec68557f00e8294e0)BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_POWER\_ONOFF\_SRV   0x1006 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Power OnOff Server.

## [◆ ](#ga69455e5b1e6def3d909c4bb6e0dee9ae)BT\_MESH\_MODEL\_ID\_GEN\_PROP\_CLI

| #define BT\_MESH\_MODEL\_ID\_GEN\_PROP\_CLI   0x1015 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic Property Client.

## [◆ ](#ga4b7b6a4b47e87de94ccf11ef1abd64b9)BT\_MESH\_MODEL\_ID\_GEN\_USER\_PROP\_SRV

| #define BT\_MESH\_MODEL\_ID\_GEN\_USER\_PROP\_SRV   0x1013 |
| --- |

`#include <[access.h](access_8h.md)>`

Generic User Property Server.

## [◆ ](#gab58b85b7a77feeb579973177c12bb446)BT\_MESH\_MODEL\_ID\_HEALTH\_CLI

| #define BT\_MESH\_MODEL\_ID\_HEALTH\_CLI   0x0003 |
| --- |

`#include <[access.h](access_8h.md)>`

Health Client.

## [◆ ](#ga6416216348d7186f91175ca50bb8c903)BT\_MESH\_MODEL\_ID\_HEALTH\_SRV

| #define BT\_MESH\_MODEL\_ID\_HEALTH\_SRV   0x0002 |
| --- |

`#include <[access.h](access_8h.md)>`

Health Server.

## [◆ ](#ga729d67e4183457932e4c837d65abd842)BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_CLI

| #define BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_CLI   0x0013 |
| --- |

`#include <[access.h](access_8h.md)>`

Large Composition Data Client.

## [◆ ](#gaec3abd6a0bd7b07a71fe5ed6a7a6931a)BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_SRV

| #define BT\_MESH\_MODEL\_ID\_LARGE\_COMP\_DATA\_SRV   0x0012 |
| --- |

`#include <[access.h](access_8h.md)>`

Large Composition Data Server.

## [◆ ](#ga58fc8d99b746b0061177ac5d95341da1)BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_CLI

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_CLI   0x1305 |
| --- |

`#include <[access.h](access_8h.md)>`

Light CTL Client.

## [◆ ](#ga28ac69b2dbeec70bae4bd3c0381e9e93)BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SETUP\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SETUP\_SRV   0x1304 |
| --- |

`#include <[access.h](access_8h.md)>`

Light CTL Setup Server.

## [◆ ](#gaa9a211341c5b3283b9b0e0842adef053)BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_SRV   0x1303 |
| --- |

`#include <[access.h](access_8h.md)>`

Light CTL Server.

## [◆ ](#gafcb1f1ea20bb78b78a9ead4bfdbe3e47)BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_TEMP\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_CTL\_TEMP\_SRV   0x1306 |
| --- |

`#include <[access.h](access_8h.md)>`

Light CTL Temperature Server.

## [◆ ](#ga2d111a352322be8e33ba0cba0feb3f0c)BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_CLI

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_CLI   0x1309 |
| --- |

`#include <[access.h](access_8h.md)>`

Light HSL Client.

## [◆ ](#ga865952346db9336a255c71bcb5f09774)BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_HUE\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_HUE\_SRV   0x130a |
| --- |

`#include <[access.h](access_8h.md)>`

Light HSL Hue Server.

## [◆ ](#gae55004e70670a8711e18e9c9b3428720)BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SAT\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SAT\_SRV   0x130b |
| --- |

`#include <[access.h](access_8h.md)>`

Light HSL Saturation Server.

## [◆ ](#ga574d3ba3f629bdbffc8f15db931a263a)BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SETUP\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SETUP\_SRV   0x1308 |
| --- |

`#include <[access.h](access_8h.md)>`

Light HSL Setup Server.

## [◆ ](#gaa0ddc753a226060d014dcd368feab17e)BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_HSL\_SRV   0x1307 |
| --- |

`#include <[access.h](access_8h.md)>`

Light HSL Server.

## [◆ ](#gaadd48b07e1eb53df24df40b7ea412e90)BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_CLI

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_CLI   0x1311 |
| --- |

`#include <[access.h](access_8h.md)>`

Light LC Client.

## [◆ ](#ga436358740bb64d845aa4d849d462a12e)BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SETUPSRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SETUPSRV   0x1310 |
| --- |

`#include <[access.h](access_8h.md)>`

Light LC Setup Server.

## [◆ ](#ga789412252034939539ba45e4bf21e3e2)BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_LC\_SRV   0x130f |
| --- |

`#include <[access.h](access_8h.md)>`

Light LC Server.

## [◆ ](#ga960055723dec7b3b366efa7c49cafc2e)BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_CLI

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_CLI   0x1302 |
| --- |

`#include <[access.h](access_8h.md)>`

Light Lightness Client.

## [◆ ](#gadb93b2ed2256a5c9c3f66237841b1bf5)BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SETUP\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SETUP\_SRV   0x1301 |
| --- |

`#include <[access.h](access_8h.md)>`

Light Lightness Setup Server.

## [◆ ](#ga16df49e84e84d0ae4a6ab5d5f3f1b2b6)BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_LIGHTNESS\_SRV   0x1300 |
| --- |

`#include <[access.h](access_8h.md)>`

Light Lightness Server.

## [◆ ](#ga0ca4d9997e6016b5c27f42549d42a99d)BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_CLI

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_CLI   0x130e |
| --- |

`#include <[access.h](access_8h.md)>`

Light xyL Client.

## [◆ ](#ga4addae460d6b3c0a914198695b3e31ea)BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SETUP\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SETUP\_SRV   0x130d |
| --- |

`#include <[access.h](access_8h.md)>`

Light xyL Setup Server.

## [◆ ](#ga29e1a90f166d88b6773d9b7ccf08e1c7)BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SRV

| #define BT\_MESH\_MODEL\_ID\_LIGHT\_XYL\_SRV   0x130c |
| --- |

`#include <[access.h](access_8h.md)>`

Light xyL Server.

## [◆ ](#gadd36546fb2cb6d1c731f7ae7674af6a7)BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_CLI

| #define BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_CLI   0x000d |
| --- |

`#include <[access.h](access_8h.md)>`

Private Proxy Client.

## [◆ ](#gaddc0bd645180a57cb9cd36745b84f7a1)BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_SRV

| #define BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_SRV   0x000c |
| --- |

`#include <[access.h](access_8h.md)>`

Private Proxy Server.

## [◆ ](#gabac62a77e7d2d7677af21c33c8629187)BT\_MESH\_MODEL\_ID\_OP\_AGG\_CLI

| #define BT\_MESH\_MODEL\_ID\_OP\_AGG\_CLI   0x0011 |
| --- |

`#include <[access.h](access_8h.md)>`

Opcodes Aggregator Client.

## [◆ ](#ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a)BT\_MESH\_MODEL\_ID\_OP\_AGG\_SRV

| #define BT\_MESH\_MODEL\_ID\_OP\_AGG\_SRV   0x0010 |
| --- |

`#include <[access.h](access_8h.md)>`

Opcodes Aggregator Server.

## [◆ ](#gab3b21cbee4e11319a6e0ba3b02b24a91)BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_CLI

| #define BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_CLI   0x000b |
| --- |

`#include <[access.h](access_8h.md)>`

Private Beacon Client.

## [◆ ](#gacca0e355982935cfbde46a06b09a7bec)BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_SRV

| #define BT\_MESH\_MODEL\_ID\_PRIV\_BEACON\_SRV   0x000a |
| --- |

`#include <[access.h](access_8h.md)>`

Private Beacon Server.

## [◆ ](#gaf373eb4d8af5d6bee76a821bd4d5e48c)BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_CLI

| #define BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_CLI   0x0005 |
| --- |

`#include <[access.h](access_8h.md)>`

Remote Provisioning Client.

## [◆ ](#ga9c7d1c5dfb87a5ce50c08747af47414f)BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_SRV

| #define BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_SRV   0x0004 |
| --- |

`#include <[access.h](access_8h.md)>`

Remote Provisioning Server.

## [◆ ](#gaf214eb7eef3530919432b62ff9b353c3)BT\_MESH\_MODEL\_ID\_SAR\_CFG\_CLI

| #define BT\_MESH\_MODEL\_ID\_SAR\_CFG\_CLI   0x000f |
| --- |

`#include <[access.h](access_8h.md)>`

SAR Configuration Client.

## [◆ ](#ga1e9d8be1d2e65d2977aea0306b015258)BT\_MESH\_MODEL\_ID\_SAR\_CFG\_SRV

| #define BT\_MESH\_MODEL\_ID\_SAR\_CFG\_SRV   0x000e |
| --- |

`#include <[access.h](access_8h.md)>`

SAR Configuration Server.

## [◆ ](#gad60472aa004a8a913aeb63ef62c45857)BT\_MESH\_MODEL\_ID\_SCENE\_CLI

| #define BT\_MESH\_MODEL\_ID\_SCENE\_CLI   0x1205 |
| --- |

`#include <[access.h](access_8h.md)>`

Scene Client.

## [◆ ](#gaa3b08fc8788684abb960fa3516726264)BT\_MESH\_MODEL\_ID\_SCENE\_SETUP\_SRV

| #define BT\_MESH\_MODEL\_ID\_SCENE\_SETUP\_SRV   0x1204 |
| --- |

`#include <[access.h](access_8h.md)>`

Scene Setup Server.

## [◆ ](#gaaa5554e3d48ae101596476e6bd6caf67)BT\_MESH\_MODEL\_ID\_SCENE\_SRV

| #define BT\_MESH\_MODEL\_ID\_SCENE\_SRV   0x1203 |
| --- |

`#include <[access.h](access_8h.md)>`

Scene Server.

## [◆ ](#gac743b26cf7e746b16302c25e8cd56221)BT\_MESH\_MODEL\_ID\_SCHEDULER\_CLI

| #define BT\_MESH\_MODEL\_ID\_SCHEDULER\_CLI   0x1208 |
| --- |

`#include <[access.h](access_8h.md)>`

Scheduler Client.

## [◆ ](#ga3dbec5a3b82cb25a142c4bc851e3fe0e)BT\_MESH\_MODEL\_ID\_SCHEDULER\_SETUP\_SRV

| #define BT\_MESH\_MODEL\_ID\_SCHEDULER\_SETUP\_SRV   0x1207 |
| --- |

`#include <[access.h](access_8h.md)>`

Scheduler Setup Server.

## [◆ ](#ga82b723752e240f22b9bcc8dc3dd10eb9)BT\_MESH\_MODEL\_ID\_SCHEDULER\_SRV

| #define BT\_MESH\_MODEL\_ID\_SCHEDULER\_SRV   0x1206 |
| --- |

`#include <[access.h](access_8h.md)>`

Scheduler Server.

## [◆ ](#ga8f1e4ff66d388627dbe91b2f8d4ed358)BT\_MESH\_MODEL\_ID\_SENSOR\_CLI

| #define BT\_MESH\_MODEL\_ID\_SENSOR\_CLI   0x1102 |
| --- |

`#include <[access.h](access_8h.md)>`

Sensor Client.

## [◆ ](#gad10780bfc1c16866fa28de750e56bec3)BT\_MESH\_MODEL\_ID\_SENSOR\_SETUP\_SRV

| #define BT\_MESH\_MODEL\_ID\_SENSOR\_SETUP\_SRV   0x1101 |
| --- |

`#include <[access.h](access_8h.md)>`

Sensor Setup Server.

## [◆ ](#ga3e0dcb14f46f6076e5b1b114b977f630)BT\_MESH\_MODEL\_ID\_SENSOR\_SRV

| #define BT\_MESH\_MODEL\_ID\_SENSOR\_SRV   0x1100 |
| --- |

`#include <[access.h](access_8h.md)>`

Sensor Server.

## [◆ ](#ga6e747dd364bcfaa368e37c5f01afd530)BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_CLI

| #define BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_CLI   0x0015 |
| --- |

`#include <[access.h](access_8h.md)>`

Solicitation PDU RPL Configuration Server.

## [◆ ](#ga165bc198dadaa0d534ec82eb8192ebc0)BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_SRV

| #define BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_SRV   0x0014 |
| --- |

`#include <[access.h](access_8h.md)>`

Solicitation PDU RPL Configuration Client.

## [◆ ](#ga500df90af7989794c5d72e760e5e65c6)BT\_MESH\_MODEL\_ID\_TIME\_CLI

| #define BT\_MESH\_MODEL\_ID\_TIME\_CLI   0x1202 |
| --- |

`#include <[access.h](access_8h.md)>`

Time Client.

## [◆ ](#ga2725121dc8c2c21c0ee469fe4348f45f)BT\_MESH\_MODEL\_ID\_TIME\_SETUP\_SRV

| #define BT\_MESH\_MODEL\_ID\_TIME\_SETUP\_SRV   0x1201 |
| --- |

`#include <[access.h](access_8h.md)>`

Time Setup Server.

## [◆ ](#ga93fbf1c661a75d70fdbd2a599353eb94)BT\_MESH\_MODEL\_ID\_TIME\_SRV

| #define BT\_MESH\_MODEL\_ID\_TIME\_SRV   0x1200 |
| --- |

`#include <[access.h](access_8h.md)>`

Time Server.

## [◆ ](#ga40204b4ccaa819a487de168bcf66c98f)BT\_MESH\_MODEL\_METADATA\_CB

| #define BT\_MESH\_MODEL\_METADATA\_CB | ( |  | *\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_op*, |
|  |  |  | *\_pub*, |
|  |  |  | *\_user\_data*, |
|  |  |  | *\_cb*, |
|  |  |  | *\_metadata* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](#gac062c101b7310020e11a527de9c40d3a)(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions and metadata.

This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

Parameters
:   | \_id | Model ID. |
    | --- | --- |
    | \_op | Array of model opcode handlers. |
    | \_pub | Model publish parameters. |
    | \_user\_data | User data for the model. |
    | \_cb | Callback structure, or NULL to keep no callbacks. |
    | \_metadata | Metadata structure. Used if  ``` CONFIG_BT_MESH_LARGE_COMP_DATA_SRV ```  is enabled. |

## [◆ ](#gae6d55e0a27bb7c448affd312a2e11656)BT\_MESH\_MODEL\_NO\_OPS

| #define BT\_MESH\_MODEL\_NO\_OPS |
| --- |

`#include <[access.h](access_8h.md)>`

**Value:**

((struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) []) \

{ [BT\_MESH\_MODEL\_OP\_END](#gaf2c164506c601214c85d451747176827) })

[BT\_MESH\_MODEL\_OP\_END](#gaf2c164506c601214c85d451747176827)

#define BT\_MESH\_MODEL\_OP\_END

End of the opcode list.

**Definition** access.h:399

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

Helper to define an empty opcode list.

This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

## [◆ ](#gab0ad2aab95d49e5b60fe8dafd69132a4)BT\_MESH\_MODEL\_NONE

| #define BT\_MESH\_MODEL\_NONE   ((const struct [bt\_mesh\_model](structbt__mesh__model.md) []){}) |
| --- |

`#include <[access.h](access_8h.md)>`

Helper to define an empty model array.

This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

## [◆ ](#ga00915cfdff7dc0646f24d6b06e124d0d)BT\_MESH\_MODEL\_OP\_1

| #define BT\_MESH\_MODEL\_OP\_1 | ( |  | *b0* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

(b0)

## [◆ ](#gaa52a40ef5972c4f34cf5ff5a10e21289)BT\_MESH\_MODEL\_OP\_2

| #define BT\_MESH\_MODEL\_OP\_2 | ( |  | *b0*, |
| --- | --- | --- | --- |
|  |  |  | *b1* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

(((b0) << 8) | (b1))

## [◆ ](#ga72d1d19701be52f5eac6af475f9b19a9)BT\_MESH\_MODEL\_OP\_3

| #define BT\_MESH\_MODEL\_OP\_3 | ( |  | *b0*, |
| --- | --- | --- | --- |
|  |  |  | *cid* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

((((b0) << 16) | 0xc00000) | (cid))

## [◆ ](#gaf2c164506c601214c85d451747176827)BT\_MESH\_MODEL\_OP\_END

| #define BT\_MESH\_MODEL\_OP\_END   { 0, 0, NULL } |
| --- |

`#include <[access.h](access_8h.md)>`

End of the opcode list.

Must always be present.

## [◆ ](#ga8334ff2da1f0dc3ab2fc914059c33622)BT\_MESH\_MODEL\_PUB\_DEFINE

| #define BT\_MESH\_MODEL\_PUB\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_update*, |
|  |  |  | *\_msg\_len* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

[NET\_BUF\_SIMPLE\_DEFINE\_STATIC](group__net__buf.md#ga21ced8b3082d57bf071008de5fffc0f4)(bt\_mesh\_pub\_msg\_##\_name, \_msg\_len); \

static struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md) \_name = { \

.msg = &bt\_mesh\_pub\_msg\_##\_name, \

.[update](structbt__mesh__model__pub.md#a0354344e08e633dc4d6c0b4e7b169080) = \_update, \

}

[NET\_BUF\_SIMPLE\_DEFINE\_STATIC](group__net__buf.md#ga21ced8b3082d57bf071008de5fffc0f4)

#define NET\_BUF\_SIMPLE\_DEFINE\_STATIC(\_name, \_size)

Define a static net\_buf\_simple variable.

**Definition** net\_buf.h:67

[bt\_mesh\_model\_pub](structbt__mesh__model__pub.md)

Model publication context.

**Definition** access.h:708

[bt\_mesh\_model\_pub::update](structbt__mesh__model__pub.md#a0354344e08e633dc4d6c0b4e7b169080)

int(\* update)(const struct bt\_mesh\_model \*mod)

Callback for updating the publication buffer.

**Definition** access.h:757

Define a model publication context.

Parameters
:   | \_name | Variable name given to the context. |
    | --- | --- |
    | \_update | Optional message update callback (may be NULL). |
    | \_msg\_len | Length of the publication message. |

## [◆ ](#ga3759c8c88db48be662bf2511ff514edd)BT\_MESH\_MODEL\_VND

| #define BT\_MESH\_MODEL\_VND | ( |  | *\_company*, |
| --- | --- | --- | --- |
|  |  |  | *\_id*, |
|  |  |  | *\_op*, |
|  |  |  | *\_pub*, |
|  |  |  | *\_user\_data* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_VND\_CB](#gabe79d914990ba2721f5bb7081910e512)(\_company, \_id, \_op, \_pub, \_user\_data, NULL)

[BT\_MESH\_MODEL\_VND\_CB](#gabe79d914990ba2721f5bb7081910e512)

#define BT\_MESH\_MODEL\_VND\_CB(\_company, \_id, \_op, \_pub, \_user\_data, \_cb)

Composition data vendor model entry with callback functions.

**Definition** access.h:550

Composition data vendor model entry.

This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

Parameters
:   | \_company | Company ID. |
    | --- | --- |
    | \_id | Model ID. |
    | \_op | Array of model opcode handlers. |
    | \_pub | Model publish parameters. |
    | \_user\_data | User data for the model. |

## [◆ ](#gabe79d914990ba2721f5bb7081910e512)BT\_MESH\_MODEL\_VND\_CB

| #define BT\_MESH\_MODEL\_VND\_CB | ( |  | *\_company*, |
| --- | --- | --- | --- |
|  |  |  | *\_id*, |
|  |  |  | *\_op*, |
|  |  |  | *\_pub*, |
|  |  |  | *\_user\_data*, |
|  |  |  | *\_cb* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CNT\_VND\_CB](#ga32733dccd9329aa938dc0bd21cf9beae)(\_company, \_id, \_op, \_pub, \_user\_data, \

CONFIG\_BT\_MESH\_MODEL\_KEY\_COUNT, \

CONFIG\_BT\_MESH\_MODEL\_GROUP\_COUNT, \_cb)

[BT\_MESH\_MODEL\_CNT\_VND\_CB](#ga32733dccd9329aa938dc0bd21cf9beae)

#define BT\_MESH\_MODEL\_CNT\_VND\_CB(\_company, \_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb)

Composition data vendor model entry with callback functions with specific number of keys & groups.

**Definition** access.h:468

Composition data vendor model entry with callback functions.

This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

Parameters
:   | \_company | Company ID. |
    | --- | --- |
    | \_id | Model ID. |
    | \_op | Array of model opcode handlers. |
    | \_pub | Model publish parameters. |
    | \_user\_data | User data for the model. |
    | \_cb | Callback structure, or NULL to keep no callbacks. |

## [◆ ](#gac62334962dcbe3a75a03ce5744b326d8)BT\_MESH\_MODEL\_VND\_METADATA\_CB

| #define BT\_MESH\_MODEL\_VND\_METADATA\_CB | ( |  | *\_company*, |
| --- | --- | --- | --- |
|  |  |  | *\_id*, |
|  |  |  | *\_op*, |
|  |  |  | *\_pub*, |
|  |  |  | *\_user\_data*, |
|  |  |  | *\_cb*, |
|  |  |  | *\_metadata* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_VND\_CB](#gabe79d914990ba2721f5bb7081910e512)(\_company, \_id, \_op, \_pub, \_user\_data, \_cb)

Composition data vendor model entry with callback functions and metadata.

This macro uses compound literal feature of C99 standard and thus is available only from C, not C++.

Parameters
:   | \_company | Company ID. |
    | --- | --- |
    | \_id | Model ID. |
    | \_op | Array of model opcode handlers. |
    | \_pub | Model publish parameters. |
    | \_user\_data | User data for the model. |
    | \_cb | Callback structure, or NULL to keep no callbacks. |
    | \_metadata | Metadata structure. Used if  ``` CONFIG_BT_MESH_LARGE_COMP_DATA_SRV ```  is enabled. |

## [◆ ](#gaab5fe51071f6e54debd9136ac6a70a49)BT\_MESH\_MODELS\_METADATA\_END

| #define BT\_MESH\_MODELS\_METADATA\_END   { 0, 0, NULL } |
| --- |

`#include <[access.h](access_8h.md)>`

End of the Models Metadata list.

Must always be present.

## [◆ ](#gaa2587adac719c50c311ae41c548b853c)BT\_MESH\_MODELS\_METADATA\_ENTRY

| #define BT\_MESH\_MODELS\_METADATA\_ENTRY | ( |  | *\_len*, |
| --- | --- | --- | --- |
|  |  |  | *\_id*, |
|  |  |  | *\_data* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

{ \

.len = (\_len), .id = \_id, .data = \_data, \

}

Initialize a Models Metadata entry structure in a list.

Parameters
:   | \_len | Length of the metadata entry. |
    | --- | --- |
    | \_id | ID of the Models Metadata entry. |
    | \_data | Pointer to a contiguous memory that contains the metadata. |

## [◆ ](#ga56b518123ab47cb3ae4a249f471ae556)BT\_MESH\_MODELS\_METADATA\_NONE

| #define BT\_MESH\_MODELS\_METADATA\_NONE   NULL |
| --- |

`#include <[access.h](access_8h.md)>`

Helper to define an empty Models metadata array.

## [◆ ](#ga115ee29aba3c3e985aa11d6692ca0d83)BT\_MESH\_PUB\_MSG\_NUM

| #define BT\_MESH\_PUB\_MSG\_NUM | ( |  | *pub* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

([BT\_MESH\_PUB\_TRANSMIT\_COUNT](#ga13986422dda5edce4f5fb1ce387093e3)((pub)->retransmit) + 1 - (pub)->count)

[BT\_MESH\_PUB\_TRANSMIT\_COUNT](#ga13986422dda5edce4f5fb1ce387093e3)

#define BT\_MESH\_PUB\_TRANSMIT\_COUNT(transmit)

Decode Publish Retransmit count from a given value.

**Definition** access.h:671

Get message number within one publication interval.

Meant to be used inside [bt\_mesh\_model\_pub::update](structbt__mesh__model__pub.md#a0354344e08e633dc4d6c0b4e7b169080 "bt_mesh_model_pub::update").

Parameters
:   | pub | Model publication context. |
    | --- | --- |

Returns
:   message number starting from 1.

## [◆ ](#ga230538bb39ac3d6c8c0327d1fad77e69)BT\_MESH\_PUB\_MSG\_TOTAL

| #define BT\_MESH\_PUB\_MSG\_TOTAL | ( |  | *pub* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

([BT\_MESH\_PUB\_TRANSMIT\_COUNT](#ga13986422dda5edce4f5fb1ce387093e3)((pub)->retransmit) + 1)

Get total number of messages within one publication interval including initial publication.

Parameters
:   | pub | Model publication context. |
    | --- | --- |

Returns
:   total number of messages.

## [◆ ](#ga19208dea7bab9f31c2c793ef6201dd91)BT\_MESH\_PUB\_TRANSMIT

| #define BT\_MESH\_PUB\_TRANSMIT | ( |  | *count*, |
| --- | --- | --- | --- |
|  |  |  | *int\_ms* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

[BT\_MESH\_TRANSMIT](#gaff82bf652232fbce71c31f38a10577a9)(count, \

(int\_ms) / 5)

[BT\_MESH\_TRANSMIT](#gaff82bf652232fbce71c31f38a10577a9)

#define BT\_MESH\_TRANSMIT(count, int\_ms)

Encode transmission count & interval steps.

**Definition** access.h:631

Encode Publish Retransmit count & interval steps.

Parameters
:   | count | Number of retransmissions (first transmission is excluded). |
    | --- | --- |
    | int\_ms | Interval steps in milliseconds. Must be greater than 0 and a multiple of 50. |

Returns
:   Mesh transmit value that can be used e.g. for the default values of the configuration model data.

## [◆ ](#ga13986422dda5edce4f5fb1ce387093e3)BT\_MESH\_PUB\_TRANSMIT\_COUNT

| #define BT\_MESH\_PUB\_TRANSMIT\_COUNT | ( |  | *transmit* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

[BT\_MESH\_TRANSMIT\_COUNT](#ga62fda0d731241efbaa4827e4eb9d1795)(transmit)

[BT\_MESH\_TRANSMIT\_COUNT](#ga62fda0d731241efbaa4827e4eb9d1795)

#define BT\_MESH\_TRANSMIT\_COUNT(transmit)

Decode transmit count from a transmit value.

**Definition** access.h:640

Decode Publish Retransmit count from a given value.

Parameters
:   | transmit | Encoded Publish Retransmit count & interval value. |
    | --- | --- |

Returns
:   Retransmission count (actual transmissions is N + 1).

## [◆ ](#gaac954956dd3913dd7ad2b93a2566afd9)BT\_MESH\_PUB\_TRANSMIT\_INT

| #define BT\_MESH\_PUB\_TRANSMIT\_INT | ( |  | *transmit* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

((((transmit) >> 3) + 1) \* 50)

Decode Publish Retransmit interval from a given value.

Parameters
:   | transmit | Encoded Publish Retransmit count & interval value. |
    | --- | --- |

Returns
:   Transmission interval in milliseconds.

## [◆ ](#ga36f299f2fc13892b5a7d871dad1ec9ce)BT\_MESH\_RX\_SDU\_MAX

| #define BT\_MESH\_RX\_SDU\_MAX |
| --- |

`#include <[access.h](access_8h.md)>`

**Value:**

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(([BT\_MESH\_RX\_SEG\_MAX](#ga18756e939ec3b312eef5c3dc9fd70270) \* \

[BT\_MESH\_APP\_SEG\_SDU\_MAX](#gaa620c32d1dce8e4b691b7f4270016506)), \

[BT\_MESH\_APP\_UNSEG\_SDU\_MAX](#ga64eb6a94b1db9899c4f5bbf4cc88cd9f))

[BT\_MESH\_RX\_SEG\_MAX](#ga18756e939ec3b312eef5c3dc9fd70270)

#define BT\_MESH\_RX\_SEG\_MAX

Maximum number of segments supported for incoming messages.

**Definition** access.h:114

[BT\_MESH\_APP\_UNSEG\_SDU\_MAX](#ga64eb6a94b1db9899c4f5bbf4cc88cd9f)

#define BT\_MESH\_APP\_UNSEG\_SDU\_MAX

Maximum payload size of an unsegmented access message (in octets).

**Definition** access.h:108

[BT\_MESH\_APP\_SEG\_SDU\_MAX](#gaa620c32d1dce8e4b691b7f4270016506)

#define BT\_MESH\_APP\_SEG\_SDU\_MAX

Maximum size of an access message segment (in octets).

**Definition** access.h:105

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)

#define MAX(a, b)

Obtain the maximum of two values.

**Definition** util.h:385

Maximum possible payload size of an incoming access message (in octets).

## [◆ ](#ga18756e939ec3b312eef5c3dc9fd70270)BT\_MESH\_RX\_SEG\_MAX

| #define BT\_MESH\_RX\_SEG\_MAX   0 |
| --- |

`#include <[access.h](access_8h.md)>`

Maximum number of segments supported for incoming messages.

## [◆ ](#gaff82bf652232fbce71c31f38a10577a9)BT\_MESH\_TRANSMIT

| #define BT\_MESH\_TRANSMIT | ( |  | *count*, |
| --- | --- | --- | --- |
|  |  |  | *int\_ms* ) |

`#include <[access.h](access_8h.md)>`

**Value:**

((count) | (((int\_ms / 10) - 1) << 3))

Encode transmission count & interval steps.

Parameters
:   | count | Number of retransmissions (first transmission is excluded). |
    | --- | --- |
    | int\_ms | Interval steps in milliseconds. Must be greater than 0, less than or equal to 320, and a multiple of 10. |

Returns
:   Mesh transmit value that can be used e.g. for the default values of the configuration model data.

## [◆ ](#ga62fda0d731241efbaa4827e4eb9d1795)BT\_MESH\_TRANSMIT\_COUNT

| #define BT\_MESH\_TRANSMIT\_COUNT | ( |  | *transmit* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

(((transmit) & ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))[BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3)))

[BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

Bit mask with bits 0 through n-1 (inclusive) set, or 0 if n is 0.

**Definition** util\_macro.h:68

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Decode transmit count from a transmit value.

Parameters
:   | transmit | Encoded transmit count & interval value. |
    | --- | --- |

Returns
:   Transmission count (actual transmissions is N + 1).

## [◆ ](#ga2aa21171c5677d23ad0c472291639417)BT\_MESH\_TRANSMIT\_INT

| #define BT\_MESH\_TRANSMIT\_INT | ( |  | *transmit* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

**Value:**

((((transmit) >> 3) + 1) \* 10)

Decode transmit interval from a transmit value.

Parameters
:   | transmit | Encoded transmit count & interval value. |
    | --- | --- |

Returns
:   Transmission interval in milliseconds.

## [◆ ](#ga16516272b42420263b1c47c3ea16c0c8)BT\_MESH\_TTL\_DEFAULT

| #define BT\_MESH\_TTL\_DEFAULT   0xff |
| --- |

`#include <[access.h](access_8h.md)>`

Special TTL value to request using configured default TTL.

## [◆ ](#ga071e85e929589d31bf876e2e09cf2f19)BT\_MESH\_TTL\_MAX

| #define BT\_MESH\_TTL\_MAX   0x7f |
| --- |

`#include <[access.h](access_8h.md)>`

Maximum allowed TTL value.

## [◆ ](#ga86d7386603ecd89952b6d540ea4243c2)BT\_MESH\_TX\_SDU\_MAX

| #define BT\_MESH\_TX\_SDU\_MAX |
| --- |

`#include <[access.h](access_8h.md)>`

**Value:**

[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(([BT\_MESH\_TX\_SEG\_MAX](#ga1b2a3610ac370266578abce195e65fa2) \* \

[BT\_MESH\_APP\_SEG\_SDU\_MAX](#gaa620c32d1dce8e4b691b7f4270016506)), \

[BT\_MESH\_APP\_UNSEG\_SDU\_MAX](#ga64eb6a94b1db9899c4f5bbf4cc88cd9f))

[BT\_MESH\_TX\_SEG\_MAX](#ga1b2a3610ac370266578abce195e65fa2)

#define BT\_MESH\_TX\_SEG\_MAX

Maximum number of segments supported for outgoing messages.

**Definition** access.h:121

Maximum possible payload size of an outgoing access message (in octets).

## [◆ ](#ga1b2a3610ac370266578abce195e65fa2)BT\_MESH\_TX\_SEG\_MAX

| #define BT\_MESH\_TX\_SEG\_MAX   0 |
| --- |

`#include <[access.h](access_8h.md)>`

Maximum number of segments supported for outgoing messages.

## Function Documentation

## [◆ ](#ga8445c550a47dba16e3fa6fea36d6d9fc)bt\_mesh\_comp2\_register()

| int bt\_mesh\_comp2\_register | ( | const struct [bt\_mesh\_comp2](structbt__mesh__comp2.md) \* | *comp2* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

Register composition data page 2 of the device.

Register Mesh Profiles information (Ref section 3.12 in Bluetooth SIG Assigned Numbers) for composition data page 2 of the device.

Note
:   There must be at least one record present in `comp2`

Parameters
:   | comp2 | Pointer to composition data page 2. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga8575f680e77d86d6c85cac27985b9f3c)bt\_mesh\_comp\_change\_prepare()

| int bt\_mesh\_comp\_change\_prepare | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

Indicate that the composition data will change on next bootup.

Tell the config server that the composition data is expected to change on the next bootup, and the current composition data should be backed up.

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga03ce9f6f9ccf734ea72beede09288923)bt\_mesh\_model\_correspond()

| int bt\_mesh\_model\_correspond | ( | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *corresponding\_mod*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *base\_mod* ) |

`#include <[access.h](access_8h.md)>`

Let a model correspond to another.

Mesh models may correspond to each other, which means that if one is present, other must be present too. A Mesh model may correspond to any number of models, in any element. All models connected together via correspondence form single Correspondence Group, which has it's unique Correspondence ID. Information about Correspondence is used to construct Composition Data Page 1.

This function must be called on already initialized base\_mod. Because this function is designed to be called in corresponding\_mod initializer, this means that base\_mod shall be initialized before corresponding\_mod is.

Parameters
:   | corresponding\_mod | Mesh model that is corresponding to the base model. |
    | --- | --- |
    | base\_mod | The model being corresponded to. |

Return values
:   | 0 | Successfully saved correspondence to the base\_mod model. |
    | --- | --- |
    | -ENOMEM | There is no more space to save this relation. |
    | -ENOTSUP | Composition Data Page 1 is not supported. |

## [◆ ](#gadff0895c5c34928d778fa615512b3d85)bt\_mesh\_model\_data\_store()

| int bt\_mesh\_model\_data\_store | ( | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *mod*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *vnd*, |
|  |  | const char \* | *name*, |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_len* ) |

`#include <[access.h](access_8h.md)>`

Immediately store the model's user data in persistent storage.

Parameters
:   | mod | Mesh model. |
    | --- | --- |
    | vnd | This is a vendor model. |
    | name | Name/key of the settings item. Only [SETTINGS\_MAX\_DIR\_DEPTH](group__settings.md#ga2afa32b032e88a188c5263156d9e73e1 "SETTINGS_MAX_DIR_DEPTH") bytes will be used at most. |
    | data | Model data to store, or NULL to delete any model data. |
    | data\_len | Length of the model data. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga762896dd2e806b5be061b220d53ce4db)bt\_mesh\_model\_data\_store\_schedule()

| void bt\_mesh\_model\_data\_store\_schedule | ( | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *mod* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

Schedule the model's user data store in persistent storage.

This function triggers the [bt\_mesh\_model\_cb::pending\_store](structbt__mesh__model__cb.md#ae28f875dffc7f5f2ce99abe590369f43 "bt_mesh_model_cb::pending_store") callback for the corresponding model after delay defined by

```
CONFIG_BT_MESH_STORE_TIMEOUT
```

.

The delay is global for all models. Once scheduled, the callback can not be re-scheduled until previous schedule completes.

Parameters
:   | mod | Mesh model. |
    | --- | --- |

## [◆ ](#ga8edba04af103fb11994d4d3e558ec4fb)bt\_mesh\_model\_elem()

| const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \* bt\_mesh\_model\_elem | ( | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *mod* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

Get the element that a model belongs to.

Parameters
:   | mod | Mesh model. |
    | --- | --- |

Returns
:   Pointer to the element that the given model belongs to.

## [◆ ](#gaf6356f715c8968151b8d539f2dd1880c)bt\_mesh\_model\_extend()

| int bt\_mesh\_model\_extend | ( | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *extending\_mod*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *base\_mod* ) |

`#include <[access.h](access_8h.md)>`

Let a model extend another.

Mesh models may be extended to reuse their functionality, forming a more complex model. A Mesh model may extend any number of models, in any element. The extensions may also be nested, ie a model that extends another may itself be extended.

A set of models that extend each other form a model extension list.

All models in an extension list share one subscription list per element. The access layer will utilize the combined subscription list of all models in an extension list and element, giving the models extended subscription list capacity.

If

```
CONFIG_BT_MESH_COMP_PAGE_1
```

is enabled, it is not allowed to call this function before the [bt\_mesh\_model\_cb::init](structbt__mesh__model__cb.md#a1688a2c6d7b3b17ba49a0975b6f4f68e "bt_mesh_model_cb::init") callback is called for both models, except if it is called as part of the final callback.

Parameters
:   | extending\_mod | Mesh model that is extending the base model. |
    | --- | --- |
    | base\_mod | The model being extended. |

Return values
:   | 0 | Successfully extended the base\_mod model. |
    | --- | --- |

## [◆ ](#gaf0510f9511d72f1d4fd07f865753a50a)bt\_mesh\_model\_find()

| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* bt\_mesh\_model\_find | ( | const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \* | *elem*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id* ) |

`#include <[access.h](access_8h.md)>`

Find a SIG model.

Parameters
:   | elem | Element to search for the model in. |
    | --- | --- |
    | id | Model ID of the model. |

Returns
:   A pointer to the Mesh model matching the given parameters, or NULL if no SIG model with the given ID exists in the given element.

## [◆ ](#gadfb473db4b23902a192e12d322ff1fd2)bt\_mesh\_model\_find\_vnd()

| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* bt\_mesh\_model\_find\_vnd | ( | const struct [bt\_mesh\_elem](structbt__mesh__elem.md) \* | *elem*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *company*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id* ) |

`#include <[access.h](access_8h.md)>`

Find a vendor model.

Parameters
:   | elem | Element to search for the model in. |
    | --- | --- |
    | company | Company ID of the model. |
    | id | Model ID of the model. |

Returns
:   A pointer to the Mesh model matching the given parameters, or NULL if no vendor model with the given ID exists in the given element.

## [◆ ](#gaa8694fdab3f514d8051dad1cc7362ac9)bt\_mesh\_model\_in\_primary()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_model\_in\_primary | ( | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *mod* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

Get whether the model is in the primary element of the device.

Parameters
:   | mod | Mesh model. |
    | --- | --- |

Returns
:   true if the model is on the primary element, false otherwise.

## [◆ ](#ga10603a5846210a397f306b227ce10c2e)bt\_mesh\_model\_is\_extended()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_model\_is\_extended | ( | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *model* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

Check if model is extended by another model.

Parameters
:   | model | The model to check. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If model is extended by another model, otherwise false |
    | --- | --- |

## [◆ ](#ga1b961d45f8b7c231c698ca229115e434)bt\_mesh\_model\_pub\_is\_retransmission()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_model\_pub\_is\_retransmission | ( | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *model* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

Check if a message is being retransmitted.

Meant to be used inside the [bt\_mesh\_model\_pub::update](structbt__mesh__model__pub.md#a0354344e08e633dc4d6c0b4e7b169080 "bt_mesh_model_pub::update") callback.

Parameters
:   | model | Mesh Model that supports publication. |
    | --- | --- |

Returns
:   true if this is a retransmission, false if this is a first publication.

## [◆ ](#ga06644f8a5fa43351328d3f3403dbad03)bt\_mesh\_model\_publish()

| int bt\_mesh\_model\_publish | ( | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *model* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

Send a model publication message.

Before calling this function, the user needs to ensure that the model publication message ([bt\_mesh\_model\_pub::msg](structbt__mesh__model__pub.md#a5f5639c01d3704ec3d527c418d35f827 "bt_mesh_model_pub::msg")) contains a valid message to be sent. Note that this API is only to be used for non-period publishing. For periodic publishing the app only needs to make sure that [bt\_mesh\_model\_pub::msg](structbt__mesh__model__pub.md#a5f5639c01d3704ec3d527c418d35f827 "bt_mesh_model_pub::msg") contains a valid message whenever the [bt\_mesh\_model\_pub::update](structbt__mesh__model__pub.md#a0354344e08e633dc4d6c0b4e7b169080 "bt_mesh_model_pub::update") callback is called.

Parameters
:   | model | Mesh (client) Model that's publishing the message. |
    | --- | --- |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga7cac052ef76f4b37a95343329b078e77)bt\_mesh\_model\_send()

| int bt\_mesh\_model\_send | ( | const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | *model*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \* | *ctx*, |
|  |  | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *msg*, |
|  |  | const struct [bt\_mesh\_send\_cb](structbt__mesh__send__cb.md) \* | *cb*, |
|  |  | void \* | *cb\_data* ) |

`#include <[access.h](access_8h.md)>`

Send an Access Layer message.

Parameters
:   | model | Mesh (client) Model that the message belongs to. |
    | --- | --- |
    | ctx | Message context, includes keys, TTL, etc. |
    | msg | Access Layer payload (the actual message to be sent). |
    | cb | Optional "message sent" callback. |
    | cb\_data | User data to be passed to the callback. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga26ac86bdd32d27e0091735d98670687a)bt\_mesh\_models\_metadata\_change\_prepare()

| int bt\_mesh\_models\_metadata\_change\_prepare | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[access.h](access_8h.md)>`

Indicate that the metadata will change on next bootup.

Tell the config server that the models metadata is expected to change on the next bootup, and the current models metadata should be backed up.

Returns
:   Zero on success or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
