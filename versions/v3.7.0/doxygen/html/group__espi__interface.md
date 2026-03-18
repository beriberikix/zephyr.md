---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__espi__interface.html
original_path: doxygen/html/group__espi__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ESPI Driver APIs

[Device Driver APIs](group__io__interfaces.md)

eSPI Driver APIs
[More...](#details)

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
| struct | [espi\_saf\_cfg](structespi__saf__cfg.md) |
|  | eSPI SAF configuration parameters [More...](structespi__saf__cfg.md#details) |
| struct | [espi\_saf\_packet](structespi__saf__packet.md) |
|  | eSPI SAF transaction packet format [More...](structespi__saf__packet.md#details) |

| Macros | |
| --- | --- |
| #define | [ESPI\_VWIRE\_SIGNAL\_OCB\_0](#gae4855b6cf8049de8aa6d67763f1be8c3)   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_0](#ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2) |
| #define | [ESPI\_VWIRE\_SIGNAL\_OCB\_1](#ga2ed490939e0249ff8196f77a74967727)   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_1](#ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de) |
| #define | [ESPI\_VWIRE\_SIGNAL\_OCB\_2](#gaf35d03bc041dc6baefe35b74c163d73b)   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_2](#ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b) |
| #define | [ESPI\_VWIRE\_SIGNAL\_OCB\_3](#gaeae1765d801cd298c27404c173a94707)   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_3](#ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a) |
| #define | [HOST\_KBC\_EVT\_IBF](#gaa0807c908666cdcbb3a85f310bfbfccc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [HOST\_KBC\_EVT\_OBE](#ga807bb75027f24e040cd28eba4bc1002c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [espi\_callback\_handler\_t](#ga9d848c7e367cf277230f365f73c15c46)) (const struct [device](structdevice.md) \*dev, struct espi\_callback \*cb, struct [espi\_event](structespi__event.md) espi\_evt) |
|  | Define the application callback handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [espi\_io\_mode](#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0) { [ESPI\_IO\_MODE\_SINGLE\_LINE](#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a9f47188ebd9bb4cb6e426d0bc0b6595c) = BIT(0) , [ESPI\_IO\_MODE\_DUAL\_LINES](#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0af766582d28d16af7c5aff6372e4ee243) = BIT(1) , [ESPI\_IO\_MODE\_QUAD\_LINES](#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a87e70bb0f5c4f6a3a21ca1bcfa4540fc) = BIT(2) } |
|  | eSPI I/O mode capabilities [More...](#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0) |
| enum | [espi\_channel](#gafaa3f7d54503c901ab23bd79a7f8a755) { [ESPI\_CHANNEL\_PERIPHERAL](#ggafaa3f7d54503c901ab23bd79a7f8a755a32f636bbad2618a6b1554656d3b53206) = BIT(0) , [ESPI\_CHANNEL\_VWIRE](#ggafaa3f7d54503c901ab23bd79a7f8a755ac2e84a127870ff50359cf96528c9a7c6) = BIT(1) , [ESPI\_CHANNEL\_OOB](#ggafaa3f7d54503c901ab23bd79a7f8a755a0ccb80544cbda501cc90ea0c3b868e54) = BIT(2) , [ESPI\_CHANNEL\_FLASH](#ggafaa3f7d54503c901ab23bd79a7f8a755a5616bf2bf49a8c457fcc2f27d9fe0518) = BIT(3) } |
|  | eSPI channel. [More...](#gafaa3f7d54503c901ab23bd79a7f8a755) |
| enum | [espi\_bus\_event](#ga36ac3fbf9813f78bad90f047e1eb1128) {     [ESPI\_BUS\_RESET](#gga36ac3fbf9813f78bad90f047e1eb1128ae6d4d43eded0d8a368c90ea653a60956) = BIT(0) , [ESPI\_BUS\_EVENT\_CHANNEL\_READY](#gga36ac3fbf9813f78bad90f047e1eb1128a996aee0a8f8ba0cead11cea0d39d2973) = BIT(1) , [ESPI\_BUS\_EVENT\_VWIRE\_RECEIVED](#gga36ac3fbf9813f78bad90f047e1eb1128aa09f7dcd4b2d3addfaddbad5b8f2e5a2) = BIT(2) , [ESPI\_BUS\_EVENT\_OOB\_RECEIVED](#gga36ac3fbf9813f78bad90f047e1eb1128a3b5e529d1d0ba11c59172ab01c30e203) = BIT(3) ,     [ESPI\_BUS\_PERIPHERAL\_NOTIFICATION](#gga36ac3fbf9813f78bad90f047e1eb1128a9ac837699f302bd10332814c7014adea) = BIT(4) , [ESPI\_BUS\_TAF\_NOTIFICATION](#gga36ac3fbf9813f78bad90f047e1eb1128a9f2a9cfda3b803687a0992a9d41f0014) = BIT(5)   } |
|  | eSPI bus event. [More...](#ga36ac3fbf9813f78bad90f047e1eb1128) |
| enum | [espi\_pc\_event](#gac55098842dd9d181144ac4b4122a610e) { [ESPI\_PC\_EVT\_BUS\_CHANNEL\_READY](#ggac55098842dd9d181144ac4b4122a610ea68ecb52b04ffddcc93fbcc77d3643687) = BIT(0) , [ESPI\_PC\_EVT\_BUS\_MASTER\_ENABLE](#ggac55098842dd9d181144ac4b4122a610ea0e245cbeef479218d4e6c9bec57e40d1) = BIT(1) } |
|  | eSPI peripheral channel events. [More...](#gac55098842dd9d181144ac4b4122a610e) |
| enum | [espi\_virtual\_peripheral](#ga2629a5518a94f031419eeccd05f07373) {     [ESPI\_PERIPHERAL\_UART](#gga2629a5518a94f031419eeccd05f07373a24478711945fd5258d8ca86bbb79b867) , [ESPI\_PERIPHERAL\_8042\_KBC](#gga2629a5518a94f031419eeccd05f07373aaea75bb5ab8a5ff31dd6b8787f44df30) , [ESPI\_PERIPHERAL\_HOST\_IO](#gga2629a5518a94f031419eeccd05f07373a8948a6f18bfbe87859a529d5f6e669b8) , [ESPI\_PERIPHERAL\_DEBUG\_PORT80](#gga2629a5518a94f031419eeccd05f07373af51b7171cf6085fa7946333ff32fe2f0) ,     [ESPI\_PERIPHERAL\_HOST\_IO\_PVT](#gga2629a5518a94f031419eeccd05f07373aa217b4786d7b8bacbaa4ec740550e71e)   } |
|  | eSPI peripheral notification type. [More...](#ga2629a5518a94f031419eeccd05f07373) |
| enum | [espi\_cycle\_type](#ga3e52615f244d7fa8ccda495ab8ec8a5b) {     [ESPI\_CYCLE\_MEMORY\_READ32](#gga3e52615f244d7fa8ccda495ab8ec8a5ba5b480e093a58849d4181bba22d5868a5) , [ESPI\_CYCLE\_MEMORY\_READ64](#gga3e52615f244d7fa8ccda495ab8ec8a5bac8ec7673b4466b278dfb5e468f7a4d79) , [ESPI\_CYCLE\_MEMORY\_WRITE32](#gga3e52615f244d7fa8ccda495ab8ec8a5ba2e5a736cf8a63491ee13d51ae4f8f073) , [ESPI\_CYCLE\_MEMORY\_WRITE64](#gga3e52615f244d7fa8ccda495ab8ec8a5ba54c11e63fcfe3f859af57e65af3f31f7) ,     [ESPI\_CYCLE\_MESSAGE\_NODATA](#gga3e52615f244d7fa8ccda495ab8ec8a5ba5f2ae0575ca4e9b61c0acd7d4f08ee82) , [ESPI\_CYCLE\_MESSAGE\_DATA](#gga3e52615f244d7fa8ccda495ab8ec8a5ba380e3d4e6b5579c8bb94e792fcb7d71f) , [ESPI\_CYCLE\_OK\_COMPLETION\_NODATA](#gga3e52615f244d7fa8ccda495ab8ec8a5ba0335f2d34fab46960939e2d2c1c12e3f) , [ESPI\_CYCLE\_OKCOMPLETION\_DATA](#gga3e52615f244d7fa8ccda495ab8ec8a5baf3dbc2bcc0ed883bc4d4160c21e6934f) ,     [ESPI\_CYCLE\_NOK\_COMPLETION\_NODATA](#gga3e52615f244d7fa8ccda495ab8ec8a5ba0edb306e5fabcbf8b009375cde6a8a2b)   } |
|  | eSPI cycle types supported over eSPI peripheral channel [More...](#ga3e52615f244d7fa8ccda495ab8ec8a5b) |
| enum | [espi\_vwire\_signal](#gab65a0951a8912d9de398cfec0aef7d35) {     [ESPI\_VWIRE\_SIGNAL\_SLP\_S3](#ggab65a0951a8912d9de398cfec0aef7d35ab880a7156e489d5f7b8f78550e72b166) , [ESPI\_VWIRE\_SIGNAL\_SLP\_S4](#ggab65a0951a8912d9de398cfec0aef7d35a4ef1fe12bd09be0875864d6c32164f73) , [ESPI\_VWIRE\_SIGNAL\_SLP\_S5](#ggab65a0951a8912d9de398cfec0aef7d35ac4b4e30c097a4ef49f21549a799e1e13) , [ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_WARN](#ggab65a0951a8912d9de398cfec0aef7d35a2f3f97b51b750050cd98e887e39431d1) ,     [ESPI\_VWIRE\_SIGNAL\_PLTRST](#ggab65a0951a8912d9de398cfec0aef7d35a0bafcd0bb7f592f0e308dcfce39bcd08) , [ESPI\_VWIRE\_SIGNAL\_SUS\_STAT](#ggab65a0951a8912d9de398cfec0aef7d35a0e13f250ba0c5a37451c7f3b0e98e663) , [ESPI\_VWIRE\_SIGNAL\_NMIOUT](#ggab65a0951a8912d9de398cfec0aef7d35ad14b4b7a25141346bfefc507c588a238) , [ESPI\_VWIRE\_SIGNAL\_SMIOUT](#ggab65a0951a8912d9de398cfec0aef7d35a1d54a71c6d2e52cb66cfaa0b55b61152) ,     [ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_WARN](#ggab65a0951a8912d9de398cfec0aef7d35af44250de6f60eabf9b0d85b8860ac56e) , [ESPI\_VWIRE\_SIGNAL\_SLP\_A](#ggab65a0951a8912d9de398cfec0aef7d35aa4c8c69475b48d88302066823d2f3592) , [ESPI\_VWIRE\_SIGNAL\_SUS\_PWRDN\_ACK](#ggab65a0951a8912d9de398cfec0aef7d35ab4f0bedd5717660cc8cac2d85c6c3d18) , [ESPI\_VWIRE\_SIGNAL\_SUS\_WARN](#ggab65a0951a8912d9de398cfec0aef7d35a9e32eee077aaa1668c356fe1d4ab1cc5) ,     [ESPI\_VWIRE\_SIGNAL\_SLP\_WLAN](#ggab65a0951a8912d9de398cfec0aef7d35a3d95f095ae41bba9ef916fc68ddd4779) , [ESPI\_VWIRE\_SIGNAL\_SLP\_LAN](#ggab65a0951a8912d9de398cfec0aef7d35aba8b891a643ca567966d091963be4615) , [ESPI\_VWIRE\_SIGNAL\_HOST\_C10](#ggab65a0951a8912d9de398cfec0aef7d35ab9deb0dd6d4e878eff6413ddc34bb36c) , [ESPI\_VWIRE\_SIGNAL\_DNX\_WARN](#ggab65a0951a8912d9de398cfec0aef7d35a923f3e602d9f8ac821ece2a625183146) ,     [ESPI\_VWIRE\_SIGNAL\_PME](#ggab65a0951a8912d9de398cfec0aef7d35aa87af5b5de184238e5f371851aaee692) , [ESPI\_VWIRE\_SIGNAL\_WAKE](#ggab65a0951a8912d9de398cfec0aef7d35a736724f8229aebc356c2720a34a0143f) , [ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_ACK](#ggab65a0951a8912d9de398cfec0aef7d35a8e15df6f8159b4c275dc4b20aaec352e) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_BOOT\_STS](#ggab65a0951a8912d9de398cfec0aef7d35a231caf3d46cde2eaf7305bf3f694838c) ,     [ESPI\_VWIRE\_SIGNAL\_ERR\_NON\_FATAL](#ggab65a0951a8912d9de398cfec0aef7d35a504ae332b89262f70a0bf1a9c8b6f527) , [ESPI\_VWIRE\_SIGNAL\_ERR\_FATAL](#ggab65a0951a8912d9de398cfec0aef7d35aae0a3fd882c5765db33a4e7bd05e1ab1) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_BOOT\_DONE](#ggab65a0951a8912d9de398cfec0aef7d35ad99ea62f91b40c8926cda944928e3631) , [ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_ACK](#ggab65a0951a8912d9de398cfec0aef7d35a89420628ae26df4c45ef7fba04a3a85e) ,     [ESPI\_VWIRE\_SIGNAL\_RST\_CPU\_INIT](#ggab65a0951a8912d9de398cfec0aef7d35a19c40230e0bb4cee7b6ee42580c28a8d) , [ESPI\_VWIRE\_SIGNAL\_SMI](#ggab65a0951a8912d9de398cfec0aef7d35a2d9b2eef499d1bfd13bec1d2caa0e2f3) , [ESPI\_VWIRE\_SIGNAL\_SCI](#ggab65a0951a8912d9de398cfec0aef7d35afa1f99a7e45b306c6736888e280f527c) , [ESPI\_VWIRE\_SIGNAL\_DNX\_ACK](#ggab65a0951a8912d9de398cfec0aef7d35a58280c68c980476aabefa16e0509dd1c) ,     [ESPI\_VWIRE\_SIGNAL\_SUS\_ACK](#ggab65a0951a8912d9de398cfec0aef7d35abe28432b566619d8c6cce5e5034e5333) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_0](#ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_1](#ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_2](#ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b) ,     [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_3](#ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_4](#ggab65a0951a8912d9de398cfec0aef7d35ad9b6bb998bea0bc983ab8a6c452d52a1) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_5](#ggab65a0951a8912d9de398cfec0aef7d35af10e9e5b320301b2fe923e6793adbeaf) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_6](#ggab65a0951a8912d9de398cfec0aef7d35aee0a1576a6e07708e1cde59597b49662) ,     [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_7](#ggab65a0951a8912d9de398cfec0aef7d35ae34962d6db346e02f175894843ce0e1e) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_8](#ggab65a0951a8912d9de398cfec0aef7d35a8a7b50f0aa53a2c80bae7747d628d219) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_9](#ggab65a0951a8912d9de398cfec0aef7d35a9410475f349afcf44ddb25ebbd454978) , [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_10](#ggab65a0951a8912d9de398cfec0aef7d35a637b5c00aaca05e5daa6969a680cbbb1) ,     [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_11](#ggab65a0951a8912d9de398cfec0aef7d35a07a6b00a4b1cfad2137dc43d7232fc9f) , [ESPI\_VWIRE\_SIGNAL\_COUNT](#ggab65a0951a8912d9de398cfec0aef7d35ad3319083735295454bc59b742988cfca)   } |
|  | eSPI system platform signals that can be send or receive through virtual wire channel [More...](#gab65a0951a8912d9de398cfec0aef7d35) |
| enum | [lpc\_peripheral\_opcode](#gad00b6a22843e5df9c6d6945d0d82310e) {     [E8042\_OBF\_HAS\_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310eac172afb38cb38970ef6242a4f45132f9) = 0x50 , [E8042\_IBF\_HAS\_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310eab70684413d736c8583f3dc53f14b7c7a) , [E8042\_WRITE\_KB\_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310eaa9135a5ea9a5ebd9d25660c37983c5d6) , [E8042\_WRITE\_MB\_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310eaaef0649f867424ec0c7889acb7354911) ,     [E8042\_RESUME\_IRQ](#ggad00b6a22843e5df9c6d6945d0d82310eac5b666b3319dc2ef0fc571684c2ea198) , [E8042\_PAUSE\_IRQ](#ggad00b6a22843e5df9c6d6945d0d82310ea5e7205b5f1371f1a0f2eaed299389475) , [E8042\_CLEAR\_OBF](#ggad00b6a22843e5df9c6d6945d0d82310eacdeb74a9534310f5dab3f1bfb5def534) , [E8042\_READ\_KB\_STS](#ggad00b6a22843e5df9c6d6945d0d82310ea8c62cd1266681c88aa0cb1af65ab551b) ,     [E8042\_SET\_FLAG](#ggad00b6a22843e5df9c6d6945d0d82310ea83266d88740588d45be6667a4034c447) , [E8042\_CLEAR\_FLAG](#ggad00b6a22843e5df9c6d6945d0d82310ea5c592b1cad381b296cde832c67264cd1) , [EACPI\_OBF\_HAS\_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310ea3cce8bd0205691ecda53fc469606929d) = EACPI\_START\_OPCODE , [EACPI\_IBF\_HAS\_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310ea09f241a3f6ffcb5b7839c81c7fc4ea6e) ,     [EACPI\_WRITE\_CHAR](#ggad00b6a22843e5df9c6d6945d0d82310ea689643f6feb724a303d3b790ff2899f7) , [EACPI\_READ\_STS](#ggad00b6a22843e5df9c6d6945d0d82310ea02bf8538a66f633e3d2ec094f57c6173) , [EACPI\_WRITE\_STS](#ggad00b6a22843e5df9c6d6945d0d82310ea02c7b1c69d803a5c45304260786afb6f)   } |

| Functions | |
| --- | --- |
| int | [espi\_config](#ga7227c53d384eb0dc666361261f069f68) (const struct [device](structdevice.md) \*dev, struct [espi\_cfg](structespi__cfg.md) \*cfg) |
|  | Configure operation of a eSPI controller. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [espi\_get\_channel\_status](#ga869551e20fc2c3be4311c21c3c53999d) (const struct [device](structdevice.md) \*dev, enum [espi\_channel](#gafaa3f7d54503c901ab23bd79a7f8a755) ch) |
|  | Query to see if it a channel is ready. |
| int | [espi\_read\_request](#ga112f7554ba614c8e5f239b1319b4a763) (const struct [device](structdevice.md) \*dev, struct [espi\_request\_packet](structespi__request__packet.md) \*req) |
|  | Sends memory, I/O or message read request over eSPI. |
| int | [espi\_write\_request](#ga143ed88b1f220f9582c809165fd983fd) (const struct [device](structdevice.md) \*dev, struct [espi\_request\_packet](structespi__request__packet.md) \*req) |
|  | Sends memory, I/O or message write request over eSPI. |
| int | [espi\_read\_lpc\_request](#gaeaae20afa90d9d825d80997369f31465) (const struct [device](structdevice.md) \*dev, enum [lpc\_peripheral\_opcode](#gad00b6a22843e5df9c6d6945d0d82310e) op, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data) |
|  | Reads SOC data from a LPC peripheral with information updated over eSPI. |
| int | [espi\_write\_lpc\_request](#ga880b6b04824f9f0deea10e8018573b88) (const struct [device](structdevice.md) \*dev, enum [lpc\_peripheral\_opcode](#gad00b6a22843e5df9c6d6945d0d82310e) op, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data) |
|  | Writes data to a LPC peripheral which generates an eSPI transaction. |
| int | [espi\_send\_vwire](#gacab2b3bff7d940e71ee1c2a9fdedf782) (const struct [device](structdevice.md) \*dev, enum [espi\_vwire\_signal](#gab65a0951a8912d9de398cfec0aef7d35) signal, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Sends system/platform signal as a virtual wire packet. |
| int | [espi\_receive\_vwire](#gaa8bb48b5592c4b49d27c9b8a42432410) (const struct [device](structdevice.md) \*dev, enum [espi\_vwire\_signal](#gab65a0951a8912d9de398cfec0aef7d35) signal, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level) |
|  | Retrieves level status for a signal encapsulated in a virtual wire. |
| int | [espi\_send\_oob](#ga2557cfc7a38f669d14e9826e3fb0fdee) (const struct [device](structdevice.md) \*dev, struct [espi\_oob\_packet](structespi__oob__packet.md) \*pckt) |
|  | Sends SMBus transaction (out-of-band) packet over eSPI bus. |
| int | [espi\_receive\_oob](#ga4b8f4fbf66a2b2ae394e00b16500f70d) (const struct [device](structdevice.md) \*dev, struct [espi\_oob\_packet](structespi__oob__packet.md) \*pckt) |
|  | Receives SMBus transaction (out-of-band) packet from eSPI bus. |
| int | [espi\_read\_flash](#ga0a97d11167367342283bfe6b6d66726e) (const struct [device](structdevice.md) \*dev, struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt) |
|  | Sends a read request packet for shared flash. |
| int | [espi\_write\_flash](#gab02d46fd690e33875cc1b2433c976891) (const struct [device](structdevice.md) \*dev, struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt) |
|  | Sends a write request packet for shared flash. |
| int | [espi\_flash\_erase](#gab42be7c76c4523cea96365aa77fd18be) (const struct [device](structdevice.md) \*dev, struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt) |
|  | Sends a write request packet for shared flash. |
| static void | [espi\_init\_callback](#ga8d88e4e3893d610713195e5352ec2565) (struct espi\_callback \*callback, [espi\_callback\_handler\_t](#ga9d848c7e367cf277230f365f73c15c46) handler, enum [espi\_bus\_event](#ga36ac3fbf9813f78bad90f047e1eb1128) evt\_type) |
|  | Callback model. |
| static int | [espi\_add\_callback](#gabf5f0ea01ec8ed5345b2e119181c2313) (const struct [device](structdevice.md) \*dev, struct espi\_callback \*callback) |
|  | Add an application callback. |
| static int | [espi\_remove\_callback](#ga7f04f98ea6a4671b821cf6ddf6bbf2a6) (const struct [device](structdevice.md) \*dev, struct espi\_callback \*callback) |
|  | Remove an application callback. |
| int | [espi\_saf\_config](#ga34b0f6336aec45016d97528767b09434) (const struct [device](structdevice.md) \*dev, const struct [espi\_saf\_cfg](structespi__saf__cfg.md) \*cfg) |
|  | Configure operation of a eSPI controller. |
| int | [espi\_saf\_set\_protection\_regions](#ga273a9707f3ca501ed2dd3019cdeaa363) (const struct [device](structdevice.md) \*dev, const struct espi\_saf\_protection \*pr) |
|  | Set one or more SAF protection regions. |
| int | [espi\_saf\_activate](#gaafe30738c18a16b056ed8dcf8638eb84) (const struct [device](structdevice.md) \*dev) |
|  | Activate SAF block. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [espi\_saf\_get\_channel\_status](#ga8b53a93559f0c67953e283f59107aa22) (const struct [device](structdevice.md) \*dev) |
|  | Query to see if SAF is ready. |
| int | [espi\_saf\_flash\_read](#ga0f5017eac05f928e635fec8e5f877c7d) (const struct [device](structdevice.md) \*dev, struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt) |
|  | Sends a read request packet for slave attached flash. |
| int | [espi\_saf\_flash\_write](#ga104175f74019e58b8b7901f3dae245db) (const struct [device](structdevice.md) \*dev, struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt) |
|  | Sends a write request packet for slave attached flash. |
| int | [espi\_saf\_flash\_erase](#ga15855a2ac593b97dc1a3e83ac9eda300) (const struct [device](structdevice.md) \*dev, struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt) |
|  | Sends a write request packet for slave attached flash. |
| int | [espi\_saf\_flash\_unsuccess](#ga6c54d9274b1a8e883484bd892f606fd5) (const struct [device](structdevice.md) \*dev, struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt) |
|  | Response unsuccessful completion for slave attached flash. |
| static void | [espi\_saf\_init\_callback](#ga324283c28e6a33be112571621d1568e8) (struct espi\_callback \*callback, [espi\_callback\_handler\_t](#ga9d848c7e367cf277230f365f73c15c46) handler, enum [espi\_bus\_event](#ga36ac3fbf9813f78bad90f047e1eb1128) evt\_type) |
|  | Callback model. |
| static int | [espi\_saf\_add\_callback](#gadb881f847082f713bb0159d1e474980a) (const struct [device](structdevice.md) \*dev, struct espi\_callback \*callback) |
|  | Add an application callback. |
| static int | [espi\_saf\_remove\_callback](#gaf987842bc7dad310c7270aed50086af9) (const struct [device](structdevice.md) \*dev, struct espi\_callback \*callback) |
|  | Remove an application callback. |

## Detailed Description

eSPI Driver APIs

eSPI SAF Driver APIs

## Macro Definition Documentation

## [◆ ](#gae4855b6cf8049de8aa6d67763f1be8c3)ESPI\_VWIRE\_SIGNAL\_OCB\_0

| #define ESPI\_VWIRE\_SIGNAL\_OCB\_0   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_0](#ggab65a0951a8912d9de398cfec0aef7d35aa075b359a98779f42bc9447adc1b27a2) |
| --- |

`#include <[espi.h](espi_8h.md)>`

## [◆ ](#ga2ed490939e0249ff8196f77a74967727)ESPI\_VWIRE\_SIGNAL\_OCB\_1

| #define ESPI\_VWIRE\_SIGNAL\_OCB\_1   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_1](#ggab65a0951a8912d9de398cfec0aef7d35ab4e6f770d2a8f8b0f2d2be6c392f92de) |
| --- |

`#include <[espi.h](espi_8h.md)>`

## [◆ ](#gaf35d03bc041dc6baefe35b74c163d73b)ESPI\_VWIRE\_SIGNAL\_OCB\_2

| #define ESPI\_VWIRE\_SIGNAL\_OCB\_2   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_2](#ggab65a0951a8912d9de398cfec0aef7d35a5e0bb79530540c15e802c852b5ee944b) |
| --- |

`#include <[espi.h](espi_8h.md)>`

## [◆ ](#gaeae1765d801cd298c27404c173a94707)ESPI\_VWIRE\_SIGNAL\_OCB\_3

| #define ESPI\_VWIRE\_SIGNAL\_OCB\_3   [ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_3](#ggab65a0951a8912d9de398cfec0aef7d35ac8c015227c6d6c2441ea811faa543b5a) |
| --- |

`#include <[espi.h](espi_8h.md)>`

## [◆ ](#gaa0807c908666cdcbb3a85f310bfbfccc)HOST\_KBC\_EVT\_IBF

| #define HOST\_KBC\_EVT\_IBF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[espi.h](espi_8h.md)>`

## [◆ ](#ga807bb75027f24e040cd28eba4bc1002c)HOST\_KBC\_EVT\_OBE

| #define HOST\_KBC\_EVT\_OBE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[espi.h](espi_8h.md)>`

## Typedef Documentation

## [◆ ](#ga9d848c7e367cf277230f365f73c15c46)espi\_callback\_handler\_t

| typedef void(\* espi\_callback\_handler\_t) (const struct [device](structdevice.md) \*dev, struct espi\_callback \*cb, struct [espi\_event](structespi__event.md) espi\_evt) |
| --- |

`#include <[espi.h](espi_8h.md)>`

Define the application callback handler function signature.

Parameters
:   | dev | Device struct for the eSPI device. |
    | --- | --- |
    | cb | Original struct espi\_callback owning this handler. |
    | espi\_evt | event details that trigger the callback handler. |

## Enumeration Type Documentation

## [◆ ](#ga36ac3fbf9813f78bad90f047e1eb1128)espi\_bus\_event

| enum [espi\_bus\_event](#ga36ac3fbf9813f78bad90f047e1eb1128) |
| --- |

`#include <[espi.h](espi_8h.md)>`

eSPI bus event.

eSPI bus event to indicate events for which user can register callbacks

| Enumerator | |
| --- | --- |
| ESPI\_BUS\_RESET | Indicates the eSPI bus was reset either via eSPI reset pin.  eSPI drivers should convey the eSPI reset status to eSPI driver clients following eSPI specification reset pin convention: 0-eSPI bus in reset, 1-eSPI bus out-of-reset  Note: There is no need to send this callback for in-band reset. |
| ESPI\_BUS\_EVENT\_CHANNEL\_READY | Indicates the eSPI HW has received channel enable notification from eSPI host, once the eSPI channel is signal as ready to the eSPI host, eSPI drivers should convey the eSPI channel ready to eSPI driver client via this event. |
| ESPI\_BUS\_EVENT\_VWIRE\_RECEIVED | Indicates the eSPI HW has received a virtual wire message from eSPI host.  eSPI drivers should convey the eSPI virtual wire latest status. |
| ESPI\_BUS\_EVENT\_OOB\_RECEIVED | Indicates the eSPI HW has received a Out-of-band package from eSPI host. |
| ESPI\_BUS\_PERIPHERAL\_NOTIFICATION | Indicates the eSPI HW has received a peripheral eSPI host event.  eSPI drivers should convey the peripheral type. |
| ESPI\_BUS\_TAF\_NOTIFICATION |  |

## [◆ ](#gafaa3f7d54503c901ab23bd79a7f8a755)espi\_channel

| enum [espi\_channel](#gafaa3f7d54503c901ab23bd79a7f8a755) |
| --- |

`#include <[espi.h](espi_8h.md)>`

eSPI channel.

+----------------------------------------------------------------------+

| |

| eSPI controller +-------------+ |

| +-----------+ | Power | +----------+ |

| |Out of band| | management | | GPIO | |

| +------------+ |processor | | controller | | sources | |

| | SPI flash | +-----------+ +-------------+ +----------+ |

| | controller | | | | |

| +------------+ | | | |

| | | | +--------+ +---------------+ |

| | | | | | |

| | | +-----+ +--------+ +----------+ +----v-----+ |

| | | | | LPC | | Tunneled | | Tunneled | |

| | | | | bridge | | SMBus | | GPIO | |

| | | | +--------+ +----------+ +----------+ |

| | | | | | | |

| | | | ------+ | | |

| | | | | | | |

| | | +------v-----+ +---v-------v-------------v----+ |

| | | | eSPI Flash | | eSPI protocol block | |

| | | | access +--->+ | |

| | | +------------+ +------------------------------+ |

| | | | |

| | +-----------+ | |

| | v v |

| | XXXXXXXXXXXXXXXXXXXXXXX |

| | XXXXXXXXXXXXXXXXXXXXX |

| | XXXXXXXXXXXXXXXXXXX |

+----------------------------------------------------------------------+

| |

v +-----------------+

+---------+ | | | | | |

| Flash | | | | | | |

+---------+ | + + + + | eSPI bus

| CH0 CH1 CH2 CH3 | (logical channels)

| + + + + |

| | | | | |

+-----------------+

|

+-----------------------------------------------------------------------+

| eSPI target |

| |

| CH0 | CH1 | CH2 | CH3 |

| eSPI endpoint | VWIRE | OOB | Flash |

+-----------------------------------------------------------------------+

Identifies each eSPI logical channel supported by eSPI controller Each channel allows independent traffic, but the assignment of channel type to channel number is fixed.

Note that generic commands are not associated with any channel, so traffic over eSPI can occur if all channels are disabled or not ready

| Enumerator | |
| --- | --- |
| ESPI\_CHANNEL\_PERIPHERAL |  |
| ESPI\_CHANNEL\_VWIRE |  |
| ESPI\_CHANNEL\_OOB |  |
| ESPI\_CHANNEL\_FLASH |  |

## [◆ ](#ga3e52615f244d7fa8ccda495ab8ec8a5b)espi\_cycle\_type

| enum [espi\_cycle\_type](#ga3e52615f244d7fa8ccda495ab8ec8a5b) |
| --- |

`#include <[espi.h](espi_8h.md)>`

eSPI cycle types supported over eSPI peripheral channel

| Enumerator | |
| --- | --- |
| ESPI\_CYCLE\_MEMORY\_READ32 |  |
| ESPI\_CYCLE\_MEMORY\_READ64 |  |
| ESPI\_CYCLE\_MEMORY\_WRITE32 |  |
| ESPI\_CYCLE\_MEMORY\_WRITE64 |  |
| ESPI\_CYCLE\_MESSAGE\_NODATA |  |
| ESPI\_CYCLE\_MESSAGE\_DATA |  |
| ESPI\_CYCLE\_OK\_COMPLETION\_NODATA |  |
| ESPI\_CYCLE\_OKCOMPLETION\_DATA |  |
| ESPI\_CYCLE\_NOK\_COMPLETION\_NODATA |  |

## [◆ ](#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0)espi\_io\_mode

| enum [espi\_io\_mode](#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0) |
| --- |

`#include <[espi.h](espi_8h.md)>`

eSPI I/O mode capabilities

| Enumerator | |
| --- | --- |
| ESPI\_IO\_MODE\_SINGLE\_LINE |  |
| ESPI\_IO\_MODE\_DUAL\_LINES |  |
| ESPI\_IO\_MODE\_QUAD\_LINES |  |

## [◆ ](#gac55098842dd9d181144ac4b4122a610e)espi\_pc\_event

| enum [espi\_pc\_event](#gac55098842dd9d181144ac4b4122a610e) |
| --- |

`#include <[espi.h](espi_8h.md)>`

eSPI peripheral channel events.

eSPI peripheral channel event types to indicate users.

| Enumerator | |
| --- | --- |
| ESPI\_PC\_EVT\_BUS\_CHANNEL\_READY |  |
| ESPI\_PC\_EVT\_BUS\_MASTER\_ENABLE |  |

## [◆ ](#ga2629a5518a94f031419eeccd05f07373)espi\_virtual\_peripheral

| enum [espi\_virtual\_peripheral](#ga2629a5518a94f031419eeccd05f07373) |
| --- |

`#include <[espi.h](espi_8h.md)>`

eSPI peripheral notification type.

eSPI peripheral notification event details to indicate which peripheral trigger the eSPI callback

| Enumerator | |
| --- | --- |
| ESPI\_PERIPHERAL\_UART |  |
| ESPI\_PERIPHERAL\_8042\_KBC |  |
| ESPI\_PERIPHERAL\_HOST\_IO |  |
| ESPI\_PERIPHERAL\_DEBUG\_PORT80 |  |
| ESPI\_PERIPHERAL\_HOST\_IO\_PVT |  |

## [◆ ](#gab65a0951a8912d9de398cfec0aef7d35)espi\_vwire\_signal

| enum [espi\_vwire\_signal](#gab65a0951a8912d9de398cfec0aef7d35) |
| --- |

`#include <[espi.h](espi_8h.md)>`

eSPI system platform signals that can be send or receive through virtual wire channel

| Enumerator | |
| --- | --- |
| ESPI\_VWIRE\_SIGNAL\_SLP\_S3 |  |
| ESPI\_VWIRE\_SIGNAL\_SLP\_S4 |  |
| ESPI\_VWIRE\_SIGNAL\_SLP\_S5 |  |
| ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_WARN |  |
| ESPI\_VWIRE\_SIGNAL\_PLTRST |  |
| ESPI\_VWIRE\_SIGNAL\_SUS\_STAT |  |
| ESPI\_VWIRE\_SIGNAL\_NMIOUT |  |
| ESPI\_VWIRE\_SIGNAL\_SMIOUT |  |
| ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_WARN |  |
| ESPI\_VWIRE\_SIGNAL\_SLP\_A |  |
| ESPI\_VWIRE\_SIGNAL\_SUS\_PWRDN\_ACK |  |
| ESPI\_VWIRE\_SIGNAL\_SUS\_WARN |  |
| ESPI\_VWIRE\_SIGNAL\_SLP\_WLAN |  |
| ESPI\_VWIRE\_SIGNAL\_SLP\_LAN |  |
| ESPI\_VWIRE\_SIGNAL\_HOST\_C10 |  |
| ESPI\_VWIRE\_SIGNAL\_DNX\_WARN |  |
| ESPI\_VWIRE\_SIGNAL\_PME |  |
| ESPI\_VWIRE\_SIGNAL\_WAKE |  |
| ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_ACK |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_BOOT\_STS |  |
| ESPI\_VWIRE\_SIGNAL\_ERR\_NON\_FATAL |  |
| ESPI\_VWIRE\_SIGNAL\_ERR\_FATAL |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_BOOT\_DONE |  |
| ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_ACK |  |
| ESPI\_VWIRE\_SIGNAL\_RST\_CPU\_INIT |  |
| ESPI\_VWIRE\_SIGNAL\_SMI |  |
| ESPI\_VWIRE\_SIGNAL\_SCI |  |
| ESPI\_VWIRE\_SIGNAL\_DNX\_ACK |  |
| ESPI\_VWIRE\_SIGNAL\_SUS\_ACK |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_0 |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_1 |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_2 |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_3 |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_4 |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_5 |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_6 |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_7 |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_8 |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_9 |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_10 |  |
| ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_11 |  |
| ESPI\_VWIRE\_SIGNAL\_COUNT |  |

## [◆ ](#gad00b6a22843e5df9c6d6945d0d82310e)lpc\_peripheral\_opcode

| enum [lpc\_peripheral\_opcode](#gad00b6a22843e5df9c6d6945d0d82310e) |
| --- |

`#include <[espi.h](espi_8h.md)>`

| Enumerator | |
| --- | --- |
| E8042\_OBF\_HAS\_CHAR |  |
| E8042\_IBF\_HAS\_CHAR |  |
| E8042\_WRITE\_KB\_CHAR |  |
| E8042\_WRITE\_MB\_CHAR |  |
| E8042\_RESUME\_IRQ |  |
| E8042\_PAUSE\_IRQ |  |
| E8042\_CLEAR\_OBF |  |
| E8042\_READ\_KB\_STS |  |
| E8042\_SET\_FLAG |  |
| E8042\_CLEAR\_FLAG |  |
| EACPI\_OBF\_HAS\_CHAR |  |
| EACPI\_IBF\_HAS\_CHAR |  |
| EACPI\_WRITE\_CHAR |  |
| EACPI\_READ\_STS |  |
| EACPI\_WRITE\_STS |  |

## Function Documentation

## [◆ ](#gabf5f0ea01ec8ed5345b2e119181c2313)espi\_add\_callback()

| | int espi\_add\_callback | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct espi\_callback \* | *callback* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[espi.h](espi_8h.md)>`

Add an application callback.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | callback | A valid Application's callback structure pointer. |

Returns
:   0 if successful, negative errno code on failure.

Note
:   Callbacks may be added to the device from within a callback handler invocation, but whether they are invoked for the current eSPI event is not specified.

Note: enables to add as many callback as needed on the same device.

## [◆ ](#ga7227c53d384eb0dc666361261f069f68)espi\_config()

| int espi\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_cfg](structespi__cfg.md) \* | *cfg* ) |

`#include <[espi.h](espi_8h.md)>`

Configure operation of a eSPI controller.

This routine provides a generic interface to override eSPI controller capabilities.

If this eSPI controller is acting as target, the values set here will be discovered as part through the GET\_CONFIGURATION command issued by the eSPI controller during initialization.

If this eSPI controller is acting as controller, the values set here will be used by eSPI controller to determine minimum common capabilities with eSPI target then send via SET\_CONFIGURATION command.

+---------+ +---------+ +------+ +---------+ +---------+

| eSPI | | eSPI | | eSPI | | eSPI | | eSPI |

| target | | driver | | bus | | driver | | host |

+--------+ +---------+ +------+ +---------+ +---------+

| | | | |

| [espi\_config](#ga7227c53d384eb0dc666361261f069f68) | Set eSPI | Set eSPI | [espi\_config](#ga7227c53d384eb0dc666361261f069f68) |

+--------------+ ctrl regs | cap ctrl reg| +-----------+

| +-------+ | +--------+ |

| |<------+ | +------->| |

| | | | |

| | | | |

| | | GET\_CONFIGURATION | |

| | +<------------------+ |

| |<-----------| | |

| | eSPI caps | | |

| |----------->+ response | |

| | |------------------>+ |

| | | | |

| | | SET\_CONFIGURATION | |

| | +<------------------+ |

| | | [accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb) | |

| | +------------------>+ |

+ + + + +

[accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb)

static int accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

POSIX wrapper for zsock\_accept.

**Definition** socket.h:910

[espi\_config](#ga7227c53d384eb0dc666361261f069f68)

int espi\_config(const struct device \*dev, struct espi\_cfg \*cfg)

Configure operation of a eSPI controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | cfg | the device runtime configuration for the eSPI controller. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error, failed to configure device. |
    | -EINVAL | invalid capabilities, failed to configure device. |
    | -ENOTSUP | capability not supported by eSPI target. |

## [◆ ](#gab42be7c76c4523cea96365aa77fd18be)espi\_flash\_erase()

| int espi\_flash\_erase | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_flash\_packet](structespi__flash__packet.md) \* | *pckt* ) |

`#include <[espi.h](espi_8h.md)>`

Sends a write request packet for shared flash.

This routines provides an interface to send a request to write to the flash components shared between the eSPI controller and eSPI targets.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pckt | Address of the representation of write flash transaction. |

Return values
:   | -ENOTSUP | eSPI flash logical channel transactions not supported. |
    | --- | --- |
    | -EBUSY | eSPI flash channel is not ready or disabled by controller. |
    | -EIO | General input / output error, failed request to controller. |

## [◆ ](#ga869551e20fc2c3be4311c21c3c53999d)espi\_get\_channel\_status()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) espi\_get\_channel\_status | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [espi\_channel](#gafaa3f7d54503c901ab23bd79a7f8a755) | *ch* ) |

`#include <[espi.h](espi_8h.md)>`

Query to see if it a channel is ready.

This routine allows to check if logical channel is ready before use. Note that queries for channels not supported will always return false.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ch | the eSPI channel for which status is to be retrieved. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If eSPI channel is ready. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | otherwise. |

## [◆ ](#ga8d88e4e3893d610713195e5352ec2565)espi\_init\_callback()

| | void espi\_init\_callback | ( | struct espi\_callback \* | *callback*, | | --- | --- | --- | --- | |  |  | [espi\_callback\_handler\_t](#ga9d848c7e367cf277230f365f73c15c46) | *handler*, | |  |  | enum [espi\_bus\_event](#ga36ac3fbf9813f78bad90f047e1eb1128) | *evt\_type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[espi.h](espi_8h.md)>`

Callback model.

+-------+ +-------------+ +------+ +---------+

| App | | eSPI driver | | HW | |eSPI Host|

+---+---+ +-------+-----+ +---+--+ +----+----+

| | | |

| [espi\_init\_callback](#ga8d88e4e3893d610713195e5352ec2565) | | |

+----------------------------> | | |

| [espi\_add\_callback](#gabf5f0ea01ec8ed5345b2e119181c2313) | |

+----------------------------->+ |

| | | eSPI reset | eSPI host

| | IRQ +<------------+ resets the

| | <-----------+ | bus

|<-----------------------------| | |

| Report eSPI bus reset | Processed | |

| | within the | |

| | driver | |

| | | |

| | | VW CH ready| eSPI host

| | IRQ +<------------+ enables VW

| | <-----------+ | channel

| | | |

| | Processed | |

| | within the | |

| | driver | |

| | | |

| | | Memory I/O | Peripheral

| | <-------------+ event

| +<------------+ |

+<-----------------------------+ callback | |

| Report peripheral event | | |

| and data for the event | | |

| | | |

| | | SLP\_S5 | eSPI host

| | <-------------+ [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d) VWire

| +<------------+ |

+<-----------------------------+ callback | |

| App enables/configures | | |

| discrete regulator | | |

| | | |

| espi\_send\_vwire\_signal | | |

+------------------------------>------------>|------------>|

| | | |

| | | HOST\_RST | eSPI host

| | <-------------+ [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d) VWire

| +<------------+ |

+<-----------------------------+ callback | |

| App reset host-related | | |

| data structures | | |

| | | |

| | | C10 | eSPI host

| | +<------------+ [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d) VWire

| <-------------+ |

<------------------------------+ | |

| App executes | | |

+ power mgmt policy | | |

[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)

static ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

POSIX wrapper for zsock\_send.

**Definition** socket.h:916

[espi\_init\_callback](#ga8d88e4e3893d610713195e5352ec2565)

static void espi\_init\_callback(struct espi\_callback \*callback, espi\_callback\_handler\_t handler, enum espi\_bus\_event evt\_type)

Callback model.

**Definition** espi.h:982

[espi\_add\_callback](#gabf5f0ea01ec8ed5345b2e119181c2313)

static int espi\_add\_callback(const struct device \*dev, struct espi\_callback \*callback)

Add an application callback.

**Definition** espi.h:1005

Helper to initialize a struct espi\_callback properly.

Parameters
:   | callback | A valid Application's callback structure pointer. |
    | --- | --- |
    | handler | A valid handler function pointer. |
    | evt\_type | indicates the eSPI event relevant for the handler. for VWIRE\_RECEIVED event the data will indicate the new level asserted |

## [◆ ](#ga0a97d11167367342283bfe6b6d66726e)espi\_read\_flash()

| int espi\_read\_flash | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_flash\_packet](structespi__flash__packet.md) \* | *pckt* ) |

`#include <[espi.h](espi_8h.md)>`

Sends a read request packet for shared flash.

This routines provides an interface to send a request to read the flash component shared between the eSPI controller and eSPI targets.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pckt | Address of the representation of read flash transaction. |

Return values
:   | -ENOTSUP | eSPI flash logical channel transactions not supported. |
    | --- | --- |
    | -EBUSY | eSPI flash channel is not ready or disabled by controller. |
    | -EIO | General input / output error, failed request to controller. |

## [◆ ](#gaeaae20afa90d9d825d80997369f31465)espi\_read\_lpc\_request()

| int espi\_read\_lpc\_request | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [lpc\_peripheral\_opcode](#gad00b6a22843e5df9c6d6945d0d82310e) | *op*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *data* ) |

`#include <[espi.h](espi_8h.md)>`

Reads SOC data from a LPC peripheral with information updated over eSPI.

This routine provides a generic interface to read a block whose information was updated by an eSPI transaction. Reading may trigger a transaction. The eSPI packet is assembled by the HW block.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | op | Enum representing opcode for peripheral type and read request. |
    | data | Parameter to be read from to the LPC peripheral. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | if eSPI peripheral is off or not supported. |
    | -EINVAL | for unimplemented lpc opcode, but in range. |

## [◆ ](#ga112f7554ba614c8e5f239b1319b4a763)espi\_read\_request()

| int espi\_read\_request | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_request\_packet](structespi__request__packet.md) \* | *req* ) |

`#include <[espi.h](espi_8h.md)>`

Sends memory, I/O or message read request over eSPI.

This routines provides a generic interface to send a read request packet.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | req | Address of structure representing a memory, I/O or message read request. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | if eSPI controller doesn't support raw packets and instead low memory transactions are handled by controller hardware directly. |
    | -EIO | General input / output error, failed to send over the bus. |

## [◆ ](#ga4b8f4fbf66a2b2ae394e00b16500f70d)espi\_receive\_oob()

| int espi\_receive\_oob | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_oob\_packet](structespi__oob__packet.md) \* | *pckt* ) |

`#include <[espi.h](espi_8h.md)>`

Receives SMBus transaction (out-of-band) packet from eSPI bus.

This routines provides an interface to receive and decoded a SMBus transaction from eSPI bus

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pckt | Address of the packet representation of SMBus transaction. |

Return values
:   | -EIO | General input / output error, failed request to controller. |
    | --- | --- |

## [◆ ](#gaa8bb48b5592c4b49d27c9b8a42432410)espi\_receive\_vwire()

| int espi\_receive\_vwire | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [espi\_vwire\_signal](#gab65a0951a8912d9de398cfec0aef7d35) | *signal*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *level* ) |

`#include <[espi.h](espi_8h.md)>`

Retrieves level status for a signal encapsulated in a virtual wire.

This routines provides a generic interface to request a virtual wire packet from eSPI controller and retrieve the signal level.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | signal | the signal to be requested from eSPI controller. |
    | level | the level of signal requested 0b LOW, 1b HIGH. |

Return values
:   | -EIO | General input / output error, failed request to controller. |
    | --- | --- |

## [◆ ](#ga7f04f98ea6a4671b821cf6ddf6bbf2a6)espi\_remove\_callback()

| | int espi\_remove\_callback | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct espi\_callback \* | *callback* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[espi.h](espi_8h.md)>`

Remove an application callback.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | callback | A valid application's callback structure pointer. |

Returns
:   0 if successful, negative errno code on failure.

Warning
:   It is explicitly permitted, within a callback handler, to remove the registration for the callback that is running, i.e. `callback`. Attempts to remove other registrations on the same device may result in undefined behavior, including failure to invoke callbacks that remain registered and unintended invocation of removed callbacks.

Note: enables to remove as many callbacks as added through [espi\_add\_callback()](#gabf5f0ea01ec8ed5345b2e119181c2313).

## [◆ ](#gaafe30738c18a16b056ed8dcf8638eb84)espi\_saf\_activate()

| int espi\_saf\_activate | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[espi_saf.h](espi__saf_8h.md)>`

Activate SAF block.

This routine activates the SAF block and should only be called after SAF has been configured and the eSPI Master has enabled the Flash Channel.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -EINVAL | if failed to activate SAF. |

## [◆ ](#gadb881f847082f713bb0159d1e474980a)espi\_saf\_add\_callback()

| | int espi\_saf\_add\_callback | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct espi\_callback \* | *callback* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[espi_saf.h](espi__saf_8h.md)>`

Add an application callback.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | callback | A valid Application's callback structure pointer. |

Returns
:   0 if successful, negative errno code on failure.

Note
:   Callbacks may be added to the device from within a callback handler invocation, but whether they are invoked for the current eSPI event is not specified.

Note: enables to add as many callback as needed on the same device.

## [◆ ](#ga34b0f6336aec45016d97528767b09434)espi\_saf\_config()

| int espi\_saf\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [espi\_saf\_cfg](structespi__saf__cfg.md) \* | *cfg* ) |

`#include <[espi_saf.h](espi__saf_8h.md)>`

Configure operation of a eSPI controller.

This routine provides a generic interface to override eSPI controller capabilities.

If this eSPI controller is acting as slave, the values set here will be discovered as part through the GET\_CONFIGURATION command issued by the eSPI master during initialization.

If this eSPI controller is acting as master, the values set here will be used by eSPI master to determine minimum common capabilities with eSPI slave then send via SET\_CONFIGURATION command.

+--------+ +---------+ +------+ +---------+ +---------+

| eSPI | | eSPI | | eSPI | | eSPI | | eSPI |

| slave | | driver | | bus | | driver | | host |

+--------+ +---------+ +------+ +---------+ +---------+

| | | | |

| [espi\_config](#ga7227c53d384eb0dc666361261f069f68) | Set eSPI | Set eSPI | [espi\_config](#ga7227c53d384eb0dc666361261f069f68) |

+--------------+ ctrl regs | cap ctrl reg| +-----------+

| +-------+ | +--------+ |

| |<------+ | +------->| |

| | | | |

| | | | |

| | | GET\_CONFIGURATION | |

| | +<------------------+ |

| |<-----------| | |

| | eSPI caps | | |

| |----------->+ response | |

| | |------------------>+ |

| | | | |

| | | SET\_CONFIGURATION | |

| | +<------------------+ |

| | | [accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb) | |

| | +------------------>+ |

+ + + + +

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | cfg | the device runtime configuration for the eSPI controller. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error, failed to configure device. |
    | -EINVAL | invalid capabilities, failed to configure device. |
    | -ENOTSUP | capability not supported by eSPI slave. |

## [◆ ](#ga15855a2ac593b97dc1a3e83ac9eda300)espi\_saf\_flash\_erase()

| int espi\_saf\_flash\_erase | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_saf\_packet](structespi__saf__packet.md) \* | *pckt* ) |

`#include <[espi_saf.h](espi__saf_8h.md)>`

Sends a write request packet for slave attached flash.

This routines provides an interface to send a request to write to the flash components shared between the eSPI master and eSPI slaves.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pckt | Address of the representation of erase flash transaction. |

Return values
:   | -ENOTSUP | eSPI flash logical channel transactions not supported. |
    | --- | --- |
    | -EBUSY | eSPI flash channel is not ready or disabled by master. |
    | -EIO | General input / output error, failed request to master. |

## [◆ ](#ga0f5017eac05f928e635fec8e5f877c7d)espi\_saf\_flash\_read()

| int espi\_saf\_flash\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_saf\_packet](structespi__saf__packet.md) \* | *pckt* ) |

`#include <[espi_saf.h](espi__saf_8h.md)>`

Sends a read request packet for slave attached flash.

This routines provides an interface to send a request to read the flash component shared between the eSPI master and eSPI slaves.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pckt | Address of the representation of read flash transaction. |

Return values
:   | -ENOTSUP | eSPI flash logical channel transactions not supported. |
    | --- | --- |
    | -EBUSY | eSPI flash channel is not ready or disabled by master. |
    | -EIO | General input / output error, failed request to master. |

## [◆ ](#ga6c54d9274b1a8e883484bd892f606fd5)espi\_saf\_flash\_unsuccess()

| int espi\_saf\_flash\_unsuccess | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_saf\_packet](structespi__saf__packet.md) \* | *pckt* ) |

`#include <[espi_saf.h](espi__saf_8h.md)>`

Response unsuccessful completion for slave attached flash.

This routines provides an interface to response that transaction is invalid and return unsuccessful completion from target to controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pckt | Address of the representation of flash transaction. |

Return values
:   | -ENOTSUP | eSPI flash logical channel transactions not supported. |
    | --- | --- |
    | -EBUSY | eSPI flash channel is not ready or disabled by master. |
    | -EIO | General input / output error, failed request to master. |

## [◆ ](#ga104175f74019e58b8b7901f3dae245db)espi\_saf\_flash\_write()

| int espi\_saf\_flash\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_saf\_packet](structespi__saf__packet.md) \* | *pckt* ) |

`#include <[espi_saf.h](espi__saf_8h.md)>`

Sends a write request packet for slave attached flash.

This routines provides an interface to send a request to write to the flash components shared between the eSPI master and eSPI slaves.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pckt | Address of the representation of write flash transaction. |

Return values
:   | -ENOTSUP | eSPI flash logical channel transactions not supported. |
    | --- | --- |
    | -EBUSY | eSPI flash channel is not ready or disabled by master. |
    | -EIO | General input / output error, failed request to master. |

## [◆ ](#ga8b53a93559f0c67953e283f59107aa22)espi\_saf\_get\_channel\_status()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) espi\_saf\_get\_channel\_status | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[espi_saf.h](espi__saf_8h.md)>`

Query to see if SAF is ready.

This routine allows to check if SAF is ready before use.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If eSPI SAF is ready. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | otherwise. |

## [◆ ](#ga324283c28e6a33be112571621d1568e8)espi\_saf\_init\_callback()

| | void espi\_saf\_init\_callback | ( | struct espi\_callback \* | *callback*, | | --- | --- | --- | --- | |  |  | [espi\_callback\_handler\_t](#ga9d848c7e367cf277230f365f73c15c46) | *handler*, | |  |  | enum [espi\_bus\_event](#ga36ac3fbf9813f78bad90f047e1eb1128) | *evt\_type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[espi_saf.h](espi__saf_8h.md)>`

Callback model.

+-------+ +-------------+ +------+ +---------+

| App | | eSPI driver | | HW | |eSPI Host|

+---+---+ +-------+-----+ +---+--+ +----+----+

| | | |

| [espi\_init\_callback](#ga8d88e4e3893d610713195e5352ec2565) | | |

+----------------------------> | | |

| [espi\_add\_callback](#gabf5f0ea01ec8ed5345b2e119181c2313) | |

+----------------------------->+ |

| | | eSPI reset | eSPI host

| | IRQ +<------------+ resets the

| | <-----------+ | bus

| | | |

| | Processed | |

| | within the | |

| | driver | |

| | | |

| | | VW CH ready| eSPI host

| | IRQ +<------------+ enables VW

| | <-----------+ | channel

| | | |

| | Processed | |

| | within the | |

| | driver | |

| | | |

| | | Memory I/O | Peripheral

| | <-------------+ event

| +<------------+ |

+<-----------------------------+ callback | |

| Report peripheral event | | |

| and data for the event | | |

| | | |

| | | SLP\_S5 | eSPI host

| | <-------------+ [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d) VWire

| +<------------+ |

+<-----------------------------+ callback | |

| App enables/configures | | |

| discrete regulator | | |

| | | |

| espi\_send\_vwire\_signal | | |

+------------------------------>------------>|------------>|

| | | |

| | | HOST\_RST | eSPI host

| | <-------------+ [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d) VWire

| +<------------+ |

+<-----------------------------+ callback | |

| App reset host-related | | |

| data structures | | |

| | | |

| | | C10 | eSPI host

| | +<------------+ [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d) VWire

| <-------------+ |

<------------------------------+ | |

| App executes | | |

+ power mgmt policy | | |

Helper to initialize a struct espi\_callback properly.

Parameters
:   | callback | A valid Application's callback structure pointer. |
    | --- | --- |
    | handler | A valid handler function pointer. |
    | evt\_type | indicates the eSPI event relevant for the handler. for VWIRE\_RECEIVED event the data will indicate the new level asserted |

## [◆ ](#gaf987842bc7dad310c7270aed50086af9)espi\_saf\_remove\_callback()

| | int espi\_saf\_remove\_callback | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct espi\_callback \* | *callback* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[espi_saf.h](espi__saf_8h.md)>`

Remove an application callback.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | callback | A valid application's callback structure pointer. |

Returns
:   0 if successful, negative errno code on failure.

Warning
:   It is explicitly permitted, within a callback handler, to remove the registration for the callback that is running, i.e. `callback`. Attempts to remove other registrations on the same device may result in undefined behavior, including failure to invoke callbacks that remain registered and unintended invocation of removed callbacks.

Note: enables to remove as many callbacks as added through [espi\_add\_callback()](#gabf5f0ea01ec8ed5345b2e119181c2313).

## [◆ ](#ga273a9707f3ca501ed2dd3019cdeaa363)espi\_saf\_set\_protection\_regions()

| int espi\_saf\_set\_protection\_regions | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct espi\_saf\_protection \* | *pr* ) |

`#include <[espi_saf.h](espi__saf_8h.md)>`

Set one or more SAF protection regions.

This routine provides an interface to override the default flash protection regions of the SAF controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pr | Pointer to the SAF protection region structure. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error, failed to configure device. |
    | -EINVAL | invalid capabilities, failed to configure device. |
    | -ENOTSUP | capability not supported by eSPI slave. |

## [◆ ](#ga2557cfc7a38f669d14e9826e3fb0fdee)espi\_send\_oob()

| int espi\_send\_oob | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_oob\_packet](structespi__oob__packet.md) \* | *pckt* ) |

`#include <[espi.h](espi_8h.md)>`

Sends SMBus transaction (out-of-band) packet over eSPI bus.

This routines provides an interface to encapsulate a SMBus transaction and send into packet over eSPI bus

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pckt | Address of the packet representation of SMBus transaction. |

Return values
:   | -EIO | General input / output error, failed request to controller. |
    | --- | --- |

## [◆ ](#gacab2b3bff7d940e71ee1c2a9fdedf782)espi\_send\_vwire()

| int espi\_send\_vwire | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [espi\_vwire\_signal](#gab65a0951a8912d9de398cfec0aef7d35) | *signal*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *level* ) |

`#include <[espi.h](espi_8h.md)>`

Sends system/platform signal as a virtual wire packet.

This routines provides a generic interface to send a virtual wire packet from target to controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | signal | The signal to be send to eSPI controller. |
    | level | The level of signal requested LOW or HIGH. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error, failed to send over the bus. |

## [◆ ](#gab02d46fd690e33875cc1b2433c976891)espi\_write\_flash()

| int espi\_write\_flash | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_flash\_packet](structespi__flash__packet.md) \* | *pckt* ) |

`#include <[espi.h](espi_8h.md)>`

Sends a write request packet for shared flash.

This routines provides an interface to send a request to write to the flash components shared between the eSPI controller and eSPI targets.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pckt | Address of the representation of write flash transaction. |

Return values
:   | -ENOTSUP | eSPI flash logical channel transactions not supported. |
    | --- | --- |
    | -EBUSY | eSPI flash channel is not ready or disabled by controller. |
    | -EIO | General input / output error, failed request to controller. |

## [◆ ](#ga880b6b04824f9f0deea10e8018573b88)espi\_write\_lpc\_request()

| int espi\_write\_lpc\_request | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [lpc\_peripheral\_opcode](#gad00b6a22843e5df9c6d6945d0d82310e) | *op*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *data* ) |

`#include <[espi.h](espi_8h.md)>`

Writes data to a LPC peripheral which generates an eSPI transaction.

This routine provides a generic interface to write data to a block which triggers an eSPI transaction. The eSPI packet is assembled by the HW block.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | op | Enum representing an opcode for peripheral type and write request. |
    | data | Represents the parameter passed to the LPC peripheral. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | if eSPI peripheral is off or not supported. |
    | -EINVAL | for unimplemented lpc opcode, but in range. |

## [◆ ](#ga143ed88b1f220f9582c809165fd983fd)espi\_write\_request()

| int espi\_write\_request | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_request\_packet](structespi__request__packet.md) \* | *req* ) |

`#include <[espi.h](espi_8h.md)>`

Sends memory, I/O or message write request over eSPI.

This routines provides a generic interface to send a write request packet.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | req | Address of structure representing a memory, I/O or message write request. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | if eSPI controller doesn't support raw packets and instead low memory transactions are handled by controller hardware directly. |
    | -EINVAL | General input / output error, failed to send over the bus. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
