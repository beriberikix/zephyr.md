---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/input__kbd__matrix_8h.html
original_path: doxygen/html/input__kbd__matrix_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_kbd\_matrix.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/sys_clock.h](include_2zephyr_2sys__clock_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](input__kbd__matrix_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md) |
|  | Keyboard matrix internal APIs. [More...](structinput__kbd__matrix__api.md#details) |
| struct | [input\_kbd\_matrix\_common\_config](structinput__kbd__matrix__common__config.md) |
|  | Common keyboard matrix config. [More...](structinput__kbd__matrix__common__config.md#details) |
| struct | [input\_kbd\_matrix\_common\_data](structinput__kbd__matrix__common__data.md) |
|  | Common keyboard matrix data. [More...](structinput__kbd__matrix__common__data.md#details) |

| Macros | |
| --- | --- |
| #define | [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_NONE](group__input__kbd__matrix.md#ga2f35f23d426f93f71057a31f612a88de)   -1 |
|  | Special drive\_column argument for not driving any column. |
| #define | [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_ALL](group__input__kbd__matrix.md#ga6d27ba5612c09d80087e854b21fb9e65)   -2 |
|  | Special drive\_column argument for driving all the columns. |
| #define | [INPUT\_KBD\_MATRIX\_SCAN\_OCURRENCES](group__input__kbd__matrix.md#ga80a384d2041dcee27d7940a1e408d82a)   30U |
|  | Number of tracked scan cycles. |
| #define | [PRIkbdrow](group__input__kbd__matrix.md#ga1343b97a8b072f8ed362e8a4f242bdd1)   "%02x" |
| #define | [INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST](group__input__kbd__matrix.md#gaec0209680e18da8584bdf41e5229aaae) |
| #define | [INPUT\_KBD\_MATRIX\_ROW\_BITS](group__input__kbd__matrix.md#gae395cd03c295673dc9563c252ba7e022)   [NUM\_BITS](util_8h.md#afa27c06d0ad6b949289431ad75f104ab)([kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86)) |
|  | Maximum number of rows. |
| #define | [INPUT\_KBD\_MATRIX\_DATA\_NAME](group__input__kbd__matrix.md#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, name) |
| #define | [INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL](group__input__kbd__matrix.md#gac1a4389b1afeab9c48a15c024bfb0cac)(node\_id, \_row\_size, \_col\_size) |
|  | Defines the common keyboard matrix support data from devicetree, specify row and col count. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_DEFINE](group__input__kbd__matrix.md#ga512bea2ca97569f465074ca8f231a0a3)(node\_id) |
|  | Defines the common keyboard matrix support data from devicetree. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE\_ROW\_COL](group__input__kbd__matrix.md#ga1d3fe52f10c75dc4c32c8583c05fb2a2)(inst, row\_size, col\_size) |
|  | Defines the common keyboard matrix support data from devicetree instance, specify row and col count. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE](group__input__kbd__matrix.md#gab3ea5b7d597574b32ced16604648a6d2)(inst) |
|  | Defines the common keyboard matrix support data from devicetree instance. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL](group__input__kbd__matrix.md#ga5ad9141616b4a63068bfbe8004bba67d)(node\_id, \_api, \_row\_size, \_col\_size) |
|  | Initialize common keyboard matrix config from devicetree, specify row and col count. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT](group__input__kbd__matrix.md#ga3281b4e5909a1c07d8190092bc31cb12)(node\_id, api) |
|  | Initialize common keyboard matrix config from devicetree. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT\_ROW\_COL](group__input__kbd__matrix.md#gac6baf9b284f0796cdd5dbcef338f9588)(inst, api, row\_size, col\_size) |
|  | Initialize common keyboard matrix config from devicetree instance, specify row and col count. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT](group__input__kbd__matrix.md#gab19b4a8c66c5540b4e690459655f92fd)(inst, api) |
|  | Initialize common keyboard matrix config from devicetree instance. |
| #define | [INPUT\_KBD\_STRUCT\_CHECK](group__input__kbd__matrix.md#ga352d484344c93c30f5cad75551793377)(config, data) |
|  | Validate the offset of the common data structures. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [kbd\_row\_t](group__input__kbd__matrix.md#gac7d5c811da0c9ab2660be3c3f2fcfe86) |
|  | Row entry data type. |

| Functions | |
| --- | --- |
| int | [input\_kbd\_matrix\_actual\_key\_mask\_set](group__input__kbd__matrix.md#gab35f4bf523760933294242ccc8226490) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) row, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) col, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Enables or disables a specific row, column combination in the actual key mask. |
| void | [input\_kbd\_matrix\_poll\_start](group__input__kbd__matrix.md#gaf97b6ff410631f111d7c3a7aa7f64171) (const struct [device](structdevice.md) \*dev) |
|  | Start scanning the keyboard matrix. |
| void | [input\_kbd\_matrix\_drive\_column\_hook](group__input__kbd__matrix.md#ga6d843c7213bf5c0af9003c165a5f3e03) (const struct [device](structdevice.md) \*dev, int col) |
|  | Drive column hook. |
| int | [input\_kbd\_matrix\_common\_init](group__input__kbd__matrix.md#ga938dc38da7e81e5a68b8b9dc585c4bab) (const struct [device](structdevice.md) \*dev) |
|  | Common function to initialize a keyboard matrix device at init time. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_kbd\_matrix.h](input__kbd__matrix_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
