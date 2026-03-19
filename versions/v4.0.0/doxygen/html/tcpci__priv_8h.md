---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/tcpci__priv_8h.html
original_path: doxygen/html/tcpci__priv_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tcpci\_priv.h File Reference

Helper functions to use by the TCPCI-compliant drivers.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h_source.md)>`  
`#include <[zephyr/usb_c/usbc.h](usbc_8h_source.md)>`

[Go to the source code of this file.](tcpci__priv_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [tcpci\_reg\_dump\_map](structtcpci__reg__dump__map.md) |
|  | Structure used to bind the register address to name in registers dump. [More...](structtcpci__reg__dump__map.md#details) |

| Macros | |
| --- | --- |
| #define | [TCPCI\_STD\_REGS\_SIZE](#a031fe5b188cbe9b4e80e9cff0c845eda)   38 |
|  | Size of the array containing the standard registers used by tcpci dump command. |

| Functions | |
| --- | --- |
| int | [tcpci\_read\_reg8](#aaad4be0dbc4c31e9d3438b7f8a3e8433) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Function to read the 8-bit register of TCPCI device. |
| int | [tcpci\_write\_reg8](#abbe63527659134a5bc14d6ecefabb0af) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Function to write a value to the 8-bit register of TCPCI device. |
| int | [tcpci\_update\_reg8](#a2f4e5571a7f272dd968dc002d70ef3f4) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Function to read and update part of the 8-bit register of TCPCI device The function is NOT performing this operation atomically. |
| int | [tcpci\_read\_reg16](#a00557a03647d6bd1ecba157ffff40e46) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value) |
|  | Function to read the 16-bit register of TCPCI device. |
| int | [tcpci\_write\_reg16](#a7db13212d494bcc8c98190f8670fcd34) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value) |
|  | Function to write a value to the 16-bit register of TCPCI device. |
| enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) | [tcpci\_alert\_reg\_to\_enum](#abafd9380a335483525d8ff5b2b9e2306) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg) |
|  | Function that converts the TCPCI alert register to the [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed "TCPC Alert bits.") enum The hard reset value takes priority, where the rest are returned in the bit order from least significant to most significant. |
| int | [tcpci\_tcpm\_get\_cc](#ade1aa43041be0cc1abcf074b8e4e07e9) (const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \*bus, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc1, enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \*cc2) |
|  | Function that reads the CC status registers and converts read values to enums representing voltages state and partner detection status. |

| Variables | |
| --- | --- |
| const struct [tcpci\_reg\_dump\_map](structtcpci__reg__dump__map.md) | [tcpci\_std\_regs](#ab2204d54c7483fb06f02dda83b0066f8) [38] |
|  | Array containing the standard TCPCI registers list. |

## Detailed Description

Helper functions to use by the TCPCI-compliant drivers.

This file contains generic TCPCI functions that may be used by the drivers to TCPCI-compliant devices that want to implement vendor-specific functionality without the need to reimplement the TCPCI generic functionality and register operations.

## Macro Definition Documentation

## [◆ ](#a031fe5b188cbe9b4e80e9cff0c845eda)TCPCI\_STD\_REGS\_SIZE

| #define TCPCI\_STD\_REGS\_SIZE   38 |
| --- |

Size of the array containing the standard registers used by tcpci dump command.

## Function Documentation

## [◆ ](#abafd9380a335483525d8ff5b2b9e2306)tcpci\_alert\_reg\_to\_enum()

| enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed) tcpci\_alert\_reg\_to\_enum | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

Function that converts the TCPCI alert register to the [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed "TCPC Alert bits.") enum The hard reset value takes priority, where the rest are returned in the bit order from least significant to most significant.

Parameters
:   | reg | Value of the TCPCI alert register. This parameter must have value other than zero. |
    | --- | --- |

Returns
:   enum [tcpc\_alert](group__usb__type__c__port__controller__api.md#ga4687047910cad0dd970bbd28adcf22ed "TCPC Alert bits.") Value of one of the flags being set in the alert register

## [◆ ](#a00557a03647d6bd1ecba157ffff40e46)tcpci\_read\_reg16()

| int tcpci\_read\_reg16 | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *value* ) |

Function to read the 16-bit register of TCPCI device.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Address of TCPCI register |
    | value | Pointer to variable that will store the register value |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#aaad4be0dbc4c31e9d3438b7f8a3e8433)tcpci\_read\_reg8()

| int tcpci\_read\_reg8 | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *value* ) |

Function to read the 8-bit register of TCPCI device.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Address of TCPCI register |
    | value | Pointer to variable that will store the register value |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#ade1aa43041be0cc1abcf074b8e4e07e9)tcpci\_tcpm\_get\_cc()

| int tcpci\_tcpm\_get\_cc | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \* | *cc1*, |
|  |  | enum [tc\_cc\_voltage\_state](group__usb__type__c.md#ga64e32ec2da97f70fd5b96975317cb92c) \* | *cc2* ) |

Function that reads the CC status registers and converts read values to enums representing voltages state and partner detection status.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | cc1 | pointer to variable where detected CC1 voltage state will be stored |
    | cc2 | pointer to variable where detected CC2 voltage state will be stored |

Returns
:   -EINVAL if cc1 or cc2 pointer is NULL
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a2f4e5571a7f272dd968dc002d70ef3f4)tcpci\_update\_reg8()

| int tcpci\_update\_reg8 | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) |

Function to read and update part of the 8-bit register of TCPCI device The function is NOT performing this operation atomically.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Address of TCPCI register |
    | mask | Bitmask specifying which bits of the device register will be modified |
    | value | Value that will be written to the device register after being ANDed with mask |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#a7db13212d494bcc8c98190f8670fcd34)tcpci\_write\_reg16()

| int tcpci\_write\_reg16 | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *value* ) |

Function to write a value to the 16-bit register of TCPCI device.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Address of TCPCI register |
    | value | Value that will be written to the device register |

Returns
:   int Status of I2C operation, 0 in case of success

## [◆ ](#abbe63527659134a5bc14d6ecefabb0af)tcpci\_write\_reg8()

| int tcpci\_write\_reg8 | ( | const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | *bus*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) |

Function to write a value to the 8-bit register of TCPCI device.

Parameters
:   | bus | I2C bus |
    | --- | --- |
    | reg | Address of TCPCI register |
    | value | Value that will be written to the device register |

Returns
:   int Status of I2C operation, 0 in case of success

## Variable Documentation

## [◆ ](#ab2204d54c7483fb06f02dda83b0066f8)tcpci\_std\_regs

| | const struct [tcpci\_reg\_dump\_map](structtcpci__reg__dump__map.md) tcpci\_std\_regs[38] | | --- | | extern |
| --- | --- | --- |

Array containing the standard TCPCI registers list.

If the TCPC driver contain any vendor-specific registers, it may override the TCPCI dump\_std\_reg function tp dump them and should also dump the standard registers using this array.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [tcpci\_priv.h](tcpci__priv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
