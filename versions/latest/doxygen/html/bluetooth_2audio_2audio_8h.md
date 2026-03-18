---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bluetooth_2audio_2audio_8h.html
original_path: doxygen/html/bluetooth_2audio_2audio_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

audio.h File Reference

Bluetooth Audio handling.
[More...](#details)

`#include <[zephyr/sys/atomic.h](atomic_8h_source.md)>`  
`#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci.h](hci_8h_source.md)>`  
`#include <[zephyr/bluetooth/iso.h](iso_8h_source.md)>`  
`#include <[zephyr/bluetooth/gatt.h](gatt_8h_source.md)>`  
`#include <[zephyr/bluetooth/audio/lc3.h](lc3_8h_source.md)>`

[Go to the source code of this file.](bluetooth_2audio_2audio_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) |
| struct | [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) |
|  | Codec capability structure. [More...](structbt__audio__codec__cap.md#details) |
| struct | [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) |
|  | Codec specific configuration structure. [More...](structbt__audio__codec__cfg.md#details) |
| struct | [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) |
|  | Codec QoS structure. [More...](structbt__audio__codec__qos.md#details) |
| struct | [bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md) |
|  | Audio Stream Quality of Service Preference structure. [More...](structbt__audio__codec__qos__pref.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_AUDIO\_BROADCAST\_ID\_SIZE](group__bt__audio.md#ga18dd9f4a4af7716dd01497309ff9c87c)   3 /\* octets \*/ |
| #define | [BT\_AUDIO\_BROADCAST\_ID\_MAX](group__bt__audio.md#ga3ed5ba09ab4c1ab7a59f8a1b4deee791)   0xFFFFFFU |
|  | Maximum broadcast ID value. |
| #define | [BT\_AUDIO\_PD\_PREF\_NONE](group__bt__audio.md#ga663ab7bf74d56f36ee6cc80b369cbc16)   0x000000U |
|  | Indicates that the server have no preference for the presentation delay. |
| #define | [BT\_AUDIO\_PD\_MAX](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc)   0xFFFFFFU |
|  | Maximum presentation delay in microseconds. |
| #define | [BT\_AUDIO\_BROADCAST\_CODE\_SIZE](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)   16 |
| #define | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MIN](group__bt__audio.md#gac1251f8a35b5e343eeeff87f22f8ab10)   1 |
|  | Minimum supported channel counts. |
| #define | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MAX](group__bt__audio.md#gad91341739d394f92ffc4988b614f47b6)   8 |
|  | Maximum supported channel counts. |
| #define | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT](group__bt__audio.md#ga8f835266fabd6461216fe13e1b3b3a0f)(...) |
|  | Channel count support capability. |
| #define | [BT\_AUDIO\_CONTEXT\_TYPE\_ANY](group__bt__audio.md#ga6320f86aab9b227385bdf52a9ff3985b) |
|  | Any known context. |
| #define | [BT\_AUDIO\_METADATA\_TYPE\_IS\_KNOWN](group__bt__audio.md#ga86a7e9ca661a3b13b7c59d41d206156e)(\_type) |
|  | Helper to check whether metadata type is known by the stack. |
| #define | [BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_GENERAL](group__bt__audio.md#ga41db714fa87e85896a52427399633bb4)   0x00 |
| #define | [BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_TARGETED](group__bt__audio.md#ga56c14acb7f182a413fdecac4e271c5cc)   0x01 |
| #define | [BT\_AUDIO\_CODEC\_DATA](group__bt__audio.md#gaddc49e39465798ae4c0cbe345e0b50d7)(\_type, \_bytes...) |
|  | Helper to declare elements of [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md "Codec capability structure.") arrays. |
| #define | [BT\_AUDIO\_CODEC\_CFG](group__bt__audio.md#gaefed7a013e282c63c9b5cbbdcdc67448)(\_id, \_cid, \_vid, \_data, \_meta) |
|  | Helper to declare [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs"). |
| #define | [BT\_AUDIO\_CODEC\_CAP](group__bt__audio.md#ga6b99f589f6cdcd9e48a83f729a7a4698)(\_id, \_cid, \_vid, \_data, \_meta) |
|  | Helper to declare [Codec capability parsing APIs](group__bt__audio__codec__cap.md "Codec capability parsing APIs") structure. |
| #define | [BT\_AUDIO\_LOCATION\_ANY](group__bt__audio.md#ga90688f158fe999ed3aa9c759c8245fcc) |
|  | Any known location. |
| #define | [BT\_AUDIO\_CODEC\_QOS](group__bt__audio.md#ga13e5148d62cb364602f01c75a88b615b)(\_interval, \_framing, \_phy, \_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare elements of [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md "Codec QoS structure."). |
| #define | [BT\_AUDIO\_CODEC\_QOS\_UNFRAMED](group__bt__audio.md#gadfc744b32a0b40da9377bb3668004bc2)(\_interval, \_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare Input Unframed [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md "Codec QoS structure."). |
| #define | [BT\_AUDIO\_CODEC\_QOS\_FRAMED](group__bt__audio.md#gae2147bca922bf3effd072d67a6b5d635)(\_interval, \_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare Input Framed [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md "Codec QoS structure."). |
| #define | [BT\_AUDIO\_CODEC\_QOS\_PREF](group__bt__audio.md#gac48a47e5177754c2e6812eee440e6d42)(\_unframed\_supported, \_phy, \_rtn, \_latency, \_pd\_min, \_pd\_max, \_pref\_pd\_min, \_pref\_pd\_max) |
|  | Helper to declare elements of [bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md "bt_audio_codec_qos_pref"). |

| Enumerations | |
| --- | --- |
| enum | [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) {     [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b) = 0x01 , [BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510) = 0x02 , [BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191) = 0x03 , [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46) = 0x04 ,     [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41) = 0x05   } |
|  | Codec capability types. [More...](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) |
| enum | [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) {     [BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83) = BIT(0) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81) = BIT(1) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361) = BIT(2) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982) = BIT(3) ,     [BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956) = BIT(4) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c) = BIT(5) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3) = BIT(6) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91) = BIT(7) ,     [BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211) = BIT(8) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663) = BIT(9) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b) = BIT(10) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890) = BIT(11) ,     [BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2) = BIT(12) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02)   } |
|  | Supported frequencies bitfield. [More...](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) |
| enum | [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) {     [BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) = BIT(0) , [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b) = BIT(1) , [BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a) , [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91) = BIT(4) ,     [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e) = BIT(5)   } |
|  | Supported frame durations bitfield. [More...](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) |
| enum | [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) {     [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc) = BIT(0) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd) = BIT(1) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39) = BIT(2) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2) = BIT(3) ,     [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51) = BIT(4) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8) = BIT(5) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82) = BIT(6) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943) = BIT(7) ,     [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219)   } |
| enum | [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) {     [BT\_AUDIO\_CODEC\_CFG\_FREQ](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3) = 0x01 , [BT\_AUDIO\_CODEC\_CFG\_DURATION](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223) = 0x02 , [BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2) = 0x03 , [BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2) = 0x04 ,     [BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8) = 0x05   } |
|  | Codec configuration types. [More...](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) |
| enum | [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) {     [BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a) = 0x01 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8) = 0x02 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245) = 0x03 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048) = 0x04 ,     [BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275) = 0x05 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e) = 0x06 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84) = 0x07 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11) = 0x08 ,     [BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409) = 0x09 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60) = 0x0a , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126) = 0x0b , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7) = 0x0c ,     [BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4) = 0x0d   } |
| enum | [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) { [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272) = 0x00 , [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7) = 0x01 } |
| enum | [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) {     [BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a) = 0 , [BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5) = BIT(0) , [BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e) = BIT(1) , [BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e) = BIT(2) ,     [BT\_AUDIO\_CONTEXT\_TYPE\_GAME](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730) = BIT(3) , [BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4) = BIT(4) , [BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e) = BIT(5) , [BT\_AUDIO\_CONTEXT\_TYPE\_LIVE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55) = BIT(6) ,     [BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9) = BIT(7) , [BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377) = BIT(8) , [BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3) = BIT(9) , [BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6) = BIT(10) ,     [BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1) = BIT(11)   } |
|  | Audio Context Type for Generic Audio. [More...](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) |
| enum | [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) {     [BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c) = 0x00 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1) = 0x01 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526) = 0x02 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc) = 0x03 ,     [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a) = 0x04 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4) = 0x05 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd) = 0x06 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2) = 0x07 ,     [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0) = 0x08 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7) = 0x09 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d) = 0x0A , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86) = 0x0B ,     [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077) = 0x0C , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92) = 0x0D , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff) = 0x0E , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071) = 0x0F   } |
|  | Parental rating defined by the Generic Audio assigned numbers (bluetooth.com). [More...](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) |
| enum | [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) { [BT\_AUDIO\_ACTIVE\_STATE\_DISABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3) = 0x00 , [BT\_AUDIO\_ACTIVE\_STATE\_ENABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940) = 0x01 } |
|  | Audio Active State defined by the Generic Audio assigned numbers (bluetooth.com). [More...](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) |
| enum | [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) {     [BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a) = 0x01 , [BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa) = 0x02 , [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7) = 0x03 , [BT\_AUDIO\_METADATA\_TYPE\_STREAM\_LANG](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354ae98c430a422e3583d19d1b391b97edda) = 0x04 ,     [BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b) = 0x05 , [BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613) = 0x06 , [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922) = 0x07 , [BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc) = 0x08 ,     [BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1) = 0x09 , [BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39) = 0xFE , [BT\_AUDIO\_METADATA\_TYPE\_VENDOR](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286) = 0xFF   } |
|  | Codec metadata type IDs. [More...](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) |
| enum | [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) {     [BT\_AUDIO\_LOCATION\_MONO\_AUDIO](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df) = 0 , [BT\_AUDIO\_LOCATION\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b) = BIT(0) , [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3) = BIT(1) , [BT\_AUDIO\_LOCATION\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337) = BIT(2) ,     [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6) = BIT(3) , [BT\_AUDIO\_LOCATION\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896) = BIT(4) , [BT\_AUDIO\_LOCATION\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa) = BIT(5) , [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e) = BIT(6) ,     [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692) = BIT(7) , [BT\_AUDIO\_LOCATION\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983) = BIT(8) , [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b) = BIT(9) , [BT\_AUDIO\_LOCATION\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064) = BIT(10) ,     [BT\_AUDIO\_LOCATION\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd) = BIT(11) , [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9) = BIT(12) , [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d) = BIT(13) , [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e) = BIT(14) ,     [BT\_AUDIO\_LOCATION\_TOP\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f) = BIT(15) , [BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06) = BIT(16) , [BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69) = BIT(17) , [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6) = BIT(18) ,     [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59) = BIT(19) , [BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd) = BIT(20) , [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376) = BIT(21) , [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29) = BIT(22) ,     [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8) = BIT(23) , [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d) = BIT(24) , [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71) = BIT(25) , [BT\_AUDIO\_LOCATION\_LEFT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6) = BIT(26) ,     [BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e) = BIT(27)   } |
|  | Location values for BT Audio. [More...](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) |
| enum | [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) { [BT\_AUDIO\_DIR\_SINK](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8) = 0x01 , [BT\_AUDIO\_DIR\_SOURCE](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c) = 0x02 } |
|  | Audio Capability type. [More...](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) |
| enum | [bt\_audio\_codec\_qos\_framing](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9) { [BT\_AUDIO\_CODEC\_QOS\_FRAMING\_UNFRAMED](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9a426ad2fe26f69d135beff6a367ef872f) = 0x00 , [BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9af7a4a07da9089c3afb248d63e3a9297a) = 0x01 } |
|  | Codec QoS Framing. [More...](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9) |
| enum | { [BT\_AUDIO\_CODEC\_QOS\_1M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ab387760c001ea6c81e889de55e74d5d5) = BIT(0) , [BT\_AUDIO\_CODEC\_QOS\_2M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ac81306188ed29b8fa17aa2afa878f297) = BIT(1) , [BT\_AUDIO\_CODEC\_QOS\_CODED](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0a9789c1b6b319370a3b98ab37b61a86e0) = BIT(2) } |
|  | Codec QoS Preferred PHY. [More...](group__bt__audio.md#gaa69a4789478a1a0aa93451d294de7ad0) |

| Functions | |
| --- | --- |
| int | [bt\_audio\_data\_parse](group__bt__audio.md#gafd8574b16141162c95653f0aa2bf6ff7) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ltv[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*func)(struct [bt\_data](structbt__data.md) \*data, void \*user\_data), void \*user\_data) |
|  | Helper for parsing length-type-value data. |
| int | [bt\_audio\_codec\_cfg\_freq\_to\_freq\_hz](group__bt__audio__codec__cfg.md#ga2e557fe726a49dc99754da16f7cc60af) (enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) freq) |
|  | Convert assigned numbers frequency to frequency value. |
| int | [bt\_audio\_codec\_cfg\_freq\_hz\_to\_freq](group__bt__audio__codec__cfg.md#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) freq\_hz) |
|  | Convert frequency value to assigned numbers frequency. |
| int | [bt\_audio\_codec\_cfg\_get\_freq](group__bt__audio__codec__cfg.md#gad8525a57d35e3e34ea591f7e20e2512d) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract the frequency from a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_set\_freq](group__bt__audio__codec__cfg.md#gac119989d5dcfa36becf4edd0ae7c6138) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) freq) |
|  | Set the frequency of a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_frame\_dur\_to\_frame\_dur\_us](group__bt__audio__codec__cfg.md#ga225e05df1f0d1efb709c972187901495) (enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) frame\_dur) |
|  | Convert assigned numbers frame duration to duration in microseconds. |
| int | [bt\_audio\_codec\_cfg\_frame\_dur\_us\_to\_frame\_dur](group__bt__audio__codec__cfg.md#ga0782a3d9254fb76b441c6c2492571556) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frame\_dur\_us) |
|  | Convert frame duration in microseconds to assigned numbers frame duration. |
| int | [bt\_audio\_codec\_cfg\_get\_frame\_dur](group__bt__audio__codec__cfg.md#ga2dd3afe41b22e989fb46614f89550007) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract frame duration from BT codec config. |
| int | [bt\_audio\_codec\_cfg\_set\_frame\_dur](group__bt__audio__codec__cfg.md#ga7d8306f98cb00f06e68a1df417825f0d) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) frame\_dur) |
|  | Set the frame duration of a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_get\_chan\_allocation](group__bt__audio__codec__cfg.md#ga93949a1b06ed1cc306c455825ebd94bd) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) \*chan\_allocation) |
|  | Extract channel allocation from BT codec config. |
| int | [bt\_audio\_codec\_cfg\_set\_chan\_allocation](group__bt__audio__codec__cfg.md#gafbbcd69fac18ed0201a5e0156209b049) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) chan\_allocation) |
|  | Set the channel allocation of a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_get\_octets\_per\_frame](group__bt__audio__codec__cfg.md#ga503be053422217502d6108b045791e02) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract frame size in octets from BT codec config. |
| int | [bt\_audio\_codec\_cfg\_set\_octets\_per\_frame](group__bt__audio__codec__cfg.md#ga866cdec28194056dc9e274d0436b45c2) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) octets\_per\_frame) |
|  | Set the octets per codec frame of a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_get\_frame\_blocks\_per\_sdu](group__bt__audio__codec__cfg.md#gadba0723f9d8a9546b659fba139051374) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fallback\_to\_default) |
|  | Extract number of audio frame blockss in each SDU from BT codec config. |
| int | [bt\_audio\_codec\_cfg\_set\_frame\_blocks\_per\_sdu](group__bt__audio__codec__cfg.md#gac9cf20bafbe24b34034bfb6ee7aaf03e) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) frame\_blocks) |
|  | Set the frame blocks per SDU of a codec configuration. |
| int | [bt\_audio\_codec\_cfg\_get\_val](group__bt__audio__codec__cfg.md#ga707c679db0193197b56acabfb08f8d1f) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
|  | Lookup a specific codec configuration value. |
| int | [bt\_audio\_codec\_cfg\_set\_val](group__bt__audio__codec__cfg.md#gab10f22938780530b1d1b95695382902e) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len) |
|  | Set or add a specific codec configuration value. |
| int | [bt\_audio\_codec\_cfg\_unset\_val](group__bt__audio__codec__cfg.md#gad3857d0ca008854df5966501caa261ba) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type) |
|  | Unset a specific codec configuration value. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_val](group__bt__audio__codec__cfg.md#gae98335e87394a491b4a311d867a5e32d) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
|  | Lookup a specific metadata value based on type. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_val](group__bt__audio__codec__cfg.md#ga3e24c2ba8de502600e647cb2f84e3ec4) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len) |
|  | Set or add a specific codec configuration metadata value. |
| int | [bt\_audio\_codec\_cfg\_meta\_unset\_val](group__bt__audio__codec__cfg.md#gab46f830daa1d9a907f47eb2a9eed7337) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type) |
|  | Unset a specific codec configuration metadata value. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_pref\_context](group__bt__audio__codec__cfg.md#ga5231504357bf52dda1912d3f065cc681) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract preferred contexts. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_pref\_context](group__bt__audio__codec__cfg.md#gab40bad609f17d24e7e0e9ffcebe4e912) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx) |
|  | Set the preferred context of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_stream\_context](group__bt__audio__codec__cfg.md#ga4cc4e1bb941206e7f1541a57fc92b8e9) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract stream contexts. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_stream\_context](group__bt__audio__codec__cfg.md#ga5cd2af1bb44c6eb5bafe824f005a77f0) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx) |
|  | Set the stream context of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_program\_info](group__bt__audio__codec__cfg.md#ga03284b8474d65443d7ecc8bdfc6f04c6) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info) |
|  | Extract program info. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_program\_info](group__bt__audio__codec__cfg.md#ga2ca9e616d20d7513c60ce905f046ac7b) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) program\_info\_len) |
|  | Set the program info of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_stream\_lang](group__bt__audio__codec__cfg.md#ga18b76dba57879b16b24f23b5b62a425c) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract stream language. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_stream\_lang](group__bt__audio__codec__cfg.md#gae2beb0c754a4956f04127aa353bb0949) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) stream\_lang) |
|  | Set the stream language of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_ccid\_list](group__bt__audio__codec__cfg.md#gaa0f9b9f608c7af881d5a928a3ae397b2) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ccid\_list) |
|  | Extract CCID list. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_ccid\_list](group__bt__audio__codec__cfg.md#ga59716b95fcea3404ff8c078564b0e29c) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ccid\_list, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ccid\_list\_len) |
|  | Set the CCID list of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_parental\_rating](group__bt__audio__codec__cfg.md#gaf0eecb02a05f0cc2b75ae9fb32c03913) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract parental rating. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_parental\_rating](group__bt__audio__codec__cfg.md#gab5d8b5877de4fe16c0e06a1d4f0d15ce) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating) |
|  | Set the parental rating of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_program\_info\_uri](group__bt__audio__codec__cfg.md#ga6bdbc0a0b929fdbdc75db479aec858df) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info\_uri) |
|  | Extract program info URI. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_program\_info\_uri](group__bt__audio__codec__cfg.md#ga99163729034e816eaef7195505d5ae20) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info\_uri, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) program\_info\_uri\_len) |
|  | Set the program info URI of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_audio\_active\_state](group__bt__audio__codec__cfg.md#ga0fd6e6baf1b4f22d60768aaed6f42e8e) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract audio active state. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_audio\_active\_state](group__bt__audio__codec__cfg.md#gaf869e7ce0c9dd467fb03e8503d36c58a) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set the audio active state of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cfg.md#ga66143aa7dcc726e06a12660b8f90fc5a) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Extract broadcast audio immediate rendering flag. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cfg.md#gaede61b65d2037c7fbf6c4c4e090990be) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg) |
|  | Set the broadcast audio immediate rendering flag of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_extended](group__bt__audio__codec__cfg.md#ga1f76f82bff63b876eb761a0bf0377428) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*extended\_meta) |
|  | Extract extended metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_extended](group__bt__audio__codec__cfg.md#gade9cb53287ab3356fb57ba8a454a3aad) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*extended\_meta, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) extended\_meta\_len) |
|  | Set the extended metadata of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_get\_vendor](group__bt__audio__codec__cfg.md#ga4a4982e3bd0e8c944b584196ef146f6c) (const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*vendor\_meta) |
|  | Extract vendor specific metadata. |
| int | [bt\_audio\_codec\_cfg\_meta\_set\_vendor](group__bt__audio__codec__cfg.md#ga6935d1c40b3178b0c8fa877ee93d1e53) (struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vendor\_meta, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) vendor\_meta\_len) |
|  | Set the vendor specific metadata of a codec configuration metadata. |
| int | [bt\_audio\_codec\_cap\_get\_val](group__bt__audio__codec__cap.md#gac3bf5dd414271bb1dcbc6590994cff6b) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
|  | Lookup a specific value based on type. |
| int | [bt\_audio\_codec\_cap\_set\_val](group__bt__audio__codec__cap.md#ga0c2c816b0b2b85aa5dd38f21caceea40) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len) |
|  | Set or add a specific codec capability value. |
| int | [bt\_audio\_codec\_cap\_unset\_val](group__bt__audio__codec__cap.md#gabc9962212ad65339ff02ba1389d5f9f8) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type) |
|  | Unset a specific codec capability value. |
| int | [bt\_audio\_codec\_cap\_get\_freq](group__bt__audio__codec__cap.md#gaa1dbf81c437c983af0144bf62433666c) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract the frequency from a codec capability. |
| int | [bt\_audio\_codec\_cap\_set\_freq](group__bt__audio__codec__cap.md#gac0655c0bd6552ab8a265076d7d0cd1b2) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) freq) |
|  | Set the supported frequencies of a codec capability. |
| int | [bt\_audio\_codec\_cap\_get\_frame\_dur](group__bt__audio__codec__cap.md#ga12336de7d908bda94427caee4dc080e0) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract the frequency from a codec capability. |
| int | [bt\_audio\_codec\_cap\_set\_frame\_dur](group__bt__audio__codec__cap.md#ga53e5df6cc4cfbed12b59a6a506657772) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) frame\_dur) |
|  | Set the frame duration of a codec capability. |
| int | [bt\_audio\_codec\_cap\_get\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#ga7a4b34dced3c5d7e11a20611bf4dee28) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract the frequency from a codec capability. |
| int | [bt\_audio\_codec\_cap\_set\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#gaf6b2717823f9f3136237ed6a6515449e) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) chan\_count) |
|  | Set the channel count of a codec capability. |
| int | [bt\_audio\_codec\_cap\_get\_octets\_per\_frame](group__bt__audio__codec__cap.md#gaa949089f2c6c143041e6cb61338e0ddc) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \*codec\_frame) |
|  | Extract the supported octets per codec frame from a codec capability. |
| int | [bt\_audio\_codec\_cap\_set\_octets\_per\_frame](group__bt__audio__codec__cap.md#gac1c42460cd3c55bbfbd467f84ab2d78d) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \*codec\_frame) |
|  | Set the octets per codec frame of a codec capability. |
| int | [bt\_audio\_codec\_cap\_get\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga4904184e69994ebb4c5f8a39150fcaa1) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract the maximum codec frames per SDU from a codec capability. |
| int | [bt\_audio\_codec\_cap\_set\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga3785bc41f56f8f2a09248396dadb31da) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) codec\_frames\_per\_sdu) |
|  | Set the maximum codec frames per SDU of a codec capability. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_val](group__bt__audio__codec__cap.md#ga5c2ecbb4d0cef26dd2cc5d023e70a163) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
|  | Lookup a specific metadata value based on type. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_val](group__bt__audio__codec__cap.md#ga1fdfd8c36f4131bcf4ffd2b7f176b631) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len) |
|  | Set or add a specific codec capability metadata value. |
| int | [bt\_audio\_codec\_cap\_meta\_unset\_val](group__bt__audio__codec__cap.md#ga40848f5375d1e58622c580112c282f2e) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type) |
|  | Unset a specific codec capability metadata value. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_pref\_context](group__bt__audio__codec__cap.md#gaaa8c6783241b1b70349354b3e36c696c) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract preferred contexts. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_pref\_context](group__bt__audio__codec__cap.md#ga7fe0d4553d6accf5c89645cbf86149bf) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx) |
|  | Set the preferred context of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_stream\_context](group__bt__audio__codec__cap.md#ga88ee657b5bd3f847bb75c9620ddb142f) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract stream contexts. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_stream\_context](group__bt__audio__codec__cap.md#ga5cc7f360049c38c8de631ea33dbc44ab) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx) |
|  | Set the stream context of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_program\_info](group__bt__audio__codec__cap.md#ga33725c3b2c06d6c22030bb5a77d702b0) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info) |
|  | Extract program info. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_program\_info](group__bt__audio__codec__cap.md#ga43d2ec3a4d621c26843de82db7fd2189) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) program\_info\_len) |
|  | Set the program info of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_stream\_lang](group__bt__audio__codec__cap.md#gac78eba1117ba8ef0c2bb02c10c09b363) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract stream language. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_stream\_lang](group__bt__audio__codec__cap.md#ga56ee81c8a9e0eaedb04a7b732d4b7a36) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) stream\_lang) |
|  | Set the stream language of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_ccid\_list](group__bt__audio__codec__cap.md#ga3095dea36e60e75cbfe786d3c2f11866) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ccid\_list) |
|  | Extract CCID list. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_ccid\_list](group__bt__audio__codec__cap.md#ga00a8ad22713dab761c81d1b8481c037d) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ccid\_list, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ccid\_list\_len) |
|  | Set the CCID list of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_parental\_rating](group__bt__audio__codec__cap.md#gab34d0369ce08efcd407d33956d32632e) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract parental rating. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_parental\_rating](group__bt__audio__codec__cap.md#ga5e267dfad978cd3d52be9c31a4fac0be) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating) |
|  | Set the parental rating of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_program\_info\_uri](group__bt__audio__codec__cap.md#gadb39b0ee1f65cdd2457fdf2c3142c040) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info\_uri) |
|  | Extract program info URI. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_program\_info\_uri](group__bt__audio__codec__cap.md#gafbb0d6282d989e8bc70caada2845b337) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info\_uri, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) program\_info\_uri\_len) |
|  | Set the program info URI of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_audio\_active\_state](group__bt__audio__codec__cap.md#ga88bb1da63b7ea0f95dd236aa1024cfb8) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract audio active state. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_audio\_active\_state](group__bt__audio__codec__cap.md#gacd3de0306a22d1a1d9ba09b4ac4f4e09) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set the audio active state of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cap.md#gab4ccc7cb7d779acb20185ae808dd8bbe) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Extract broadcast audio immediate rendering flag. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cap.md#gaa1d382b4fa53f7cbe8426df53a3317ce) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Set the broadcast audio immediate rendering flag of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_extended](group__bt__audio__codec__cap.md#ga69aecd7e98f90a5162ff8ea3373b43d4) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*extended\_meta) |
|  | Extract extended metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_extended](group__bt__audio__codec__cap.md#gac00aabc7329027852a7caf5cdff2bc26) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*extended\_meta, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) extended\_meta\_len) |
|  | Set the extended metadata of a codec capability metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_get\_vendor](group__bt__audio__codec__cap.md#gab8c80a0f55041f026d453fd88cdeb727) (const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*vendor\_meta) |
|  | Extract vendor specific metadata. |
| int | [bt\_audio\_codec\_cap\_meta\_set\_vendor](group__bt__audio__codec__cap.md#ga1f06789782541beab9aab4914f91bb57) (struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vendor\_meta, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) vendor\_meta\_len) |
|  | Set the vendor specific metadata of a codec capability metadata. |

## Detailed Description

Bluetooth Audio handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [audio.h](bluetooth_2audio_2audio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
