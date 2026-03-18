---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pinctrl-rcar-common_8h.html
original_path: doxygen/html/pinctrl-rcar-common_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rcar-common.h File Reference

[Go to the source code of this file.](pinctrl-rcar-common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IPSR](#adbde593c77123c64c2f63e4e8f508ccb)(bank, shift, func) |
|  | Utility macro to build IPSR property entry. |
| #define | [PIN\_NOGPSR\_START](#a165cdeba11c616c3c14e1d02e6c4d552)   1024U |
| #define | [RCAR\_GP\_PIN](#a840b9b9f9f5513088896bbb960724d8f)(bank, pin) |
|  | Utility macro to encode a GPIO capable pin. |
| #define | [RCAR\_NOGP\_PIN](#a6e8b18f9578375cb325e9e5b204b6c66)(pin) |
|  | Utility macro to encode a non capable GPIO pin. |
| #define | [IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(bank, reg, shift, func) |
| #define | [IP0SR0](#ab51addcdd30207beec6a6b407b03bda0)(shift, func) |
| #define | [IP1SR0](#a589208eb9220dbb7df9e69c3fcba2b81)(shift, func) |
| #define | [IP2SR0](#a051053920b8e6bf22e28411e1f6fc4c8)(shift, func) |
| #define | [IP3SR0](#a6ebd6c3699a13fd9e98d610c82a3df25)(shift, func) |
| #define | [IP0SR1](#ade8ab39b443828811cf43da560741d30)(shift, func) |
| #define | [IP1SR1](#a500166c8427d495d8811f51c19091738)(shift, func) |
| #define | [IP2SR1](#aee2ad7f7a43248b8d1fdc68cac741f00)(shift, func) |
| #define | [IP3SR1](#aa19b6f71f524cf0f68caeac0b90eee48)(shift, func) |
| #define | [IP0SR2](#aea6fa1ee9aa68fcbad9a7cad7df0534b)(shift, func) |
| #define | [IP1SR2](#a0e288300855fb369dcee23d96d372438)(shift, func) |
| #define | [IP2SR2](#a394520e1fcf63bf5f8943d0bea1cab24)(shift, func) |
| #define | [IP3SR2](#a0fa1dcfc6401dd2b00358651b38599b6)(shift, func) |
| #define | [IP0SR3](#ad965c683495fb478007f7b3cf990fb59)(shift, func) |
| #define | [IP1SR3](#a021e17a25abb44ce72945e36139a02c9)(shift, func) |
| #define | [IP2SR3](#ab159b7a4d4194011ce63fab0dada6074)(shift, func) |
| #define | [IP3SR3](#ad28172ec262b56b921c8b2236f9ab55a)(shift, func) |
| #define | [IP0SR4](#aaf9b88b2ff558f2656c283f95c788f28)(shift, func) |
| #define | [IP1SR4](#a1f27d51000a30d18a6036be7aa6aabd3)(shift, func) |
| #define | [IP2SR4](#af1e67326feb755694a68c688342ff72d)(shift, func) |
| #define | [IP3SR4](#a1a57c0446bc7384b14df6b27fc10ebaf)(shift, func) |
| #define | [IP0SR5](#a13a0b7d3677364aa239400adf7de4e80)(shift, func) |
| #define | [IP1SR5](#a5c60a8466fef3878180305153d81f070)(shift, func) |
| #define | [IP2SR5](#ac6f43f2973e0b423f3f739dfbf682c06)(shift, func) |
| #define | [IP3SR5](#a9d172a3cf5402e07487caf4c2e88a673)(shift, func) |
| #define | [IP0SR6](#a7e1583caf721967f93f862d846b62545)(shift, func) |
| #define | [IP1SR6](#a1a975de92d8a33ac57a26d71dd98ad9c)(shift, func) |
| #define | [IP2SR6](#a5b7e9ba907566b64cafd8d00f4eb6eaf)(shift, func) |
| #define | [IP3SR6](#a6a406638dadb4d7c99c999d5a6041174)(shift, func) |
| #define | [IP0SR7](#a70a6ae0173ed04d171d73b9d8673be30)(shift, func) |
| #define | [IP1SR7](#a75720c99b0d0e1406599ddca8480905d)(shift, func) |
| #define | [IP2SR7](#ac8914ec1a230d65ee43bac854e9825cd)(shift, func) |
| #define | [IP3SR7](#ac2287f3a881d97a63fcedd77bd649823)(shift, func) |
| #define | [PIN\_VOLTAGE\_NONE](#a866ef498674c60a51c56decc15421e25)   0 |
| #define | [PIN\_VOLTAGE\_1P8V](#aeb4cb1a9f61be2a30c5b11bec746b839)   1 |
| #define | [PIN\_VOLTAGE\_3P3V](#acc995ebea352dc5bf5042e29cd1e15d0)   2 |

## Macro Definition Documentation

## [◆ ](#ab51addcdd30207beec6a6b407b03bda0)IP0SR0

| #define IP0SR0 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(0, 0, shift, func)

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)

