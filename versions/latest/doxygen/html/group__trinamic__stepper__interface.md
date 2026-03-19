---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__trinamic__stepper__interface.html
original_path: doxygen/html/group__trinamic__stepper__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| #define | [TMC\_RAMP\_VCOOLTHRS\_MAX](#gabbdadfe7e2dac7851c1bd5b6c5dd4a42)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) |
| #define | [TMC\_RAMP\_VCOOLTHRS\_MIN](#ga37a395c0056c9b20520cace7ba925014)   0 |
| #define | [TMC\_RAMP\_VHIGH\_MAX](#ga4134f638119d89b559118028a65fd5c7)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) |
| #define | [TMC\_RAMP\_VHIGH\_MIN](#ga7d87a071f418cecd2f80a1a1403ff2c5)   0 |
| #define | [TMC\_RAMP\_IHOLD\_IRUN\_MAX](#gaeab2e7683232b2f77c6e57602af268e1)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 0) |
| #define | [TMC\_RAMP\_IHOLD\_IRUN\_MIN](#ga732705b9ea5208d16caabfd36f9b0ea8)   0 |
| #define | [TMC\_RAMP\_IHOLDDELAY\_MAX](#ga5cdbd0068d00533a8cf6d952be8c943e)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| #define | [TMC\_RAMP\_IHOLDDELAY\_MIN](#ga7b787ce2fffd9e689230a4abf2070bf2)   0 |
| #define | [TMC\_RAMP\_VACTUAL\_SHIFT](#ga3aee23f87376c760f43d714df646ad54)   22 |
| #define | [CHECK\_RAMP\_DT\_DATA](#ga2066d314a74cbcb47934b7c9b0067791)(node) |
|  | Check if Ramp DT data is within limits. |
| #define | [TMC\_RAMP\_DT\_SPEC\_GET](#gab5e5f7c14b896b580051f8b72afb529d)(node) |
|  | Get Trinamic Stepper Ramp Generator data from DT. |

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

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

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

