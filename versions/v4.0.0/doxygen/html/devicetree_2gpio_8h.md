---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/devicetree_2gpio_8h.html
original_path: doxygen/html/devicetree_2gpio_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio.h File Reference

GPIO Devicetree macro public API header file.
[More...](#details)

[Go to the source code of this file.](devicetree_2gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_GPIO\_CTLR\_BY\_IDX](group__devicetree-gpio.md#ga97bd46d2ab88d392a3f336f4d23184eb)(node\_id, gpio\_pha, idx) |
|  | Get the node identifier for the controller phandle from a gpio phandle-array property at an index. |
| #define | [DT\_GPIO\_CTLR](group__devicetree-gpio.md#gafbad7d0d7f7fb9338997482c8da0e566)(node\_id, gpio\_pha) |
|  | Equivalent to [DT\_GPIO\_CTLR\_BY\_IDX(node\_id, gpio\_pha, 0)](group__devicetree-gpio.md#ga97bd46d2ab88d392a3f336f4d23184eb "Get the node identifier for the controller phandle from a gpio phandle-array property at an index."). |
| #define | [DT\_GPIO\_PIN\_BY\_IDX](group__devicetree-gpio.md#ga8f7d82567056266bab1603865f8b27af)(node\_id, gpio\_pha, idx) |
|  | Get a GPIO specifier's pin cell at an index. |
| #define | [DT\_GPIO\_PIN](group__devicetree-gpio.md#ga4e41ec30ece058555333811a9fcee333)(node\_id, gpio\_pha) |
|  | Equivalent to [DT\_GPIO\_PIN\_BY\_IDX(node\_id, gpio\_pha, 0)](group__devicetree-gpio.md#ga8f7d82567056266bab1603865f8b27af "Get a GPIO specifier's pin cell at an index."). |
| #define | [DT\_GPIO\_FLAGS\_BY\_IDX](group__devicetree-gpio.md#ga672b2597b99194b8cbd42b3f3401d2b5)(node\_id, gpio\_pha, idx) |
|  | Get a GPIO specifier's flags cell at an index. |
| #define | [DT\_GPIO\_FLAGS](group__devicetree-gpio.md#ga32b3383d7ed543602a7b4a031018316f)(node\_id, gpio\_pha) |
|  | Equivalent to [DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, gpio\_pha, 0)](group__devicetree-gpio.md#ga672b2597b99194b8cbd42b3f3401d2b5 "Get a GPIO specifier's flags cell at an index."). |
| #define | [DT\_NUM\_GPIO\_HOGS](group__devicetree-gpio.md#ga0a4575c3750db76692fd0f817a169b50)(node\_id) |
|  | Get the number of GPIO hogs in a node. |
| #define | [DT\_GPIO\_HOG\_PIN\_BY\_IDX](group__devicetree-gpio.md#gaf4ecdebbd433473f654f4b6859542af9)(node\_id, idx) |
|  | Get a GPIO hog specifier's pin cell at an index. |
| #define | [DT\_GPIO\_HOG\_FLAGS\_BY\_IDX](group__devicetree-gpio.md#gaed024e6acac49f591fe50cd43e8af14f)(node\_id, idx) |
|  | Get a GPIO hog specifier's flags cell at an index. |
| #define | [DT\_INST\_GPIO\_PIN\_BY\_IDX](group__devicetree-gpio.md#ga162bca126f7015816286358f09bde6ff)(inst, gpio\_pha, idx) |
|  | Get a DT\_DRV\_COMPAT instance's GPIO specifier's pin cell value at an index. |
| #define | [DT\_INST\_GPIO\_PIN](group__devicetree-gpio.md#ga5ee13b3de1d4cecc877963dfa8820cfd)(inst, gpio\_pha) |
|  | Equivalent to [DT\_INST\_GPIO\_PIN\_BY\_IDX(inst, gpio\_pha, 0)](group__devicetree-gpio.md#ga162bca126f7015816286358f09bde6ff "Get a DT_DRV_COMPAT instance's GPIO specifier's pin cell value at an index."). |
| #define | [DT\_INST\_GPIO\_FLAGS\_BY\_IDX](group__devicetree-gpio.md#gafd40d1eec5c1672b7675ae47388c1cef)(inst, gpio\_pha, idx) |
|  | Get a DT\_DRV\_COMPAT instance's GPIO specifier's flags cell at an index. |
| #define | [DT\_INST\_GPIO\_FLAGS](group__devicetree-gpio.md#ga8d3edd53d6d8e89afc68f0c10176f57f)(inst, gpio\_pha) |
|  | Equivalent to [DT\_INST\_GPIO\_FLAGS\_BY\_IDX(inst, gpio\_pha, 0)](group__devicetree-gpio.md#gafd40d1eec5c1672b7675ae47388c1cef "Get a DT_DRV_COMPAT instance's GPIO specifier's flags cell at an index."). |

## Detailed Description

GPIO Devicetree macro public API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [gpio.h](devicetree_2gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
