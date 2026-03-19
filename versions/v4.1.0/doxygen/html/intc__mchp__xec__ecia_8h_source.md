---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__mchp__xec__ecia_8h_source.html
original_path: doxygen/html/intc__mchp__xec__ecia_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_mchp\_xec\_ecia.h

[Go to the documentation of this file.](intc__mchp__xec__ecia_8h.md)

1/\*

2 \* Copyright (c) 2021 Microchip Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

16

17#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_MCHP\_XEC\_ECIA\_H\_

18#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_MCHP\_XEC\_ECIA\_H\_

19

20#include <[zephyr/device.h](device_8h.md)>

21#include <[zephyr/irq.h](irq_8h.md)>

22

[ 29](intc__mchp__xec__ecia_8h.md#a91e7ab27d1b62f72a392ebbb5c38a4d8)int [mchp\_xec\_ecia\_enable](intc__mchp__xec__ecia_8h.md#a91e7ab27d1b62f72a392ebbb5c38a4d8)(int girq\_id, int src);

30

[ 37](intc__mchp__xec__ecia_8h.md#a9026ff2f7a60f8e244537cbab4a0e891)int [mchp\_xec\_ecia\_info\_enable](intc__mchp__xec__ecia_8h.md#a9026ff2f7a60f8e244537cbab4a0e891)(int ecia\_info);

38

[ 45](intc__mchp__xec__ecia_8h.md#a6432ee01ae43598bc7ee8387f38ce5de)int [mchp\_xec\_ecia\_disable](intc__mchp__xec__ecia_8h.md#a6432ee01ae43598bc7ee8387f38ce5de)(int girq\_id, int src);

46

[ 53](intc__mchp__xec__ecia_8h.md#a363949f5b133f05b94dd8f17d572bbac)int [mchp\_xec\_ecia\_info\_disable](intc__mchp__xec__ecia_8h.md#a363949f5b133f05b94dd8f17d572bbac)(int ecia\_info);

54

55

56/\* callback for ECIA GIRQ interrupt source \*/

[ 57](intc__mchp__xec__ecia_8h.md#a946f876915453dd27eccc24d3e39210a)typedef void (\*[mchp\_xec\_ecia\_callback\_t](intc__mchp__xec__ecia_8h.md#a946f876915453dd27eccc24d3e39210a)) (int girq\_id, int src, void \*user);

58

[ 67](intc__mchp__xec__ecia_8h.md#a980dfa5d5751cdefd5c911e6cac6075d)int [mchp\_xec\_ecia\_set\_callback](intc__mchp__xec__ecia_8h.md#a980dfa5d5751cdefd5c911e6cac6075d)(int girq\_id, int src,

68 [mchp\_xec\_ecia\_callback\_t](intc__mchp__xec__ecia_8h.md#a946f876915453dd27eccc24d3e39210a) cb, void \*data);

69

[ 77](intc__mchp__xec__ecia_8h.md#a1b75b3213eace2931bfee965bb2bc1b9)int [mchp\_xec\_ecia\_info\_set\_callback](intc__mchp__xec__ecia_8h.md#a1b75b3213eace2931bfee965bb2bc1b9)(int ecia\_info, [mchp\_xec\_ecia\_callback\_t](intc__mchp__xec__ecia_8h.md#a946f876915453dd27eccc24d3e39210a) cb,

78 void \*data);

79

[ 88](intc__mchp__xec__ecia_8h.md#a65d91d241885c1b8ff7bdc7bd92e2a13)int [mchp\_xec\_ecia\_set\_callback\_by\_dev](intc__mchp__xec__ecia_8h.md#a65d91d241885c1b8ff7bdc7bd92e2a13)(const struct [device](structdevice.md) \*dev\_girq, int src,

89 [mchp\_xec\_ecia\_callback\_t](intc__mchp__xec__ecia_8h.md#a946f876915453dd27eccc24d3e39210a) cb, void \*data);

90

[ 97](intc__mchp__xec__ecia_8h.md#a636a559083647193d154076c8d901bb5)int [mchp\_ecia\_unset\_callback](intc__mchp__xec__ecia_8h.md#a636a559083647193d154076c8d901bb5)(int girq\_id, int src);

98

[ 105](intc__mchp__xec__ecia_8h.md#a756f04d2ad6680d4324326244f0b84b0)int [mchp\_ecia\_unset\_callback\_by\_dev](intc__mchp__xec__ecia_8h.md#a756f04d2ad6680d4324326244f0b84b0)(const struct [device](structdevice.md) \*dev\_girq, int src);

106

107/\* platform specific \*/

[ 113](intc__mchp__xec__ecia_8h.md#aa0acc2a2f6fe2c21e385aeb650d4e195)void [mchp\_xec\_ecia\_girq\_aggr\_en](intc__mchp__xec__ecia_8h.md#aa0acc2a2f6fe2c21e385aeb650d4e195)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) enable);

114

[ 120](intc__mchp__xec__ecia_8h.md#a042b0afeb07493d13b068b26bc20c4f3)void [mchp\_xec\_ecia\_girq\_src\_clr](intc__mchp__xec__ecia_8h.md#a042b0afeb07493d13b068b26bc20c4f3)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_bit);

121

[ 127](intc__mchp__xec__ecia_8h.md#afce3bbeeb977efc4349d58e676c17fbe)void [mchp\_xec\_ecia\_girq\_src\_en](intc__mchp__xec__ecia_8h.md#afce3bbeeb977efc4349d58e676c17fbe)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_bit);

128

[ 134](intc__mchp__xec__ecia_8h.md#a4335e0f409723ffef63198b4ec026fe7)void [mchp\_xec\_ecia\_girq\_src\_dis](intc__mchp__xec__ecia_8h.md#a4335e0f409723ffef63198b4ec026fe7)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src\_bit);

135

[ 141](intc__mchp__xec__ecia_8h.md#a61c65d98a3781449fcb2363029fa0856)void [mchp\_xec\_ecia\_girq\_src\_clr\_bitmap](intc__mchp__xec__ecia_8h.md#a61c65d98a3781449fcb2363029fa0856)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitmap);

142

[ 148](intc__mchp__xec__ecia_8h.md#ab6d12794d0c1762efc2fdeb1a337580b)void [mchp\_xec\_ecia\_girq\_src\_en\_bitmap](intc__mchp__xec__ecia_8h.md#ab6d12794d0c1762efc2fdeb1a337580b)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitmap);

149

[ 155](intc__mchp__xec__ecia_8h.md#a44d6bffbe40f09fc063580f9bb936cd8)void [mchp\_xec\_ecia\_girq\_src\_dis\_bitmap](intc__mchp__xec__ecia_8h.md#a44d6bffbe40f09fc063580f9bb936cd8)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitmap);

156

[ 162](intc__mchp__xec__ecia_8h.md#a96a9db2c2a7e650c87457a1f5b1b395a)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mchp\_xec\_ecia\_girq\_result](intc__mchp__xec__ecia_8h.md#a96a9db2c2a7e650c87457a1f5b1b395a)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) girq\_id);

163

[ 168](intc__mchp__xec__ecia_8h.md#ac563ac5fcc47e2b3b375ce4d3ade897b)void [mchp\_xec\_ecia\_nvic\_clr\_pend](intc__mchp__xec__ecia_8h.md#ac563ac5fcc47e2b3b375ce4d3ade897b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) nvic\_num);

169

170/\* API using GIRQ parameters encoded with MCHP\_XEC\_ECIA \*/

171

[ 177](intc__mchp__xec__ecia_8h.md#a4dab0aa1c6f77906ecd618d4269cf764)void [mchp\_xec\_ecia\_info\_girq\_aggr\_en](intc__mchp__xec__ecia_8h.md#a4dab0aa1c6f77906ecd618d4269cf764)(int ecia\_info, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) enable);

178

[ 183](intc__mchp__xec__ecia_8h.md#a73c19286d1f406aef34a4bda562d933b)void [mchp\_xec\_ecia\_info\_girq\_src\_clr](intc__mchp__xec__ecia_8h.md#a73c19286d1f406aef34a4bda562d933b)(int ecia\_info);

184

[ 189](intc__mchp__xec__ecia_8h.md#a5a4b9d83a396438e22f1c694b7e7c82a)void [mchp\_xec\_ecia\_info\_girq\_src\_en](intc__mchp__xec__ecia_8h.md#a5a4b9d83a396438e22f1c694b7e7c82a)(int ecia\_info);

190

[ 195](intc__mchp__xec__ecia_8h.md#af90b2ce499b8109bae272d5bac444f51)void [mchp\_xec\_ecia\_info\_girq\_src\_dis](intc__mchp__xec__ecia_8h.md#af90b2ce499b8109bae272d5bac444f51)(int ecia\_info);

196

[ 202](intc__mchp__xec__ecia_8h.md#a38ce7498c75d5f8c44facc3a625edbe9)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mchp\_xec\_ecia\_info\_girq\_result](intc__mchp__xec__ecia_8h.md#a38ce7498c75d5f8c44facc3a625edbe9)(int ecia\_info);

203

[ 208](intc__mchp__xec__ecia_8h.md#a94b5aa34aaacb1e59ba2dffd625b200c)void [mchp\_xec\_ecia\_info\_nvic\_clr\_pend](intc__mchp__xec__ecia_8h.md#a94b5aa34aaacb1e59ba2dffd625b200c)(int ecia\_info);

209

210#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_MCHP\_XEC\_ECIA\_H\_ \*/

[device.h](device_8h.md)

[mchp\_xec\_ecia\_girq\_src\_clr](intc__mchp__xec__ecia_8h.md#a042b0afeb07493d13b068b26bc20c4f3)

void mchp\_xec\_ecia\_girq\_src\_clr(uint8\_t girq\_id, uint8\_t src\_bit)

clear GIRQ latched source status bit

[mchp\_xec\_ecia\_info\_set\_callback](intc__mchp__xec__ecia_8h.md#a1b75b3213eace2931bfee965bb2bc1b9)

int mchp\_xec\_ecia\_info\_set\_callback(int ecia\_info, mchp\_xec\_ecia\_callback\_t cb, void \*data)

set GIRQn interrupt source callback

[mchp\_xec\_ecia\_info\_disable](intc__mchp__xec__ecia_8h.md#a363949f5b133f05b94dd8f17d572bbac)

int mchp\_xec\_ecia\_info\_disable(int ecia\_info)

disable EXTI interrupt for specific line specified by parameter encoded with MCHP\_XEC\_ECIA macro.

[mchp\_xec\_ecia\_info\_girq\_result](intc__mchp__xec__ecia_8h.md#a38ce7498c75d5f8c44facc3a625edbe9)

uint32\_t mchp\_xec\_ecia\_info\_girq\_result(int ecia\_info)

Read GIRQ result register (bit-wise OR of enable and source).

[mchp\_xec\_ecia\_girq\_src\_dis](intc__mchp__xec__ecia_8h.md#a4335e0f409723ffef63198b4ec026fe7)

void mchp\_xec\_ecia\_girq\_src\_dis(uint8\_t girq\_id, uint8\_t src\_bit)

disable a source in a GIRQ

[mchp\_xec\_ecia\_girq\_src\_dis\_bitmap](intc__mchp__xec__ecia_8h.md#a44d6bffbe40f09fc063580f9bb936cd8)

void mchp\_xec\_ecia\_girq\_src\_dis\_bitmap(uint8\_t girq\_id, uint32\_t bitmap)

disable sources in a GIRQ

[mchp\_xec\_ecia\_info\_girq\_aggr\_en](intc__mchp__xec__ecia_8h.md#a4dab0aa1c6f77906ecd618d4269cf764)

void mchp\_xec\_ecia\_info\_girq\_aggr\_en(int ecia\_info, uint8\_t enable)

enable or disable aggregated GIRQ output

[mchp\_xec\_ecia\_info\_girq\_src\_en](intc__mchp__xec__ecia_8h.md#a5a4b9d83a396438e22f1c694b7e7c82a)

void mchp\_xec\_ecia\_info\_girq\_src\_en(int ecia\_info)

enable a source in a GIRQ

[mchp\_xec\_ecia\_girq\_src\_clr\_bitmap](intc__mchp__xec__ecia_8h.md#a61c65d98a3781449fcb2363029fa0856)

void mchp\_xec\_ecia\_girq\_src\_clr\_bitmap(uint8\_t girq\_id, uint32\_t bitmap)

clear GIRQ latches sources specified in bitmap

[mchp\_ecia\_unset\_callback](intc__mchp__xec__ecia_8h.md#a636a559083647193d154076c8d901bb5)

int mchp\_ecia\_unset\_callback(int girq\_id, int src)

unset GIRQn interrupt source callback

[mchp\_xec\_ecia\_disable](intc__mchp__xec__ecia_8h.md#a6432ee01ae43598bc7ee8387f38ce5de)

int mchp\_xec\_ecia\_disable(int girq\_id, int src)

disable EXTI interrupt for specific line

[mchp\_xec\_ecia\_set\_callback\_by\_dev](intc__mchp__xec__ecia_8h.md#a65d91d241885c1b8ff7bdc7bd92e2a13)

int mchp\_xec\_ecia\_set\_callback\_by\_dev(const struct device \*dev\_girq, int src, mchp\_xec\_ecia\_callback\_t cb, void \*data)

set GIRQn interrupt source callback

[mchp\_xec\_ecia\_info\_girq\_src\_clr](intc__mchp__xec__ecia_8h.md#a73c19286d1f406aef34a4bda562d933b)

void mchp\_xec\_ecia\_info\_girq\_src\_clr(int ecia\_info)

clear GIRQ latched source status bit

[mchp\_ecia\_unset\_callback\_by\_dev](intc__mchp__xec__ecia_8h.md#a756f04d2ad6680d4324326244f0b84b0)

int mchp\_ecia\_unset\_callback\_by\_dev(const struct device \*dev\_girq, int src)

unset GIRQn interrupt source callback

[mchp\_xec\_ecia\_info\_enable](intc__mchp__xec__ecia_8h.md#a9026ff2f7a60f8e244537cbab4a0e891)

int mchp\_xec\_ecia\_info\_enable(int ecia\_info)

enable EXTI interrupt for specific line specified by parameter encoded with MCHP\_XEC\_ECIA macro.

[mchp\_xec\_ecia\_enable](intc__mchp__xec__ecia_8h.md#a91e7ab27d1b62f72a392ebbb5c38a4d8)

int mchp\_xec\_ecia\_enable(int girq\_id, int src)

Driver for External interrupt controller in Microchip XEC devices.

[mchp\_xec\_ecia\_callback\_t](intc__mchp__xec__ecia_8h.md#a946f876915453dd27eccc24d3e39210a)

void(\* mchp\_xec\_ecia\_callback\_t)(int girq\_id, int src, void \*user)

**Definition** intc\_mchp\_xec\_ecia.h:57

[mchp\_xec\_ecia\_info\_nvic\_clr\_pend](intc__mchp__xec__ecia_8h.md#a94b5aa34aaacb1e59ba2dffd625b200c)

void mchp\_xec\_ecia\_info\_nvic\_clr\_pend(int ecia\_info)

Clear external NVIC input pending status given encoded ECIA info.

[mchp\_xec\_ecia\_girq\_result](intc__mchp__xec__ecia_8h.md#a96a9db2c2a7e650c87457a1f5b1b395a)

uint32\_t mchp\_xec\_ecia\_girq\_result(uint8\_t girq\_id)

Read GIRQ result register (bit-wise OR of enable and source).

[mchp\_xec\_ecia\_set\_callback](intc__mchp__xec__ecia_8h.md#a980dfa5d5751cdefd5c911e6cac6075d)

int mchp\_xec\_ecia\_set\_callback(int girq\_id, int src, mchp\_xec\_ecia\_callback\_t cb, void \*data)

set GIRQn interrupt source callback

[mchp\_xec\_ecia\_girq\_aggr\_en](intc__mchp__xec__ecia_8h.md#aa0acc2a2f6fe2c21e385aeb650d4e195)

void mchp\_xec\_ecia\_girq\_aggr\_en(uint8\_t girq\_id, uint8\_t enable)

enable or disable aggregated GIRQ output

[mchp\_xec\_ecia\_girq\_src\_en\_bitmap](intc__mchp__xec__ecia_8h.md#ab6d12794d0c1762efc2fdeb1a337580b)

void mchp\_xec\_ecia\_girq\_src\_en\_bitmap(uint8\_t girq\_id, uint32\_t bitmap)

enable sources in a GIRQ

[mchp\_xec\_ecia\_nvic\_clr\_pend](intc__mchp__xec__ecia_8h.md#ac563ac5fcc47e2b3b375ce4d3ade897b)

void mchp\_xec\_ecia\_nvic\_clr\_pend(uint32\_t nvic\_num)

Clear external NVIC input pending status.

[mchp\_xec\_ecia\_info\_girq\_src\_dis](intc__mchp__xec__ecia_8h.md#af90b2ce499b8109bae272d5bac444f51)

void mchp\_xec\_ecia\_info\_girq\_src\_dis(int ecia\_info)

disable a source in a GIRQ

[mchp\_xec\_ecia\_girq\_src\_en](intc__mchp__xec__ecia_8h.md#afce3bbeeb977efc4349d58e676c17fbe)

void mchp\_xec\_ecia\_girq\_src\_en(uint8\_t girq\_id, uint8\_t src\_bit)

enable a source in a GIRQ

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_mchp\_xec\_ecia.h](intc__mchp__xec__ecia_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
