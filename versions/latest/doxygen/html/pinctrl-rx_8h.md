---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pinctrl-rx_8h.html
original_path: doxygen/html/pinctrl-rx_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rx.h File Reference

[Go to the source code of this file.](pinctrl-rx_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RX\_PORT\_NUM\_POS](#a33c8631dc344fa69c4e14e4cb43b490b)   0 |
| #define | [RX\_PORT\_NUM\_MASK](#af32dac5bcf375bbcf33375877f6e49e3)   0x1f |
| #define | [RX\_PIN\_NUM\_POS](#a8d620aa7e9514a75e3affc1ef8e950c9)   5 |
| #define | [RX\_PIN\_NUM\_MASK](#a5b11958c204ab0c6008ba32445d3c5b1)   0xf |
| #define | [RX\_PSEL\_MASK](#af0ee9eb8939cfd4e527a66c3d0f58f32)   0x1f |
| #define | [RX\_PSEL\_POS](#a58e6ba874d0ff5290cae17d3a6f11905)   9 |
| #define | [RX\_PSEL\_SCI\_1](#a0fd7aa971c81e73658b9ad99408ff61f)   0xA |
| #define | [RX\_PSEL\_SCI\_6](#a5275129885c5edd8dfff443723a59022)   0xB |
| #define | [RX\_PSEL\_TMR](#ad8c118ed209b1757032ab96daa7381e9)   0x5 |
| #define | [RX\_PSEL\_POE](#aca4687fe2b8f282995d3949e5ea2da10)   0x7 |
| #define | [RX\_PSEL\_P0nPFS\_HIZ](#aad48291cdeb29d13f13ebe0c07259594)   0x0 |
| #define | [RX\_PSEL\_P0nPFS\_ADTRG0](#a788c40b5e5a82083432968317a7d6c4e)   0x1 |
| #define | [RX\_PSEL\_P1nPFS\_MTIOC0B](#a1000a138a65b0a2dfbf56ced7d00508f)   0x01 |
| #define | [RX\_PSEL\_P1nPFS\_MTIOC3A](#a66b406de32b93246a9710d580deebf97)   0x01 |
| #define | [RX\_PSEL\_P1nPFS\_MTIOC3C](#a8a4dc3f07c7c9da139afcfb48c61277b)   0x01 |
| #define | [RX\_PSEL\_P1nPFS\_MTCLKA](#a2ce48e6029d58e6a0d9bb5a1d968ebe6)   0x02 |
| #define | [RX\_PSEL\_P1nPFS\_MTCLKB](#aadd46dc94695780f5c55fbdd7b9a831d)   0x02 |
| #define | [RX\_PSEL\_P1nPFS\_MTIOC3B](#a9c64a0d8e03b70ca45aebd8934f2a7d2)   0x02 |
| #define | [RX\_PSEL\_P1nPFS\_MTIOC3D](#a642a310aca921400209039992742d2c5)   0x02 |
| #define | [RX\_PSEL\_P1nPFS\_TMCI1](#a9bd05a6002222fd6febd332fc7a0525f)   0x5 |
| #define | [RX\_PSEL\_P1nPFS\_TMO1](#ad047c079d8ca34f4a489e63ea3ddd642)   0x5 |
| #define | [RX\_PSEL\_P1nPFS\_TMCI2](#a2c1fe2875a8f8f104cf7f36c6d6fca67)   0x5 |
| #define | [RX\_PSEL\_P1nPFS\_TMO2](#a6c59dcdcd76a0bb4c6cafdda3159bb68)   0x5 |
| #define | [RX\_PSEL\_P1nPFS\_TMRI2](#ac01000e60804a365ec8ab51235362e53)   0x5 |
| #define | [RX\_PSEL\_P1nPFS\_TMO3](#a82f52b919e109c185647242656538fb7)   0x5 |
| #define | [RX\_PSEL\_P1nPFS\_RTCOUT](#a11122cc8240be20777710e75cf00122d)   0x7 |
| #define | [RX\_PSEL\_P1nPFS\_POE8](#aa8cfdc8a4947b721c332375226f271a4)   0x7 |
| #define | [RX\_PSEL\_P1nPFS\_ADTRG0](#a9925ff98a4835feb94f295004f896c3c)   0x9 |
| #define | [RX\_PSEL\_P1nPFS\_RXD1](#ac9945fc6a230be884638863306b515a1)   0xA |
| #define | [RX\_PSEL\_P1nPFS\_SMISO1](#a252044667e25c0c87970b263bce8e8a1)   0xA |
| #define | [RX\_PSEL\_P1nPFS\_SSCL1](#a1ce8f440328f511c996bb79f957fedde)   0xA |
| #define | [RX\_PSEL\_P1nPFS\_TXD1](#a9e8985892fa25c60c00770d0265c7076)   0xA |
| #define | [RX\_PSEL\_P1nPFS\_SMOSI1](#acd3dc3dc1fa13168bb3052c8e4584019)   0xA |
| #define | [RX\_PSEL\_P1nPFS\_SSDA1](#a7ed94521bbda969b0b81f19d39fd563a)   0xA |
| #define | [RX\_PSEL\_P1nPFS\_CTS1](#a930c4df4b47a5b7dfe3278f0daea4654)   0xB |
| #define | [RX\_PSEL\_P1nPFS\_RTS1](#a0511157c9149ab334d022f46ddcf952b)   0xB |
| #define | [RX\_PSEL\_P1nPFS\_SS1](#a60b58d2d19666957f3725b87719538da)   0xB |
| #define | [RX\_PSEL\_P1nPFS\_MOSIA](#a6aa86965cd5ea93e6d300d9ea64dd4ed)   0xD |
| #define | [RX\_PSEL\_P1nPFS\_MISOA](#a8da1cb599f5ead00b7c142315b79ecc8)   0xD |
| #define | [RX\_PSEL\_P1nPFS\_SCL](#a313cec1391590cdf0e371b1975f6a2a9)   0xF |
| #define | [RX\_PSEL\_P1nPFS\_SDA](#a3e8733fee102ece6c412fbfbe2d40482)   0xF |
| #define | [RX\_PSEL\_P1nPFS\_TS5](#a09021fba8d5f0b62cadab76c408f0903)   0x19 |
| #define | [RX\_PSEL\_P1nPFS\_TS6](#a1409faaabb112be224a47aedb34564a0)   0x19 |
| #define | [RX\_PSEL\_P2nPFS\_MTIOC1A](#ae03c6c7a8a1c0d67f314533ccfac715e)   0x01 |
| #define | [RX\_PSEL\_P2nPFS\_MTIOC1B](#a148fe9efdef4a2497296f9268c1a8944)   0x01 |
| #define | [RX\_PSEL\_P2nPFS\_MTIOC2A](#ae0cfb4142c65b33e227907298b404541)   0x01 |
| #define | [RX\_PSEL\_P2nPFS\_MTIOC2B](#a9aa22ce6e3bc9855075281bb6b853c7a)   0x01 |
| #define | [RX\_PSEL\_P2nPFS\_MTIOC3B](#adda0ffa844d9be1603697598618c7a69)   0x01 |
| #define | [RX\_PSEL\_P2nPFS\_MTIOC3D](#a2ac9fabd592b2c4ad45b8d36475aefde)   0x01 |
| #define | [RX\_PSEL\_P2nPFS\_MTIOC4A](#a8f33600b8a26ad32056d89dff90f93af)   0x01 |
| #define | [RX\_PSEL\_P2nPFS\_MTIOC4C](#a035bdd99f2a958b9bef5d7e78be3aa9b)   0x01 |
| #define | [RX\_PSEL\_P2nPFS\_MTCLKA](#a946c850386e432cb2365facb3e8253f4)   0x02 |
| #define | [RX\_PSEL\_P2nPFS\_MTCLKB](#a2637c6326ea9f8792c5bcbc1d2cb6a86)   0x02 |
| #define | [RX\_PSEL\_P2nPFS\_MTCLKC](#a26e1bebe6fa54f6f542834d36e6a5a15)   0x02 |
| #define | [RX\_PSEL\_P2nPFS\_MTCLKD](#a83170987a059d0f4b4474518d1dc9f5c)   0x02 |
| #define | [RX\_PSEL\_P2nPFS\_TMCI0](#a54b553a2a753b03869c5834d5f7cf1ad)   0x5 |
| #define | [RX\_PSEL\_P2nPFS\_TMO0](#a39e6f7ec8b8e7ae970e6073e50a7ab2f)   0x5 |
| #define | [RX\_PSEL\_P2nPFS\_TMRI0](#a088e40350516ce25b1c5644e1f68661b)   0x5 |
| #define | [RX\_PSEL\_P2nPFS\_TMO1](#ad2b07aa7a06c371eac12cc1cc0ba122b)   0x5 |
| #define | [RX\_PSEL\_P2nPFS\_TMRI1](#a464af4730f95dbf0e25e38f218408f44)   0x5 |
| #define | [RX\_PSEL\_P2nPFS\_TMCI3](#a0418b8e109dccab2a5b39b73c8d34de6)   0x5 |
| #define | [RX\_PSEL\_P2nPFS\_ADTRG0](#aa59954a10be331a3adf63cae63cc6781)   0x9 |
| #define | [RX\_PSEL\_P2nPFS\_RXD0](#a644d0126190885ca9dbdfe09d3891911)   0xA |
| #define | [RX\_PSEL\_P2nPFS\_SMISO0](#a3c7dbd625604d3baab379953eecd4dd2)   0xA |
| #define | [RX\_PSEL\_P2nPFS\_SSCL0](#acb6c1ab729ac222872edcac9be75388d)   0xA |
| #define | [RX\_PSEL\_P2nPFS\_TXD0](#a296d05ae948f7bd999ad5549e9923af6)   0xA |
| #define | [RX\_PSEL\_P2nPFS\_SMOSI0](#a2fc0d75b547deee80cc88f4c15497873)   0xA |
| #define | [RX\_PSEL\_P2nPFS\_SSDA0](#a53817593b75446ddd77490d5144d07f3)   0xA |
| #define | [RX\_PSEL\_P2nPFS\_SCK0](#a8f18c698cfc5111ece10aada38e8ed0b)   0xA |
| #define | [RX\_PSEL\_P2nPFS\_TXD1](#a52375313e6b8333693f42925fa875061)   0xA |
| #define | [RX\_PSEL\_P2nPFS\_SMOSI1](#ad5241521982236501d3f59c315a212a7)   0xA |
| #define | [RX\_PSEL\_P2nPFS\_SSDA1](#ae3dbbed0bf6c3c928668fdcdfb8c2bd2)   0xA |
| #define | [RX\_PSEL\_P2nPFS\_SCK1](#a3d23cbbaffcfce61a09c552d128ade85)   0xA |
| #define | [RX\_PSEL\_P2nPFS\_CTS0](#af620f79d871fceafd43648bbf482ff74)   0xB |
| #define | [RX\_PSEL\_P2nPFS\_RTS0](#aa35d75b72a5aab5dd3ca61f158c401df)   0xB |
| #define | [RX\_PSEL\_P2nPFS\_SS0](#a963049f6db48bb8d470dc20f1af0b229)   0xB |
| #define | [RX\_PSEL\_P2nPFS\_TS3](#aa6b377d29e609a0a6cf9314f792a84c0)   0x19 |
| #define | [RX\_PSEL\_P2nPFS\_TS4](#a9c4eb492ef55cbe8294b9a785e178ac8)   0x19 |
| #define | [RX\_PSEL\_P3nPFS\_MTIOC0A](#a912cf155ad9b90d57cc2e54b5bc5f08a)   0x01 |
| #define | [RX\_PSEL\_P3nPFS\_MTIOC0C](#a94532f7a2a10d1ab8e2ba677e2697026)   0x01 |
| #define | [RX\_PSEL\_P3nPFS\_MTIOC0D](#a64da185fff98b3917f8895dd5d7baf65)   0x01 |
| #define | [RX\_PSEL\_P3nPFS\_MTIOC4B](#a7ee97491a03815f769f10104fb8f3abc)   0x01 |
| #define | [RX\_PSEL\_P3nPFS\_MTIOC4D](#addb1546bf2cf2f44ffc69e763ac977ee)   0x01 |
| #define | [RX\_PSEL\_P3nPFS\_TMCI2](#a5cfb12676b99d16d7602d510f182b5cb)   0x5 |
| #define | [RX\_PSEL\_P3nPFS\_TMO3](#a9071547e298af703f78fb8602d479ac6)   0x5 |
| #define | [RX\_PSEL\_P3nPFS\_TMRI3](#aa93265941791184b4aede61f922c2b18)   0x5 |
| #define | [RX\_PSEL\_P3nPFS\_TMCI3](#a9861a7bd48e1ec94eca541d230164874)   0x5 |
| #define | [RX\_PSEL\_P3nPFS\_RTCOUT](#ae61abf1a2343b39ffd50aa4f1cea1437)   0x7 |
| #define | [RX\_PSEL\_P3nPFS\_POE2](#a9d29e69cf44686dc6acf2876fae48ea5)   0x7 |
| #define | [RX\_PSEL\_P3nPFS\_POE3](#a7549ce5ac03ef03c97b13d7421540c02)   0x7 |
| #define | [RX\_PSEL\_P3nPFS\_POE8](#aedd2d3acb9455157b0f9920911af5c10)   0x7 |
| #define | [RX\_PSEL\_P3nPFS\_RXD1](#ae0da688c9e0bb84b4862d194269bec2a)   0xA |
| #define | [RX\_PSEL\_P3nPFS\_SMISO1](#a89adb49de0a99e0548e8ed242d4f0b62)   0xA |
| #define | [RX\_PSEL\_P3nPFS\_SSCL1](#a43f68e75a17d68fde57806db3691c3b2)   0xA |
| #define | [RX\_PSEL\_P3nPFS\_CTS1](#a08e879eb32d7096f08827e121e92fe50)   0xB |
| #define | [RX\_PSEL\_P3nPFS\_RTS1](#a6366c1fd6ad7e5d5ed540d25ca00e836)   0xB |
| #define | [RX\_PSEL\_P3nPFS\_SS1](#af53411085e8857438e5c9abb7888079f)   0xB |
| #define | [RX\_PSEL\_P3nPFS\_RXD6](#aac363230de113bd65dd17fe3b05c0a45)   0xB |
| #define | [RX\_PSEL\_P3nPFS\_SMISO6](#afcefa777d2064118ed7aec73bac19f08)   0xB |
| #define | [RX\_PSEL\_P3nPFS\_SSCL6](#a2d42e557aa6ba6e3ac2adb7215618935)   0xB |
| #define | [RX\_PSEL\_P3nPFS\_TXD6](#ae57aed1d69d9e791943206ea9c75eedc)   0xB |
| #define | [RX\_PSEL\_P3nPFS\_SMOSI6](#abd8dde16e830b4d61be34bde6c8552d2)   0xB |
| #define | [RX\_PSEL\_P3nPFS\_SSDA6](#aebd62a6fd208525bac61b7c198578f23)   0xB |
| #define | [RX\_PSEL\_P3nPFS\_SCK6](#a523ea0495c5667c4acb97100bcb81373)   0xB |
| #define | [RX\_PSEL\_P3nPFS\_TS0](#a9b1b5dfc5099562d6965bf801b00c71d)   0x19 |
| #define | [RX\_PSEL\_P3nPFS\_TS1](#a04794c793e252a3d9d260bc7902295ba)   0x19 |
| #define | [RX\_PSEL\_P3nPFS\_TS2](#ac8312cdd9d396e15081d5873b5f25afd)   0x19 |
| #define | [RX\_PSEL\_P5nPFS\_MTIOC4B](#a142d0481f6512159c7f280419834f96f)   0x01 |
| #define | [RX\_PSEL\_P5nPFS\_MTIOC4D](#a73b2361a0599be381e5b234b852b1dec)   0x01 |
| #define | [RX\_PSEL\_P5nPFS\_TMCI1](#a384f77f5ef58df21c990ec1f244a582d)   0x5 |
| #define | [RX\_PSEL\_P5nPFS\_TMO3](#aeb2b78345a96979b0938c17f032739cc)   0x5 |
| #define | [RX\_PSEL\_P5nPFS\_TS11](#aee8c3bbb3a4341bf23aae2376c0d63da)   0x19 |
| #define | [RX\_PSEL\_P5nPFS\_TS12](#a1fae9f412c3a00786292e6a55a480ea0)   0x19 |
| #define | [RX\_PSEL\_P5nPFS\_PMC0](#a3f85d862897a3ed788adbac2dcdfd3ce)   0x19 |
| #define | [RX\_PSEL\_P5nPFS\_PMC1](#a1813788221910ec1a0e1065d3745864c)   0x19 |
| #define | [RX\_PSEL\_PAnPFS\_MTIOC4A](#a87c47d0c6734ce3547b23754234502f4)   0x01 |
| #define | [RX\_PSEL\_PAnPFS\_MTIOC0B](#a884e497ea0370a0fd1fdd351f5b6a786)   0x01 |
| #define | [RX\_PSEL\_PAnPFS\_MTIOC0D](#a2b8d4b23f5172d4798e8519644e35e9a)   0x01 |
| #define | [RX\_PSEL\_PAnPFS\_MTIOC5U](#aba913f6670da680ac45030c6ec6f427a)   0x01 |
| #define | [RX\_PSEL\_PAnPFS\_MTIOC5V](#a475663b42a042fe06c9f340e3e63adb1)   0x01 |
| #define | [RX\_PSEL\_PAnPFS\_MTCLKA](#af579ae4fd94b09b8d76a9f8f89e6acb3)   0x02 |
| #define | [RX\_PSEL\_PAnPFS\_MTCLKB](#a8b47dba63dd54bd6a7034fae4b875d15)   0x02 |
| #define | [RX\_PSEL\_PAnPFS\_MTCLKC](#a82fd05e3e993fb86fc4d18a5ec7cddc6)   0x02 |
| #define | [RX\_PSEL\_PAnPFS\_MTCLKD](#a970d467907e0c4e8829f20eb0de9e4c4)   0x02 |
| #define | [RX\_PSEL\_PAnPFS\_TMRI0](#a50d18bf6681275da284b2348aaa626d7)   0x5 |
| #define | [RX\_PSEL\_PAnPFS\_TMCI3](#a26ce828aab38d7005ae7ccf5d3809f1e)   0x5 |
| #define | [RX\_PSEL\_PAnPFS\_POE2](#a3985ebc7577dc17f64ab2e2c0a676910)   0x7 |
| #define | [RX\_PSEL\_PAnPFS\_CACREF](#ac0c66c71e791fbcdf75a15c1acc58bc2)   0x7 |
| #define | [RX\_PSEL\_PAnPFS\_RXD5](#a819aa2b70f2cbb0165c93fc06b1784e2)   0xA |
| #define | [RX\_PSEL\_PAnPFS\_SMISO5](#aa7ffb4053ffa015c30a6906885a007bc)   0xA |
| #define | [RX\_PSEL\_PAnPFS\_SSCL5](#a080fa1148d00016a8663f0adc0f3a81c)   0xA |
| #define | [RX\_PSEL\_PAnPFS\_TXD5](#a6cda040400df3fc63b2ea5b35b09347e)   0xA |
| #define | [RX\_PSEL\_PAnPFS\_SMOSI5](#aadf3aca998e7796fb8724264966b1c17)   0xA |
| #define | [RX\_PSEL\_PAnPFS\_SSDA5](#ab5eec46fe3c3ec8a79b78d6f14652631)   0xA |
| #define | [RX\_PSEL\_PAnPFS\_SCK5](#a4a358940161583dac3d6e99e5a65da7a)   0xA |
| #define | [RX\_PSEL\_PAnPFS\_CTS5](#aca996f81268ef4573b837b4da0491ef4)   0xB |
| #define | [RX\_PSEL\_PAnPFS\_RTS5](#a2a3f02bd3a18a96355ecc8c6aca215bd)   0xB |
| #define | [RX\_PSEL\_PAnPFS\_SS5](#acdbcff26b1e0c1ec95904359831101a6)   0xB |
| #define | [RX\_PSEL\_PAnPFS\_SSLA0](#ac5a1bb8cc48cc3975e989d0ae8301b85)   0xD |
| #define | [RX\_PSEL\_PAnPFS\_SSLA1](#a695b1d61fa2af644e8e713bde9008b67)   0xD |
| #define | [RX\_PSEL\_PAnPFS\_SSLA2](#a4f9ce98bb1087fdfa8a4820dec774b88)   0xD |
| #define | [RX\_PSEL\_PAnPFS\_SSLA3](#a4a1682361951b36cbaca4a469ede48d7)   0xD |
| #define | [RX\_PSEL\_PAnPFS\_RSPCKA](#a3001136d224d46c165f437e44733457b)   0xD |
| #define | [RX\_PSEL\_PAnPFS\_MOSIA](#abcf66e981b8dce6df3552dfe23f87440)   0xD |
| #define | [RX\_PSEL\_PAnPFS\_MISOA](#abc8dccd90af6bfbb74012df17f256709)   0xD |
| #define | [RX\_PSEL\_PAnPFS\_TS26](#a09b4a8fe6520da1a3239890590ef90d3)   0x19 |
| #define | [RX\_PSEL\_PAnPFS\_TS27](#a988e53dc6d5a7c139747be285598fe96)   0x19 |
| #define | [RX\_PSEL\_PAnPFS\_TS28](#ae00078451e050502337206f9bd6362bc)   0x19 |
| #define | [RX\_PSEL\_PAnPFS\_TS29](#a67cf8ad3d73c35f2659a2af3f5b3d6f3)   0x19 |
| #define | [RX\_PSEL\_PAnPFS\_TS30](#a4b080b72196e98924c3a9d02b2d1756e)   0x19 |
| #define | [RX\_PSEL\_PAnPFS\_TS31](#a8b434c0a6b494ab4020b49c8df2707c0)   0x19 |
| #define | [RX\_PSEL\_PAnPFS\_TS32](#a0b2a031acfb9f73f5e34d58d1bf21a3e)   0x19 |
| #define | [RX\_PSEL\_PBnPFS\_MTIOC0A](#ab70484c773d08b3331e93d5f16e74e8a)   0x01 |
| #define | [RX\_PSEL\_PBnPFS\_MTIOC0C](#aa16664b39a03dc8f5cf1eff2df22d132)   0x01 |
| #define | [RX\_PSEL\_PBnPFS\_MTIOC2A](#a78103875ae7f2bf781da23c8033fed59)   0x01 |
| #define | [RX\_PSEL\_PBnPFS\_MTIOC3B](#a1e5ccf9190a3dc5970f4254d737ae072)   0x01 |
| #define | [RX\_PSEL\_PBnPFS\_MTIOC3D](#ae583a13420640109ebe70590b4d499ba)   0x01 |
| #define | [RX\_PSEL\_PBnPFS\_MTIOC5W](#a151d204a2e111718abf98b37a5c30d02)   0x01 |
| #define | [RX\_PSEL\_PBnPFS\_MTIOC1B](#a867fdf6ad0579c0022dc82999e161db6)   0x02 |
| #define | [RX\_PSEL\_PBnPFS\_MTIOC4A](#a021849717993b6ddcd5944b737a2aaf4)   0x02 |
| #define | [RX\_PSEL\_PBnPFS\_MTIOC4C](#a3375281ff859dfe401d503032a1d6b80)   0x02 |
| #define | [RX\_PSEL\_PBnPFS\_TMO0](#a5e3a37d153b356ae71c638fc7010a9f7)   0x5 |
| #define | [RX\_PSEL\_PBnPFS\_TMRI1](#aafc8cd3f09a9fc7b8cc3f59403ed514d)   0x5 |
| #define | [RX\_PSEL\_PBnPFS\_TMCI0](#a1bfa8645f34a063435061facc3c4736a)   0x5 |
| #define | [RX\_PSEL\_PBnPFS\_POE1](#a7deea898404b855145576f716f851a92)   0x7 |
| #define | [RX\_PSEL\_PBnPFS\_POE3](#aaef5911c5707323f20fec35fec6bdea2)   0x7 |
| #define | [RX\_PSEL\_PBnPFS\_RXD9](#a3560ff40295f809b6035026957014457)   0xA |
| #define | [RX\_PSEL\_PBnPFS\_SMISO9](#a95fa86bdf6128a0c911cf3258dcac3c5)   0xA |
| #define | [RX\_PSEL\_PBnPFS\_SSCL9](#abbc0966da3e8a31b0862639c73d298ee)   0xA |
| #define | [RX\_PSEL\_PBnPFS\_TXD9](#a6a8de4826f40799a5377d6b0ddba973b)   0xA |
| #define | [RX\_PSEL\_PBnPFS\_SMOSI9](#a47f17b912597e5cb66846711e37f9b6d)   0xA |
| #define | [RX\_PSEL\_PBnPFS\_SSDA9](#a2e06bb5584c33d2124e2fc6e2b0ed381)   0xA |
| #define | [RX\_PSEL\_PBnPFS\_SCK9](#a3ebc1ec3ce34c09b02698b4cbb3ef0ce)   0xA |
| #define | [RX\_PSEL\_PBnPFS\_CTS6](#a2fdd18ec059ab4e4d8a2284b16f8c160)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_RTS6](#a4cf58353b52de3273826db6666c94cba)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_SS6](#aa543049ed2b1ad9e216ce6e85fcee876)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_CTS9](#afc347de58db4d6795ded3a76afb1abf6)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_RTS9](#aefb72d4fad4867bcd5fef242322fdb46)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_SS9](#a8c2cef051d3a5db19460d89c608c6233)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_RXD6](#aad2ab397717736311073efe4bad48818)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_SMISO6](#a7e9537931de468389d51b0355754ab1f)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_SSCL6](#a78aa89352d217d85b4f36bd55cc202a5)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_TXD6](#a514b3b4d6eefd9ae830f3ea29e69b07b)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_SMOSI6](#af3c3885de61f44965d296f35aeae8f78)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_SSDA6](#afe28b85756fab74733b87fa10ee63d8e)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_SCK6](#a8b6978e1aebd1fcd55c7a543a38496ba)   0xB |
| #define | [RX\_PSEL\_PBnPFS\_RSPCKA](#a9d01bbc858e16531b932ba4a10783e03)   0xD |
| #define | [RX\_PSEL\_PBnPFS\_CMPOB1](#a230a3999d4881be6074e4380107075ce)   0x10 |
| #define | [RX\_PSEL\_PBnPFS\_TS18](#a7b4f647d5bdfb3fb8a2107949629994a)   0x19 |
| #define | [RX\_PSEL\_PBnPFS\_TS19](#ad356f13b07220a235c1f971d2b1ab7ea)   0x19 |
| #define | [RX\_PSEL\_PBnPFS\_TS20](#a364a18874eefb53563242194d1150910)   0x19 |
| #define | [RX\_PSEL\_PBnPFS\_TS21](#a0342b766bac5038c1fc6134a7d1bd85f)   0x19 |
| #define | [RX\_PSEL\_PBnPFS\_TS22](#a3db09a4ebeee6872100e3916a160b099)   0x19 |
| #define | [RX\_PSEL\_PBnPFS\_TS23](#a66af16b3b335123ccda6d1ad5efda434)   0x19 |
| #define | [RX\_PSEL\_PBnPFS\_TS24](#a4ddfb9a65c9dc5b58e08e48be2171664)   0x19 |
| #define | [RX\_PSEL\_PBnPFS\_TS25](#a79f5033bf88f0d42632e70de11990c13)   0x19 |
| #define | [RX\_PSEL\_PCnPFS\_MTIOC3A](#a0a0e1289dc503260b7d4d9ad99813bcf)   0x01 |
| #define | [RX\_PSEL\_PCnPFS\_MTIOC3B](#accdce2d8f48796e5eaa7b6cf4bdaf225)   0x01 |
| #define | [RX\_PSEL\_PCnPFS\_MTIOC3C](#a9a281dbe06b3123d1afb0809df50d188)   0x01 |
| #define | [RX\_PSEL\_PCnPFS\_MTIOC3D](#adfa80b9c6df7c803e6d158e9825f7931)   0x01 |
| #define | [RX\_PSEL\_PCnPFS\_MTIOC4B](#a3878479bf2dc042792d6174496038207)   0x01 |
| #define | [RX\_PSEL\_PCnPFS\_MTIOC4D](#ac25138271990797712728f0e5d5909e6)   0x01 |
| #define | [RX\_PSEL\_PCnPFS\_MTCLKA](#a9e0b4711dd92fdff630516fc963187c6)   0x02 |
| #define | [RX\_PSEL\_PCnPFS\_MTCLKB](#a73c23ead228baca49158d7486ec7f0e0)   0x02 |
| #define | [RX\_PSEL\_PCnPFS\_MTCLKC](#abc55942f4d533288287d602ec46a3384)   0x02 |
| #define | [RX\_PSEL\_PCnPFS\_MTCLKD](#a2e9e94477161bfbd4ece9e926c6b20f3)   0x02 |
| #define | [RX\_PSEL\_PCnPFS\_TMCI1](#aad2d8d27f0b4bcc06c69d60f4ba32415)   0x5 |
| #define | [RX\_PSEL\_PCnPFS\_TMO2](#aeb895a0766941862427dcfe548fe795b)   0x5 |
| #define | [RX\_PSEL\_PCnPFS\_TMRI2](#aa9ca76efaf979f4f1bacb444a93c2338)   0x5 |
| #define | [RX\_PSEL\_PCnPFS\_TMCI2](#a104b8044a91acadbb73c6fedd01e3128)   0x5 |
| #define | [RX\_PSEL\_PCnPFS\_POE0](#af7fbf061ff82639825805cc3cca28a0b)   0x7 |
| #define | [RX\_PSEL\_PCnPFS\_CACREF](#af33cdb03242b52a66aa312834f738ab1)   0x7 |
| #define | [RX\_PSEL\_PCnPFS\_RXD5](#a5a69027c56b05fab8d7d53a6880b9423)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_SMISO5](#a392276adc9abd36a582d590446f96038)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_SSCL5](#a2437838e9799abd2b17b6376675e70ca)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_TXD5](#a3d8cb88bf920515954d3833b2d5e90f9)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_SMOSI5](#aa346eb221834f7e0df6d778da6ec35cd)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_SSDA5](#a4f2bc6a3a5b8561f37f778fa577ac0e8)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_SCK5](#a01d49d963a3136acef38a2a831a076a1)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_RXD8](#a86211091c53c6dbbdd657bce75e70986)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_SMISO8](#ae44a9ac365c5d056ee2921a5c4bcb5ee)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_SSCL8](#a8990d81f5d74427c71cc37eee6647c98)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_TXD8](#a257eaa3c131105d680ff05e9def319c4)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_SMOSI8](#a953ca81bde404c7f9a159725a090af04)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_SSDA8](#a8cba60fc83718e0dde6361fcf2fb9a5c)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_SCK8](#aff658c7c324fa5bf4461b7436aa97e5c)   0xA |
| #define | [RX\_PSEL\_PCnPFS\_CTS5](#a20997f4c8188883ca8b1094a0b7e873b)   0xB |
| #define | [RX\_PSEL\_PCnPFS\_RTS5](#a5d8408785316cd7187e5fda2f7cf4152)   0xB |
| #define | [RX\_PSEL\_PCnPFS\_SS5](#a73b65f6a77adb07c2f17d1589f5e5d68)   0xB |
| #define | [RX\_PSEL\_PCnPFS\_CTS8](#a0fa3dde24d9c4f689237a5e21153efcc)   0xB |
| #define | [RX\_PSEL\_PCnPFS\_RTS8](#a97c6a44c096c0c5873e7a57f9c956083)   0xB |
| #define | [RX\_PSEL\_PCnPFS\_SS8](#a0b5c3248fe7278e43a9dab8bb47b347c)   0xB |
| #define | [RX\_PSEL\_PCnPFS\_SSLA0](#a3b5990fb7b76f0befd197dac661a9036)   0xD |
| #define | [RX\_PSEL\_PCnPFS\_SSLA1](#af7ca895592d0ac3d46cddcc40c315f70)   0xD |
| #define | [RX\_PSEL\_PCnPFS\_SSLA2](#af563abf494e2730c8895b3fb4de6c85a)   0xD |
| #define | [RX\_PSEL\_PCnPFS\_SSLA3](#a1c74ab46805e2ec72c1477059aa7c6f4)   0xD |
| #define | [RX\_PSEL\_PCnPFS\_RSPCKA](#ac88a47a2634a1f730fe58009d277c56d)   0xD |
| #define | [RX\_PSEL\_PCnPFS\_MOSIA](#aca94166ceb510874373df19e74c1e171)   0xD |
| #define | [RX\_PSEL\_PCnPFS\_MISOA](#ac8c1b07159883e4c934ce5e2bd61d057)   0xD |
| #define | [RX\_PSEL\_PCnPFS\_TS13](#a0f4ba5772ff554184551e10371af83ba)   0x19 |
| #define | [RX\_PSEL\_PCnPFS\_TS14](#a5b61df843dcd7e9e4bc5d6e275ebb99c)   0x19 |
| #define | [RX\_PSEL\_PCnPFS\_TS15](#a1c12baa481da0305da0e91d4eb3a2c31)   0x19 |
| #define | [RX\_PSEL\_PCnPFS\_TS16](#a6283542c2054052770c40941cffd508e)   0x19 |
| #define | [RX\_PSEL\_PCnPFS\_TS17](#ae70d84e57e3293b2916db85ffd91e7a1)   0x19 |
| #define | [RX\_PSEL\_PCnPFS\_TSCAP](#a77444df0b11d61ceb285b18600032e88)   0x19 |
| #define | [RX\_PSEL\_PDnPFS\_MTIOC4B](#aafbb53acfb95de11fdf6a75e75c3fc97)   0x01 |
| #define | [RX\_PSEL\_PDnPFS\_MTIOC4D](#ac3de35bbc1a916e8449698eb24a34cec)   0x01 |
| #define | [RX\_PSEL\_PDnPFS\_MTIOC5W](#a7a096c87787f645323ca16bd1ae3bac6)   0x01 |
| #define | [RX\_PSEL\_PDnPFS\_MTIOC5V](#a45c847394001f31be768944b7acaf906)   0x01 |
| #define | [RX\_PSEL\_PDnPFS\_MTIOC5U](#ab5f02479510f1babd64ba6cbb169f42c)   0x01 |
| #define | [RX\_PSEL\_PDnPFS\_POE0](#a2a77be1f3443daaab5f4b3066c1f8278)   0x7 |
| #define | [RX\_PSEL\_PDnPFS\_POE1](#af94b267110bc98221219a97c58f4e697)   0x7 |
| #define | [RX\_PSEL\_PDnPFS\_POE2](#a267d05d58ffcab0f60ae8427f8aecaf2)   0x7 |
| #define | [RX\_PSEL\_PDnPFS\_POE3](#ae0e7f8f472d0f64c2dd328b57615dc98)   0x7 |
| #define | [RX\_PSEL\_PDnPFS\_POE8](#a6c9a976cb22cc6b0e69d9d31b41e0321)   0x7 |
| #define | [RX\_PSEL\_PDnPFS\_RXD6](#a9733d54b731df033e6c1eda5293c5317)   0xB |
| #define | [RX\_PSEL\_PDnPFS\_SMISO6](#aa2f83777eb6e976f0451786a1f6edceb)   0xB |
| #define | [RX\_PSEL\_PDnPFS\_SSCL6](#a3d03c22b4f7adbb20f10208e471ce276)   0xB |
| #define | [RX\_PSEL\_PDnPFS\_TXD6](#a8ae0cab25d78a40565870fc28428def3)   0xB |
| #define | [RX\_PSEL\_PDnPFS\_SMOSI6](#a8f5941502abad2c8995bc57b986ca81f)   0xB |
| #define | [RX\_PSEL\_PDnPFS\_SSDA6](#a88acb98416906f6abdf2f6172d80bdaf)   0xB |
| #define | [RX\_PSEL\_PDnPFS\_SCK6](#a3e318ee5f28ce26bbd73dabed4b1a44a)   0xB |
| #define | [RX\_PSEL\_PEnPFS\_MTIOC4A](#a57abebe2638d36ca13d2d72d65436497)   0x01 |
| #define | [RX\_PSEL\_PEnPFS\_MTIOC4B](#a51e4a949c884b35891f1503e489291e8)   0x01 |
| #define | [RX\_PSEL\_PEnPFS\_MTIOC4C](#a6ef5a9460e67440d1f4e82c13fef35bf)   0x01 |
| #define | [RX\_PSEL\_PEnPFS\_MTIOC4D](#a2f800b39f958ec49897fb7d3b0a1574f)   0x01 |
| #define | [RX\_PSEL\_PEnPFS\_MTIOC1A](#a989c6f0452e964e6a6875b4924339b22)   0x02 |
| #define | [RX\_PSEL\_PEnPFS\_MTIOC2B](#a967c82a27a33b39b1ba1ae051090e6db)   0x02 |
| #define | [RX\_PSEL\_PEnPFS\_POE8](#a53a29ae9db04f7dab6bced306a47cfac)   0x7 |
| #define | [RX\_PSEL\_PEnPFS\_CLKOUT](#a2bf6e1d791920bd5b44f10b62fb12db4)   0x9 |
| #define | [RX\_PSEL\_PEnPFS\_RXD12](#a85764cf1f6755fe00531703e20f9a587)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_SMISO12](#acbacde7e28a5160ec6190aee9f3b4706)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_SSCL12](#a582c1aad6d4ce2aae7d683cbd179950e)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_TXD12](#a9a4f83a8487dfd0f32fb3180f71853b5)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_SMOSI12](#a6fed05bb93fd3a18a53372660a6faaff)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_SSDA12](#ae63305a2e7c8d27d85c7702e5826c918)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_SCK12](#af2cb8b0acdc39ba3a4a659394a6884e5)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_TXDX12](#a08d429e3e500db8b87f95a11cc61bf66)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_RXDX12](#ad769da51c412edc773cad5f959364763)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_SIOX12](#a58da776438c101eb043756f40ef5259a)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_CTS12](#a49ed2fbfbd7c155fc22f744b4426502a)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_RTS12](#a39012da0abc5634d6ae1c1964653f392)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_SS12](#abc093255f500eb7bbc1aac866afe7ef6)   0xC |
| #define | [RX\_PSEL\_PEnPFS\_CMPOB0](#ac2d89df9365a11dd0388d122b11f2536)   0X10 |
| #define | [RX\_PSEL\_PEnPFS\_TS33](#ad19b9859c60e5e84cf356a72048005d3)   0X19 |
| #define | [RX\_PSEL\_PEnPFS\_TS34](#a301d3eaf6cf49e216b3bf0759b789bea)   0x19 |
| #define | [RX\_PSEL\_PEnPFS\_TS35](#a9fbfd7aac05dfd05608264fa944c6287)   0x19 |
| #define | [RX\_PSEL\_PHnPFS\_TMO0](#a84b2b05520efe0683f9db4e07155bfba)   0x05 |
| #define | [RX\_PSEL\_PHnPFS\_TMRI0](#a6d8d96eaf1add151dd4629931fe61d1c)   0x05 |
| #define | [RX\_PSEL\_PHnPFS\_TMCI0](#a0026241158d3b5ecf428c4836a3d875f)   0x05 |
| #define | [RX\_PSEL\_PHnPFS\_CACREF](#a6ebe5c08ff146f995ac212e1ea716742)   0x7 |
| #define | [RX\_PSEL\_PHnPFS\_TS7](#aa8cfeedd877a6952f8d97a341da8d50d)   0x19 |
| #define | [RX\_PSEL\_PHnPFS\_TS8](#aeaf0f72ae91e634a1683a06e08b1f6c7)   0x19 |
| #define | [RX\_PSEL\_PHnPFS\_TS9](#a70dd840a2bba0791a151bc09c4be36f0)   0x19 |
| #define | [RX\_PSEL\_PHnPFS\_TS10](#a2c067233e929b0cec2b3d2a09097deae)   0x19 |
| #define | [RX\_PSEL\_PJnPFS\_MTIOC3A](#ad8dfc05cfc1d8415d91b29ffe39c9b96)   0x01 |
| #define | [RX\_PSEL\_PJnPFS\_MTIOC3C](#a580dc22127edf2f64729314f6dd7e910)   0x01 |
| #define | [RX\_PSEL\_PJnPFS\_CTS6](#a089de182c44f003fe50d1d5be28fc69c)   0xB |
| #define | [RX\_PSEL\_PJnPFS\_TTS6](#a196e453a63cbbb6be004b3deb11aebc7)   0xB |
| #define | [RX\_PSEL\_PJnPFS\_SS6](#a319993d775bb37dfcdfc545e358c6e6e)   0xB |
| #define | [RX\_PSEL](#ab1a754c6466137c60093291517676f24)(psel, port\_num, pin\_num) |

## Macro Definition Documentation

## [◆ ](#a5b11958c204ab0c6008ba32445d3c5b1)RX\_PIN\_NUM\_MASK

| #define RX\_PIN\_NUM\_MASK   0xf |
| --- |

## [◆ ](#a8d620aa7e9514a75e3affc1ef8e950c9)RX\_PIN\_NUM\_POS

| #define RX\_PIN\_NUM\_POS   5 |
| --- |

## [◆ ](#af32dac5bcf375bbcf33375877f6e49e3)RX\_PORT\_NUM\_MASK

| #define RX\_PORT\_NUM\_MASK   0x1f |
| --- |

## [◆ ](#a33c8631dc344fa69c4e14e4cb43b490b)RX\_PORT\_NUM\_POS

| #define RX\_PORT\_NUM\_POS   0 |
| --- |

## [◆ ](#ab1a754c6466137c60093291517676f24)RX\_PSEL

| #define RX\_PSEL | ( |  | *psel*, |
| --- | --- | --- | --- |
|  |  |  | *port\_num*, |
|  |  |  | *pin\_num* ) |

