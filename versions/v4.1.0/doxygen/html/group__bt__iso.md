---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__iso.html
original_path: doxygen/html/group__bt__iso.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Isochronous channels (ISO)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Isochronous channels (ISO).
[More...](#details)

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
| struct | [bt\_iso\_big\_cb](structbt__iso__big__cb.md) |
|  | Struct to hold the Broadcast Isochronous Group callbacks. [More...](structbt__iso__big__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_ISO\_CHAN\_SEND\_RESERVE](#ga15c9cafd39e89f07eef115e147741098)   [BT\_BUF\_ISO\_SIZE](group__bt__buf.md#gaa820dee05a7202304e1aaa9a36386ca4)(0) |
|  | Headroom needed for outgoing ISO SDUs. |
| #define | [BT\_ISO\_SDU\_BUF\_SIZE](#ga3c0af738d118341da7d370aaa48a89d1)(mtu) |
|  | Helper to calculate needed buffer size for ISO SDUs. |
| #define | [BT\_ISO\_BIS\_INDEX\_BIT](#ga01b975b441fa5d8f039562ab66857bbf)(x) |
|  | Convert BIS index to bit. |
| #define | [BT\_ISO\_DATA\_PATH\_HCI](#gadd421c69edccfd695d728ded5feb6862)   0x00 |
|  | Value to set the ISO data path over HCi. |
| #define | [BT\_ISO\_SDU\_INTERVAL\_UNKNOWN](#ga4f0cc6262171fbee9d0ef173123b8f3d)   0x000000U |
|  | Unknown SDU interval. |
| #define | [BT\_ISO\_SDU\_INTERVAL\_MIN](#ga8122de88b6e5423dca653b1f0a484316)   0x0000FFU |
|  | Minimum interval value in microseconds. |
| #define | [BT\_ISO\_SDU\_INTERVAL\_MAX](#ga077eb6d219bba947d363e2cce8e0080c)   0x0FFFFFU |
|  | Maximum interval value in microseconds. |
| #define | [BT\_ISO\_ISO\_INTERVAL\_MIN](#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de)   0x0004U |
|  | Minimum ISO interval (N \* 1.25 ms). |
| #define | [BT\_ISO\_ISO\_INTERVAL\_MAX](#gabc381a7f565061ec91d23b7783521da3)   0x0C80U |
|  | Maximum ISO interval (N \* 1.25 ms). |
| #define | [BT\_ISO\_LATENCY\_MIN](#ga77ae350543eb05617c590c0ad9cb0048)   0x0005 |
|  | Minimum latency value in milliseconds. |
| #define | [BT\_ISO\_LATENCY\_MAX](#gad5e89d05d8706509d8d9d8dac40e3347)   0x0FA0 |
|  | Maximum latency value in milliseconds. |
| #define | [BT\_ISO\_PACKING\_SEQUENTIAL](#ga6275e8d805e2366522a78f18ca47ac19)   0x00 |
|  | Packets will be sent sequentially between the channels in the group. |
| #define | [BT\_ISO\_PACKING\_INTERLEAVED](#ga35b037fcce858857642b4c54bae8dd79)   0x01 |
|  | Packets will be sent interleaved between the channels in the group. |
| #define | [BT\_ISO\_FRAMING\_UNFRAMED](#ga696a81180ae25aa686a53b73e352c9d2)   0x00 |
|  | Packets may be framed or unframed. |
| #define | [BT\_ISO\_FRAMING\_FRAMED](#ga8f9aba389529ad2a3667ca378e99de2b)   0x01 |
|  | Packets are always framed. |
| #define | [BT\_ISO\_MAX\_GROUP\_ISO\_COUNT](#gae9dc30b300e2c309d646e3227e8cc00e)   0x1F |
|  | Maximum number of isochronous channels in a single group. |
| #define | [BT\_ISO\_MIN\_SDU](#ga4cc5565eeda9a3661d49d485637d1db2)   0x0001 |
|  | Minimum SDU size. |
| #define | [BT\_ISO\_MAX\_SDU](#gaa5d5588e7229db16219b0c44921bbcf7)   0x0FFF |
|  | Maximum SDU size. |
| #define | [BT\_ISO\_CONNECTED\_PDU\_MIN](#ga4e29d5966f959114754d62a8763c8c1e)   0x0000U |
|  | Minimum PDU size. |
| #define | [BT\_ISO\_BROADCAST\_PDU\_MIN](#gaee766ff789f1bf01f75c88112ddd2afa)   0x0001U |
|  | Minimum PDU size. |
| #define | [BT\_ISO\_PDU\_MAX](#ga88fb5690cd1cab4e5e8d5c025cc1af00)   0x00FBU |
|  | Maximum PDU size. |
| #define | [BT\_ISO\_BN\_MIN](#ga2905cddfa456fc846f0c8025487b404d)   0x01U |
|  | Minimum burst number. |
| #define | [BT\_ISO\_BN\_MAX](#gac05f4f51ea04962679f616bb167b724d)   0x0FU |
|  | Maximum burst number. |
| #define | [BT\_ISO\_FT\_MIN](#ga2d3bde6b34f6b15474926ed97ad11d98)   0x01U |
|  | Minimum flush timeout. |
| #define | [BT\_ISO\_FT\_MAX](#ga011c9d5840658fd0ef244f47893ec70e)   0xFFU |
|  | Maximum flush timeout. |
| #define | [BT\_ISO\_NSE\_MIN](#ga3eba4c20b4203b0323b14178522e6159)   0x01U |
|  | Minimum number of subevents. |
| #define | [BT\_ISO\_NSE\_MAX](#gab7637d96bde7a41123b34f487eec3436)   0x1FU |
|  | Maximum number of subevents. |
| #define | [BT\_ISO\_SYNC\_TIMEOUT\_MIN](#gaa1bd6484a248a6fb5abc31202e5076d4)   0x000A |
|  | Minimum BIG sync timeout value (N \* 10 ms). |
| #define | [BT\_ISO\_SYNC\_TIMEOUT\_MAX](#gaeb66806b649bf828afbd83d15c9823eb)   0x4000 |
|  | Maximum BIG sync timeout value (N \* 10 ms). |
| #define | [BT\_ISO\_SYNC\_MSE\_ANY](#ga47802144b8523b3d46af9ef97e744bbd)   0x00 |
|  | Controller controlled maximum subevent count value. |
| #define | [BT\_ISO\_SYNC\_MSE\_MIN](#gafef299e43e0f58ac23e1a1e75ccd0163)   0x01 |
|  | Minimum BIG sync maximum subevent count value. |
| #define | [BT\_ISO\_SYNC\_MSE\_MAX](#gafd6e7b48394d6f6c8ddd485927b02b4b)   0x1F |
|  | Maximum BIG sync maximum subevent count value. |
| #define | [BT\_ISO\_CONNECTED\_RTN\_MAX](#ga1b52aba83eff5d6ae14169d1d3afa1a7)   0xFF |
|  | Maximum connected ISO retransmission value. |
| #define | [BT\_ISO\_BROADCAST\_RTN\_MAX](#ga3a579a5d752d4b19dcb668dd7ef27333)   0x1E |
|  | Maximum broadcast ISO retransmission value. |
| #define | [BT\_ISO\_BROADCAST\_CODE\_SIZE](#ga5551cab9896764eec39b8e6102e561e5)   16 |
|  | Broadcast code size. |
| #define | [BT\_ISO\_BIS\_INDEX\_MIN](#ga0333b406b29a0a3c355db4f52815ff1a)   0x01 |
|  | Lowest BIS index. |
| #define | [BT\_ISO\_BIS\_INDEX\_MAX](#ga834652af6ceef1824799ab0bfa0e426f)   0x1F |
|  | Highest BIS index. |
| #define | [BT\_ISO\_IRC\_MIN](#ga52df7bd114b77872c084e28ca86e0b2e)   0x01U |
|  | Minimum Immediate Repetition Count. |
| #define | [BT\_ISO\_IRC\_MAX](#ga0f412f1593bcdcfa2b323b285bd508a4)   0x0FU |
|  | Maximum Immediate Repetition Count. |
| #define | [BT\_ISO\_PTO\_MIN](#ga3f19aaa432290d67fdf4911d1d044dd8)   0x00U |
|  | Minimum pre-transmission offset. |
| #define | [BT\_ISO\_PTO\_MAX](#ga27e812e35a1f12329310851eb9c056f2)   0x0FU |
|  | Maximum pre-transmission offset. |
| #define | [BT\_ISO\_SUBINTERVAL\_NONE](#ga4fb7985aa35292671abe881c1570c445)   0x00000000U |
|  | No subinterval. |
| #define | [BT\_ISO\_SUBINTERVAL\_UNKNOWN](#ga8085b01de2d1facb666215282690d674)   0xFFFFFFFFU |
|  | Unknown subinterval. |
| #define | [BT\_ISO\_VALID\_BIS\_BITFIELD](#ga9becee6d629b8f54f55d2264b6d1baef)(\_bis\_bitfield) |
|  | Check if ISO BIS bitfield is valid ([BT\_ISO\_BIS\_INDEX\_BIT(1)](#ga01b975b441fa5d8f039562ab66857bbf)|..|BT\_ISO\_BIS\_INDEX\_BIT(31)). |

| Enumerations | |
| --- | --- |
| enum | [bt\_iso\_state](#gaf2925460cc22cc4220dc376bcbee6201) {     [BT\_ISO\_STATE\_DISCONNECTED](#ggaf2925460cc22cc4220dc376bcbee6201af392f8825090c7beb304efc860a1911d) , [BT\_ISO\_STATE\_ENCRYPT\_PENDING](#ggaf2925460cc22cc4220dc376bcbee6201a3ff6aa78bb7ed364b46c1457555aaba5) , [BT\_ISO\_STATE\_CONNECTING](#ggaf2925460cc22cc4220dc376bcbee6201a4cb48a0a2a2ac37bbab5eded1bc3fd22) , [BT\_ISO\_STATE\_CONNECTED](#ggaf2925460cc22cc4220dc376bcbee6201acfa2a00a1c203418768ce789cd0cec7d) ,     [BT\_ISO\_STATE\_DISCONNECTING](#ggaf2925460cc22cc4220dc376bcbee6201aebc34f9c32f1cd5e3197c7edaf657340)   } |
|  | Life-span states of ISO channel. [More...](#gaf2925460cc22cc4220dc376bcbee6201) |
| enum | [bt\_iso\_chan\_type](#gafcbd720c67c6a6e5f1cae1395e1e06f0) { [BT\_ISO\_CHAN\_TYPE\_NONE](#ggafcbd720c67c6a6e5f1cae1395e1e06f0a58579ee03e3769501536826248758f17) , [BT\_ISO\_CHAN\_TYPE\_CONNECTED](#ggafcbd720c67c6a6e5f1cae1395e1e06f0aec07ed1b714b6c042c71ca5e96ff4cce) , [BT\_ISO\_CHAN\_TYPE\_BROADCASTER](#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b) , [BT\_ISO\_CHAN\_TYPE\_SYNC\_RECEIVER](#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2) } |
|  | ISO Channel Type. [More...](#gafcbd720c67c6a6e5f1cae1395e1e06f0) |
| enum | { [BT\_ISO\_FLAGS\_VALID](#gga2c62af103a71aa8f5f8aa103b1245866a143de2c153179b3c40aca51c016e6382) = BIT(0) , [BT\_ISO\_FLAGS\_ERROR](#gga2c62af103a71aa8f5f8aa103b1245866a5f0aa6e3150819821f800dd7376e2218) = BIT(1) , [BT\_ISO\_FLAGS\_LOST](#gga2c62af103a71aa8f5f8aa103b1245866a5e87d48b6e96275744590194b75396ff) = BIT(2) , [BT\_ISO\_FLAGS\_TS](#gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23) = BIT(3) } |
|  | ISO packet status flag bits. [More...](#ga2c62af103a71aa8f5f8aa103b1245866) |

| Functions | |
| --- | --- |
| int | [bt\_iso\_server\_register](#gaff0e52777b2140519c63b54b9618bca8) (struct [bt\_iso\_server](structbt__iso__server.md) \*server) |
|  | Register ISO server. |
| int | [bt\_iso\_server\_unregister](#ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6) (struct [bt\_iso\_server](structbt__iso__server.md) \*server) |
|  | Unregister ISO server. |
| int | [bt\_iso\_cig\_create](#gaea03fc251206f18de320506064c1631f) (const struct [bt\_iso\_cig\_param](structbt__iso__cig__param.md) \*param, struct bt\_iso\_cig \*\*out\_cig) |
|  | Creates a CIG as a central. |
| int | [bt\_iso\_cig\_reconfigure](#ga98f557c183a82066b81f0265c225bebe) (struct bt\_iso\_cig \*cig, const struct [bt\_iso\_cig\_param](structbt__iso__cig__param.md) \*param) |
|  | Reconfigure a CIG as a central. |
| int | [bt\_iso\_cig\_terminate](#gad4b6a7286593ff099117113b6ca996f8) (struct bt\_iso\_cig \*cig) |
|  | Terminates a CIG as a central. |
| int | [bt\_iso\_chan\_connect](#ga98953a261f3699b62cd19ab4977e0b4c) (const struct [bt\_iso\_connect\_param](structbt__iso__connect__param.md) \*param, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Connect ISO channels on ACL connections. |
| int | [bt\_iso\_chan\_disconnect](#ga94c5c788b099284219e5a303b4b8ea69) (struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan) |
|  | Disconnect connected ISO channel. |
| int | [bt\_iso\_chan\_send](#ga0dbb89a133011a833be7d18161471c6a) (struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num) |
|  | Send data to ISO channel without timestamp. |
| int | [bt\_iso\_chan\_send\_ts](#gab75b817770e3b685920587afde39d6cd) (struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts) |
|  | Send data to ISO channel with timestamp. |
| int | [bt\_iso\_chan\_get\_info](#ga75e58ed5bfa48f84000f1ce974d649c6) (const struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [bt\_iso\_info](structbt__iso__info.md) \*info) |
|  | Get ISO channel info. |
| int | [bt\_iso\_chan\_get\_tx\_sync](#gaa3942147fdeebc36039cc35c4e984411) (const struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info) |
|  | Get ISO transmission timing info. |
| int | [bt\_iso\_big\_register\_cb](#ga8a01a56e4a4555ed65a67065facfca76) (struct [bt\_iso\_big\_cb](structbt__iso__big__cb.md) \*cb) |
|  | Registers callbacks for Broadcast Sources. |
| int | [bt\_iso\_big\_create](#gac9937316382d257493c7d0359f1341f5) (struct bt\_le\_ext\_adv \*padv, struct [bt\_iso\_big\_create\_param](structbt__iso__big__create__param.md) \*param, struct bt\_iso\_big \*\*out\_big) |
|  | Creates a BIG as a broadcaster. |
| int | [bt\_iso\_big\_terminate](#gab9c06a86bf5cc023f5f9bd16c5d3265b) (struct bt\_iso\_big \*big) |
|  | Terminates a BIG as a broadcaster or receiver. |
| int | [bt\_iso\_big\_sync](#ga790cfeb8516020f317802e019dca4754) (struct bt\_le\_per\_adv\_sync \*sync, struct [bt\_iso\_big\_sync\_param](structbt__iso__big__sync__param.md) \*param, struct bt\_iso\_big \*\*out\_big) |
|  | Creates a BIG as a receiver. |

## Detailed Description

Isochronous channels (ISO).

Since
:   2.3

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga01b975b441fa5d8f039562ab66857bbf)BT\_ISO\_BIS\_INDEX\_BIT

| #define BT\_ISO\_BIS\_INDEX\_BIT | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iso.h](iso_8h.md)>`

**Value:**

([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)((x) - 1))

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

Convert BIS index to bit.

The BIS indexes start from 0x01, so the lowest allowed bit is [BIT(0)](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language).") that represents index 0x01. To synchronize to e.g. BIS indexes 0x01 and 0x02, the bitfield value should be [BIT(0)](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language).") | [BIT(1)](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language)."). As a general notation, to sync to BIS index N use BIT(N - 1).

## [◆ ](#ga834652af6ceef1824799ab0bfa0e426f)BT\_ISO\_BIS\_INDEX\_MAX

| #define BT\_ISO\_BIS\_INDEX\_MAX   0x1F |
| --- |

`#include <[iso.h](iso_8h.md)>`

Highest BIS index.

## [◆ ](#ga0333b406b29a0a3c355db4f52815ff1a)BT\_ISO\_BIS\_INDEX\_MIN

| #define BT\_ISO\_BIS\_INDEX\_MIN   0x01 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Lowest BIS index.

## [◆ ](#gac05f4f51ea04962679f616bb167b724d)BT\_ISO\_BN\_MAX

| #define BT\_ISO\_BN\_MAX   0x0FU |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum burst number.

## [◆ ](#ga2905cddfa456fc846f0c8025487b404d)BT\_ISO\_BN\_MIN

| #define BT\_ISO\_BN\_MIN   0x01U |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum burst number.

## [◆ ](#ga5551cab9896764eec39b8e6102e561e5)BT\_ISO\_BROADCAST\_CODE\_SIZE

| #define BT\_ISO\_BROADCAST\_CODE\_SIZE   16 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Broadcast code size.

## [◆ ](#gaee766ff789f1bf01f75c88112ddd2afa)BT\_ISO\_BROADCAST\_PDU\_MIN

| #define BT\_ISO\_BROADCAST\_PDU\_MIN   0x0001U |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum PDU size.

## [◆ ](#ga3a579a5d752d4b19dcb668dd7ef27333)BT\_ISO\_BROADCAST\_RTN\_MAX

| #define BT\_ISO\_BROADCAST\_RTN\_MAX   0x1E |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum broadcast ISO retransmission value.

## [◆ ](#ga15c9cafd39e89f07eef115e147741098)BT\_ISO\_CHAN\_SEND\_RESERVE

| #define BT\_ISO\_CHAN\_SEND\_RESERVE   [BT\_BUF\_ISO\_SIZE](group__bt__buf.md#gaa820dee05a7202304e1aaa9a36386ca4)(0) |
| --- |

`#include <[iso.h](iso_8h.md)>`

Headroom needed for outgoing ISO SDUs.

## [◆ ](#ga4e29d5966f959114754d62a8763c8c1e)BT\_ISO\_CONNECTED\_PDU\_MIN

| #define BT\_ISO\_CONNECTED\_PDU\_MIN   0x0000U |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum PDU size.

## [◆ ](#ga1b52aba83eff5d6ae14169d1d3afa1a7)BT\_ISO\_CONNECTED\_RTN\_MAX

| #define BT\_ISO\_CONNECTED\_RTN\_MAX   0xFF |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum connected ISO retransmission value.

## [◆ ](#gadd421c69edccfd695d728ded5feb6862)BT\_ISO\_DATA\_PATH\_HCI

| #define BT\_ISO\_DATA\_PATH\_HCI   0x00 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Value to set the ISO data path over HCi.

## [◆ ](#ga8f9aba389529ad2a3667ca378e99de2b)BT\_ISO\_FRAMING\_FRAMED

| #define BT\_ISO\_FRAMING\_FRAMED   0x01 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Packets are always framed.

## [◆ ](#ga696a81180ae25aa686a53b73e352c9d2)BT\_ISO\_FRAMING\_UNFRAMED

| #define BT\_ISO\_FRAMING\_UNFRAMED   0x00 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Packets may be framed or unframed.

## [◆ ](#ga011c9d5840658fd0ef244f47893ec70e)BT\_ISO\_FT\_MAX

| #define BT\_ISO\_FT\_MAX   0xFFU |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum flush timeout.

## [◆ ](#ga2d3bde6b34f6b15474926ed97ad11d98)BT\_ISO\_FT\_MIN

| #define BT\_ISO\_FT\_MIN   0x01U |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum flush timeout.

## [◆ ](#ga0f412f1593bcdcfa2b323b285bd508a4)BT\_ISO\_IRC\_MAX

| #define BT\_ISO\_IRC\_MAX   0x0FU |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum Immediate Repetition Count.

## [◆ ](#ga52df7bd114b77872c084e28ca86e0b2e)BT\_ISO\_IRC\_MIN

| #define BT\_ISO\_IRC\_MIN   0x01U |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum Immediate Repetition Count.

## [◆ ](#gabc381a7f565061ec91d23b7783521da3)BT\_ISO\_ISO\_INTERVAL\_MAX

| #define BT\_ISO\_ISO\_INTERVAL\_MAX   0x0C80U |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum ISO interval (N \* 1.25 ms).

## [◆ ](#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de)BT\_ISO\_ISO\_INTERVAL\_MIN

| #define BT\_ISO\_ISO\_INTERVAL\_MIN   0x0004U |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum ISO interval (N \* 1.25 ms).

## [◆ ](#gad5e89d05d8706509d8d9d8dac40e3347)BT\_ISO\_LATENCY\_MAX

| #define BT\_ISO\_LATENCY\_MAX   0x0FA0 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum latency value in milliseconds.

## [◆ ](#ga77ae350543eb05617c590c0ad9cb0048)BT\_ISO\_LATENCY\_MIN

| #define BT\_ISO\_LATENCY\_MIN   0x0005 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum latency value in milliseconds.

## [◆ ](#gae9dc30b300e2c309d646e3227e8cc00e)BT\_ISO\_MAX\_GROUP\_ISO\_COUNT

| #define BT\_ISO\_MAX\_GROUP\_ISO\_COUNT   0x1F |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum number of isochronous channels in a single group.

## [◆ ](#gaa5d5588e7229db16219b0c44921bbcf7)BT\_ISO\_MAX\_SDU

| #define BT\_ISO\_MAX\_SDU   0x0FFF |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum SDU size.

## [◆ ](#ga4cc5565eeda9a3661d49d485637d1db2)BT\_ISO\_MIN\_SDU

| #define BT\_ISO\_MIN\_SDU   0x0001 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum SDU size.

## [◆ ](#gab7637d96bde7a41123b34f487eec3436)BT\_ISO\_NSE\_MAX

| #define BT\_ISO\_NSE\_MAX   0x1FU |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum number of subevents.

## [◆ ](#ga3eba4c20b4203b0323b14178522e6159)BT\_ISO\_NSE\_MIN

| #define BT\_ISO\_NSE\_MIN   0x01U |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum number of subevents.

## [◆ ](#ga35b037fcce858857642b4c54bae8dd79)BT\_ISO\_PACKING\_INTERLEAVED

| #define BT\_ISO\_PACKING\_INTERLEAVED   0x01 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Packets will be sent interleaved between the channels in the group.

## [◆ ](#ga6275e8d805e2366522a78f18ca47ac19)BT\_ISO\_PACKING\_SEQUENTIAL

| #define BT\_ISO\_PACKING\_SEQUENTIAL   0x00 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Packets will be sent sequentially between the channels in the group.

## [◆ ](#ga88fb5690cd1cab4e5e8d5c025cc1af00)BT\_ISO\_PDU\_MAX

| #define BT\_ISO\_PDU\_MAX   0x00FBU |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum PDU size.

## [◆ ](#ga27e812e35a1f12329310851eb9c056f2)BT\_ISO\_PTO\_MAX

| #define BT\_ISO\_PTO\_MAX   0x0FU |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum pre-transmission offset.

## [◆ ](#ga3f19aaa432290d67fdf4911d1d044dd8)BT\_ISO\_PTO\_MIN

| #define BT\_ISO\_PTO\_MIN   0x00U |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum pre-transmission offset.

## [◆ ](#ga3c0af738d118341da7d370aaa48a89d1)BT\_ISO\_SDU\_BUF\_SIZE

| #define BT\_ISO\_SDU\_BUF\_SIZE | ( |  | *mtu* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iso.h](iso_8h.md)>`

**Value:**

[BT\_BUF\_ISO\_SIZE](group__bt__buf.md#gaa820dee05a7202304e1aaa9a36386ca4)(mtu)

[BT\_BUF\_ISO\_SIZE](group__bt__buf.md#gaa820dee05a7202304e1aaa9a36386ca4)

#define BT\_BUF\_ISO\_SIZE(size)

Helper to calculate needed buffer size for HCI ISO packets.

**Definition** buf.h:70

Helper to calculate needed buffer size for ISO SDUs.

Useful for creating buffer pools.

Parameters
:   | mtu | Required ISO SDU size |
    | --- | --- |

Returns
:   Needed buffer size to match the requested ISO SDU MTU.

## [◆ ](#ga077eb6d219bba947d363e2cce8e0080c)BT\_ISO\_SDU\_INTERVAL\_MAX

| #define BT\_ISO\_SDU\_INTERVAL\_MAX   0x0FFFFFU |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum interval value in microseconds.

## [◆ ](#ga8122de88b6e5423dca653b1f0a484316)BT\_ISO\_SDU\_INTERVAL\_MIN

| #define BT\_ISO\_SDU\_INTERVAL\_MIN   0x0000FFU |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum interval value in microseconds.

## [◆ ](#ga4f0cc6262171fbee9d0ef173123b8f3d)BT\_ISO\_SDU\_INTERVAL\_UNKNOWN

| #define BT\_ISO\_SDU\_INTERVAL\_UNKNOWN   0x000000U |
| --- |

`#include <[iso.h](iso_8h.md)>`

Unknown SDU interval.

## [◆ ](#ga4fb7985aa35292671abe881c1570c445)BT\_ISO\_SUBINTERVAL\_NONE

| #define BT\_ISO\_SUBINTERVAL\_NONE   0x00000000U |
| --- |

`#include <[iso.h](iso_8h.md)>`

No subinterval.

## [◆ ](#ga8085b01de2d1facb666215282690d674)BT\_ISO\_SUBINTERVAL\_UNKNOWN

| #define BT\_ISO\_SUBINTERVAL\_UNKNOWN   0xFFFFFFFFU |
| --- |

`#include <[iso.h](iso_8h.md)>`

Unknown subinterval.

## [◆ ](#ga47802144b8523b3d46af9ef97e744bbd)BT\_ISO\_SYNC\_MSE\_ANY

| #define BT\_ISO\_SYNC\_MSE\_ANY   0x00 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Controller controlled maximum subevent count value.

## [◆ ](#gafd6e7b48394d6f6c8ddd485927b02b4b)BT\_ISO\_SYNC\_MSE\_MAX

| #define BT\_ISO\_SYNC\_MSE\_MAX   0x1F |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum BIG sync maximum subevent count value.

## [◆ ](#gafef299e43e0f58ac23e1a1e75ccd0163)BT\_ISO\_SYNC\_MSE\_MIN

| #define BT\_ISO\_SYNC\_MSE\_MIN   0x01 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum BIG sync maximum subevent count value.

## [◆ ](#gaeb66806b649bf828afbd83d15c9823eb)BT\_ISO\_SYNC\_TIMEOUT\_MAX

| #define BT\_ISO\_SYNC\_TIMEOUT\_MAX   0x4000 |
| --- |

`#include <[iso.h](iso_8h.md)>`

Maximum BIG sync timeout value (N \* 10 ms).

## [◆ ](#gaa1bd6484a248a6fb5abc31202e5076d4)BT\_ISO\_SYNC\_TIMEOUT\_MIN

| #define BT\_ISO\_SYNC\_TIMEOUT\_MIN   0x000A |
| --- |

`#include <[iso.h](iso_8h.md)>`

Minimum BIG sync timeout value (N \* 10 ms).

## [◆ ](#ga9becee6d629b8f54f55d2264b6d1baef)BT\_ISO\_VALID\_BIS\_BITFIELD

| #define BT\_ISO\_VALID\_BIS\_BITFIELD | ( |  | *\_bis\_bitfield* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iso.h](iso_8h.md)>`

**Value:**

((\_bis\_bitfield) != 0U && (\_bis\_bitfield) <= [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)([BT\_ISO\_BIS\_INDEX\_MAX](#ga834652af6ceef1824799ab0bfa0e426f)))

[BT\_ISO\_BIS\_INDEX\_MAX](#ga834652af6ceef1824799ab0bfa0e426f)

#define BT\_ISO\_BIS\_INDEX\_MAX

Highest BIS index.

**Definition** iso.h:136

[BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

Bit mask with bits 0 through n-1 (inclusive) set, or 0 if n is 0.

**Definition** util\_macro.h:68

Check if ISO BIS bitfield is valid ([BT\_ISO\_BIS\_INDEX\_BIT(1)](#ga01b975b441fa5d8f039562ab66857bbf)|..|BT\_ISO\_BIS\_INDEX\_BIT(31)).

Parameters
:   | \_bis\_bitfield | BIS index bitfield (uint32) |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#ga2c62af103a71aa8f5f8aa103b1245866)anonymous enum

| anonymous enum |
| --- |

`#include <[iso.h](iso_8h.md)>`

ISO packet status flag bits.

| Enumerator | |
| --- | --- |
| BT\_ISO\_FLAGS\_VALID | The ISO packet is valid. |
| BT\_ISO\_FLAGS\_ERROR | The ISO packet may possibly contain errors.  May be caused by a failed CRC check or if missing a part of the SDU. |
| BT\_ISO\_FLAGS\_LOST | The ISO packet was lost. |
| BT\_ISO\_FLAGS\_TS | Timestamp is valid.  If not set, then the [bt\_iso\_recv\_info.ts](structbt__iso__recv__info.md#a4bf778ae9be39eb4a740c2eb9670d98a "ISO timestamp.") value is not valid, and should not be used. |

## [◆ ](#gafcbd720c67c6a6e5f1cae1395e1e06f0)bt\_iso\_chan\_type

| enum [bt\_iso\_chan\_type](#gafcbd720c67c6a6e5f1cae1395e1e06f0) |
| --- |

`#include <[iso.h](iso_8h.md)>`

ISO Channel Type.

| Enumerator | |
| --- | --- |
| BT\_ISO\_CHAN\_TYPE\_NONE | No channel type. |
| BT\_ISO\_CHAN\_TYPE\_CONNECTED | Connected. |
| BT\_ISO\_CHAN\_TYPE\_BROADCASTER | Isochronous broadcaster. |
| BT\_ISO\_CHAN\_TYPE\_SYNC\_RECEIVER | Synchronized receiver. |

## [◆ ](#gaf2925460cc22cc4220dc376bcbee6201)bt\_iso\_state

| enum [bt\_iso\_state](#gaf2925460cc22cc4220dc376bcbee6201) |
| --- |

`#include <[iso.h](iso_8h.md)>`

Life-span states of ISO channel.

Used only by internal APIs dealing with setting channel to proper state depending on operational context.

| Enumerator | |
| --- | --- |
| BT\_ISO\_STATE\_DISCONNECTED | Channel disconnected. |
| BT\_ISO\_STATE\_ENCRYPT\_PENDING | Channel is pending ACL encryption before connecting. |
| BT\_ISO\_STATE\_CONNECTING | Channel in connecting state. |
| BT\_ISO\_STATE\_CONNECTED | Channel ready for upper layer traffic on it. |
| BT\_ISO\_STATE\_DISCONNECTING | Channel in disconnecting state. |

## Function Documentation

## [◆ ](#gac9937316382d257493c7d0359f1341f5)bt\_iso\_big\_create()

| int bt\_iso\_big\_create | ( | struct bt\_le\_ext\_adv \* | *padv*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_iso\_big\_create\_param](structbt__iso__big__create__param.md) \* | *param*, |
|  |  | struct bt\_iso\_big \*\* | *out\_big* ) |

`#include <[iso.h](iso_8h.md)>`

Creates a BIG as a broadcaster.

Parameters
:   | [in] | padv | Pointer to the periodic advertising object the BIGInfo shall be sent on. |
    | --- | --- | --- |
    | [in] | param | The parameters used to create and enable the BIG. The QOS parameters are determined by the QOS field of the first BIS in the BIS list of this parameter. |
    | [out] | out\_big | Broadcast Isochronous Group object on success. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga8a01a56e4a4555ed65a67065facfca76)bt\_iso\_big\_register\_cb()

| int bt\_iso\_big\_register\_cb | ( | struct [bt\_iso\_big\_cb](structbt__iso__big__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iso.h](iso_8h.md)>`

Registers callbacks for Broadcast Sources.

Parameters
:   | cb | Pointer to the callback structure. |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | if `cb` is NULL |
    | -EEXIST | if `cb` is already registered |

## [◆ ](#ga790cfeb8516020f317802e019dca4754)bt\_iso\_big\_sync()

| int bt\_iso\_big\_sync | ( | struct bt\_le\_per\_adv\_sync \* | *sync*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_iso\_big\_sync\_param](structbt__iso__big__sync__param.md) \* | *param*, |
|  |  | struct bt\_iso\_big \*\* | *out\_big* ) |

`#include <[iso.h](iso_8h.md)>`

Creates a BIG as a receiver.

Parameters
:   | [in] | sync | Pointer to the periodic advertising sync object the BIGInfo was received on. |
    | --- | --- | --- |
    | [in] | param | The parameters used to create and enable the BIG sync. |
    | [out] | out\_big | Broadcast Isochronous Group object on success. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gab9c06a86bf5cc023f5f9bd16c5d3265b)bt\_iso\_big\_terminate()

| int bt\_iso\_big\_terminate | ( | struct bt\_iso\_big \* | *big* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iso.h](iso_8h.md)>`

Terminates a BIG as a broadcaster or receiver.

Parameters
:   | big | Pointer to the BIG structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga98953a261f3699b62cd19ab4977e0b4c)bt\_iso\_chan\_connect()

| int bt\_iso\_chan\_connect | ( | const struct [bt\_iso\_connect\_param](structbt__iso__connect__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count* ) |

`#include <[iso.h](iso_8h.md)>`

Connect ISO channels on ACL connections.

Connect ISO channels. The ISO channels must have been initialized in a CIG first by calling [bt\_iso\_cig\_create()](#gaea03fc251206f18de320506064c1631f).

Once the connection is completed the channels' connected() callback will be called. If the connection is rejected disconnected() callback is called instead.

This function will also setup the ISO data path based on the `path` parameter of the [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md "bt_iso_chan_io_qos") for each channel.

Parameters
:   | param | Pointer to a connect parameter array with the ISO and ACL pointers. |
    | --- | --- |
    | count | Number of connect parameters. |

Return values
:   | 0 | Successfully started the connecting procedure. |
    | --- | --- |
    | -EINVAL | Invalid parameters were supplied. |
    | -EBUSY | Some ISO channels are already being connected. It is not possible to have multiple outstanding connection requests. May also be returned if `CONFIG_BT_SMP` is enabled and a pairing procedure is already in progress. |
    | -ENOBUFS | Not buffers available to send request to controller or if `CONFIG_BT_SMP` is enabled and no more keys could be stored. |
    | -ENOMEM | If `CONFIG_BT_SMP` is enabled and no more keys could be stored. |
    | -EIO | Controller rejected the request or if `CONFIG_BT_SMP` is enabled and pairing has timed out. |
    | -ENOTCONN | If `CONFIG_BT_SMP` is enabled the ACL is not connected. |

## [◆ ](#ga94c5c788b099284219e5a303b4b8ea69)bt\_iso\_chan\_disconnect()

| int bt\_iso\_chan\_disconnect | ( | struct [bt\_iso\_chan](structbt__iso__chan.md) \* | *chan* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iso.h](iso_8h.md)>`

Disconnect connected ISO channel.

Disconnect connected ISO channel.

If the device is a central and the connection is pending it will be canceled and as a result the channel [bt\_iso\_chan\_ops.disconnected()](structbt__iso__chan__ops.md#a2069849352019362e5dc7d68f835f359 "Channel disconnected callback.") callback is called.

If the device is a peripheral and the connection is pending it will be rejected, as a peripheral shall wait for a CIS Established event (which may trigger a [bt\_iso\_chan\_ops.disconnected()](structbt__iso__chan__ops.md#a2069849352019362e5dc7d68f835f359 "Channel disconnected callback.") callback in case of an error).

Regarding to input parameter, to get details see reference description to [bt\_iso\_chan\_connect()](#ga98953a261f3699b62cd19ab4977e0b4c) API.

Parameters
:   | chan | Channel object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga75e58ed5bfa48f84000f1ce974d649c6)bt\_iso\_chan\_get\_info()

| int bt\_iso\_chan\_get\_info | ( | const struct [bt\_iso\_chan](structbt__iso__chan.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_iso\_info](structbt__iso__info.md) \* | *info* ) |

`#include <[iso.h](iso_8h.md)>`

Get ISO channel info.

Parameters
:   | chan | Channel object. |
    | --- | --- |
    | info | Channel info object. |

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#gaa3942147fdeebc36039cc35c4e984411)bt\_iso\_chan\_get\_tx\_sync()

| int bt\_iso\_chan\_get\_tx\_sync | ( | const struct [bt\_iso\_chan](structbt__iso__chan.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \* | *info* ) |

`#include <[iso.h](iso_8h.md)>`

Get ISO transmission timing info.

Reads timing information for transmitted ISO packet on an ISO channel. The HCI\_LE\_Read\_ISO\_TX\_Sync HCI command is used to retrieve this information from the controller.

Note
:   An SDU must have already been successfully transmitted on the ISO channel for this function to return successfully.

Parameters
:   | [in] | chan | Channel object. |
    | --- | --- | --- |
    | [out] | info | Transmit info object. |

Returns
:   Zero on success or (negative) error code on failure.

## [◆ ](#ga0dbb89a133011a833be7d18161471c6a)bt\_iso\_chan\_send()

| int bt\_iso\_chan\_send | ( | struct [bt\_iso\_chan](structbt__iso__chan.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *seq\_num* ) |

`#include <[iso.h](iso_8h.md)>`

Send data to ISO channel without timestamp.

Send data from buffer to the channel. If credits are not available, buf will be queued and sent as and when credits are received from peer. Regarding to first input parameter, to get details see reference description to [bt\_iso\_chan\_connect()](#ga98953a261f3699b62cd19ab4977e0b4c) API.

Note
:   Buffer ownership is transferred to the stack in case of success, in case of an error the caller retains the ownership of the buffer.

Parameters
:   | chan | Channel object. |
    | --- | --- |
    | buf | Buffer containing data to be sent. |
    | seq\_num | Packet Sequence number. This value shall be incremented for each call to this function and at least once per SDU interval for a specific channel. |

Returns
:   Number of octets sent in case of success or negative value in case of error.

## [◆ ](#gab75b817770e3b685920587afde39d6cd)bt\_iso\_chan\_send\_ts()

| int bt\_iso\_chan\_send\_ts | ( | struct [bt\_iso\_chan](structbt__iso__chan.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *seq\_num*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *ts* ) |

`#include <[iso.h](iso_8h.md)>`

Send data to ISO channel with timestamp.

Send data from buffer to the channel. If credits are not available, buf will be queued and sent as and when credits are received from peer. Regarding to first input parameter, to get details see reference description to [bt\_iso\_chan\_connect()](#ga98953a261f3699b62cd19ab4977e0b4c) API.

Note
:   Buffer ownership is transferred to the stack in case of success, in case of an error the caller retains the ownership of the buffer.

Parameters
:   | chan | Channel object. |
    | --- | --- |
    | buf | Buffer containing data to be sent. |
    | seq\_num | Packet Sequence number. This value shall be incremented for each call to this function and at least once per SDU interval for a specific channel. |
    | ts | Timestamp of the SDU in microseconds (us). This value can be used to transmit multiple SDUs in the same SDU interval in a CIG or BIG. |

Returns
:   Number of octets sent in case of success or negative value in case of error.

## [◆ ](#gaea03fc251206f18de320506064c1631f)bt\_iso\_cig\_create()

| int bt\_iso\_cig\_create | ( | const struct [bt\_iso\_cig\_param](structbt__iso__cig__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct bt\_iso\_cig \*\* | *out\_cig* ) |

`#include <[iso.h](iso_8h.md)>`

Creates a CIG as a central.

This can called at any time, even before connecting to a remote device. This must be called before any connected isochronous stream (CIS) channel can be connected.

Once a CIG is created, the channels supplied in the `param` can be connected using [bt\_iso\_chan\_connect()](#ga98953a261f3699b62cd19ab4977e0b4c).

Parameters
:   | [in] | param | The parameters used to create and enable the CIG. |
    | --- | --- | --- |
    | [out] | out\_cig | Connected Isochronous Group object on success. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga98f557c183a82066b81f0265c225bebe)bt\_iso\_cig\_reconfigure()

| int bt\_iso\_cig\_reconfigure | ( | struct bt\_iso\_cig \* | *cig*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_iso\_cig\_param](structbt__iso__cig__param.md) \* | *param* ) |

`#include <[iso.h](iso_8h.md)>`

Reconfigure a CIG as a central.

This function can be used to update a CIG. It will update the group specific parameters, and, if supplied, change the QoS parameters of the individual CIS. If the cis\_channels in `param` contains CIS that was not originally in the call to [bt\_iso\_cig\_create()](#gaea03fc251206f18de320506064c1631f), these will be added to the group. It is not possible to remove any CIS from the group after creation.

This can be called at any time before connecting an ISO to a remote device. Once any CIS in the group has connected, the group cannot be changed.

Once a CIG is created, the channels supplied in the `param` can be connected using [bt\_iso\_chan\_connect()](#ga98953a261f3699b62cd19ab4977e0b4c).

Parameters
:   | cig | Connected Isochronous Group object. |
    | --- | --- |
    | param | The parameters used to reconfigure the CIG. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gad4b6a7286593ff099117113b6ca996f8)bt\_iso\_cig\_terminate()

| int bt\_iso\_cig\_terminate | ( | struct bt\_iso\_cig \* | *cig* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iso.h](iso_8h.md)>`

Terminates a CIG as a central.

All the CIS in the CIG shall be disconnected first.

Parameters
:   | cig | Pointer to the CIG structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaff0e52777b2140519c63b54b9618bca8)bt\_iso\_server\_register()

| int bt\_iso\_server\_register | ( | struct [bt\_iso\_server](structbt__iso__server.md) \* | *server* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iso.h](iso_8h.md)>`

Register ISO server.

Register ISO server, each new connection is authorized using the [accept()](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864) callback which in case of success shall allocate the channel structure to be used by the new connection.

Parameters
:   | server | Server structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6)bt\_iso\_server\_unregister()

| int bt\_iso\_server\_unregister | ( | struct [bt\_iso\_server](structbt__iso__server.md) \* | *server* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iso.h](iso_8h.md)>`

Unregister ISO server.

Unregister previously registered ISO server.

Parameters
:   | server | Server structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
