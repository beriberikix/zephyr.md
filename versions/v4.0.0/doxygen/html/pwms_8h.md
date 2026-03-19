---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pwms_8h.html
original_path: doxygen/html/pwms_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pwms.h File Reference

PWMs Devicetree macro public API header file.
[More...](#details)

[Go to the source code of this file.](pwms_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_PWMS\_CTLR\_BY\_IDX](group__devicetree-pwms.md#ga2f16d00a53717a66668fb8bc967acce5)(node\_id, idx) |
|  | Get the node identifier for the PWM controller from a pwms property at an index. |
| #define | [DT\_PWMS\_CTLR\_BY\_NAME](group__devicetree-pwms.md#ga6922e69c707219cd766fe317484dac8a)(node\_id, name) |
|  | Get the node identifier for the PWM controller from a pwms property by name. |
| #define | [DT\_PWMS\_CTLR](group__devicetree-pwms.md#gaff7a0b201d97a1d1bb1893b556d5a194)(node\_id) |
|  | Equivalent to [DT\_PWMS\_CTLR\_BY\_IDX(node\_id, 0)](group__devicetree-pwms.md#ga2f16d00a53717a66668fb8bc967acce5 "Get the node identifier for the PWM controller from a pwms property at an index."). |
| #define | [DT\_PWMS\_CELL\_BY\_IDX](group__devicetree-pwms.md#ga0c1ab3329448f92936d57a83b5b3594e)(node\_id, idx, cell) |
|  | Get PWM specifier's cell value at an index. |
| #define | [DT\_PWMS\_CELL\_BY\_NAME](group__devicetree-pwms.md#ga69233198a489283068bc1ded5072ca26)(node\_id, name, cell) |
|  | Get a PWM specifier's cell value by name. |
| #define | [DT\_PWMS\_CELL](group__devicetree-pwms.md#ga2062b31a090c05ccd267ae1468b182ef)(node\_id, cell) |
|  | Equivalent to [DT\_PWMS\_CELL\_BY\_IDX(node\_id, 0, cell)](group__devicetree-pwms.md#ga0c1ab3329448f92936d57a83b5b3594e "Get PWM specifier's cell value at an index."). |
| #define | [DT\_PWMS\_CHANNEL\_BY\_IDX](group__devicetree-pwms.md#ga10a372e44c7e3feb551ca996c6ca5a8f)(node\_id, idx) |
|  | Get a PWM specifier's channel cell value at an index. |
| #define | [DT\_PWMS\_CHANNEL\_BY\_NAME](group__devicetree-pwms.md#ga59a4b9884e9620eac04c3808a3a6d164)(node\_id, name) |
|  | Get a PWM specifier's channel cell value by name. |
| #define | [DT\_PWMS\_CHANNEL](group__devicetree-pwms.md#gaeb0a10ad37fdfd3dcc75bd379908acdc)(node\_id) |
|  | Equivalent to [DT\_PWMS\_CHANNEL\_BY\_IDX(node\_id, 0)](group__devicetree-pwms.md#ga10a372e44c7e3feb551ca996c6ca5a8f "Get a PWM specifier's channel cell value at an index."). |
| #define | [DT\_PWMS\_PERIOD\_BY\_IDX](group__devicetree-pwms.md#ga9456f65777e6fc7c057c6e0709c9245f)(node\_id, idx) |
|  | Get PWM specifier's period cell value at an index. |
| #define | [DT\_PWMS\_PERIOD\_BY\_NAME](group__devicetree-pwms.md#ga74af83d31fc38f331808dedfaecf4c74)(node\_id, name) |
|  | Get a PWM specifier's period cell value by name. |
| #define | [DT\_PWMS\_PERIOD](group__devicetree-pwms.md#gac6006a723932325b96a1b50619be153b)(node\_id) |
|  | Equivalent to [DT\_PWMS\_PERIOD\_BY\_IDX(node\_id, 0)](group__devicetree-pwms.md#ga9456f65777e6fc7c057c6e0709c9245f "Get PWM specifier's period cell value at an index."). |
| #define | [DT\_PWMS\_FLAGS\_BY\_IDX](group__devicetree-pwms.md#gaf9c1ac7f3a39f4022f3ec31ef8de98e6)(node\_id, idx) |
|  | Get a PWM specifier's flags cell value at an index. |
| #define | [DT\_PWMS\_FLAGS\_BY\_NAME](group__devicetree-pwms.md#ga7a1621bfb223da23aa030b64fc0c0bcd)(node\_id, name) |
|  | Get a PWM specifier's flags cell value by name. |
| #define | [DT\_PWMS\_FLAGS](group__devicetree-pwms.md#ga8dcd2d18129504d1a4ab71ae05c48c44)(node\_id) |
|  | Equivalent to [DT\_PWMS\_FLAGS\_BY\_IDX(node\_id, 0)](group__devicetree-pwms.md#gaf9c1ac7f3a39f4022f3ec31ef8de98e6 "Get a PWM specifier's flags cell value at an index."). |
| #define | [DT\_INST\_PWMS\_CTLR\_BY\_IDX](group__devicetree-pwms.md#ga4f751ba5f3c1aad5d62178b166f36c24)(inst, idx) |
|  | Get the node identifier for the PWM controller from a DT\_DRV\_COMPAT instance's pwms property at an index. |
| #define | [DT\_INST\_PWMS\_CTLR\_BY\_NAME](group__devicetree-pwms.md#gae66d3e710496bff9789996ddb72e1ebe)(inst, name) |
|  | Get the node identifier for the PWM controller from a DT\_DRV\_COMPAT instance's pwms property by name. |
| #define | [DT\_INST\_PWMS\_CTLR](group__devicetree-pwms.md#ga2f79a0a48e08c89bac58d16d9731e683)(inst) |
|  | Equivalent to [DT\_INST\_PWMS\_CTLR\_BY\_IDX(inst, 0)](group__devicetree-pwms.md#ga4f751ba5f3c1aad5d62178b166f36c24 "Get the node identifier for the PWM controller from a DT_DRV_COMPAT instance's pwms property at an in..."). |
| #define | [DT\_INST\_PWMS\_CELL\_BY\_IDX](group__devicetree-pwms.md#gad106bf22d9dc90384519cd6ccc8fd1c6)(inst, idx, cell) |
|  | Get a DT\_DRV\_COMPAT instance's PWM specifier's cell value at an index. |
| #define | [DT\_INST\_PWMS\_CELL\_BY\_NAME](group__devicetree-pwms.md#ga5731d949be09461f5da040e451cc509c)(inst, name, cell) |
|  | Get a DT\_DRV\_COMPAT instance's PWM specifier's cell value by name. |
| #define | [DT\_INST\_PWMS\_CELL](group__devicetree-pwms.md#ga199804a2d06c301f19c5c8de232ede15)(inst, cell) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, 0, cell)](group__devicetree-pwms.md#gad106bf22d9dc90384519cd6ccc8fd1c6 "Get a DT_DRV_COMPAT instance's PWM specifier's cell value at an index."). |
| #define | [DT\_INST\_PWMS\_CHANNEL\_BY\_IDX](group__devicetree-pwms.md#ga154ece84d782a7df2ce31b2a34f43870)(inst, idx) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, channel)](group__devicetree-pwms.md#gad106bf22d9dc90384519cd6ccc8fd1c6 "Get a DT_DRV_COMPAT instance's PWM specifier's cell value at an index."). |
| #define | [DT\_INST\_PWMS\_CHANNEL\_BY\_NAME](group__devicetree-pwms.md#ga60901952d81e29dbfbbe88ee3ffe3e17)(inst, name) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, channel)](group__devicetree-pwms.md#ga5731d949be09461f5da040e451cc509c "Get a DT_DRV_COMPAT instance's PWM specifier's cell value by name."). |
| #define | [DT\_INST\_PWMS\_CHANNEL](group__devicetree-pwms.md#gad871b89fd1b2d62aae84dc35a0819032)(inst) |
|  | Equivalent to [DT\_INST\_PWMS\_CHANNEL\_BY\_IDX(inst, 0)](group__devicetree-pwms.md#ga154ece84d782a7df2ce31b2a34f43870 "Equivalent to DT_INST_PWMS_CELL_BY_IDX(inst, idx, channel)."). |
| #define | [DT\_INST\_PWMS\_PERIOD\_BY\_IDX](group__devicetree-pwms.md#ga7e7408507ecdac75cb7c9ba2b9176ec8)(inst, idx) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, period)](group__devicetree-pwms.md#gad106bf22d9dc90384519cd6ccc8fd1c6 "Get a DT_DRV_COMPAT instance's PWM specifier's cell value at an index."). |
| #define | [DT\_INST\_PWMS\_PERIOD\_BY\_NAME](group__devicetree-pwms.md#ga7ac719270232e67f91bc65e3786be1a1)(inst, name) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, period)](group__devicetree-pwms.md#ga5731d949be09461f5da040e451cc509c "Get a DT_DRV_COMPAT instance's PWM specifier's cell value by name."). |
| #define | [DT\_INST\_PWMS\_PERIOD](group__devicetree-pwms.md#ga2b122199764cff41c04bad243f4456dc)(inst) |
|  | Equivalent to [DT\_INST\_PWMS\_PERIOD\_BY\_IDX(inst, 0)](group__devicetree-pwms.md#ga7e7408507ecdac75cb7c9ba2b9176ec8 "Equivalent to DT_INST_PWMS_CELL_BY_IDX(inst, idx, period)."). |
| #define | [DT\_INST\_PWMS\_FLAGS\_BY\_IDX](group__devicetree-pwms.md#ga9cfbc4e3c0ab9d419cfb7700a5b42ced)(inst, idx) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, flags)](group__devicetree-pwms.md#gad106bf22d9dc90384519cd6ccc8fd1c6 "Get a DT_DRV_COMPAT instance's PWM specifier's cell value at an index."). |
| #define | [DT\_INST\_PWMS\_FLAGS\_BY\_NAME](group__devicetree-pwms.md#ga23a8815368cbd82a8673e00abdfeab6b)(inst, name) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, flags)](group__devicetree-pwms.md#ga5731d949be09461f5da040e451cc509c "Get a DT_DRV_COMPAT instance's PWM specifier's cell value by name."). |
| #define | [DT\_INST\_PWMS\_FLAGS](group__devicetree-pwms.md#ga5ca45d33eae6b50012e8c052e3bd5df0)(inst) |
|  | Equivalent to [DT\_INST\_PWMS\_FLAGS\_BY\_IDX(inst, 0)](group__devicetree-pwms.md#ga9cfbc4e3c0ab9d419cfb7700a5b42ced "Equivalent to DT_INST_PWMS_CELL_BY_IDX(inst, idx, flags)."). |

## Detailed Description

PWMs Devicetree macro public API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [pwms.h](pwms_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
