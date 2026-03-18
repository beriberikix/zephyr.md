---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2mfd_2npm1300_8h.html
original_path: doxygen/html/drivers_2mfd_2npm1300_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm1300.h File Reference

`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](drivers_2mfd_2npm1300_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [mfd\_npm1300\_event\_t](group__mdf__interface__npm1300.md#gad15bf59ebf3c5572347e939c4c2e6989) {     [NPM1300\_EVENT\_CHG\_COMPLETED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a04241a0410734d82aee28c515a0a92c0) , [NPM1300\_EVENT\_CHG\_ERROR](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a153a82c7f6bac3393267c4ca0f16b8e3) , [NPM1300\_EVENT\_BATTERY\_DETECTED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a8524187e6aa6ef0683265b1340cc117f) , [NPM1300\_EVENT\_BATTERY\_REMOVED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a98ff199ec155bd8ce7e42ede4aa90c78) ,     [NPM1300\_EVENT\_SHIPHOLD\_PRESS](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a70c303c4863161a086ddfe07fe315cd0) , [NPM1300\_EVENT\_SHIPHOLD\_RELEASE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989abb790b641b8d0a8d87b2fb5aabbc5bae) , [NPM1300\_EVENT\_WATCHDOG\_WARN](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a182e6c0806f1d21802a628ccdf92c018) , [NPM1300\_EVENT\_VBUS\_DETECTED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989aebe54d5f1704b81873ca2dce17e44a47) ,     [NPM1300\_EVENT\_VBUS\_REMOVED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a94a3133140147f38e358ac97ed45ccaf) , [NPM1300\_EVENT\_GPIO0\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a16f39a059833d1bb848c1e675748b582) , [NPM1300\_EVENT\_GPIO1\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a82fe1a2bcc5d2a4638d71f2b18fa73c7) , [NPM1300\_EVENT\_GPIO2\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a87ca56a02af057ff1920c7b2537ccecc) ,     [NPM1300\_EVENT\_GPIO3\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a89b2ea4f842c92b118b36003b6b8175a) , [NPM1300\_EVENT\_GPIO4\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a0a9d44a031ee84024ab13cccf2441f0e) , [NPM1300\_EVENT\_MAX](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a28557da1ca76c99c0a646cb687ef6291)   } |

| Functions | |
| --- | --- |
| int | [mfd\_npm1300\_reg\_read\_burst](group__mdf__interface__npm1300.md#ga021909959af74df2d324c7a98ce30c96) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read multiple registers from npm1300. |
| int | [mfd\_npm1300\_reg\_read](group__mdf__interface__npm1300.md#gaf068cde6e9482ee498429f75ab30c851) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Read single register from npm1300. |
| int | [mfd\_npm1300\_reg\_write](group__mdf__interface__npm1300.md#ga36e6db4a42e0ef3db7e63fcaad98d8cf) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | Write single register to npm1300. |
| int | [mfd\_npm1300\_reg\_write2](group__mdf__interface__npm1300.md#ga9bc9a9ae79181004f1303c12e2158fc7) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data1, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data2) |
|  | Write two registers to npm1300. |
| int | [mfd\_npm1300\_reg\_update](group__mdf__interface__npm1300.md#gade28611b9ee6caee19d62f4de6f428f9) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | Update selected bits in npm1300 register. |
| int | [mfd\_npm1300\_set\_timer](group__mdf__interface__npm1300.md#gae009c00f3935a655631aef7b00efbffb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms) |
|  | Write npm1300 timer register. |
| int | [mfd\_npm1300\_reset](group__mdf__interface__npm1300.md#ga470c32ccd5eb357bbf7578ceb57be686) (const struct [device](structdevice.md) \*dev) |
|  | npm1300 full power reset |
| int | [mfd\_npm1300\_hibernate](group__mdf__interface__npm1300.md#ga8ebf64d5161863d8cf70179e5d9bc8e6) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms) |
|  | npm1300 hibernate |
| int | [mfd\_npm1300\_add\_callback](group__mdf__interface__npm1300.md#ga2ea73b039df7ae7a26b67ffe96de8cf0) (const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Add npm1300 event callback. |
| int | [mfd\_npm1300\_remove\_callback](group__mdf__interface__npm1300.md#ga917ef06548659c0e447081ac475b4624) (const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Remove npm1300 event callback. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [npm1300.h](drivers_2mfd_2npm1300_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
