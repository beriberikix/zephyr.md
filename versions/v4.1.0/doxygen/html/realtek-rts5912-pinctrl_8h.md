---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/realtek-rts5912-pinctrl_8h.html
original_path: doxygen/html/realtek-rts5912-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

realtek-rts5912-pinctrl.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](realtek-rts5912-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [REALTEK\_RTS5912\_GPIO\_INOUT](#acaf6fce01a1687b4286a749ead4ca90c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* IN/OUT : 0 input 1 output \*/ |
| #define | [REALTEK\_RTS5912\_GPIO\_PINON](#a37c9b457ded69e287ac79d93d75392f1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* Input\_detect : 1 enable 0 disable \*/ |
| #define | [REALTEK\_RTS5912\_GPIO\_VOLT](#af6ac5662dc1122df9934acdfda1a972f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\* Pin Volt : 1 1.8V 0 3.3V \*/ |
| #define | [REALTEK\_RTS5912\_FUNC0](#aa068c89b25e53c56cebaa2c292f0d496)   0 /\* GPIO mode \*/ |
| #define | [REALTEK\_RTS5912\_FUNC1](#a320f452117e29ea363d8e92791d11a62)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) /\* Function mode use BIT0~2 \*/ |
| #define | [REALTEK\_RTS5912\_FUNC2](#a0f1aeb726f327dd57aa91fcd68fb96e7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [REALTEK\_RTS5912\_FUNC3](#a1cf29b9a5799e9ecc455e8f304114574)   (([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8)) | ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9))) |
| #define | [REALTEK\_RTS5912\_FUNC4](#a2f9db2ea5d8996c5374eb1c314f2b206)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [REALTEK\_RTS5912\_INPUT\_OUTPUT\_POS](#ad919b2c55c39409ce55e61c9a6c4b517)   0 |
| #define | [REALTEK\_RTS5912\_INPUT\_DETECTION\_POS](#a126ef964f014695a4ba2bb12f80df4b7)   1 |
| #define | [REALTEK\_RTS5912\_VOLTAGE\_POS](#a129d1a2771427bf45ebe1d68b86d1f52)   2 |
| #define | [REALTEK\_RTS5912\_DRV\_STR\_POS](#af2020d8bbae4e24b4e5f48ce1f4fc7f1)   11 |
| #define | [REALTEK\_RTS5912\_SLEW\_RATE\_POS](#af5aa6f81b75e84553e31401a798266f5)   12 |
| #define | [REALTEK\_RTS5912\_PD\_POS](#af8faf52c5ea35defe026cb4f6cc95cdc)   13 |
| #define | [REALTEK\_RTS5912\_PU\_POS](#ae3fc4f59fc38de4f3380b13eab30842d)   14 |
| #define | [REALTEK\_RTS5912\_SCHMITTER\_POS](#ac89f34fde098b5df324b3ed69f108aec)   15 |
| #define | [REALTEK\_RTS5912\_TYPE\_POS](#ab4802986241c477ce74d7ab082ef9ff3)   16 |
| #define | [REALTEK\_RTS5912\_HIGH\_LOW\_POS](#a67f5fb84972d53406c8c9e440815fe60)   17 |
| #define | [REALTEK\_RTS5912\_GPIO\_HIGH\_POS](#ab00c925ffba481594ed7216d41efa52a)   18 |
| #define | [REALTEK\_RTS5912\_GPIO\_HIGH\_MSK](#a7524cfe0cc5990bf5bc835d030deaf11)   0x3f |
| #define | [REALTEK\_RTS5912\_GPIO\_LOW\_POS](#a3f09fb1e1ad93e1fc1189ad5babbc533)   3 |
| #define | [REALTEK\_RTS5912\_GPIO\_LOW\_MSK](#a9cbb1539029aa9b58ffedb4b3ede0e93)   0x1f |
| #define | [FUNC0](#aa3ba064ba85ae0da9c55e7cdb8ea09b3)   [REALTEK\_RTS5912\_FUNC0](#aa068c89b25e53c56cebaa2c292f0d496) |
| #define | [FUNC1](#a3f9b8eb1b4789fef1da73f4eb041ddfc)   [REALTEK\_RTS5912\_FUNC1](#a320f452117e29ea363d8e92791d11a62) |
| #define | [FUNC2](#a0e8023a25dd46655b8eda5b0476ba169)   [REALTEK\_RTS5912\_FUNC2](#a0f1aeb726f327dd57aa91fcd68fb96e7) |
| #define | [FUNC3](#adeea02cdf0e8b64c27b6fad4d2b3b2b5)   [REALTEK\_RTS5912\_FUNC3](#a1cf29b9a5799e9ecc455e8f304114574) |
| #define | [FUNC4](#a769e96bef0ce818be7aa2cb0a0a67753)   [REALTEK\_RTS5912\_FUNC4](#a2f9db2ea5d8996c5374eb1c314f2b206) |
| #define | [REALTEK\_RTS5912\_PINMUX](#aa3e9ea3bc9606018c92e70d6728c8594)(n, f) |

## Macro Definition Documentation

## [◆ ](#aa3ba064ba85ae0da9c55e7cdb8ea09b3)FUNC0

| #define FUNC0   [REALTEK\_RTS5912\_FUNC0](#aa068c89b25e53c56cebaa2c292f0d496) |
| --- |

## [◆ ](#a3f9b8eb1b4789fef1da73f4eb041ddfc)FUNC1

| #define FUNC1   [REALTEK\_RTS5912\_FUNC1](#a320f452117e29ea363d8e92791d11a62) |
| --- |

## [◆ ](#a0e8023a25dd46655b8eda5b0476ba169)FUNC2

| #define FUNC2   [REALTEK\_RTS5912\_FUNC2](#a0f1aeb726f327dd57aa91fcd68fb96e7) |
| --- |

## [◆ ](#adeea02cdf0e8b64c27b6fad4d2b3b2b5)FUNC3

| #define FUNC3   [REALTEK\_RTS5912\_FUNC3](#a1cf29b9a5799e9ecc455e8f304114574) |
| --- |

## [◆ ](#a769e96bef0ce818be7aa2cb0a0a67753)FUNC4

| #define FUNC4   [REALTEK\_RTS5912\_FUNC4](#a2f9db2ea5d8996c5374eb1c314f2b206) |
| --- |

## [◆ ](#af2020d8bbae4e24b4e5f48ce1f4fc7f1)REALTEK\_RTS5912\_DRV\_STR\_POS

| #define REALTEK\_RTS5912\_DRV\_STR\_POS   11 |
| --- |

## [◆ ](#aa068c89b25e53c56cebaa2c292f0d496)REALTEK\_RTS5912\_FUNC0

| #define REALTEK\_RTS5912\_FUNC0   0 /\* GPIO mode \*/ |
| --- |

## [◆ ](#a320f452117e29ea363d8e92791d11a62)REALTEK\_RTS5912\_FUNC1

| #define REALTEK\_RTS5912\_FUNC1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) /\* Function mode use BIT0~2 \*/ |
| --- |

## [◆ ](#a0f1aeb726f327dd57aa91fcd68fb96e7)REALTEK\_RTS5912\_FUNC2

| #define REALTEK\_RTS5912\_FUNC2   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#a1cf29b9a5799e9ecc455e8f304114574)REALTEK\_RTS5912\_FUNC3

| #define REALTEK\_RTS5912\_FUNC3   (([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8)) | ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9))) |
| --- |

## [◆ ](#a2f9db2ea5d8996c5374eb1c314f2b206)REALTEK\_RTS5912\_FUNC4

| #define REALTEK\_RTS5912\_FUNC4   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#a7524cfe0cc5990bf5bc835d030deaf11)REALTEK\_RTS5912\_GPIO\_HIGH\_MSK

| #define REALTEK\_RTS5912\_GPIO\_HIGH\_MSK   0x3f |
| --- |

## [◆ ](#ab00c925ffba481594ed7216d41efa52a)REALTEK\_RTS5912\_GPIO\_HIGH\_POS

| #define REALTEK\_RTS5912\_GPIO\_HIGH\_POS   18 |
| --- |

## [◆ ](#acaf6fce01a1687b4286a749ead4ca90c)REALTEK\_RTS5912\_GPIO\_INOUT

| #define REALTEK\_RTS5912\_GPIO\_INOUT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* IN/OUT : 0 input 1 output \*/ |
| --- |

## [◆ ](#a9cbb1539029aa9b58ffedb4b3ede0e93)REALTEK\_RTS5912\_GPIO\_LOW\_MSK

| #define REALTEK\_RTS5912\_GPIO\_LOW\_MSK   0x1f |
| --- |

## [◆ ](#a3f09fb1e1ad93e1fc1189ad5babbc533)REALTEK\_RTS5912\_GPIO\_LOW\_POS

| #define REALTEK\_RTS5912\_GPIO\_LOW\_POS   3 |
| --- |

## [◆ ](#a37c9b457ded69e287ac79d93d75392f1)REALTEK\_RTS5912\_GPIO\_PINON

| #define REALTEK\_RTS5912\_GPIO\_PINON   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* Input\_detect : 1 enable 0 disable \*/ |
| --- |

## [◆ ](#af6ac5662dc1122df9934acdfda1a972f)REALTEK\_RTS5912\_GPIO\_VOLT

| #define REALTEK\_RTS5912\_GPIO\_VOLT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\* Pin Volt : 1 1.8V 0 3.3V \*/ |
| --- |

## [◆ ](#a67f5fb84972d53406c8c9e440815fe60)REALTEK\_RTS5912\_HIGH\_LOW\_POS

| #define REALTEK\_RTS5912\_HIGH\_LOW\_POS   17 |
| --- |

## [◆ ](#a126ef964f014695a4ba2bb12f80df4b7)REALTEK\_RTS5912\_INPUT\_DETECTION\_POS

| #define REALTEK\_RTS5912\_INPUT\_DETECTION\_POS   1 |
| --- |

## [◆ ](#ad919b2c55c39409ce55e61c9a6c4b517)REALTEK\_RTS5912\_INPUT\_OUTPUT\_POS

| #define REALTEK\_RTS5912\_INPUT\_OUTPUT\_POS   0 |
| --- |

## [◆ ](#af8faf52c5ea35defe026cb4f6cc95cdc)REALTEK\_RTS5912\_PD\_POS

| #define REALTEK\_RTS5912\_PD\_POS   13 |
| --- |

## [◆ ](#aa3e9ea3bc9606018c92e70d6728c8594)REALTEK\_RTS5912\_PINMUX

| #define REALTEK\_RTS5912\_PINMUX | ( |  | *n*, |
| --- | --- | --- | --- |
|  |  |  | *f* ) |

**Value:**

(((((n) >> 5) & [REALTEK\_RTS5912\_GPIO\_HIGH\_MSK](#a7524cfe0cc5990bf5bc835d030deaf11)) << [REALTEK\_RTS5912\_GPIO\_HIGH\_POS](#ab00c925ffba481594ed7216d41efa52a)) | \

(((n) & [REALTEK\_RTS5912\_GPIO\_LOW\_MSK](#a9cbb1539029aa9b58ffedb4b3ede0e93)) << [REALTEK\_RTS5912\_GPIO\_LOW\_POS](#a3f09fb1e1ad93e1fc1189ad5babbc533)) | (f))

[REALTEK\_RTS5912\_GPIO\_LOW\_POS](#a3f09fb1e1ad93e1fc1189ad5babbc533)

#define REALTEK\_RTS5912\_GPIO\_LOW\_POS

**Definition** realtek-rts5912-pinctrl.h:35

[REALTEK\_RTS5912\_GPIO\_HIGH\_MSK](#a7524cfe0cc5990bf5bc835d030deaf11)

#define REALTEK\_RTS5912\_GPIO\_HIGH\_MSK

**Definition** realtek-rts5912-pinctrl.h:34

[REALTEK\_RTS5912\_GPIO\_LOW\_MSK](#a9cbb1539029aa9b58ffedb4b3ede0e93)

#define REALTEK\_RTS5912\_GPIO\_LOW\_MSK

**Definition** realtek-rts5912-pinctrl.h:36

[REALTEK\_RTS5912\_GPIO\_HIGH\_POS](#ab00c925ffba481594ed7216d41efa52a)

#define REALTEK\_RTS5912\_GPIO\_HIGH\_POS

**Definition** realtek-rts5912-pinctrl.h:33

## [◆ ](#ae3fc4f59fc38de4f3380b13eab30842d)REALTEK\_RTS5912\_PU\_POS

| #define REALTEK\_RTS5912\_PU\_POS   14 |
| --- |

## [◆ ](#ac89f34fde098b5df324b3ed69f108aec)REALTEK\_RTS5912\_SCHMITTER\_POS

| #define REALTEK\_RTS5912\_SCHMITTER\_POS   15 |
| --- |

## [◆ ](#af5aa6f81b75e84553e31401a798266f5)REALTEK\_RTS5912\_SLEW\_RATE\_POS

| #define REALTEK\_RTS5912\_SLEW\_RATE\_POS   12 |
| --- |

## [◆ ](#ab4802986241c477ce74d7ab082ef9ff3)REALTEK\_RTS5912\_TYPE\_POS

| #define REALTEK\_RTS5912\_TYPE\_POS   16 |
| --- |

## [◆ ](#a129d1a2771427bf45ebe1d68b86d1f52)REALTEK\_RTS5912\_VOLTAGE\_POS

| #define REALTEK\_RTS5912\_VOLTAGE\_POS   2 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [realtek-rts5912-pinctrl.h](realtek-rts5912-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
