---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fuel__gauge_8h.html
original_path: doxygen/html/fuel__gauge_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fuel\_gauge.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/fuel_gauge.h>`

[Go to the source code of this file.](fuel__gauge_8h_source.md)

| Data Structures | |
| --- | --- |
| union | [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) |
|  | Property field to value/type union. [More...](unionfuel__gauge__prop__val.md#details) |
| struct | [sbs\_gauge\_manufacturer\_name](structsbs__gauge__manufacturer__name.md) |
| struct | [sbs\_gauge\_device\_name](structsbs__gauge__device__name.md) |
| struct | [sbs\_gauge\_device\_chemistry](structsbs__gauge__device__chemistry.md) |
| struct | [fuel\_gauge\_driver\_api](structfuel__gauge__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [SBS\_GAUGE\_MANUFACTURER\_NAME\_MAX\_SIZE](group__fuel__gauge__interface.md#ga824e00f1d607cdfe2598625f154636f1)   20 |
|  | Data structures for reading SBS buffer properties. |
| #define | [SBS\_GAUGE\_DEVICE\_NAME\_MAX\_SIZE](group__fuel__gauge__interface.md#ga41b8379542b9cbd0b3ee9e1bbe4bc599)   20 |
| #define | [SBS\_GAUGE\_DEVICE\_CHEMISTRY\_MAX\_SIZE](group__fuel__gauge__interface.md#gafe9bdc00d856d4cc787265edb7eb0ed2)   4 |

| Typedefs | |
| --- | --- |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) |
| typedef int(\* | [fuel\_gauge\_get\_property\_t](group__fuel__gauge__interface.md#gaed940ae925236ad2f25cf05d78304568)) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*val) |
|  | Callback API for getting a fuel\_gauge property. |
| typedef int(\* | [fuel\_gauge\_set\_property\_t](group__fuel__gauge__interface.md#gae87a20a20f4f1fbb74d72afb2bcee4c9)) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) val) |
|  | Callback API for setting a fuel\_gauge property. |
| typedef int(\* | [fuel\_gauge\_get\_buffer\_property\_t](group__fuel__gauge__interface.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop\_type, void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dst\_len) |
|  | Callback API for getting a fuel\_gauge buffer property. |
| typedef int(\* | [fuel\_gauge\_battery\_cutoff\_t](group__fuel__gauge__interface.md#ga698c8f84da7d1cbe7db1fc024e2388b7)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API for doing a battery cutoff. |

| Enumerations | |
| --- | --- |
| enum | [fuel\_gauge\_prop\_type](group__fuel__gauge__interface.md#gae49908857800bdd010d59895cfad9171) {     [FUEL\_GAUGE\_AVG\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396) = 0 , [FUEL\_GAUGE\_BATTERY\_CUTOFF](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad431ab05b79f942dd500ce84980cf81f) , [FUEL\_GAUGE\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354) , [FUEL\_GAUGE\_CHARGE\_CUTOFF](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f) ,     [FUEL\_GAUGE\_CYCLE\_COUNT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984) , [FUEL\_GAUGE\_CONNECT\_STATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d) , [FUEL\_GAUGE\_FLAGS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c) , [FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9) ,     [FUEL\_GAUGE\_PRESENT\_STATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b) , [FUEL\_GAUGE\_REMAINING\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4) , [FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd) , [FUEL\_GAUGE\_RUNTIME\_TO\_FULL](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399) ,     [FUEL\_GAUGE\_SBS\_MFR\_ACCESS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd) , [FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee) , [FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b) , [FUEL\_GAUGE\_TEMPERATURE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009) ,     [FUEL\_GAUGE\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71) , [FUEL\_GAUGE\_SBS\_MODE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae) , [FUEL\_GAUGE\_CHARGE\_CURRENT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e) , [FUEL\_GAUGE\_CHARGE\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920) ,     [FUEL\_GAUGE\_STATUS](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40) , [FUEL\_GAUGE\_DESIGN\_CAPACITY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67) , [FUEL\_GAUGE\_DESIGN\_VOLTAGE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf) , [FUEL\_GAUGE\_SBS\_ATRATE](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58) ,     [FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70) , [FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0) , [FUEL\_GAUGE\_SBS\_ATRATE\_OK](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec) , [FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2) ,     [FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a) , [FUEL\_GAUGE\_MANUFACTURER\_NAME](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8) , [FUEL\_GAUGE\_DEVICE\_NAME](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10) , [FUEL\_GAUGE\_DEVICE\_CHEMISTRY](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9) ,     [FUEL\_GAUGE\_COMMON\_COUNT](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815) , [FUEL\_GAUGE\_CUSTOM\_BEGIN](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584) , [FUEL\_GAUGE\_PROP\_MAX](group__fuel__gauge__interface.md#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81) = UINT16\_MAX   } |

| Functions | |
| --- | --- |
| int | [fuel\_gauge\_get\_prop](group__fuel__gauge__interface.md#gab84999beab9a43241992945a3b2d37e1) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*val) |
|  | Fetch a battery fuel-gauge property. |
| int | [fuel\_gauge\_get\_props](group__fuel__gauge__interface.md#gac721c19bc2c9714c11ede5e6d86fd0b0) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) \*props, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Fetch multiple battery fuel-gauge properties. |
| int | [fuel\_gauge\_set\_prop](group__fuel__gauge__interface.md#ga936be681a82f173b664ae2187bc5a73d) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) val) |
|  | Set a battery fuel-gauge property. |
| int | [fuel\_gauge\_set\_props](group__fuel__gauge__interface.md#ga55bb2be9c9eae7c3a8d01df051178d01) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) \*props, union [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md) \*vals, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Set a battery fuel-gauge property. |
| int | [fuel\_gauge\_get\_buffer\_prop](group__fuel__gauge__interface.md#ga7e6cb77d2d4dd7a0feb25c92d031614c) (const struct [device](structdevice.md) \*dev, [fuel\_gauge\_prop\_t](group__fuel__gauge__interface.md#ga633eb1cb8dd64123252634b833b2f806) prop\_type, void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dst\_len) |
|  | Fetch a battery fuel-gauge buffer property. |
| int | [fuel\_gauge\_battery\_cutoff](group__fuel__gauge__interface.md#ga763a40688dc8fc6a0ba85fdc79178ebc) (const struct [device](structdevice.md) \*dev) |
|  | Have fuel gauge cutoff its associated battery. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [fuel\_gauge.h](fuel__gauge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
