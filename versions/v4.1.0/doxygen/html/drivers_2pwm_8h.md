---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2pwm_8h.html
original_path: doxygen/html/drivers_2pwm_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pwm.h File Reference

Public PWM Driver APIs.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/sys_clock.h](sys__clock_8h_source.md)>`  
`#include <[zephyr/sys/math_extras.h](math__extras_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/dt-bindings/pwm/pwm.h](dt-bindings_2pwm_2pwm_8h_source.md)>`  
`#include <zephyr/syscalls/pwm.h>`

[Go to the source code of this file.](drivers_2pwm_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pwm\_dt\_spec](structpwm__dt__spec.md) |
|  | Container for PWM information specified in devicetree. [More...](structpwm__dt__spec.md#details) |

| Macros | |
| --- | --- |
| #define | [PWM\_DT\_SPEC\_GET\_BY\_NAME](group__pwm__interface.md#ga88b92c580860441c83d1b03db25fc4f1)(node\_id, name) |
|  | Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree."). |
| #define | [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME](group__pwm__interface.md#ga104a81a3481362d2da9046c0e93a8cd0)(inst, name) |
|  | Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") from a DT\_DRV\_COMPAT instance. |
| #define | [PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR](group__pwm__interface.md#ga5557add2123a7138b64997cd070e0ee6)(node\_id, name, default\_value) |
|  | Like [PWM\_DT\_SPEC\_GET\_BY\_NAME()](group__pwm__interface.md#ga88b92c580860441c83d1b03db25fc4f1 "Static initializer for a struct pwm_dt_spec."), with a fallback to a default value. |
| #define | [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME\_OR](group__pwm__interface.md#gac00e53eccaf9eb515aed0921404adb31)(inst, name, default\_value) |
|  | Like [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME()](group__pwm__interface.md#ga104a81a3481362d2da9046c0e93a8cd0 "Static initializer for a struct pwm_dt_spec from a DT_DRV_COMPAT instance."), with a fallback to a default value. |
| #define | [PWM\_DT\_SPEC\_GET\_BY\_IDX](group__pwm__interface.md#ga7e8375bcf95ae6a9500ce3aba4586de4)(node\_id, idx) |
|  | Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree."). |
| #define | [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX](group__pwm__interface.md#ga3c1c557fa4461e61f4a147fc72f87f8d)(inst, idx) |
|  | Static initializer for a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") from a DT\_DRV\_COMPAT instance. |
| #define | [PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__pwm__interface.md#gaf5808fd88b101208681820b53bca33e1)(node\_id, idx, default\_value) |
|  | Like [PWM\_DT\_SPEC\_GET\_BY\_IDX()](group__pwm__interface.md#ga7e8375bcf95ae6a9500ce3aba4586de4 "Static initializer for a struct pwm_dt_spec."), with a fallback to a default value. |
| #define | [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](group__pwm__interface.md#ga7eeef648c3142fced48b7ab52c9c1ead)(inst, idx, default\_value) |
|  | Like [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX()](group__pwm__interface.md#ga3c1c557fa4461e61f4a147fc72f87f8d "Static initializer for a struct pwm_dt_spec from a DT_DRV_COMPAT instance."), with a fallback to a default value. |
| #define | [PWM\_DT\_SPEC\_GET](group__pwm__interface.md#ga59a79f0b77c5b71252bde126f333a84b)(node\_id) |
|  | Equivalent to [PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)](group__pwm__interface.md#ga7e8375bcf95ae6a9500ce3aba4586de4 "Static initializer for a struct pwm_dt_spec."). |
| #define | [PWM\_DT\_SPEC\_INST\_GET](group__pwm__interface.md#gaa346428c6cb1f11aafaa6306486e8a4b)(inst) |
|  | Equivalent to [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)](group__pwm__interface.md#ga3c1c557fa4461e61f4a147fc72f87f8d "Static initializer for a struct pwm_dt_spec from a DT_DRV_COMPAT instance."). |
| #define | [PWM\_DT\_SPEC\_GET\_OR](group__pwm__interface.md#ga82f8efe8f0bc088fdda58c09dd4be4ff)(node\_id, default\_value) |
|  | Equivalent to [PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)](group__pwm__interface.md#gaf5808fd88b101208681820b53bca33e1 "Like PWM_DT_SPEC_GET_BY_IDX(), with a fallback to a default value."). |
| #define | [PWM\_DT\_SPEC\_INST\_GET\_OR](group__pwm__interface.md#ga6bd84121715beb62a3ca2672dfae0630)(inst, default\_value) |
|  | Equivalent to [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, 0, default\_value)](group__pwm__interface.md#ga7eeef648c3142fced48b7ab52c9c1ead "Like PWM_DT_SPEC_INST_GET_BY_IDX(), with a fallback to a default value."). |
| PWM capture configuration flags | |
|  | |
| #define | [PWM\_CAPTURE\_TYPE\_PERIOD](group__pwm__interface.md#ga5b4b41ccdf8810a77f71c2155a521f44)   (1U << PWM\_CAPTURE\_TYPE\_SHIFT) |
|  | PWM pin capture captures period. |
| #define | [PWM\_CAPTURE\_TYPE\_PULSE](group__pwm__interface.md#gab883b83cc5418555a437ce128f32ab01)   (2U << PWM\_CAPTURE\_TYPE\_SHIFT) |
|  | PWM pin capture captures pulse width. |
| #define | [PWM\_CAPTURE\_TYPE\_BOTH](group__pwm__interface.md#ga76175b0c2d5187ded5bbd314dc798bd5) |
|  | PWM pin capture captures both period and pulse width. |
| #define | [PWM\_CAPTURE\_MODE\_SINGLE](group__pwm__interface.md#gad59fe75340facda843cad06993cf1814)   (0U << PWM\_CAPTURE\_MODE\_SHIFT) |
|  | PWM pin capture captures a single period/pulse width. |
| #define | [PWM\_CAPTURE\_MODE\_CONTINUOUS](group__pwm__interface.md#gabe9bbff9832b4fa40faa057fad8fdaa9)   (1U << PWM\_CAPTURE\_MODE\_SHIFT) |
|  | PWM pin capture captures period/pulse width continuously. |

| Typedefs | |
| --- | --- |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) |
|  | Provides a type to hold PWM configuration flags. |
| typedef void(\* | [pwm\_capture\_callback\_handler\_t](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse\_cycles, int status, void \*user\_data) |
|  | PWM capture callback handler function signature. |

| Functions | |
| --- | --- |
| int | [pwm\_set\_cycles](group__pwm__interface.md#gaff280789f7b45fdefc354b3f841fe3ef) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set the period and pulse width for a single PWM output. |
| int | [pwm\_get\_cycles\_per\_sec](group__pwm__interface.md#ga310d416087a619f90e946222668135af) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*cycles) |
|  | Get the clock rate (cycles per second) for a single PWM output. |
| static int | [pwm\_set](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set the period and pulse width in nanoseconds for a single PWM output. |
| static int | [pwm\_set\_dt](group__pwm__interface.md#ga225ce58ceb3de3d76df3e03439d655b9) (const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse) |
|  | Set the period and pulse width in nanoseconds from a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree.") (with custom period). |
| static int | [pwm\_set\_pulse\_dt](group__pwm__interface.md#ga8ff263177143d33c6d0a284b837bc4da) (const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pulse) |
|  | Set the period and pulse width in nanoseconds from a struct [pwm\_dt\_spec](structpwm__dt__spec.md "Container for PWM information specified in devicetree."). |
| static int | [pwm\_cycles\_to\_usec](group__pwm__interface.md#gae57fb205e43dde82d96abe79966539a9) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cycles, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*usec) |
|  | Convert from PWM cycles to microseconds. |
| static int | [pwm\_cycles\_to\_nsec](group__pwm__interface.md#ga6f0281398611dd876386c66a63373a2e) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cycles, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*nsec) |
|  | Convert from PWM cycles to nanoseconds. |
| static int | [pwm\_configure\_capture](group__pwm__interface.md#ga9603146d7f9c2690c1e1983113d6c6bb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [pwm\_capture\_callback\_handler\_t](group__pwm__interface.md#ga2395ef29b77674d9f1b56d8091b8695a) cb, void \*user\_data) |
|  | Configure PWM period/pulse width capture for a single PWM input. |
| int | [pwm\_enable\_capture](group__pwm__interface.md#gad14ca53862a465d1789e8936ce394f9a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Enable PWM period/pulse width capture for a single PWM input. |
| int | [pwm\_disable\_capture](group__pwm__interface.md#ga1df2bb40af2fa3ce945cc9cd67edc2bf) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Disable PWM period/pulse width capture for a single PWM input. |
| int | [pwm\_capture\_cycles](group__pwm__interface.md#ga09767ae3c8d970675dbf9e3e50291743) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*period, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Capture a single PWM period/pulse width in clock cycles for a single PWM input. |
| static int | [pwm\_capture\_usec](group__pwm__interface.md#ga3a1552ea924eeec21477396da6d3890b) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*period, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Capture a single PWM period/pulse width in microseconds for a single PWM input. |
| static int | [pwm\_capture\_nsec](group__pwm__interface.md#ga6489095d890224d23c5ed05bc884d24a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*period, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*pulse, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Capture a single PWM period/pulse width in nanoseconds for a single PWM input. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pwm\_is\_ready\_dt](group__pwm__interface.md#ga70aad0d88e8041c880499e7cdaa9ae57) (const struct [pwm\_dt\_spec](structpwm__dt__spec.md) \*spec) |
|  | Validate that the PWM device is ready. |

## Detailed Description

Public PWM Driver APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pwm.h](drivers_2pwm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
