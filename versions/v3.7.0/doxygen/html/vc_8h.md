---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/vc_8h.html
original_path: doxygen/html/vc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vc.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/drivers/pcie/pcie.h](drivers_2pcie_2pcie_8h_source.md)>`

[Go to the source code of this file.](vc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pcie\_vctc\_map](structpcie__vctc__map.md) |

| Macros | |
| --- | --- |
| #define | [PCIE\_VC\_MAX\_COUNT](group__pcie__vc__host__interface.md#ga0567fabc02828372f4e901bb193c9b89)   8U |
| #define | [PCIE\_VC\_SET\_TC0](group__pcie__vc__host__interface.md#gae1ec2ec11736ed97c6e41a2d8c7f4a39)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [PCIE\_VC\_SET\_TC1](group__pcie__vc__host__interface.md#gab4d53cac004ac7b6258fbd387fc90051)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [PCIE\_VC\_SET\_TC2](group__pcie__vc__host__interface.md#ga3d0311d99240527d86e8f8452f405736)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [PCIE\_VC\_SET\_TC3](group__pcie__vc__host__interface.md#ga3122990fd5879e076346efdc706b640e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [PCIE\_VC\_SET\_TC4](group__pcie__vc__host__interface.md#ga2259546ee27ce43dfb15ea69bdb66a7c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [PCIE\_VC\_SET\_TC5](group__pcie__vc__host__interface.md#ga9a796b9570585c60c70fb641e0a5a733)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [PCIE\_VC\_SET\_TC6](group__pcie__vc__host__interface.md#gaf8ff3086a4a5003f303f7b17e2319c09)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [PCIE\_VC\_SET\_TC7](group__pcie__vc__host__interface.md#gacbd9b1877530539d1a14a35d35744634)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |

| Functions | |
| --- | --- |
| int | [pcie\_vc\_enable](group__pcie__vc__host__interface.md#ga179628024fc9d651d1027833377ee9d2) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Enable PCIe Virtual Channel handling. |
| int | [pcie\_vc\_disable](group__pcie__vc__host__interface.md#ga89c684f7ff5e82da86df27d061a8fbd7) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Disable PCIe Virtual Channel handling. |
| int | [pcie\_vc\_map\_tc](group__pcie__vc__host__interface.md#gafd4429e8c14821c685c4103f34b340c8) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, struct [pcie\_vctc\_map](structpcie__vctc__map.md) \*map) |
|  | Map PCIe TC/VC. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [vc.h](vc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
