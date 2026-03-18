---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pinctrl__esp32__common_8h.html
original_path: doxygen/html/pinctrl__esp32__common_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_esp32\_common.h File Reference

[Go to the source code of this file.](pinctrl__esp32__common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP32\_PORT\_IDX](#a2126dde6e9ab7d1a67fb1c4cc66f03a0)(\_pin) |
| #define | [ESP32\_PIN\_NUM](#a38701de31ad20d7bf76c619ec7c42649)(\_mux) |
| #define | [ESP32\_PIN\_SIGI](#a1e12a6dec8edef8d13d02d57b1af2be8)(\_mux) |
| #define | [ESP32\_PIN\_SIGO](#a51eba3c904687c6ca113f83623498357)(\_mux) |
| #define | [ESP32\_PIN\_BIAS](#acce125cecd6af2debe225c2127188e62)(\_cfg) |
| #define | [ESP32\_PIN\_DRV](#a11ee4c4491be52a383c773be7631769d)(\_cfg) |
| #define | [ESP32\_PIN\_MODE\_OUT](#a0e05c5abc28558d0a351f661f5c37d09)(\_cfg) |
| #define | [ESP32\_PIN\_EN\_DIR](#a2283009110fe8c4eb6fe2855c2bb3451)(\_cfg) |

## Macro Definition Documentation

## [◆ ](#acce125cecd6af2debe225c2127188e62)ESP32\_PIN\_BIAS

| #define ESP32\_PIN\_BIAS | ( |  | *\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((\_cfg) >> [ESP32\_PIN\_BIAS\_SHIFT](esp-pinctrl-common_8h.md#a47498f4ba429ddaedc5b2547888bfa00)) & [ESP32\_PIN\_BIAS\_MASK](esp-pinctrl-common_8h.md#a65d2b03b1a813cb4d2921c7cc8deec79))

[ESP32\_PIN\_BIAS\_SHIFT](esp-pinctrl-common_8h.md#a47498f4ba429ddaedc5b2547888bfa00)

#define ESP32\_PIN\_BIAS\_SHIFT

**Definition** esp-pinctrl-common.h:36

[ESP32\_PIN\_BIAS\_MASK](esp-pinctrl-common_8h.md#a65d2b03b1a813cb4d2921c7cc8deec79)

#define ESP32\_PIN\_BIAS\_MASK

**Definition** esp-pinctrl-common.h:37

## [◆ ](#a11ee4c4491be52a383c773be7631769d)ESP32\_PIN\_DRV

| #define ESP32\_PIN\_DRV | ( |  | *\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((\_cfg) >> [ESP32\_PIN\_DRV\_SHIFT](esp-pinctrl-common_8h.md#abfdf0aa9a8a5116f3ca66e54e72552ac)) & [ESP32\_PIN\_DRV\_MASK](esp-pinctrl-common_8h.md#a4d05215be796ff091633a5f0de2a6748))

[ESP32\_PIN\_DRV\_MASK](esp-pinctrl-common_8h.md#a4d05215be796ff091633a5f0de2a6748)

#define ESP32\_PIN\_DRV\_MASK

**Definition** esp-pinctrl-common.h:39

[ESP32\_PIN\_DRV\_SHIFT](esp-pinctrl-common_8h.md#abfdf0aa9a8a5116f3ca66e54e72552ac)

#define ESP32\_PIN\_DRV\_SHIFT

**Definition** esp-pinctrl-common.h:38

## [◆ ](#a2283009110fe8c4eb6fe2855c2bb3451)ESP32\_PIN\_EN\_DIR

| #define ESP32\_PIN\_EN\_DIR | ( |  | *\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((\_cfg) >> [ESP32\_PIN\_EN\_DIR\_SHIFT](esp-pinctrl-common_8h.md#ada547ab4673154f6645f8d262196bf54)) & [ESP32\_PIN\_EN\_DIR\_MASK](esp-pinctrl-common_8h.md#a8941e50a06706315fcddfd327f10e7f2))

[ESP32\_PIN\_EN\_DIR\_MASK](esp-pinctrl-common_8h.md#a8941e50a06706315fcddfd327f10e7f2)

#define ESP32\_PIN\_EN\_DIR\_MASK

**Definition** esp-pinctrl-common.h:43

[ESP32\_PIN\_EN\_DIR\_SHIFT](esp-pinctrl-common_8h.md#ada547ab4673154f6645f8d262196bf54)

#define ESP32\_PIN\_EN\_DIR\_SHIFT

**Definition** esp-pinctrl-common.h:42

## [◆ ](#a0e05c5abc28558d0a351f661f5c37d09)ESP32\_PIN\_MODE\_OUT

| #define ESP32\_PIN\_MODE\_OUT | ( |  | *\_cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((\_cfg) >> [ESP32\_PIN\_OUT\_SHIFT](esp-pinctrl-common_8h.md#af20225f7ed095e083c3b7a2fa55a5313)) & [ESP32\_PIN\_OUT\_MASK](esp-pinctrl-common_8h.md#a0c806899f6fb854f50c3a88a40240691))

[ESP32\_PIN\_OUT\_MASK](esp-pinctrl-common_8h.md#a0c806899f6fb854f50c3a88a40240691)

#define ESP32\_PIN\_OUT\_MASK

**Definition** esp-pinctrl-common.h:41

[ESP32\_PIN\_OUT\_SHIFT](esp-pinctrl-common_8h.md#af20225f7ed095e083c3b7a2fa55a5313)

#define ESP32\_PIN\_OUT\_SHIFT

**Definition** esp-pinctrl-common.h:40

## [◆ ](#a38701de31ad20d7bf76c619ec7c42649)ESP32\_PIN\_NUM

| #define ESP32\_PIN\_NUM | ( |  | *\_mux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((\_mux) >> [ESP32\_PIN\_NUM\_SHIFT](esp-pinctrl-common_8h.md#a14b1575596d4a3c7f349e140a206e7fc)) & [ESP32\_PIN\_NUM\_MASK](esp-pinctrl-common_8h.md#aff8c7306c9eb06955c069a08700b9602))

[ESP32\_PIN\_NUM\_SHIFT](esp-pinctrl-common_8h.md#a14b1575596d4a3c7f349e140a206e7fc)

#define ESP32\_PIN\_NUM\_SHIFT

**Definition** esp-pinctrl-common.h:12

[ESP32\_PIN\_NUM\_MASK](esp-pinctrl-common_8h.md#aff8c7306c9eb06955c069a08700b9602)

#define ESP32\_PIN\_NUM\_MASK

**Definition** esp-pinctrl-common.h:13

## [◆ ](#a1e12a6dec8edef8d13d02d57b1af2be8)ESP32\_PIN\_SIGI

| #define ESP32\_PIN\_SIGI | ( |  | *\_mux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((\_mux) >> [ESP32\_PIN\_SIGI\_SHIFT](esp-pinctrl-common_8h.md#a457b5af6f423f5d743b81317f331f175)) & [ESP32\_PIN\_SIGI\_MASK](esp-pinctrl-common_8h.md#a0069fd5363ff598a903823729ac7b785))

[ESP32\_PIN\_SIGI\_MASK](esp-pinctrl-common_8h.md#a0069fd5363ff598a903823729ac7b785)

#define ESP32\_PIN\_SIGI\_MASK

**Definition** esp-pinctrl-common.h:20

[ESP32\_PIN\_SIGI\_SHIFT](esp-pinctrl-common_8h.md#a457b5af6f423f5d743b81317f331f175)

#define ESP32\_PIN\_SIGI\_SHIFT

**Definition** esp-pinctrl-common.h:21

## [◆ ](#a51eba3c904687c6ca113f83623498357)ESP32\_PIN\_SIGO

| #define ESP32\_PIN\_SIGO | ( |  | *\_mux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((\_mux) >> [ESP32\_PIN\_SIGO\_SHIFT](esp-pinctrl-common_8h.md#ab7b2f3303e89bb59c9fc0aec216678fd)) & [ESP32\_PIN\_SIGO\_MASK](esp-pinctrl-common_8h.md#a97e539c13c42cabdb31c53dba9573bb8))

[ESP32\_PIN\_SIGO\_MASK](esp-pinctrl-common_8h.md#a97e539c13c42cabdb31c53dba9573bb8)

#define ESP32\_PIN\_SIGO\_MASK

**Definition** esp-pinctrl-common.h:22

[ESP32\_PIN\_SIGO\_SHIFT](esp-pinctrl-common_8h.md#ab7b2f3303e89bb59c9fc0aec216678fd)

#define ESP32\_PIN\_SIGO\_SHIFT

**Definition** esp-pinctrl-common.h:23

## [◆ ](#a2126dde6e9ab7d1a67fb1c4cc66f03a0)ESP32\_PORT\_IDX

| #define ESP32\_PORT\_IDX | ( |  | *\_pin* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((\_pin) < 32) ? 0 : 1)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl](dir_c0bb3bf986f9412b3a6b9d85dc06c157.md)
- [pinctrl\_esp32\_common.h](pinctrl__esp32__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
