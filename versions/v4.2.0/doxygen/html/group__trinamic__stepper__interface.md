---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__trinamic__stepper__interface.html
original_path: doxygen/html/group__trinamic__stepper__interface.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Trinamic Stepper Controller Interface

[Device Driver APIs](group__io__interfaces.md) » [Stepper Driver Interface](group__stepper__interface.md)

Trinamic Stepper Controller Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md) |
|  | Trinamic Stepper Ramp Generator data. [More...](structtmc__ramp__generator__data.md#details) |

| Macros | |
| --- | --- |
| #define | [TMC\_RAMP\_VSTART\_MAX](#ga9e9a9e371a79b153226645383867f57c)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(17, 0) |
|  | Trinamic stepper controller ramp generator data limits. |
| #define | [TMC\_RAMP\_VSTART\_MIN](#ga7569a6172df37f1e669eed75a1acb5d5)   0 |
| #define | [TMC\_RAMP\_V1\_MAX](#ga9530d64f9c331681b33230fcc8ef7512)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| #define | [TMC\_RAMP\_V1\_MIN](#ga6f07fdd1e99eff62f93d28b7c2527283)   0 |
| #define | [TMC\_RAMP\_VMAX\_MAX](#ga6bd3a7d1578f4d9729327cdc9bcb2214)   ([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) - 512) |
| #define | [TMC\_RAMP\_VMAX\_MIN](#ga42fe12c7afa3411279df79323b6005ff)   0 |
| #define | [TMC\_RAMP\_A1\_MAX](#ga2043631a9382df69c0cddf69e57845ba)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| #define | [TMC\_RAMP\_A1\_MIN](#gae93384303a1aa78ecee86df6749449a1)   0 |
| #define | [TMC\_RAMP\_AMAX\_MAX](#gac4ae29a8dee3c5f30afd9ad879eb841f)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| #define | [TMC\_RAMP\_AMAX\_MIN](#ga50e4297381755484bbddf9976f1d51f5)   0 |
| #define | [TMC\_RAMP\_D1\_MAX](#ga9ae3e36281fbf1a83e3c6cf71ef2441f)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| #define | [TMC\_RAMP\_D1\_MIN](#ga9d825b4269d204eaded8b0559114a8ac)   1 |
| #define | [TMC\_RAMP\_DMAX\_MAX](#ga80d3cbcb6455cbafd36c677e292622c4)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| #define | [TMC\_RAMP\_DMAX\_MIN](#gaed3825c79b588840c355fd1d3da9d3bb)   0 |
| #define | [TMC\_RAMP\_VSTOP\_MAX](#ga7b121c433e4bf33da2a5f14ec53bf627)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(17, 0) |
| #define | [TMC\_RAMP\_VSTOP\_MIN](#gada43f70cfca38bd5bb3208474c92f276)   1 |
| #define | [TMC\_RAMP\_TZEROWAIT\_MAX](#ga0bb50350111fb8a7dc22dae9948690f6)   ([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) - 512) |
| #define | [TMC\_RAMP\_TZEROWAIT\_MIN](#ga509b5bb88d3976323f90cd9647af97b1)   0 |
| #define | [TMC\_RAMP\_IHOLD\_IRUN\_MAX](#gaeab2e7683232b2f77c6e57602af268e1)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 0) |
| #define | [TMC\_RAMP\_IHOLD\_IRUN\_MIN](#ga732705b9ea5208d16caabfd36f9b0ea8)   0 |
| #define | [TMC\_RAMP\_IHOLDDELAY\_MAX](#ga5cdbd0068d00533a8cf6d952be8c943e)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| #define | [TMC\_RAMP\_IHOLDDELAY\_MIN](#ga7b787ce2fffd9e689230a4abf2070bf2)   0 |
| #define | [TMC\_RAMP\_VACTUAL\_SHIFT](#ga3aee23f87376c760f43d714df646ad54)   22 |
| #define | [TMC\_RAMP\_XACTUAL\_SHIFT](#ga5e6d87a484aa64da36d05321f12c92a5)   31 |
| #define | [TMC\_RAMP\_VCOOLTHRS\_MAX](#gabbdadfe7e2dac7851c1bd5b6c5dd4a42)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) |
| #define | [TMC\_RAMP\_VCOOLTHRS\_MIN](#ga37a395c0056c9b20520cace7ba925014)   0 |
| #define | [TMC\_RAMP\_VHIGH\_MAX](#ga4134f638119d89b559118028a65fd5c7)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) |
| #define | [TMC\_RAMP\_VHIGH\_MIN](#ga7d87a071f418cecd2f80a1a1403ff2c5)   0 |
| #define | [TMC\_RAMP\_TPOWERDOWN\_MAX](#ga686fee8768ba3821f67e533067b4b165)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| #define | [TMC\_RAMP\_TPOWERDOWN\_MIN](#ga03f09f2a3a8b1ee37a7abf49baaeab0a)   0 |
| #define | [TMC\_RAMP\_TPWMTHRS\_MAX](#gad06256f808f37c879533254468f3920c)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| #define | [TMC\_RAMP\_TPWMTHRS\_MIN](#gacd563e95d901c133624fc24678a88040)   0 |
| #define | [TMC\_RAMP\_TCOOLTHRS\_MAX](#gaf43cc157aa2842cfbf5577d8b98c3d4c)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| #define | [TMC\_RAMP\_TCOOLTHRS\_MIN](#ga0dc9a4f1d7e83849220b62175855548b)   0 |
| #define | [TMC\_RAMP\_THIGH\_MAX](#ga74c583adc60323a2753b82425a9dd745)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| #define | [TMC\_RAMP\_THIGH\_MIN](#gaa3a1c83e852bf2e020eb793f495eee23)   0 |
| #define | [CHECK\_RAMP\_DT\_DATA](#ga2066d314a74cbcb47934b7c9b0067791)(node) |
|  | Check if Ramp DT data is within limits. |
| #define | [TMC\_RAMP\_DT\_SPEC\_GET\_COMMON](#ga05fe4dd5a148d23cd1240d3e3534726c)(node) |
|  | Get Trinamic Stepper Ramp Generator data from DT. |
| #define | [TMC\_RAMP\_DT\_SPEC\_GET\_TMC50XX](#ga485a07aa34b72643ef77203d6e7c0de2)(node) |
| #define | [TMC\_RAMP\_DT\_SPEC\_GET\_TMC51XX](#ga92c5a6a95451f15cc5b5712ac2e50ad7)(node) |

| Functions | |
| --- | --- |
| int | [tmc50xx\_stepper\_set\_ramp](#ga9c186c3a7e094dce76ace821abcc9e86) (const struct [device](structdevice.md) \*dev, const struct [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md) \*ramp\_data) |
|  | Configure Trinamic Stepper Ramp Generator. |
| int | [tmc50xx\_stepper\_set\_max\_velocity](#gac2c7168e3618951b65df3257553260f6) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) velocity) |
|  | Set the maximum velocity of the stepper motor. |

## Detailed Description

Trinamic Stepper Controller Interface.

## Macro Definition Documentation

## [◆ ](#ga2066d314a74cbcb47934b7c9b0067791)CHECK\_RAMP\_DT\_DATA

| #define CHECK\_RAMP\_DT\_DATA | ( |  | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(DT\_PROP\_EXISTS(node, vstart), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vstart), [TMC\_RAMP\_VSTART\_MIN](#ga7569a6172df37f1e669eed75a1acb5d5), \

[TMC\_RAMP\_VSTART\_MAX](#ga9e9a9e371a79b153226645383867f57c)), "vstart out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, v1), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, v1), [TMC\_RAMP\_V1\_MIN](#ga6f07fdd1e99eff62f93d28b7c2527283), \

[TMC\_RAMP\_V1\_MAX](#ga9530d64f9c331681b33230fcc8ef7512)), "v1 out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, vmax), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vmax), [TMC\_RAMP\_VMAX\_MIN](#ga42fe12c7afa3411279df79323b6005ff), \

[TMC\_RAMP\_VMAX\_MAX](#ga6bd3a7d1578f4d9729327cdc9bcb2214)), "vmax out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, a1), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, a1), [TMC\_RAMP\_A1\_MIN](#gae93384303a1aa78ecee86df6749449a1), \

[TMC\_RAMP\_A1\_MAX](#ga2043631a9382df69c0cddf69e57845ba)), "a1 out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, amax), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, amax), [TMC\_RAMP\_AMAX\_MIN](#ga50e4297381755484bbddf9976f1d51f5), \

[TMC\_RAMP\_AMAX\_MAX](#gac4ae29a8dee3c5f30afd9ad879eb841f)), "amax out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, d1), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, d1), [TMC\_RAMP\_D1\_MIN](#ga9d825b4269d204eaded8b0559114a8ac), \

[TMC\_RAMP\_D1\_MAX](#ga9ae3e36281fbf1a83e3c6cf71ef2441f)), "d1 out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, dmax), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, dmax), [TMC\_RAMP\_DMAX\_MIN](#gaed3825c79b588840c355fd1d3da9d3bb), \

[TMC\_RAMP\_DMAX\_MAX](#ga80d3cbcb6455cbafd36c677e292622c4)), "dmax out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, vstop), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vstop), [TMC\_RAMP\_VSTOP\_MIN](#gada43f70cfca38bd5bb3208474c92f276), \

[TMC\_RAMP\_VSTOP\_MAX](#ga7b121c433e4bf33da2a5f14ec53bf627)), "vstop out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, tzerowait), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, tzerowait), [TMC\_RAMP\_TZEROWAIT\_MIN](#ga509b5bb88d3976323f90cd9647af97b1), \

[TMC\_RAMP\_TZEROWAIT\_MAX](#ga0bb50350111fb8a7dc22dae9948690f6)), "tzerowait out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, ihold), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, ihold), [TMC\_RAMP\_IHOLD\_IRUN\_MIN](#ga732705b9ea5208d16caabfd36f9b0ea8), \

[TMC\_RAMP\_IHOLD\_IRUN\_MAX](#gaeab2e7683232b2f77c6e57602af268e1)), "ihold out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, irun), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, irun), [TMC\_RAMP\_IHOLD\_IRUN\_MIN](#ga732705b9ea5208d16caabfd36f9b0ea8), \

[TMC\_RAMP\_IHOLD\_IRUN\_MAX](#gaeab2e7683232b2f77c6e57602af268e1)), "irun out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, iholddelay), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, iholddelay), [TMC\_RAMP\_IHOLDDELAY\_MIN](#ga7b787ce2fffd9e689230a4abf2070bf2), \

[TMC\_RAMP\_IHOLDDELAY\_MAX](#ga5cdbd0068d00533a8cf6d952be8c943e)), "iholddelay out of range"), ());\

/\* TMC50XX specific \*/ \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, vcoolthrs), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vcoolthrs), [TMC\_RAMP\_VCOOLTHRS\_MIN](#ga37a395c0056c9b20520cace7ba925014), \

[TMC\_RAMP\_VCOOLTHRS\_MAX](#gabbdadfe7e2dac7851c1bd5b6c5dd4a42)), "vcoolthrs out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, vhigh), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vhigh), [TMC\_RAMP\_VHIGH\_MIN](#ga7d87a071f418cecd2f80a1a1403ff2c5), \

[TMC\_RAMP\_VHIGH\_MAX](#ga4134f638119d89b559118028a65fd5c7)), "vhigh out of range"), ()); \

/\* TMC51XX specific \*/ \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, tpowerdown), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, tpowerdown), [TMC\_RAMP\_TPOWERDOWN\_MIN](#ga03f09f2a3a8b1ee37a7abf49baaeab0a), \

[TMC\_RAMP\_TPOWERDOWN\_MAX](#ga686fee8768ba3821f67e533067b4b165)), "tpowerdown out of range"), ());\

COND\_CODE\_1(DT\_PROP\_EXISTS(node, tpwmthrs), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, tpwmthrs), [TMC\_RAMP\_TPWMTHRS\_MIN](#gacd563e95d901c133624fc24678a88040), \

[TMC\_RAMP\_TPWMTHRS\_MAX](#gad06256f808f37c879533254468f3920c)), "tpwmthrs out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, tcoolthrs), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, tcoolthrs), [TMC\_RAMP\_TCOOLTHRS\_MIN](#ga0dc9a4f1d7e83849220b62175855548b), \

[TMC\_RAMP\_TCOOLTHRS\_MAX](#gaf43cc157aa2842cfbf5577d8b98c3d4c)), "tcoolthrs out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, thigh), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, thigh), [TMC\_RAMP\_THIGH\_MIN](#gaa3a1c83e852bf2e020eb793f495eee23), \

[TMC\_RAMP\_THIGH\_MAX](#ga74c583adc60323a2753b82425a9dd745)), "thigh out of range"), ());

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

[IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)

#define IN\_RANGE(val, min, max)

Checks if a value is within range.

**Definition** util.h:433

[TMC\_RAMP\_TPOWERDOWN\_MIN](#ga03f09f2a3a8b1ee37a7abf49baaeab0a)

#define TMC\_RAMP\_TPOWERDOWN\_MIN

**Definition** stepper\_trinamic.h:68

[TMC\_RAMP\_TZEROWAIT\_MAX](#ga0bb50350111fb8a7dc22dae9948690f6)

#define TMC\_RAMP\_TZEROWAIT\_MAX

**Definition** stepper\_trinamic.h:51

[TMC\_RAMP\_TCOOLTHRS\_MIN](#ga0dc9a4f1d7e83849220b62175855548b)

#define TMC\_RAMP\_TCOOLTHRS\_MIN

**Definition** stepper\_trinamic.h:72

[TMC\_RAMP\_A1\_MAX](#ga2043631a9382df69c0cddf69e57845ba)

#define TMC\_RAMP\_A1\_MAX

**Definition** stepper\_trinamic.h:41

[TMC\_RAMP\_VCOOLTHRS\_MIN](#ga37a395c0056c9b20520cace7ba925014)

#define TMC\_RAMP\_VCOOLTHRS\_MIN

**Definition** stepper\_trinamic.h:62

[TMC\_RAMP\_VHIGH\_MAX](#ga4134f638119d89b559118028a65fd5c7)

#define TMC\_RAMP\_VHIGH\_MAX

**Definition** stepper\_trinamic.h:63

[TMC\_RAMP\_VMAX\_MIN](#ga42fe12c7afa3411279df79323b6005ff)

#define TMC\_RAMP\_VMAX\_MIN

**Definition** stepper\_trinamic.h:40

[TMC\_RAMP\_TZEROWAIT\_MIN](#ga509b5bb88d3976323f90cd9647af97b1)

#define TMC\_RAMP\_TZEROWAIT\_MIN

**Definition** stepper\_trinamic.h:52

[TMC\_RAMP\_AMAX\_MIN](#ga50e4297381755484bbddf9976f1d51f5)

#define TMC\_RAMP\_AMAX\_MIN

**Definition** stepper\_trinamic.h:44

[TMC\_RAMP\_IHOLDDELAY\_MAX](#ga5cdbd0068d00533a8cf6d952be8c943e)

#define TMC\_RAMP\_IHOLDDELAY\_MAX

**Definition** stepper\_trinamic.h:55

[TMC\_RAMP\_TPOWERDOWN\_MAX](#ga686fee8768ba3821f67e533067b4b165)

#define TMC\_RAMP\_TPOWERDOWN\_MAX

**Definition** stepper\_trinamic.h:67

[TMC\_RAMP\_VMAX\_MAX](#ga6bd3a7d1578f4d9729327cdc9bcb2214)

#define TMC\_RAMP\_VMAX\_MAX

**Definition** stepper\_trinamic.h:39

[TMC\_RAMP\_V1\_MIN](#ga6f07fdd1e99eff62f93d28b7c2527283)

#define TMC\_RAMP\_V1\_MIN

**Definition** stepper\_trinamic.h:38

[TMC\_RAMP\_IHOLD\_IRUN\_MIN](#ga732705b9ea5208d16caabfd36f9b0ea8)

#define TMC\_RAMP\_IHOLD\_IRUN\_MIN

**Definition** stepper\_trinamic.h:54

[TMC\_RAMP\_THIGH\_MAX](#ga74c583adc60323a2753b82425a9dd745)

#define TMC\_RAMP\_THIGH\_MAX

**Definition** stepper\_trinamic.h:73

[TMC\_RAMP\_VSTART\_MIN](#ga7569a6172df37f1e669eed75a1acb5d5)

#define TMC\_RAMP\_VSTART\_MIN

**Definition** stepper\_trinamic.h:36

[TMC\_RAMP\_VSTOP\_MAX](#ga7b121c433e4bf33da2a5f14ec53bf627)

#define TMC\_RAMP\_VSTOP\_MAX

**Definition** stepper\_trinamic.h:49

[TMC\_RAMP\_IHOLDDELAY\_MIN](#ga7b787ce2fffd9e689230a4abf2070bf2)

#define TMC\_RAMP\_IHOLDDELAY\_MIN

**Definition** stepper\_trinamic.h:56

[TMC\_RAMP\_VHIGH\_MIN](#ga7d87a071f418cecd2f80a1a1403ff2c5)

#define TMC\_RAMP\_VHIGH\_MIN

**Definition** stepper\_trinamic.h:64

[TMC\_RAMP\_DMAX\_MAX](#ga80d3cbcb6455cbafd36c677e292622c4)

#define TMC\_RAMP\_DMAX\_MAX

**Definition** stepper\_trinamic.h:47

[TMC\_RAMP\_V1\_MAX](#ga9530d64f9c331681b33230fcc8ef7512)

#define TMC\_RAMP\_V1\_MAX

**Definition** stepper\_trinamic.h:37

[TMC\_RAMP\_D1\_MAX](#ga9ae3e36281fbf1a83e3c6cf71ef2441f)

#define TMC\_RAMP\_D1\_MAX

**Definition** stepper\_trinamic.h:45

[TMC\_RAMP\_D1\_MIN](#ga9d825b4269d204eaded8b0559114a8ac)

#define TMC\_RAMP\_D1\_MIN

**Definition** stepper\_trinamic.h:46

[TMC\_RAMP\_VSTART\_MAX](#ga9e9a9e371a79b153226645383867f57c)

#define TMC\_RAMP\_VSTART\_MAX

Trinamic stepper controller ramp generator data limits.

**Definition** stepper\_trinamic.h:35

[TMC\_RAMP\_THIGH\_MIN](#gaa3a1c83e852bf2e020eb793f495eee23)

#define TMC\_RAMP\_THIGH\_MIN

**Definition** stepper\_trinamic.h:74

[TMC\_RAMP\_VCOOLTHRS\_MAX](#gabbdadfe7e2dac7851c1bd5b6c5dd4a42)

#define TMC\_RAMP\_VCOOLTHRS\_MAX

**Definition** stepper\_trinamic.h:61

[TMC\_RAMP\_AMAX\_MAX](#gac4ae29a8dee3c5f30afd9ad879eb841f)

#define TMC\_RAMP\_AMAX\_MAX

**Definition** stepper\_trinamic.h:43

[TMC\_RAMP\_TPWMTHRS\_MIN](#gacd563e95d901c133624fc24678a88040)

#define TMC\_RAMP\_TPWMTHRS\_MIN

**Definition** stepper\_trinamic.h:70

[TMC\_RAMP\_TPWMTHRS\_MAX](#gad06256f808f37c879533254468f3920c)

#define TMC\_RAMP\_TPWMTHRS\_MAX

**Definition** stepper\_trinamic.h:69

[TMC\_RAMP\_VSTOP\_MIN](#gada43f70cfca38bd5bb3208474c92f276)

#define TMC\_RAMP\_VSTOP\_MIN

**Definition** stepper\_trinamic.h:50

[TMC\_RAMP\_A1\_MIN](#gae93384303a1aa78ecee86df6749449a1)

#define TMC\_RAMP\_A1\_MIN

**Definition** stepper\_trinamic.h:42

[TMC\_RAMP\_IHOLD\_IRUN\_MAX](#gaeab2e7683232b2f77c6e57602af268e1)

#define TMC\_RAMP\_IHOLD\_IRUN\_MAX

**Definition** stepper\_trinamic.h:53

[TMC\_RAMP\_DMAX\_MIN](#gaed3825c79b588840c355fd1d3da9d3bb)

#define TMC\_RAMP\_DMAX\_MIN

**Definition** stepper\_trinamic.h:48

[TMC\_RAMP\_TCOOLTHRS\_MAX](#gaf43cc157aa2842cfbf5577d8b98c3d4c)

#define TMC\_RAMP\_TCOOLTHRS\_MAX

**Definition** stepper\_trinamic.h:71

Check if Ramp DT data is within limits.

## [◆ ](#ga2043631a9382df69c0cddf69e57845ba)TMC\_RAMP\_A1\_MAX

| #define TMC\_RAMP\_A1\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gae93384303a1aa78ecee86df6749449a1)TMC\_RAMP\_A1\_MIN

| #define TMC\_RAMP\_A1\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gac4ae29a8dee3c5f30afd9ad879eb841f)TMC\_RAMP\_AMAX\_MAX

| #define TMC\_RAMP\_AMAX\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga50e4297381755484bbddf9976f1d51f5)TMC\_RAMP\_AMAX\_MIN

| #define TMC\_RAMP\_AMAX\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga9ae3e36281fbf1a83e3c6cf71ef2441f)TMC\_RAMP\_D1\_MAX

| #define TMC\_RAMP\_D1\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga9d825b4269d204eaded8b0559114a8ac)TMC\_RAMP\_D1\_MIN

| #define TMC\_RAMP\_D1\_MIN   1 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga80d3cbcb6455cbafd36c677e292622c4)TMC\_RAMP\_DMAX\_MAX

| #define TMC\_RAMP\_DMAX\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gaed3825c79b588840c355fd1d3da9d3bb)TMC\_RAMP\_DMAX\_MIN

| #define TMC\_RAMP\_DMAX\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga05fe4dd5a148d23cd1240d3e3534726c)TMC\_RAMP\_DT\_SPEC\_GET\_COMMON

| #define TMC\_RAMP\_DT\_SPEC\_GET\_COMMON | ( |  | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

**Value:**

.vstart = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vstart), \

.v1 = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, v1), \

.vmax = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vmax), \

.a1 = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, a1), \

.amax = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, amax), \

.d1 = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, d1), \

.dmax = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, dmax), \

.vstop = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vstop), \

.tzerowait = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, tzerowait), \

.iholdrun = (TMC5XXX\_IRUN([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, irun)) | \

TMC5XXX\_IHOLD([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, ihold)) | \

TMC5XXX\_IHOLDDELAY([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, iholddelay))),

Get Trinamic Stepper Ramp Generator data from DT.

Parameters
:   | node | DT node identifier |
    | --- | --- |

Returns
:   struct [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md "Trinamic Stepper Ramp Generator data.")

## [◆ ](#ga485a07aa34b72643ef77203d6e7c0de2)TMC\_RAMP\_DT\_SPEC\_GET\_TMC50XX

| #define TMC\_RAMP\_DT\_SPEC\_GET\_TMC50XX | ( |  | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

**Value:**

{ \

TMC\_RAMP\_DT\_SPEC\_GET\_COMMON(node) \

.vhigh = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vhigh), \

.vcoolthrs = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vcoolthrs), \

}

## [◆ ](#ga92c5a6a95451f15cc5b5712ac2e50ad7)TMC\_RAMP\_DT\_SPEC\_GET\_TMC51XX

| #define TMC\_RAMP\_DT\_SPEC\_GET\_TMC51XX | ( |  | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

**Value:**

{ \

TMC\_RAMP\_DT\_SPEC\_GET\_COMMON([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(node)) \

.tpowerdown = [DT\_INST\_PROP](group__devicetree-inst.md#ga9dce2e631b2a94804e8f2bcc76c6eff8)(node, tpowerdown), \

.tpwmthrs = [DT\_INST\_PROP](group__devicetree-inst.md#ga9dce2e631b2a94804e8f2bcc76c6eff8)(node, tpwmthrs), \

.tcoolthrs = [DT\_INST\_PROP](group__devicetree-inst.md#ga9dce2e631b2a94804e8f2bcc76c6eff8)(node, tcoolthrs), \

.thigh = [DT\_INST\_PROP](group__devicetree-inst.md#ga9dce2e631b2a94804e8f2bcc76c6eff8)(node, thigh), \

}

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

[DT\_INST\_PROP](group__devicetree-inst.md#ga9dce2e631b2a94804e8f2bcc76c6eff8)

#define DT\_INST\_PROP(inst, prop)

Get a DT\_DRV\_COMPAT instance property.

**Definition** devicetree.h:4187

## [◆ ](#gaeab2e7683232b2f77c6e57602af268e1)TMC\_RAMP\_IHOLD\_IRUN\_MAX

| #define TMC\_RAMP\_IHOLD\_IRUN\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga732705b9ea5208d16caabfd36f9b0ea8)TMC\_RAMP\_IHOLD\_IRUN\_MIN

| #define TMC\_RAMP\_IHOLD\_IRUN\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga5cdbd0068d00533a8cf6d952be8c943e)TMC\_RAMP\_IHOLDDELAY\_MAX

| #define TMC\_RAMP\_IHOLDDELAY\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga7b787ce2fffd9e689230a4abf2070bf2)TMC\_RAMP\_IHOLDDELAY\_MIN

| #define TMC\_RAMP\_IHOLDDELAY\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gaf43cc157aa2842cfbf5577d8b98c3d4c)TMC\_RAMP\_TCOOLTHRS\_MAX

| #define TMC\_RAMP\_TCOOLTHRS\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga0dc9a4f1d7e83849220b62175855548b)TMC\_RAMP\_TCOOLTHRS\_MIN

| #define TMC\_RAMP\_TCOOLTHRS\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga74c583adc60323a2753b82425a9dd745)TMC\_RAMP\_THIGH\_MAX

| #define TMC\_RAMP\_THIGH\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gaa3a1c83e852bf2e020eb793f495eee23)TMC\_RAMP\_THIGH\_MIN

| #define TMC\_RAMP\_THIGH\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga686fee8768ba3821f67e533067b4b165)TMC\_RAMP\_TPOWERDOWN\_MAX

| #define TMC\_RAMP\_TPOWERDOWN\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga03f09f2a3a8b1ee37a7abf49baaeab0a)TMC\_RAMP\_TPOWERDOWN\_MIN

| #define TMC\_RAMP\_TPOWERDOWN\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gad06256f808f37c879533254468f3920c)TMC\_RAMP\_TPWMTHRS\_MAX

| #define TMC\_RAMP\_TPWMTHRS\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gacd563e95d901c133624fc24678a88040)TMC\_RAMP\_TPWMTHRS\_MIN

| #define TMC\_RAMP\_TPWMTHRS\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga0bb50350111fb8a7dc22dae9948690f6)TMC\_RAMP\_TZEROWAIT\_MAX

| #define TMC\_RAMP\_TZEROWAIT\_MAX   ([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) - 512) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga509b5bb88d3976323f90cd9647af97b1)TMC\_RAMP\_TZEROWAIT\_MIN

| #define TMC\_RAMP\_TZEROWAIT\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga9530d64f9c331681b33230fcc8ef7512)TMC\_RAMP\_V1\_MAX

| #define TMC\_RAMP\_V1\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga6f07fdd1e99eff62f93d28b7c2527283)TMC\_RAMP\_V1\_MIN

| #define TMC\_RAMP\_V1\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga3aee23f87376c760f43d714df646ad54)TMC\_RAMP\_VACTUAL\_SHIFT

| #define TMC\_RAMP\_VACTUAL\_SHIFT   22 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gabbdadfe7e2dac7851c1bd5b6c5dd4a42)TMC\_RAMP\_VCOOLTHRS\_MAX

| #define TMC\_RAMP\_VCOOLTHRS\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga37a395c0056c9b20520cace7ba925014)TMC\_RAMP\_VCOOLTHRS\_MIN

| #define TMC\_RAMP\_VCOOLTHRS\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga4134f638119d89b559118028a65fd5c7)TMC\_RAMP\_VHIGH\_MAX

| #define TMC\_RAMP\_VHIGH\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga7d87a071f418cecd2f80a1a1403ff2c5)TMC\_RAMP\_VHIGH\_MIN

| #define TMC\_RAMP\_VHIGH\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga6bd3a7d1578f4d9729327cdc9bcb2214)TMC\_RAMP\_VMAX\_MAX

| #define TMC\_RAMP\_VMAX\_MAX   ([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) - 512) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga42fe12c7afa3411279df79323b6005ff)TMC\_RAMP\_VMAX\_MIN

| #define TMC\_RAMP\_VMAX\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga9e9a9e371a79b153226645383867f57c)TMC\_RAMP\_VSTART\_MAX

| #define TMC\_RAMP\_VSTART\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(17, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

Trinamic stepper controller ramp generator data limits.

## [◆ ](#ga7569a6172df37f1e669eed75a1acb5d5)TMC\_RAMP\_VSTART\_MIN

| #define TMC\_RAMP\_VSTART\_MIN   0 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga7b121c433e4bf33da2a5f14ec53bf627)TMC\_RAMP\_VSTOP\_MAX

| #define TMC\_RAMP\_VSTOP\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(17, 0) |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gada43f70cfca38bd5bb3208474c92f276)TMC\_RAMP\_VSTOP\_MIN

| #define TMC\_RAMP\_VSTOP\_MIN   1 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga5e6d87a484aa64da36d05321f12c92a5)TMC\_RAMP\_XACTUAL\_SHIFT

| #define TMC\_RAMP\_XACTUAL\_SHIFT   31 |
| --- |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

## Function Documentation

## [◆ ](#gac2c7168e3618951b65df3257553260f6)tmc50xx\_stepper\_set\_max\_velocity()

| int tmc50xx\_stepper\_set\_max\_velocity | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *velocity* ) |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

Set the maximum velocity of the stepper motor.

Parameters
:   | dev | Pointer to the stepper motor controller instance |
    | --- | --- |
    | velocity | Maximum velocity in microsteps per second. |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | 0 | Success |

## [◆ ](#ga9c186c3a7e094dce76ace821abcc9e86)tmc50xx\_stepper\_set\_ramp()

| int tmc50xx\_stepper\_set\_ramp | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md) \* | *ramp\_data* ) |

`#include <[zephyr/drivers/stepper/stepper_trinamic.h](stepper__trinamic_8h.md)>`

Configure Trinamic Stepper Ramp Generator.

Parameters
:   | dev | Pointer to the stepper motor controller instance |
    | --- | --- |
    | ramp\_data | Pointer to a struct containing the required ramp parameters |

Return values
:   | -EIO | General input / output error |
    | --- | --- |
    | -ENOSYS | If not implemented by device driver |
    | 0 | Success |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
