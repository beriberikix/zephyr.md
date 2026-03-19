---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/iso_8h.html
original_path: doxygen/html/iso_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iso.h File Reference

Bluetooth ISO handling.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/bluetooth/addr.h](addr_8h_source.md)>`  
`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`  
`#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci.h](hci_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](iso_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_iso\_chan](structbt__iso__chan.md) |
|  | ISO Channel structure. [More...](structbt__iso__chan.md#details) |
| struct | [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md) |
|  | ISO Channel IO QoS structure. [More...](structbt__iso__chan__io__qos.md#details) |
| struct | [bt\_iso\_chan\_qos](structbt__iso__chan__qos.md) |
|  | ISO Channel QoS structure. [More...](structbt__iso__chan__qos.md#details) |
| struct | [bt\_iso\_chan\_path](structbt__iso__chan__path.md) |
|  | ISO Channel Data Path structure. [More...](structbt__iso__chan__path.md#details) |
| struct | [bt\_iso\_recv\_info](structbt__iso__recv__info.md) |
|  | ISO Meta Data structure for received ISO packets. [More...](structbt__iso__recv__info.md#details) |
| struct | [bt\_iso\_tx\_info](structbt__iso__tx__info.md) |
|  | ISO Meta Data structure for transmitted ISO packets. [More...](structbt__iso__tx__info.md#details) |
| struct | [bt\_iso\_cig\_param](structbt__iso__cig__param.md) |
|  | Connected Isochronous Group (CIG) parameters. [More...](structbt__iso__cig__param.md#details) |
| struct | [bt\_iso\_connect\_param](structbt__iso__connect__param.md) |
|  | ISO connection parameters structure. [More...](structbt__iso__connect__param.md#details) |
| struct | [bt\_iso\_big\_create\_param](structbt__iso__big__create__param.md) |
|  | Broadcast Isochronous Group (BIG) creation parameters. [More...](structbt__iso__big__create__param.md#details) |
| struct | [bt\_iso\_big\_sync\_param](structbt__iso__big__sync__param.md) |
|  | Broadcast Isochronous Group (BIG) Sync Parameters. [More...](structbt__iso__big__sync__param.md#details) |
| struct | [bt\_iso\_biginfo](structbt__iso__biginfo.md) |
|  | Broadcast Isochronous Group (BIG) information. [More...](structbt__iso__biginfo.md#details) |
| struct | [bt\_iso\_chan\_ops](structbt__iso__chan__ops.md) |
|  | ISO Channel operations structure. [More...](structbt__iso__chan__ops.md#details) |
| struct | [bt\_iso\_accept\_info](structbt__iso__accept__info.md) |
|  | ISO Accept Info Structure. [More...](structbt__iso__accept__info.md#details) |
| struct | [bt\_iso\_server](structbt__iso__server.md) |
|  | ISO Server structure. [More...](structbt__iso__server.md#details) |
| struct | [bt\_iso\_unicast\_tx\_info](structbt__iso__unicast__tx__info.md) |
|  | ISO Unicast TX Info Structure. [More...](structbt__iso__unicast__tx__info.md#details) |
| struct | [bt\_iso\_unicast\_info](structbt__iso__unicast__info.md) |
|  | ISO Unicast Info Structure. [More...](structbt__iso__unicast__info.md#details) |
| struct | [bt\_iso\_broadcaster\_info](structbt__iso__broadcaster__info.md) |
|  | ISO Broadcaster Info Structure. [More...](structbt__iso__broadcaster__info.md#details) |
| struct | [bt\_iso\_sync\_receiver\_info](structbt__iso__sync__receiver__info.md) |
|  | ISO Synchronized Receiver Info Structure. [More...](structbt__iso__sync__receiver__info.md#details) |
| struct | [bt\_iso\_info](structbt__iso__info.md) |
|  | ISO channel Info Structure. [More...](structbt__iso__info.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_ISO\_CHAN\_SEND\_RESERVE](group__bt__iso.md#ga15c9cafd39e89f07eef115e147741098)   [BT\_BUF\_ISO\_SIZE](group__bt__buf.md#gaa820dee05a7202304e1aaa9a36386ca4)(0) |
|  | Headroom needed for outgoing ISO SDUs. |
| #define | [BT\_ISO\_SDU\_BUF\_SIZE](group__bt__iso.md#ga3c0af738d118341da7d370aaa48a89d1)(mtu) |
|  | Helper to calculate needed buffer size for ISO SDUs. |
| #define | [BT\_ISO\_BIS\_INDEX\_BIT](group__bt__iso.md#ga01b975b441fa5d8f039562ab66857bbf)(x) |
|  | Convert BIS index to bit. |
| #define | [BT\_ISO\_DATA\_PATH\_HCI](group__bt__iso.md#gadd421c69edccfd695d728ded5feb6862)   0x00 |
|  | Value to set the ISO data path over HCi. |
| #define | [BT\_ISO\_SDU\_INTERVAL\_MIN](group__bt__iso.md#ga8122de88b6e5423dca653b1f0a484316)   0x0000FFU |
|  | Minimum interval value in microseconds. |
| #define | [BT\_ISO\_SDU\_INTERVAL\_MAX](group__bt__iso.md#ga077eb6d219bba947d363e2cce8e0080c)   0x0FFFFFU |
|  | Maximum interval value in microseconds. |
| #define | [BT\_ISO\_ISO\_INTERVAL\_MIN](group__bt__iso.md#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de)   0x0004U |
|  | Minimum ISO interval (N \* 1.25 ms). |
| #define | [BT\_ISO\_ISO\_INTERVAL\_MAX](group__bt__iso.md#gabc381a7f565061ec91d23b7783521da3)   0x0C80U |
|  | Maximum ISO interval (N \* 1.25 ms). |
| #define | [BT\_ISO\_LATENCY\_MIN](group__bt__iso.md#ga77ae350543eb05617c590c0ad9cb0048)   0x0005 |
|  | Minimum latency value in milliseconds. |
| #define | [BT\_ISO\_LATENCY\_MAX](group__bt__iso.md#gad5e89d05d8706509d8d9d8dac40e3347)   0x0FA0 |
|  | Maximum latency value in milliseconds. |
| #define | [BT\_ISO\_PACKING\_SEQUENTIAL](group__bt__iso.md#ga6275e8d805e2366522a78f18ca47ac19)   0x00 |
|  | Packets will be sent sequentially between the channels in the group. |
| #define | [BT\_ISO\_PACKING\_INTERLEAVED](group__bt__iso.md#ga35b037fcce858857642b4c54bae8dd79)   0x01 |
|  | Packets will be sent interleaved between the channels in the group. |
| #define | [BT\_ISO\_FRAMING\_UNFRAMED](group__bt__iso.md#ga696a81180ae25aa686a53b73e352c9d2)   0x00 |
|  | Packets may be framed or unframed. |
| #define | [BT\_ISO\_FRAMING\_FRAMED](group__bt__iso.md#ga8f9aba389529ad2a3667ca378e99de2b)   0x01 |
|  | Packets are always framed. |
| #define | [BT\_ISO\_MAX\_GROUP\_ISO\_COUNT](group__bt__iso.md#gae9dc30b300e2c309d646e3227e8cc00e)   0x1F |
|  | Maximum number of isochronous channels in a single group. |
| #define | [BT\_ISO\_MIN\_SDU](group__bt__iso.md#ga4cc5565eeda9a3661d49d485637d1db2)   0x0001 |
|  | Minimum SDU size. |
| #define | [BT\_ISO\_MAX\_SDU](group__bt__iso.md#gaa5d5588e7229db16219b0c44921bbcf7)   0x0FFF |
|  | Maximum SDU size. |
| #define | [BT\_ISO\_CONNECTED\_PDU\_MIN](group__bt__iso.md#ga4e29d5966f959114754d62a8763c8c1e)   0x0000U |
|  | Minimum PDU size. |
| #define | [BT\_ISO\_BROADCAST\_PDU\_MIN](group__bt__iso.md#gaee766ff789f1bf01f75c88112ddd2afa)   0x0001U |
|  | Minimum PDU size. |
| #define | [BT\_ISO\_PDU\_MAX](group__bt__iso.md#ga88fb5690cd1cab4e5e8d5c025cc1af00)   0x00FBU |
|  | Maximum PDU size. |
| #define | [BT\_ISO\_BN\_MIN](group__bt__iso.md#ga2905cddfa456fc846f0c8025487b404d)   0x01U |
|  | Minimum burst number. |
| #define | [BT\_ISO\_BN\_MAX](group__bt__iso.md#gac05f4f51ea04962679f616bb167b724d)   0x0FU |
|  | Maximum burst number. |
| #define | [BT\_ISO\_FT\_MIN](group__bt__iso.md#ga2d3bde6b34f6b15474926ed97ad11d98)   0x01U |
|  | Minimum flush timeout. |
| #define | [BT\_ISO\_FT\_MAX](group__bt__iso.md#ga011c9d5840658fd0ef244f47893ec70e)   0xFFU |
|  | Maximum flush timeout. |
| #define | [BT\_ISO\_NSE\_MIN](group__bt__iso.md#ga3eba4c20b4203b0323b14178522e6159)   0x01U |
|  | Minimum number of subevents. |
| #define | [BT\_ISO\_NSE\_MAX](group__bt__iso.md#gab7637d96bde7a41123b34f487eec3436)   0x1FU |
|  | Maximum number of subevents. |
| #define | [BT\_ISO\_SYNC\_TIMEOUT\_MIN](group__bt__iso.md#gaa1bd6484a248a6fb5abc31202e5076d4)   0x000A |
|  | Minimum BIG sync timeout value (N \* 10 ms). |
| #define | [BT\_ISO\_SYNC\_TIMEOUT\_MAX](group__bt__iso.md#gaeb66806b649bf828afbd83d15c9823eb)   0x4000 |
|  | Maximum BIG sync timeout value (N \* 10 ms). |
| #define | [BT\_ISO\_SYNC\_MSE\_ANY](group__bt__iso.md#ga47802144b8523b3d46af9ef97e744bbd)   0x00 |
|  | Controller controlled maximum subevent count value. |
| #define | [BT\_ISO\_SYNC\_MSE\_MIN](group__bt__iso.md#gafef299e43e0f58ac23e1a1e75ccd0163)   0x01 |
|  | Minimum BIG sync maximum subevent count value. |
| #define | [BT\_ISO\_SYNC\_MSE\_MAX](group__bt__iso.md#gafd6e7b48394d6f6c8ddd485927b02b4b)   0x1F |
|  | Maximum BIG sync maximum subevent count value. |
| #define | [BT\_ISO\_CONNECTED\_RTN\_MAX](group__bt__iso.md#ga1b52aba83eff5d6ae14169d1d3afa1a7)   0xFF |
|  | Maximum connected ISO retransmission value. |
| #define | [BT\_ISO\_BROADCAST\_RTN\_MAX](group__bt__iso.md#ga3a579a5d752d4b19dcb668dd7ef27333)   0x1E |
|  | Maximum broadcast ISO retransmission value. |
| #define | [BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)   16 |
|  | Broadcast code size. |
| #define | [BT\_ISO\_BIS\_INDEX\_MIN](group__bt__iso.md#ga0333b406b29a0a3c355db4f52815ff1a)   0x01 |
|  | Lowest BIS index. |
| #define | [BT\_ISO\_BIS\_INDEX\_MAX](group__bt__iso.md#ga834652af6ceef1824799ab0bfa0e426f)   0x1F |
|  | Highest BIS index. |
| #define | [BT\_ISO\_IRC\_MIN](group__bt__iso.md#ga52df7bd114b77872c084e28ca86e0b2e)   0x01U |
|  | Minimum Immediate Repetition Count. |
| #define | [BT\_ISO\_IRC\_MAX](group__bt__iso.md#ga0f412f1593bcdcfa2b323b285bd508a4)   0x0FU |
|  | Maximum Immediate Repetition Count. |
| #define | [BT\_ISO\_PTO\_MIN](group__bt__iso.md#ga3f19aaa432290d67fdf4911d1d044dd8)   0x00U |
|  | Minimum pre-transmission offset. |
| #define | [BT\_ISO\_PTO\_MAX](group__bt__iso.md#ga27e812e35a1f12329310851eb9c056f2)   0x0FU |
|  | Maximum pre-transmission offset. |
| #define | [BT\_ISO\_VALID\_BIS\_BITFIELD](group__bt__iso.md#ga9becee6d629b8f54f55d2264b6d1baef)(\_bis\_bitfield) |
|  | Check if ISO BIS bitfield is valid ([BT\_ISO\_BIS\_INDEX\_BIT(1)](group__bt__iso.md#ga01b975b441fa5d8f039562ab66857bbf "Convert BIS index to bit.")|..|BT\_ISO\_BIS\_INDEX\_BIT(31)). |

| Enumerations | |
| --- | --- |
| enum | [bt\_iso\_state](group__bt__iso.md#gaf2925460cc22cc4220dc376bcbee6201) {     [BT\_ISO\_STATE\_DISCONNECTED](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201af392f8825090c7beb304efc860a1911d) , [BT\_ISO\_STATE\_ENCRYPT\_PENDING](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201a3ff6aa78bb7ed364b46c1457555aaba5) , [BT\_ISO\_STATE\_CONNECTING](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201a4cb48a0a2a2ac37bbab5eded1bc3fd22) , [BT\_ISO\_STATE\_CONNECTED](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201acfa2a00a1c203418768ce789cd0cec7d) ,     [BT\_ISO\_STATE\_DISCONNECTING](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201aebc34f9c32f1cd5e3197c7edaf657340)   } |
|  | Life-span states of ISO channel. [More...](group__bt__iso.md#gaf2925460cc22cc4220dc376bcbee6201) |
| enum | [bt\_iso\_chan\_type](group__bt__iso.md#gafcbd720c67c6a6e5f1cae1395e1e06f0) { [BT\_ISO\_CHAN\_TYPE\_NONE](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a58579ee03e3769501536826248758f17) , [BT\_ISO\_CHAN\_TYPE\_CONNECTED](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0aec07ed1b714b6c042c71ca5e96ff4cce) , [BT\_ISO\_CHAN\_TYPE\_BROADCASTER](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b) , [BT\_ISO\_CHAN\_TYPE\_SYNC\_RECEIVER](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2) } |
|  | ISO Channel Type. [More...](group__bt__iso.md#gafcbd720c67c6a6e5f1cae1395e1e06f0) |
| enum | { [BT\_ISO\_FLAGS\_VALID](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a143de2c153179b3c40aca51c016e6382) = BIT(0) , [BT\_ISO\_FLAGS\_ERROR](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a5f0aa6e3150819821f800dd7376e2218) = BIT(1) , [BT\_ISO\_FLAGS\_LOST](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a5e87d48b6e96275744590194b75396ff) = BIT(2) , [BT\_ISO\_FLAGS\_TS](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23) = BIT(3) } |
|  | ISO packet status flag bits. [More...](group__bt__iso.md#ga2c62af103a71aa8f5f8aa103b1245866) |

| Functions | |
| --- | --- |
| int | [bt\_iso\_server\_register](group__bt__iso.md#gaff0e52777b2140519c63b54b9618bca8) (struct [bt\_iso\_server](structbt__iso__server.md) \*server) |
|  | Register ISO server. |
| int | [bt\_iso\_server\_unregister](group__bt__iso.md#ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6) (struct [bt\_iso\_server](structbt__iso__server.md) \*server) |
|  | Unregister ISO server. |
| int | [bt\_iso\_cig\_create](group__bt__iso.md#gaea03fc251206f18de320506064c1631f) (const struct [bt\_iso\_cig\_param](structbt__iso__cig__param.md) \*param, struct bt\_iso\_cig \*\*out\_cig) |
|  | Creates a CIG as a central. |
| int | [bt\_iso\_cig\_reconfigure](group__bt__iso.md#ga98f557c183a82066b81f0265c225bebe) (struct bt\_iso\_cig \*cig, const struct [bt\_iso\_cig\_param](structbt__iso__cig__param.md) \*param) |
|  | Reconfigure a CIG as a central. |
| int | [bt\_iso\_cig\_terminate](group__bt__iso.md#gad4b6a7286593ff099117113b6ca996f8) (struct bt\_iso\_cig \*cig) |
|  | Terminates a CIG as a central. |
| int | [bt\_iso\_chan\_connect](group__bt__iso.md#ga98953a261f3699b62cd19ab4977e0b4c) (const struct [bt\_iso\_connect\_param](structbt__iso__connect__param.md) \*param, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Connect ISO channels on ACL connections. |
| int | [bt\_iso\_chan\_disconnect](group__bt__iso.md#ga94c5c788b099284219e5a303b4b8ea69) (struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan) |
|  | Disconnect connected ISO channel. |
| int | [bt\_iso\_chan\_send](group__bt__iso.md#ga0dbb89a133011a833be7d18161471c6a) (struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num) |
|  | Send data to ISO channel without timestamp. |
| int | [bt\_iso\_chan\_send\_ts](group__bt__iso.md#gab75b817770e3b685920587afde39d6cd) (struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts) |
|  | Send data to ISO channel with timestamp. |
| int | [bt\_iso\_chan\_get\_info](group__bt__iso.md#ga75e58ed5bfa48f84000f1ce974d649c6) (const struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [bt\_iso\_info](structbt__iso__info.md) \*info) |
|  | Get ISO channel info. |
| int | [bt\_iso\_chan\_get\_tx\_sync](group__bt__iso.md#gaa3942147fdeebc36039cc35c4e984411) (const struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info) |
|  | Get ISO transmission timing info. |
| int | [bt\_iso\_big\_create](group__bt__iso.md#gac9937316382d257493c7d0359f1341f5) (struct bt\_le\_ext\_adv \*padv, struct [bt\_iso\_big\_create\_param](structbt__iso__big__create__param.md) \*param, struct bt\_iso\_big \*\*out\_big) |
|  | Creates a BIG as a broadcaster. |
| int | [bt\_iso\_big\_terminate](group__bt__iso.md#gab9c06a86bf5cc023f5f9bd16c5d3265b) (struct bt\_iso\_big \*big) |
|  | Terminates a BIG as a broadcaster or receiver. |
| int | [bt\_iso\_big\_sync](group__bt__iso.md#ga790cfeb8516020f317802e019dca4754) (struct bt\_le\_per\_adv\_sync \*sync, struct [bt\_iso\_big\_sync\_param](structbt__iso__big__sync__param.md) \*param, struct bt\_iso\_big \*\*out\_big) |
|  | Creates a BIG as a receiver. |

## Detailed Description

Bluetooth ISO handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [iso.h](iso_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
