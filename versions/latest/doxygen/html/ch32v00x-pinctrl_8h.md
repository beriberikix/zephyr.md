---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ch32v00x-pinctrl_8h.html
original_path: doxygen/html/ch32v00x-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ch32v00x-pinctrl.h File Reference

[Go to the source code of this file.](ch32v00x-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CH32V00X\_PINMUX\_PORT\_PA](#a342a836de3a2ffdda83f5c3d57966abf)   0 |
| #define | [CH32V00X\_PINMUX\_PORT\_PB](#ae9f35f667ca89936c8ad246287bf9f43)   1 |
| #define | [CH32V00X\_PINMUX\_PORT\_PC](#a1e2d2bd6331286774357771211bebdff)   2 |
| #define | [CH32V00X\_PINMUX\_PORT\_PD](#a97f123c1518d8c9c66e97166fc8a5ab6)   3 |
| #define | [CH32V00X\_PINMUX\_SPI1\_RM](#a3c398e69bd9aba0d8ef646f31e4d98d3)   0 |
| #define | [CH32V00X\_PINMUX\_I2C1\_RM](#a38bd15803e839874fd1db5408f03f330)   3 |
| #define | [CH32V00X\_PINMUX\_USART1\_RM](#a46a8b78e5eed35dab015c9c09fac238f)   6 |
| #define | [CH32V00X\_PINMUX\_TIM1\_RM](#aecf76dc2f53a7ae6c5226fd51185dfa8)   10 |
| #define | [CH32V00X\_PINMUX\_TIM2\_RM](#aacb406305b44a788dc831829f719fed0)   14 |
| #define | [CH32V00X\_PINMUX\_PA1PA2\_RM](#ae4299414eb81619866db635b1f3632a2)   17 |
| #define | [CH32V00X\_PINMUX\_ADC\_DTR\_GINJ\_RM](#a10d20ad95129b7e6ddcf331582d13897)   18 |
| #define | [CH32V00X\_PINMUX\_ADC\_DTR\_GREG\_RM](#a9a2214e447c9d821340803dbd5c9a1ef)   19 |
| #define | [CH32V00X\_PINMUX\_USART2\_RM](#a5b7e2562a6a6c664e9e0ca1b6de5d4df)   20 |
| #define | [CH32V00X\_PINCTRL\_PORT\_SHIFT](#abc6ff06e0fcacdbfa4a05066e87904a7)   0 |
| #define | [CH32V00X\_PINCTRL\_PORT\_MASK](#a7d221d51318c7235b823651802a25192)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| #define | [CH32V00X\_PINCTRL\_PIN\_SHIFT](#a16dd7dab2521cfbfec5860a6bea3820e)   2 |
| #define | [CH32V00X\_PINCTRL\_PIN\_MASK](#a252c604982e448ab4e2f7333a431bdb6)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 2) |
| #define | [CH32V00X\_PINCTRL\_BASE\_SHIFT](#a32c6a5a4f753487e92c5b0add73c0a97)   5 |
| #define | [CH32V00X\_PINCTRL\_BASE\_MASK](#ab30a0f46632e9eb8529306664c618eae)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(9, 5) |
| #define | [CH32V00X\_PINCTRL\_RM\_SHIFT](#a94441bfaa665e8f31bcead94137e5c05)   10 |
| #define | [CH32V00X\_PINCTRL\_RM\_MASK](#ac1154192c3a9120cbb1dfbf28400e664)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(12, 10) |
| #define | [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(port, pin, rm, remapping) |
| #define | [TIM1\_ETR\_PC5\_0](#a8fca20f25cd86b6185a1c2674342bc48)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 0) |
| #define | [TIM1\_ETR\_PD4\_1](#aaae81f3909b0a548b6971e4f5ad727eb)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM1, 1) |
| #define | [TIM1\_ETR\_PC5\_2](#a44dd79259ce6ff88ee97a6f5e2ae93c8)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 2) |
| #define | [TIM1\_ETR\_PC2\_3](#af03e0801b80f311ffa8ff53f71e895b6)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 3) |
| #define | [TIM1\_ETR\_PD4\_4](#a880fc5b619497c9ad0d3f7cbfab85649)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM1, 4) |
| #define | [TIM1\_ETR\_PD4\_5](#a5c196d9f8fe45f609fb45849acef552b)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM1, 5) |
| #define | [TIM1\_ETR\_PD4\_6](#a4ac6d50841b3beaf5b8ab824afd8d8a9)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM1, 6) |
| #define | [TIM1\_ETR\_PB4\_7](#a1e753c5cdf4dad1201b8a1e3a9130b71)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, TIM1, 7) |
| #define | [TIM1\_ETR\_PB4\_8](#a68f0acdd096d3848a340ad6fb3720234)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, TIM1, 8) |
| #define | [TIM1\_ETR\_PB4\_9](#a9ebc70c362069993fd1dab3cae650b6e)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, TIM1, 9) |
| #define | [TIM1\_CH1\_PD2\_0](#a0358320b2a97250777a32de61ac74e11)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, TIM1, 0) |
| #define | [TIM1\_CH1\_PD2\_1](#a8ea959a185d8282797e3ad253f7d70a0)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, TIM1, 1) |
| #define | [TIM1\_CH1\_PC6\_2](#aee2da94a1c434f98caf2b6a8717173fb)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 2) |
| #define | [TIM1\_CH1\_PC4\_3](#aa4f03f6f1206146731ed38b33fec5c99)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 3) |
| #define | [TIM1\_CH1\_PA3\_4](#adf27aba2c5d9b8d06eca64e58fb29ee8)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM1, 4) |
| #define | [TIM1\_CH1\_PA3\_5](#a290726fb42e4072388c7fca6965c8519)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM1, 5) |
| #define | [TIM1\_CH1\_PA3\_6](#af7d3e5f026e32be361f8e9e3258ab95c)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM1, 6) |
| #define | [TIM1\_CH1\_PC4\_7](#a94eb34ef91947e256a43df8a5f578162)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 7) |
| #define | [TIM1\_CH1\_PC4\_8](#ae5781ea1006d017f5207e259c7647653)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 8) |
| #define | [TIM1\_CH1\_PA0\_9](#a0e8bde418956cb9704f50246f7454773)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM1, 9) |
| #define | [TIM1\_CH2\_PA1\_0](#ab154f084c5ca48b3010e6e7744b03d3c)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, TIM1, 0) |
| #define | [TIM1\_CH2\_PA1\_1](#ab9707e688fd0e10707341dfba99806c7)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, TIM1, 1) |
| #define | [TIM1\_CH2\_PC7\_2](#a59253a312e1aa02c520b64563240bf8d)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 2) |
| #define | [TIM1\_CH2\_PC7\_3](#ac062779803078d0f4398dc9979ab09c6)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 3) |
| #define | [TIM1\_CH2\_PB0\_4](#a40288ef1c2693e428727b73c0955beb0)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, TIM1, 4) |
| #define | [TIM1\_CH2\_PB0\_5](#ac4785ebb2b6bb90090bdd1c79d2da0f3)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, TIM1, 5) |
| #define | [TIM1\_CH2\_PB0\_6](#a1f428966756273de6718403679b74332)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, TIM1, 6) |
| #define | [TIM1\_CH2\_PC5\_7](#a98a253a2d5a2b5d131eb234162ac840f)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 7) |
| #define | [TIM1\_CH2\_PC5\_8](#affeb6faff8ee97b7747f0b209fd015ac)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 8) |
| #define | [TIM1\_CH2\_PA1\_9](#ad8637e4b990a4144dd075e0db826ea03)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, TIM1, 9) |
| #define | [TIM1\_CH3\_PC3\_0](#a8c34342b714e0bb8fc5dbffbbba87a98)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 0) |
| #define | [TIM1\_CH3\_PC3\_1](#ab2a9390300a6a8d835a7bb5d860e3e31)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 1) |
| #define | [TIM1\_CH3\_PC0\_2](#ae13f1692e05743d7270d15be74ceef6b)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM1, 2) |
| #define | [TIM1\_CH3\_PC5\_3](#ac0ef4ba763211a0f47cdbc4f1ec3891f)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 3) |
| #define | [TIM1\_CH3\_PB1\_4](#ae7dcb6643d0745ccfcd9a23f2b5ca9dd)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, TIM1, 4) |
| #define | [TIM1\_CH3\_PC3\_5](#a55dad5236421b9db9cfec232d194b39f)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 5) |
| #define | [TIM1\_CH3\_PB1\_6](#a48b4e7d8a26d1c640e7daa76f72723c7)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, TIM1, 6) |
| #define | [TIM1\_CH3\_PC6\_7](#a79e4869cf7f60c3e188e5f417193465c)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 7) |
| #define | [TIM1\_CH3\_PC6\_8](#adb77560754e43007d8b2606c0fb21aff)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 8) |
| #define | [TIM1\_CH3\_PA2\_9](#a66384e30f77c4ac2b0a5ee8fa41c4783)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 9) |
| #define | [TIM1\_CH4\_PC4\_0](#a6da952b7542e4fa5027cdf978e9251cb)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 0) |
| #define | [TIM1\_CH4\_PC4\_1](#a80c880c845d8c5c203a25f988768e93a)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 1) |
| #define | [TIM1\_CH4\_PD3\_2](#a499c31d306fe8e8b8f594690c7b85284)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, TIM1, 2) |
| #define | [TIM1\_CH4\_PD4\_3](#a9ee2b1bcdf2de7573f121736348d7774)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM1, 3) |
| #define | [TIM1\_CH4\_PD1\_4](#a573a0502889ee3abfa6d1d57da64fb2e)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, TIM1, 4) |
| #define | [TIM1\_CH4\_PD1\_5](#a1ddb484a7d46b253217362b525aef2b8)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, TIM1, 5) |
| #define | [TIM1\_CH4\_PB2\_6](#aad0f00059539fc47934e8649ea7768e2)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 2, TIM1, 6) |
| #define | [TIM1\_CH4\_PC7\_7](#affc60f50225b56abaa48e4b143d3fd7e)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 7) |
| #define | [TIM1\_CH4\_PC7\_8](#adbf133f0751d534b4a5c13863a38e721)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 8) |
| #define | [TIM1\_CH4\_PA3\_9](#a373943b6d935db7069c383651f5f9b1f)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM1, 9) |
| #define | [TIM1\_BKIN\_PC2\_0](#a0dd235ad3e6100a470c4d94140a24492)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 0) |
| #define | [TIM1\_BKIN\_PC2\_1](#a2662ae8a0f03cc66f1b99028379188a1)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 1) |
| #define | [TIM1\_BKIN\_PC1\_2](#ada827056b2498ea5843abb89e5ec0b49)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 2) |
| #define | [TIM1\_BKIN\_PC1\_3](#ac62dec76593bb03d91e786fb1c4ce044)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 3) |
| #define | [TIM1\_BKIN\_PB3\_4](#a12846390d681f4eda9f58483b86ede0d)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, TIM1, 4) |
| #define | [TIM1\_BKIN\_PB3\_5](#ae8a1630a2fd318f10069b52392e2d940)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, TIM1, 5) |
| #define | [TIM1\_BKIN\_PA7\_6](#a85faad2e83325648a340cfde87dba29f)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 7, TIM1, 6) |
| #define | [TIM1\_BKIN\_PB2\_7](#a5f220ff6b2aed5b482aed10efd453505)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 2, TIM1, 7) |
| #define | [TIM1\_BKIN\_PB2\_8](#a77bdb78dfe79ad4ebbc188025f1c61e1)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 2, TIM1, 8) |
| #define | [TIM1\_BKIN\_PB2\_9](#ad0e33c032d1f123c239e9628f09eff2c)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 2, TIM1, 9) |
| #define | [TIM1\_CH1N\_PD0\_0](#ae46dd3d78d8130e198f788e1fef871f4)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, TIM1, 0) |
| #define | [TIM1\_CH1N\_PD0\_1](#a4c664e4f5412238e223225cdc4c07bd6)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, TIM1, 1) |
| #define | [TIM1\_CH1N\_PC3\_2](#a00487f2196f5ff5f0e6b74c2cd9bf7e5)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 2) |
| #define | [TIM1\_CH1N\_PC3\_3](#aeb3bff0dbfa45aed7b63fd2a2979f3ec)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 3) |
| #define | [TIM1\_CH1N\_PA0\_4](#a40255c693cb786e8a7dc466388bea77a)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM1, 4) |
| #define | [TIM1\_CH1N\_PA0\_5](#a9cb36b7c16682e7e921c40cb53cad74e)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM1, 5) |
| #define | [TIM1\_CH1N\_PA0\_6](#aeadeed54e30fbad9b711e724e07bb937)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM1, 6) |
| #define | [TIM1\_CH1N\_PC0\_7](#a62c71c4837307dc47cc9d23994e4cc70)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM1, 7) |
| #define | [TIM1\_CH1N\_PA3\_8](#a8724c9ff43aea0ba6bce3492f8bbb38a)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM1, 8) |
| #define | [TIM1\_CH1N\_PC0\_9](#a7408dd36bfe27994a3c8ec1917e15c2e)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM1, 9) |
| #define | [TIM1\_CH2N\_PA2\_0](#a092da60f0a9603ec8c1553008a78d8f3)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 0) |
| #define | [TIM1\_CH2N\_PA2\_1](#aa3671b55886c2b8c950dc9993fb8c4da)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 1) |
| #define | [TIM1\_CH2N\_PC4\_2](#ae3e624aea83d00aef0d03c411714a854)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 2) |
| #define | [TIM1\_CH2N\_PD2\_3](#aa193ff08432db07685ca309f0e8b9e66)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, TIM1, 3) |
| #define | [TIM1\_CH2N\_PA2\_4](#ab1f836eb485a06d4a3711e364b22b85c)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 4) |
| #define | [TIM1\_CH2N\_PA2\_5](#afa02981c691207cde6b6d4748c46a7ae)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 5) |
| #define | [TIM1\_CH2N\_PA2\_6](#a7928f8a95130e9d2e07ccd903d0fccf5)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 6) |
| #define | [TIM1\_CH2N\_PC1\_7](#a0d6c8f82a35dead8d2725563eb57f2ac)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 7) |
| #define | [TIM1\_CH2N\_PB0\_8](#a681a380530c47dfb19a9db6f6511b67c)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, TIM1, 8) |
| #define | [TIM1\_CH2N\_PC1\_9](#aa838e5e9e05227c9186135b34b029a36)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 9) |
| #define | [TIM1\_CH3N\_PD1\_0](#a26b5659eb69c2b6f1b79497901a6bf32)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, TIM1, 0) |
| #define | [TIM1\_CH3N\_PD1\_1](#ad1c9dee54a8043b519176d67c14d949d)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, TIM1, 1) |
| #define | [TIM1\_CH3N\_PD1\_2](#ad986d12a63211d622c2debcecd7984e0)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, TIM1, 2) |
| #define | [TIM1\_CH3N\_PC6\_3](#aceeee0e77912b38e24bda43ab6819516)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 3) |
| #define | [TIM1\_CH3N\_PD0\_4](#a8fd1e6357bd9f1ed60fb4c4f5dc04c7d)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, TIM1, 4) |
| #define | [TIM1\_CH3N\_PD0\_5](#a094aca207f630409ffdee3639112d85c)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, TIM1, 5) |
| #define | [TIM1\_CH3N\_PD0\_6](#a80b1d1c1b3fc189fc657458dd27e3b5b)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, TIM1, 6) |
| #define | [TIM1\_CH3N\_PC2\_7](#af1a467261e44da2b38e55a4530d8df91)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 7) |
| #define | [TIM1\_CH3N\_PB1\_8](#a1e92f4108836bb55273bee5b77044bc5)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, TIM1, 8) |
| #define | [TIM1\_CH3N\_PC2\_9](#aa925b18d6d35fe174983269b9fb267d1)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 9) |
| #define | [TIM2\_ETR\_PD4\_0](#a43c2c900f95d5f44905e65ddaa4cc0ef)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM2, 0) |
| #define | [TIM2\_ETR\_PC1\_1](#a1e82702b5fb67f4f7d57223c15cae6f8)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 1) |
| #define | [TIM2\_ETR\_PC5\_2](#a4781cf5654db89611a12ca9604560576)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM2, 2) |
| #define | [TIM2\_ETR\_PC1\_3](#afe0830763b0bd0a6784e10a6f4b3f89d)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 3) |
| #define | [TIM2\_ETR\_PC0\_4](#a3cccc168a38f54f1edeb37e6cd592d71)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 4) |
| #define | [TIM2\_ETR\_PA0\_5](#afd09d1c107687c21da9a5e2d75939838)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM2, 5) |
| #define | [TIM2\_ETR\_PB1\_6](#aa054a19799ab29a7b2129153572eed8f)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, TIM2, 6) |
| #define | [TIM2\_ETR\_PD3\_7](#a0d9e3aa56edf19e0bb2e7fbcddfbb9ce)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, TIM2, 7) |
| #define | [TIM2\_CH1\_PD4\_0](#a321ccc1d95043b1c49086c450ca0ea7e)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM2, 0) |
| #define | [TIM2\_CH1\_PC1\_1](#a0e4c3a71c9987421ab1b547e055654ed)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 1) |
| #define | [TIM2\_CH1\_PC5\_2](#aff489f00d8271543d8c04fe7940ea060)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM2, 2) |
| #define | [TIM2\_CH1\_PC1\_3](#aa9887268c3ecfe994f570285ced244d7)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 3) |
| #define | [TIM2\_CH1\_PC0\_4](#a25597451c91e38e58a1dff02a1c58879)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 4) |
| #define | [TIM2\_CH1\_PA0\_5](#a0ac0fbb7306bcae050ac7317bf0683f0)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM2, 5) |
| #define | [TIM2\_CH1\_PB1\_6](#aff43d541a8a7f905e16dafee7cdbaefc)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, TIM2, 6) |
| #define | [TIM2\_CH1\_PD3\_7](#a4f78b93ccd2715c056dedd9646e68a9c)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, TIM2, 7) |
| #define | [TIM2\_CH2\_PD3\_0](#a3d7058511a77c977c3ae54e9fb9ca4c2)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, TIM2, 0) |
| #define | [TIM2\_CH2\_PD3\_1](#a5461f77514cd20461a7d4376674e7cdc)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, TIM2, 1) |
| #define | [TIM2\_CH2\_PC2\_2](#af2055fe4a8524bc3518f62ba0b1acef1)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM2, 2) |
| #define | [TIM2\_CH2\_PB3\_2](#a51d2aa9fe41cd68678d3858c92f0c199)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, TIM2, 2) |
| #define | [TIM2\_CH2\_PC7\_3](#a4f93f520fe35543b5af8f4b000902937)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM2, 3) |
| #define | [TIM2\_CH2\_PC1\_4](#ad79947e399c161a589f8686c9dbf5224)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 4) |
| #define | [TIM2\_CH2\_PA1\_5](#ad5d1ffaa52531ec0b9ffddc4f396f59c)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, TIM2, 5) |
| #define | [TIM2\_CH2\_PA1\_6](#a13f1487fa7b4636297d56e69f5149cae)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, TIM2, 6) |
| #define | [TIM2\_CH2\_PD4\_7](#a39e4871d13613c2a14155db3728bd0d9)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM2, 7) |
| #define | [TIM2\_CH3\_PC0\_0](#aa81c6b179d7f6a05448f9e48af7fd7db)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 0) |
| #define | [TIM2\_CH3\_PC0\_1](#a2b00dafcb21394a8ff8b29080053b28a)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 1) |
| #define | [TIM2\_CH3\_PD2\_2](#ad96e8521f75aacbae9d8d8519faf7f06)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, TIM2, 2) |
| #define | [TIM2\_CH3\_PD6\_3](#a75e6de87ea2b60d8652b87150344f170)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 6, TIM2, 3) |
| #define | [TIM2\_CH3\_PC3\_4](#a6b9c3e0d4ee5c2392b452de94452f975)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM2, 4) |
| #define | [TIM2\_CH3\_PA2\_5](#ae02653c1dd0ba1feaf1606788229b58d)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM2, 5) |
| #define | [TIM2\_CH3\_PA2\_6](#a0189beb481481407d34ee2072b8489df)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM2, 6) |
| #define | [TIM2\_CH3\_PA2\_7](#ae8c433976c689b694b94077e4ea512ab)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM2, 7) |
| #define | [TIM2\_CH4\_PD7\_0](#acde18507b0874abe39c646ec52fe1444)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 7, TIM2, 0) |
| #define | [TIM2\_CH4\_PD7\_1](#ab61cd11e67968a0f32bda93349ed93a7)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 7, TIM2, 1) |
| #define | [TIM2\_CH4\_PC1\_2](#a41632f89d316ce79bd44e76e0b4c6b5b)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 2) |
| #define | [TIM2\_CH4\_PD5\_3](#aabc5e55cfb4e46ef7108b3794e7559ff)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 5, TIM2, 3) |
| #define | [TIM2\_CH4\_PB6\_4](#a8a94778319d035a2e29e9ef14416f806)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 6, TIM2, 4) |
| #define | [TIM2\_CH4\_PA3\_5](#a101951f237744ecb0e273e8815275b7f)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM2, 5) |
| #define | [TIM2\_CH4\_PA3\_6](#a32bcb4f01637b7c23b5f936e00b02229)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM2, 6) |
| #define | [TIM2\_CH4\_PA3\_7](#a46aa58720a97ecd2e5594cf416bdfc2d)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM2, 7) |
| #define | [USART1\_TX\_PD5\_0](#ab7c3bcaa4f01310261473cb734aeba23)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 5, USART1, 0) |
| #define | [USART1\_TX\_PD6\_1](#a65805902e3f58b907beb0d7f39380d87)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 6, USART1, 1) |
| #define | [USART1\_TX\_PD0\_2](#a2929a6724518bf36c15be8fc658bde05)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, USART1, 2) |
| #define | [USART1\_TX\_PC0\_3](#ada26f8c1b5c0e9d74bc82ac68b836382)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, USART1, 3) |
| #define | [USART1\_TX\_PD1\_4](#a46939eb59b23c13c4963035abfe5e0fc)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, USART1, 4) |
| #define | [USART1\_TX\_PB3\_5](#a874ce1580f9150018621cd69fc593278)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, USART1, 5) |
| #define | [USART1\_TX\_PC5\_6](#a273118d50602170728e67f4bbfe166f9)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, USART1, 6) |
| #define | [USART1\_TX\_PB5\_7](#a88180919d778bce4a76a50ebbdec9a01)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 5, USART1, 7) |
| #define | [USART1\_TX\_PA0\_8](#ad4bbf2f73d5cf308809e72a59f279d4f)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, USART1, 8) |
| #define | [USART1\_TX\_PA0\_9](#a9e1cb2fc5b61479fca18f844c7b2a25b)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, USART1, 9) |
| #define | [USART1\_RX\_PD6\_0](#a0f6ad0455dc48303bde7bc475f7215de)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 6, USART1, 0) |
| #define | [USART1\_RX\_PD5\_1](#aca9c065151c7d1439d03a218bad28953)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 5, USART1, 1) |
| #define | [USART1\_RX\_PD1\_2](#ad17459ba5c85756bb6b35215908e552b)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, USART1, 2) |
| #define | [USART1\_RX\_PC1\_3](#a61ec872334034b3d83feacf87a71ee51)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, USART1, 3) |
| #define | [USART1\_RX\_PB3\_4](#adecf7a857f74ccd2bc11c58ae935564b)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, USART1, 4) |
| #define | [USART1\_RX\_PD1\_5](#aac2be2e46c973ba5efe27f0fff98cabb)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, USART1, 5) |
| #define | [USART1\_RX\_PC6\_6](#a535de4a0f3d5c2844b8a6787820fc6ef)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, USART1, 6) |
| #define | [USART1\_RX\_PB6\_7](#a842305cdfe152b432b2b0935d4066aa1)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 6, USART1, 7) |
| #define | [USART1\_RX\_PA1\_8](#aafac07305b388d70b6d7f54bd980910c)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, USART1, 8) |
| #define | [USART1\_RX\_PC4\_9](#addb61f3eb63ef8a3a403a8587502aaf4)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, USART1, 9) |
| #define | [USART1\_CTS\_PD3\_0](#a5b33948c25cf17dc8d9cad67866087d1)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, USART1, 0) |
| #define | [USART1\_CTS\_PC6\_1](#a3f897a8115f49f630ee03a6a704fbc71)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, USART1, 1) |
| #define | [USART1\_CTS\_PC3\_2](#a2d8bc44640f7e08bfdfbf5a3d22cc255)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, USART1, 2) |
| #define | [USART1\_CTS\_PC6\_3](#a337b56d0fed1c6d90d391005f0247711)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, USART1, 3) |
| #define | [USART1\_CTS\_PD7\_4](#a7b1678aa77d79161e3228ba5a831093f)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 7, USART1, 4) |
| #define | [USART1\_CTS\_PD7\_5](#a084634f691aaebd09dfcd7a3a1e6d88e)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 7, USART1, 5) |
| #define | [USART1\_CTS\_PC7\_6](#abc5be4741bdf8924e7ab39ba72da98ef)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 6) |
| #define | [USART1\_CTS\_PC7\_7](#ac63ce23aa86ed5aeb1cfd8034e40537b)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 7) |
| #define | [USART1\_CTS\_PD2\_8](#a0d95aaa159b3972b09c3f0aa11ef0ab7)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, USART1, 8) |
| #define | [USART1\_CTS\_PD5\_9](#a7d2f21eac60c1106b8bf4e1b7db3a204)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 5, USART1, 9) |
| #define | [USART1\_RTS\_PC2\_0](#a2815ef4f646852914ddd2b8e8b7badef)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, USART1, 0) |
| #define | [USART1\_RTS\_PC7\_1](#aea3a162c52835b61fea5ffcb19793947)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 1) |
| #define | [USART1\_RTS\_PC2\_2](#a8a863333c39e43bcebaef2476f342f1f)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, USART1, 2) |
| #define | [USART1\_RTS\_PC7\_3](#ae8804a9a24491c2f723261061f783375)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 3) |
| #define | [USART1\_RTS\_PA5\_4](#afcd1f752d8e97796f0985417851710bd)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 5, USART1, 4) |
| #define | [USART1\_RTS\_PA5\_5](#a7aabe7289738f464b844869f11d2ad77)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 5, USART1, 5) |
| #define | [USART1\_RTS\_PB4\_6](#a9fd3866c5f193a5adc0b39c839c7bb66)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, USART1, 6) |
| #define | [USART1\_RTS\_PB4\_7](#a0d05f6fd7d5b563889e66918cd5f20d5)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, USART1, 7) |
| #define | [USART1\_RTS\_PD3\_8](#a7bd4d249b211ba28ad2d06f7b67ab631)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, USART1, 8) |
| #define | [USART1\_RTS\_PD4\_9](#a9c03c1d8a7a68304271ed06439a10378)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, USART1, 9) |
| #define | [USART2\_TX\_PA7\_0](#a0152727406750ce80df2377242967147)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 7, USART2, 0) |
| #define | [USART2\_TX\_PA4\_1](#af11623f802cf65e3626b38050a8404fe)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 4, USART2, 1) |
| #define | [USART2\_TX\_PA2\_2](#a9a4cf7fffcb285c0ad955f66f8fbd2c0)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, USART2, 2) |
| #define | [USART2\_TX\_PD2\_3](#a9b0571dfb1330177950f6531feb90a50)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, USART2, 3) |
| #define | [USART2\_TX\_PB0\_4](#acef47a522b84c0971442a3498fd2cf3e)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, USART2, 4) |
| #define | [USART2\_TX\_PC4\_5](#a49dc559bd4fe32265256417609b84fd7)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, USART2, 5) |
| #define | [USART2\_TX\_PA6\_6](#a24153b4ce2024673ad86cd9c490f0889)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 6, USART2, 6) |
| #define | [USART2\_RX\_PB3\_0](#ac0c914e26ad7390875e5080dee790103)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, USART2, 0) |
| #define | [USART2\_RX\_PA5\_1](#aff4e0a27fc6b6dd4ffd83931e520172b)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 5, USART2, 1) |
| #define | [USART2\_RX\_PA3\_2](#a8be97f0b92fc2e84e6167f753583b3bd)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, USART2, 2) |
| #define | [USART2\_RX\_PD3\_3](#ab7dce0cc7991ebd63d81421422f317a3)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, USART2, 3) |
| #define | [USART2\_RX\_PB1\_4](#aaee97f5922b1307da5c4c390056b70b3)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, USART2, 4) |
| #define | [USART2\_RX\_PD1\_5](#a8b8d33c7c70681cbf95eaed62e9aab41)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, USART2, 5) |
| #define | [USART2\_RX\_PA5\_6](#a858fad6e9a5e6cbad0abba8836717438)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 5, USART2, 6) |
| #define | [USART2\_CTS\_PA4\_0](#ab0fed132ce4b4e328ad5abec7623fb34)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 4, USART2, 0) |
| #define | [USART2\_CTS\_PA7\_1](#adce3d83fc3e34f6e0bd8910e079ac8e1)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 7, USART2, 1) |
| #define | [USART2\_CTS\_PA0\_2](#ac0a15096977f216e21f51d72f57eec14)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, USART2, 2) |
| #define | [USART2\_CTS\_PA0\_3](#a2a1d5ae373cabd13b5353dacf9d8ccb1)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, USART2, 3) |
| #define | [USART2\_CTS\_PB6\_4](#a9c29cf0c467d5806bbd31bf492e446b8)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 6, USART2, 4) |
| #define | [USART2\_CTS\_PA4\_5](#aef802806cabe330d83fb51b60b3a11c3)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 4, USART2, 5) |
| #define | [USART2\_CTS\_PA7\_6](#a0783ddd911225e749bc93997d9c95b03)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 7, USART2, 6) |
| #define | [USART2\_RTS\_PA5\_0](#ac899df236d1a1698b96882eaba4c1164)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 5, USART2, 0) |
| #define | [USART2\_RTS\_PB3\_1](#a53cf31b3362a596622e3cbe3d768e80a)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, USART2, 1) |
| #define | [USART2\_RTS\_PA1\_2](#a5c3789ef5097d4f3d85f701e7263ab8f)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, USART2, 2) |
| #define | [USART2\_RTS\_PA1\_3](#aaa1dc5b02f8af2f3ccddf8001ff38bd7)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, USART2, 3) |
| #define | [USART2\_RTS\_PA1\_4](#ae700c6a7177c687a5fc1094a590b6843)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, USART2, 4) |
| #define | [USART2\_RTS\_PA1\_5](#af854dc720498465e10d20d7c1b695aa8)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, USART2, 5) |
| #define | [USART2\_RTS\_PB3\_6](#a75465838304ad680659ba79288d3b44a)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, USART2, 6) |
| #define | [SPI1\_NSS\_PC1\_0](#a58c3e7301808054c6f9dd6fcc6ca7f62)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, SPI1, 0) |
| #define | [SPI1\_NSS\_PC0\_1](#a1332cb377a889a8f4847dae6ba3bc8c2)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, SPI1, 1) |
| #define | [SPI1\_NSS\_PC4\_2](#acae8b2ea0b5029ae8f25e47930b9de6d)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, SPI1, 2) |
| #define | [SPI1\_NSS\_PB0\_3](#a90a6e4c99bf81434bf2ffb9d57e679c5)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, SPI1, 3) |
| #define | [SPI1\_NSS\_PD3\_4](#a6f5975e7451211c7eb23f120cb8e24ee)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, SPI1, 4) |
| #define | [SPI1\_NSS\_PC1\_5](#a7d463e72606e299d5750a12b3973bb17)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, SPI1, 5) |
| #define | [SPI1\_NSS\_PC4\_6](#a530988f4281bb646ad5c9678cc0e1a69)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, SPI1, 6) |
| #define | [SPI1\_SCK\_PC5\_0](#a98dcc6496a51b59ab09423625e3b85ec)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, SPI1, 0) |
| #define | [SPI1\_SCK\_PC5\_1](#ab64b8359184eeb5453bd4fa9b3f69dcc)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, SPI1, 1) |
| #define | [SPI1\_SCK\_PD2\_2](#a8f22682b558492fee17f65ad06000322)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, SPI1, 2) |
| #define | [SPI1\_SCK\_PB1\_3](#a34bf7d21a313be01cb4c5eb0d1793801)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, SPI1, 3) |
| #define | [SPI1\_SCK\_PD4\_4](#abe4fea5976b8be70ad967413ecb06b2b)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, SPI1, 4) |
| #define | [SPI1\_SCK\_PA1\_5](#ac63d045b41eab1c94f43e81082023a88)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, SPI1, 5) |
| #define | [SPI1\_SCK\_PB5\_6](#a58acd5094a9b6887aecf1fb7c94b6624)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 5, SPI1, 6) |
| #define | [SPI1\_MISO\_PC7\_0](#a134d2e821fef85267e11d36daa50c621)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, SPI1, 0) |
| #define | [SPI1\_MISO\_PC7\_1](#a921212305fac7d0cdeb3903ff2a724a2)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, SPI1, 1) |
| #define | [SPI1\_MISO\_PB3\_2](#a67692d019467885f07a29a4a5be7e7fe)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, SPI1, 2) |
| #define | [SPI1\_MISO\_PB2\_3](#aaa2fa84ed3ae63026f6a4aa86e2821f6)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 2, SPI1, 3) |
| #define | [SPI1\_MISO\_PD5\_4](#a69007bf94e971e8862141be09c5cac8a)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 5, SPI1, 4) |
| #define | [SPI1\_MISO\_PB5\_5](#ae3579a049f91fe61f54d8b284c304bc1)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 5, SPI1, 5) |
| #define | [SPI1\_MISO\_PC7\_6](#a8720731a1831220108703cd4a1cf1ebd)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, SPI1, 6) |
| #define | [SPI1\_MOSI\_PC6\_0](#a76fe4ef21032a97eec11fe128e833986)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, SPI1, 0) |
| #define | [SPI1\_MOSI\_PC6\_1](#a20d9d1bf8c95947a905c8e2ccc86b124)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, SPI1, 1) |
| #define | [SPI1\_MOSI\_PD3\_2](#a348ff7755cc0c68776b90a318649766a)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, SPI1, 2) |
| #define | [SPI1\_MOSI\_PC0\_3](#a2995d7e2809ba68f000ee6c210161d3d)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, SPI1, 3) |
| #define | [SPI1\_MOSI\_PD6\_4](#a192b1ac9faee8695e064b9d0b0edf645)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 6, SPI1, 4) |
| #define | [SPI1\_MOSI\_PA2\_5](#a166a79543544e6427f3309dcb74b70ac)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, SPI1, 5) |
| #define | [SPI1\_MOSI\_PB4\_6](#a77a0e9f3f26b818c9078f3e60d00aaaf)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, SPI1, 6) |
| #define | [I2C1\_SCL\_PC2\_0](#a67a11ecb19690536672833e7d53c491a)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, I2C1, 0) |
| #define | [I2C1\_SCL\_PD1\_1](#acdd92bea3d3473ee4ea99aa63344b2ad)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, I2C1, 1) |
| #define | [I2C1\_SCL\_PC5\_2](#a603f2282e70d445edd7c1d9e45fe0750)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, I2C1, 2) |
| #define | [I2C1\_SCL\_PB5\_3](#a0d1a5b36cb29b488f710bba92c949d68)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 5, I2C1, 3) |
| #define | [I2C1\_SCL\_PB3\_4](#a31e2a1d7e95fd0dea39f4453c5bd3014)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, I2C1, 4) |
| #define | [I2C1\_SDA\_PC1\_0](#a7cbade793a166dacc06ec69353913e49)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, I2C1, 0) |
| #define | [I2C1\_SDA\_PD0\_1](#a097905ef14012784d810f485210bdad9)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, I2C1, 1) |
| #define | [I2C1\_SDA\_PC6\_2](#a90e0117d875929fb2baa388ed06f085d)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, I2C1, 2) |
| #define | [I2C1\_SDA\_PC4\_2](#a006fc38bf6e42f9ce6627b5ad5dc6f39)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, I2C1, 2) |
| #define | [I2C1\_SDA\_PB6\_3](#a096df412c6768c054fe137da7f8c8607)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 6, I2C1, 3) |
| #define | [I2C1\_SDA\_PD1\_4](#a0577e12fc011b890a4ff6cc7e8588946)   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, I2C1, 4) |

## Macro Definition Documentation

## [◆ ](#ab30a0f46632e9eb8529306664c618eae)CH32V00X\_PINCTRL\_BASE\_MASK

| #define CH32V00X\_PINCTRL\_BASE\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(9, 5) |
| --- |

## [◆ ](#a32c6a5a4f753487e92c5b0add73c0a97)CH32V00X\_PINCTRL\_BASE\_SHIFT

| #define CH32V00X\_PINCTRL\_BASE\_SHIFT   5 |
| --- |

## [◆ ](#a252c604982e448ab4e2f7333a431bdb6)CH32V00X\_PINCTRL\_PIN\_MASK

| #define CH32V00X\_PINCTRL\_PIN\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 2) |
| --- |

## [◆ ](#a16dd7dab2521cfbfec5860a6bea3820e)CH32V00X\_PINCTRL\_PIN\_SHIFT

| #define CH32V00X\_PINCTRL\_PIN\_SHIFT   2 |
| --- |

## [◆ ](#a7d221d51318c7235b823651802a25192)CH32V00X\_PINCTRL\_PORT\_MASK

| #define CH32V00X\_PINCTRL\_PORT\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| --- |

## [◆ ](#abc6ff06e0fcacdbfa4a05066e87904a7)CH32V00X\_PINCTRL\_PORT\_SHIFT

| #define CH32V00X\_PINCTRL\_PORT\_SHIFT   0 |
| --- |

## [◆ ](#ac1154192c3a9120cbb1dfbf28400e664)CH32V00X\_PINCTRL\_RM\_MASK

| #define CH32V00X\_PINCTRL\_RM\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(12, 10) |
| --- |

## [◆ ](#a94441bfaa665e8f31bcead94137e5c05)CH32V00X\_PINCTRL\_RM\_SHIFT

| #define CH32V00X\_PINCTRL\_RM\_SHIFT   10 |
| --- |

## [◆ ](#a10d20ad95129b7e6ddcf331582d13897)CH32V00X\_PINMUX\_ADC\_DTR\_GINJ\_RM

| #define CH32V00X\_PINMUX\_ADC\_DTR\_GINJ\_RM   18 |
| --- |

## [◆ ](#a9a2214e447c9d821340803dbd5c9a1ef)CH32V00X\_PINMUX\_ADC\_DTR\_GREG\_RM

| #define CH32V00X\_PINMUX\_ADC\_DTR\_GREG\_RM   19 |
| --- |

## [◆ ](#a1c30350d4532ec3cfb69a2febfa9dc09)CH32V00X\_PINMUX\_DEFINE

| #define CH32V00X\_PINMUX\_DEFINE | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *rm*, |
|  |  |  | *remapping* ) |

