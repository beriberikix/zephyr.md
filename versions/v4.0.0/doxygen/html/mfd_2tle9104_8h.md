---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mfd_2tle9104_8h.html
original_path: doxygen/html/mfd_2tle9104_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tle9104.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](mfd_2tle9104_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [gpio\_tle9104\_channel\_diagnostics](structgpio__tle9104__channel__diagnostics.md) |

| Macros | |
| --- | --- |
| #define | [TLE9104\_GPIO\_COUNT](#a3f6f8709aa1b46781268154e34c298a9)   4 |

| Enumerations | |
| --- | --- |
| enum | [tle9104\_on\_state\_diagnostics](#aa40748ba46d1bc413f8bf3caa5d7b4b0) {     [TLE9104\_ONDIAG\_OT](#aa40748ba46d1bc413f8bf3caa5d7b4b0a359b0a412ecb9de36e12a50946dc2173) = 5 , [TLE9104\_ONDIAG\_OCTIME](#aa40748ba46d1bc413f8bf3caa5d7b4b0a36e248aad4b5b47c338589d86f4e2925) = 4 , [TLE9104\_ONDIAG\_OCOT](#aa40748ba46d1bc413f8bf3caa5d7b4b0a7cea6cba428b062f1951809d12e15685) = 3 , [TLE9104\_ONDIAG\_SCB](#aa40748ba46d1bc413f8bf3caa5d7b4b0a9d82a99fcc6ea7017e38959d5e299f4c) = 2 ,     [TLE9104\_ONDIAG\_NOFAIL](#aa40748ba46d1bc413f8bf3caa5d7b4b0a7aace824362e7c51841585b9f3a64ca4) = 1 , [TLE9104\_ONDIAG\_UNKNOWN](#aa40748ba46d1bc413f8bf3caa5d7b4b0addb7f997401544e59dc6a181c1341679) = 0   } |
| enum | [tle9104\_off\_state\_diagnostics](#acd342488b1a9b0e2b4a0e79a1441d8e3) { [TLE9104\_OFFDIAG\_SCG](#acd342488b1a9b0e2b4a0e79a1441d8e3abc547081143f840a6261d807fa72284e) = 3 , [TLE9104\_OFFDIAG\_OL](#acd342488b1a9b0e2b4a0e79a1441d8e3ac37a0b72b862d7279572eaf960e5507d) = 2 , [TLE9104\_OFFDIAG\_NOFAIL](#acd342488b1a9b0e2b4a0e79a1441d8e3a2dfab15a18c96bcbe413a4ed94da6af7) = 1 , [TLE9104\_OFFDIAG\_UNKNOWN](#acd342488b1a9b0e2b4a0e79a1441d8e3ad16bbd2e028e21957316609bda7f8393) = 0 } |

| Functions | |
| --- | --- |
| int | [tle9104\_get\_diagnostics](#a3fbd8b8e3cdf6998990d055a6e503361) (const struct [device](structdevice.md) \*dev, struct [gpio\_tle9104\_channel\_diagnostics](structgpio__tle9104__channel__diagnostics.md) diag[4]) |
|  | get the diagnostics of the outputs |
| int | [tle9104\_clear\_diagnostics](#a1c4925c222bbdd94c0fe1eb295244ec3) (const struct [device](structdevice.md) \*dev) |
|  | clear the diagnostics of the outputs |
| int | [tle9104\_write\_state](#a5febfb7f1b4fd5859bf503e9ff4c2ed4) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | write output state |

## Macro Definition Documentation

## [◆ ](#a3f6f8709aa1b46781268154e34c298a9)TLE9104\_GPIO\_COUNT

| #define TLE9104\_GPIO\_COUNT   4 |
| --- |

## Enumeration Type Documentation

## [◆ ](#acd342488b1a9b0e2b4a0e79a1441d8e3)tle9104\_off\_state\_diagnostics

| enum [tle9104\_off\_state\_diagnostics](#acd342488b1a9b0e2b4a0e79a1441d8e3) |
| --- |

| Enumerator | |
| --- | --- |
| TLE9104\_OFFDIAG\_SCG |  |
| TLE9104\_OFFDIAG\_OL |  |
| TLE9104\_OFFDIAG\_NOFAIL |  |
| TLE9104\_OFFDIAG\_UNKNOWN |  |

## [◆ ](#aa40748ba46d1bc413f8bf3caa5d7b4b0)tle9104\_on\_state\_diagnostics

| enum [tle9104\_on\_state\_diagnostics](#aa40748ba46d1bc413f8bf3caa5d7b4b0) |
| --- |

| Enumerator | |
| --- | --- |
| TLE9104\_ONDIAG\_OT |  |
| TLE9104\_ONDIAG\_OCTIME |  |
| TLE9104\_ONDIAG\_OCOT |  |
| TLE9104\_ONDIAG\_SCB |  |
| TLE9104\_ONDIAG\_NOFAIL |  |
| TLE9104\_ONDIAG\_UNKNOWN |  |

## Function Documentation

## [◆ ](#a1c4925c222bbdd94c0fe1eb295244ec3)tle9104\_clear\_diagnostics()

| int tle9104\_clear\_diagnostics | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

clear the diagnostics of the outputs

Parameters
:   | dev | instance of TLE9104 |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |

## [◆ ](#a3fbd8b8e3cdf6998990d055a6e503361)tle9104\_get\_diagnostics()

| int tle9104\_get\_diagnostics | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [gpio\_tle9104\_channel\_diagnostics](structgpio__tle9104__channel__diagnostics.md) | *diag*[4] ) |

get the diagnostics of the outputs

Parameters
:   | dev | instance of TLE9104 |
    | --- | --- |
    | diag | destination where the result is written to |

Return values
:   | 0 | If successful. |
    | --- | --- |

## [◆ ](#a5febfb7f1b4fd5859bf503e9ff4c2ed4)tle9104\_write\_state()

| int tle9104\_write\_state | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *state* ) |

write output state

Parameters
:   | dev | instance of TLE9104 |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | output state, each bit represents on output |

Return values
:   | 0 | If successful. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [tle9104.h](mfd_2tle9104_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