COND\_CODE\_1(DT\_PROP\_EXISTS(node, vcoolthrs), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vcoolthrs), [TMC\_RAMP\_VCOOLTHRS\_MIN](#ga37a395c0056c9b20520cace7ba925014), \

[TMC\_RAMP\_VCOOLTHRS\_MAX](#gabbdadfe7e2dac7851c1bd5b6c5dd4a42)), "vcoolthrs out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, vhigh), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vhigh), [TMC\_RAMP\_VHIGH\_MIN](#ga7d87a071f418cecd2f80a1a1403ff2c5), \

[TMC\_RAMP\_VHIGH\_MAX](#ga4134f638119d89b559118028a65fd5c7)), "vhigh out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, ihold), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, ihold), [TMC\_RAMP\_IHOLD\_IRUN\_MIN](#ga732705b9ea5208d16caabfd36f9b0ea8), \

[TMC\_RAMP\_IHOLD\_IRUN\_MAX](#gaeab2e7683232b2f77c6e57602af268e1)), "ihold out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, irun), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, irun), [TMC\_RAMP\_IHOLD\_IRUN\_MIN](#ga732705b9ea5208d16caabfd36f9b0ea8), \

[TMC\_RAMP\_IHOLD\_IRUN\_MAX](#gaeab2e7683232b2f77c6e57602af268e1)), "irun out of range"), ()); \

COND\_CODE\_1(DT\_PROP\_EXISTS(node, iholddelay), \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, iholddelay), [TMC\_RAMP\_IHOLDDELAY\_MIN](#ga7b787ce2fffd9e689230a4abf2070bf2), \

[TMC\_RAMP\_IHOLDDELAY\_MAX](#ga5cdbd0068d00533a8cf6d952be8c943e)), "iholddelay out of range"), ());

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

**Definition** util.h:432

[TMC\_RAMP\_TZEROWAIT\_MAX](#ga0bb50350111fb8a7dc22dae9948690f6)

#define TMC\_RAMP\_TZEROWAIT\_MAX

**Definition** stepper\_trinamic.h:50

[TMC\_RAMP\_A1\_MAX](#ga2043631a9382df69c0cddf69e57845ba)

#define TMC\_RAMP\_A1\_MAX

**Definition** stepper\_trinamic.h:40

[TMC\_RAMP\_VCOOLTHRS\_MIN](#ga37a395c0056c9b20520cace7ba925014)

#define TMC\_RAMP\_VCOOLTHRS\_MIN

**Definition** stepper\_trinamic.h:53

[TMC\_RAMP\_VHIGH\_MAX](#ga4134f638119d89b559118028a65fd5c7)

#define TMC\_RAMP\_VHIGH\_MAX

**Definition** stepper\_trinamic.h:54

[TMC\_RAMP\_VMAX\_MIN](#ga42fe12c7afa3411279df79323b6005ff)

#define TMC\_RAMP\_VMAX\_MIN

**Definition** stepper\_trinamic.h:39

[TMC\_RAMP\_TZEROWAIT\_MIN](#ga509b5bb88d3976323f90cd9647af97b1)

#define TMC\_RAMP\_TZEROWAIT\_MIN

**Definition** stepper\_trinamic.h:51

[TMC\_RAMP\_AMAX\_MIN](#ga50e4297381755484bbddf9976f1d51f5)

#define TMC\_RAMP\_AMAX\_MIN

**Definition** stepper\_trinamic.h:43

[TMC\_RAMP\_IHOLDDELAY\_MAX](#ga5cdbd0068d00533a8cf6d952be8c943e)

#define TMC\_RAMP\_IHOLDDELAY\_MAX

**Definition** stepper\_trinamic.h:58

[TMC\_RAMP\_VMAX\_MAX](#ga6bd3a7d1578f4d9729327cdc9bcb2214)

#define TMC\_RAMP\_VMAX\_MAX

**Definition** stepper\_trinamic.h:38

[TMC\_RAMP\_V1\_MIN](#ga6f07fdd1e99eff62f93d28b7c2527283)

#define TMC\_RAMP\_V1\_MIN

**Definition** stepper\_trinamic.h:37

[TMC\_RAMP\_IHOLD\_IRUN\_MIN](#ga732705b9ea5208d16caabfd36f9b0ea8)

#define TMC\_RAMP\_IHOLD\_IRUN\_MIN

**Definition** stepper\_trinamic.h:57

[TMC\_RAMP\_VSTART\_MIN](#ga7569a6172df37f1e669eed75a1acb5d5)

#define TMC\_RAMP\_VSTART\_MIN

**Definition** stepper\_trinamic.h:35

[TMC\_RAMP\_VSTOP\_MAX](#ga7b121c433e4bf33da2a5f14ec53bf627)

#define TMC\_RAMP\_VSTOP\_MAX

**Definition** stepper\_trinamic.h:48

[TMC\_RAMP\_IHOLDDELAY\_MIN](#ga7b787ce2fffd9e689230a4abf2070bf2)

#define TMC\_RAMP\_IHOLDDELAY\_MIN

**Definition** stepper\_trinamic.h:59

[TMC\_RAMP\_VHIGH\_MIN](#ga7d87a071f418cecd2f80a1a1403ff2c5)

#define TMC\_RAMP\_VHIGH\_MIN

**Definition** stepper\_trinamic.h:55

[TMC\_RAMP\_DMAX\_MAX](#ga80d3cbcb6455cbafd36c677e292622c4)

#define TMC\_RAMP\_DMAX\_MAX

**Definition** stepper\_trinamic.h:46

[TMC\_RAMP\_V1\_MAX](#ga9530d64f9c331681b33230fcc8ef7512)

#define TMC\_RAMP\_V1\_MAX

**Definition** stepper\_trinamic.h:36

[TMC\_RAMP\_D1\_MAX](#ga9ae3e36281fbf1a83e3c6cf71ef2441f)

#define TMC\_RAMP\_D1\_MAX

**Definition** stepper\_trinamic.h:44

[TMC\_RAMP\_D1\_MIN](#ga9d825b4269d204eaded8b0559114a8ac)

#define TMC\_RAMP\_D1\_MIN

**Definition** stepper\_trinamic.h:45

[TMC\_RAMP\_VSTART\_MAX](#ga9e9a9e371a79b153226645383867f57c)

#define TMC\_RAMP\_VSTART\_MAX

Trinamic stepper controller ramp generator data limits.

**Definition** stepper\_trinamic.h:34

[TMC\_RAMP\_VCOOLTHRS\_MAX](#gabbdadfe7e2dac7851c1bd5b6c5dd4a42)

#define TMC\_RAMP\_VCOOLTHRS\_MAX

**Definition** stepper\_trinamic.h:52

[TMC\_RAMP\_AMAX\_MAX](#gac4ae29a8dee3c5f30afd9ad879eb841f)

#define TMC\_RAMP\_AMAX\_MAX

**Definition** stepper\_trinamic.h:42

[TMC\_RAMP\_VSTOP\_MIN](#gada43f70cfca38bd5bb3208474c92f276)

#define TMC\_RAMP\_VSTOP\_MIN

**Definition** stepper\_trinamic.h:49

[TMC\_RAMP\_A1\_MIN](#gae93384303a1aa78ecee86df6749449a1)

#define TMC\_RAMP\_A1\_MIN

**Definition** stepper\_trinamic.h:41

[TMC\_RAMP\_IHOLD\_IRUN\_MAX](#gaeab2e7683232b2f77c6e57602af268e1)

#define TMC\_RAMP\_IHOLD\_IRUN\_MAX

**Definition** stepper\_trinamic.h:56

[TMC\_RAMP\_DMAX\_MIN](#gaed3825c79b588840c355fd1d3da9d3bb)

#define TMC\_RAMP\_DMAX\_MIN

**Definition** stepper\_trinamic.h:47

Check if Ramp DT data is within limits.

## [◆ ](#ga2043631a9382df69c0cddf69e57845ba)TMC\_RAMP\_A1\_MAX

| #define TMC\_RAMP\_A1\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gae93384303a1aa78ecee86df6749449a1)TMC\_RAMP\_A1\_MIN

| #define TMC\_RAMP\_A1\_MIN   0 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gac4ae29a8dee3c5f30afd9ad879eb841f)TMC\_RAMP\_AMAX\_MAX

| #define TMC\_RAMP\_AMAX\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga50e4297381755484bbddf9976f1d51f5)TMC\_RAMP\_AMAX\_MIN

| #define TMC\_RAMP\_AMAX\_MIN   0 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga9ae3e36281fbf1a83e3c6cf71ef2441f)TMC\_RAMP\_D1\_MAX

| #define TMC\_RAMP\_D1\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga9d825b4269d204eaded8b0559114a8ac)TMC\_RAMP\_D1\_MIN

| #define TMC\_RAMP\_D1\_MIN   1 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga80d3cbcb6455cbafd36c677e292622c4)TMC\_RAMP\_DMAX\_MAX

| #define TMC\_RAMP\_DMAX\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gaed3825c79b588840c355fd1d3da9d3bb)TMC\_RAMP\_DMAX\_MIN

| #define TMC\_RAMP\_DMAX\_MIN   0 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gab5e5f7c14b896b580051f8b72afb529d)TMC\_RAMP\_DT\_SPEC\_GET

| #define TMC\_RAMP\_DT\_SPEC\_GET | ( |  | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

**Value:**

{ \

.vstart = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vstart), \

.v1 = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, v1), \

.vmax = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vmax), \

.a1 = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, a1), \

.amax = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, amax), \

.d1 = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, d1), \

.dmax = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, dmax), \

.vstop = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vstop), \

.tzerowait = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, tzerowait), \

.vcoolthrs = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vcoolthrs), \

.vhigh = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, vhigh), \

.iholdrun = (TMC5XXX\_IRUN([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, irun)) | \

TMC5XXX\_IHOLD([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, ihold)) | \

TMC5XXX\_IHOLDDELAY([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, iholddelay))), \

}

Get Trinamic Stepper Ramp Generator data from DT.

Parameters
:   | node | DT node identifier |
    | --- | --- |

Returns
:   struct [tmc\_ramp\_generator\_data](structtmc__ramp__generator__data.md "Trinamic Stepper Ramp Generator data.")

## [◆ ](#gaeab2e7683232b2f77c6e57602af268e1)TMC\_RAMP\_IHOLD\_IRUN\_MAX

| #define TMC\_RAMP\_IHOLD\_IRUN\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 0) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga732705b9ea5208d16caabfd36f9b0ea8)TMC\_RAMP\_IHOLD\_IRUN\_MIN

| #define TMC\_RAMP\_IHOLD\_IRUN\_MIN   0 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga5cdbd0068d00533a8cf6d952be8c943e)TMC\_RAMP\_IHOLDDELAY\_MAX

| #define TMC\_RAMP\_IHOLDDELAY\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga7b787ce2fffd9e689230a4abf2070bf2)TMC\_RAMP\_IHOLDDELAY\_MIN

| #define TMC\_RAMP\_IHOLDDELAY\_MIN   0 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga0bb50350111fb8a7dc22dae9948690f6)TMC\_RAMP\_TZEROWAIT\_MAX

| #define TMC\_RAMP\_TZEROWAIT\_MAX   ([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) - 512) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga509b5bb88d3976323f90cd9647af97b1)TMC\_RAMP\_TZEROWAIT\_MIN

| #define TMC\_RAMP\_TZEROWAIT\_MIN   0 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga9530d64f9c331681b33230fcc8ef7512)TMC\_RAMP\_V1\_MAX

| #define TMC\_RAMP\_V1\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 0) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga6f07fdd1e99eff62f93d28b7c2527283)TMC\_RAMP\_V1\_MIN

| #define TMC\_RAMP\_V1\_MIN   0 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga3aee23f87376c760f43d714df646ad54)TMC\_RAMP\_VACTUAL\_SHIFT

| #define TMC\_RAMP\_VACTUAL\_SHIFT   22 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gabbdadfe7e2dac7851c1bd5b6c5dd4a42)TMC\_RAMP\_VCOOLTHRS\_MAX

| #define TMC\_RAMP\_VCOOLTHRS\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga37a395c0056c9b20520cace7ba925014)TMC\_RAMP\_VCOOLTHRS\_MIN

| #define TMC\_RAMP\_VCOOLTHRS\_MIN   0 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga4134f638119d89b559118028a65fd5c7)TMC\_RAMP\_VHIGH\_MAX

| #define TMC\_RAMP\_VHIGH\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga7d87a071f418cecd2f80a1a1403ff2c5)TMC\_RAMP\_VHIGH\_MIN

| #define TMC\_RAMP\_VHIGH\_MIN   0 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga6bd3a7d1578f4d9729327cdc9bcb2214)TMC\_RAMP\_VMAX\_MAX

| #define TMC\_RAMP\_VMAX\_MAX   ([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 0) - 512) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga42fe12c7afa3411279df79323b6005ff)TMC\_RAMP\_VMAX\_MIN

| #define TMC\_RAMP\_VMAX\_MIN   0 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga9e9a9e371a79b153226645383867f57c)TMC\_RAMP\_VSTART\_MAX

| #define TMC\_RAMP\_VSTART\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(17, 0) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

Trinamic stepper controller ramp generator data limits.

## [◆ ](#ga7569a6172df37f1e669eed75a1acb5d5)TMC\_RAMP\_VSTART\_MIN

| #define TMC\_RAMP\_VSTART\_MIN   0 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#ga7b121c433e4bf33da2a5f14ec53bf627)TMC\_RAMP\_VSTOP\_MAX

| #define TMC\_RAMP\_VSTOP\_MAX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(17, 0) |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## [◆ ](#gada43f70cfca38bd5bb3208474c92f276)TMC\_RAMP\_VSTOP\_MIN

| #define TMC\_RAMP\_VSTOP\_MIN   1 |
| --- |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

## Function Documentation

## [◆ ](#gac2c7168e3618951b65df3257553260f6)tmc50xx\_stepper\_set\_max\_velocity()

| int tmc50xx\_stepper\_set\_max\_velocity | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *velocity* ) |

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

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

`#include <[stepper_trinamic.h](stepper__trinamic_8h.md)>`

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
