---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xg24-clock_8h.html
original_path: doxygen/html/xg24-clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xg24-clock.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`  
`#include "[common-clock.h](common-clock_8h_source.md)"`

[Go to the source code of this file.](xg24-clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CLOCK\_ACMP0](#aa32e8dd815ce9bdc0b7522870897dcb6)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 18)) |
| #define | [CLOCK\_ACMP1](#ae61fef5c45a7a46b73ab7da7626c2b0e)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 19)) |
| #define | [CLOCK\_AGC](#ac423554c8fbc051d4e0a92ac522c12fd)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 0)) |
| #define | [CLOCK\_AMUXCP0](#ae337a36d2929e0fb5bfae761fb5e4133)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 11)) |
| #define | [CLOCK\_BUFC](#a96e069b371ff072641af60e430fde7ce)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 11)) |
| #define | [CLOCK\_BURAM](#a8cf43d2d70becc6693f00f1d13df6672)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 28)) |
| #define | [CLOCK\_BURTC](#ac6695946933b50787d425561a25e9dce)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 29)) |
| #define | [CLOCK\_DCDC](#a9504e14e6a046f49d4ef84eeae2df2bf)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 31)) |
| #define | [CLOCK\_DMEM](#a8e50572855850c3f04e1114a1520a140)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 27)) |
| #define | [CLOCK\_DPLL0](#a43e09951e6aa4e639eae06a5e0c6677a)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 17)) |
| #define | [CLOCK\_ECAIFADC](#af8d36ae7fb5a31d6acf4e3f3972bd619)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 28)) |
| #define | [CLOCK\_EUSART0](#a1d5233b4a9be81005ddf56f66568baec)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 22)) |
| #define | [CLOCK\_EUSART1](#ad398276d374ded1ccf287e1c045bd044)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 23)) |
| #define | [CLOCK\_FRC](#a2353de593fcfd3470ea74ac3f31a5733)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 3)) |
| #define | [CLOCK\_FSRCO](#abfe043f434d02bdfe02fbfb3d366b635)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 21)) |
| #define | [CLOCK\_GPCRC0](#acf6f54d61368bab9ce995f5110043a16)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 3)) |
| #define | [CLOCK\_GPIO](#ac9a5b112066c69cd6a28a5baa5d97763)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 26)) |
| #define | [CLOCK\_HFRCO0](#a4033b997dcc4154c2a0a45ac5e268b34)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 18)) |
| #define | [CLOCK\_HFRCOEM23](#a09a36ffa8404e69c113b6740c6dc56f7)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 19)) |
| #define | [CLOCK\_HFXO0](#a211db0ef9eb5fd922a1da0d176bbd77f)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 20)) |
| #define | [CLOCK\_HOSTMAILBOX](#a4675a43d737508b80a9855fb6039d1a4)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 8)) |
| #define | [CLOCK\_I2C0](#a65099db536e93d1a86dd906b60eea384)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 14)) |
| #define | [CLOCK\_I2C1](#a1222ea08bdd44c6134086340603db3ef)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 15)) |
| #define | [CLOCK\_IADC0](#a70da15f668624c0248a0658d6f67045b)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 10)) |
| #define | [CLOCK\_ICACHE0](#afaa58305165ee49bb49ecfad5a8921cb)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 15)) |
| #define | [CLOCK\_KEYSCAN](#abf9a2c01e905a1719bab856ef72102e8)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 13)) |
| #define | [CLOCK\_LDMA0](#a0b7b2229ddfaf6fa50a563fbf528cab1)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 0)) |
| #define | [CLOCK\_LDMAXBAR0](#afe5cc402821e803fab34737c189cec7a)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 1)) |
| #define | [CLOCK\_LETIMER0](#ad870dd62c2096ad2900ef45e6712fb49)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 12)) |
| #define | [CLOCK\_LFRCO](#ad2d432d8875b83c61dc68cdd4af502eb)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 22)) |
| #define | [CLOCK\_LFXO](#a733a59a9c18f28f1be26d1130db4efea)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 23)) |
| #define | [CLOCK\_MODEM](#a607ed604d7ba35581c270d2d709c61d3)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 1)) |
| #define | [CLOCK\_MSC](#a5a31a3404f0493d75883df158a1aced7)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 16)) |
| #define | [CLOCK\_MVP](#a250078dd8cc2c15aa0c9682651b8389a)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 30)) |
| #define | [CLOCK\_PCNT0](#ad545d81b3eb92be7af16bda62992d836)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 21)) |
| #define | [CLOCK\_PROTIMER](#a176efcb9464ddb31ea542656e9135e8c)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 4)) |
| #define | [CLOCK\_PRS](#a2817c4a05dcc4e1396ec6c63a367f447)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 27)) |
| #define | [CLOCK\_RAC](#a9a0ffab31dccc0d5d51714b77e3634e9)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 5)) |
| #define | [CLOCK\_RADIOAES](#a295e418f558aaeb62205b7cf36a8323d)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 2)) |
| #define | [CLOCK\_RFCRC](#ab5c58598f68a536bc02cef4c637ba7f3)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 2)) |
| #define | [CLOCK\_RFECA0](#a0c8c44e37a5079d0f1341d4bdd34f29d)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 25)) |
| #define | [CLOCK\_RFECA1](#a84ad7235efe443d2d3b3d6d96055fd72)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 26)) |
| #define | [CLOCK\_RFMAILBOX](#a8a6a93f7fc102a4f4e6c065fa82bca98)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 9)) |
| #define | [CLOCK\_RFSCRATCHPAD](#ae2611f620e722482b43df43a0e9521e6)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 7)) |
| #define | [CLOCK\_SEMAILBOX](#a93f506b24bf622e44f63cf610fe31f41)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 10)) |
| #define | [CLOCK\_SMU](#a0f07f886f88f078cae0881b0acb52cc0)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 14)) |
| #define | [CLOCK\_SYNTH](#aa6a892710ce9bf2be66d3e8fe841e6e1)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 6)) |
| #define | [CLOCK\_SYSCFG](#a329ef704c35a3eaa8d090df174447fb9)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 16)) |
| #define | [CLOCK\_SYSRTC0](#a25b5c00156e05033439f8dbd15370e2f)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 30)) |
| #define | [CLOCK\_TIMER0](#aaadc635085924c9617dad97b02599427)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 4)) |
| #define | [CLOCK\_TIMER1](#aecedef6c3a70a73218e22df6e0eaddf0)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 5)) |
| #define | [CLOCK\_TIMER2](#a851d358e4228381ab0e07d0ac2cff900)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 6)) |
| #define | [CLOCK\_TIMER3](#ab3325cceec53072d0a1d6a3b891e9d2f)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 7)) |
| #define | [CLOCK\_TIMER4](#ae21cf62d77f707b63565874f43991907)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 8)) |
| #define | [CLOCK\_ULFRCO](#ae47c38f62d4a6a8b00bfa83820c242d3)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 24)) |
| #define | [CLOCK\_USART0](#a3efea2284aac64b602f7fdb9ebd301ae)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 9)) |
| #define | [CLOCK\_VDAC0](#a5ffac1952fae08520cd6794a77f61591)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 20)) |
| #define | [CLOCK\_VDAC1](#a20b79a4e9ccedeff27492c400e2bf882)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 29)) |
| #define | [CLOCK\_WDOG0](#ad2c27e5766fc2d7d458b62cfd7670d94)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 13)) |
| #define | [CLOCK\_WDOG1](#a15d2f4f9261ee4a748a5c25b9e956618)   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 17)) |

## Macro Definition Documentation

## [◆ ](#aa32e8dd815ce9bdc0b7522870897dcb6)CLOCK\_ACMP0

| #define CLOCK\_ACMP0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 18)) |
| --- |

## [◆ ](#ae61fef5c45a7a46b73ab7da7626c2b0e)CLOCK\_ACMP1

| #define CLOCK\_ACMP1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 19)) |
| --- |

## [◆ ](#ac423554c8fbc051d4e0a92ac522c12fd)CLOCK\_AGC

| #define CLOCK\_AGC   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 0)) |
| --- |

## [◆ ](#ae337a36d2929e0fb5bfae761fb5e4133)CLOCK\_AMUXCP0

| #define CLOCK\_AMUXCP0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 11)) |
| --- |

## [◆ ](#a96e069b371ff072641af60e430fde7ce)CLOCK\_BUFC

| #define CLOCK\_BUFC   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 11)) |
| --- |

## [◆ ](#a8cf43d2d70becc6693f00f1d13df6672)CLOCK\_BURAM

| #define CLOCK\_BURAM   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 28)) |
| --- |

## [◆ ](#ac6695946933b50787d425561a25e9dce)CLOCK\_BURTC

| #define CLOCK\_BURTC   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 29)) |
| --- |

## [◆ ](#a9504e14e6a046f49d4ef84eeae2df2bf)CLOCK\_DCDC

| #define CLOCK\_DCDC   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 31)) |
| --- |

## [◆ ](#a8e50572855850c3f04e1114a1520a140)CLOCK\_DMEM

| #define CLOCK\_DMEM   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 27)) |
| --- |

## [◆ ](#a43e09951e6aa4e639eae06a5e0c6677a)CLOCK\_DPLL0

| #define CLOCK\_DPLL0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 17)) |
| --- |

## [◆ ](#af8d36ae7fb5a31d6acf4e3f3972bd619)CLOCK\_ECAIFADC

| #define CLOCK\_ECAIFADC   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 28)) |
| --- |

## [◆ ](#a1d5233b4a9be81005ddf56f66568baec)CLOCK\_EUSART0

| #define CLOCK\_EUSART0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 22)) |
| --- |

## [◆ ](#ad398276d374ded1ccf287e1c045bd044)CLOCK\_EUSART1

| #define CLOCK\_EUSART1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 23)) |
| --- |

## [◆ ](#a2353de593fcfd3470ea74ac3f31a5733)CLOCK\_FRC

| #define CLOCK\_FRC   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 3)) |
| --- |

## [◆ ](#abfe043f434d02bdfe02fbfb3d366b635)CLOCK\_FSRCO

| #define CLOCK\_FSRCO   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 21)) |
| --- |

## [◆ ](#acf6f54d61368bab9ce995f5110043a16)CLOCK\_GPCRC0

| #define CLOCK\_GPCRC0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 3)) |
| --- |

## [◆ ](#ac9a5b112066c69cd6a28a5baa5d97763)CLOCK\_GPIO

| #define CLOCK\_GPIO   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 26)) |
| --- |

## [◆ ](#a4033b997dcc4154c2a0a45ac5e268b34)CLOCK\_HFRCO0

| #define CLOCK\_HFRCO0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 18)) |
| --- |

## [◆ ](#a09a36ffa8404e69c113b6740c6dc56f7)CLOCK\_HFRCOEM23

| #define CLOCK\_HFRCOEM23   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 19)) |
| --- |

## [◆ ](#a211db0ef9eb5fd922a1da0d176bbd77f)CLOCK\_HFXO0

| #define CLOCK\_HFXO0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 20)) |
| --- |

## [◆ ](#a4675a43d737508b80a9855fb6039d1a4)CLOCK\_HOSTMAILBOX

| #define CLOCK\_HOSTMAILBOX   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 8)) |
| --- |

## [◆ ](#a65099db536e93d1a86dd906b60eea384)CLOCK\_I2C0

| #define CLOCK\_I2C0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 14)) |
| --- |

## [◆ ](#a1222ea08bdd44c6134086340603db3ef)CLOCK\_I2C1

| #define CLOCK\_I2C1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 15)) |
| --- |

## [◆ ](#a70da15f668624c0248a0658d6f67045b)CLOCK\_IADC0

| #define CLOCK\_IADC0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 10)) |
| --- |

## [◆ ](#afaa58305165ee49bb49ecfad5a8921cb)CLOCK\_ICACHE0

| #define CLOCK\_ICACHE0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 15)) |
| --- |

## [◆ ](#abf9a2c01e905a1719bab856ef72102e8)CLOCK\_KEYSCAN

| #define CLOCK\_KEYSCAN   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 13)) |
| --- |

## [◆ ](#a0b7b2229ddfaf6fa50a563fbf528cab1)CLOCK\_LDMA0

| #define CLOCK\_LDMA0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 0)) |
| --- |

## [◆ ](#afe5cc402821e803fab34737c189cec7a)CLOCK\_LDMAXBAR0

| #define CLOCK\_LDMAXBAR0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 1)) |
| --- |

## [◆ ](#ad870dd62c2096ad2900ef45e6712fb49)CLOCK\_LETIMER0

| #define CLOCK\_LETIMER0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 12)) |
| --- |

## [◆ ](#ad2d432d8875b83c61dc68cdd4af502eb)CLOCK\_LFRCO

| #define CLOCK\_LFRCO   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 22)) |
| --- |

## [◆ ](#a733a59a9c18f28f1be26d1130db4efea)CLOCK\_LFXO

| #define CLOCK\_LFXO   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 23)) |
| --- |

## [◆ ](#a607ed604d7ba35581c270d2d709c61d3)CLOCK\_MODEM

| #define CLOCK\_MODEM   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 1)) |
| --- |

## [◆ ](#a5a31a3404f0493d75883df158a1aced7)CLOCK\_MSC

| #define CLOCK\_MSC   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 16)) |
| --- |

## [◆ ](#a250078dd8cc2c15aa0c9682651b8389a)CLOCK\_MVP

| #define CLOCK\_MVP   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 30)) |
| --- |

## [◆ ](#ad545d81b3eb92be7af16bda62992d836)CLOCK\_PCNT0

| #define CLOCK\_PCNT0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 21)) |
| --- |

## [◆ ](#a176efcb9464ddb31ea542656e9135e8c)CLOCK\_PROTIMER

| #define CLOCK\_PROTIMER   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 4)) |
| --- |

## [◆ ](#a2817c4a05dcc4e1396ec6c63a367f447)CLOCK\_PRS

| #define CLOCK\_PRS   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 27)) |
| --- |

## [◆ ](#a9a0ffab31dccc0d5d51714b77e3634e9)CLOCK\_RAC

| #define CLOCK\_RAC   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 5)) |
| --- |

## [◆ ](#a295e418f558aaeb62205b7cf36a8323d)CLOCK\_RADIOAES

| #define CLOCK\_RADIOAES   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 2)) |
| --- |

## [◆ ](#ab5c58598f68a536bc02cef4c637ba7f3)CLOCK\_RFCRC

| #define CLOCK\_RFCRC   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 2)) |
| --- |

## [◆ ](#a0c8c44e37a5079d0f1341d4bdd34f29d)CLOCK\_RFECA0

| #define CLOCK\_RFECA0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 25)) |
| --- |

## [◆ ](#a84ad7235efe443d2d3b3d6d96055fd72)CLOCK\_RFECA1

| #define CLOCK\_RFECA1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 26)) |
| --- |

## [◆ ](#a8a6a93f7fc102a4f4e6c065fa82bca98)CLOCK\_RFMAILBOX

| #define CLOCK\_RFMAILBOX   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 9)) |
| --- |

## [◆ ](#ae2611f620e722482b43df43a0e9521e6)CLOCK\_RFSCRATCHPAD

| #define CLOCK\_RFSCRATCHPAD   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 7)) |
| --- |

## [◆ ](#a93f506b24bf622e44f63cf610fe31f41)CLOCK\_SEMAILBOX

| #define CLOCK\_SEMAILBOX   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 10)) |
| --- |

## [◆ ](#a0f07f886f88f078cae0881b0acb52cc0)CLOCK\_SMU

| #define CLOCK\_SMU   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 14)) |
| --- |

## [◆ ](#aa6a892710ce9bf2be66d3e8fe841e6e1)CLOCK\_SYNTH

| #define CLOCK\_SYNTH   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 6)) |
| --- |

## [◆ ](#a329ef704c35a3eaa8d090df174447fb9)CLOCK\_SYSCFG

| #define CLOCK\_SYSCFG   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 16)) |
| --- |

## [◆ ](#a25b5c00156e05033439f8dbd15370e2f)CLOCK\_SYSRTC0

| #define CLOCK\_SYSRTC0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 30)) |
| --- |

## [◆ ](#aaadc635085924c9617dad97b02599427)CLOCK\_TIMER0

| #define CLOCK\_TIMER0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 4)) |
| --- |

## [◆ ](#aecedef6c3a70a73218e22df6e0eaddf0)CLOCK\_TIMER1

| #define CLOCK\_TIMER1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 5)) |
| --- |

## [◆ ](#a851d358e4228381ab0e07d0ac2cff900)CLOCK\_TIMER2

| #define CLOCK\_TIMER2   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 6)) |
| --- |

## [◆ ](#ab3325cceec53072d0a1d6a3b891e9d2f)CLOCK\_TIMER3

| #define CLOCK\_TIMER3   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 7)) |
| --- |

## [◆ ](#ae21cf62d77f707b63565874f43991907)CLOCK\_TIMER4

| #define CLOCK\_TIMER4   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 8)) |
| --- |

## [◆ ](#ae47c38f62d4a6a8b00bfa83820c242d3)CLOCK\_ULFRCO

| #define CLOCK\_ULFRCO   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 24)) |
| --- |

## [◆ ](#a3efea2284aac64b602f7fdb9ebd301ae)CLOCK\_USART0

| #define CLOCK\_USART0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 9)) |
| --- |

## [◆ ](#a5ffac1952fae08520cd6794a77f61591)CLOCK\_VDAC0

| #define CLOCK\_VDAC0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 20)) |
| --- |

## [◆ ](#a20b79a4e9ccedeff27492c400e2bf882)CLOCK\_VDAC1

| #define CLOCK\_VDAC1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 29)) |
| --- |

## [◆ ](#ad2c27e5766fc2d7d458b62cfd7670d94)CLOCK\_WDOG0

| #define CLOCK\_WDOG0   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 0) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 13)) |
| --- |

## [◆ ](#a15d2f4f9261ee4a748a5c25b9e956618)CLOCK\_WDOG1

| #define CLOCK\_WDOG1   ([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_REG\_MASK](common-clock_8h.md#adb54589c8ff63fe8dd82d1739fb4d256), 1) | [FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([CLOCK\_BIT\_MASK](common-clock_8h.md#a81609d56a415da8a22bd83d651cab503), 17)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [silabs](dir_9d9a53d793dad9345737df2b8d108293.md)
- [xg24-clock.h](xg24-clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
