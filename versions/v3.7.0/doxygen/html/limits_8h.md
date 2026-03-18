---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/limits_8h.html
original_path: doxygen/html/limits_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

limits.h File Reference

[Go to the source code of this file.](limits_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SCHAR\_MAX](#a8c13fdd8c2840edf0cb04a65297037bb)   \_\_SCHAR\_MAX\_\_ |
| #define | [SCHAR\_MIN](#aa05d197000ad5c143ada0fcd9379b236)   (-[SCHAR\_MAX](#a8c13fdd8c2840edf0cb04a65297037bb) - 1) |
| #define | [CHAR\_MAX](#a778eefd6535a9d4b752fca5dd0af58db)   [SCHAR\_MAX](#a8c13fdd8c2840edf0cb04a65297037bb) |
| #define | [CHAR\_MIN](#a5d707bd32338557ced18c6ac76ca1b3a)   [SCHAR\_MIN](#aa05d197000ad5c143ada0fcd9379b236) |
| #define | [CHAR\_BIT](#a308d9dd2c0028ddb184b455bbd7865de)   \_\_CHAR\_BIT\_\_ |
| #define | [LONG\_BIT](#a88c78a5170af546a3417d28875fd3710)   (\_\_SIZEOF\_LONG\_\_ \* [CHAR\_BIT](#a308d9dd2c0028ddb184b455bbd7865de)) |
| #define | [WORD\_BIT](#af95e2cdeed2bb68c59e2c3d07b6c3d04)   (\_\_SIZEOF\_POINTER\_\_ \* [CHAR\_BIT](#a308d9dd2c0028ddb184b455bbd7865de)) |
| #define | [INT\_MAX](#a9ec306f36d50c7375e74f0d1c55a3a67)   \_\_INT\_MAX\_\_ |
| #define | [SHRT\_MAX](#a1f758438cb1c7bcf55da2431f5e319e6)   \_\_SHRT\_MAX\_\_ |
| #define | [LONG\_MAX](#a50fece4db74f09568b2938db583c5655)   \_\_LONG\_MAX\_\_ |
| #define | [LLONG\_MAX](#a23ec2cf7fc07ea8f817bbac758402baf)   \_\_LONG\_LONG\_MAX\_\_ |
| #define | [INT\_MIN](#a21658776274b3d146c674318b635a334)   (-[INT\_MAX](#a9ec306f36d50c7375e74f0d1c55a3a67) - 1) |
| #define | [SHRT\_MIN](#ae59de266aceffa1c258ac13f45fe0d18)   (-[SHRT\_MAX](#a1f758438cb1c7bcf55da2431f5e319e6) - 1) |
| #define | [LONG\_MIN](#ae8a44c5a7436466221e0f3859d02420f)   (-[LONG\_MAX](#a50fece4db74f09568b2938db583c5655) - 1L) |
| #define | [LLONG\_MIN](#af17a13b2ae0e9c24c020ac1f044f30c2)   (-[LLONG\_MAX](#a23ec2cf7fc07ea8f817bbac758402baf) - 1LL) |
| #define | [SSIZE\_MAX](#a2d6569aa794c2f23e90691e60d2f3ad2)   \_\_INT32\_MAX\_\_ |
| #define | [PATH\_MAX](#ae688d728e1acdfe5988c7db45d6f0166)   256 |

## Macro Definition Documentation

## [◆ ](#a308d9dd2c0028ddb184b455bbd7865de)CHAR\_BIT

| #define CHAR\_BIT   \_\_CHAR\_BIT\_\_ |
| --- |

## [◆ ](#a778eefd6535a9d4b752fca5dd0af58db)CHAR\_MAX

| #define CHAR\_MAX   [SCHAR\_MAX](#a8c13fdd8c2840edf0cb04a65297037bb) |
| --- |

## [◆ ](#a5d707bd32338557ced18c6ac76ca1b3a)CHAR\_MIN

| #define CHAR\_MIN   [SCHAR\_MIN](#aa05d197000ad5c143ada0fcd9379b236) |
| --- |

## [◆ ](#a9ec306f36d50c7375e74f0d1c55a3a67)INT\_MAX

| #define INT\_MAX   \_\_INT\_MAX\_\_ |
| --- |

## [◆ ](#a21658776274b3d146c674318b635a334)INT\_MIN

| #define INT\_MIN   (-[INT\_MAX](#a9ec306f36d50c7375e74f0d1c55a3a67) - 1) |
| --- |

## [◆ ](#a23ec2cf7fc07ea8f817bbac758402baf)LLONG\_MAX

| #define LLONG\_MAX   \_\_LONG\_LONG\_MAX\_\_ |
| --- |

## [◆ ](#af17a13b2ae0e9c24c020ac1f044f30c2)LLONG\_MIN

| #define LLONG\_MIN   (-[LLONG\_MAX](#a23ec2cf7fc07ea8f817bbac758402baf) - 1LL) |
| --- |

## [◆ ](#a88c78a5170af546a3417d28875fd3710)LONG\_BIT

| #define LONG\_BIT   (\_\_SIZEOF\_LONG\_\_ \* [CHAR\_BIT](#a308d9dd2c0028ddb184b455bbd7865de)) |
| --- |

## [◆ ](#a50fece4db74f09568b2938db583c5655)LONG\_MAX

| #define LONG\_MAX   \_\_LONG\_MAX\_\_ |
| --- |

## [◆ ](#ae8a44c5a7436466221e0f3859d02420f)LONG\_MIN

| #define LONG\_MIN   (-[LONG\_MAX](#a50fece4db74f09568b2938db583c5655) - 1L) |
| --- |

## [◆ ](#ae688d728e1acdfe5988c7db45d6f0166)PATH\_MAX

| #define PATH\_MAX   256 |
| --- |

## [◆ ](#a8c13fdd8c2840edf0cb04a65297037bb)SCHAR\_MAX

| #define SCHAR\_MAX   \_\_SCHAR\_MAX\_\_ |
| --- |

## [◆ ](#aa05d197000ad5c143ada0fcd9379b236)SCHAR\_MIN

| #define SCHAR\_MIN   (-[SCHAR\_MAX](#a8c13fdd8c2840edf0cb04a65297037bb) - 1) |
| --- |

## [◆ ](#a1f758438cb1c7bcf55da2431f5e319e6)SHRT\_MAX

| #define SHRT\_MAX   \_\_SHRT\_MAX\_\_ |
| --- |

## [◆ ](#ae59de266aceffa1c258ac13f45fe0d18)SHRT\_MIN

| #define SHRT\_MIN   (-[SHRT\_MAX](#a1f758438cb1c7bcf55da2431f5e319e6) - 1) |
| --- |

## [◆ ](#a2d6569aa794c2f23e90691e60d2f3ad2)SSIZE\_MAX

| #define SSIZE\_MAX   \_\_INT32\_MAX\_\_ |
| --- |

## [◆ ](#af95e2cdeed2bb68c59e2c3d07b6c3d04)WORD\_BIT

| #define WORD\_BIT   (\_\_SIZEOF\_POINTER\_\_ \* [CHAR\_BIT](#a308d9dd2c0028ddb184b455bbd7865de)) |
| --- |

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [limits.h](limits_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
