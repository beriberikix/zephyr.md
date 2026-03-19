---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2mfd_2axp192_8h.html
original_path: doxygen/html/drivers_2mfd_2axp192_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

axp192.h File Reference

`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](drivers_2mfd_2axp192_8h_source.md)

| Macros | |
| --- | --- |
| #define | [AXP192\_GPIO\_FUNC\_VALID](#a61d7d88bead4733fedcbfb70f8ada464)(func) |
|  | Check if a given GPIO function value is valid. |
| #define | [AXP192\_GPIO\_MAX\_NUM](#a0df71981c80a3c46e168287c39df88ee)   6U |
|  | Maximum number of GPIOs supported by AXP192 PMIC. |

| Enumerations | |
| --- | --- |
| enum | [axp192\_gpio\_func](#ac92e5fa77591e02e49570d1a1c38e249) {     [AXP192\_GPIO\_FUNC\_INPUT](#ac92e5fa77591e02e49570d1a1c38e249ab8eee3f4b6ce22594b90d7e49e4927df) = BIT(0) , [AXP192\_GPIO\_FUNC\_OUTPUT\_OD](#ac92e5fa77591e02e49570d1a1c38e249af1c2244571c0a3b12c0ae94c583c1a4b) = BIT(1) , [AXP192\_GPIO\_FUNC\_OUTPUT\_LOW](#ac92e5fa77591e02e49570d1a1c38e249a8d006f1e4284057f5b952b236729c5f5) = BIT(2) , [AXP192\_GPIO\_FUNC\_LDO](#ac92e5fa77591e02e49570d1a1c38e249ae9f961ad84c38f3315e3cdb25ede9328) = BIT(3) ,     [AXP192\_GPIO\_FUNC\_ADC](#ac92e5fa77591e02e49570d1a1c38e249ab3a2622cccb9ec1cdf22ddd5ac75ae6a) = BIT(4) , [AXP192\_GPIO\_FUNC\_PWM](#ac92e5fa77591e02e49570d1a1c38e249a2634f857f19e03ab8337780025c25579) = BIT(5) , [AXP192\_GPIO\_FUNC\_FLOAT](#ac92e5fa77591e02e49570d1a1c38e249a69c1f986672389305a3000b83a12417f) = BIT(6) , [AXP192\_GPIO\_FUNC\_CHARGE\_CTL](#ac92e5fa77591e02e49570d1a1c38e249a5955f43848da067d9134790f9fe1c240) = BIT(7) ,     [AXP192\_GPIO\_FUNC\_INVALID](#ac92e5fa77591e02e49570d1a1c38e249ad16e246ca71f2e865cccf1b4ad2f9286)   } |
|  | GPIO function type. [More...](#ac92e5fa77591e02e49570d1a1c38e249) |

| Functions | |
| --- | --- |
| int | [mfd\_axp192\_gpio\_func\_ctrl](group__mdf__interface__axp192.md#ga61c3f46791f4efa08ee45fc85dc32c81) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*client\_dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, enum [axp192\_gpio\_func](#ac92e5fa77591e02e49570d1a1c38e249) func) |
|  | Request a GPIO pin to be configured to a specific function. |
| int | [mfd\_axp192\_gpio\_func\_get](group__mdf__interface__axp192.md#ga29db6e44c801fecfa1df2d9da93c2e0b) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, enum [axp192\_gpio\_func](#ac92e5fa77591e02e49570d1a1c38e249) \*func) |
|  | Read out current configuration of a specific GPIO pin. |
| int | [mfd\_axp192\_gpio\_pd\_ctrl](group__mdf__interface__axp192.md#ga8db91c44adbf8ca6f727e2deb0aa96dd) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable pull-down on specified GPIO pin. |
| int | [mfd\_axp192\_gpio\_pd\_get](group__mdf__interface__axp192.md#gabdacd1e10bacf9f0393beb65327eaeea) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*enabled) |
|  | Read out the current pull-down configuration of a specific GPIO. |
| int | [mfd\_axp192\_gpio\_read\_port](group__mdf__interface__axp192.md#gaa12241d0655122f05da06dc506d2a5c0) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read GPIO port. |
| int | [mfd\_axp192\_gpio\_write\_port](group__mdf__interface__axp192.md#ga7570c8657918c15c71fddca264bce10e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | Write GPIO port. |

## Macro Definition Documentation

## [◆ ](#a61d7d88bead4733fedcbfb70f8ada464)AXP192\_GPIO\_FUNC\_VALID

| #define AXP192\_GPIO\_FUNC\_VALID | ( |  | *func* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(func < [AXP192\_GPIO\_FUNC\_INVALID](#ac92e5fa77591e02e49570d1a1c38e249ad16e246ca71f2e865cccf1b4ad2f9286))

[AXP192\_GPIO\_FUNC\_INVALID](#ac92e5fa77591e02e49570d1a1c38e249ad16e246ca71f2e865cccf1b4ad2f9286)

@ AXP192\_GPIO\_FUNC\_INVALID

**Definition** axp192.h:32

Check if a given GPIO function value is valid.

## [◆ ](#a0df71981c80a3c46e168287c39df88ee)AXP192\_GPIO\_MAX\_NUM

| #define AXP192\_GPIO\_MAX\_NUM   6U |
| --- |

Maximum number of GPIOs supported by AXP192 PMIC.

## Enumeration Type Documentation

## [◆ ](#ac92e5fa77591e02e49570d1a1c38e249)axp192\_gpio\_func

| enum [axp192\_gpio\_func](#ac92e5fa77591e02e49570d1a1c38e249) |
| --- |

GPIO function type.

Only one function can be configured per GPIO.

| Enumerator | |
| --- | --- |
| AXP192\_GPIO\_FUNC\_INPUT |  |
| AXP192\_GPIO\_FUNC\_OUTPUT\_OD |  |
| AXP192\_GPIO\_FUNC\_OUTPUT\_LOW |  |
| AXP192\_GPIO\_FUNC\_LDO |  |
| AXP192\_GPIO\_FUNC\_ADC |  |
| AXP192\_GPIO\_FUNC\_PWM |  |
| AXP192\_GPIO\_FUNC\_FLOAT |  |
| AXP192\_GPIO\_FUNC\_CHARGE\_CTL |  |
| AXP192\_GPIO\_FUNC\_INVALID |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [axp192.h](drivers_2mfd_2axp192_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
