---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/espi_8h.html
original_path: doxygen/html/espi_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi.h File Reference

Public APIs for eSPI driver.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <zephyr/syscalls/espi.h>`

[Go to the source code of this file.](espi_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [espi\_evt\_data\_kbc](structespi__evt__data__kbc.md) |
|  | Bit field definition of evt\_data in struct [espi\_event](structespi__event.md "eSPI event") for KBC. [More...](structespi__evt__data__kbc.md#details) |
| struct | [espi\_evt\_data\_acpi](structespi__evt__data__acpi.md) |
|  | Bit field definition of evt\_data in struct [espi\_event](structespi__event.md "eSPI event") for ACPI. [More...](structespi__evt__data__acpi.md#details) |
| struct | [espi\_event](structespi__event.md) |
|  | eSPI event [More...](structespi__event.md#details) |
| struct | [espi\_cfg](structespi__cfg.md) |
|  | eSPI bus configuration parameters [More...](structespi__cfg.md#details) |
| struct | [espi\_request\_packet](structespi__request__packet.md) |
|  | eSPI peripheral request packet format [More...](structespi__request__packet.md#details) |
| struct | [espi\_oob\_packet](structespi__oob__packet.md) |
|  | eSPI out-of-band transaction packet format [More...](structespi__oob__packet.md#details) |
| struct | [espi\_flash\_packet](structespi__flash__packet.md) |
|  | eSPI flash transactions packet format [More...](structespi__flash__packet.md#details) |

| Macros | |
| --- | --- |
| #define | [ESPI\_VWIRE\_SIGNAL\_OCB\_0](group__espi__interface.md#gae4855b6cf8049de8aa6d67763f1be8c3)   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_0](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2) |
| #define | [ESPI\_VWIRE\_SIGNAL\_OCB\_1](group__espi__interface.md#ga2ed490939e0249ff8196f77a74967727)   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_1](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de) |
| #define | [ESPI\_VWIRE\_SIGNAL\_OCB\_2](group__espi__interface.md#gaf35d03bc041dc6baefe35b74c163d73b)   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_2](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b) |
| #define | [ESPI\_VWIRE\_SIGNAL\_OCB\_3](group__espi__interface.md#gaeae1765d801cd298c27404c173a94707)   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_3](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a) |
| #define | [HOST\_KBC\_EVT\_IBF](group__espi__interface.md#gaa0807c908666cdcbb3a85f310bfbfccc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [HOST\_KBC\_EVT\_OBE](group__espi__interface.md#ga807bb75027f24e040cd28eba4bc1002c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [espi\_callback\_handler\_t](group__espi__interface.md#ga9d848c7e367cf277230f365f73c15c46)) (const struct [device](structdevice.md) \*dev, struct espi\_callback \*cb, struct [espi\_event](structespi__event.md) espi\_evt) |
|  | Define the application callback handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [espi\_io\_mode](group__espi__interface.md#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0) { [ESPI\_IO\_MODE\_SINGLE\_LINE](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a9f47188ebd9bb4cb6e426d0bc0b6595c) = BIT(0) , [ESPI\_IO\_MODE\_DUAL\_LINES](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0af766582d28d16af7c5aff6372e4ee243) = BIT(1) , [ESPI\_IO\_MODE\_QUAD\_LINES](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a87e70bb0f5c4f6a3a21ca1bcfa4540fc) = BIT(2) } |
|  | eSPI I/O mode capabilities [More...](group__espi__interface.md#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0) |
| enum | [espi\_channel](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755) { [ESPI\_CHANNEL\_PERIPHERAL](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a32f636bbad2618a6b1554656d3b53206) = BIT(0) , [ESPI\_CHANNEL\_VWIRE](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755ac2e84a127870ff50359cf96528c9a7c6) = BIT(1) , [ESPI\_CHANNEL\_OOB](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a0ccb80544cbda501cc90ea0c3b868e54) = BIT(2) , [ESPI\_CHANNEL\_FLASH](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a5616bf2bf49a8c457fcc2f27d9fe0518) = BIT(3) } |
|  | eSPI channel. [More...](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755) |
| enum | [espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128) {     [ESPI\_BUS\_RESET](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128ae6d4d43eded0d8a368c90ea653a60956) = BIT(0) , [ESPI\_BUS\_EVENT\_CHANNEL\_READY](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a996aee0a8f8ba0cead11cea0d39d2973) = BIT(1) , [ESPI\_BUS\_EVENT\_VWIRE\_RECEIVED](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128aa09f7dcd4b2d3addfaddbad5b8f2e5a2) = BIT(2) , [ESPI\_BUS\_EVENT\_OOB\_RECEIVED](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a3b5e529d1d0ba11c59172ab01c30e203) = BIT(3) ,     [ESPI\_BUS\_PERIPHERAL\_NOTIFICATION](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a9ac837699f302bd10332814c7014adea) = BIT(4) , [ESPI\_BUS\_TAF\_NOTIFICATION](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a9f2a9cfda3b803687a0992a9d41f0014) = BIT(5)   } |
|  | eSPI bus event. [More...](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128) |
| enum | [espi\_pc\_event](group__espi__interface.md#gac55098842dd9d181144ac4b4122a610e) { [ESPI\_PC\_EVT\_BUS\_CHANNEL\_READY](group__espi__interface.md#ggac55098842dd9d181144ac4b4122a610ea68ecb52b04ffddcc93fbcc77d3643687) = BIT(0) , [ESPI\_PC\_EVT\_BUS\_MASTER\_ENABLE](group__espi__interface.md#ggac55098842dd9d181144ac4b4122a610ea0e245cbeef479218d4e6c9bec57e40d1) = BIT(1) } |
|  | eSPI peripheral channel events. [More...](group__espi__interface.md#gac55098842dd9d181144ac4b4122a610e) |
| enum | [espi\_virtual\_peripheral](group__espi__interface.md#ga2629a5518a94f031419eeccd05f07373) {     [ESPI\_PERIPHERAL\_UART](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373a24478711945fd5258d8ca86bbb79b867) , [ESPI\_PERIPHERAL\_8042\_KBC](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373aaea75bb5ab8a5ff31dd6b8787f44df30) , [ESPI\_PERIPHERAL\_HOST\_IO](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373a8948a6f18bfbe87859a529d5f6e669b8) , [ESPI\_PERIPHERAL\_DEBUG\_PORT80](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373af51b7171cf6085fa7946333ff32fe2f0) ,     [ESPI\_PERIPHERAL\_HOST\_IO\_PVT](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373aa217b4786d7b8bacbaa4ec740550e71e)   } |
|  | eSPI peripheral notification type. [More...](group__espi__interface.md#ga2629a5518a94f031419eeccd05f07373) |
| enum | [espi\_cycle\_type](group__espi__interface.md#ga3e52615f244d7fa8ccda495ab8ec8a5b) {     [ESPI\_CYCLE\_MEMORY\_READ32](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba5b480e093a58849d4181bba22d5868a5) , [ESPI\_CYCLE\_MEMORY\_READ64](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5bac8ec7673b4466b278dfb5e468f7a4d79) , [ESPI\_CYCLE\_MEMORY\_WRITE32](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba2e5a736cf8a63491ee13d51ae4f8f073) , [ESPI\_CYCLE\_MEMORY\_WRITE64](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba54c11e63fcfe3f859af57e65af3f31f7) ,     [ESPI\_CYCLE\_MESSAGE\_NODATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba5f2ae0575ca4e9b61c0acd7d4f08ee82) , [ESPI\_CYCLE\_MESSAGE\_DATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba380e3d4e6b5579c8bb94e792fcb7d71f) , [ESPI\_CYCLE\_OK\_COMPLETION\_NODATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba0335f2d34fab46960939e2d2c1c12e3f) , [ESPI\_CYCLE\_OKCOMPLETION\_DATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5baf3dbc2bcc0ed883bc4d4160c21e6934f) ,     [ESPI\_CYCLE\_NOK\_COMPLETION\_NODATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba0edb306e5fabcbf8b009375cde6a8a2b)   } |
|  | eSPI cycle types supported over eSPI peripheral channel [More...](group__espi__interface.md#ga3e52615f244d7fa8ccda495ab8ec8a5b) |
| enum | [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) {     [ESPI\_VWIRE\_SIGNAL\_SLP\_S3](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab880a7156e489d5f7b8f78550e72b166) , [ESPI\_VWIRE\_SIGNAL\_SLP\_S4](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a4ef1fe12bd09be0875864d6c32164f73) , [ESPI\_VWIRE\_SIGNAL\_SLP\_S5](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ac4b4e30c097a4ef49f21549a799e1e13) , [ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a2f3f97b51b750050cd98e887e39431d1) ,     [ESPI\_VWIRE\_SIGNAL\_PLTRST](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a0bafcd0bb7f592f0e308dcfce39bcd08) , [ESPI\_VWIRE\_SIGNAL\_SUS\_STAT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a0e13f250ba0c5a37451c7f3b0e98e663) , [ESPI\_VWIRE\_SIGNAL\_NMIOUT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ad14b4b7a25141346bfefc507c588a238) , [ESPI\_VWIRE\_SIGNAL\_SMIOUT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a1d54a71c6d2e52cb66cfaa0b55b61152) ,     [ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35af44250de6f60eabf9b0d85b8860ac56e) , [ESPI\_VWIRE\_SIGNAL\_SLP\_A](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa4c8c69475b48d88302066823d2f3592) , [ESPI\_VWIRE\_SIGNAL\_SUS\_PWRDN\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab4f0bedd5717660cc8cac2d85c6c3d18) , [ESPI\_VWIRE\_SIGNAL\_SUS\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a9e32eee077aaa1668c356fe1d4ab1cc5) ,     [ESPI\_VWIRE\_SIGNAL\_SLP\_WLAN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a3d95f095ae41bba9ef916fc68ddd4779) , [ESPI\_VWIRE\_SIGNAL\_SLP\_LAN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aba8b891a643ca567966d091963be4615) , [ESPI\_VWIRE\_SIGNAL\_HOST\_C10](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab9deb0dd6d4e878eff6413ddc34bb36c) , [ESPI\_VWIRE\_SIGNAL\_DNX\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a923f3e602d9f8ac821ece2a625183146) ,     [ESPI\_VWIRE\_SIGNAL\_PME](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa87af5b5de184238e5f371851aaee692) , [ESPI\_VWIRE\_SIGNAL\_WAKE](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a736724f8229aebc356c2720a34a0143f) , [ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a8e15df6f8159b4c275dc4b20aaec352e) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_BOOT\_STS](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a231caf3d46cde2eaf7305bf3f694838c) ,     [ESPI\_VWIRE\_SIGNAL\_ERR\_NON\_FATAL](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a504ae332b89262f70a0bf1a9c8b6f527) , [ESPI\_VWIRE\_SIGNAL\_ERR\_FATAL](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aae0a3fd882c5765db33a4e7bd05e1ab1) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_BOOT\_DONE](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ad99ea62f91b40c8926cda944928e3631) , [ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a89420628ae26df4c45ef7fba04a3a85e) ,     [ESPI\_VWIRE\_SIGNAL\_RST\_CPU\_INIT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a19c40230e0bb4cee7b6ee42580c28a8d) , [ESPI\_VWIRE\_SIGNAL\_SMI](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a2d9b2eef499d1bfd13bec1d2caa0e2f3) , [ESPI\_VWIRE\_SIGNAL\_SCI](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35afa1f99a7e45b306c6736888e280f527c) , [ESPI\_VWIRE\_SIGNAL\_DNX\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a58280c68c980476aabefa16e0509dd1c) ,     [ESPI\_VWIRE\_SIGNAL\_SUS\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35abe28432b566619d8c6cce5e5034e5333) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_0](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_1](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_2](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b) ,     [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_3](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_4](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ad9b6bb998bea0bc983ab8a6c452d52a1) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_5](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35af10e9e5b320301b2fe923e6793adbeaf) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_6](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aee0a1576a6e07708e1cde59597b49662) ,     [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_7](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ae34962d6db346e02f175894843ce0e1e) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_8](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a8a7b50f0aa53a2c80bae7747d628d219) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_9](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a9410475f349afcf44ddb25ebbd454978) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_10](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a637b5c00aaca05e5daa6969a680cbbb1) ,     [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_11](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a07a6b00a4b1cfad2137dc43d7232fc9f) , [ESPI\_VWIRE\_SIGNAL\_COUNT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ad3319083735295454bc59b742988cfca)   } |
|  | eSPI system platform signals that can be send or receive through virtual wire channel [More...](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) |
| enum | [lpc\_peripheral\_opcode](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e) {     [E8042\_OBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eac172afb38cb38970ef6242a4f45132f9) = 0x50 , [E8042\_IBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eab70684413d736c8583f3dc53f14b7c7a) , [E8042\_WRITE\_KB\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eaa9135a5ea9a5ebd9d25660c37983c5d6) , [E8042\_WRITE\_MB\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eaaef0649f867424ec0c7889acb7354911) ,     [E8042\_RESUME\_IRQ](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eac5b666b3319dc2ef0fc571684c2ea198) , [E8042\_PAUSE\_IRQ](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea5e7205b5f1371f1a0f2eaed299389475) , [E8042\_CLEAR\_OBF](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eacdeb74a9534310f5dab3f1bfb5def534) , [E8042\_READ\_KB\_STS](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea8c62cd1266681c88aa0cb1af65ab551b) ,     [E8042\_SET\_FLAG](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea83266d88740588d45be6667a4034c447) , [E8042\_CLEAR\_FLAG](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea5c592b1cad381b296cde832c67264cd1) , [EACPI\_OBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea3cce8bd0205691ecda53fc469606929d) = EACPI\_START\_OPCODE , [EACPI\_IBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea09f241a3f6ffcb5b7839c81c7fc4ea6e) ,     [EACPI\_WRITE\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea689643f6feb724a303d3b790ff2899f7) , [EACPI\_READ\_STS](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea02bf8538a66f633e3d2ec094f57c6173) , [EACPI\_WRITE\_STS](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea02c7b1c69d803a5c45304260786afb6f)   } |

| Functions | |
| --- | --- |
| int | [espi\_config](group__espi__interface.md#ga7227c53d384eb0dc666361261f069f68) (const struct [device](structdevice.md) \*dev, struct [espi\_cfg](structespi__cfg.md) \*cfg) |
|  | Configure operation of a eSPI controller. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [espi\_get\_channel\_status](group__espi__interface.md#ga869551e20fc2c3be4311c21c3c53999d) (const struct [device](structdevice.md) \*dev, enum [espi\_channel](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755) ch) |
|  | Query to see if it a channel is ready. |
| int | [espi\_read\_request](group__espi__interface.md#ga112f7554ba614c8e5f239b1319b4a763) (const struct [device](structdevice.md) \*dev, struct [espi\_request\_packet](structespi__request__packet.md) \*req) |
|  | Sends memory, I/O or message read request over eSPI. |
| int | [espi\_write\_request](group__espi__interface.md#ga143ed88b1f220f9582c809165fd983fd) (const struct [device](structdevice.md) \*dev, struct [espi\_request\_packet](structespi__request__packet.md) \*req) |
|  | Sends memory, I/O or message write request over eSPI. |
| int | [espi\_read\_lpc\_request](group__espi__interface.md#gaeaae20afa90d9d825d80997369f31465) (const struct [device](structdevice.md) \*dev, enum [lpc\_peripheral\_opcode](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e) op, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data) |
|  | Reads SOC data from a LPC peripheral with information updated over eSPI. |
| int | [espi\_write\_lpc\_request](group__espi__interface.md#ga880b6b04824f9f0deea10e8018573b88) (const struct [device](structdevice.md) \*dev, enum [lpc\_peripheral\_opcode](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e) op, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data) |
|  | Writes data to a LPC peripheral which generates an eSPI transaction. |
| int | [espi\_send\_vwire](group__espi__interface.md#gacab2b3bff7d940e71ee1c2a9fdedf782) (const struct [device](structdevice.md) \*dev, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) signal, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Sends system/platform signal as a virtual wire packet. |
| int | [espi\_receive\_vwire](group__espi__interface.md#gaa8bb48b5592c4b49d27c9b8a42432410) (const struct [device](structdevice.md) \*dev, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) signal, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level) |
|  | Retrieves level status for a signal encapsulated in a virtual wire. |
| int | [espi\_send\_oob](group__espi__interface.md#ga2557cfc7a38f669d14e9826e3fb0fdee) (const struct [device](structdevice.md) \*dev, struct [espi\_oob\_packet](structespi__oob__packet.md) \*pckt) |
|  | Sends SMBus transaction (out-of-band) packet over eSPI bus. |
| int | [espi\_receive\_oob](group__espi__interface.md#ga4b8f4fbf66a2b2ae394e00b16500f70d) (const struct [device](structdevice.md) \*dev, struct [espi\_oob\_packet](structespi__oob__packet.md) \*pckt) |
|  | Receives SMBus transaction (out-of-band) packet from eSPI bus. |
| int | [espi\_read\_flash](group__espi__interface.md#ga0a97d11167367342283bfe6b6d66726e) (const struct [device](structdevice.md) \*dev, struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt) |
|  | Sends a read request packet for shared flash. |
| int | [espi\_write\_flash](group__espi__interface.md#gab02d46fd690e33875cc1b2433c976891) (const struct [device](structdevice.md) \*dev, struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt) |
|  | Sends a write request packet for shared flash. |
| int | [espi\_flash\_erase](group__espi__interface.md#gab42be7c76c4523cea96365aa77fd18be) (const struct [device](structdevice.md) \*dev, struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt) |
|  | Sends a write request packet for shared flash. |
| static void | [espi\_init\_callback](group__espi__interface.md#ga8d88e4e3893d610713195e5352ec2565) (struct espi\_callback \*callback, [espi\_callback\_handler\_t](group__espi__interface.md#ga9d848c7e367cf277230f365f73c15c46) handler, enum [espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128) evt\_type) |
|  | Callback model. |
| static int | [espi\_add\_callback](group__espi__interface.md#gabf5f0ea01ec8ed5345b2e119181c2313) (const struct [device](structdevice.md) \*dev, struct espi\_callback \*callback) |
|  | Add an application callback. |
| static int | [espi\_remove\_callback](group__espi__interface.md#ga7f04f98ea6a4671b821cf6ddf6bbf2a6) (const struct [device](structdevice.md) \*dev, struct espi\_callback \*callback) |
|  | Remove an application callback. |

## Detailed Description

Public APIs for eSPI driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [espi.h](espi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
