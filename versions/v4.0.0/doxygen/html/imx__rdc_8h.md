---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/imx__rdc_8h.html
original_path: doxygen/html/imx__rdc_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx\_rdc.h File Reference

[Go to the source code of this file.](imx__rdc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [A7\_DOMAIN\_ID](#aac94244543640603434faa2862eb1eef)   0 |
| #define | [A9\_DOMAIN\_ID](#a2f961de9f7c100cf1ef6aa65cf40cd4f)   0 |
| #define | [A53\_DOMAIN\_ID](#ad150e5ccb613174d8aadea285fd99a03)   0 |
| #define | [M4\_DOMAIN\_ID](#adf4bff1dbb4418d4c9aa2ecb5d8e129a)   1 |
| #define | [M7\_DOMAIN\_ID](#a926358589743b689f3b9fc11a06c9f52)   1 |
| #define | [RDC\_DOMAIN\_PERM\_NONE](#aacbb82ed8695c00e9bfcb0458495c17d)   (0x0) |
| #define | [RDC\_DOMAIN\_PERM\_W](#a29b98390e0431ebd6c92e227c5fda530)   (0x1) |
| #define | [RDC\_DOMAIN\_PERM\_R](#a95d915525ff5b3873462f00f2f64dedc)   (0x2) |
| #define | [RDC\_DOMAIN\_PERM\_RW](#ad50d355ba8404bbd872a0d6a8ea23f9d)   ([RDC\_DOMAIN\_PERM\_W](#a29b98390e0431ebd6c92e227c5fda530)|[RDC\_DOMAIN\_PERM\_R](#a95d915525ff5b3873462f00f2f64dedc)) |
| #define | [RDC\_DOMAIN\_PERM](#a6e2ca7030bfeb01a10d3b66e37f06a03)(domain, perm) |
| #define | [RDC\_DT\_VAL](#acdbb0f6700bd61336079152f3e704896)(nodelabel) |

## Macro Definition Documentation

## [◆ ](#ad150e5ccb613174d8aadea285fd99a03)A53\_DOMAIN\_ID

| #define A53\_DOMAIN\_ID   0 |
| --- |

## [◆ ](#aac94244543640603434faa2862eb1eef)A7\_DOMAIN\_ID

| #define A7\_DOMAIN\_ID   0 |
| --- |

## [◆ ](#a2f961de9f7c100cf1ef6aa65cf40cd4f)A9\_DOMAIN\_ID

| #define A9\_DOMAIN\_ID   0 |
| --- |

## [◆ ](#adf4bff1dbb4418d4c9aa2ecb5d8e129a)M4\_DOMAIN\_ID

| #define M4\_DOMAIN\_ID   1 |
| --- |

## [◆ ](#a926358589743b689f3b9fc11a06c9f52)M7\_DOMAIN\_ID

| #define M7\_DOMAIN\_ID   1 |
| --- |

## [◆ ](#a6e2ca7030bfeb01a10d3b66e37f06a03)RDC\_DOMAIN\_PERM

| #define RDC\_DOMAIN\_PERM | ( |  | *domain*, |
| --- | --- | --- | --- |
|  |  |  | *perm* ) |

**Value:**

(perm << (domain \* 2))

## [◆ ](#aacbb82ed8695c00e9bfcb0458495c17d)RDC\_DOMAIN\_PERM\_NONE

| #define RDC\_DOMAIN\_PERM\_NONE   (0x0) |
| --- |

## [◆ ](#a95d915525ff5b3873462f00f2f64dedc)RDC\_DOMAIN\_PERM\_R

| #define RDC\_DOMAIN\_PERM\_R   (0x2) |
| --- |

## [◆ ](#ad50d355ba8404bbd872a0d6a8ea23f9d)RDC\_DOMAIN\_PERM\_RW

| #define RDC\_DOMAIN\_PERM\_RW   ([RDC\_DOMAIN\_PERM\_W](#a29b98390e0431ebd6c92e227c5fda530)|[RDC\_DOMAIN\_PERM\_R](#a95d915525ff5b3873462f00f2f64dedc)) |
| --- |

## [◆ ](#a29b98390e0431ebd6c92e227c5fda530)RDC\_DOMAIN\_PERM\_W

| #define RDC\_DOMAIN\_PERM\_W   (0x1) |
| --- |

## [◆ ](#acdbb0f6700bd61336079152f3e704896)RDC\_DT\_VAL

| #define RDC\_DT\_VAL | ( |  | *nodelabel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(nodelabel), rdc)

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:745

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [rdc](dir_05c3918b97c5e0e97965e827aa660eab.md)
- [imx\_rdc.h](imx__rdc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
