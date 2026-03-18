---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/intc__mchp__xec__ecia_8h.html
original_path: doxygen/html/intc__mchp__xec__ecia_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_mchp\_xec\_ecia.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/irq.h](irq_8h_source.md)>`

[Go to the source code of this file.](intc__mchp__xec__ecia_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [mchp\_xec\_ecia\_callback\_t](#a946f876915453dd27eccc24d3e39210a)) (int girq\_id, int src, void \*user) |

| Functions | |
| --- | --- |
| int | [mchp\_xec\_ecia\_enable](#a91e7ab27d1b62f72a392ebbb5c38a4d8) (int girq\_id, int src) |
|  | Driver for External interrupt controller in Microchip XEC devices. |
| int | [mchp\_xec\_ecia\_info\_enable](#a9026ff2f7a60f8e244537cbab4a0e891) (int ecia\_info) |
|  | enable EXTI interrupt for specific line specified by parameter encoded with MCHP\_XEC\_ECIA macro. |
| int | [mchp\_xec\_ecia\_disable](#a6432ee01ae43598bc7ee8387f38ce5de) (int girq\_id, int src) |
|  | disable EXTI interrupt for specific line |
| int | [mchp\_xec\_ecia\_info\_disable](#a363949f5b133f05b94dd8f17d572bbac) (int ecia\_info) |
|  | disable EXTI interrupt for specific line specified by parameter encoded with MCHP\_XEC\_ECIA macro. |
| int | [mchp\_xec\_ecia\_set\_callback](#a980dfa5d5751cdefd5c911e6cac6075d) (int girq\_id, int src, [mchp\_xec\_ecia\_callback\_t](#a946f876915453dd27eccc24d3e39210a) cb, void \*data) |
|  | set GIRQn interrupt source callback |
| int | [mchp\_xec\_ecia\_info\_set\_callback](#a1b75b3213eace2931bfee965bb2bc1b9) (int ecia\_info, [mchp\_xec\_ecia\_callback\_t](#a946f876915453dd27eccc24d3e39210a) cb, void \*data) |
|  | set GIRQn interrupt source callback |
| int | [mchp\_xec\_ecia\_set\_callback\_by\_dev](#a65d91d241885c1b8ff7bdc7bd92e2a13) (const struct [device](structdevice.md) \*dev\_girq, int src, [mchp\_xec\_ecia\_callback\_t](#a946f876915453dd27eccc24d3e39210a) cb, void \*data) |
|  | set GIRQn interrupt source callback |
| int | [mchp\_ecia\_unset\_callback](#a636a559083647193d154076c8d901bb5) (int girq\_id, int src) |
|  | unset GIRQn interrupt source callback |
| int | [mchp\_ecia\_unset\_callback\_by\_dev](#a756f04d2ad6680d4324326244f0b84b0) (const struct [device](structdevice.md) \*dev\_girq, int src) |
|  | unset GIRQn interrupt source callback |
| void | [mchp\_xec\_ecia\_girq\_aggr\_en](#aa0acc2a2f6fe2c21e385aeb650d4e195) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) enable) |
|  | enable or disable aggregated GIRQ output |
| void | [mchp\_xec\_ecia\_girq\_src\_clr](#a042b0afeb07493d13b068b26bc20c4f3) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_bit) |
|  | clear GIRQ latched source status bit |
| void | [mchp\_xec\_ecia\_girq\_src\_en](#afce3bbeeb977efc4349d58e676c17fbe) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_bit) |
|  | enable a source in a GIRQ |
| void | [mchp\_xec\_ecia\_girq\_src\_dis](#a4335e0f409723ffef63198b4ec026fe7) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_bit) |
|  | disable a source in a GIRQ |
| void | [mchp\_xec\_ecia\_girq\_src\_clr\_bitmap](#a61c65d98a3781449fcb2363029fa0856) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitmap) |
|  | clear GIRQ latches sources specified in bitmap |
| void | [mchp\_xec\_ecia\_girq\_src\_en\_bitmap](#ab6d12794d0c1762efc2fdeb1a337580b) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitmap) |
|  | enable sources in a GIRQ |
| void | [mchp\_xec\_ecia\_girq\_src\_dis\_bitmap](#a44d6bffbe40f09fc063580f9bb936cd8) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitmap) |
|  | disable sources in a GIRQ |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mchp\_xec\_ecia\_girq\_result](#a96a9db2c2a7e650c87457a1f5b1b395a) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id) |
|  | Read GIRQ result register (bit-wise OR of enable and source). |
| void | [mchp\_xec\_ecia\_nvic\_clr\_pend](#ac563ac5fcc47e2b3b375ce4d3ade897b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) nvic\_num) |
|  | Clear external NVIC input pending status. |
| void | [mchp\_xec\_ecia\_info\_girq\_aggr\_en](#a4dab0aa1c6f77906ecd618d4269cf764) (int ecia\_info, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) enable) |
|  | enable or disable aggregated GIRQ output |
| void | [mchp\_xec\_ecia\_info\_girq\_src\_clr](#a73c19286d1f406aef34a4bda562d933b) (int ecia\_info) |
|  | clear GIRQ latched source status bit |
| void | [mchp\_xec\_ecia\_info\_girq\_src\_en](#a5a4b9d83a396438e22f1c694b7e7c82a) (int ecia\_info) |
|  | enable a source in a GIRQ |
| void | [mchp\_xec\_ecia\_info\_girq\_src\_dis](#af90b2ce499b8109bae272d5bac444f51) (int ecia\_info) |
|  | disable a source in a GIRQ |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mchp\_xec\_ecia\_info\_girq\_result](#a38ce7498c75d5f8c44facc3a625edbe9) (int ecia\_info) |
|  | Read GIRQ result register (bit-wise OR of enable and source). |
| void | [mchp\_xec\_ecia\_info\_nvic\_clr\_pend](#a94b5aa34aaacb1e59ba2dffd625b200c) (int ecia\_info) |
|  | Clear external NVIC input pending status given encoded ECIA info. |

## Typedef Documentation

## [◆ ](#a946f876915453dd27eccc24d3e39210a)mchp\_xec\_ecia\_callback\_t

| typedef void(\* mchp\_xec\_ecia\_callback\_t) (int girq\_id, int src, void \*user) |
| --- |

## Function Documentation

## [◆ ](#a636a559083647193d154076c8d901bb5)mchp\_ecia\_unset\_callback()

| int mchp\_ecia\_unset\_callback | ( | int | *girq\_id*, |
| --- | --- | --- | --- |
|  |  | int | *src* ) |

unset GIRQn interrupt source callback

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |
    | src | is the interrupt source in the GIRQ (0 - 31) |

## [◆ ](#a756f04d2ad6680d4324326244f0b84b0)mchp\_ecia\_unset\_callback\_by\_dev()

| int mchp\_ecia\_unset\_callback\_by\_dev | ( | const struct [device](structdevice.md) \* | *dev\_girq*, |
| --- | --- | --- | --- |
|  |  | int | *src* ) |

unset GIRQn interrupt source callback

Parameters
:   | dev\_girq | is a handle to the GIRQn device |
    | --- | --- |
    | src | is the interrupt source in the GIRQ (0 - 31) |

## [◆ ](#a6432ee01ae43598bc7ee8387f38ce5de)mchp\_xec\_ecia\_disable()

| int mchp\_xec\_ecia\_disable | ( | int | *girq\_id*, |
| --- | --- | --- | --- |
|  |  | int | *src* ) |

disable EXTI interrupt for specific line

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |
    | src | is the interrupt source in the GIRQ (0 - 31) |

## [◆ ](#a91e7ab27d1b62f72a392ebbb5c38a4d8)mchp\_xec\_ecia\_enable()

| int mchp\_xec\_ecia\_enable | ( | int | *girq\_id*, |
| --- | --- | --- | --- |
|  |  | int | *src* ) |

Driver for External interrupt controller in Microchip XEC devices.

Based on reference manuals: Reference Manuals for MEC152x and MEC172x ARM(r) 32-bit MCUs

Chapter: EC Interrupt Aggregator (ECIA)

enable GIRQn interrupt for specific source

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |
    | src | is the interrupt source in the GIRQ (0 - 31) |

## [◆ ](#aa0acc2a2f6fe2c21e385aeb650d4e195)mchp\_xec\_ecia\_girq\_aggr\_en()

| void mchp\_xec\_ecia\_girq\_aggr\_en | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *girq\_id*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *enable* ) |

enable or disable aggregated GIRQ output

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |
    | enable | non-zero enables aggregated output else disables |

## [◆ ](#a96a9db2c2a7e650c87457a1f5b1b395a)mchp\_xec\_ecia\_girq\_result()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mchp\_xec\_ecia\_girq\_result | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *girq\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

Read GIRQ result register (bit-wise OR of enable and source).

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |

Returns
:   32-bit unsigned result register value

## [◆ ](#a042b0afeb07493d13b068b26bc20c4f3)mchp\_xec\_ecia\_girq\_src\_clr()

| void mchp\_xec\_ecia\_girq\_src\_clr | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *girq\_id*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src\_bit* ) |

clear GIRQ latched source status bit

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |
    | src\_bit | is the source bit position in the GIRQ registers (0 - 31) |

## [◆ ](#a61c65d98a3781449fcb2363029fa0856)mchp\_xec\_ecia\_girq\_src\_clr\_bitmap()

| void mchp\_xec\_ecia\_girq\_src\_clr\_bitmap | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *girq\_id*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *bitmap* ) |

clear GIRQ latches sources specified in bitmap

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |
    | bitmap | contains the source bits to clear |

## [◆ ](#a4335e0f409723ffef63198b4ec026fe7)mchp\_xec\_ecia\_girq\_src\_dis()

| void mchp\_xec\_ecia\_girq\_src\_dis | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *girq\_id*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src\_bit* ) |

disable a source in a GIRQ

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |
    | src\_bit | is the source bit position in the GIRQ registers (0 - 31) |

## [◆ ](#a44d6bffbe40f09fc063580f9bb936cd8)mchp\_xec\_ecia\_girq\_src\_dis\_bitmap()

| void mchp\_xec\_ecia\_girq\_src\_dis\_bitmap | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *girq\_id*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *bitmap* ) |

disable sources in a GIRQ

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |
    | bitmap | contains the source bits to disable |

## [◆ ](#afce3bbeeb977efc4349d58e676c17fbe)mchp\_xec\_ecia\_girq\_src\_en()

| void mchp\_xec\_ecia\_girq\_src\_en | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *girq\_id*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src\_bit* ) |

enable a source in a GIRQ

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |
    | src\_bit | is the source bit position in the GIRQ registers (0 - 31) |

## [◆ ](#ab6d12794d0c1762efc2fdeb1a337580b)mchp\_xec\_ecia\_girq\_src\_en\_bitmap()

| void mchp\_xec\_ecia\_girq\_src\_en\_bitmap | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *girq\_id*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *bitmap* ) |

enable sources in a GIRQ

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |
    | bitmap | contains the source bits to enable |

## [◆ ](#a363949f5b133f05b94dd8f17d572bbac)mchp\_xec\_ecia\_info\_disable()

| int mchp\_xec\_ecia\_info\_disable | ( | int | *ecia\_info* | ) |  |
| --- | --- | --- | --- | --- | --- |

disable EXTI interrupt for specific line specified by parameter encoded with MCHP\_XEC\_ECIA macro.

Parameters
:   | ecia\_info | is GIRQ connection encoded with MCHP\_XEC\_ECIA |
    | --- | --- |

## [◆ ](#a9026ff2f7a60f8e244537cbab4a0e891)mchp\_xec\_ecia\_info\_enable()

| int mchp\_xec\_ecia\_info\_enable | ( | int | *ecia\_info* | ) |  |
| --- | --- | --- | --- | --- | --- |

enable EXTI interrupt for specific line specified by parameter encoded with MCHP\_XEC\_ECIA macro.

Parameters
:   | ecia\_info | is GIRQ connection encoded with MCHP\_XEC\_ECIA |
    | --- | --- |

## [◆ ](#a4dab0aa1c6f77906ecd618d4269cf764)mchp\_xec\_ecia\_info\_girq\_aggr\_en()

| void mchp\_xec\_ecia\_info\_girq\_aggr\_en | ( | int | *ecia\_info*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *enable* ) |

enable or disable aggregated GIRQ output

Parameters
:   | ecia\_info | is GIRQ connection encoded with MCHP\_XEC\_ECIA |
    | --- | --- |
    | enable | is flag to indicate enable(1) or disable(0) |

## [◆ ](#a38ce7498c75d5f8c44facc3a625edbe9)mchp\_xec\_ecia\_info\_girq\_result()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mchp\_xec\_ecia\_info\_girq\_result | ( | int | *ecia\_info* | ) |  |
| --- | --- | --- | --- | --- | --- |

Read GIRQ result register (bit-wise OR of enable and source).

Parameters
:   | ecia\_info | is GIRQ connection encoded with MCHP\_XEC\_ECIA |
    | --- | --- |

Returns
:   32-bit unsigned result register value

## [◆ ](#a73c19286d1f406aef34a4bda562d933b)mchp\_xec\_ecia\_info\_girq\_src\_clr()

| void mchp\_xec\_ecia\_info\_girq\_src\_clr | ( | int | *ecia\_info* | ) |  |
| --- | --- | --- | --- | --- | --- |

clear GIRQ latched source status bit

Parameters
:   | ecia\_info | is GIRQ connection encoded with MCHP\_XEC\_ECIA |
    | --- | --- |

## [◆ ](#af90b2ce499b8109bae272d5bac444f51)mchp\_xec\_ecia\_info\_girq\_src\_dis()

| void mchp\_xec\_ecia\_info\_girq\_src\_dis | ( | int | *ecia\_info* | ) |  |
| --- | --- | --- | --- | --- | --- |

disable a source in a GIRQ

Parameters
:   | ecia\_info | is GIRQ connection encoded with MCHP\_XEC\_ECIA |
    | --- | --- |

## [◆ ](#a5a4b9d83a396438e22f1c694b7e7c82a)mchp\_xec\_ecia\_info\_girq\_src\_en()

| void mchp\_xec\_ecia\_info\_girq\_src\_en | ( | int | *ecia\_info* | ) |  |
| --- | --- | --- | --- | --- | --- |

enable a source in a GIRQ

Parameters
:   | ecia\_info | is GIRQ connection encoded with MCHP\_XEC\_ECIA |
    | --- | --- |

## [◆ ](#a94b5aa34aaacb1e59ba2dffd625b200c)mchp\_xec\_ecia\_info\_nvic\_clr\_pend()

| void mchp\_xec\_ecia\_info\_nvic\_clr\_pend | ( | int | *ecia\_info* | ) |  |
| --- | --- | --- | --- | --- | --- |

Clear external NVIC input pending status given encoded ECIA info.

Parameters
:   | ecia\_info | is GIRQ connection encoded with MCHP\_XEC\_ECIA |
    | --- | --- |

## [◆ ](#a1b75b3213eace2931bfee965bb2bc1b9)mchp\_xec\_ecia\_info\_set\_callback()

| int mchp\_xec\_ecia\_info\_set\_callback | ( | int | *ecia\_info*, |
| --- | --- | --- | --- |
|  |  | [mchp\_xec\_ecia\_callback\_t](#a946f876915453dd27eccc24d3e39210a) | *cb*, |
|  |  | void \* | *data* ) |

set GIRQn interrupt source callback

Parameters
:   | ecia\_info | is GIRQ connection encoded with MCHP\_XEC\_ECIA |
    | --- | --- |
    | cb | user callback |
    | data | user data |

## [◆ ](#ac563ac5fcc47e2b3b375ce4d3ade897b)mchp\_xec\_ecia\_nvic\_clr\_pend()

| void mchp\_xec\_ecia\_nvic\_clr\_pend | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *nvic\_num* | ) |  |
| --- | --- | --- | --- | --- | --- |

Clear external NVIC input pending status.

Parameters
:   | nvic\_num | is 0 to maximum NVIC inputs for the chip. |
    | --- | --- |

## [◆ ](#a980dfa5d5751cdefd5c911e6cac6075d)mchp\_xec\_ecia\_set\_callback()

| int mchp\_xec\_ecia\_set\_callback | ( | int | *girq\_id*, |
| --- | --- | --- | --- |
|  |  | int | *src*, |
|  |  | [mchp\_xec\_ecia\_callback\_t](#a946f876915453dd27eccc24d3e39210a) | *cb*, |
|  |  | void \* | *data* ) |

set GIRQn interrupt source callback

Parameters
:   | girq\_id | is the GIRQ number (8 - 26) |
    | --- | --- |
    | src | is the interrupt source in the GIRQ (0 - 31) |
    | cb | user callback |
    | data | user data |

## [◆ ](#a65d91d241885c1b8ff7bdc7bd92e2a13)mchp\_xec\_ecia\_set\_callback\_by\_dev()

| int mchp\_xec\_ecia\_set\_callback\_by\_dev | ( | const struct [device](structdevice.md) \* | *dev\_girq*, |
| --- | --- | --- | --- |
|  |  | int | *src*, |
|  |  | [mchp\_xec\_ecia\_callback\_t](#a946f876915453dd27eccc24d3e39210a) | *cb*, |
|  |  | void \* | *data* ) |

set GIRQn interrupt source callback

Parameters
:   | dev\_girq | is a handle to the GIRQn device |
    | --- | --- |
    | src | is the interrupt source in the GIRQ (0 - 31) |
    | cb | user callback |
    | data | user data |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_mchp\_xec\_ecia.h](intc__mchp__xec__ecia_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
