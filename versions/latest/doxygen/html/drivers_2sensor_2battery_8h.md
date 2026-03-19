---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2sensor_2battery_8h.html
original_path: doxygen/html/drivers_2sensor_2battery_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

battery.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/math/interpolation.h](interpolation_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](drivers_2sensor_2battery_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BATTERY\_OCV\_TABLE\_LEN](group__battery__apis.md#ga02de0e4f76b8e5804b82cd397c13ef86)   11 |
| #define | [BATTERY\_CHEMISTRY\_DT\_GET](group__battery__apis.md#gae2c365581f7c8c71e1ec31b223545711)(node\_id) |
|  | Get the battery chemistry enum value. |
| #define | [BATTERY\_OCV\_TABLE\_DT\_GET](group__battery__apis.md#ga833bf8bf88136fd277a69fb41ad0fb7f)(node\_id, table) |
|  | Get the OCV curve for a given table. |

| Enumerations | |
| --- | --- |
| enum | [battery\_chemistry](group__battery__apis.md#gaf7ee6b6e85da9f31231cac577428de01) {     [BATTERY\_CHEMISTRY\_UNKNOWN](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a52bae762c2ef4ca140c1e7f89440b007) = 0 , [BATTERY\_CHEMISTRY\_NICKEL\_CADMIUM](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a00f07b177e6246e139b469386064698f) , [BATTERY\_CHEMISTRY\_NICKEL\_METAL\_HYDRIDE](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a377834c71930068b6a822d4afd2112f4) , [BATTERY\_CHEMISTRY\_LITHIUM\_ION](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a450162d694da85864af48712cb05badd) ,     [BATTERY\_CHEMISTRY\_LITHIUM\_ION\_POLYMER](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01ab21f5e769426047924d83e5301b8a19f) , [BATTERY\_CHEMISTRY\_LITHIUM\_ION\_IRON\_PHOSPHATE](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a951b3bea1c503ce6f1d78e8cc1ed9e37) , [BATTERY\_CHEMISTRY\_LITHIUM\_ION\_MANGANESE\_OXIDE](group__battery__apis.md#ggaf7ee6b6e85da9f31231cac577428de01a30cd5d02bb416248b9380ab953836e96)   } |

| Functions | |
| --- | --- |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [battery\_soc\_lookup](group__battery__apis.md#gaea81fb0c63b85654005b6f65521c3345) (const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ocv\_table[11], [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) voltage\_uv) |
|  | Convert an OCV table and battery voltage to a charge percentage. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [battery.h](drivers_2sensor_2battery_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
