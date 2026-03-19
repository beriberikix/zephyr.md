---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lis2dux12_8h.html
original_path: doxygen/html/lis2dux12_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lis2dux12.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](lis2dux12_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LIS2DUX12\_OPER\_MODE\_POWER\_DOWN](#a2319e5357a3b3933e46e0e445d8bb868)   0 |
| #define | [LIS2DUX12\_OPER\_MODE\_LOW\_POWER](#a03d276c97b5ee65f80ce301f78d8d620)   1 |
| #define | [LIS2DUX12\_OPER\_MODE\_HIGH\_RESOLUTION](#aee9aa425da279bd1f39a34954f76ec4d)   2 |
| #define | [LIS2DUX12\_OPER\_MODE\_HIGH\_FREQUENCY](#a91f64cdb166b4e3ef48d72f754c23f62)   3 |
| #define | [LIS2DUX12\_DT\_ODR\_OFF](#a94ab30f7ef8aec193a84188ccf63a21d)   0 |
| #define | [LIS2DUX12\_DT\_ODR\_1Hz\_ULP](#ae8f5f4224653c75ba0343d13d0588910)   1 /\* available in ultra-low power mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_3Hz\_ULP](#a4a85ef36d5836a6c216a36272c645cfb)   2 /\* available in ultra-low power mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_25Hz\_ULP](#af649bb985c44d6631e6fd1a0a91fbf85)   3 /\* available in ultra-low power mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_6Hz](#a7c83ff001a3ff25aaab5cbac32a56df0)   4 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_12Hz5](#a01ab37065a2bb53366adc7740af37d62)   5 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_25Hz](#a1daa6448cea439025041b74f5dc3e58f)   6 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_50Hz](#aea1f056b715ed59a38ddb4c8aac48804)   7 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_100Hz](#a3b40a334bea0de6546b783ab65e9f4dd)   8 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_200Hz](#a230b18cdf50c202d1bced583914332e1)   9 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_400Hz](#ae3dc67b51572e8f0c5d5ec3394d5d750)   10 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_800Hz](#a6a8105006b18fe6632fbce06c77bed52)   11 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_END](#a68214dc2825057ef3fa3e87a7ae1fcc1)   12 |
| #define | [LIS2DUX12\_DT\_FS\_2G](#a9793fcda818ea10e61e844a3b94cda62)   0 /\* 2g (0.061 mg/LSB) \*/ |
| #define | [LIS2DUX12\_DT\_FS\_4G](#ab50eb77d0d2bac9eb493ec0490f2b4f7)   1 /\* 4g (0.122 mg/LSB) \*/ |
| #define | [LIS2DUX12\_DT\_FS\_8G](#ad0119b9353cec4ff57ad4e6fe1c7c055)   2 /\* 8g (0.244 mg/LSB) \*/ |
| #define | [LIS2DUX12\_DT\_FS\_16G](#a6e29f5351f4eebe482648629024af77e)   3 /\* 16g (0.488 mg/LSB) \*/ |

## Macro Definition Documentation

## [◆ ](#a6e29f5351f4eebe482648629024af77e)LIS2DUX12\_DT\_FS\_16G

| #define LIS2DUX12\_DT\_FS\_16G   3 /\* 16g (0.488 mg/LSB) \*/ |
| --- |

## [◆ ](#a9793fcda818ea10e61e844a3b94cda62)LIS2DUX12\_DT\_FS\_2G

| #define LIS2DUX12\_DT\_FS\_2G   0 /\* 2g (0.061 mg/LSB) \*/ |
| --- |

## [◆ ](#ab50eb77d0d2bac9eb493ec0490f2b4f7)LIS2DUX12\_DT\_FS\_4G

| #define LIS2DUX12\_DT\_FS\_4G   1 /\* 4g (0.122 mg/LSB) \*/ |
| --- |

## [◆ ](#ad0119b9353cec4ff57ad4e6fe1c7c055)LIS2DUX12\_DT\_FS\_8G

| #define LIS2DUX12\_DT\_FS\_8G   2 /\* 8g (0.244 mg/LSB) \*/ |
| --- |

## [◆ ](#a3b40a334bea0de6546b783ab65e9f4dd)LIS2DUX12\_DT\_ODR\_100Hz

| #define LIS2DUX12\_DT\_ODR\_100Hz   8 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#a01ab37065a2bb53366adc7740af37d62)LIS2DUX12\_DT\_ODR\_12Hz5

| #define LIS2DUX12\_DT\_ODR\_12Hz5   5 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#ae8f5f4224653c75ba0343d13d0588910)LIS2DUX12\_DT\_ODR\_1Hz\_ULP

| #define LIS2DUX12\_DT\_ODR\_1Hz\_ULP   1 /\* available in ultra-low power mode \*/ |
| --- |

## [◆ ](#a230b18cdf50c202d1bced583914332e1)LIS2DUX12\_DT\_ODR\_200Hz

| #define LIS2DUX12\_DT\_ODR\_200Hz   9 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#a1daa6448cea439025041b74f5dc3e58f)LIS2DUX12\_DT\_ODR\_25Hz

| #define LIS2DUX12\_DT\_ODR\_25Hz   6 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#af649bb985c44d6631e6fd1a0a91fbf85)LIS2DUX12\_DT\_ODR\_25Hz\_ULP

| #define LIS2DUX12\_DT\_ODR\_25Hz\_ULP   3 /\* available in ultra-low power mode \*/ |
| --- |

## [◆ ](#a4a85ef36d5836a6c216a36272c645cfb)LIS2DUX12\_DT\_ODR\_3Hz\_ULP

| #define LIS2DUX12\_DT\_ODR\_3Hz\_ULP   2 /\* available in ultra-low power mode \*/ |
| --- |

## [◆ ](#ae3dc67b51572e8f0c5d5ec3394d5d750)LIS2DUX12\_DT\_ODR\_400Hz

| #define LIS2DUX12\_DT\_ODR\_400Hz   10 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#aea1f056b715ed59a38ddb4c8aac48804)LIS2DUX12\_DT\_ODR\_50Hz

| #define LIS2DUX12\_DT\_ODR\_50Hz   7 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#a7c83ff001a3ff25aaab5cbac32a56df0)LIS2DUX12\_DT\_ODR\_6Hz

| #define LIS2DUX12\_DT\_ODR\_6Hz   4 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#a6a8105006b18fe6632fbce06c77bed52)LIS2DUX12\_DT\_ODR\_800Hz

| #define LIS2DUX12\_DT\_ODR\_800Hz   11 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#a68214dc2825057ef3fa3e87a7ae1fcc1)LIS2DUX12\_DT\_ODR\_END

| #define LIS2DUX12\_DT\_ODR\_END   12 |
| --- |

## [◆ ](#a94ab30f7ef8aec193a84188ccf63a21d)LIS2DUX12\_DT\_ODR\_OFF

| #define LIS2DUX12\_DT\_ODR\_OFF   0 |
| --- |

## [◆ ](#a91f64cdb166b4e3ef48d72f754c23f62)LIS2DUX12\_OPER\_MODE\_HIGH\_FREQUENCY

| #define LIS2DUX12\_OPER\_MODE\_HIGH\_FREQUENCY   3 |
| --- |

## [◆ ](#aee9aa425da279bd1f39a34954f76ec4d)LIS2DUX12\_OPER\_MODE\_HIGH\_RESOLUTION

| #define LIS2DUX12\_OPER\_MODE\_HIGH\_RESOLUTION   2 |
| --- |

## [◆ ](#a03d276c97b5ee65f80ce301f78d8d620)LIS2DUX12\_OPER\_MODE\_LOW\_POWER

| #define LIS2DUX12\_OPER\_MODE\_LOW\_POWER   1 |
| --- |

## [◆ ](#a2319e5357a3b3933e46e0e445d8bb868)LIS2DUX12\_OPER\_MODE\_POWER\_DOWN

| #define LIS2DUX12\_OPER\_MODE\_POWER\_DOWN   0 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lis2dux12.h](lis2dux12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