#define IPnSR(bank, reg, shift, func)

**Definition** pinctrl-rcar-common.h:49

## [◆ ](#ade8ab39b443828811cf43da560741d30)IP0SR1

| #define IP0SR1 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(0, 1, shift, func)

## [◆ ](#aea6fa1ee9aa68fcbad9a7cad7df0534b)IP0SR2

| #define IP0SR2 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(0, 2, shift, func)

## [◆ ](#ad965c683495fb478007f7b3cf990fb59)IP0SR3

| #define IP0SR3 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(0, 3, shift, func)

## [◆ ](#aaf9b88b2ff558f2656c283f95c788f28)IP0SR4

| #define IP0SR4 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(0, 4, shift, func)

## [◆ ](#a13a0b7d3677364aa239400adf7de4e80)IP0SR5

| #define IP0SR5 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(0, 5, shift, func)

## [◆ ](#a7e1583caf721967f93f862d846b62545)IP0SR6

| #define IP0SR6 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(0, 6, shift, func)

## [◆ ](#a70a6ae0173ed04d171d73b9d8673be30)IP0SR7

| #define IP0SR7 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(0, 7, shift, func)

## [◆ ](#a589208eb9220dbb7df9e69c3fcba2b81)IP1SR0

| #define IP1SR0 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(1, 0, shift, func)

## [◆ ](#a500166c8427d495d8811f51c19091738)IP1SR1

| #define IP1SR1 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(1, 1, shift, func)

## [◆ ](#a0e288300855fb369dcee23d96d372438)IP1SR2

| #define IP1SR2 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(1, 2, shift, func)

## [◆ ](#a021e17a25abb44ce72945e36139a02c9)IP1SR3

| #define IP1SR3 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(1, 3, shift, func)

## [◆ ](#a1f27d51000a30d18a6036be7aa6aabd3)IP1SR4

| #define IP1SR4 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(1, 4, shift, func)

## [◆ ](#a5c60a8466fef3878180305153d81f070)IP1SR5

| #define IP1SR5 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(1, 5, shift, func)

## [◆ ](#a1a975de92d8a33ac57a26d71dd98ad9c)IP1SR6

| #define IP1SR6 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(1, 6, shift, func)

## [◆ ](#a75720c99b0d0e1406599ddca8480905d)IP1SR7

| #define IP1SR7 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(1, 7, shift, func)

## [◆ ](#a051053920b8e6bf22e28411e1f6fc4c8)IP2SR0

| #define IP2SR0 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(2, 0, shift, func)

## [◆ ](#aee2ad7f7a43248b8d1fdc68cac741f00)IP2SR1

| #define IP2SR1 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(2, 1, shift, func)

## [◆ ](#a394520e1fcf63bf5f8943d0bea1cab24)IP2SR2

| #define IP2SR2 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(2, 2, shift, func)

## [◆ ](#ab159b7a4d4194011ce63fab0dada6074)IP2SR3

| #define IP2SR3 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(2, 3, shift, func)

## [◆ ](#af1e67326feb755694a68c688342ff72d)IP2SR4

| #define IP2SR4 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(2, 4, shift, func)

## [◆ ](#ac6f43f2973e0b423f3f739dfbf682c06)IP2SR5

| #define IP2SR5 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(2, 5, shift, func)

## [◆ ](#a5b7e9ba907566b64cafd8d00f4eb6eaf)IP2SR6

| #define IP2SR6 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(2, 6, shift, func)

## [◆ ](#ac8914ec1a230d65ee43bac854e9825cd)IP2SR7

| #define IP2SR7 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(2, 7, shift, func)

## [◆ ](#a6ebd6c3699a13fd9e98d610c82a3df25)IP3SR0

| #define IP3SR0 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(3, 0, shift, func)

## [◆ ](#aa19b6f71f524cf0f68caeac0b90eee48)IP3SR1

