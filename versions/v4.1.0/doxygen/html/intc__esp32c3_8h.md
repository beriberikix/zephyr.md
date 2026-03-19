---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__esp32c3_8h.html
original_path: doxygen/html/intc__esp32c3_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_esp32c3.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <soc.h>`

[Go to the source code of this file.](intc__esp32c3_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP\_INTR\_FLAG\_LEVEL1](#ab1ef5952bffcb1811d4f831b98ecf42a)   (1<<1) /\* Accept a Level 1 int vector, lowest priority \*/ |
| #define | [ESP\_INTR\_FLAG\_LEVEL2](#a8e4478d65d49a4f17fb77599764239e2)   (1<<2) /\* Accept a Level 2 int vector \*/ |
| #define | [ESP\_INTR\_FLAG\_LEVEL3](#a88ed1ea08351b07086a6e73a0487b0d8)   (1<<3) /\* Accept a Level 3 int vector \*/ |
| #define | [ESP\_INTR\_FLAG\_LEVEL4](#abb43226aa7d32763f17ee6a56090b322)   (1<<4) /\* Accept a Level 4 int vector \*/ |
| #define | [ESP\_INTR\_FLAG\_LEVEL5](#a44a1013070e7d9a06e8f08ed3f2cbca9)   (1<<5) /\* Accept a Level 5 int vector \*/ |
| #define | [ESP\_INTR\_FLAG\_LEVEL6](#a8defb5130273462e32ed399dece67024)   (1<<6) /\* Accept a Level 6 int vector \*/ |
| #define | [ESP\_INTR\_FLAG\_NMI](#a9e57c700cf362161d807657571280abe)   (1<<7) /\* Accept a Level 7 int vector, highest priority \*/ |
| #define | [ESP\_INTR\_FLAG\_SHARED](#afc7bfcea2e621d81336ea6dd23310363)   (1<<8) /\* Interrupt can be shared between ISRs \*/ |
| #define | [ESP\_INTR\_FLAG\_EDGE](#a0ab957dd5055fe20725624db223f9535)   (1<<9) /\* Edge-triggered interrupt \*/ |
| #define | [ESP\_INTR\_FLAG\_IRAM](#a3fb8d6fa8b5e33b3503e86917bc8367b)   (1<<10) /\* ISR can be called if cache is disabled \*/ |
| #define | [ESP\_INTR\_FLAG\_INTRDISABLED](#a76d024609ecd48dc17b586b91e779b88)   (1<<11) /\* Return with this interrupt disabled \*/ |
| #define | [ESP\_INTR\_FLAG\_LOWMED](#a9b0bc1a2b5cc22b499e041742ae1b17b)   ([ESP\_INTR\_FLAG\_LEVEL1](#ab1ef5952bffcb1811d4f831b98ecf42a)|[ESP\_INTR\_FLAG\_LEVEL2](#a8e4478d65d49a4f17fb77599764239e2)|[ESP\_INTR\_FLAG\_LEVEL3](#a88ed1ea08351b07086a6e73a0487b0d8)) |
| #define | [ESP\_INTR\_FLAG\_HIGH](#a63b4eee1d70d2e9cb1dc0ecb41f40aa4) |
| #define | [ESP\_INTR\_FLAG\_LEVELMASK](#a610949ce2bf8d7adae528f816acc5725) |
| #define | [IRQ\_NA](#a0da8577e46721fb23629536f175b6661)   0xFF /\* IRQ not available \*/ |
| #define | [IRQ\_FREE](#aac65746f3615e2b6c23cfc6344293012)   0xFE /\* IRQ available for use \*/ |
| #define | [ESP\_PRIO\_TO\_FLAGS](#a447e94d9632ed5c38f1ea36cbc283c4a)(priority) |
| #define | [ESP\_INT\_FLAGS\_CHECK](#a4dac251442759ec39f07862b435e3dc1)(int\_flags) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [isr\_handler\_t](#ae96c682b20638830cd816926696e781a)) (const void \*arg) |

| Functions | |
| --- | --- |
| void | [esp\_intr\_initialize](#aede8e7c90fd3138cf165a0eea1c920fe) (void) |
|  | Initializes interrupt table to its defaults. |
| int | [esp\_intr\_alloc](#aa2dbfcb97856d74deaf1054cdc5521a5) (int source, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [isr\_handler\_t](#ae96c682b20638830cd816926696e781a) handler, void \*arg, void \*\*ret\_handle) |
|  | Allocate an interrupt with the given parameters. |
| int | [esp\_intr\_disable](#abaf6326b21c234959e34e8bef32987be) (int source) |
|  | Disable the interrupt associated with the source. |
| int | [esp\_intr\_enable](#af52c1b16bd4c4d05167401e34bf03983) (int source) |
|  | Enable the interrupt associated with the source. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [esp\_intr\_get\_enabled\_intmask](#ae5cd92e8d61acc30607bf4acdb992aaa) (int status\_mask\_number) |
|  | Gets the current enabled interrupts. |

## Macro Definition Documentation

## [◆ ](#a4dac251442759ec39f07862b435e3dc1)ESP\_INT\_FLAGS\_CHECK

| #define ESP\_INT\_FLAGS\_CHECK | ( |  | *int\_flags* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((int\_flags) & [ESP\_INTR\_FLAG\_SHARED](intc__esp32_8h.md#afc7bfcea2e621d81336ea6dd23310363))

[ESP\_INTR\_FLAG\_SHARED](intc__esp32_8h.md#afc7bfcea2e621d81336ea6dd23310363)

#define ESP\_INTR\_FLAG\_SHARED

**Definition** intc\_esp32.h:30

## [◆ ](#a0ab957dd5055fe20725624db223f9535)ESP\_INTR\_FLAG\_EDGE

| #define ESP\_INTR\_FLAG\_EDGE   (1<<9) /\* Edge-triggered interrupt \*/ |
| --- |

## [◆ ](#a63b4eee1d70d2e9cb1dc0ecb41f40aa4)ESP\_INTR\_FLAG\_HIGH

| #define ESP\_INTR\_FLAG\_HIGH |
| --- |

**Value:**

([ESP\_INTR\_FLAG\_LEVEL4](intc__esp32_8h.md#abb43226aa7d32763f17ee6a56090b322)|[ESP\_INTR\_FLAG\_LEVEL5](intc__esp32_8h.md#a44a1013070e7d9a06e8f08ed3f2cbca9)|[ESP\_INTR\_FLAG\_LEVEL6](intc__esp32_8h.md#a8defb5130273462e32ed399dece67024)| \

[ESP\_INTR\_FLAG\_NMI](intc__esp32_8h.md#a9e57c700cf362161d807657571280abe))

[ESP\_INTR\_FLAG\_LEVEL5](intc__esp32_8h.md#a44a1013070e7d9a06e8f08ed3f2cbca9)

#define ESP\_INTR\_FLAG\_LEVEL5

**Definition** intc\_esp32.h:27

[ESP\_INTR\_FLAG\_LEVEL6](intc__esp32_8h.md#a8defb5130273462e32ed399dece67024)

#define ESP\_INTR\_FLAG\_LEVEL6

**Definition** intc\_esp32.h:28

[ESP\_INTR\_FLAG\_NMI](intc__esp32_8h.md#a9e57c700cf362161d807657571280abe)

#define ESP\_INTR\_FLAG\_NMI

**Definition** intc\_esp32.h:29

[ESP\_INTR\_FLAG\_LEVEL4](intc__esp32_8h.md#abb43226aa7d32763f17ee6a56090b322)

#define ESP\_INTR\_FLAG\_LEVEL4

**Definition** intc\_esp32.h:26

## [◆ ](#a76d024609ecd48dc17b586b91e779b88)ESP\_INTR\_FLAG\_INTRDISABLED

| #define ESP\_INTR\_FLAG\_INTRDISABLED   (1<<11) /\* Return with this interrupt disabled \*/ |
| --- |

## [◆ ](#a3fb8d6fa8b5e33b3503e86917bc8367b)ESP\_INTR\_FLAG\_IRAM

| #define ESP\_INTR\_FLAG\_IRAM   (1<<10) /\* ISR can be called if cache is disabled \*/ |
| --- |

## [◆ ](#ab1ef5952bffcb1811d4f831b98ecf42a)ESP\_INTR\_FLAG\_LEVEL1

| #define ESP\_INTR\_FLAG\_LEVEL1   (1<<1) /\* Accept a Level 1 int vector, lowest priority \*/ |
| --- |

## [◆ ](#a8e4478d65d49a4f17fb77599764239e2)ESP\_INTR\_FLAG\_LEVEL2

| #define ESP\_INTR\_FLAG\_LEVEL2   (1<<2) /\* Accept a Level 2 int vector \*/ |
| --- |

## [◆ ](#a88ed1ea08351b07086a6e73a0487b0d8)ESP\_INTR\_FLAG\_LEVEL3

| #define ESP\_INTR\_FLAG\_LEVEL3   (1<<3) /\* Accept a Level 3 int vector \*/ |
| --- |

## [◆ ](#abb43226aa7d32763f17ee6a56090b322)ESP\_INTR\_FLAG\_LEVEL4

| #define ESP\_INTR\_FLAG\_LEVEL4   (1<<4) /\* Accept a Level 4 int vector \*/ |
| --- |

## [◆ ](#a44a1013070e7d9a06e8f08ed3f2cbca9)ESP\_INTR\_FLAG\_LEVEL5

| #define ESP\_INTR\_FLAG\_LEVEL5   (1<<5) /\* Accept a Level 5 int vector \*/ |
| --- |

## [◆ ](#a8defb5130273462e32ed399dece67024)ESP\_INTR\_FLAG\_LEVEL6

| #define ESP\_INTR\_FLAG\_LEVEL6   (1<<6) /\* Accept a Level 6 int vector \*/ |
| --- |

## [◆ ](#a610949ce2bf8d7adae528f816acc5725)ESP\_INTR\_FLAG\_LEVELMASK

| #define ESP\_INTR\_FLAG\_LEVELMASK |
| --- |

**Value:**

([ESP\_INTR\_FLAG\_LEVEL1](intc__esp32_8h.md#ab1ef5952bffcb1811d4f831b98ecf42a)|[ESP\_INTR\_FLAG\_LEVEL2](intc__esp32_8h.md#a8e4478d65d49a4f17fb77599764239e2)|[ESP\_INTR\_FLAG\_LEVEL3](intc__esp32_8h.md#a88ed1ea08351b07086a6e73a0487b0d8)| \

[ESP\_INTR\_FLAG\_LEVEL4](intc__esp32_8h.md#abb43226aa7d32763f17ee6a56090b322)|[ESP\_INTR\_FLAG\_LEVEL5](intc__esp32_8h.md#a44a1013070e7d9a06e8f08ed3f2cbca9)|[ESP\_INTR\_FLAG\_LEVEL6](intc__esp32_8h.md#a8defb5130273462e32ed399dece67024)| \

[ESP\_INTR\_FLAG\_NMI](intc__esp32_8h.md#a9e57c700cf362161d807657571280abe))

[ESP\_INTR\_FLAG\_LEVEL3](intc__esp32_8h.md#a88ed1ea08351b07086a6e73a0487b0d8)

#define ESP\_INTR\_FLAG\_LEVEL3

**Definition** intc\_esp32.h:25

[ESP\_INTR\_FLAG\_LEVEL2](intc__esp32_8h.md#a8e4478d65d49a4f17fb77599764239e2)

#define ESP\_INTR\_FLAG\_LEVEL2

**Definition** intc\_esp32.h:24

[ESP\_INTR\_FLAG\_LEVEL1](intc__esp32_8h.md#ab1ef5952bffcb1811d4f831b98ecf42a)

#define ESP\_INTR\_FLAG\_LEVEL1

**Definition** intc\_esp32.h:23

## [◆ ](#a9b0bc1a2b5cc22b499e041742ae1b17b)ESP\_INTR\_FLAG\_LOWMED

| #define ESP\_INTR\_FLAG\_LOWMED   ([ESP\_INTR\_FLAG\_LEVEL1](#ab1ef5952bffcb1811d4f831b98ecf42a)|[ESP\_INTR\_FLAG\_LEVEL2](#a8e4478d65d49a4f17fb77599764239e2)|[ESP\_INTR\_FLAG\_LEVEL3](#a88ed1ea08351b07086a6e73a0487b0d8)) |
| --- |

## [◆ ](#a9e57c700cf362161d807657571280abe)ESP\_INTR\_FLAG\_NMI

| #define ESP\_INTR\_FLAG\_NMI   (1<<7) /\* Accept a Level 7 int vector, highest priority \*/ |
| --- |

## [◆ ](#afc7bfcea2e621d81336ea6dd23310363)ESP\_INTR\_FLAG\_SHARED

| #define ESP\_INTR\_FLAG\_SHARED   (1<<8) /\* Interrupt can be shared between ISRs \*/ |
| --- |

## [◆ ](#a447e94d9632ed5c38f1ea36cbc283c4a)ESP\_PRIO\_TO\_FLAGS

| #define ESP\_PRIO\_TO\_FLAGS | ( |  | *priority* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((priority) > 0 ? ((1 << (priority)) & [ESP\_INTR\_FLAG\_LEVELMASK](intc__esp32_8h.md#a610949ce2bf8d7adae528f816acc5725)) : 0)

[ESP\_INTR\_FLAG\_LEVELMASK](intc__esp32_8h.md#a610949ce2bf8d7adae528f816acc5725)

#define ESP\_INTR\_FLAG\_LEVELMASK

**Definition** intc\_esp32.h:43

## [◆ ](#aac65746f3615e2b6c23cfc6344293012)IRQ\_FREE

| #define IRQ\_FREE   0xFE /\* IRQ available for use \*/ |
| --- |

## [◆ ](#a0da8577e46721fb23629536f175b6661)IRQ\_NA

| #define IRQ\_NA   0xFF /\* IRQ not available \*/ |
| --- |

## Typedef Documentation

## [◆ ](#ae96c682b20638830cd816926696e781a)isr\_handler\_t

| typedef void(\* isr\_handler\_t) (const void \*arg) |
| --- |

## Function Documentation

## [◆ ](#aa2dbfcb97856d74deaf1054cdc5521a5)esp\_intr\_alloc()

| int esp\_intr\_alloc | ( | int | *source*, |
| --- | --- | --- | --- |
|  |  | int | *flags*, |
|  |  | [isr\_handler\_t](#ae96c682b20638830cd816926696e781a) | *handler*, |
|  |  | void \* | *arg*, |
|  |  | void \*\* | *ret\_handle* ) |

Allocate an interrupt with the given parameters.

This finds an interrupt that matches the restrictions as given in the flags parameter, maps the given interrupt source to it and hooks up the given interrupt handler (with optional argument) as well. If needed, it can return a handle for the interrupt as well.

Parameters
:   | source | The interrupt source. |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | An ORred mask of the ESP\_INTR\_FLAG\_\* defines. These restrict the choice of interrupts that this routine can choose from. If this value is 0, it will default to allocating a non-shared interrupt of level 1, 2 or 3. If this is ESP\_INTR\_FLAG\_SHARED, it will allocate a shared interrupt of level 1. Setting ESP\_INTR\_FLAG\_INTRDISABLED will return from this function with the interrupt disabled. |
    | handler | The interrupt handler. |
    | arg | Optional argument for passed to the interrupt handler |
    | ret\_handle | Pointer to a struct [intr\_handle\_data\_t](structintr__handle__data__t.md "Interrupt handler associated data structure.") pointer to store a handle that can later be used to request details or free the interrupt. Can be NULL if no handle is required. |

Returns
:   -EINVAL if the combination of arguments is invalid. -ENODEV No free interrupt found with the specified flags 0 otherwise

## [◆ ](#abaf6326b21c234959e34e8bef32987be)esp\_intr\_disable()

| int esp\_intr\_disable | ( | int | *source* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable the interrupt associated with the source.

Parameters
:   | source | The interrupt source |
    | --- | --- |

Returns
:   -EINVAL if the combination of arguments is invalid. 0 otherwise

## [◆ ](#af52c1b16bd4c4d05167401e34bf03983)esp\_intr\_enable()

| int esp\_intr\_enable | ( | int | *source* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable the interrupt associated with the source.

Parameters
:   | source | The interrupt source |
    | --- | --- |

Returns
:   -EINVAL if the combination of arguments is invalid. 0 otherwise

## [◆ ](#ae5cd92e8d61acc30607bf4acdb992aaa)esp\_intr\_get\_enabled\_intmask()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) esp\_intr\_get\_enabled\_intmask | ( | int | *status\_mask\_number* | ) |  |
| --- | --- | --- | --- | --- | --- |

Gets the current enabled interrupts.

Parameters
:   | status\_mask\_number | the status mask can be 0 or 1 |
    | --- | --- |

Returns
:   bitmask of enabled interrupt sources

## [◆ ](#aede8e7c90fd3138cf165a0eea1c920fe)esp\_intr\_initialize()

| void esp\_intr\_initialize | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Initializes interrupt table to its defaults.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_esp32c3.h](intc__esp32c3_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
