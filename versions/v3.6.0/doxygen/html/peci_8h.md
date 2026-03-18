---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/peci_8h.html
original_path: doxygen/html/peci_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

peci.h File Reference

Public Platform Environment Control Interface driver APIs.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <syscalls/peci.h>`

[Go to the source code of this file.](peci_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [peci\_buf](structpeci__buf.md) |
|  | PECI buffer structure. [More...](structpeci__buf.md#details) |
| struct | [peci\_msg](structpeci__msg.md) |
|  | PECI transaction packet format. [More...](structpeci__msg.md#details) |

| Macros | |
| --- | --- |
| PECI read/write supported responses. | |
| #define | [PECI\_CC\_RSP\_SUCCESS](group__peci__interface.md#gaaa72e987f7345168055de5dc4e206d05)   (0x40U) |
| #define | [PECI\_CC\_RSP\_TIMEOUT](group__peci__interface.md#ga797ae69ec374fb64bb89f944f6985c6d)   (0x80U) |
| #define | [PECI\_CC\_OUT\_OF\_RESOURCES\_TIMEOUT](group__peci__interface.md#gaac992f1ccc084c3ea5f517cd3fba8271)   (0x81U) |
| #define | [PECI\_CC\_RESOURCES\_LOWPWR\_TIMEOUT](group__peci__interface.md#gaae8cfb17318fa562c45c797c24e69abe)   (0x82U) |
| #define | [PECI\_CC\_ILLEGAL\_REQUEST](group__peci__interface.md#gac26eca50fb7dd2b899ae0e820bbb4412)   (0x90U) |
| Ping command format. | |
| #define | [PECI\_PING\_WR\_LEN](group__peci__interface.md#ga22a92f0547fd1fe30dd413b071f53d22)   (0U) |
| #define | [PECI\_PING\_RD\_LEN](group__peci__interface.md#ga28b67489837aa513c987a56cfd2a52ed)   (0U) |
| #define | [PECI\_PING\_LEN](group__peci__interface.md#ga260b7df883f39c44ac77c0504688fcd4)   (3U) |
| GetDIB command format. | |
| #define | [PECI\_GET\_DIB\_WR\_LEN](group__peci__interface.md#ga326203908d537fd303b865a32100d45b)   (1U) |
| #define | [PECI\_GET\_DIB\_RD\_LEN](group__peci__interface.md#gaa3da9245648157eed5d483dd934b3874)   (8U) |
| #define | [PECI\_GET\_DIB\_CMD\_LEN](group__peci__interface.md#gad7c7732a98738308f4f3f5f4e3cc29ee)   (4U) |
| #define | [PECI\_GET\_DIB\_DEVINFO](group__peci__interface.md#ga679c229499e6669bdf577dad45b51da2)   (0U) |
| #define | [PECI\_GET\_DIB\_REVNUM](group__peci__interface.md#ga83fab6ba4c3ee0df1997b322bc28d986)   (1U) |
| #define | [PECI\_GET\_DIB\_DOMAIN\_BIT\_MASK](group__peci__interface.md#ga4fad3e307b5eee6de75b2e9d5b7c5252)   (0x4U) |
| #define | [PECI\_GET\_DIB\_MAJOR\_REV\_MASK](group__peci__interface.md#ga56be056f7286d8633a9dcad3904aadc6)   0xF0 |
| #define | [PECI\_GET\_DIB\_MINOR\_REV\_MASK](group__peci__interface.md#gaaaf4e2450fe327826451899458011669)   0x0F |
| GetTemp command format. | |
| #define | [PECI\_GET\_TEMP\_WR\_LEN](group__peci__interface.md#ga782d004f484ba89a2a85552b1367f5e3)   (1U) |
| #define | [PECI\_GET\_TEMP\_RD\_LEN](group__peci__interface.md#ga8abc4778c30a938b891e45595e1a05bb)   (2U) |
| #define | [PECI\_GET\_TEMP\_CMD\_LEN](group__peci__interface.md#gac9eb9af198bcad988f756e5bbfa610e6)   (4U) |
| #define | [PECI\_GET\_TEMP\_LSB](group__peci__interface.md#gac57d46b51397b3f86ab1850e45a14d8d)   (0U) |
| #define | [PECI\_GET\_TEMP\_MSB](group__peci__interface.md#gab10cf44c7f53989d0d3eb7646c7a2ebf)   (1U) |
| #define | [PECI\_GET\_TEMP\_ERR\_MSB](group__peci__interface.md#ga0a748818ab3e256a372a1444fbbeb4d2)   (0x80U) |
| #define | [PECI\_GET\_TEMP\_ERR\_LSB\_GENERAL](group__peci__interface.md#ga5c8b7afaf9e84ffc289551bf65d27888)   (0x0U) |
| #define | [PECI\_GET\_TEMP\_ERR\_LSB\_RES](group__peci__interface.md#ga5fc4196ce832e80a9219ab66b6018b40)   (0x1U) |
| #define | [PECI\_GET\_TEMP\_ERR\_LSB\_TEMP\_LO](group__peci__interface.md#ga48cdea4c953b8f9f71fc4d38cc9e1b52)   (0x2U) |
| #define | [PECI\_GET\_TEMP\_ERR\_LSB\_TEMP\_HI](group__peci__interface.md#ga3d13f32e4aa52df7f5a14bfbe7bef310)   (0x3U) |
| RdPkgConfig command format. | |
| #define | [PECI\_RD\_PKG\_WR\_LEN](group__peci__interface.md#ga14c5301c855e0fd6d3e6ce2671ca2630)   (5U) |
| #define | [PECI\_RD\_PKG\_LEN\_BYTE](group__peci__interface.md#gae73ca3befdbc95c6ed95fa64deca40f2)   (2U) |
| #define | [PECI\_RD\_PKG\_LEN\_WORD](group__peci__interface.md#ga8b37ea69eb7194fb68162fabcf47abd4)   (3U) |
| #define | [PECI\_RD\_PKG\_LEN\_DWORD](group__peci__interface.md#ga7ffc8df46be38442238e3a1913d80a43)   (5U) |
| #define | [PECI\_RD\_PKG\_CMD\_LEN](group__peci__interface.md#ga617975c279fa6c25d00c3611388c7c87)   (8U) |
| WrPkgConfig command format. | |
| #define | [PECI\_WR\_PKG\_RD\_LEN](group__peci__interface.md#ga3a48be4c578e26e0425281d8dc45b675)   (1U) |
| #define | [PECI\_WR\_PKG\_LEN\_BYTE](group__peci__interface.md#ga25a60618673b02a987049d7bf9e0d177)   (7U) |
| #define | [PECI\_WR\_PKG\_LEN\_WORD](group__peci__interface.md#ga3b3bb82e32dfb47e642485cd90046805)   (8U) |
| #define | [PECI\_WR\_PKG\_LEN\_DWORD](group__peci__interface.md#gae47cf47f1bacc97b29da8a77754b1856)   (10U) |
| #define | [PECI\_WR\_PKG\_CMD\_LEN](group__peci__interface.md#ga44721cfff04cf37a9dad8e6290efadd8)   (9U) |
| RdIAMSR command format. | |
| #define | [PECI\_RD\_IAMSR\_WR\_LEN](group__peci__interface.md#ga32a758a9489a4dc40a6f451a33b3873e)   (5U) |
| #define | [PECI\_RD\_IAMSR\_LEN\_BYTE](group__peci__interface.md#gac1a68fb49b86937dbbcea02a6e38678e)   (2U) |
| #define | [PECI\_RD\_IAMSR\_LEN\_WORD](group__peci__interface.md#gad95974df60609e97652d090aaeb15dbd)   (3U) |
| #define | [PECI\_RD\_IAMSR\_LEN\_DWORD](group__peci__interface.md#gaee3af8380685c9162102439790c43bca)   (5U) |
| #define | [PECI\_RD\_IAMSR\_LEN\_QWORD](group__peci__interface.md#ga6075e0aabf13898467ce99bd32234acd)   (9U) |
| #define | [PECI\_RD\_IAMSR\_CMD\_LEN](group__peci__interface.md#gaac4377037fe078d06ba711ffd92ece3a)   (8U) |
| WrIAMSR command format. | |
| #define | [PECI\_WR\_IAMSR\_RD\_LEN](group__peci__interface.md#ga84bac67b2d70a27b029ef58a37b18656)   (1U) |
| #define | [PECI\_WR\_IAMSR\_LEN\_BYTE](group__peci__interface.md#gacff3b7ae6bc7b054a9b14474372a4932)   (7U) |
| #define | [PECI\_WR\_IAMSR\_LEN\_WORD](group__peci__interface.md#ga2a9278a92885a8dc23254ced8e717dee)   (8U) |
| #define | [PECI\_WR\_IAMSR\_LEN\_DWORD](group__peci__interface.md#ga0fdcb8d4cddc7f8bf778253f17b8d622)   (10U) |
| #define | [PECI\_WR\_IAMSR\_LEN\_QWORD](group__peci__interface.md#gaa53d79877fa3a8df479edae01fdb02cc)   (14U) |
| #define | [PECI\_WR\_IAMSR\_CMD\_LEN](group__peci__interface.md#gaf6743aec8256e30c862470d20401c80b)   (9U) |
| RdPCIConfig command format. | |
| #define | [PECI\_RD\_PCICFG\_WR\_LEN](group__peci__interface.md#ga28d95625dca7dcd18009b8a9d1af1b40)   (6U) |
| #define | [PECI\_RD\_PCICFG\_LEN\_BYTE](group__peci__interface.md#gae64fc86f4a5dc7ffa4317312eba25ace)   (2U) |
| #define | [PECI\_RD\_PCICFG\_LEN\_WORD](group__peci__interface.md#gaac909c672633eb8aea767eca556e9684)   (3U) |
| #define | [PECI\_RD\_PCICFG\_LEN\_DWORD](group__peci__interface.md#gaee3c84370914cb27509ea9a91ca5f6b9)   (5U) |
| #define | [PECI\_RD\_PCICFG\_CMD\_LEN](group__peci__interface.md#ga8bec0be2c5762df6a451b322f4652f8a)   (9U) |
| WrPCIConfig command format. | |
| #define | [PECI\_WR\_PCICFG\_RD\_LEN](group__peci__interface.md#gac81baf9413648e72cd12c5a0a4afafb1)   (1U) |
| #define | [PECI\_WR\_PCICFG\_LEN\_BYTE](group__peci__interface.md#ga74d1759fc8b25a191af7a50f929b3ccc)   (8U) |
| #define | [PECI\_WR\_PCICFG\_LEN\_WORD](group__peci__interface.md#ga94107bc6d6384cac4a93f2dc31d4ff0a)   (9U) |
| #define | [PECI\_WR\_PCICFG\_LEN\_DWORD](group__peci__interface.md#gab2ec9a3f5b1cd095c510b8526ecfb788)   (11U) |
| #define | [PECI\_WR\_PCICFG\_CMD\_LEN](group__peci__interface.md#ga431b61c8b4a2e3d12aa681abec3433fa)   (10U) |
| RdPCIConfigLocal command format. | |
| #define | [PECI\_RD\_PCICFGL\_WR\_LEN](group__peci__interface.md#ga60ba164ab5036ce14dc2f18daf0c264e)   (5U) |
| #define | [PECI\_RD\_PCICFGL\_RD\_LEN\_BYTE](group__peci__interface.md#ga712626f9f7ec395fa0781b3a2f7b5cfb)   (2U) |
| #define | [PECI\_RD\_PCICFGL\_RD\_LEN\_WORD](group__peci__interface.md#ga27dfea893aa66268fcb938152cff4974)   (3U) |
| #define | [PECI\_RD\_PCICFGL\_RD\_LEN\_DWORD](group__peci__interface.md#ga3df08231dc4cec3f8c8706c7a63421d1)   (5U) |
| #define | [PECI\_RD\_PCICFGL\_CMD\_LEN](group__peci__interface.md#gaf9fd6d6eefe3133aec4e6ee2d682a238)   (8U) |
| WrPCIConfigLocal command format. | |
| #define | [PECI\_WR\_PCICFGL\_RD\_LEN](group__peci__interface.md#ga8063cf05f9f26b28219e5fece331717d)   (1U) |
| #define | [PECI\_WR\_PCICFGL\_WR\_LEN\_BYTE](group__peci__interface.md#gac3cd61027ba11b6a0304c51616e17be9)   (7U) |
| #define | [PECI\_WR\_PCICFGL\_WR\_LEN\_WORD](group__peci__interface.md#ga240fcf510dc8f3aae66ca45750b6939f)   (8U) |
| #define | [PECI\_WR\_PCICFGL\_WR\_LEN\_DWORD](group__peci__interface.md#gad33f4be78198ba75fdcde410a5660b39)   (10U) |
| #define | [PECI\_WR\_PCICFGL\_CMD\_LEN](group__peci__interface.md#gaa9fcd8acb3578585afbbda38b76e40c3)   (9U) |

| Enumerations | |
| --- | --- |
| enum | [peci\_error\_code](group__peci__interface.md#ga76ad37d4317b48311cf23cf516549544) { [PECI\_GENERAL\_SENSOR\_ERROR](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544ae443a31c6771f672eecbdcbc1839215f) = 0x8000 , [PECI\_UNDERFLOW\_SENSOR\_ERROR](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544a3444a28dba8e6a5d0eec8a3128e73c41) = 0x8002 , [PECI\_OVERFLOW\_SENSOR\_ERROR](group__peci__interface.md#gga76ad37d4317b48311cf23cf516549544afd2181728ca4397f39c9d632df015ed2) = 0x8003 } |
|  | PECI error codes. [More...](group__peci__interface.md#ga76ad37d4317b48311cf23cf516549544) |
| enum | [peci\_command\_code](group__peci__interface.md#gacd243f64973f7bdcc8c999dc14ed2bd6) {     [PECI\_CMD\_PING](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6aeb58e4fba76910717759cb6e2ea7189d) = 0x00 , [PECI\_CMD\_GET\_TEMP0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6afbb78950e41573a7d0e1e5c4d63e96bf) = 0x01 , [PECI\_CMD\_GET\_TEMP1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a13c808d7543b5cd45afbefc8eb21611c) = 0x02 , [PECI\_CMD\_RD\_PCI\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6aa38f576d83e4fc3555cd7bffb5c5ce6d) = 0x61 ,     [PECI\_CMD\_RD\_PCI\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a709af27dd39811f4ee57ee6b9f4675fa) = 0x62 , [PECI\_CMD\_WR\_PCI\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6acb02d1f73e2b9701a108f595763c84bc) = 0x65 , [PECI\_CMD\_WR\_PCI\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a572da95ca81979ad1444a4bd302c7f12) = 0x66 , [PECI\_CMD\_RD\_PKG\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a4323adb5af1251cb30f3cdffb485b523) = 0xA1 ,     [PECI\_CMD\_RD\_PKG\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a21c9a89c7a6411fc16c0a651d0239fed) = 0xA , [PECI\_CMD\_WR\_PKG\_CFG0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ac43d5530697b1e3ca0d6dd2b210cbc55) = 0xA5 , [PECI\_CMD\_WR\_PKG\_CFG1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a42fe60d1ad58a3182c42217ef3b87a95) = 0xA6 , [PECI\_CMD\_RD\_IAMSR0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ae944a14033aecc7323578cac792b9e10) = 0xB1 ,     [PECI\_CMD\_RD\_IAMSR1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a6769388430077f82dca456470a76ae53) = 0xB2 , [PECI\_CMD\_WR\_IAMSR0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a31e61a2e884286a53663dfcd932d28a2) = 0xB5 , [PECI\_CMD\_WR\_IAMSR1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6ab1ba81b33438013543b7b61cc34a04b3) = 0xB6 , [PECI\_CMD\_RD\_PCI\_CFG\_LOCAL0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a16549485b6fcd531afcda48c323f30a5) = 0xE1 ,     [PECI\_CMD\_RD\_PCI\_CFG\_LOCAL1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6acd12ed51a5dd15b29d82913149775f2c) = 0xE2 , [PECI\_CMD\_WR\_PCI\_CFG\_LOCAL0](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6af737a18cbf850948594519eacfe33158) = 0xE5 , [PECI\_CMD\_WR\_PCI\_CFG\_LOCAL1](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a7ddc4229ec37021b78ea50d0cde69cdd) = 0xE6 , [PECI\_CMD\_GET\_DIB](group__peci__interface.md#ggacd243f64973f7bdcc8c999dc14ed2bd6a000d0e023fd6382fb1a503a3317495d8) = 0xF7   } |
|  | PECI commands. [More...](group__peci__interface.md#gacd243f64973f7bdcc8c999dc14ed2bd6) |

| Functions | |
| --- | --- |
| int | [peci\_config](group__peci__interface.md#gaa1fee6839b68eed73f0a8d93b3a3ec82) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate) |
|  | Configures the PECI interface. |
| int | [peci\_enable](group__peci__interface.md#gaa42e2e015a2c778a9eaf2dc1b697630f) (const struct [device](structdevice.md) \*dev) |
|  | Enable PECI interface. |
| int | [peci\_disable](group__peci__interface.md#gaf197262cd58db5eb7691d1ce816057de) (const struct [device](structdevice.md) \*dev) |
|  | Disable PECI interface. |
| int | [peci\_transfer](group__peci__interface.md#gacf15bdae6483ad3e9498ed984a959687) (const struct [device](structdevice.md) \*dev, struct [peci\_msg](structpeci__msg.md) \*msg) |
|  | Performs a PECI transaction. |

## Detailed Description

Public Platform Environment Control Interface driver APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [peci.h](peci_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