| #define IP3SR1 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(3, 1, shift, func)

## [◆ ](#a0fa1dcfc6401dd2b00358651b38599b6)IP3SR2

| #define IP3SR2 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(3, 2, shift, func)

## [◆ ](#ad28172ec262b56b921c8b2236f9ab55a)IP3SR3

| #define IP3SR3 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(3, 3, shift, func)

## [◆ ](#a1a57c0446bc7384b14df6b27fc10ebaf)IP3SR4

| #define IP3SR4 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(3, 4, shift, func)

## [◆ ](#a9d172a3cf5402e07487caf4c2e88a673)IP3SR5

| #define IP3SR5 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(3, 5, shift, func)

## [◆ ](#a6a406638dadb4d7c99c999d5a6041174)IP3SR6

| #define IP3SR6 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(3, 6, shift, func)

## [◆ ](#ac2287f3a881d97a63fcedd77bd649823)IP3SR7

| #define IP3SR7 | ( |  | *shift*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

[IPnSR](#a0d4d66df6e1565e2d9f3cfdca9aa5362)(3, 7, shift, func)

## [◆ ](#a0d4d66df6e1565e2d9f3cfdca9aa5362)IPnSR

| #define IPnSR | ( |  | *bank*, |
| --- | --- | --- | --- |
|  |  |  | *reg*, |
|  |  |  | *shift*, |
|  |  |  | *func* ) |

**Value:**

[IPSR](#adbde593c77123c64c2f63e4e8f508ccb)(((reg) << 5U) | (bank), shift, func)

[IPSR](#adbde593c77123c64c2f63e4e8f508ccb)

#define IPSR(bank, shift, func)

Utility macro to build IPSR property entry.

**Definition** pinctrl-rcar-common.h:25

## [◆ ](#adbde593c77123c64c2f63e4e8f508ccb)IPSR

| #define IPSR | ( |  | *bank*, |
| --- | --- | --- | --- |
|  |  |  | *shift*, |
|  |  |  | *func* ) |

**Value:**

(((bank) << 10U) | ((shift) << 4U) | (func))

Utility macro to build IPSR property entry.

IPSR: Peripheral Function Select Register Each IPSR bank can hold 8 cellules of 4 bits coded function.

Parameters
:   | bank | the IPSR register bank. |
    | --- | --- |
    | shift | the bit shift for this alternate function. |
    | func | the 4 bits encoded alternate function. |

Function code [ 0 : 3 ] Function shift [ 4 : 8 ] Empty [ 9 ] IPSR bank [ 10 : 14 ] Register index [ 15 : 17 ] (S4 only)

## [◆ ](#a165cdeba11c616c3c14e1d02e6c4d552)PIN\_NOGPSR\_START

| #define PIN\_NOGPSR\_START   1024U |
| --- |

## [◆ ](#aeb4cb1a9f61be2a30c5b11bec746b839)PIN\_VOLTAGE\_1P8V

| #define PIN\_VOLTAGE\_1P8V   1 |
| --- |

## [◆ ](#acc995ebea352dc5bf5042e29cd1e15d0)PIN\_VOLTAGE\_3P3V

| #define PIN\_VOLTAGE\_3P3V   2 |
| --- |

## [◆ ](#a866ef498674c60a51c56decc15421e25)PIN\_VOLTAGE\_NONE

| #define PIN\_VOLTAGE\_NONE   0 |
| --- |

## [◆ ](#a840b9b9f9f5513088896bbb960724d8f)RCAR\_GP\_PIN

| #define RCAR\_GP\_PIN | ( |  | *bank*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

(((bank) \* 32U) + (pin))

Utility macro to encode a GPIO capable pin.

Parameters
:   | bank | the GPIO bank |
    | --- | --- |
    | pin | the pin within the GPIO bank (0..31) |

## [◆ ](#a6e8b18f9578375cb325e9e5b204b6c66)RCAR\_NOGP\_PIN

| #define RCAR\_NOGP\_PIN | ( |  | *pin* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([PIN\_NOGPSR\_START](#a165cdeba11c616c3c14e1d02e6c4d552) + pin)

[PIN\_NOGPSR\_START](#a165cdeba11c616c3c14e1d02e6c4d552)

#define PIN\_NOGPSR\_START

**Definition** pinctrl-rcar-common.h:28

Utility macro to encode a non capable GPIO pin.

Parameters
:   | pin | the encoded pin number |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rcar-common.h](pinctrl-rcar-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
