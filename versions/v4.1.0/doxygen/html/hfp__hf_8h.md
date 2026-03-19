---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hfp__hf_8h.html
original_path: doxygen/html/hfp__hf_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hfp\_hf.h File Reference

Handsfree Profile handling.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

[Go to the source code of this file.](hfp__hf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_hfp\_hf\_cmd\_complete](structbt__hfp__hf__cmd__complete.md) |
|  | HFP HF Command completion field. [More...](structbt__hfp__hf__cmd__complete.md#details) |
| struct | [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) |
|  | HFP profile application callback. [More...](structbt__hfp__hf__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [HFP\_HF\_CMD\_OK](group__bt__hfp.md#ga7c90e2ab7ed6c5b25252f88408235598)   0 |
| #define | [HFP\_HF\_CMD\_ERROR](group__bt__hfp.md#ga463b8eb680e7cbedfbf9c5e5628558af)   1 |
| #define | [HFP\_HF\_CMD\_CME\_ERROR](group__bt__hfp.md#ga80133496d4868f11381d14fe46cfdb51)   2 |
| #define | [HFP\_HF\_CMD\_UNKNOWN\_ERROR](group__bt__hfp.md#ga613fa4c3e102c7ab20e587f34c14d5c6)   4 |

| Enumerations | |
| --- | --- |
| enum | [bt\_hfp\_hf\_at\_cmd](group__bt__hfp.md#gae88edd233a1f00e6d12be7fe3ac8c9fd) { [BT\_HFP\_HF\_ATA](group__bt__hfp.md#ggae88edd233a1f00e6d12be7fe3ac8c9fdae80220d66b99e9f0954fa9491565f641) , [BT\_HFP\_HF\_AT\_CHUP](group__bt__hfp.md#ggae88edd233a1f00e6d12be7fe3ac8c9fdaa777f4b5e3b8310e528e535ca0667a18) } |

| Functions | |
| --- | --- |
| int | [bt\_hfp\_hf\_register](group__bt__hfp.md#ga2e4a7c05a3ba9a32eab50b9904f7f161) (struct [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) \*cb) |
|  | Register HFP HF profile. |
| int | [bt\_hfp\_hf\_send\_cmd](group__bt__hfp.md#ga88f700df453cfca14926afb1db9c70d0) (struct bt\_conn \*conn, enum [bt\_hfp\_hf\_at\_cmd](group__bt__hfp.md#gae88edd233a1f00e6d12be7fe3ac8c9fd) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Handsfree client Send AT. |

## Detailed Description

Handsfree Profile handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [hfp\_hf.h](hfp__hf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
