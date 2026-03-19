---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2emul_8h.html
original_path: doxygen/html/drivers_2emul_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/drivers/espi_emul.h](espi__emul_8h_source.md)>`  
`#include <[zephyr/drivers/i2c_emul.h](i2c__emul_8h_source.md)>`  
`#include <[zephyr/drivers/spi_emul.h](spi__emul_8h_source.md)>`  
`#include <[zephyr/drivers/mspi_emul.h](mspi__emul_8h_source.md)>`  
`#include <[zephyr/drivers/uart_emul.h](uart__emul_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](drivers_2emul_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [emul\_link\_for\_bus](structemul__link__for__bus.md) |
|  | Structure uniquely identifying a device to be emulated. [More...](structemul__link__for__bus.md#details) |
| struct | [emul\_list\_for\_bus](structemul__list__for__bus.md) |
|  | List of emulators attached to a bus. [More...](structemul__list__for__bus.md#details) |
| struct | [no\_bus\_emul](structno__bus__emul.md) |
|  | Emulator API stub when an emulator is not actually placed on a bus. [More...](structno__bus__emul.md#details) |
| struct | [emul](structemul.md) |
|  | An emulator instance - represents the *target* emulated device/peripheral that is interacted with through an emulated bus. [More...](structemul.md#details) |
| union | [emul::bus](unionemul_1_1bus.md) |
|  | Pointer to the emulated bus node. [More...](unionemul_1_1bus.md#details) |

| Macros | |
| --- | --- |
| #define | [EMUL\_DT\_NAME\_GET](group__io__emulators.md#gac1638c8cad48dab50f9ebc83592236db)(node\_id) |
|  | Use the devicetree node identifier as a unique name. |
| #define | [EMUL\_DT\_DEFINE](group__io__emulators.md#gad6292e3cd7f17a3600be396777f304c8)(node\_id, init\_fn, data\_ptr, cfg\_ptr, bus\_api, \_backend\_api) |
|  | Define a new emulator. |
| #define | [EMUL\_DT\_INST\_DEFINE](group__io__emulators.md#gafe7f4912bcffed1366ce07d024a4f977)(inst, ...) |
|  | Like [EMUL\_DT\_DEFINE()](group__io__emulators.md#gad6292e3cd7f17a3600be396777f304c8 "Define a new emulator."), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier. |
| #define | [EMUL\_DT\_GET](group__io__emulators.md#ga300d997df388118ae380e79b972f85cf)(node\_id) |
|  | Get a const struct emul\* from a devicetree node identifier. |
| #define | [EMUL\_DT\_GET\_OR\_NULL](group__io__emulators.md#gab37b4f8b4c434ca38f523eb6391d4e3b)(node\_id) |
|  | Utility macro to obtain an optional reference to an emulator. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [emul\_init\_t](group__io__emulators.md#gaa6129de6e0edef345242559a3dac3a50)) (const struct [emul](structemul.md) \*[emul](structemul.md), const struct [device](structdevice.md) \*parent) |
|  | Standard callback for emulator initialisation providing the initialiser record and the device that calls the emulator functions. |

| Enumerations | |
| --- | --- |
| enum | [emul\_bus\_type](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa) {     [EMUL\_BUS\_TYPE\_I2C](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa37469f6df0ab808efe8d8a28f3424b5f) , [EMUL\_BUS\_TYPE\_ESPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa58714c3eeb3b9828fab041bd9a9f6ec1) , [EMUL\_BUS\_TYPE\_SPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa037e86fa4d585eac9420053d869b423a) , [EMUL\_BUS\_TYPE\_MSPI](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa532ba489c52ce6919751fc1a45f70a46) ,     [EMUL\_BUS\_TYPE\_UART](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaae93177d41e38aa873c603fb606db13b6) , [EMUL\_BUS\_TYPE\_NONE](group__io__emulators.md#gga39b7a9438507b0be95038fe9464762aaa942dd8fbb58d92fc987b0b2715a4a15d)   } |
|  | The types of supported buses. [More...](group__io__emulators.md#ga39b7a9438507b0be95038fe9464762aa) |

| Functions | |
| --- | --- |
| int | [emul\_init\_for\_bus](group__io__emulators.md#gad587b2852a182e1a7fdcb3b056d898f1) (const struct [device](structdevice.md) \*dev) |
|  | Set up a list of emulators. |
| const struct [emul](structemul.md) \* | [emul\_get\_binding](group__io__emulators.md#gaad94c1e07998417cb9aa06d03be3b280) (const char \*name) |
|  | Retrieve the emul structure for an emulator by name. |
|  | [DT\_FOREACH\_STATUS\_OKAY\_NODE](#a6b4463d5ce37aa4a16f66e8981be6007) (Z\_MAYBE\_EMUL\_DECLARE\_INTERNAL) |

## Function Documentation

## [◆ ](#a6b4463d5ce37aa4a16f66e8981be6007)DT\_FOREACH\_STATUS\_OKAY\_NODE()

| DT\_FOREACH\_STATUS\_OKAY\_NODE | ( | Z\_MAYBE\_EMUL\_DECLARE\_INTERNAL |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul.h](drivers_2emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
