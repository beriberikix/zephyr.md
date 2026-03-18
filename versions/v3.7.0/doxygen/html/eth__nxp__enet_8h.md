---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/eth__nxp__enet_8h.html
original_path: doxygen/html/eth__nxp__enet_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eth\_nxp\_enet.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](eth__nxp__enet_8h_source.md)

| Macros | |
| --- | --- |
| #define | [nxp\_enet\_ptp\_clock\_callback](#ad11ef7c9660268acaccf3f39d662149a)(...) |

| Enumerations | |
| --- | --- |
| enum | [nxp\_enet\_callback\_reason](#a91a8c6d4a482c50577ed686748f84a47) { [NXP\_ENET\_MODULE\_RESET](#a91a8c6d4a482c50577ed686748f84a47a019cb78bbe3a2ff74bd1ab1cbedb5ccd) , [NXP\_ENET\_INTERRUPT](#a91a8c6d4a482c50577ed686748f84a47ae355aed11d966069b2a77717fd1a46a9) , [NXP\_ENET\_INTERRUPT\_ENABLED](#a91a8c6d4a482c50577ed686748f84a47affa6c7124f8f9a0e3eda750287c05d18) } |
| enum | [nxp\_enet\_driver](#ae3c6272946ff0e510271158ff1ab4416) { [NXP\_ENET\_MAC](#ae3c6272946ff0e510271158ff1ab4416af008b300d92db2371541464d6c577178) , [NXP\_ENET\_MDIO](#ae3c6272946ff0e510271158ff1ab4416ac29234a2e347018f80a71078df4538a1) , [NXP\_ENET\_PTP\_CLOCK](#ae3c6272946ff0e510271158ff1ab4416aa09c872026c5287cd6ae55847dcf4ebc) } |

| Functions | |
| --- | --- |
| void | [nxp\_enet\_mdio\_callback](#a5dd34e9d1bbe8e695995e647656cf564) (const struct [device](structdevice.md) \*mdio\_dev, enum [nxp\_enet\_callback\_reason](#a91a8c6d4a482c50577ed686748f84a47) event, void \*data) |
| void | [nxp\_enet\_driver\_cb](#aa1876fb8edfa98cdb8f9f92abc48a572) (const struct [device](structdevice.md) \*dev, enum [nxp\_enet\_driver](#ae3c6272946ff0e510271158ff1ab4416) dev\_type, enum [nxp\_enet\_callback\_reason](#a91a8c6d4a482c50577ed686748f84a47) event, void \*data) |

## Macro Definition Documentation

## [◆ ](#ad11ef7c9660268acaccf3f39d662149a)nxp\_enet\_ptp\_clock\_callback

| #define nxp\_enet\_ptp\_clock\_callback | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

## Enumeration Type Documentation

## [◆ ](#a91a8c6d4a482c50577ed686748f84a47)nxp\_enet\_callback\_reason

| enum [nxp\_enet\_callback\_reason](#a91a8c6d4a482c50577ed686748f84a47) |
| --- |

| Enumerator | |
| --- | --- |
| NXP\_ENET\_MODULE\_RESET |  |
| NXP\_ENET\_INTERRUPT |  |
| NXP\_ENET\_INTERRUPT\_ENABLED |  |

## [◆ ](#ae3c6272946ff0e510271158ff1ab4416)nxp\_enet\_driver

| enum [nxp\_enet\_driver](#ae3c6272946ff0e510271158ff1ab4416) |
| --- |

| Enumerator | |
| --- | --- |
| NXP\_ENET\_MAC |  |
| NXP\_ENET\_MDIO |  |
| NXP\_ENET\_PTP\_CLOCK |  |

## Function Documentation

## [◆ ](#aa1876fb8edfa98cdb8f9f92abc48a572)nxp\_enet\_driver\_cb()

| | void nxp\_enet\_driver\_cb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [nxp\_enet\_driver](#ae3c6272946ff0e510271158ff1ab4416) | *dev\_type*, | |  |  | enum [nxp\_enet\_callback\_reason](#a91a8c6d4a482c50577ed686748f84a47) | *event*, | |  |  | void \* | *data* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5dd34e9d1bbe8e695995e647656cf564)nxp\_enet\_mdio\_callback()

| | void nxp\_enet\_mdio\_callback | ( | const struct [device](structdevice.md) \* | *mdio\_dev*, | | --- | --- | --- | --- | |  |  | enum [nxp\_enet\_callback\_reason](#a91a8c6d4a482c50577ed686748f84a47) | *event*, | |  |  | void \* | *data* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ethernet](dir_e26e025f1b2d5c43527f6232564fe44e.md)
- [eth\_nxp\_enet.h](eth__nxp__enet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
