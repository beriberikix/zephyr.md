---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__esp32_8h.html
original_path: doxygen/html/intc__esp32_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_esp32.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](intc__esp32_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shared\_vector\_desc\_t](structshared__vector__desc__t.md) |
| struct | [vector\_desc\_t](structvector__desc__t.md) |
| struct | [intr\_handle\_data\_t](structintr__handle__data__t.md) |
|  | Interrupt handler associated data structure. [More...](structintr__handle__data__t.md#details) |

| Macros | |
| --- | --- |
| #define | [ESP\_INTC\_INTS\_NUM](#a1bc4233beade6702b76413dd4ee6497f)   (32) |
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
| #define | [ESP\_PRIO\_TO\_FLAGS](#a447e94d9632ed5c38f1ea36cbc283c4a)(priority) |
| #define | [ESP\_INT\_FLAGS\_CHECK](#a4dac251442759ec39f07862b435e3dc1)(int\_flags) |
| #define | [ETS\_INTERNAL\_TIMER0\_INTR\_SOURCE](#a2ff354dc48600b4dcbce4569c5d15bc1)   -1 /\* Xtensa timer 0 interrupt source \*/ |
| #define | [ETS\_INTERNAL\_TIMER1\_INTR\_SOURCE](#ad28849af2335d2c6d9e07949f8ea953d)   -2 /\* Xtensa timer 1 interrupt source \*/ |
| #define | [ETS\_INTERNAL\_TIMER2\_INTR\_SOURCE](#ad94487ae3c0ae2b9e4bccad6ce26d761)   -3 /\* Xtensa timer 2 interrupt source \*/ |
| #define | [ETS\_INTERNAL\_SW0\_INTR\_SOURCE](#a7cd02abe5015f1be30d77e1be15bd448)   -4 /\* Software int source 1 \*/ |
| #define | [ETS\_INTERNAL\_SW1\_INTR\_SOURCE](#aa81d606c0199b91aba7633270ca314e6)   -5 /\* Software int source 2 \*/ |
| #define | [ETS\_INTERNAL\_PROFILING\_INTR\_SOURCE](#a6cac8d828d3ec24b9bb58fe0cb3d59fc)   -6 /\* Int source for profiling \*/ |

| Typedefs | |
| --- | --- |
| typedef void(\* | [intr\_handler\_t](#a637aa0db4839d3e945e74c56e82218f2)) (void \*arg) |

| Functions | |
| --- | --- |
| void | [esp\_intr\_initialize](#aede8e7c90fd3138cf165a0eea1c920fe) (void) |
|  | Initializes interrupt table to its defaults. |
| int | [esp\_intr\_mark\_shared](#aafc6d38bb52a59bd024809efcb3b64f0) (int intno, int cpu, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_in\_iram) |
|  | Mark an interrupt as a shared interrupt. |
| int | [esp\_intr\_reserve](#aa6eef593f8a838adec4d258346b087d0) (int intno, int cpu) |
|  | Reserve an interrupt to be used outside of this framework. |
| int | [esp\_intr\_alloc](#a480a4405ea151074f2ce4ffbab1265ea) (int source, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [intr\_handler\_t](#a637aa0db4839d3e945e74c56e82218f2) handler, void \*arg, struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*\*ret\_handle) |
|  | Allocate an interrupt with the given parameters. |
| int | [esp\_intr\_alloc\_intrstatus](#a8659159ab9a4fea92d989068bb6d6f7b) (int source, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) intrstatusreg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) intrstatusmask, [intr\_handler\_t](#a637aa0db4839d3e945e74c56e82218f2) handler, void \*arg, struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*\*ret\_handle) |
|  | Allocate an interrupt with the given parameters. |
| int | [esp\_intr\_free](#a90993df0cbd038640609df8c3e1957d3) (struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle) |
|  | Disable and free an interrupt. |
| int | [esp\_intr\_get\_cpu](#a6c399aafeab8bff0a49bc2b127445e10) (struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle) |
|  | Get CPU number an interrupt is tied to. |
| int | [esp\_intr\_get\_intno](#a5261fac231a9d1428b4131da33f1ef90) (struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle) |
|  | Get the allocated interrupt for a certain handle. |
| int | [esp\_intr\_disable](#a3ee7a7cc9ed4f7bb6e0fa65ac7e77ba6) (struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle) |
|  | Disable the interrupt associated with the handle. |
| int | [esp\_intr\_enable](#a3a9ed282687252cd3a8e5c18284257ff) (struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle) |
|  | Enable the interrupt associated with the handle. |
| int | [esp\_intr\_set\_in\_iram](#af1417d7a4a9faba280ac4e17c9ee60ab) (struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*handle, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_in\_iram) |
|  | Set the "in IRAM" status of the handler. |
| void | [esp\_intr\_noniram\_disable](#a63263dc3bf78c25b514f739e6381ee64) (void) |
|  | Disable interrupts that aren't specifically marked as running from IRAM. |
| void | [esp\_intr\_noniram\_enable](#a917f8af7f0c6af92dfbd1f7689c39cae) (void) |
|  | Re-enable interrupts disabled by esp\_intr\_noniram\_disable. |

## Macro Definition Documentation

## [◆ ](#a4dac251442759ec39f07862b435e3dc1)ESP\_INT\_FLAGS\_CHECK

| #define ESP\_INT\_FLAGS\_CHECK | ( |  | *int\_flags* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((int\_flags) & [ESP\_INTR\_FLAG\_SHARED](#afc7bfcea2e621d81336ea6dd23310363))

[ESP\_INTR\_FLAG\_SHARED](#afc7bfcea2e621d81336ea6dd23310363)

#define ESP\_INTR\_FLAG\_SHARED

**Definition** intc\_esp32.h:30

## [◆ ](#a1bc4233beade6702b76413dd4ee6497f)ESP\_INTC\_INTS\_NUM

| #define ESP\_INTC\_INTS\_NUM   (32) |
| --- |

## [◆ ](#a0ab957dd5055fe20725624db223f9535)ESP\_INTR\_FLAG\_EDGE

| #define ESP\_INTR\_FLAG\_EDGE   (1<<9) /\* Edge-triggered interrupt \*/ |
| --- |

## [◆ ](#a63b4eee1d70d2e9cb1dc0ecb41f40aa4)ESP\_INTR\_FLAG\_HIGH

| #define ESP\_INTR\_FLAG\_HIGH |
| --- |

**Value:**

([ESP\_INTR\_FLAG\_LEVEL4](#abb43226aa7d32763f17ee6a56090b322)|[ESP\_INTR\_FLAG\_LEVEL5](#a44a1013070e7d9a06e8f08ed3f2cbca9)|[ESP\_INTR\_FLAG\_LEVEL6](#a8defb5130273462e32ed399dece67024)| \

[ESP\_INTR\_FLAG\_NMI](#a9e57c700cf362161d807657571280abe))

[ESP\_INTR\_FLAG\_LEVEL5](#a44a1013070e7d9a06e8f08ed3f2cbca9)

#define ESP\_INTR\_FLAG\_LEVEL5

**Definition** intc\_esp32.h:27

[ESP\_INTR\_FLAG\_LEVEL6](#a8defb5130273462e32ed399dece67024)

#define ESP\_INTR\_FLAG\_LEVEL6

**Definition** intc\_esp32.h:28

[ESP\_INTR\_FLAG\_NMI](#a9e57c700cf362161d807657571280abe)

#define ESP\_INTR\_FLAG\_NMI

**Definition** intc\_esp32.h:29

[ESP\_INTR\_FLAG\_LEVEL4](#abb43226aa7d32763f17ee6a56090b322)

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

([ESP\_INTR\_FLAG\_LEVEL1](#ab1ef5952bffcb1811d4f831b98ecf42a)|[ESP\_INTR\_FLAG\_LEVEL2](#a8e4478d65d49a4f17fb77599764239e2)|[ESP\_INTR\_FLAG\_LEVEL3](#a88ed1ea08351b07086a6e73a0487b0d8)| \

[ESP\_INTR\_FLAG\_LEVEL4](#abb43226aa7d32763f17ee6a56090b322)|[ESP\_INTR\_FLAG\_LEVEL5](#a44a1013070e7d9a06e8f08ed3f2cbca9)|[ESP\_INTR\_FLAG\_LEVEL6](#a8defb5130273462e32ed399dece67024)| \

[ESP\_INTR\_FLAG\_NMI](#a9e57c700cf362161d807657571280abe))

[ESP\_INTR\_FLAG\_LEVEL3](#a88ed1ea08351b07086a6e73a0487b0d8)

#define ESP\_INTR\_FLAG\_LEVEL3

**Definition** intc\_esp32.h:25

[ESP\_INTR\_FLAG\_LEVEL2](#a8e4478d65d49a4f17fb77599764239e2)

#define ESP\_INTR\_FLAG\_LEVEL2

**Definition** intc\_esp32.h:24

[ESP\_INTR\_FLAG\_LEVEL1](#ab1ef5952bffcb1811d4f831b98ecf42a)

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

((priority) > 0 ? ((1 << (priority)) & [ESP\_INTR\_FLAG\_LEVELMASK](#a610949ce2bf8d7adae528f816acc5725)) : 0)

[ESP\_INTR\_FLAG\_LEVELMASK](#a610949ce2bf8d7adae528f816acc5725)

#define ESP\_INTR\_FLAG\_LEVELMASK

**Definition** intc\_esp32.h:43

## [◆ ](#a6cac8d828d3ec24b9bb58fe0cb3d59fc)ETS\_INTERNAL\_PROFILING\_INTR\_SOURCE

| #define ETS\_INTERNAL\_PROFILING\_INTR\_SOURCE   -6 /\* Int source for profiling \*/ |
| --- |

## [◆ ](#a7cd02abe5015f1be30d77e1be15bd448)ETS\_INTERNAL\_SW0\_INTR\_SOURCE

| #define ETS\_INTERNAL\_SW0\_INTR\_SOURCE   -4 /\* Software int source 1 \*/ |
| --- |

## [◆ ](#aa81d606c0199b91aba7633270ca314e6)ETS\_INTERNAL\_SW1\_INTR\_SOURCE

| #define ETS\_INTERNAL\_SW1\_INTR\_SOURCE   -5 /\* Software int source 2 \*/ |
| --- |

## [◆ ](#a2ff354dc48600b4dcbce4569c5d15bc1)ETS\_INTERNAL\_TIMER0\_INTR\_SOURCE

| #define ETS\_INTERNAL\_TIMER0\_INTR\_SOURCE   -1 /\* Xtensa timer 0 interrupt source \*/ |
| --- |

## [◆ ](#ad28849af2335d2c6d9e07949f8ea953d)ETS\_INTERNAL\_TIMER1\_INTR\_SOURCE

| #define ETS\_INTERNAL\_TIMER1\_INTR\_SOURCE   -2 /\* Xtensa timer 1 interrupt source \*/ |
| --- |

## [◆ ](#ad94487ae3c0ae2b9e4bccad6ce26d761)ETS\_INTERNAL\_TIMER2\_INTR\_SOURCE

| #define ETS\_INTERNAL\_TIMER2\_INTR\_SOURCE   -3 /\* Xtensa timer 2 interrupt source \*/ |
| --- |

## Typedef Documentation

## [◆ ](#a637aa0db4839d3e945e74c56e82218f2)intr\_handler\_t

| typedef void(\* intr\_handler\_t) (void \*arg) |
| --- |

## Function Documentation

## [◆ ](#a480a4405ea151074f2ce4ffbab1265ea)esp\_intr\_alloc()

| int esp\_intr\_alloc | ( | int | *source*, |
| --- | --- | --- | --- |
|  |  | int | *flags*, |
|  |  | [intr\_handler\_t](#a637aa0db4839d3e945e74c56e82218f2) | *handler*, |
|  |  | void \* | *arg*, |
|  |  | struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*\* | *ret\_handle* ) |

Allocate an interrupt with the given parameters.

This finds an interrupt that matches the restrictions as given in the flags parameter, maps the given interrupt source to it and hooks up the given interrupt handler (with optional argument) as well. If needed, it can return a handle for the interrupt as well.

The interrupt will always be allocated on the core that runs this function.

If ESP\_INTR\_FLAG\_IRAM flag is used, and handler address is not in IRAM or RTC\_FAST\_MEM, then ESP\_ERR\_INVALID\_ARG is returned.

Parameters
:   | source | The interrupt source. One of the **INTR\_SOURCE interrupt mux sources, as defined in [esp-xtensa-intmux.h](esp-xtensa-intmux_8h.md), or one of the internal ETS\_INTERNAL**\_INTR\_SOURCE sources as defined in this header. |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | An ORred mask of the ESP\_INTR\_FLAG\_\* defines. These restrict the choice of interrupts that this routine can choose from. If this value is 0, it will default to allocating a non-shared interrupt of level 1, 2 or 3. If this is ESP\_INTR\_FLAG\_SHARED, it will allocate a shared interrupt of level 1. Setting ESP\_INTR\_FLAG\_INTRDISABLED will return from this function with the interrupt disabled. |
    | handler | The interrupt handler. Must be NULL when an interrupt of level >3 is requested, because these types of interrupts aren't C-callable. |
    | arg | Optional argument for passed to the interrupt handler |
    | ret\_handle | Pointer to a struct [intr\_handle\_data\_t](structintr__handle__data__t.md "Interrupt handler associated data structure.") pointer to store a handle that can later be used to request details or free the interrupt. Can be NULL if no handle is required. |

Returns
:   -EINVAL if the combination of arguments is invalid. -ENODEV No free interrupt found with the specified flags 0 otherwise

## [◆ ](#a8659159ab9a4fea92d989068bb6d6f7b)esp\_intr\_alloc\_intrstatus()

| int esp\_intr\_alloc\_intrstatus | ( | int | *source*, |
| --- | --- | --- | --- |
|  |  | int | *flags*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *intrstatusreg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *intrstatusmask*, |
|  |  | [intr\_handler\_t](#a637aa0db4839d3e945e74c56e82218f2) | *handler*, |
|  |  | void \* | *arg*, |
|  |  | struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \*\* | *ret\_handle* ) |

Allocate an interrupt with the given parameters.

This essentially does the same as esp\_intr\_alloc, but allows specifying a register and mask combo. For shared interrupts, the handler is only called if a read from the specified register, ANDed with the mask, returns non-zero. By passing an interrupt status register address and a fitting mask, this can be used to accelerate interrupt handling in the case a shared interrupt is triggered; by checking the interrupt statuses first, the code can decide which ISRs can be skipped

Parameters
:   | source | The interrupt source. One of the **INTR\_SOURCE interrupt mux sources, as defined in [esp-xtensa-intmux.h](esp-xtensa-intmux_8h.md), or one of the internal ETS\_INTERNAL**\_INTR\_SOURCE sources as defined in this header. |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | An ORred mask of the ESP\_INTR\_FLAG\_\* defines. These restrict the choice of interrupts that this routine can choose from. If this value is 0, it will default to allocating a non-shared interrupt of level 1, 2 or 3. If this is ESP\_INTR\_FLAG\_SHARED, it will allocate a shared interrupt of level 1. Setting ESP\_INTR\_FLAG\_INTRDISABLED will return from this function with the interrupt disabled. |
    | intrstatusreg | The address of an interrupt status register |
    | intrstatusmask | A mask. If a read of address intrstatusreg has any of the bits that are 1 in the mask set, the ISR will be called. If not, it will be skipped. |
    | handler | The interrupt handler. Must be NULL when an interrupt of level >3 is requested, because these types of interrupts aren't C-callable. |
    | arg | Optional argument for passed to the interrupt handler |
    | ret\_handle | Pointer to a struct [intr\_handle\_data\_t](structintr__handle__data__t.md "Interrupt handler associated data structure.") pointer to store a handle that can later be used to request details or free the interrupt. Can be NULL if no handle is required. |

Returns
:   -EINVAL if the combination of arguments is invalid. -ENODEV No free interrupt found with the specified flags 0 otherwise

## [◆ ](#a3ee7a7cc9ed4f7bb6e0fa65ac7e77ba6)esp\_intr\_disable()

| int esp\_intr\_disable | ( | struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \* | *handle* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable the interrupt associated with the handle.

Note
:   1. For local interrupts (ESP\_INTERNAL\_\* sources), this function has to be called on the CPU the interrupt is allocated on. Other interrupts have no such restriction.
    2. When several handlers sharing a same interrupt source, interrupt status bits, which are handled in the handler to be disabled, should be masked before the disabling, or handled in other enabled interrupts properly. Miss of interrupt status handling will cause infinite interrupt calls and finally system crash.

Parameters
:   | handle | The handle, as obtained by esp\_intr\_alloc or esp\_intr\_alloc\_intrstatus |
    | --- | --- |

Returns
:   -EINVAL if the combination of arguments is invalid. 0 otherwise

## [◆ ](#a3a9ed282687252cd3a8e5c18284257ff)esp\_intr\_enable()

| int esp\_intr\_enable | ( | struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \* | *handle* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable the interrupt associated with the handle.

Note
:   For local interrupts (ESP\_INTERNAL\_\* sources), this function has to be called on the CPU the interrupt is allocated on. Other interrupts have no such restriction.

Parameters
:   | handle | The handle, as obtained by esp\_intr\_alloc or esp\_intr\_alloc\_intrstatus |
    | --- | --- |

Returns
:   -EINVAL if the combination of arguments is invalid. 0 otherwise

## [◆ ](#a90993df0cbd038640609df8c3e1957d3)esp\_intr\_free()

| int esp\_intr\_free | ( | struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \* | *handle* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable and free an interrupt.

Use an interrupt handle to disable the interrupt and release the resources associated with it. If the current core is not the core that registered this interrupt, this routine will be assigned to the core that allocated this interrupt, blocking and waiting until the resource is successfully released.

Note
:   When the handler shares its source with other handlers, the interrupt status bits it's responsible for should be managed properly before freeing it. See [esp\_intr\_disable](#a3ee7a7cc9ed4f7bb6e0fa65ac7e77ba6) for more details. Please do not call this function in esp\_ipc\_call\_blocking.

Parameters
:   | handle | The handle, as obtained by esp\_intr\_alloc or esp\_intr\_alloc\_intrstatus |
    | --- | --- |

Returns
:   -EINVAL the handle is NULL 0 otherwise

## [◆ ](#a6c399aafeab8bff0a49bc2b127445e10)esp\_intr\_get\_cpu()

| int esp\_intr\_get\_cpu | ( | struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \* | *handle* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get CPU number an interrupt is tied to.

Parameters
:   | handle | The handle, as obtained by esp\_intr\_alloc or esp\_intr\_alloc\_intrstatus |
    | --- | --- |

Returns
:   The core number where the interrupt is allocated

## [◆ ](#a5261fac231a9d1428b4131da33f1ef90)esp\_intr\_get\_intno()

| int esp\_intr\_get\_intno | ( | struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \* | *handle* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the allocated interrupt for a certain handle.

Parameters
:   | handle | The handle, as obtained by esp\_intr\_alloc or esp\_intr\_alloc\_intrstatus |
    | --- | --- |

Returns
:   The interrupt number

## [◆ ](#aede8e7c90fd3138cf165a0eea1c920fe)esp\_intr\_initialize()

| void esp\_intr\_initialize | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Initializes interrupt table to its defaults.

## [◆ ](#aafc6d38bb52a59bd024809efcb3b64f0)esp\_intr\_mark\_shared()

| int esp\_intr\_mark\_shared | ( | int | *intno*, |
| --- | --- | --- | --- |
|  |  | int | *cpu*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *is\_in\_iram* ) |

Mark an interrupt as a shared interrupt.

This will mark a certain interrupt on the specified CPU as an interrupt that can be used to hook shared interrupt handlers to.

Parameters
:   | intno | The number of the interrupt (0-31) |
    | --- | --- |
    | cpu | CPU on which the interrupt should be marked as shared (0 or 1) |
    | is\_in\_iram | Shared interrupt is for handlers that reside in IRAM and the int can be left enabled while the flash cache is disabled. |

Returns
:   -EINVAL if cpu or intno is invalid 0 otherwise

## [◆ ](#a63263dc3bf78c25b514f739e6381ee64)esp\_intr\_noniram\_disable()

| void esp\_intr\_noniram\_disable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable interrupts that aren't specifically marked as running from IRAM.

## [◆ ](#a917f8af7f0c6af92dfbd1f7689c39cae)esp\_intr\_noniram\_enable()

| void esp\_intr\_noniram\_enable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Re-enable interrupts disabled by esp\_intr\_noniram\_disable.

## [◆ ](#aa6eef593f8a838adec4d258346b087d0)esp\_intr\_reserve()

| int esp\_intr\_reserve | ( | int | *intno*, |
| --- | --- | --- | --- |
|  |  | int | *cpu* ) |

Reserve an interrupt to be used outside of this framework.

This will mark a certain interrupt on the specified CPU as reserved, not to be allocated for any reason.

Parameters
:   | intno | The number of the interrupt (0-31) |
    | --- | --- |
    | cpu | CPU on which the interrupt should be marked as shared (0 or 1) |

Returns
:   -EINVAL if cpu or intno is invalid 0 otherwise

## [◆ ](#af1417d7a4a9faba280ac4e17c9ee60ab)esp\_intr\_set\_in\_iram()

| int esp\_intr\_set\_in\_iram | ( | struct [intr\_handle\_data\_t](structintr__handle__data__t.md) \* | *handle*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *is\_in\_iram* ) |

Set the "in IRAM" status of the handler.

Note
:   Does not work on shared interrupts.

Parameters
:   | handle | The handle, as obtained by esp\_intr\_alloc or esp\_intr\_alloc\_intrstatus |
    | --- | --- |
    | is\_in\_iram | Whether the handler associated with this handle resides in IRAM. Handlers residing in IRAM can be called when cache is disabled. |

Returns
:   -EINVAL if the combination of arguments is invalid. 0 otherwise

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_esp32.h](intc__esp32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