**Value:**

((CH32V00X\_PINMUX\_PORT\_##port << [CH32V00X\_PINCTRL\_PORT\_SHIFT](#abc6ff06e0fcacdbfa4a05066e87904a7)) | \

(pin << [CH32V00X\_PINCTRL\_PIN\_SHIFT](#a16dd7dab2521cfbfec5860a6bea3820e)) | \

(CH32V00X\_PINMUX\_##rm##\_RM << [CH32V00X\_PINCTRL\_BASE\_SHIFT](#a32c6a5a4f753487e92c5b0add73c0a97)) | \

(remapping << [CH32V00X\_PINCTRL\_RM\_SHIFT](#a94441bfaa665e8f31bcead94137e5c05)))

[CH32V00X\_PINCTRL\_PIN\_SHIFT](#a16dd7dab2521cfbfec5860a6bea3820e)

#define CH32V00X\_PINCTRL\_PIN\_SHIFT

**Definition** ch32v00x-pinctrl.h:30

[CH32V00X\_PINCTRL\_BASE\_SHIFT](#a32c6a5a4f753487e92c5b0add73c0a97)

#define CH32V00X\_PINCTRL\_BASE\_SHIFT

**Definition** ch32v00x-pinctrl.h:33

[CH32V00X\_PINCTRL\_RM\_SHIFT](#a94441bfaa665e8f31bcead94137e5c05)

#define CH32V00X\_PINCTRL\_RM\_SHIFT

**Definition** ch32v00x-pinctrl.h:36

[CH32V00X\_PINCTRL\_PORT\_SHIFT](#abc6ff06e0fcacdbfa4a05066e87904a7)

#define CH32V00X\_PINCTRL\_PORT\_SHIFT

**Definition** ch32v00x-pinctrl.h:27

## [◆ ](#a38bd15803e839874fd1db5408f03f330)CH32V00X\_PINMUX\_I2C1\_RM

| #define CH32V00X\_PINMUX\_I2C1\_RM   3 |
| --- |

## [◆ ](#ae4299414eb81619866db635b1f3632a2)CH32V00X\_PINMUX\_PA1PA2\_RM

| #define CH32V00X\_PINMUX\_PA1PA2\_RM   17 |
| --- |

## [◆ ](#a342a836de3a2ffdda83f5c3d57966abf)CH32V00X\_PINMUX\_PORT\_PA

| #define CH32V00X\_PINMUX\_PORT\_PA   0 |
| --- |

## [◆ ](#ae9f35f667ca89936c8ad246287bf9f43)CH32V00X\_PINMUX\_PORT\_PB

| #define CH32V00X\_PINMUX\_PORT\_PB   1 |
| --- |

## [◆ ](#a1e2d2bd6331286774357771211bebdff)CH32V00X\_PINMUX\_PORT\_PC

| #define CH32V00X\_PINMUX\_PORT\_PC   2 |
| --- |

## [◆ ](#a97f123c1518d8c9c66e97166fc8a5ab6)CH32V00X\_PINMUX\_PORT\_PD

| #define CH32V00X\_PINMUX\_PORT\_PD   3 |
| --- |

## [◆ ](#a3c398e69bd9aba0d8ef646f31e4d98d3)CH32V00X\_PINMUX\_SPI1\_RM

| #define CH32V00X\_PINMUX\_SPI1\_RM   0 |
| --- |

## [◆ ](#aecf76dc2f53a7ae6c5226fd51185dfa8)CH32V00X\_PINMUX\_TIM1\_RM

| #define CH32V00X\_PINMUX\_TIM1\_RM   10 |
| --- |

## [◆ ](#aacb406305b44a788dc831829f719fed0)CH32V00X\_PINMUX\_TIM2\_RM

| #define CH32V00X\_PINMUX\_TIM2\_RM   14 |
| --- |

## [◆ ](#a46a8b78e5eed35dab015c9c09fac238f)CH32V00X\_PINMUX\_USART1\_RM

| #define CH32V00X\_PINMUX\_USART1\_RM   6 |
| --- |

## [◆ ](#a5b7e2562a6a6c664e9e0ca1b6de5d4df)CH32V00X\_PINMUX\_USART2\_RM

| #define CH32V00X\_PINMUX\_USART2\_RM   20 |
| --- |

## [◆ ](#a31e2a1d7e95fd0dea39f4453c5bd3014)I2C1\_SCL\_PB3\_4

| #define I2C1\_SCL\_PB3\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, I2C1, 4) |
| --- |

## [◆ ](#a0d1a5b36cb29b488f710bba92c949d68)I2C1\_SCL\_PB5\_3

| #define I2C1\_SCL\_PB5\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 5, I2C1, 3) |
| --- |

## [◆ ](#a67a11ecb19690536672833e7d53c491a)I2C1\_SCL\_PC2\_0

| #define I2C1\_SCL\_PC2\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, I2C1, 0) |
| --- |

## [◆ ](#a603f2282e70d445edd7c1d9e45fe0750)I2C1\_SCL\_PC5\_2

| #define I2C1\_SCL\_PC5\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, I2C1, 2) |
| --- |

## [◆ ](#acdd92bea3d3473ee4ea99aa63344b2ad)I2C1\_SCL\_PD1\_1

| #define I2C1\_SCL\_PD1\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, I2C1, 1) |
| --- |

## [◆ ](#a096df412c6768c054fe137da7f8c8607)I2C1\_SDA\_PB6\_3

| #define I2C1\_SDA\_PB6\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 6, I2C1, 3) |
| --- |

## [◆ ](#a7cbade793a166dacc06ec69353913e49)I2C1\_SDA\_PC1\_0

| #define I2C1\_SDA\_PC1\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, I2C1, 0) |
| --- |

## [◆ ](#a006fc38bf6e42f9ce6627b5ad5dc6f39)I2C1\_SDA\_PC4\_2

| #define I2C1\_SDA\_PC4\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, I2C1, 2) |
| --- |

## [◆ ](#a90e0117d875929fb2baa388ed06f085d)I2C1\_SDA\_PC6\_2

| #define I2C1\_SDA\_PC6\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, I2C1, 2) |
| --- |

## [◆ ](#a097905ef14012784d810f485210bdad9)I2C1\_SDA\_PD0\_1

| #define I2C1\_SDA\_PD0\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, I2C1, 1) |
| --- |

## [◆ ](#a0577e12fc011b890a4ff6cc7e8588946)I2C1\_SDA\_PD1\_4

| #define I2C1\_SDA\_PD1\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, I2C1, 4) |
| --- |

## [◆ ](#aaa2fa84ed3ae63026f6a4aa86e2821f6)SPI1\_MISO\_PB2\_3

| #define SPI1\_MISO\_PB2\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 2, SPI1, 3) |
| --- |

## [◆ ](#a67692d019467885f07a29a4a5be7e7fe)SPI1\_MISO\_PB3\_2

| #define SPI1\_MISO\_PB3\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, SPI1, 2) |
| --- |

## [◆ ](#ae3579a049f91fe61f54d8b284c304bc1)SPI1\_MISO\_PB5\_5

| #define SPI1\_MISO\_PB5\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 5, SPI1, 5) |
| --- |

## [◆ ](#a134d2e821fef85267e11d36daa50c621)SPI1\_MISO\_PC7\_0

| #define SPI1\_MISO\_PC7\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, SPI1, 0) |
| --- |

## [◆ ](#a921212305fac7d0cdeb3903ff2a724a2)SPI1\_MISO\_PC7\_1

| #define SPI1\_MISO\_PC7\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, SPI1, 1) |
| --- |

## [◆ ](#a8720731a1831220108703cd4a1cf1ebd)SPI1\_MISO\_PC7\_6

| #define SPI1\_MISO\_PC7\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, SPI1, 6) |
| --- |

## [◆ ](#a69007bf94e971e8862141be09c5cac8a)SPI1\_MISO\_PD5\_4

| #define SPI1\_MISO\_PD5\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 5, SPI1, 4) |
| --- |

## [◆ ](#a166a79543544e6427f3309dcb74b70ac)SPI1\_MOSI\_PA2\_5

| #define SPI1\_MOSI\_PA2\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, SPI1, 5) |
| --- |

## [◆ ](#a77a0e9f3f26b818c9078f3e60d00aaaf)SPI1\_MOSI\_PB4\_6

| #define SPI1\_MOSI\_PB4\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, SPI1, 6) |
| --- |

## [◆ ](#a2995d7e2809ba68f000ee6c210161d3d)SPI1\_MOSI\_PC0\_3

| #define SPI1\_MOSI\_PC0\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, SPI1, 3) |
| --- |

## [◆ ](#a76fe4ef21032a97eec11fe128e833986)SPI1\_MOSI\_PC6\_0

| #define SPI1\_MOSI\_PC6\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, SPI1, 0) |
| --- |

## [◆ ](#a20d9d1bf8c95947a905c8e2ccc86b124)SPI1\_MOSI\_PC6\_1

| #define SPI1\_MOSI\_PC6\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, SPI1, 1) |
| --- |

## [◆ ](#a348ff7755cc0c68776b90a318649766a)SPI1\_MOSI\_PD3\_2

| #define SPI1\_MOSI\_PD3\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, SPI1, 2) |
| --- |

## [◆ ](#a192b1ac9faee8695e064b9d0b0edf645)SPI1\_MOSI\_PD6\_4

| #define SPI1\_MOSI\_PD6\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 6, SPI1, 4) |
| --- |

## [◆ ](#a90a6e4c99bf81434bf2ffb9d57e679c5)SPI1\_NSS\_PB0\_3

| #define SPI1\_NSS\_PB0\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, SPI1, 3) |
| --- |

## [◆ ](#a1332cb377a889a8f4847dae6ba3bc8c2)SPI1\_NSS\_PC0\_1

| #define SPI1\_NSS\_PC0\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, SPI1, 1) |
| --- |

## [◆ ](#a58c3e7301808054c6f9dd6fcc6ca7f62)SPI1\_NSS\_PC1\_0

| #define SPI1\_NSS\_PC1\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, SPI1, 0) |
| --- |

## [◆ ](#a7d463e72606e299d5750a12b3973bb17)SPI1\_NSS\_PC1\_5

| #define SPI1\_NSS\_PC1\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, SPI1, 5) |
| --- |

## [◆ ](#acae8b2ea0b5029ae8f25e47930b9de6d)SPI1\_NSS\_PC4\_2

| #define SPI1\_NSS\_PC4\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, SPI1, 2) |
| --- |

## [◆ ](#a530988f4281bb646ad5c9678cc0e1a69)SPI1\_NSS\_PC4\_6

| #define SPI1\_NSS\_PC4\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, SPI1, 6) |
| --- |

## [◆ ](#a6f5975e7451211c7eb23f120cb8e24ee)SPI1\_NSS\_PD3\_4

| #define SPI1\_NSS\_PD3\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, SPI1, 4) |
| --- |

## [◆ ](#ac63d045b41eab1c94f43e81082023a88)SPI1\_SCK\_PA1\_5

| #define SPI1\_SCK\_PA1\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, SPI1, 5) |
| --- |

## [◆ ](#a34bf7d21a313be01cb4c5eb0d1793801)SPI1\_SCK\_PB1\_3

| #define SPI1\_SCK\_PB1\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, SPI1, 3) |
| --- |

## [◆ ](#a58acd5094a9b6887aecf1fb7c94b6624)SPI1\_SCK\_PB5\_6

| #define SPI1\_SCK\_PB5\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 5, SPI1, 6) |
| --- |

## [◆ ](#a98dcc6496a51b59ab09423625e3b85ec)SPI1\_SCK\_PC5\_0

| #define SPI1\_SCK\_PC5\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, SPI1, 0) |
| --- |

## [◆ ](#ab64b8359184eeb5453bd4fa9b3f69dcc)SPI1\_SCK\_PC5\_1

| #define SPI1\_SCK\_PC5\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, SPI1, 1) |
| --- |

## [◆ ](#a8f22682b558492fee17f65ad06000322)SPI1\_SCK\_PD2\_2

| #define SPI1\_SCK\_PD2\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, SPI1, 2) |
| --- |

## [◆ ](#abe4fea5976b8be70ad967413ecb06b2b)SPI1\_SCK\_PD4\_4

| #define SPI1\_SCK\_PD4\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, SPI1, 4) |
| --- |

## [◆ ](#a85faad2e83325648a340cfde87dba29f)TIM1\_BKIN\_PA7\_6

| #define TIM1\_BKIN\_PA7\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 7, TIM1, 6) |
| --- |

## [◆ ](#a5f220ff6b2aed5b482aed10efd453505)TIM1\_BKIN\_PB2\_7

| #define TIM1\_BKIN\_PB2\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 2, TIM1, 7) |
| --- |

## [◆ ](#a77bdb78dfe79ad4ebbc188025f1c61e1)TIM1\_BKIN\_PB2\_8

| #define TIM1\_BKIN\_PB2\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 2, TIM1, 8) |
| --- |

## [◆ ](#ad0e33c032d1f123c239e9628f09eff2c)TIM1\_BKIN\_PB2\_9

| #define TIM1\_BKIN\_PB2\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 2, TIM1, 9) |
| --- |

## [◆ ](#a12846390d681f4eda9f58483b86ede0d)TIM1\_BKIN\_PB3\_4

| #define TIM1\_BKIN\_PB3\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, TIM1, 4) |
| --- |

## [◆ ](#ae8a1630a2fd318f10069b52392e2d940)TIM1\_BKIN\_PB3\_5

| #define TIM1\_BKIN\_PB3\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, TIM1, 5) |
| --- |

## [◆ ](#ada827056b2498ea5843abb89e5ec0b49)TIM1\_BKIN\_PC1\_2

| #define TIM1\_BKIN\_PC1\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 2) |
| --- |

## [◆ ](#ac62dec76593bb03d91e786fb1c4ce044)TIM1\_BKIN\_PC1\_3

| #define TIM1\_BKIN\_PC1\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 3) |
| --- |

## [◆ ](#a0dd235ad3e6100a470c4d94140a24492)TIM1\_BKIN\_PC2\_0

| #define TIM1\_BKIN\_PC2\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 0) |
| --- |

## [◆ ](#a2662ae8a0f03cc66f1b99028379188a1)TIM1\_BKIN\_PC2\_1

| #define TIM1\_BKIN\_PC2\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 1) |
| --- |

## [◆ ](#a0e8bde418956cb9704f50246f7454773)TIM1\_CH1\_PA0\_9

| #define TIM1\_CH1\_PA0\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM1, 9) |
| --- |

## [◆ ](#adf27aba2c5d9b8d06eca64e58fb29ee8)TIM1\_CH1\_PA3\_4

| #define TIM1\_CH1\_PA3\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM1, 4) |
| --- |

## [◆ ](#a290726fb42e4072388c7fca6965c8519)TIM1\_CH1\_PA3\_5

| #define TIM1\_CH1\_PA3\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM1, 5) |
| --- |

## [◆ ](#af7d3e5f026e32be361f8e9e3258ab95c)TIM1\_CH1\_PA3\_6

| #define TIM1\_CH1\_PA3\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM1, 6) |
| --- |

## [◆ ](#aa4f03f6f1206146731ed38b33fec5c99)TIM1\_CH1\_PC4\_3

| #define TIM1\_CH1\_PC4\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 3) |
| --- |

## [◆ ](#a94eb34ef91947e256a43df8a5f578162)TIM1\_CH1\_PC4\_7

| #define TIM1\_CH1\_PC4\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 7) |
| --- |

## [◆ ](#ae5781ea1006d017f5207e259c7647653)TIM1\_CH1\_PC4\_8

| #define TIM1\_CH1\_PC4\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 8) |
| --- |

## [◆ ](#aee2da94a1c434f98caf2b6a8717173fb)TIM1\_CH1\_PC6\_2

| #define TIM1\_CH1\_PC6\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 2) |
| --- |

## [◆ ](#a0358320b2a97250777a32de61ac74e11)TIM1\_CH1\_PD2\_0

| #define TIM1\_CH1\_PD2\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, TIM1, 0) |
| --- |

## [◆ ](#a8ea959a185d8282797e3ad253f7d70a0)TIM1\_CH1\_PD2\_1

| #define TIM1\_CH1\_PD2\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, TIM1, 1) |
| --- |

## [◆ ](#a40255c693cb786e8a7dc466388bea77a)TIM1\_CH1N\_PA0\_4

| #define TIM1\_CH1N\_PA0\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM1, 4) |
| --- |

## [◆ ](#a9cb36b7c16682e7e921c40cb53cad74e)TIM1\_CH1N\_PA0\_5

| #define TIM1\_CH1N\_PA0\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM1, 5) |
| --- |

## [◆ ](#aeadeed54e30fbad9b711e724e07bb937)TIM1\_CH1N\_PA0\_6

| #define TIM1\_CH1N\_PA0\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM1, 6) |
| --- |

## [◆ ](#a8724c9ff43aea0ba6bce3492f8bbb38a)TIM1\_CH1N\_PA3\_8

| #define TIM1\_CH1N\_PA3\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM1, 8) |
| --- |

## [◆ ](#a62c71c4837307dc47cc9d23994e4cc70)TIM1\_CH1N\_PC0\_7

| #define TIM1\_CH1N\_PC0\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM1, 7) |
| --- |

## [◆ ](#a7408dd36bfe27994a3c8ec1917e15c2e)TIM1\_CH1N\_PC0\_9

| #define TIM1\_CH1N\_PC0\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM1, 9) |
| --- |

## [◆ ](#a00487f2196f5ff5f0e6b74c2cd9bf7e5)TIM1\_CH1N\_PC3\_2

| #define TIM1\_CH1N\_PC3\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 2) |
| --- |

## [◆ ](#aeb3bff0dbfa45aed7b63fd2a2979f3ec)TIM1\_CH1N\_PC3\_3

| #define TIM1\_CH1N\_PC3\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 3) |
| --- |

## [◆ ](#ae46dd3d78d8130e198f788e1fef871f4)TIM1\_CH1N\_PD0\_0

| #define TIM1\_CH1N\_PD0\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, TIM1, 0) |
| --- |

## [◆ ](#a4c664e4f5412238e223225cdc4c07bd6)TIM1\_CH1N\_PD0\_1

| #define TIM1\_CH1N\_PD0\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, TIM1, 1) |
| --- |

## [◆ ](#ab154f084c5ca48b3010e6e7744b03d3c)TIM1\_CH2\_PA1\_0

| #define TIM1\_CH2\_PA1\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, TIM1, 0) |
| --- |

## [◆ ](#ab9707e688fd0e10707341dfba99806c7)TIM1\_CH2\_PA1\_1

| #define TIM1\_CH2\_PA1\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, TIM1, 1) |
| --- |

## [◆ ](#ad8637e4b990a4144dd075e0db826ea03)TIM1\_CH2\_PA1\_9

| #define TIM1\_CH2\_PA1\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, TIM1, 9) |
| --- |

## [◆ ](#a40288ef1c2693e428727b73c0955beb0)TIM1\_CH2\_PB0\_4

| #define TIM1\_CH2\_PB0\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, TIM1, 4) |
| --- |

## [◆ ](#ac4785ebb2b6bb90090bdd1c79d2da0f3)TIM1\_CH2\_PB0\_5

| #define TIM1\_CH2\_PB0\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, TIM1, 5) |
| --- |

## [◆ ](#a1f428966756273de6718403679b74332)TIM1\_CH2\_PB0\_6

| #define TIM1\_CH2\_PB0\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, TIM1, 6) |
| --- |

## [◆ ](#a98a253a2d5a2b5d131eb234162ac840f)TIM1\_CH2\_PC5\_7

| #define TIM1\_CH2\_PC5\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 7) |
| --- |

## [◆ ](#affeb6faff8ee97b7747f0b209fd015ac)TIM1\_CH2\_PC5\_8

| #define TIM1\_CH2\_PC5\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 8) |
| --- |

## [◆ ](#a59253a312e1aa02c520b64563240bf8d)TIM1\_CH2\_PC7\_2

| #define TIM1\_CH2\_PC7\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 2) |
| --- |

## [◆ ](#ac062779803078d0f4398dc9979ab09c6)TIM1\_CH2\_PC7\_3

| #define TIM1\_CH2\_PC7\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 3) |
| --- |

## [◆ ](#a092da60f0a9603ec8c1553008a78d8f3)TIM1\_CH2N\_PA2\_0

| #define TIM1\_CH2N\_PA2\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 0) |
| --- |

## [◆ ](#aa3671b55886c2b8c950dc9993fb8c4da)TIM1\_CH2N\_PA2\_1

| #define TIM1\_CH2N\_PA2\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 1) |
| --- |

## [◆ ](#ab1f836eb485a06d4a3711e364b22b85c)TIM1\_CH2N\_PA2\_4

| #define TIM1\_CH2N\_PA2\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 4) |
| --- |

## [◆ ](#afa02981c691207cde6b6d4748c46a7ae)TIM1\_CH2N\_PA2\_5

| #define TIM1\_CH2N\_PA2\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 5) |
| --- |

## [◆ ](#a7928f8a95130e9d2e07ccd903d0fccf5)TIM1\_CH2N\_PA2\_6

| #define TIM1\_CH2N\_PA2\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 6) |
| --- |

## [◆ ](#a681a380530c47dfb19a9db6f6511b67c)TIM1\_CH2N\_PB0\_8

| #define TIM1\_CH2N\_PB0\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, TIM1, 8) |
| --- |

## [◆ ](#a0d6c8f82a35dead8d2725563eb57f2ac)TIM1\_CH2N\_PC1\_7

| #define TIM1\_CH2N\_PC1\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 7) |
| --- |

## [◆ ](#aa838e5e9e05227c9186135b34b029a36)TIM1\_CH2N\_PC1\_9

| #define TIM1\_CH2N\_PC1\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 9) |
| --- |

## [◆ ](#ae3e624aea83d00aef0d03c411714a854)TIM1\_CH2N\_PC4\_2

| #define TIM1\_CH2N\_PC4\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 2) |
| --- |

## [◆ ](#aa193ff08432db07685ca309f0e8b9e66)TIM1\_CH2N\_PD2\_3

| #define TIM1\_CH2N\_PD2\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, TIM1, 3) |
| --- |

## [◆ ](#a66384e30f77c4ac2b0a5ee8fa41c4783)TIM1\_CH3\_PA2\_9

| #define TIM1\_CH3\_PA2\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM1, 9) |
| --- |

## [◆ ](#ae7dcb6643d0745ccfcd9a23f2b5ca9dd)TIM1\_CH3\_PB1\_4

| #define TIM1\_CH3\_PB1\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, TIM1, 4) |
| --- |

## [◆ ](#a48b4e7d8a26d1c640e7daa76f72723c7)TIM1\_CH3\_PB1\_6

| #define TIM1\_CH3\_PB1\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, TIM1, 6) |
| --- |

## [◆ ](#ae13f1692e05743d7270d15be74ceef6b)TIM1\_CH3\_PC0\_2

| #define TIM1\_CH3\_PC0\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM1, 2) |
| --- |

## [◆ ](#a8c34342b714e0bb8fc5dbffbbba87a98)TIM1\_CH3\_PC3\_0

| #define TIM1\_CH3\_PC3\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 0) |
| --- |

## [◆ ](#ab2a9390300a6a8d835a7bb5d860e3e31)TIM1\_CH3\_PC3\_1

| #define TIM1\_CH3\_PC3\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 1) |
| --- |

## [◆ ](#a55dad5236421b9db9cfec232d194b39f)TIM1\_CH3\_PC3\_5

| #define TIM1\_CH3\_PC3\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 5) |
| --- |

## [◆ ](#ac0ef4ba763211a0f47cdbc4f1ec3891f)TIM1\_CH3\_PC5\_3

| #define TIM1\_CH3\_PC5\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 3) |
| --- |

## [◆ ](#a79e4869cf7f60c3e188e5f417193465c)TIM1\_CH3\_PC6\_7

| #define TIM1\_CH3\_PC6\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 7) |
| --- |

## [◆ ](#adb77560754e43007d8b2606c0fb21aff)TIM1\_CH3\_PC6\_8

| #define TIM1\_CH3\_PC6\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 8) |
| --- |

## [◆ ](#a1e92f4108836bb55273bee5b77044bc5)TIM1\_CH3N\_PB1\_8

| #define TIM1\_CH3N\_PB1\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, TIM1, 8) |
| --- |

## [◆ ](#af1a467261e44da2b38e55a4530d8df91)TIM1\_CH3N\_PC2\_7

| #define TIM1\_CH3N\_PC2\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 7) |
| --- |

## [◆ ](#aa925b18d6d35fe174983269b9fb267d1)TIM1\_CH3N\_PC2\_9

| #define TIM1\_CH3N\_PC2\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 9) |
| --- |

## [◆ ](#aceeee0e77912b38e24bda43ab6819516)TIM1\_CH3N\_PC6\_3

| #define TIM1\_CH3N\_PC6\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 3) |
| --- |

## [◆ ](#a8fd1e6357bd9f1ed60fb4c4f5dc04c7d)TIM1\_CH3N\_PD0\_4

| #define TIM1\_CH3N\_PD0\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, TIM1, 4) |
| --- |

## [◆ ](#a094aca207f630409ffdee3639112d85c)TIM1\_CH3N\_PD0\_5

| #define TIM1\_CH3N\_PD0\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, TIM1, 5) |
| --- |

## [◆ ](#a80b1d1c1b3fc189fc657458dd27e3b5b)TIM1\_CH3N\_PD0\_6

| #define TIM1\_CH3N\_PD0\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, TIM1, 6) |
| --- |

## [◆ ](#a26b5659eb69c2b6f1b79497901a6bf32)TIM1\_CH3N\_PD1\_0

| #define TIM1\_CH3N\_PD1\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, TIM1, 0) |
| --- |

## [◆ ](#ad1c9dee54a8043b519176d67c14d949d)TIM1\_CH3N\_PD1\_1

| #define TIM1\_CH3N\_PD1\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, TIM1, 1) |
| --- |

## [◆ ](#ad986d12a63211d622c2debcecd7984e0)TIM1\_CH3N\_PD1\_2

| #define TIM1\_CH3N\_PD1\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, TIM1, 2) |
| --- |

## [◆ ](#a373943b6d935db7069c383651f5f9b1f)TIM1\_CH4\_PA3\_9

| #define TIM1\_CH4\_PA3\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM1, 9) |
| --- |

## [◆ ](#aad0f00059539fc47934e8649ea7768e2)TIM1\_CH4\_PB2\_6

| #define TIM1\_CH4\_PB2\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 2, TIM1, 6) |
| --- |

## [◆ ](#a6da952b7542e4fa5027cdf978e9251cb)TIM1\_CH4\_PC4\_0

| #define TIM1\_CH4\_PC4\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 0) |
| --- |

## [◆ ](#a80c880c845d8c5c203a25f988768e93a)TIM1\_CH4\_PC4\_1

| #define TIM1\_CH4\_PC4\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 1) |
| --- |

## [◆ ](#affc60f50225b56abaa48e4b143d3fd7e)TIM1\_CH4\_PC7\_7

| #define TIM1\_CH4\_PC7\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 7) |
| --- |

## [◆ ](#adbf133f0751d534b4a5c13863a38e721)TIM1\_CH4\_PC7\_8

| #define TIM1\_CH4\_PC7\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 8) |
| --- |

## [◆ ](#a573a0502889ee3abfa6d1d57da64fb2e)TIM1\_CH4\_PD1\_4

| #define TIM1\_CH4\_PD1\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, TIM1, 4) |
| --- |

## [◆ ](#a1ddb484a7d46b253217362b525aef2b8)TIM1\_CH4\_PD1\_5

| #define TIM1\_CH4\_PD1\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, TIM1, 5) |
| --- |

## [◆ ](#a499c31d306fe8e8b8f594690c7b85284)TIM1\_CH4\_PD3\_2

| #define TIM1\_CH4\_PD3\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, TIM1, 2) |
| --- |

## [◆ ](#a9ee2b1bcdf2de7573f121736348d7774)TIM1\_CH4\_PD4\_3

| #define TIM1\_CH4\_PD4\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM1, 3) |
| --- |

## [◆ ](#a1e753c5cdf4dad1201b8a1e3a9130b71)TIM1\_ETR\_PB4\_7

| #define TIM1\_ETR\_PB4\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, TIM1, 7) |
| --- |

## [◆ ](#a68f0acdd096d3848a340ad6fb3720234)TIM1\_ETR\_PB4\_8

| #define TIM1\_ETR\_PB4\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, TIM1, 8) |
| --- |

## [◆ ](#a9ebc70c362069993fd1dab3cae650b6e)TIM1\_ETR\_PB4\_9

| #define TIM1\_ETR\_PB4\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, TIM1, 9) |
| --- |

## [◆ ](#af03e0801b80f311ffa8ff53f71e895b6)TIM1\_ETR\_PC2\_3

| #define TIM1\_ETR\_PC2\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 3) |
| --- |

## [◆ ](#a8fca20f25cd86b6185a1c2674342bc48)TIM1\_ETR\_PC5\_0

| #define TIM1\_ETR\_PC5\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 0) |
| --- |

## [◆ ](#a44dd79259ce6ff88ee97a6f5e2ae93c8)TIM1\_ETR\_PC5\_2

| #define TIM1\_ETR\_PC5\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 2) |
| --- |

## [◆ ](#aaae81f3909b0a548b6971e4f5ad727eb)TIM1\_ETR\_PD4\_1

| #define TIM1\_ETR\_PD4\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM1, 1) |
| --- |

## [◆ ](#a880fc5b619497c9ad0d3f7cbfab85649)TIM1\_ETR\_PD4\_4

| #define TIM1\_ETR\_PD4\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM1, 4) |
| --- |

## [◆ ](#a5c196d9f8fe45f609fb45849acef552b)TIM1\_ETR\_PD4\_5

| #define TIM1\_ETR\_PD4\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM1, 5) |
| --- |

## [◆ ](#a4ac6d50841b3beaf5b8ab824afd8d8a9)TIM1\_ETR\_PD4\_6

| #define TIM1\_ETR\_PD4\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM1, 6) |
| --- |

## [◆ ](#a0ac0fbb7306bcae050ac7317bf0683f0)TIM2\_CH1\_PA0\_5

| #define TIM2\_CH1\_PA0\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM2, 5) |
| --- |

## [◆ ](#aff43d541a8a7f905e16dafee7cdbaefc)TIM2\_CH1\_PB1\_6

| #define TIM2\_CH1\_PB1\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, TIM2, 6) |
| --- |

## [◆ ](#a25597451c91e38e58a1dff02a1c58879)TIM2\_CH1\_PC0\_4

| #define TIM2\_CH1\_PC0\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 4) |
| --- |

## [◆ ](#a0e4c3a71c9987421ab1b547e055654ed)TIM2\_CH1\_PC1\_1

| #define TIM2\_CH1\_PC1\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 1) |
| --- |

## [◆ ](#aa9887268c3ecfe994f570285ced244d7)TIM2\_CH1\_PC1\_3

| #define TIM2\_CH1\_PC1\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 3) |
| --- |

## [◆ ](#aff489f00d8271543d8c04fe7940ea060)TIM2\_CH1\_PC5\_2

| #define TIM2\_CH1\_PC5\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM2, 2) |
| --- |

## [◆ ](#a4f78b93ccd2715c056dedd9646e68a9c)TIM2\_CH1\_PD3\_7

| #define TIM2\_CH1\_PD3\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, TIM2, 7) |
| --- |

## [◆ ](#a321ccc1d95043b1c49086c450ca0ea7e)TIM2\_CH1\_PD4\_0

| #define TIM2\_CH1\_PD4\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM2, 0) |
| --- |

## [◆ ](#ad5d1ffaa52531ec0b9ffddc4f396f59c)TIM2\_CH2\_PA1\_5

| #define TIM2\_CH2\_PA1\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, TIM2, 5) |
| --- |

## [◆ ](#a13f1487fa7b4636297d56e69f5149cae)TIM2\_CH2\_PA1\_6

| #define TIM2\_CH2\_PA1\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, TIM2, 6) |
| --- |

## [◆ ](#a51d2aa9fe41cd68678d3858c92f0c199)TIM2\_CH2\_PB3\_2

| #define TIM2\_CH2\_PB3\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, TIM2, 2) |
| --- |

## [◆ ](#ad79947e399c161a589f8686c9dbf5224)TIM2\_CH2\_PC1\_4

| #define TIM2\_CH2\_PC1\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 4) |
| --- |

## [◆ ](#af2055fe4a8524bc3518f62ba0b1acef1)TIM2\_CH2\_PC2\_2

| #define TIM2\_CH2\_PC2\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM2, 2) |
| --- |

## [◆ ](#a4f93f520fe35543b5af8f4b000902937)TIM2\_CH2\_PC7\_3

| #define TIM2\_CH2\_PC7\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM2, 3) |
| --- |

## [◆ ](#a3d7058511a77c977c3ae54e9fb9ca4c2)TIM2\_CH2\_PD3\_0

| #define TIM2\_CH2\_PD3\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, TIM2, 0) |
| --- |

## [◆ ](#a5461f77514cd20461a7d4376674e7cdc)TIM2\_CH2\_PD3\_1

| #define TIM2\_CH2\_PD3\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, TIM2, 1) |
| --- |

## [◆ ](#a39e4871d13613c2a14155db3728bd0d9)TIM2\_CH2\_PD4\_7

| #define TIM2\_CH2\_PD4\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM2, 7) |
| --- |

## [◆ ](#ae02653c1dd0ba1feaf1606788229b58d)TIM2\_CH3\_PA2\_5

| #define TIM2\_CH3\_PA2\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM2, 5) |
| --- |

## [◆ ](#a0189beb481481407d34ee2072b8489df)TIM2\_CH3\_PA2\_6

| #define TIM2\_CH3\_PA2\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM2, 6) |
| --- |

## [◆ ](#ae8c433976c689b694b94077e4ea512ab)TIM2\_CH3\_PA2\_7

| #define TIM2\_CH3\_PA2\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, TIM2, 7) |
| --- |

## [◆ ](#aa81c6b179d7f6a05448f9e48af7fd7db)TIM2\_CH3\_PC0\_0

| #define TIM2\_CH3\_PC0\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 0) |
| --- |

## [◆ ](#a2b00dafcb21394a8ff8b29080053b28a)TIM2\_CH3\_PC0\_1

| #define TIM2\_CH3\_PC0\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 1) |
| --- |

## [◆ ](#a6b9c3e0d4ee5c2392b452de94452f975)TIM2\_CH3\_PC3\_4

| #define TIM2\_CH3\_PC3\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM2, 4) |
| --- |

## [◆ ](#ad96e8521f75aacbae9d8d8519faf7f06)TIM2\_CH3\_PD2\_2

| #define TIM2\_CH3\_PD2\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, TIM2, 2) |
| --- |

## [◆ ](#a75e6de87ea2b60d8652b87150344f170)TIM2\_CH3\_PD6\_3

| #define TIM2\_CH3\_PD6\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 6, TIM2, 3) |
| --- |

## [◆ ](#a101951f237744ecb0e273e8815275b7f)TIM2\_CH4\_PA3\_5

| #define TIM2\_CH4\_PA3\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM2, 5) |
| --- |

## [◆ ](#a32bcb4f01637b7c23b5f936e00b02229)TIM2\_CH4\_PA3\_6

| #define TIM2\_CH4\_PA3\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM2, 6) |
| --- |

## [◆ ](#a46aa58720a97ecd2e5594cf416bdfc2d)TIM2\_CH4\_PA3\_7

| #define TIM2\_CH4\_PA3\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, TIM2, 7) |
| --- |

## [◆ ](#a8a94778319d035a2e29e9ef14416f806)TIM2\_CH4\_PB6\_4

| #define TIM2\_CH4\_PB6\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 6, TIM2, 4) |
| --- |

## [◆ ](#a41632f89d316ce79bd44e76e0b4c6b5b)TIM2\_CH4\_PC1\_2

| #define TIM2\_CH4\_PC1\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 2) |
| --- |

## [◆ ](#aabc5e55cfb4e46ef7108b3794e7559ff)TIM2\_CH4\_PD5\_3

| #define TIM2\_CH4\_PD5\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 5, TIM2, 3) |
| --- |

## [◆ ](#acde18507b0874abe39c646ec52fe1444)TIM2\_CH4\_PD7\_0

| #define TIM2\_CH4\_PD7\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 7, TIM2, 0) |
| --- |

## [◆ ](#ab61cd11e67968a0f32bda93349ed93a7)TIM2\_CH4\_PD7\_1

| #define TIM2\_CH4\_PD7\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 7, TIM2, 1) |
| --- |

## [◆ ](#afd09d1c107687c21da9a5e2d75939838)TIM2\_ETR\_PA0\_5

| #define TIM2\_ETR\_PA0\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, TIM2, 5) |
| --- |

## [◆ ](#aa054a19799ab29a7b2129153572eed8f)TIM2\_ETR\_PB1\_6

| #define TIM2\_ETR\_PB1\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, TIM2, 6) |
| --- |

## [◆ ](#a3cccc168a38f54f1edeb37e6cd592d71)TIM2\_ETR\_PC0\_4

| #define TIM2\_ETR\_PC0\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 4) |
| --- |

## [◆ ](#a1e82702b5fb67f4f7d57223c15cae6f8)TIM2\_ETR\_PC1\_1

| #define TIM2\_ETR\_PC1\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 1) |
| --- |

## [◆ ](#afe0830763b0bd0a6784e10a6f4b3f89d)TIM2\_ETR\_PC1\_3

| #define TIM2\_ETR\_PC1\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 3) |
| --- |

## [◆ ](#a4781cf5654db89611a12ca9604560576)TIM2\_ETR\_PC5\_2

| #define TIM2\_ETR\_PC5\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM2, 2) |
| --- |

## [◆ ](#a0d9e3aa56edf19e0bb2e7fbcddfbb9ce)TIM2\_ETR\_PD3\_7

| #define TIM2\_ETR\_PD3\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, TIM2, 7) |
| --- |

## [◆ ](#a43c2c900f95d5f44905e65ddaa4cc0ef)TIM2\_ETR\_PD4\_0

| #define TIM2\_ETR\_PD4\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, TIM2, 0) |
| --- |

## [◆ ](#a2d8bc44640f7e08bfdfbf5a3d22cc255)USART1\_CTS\_PC3\_2

| #define USART1\_CTS\_PC3\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, USART1, 2) |
| --- |

## [◆ ](#a3f897a8115f49f630ee03a6a704fbc71)USART1\_CTS\_PC6\_1

| #define USART1\_CTS\_PC6\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, USART1, 1) |
| --- |

## [◆ ](#a337b56d0fed1c6d90d391005f0247711)USART1\_CTS\_PC6\_3

| #define USART1\_CTS\_PC6\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, USART1, 3) |
| --- |

## [◆ ](#abc5be4741bdf8924e7ab39ba72da98ef)USART1\_CTS\_PC7\_6

| #define USART1\_CTS\_PC7\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 6) |
| --- |

## [◆ ](#ac63ce23aa86ed5aeb1cfd8034e40537b)USART1\_CTS\_PC7\_7

| #define USART1\_CTS\_PC7\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 7) |
| --- |

## [◆ ](#a0d95aaa159b3972b09c3f0aa11ef0ab7)USART1\_CTS\_PD2\_8

| #define USART1\_CTS\_PD2\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, USART1, 8) |
| --- |

## [◆ ](#a5b33948c25cf17dc8d9cad67866087d1)USART1\_CTS\_PD3\_0

| #define USART1\_CTS\_PD3\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, USART1, 0) |
| --- |

## [◆ ](#a7d2f21eac60c1106b8bf4e1b7db3a204)USART1\_CTS\_PD5\_9

| #define USART1\_CTS\_PD5\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 5, USART1, 9) |
| --- |

## [◆ ](#a7b1678aa77d79161e3228ba5a831093f)USART1\_CTS\_PD7\_4

| #define USART1\_CTS\_PD7\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 7, USART1, 4) |
| --- |

## [◆ ](#a084634f691aaebd09dfcd7a3a1e6d88e)USART1\_CTS\_PD7\_5

| #define USART1\_CTS\_PD7\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 7, USART1, 5) |
| --- |

## [◆ ](#afcd1f752d8e97796f0985417851710bd)USART1\_RTS\_PA5\_4

| #define USART1\_RTS\_PA5\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 5, USART1, 4) |
| --- |

## [◆ ](#a7aabe7289738f464b844869f11d2ad77)USART1\_RTS\_PA5\_5

| #define USART1\_RTS\_PA5\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 5, USART1, 5) |
| --- |

## [◆ ](#a9fd3866c5f193a5adc0b39c839c7bb66)USART1\_RTS\_PB4\_6

| #define USART1\_RTS\_PB4\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, USART1, 6) |
| --- |

## [◆ ](#a0d05f6fd7d5b563889e66918cd5f20d5)USART1\_RTS\_PB4\_7

| #define USART1\_RTS\_PB4\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 4, USART1, 7) |
| --- |

## [◆ ](#a2815ef4f646852914ddd2b8e8b7badef)USART1\_RTS\_PC2\_0

| #define USART1\_RTS\_PC2\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, USART1, 0) |
| --- |

## [◆ ](#a8a863333c39e43bcebaef2476f342f1f)USART1\_RTS\_PC2\_2

| #define USART1\_RTS\_PC2\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, USART1, 2) |
| --- |

## [◆ ](#aea3a162c52835b61fea5ffcb19793947)USART1\_RTS\_PC7\_1

| #define USART1\_RTS\_PC7\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 1) |
| --- |

## [◆ ](#ae8804a9a24491c2f723261061f783375)USART1\_RTS\_PC7\_3

| #define USART1\_RTS\_PC7\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 3) |
| --- |

## [◆ ](#a7bd4d249b211ba28ad2d06f7b67ab631)USART1\_RTS\_PD3\_8

| #define USART1\_RTS\_PD3\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, USART1, 8) |
| --- |

## [◆ ](#a9c03c1d8a7a68304271ed06439a10378)USART1\_RTS\_PD4\_9

| #define USART1\_RTS\_PD4\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 4, USART1, 9) |
| --- |

## [◆ ](#aafac07305b388d70b6d7f54bd980910c)USART1\_RX\_PA1\_8

| #define USART1\_RX\_PA1\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, USART1, 8) |
| --- |

## [◆ ](#adecf7a857f74ccd2bc11c58ae935564b)USART1\_RX\_PB3\_4

| #define USART1\_RX\_PB3\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, USART1, 4) |
| --- |

## [◆ ](#a842305cdfe152b432b2b0935d4066aa1)USART1\_RX\_PB6\_7

| #define USART1\_RX\_PB6\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 6, USART1, 7) |
| --- |

## [◆ ](#a61ec872334034b3d83feacf87a71ee51)USART1\_RX\_PC1\_3

| #define USART1\_RX\_PC1\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, USART1, 3) |
| --- |

## [◆ ](#addb61f3eb63ef8a3a403a8587502aaf4)USART1\_RX\_PC4\_9

| #define USART1\_RX\_PC4\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, USART1, 9) |
| --- |

## [◆ ](#a535de4a0f3d5c2844b8a6787820fc6ef)USART1\_RX\_PC6\_6

| #define USART1\_RX\_PC6\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, USART1, 6) |
| --- |

## [◆ ](#ad17459ba5c85756bb6b35215908e552b)USART1\_RX\_PD1\_2

| #define USART1\_RX\_PD1\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, USART1, 2) |
| --- |

## [◆ ](#aac2be2e46c973ba5efe27f0fff98cabb)USART1\_RX\_PD1\_5

| #define USART1\_RX\_PD1\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, USART1, 5) |
| --- |

## [◆ ](#aca9c065151c7d1439d03a218bad28953)USART1\_RX\_PD5\_1

| #define USART1\_RX\_PD5\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 5, USART1, 1) |
| --- |

## [◆ ](#a0f6ad0455dc48303bde7bc475f7215de)USART1\_RX\_PD6\_0

| #define USART1\_RX\_PD6\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 6, USART1, 0) |
| --- |

## [◆ ](#ad4bbf2f73d5cf308809e72a59f279d4f)USART1\_TX\_PA0\_8

| #define USART1\_TX\_PA0\_8   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, USART1, 8) |
| --- |

## [◆ ](#a9e1cb2fc5b61479fca18f844c7b2a25b)USART1\_TX\_PA0\_9

| #define USART1\_TX\_PA0\_9   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, USART1, 9) |
| --- |

## [◆ ](#a874ce1580f9150018621cd69fc593278)USART1\_TX\_PB3\_5

| #define USART1\_TX\_PB3\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, USART1, 5) |
| --- |

## [◆ ](#a88180919d778bce4a76a50ebbdec9a01)USART1\_TX\_PB5\_7

| #define USART1\_TX\_PB5\_7   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 5, USART1, 7) |
| --- |

## [◆ ](#ada26f8c1b5c0e9d74bc82ac68b836382)USART1\_TX\_PC0\_3

| #define USART1\_TX\_PC0\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, USART1, 3) |
| --- |

## [◆ ](#a273118d50602170728e67f4bbfe166f9)USART1\_TX\_PC5\_6

| #define USART1\_TX\_PC5\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, USART1, 6) |
| --- |

## [◆ ](#a2929a6724518bf36c15be8fc658bde05)USART1\_TX\_PD0\_2

| #define USART1\_TX\_PD0\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 0, USART1, 2) |
| --- |

## [◆ ](#a46939eb59b23c13c4963035abfe5e0fc)USART1\_TX\_PD1\_4

| #define USART1\_TX\_PD1\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, USART1, 4) |
| --- |

## [◆ ](#ab7c3bcaa4f01310261473cb734aeba23)USART1\_TX\_PD5\_0

| #define USART1\_TX\_PD5\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 5, USART1, 0) |
| --- |

## [◆ ](#a65805902e3f58b907beb0d7f39380d87)USART1\_TX\_PD6\_1

| #define USART1\_TX\_PD6\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 6, USART1, 1) |
| --- |

## [◆ ](#ac0a15096977f216e21f51d72f57eec14)USART2\_CTS\_PA0\_2

| #define USART2\_CTS\_PA0\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, USART2, 2) |
| --- |

## [◆ ](#a2a1d5ae373cabd13b5353dacf9d8ccb1)USART2\_CTS\_PA0\_3

| #define USART2\_CTS\_PA0\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 0, USART2, 3) |
| --- |

## [◆ ](#ab0fed132ce4b4e328ad5abec7623fb34)USART2\_CTS\_PA4\_0

| #define USART2\_CTS\_PA4\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 4, USART2, 0) |
| --- |

## [◆ ](#aef802806cabe330d83fb51b60b3a11c3)USART2\_CTS\_PA4\_5

| #define USART2\_CTS\_PA4\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 4, USART2, 5) |
| --- |

## [◆ ](#adce3d83fc3e34f6e0bd8910e079ac8e1)USART2\_CTS\_PA7\_1

| #define USART2\_CTS\_PA7\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 7, USART2, 1) |
| --- |

## [◆ ](#a0783ddd911225e749bc93997d9c95b03)USART2\_CTS\_PA7\_6

| #define USART2\_CTS\_PA7\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 7, USART2, 6) |
| --- |

## [◆ ](#a9c29cf0c467d5806bbd31bf492e446b8)USART2\_CTS\_PB6\_4

| #define USART2\_CTS\_PB6\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 6, USART2, 4) |
| --- |

## [◆ ](#a5c3789ef5097d4f3d85f701e7263ab8f)USART2\_RTS\_PA1\_2

| #define USART2\_RTS\_PA1\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, USART2, 2) |
| --- |

## [◆ ](#aaa1dc5b02f8af2f3ccddf8001ff38bd7)USART2\_RTS\_PA1\_3

| #define USART2\_RTS\_PA1\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, USART2, 3) |
| --- |

## [◆ ](#ae700c6a7177c687a5fc1094a590b6843)USART2\_RTS\_PA1\_4

| #define USART2\_RTS\_PA1\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, USART2, 4) |
| --- |

## [◆ ](#af854dc720498465e10d20d7c1b695aa8)USART2\_RTS\_PA1\_5

| #define USART2\_RTS\_PA1\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 1, USART2, 5) |
| --- |

## [◆ ](#ac899df236d1a1698b96882eaba4c1164)USART2\_RTS\_PA5\_0

| #define USART2\_RTS\_PA5\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 5, USART2, 0) |
| --- |

## [◆ ](#a53cf31b3362a596622e3cbe3d768e80a)USART2\_RTS\_PB3\_1

| #define USART2\_RTS\_PB3\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, USART2, 1) |
| --- |

## [◆ ](#a75465838304ad680659ba79288d3b44a)USART2\_RTS\_PB3\_6

| #define USART2\_RTS\_PB3\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, USART2, 6) |
| --- |

## [◆ ](#a8be97f0b92fc2e84e6167f753583b3bd)USART2\_RX\_PA3\_2

| #define USART2\_RX\_PA3\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 3, USART2, 2) |
| --- |

## [◆ ](#aff4e0a27fc6b6dd4ffd83931e520172b)USART2\_RX\_PA5\_1

| #define USART2\_RX\_PA5\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 5, USART2, 1) |
| --- |

## [◆ ](#a858fad6e9a5e6cbad0abba8836717438)USART2\_RX\_PA5\_6

| #define USART2\_RX\_PA5\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 5, USART2, 6) |
| --- |

## [◆ ](#aaee97f5922b1307da5c4c390056b70b3)USART2\_RX\_PB1\_4

| #define USART2\_RX\_PB1\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 1, USART2, 4) |
| --- |

## [◆ ](#ac0c914e26ad7390875e5080dee790103)USART2\_RX\_PB3\_0

| #define USART2\_RX\_PB3\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 3, USART2, 0) |
| --- |

## [◆ ](#a8b8d33c7c70681cbf95eaed62e9aab41)USART2\_RX\_PD1\_5

| #define USART2\_RX\_PD1\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 1, USART2, 5) |
| --- |

## [◆ ](#ab7dce0cc7991ebd63d81421422f317a3)USART2\_RX\_PD3\_3

| #define USART2\_RX\_PD3\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 3, USART2, 3) |
| --- |

## [◆ ](#a9a4cf7fffcb285c0ad955f66f8fbd2c0)USART2\_TX\_PA2\_2

| #define USART2\_TX\_PA2\_2   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 2, USART2, 2) |
| --- |

## [◆ ](#af11623f802cf65e3626b38050a8404fe)USART2\_TX\_PA4\_1

| #define USART2\_TX\_PA4\_1   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 4, USART2, 1) |
| --- |

## [◆ ](#a24153b4ce2024673ad86cd9c490f0889)USART2\_TX\_PA6\_6

| #define USART2\_TX\_PA6\_6   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 6, USART2, 6) |
| --- |

## [◆ ](#a0152727406750ce80df2377242967147)USART2\_TX\_PA7\_0

| #define USART2\_TX\_PA7\_0   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PA, 7, USART2, 0) |
| --- |

## [◆ ](#acef47a522b84c0971442a3498fd2cf3e)USART2\_TX\_PB0\_4

| #define USART2\_TX\_PB0\_4   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PB, 0, USART2, 4) |
| --- |

## [◆ ](#a49dc559bd4fe32265256417609b84fd7)USART2\_TX\_PC4\_5

| #define USART2\_TX\_PC4\_5   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, USART2, 5) |
| --- |

## [◆ ](#a9b0571dfb1330177950f6531feb90a50)USART2\_TX\_PD2\_3

| #define USART2\_TX\_PD2\_3   [CH32V00X\_PINMUX\_DEFINE](#a1c30350d4532ec3cfb69a2febfa9dc09)(PD, 2, USART2, 3) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ch32v00x-pinctrl.h](ch32v00x-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
