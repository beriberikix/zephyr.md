---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__audio.html
original_path: doxygen/html/group__bt__audio.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Audio

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Bluetooth Audio.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Assigned numbers to string API](group__bt__audio__to__str.md) |
|  | Assigned numbers to string API. |
|  | [Codec capability parsing APIs](group__bt__audio__codec__cap.md) |
|  | Audio codec capabilities APIs. |
|  | [Codec config parsing APIs](group__bt__audio__codec__cfg.md) |
|  | Audio codec Config APIs. |

| Data Structures | |
| --- | --- |
| struct | [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) |
|  | struct to hold minimum and maximum supported codec frame sizes [More...](structbt__audio__codec__octets__per__codec__frame.md#details) |
| struct | [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) |
|  | Codec capability structure. [More...](structbt__audio__codec__cap.md#details) |
| struct | [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) |
|  | Codec specific configuration structure. [More...](structbt__audio__codec__cfg.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_AUDIO\_BROADCAST\_ID\_SIZE](#ga18dd9f4a4af7716dd01497309ff9c87c)   3 |
|  | Size of the broadcast ID in octets. |
| #define | [BT\_AUDIO\_BROADCAST\_ID\_MAX](#ga3ed5ba09ab4c1ab7a59f8a1b4deee791)   0xFFFFFFU |
|  | Maximum broadcast ID value. |
| #define | [BT\_AUDIO\_PD\_PREF\_NONE](#ga663ab7bf74d56f36ee6cc80b369cbc16)   0x000000U |
|  | Indicates that the server have no preference for the presentation delay. |
| #define | [BT\_AUDIO\_PD\_MAX](#gaaa0414a4baef5a867fd1c6b1865d2dbc)   0xFFFFFFU |
|  | Maximum presentation delay in microseconds. |
| #define | [BT\_AUDIO\_RTN\_PREF\_NONE](#ga4a5fd440b96f4e4acbb791badef8c255)   0xFFU |
|  | Indicates that the unicast server does not have a preference for any retransmission number. |
| #define | [BT\_AUDIO\_BROADCAST\_NAME\_LEN\_MIN](#gaa3bf677a479a90793f28a5a3ed69c7e0)   4 |
|  | The minimum size of a Broadcast Name as defined by Bluetooth Assigned Numbers. |
| #define | [BT\_AUDIO\_BROADCAST\_NAME\_LEN\_MAX](#gaa2fafcbb6a826c3f4cee16ebb545dad6)   128 |
|  | The maximum size of a Broadcast Name as defined by Bluetooth Assigned Numbers. |
| #define | [BT\_AUDIO\_LANG\_SIZE](#gab6e5f793d514626deca21940d35d8f21)   3 |
|  | Size of the stream language value, e.g. |
| #define | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MIN](#gac1251f8a35b5e343eeeff87f22f8ab10)   1 |
|  | Minimum supported channel counts. |
| #define | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MAX](#gad91341739d394f92ffc4988b614f47b6)   8 |
|  | Maximum supported channel counts. |
| #define | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT](#ga8f835266fabd6461216fe13e1b3b3a0f)(...) |
|  | Channel count support capability. |
| #define | [BT\_AUDIO\_CONTEXT\_TYPE\_ANY](#ga6320f86aab9b227385bdf52a9ff3985b) |
|  | Any known context. |
| #define | [BT\_AUDIO\_METADATA\_TYPE\_IS\_KNOWN](#ga86a7e9ca661a3b13b7c59d41d206156e)(\_type) |
|  | Helper to check whether metadata type is known by the stack. |
| #define | [BT\_AUDIO\_CODEC\_DATA](#gaddc49e39465798ae4c0cbe345e0b50d7)(\_type, \_bytes...) |
|  | Helper to declare elements of [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md "Codec capability structure.") arrays. |
| #define | [BT\_AUDIO\_CODEC\_CFG](#gaefed7a013e282c63c9b5cbbdcdc67448)(\_id, \_cid, \_vid, \_data, \_meta) |
|  | Helper to declare [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs"). |
| #define | [BT\_AUDIO\_CODEC\_CAP](#ga6b99f589f6cdcd9e48a83f729a7a4698)(\_id, \_cid, \_vid, \_data, \_meta) |
|  | Helper to declare [Codec capability parsing APIs](group__bt__audio__codec__cap.md "Codec capability parsing APIs") structure. |
| #define | [BT\_AUDIO\_LOCATION\_ANY](#ga90688f158fe999ed3aa9c759c8245fcc) |
|  | Any known location. |

| Enumerations | |
| --- | --- |
| enum | [bt\_audio\_codec\_cap\_type](#gaf58823a56eb36cfd22e582ab1ea3d015) {     [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ](#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b) = 0x01 , [BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION](#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510) = 0x02 , [BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191) = 0x03 , [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN](#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46) = 0x04 ,     [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT](#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41) = 0x05   } |
|  | Codec capability types. [More...](#gaf58823a56eb36cfd22e582ab1ea3d015) |
| enum | [bt\_audio\_codec\_cap\_freq](#gaafc1106d5d305874ee2f540c850ff5b4) {     [BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83) = BIT(0) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81) = BIT(1) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361) = BIT(2) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982) = BIT(3) ,     [BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956) = BIT(4) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c) = BIT(5) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3) = BIT(6) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91) = BIT(7) ,     [BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211) = BIT(8) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663) = BIT(9) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b) = BIT(10) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890) = BIT(11) ,     [BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2) = BIT(12) , [BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY](#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02)   } |
|  | Supported frequencies bitfield. [More...](#gaafc1106d5d305874ee2f540c850ff5b4) |
| enum | [bt\_audio\_codec\_cap\_frame\_dur](#gaf37e8e19f956afb3c3a413cbaa1a21f5) {     [BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) = BIT(0) , [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b) = BIT(1) , [BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY](#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a) , [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5](#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91) = BIT(4) ,     [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10](#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e) = BIT(5)   } |
|  | Supported frame durations bitfield. [More...](#gaf37e8e19f956afb3c3a413cbaa1a21f5) |
| enum | [bt\_audio\_codec\_cap\_chan\_count](#gae695b5d17359967703f2509db1671fa5) {     [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc) = BIT(0) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd) = BIT(1) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39) = BIT(2) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2) = BIT(3) ,     [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51) = BIT(4) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8) = BIT(5) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82) = BIT(6) , [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943) = BIT(7) ,     [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY](#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219)   } |
|  | Supported audio capabilities channel count bitfield. [More...](#gae695b5d17359967703f2509db1671fa5) |
| enum | [bt\_audio\_codec\_cfg\_type](#ga9230ec4d7518bd243207ba2decb1a974) {     [BT\_AUDIO\_CODEC\_CFG\_FREQ](#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3) = 0x01 , [BT\_AUDIO\_CODEC\_CFG\_DURATION](#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223) = 0x02 , [BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC](#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2) = 0x03 , [BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN](#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2) = 0x04 ,     [BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU](#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8) = 0x05   } |
|  | Codec configuration types. [More...](#ga9230ec4d7518bd243207ba2decb1a974) |
| enum | [bt\_audio\_codec\_cfg\_freq](#ga8e99fb678cc011bb8c9f6e1858bae0d7) {     [BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a) = 0x01 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8) = 0x02 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245) = 0x03 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048) = 0x04 ,     [BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275) = 0x05 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e) = 0x06 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84) = 0x07 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11) = 0x08 ,     [BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409) = 0x09 , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60) = 0x0a , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126) = 0x0b , [BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7) = 0x0c ,     [BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ](#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4) = 0x0d   } |
|  | Codec configuration sampling freqency. [More...](#ga8e99fb678cc011bb8c9f6e1858bae0d7) |
| enum | [bt\_audio\_codec\_cfg\_frame\_dur](#ga83701b5eadfcbc9b84dc0b1a85ebeb74) { [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272) = 0x00 , [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7) = 0x01 } |
|  | Codec configuration frame duration. [More...](#ga83701b5eadfcbc9b84dc0b1a85ebeb74) |
| enum | [bt\_audio\_context](#gafb379ffa88388cc1397960155bbb2ab3) {     [BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a) = 0 , [BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5) = BIT(0) , [BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL](#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e) = BIT(1) , [BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA](#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e) = BIT(2) ,     [BT\_AUDIO\_CONTEXT\_TYPE\_GAME](#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730) = BIT(3) , [BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL](#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4) = BIT(4) , [BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS](#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e) = BIT(5) , [BT\_AUDIO\_CONTEXT\_TYPE\_LIVE](#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55) = BIT(6) ,     [BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS](#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9) = BIT(7) , [BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS](#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377) = BIT(8) , [BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE](#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3) = BIT(9) , [BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS](#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6) = BIT(10) ,     [BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM](#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1) = BIT(11)   } |
|  | Audio Context Type for Generic Audio. [More...](#gafb379ffa88388cc1397960155bbb2ab3) |
| enum | [bt\_audio\_parental\_rating](#ga6d4aff1f93dc0b902e4b5d1355f15760) {     [BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING](#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c) = 0x00 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY](#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1) = 0x01 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526) = 0x02 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc) = 0x03 ,     [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a) = 0x04 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4) = 0x05 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd) = 0x06 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2) = 0x07 ,     [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0) = 0x08 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7) = 0x09 , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d) = 0x0A , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86) = 0x0B ,     [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077) = 0x0C , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92) = 0x0D , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff) = 0x0E , [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE](#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071) = 0x0F   } |
|  | Parental rating defined by the Generic Audio assigned numbers (bluetooth.com). [More...](#ga6d4aff1f93dc0b902e4b5d1355f15760) |
| enum | [bt\_audio\_active\_state](#ga16d403ec4db7be997682331ad365ff5f) { [BT\_AUDIO\_ACTIVE\_STATE\_DISABLED](#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3) = 0x00 , [BT\_AUDIO\_ACTIVE\_STATE\_ENABLED](#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940) = 0x01 } |
|  | Audio Active State defined by the Generic Audio assigned numbers (bluetooth.com). [More...](#ga16d403ec4db7be997682331ad365ff5f) |
| enum | [bt\_audio\_assisted\_listening\_stream](#ga207fbf0fbca9b24cba02c7f1d184e7f5) { [BT\_AUDIO\_ASSISTED\_LISTENING\_STREAM\_UNSPECIFIED](#gga207fbf0fbca9b24cba02c7f1d184e7f5ab1714206feaa04b3be586ddb33ed5285) = 0x00 } |
|  | Assisted Listening Stream defined by the Generic Audio assigned numbers (bluetooth.com). [More...](#ga207fbf0fbca9b24cba02c7f1d184e7f5) |
| enum | [bt\_audio\_metadata\_type](#gab53d0dd62bceff97cf8eed7d8cf80354) {     [BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a) = 0x01 , [BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa) = 0x02 , [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO](#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7) = 0x03 , [BT\_AUDIO\_METADATA\_TYPE\_LANG](#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1) = 0x04 ,     [BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b) = 0x05 , [BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING](#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613) = 0x06 , [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI](#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922) = 0x07 , [BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE](#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc) = 0x08 ,     [BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1) = 0x09 , [BT\_AUDIO\_METADATA\_TYPE\_ASSISTED\_LISTENING\_STREAM](#ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf) = 0x0A , [BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_NAME](#ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6) = 0x0B , [BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39) = 0xFE ,     [BT\_AUDIO\_METADATA\_TYPE\_VENDOR](#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286) = 0xFF   } |
|  | Codec metadata type IDs. [More...](#gab53d0dd62bceff97cf8eed7d8cf80354) |
| enum | [bt\_audio\_location](#ga61230848c02098352320fe751332c4e8) {     [BT\_AUDIO\_LOCATION\_MONO\_AUDIO](#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df) = 0 , [BT\_AUDIO\_LOCATION\_FRONT\_LEFT](#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b) = BIT(0) , [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT](#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3) = BIT(1) , [BT\_AUDIO\_LOCATION\_FRONT\_CENTER](#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337) = BIT(2) ,     [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1](#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6) = BIT(3) , [BT\_AUDIO\_LOCATION\_BACK\_LEFT](#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896) = BIT(4) , [BT\_AUDIO\_LOCATION\_BACK\_RIGHT](#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa) = BIT(5) , [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER](#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e) = BIT(6) ,     [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER](#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692) = BIT(7) , [BT\_AUDIO\_LOCATION\_BACK\_CENTER](#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983) = BIT(8) , [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2](#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b) = BIT(9) , [BT\_AUDIO\_LOCATION\_SIDE\_LEFT](#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064) = BIT(10) ,     [BT\_AUDIO\_LOCATION\_SIDE\_RIGHT](#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd) = BIT(11) , [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT](#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9) = BIT(12) , [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT](#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d) = BIT(13) , [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER](#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e) = BIT(14) ,     [BT\_AUDIO\_LOCATION\_TOP\_CENTER](#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f) = BIT(15) , [BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT](#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06) = BIT(16) , [BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT](#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69) = BIT(17) , [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT](#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6) = BIT(18) ,     [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT](#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59) = BIT(19) , [BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER](#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd) = BIT(20) , [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER](#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376) = BIT(21) , [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT](#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29) = BIT(22) ,     [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT](#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8) = BIT(23) , [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE](#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d) = BIT(24) , [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE](#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71) = BIT(25) , [BT\_AUDIO\_LOCATION\_LEFT\_SURROUND](#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6) = BIT(26) ,     [BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND](#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e) = BIT(27)   } |
|  | Location values for BT Audio. [More...](#ga61230848c02098352320fe751332c4e8) |
| enum | [bt\_audio\_dir](#ga5bd899fb5e4d844058184913866e462f) { [BT\_AUDIO\_DIR\_SINK](#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8) = 0x01 , [BT\_AUDIO\_DIR\_SOURCE](#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c) = 0x02 } |
|  | Audio direction from the perspective of the BAP Unicast Server / BAP Broadcast Sink. [More...](#ga5bd899fb5e4d844058184913866e462f) |

| Functions | |
| --- | --- |
| int | [bt\_audio\_data\_parse](#gafd8574b16141162c95653f0aa2bf6ff7) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ltv[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*func)(struct [bt\_data](structbt__data.md) \*data, void \*user\_data), void \*user\_data) |
|  | Helper for parsing length-type-value data. |
| int | [bt\_audio\_data\_get\_val](#gabbd1b9c46caa9a19de6c95b08c31e5b5) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ltv\_data[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data) |
|  | Get the value of a specific data type in an length-type-value data array. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_audio\_get\_chan\_count](#ga87415f8dddd38b3f5641c96e9722a44a) (enum [bt\_audio\_location](#ga61230848c02098352320fe751332c4e8) chan\_allocation) |
|  | Function to get the number of channels from the channel allocation. |

| Unicast Announcement Type | |
| --- | --- |
| #define | [BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_GENERAL](#ga41db714fa87e85896a52427399633bb4)   0x00 |
|  | Unicast Server is connectable and is requesting a connection. |
| #define | [BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_TARGETED](#ga56c14acb7f182a413fdecac4e271c5cc)   0x01 |
|  | Unicast Server is connectable but is not requesting a connection. |

## Detailed Description

Bluetooth Audio.

## Macro Definition Documentation

## [◆ ](#ga3ed5ba09ab4c1ab7a59f8a1b4deee791)BT\_AUDIO\_BROADCAST\_ID\_MAX

| #define BT\_AUDIO\_BROADCAST\_ID\_MAX   0xFFFFFFU |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Maximum broadcast ID value.

## [◆ ](#ga18dd9f4a4af7716dd01497309ff9c87c)BT\_AUDIO\_BROADCAST\_ID\_SIZE

| #define BT\_AUDIO\_BROADCAST\_ID\_SIZE   3 |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Size of the broadcast ID in octets.

## [◆ ](#gaa2fafcbb6a826c3f4cee16ebb545dad6)BT\_AUDIO\_BROADCAST\_NAME\_LEN\_MAX

| #define BT\_AUDIO\_BROADCAST\_NAME\_LEN\_MAX   128 |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

The maximum size of a Broadcast Name as defined by Bluetooth Assigned Numbers.

## [◆ ](#gaa3bf677a479a90793f28a5a3ed69c7e0)BT\_AUDIO\_BROADCAST\_NAME\_LEN\_MIN

| #define BT\_AUDIO\_BROADCAST\_NAME\_LEN\_MIN   4 |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

The minimum size of a Broadcast Name as defined by Bluetooth Assigned Numbers.

## [◆ ](#ga6b99f589f6cdcd9e48a83f729a7a4698)BT\_AUDIO\_CODEC\_CAP

| #define BT\_AUDIO\_CODEC\_CAP | ( |  | *\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_cid*, |
|  |  |  | *\_vid*, |
|  |  |  | *\_data*, |
|  |  |  | *\_meta* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

**Value:**

((struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md)){ \

/\* Use HCI data path as default, can be overwritten by application \*/ \

.path\_id = [BT\_ISO\_DATA\_PATH\_HCI](group__bt__iso.md#gadd421c69edccfd695d728ded5feb6862), \

.ctlr\_transcode = false, \

.id = (\_id), \

.cid = (\_cid), \

.vid = (\_vid), \

.data\_len = sizeof(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)[])\_data), \

.data = \_data, \

.meta\_len = sizeof(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)[])\_meta), \

.meta = \_meta, \

})

[BT\_ISO\_DATA\_PATH\_HCI](group__bt__iso.md#gadd421c69edccfd695d728ded5feb6862)

#define BT\_ISO\_DATA\_PATH\_HCI

Value to set the ISO data path over HCi.

**Definition** iso.h:69

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_audio\_codec\_cap](structbt__audio__codec__cap.md)

Codec capability structure.

**Definition** audio.h:684

Helper to declare [Codec capability parsing APIs](group__bt__audio__codec__cap.md "Codec capability parsing APIs") structure.

Parameters
:   | \_id | Codec ID |
    | --- | --- |
    | \_cid | Company ID |
    | \_vid | Vendor ID |
    | \_data | Codec Specific Data in LVT format |
    | \_meta | Codec Specific Metadata in LVT format |

## [◆ ](#gad91341739d394f92ffc4988b614f47b6)BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MAX

| #define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MAX   8 |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Maximum supported channel counts.

## [◆ ](#gac1251f8a35b5e343eeeff87f22f8ab10)BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MIN

| #define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MIN   1 |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Minimum supported channel counts.

## [◆ ](#ga8f835266fabd6461216fe13e1b3b3a0f)BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT

| #define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

**Value:**

((enum [bt\_audio\_codec\_cap\_chan\_count](#gae695b5d17359967703f2509db1671fa5))(([FOR\_EACH](group__sys-util.md#ga278c8b7cbbea2f585e371d3568f3cb12)([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c), (|), \_\_VA\_ARGS\_\_)) >> 1))

[bt\_audio\_codec\_cap\_chan\_count](#gae695b5d17359967703f2509db1671fa5)

bt\_audio\_codec\_cap\_chan\_count

Supported audio capabilities channel count bitfield.

**Definition** audio.h:165

[FOR\_EACH](group__sys-util.md#ga278c8b7cbbea2f585e371d3568f3cb12)

#define FOR\_EACH(F, sep,...)

Call a macro F on each provided argument with a given separator between each call.

**Definition** util\_macro.h:501

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

Channel count support capability.

Macro accepts variable number of channel counts. The allowed channel counts are defined by specification and have to be in range from [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MIN](#gac1251f8a35b5e343eeeff87f22f8ab10) to [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MAX](#gad91341739d394f92ffc4988b614f47b6) inclusive.

Example to support 1 and 3 channels: [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT(1, 3)](#ga8f835266fabd6461216fe13e1b3b3a0f)

## [◆ ](#gaefed7a013e282c63c9b5cbbdcdc67448)BT\_AUDIO\_CODEC\_CFG

| #define BT\_AUDIO\_CODEC\_CFG | ( |  | *\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_cid*, |
|  |  |  | *\_vid*, |
|  |  |  | *\_data*, |
|  |  |  | *\_meta* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

**Value:**

((struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)){ \

/\* Use HCI data path as default, can be overwritten by application \*/ \

.path\_id = [BT\_ISO\_DATA\_PATH\_HCI](group__bt__iso.md#gadd421c69edccfd695d728ded5feb6862), \

.ctlr\_transcode = false, \

.id = \_id, \

.cid = \_cid, \

.vid = \_vid, \

.data\_len = sizeof(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)[])\_data), \

.data = \_data, \

.meta\_len = sizeof(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)[])\_meta), \

.meta = \_meta, \

})

[bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)

Codec specific configuration structure.

**Definition** audio.h:718

Helper to declare [Codec config parsing APIs](group__bt__audio__codec__cfg.md "Codec config parsing APIs").

Parameters
:   | \_id | Codec ID |
    | --- | --- |
    | \_cid | Company ID |
    | \_vid | Vendor ID |
    | \_data | Codec Specific Data in LVT format |
    | \_meta | Codec Specific Metadata in LVT format |

## [◆ ](#gaddc49e39465798ae4c0cbe345e0b50d7)BT\_AUDIO\_CODEC\_DATA

| #define BT\_AUDIO\_CODEC\_DATA | ( |  | *\_type*, |
| --- | --- | --- | --- |
|  |  |  | *\_bytes...* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

**Value:**

(sizeof(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))\_type) + sizeof(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)[]){\_bytes})), (\_type), \_bytes

Helper to declare elements of [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md "Codec capability structure.") arrays.

This macro is mainly for creating an array of struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md "Codec capability structure.") data arrays.

Parameters
:   | \_type | Type of advertising data field |
    | --- | --- |
    | \_bytes | Variable number of single-byte parameters |

## [◆ ](#ga6320f86aab9b227385bdf52a9ff3985b)BT\_AUDIO\_CONTEXT\_TYPE\_ANY

| #define BT\_AUDIO\_CONTEXT\_TYPE\_ANY |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

**Value:**

([BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5) | \

[BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL](#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e) | \

[BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA](#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e) | \

[BT\_AUDIO\_CONTEXT\_TYPE\_GAME](#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730) | \

[BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL](#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4) | \

[BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS](#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e) | \

[BT\_AUDIO\_CONTEXT\_TYPE\_LIVE](#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55) | \

[BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS](#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9) | \

[BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS](#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377) | \

[BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE](#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3) | \

[BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS](#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6) | \

[BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM](#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1))

[BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS](#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377)

@ BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS

Notification and reminder sounds; attention-seeking audio, for example, in beeps signaling the arriva...

**Definition** audio.h:341

[BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM](#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1)

@ BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM

Emergency alarm Emergency sounds, for example, fire alarms or other urgent alerts.

**Definition** audio.h:353

[BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL](#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4)

@ BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL

Instructional audio, for example, in navigation, announcements, or user guidance.

**Definition** audio.h:324

[BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE](#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3)

@ BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE

Alerts the user to an incoming call, for example, an incoming telephony or video call,...

**Definition** audio.h:346

[BT\_AUDIO\_CONTEXT\_TYPE\_LIVE](#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55)

@ BT\_AUDIO\_CONTEXT\_TYPE\_LIVE

Live audio, for example, from a microphone where audio is perceived both through a direct acoustic pa...

**Definition** audio.h:331

[BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA](#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA

Media, for example, music playback, radio, podcast or movie soundtrack, or tv audio.

**Definition** audio.h:317

[BT\_AUDIO\_CONTEXT\_TYPE\_GAME](#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730)

@ BT\_AUDIO\_CONTEXT\_TYPE\_GAME

Audio associated with video gaming, for example gaming media; gaming effects; music and in-game voice...

**Definition** audio.h:322

[BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS](#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9)

@ BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS

Sound effects including keyboard and touch feedback; menu and user interface sounds; and other system...

**Definition** audio.h:336

[BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS](#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS

Man-machine communication, for example, with voice recognition or virtual assistants.

**Definition** audio.h:326

[BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL](#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL

Conversation between humans, for example, in telephony or video calls, including traditional cellular...

**Definition** audio.h:315

[BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS](#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6)

@ BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS

Alarms and timers; immediate alerts, for example, in a critical battery alarm, timer expiry or alarm ...

**Definition** audio.h:351

[BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5)

@ BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED

Identifies audio where the use case context does not match any other defined value,...

**Definition** audio.h:310

Any known context.

## [◆ ](#gab6e5f793d514626deca21940d35d8f21)BT\_AUDIO\_LANG\_SIZE

| #define BT\_AUDIO\_LANG\_SIZE   3 |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Size of the stream language value, e.g.

"eng"

## [◆ ](#ga90688f158fe999ed3aa9c759c8245fcc)BT\_AUDIO\_LOCATION\_ANY

| #define BT\_AUDIO\_LOCATION\_ANY |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

**Value:**

([BT\_AUDIO\_LOCATION\_FRONT\_LEFT](#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b) | \

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT](#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3) | \

[BT\_AUDIO\_LOCATION\_FRONT\_CENTER](#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337) | \

[BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1](#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6) | \

[BT\_AUDIO\_LOCATION\_BACK\_LEFT](#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896) | \

[BT\_AUDIO\_LOCATION\_BACK\_RIGHT](#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa) | \

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER](#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e) | \

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER](#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692) | \

[BT\_AUDIO\_LOCATION\_BACK\_CENTER](#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983) | \

[BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2](#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b) | \

[BT\_AUDIO\_LOCATION\_SIDE\_LEFT](#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064) | \

[BT\_AUDIO\_LOCATION\_SIDE\_RIGHT](#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd) | \

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT](#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9) | \

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT](#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d) | \

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER](#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e) | \

[BT\_AUDIO\_LOCATION\_TOP\_CENTER](#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f) | \

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT](#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06) | \

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT](#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69) | \

[BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT](#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6) | \

[BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT](#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59) | \

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER](#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd) | \

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER](#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376) | \

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT](#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29) | \

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT](#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8) | \

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE](#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d) | \

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE](#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71) | \

[BT\_AUDIO\_LOCATION\_LEFT\_SURROUND](#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6) | \

[BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND](#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e))

[BT\_AUDIO\_LOCATION\_FRONT\_CENTER](#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337)

@ BT\_AUDIO\_LOCATION\_FRONT\_CENTER

Front Center.

**Definition** audio.h:598

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT](#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT

Top Back Left.

**Definition** audio.h:626

[BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2](#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b)

@ BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2

Low Frequency Effects 2.

**Definition** audio.h:612

[BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT](#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59)

@ BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT

Top Side Right.

**Definition** audio.h:632

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT](#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT

Front Right.

**Definition** audio.h:596

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT](#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT

Bottom Front Right.

**Definition** audio.h:640

[BT\_AUDIO\_LOCATION\_BACK\_RIGHT](#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa)

@ BT\_AUDIO\_LOCATION\_BACK\_RIGHT

Back Right.

**Definition** audio.h:604

[BT\_AUDIO\_LOCATION\_TOP\_CENTER](#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f)

@ BT\_AUDIO\_LOCATION\_TOP\_CENTER

Top Center.

**Definition** audio.h:624

[BT\_AUDIO\_LOCATION\_LEFT\_SURROUND](#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6)

@ BT\_AUDIO\_LOCATION\_LEFT\_SURROUND

Left Surround.

**Definition** audio.h:646

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT](#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT

Top Front Right.

**Definition** audio.h:620

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER](#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER

Front Right of Center.

**Definition** audio.h:608

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE](#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE

Front Right Wide.

**Definition** audio.h:644

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT](#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT

Top Back Right.

**Definition** audio.h:628

[BT\_AUDIO\_LOCATION\_BACK\_LEFT](#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896)

@ BT\_AUDIO\_LOCATION\_BACK\_LEFT

Back Left.

**Definition** audio.h:602

[BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND](#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e)

@ BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND

Right Surround.

**Definition** audio.h:648

[BT\_AUDIO\_LOCATION\_SIDE\_RIGHT](#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd)

@ BT\_AUDIO\_LOCATION\_SIDE\_RIGHT

Side Right.

**Definition** audio.h:616

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT](#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT

Top Front Left.

**Definition** audio.h:618

[BT\_AUDIO\_LOCATION\_SIDE\_LEFT](#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064)

@ BT\_AUDIO\_LOCATION\_SIDE\_LEFT

Side Left.

**Definition** audio.h:614

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT](#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT

Bottom Front Left.

**Definition** audio.h:638

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER](#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER

Top Front Center.

**Definition** audio.h:622

[BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1](#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6)

@ BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1

Low Frequency Effects 1.

**Definition** audio.h:600

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT](#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT

Front Left.

**Definition** audio.h:594

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE](#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE

Front Left Wide.

**Definition** audio.h:642

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER](#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER

Bottom Front Center.

**Definition** audio.h:636

[BT\_AUDIO\_LOCATION\_BACK\_CENTER](#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983)

@ BT\_AUDIO\_LOCATION\_BACK\_CENTER

Back Center.

**Definition** audio.h:610

[BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT](#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6)

@ BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT

Top Side Left.

**Definition** audio.h:630

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER](#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER

Top Back Center.

**Definition** audio.h:634

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER](#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER

Front Left of Center.

**Definition** audio.h:606

Any known location.

## [◆ ](#ga86a7e9ca661a3b13b7c59d41d206156e)BT\_AUDIO\_METADATA\_TYPE\_IS\_KNOWN

| #define BT\_AUDIO\_METADATA\_TYPE\_IS\_KNOWN | ( |  | *\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

**Value:**

([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)((\_type), [BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a), \

[BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1)) || \

(\_type) == [BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39) || (\_type) == [BT\_AUDIO\_METADATA\_TYPE\_VENDOR](#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286))

[BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39)

@ BT\_AUDIO\_METADATA\_TYPE\_EXTENDED

Extended metadata.

**Definition** audio.h:502

[BT\_AUDIO\_METADATA\_TYPE\_VENDOR](#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286)

@ BT\_AUDIO\_METADATA\_TYPE\_VENDOR

Vendor specific metadata.

**Definition** audio.h:505

[BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1)

@ BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE

Broadcast Audio Immediate Rendering flag.

**Definition** audio.h:489

[BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)

@ BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT

Preferred audio context.

**Definition** audio.h:443

[IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)

#define IN\_RANGE(val, min, max)

Checks if a value is within range.

**Definition** util.h:432

Helper to check whether metadata type is known by the stack.

Note
:   `_type` is evaluated thrice.

## [◆ ](#gaaa0414a4baef5a867fd1c6b1865d2dbc)BT\_AUDIO\_PD\_MAX

| #define BT\_AUDIO\_PD\_MAX   0xFFFFFFU |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Maximum presentation delay in microseconds.

## [◆ ](#ga663ab7bf74d56f36ee6cc80b369cbc16)BT\_AUDIO\_PD\_PREF\_NONE

| #define BT\_AUDIO\_PD\_PREF\_NONE   0x000000U |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Indicates that the server have no preference for the presentation delay.

## [◆ ](#ga4a5fd440b96f4e4acbb791badef8c255)BT\_AUDIO\_RTN\_PREF\_NONE

| #define BT\_AUDIO\_RTN\_PREF\_NONE   0xFFU |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Indicates that the unicast server does not have a preference for any retransmission number.

## [◆ ](#ga41db714fa87e85896a52427399633bb4)BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_GENERAL

| #define BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_GENERAL   0x00 |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Unicast Server is connectable and is requesting a connection.

## [◆ ](#ga56c14acb7f182a413fdecac4e271c5cc)BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_TARGETED

| #define BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_TARGETED   0x01 |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Unicast Server is connectable but is not requesting a connection.

## Enumeration Type Documentation

## [◆ ](#ga16d403ec4db7be997682331ad365ff5f)bt\_audio\_active\_state

| enum [bt\_audio\_active\_state](#ga16d403ec4db7be997682331ad365ff5f) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Audio Active State defined by the Generic Audio assigned numbers (bluetooth.com).

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_ACTIVE\_STATE\_DISABLED | No audio data is being transmitted. |
| BT\_AUDIO\_ACTIVE\_STATE\_ENABLED | Audio data is being transmitted. |

## [◆ ](#ga207fbf0fbca9b24cba02c7f1d184e7f5)bt\_audio\_assisted\_listening\_stream

| enum [bt\_audio\_assisted\_listening\_stream](#ga207fbf0fbca9b24cba02c7f1d184e7f5) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Assisted Listening Stream defined by the Generic Audio assigned numbers (bluetooth.com).

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_ASSISTED\_LISTENING\_STREAM\_UNSPECIFIED | Unspecified audio enhancement. |

## [◆ ](#gae695b5d17359967703f2509db1671fa5)bt\_audio\_codec\_cap\_chan\_count

| enum [bt\_audio\_codec\_cap\_chan\_count](#gae695b5d17359967703f2509db1671fa5) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Supported audio capabilities channel count bitfield.

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1 | Supporting 1 channel. |
| BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2 | Supporting 2 channel. |
| BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3 | Supporting 3 channel. |
| BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4 | Supporting 4 channel. |
| BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5 | Supporting 5 channel. |
| BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6 | Supporting 6 channel. |
| BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7 | Supporting 7 channel. |
| BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8 | Supporting 8 channel. |
| BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY | Supporting all channels. |

## [◆ ](#gaf37e8e19f956afb3c3a413cbaa1a21f5)bt\_audio\_codec\_cap\_frame\_dur

| enum [bt\_audio\_codec\_cap\_frame\_dur](#gaf37e8e19f956afb3c3a413cbaa1a21f5) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Supported frame durations bitfield.

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5 | 7.5 msec frame duration capability |
| BT\_AUDIO\_CODEC\_CAP\_DURATION\_10 | 10 msec frame duration capability |
| BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY | Any frame duration capability. |
| BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5 | 7.5 msec preferred frame duration capability.  This shall only be set if [BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) is also set, and if [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10](#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e) is not set. |
| BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10 | 10 msec preferred frame duration capability  This shall only be set if [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b) is also set, and if [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5](#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91) is not set. |

## [◆ ](#gaafc1106d5d305874ee2f540c850ff5b4)bt\_audio\_codec\_cap\_freq

| enum [bt\_audio\_codec\_cap\_freq](#gaafc1106d5d305874ee2f540c850ff5b4) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Supported frequencies bitfield.

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ | 8 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ | 11.025 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ | 16 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ | 22.05 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ | 24 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ | 32 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ | 44.1 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ | 48 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ | 88.2 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ | 96 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ | 176.4 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ | 192 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ | 384 Khz sampling frequency |
| BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY | Any frequency capability. |

## [◆ ](#gaf58823a56eb36cfd22e582ab1ea3d015)bt\_audio\_codec\_cap\_type

| enum [bt\_audio\_codec\_cap\_type](#gaf58823a56eb36cfd22e582ab1ea3d015) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Codec capability types.

Used to build and parse codec capabilities as specified in the PAC specification. Source is assigned numbers for Generic Audio, bluetooth.com.

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ | Supported sampling frequencies. |
| BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION | Supported frame durations. |
| BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT | Supported audio channel counts. |
| BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN | Supported octets per codec frame. |
| BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT | Supported maximum codec frames per SDU. |

## [◆ ](#ga83701b5eadfcbc9b84dc0b1a85ebeb74)bt\_audio\_codec\_cfg\_frame\_dur

| enum [bt\_audio\_codec\_cfg\_frame\_dur](#ga83701b5eadfcbc9b84dc0b1a85ebeb74) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Codec configuration frame duration.

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5 | 7.5 msec Frame Duration configuration |
| BT\_AUDIO\_CODEC\_CFG\_DURATION\_10 | 10 msec Frame Duration configuration |

## [◆ ](#ga8e99fb678cc011bb8c9f6e1858bae0d7)bt\_audio\_codec\_cfg\_freq

| enum [bt\_audio\_codec\_cfg\_freq](#ga8e99fb678cc011bb8c9f6e1858bae0d7) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Codec configuration sampling freqency.

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ | 8 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ | 11.025 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ | 16 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ | 22.05 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ | 24 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ | 32 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ | 44.1 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ | 48 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ | 88.2 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ | 96 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ | 176.4 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ | 192 Khz codec sampling frequency |
| BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ | 384 Khz codec sampling frequency |

## [◆ ](#ga9230ec4d7518bd243207ba2decb1a974)bt\_audio\_codec\_cfg\_type

| enum [bt\_audio\_codec\_cfg\_type](#ga9230ec4d7518bd243207ba2decb1a974) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Codec configuration types.

Used to build and parse codec configurations as specified in the ASCS and BAP specifications. Source is assigned numbers for Generic Audio, bluetooth.com.

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_CODEC\_CFG\_FREQ | Sampling frequency. |
| BT\_AUDIO\_CODEC\_CFG\_DURATION | Frame duration. |
| BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC | Audio channel allocation. |
| BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN | Octets per codec frame. |
| BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU | Codec frame blocks per SDU. |

## [◆ ](#gafb379ffa88388cc1397960155bbb2ab3)bt\_audio\_context

| enum [bt\_audio\_context](#gafb379ffa88388cc1397960155bbb2ab3) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Audio Context Type for Generic Audio.

These values are defined by the Generic Audio Assigned Numbers, bluetooth.com

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED | Prohibited. |
| BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED | Identifies audio where the use case context does not match any other defined value, or where the context is unknown or cannot be determined. |
| BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL | Conversation between humans, for example, in telephony or video calls, including traditional cellular as well as VoIP and Push-to-Talk. |
| BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA | Media, for example, music playback, radio, podcast or movie soundtrack, or tv audio. |
| BT\_AUDIO\_CONTEXT\_TYPE\_GAME | Audio associated with video gaming, for example gaming media; gaming effects; music and in-game voice chat between participants; or a mix of all the above. |
| BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL | Instructional audio, for example, in navigation, announcements, or user guidance. |
| BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS | Man-machine communication, for example, with voice recognition or virtual assistants. |
| BT\_AUDIO\_CONTEXT\_TYPE\_LIVE | Live audio, for example, from a microphone where audio is perceived both through a direct acoustic path and through an LE Audio Stream. |
| BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS | Sound effects including keyboard and touch feedback; menu and user interface sounds; and other system sounds. |
| BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS | Notification and reminder sounds; attention-seeking audio, for example, in beeps signaling the arrival of a message. |
| BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE | Alerts the user to an incoming call, for example, an incoming telephony or video call, including traditional cellular as well as VoIP and Push-to-Talk. |
| BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS | Alarms and timers; immediate alerts, for example, in a critical battery alarm, timer expiry or alarm clock, toaster, cooker, kettle, microwave, etc. |
| BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM | Emergency alarm Emergency sounds, for example, fire alarms or other urgent alerts. |

## [◆ ](#ga5bd899fb5e4d844058184913866e462f)bt\_audio\_dir

| enum [bt\_audio\_dir](#ga5bd899fb5e4d844058184913866e462f) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Audio direction from the perspective of the BAP Unicast Server / BAP Broadcast Sink.

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_DIR\_SINK | Audio direction sink.  For a BAP Unicast Client or Broadcast Source this is considered outgoing audio (TX). For a BAP Unicast Server or Broadcast Sink this is considered incoming audio (RX). |
| BT\_AUDIO\_DIR\_SOURCE | Audio direction source.  For a BAP Unicast Client or Broadcast Source this is considered incoming audio (RX). For a BAP Unicast Server or Broadcast Sink this is considered outgoing audio (TX). |

## [◆ ](#ga61230848c02098352320fe751332c4e8)bt\_audio\_location

| enum [bt\_audio\_location](#ga61230848c02098352320fe751332c4e8) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Location values for BT Audio.

These values are defined by the Generic Audio Assigned Numbers, bluetooth.com

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_LOCATION\_MONO\_AUDIO | Mono Audio (no specified Audio Location). |
| BT\_AUDIO\_LOCATION\_FRONT\_LEFT | Front Left. |
| BT\_AUDIO\_LOCATION\_FRONT\_RIGHT | Front Right. |
| BT\_AUDIO\_LOCATION\_FRONT\_CENTER | Front Center. |
| BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1 | Low Frequency Effects 1. |
| BT\_AUDIO\_LOCATION\_BACK\_LEFT | Back Left. |
| BT\_AUDIO\_LOCATION\_BACK\_RIGHT | Back Right. |
| BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER | Front Left of Center. |
| BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER | Front Right of Center. |
| BT\_AUDIO\_LOCATION\_BACK\_CENTER | Back Center. |
| BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2 | Low Frequency Effects 2. |
| BT\_AUDIO\_LOCATION\_SIDE\_LEFT | Side Left. |
| BT\_AUDIO\_LOCATION\_SIDE\_RIGHT | Side Right. |
| BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT | Top Front Left. |
| BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT | Top Front Right. |
| BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER | Top Front Center. |
| BT\_AUDIO\_LOCATION\_TOP\_CENTER | Top Center. |
| BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT | Top Back Left. |
| BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT | Top Back Right. |
| BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT | Top Side Left. |
| BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT | Top Side Right. |
| BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER | Top Back Center. |
| BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER | Bottom Front Center. |
| BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT | Bottom Front Left. |
| BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT | Bottom Front Right. |
| BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE | Front Left Wide. |
| BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE | Front Right Wide. |
| BT\_AUDIO\_LOCATION\_LEFT\_SURROUND | Left Surround. |
| BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND | Right Surround. |

## [◆ ](#gab53d0dd62bceff97cf8eed7d8cf80354)bt\_audio\_metadata\_type

| enum [bt\_audio\_metadata\_type](#gab53d0dd62bceff97cf8eed7d8cf80354) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Codec metadata type IDs.

Metadata types defined by the Generic Audio assigned numbers (bluetooth.com).

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT | Preferred audio context.  Bitfield of preferred audio contexts.  If 0, the context type is not a preferred use case for this codec configuration.  See the BT\_AUDIO\_CONTEXT\_\* for valid values. |
| BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT | Streaming audio context.  Bitfield of streaming audio contexts.  If 0, the context type is not a preferred use case for this codec configuration.  See the BT\_AUDIO\_CONTEXT\_\* for valid values. |
| BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO | UTF-8 encoded title or summary of stream content. |
| BT\_AUDIO\_METADATA\_TYPE\_LANG | Language.  3 octet lower case language code defined by ISO 639-3 Possible values can be found at [https://iso639-3.sil.org/code\_tables/639/data](https://iso639-3.sil.org/code_tables/639/data) |
| BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST | Array of 8-bit CCID values. |
| BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING | Parental rating.  See [bt\_audio\_parental\_rating](#ga6d4aff1f93dc0b902e4b5d1355f15760) for valid values. |
| BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI | UTF-8 encoded URI for additional Program information. |
| BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE | Audio active state.  See [bt\_audio\_active\_state](#ga16d403ec4db7be997682331ad365ff5f) for valid values. |
| BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE | Broadcast Audio Immediate Rendering flag. |
| BT\_AUDIO\_METADATA\_TYPE\_ASSISTED\_LISTENING\_STREAM | Assisted listening stream.  See [bt\_audio\_assisted\_listening\_stream](#ga207fbf0fbca9b24cba02c7f1d184e7f5) for valid values. |
| BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_NAME | UTF-8 encoded Broadcast name. |
| BT\_AUDIO\_METADATA\_TYPE\_EXTENDED | Extended metadata. |
| BT\_AUDIO\_METADATA\_TYPE\_VENDOR | Vendor specific metadata. |

## [◆ ](#ga6d4aff1f93dc0b902e4b5d1355f15760)bt\_audio\_parental\_rating

| enum [bt\_audio\_parental\_rating](#ga6d4aff1f93dc0b902e4b5d1355f15760) |
| --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Parental rating defined by the Generic Audio assigned numbers (bluetooth.com).

The numbering scheme is aligned with Annex F of EN 300 707 v1.2.1 which defined parental rating for viewing.

| Enumerator | |
| --- | --- |
| BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING | No rating. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY | For all ages. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE | Recommended for listeners of age 5 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE | Recommended for listeners of age 6 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE | Recommended for listeners of age 7 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE | Recommended for listeners of age 8 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE | Recommended for listeners of age 9 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE | Recommended for listeners of age 10 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE | Recommended for listeners of age 11 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE | Recommended for listeners of age 12 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE | Recommended for listeners of age 13 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE | Recommended for listeners of age 14 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE | Recommended for listeners of age 15 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE | Recommended for listeners of age 16 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE | Recommended for listeners of age 17 and above. |
| BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE | Recommended for listeners of age 18 and above. |

## Function Documentation

## [◆ ](#gabbd1b9c46caa9a19de6c95b08c31e5b5)bt\_audio\_data\_get\_val()

| int bt\_audio\_data\_get\_val | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ltv\_data*[], |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *type*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *data* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Get the value of a specific data type in an length-type-value data array.

Parameters
:   | [in] | ltv\_data | The array containing the length-type-value tuples |
    | --- | --- | --- |
    | [in] | size | The size of `ltv_data` |
    | [in] | type | The type to get the value for. May be any type, but typically either [bt\_audio\_codec\_cap\_type](#gaf58823a56eb36cfd22e582ab1ea3d015), [bt\_audio\_codec\_cfg\_type](#ga9230ec4d7518bd243207ba2decb1a974) or [bt\_audio\_metadata\_type](#gab53d0dd62bceff97cf8eed7d8cf80354). |
    | [out] | data | Pointer to the data-pointer to update when item is found. Any found data will be little endian. |

Return values
:   | length | The length of found `data` (may be 0). |
    | --- | --- |
    | -EINVAL | Arguments are invalid |
    | -ENODATA | Data not found |

## [◆ ](#gafd8574b16141162c95653f0aa2bf6ff7)bt\_audio\_data\_parse()

| int bt\_audio\_data\_parse | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ltv*[], |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | *func*)(struct [bt\_data](structbt__data.md) \*data, void \*user\_data), |
|  |  | void \* | *user\_data* ) |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Helper for parsing length-type-value data.

Parameters
:   | ltv | Length-type-value (LTV) encoded data. |
    | --- | --- |
    | size | Size of the `ltv` data. |
    | func | Callback function which will be called for each element that's found in the data. The callback should return true to continue parsing, or false to stop parsing. |
    | user\_data | User data to be passed to the callback. |

Return values
:   | 0 | All entries were parsed. |
    | --- | --- |
    | -EINVAL | The data is incorrectly encoded |
    | -ECANCELED | Parsing was prematurely cancelled by the callback |

## [◆ ](#ga87415f8dddd38b3f5641c96e9722a44a)bt\_audio\_get\_chan\_count()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_get\_chan\_count | ( | enum [bt\_audio\_location](#ga61230848c02098352320fe751332c4e8) | *chan\_allocation* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Function to get the number of channels from the channel allocation.

Parameters
:   | chan\_allocation | The channel allocation |
    | --- | --- |

Returns
:   The number of channels

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
