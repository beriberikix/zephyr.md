---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpwm__dt__spec.html
original_path: doxygen/html/structpwm__dt__spec.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pwm\_dt\_spec Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [PWM Interface](group__pwm__interface.md)

Container for PWM information specified in devicetree.
[More...](#details)

`#include <[pwm.h](drivers_2pwm_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#ad9f2991bcf978940e638d17c5e17311e) |
|  | PWM device instance. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [channel](#a739a2672afa1d56ec1d865d6d5be47b2) |
|  | Channel number. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [period](#a935c72595e2248ab75ce0c43a394c0b3) |
|  | Period in nanoseconds. |
| [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) | [flags](#a2ddb45cbde80314a5a50dffe2e43921b) |
|  | Flags. |

## Detailed Description

Container for PWM information specified in devicetree.

This type contains a pointer to a PWM device, channel number (controlled by the PWM device), the PWM signal period in nanoseconds and the flags applicable to the channel. Note that not all PWM drivers support flags. In such case, flags will be set to 0.

See also
:   [PWM\_DT\_SPEC\_GET\_BY\_NAME](group__pwm__interface.md#ga88b92c580860441c83d1b03db25fc4f1 "Static initializer for a struct pwm_dt_spec.")
:   [PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR](group__pwm__interface.md#ga5557add2123a7138b64997cd070e0ee6 "Like PWM_DT_SPEC_GET_BY_NAME(), with a fallback to a default value.")
:   [PWM\_DT\_SPEC\_GET\_BY\_IDX](group__pwm__interface.md#ga7e8375bcf95ae6a9500ce3aba4586de4 "Static initializer for a struct pwm_dt_spec.")
:   [PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__pwm__interface.md#gaf5808fd88b101208681820b53bca33e1 "Like PWM_DT_SPEC_GET_BY_IDX(), with a fallback to a default value.")
:   [PWM\_DT\_SPEC\_GET](group__pwm__interface.md#ga59a79f0b77c5b71252bde126f333a84b "Equivalent to PWM_DT_SPEC_GET_BY_IDX(node_id, 0).")
:   [PWM\_DT\_SPEC\_GET\_OR](group__pwm__interface.md#ga82f8efe8f0bc088fdda58c09dd4be4ff "Equivalent to PWM_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value).")

## Field Documentation

## [◆ ](#a739a2672afa1d56ec1d865d6d5be47b2)channel

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pwm\_dt\_spec::channel |
| --- |

Channel number.

## [◆ ](#ad9f2991bcf978940e638d17c5e17311e)dev

| const struct [device](structdevice.md)\* pwm\_dt\_spec::dev |
| --- |

PWM device instance.

## [◆ ](#a2ddb45cbde80314a5a50dffe2e43921b)flags

| [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) pwm\_dt\_spec::flags |
| --- |

Flags.

## [◆ ](#a935c72595e2248ab75ce0c43a394c0b3)period

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pwm\_dt\_spec::period |
| --- |

Period in nanoseconds.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[pwm.h](drivers_2pwm_8h_source.md)

- [pwm\_dt\_spec](structpwm__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
