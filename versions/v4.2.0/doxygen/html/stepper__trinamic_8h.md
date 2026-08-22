---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stepper__trinamic_8h.html
original_path: doxygen/html/stepper__trinamic_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stepper\_trinamic.h File Reference

Public API for Trinamic Stepper Controller Specific Functions.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/drivers/stepper.h](stepper_8h_source.md)>`

[Go to the source code of this file.](stepper__trinamic_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md) |
|  | Trinamic Stepper Ramp Generator data. [More...](structtmc__ramp__generator__data.md#details) |

| Macros | |
| --- | --- |
| #define | [TMC\_RAMP\_VSTART\_MAX](group__trinamic__stepper__interface.md#ga9e9a9e371a79b153226645383867f57c)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(17, 0) |
|  | Trinamic stepper controller ramp generator data limits. |
| #define | [TMC\_RAMP\_VSTART\_MIN](group__trinamic__stepper__interface.md#ga7569a6172df37f1e669eed75a1acb5d5)   0 |
| #define | [TMC\_RAMP\_V1\_MAX](group__trinamic__stepper__interface.md#ga9530d64f9c331681b33230fcc8ef7512)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| #define | [TMC\_RAMP\_V1\_MIN](group__trinamic__stepper__interface.md#ga6f07fdd1e99eff62f93d28b7c2527283)   0 |
| #define | [TMC\_RAMP\_VMAX\_MAX](group__trinamic__stepper__interface.md#ga6bd3a7d1578f4d9729327cdc9bcb2214)   ([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) - 512) |
| #define | [TMC\_RAMP\_VMAX\_MIN](group__trinamic__stepper__interface.md#ga42fe12c7afa3411279df79323b6005ff)   0 |
| #define | [TMC\_RAMP\_A1\_MAX](group__trinamic__stepper__interface.md#ga2043631a9382df69c0cddf69e57845ba)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| #define | [TMC\_RAMP\_A1\_MIN](group__trinamic__stepper__interface.md#gae93384303a1aa78ecee86df6749449a1)   0 |
| #define | [TMC\_RAMP\_AMAX\_MAX](group__trinamic__stepper__interface.md#gac4ae29a8dee3c5f30afd9ad879eb841f)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| #define | [TMC\_RAMP\_AMAX\_MIN](group__trinamic__stepper__interface.md#ga50e4297381755484bbddf9976f1d51f5)   0 |
| #define | [TMC\_RAMP\_D1\_MAX](group__trinamic__stepper__interface.md#ga9ae3e36281fbf1a83e3c6cf71ef2441f)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| #define | [TMC\_RAMP\_D1\_MIN](group__trinamic__stepper__interface.md#ga9d825b4269d204eaded8b0559114a8ac)   1 |
| #define | [TMC\_RAMP\_DMAX\_MAX](group__trinamic__stepper__interface.md#ga80d3cbcb6455cbafd36c677e292622c4)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| #define | [TMC\_RAMP\_DMAX\_MIN](group__trinamic__stepper__interface.md#gaed3825c79b588840c355fd1d3da9d3bb)   0 |
| #define | [TMC\_RAMP\_VSTOP\_MAX](group__trinamic__stepper__interface.md#ga7b121c433e4bf33da2a5f14ec53bf627)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(17, 0) |
| #define | [TMC\_RAMP\_VSTOP\_MIN](group__trinamic__stepper__interface.md#gada43f70cfca38bd5bb3208474c92f276)   1 |
| #define | [TMC\_RAMP\_TZEROWAIT\_MAX](group__trinamic__stepper__interface.md#ga0bb50350111fb8a7dc22dae9948690f6)   ([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) - 512) |
| #define | [TMC\_RAMP\_TZEROWAIT\_MIN](group__trinamic__stepper__interface.md#ga509b5bb88d3976323f90cd9647af97b1)   0 |
| #define | [TMC\_RAMP\_IHOLD\_IRUN\_MAX](group__trinamic__stepper__interface.md#gaeab2e7683232b2f77c6e57602af268e1)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 0) |
| #define | [TMC\_RAMP\_IHOLD\_IRUN\_MIN](group__trinamic__stepper__interface.md#ga732705b9ea5208d16caabfd36f9b0ea8)   0 |
| #define | [TMC\_RAMP\_IHOLDDELAY\_MAX](group__trinamic__stepper__interface.md#ga5cdbd0068d00533a8cf6d952be8c943e)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| #define | [TMC\_RAMP\_IHOLDDELAY\_MIN](group__trinamic__stepper__interface.md#ga7b787ce2fffd9e689230a4abf2070bf2)   0 |
| #define | [TMC\_RAMP\_VACTUAL\_SHIFT](group__trinamic__stepper__interface.md#ga3aee23f87376c760f43d714df646ad54)   22 |
| #define | [TMC\_RAMP\_XACTUAL\_SHIFT](group__trinamic__stepper__interface.md#ga5e6d87a484aa64da36d05321f12c92a5)   31 |
| #define | [TMC\_RAMP\_VCOOLTHRS\_MAX](group__trinamic__stepper__interface.md#gabbdadfe7e2dac7851c1bd5b6c5dd4a42)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) |
| #define | [TMC\_RAMP\_VCOOLTHRS\_MIN](group__trinamic__stepper__interface.md#ga37a395c0056c9b20520cace7ba925014)   0 |
| #define | [TMC\_RAMP\_VHIGH\_MAX](group__trinamic__stepper__interface.md#ga4134f638119d89b559118028a65fd5c7)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) |
| #define | [TMC\_RAMP\_VHIGH\_MIN](group__trinamic__stepper__interface.md#ga7d87a071f418cecd2f80a1a1403ff2c5)   0 |
| #define | [TMC\_RAMP\_TPOWERDOWN\_MAX](group__trinamic__stepper__interface.md#ga686fee8768ba3821f67e533067b4b165)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| #define | [TMC\_RAMP\_TPOWERDOWN\_MIN](group__trinamic__stepper__interface.md#ga03f09f2a3a8b1ee37a7abf49baaeab0a)   0 |
| #define | [TMC\_RAMP\_TPWMTHRS\_MAX](group__trinamic__stepper__interface.md#gad06256f808f37c879533254468f3920c)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| #define | [TMC\_RAMP\_TPWMTHRS\_MIN](group__trinamic__stepper__interface.md#gacd563e95d901c133624fc24678a88040)   0 |
| #define | [TMC\_RAMP\_TCOOLTHRS\_MAX](group__trinamic__stepper__interface.md#gaf43cc157aa2842cfbf5577d8b98c3d4c)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| #define | [TMC\_RAMP\_TCOOLTHRS\_MIN](group__trinamic__stepper__interface.md#ga0dc9a4f1d7e83849220b62175855548b)   0 |
| #define | [TMC\_RAMP\_THIGH\_MAX](group__trinamic__stepper__interface.md#ga74c583adc60323a2753b82425a9dd745)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| #define | [TMC\_RAMP\_THIGH\_MIN](group__trinamic__stepper__interface.md#gaa3a1c83e852bf2e020eb793f495eee23)   0 |
| #define | [CHECK\_RAMP\_DT\_DATA](group__trinamic__stepper__interface.md#ga2066d314a74cbcb47934b7c9b0067791)(node) |
|  | Check if Ramp DT data is within limits. |
| #define | [TMC\_RAMP\_DT\_SPEC\_GET\_COMMON](group__trinamic__stepper__interface.md#ga05fe4dd5a148d23cd1240d3e3534726c)(node) |
|  | Get Trinamic Stepper Ramp Generator data from DT. |
| #define | [TMC\_RAMP\_DT\_SPEC\_GET\_TMC50XX](group__trinamic__stepper__interface.md#ga485a07aa34b72643ef77203d6e7c0de2)(node) |
| #define | [TMC\_RAMP\_DT\_SPEC\_GET\_TMC51XX](group__trinamic__stepper__interface.md#ga92c5a6a95451f15cc5b5712ac2e50ad7)(node) |

| Functions | |
| --- | --- |
| int | [tmc50xx\_stepper\_set\_ramp](group__trinamic__stepper__interface.md#ga9c186c3a7e094dce76ace821abcc9e86) (const struct [device](structdevice.md) \*dev, const struct [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md) \*ramp\_data) |
|  | Configure Trinamic Stepper Ramp Generator. |
| int | [tmc50xx\_stepper\_set\_max\_velocity](group__trinamic__stepper__interface.md#gac2c7168e3618951b65df3257553260f6) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) velocity) |
|  | Set the maximum velocity of the stepper motor. |

## Detailed Description

Public API for Trinamic Stepper Controller Specific Functions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper](dir_975614d18b9dbb5293fe20c1ce7c38bb.md)
- [stepper\_trinamic.h](stepper__trinamic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