**Value:**

(psel << [RX\_PSEL\_POS](#a58e6ba874d0ff5290cae17d3a6f11905) | pin\_num << [RX\_PIN\_NUM\_POS](#a8d620aa7e9514a75e3affc1ef8e950c9) | port\_num << [RX\_PORT\_NUM\_POS](#a33c8631dc344fa69c4e14e4cb43b490b))

[RX\_PORT\_NUM\_POS](#a33c8631dc344fa69c4e14e4cb43b490b)

#define RX\_PORT\_NUM\_POS

**Definition** pinctrl-rx.h:10

[RX\_PSEL\_POS](#a58e6ba874d0ff5290cae17d3a6f11905)

#define RX\_PSEL\_POS

**Definition** pinctrl-rx.h:17

[RX\_PIN\_NUM\_POS](#a8d620aa7e9514a75e3affc1ef8e950c9)

#define RX\_PIN\_NUM\_POS

**Definition** pinctrl-rx.h:13

## [◆ ](#af0ee9eb8939cfd4e527a66c3d0f58f32)RX\_PSEL\_MASK

| #define RX\_PSEL\_MASK   0x1f |
| --- |

## [◆ ](#a788c40b5e5a82083432968317a7d6c4e)RX\_PSEL\_P0nPFS\_ADTRG0

| #define RX\_PSEL\_P0nPFS\_ADTRG0   0x1 |
| --- |

## [◆ ](#aad48291cdeb29d13f13ebe0c07259594)RX\_PSEL\_P0nPFS\_HIZ

| #define RX\_PSEL\_P0nPFS\_HIZ   0x0 |
| --- |

## [◆ ](#a9925ff98a4835feb94f295004f896c3c)RX\_PSEL\_P1nPFS\_ADTRG0

| #define RX\_PSEL\_P1nPFS\_ADTRG0   0x9 |
| --- |

## [◆ ](#a930c4df4b47a5b7dfe3278f0daea4654)RX\_PSEL\_P1nPFS\_CTS1

| #define RX\_PSEL\_P1nPFS\_CTS1   0xB |
| --- |

## [◆ ](#a8da1cb599f5ead00b7c142315b79ecc8)RX\_PSEL\_P1nPFS\_MISOA

| #define RX\_PSEL\_P1nPFS\_MISOA   0xD |
| --- |

## [◆ ](#a6aa86965cd5ea93e6d300d9ea64dd4ed)RX\_PSEL\_P1nPFS\_MOSIA

| #define RX\_PSEL\_P1nPFS\_MOSIA   0xD |
| --- |

## [◆ ](#a2ce48e6029d58e6a0d9bb5a1d968ebe6)RX\_PSEL\_P1nPFS\_MTCLKA

| #define RX\_PSEL\_P1nPFS\_MTCLKA   0x02 |
| --- |

## [◆ ](#aadd46dc94695780f5c55fbdd7b9a831d)RX\_PSEL\_P1nPFS\_MTCLKB

| #define RX\_PSEL\_P1nPFS\_MTCLKB   0x02 |
| --- |

## [◆ ](#a1000a138a65b0a2dfbf56ced7d00508f)RX\_PSEL\_P1nPFS\_MTIOC0B

| #define RX\_PSEL\_P1nPFS\_MTIOC0B   0x01 |
| --- |

## [◆ ](#a66b406de32b93246a9710d580deebf97)RX\_PSEL\_P1nPFS\_MTIOC3A

| #define RX\_PSEL\_P1nPFS\_MTIOC3A   0x01 |
| --- |

## [◆ ](#a9c64a0d8e03b70ca45aebd8934f2a7d2)RX\_PSEL\_P1nPFS\_MTIOC3B

| #define RX\_PSEL\_P1nPFS\_MTIOC3B   0x02 |
| --- |

## [◆ ](#a8a4dc3f07c7c9da139afcfb48c61277b)RX\_PSEL\_P1nPFS\_MTIOC3C

| #define RX\_PSEL\_P1nPFS\_MTIOC3C   0x01 |
| --- |

## [◆ ](#a642a310aca921400209039992742d2c5)RX\_PSEL\_P1nPFS\_MTIOC3D

| #define RX\_PSEL\_P1nPFS\_MTIOC3D   0x02 |
| --- |

## [◆ ](#aa8cfdc8a4947b721c332375226f271a4)RX\_PSEL\_P1nPFS\_POE8

| #define RX\_PSEL\_P1nPFS\_POE8   0x7 |
| --- |

## [◆ ](#a11122cc8240be20777710e75cf00122d)RX\_PSEL\_P1nPFS\_RTCOUT

| #define RX\_PSEL\_P1nPFS\_RTCOUT   0x7 |
| --- |

## [◆ ](#a0511157c9149ab334d022f46ddcf952b)RX\_PSEL\_P1nPFS\_RTS1

| #define RX\_PSEL\_P1nPFS\_RTS1   0xB |
| --- |

## [◆ ](#ac9945fc6a230be884638863306b515a1)RX\_PSEL\_P1nPFS\_RXD1

| #define RX\_PSEL\_P1nPFS\_RXD1   0xA |
| --- |

## [◆ ](#a313cec1391590cdf0e371b1975f6a2a9)RX\_PSEL\_P1nPFS\_SCL

| #define RX\_PSEL\_P1nPFS\_SCL   0xF |
| --- |

## [◆ ](#a3e8733fee102ece6c412fbfbe2d40482)RX\_PSEL\_P1nPFS\_SDA

| #define RX\_PSEL\_P1nPFS\_SDA   0xF |
| --- |

## [◆ ](#a252044667e25c0c87970b263bce8e8a1)RX\_PSEL\_P1nPFS\_SMISO1

| #define RX\_PSEL\_P1nPFS\_SMISO1   0xA |
| --- |

## [◆ ](#acd3dc3dc1fa13168bb3052c8e4584019)RX\_PSEL\_P1nPFS\_SMOSI1

| #define RX\_PSEL\_P1nPFS\_SMOSI1   0xA |
| --- |

## [◆ ](#a60b58d2d19666957f3725b87719538da)RX\_PSEL\_P1nPFS\_SS1

| #define RX\_PSEL\_P1nPFS\_SS1   0xB |
| --- |

## [◆ ](#a1ce8f440328f511c996bb79f957fedde)RX\_PSEL\_P1nPFS\_SSCL1

| #define RX\_PSEL\_P1nPFS\_SSCL1   0xA |
| --- |

## [◆ ](#a7ed94521bbda969b0b81f19d39fd563a)RX\_PSEL\_P1nPFS\_SSDA1

| #define RX\_PSEL\_P1nPFS\_SSDA1   0xA |
| --- |

## [◆ ](#a9bd05a6002222fd6febd332fc7a0525f)RX\_PSEL\_P1nPFS\_TMCI1

| #define RX\_PSEL\_P1nPFS\_TMCI1   0x5 |
| --- |

## [◆ ](#a2c1fe2875a8f8f104cf7f36c6d6fca67)RX\_PSEL\_P1nPFS\_TMCI2

| #define RX\_PSEL\_P1nPFS\_TMCI2   0x5 |
| --- |

## [◆ ](#ad047c079d8ca34f4a489e63ea3ddd642)RX\_PSEL\_P1nPFS\_TMO1

| #define RX\_PSEL\_P1nPFS\_TMO1   0x5 |
| --- |

## [◆ ](#a6c59dcdcd76a0bb4c6cafdda3159bb68)RX\_PSEL\_P1nPFS\_TMO2

| #define RX\_PSEL\_P1nPFS\_TMO2   0x5 |
| --- |

## [◆ ](#a82f52b919e109c185647242656538fb7)RX\_PSEL\_P1nPFS\_TMO3

| #define RX\_PSEL\_P1nPFS\_TMO3   0x5 |
| --- |

## [◆ ](#ac01000e60804a365ec8ab51235362e53)RX\_PSEL\_P1nPFS\_TMRI2

| #define RX\_PSEL\_P1nPFS\_TMRI2   0x5 |
| --- |

## [◆ ](#a09021fba8d5f0b62cadab76c408f0903)RX\_PSEL\_P1nPFS\_TS5

| #define RX\_PSEL\_P1nPFS\_TS5   0x19 |
| --- |

## [◆ ](#a1409faaabb112be224a47aedb34564a0)RX\_PSEL\_P1nPFS\_TS6

| #define RX\_PSEL\_P1nPFS\_TS6   0x19 |
| --- |

## [◆ ](#a9e8985892fa25c60c00770d0265c7076)RX\_PSEL\_P1nPFS\_TXD1

| #define RX\_PSEL\_P1nPFS\_TXD1   0xA |
| --- |

## [◆ ](#aa59954a10be331a3adf63cae63cc6781)RX\_PSEL\_P2nPFS\_ADTRG0

| #define RX\_PSEL\_P2nPFS\_ADTRG0   0x9 |
| --- |

## [◆ ](#af620f79d871fceafd43648bbf482ff74)RX\_PSEL\_P2nPFS\_CTS0

| #define RX\_PSEL\_P2nPFS\_CTS0   0xB |
| --- |

## [◆ ](#a946c850386e432cb2365facb3e8253f4)RX\_PSEL\_P2nPFS\_MTCLKA

| #define RX\_PSEL\_P2nPFS\_MTCLKA   0x02 |
| --- |

## [◆ ](#a2637c6326ea9f8792c5bcbc1d2cb6a86)RX\_PSEL\_P2nPFS\_MTCLKB

| #define RX\_PSEL\_P2nPFS\_MTCLKB   0x02 |
| --- |

## [◆ ](#a26e1bebe6fa54f6f542834d36e6a5a15)RX\_PSEL\_P2nPFS\_MTCLKC

| #define RX\_PSEL\_P2nPFS\_MTCLKC   0x02 |
| --- |

## [◆ ](#a83170987a059d0f4b4474518d1dc9f5c)RX\_PSEL\_P2nPFS\_MTCLKD

| #define RX\_PSEL\_P2nPFS\_MTCLKD   0x02 |
| --- |

## [◆ ](#ae03c6c7a8a1c0d67f314533ccfac715e)RX\_PSEL\_P2nPFS\_MTIOC1A

| #define RX\_PSEL\_P2nPFS\_MTIOC1A   0x01 |
| --- |

## [◆ ](#a148fe9efdef4a2497296f9268c1a8944)RX\_PSEL\_P2nPFS\_MTIOC1B

| #define RX\_PSEL\_P2nPFS\_MTIOC1B   0x01 |
| --- |

## [◆ ](#ae0cfb4142c65b33e227907298b404541)RX\_PSEL\_P2nPFS\_MTIOC2A

| #define RX\_PSEL\_P2nPFS\_MTIOC2A   0x01 |
| --- |

## [◆ ](#a9aa22ce6e3bc9855075281bb6b853c7a)RX\_PSEL\_P2nPFS\_MTIOC2B

| #define RX\_PSEL\_P2nPFS\_MTIOC2B   0x01 |
| --- |

## [◆ ](#adda0ffa844d9be1603697598618c7a69)RX\_PSEL\_P2nPFS\_MTIOC3B

| #define RX\_PSEL\_P2nPFS\_MTIOC3B   0x01 |
| --- |

## [◆ ](#a2ac9fabd592b2c4ad45b8d36475aefde)RX\_PSEL\_P2nPFS\_MTIOC3D

| #define RX\_PSEL\_P2nPFS\_MTIOC3D   0x01 |
| --- |

## [◆ ](#a8f33600b8a26ad32056d89dff90f93af)RX\_PSEL\_P2nPFS\_MTIOC4A

| #define RX\_PSEL\_P2nPFS\_MTIOC4A   0x01 |
| --- |

## [◆ ](#a035bdd99f2a958b9bef5d7e78be3aa9b)RX\_PSEL\_P2nPFS\_MTIOC4C

| #define RX\_PSEL\_P2nPFS\_MTIOC4C   0x01 |
| --- |

## [◆ ](#aa35d75b72a5aab5dd3ca61f158c401df)RX\_PSEL\_P2nPFS\_RTS0

| #define RX\_PSEL\_P2nPFS\_RTS0   0xB |
| --- |

## [◆ ](#a644d0126190885ca9dbdfe09d3891911)RX\_PSEL\_P2nPFS\_RXD0

| #define RX\_PSEL\_P2nPFS\_RXD0   0xA |
| --- |

## [◆ ](#a8f18c698cfc5111ece10aada38e8ed0b)RX\_PSEL\_P2nPFS\_SCK0

| #define RX\_PSEL\_P2nPFS\_SCK0   0xA |
| --- |

## [◆ ](#a3d23cbbaffcfce61a09c552d128ade85)RX\_PSEL\_P2nPFS\_SCK1

| #define RX\_PSEL\_P2nPFS\_SCK1   0xA |
| --- |

## [◆ ](#a3c7dbd625604d3baab379953eecd4dd2)RX\_PSEL\_P2nPFS\_SMISO0

| #define RX\_PSEL\_P2nPFS\_SMISO0   0xA |
| --- |

## [◆ ](#a2fc0d75b547deee80cc88f4c15497873)RX\_PSEL\_P2nPFS\_SMOSI0

| #define RX\_PSEL\_P2nPFS\_SMOSI0   0xA |
| --- |

## [◆ ](#ad5241521982236501d3f59c315a212a7)RX\_PSEL\_P2nPFS\_SMOSI1

| #define RX\_PSEL\_P2nPFS\_SMOSI1   0xA |
| --- |

## [◆ ](#a963049f6db48bb8d470dc20f1af0b229)RX\_PSEL\_P2nPFS\_SS0

| #define RX\_PSEL\_P2nPFS\_SS0   0xB |
| --- |

## [◆ ](#acb6c1ab729ac222872edcac9be75388d)RX\_PSEL\_P2nPFS\_SSCL0

| #define RX\_PSEL\_P2nPFS\_SSCL0   0xA |
| --- |

## [◆ ](#a53817593b75446ddd77490d5144d07f3)RX\_PSEL\_P2nPFS\_SSDA0

| #define RX\_PSEL\_P2nPFS\_SSDA0   0xA |
| --- |

## [◆ ](#ae3dbbed0bf6c3c928668fdcdfb8c2bd2)RX\_PSEL\_P2nPFS\_SSDA1

| #define RX\_PSEL\_P2nPFS\_SSDA1   0xA |
| --- |

## [◆ ](#a54b553a2a753b03869c5834d5f7cf1ad)RX\_PSEL\_P2nPFS\_TMCI0

| #define RX\_PSEL\_P2nPFS\_TMCI0   0x5 |
| --- |

## [◆ ](#a0418b8e109dccab2a5b39b73c8d34de6)RX\_PSEL\_P2nPFS\_TMCI3

| #define RX\_PSEL\_P2nPFS\_TMCI3   0x5 |
| --- |

## [◆ ](#a39e6f7ec8b8e7ae970e6073e50a7ab2f)RX\_PSEL\_P2nPFS\_TMO0

| #define RX\_PSEL\_P2nPFS\_TMO0   0x5 |
| --- |

## [◆ ](#ad2b07aa7a06c371eac12cc1cc0ba122b)RX\_PSEL\_P2nPFS\_TMO1

| #define RX\_PSEL\_P2nPFS\_TMO1   0x5 |
| --- |

## [◆ ](#a088e40350516ce25b1c5644e1f68661b)RX\_PSEL\_P2nPFS\_TMRI0

| #define RX\_PSEL\_P2nPFS\_TMRI0   0x5 |
| --- |

## [◆ ](#a464af4730f95dbf0e25e38f218408f44)RX\_PSEL\_P2nPFS\_TMRI1

| #define RX\_PSEL\_P2nPFS\_TMRI1   0x5 |
| --- |

## [◆ ](#aa6b377d29e609a0a6cf9314f792a84c0)RX\_PSEL\_P2nPFS\_TS3

| #define RX\_PSEL\_P2nPFS\_TS3   0x19 |
| --- |

## [◆ ](#a9c4eb492ef55cbe8294b9a785e178ac8)RX\_PSEL\_P2nPFS\_TS4

| #define RX\_PSEL\_P2nPFS\_TS4   0x19 |
| --- |

## [◆ ](#a296d05ae948f7bd999ad5549e9923af6)RX\_PSEL\_P2nPFS\_TXD0

| #define RX\_PSEL\_P2nPFS\_TXD0   0xA |
| --- |

## [◆ ](#a52375313e6b8333693f42925fa875061)RX\_PSEL\_P2nPFS\_TXD1

| #define RX\_PSEL\_P2nPFS\_TXD1   0xA |
| --- |

## [◆ ](#a08e879eb32d7096f08827e121e92fe50)RX\_PSEL\_P3nPFS\_CTS1

| #define RX\_PSEL\_P3nPFS\_CTS1   0xB |
| --- |

## [◆ ](#a912cf155ad9b90d57cc2e54b5bc5f08a)RX\_PSEL\_P3nPFS\_MTIOC0A

| #define RX\_PSEL\_P3nPFS\_MTIOC0A   0x01 |
| --- |

## [◆ ](#a94532f7a2a10d1ab8e2ba677e2697026)RX\_PSEL\_P3nPFS\_MTIOC0C

| #define RX\_PSEL\_P3nPFS\_MTIOC0C   0x01 |
| --- |

## [◆ ](#a64da185fff98b3917f8895dd5d7baf65)RX\_PSEL\_P3nPFS\_MTIOC0D

| #define RX\_PSEL\_P3nPFS\_MTIOC0D   0x01 |
| --- |

## [◆ ](#a7ee97491a03815f769f10104fb8f3abc)RX\_PSEL\_P3nPFS\_MTIOC4B

| #define RX\_PSEL\_P3nPFS\_MTIOC4B   0x01 |
| --- |

## [◆ ](#addb1546bf2cf2f44ffc69e763ac977ee)RX\_PSEL\_P3nPFS\_MTIOC4D

| #define RX\_PSEL\_P3nPFS\_MTIOC4D   0x01 |
| --- |

## [◆ ](#a9d29e69cf44686dc6acf2876fae48ea5)RX\_PSEL\_P3nPFS\_POE2

| #define RX\_PSEL\_P3nPFS\_POE2   0x7 |
| --- |

## [◆ ](#a7549ce5ac03ef03c97b13d7421540c02)RX\_PSEL\_P3nPFS\_POE3

| #define RX\_PSEL\_P3nPFS\_POE3   0x7 |
| --- |

## [◆ ](#aedd2d3acb9455157b0f9920911af5c10)RX\_PSEL\_P3nPFS\_POE8

| #define RX\_PSEL\_P3nPFS\_POE8   0x7 |
| --- |

## [◆ ](#ae61abf1a2343b39ffd50aa4f1cea1437)RX\_PSEL\_P3nPFS\_RTCOUT

| #define RX\_PSEL\_P3nPFS\_RTCOUT   0x7 |
| --- |

## [◆ ](#a6366c1fd6ad7e5d5ed540d25ca00e836)RX\_PSEL\_P3nPFS\_RTS1

| #define RX\_PSEL\_P3nPFS\_RTS1   0xB |
| --- |

## [◆ ](#ae0da688c9e0bb84b4862d194269bec2a)RX\_PSEL\_P3nPFS\_RXD1

| #define RX\_PSEL\_P3nPFS\_RXD1   0xA |
| --- |

## [◆ ](#aac363230de113bd65dd17fe3b05c0a45)RX\_PSEL\_P3nPFS\_RXD6

| #define RX\_PSEL\_P3nPFS\_RXD6   0xB |
| --- |

## [◆ ](#a523ea0495c5667c4acb97100bcb81373)RX\_PSEL\_P3nPFS\_SCK6

| #define RX\_PSEL\_P3nPFS\_SCK6   0xB |
| --- |

## [◆ ](#a89adb49de0a99e0548e8ed242d4f0b62)RX\_PSEL\_P3nPFS\_SMISO1

| #define RX\_PSEL\_P3nPFS\_SMISO1   0xA |
| --- |

## [◆ ](#afcefa777d2064118ed7aec73bac19f08)RX\_PSEL\_P3nPFS\_SMISO6

| #define RX\_PSEL\_P3nPFS\_SMISO6   0xB |
| --- |

## [◆ ](#abd8dde16e830b4d61be34bde6c8552d2)RX\_PSEL\_P3nPFS\_SMOSI6

| #define RX\_PSEL\_P3nPFS\_SMOSI6   0xB |
| --- |

## [◆ ](#af53411085e8857438e5c9abb7888079f)RX\_PSEL\_P3nPFS\_SS1

| #define RX\_PSEL\_P3nPFS\_SS1   0xB |
| --- |

## [◆ ](#a43f68e75a17d68fde57806db3691c3b2)RX\_PSEL\_P3nPFS\_SSCL1

| #define RX\_PSEL\_P3nPFS\_SSCL1   0xA |
| --- |

## [◆ ](#a2d42e557aa6ba6e3ac2adb7215618935)RX\_PSEL\_P3nPFS\_SSCL6

| #define RX\_PSEL\_P3nPFS\_SSCL6   0xB |
| --- |

## [◆ ](#aebd62a6fd208525bac61b7c198578f23)RX\_PSEL\_P3nPFS\_SSDA6

| #define RX\_PSEL\_P3nPFS\_SSDA6   0xB |
| --- |

## [◆ ](#a5cfb12676b99d16d7602d510f182b5cb)RX\_PSEL\_P3nPFS\_TMCI2

| #define RX\_PSEL\_P3nPFS\_TMCI2   0x5 |
| --- |

## [◆ ](#a9861a7bd48e1ec94eca541d230164874)RX\_PSEL\_P3nPFS\_TMCI3

| #define RX\_PSEL\_P3nPFS\_TMCI3   0x5 |
| --- |

## [◆ ](#a9071547e298af703f78fb8602d479ac6)RX\_PSEL\_P3nPFS\_TMO3

| #define RX\_PSEL\_P3nPFS\_TMO3   0x5 |
| --- |

## [◆ ](#aa93265941791184b4aede61f922c2b18)RX\_PSEL\_P3nPFS\_TMRI3

| #define RX\_PSEL\_P3nPFS\_TMRI3   0x5 |
| --- |

## [◆ ](#a9b1b5dfc5099562d6965bf801b00c71d)RX\_PSEL\_P3nPFS\_TS0

| #define RX\_PSEL\_P3nPFS\_TS0   0x19 |
| --- |

## [◆ ](#a04794c793e252a3d9d260bc7902295ba)RX\_PSEL\_P3nPFS\_TS1

| #define RX\_PSEL\_P3nPFS\_TS1   0x19 |
| --- |

## [◆ ](#ac8312cdd9d396e15081d5873b5f25afd)RX\_PSEL\_P3nPFS\_TS2

| #define RX\_PSEL\_P3nPFS\_TS2   0x19 |
| --- |

## [◆ ](#ae57aed1d69d9e791943206ea9c75eedc)RX\_PSEL\_P3nPFS\_TXD6

| #define RX\_PSEL\_P3nPFS\_TXD6   0xB |
| --- |

## [◆ ](#a142d0481f6512159c7f280419834f96f)RX\_PSEL\_P5nPFS\_MTIOC4B

| #define RX\_PSEL\_P5nPFS\_MTIOC4B   0x01 |
| --- |

## [◆ ](#a73b2361a0599be381e5b234b852b1dec)RX\_PSEL\_P5nPFS\_MTIOC4D

| #define RX\_PSEL\_P5nPFS\_MTIOC4D   0x01 |
| --- |

## [◆ ](#a3f85d862897a3ed788adbac2dcdfd3ce)RX\_PSEL\_P5nPFS\_PMC0

| #define RX\_PSEL\_P5nPFS\_PMC0   0x19 |
| --- |

## [◆ ](#a1813788221910ec1a0e1065d3745864c)RX\_PSEL\_P5nPFS\_PMC1

| #define RX\_PSEL\_P5nPFS\_PMC1   0x19 |
| --- |

## [◆ ](#a384f77f5ef58df21c990ec1f244a582d)RX\_PSEL\_P5nPFS\_TMCI1

| #define RX\_PSEL\_P5nPFS\_TMCI1   0x5 |
| --- |

## [◆ ](#aeb2b78345a96979b0938c17f032739cc)RX\_PSEL\_P5nPFS\_TMO3

| #define RX\_PSEL\_P5nPFS\_TMO3   0x5 |
| --- |

## [◆ ](#aee8c3bbb3a4341bf23aae2376c0d63da)RX\_PSEL\_P5nPFS\_TS11

| #define RX\_PSEL\_P5nPFS\_TS11   0x19 |
| --- |

## [◆ ](#a1fae9f412c3a00786292e6a55a480ea0)RX\_PSEL\_P5nPFS\_TS12

| #define RX\_PSEL\_P5nPFS\_TS12   0x19 |
| --- |

## [◆ ](#ac0c66c71e791fbcdf75a15c1acc58bc2)RX\_PSEL\_PAnPFS\_CACREF

| #define RX\_PSEL\_PAnPFS\_CACREF   0x7 |
| --- |

## [◆ ](#aca996f81268ef4573b837b4da0491ef4)RX\_PSEL\_PAnPFS\_CTS5

| #define RX\_PSEL\_PAnPFS\_CTS5   0xB |
| --- |

## [◆ ](#abc8dccd90af6bfbb74012df17f256709)RX\_PSEL\_PAnPFS\_MISOA

| #define RX\_PSEL\_PAnPFS\_MISOA   0xD |
| --- |

## [◆ ](#abcf66e981b8dce6df3552dfe23f87440)RX\_PSEL\_PAnPFS\_MOSIA

| #define RX\_PSEL\_PAnPFS\_MOSIA   0xD |
| --- |

## [◆ ](#af579ae4fd94b09b8d76a9f8f89e6acb3)RX\_PSEL\_PAnPFS\_MTCLKA

| #define RX\_PSEL\_PAnPFS\_MTCLKA   0x02 |
| --- |

## [◆ ](#a8b47dba63dd54bd6a7034fae4b875d15)RX\_PSEL\_PAnPFS\_MTCLKB

| #define RX\_PSEL\_PAnPFS\_MTCLKB   0x02 |
| --- |

## [◆ ](#a82fd05e3e993fb86fc4d18a5ec7cddc6)RX\_PSEL\_PAnPFS\_MTCLKC

| #define RX\_PSEL\_PAnPFS\_MTCLKC   0x02 |
| --- |

## [◆ ](#a970d467907e0c4e8829f20eb0de9e4c4)RX\_PSEL\_PAnPFS\_MTCLKD

| #define RX\_PSEL\_PAnPFS\_MTCLKD   0x02 |
| --- |

## [◆ ](#a884e497ea0370a0fd1fdd351f5b6a786)RX\_PSEL\_PAnPFS\_MTIOC0B

| #define RX\_PSEL\_PAnPFS\_MTIOC0B   0x01 |
| --- |

## [◆ ](#a2b8d4b23f5172d4798e8519644e35e9a)RX\_PSEL\_PAnPFS\_MTIOC0D

| #define RX\_PSEL\_PAnPFS\_MTIOC0D   0x01 |
| --- |

## [◆ ](#a87c47d0c6734ce3547b23754234502f4)RX\_PSEL\_PAnPFS\_MTIOC4A

| #define RX\_PSEL\_PAnPFS\_MTIOC4A   0x01 |
| --- |

## [◆ ](#aba913f6670da680ac45030c6ec6f427a)RX\_PSEL\_PAnPFS\_MTIOC5U

| #define RX\_PSEL\_PAnPFS\_MTIOC5U   0x01 |
| --- |

## [◆ ](#a475663b42a042fe06c9f340e3e63adb1)RX\_PSEL\_PAnPFS\_MTIOC5V

| #define RX\_PSEL\_PAnPFS\_MTIOC5V   0x01 |
| --- |

## [◆ ](#a3985ebc7577dc17f64ab2e2c0a676910)RX\_PSEL\_PAnPFS\_POE2

| #define RX\_PSEL\_PAnPFS\_POE2   0x7 |
| --- |

## [◆ ](#a3001136d224d46c165f437e44733457b)RX\_PSEL\_PAnPFS\_RSPCKA

| #define RX\_PSEL\_PAnPFS\_RSPCKA   0xD |
| --- |

## [◆ ](#a2a3f02bd3a18a96355ecc8c6aca215bd)RX\_PSEL\_PAnPFS\_RTS5

| #define RX\_PSEL\_PAnPFS\_RTS5   0xB |
| --- |

## [◆ ](#a819aa2b70f2cbb0165c93fc06b1784e2)RX\_PSEL\_PAnPFS\_RXD5

| #define RX\_PSEL\_PAnPFS\_RXD5   0xA |
| --- |

## [◆ ](#a4a358940161583dac3d6e99e5a65da7a)RX\_PSEL\_PAnPFS\_SCK5

| #define RX\_PSEL\_PAnPFS\_SCK5   0xA |
| --- |

## [◆ ](#aa7ffb4053ffa015c30a6906885a007bc)RX\_PSEL\_PAnPFS\_SMISO5

| #define RX\_PSEL\_PAnPFS\_SMISO5   0xA |
| --- |

## [◆ ](#aadf3aca998e7796fb8724264966b1c17)RX\_PSEL\_PAnPFS\_SMOSI5

| #define RX\_PSEL\_PAnPFS\_SMOSI5   0xA |
| --- |

## [◆ ](#acdbcff26b1e0c1ec95904359831101a6)RX\_PSEL\_PAnPFS\_SS5

| #define RX\_PSEL\_PAnPFS\_SS5   0xB |
| --- |

## [◆ ](#a080fa1148d00016a8663f0adc0f3a81c)RX\_PSEL\_PAnPFS\_SSCL5

| #define RX\_PSEL\_PAnPFS\_SSCL5   0xA |
| --- |

## [◆ ](#ab5eec46fe3c3ec8a79b78d6f14652631)RX\_PSEL\_PAnPFS\_SSDA5

| #define RX\_PSEL\_PAnPFS\_SSDA5   0xA |
| --- |

## [◆ ](#ac5a1bb8cc48cc3975e989d0ae8301b85)RX\_PSEL\_PAnPFS\_SSLA0

| #define RX\_PSEL\_PAnPFS\_SSLA0   0xD |
| --- |

## [◆ ](#a695b1d61fa2af644e8e713bde9008b67)RX\_PSEL\_PAnPFS\_SSLA1

| #define RX\_PSEL\_PAnPFS\_SSLA1   0xD |
| --- |

## [◆ ](#a4f9ce98bb1087fdfa8a4820dec774b88)RX\_PSEL\_PAnPFS\_SSLA2

| #define RX\_PSEL\_PAnPFS\_SSLA2   0xD |
| --- |

## [◆ ](#a4a1682361951b36cbaca4a469ede48d7)RX\_PSEL\_PAnPFS\_SSLA3

| #define RX\_PSEL\_PAnPFS\_SSLA3   0xD |
| --- |

## [◆ ](#a26ce828aab38d7005ae7ccf5d3809f1e)RX\_PSEL\_PAnPFS\_TMCI3

| #define RX\_PSEL\_PAnPFS\_TMCI3   0x5 |
| --- |

## [◆ ](#a50d18bf6681275da284b2348aaa626d7)RX\_PSEL\_PAnPFS\_TMRI0

| #define RX\_PSEL\_PAnPFS\_TMRI0   0x5 |
| --- |

## [◆ ](#a09b4a8fe6520da1a3239890590ef90d3)RX\_PSEL\_PAnPFS\_TS26

| #define RX\_PSEL\_PAnPFS\_TS26   0x19 |
| --- |

## [◆ ](#a988e53dc6d5a7c139747be285598fe96)RX\_PSEL\_PAnPFS\_TS27

| #define RX\_PSEL\_PAnPFS\_TS27   0x19 |
| --- |

## [◆ ](#ae00078451e050502337206f9bd6362bc)RX\_PSEL\_PAnPFS\_TS28

| #define RX\_PSEL\_PAnPFS\_TS28   0x19 |
| --- |

## [◆ ](#a67cf8ad3d73c35f2659a2af3f5b3d6f3)RX\_PSEL\_PAnPFS\_TS29

| #define RX\_PSEL\_PAnPFS\_TS29   0x19 |
| --- |

## [◆ ](#a4b080b72196e98924c3a9d02b2d1756e)RX\_PSEL\_PAnPFS\_TS30

| #define RX\_PSEL\_PAnPFS\_TS30   0x19 |
| --- |

## [◆ ](#a8b434c0a6b494ab4020b49c8df2707c0)RX\_PSEL\_PAnPFS\_TS31

| #define RX\_PSEL\_PAnPFS\_TS31   0x19 |
| --- |

## [◆ ](#a0b2a031acfb9f73f5e34d58d1bf21a3e)RX\_PSEL\_PAnPFS\_TS32

| #define RX\_PSEL\_PAnPFS\_TS32   0x19 |
| --- |

## [◆ ](#a6cda040400df3fc63b2ea5b35b09347e)RX\_PSEL\_PAnPFS\_TXD5

| #define RX\_PSEL\_PAnPFS\_TXD5   0xA |
| --- |

## [◆ ](#a230a3999d4881be6074e4380107075ce)RX\_PSEL\_PBnPFS\_CMPOB1

| #define RX\_PSEL\_PBnPFS\_CMPOB1   0x10 |
| --- |

## [◆ ](#a2fdd18ec059ab4e4d8a2284b16f8c160)RX\_PSEL\_PBnPFS\_CTS6

| #define RX\_PSEL\_PBnPFS\_CTS6   0xB |
| --- |

## [◆ ](#afc347de58db4d6795ded3a76afb1abf6)RX\_PSEL\_PBnPFS\_CTS9

| #define RX\_PSEL\_PBnPFS\_CTS9   0xB |
| --- |

## [◆ ](#ab70484c773d08b3331e93d5f16e74e8a)RX\_PSEL\_PBnPFS\_MTIOC0A

| #define RX\_PSEL\_PBnPFS\_MTIOC0A   0x01 |
| --- |

## [◆ ](#aa16664b39a03dc8f5cf1eff2df22d132)RX\_PSEL\_PBnPFS\_MTIOC0C

| #define RX\_PSEL\_PBnPFS\_MTIOC0C   0x01 |
| --- |

## [◆ ](#a867fdf6ad0579c0022dc82999e161db6)RX\_PSEL\_PBnPFS\_MTIOC1B

| #define RX\_PSEL\_PBnPFS\_MTIOC1B   0x02 |
| --- |

## [◆ ](#a78103875ae7f2bf781da23c8033fed59)RX\_PSEL\_PBnPFS\_MTIOC2A

| #define RX\_PSEL\_PBnPFS\_MTIOC2A   0x01 |
| --- |

## [◆ ](#a1e5ccf9190a3dc5970f4254d737ae072)RX\_PSEL\_PBnPFS\_MTIOC3B

| #define RX\_PSEL\_PBnPFS\_MTIOC3B   0x01 |
| --- |

## [◆ ](#ae583a13420640109ebe70590b4d499ba)RX\_PSEL\_PBnPFS\_MTIOC3D

| #define RX\_PSEL\_PBnPFS\_MTIOC3D   0x01 |
| --- |

## [◆ ](#a021849717993b6ddcd5944b737a2aaf4)RX\_PSEL\_PBnPFS\_MTIOC4A

| #define RX\_PSEL\_PBnPFS\_MTIOC4A   0x02 |
| --- |

## [◆ ](#a3375281ff859dfe401d503032a1d6b80)RX\_PSEL\_PBnPFS\_MTIOC4C

| #define RX\_PSEL\_PBnPFS\_MTIOC4C   0x02 |
| --- |

## [◆ ](#a151d204a2e111718abf98b37a5c30d02)RX\_PSEL\_PBnPFS\_MTIOC5W

| #define RX\_PSEL\_PBnPFS\_MTIOC5W   0x01 |
| --- |

## [◆ ](#a7deea898404b855145576f716f851a92)RX\_PSEL\_PBnPFS\_POE1

| #define RX\_PSEL\_PBnPFS\_POE1   0x7 |
| --- |

## [◆ ](#aaef5911c5707323f20fec35fec6bdea2)RX\_PSEL\_PBnPFS\_POE3

| #define RX\_PSEL\_PBnPFS\_POE3   0x7 |
| --- |

## [◆ ](#a9d01bbc858e16531b932ba4a10783e03)RX\_PSEL\_PBnPFS\_RSPCKA

| #define RX\_PSEL\_PBnPFS\_RSPCKA   0xD |
| --- |

## [◆ ](#a4cf58353b52de3273826db6666c94cba)RX\_PSEL\_PBnPFS\_RTS6

| #define RX\_PSEL\_PBnPFS\_RTS6   0xB |
| --- |

## [◆ ](#aefb72d4fad4867bcd5fef242322fdb46)RX\_PSEL\_PBnPFS\_RTS9

| #define RX\_PSEL\_PBnPFS\_RTS9   0xB |
| --- |

## [◆ ](#aad2ab397717736311073efe4bad48818)RX\_PSEL\_PBnPFS\_RXD6

| #define RX\_PSEL\_PBnPFS\_RXD6   0xB |
| --- |

## [◆ ](#a3560ff40295f809b6035026957014457)RX\_PSEL\_PBnPFS\_RXD9

| #define RX\_PSEL\_PBnPFS\_RXD9   0xA |
| --- |

## [◆ ](#a8b6978e1aebd1fcd55c7a543a38496ba)RX\_PSEL\_PBnPFS\_SCK6

| #define RX\_PSEL\_PBnPFS\_SCK6   0xB |
| --- |

## [◆ ](#a3ebc1ec3ce34c09b02698b4cbb3ef0ce)RX\_PSEL\_PBnPFS\_SCK9

| #define RX\_PSEL\_PBnPFS\_SCK9   0xA |
| --- |

## [◆ ](#a7e9537931de468389d51b0355754ab1f)RX\_PSEL\_PBnPFS\_SMISO6

| #define RX\_PSEL\_PBnPFS\_SMISO6   0xB |
| --- |

## [◆ ](#a95fa86bdf6128a0c911cf3258dcac3c5)RX\_PSEL\_PBnPFS\_SMISO9

| #define RX\_PSEL\_PBnPFS\_SMISO9   0xA |
| --- |

## [◆ ](#af3c3885de61f44965d296f35aeae8f78)RX\_PSEL\_PBnPFS\_SMOSI6

| #define RX\_PSEL\_PBnPFS\_SMOSI6   0xB |
| --- |

## [◆ ](#a47f17b912597e5cb66846711e37f9b6d)RX\_PSEL\_PBnPFS\_SMOSI9

| #define RX\_PSEL\_PBnPFS\_SMOSI9   0xA |
| --- |

## [◆ ](#aa543049ed2b1ad9e216ce6e85fcee876)RX\_PSEL\_PBnPFS\_SS6

| #define RX\_PSEL\_PBnPFS\_SS6   0xB |
| --- |

## [◆ ](#a8c2cef051d3a5db19460d89c608c6233)RX\_PSEL\_PBnPFS\_SS9

| #define RX\_PSEL\_PBnPFS\_SS9   0xB |
| --- |

## [◆ ](#a78aa89352d217d85b4f36bd55cc202a5)RX\_PSEL\_PBnPFS\_SSCL6

| #define RX\_PSEL\_PBnPFS\_SSCL6   0xB |
| --- |

## [◆ ](#abbc0966da3e8a31b0862639c73d298ee)RX\_PSEL\_PBnPFS\_SSCL9

| #define RX\_PSEL\_PBnPFS\_SSCL9   0xA |
| --- |

## [◆ ](#afe28b85756fab74733b87fa10ee63d8e)RX\_PSEL\_PBnPFS\_SSDA6

| #define RX\_PSEL\_PBnPFS\_SSDA6   0xB |
| --- |

## [◆ ](#a2e06bb5584c33d2124e2fc6e2b0ed381)RX\_PSEL\_PBnPFS\_SSDA9

| #define RX\_PSEL\_PBnPFS\_SSDA9   0xA |
| --- |

## [◆ ](#a1bfa8645f34a063435061facc3c4736a)RX\_PSEL\_PBnPFS\_TMCI0

| #define RX\_PSEL\_PBnPFS\_TMCI0   0x5 |
| --- |

## [◆ ](#a5e3a37d153b356ae71c638fc7010a9f7)RX\_PSEL\_PBnPFS\_TMO0

| #define RX\_PSEL\_PBnPFS\_TMO0   0x5 |
| --- |

## [◆ ](#aafc8cd3f09a9fc7b8cc3f59403ed514d)RX\_PSEL\_PBnPFS\_TMRI1

| #define RX\_PSEL\_PBnPFS\_TMRI1   0x5 |
| --- |

## [◆ ](#a7b4f647d5bdfb3fb8a2107949629994a)RX\_PSEL\_PBnPFS\_TS18

| #define RX\_PSEL\_PBnPFS\_TS18   0x19 |
| --- |

## [◆ ](#ad356f13b07220a235c1f971d2b1ab7ea)RX\_PSEL\_PBnPFS\_TS19

| #define RX\_PSEL\_PBnPFS\_TS19   0x19 |
| --- |

## [◆ ](#a364a18874eefb53563242194d1150910)RX\_PSEL\_PBnPFS\_TS20

| #define RX\_PSEL\_PBnPFS\_TS20   0x19 |
| --- |

## [◆ ](#a0342b766bac5038c1fc6134a7d1bd85f)RX\_PSEL\_PBnPFS\_TS21

| #define RX\_PSEL\_PBnPFS\_TS21   0x19 |
| --- |

## [◆ ](#a3db09a4ebeee6872100e3916a160b099)RX\_PSEL\_PBnPFS\_TS22

| #define RX\_PSEL\_PBnPFS\_TS22   0x19 |
| --- |

## [◆ ](#a66af16b3b335123ccda6d1ad5efda434)RX\_PSEL\_PBnPFS\_TS23

| #define RX\_PSEL\_PBnPFS\_TS23   0x19 |
| --- |

## [◆ ](#a4ddfb9a65c9dc5b58e08e48be2171664)RX\_PSEL\_PBnPFS\_TS24

| #define RX\_PSEL\_PBnPFS\_TS24   0x19 |
| --- |

## [◆ ](#a79f5033bf88f0d42632e70de11990c13)RX\_PSEL\_PBnPFS\_TS25

| #define RX\_PSEL\_PBnPFS\_TS25   0x19 |
| --- |

## [◆ ](#a514b3b4d6eefd9ae830f3ea29e69b07b)RX\_PSEL\_PBnPFS\_TXD6

| #define RX\_PSEL\_PBnPFS\_TXD6   0xB |
| --- |

## [◆ ](#a6a8de4826f40799a5377d6b0ddba973b)RX\_PSEL\_PBnPFS\_TXD9

| #define RX\_PSEL\_PBnPFS\_TXD9   0xA |
| --- |

## [◆ ](#af33cdb03242b52a66aa312834f738ab1)RX\_PSEL\_PCnPFS\_CACREF

| #define RX\_PSEL\_PCnPFS\_CACREF   0x7 |
| --- |

## [◆ ](#a20997f4c8188883ca8b1094a0b7e873b)RX\_PSEL\_PCnPFS\_CTS5

| #define RX\_PSEL\_PCnPFS\_CTS5   0xB |
| --- |

## [◆ ](#a0fa3dde24d9c4f689237a5e21153efcc)RX\_PSEL\_PCnPFS\_CTS8

| #define RX\_PSEL\_PCnPFS\_CTS8   0xB |
| --- |

## [◆ ](#ac8c1b07159883e4c934ce5e2bd61d057)RX\_PSEL\_PCnPFS\_MISOA

| #define RX\_PSEL\_PCnPFS\_MISOA   0xD |
| --- |

## [◆ ](#aca94166ceb510874373df19e74c1e171)RX\_PSEL\_PCnPFS\_MOSIA

| #define RX\_PSEL\_PCnPFS\_MOSIA   0xD |
| --- |

## [◆ ](#a9e0b4711dd92fdff630516fc963187c6)RX\_PSEL\_PCnPFS\_MTCLKA

| #define RX\_PSEL\_PCnPFS\_MTCLKA   0x02 |
| --- |

## [◆ ](#a73c23ead228baca49158d7486ec7f0e0)RX\_PSEL\_PCnPFS\_MTCLKB

| #define RX\_PSEL\_PCnPFS\_MTCLKB   0x02 |
| --- |

## [◆ ](#abc55942f4d533288287d602ec46a3384)RX\_PSEL\_PCnPFS\_MTCLKC

| #define RX\_PSEL\_PCnPFS\_MTCLKC   0x02 |
| --- |

## [◆ ](#a2e9e94477161bfbd4ece9e926c6b20f3)RX\_PSEL\_PCnPFS\_MTCLKD

| #define RX\_PSEL\_PCnPFS\_MTCLKD   0x02 |
| --- |

## [◆ ](#a0a0e1289dc503260b7d4d9ad99813bcf)RX\_PSEL\_PCnPFS\_MTIOC3A

| #define RX\_PSEL\_PCnPFS\_MTIOC3A   0x01 |
| --- |

## [◆ ](#accdce2d8f48796e5eaa7b6cf4bdaf225)RX\_PSEL\_PCnPFS\_MTIOC3B

| #define RX\_PSEL\_PCnPFS\_MTIOC3B   0x01 |
| --- |

## [◆ ](#a9a281dbe06b3123d1afb0809df50d188)RX\_PSEL\_PCnPFS\_MTIOC3C

| #define RX\_PSEL\_PCnPFS\_MTIOC3C   0x01 |
| --- |

## [◆ ](#adfa80b9c6df7c803e6d158e9825f7931)RX\_PSEL\_PCnPFS\_MTIOC3D

| #define RX\_PSEL\_PCnPFS\_MTIOC3D   0x01 |
| --- |

## [◆ ](#a3878479bf2dc042792d6174496038207)RX\_PSEL\_PCnPFS\_MTIOC4B

| #define RX\_PSEL\_PCnPFS\_MTIOC4B   0x01 |
| --- |

## [◆ ](#ac25138271990797712728f0e5d5909e6)RX\_PSEL\_PCnPFS\_MTIOC4D

| #define RX\_PSEL\_PCnPFS\_MTIOC4D   0x01 |
| --- |

## [◆ ](#af7fbf061ff82639825805cc3cca28a0b)RX\_PSEL\_PCnPFS\_POE0

| #define RX\_PSEL\_PCnPFS\_POE0   0x7 |
| --- |

## [◆ ](#ac88a47a2634a1f730fe58009d277c56d)RX\_PSEL\_PCnPFS\_RSPCKA

| #define RX\_PSEL\_PCnPFS\_RSPCKA   0xD |
| --- |

## [◆ ](#a5d8408785316cd7187e5fda2f7cf4152)RX\_PSEL\_PCnPFS\_RTS5

| #define RX\_PSEL\_PCnPFS\_RTS5   0xB |
| --- |

## [◆ ](#a97c6a44c096c0c5873e7a57f9c956083)RX\_PSEL\_PCnPFS\_RTS8

| #define RX\_PSEL\_PCnPFS\_RTS8   0xB |
| --- |

## [◆ ](#a5a69027c56b05fab8d7d53a6880b9423)RX\_PSEL\_PCnPFS\_RXD5

| #define RX\_PSEL\_PCnPFS\_RXD5   0xA |
| --- |

## [◆ ](#a86211091c53c6dbbdd657bce75e70986)RX\_PSEL\_PCnPFS\_RXD8

| #define RX\_PSEL\_PCnPFS\_RXD8   0xA |
| --- |

## [◆ ](#a01d49d963a3136acef38a2a831a076a1)RX\_PSEL\_PCnPFS\_SCK5

| #define RX\_PSEL\_PCnPFS\_SCK5   0xA |
| --- |

## [◆ ](#aff658c7c324fa5bf4461b7436aa97e5c)RX\_PSEL\_PCnPFS\_SCK8

| #define RX\_PSEL\_PCnPFS\_SCK8   0xA |
| --- |

## [◆ ](#a392276adc9abd36a582d590446f96038)RX\_PSEL\_PCnPFS\_SMISO5

| #define RX\_PSEL\_PCnPFS\_SMISO5   0xA |
| --- |

## [◆ ](#ae44a9ac365c5d056ee2921a5c4bcb5ee)RX\_PSEL\_PCnPFS\_SMISO8

| #define RX\_PSEL\_PCnPFS\_SMISO8   0xA |
| --- |

## [◆ ](#aa346eb221834f7e0df6d778da6ec35cd)RX\_PSEL\_PCnPFS\_SMOSI5

| #define RX\_PSEL\_PCnPFS\_SMOSI5   0xA |
| --- |

## [◆ ](#a953ca81bde404c7f9a159725a090af04)RX\_PSEL\_PCnPFS\_SMOSI8

| #define RX\_PSEL\_PCnPFS\_SMOSI8   0xA |
| --- |

## [◆ ](#a73b65f6a77adb07c2f17d1589f5e5d68)RX\_PSEL\_PCnPFS\_SS5

| #define RX\_PSEL\_PCnPFS\_SS5   0xB |
| --- |

## [◆ ](#a0b5c3248fe7278e43a9dab8bb47b347c)RX\_PSEL\_PCnPFS\_SS8

| #define RX\_PSEL\_PCnPFS\_SS8   0xB |
| --- |

## [◆ ](#a2437838e9799abd2b17b6376675e70ca)RX\_PSEL\_PCnPFS\_SSCL5

| #define RX\_PSEL\_PCnPFS\_SSCL5   0xA |
| --- |

## [◆ ](#a8990d81f5d74427c71cc37eee6647c98)RX\_PSEL\_PCnPFS\_SSCL8

| #define RX\_PSEL\_PCnPFS\_SSCL8   0xA |
| --- |

## [◆ ](#a4f2bc6a3a5b8561f37f778fa577ac0e8)RX\_PSEL\_PCnPFS\_SSDA5

| #define RX\_PSEL\_PCnPFS\_SSDA5   0xA |
| --- |

## [◆ ](#a8cba60fc83718e0dde6361fcf2fb9a5c)RX\_PSEL\_PCnPFS\_SSDA8

| #define RX\_PSEL\_PCnPFS\_SSDA8   0xA |
| --- |

## [◆ ](#a3b5990fb7b76f0befd197dac661a9036)RX\_PSEL\_PCnPFS\_SSLA0

| #define RX\_PSEL\_PCnPFS\_SSLA0   0xD |
| --- |

## [◆ ](#af7ca895592d0ac3d46cddcc40c315f70)RX\_PSEL\_PCnPFS\_SSLA1

| #define RX\_PSEL\_PCnPFS\_SSLA1   0xD |
| --- |

## [◆ ](#af563abf494e2730c8895b3fb4de6c85a)RX\_PSEL\_PCnPFS\_SSLA2

| #define RX\_PSEL\_PCnPFS\_SSLA2   0xD |
| --- |

## [◆ ](#a1c74ab46805e2ec72c1477059aa7c6f4)RX\_PSEL\_PCnPFS\_SSLA3

| #define RX\_PSEL\_PCnPFS\_SSLA3   0xD |
| --- |

## [◆ ](#aad2d8d27f0b4bcc06c69d60f4ba32415)RX\_PSEL\_PCnPFS\_TMCI1

| #define RX\_PSEL\_PCnPFS\_TMCI1   0x5 |
| --- |

## [◆ ](#a104b8044a91acadbb73c6fedd01e3128)RX\_PSEL\_PCnPFS\_TMCI2

| #define RX\_PSEL\_PCnPFS\_TMCI2   0x5 |
| --- |

## [◆ ](#aeb895a0766941862427dcfe548fe795b)RX\_PSEL\_PCnPFS\_TMO2

| #define RX\_PSEL\_PCnPFS\_TMO2   0x5 |
| --- |

## [◆ ](#aa9ca76efaf979f4f1bacb444a93c2338)RX\_PSEL\_PCnPFS\_TMRI2

| #define RX\_PSEL\_PCnPFS\_TMRI2   0x5 |
| --- |

## [◆ ](#a0f4ba5772ff554184551e10371af83ba)RX\_PSEL\_PCnPFS\_TS13

| #define RX\_PSEL\_PCnPFS\_TS13   0x19 |
| --- |

## [◆ ](#a5b61df843dcd7e9e4bc5d6e275ebb99c)RX\_PSEL\_PCnPFS\_TS14

| #define RX\_PSEL\_PCnPFS\_TS14   0x19 |
| --- |

## [◆ ](#a1c12baa481da0305da0e91d4eb3a2c31)RX\_PSEL\_PCnPFS\_TS15

| #define RX\_PSEL\_PCnPFS\_TS15   0x19 |
| --- |

## [◆ ](#a6283542c2054052770c40941cffd508e)RX\_PSEL\_PCnPFS\_TS16

| #define RX\_PSEL\_PCnPFS\_TS16   0x19 |
| --- |

## [◆ ](#ae70d84e57e3293b2916db85ffd91e7a1)RX\_PSEL\_PCnPFS\_TS17

| #define RX\_PSEL\_PCnPFS\_TS17   0x19 |
| --- |

## [◆ ](#a77444df0b11d61ceb285b18600032e88)RX\_PSEL\_PCnPFS\_TSCAP

| #define RX\_PSEL\_PCnPFS\_TSCAP   0x19 |
| --- |

## [◆ ](#a3d8cb88bf920515954d3833b2d5e90f9)RX\_PSEL\_PCnPFS\_TXD5

| #define RX\_PSEL\_PCnPFS\_TXD5   0xA |
| --- |

## [◆ ](#a257eaa3c131105d680ff05e9def319c4)RX\_PSEL\_PCnPFS\_TXD8

| #define RX\_PSEL\_PCnPFS\_TXD8   0xA |
| --- |

## [◆ ](#aafbb53acfb95de11fdf6a75e75c3fc97)RX\_PSEL\_PDnPFS\_MTIOC4B

| #define RX\_PSEL\_PDnPFS\_MTIOC4B   0x01 |
| --- |

## [◆ ](#ac3de35bbc1a916e8449698eb24a34cec)RX\_PSEL\_PDnPFS\_MTIOC4D

| #define RX\_PSEL\_PDnPFS\_MTIOC4D   0x01 |
| --- |

## [◆ ](#ab5f02479510f1babd64ba6cbb169f42c)RX\_PSEL\_PDnPFS\_MTIOC5U

| #define RX\_PSEL\_PDnPFS\_MTIOC5U   0x01 |
| --- |

## [◆ ](#a45c847394001f31be768944b7acaf906)RX\_PSEL\_PDnPFS\_MTIOC5V

| #define RX\_PSEL\_PDnPFS\_MTIOC5V   0x01 |
| --- |

## [◆ ](#a7a096c87787f645323ca16bd1ae3bac6)RX\_PSEL\_PDnPFS\_MTIOC5W

| #define RX\_PSEL\_PDnPFS\_MTIOC5W   0x01 |
| --- |

## [◆ ](#a2a77be1f3443daaab5f4b3066c1f8278)RX\_PSEL\_PDnPFS\_POE0

| #define RX\_PSEL\_PDnPFS\_POE0   0x7 |
| --- |

## [◆ ](#af94b267110bc98221219a97c58f4e697)RX\_PSEL\_PDnPFS\_POE1

| #define RX\_PSEL\_PDnPFS\_POE1   0x7 |
| --- |

## [◆ ](#a267d05d58ffcab0f60ae8427f8aecaf2)RX\_PSEL\_PDnPFS\_POE2

| #define RX\_PSEL\_PDnPFS\_POE2   0x7 |
| --- |

## [◆ ](#ae0e7f8f472d0f64c2dd328b57615dc98)RX\_PSEL\_PDnPFS\_POE3

| #define RX\_PSEL\_PDnPFS\_POE3   0x7 |
| --- |

## [◆ ](#a6c9a976cb22cc6b0e69d9d31b41e0321)RX\_PSEL\_PDnPFS\_POE8

| #define RX\_PSEL\_PDnPFS\_POE8   0x7 |
| --- |

## [◆ ](#a9733d54b731df033e6c1eda5293c5317)RX\_PSEL\_PDnPFS\_RXD6

| #define RX\_PSEL\_PDnPFS\_RXD6   0xB |
| --- |

## [◆ ](#a3e318ee5f28ce26bbd73dabed4b1a44a)RX\_PSEL\_PDnPFS\_SCK6

| #define RX\_PSEL\_PDnPFS\_SCK6   0xB |
| --- |

## [◆ ](#aa2f83777eb6e976f0451786a1f6edceb)RX\_PSEL\_PDnPFS\_SMISO6

| #define RX\_PSEL\_PDnPFS\_SMISO6   0xB |
| --- |

## [◆ ](#a8f5941502abad2c8995bc57b986ca81f)RX\_PSEL\_PDnPFS\_SMOSI6

| #define RX\_PSEL\_PDnPFS\_SMOSI6   0xB |
| --- |

## [◆ ](#a3d03c22b4f7adbb20f10208e471ce276)RX\_PSEL\_PDnPFS\_SSCL6

| #define RX\_PSEL\_PDnPFS\_SSCL6   0xB |
| --- |

## [◆ ](#a88acb98416906f6abdf2f6172d80bdaf)RX\_PSEL\_PDnPFS\_SSDA6

| #define RX\_PSEL\_PDnPFS\_SSDA6   0xB |
| --- |

## [◆ ](#a8ae0cab25d78a40565870fc28428def3)RX\_PSEL\_PDnPFS\_TXD6

| #define RX\_PSEL\_PDnPFS\_TXD6   0xB |
| --- |

## [◆ ](#a2bf6e1d791920bd5b44f10b62fb12db4)RX\_PSEL\_PEnPFS\_CLKOUT

| #define RX\_PSEL\_PEnPFS\_CLKOUT   0x9 |
| --- |

## [◆ ](#ac2d89df9365a11dd0388d122b11f2536)RX\_PSEL\_PEnPFS\_CMPOB0

| #define RX\_PSEL\_PEnPFS\_CMPOB0   0X10 |
| --- |

## [◆ ](#a49ed2fbfbd7c155fc22f744b4426502a)RX\_PSEL\_PEnPFS\_CTS12

| #define RX\_PSEL\_PEnPFS\_CTS12   0xC |
| --- |

## [◆ ](#a989c6f0452e964e6a6875b4924339b22)RX\_PSEL\_PEnPFS\_MTIOC1A

| #define RX\_PSEL\_PEnPFS\_MTIOC1A   0x02 |
| --- |

## [◆ ](#a967c82a27a33b39b1ba1ae051090e6db)RX\_PSEL\_PEnPFS\_MTIOC2B

| #define RX\_PSEL\_PEnPFS\_MTIOC2B   0x02 |
| --- |

## [◆ ](#a57abebe2638d36ca13d2d72d65436497)RX\_PSEL\_PEnPFS\_MTIOC4A

| #define RX\_PSEL\_PEnPFS\_MTIOC4A   0x01 |
| --- |

## [◆ ](#a51e4a949c884b35891f1503e489291e8)RX\_PSEL\_PEnPFS\_MTIOC4B

| #define RX\_PSEL\_PEnPFS\_MTIOC4B   0x01 |
| --- |

## [◆ ](#a6ef5a9460e67440d1f4e82c13fef35bf)RX\_PSEL\_PEnPFS\_MTIOC4C

| #define RX\_PSEL\_PEnPFS\_MTIOC4C   0x01 |
| --- |

## [◆ ](#a2f800b39f958ec49897fb7d3b0a1574f)RX\_PSEL\_PEnPFS\_MTIOC4D

| #define RX\_PSEL\_PEnPFS\_MTIOC4D   0x01 |
| --- |

## [◆ ](#a53a29ae9db04f7dab6bced306a47cfac)RX\_PSEL\_PEnPFS\_POE8

| #define RX\_PSEL\_PEnPFS\_POE8   0x7 |
| --- |

## [◆ ](#a39012da0abc5634d6ae1c1964653f392)RX\_PSEL\_PEnPFS\_RTS12

| #define RX\_PSEL\_PEnPFS\_RTS12   0xC |
| --- |

## [◆ ](#a85764cf1f6755fe00531703e20f9a587)RX\_PSEL\_PEnPFS\_RXD12

| #define RX\_PSEL\_PEnPFS\_RXD12   0xC |
| --- |

## [◆ ](#ad769da51c412edc773cad5f959364763)RX\_PSEL\_PEnPFS\_RXDX12

| #define RX\_PSEL\_PEnPFS\_RXDX12   0xC |
| --- |

## [◆ ](#af2cb8b0acdc39ba3a4a659394a6884e5)RX\_PSEL\_PEnPFS\_SCK12

| #define RX\_PSEL\_PEnPFS\_SCK12   0xC |
| --- |

## [◆ ](#a58da776438c101eb043756f40ef5259a)RX\_PSEL\_PEnPFS\_SIOX12

| #define RX\_PSEL\_PEnPFS\_SIOX12   0xC |
| --- |

## [◆ ](#acbacde7e28a5160ec6190aee9f3b4706)RX\_PSEL\_PEnPFS\_SMISO12

| #define RX\_PSEL\_PEnPFS\_SMISO12   0xC |
| --- |

## [◆ ](#a6fed05bb93fd3a18a53372660a6faaff)RX\_PSEL\_PEnPFS\_SMOSI12

| #define RX\_PSEL\_PEnPFS\_SMOSI12   0xC |
| --- |

## [◆ ](#abc093255f500eb7bbc1aac866afe7ef6)RX\_PSEL\_PEnPFS\_SS12

| #define RX\_PSEL\_PEnPFS\_SS12   0xC |
| --- |

## [◆ ](#a582c1aad6d4ce2aae7d683cbd179950e)RX\_PSEL\_PEnPFS\_SSCL12

| #define RX\_PSEL\_PEnPFS\_SSCL12   0xC |
| --- |

## [◆ ](#ae63305a2e7c8d27d85c7702e5826c918)RX\_PSEL\_PEnPFS\_SSDA12

| #define RX\_PSEL\_PEnPFS\_SSDA12   0xC |
| --- |

## [◆ ](#ad19b9859c60e5e84cf356a72048005d3)RX\_PSEL\_PEnPFS\_TS33

| #define RX\_PSEL\_PEnPFS\_TS33   0X19 |
| --- |

## [◆ ](#a301d3eaf6cf49e216b3bf0759b789bea)RX\_PSEL\_PEnPFS\_TS34

| #define RX\_PSEL\_PEnPFS\_TS34   0x19 |
| --- |

## [◆ ](#a9fbfd7aac05dfd05608264fa944c6287)RX\_PSEL\_PEnPFS\_TS35

| #define RX\_PSEL\_PEnPFS\_TS35   0x19 |
| --- |

## [◆ ](#a9a4f83a8487dfd0f32fb3180f71853b5)RX\_PSEL\_PEnPFS\_TXD12

| #define RX\_PSEL\_PEnPFS\_TXD12   0xC |
| --- |

## [◆ ](#a08d429e3e500db8b87f95a11cc61bf66)RX\_PSEL\_PEnPFS\_TXDX12

| #define RX\_PSEL\_PEnPFS\_TXDX12   0xC |
| --- |

## [◆ ](#a6ebe5c08ff146f995ac212e1ea716742)RX\_PSEL\_PHnPFS\_CACREF

| #define RX\_PSEL\_PHnPFS\_CACREF   0x7 |
| --- |

## [◆ ](#a0026241158d3b5ecf428c4836a3d875f)RX\_PSEL\_PHnPFS\_TMCI0

| #define RX\_PSEL\_PHnPFS\_TMCI0   0x05 |
| --- |

## [◆ ](#a84b2b05520efe0683f9db4e07155bfba)RX\_PSEL\_PHnPFS\_TMO0

| #define RX\_PSEL\_PHnPFS\_TMO0   0x05 |
| --- |

## [◆ ](#a6d8d96eaf1add151dd4629931fe61d1c)RX\_PSEL\_PHnPFS\_TMRI0

| #define RX\_PSEL\_PHnPFS\_TMRI0   0x05 |
| --- |

## [◆ ](#a2c067233e929b0cec2b3d2a09097deae)RX\_PSEL\_PHnPFS\_TS10

| #define RX\_PSEL\_PHnPFS\_TS10   0x19 |
| --- |

## [◆ ](#aa8cfeedd877a6952f8d97a341da8d50d)RX\_PSEL\_PHnPFS\_TS7

| #define RX\_PSEL\_PHnPFS\_TS7   0x19 |
| --- |

## [◆ ](#aeaf0f72ae91e634a1683a06e08b1f6c7)RX\_PSEL\_PHnPFS\_TS8

| #define RX\_PSEL\_PHnPFS\_TS8   0x19 |
| --- |

## [◆ ](#a70dd840a2bba0791a151bc09c4be36f0)RX\_PSEL\_PHnPFS\_TS9

| #define RX\_PSEL\_PHnPFS\_TS9   0x19 |
| --- |

## [◆ ](#a089de182c44f003fe50d1d5be28fc69c)RX\_PSEL\_PJnPFS\_CTS6

| #define RX\_PSEL\_PJnPFS\_CTS6   0xB |
| --- |

## [◆ ](#ad8dfc05cfc1d8415d91b29ffe39c9b96)RX\_PSEL\_PJnPFS\_MTIOC3A

| #define RX\_PSEL\_PJnPFS\_MTIOC3A   0x01 |
| --- |

## [◆ ](#a580dc22127edf2f64729314f6dd7e910)RX\_PSEL\_PJnPFS\_MTIOC3C

| #define RX\_PSEL\_PJnPFS\_MTIOC3C   0x01 |
| --- |

## [◆ ](#a319993d775bb37dfcdfc545e358c6e6e)RX\_PSEL\_PJnPFS\_SS6

| #define RX\_PSEL\_PJnPFS\_SS6   0xB |
| --- |

## [◆ ](#a196e453a63cbbb6be004b3deb11aebc7)RX\_PSEL\_PJnPFS\_TTS6

| #define RX\_PSEL\_PJnPFS\_TTS6   0xB |
| --- |

## [◆ ](#aca4687fe2b8f282995d3949e5ea2da10)RX\_PSEL\_POE

| #define RX\_PSEL\_POE   0x7 |
| --- |

## [◆ ](#a58e6ba874d0ff5290cae17d3a6f11905)RX\_PSEL\_POS

| #define RX\_PSEL\_POS   9 |
| --- |

## [◆ ](#a0fd7aa971c81e73658b9ad99408ff61f)RX\_PSEL\_SCI\_1

| #define RX\_PSEL\_SCI\_1   0xA |
| --- |

## [◆ ](#a5275129885c5edd8dfff443723a59022)RX\_PSEL\_SCI\_6

| #define RX\_PSEL\_SCI\_6   0xB |
| --- |

## [◆ ](#ad8c118ed209b1757032ab96daa7381e9)RX\_PSEL\_TMR

| #define RX\_PSEL\_TMR   0x5 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rx.h](pinctrl-rx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
