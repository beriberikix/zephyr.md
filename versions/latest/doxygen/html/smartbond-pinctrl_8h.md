---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/smartbond-pinctrl_8h.html
original_path: doxygen/html/smartbond-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smartbond-pinctrl.h File Reference

[Go to the source code of this file.](smartbond-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SMARTBOND\_FUNC\_GPIO](#a7089e1e95fff22ba99344704b7f731b7)   0 |
|  | Definitions of pin functions. |
| #define | [SMARTBOND\_FUNC\_UART\_RX](#a6ed07d7b66f1b82356a972237319ac9b)   1 |
| #define | [SMARTBOND\_FUNC\_UART\_TX](#a5dfe9979613105acf742ea4c64afb8f2)   2 |
| #define | [SMARTBOND\_FUNC\_UART2\_RX](#ad9b9d93fd00717dba1a32feac99a760a)   3 |
| #define | [SMARTBOND\_FUNC\_UART2\_TX](#ab8dc0782b4c39f9f04bffbd68e201b07)   4 |
| #define | [SMARTBOND\_FUNC\_UART2\_CTSN](#a28291720995487ed1909701d27bb6608)   5 |
| #define | [SMARTBOND\_FUNC\_UART2\_RTSN](#aea2618531f8eca9f53a66df1c2e40cbe)   6 |
| #define | [SMARTBOND\_FUNC\_UART3\_RX](#a5b3943d551d13bdd36407145262a56f9)   7 |
| #define | [SMARTBOND\_FUNC\_UART3\_TX](#aa0d293e2a1c45c9f4a8b33b81d0efe09)   8 |
| #define | [SMARTBOND\_FUNC\_UART3\_CTSN](#ab78ba1d4ce9f4551480a8245439607f2)   9 |
| #define | [SMARTBOND\_FUNC\_UART3\_RTSN](#a34305c8d6c03afebd72736e274f34c86)   10 |
| #define | [SMARTBOND\_FUNC\_ISO\_CLK](#acf912059ad7e32d8241f6c7881c4cb28)   11 |
| #define | [SMARTBOND\_FUNC\_ISO\_DATA](#aac93ef7075ed12f86b829bd705c7400a)   12 |
| #define | [SMARTBOND\_FUNC\_SPI\_DI](#a43277e708883b30efd1fa2360801c9ea)   13 |
| #define | [SMARTBOND\_FUNC\_SPI\_DO](#a64d7cd483d90e3b1102243c191d189eb)   14 |
| #define | [SMARTBOND\_FUNC\_SPI\_CLK](#a7b9f3eec74e21b5b2aaef12c234bea64)   15 |
| #define | [SMARTBOND\_FUNC\_SPI\_EN](#a41d2f9824fb7d591b61482431b39d049)   16 |
| #define | [SMARTBOND\_FUNC\_SPI2\_DI](#acab6331b3ee09ed93b7963c9e3c4e0e7)   17 |
| #define | [SMARTBOND\_FUNC\_SPI2\_DO](#ae0282ae5f03793c9c8af9d7affeefe23)   18 |
| #define | [SMARTBOND\_FUNC\_SPI2\_CLK](#abb67eca8ba3b48ab5436a4609f1a633f)   19 |
| #define | [SMARTBOND\_FUNC\_SPI2\_EN](#abe46de2948d1c93a938511a78f7a762f)   20 |
| #define | [SMARTBOND\_FUNC\_I2C\_SCL](#a5b5f41a1016d0430196ee473cbc7a2c5)   21 |
| #define | [SMARTBOND\_FUNC\_I2C\_SDA](#a3a8535069c0b427b0f970248563739fe)   22 |
| #define | [SMARTBOND\_FUNC\_I2C2\_SCL](#ada4dba2404b4f79eb57ad2a8865c94e4)   23 |
| #define | [SMARTBOND\_FUNC\_I2C2\_SDA](#ac456dcf0d16f720e6f19459eb11f7ef3)   24 |
| #define | [SMARTBOND\_FUNC\_USB\_SOF](#a5613a9d97ed91227f724e632cd3a995a)   25 |
| #define | [SMARTBOND\_FUNC\_ADC](#a93ae4c46ba7233a074cae8a9750e3246)   26 |
| #define | [SMARTBOND\_FUNC\_USB](#af55696a1a2c476841085901eb030bf06)   27 |
| #define | [SMARTBOND\_FUNC\_PCM\_DI](#aa8f8d6b30ff693e02863aebce0fda1f7)   28 |
| #define | [SMARTBOND\_FUNC\_PCM\_DO](#a8d2af85827bae92e3323ae7af6795d39)   29 |
| #define | [SMARTBOND\_FUNC\_PCM\_FSC](#a0350a10a2a18f35042eb1d1380d06e71)   30 |
| #define | [SMARTBOND\_FUNC\_PCM\_CLK](#ab966d361e29c0a4bec64edb8f1f13fcd)   31 |
| #define | [SMARTBOND\_FUNC\_PDM\_DATA](#a41038d013590b0fa06e0009071e77913)   32 |
| #define | [SMARTBOND\_FUNC\_PDM\_CLK](#a9c6dc0a72667b6659761fb900e6cb74e)   33 |
| #define | [SMARTBOND\_FUNC\_COEX\_EXT\_ACT](#a10e19e7f0d69a912341211e18d88d9fb)   34 |
| #define | [SMARTBOND\_FUNC\_COEX\_SMART\_ACT](#a7e470cb7f8deb22199ac0fb2ec7e6867)   35 |
| #define | [SMARTBOND\_FUNC\_COEX\_SMART\_PRI](#a17ad842b2c1dfa9f7d2cf8ec9ec67589)   36 |
| #define | [SMARTBOND\_FUNC\_PORT0\_DCF](#ada643666dd9d0e7423c01b1852d01e08)   37 |
| #define | [SMARTBOND\_FUNC\_PORT1\_DCF](#a633ffca67ab63d296c82588a16717ecd)   38 |
| #define | [SMARTBOND\_FUNC\_PORT2\_DCF](#ae269c4303f7cbb595d015805870d489a)   39 |
| #define | [SMARTBOND\_FUNC\_PORT3\_DCF](#aee13677eb591c737d9aa87a56d5ab60e)   40 |
| #define | [SMARTBOND\_FUNC\_PORT4\_DCF](#a575776c065bdf0795f03931ef32a8014)   41 |
| #define | [SMARTBOND\_FUNC\_CLOCK](#adf15b25b1e76a63945454870bf8a5880)   42 |
| #define | [SMARTBOND\_FUNC\_PG](#a2710985bfb03536edebe925e42701372)   43 |
| #define | [SMARTBOND\_FUNC\_LCD](#a7131a57cb82a1fc7dff9e626dfaed3fa)   44 |
| #define | [SMARTBOND\_FUNC\_LCD\_SPI\_DC](#ac101bc374eb5a717b7bf8188683c2f2e)   45 |
| #define | [SMARTBOND\_FUNC\_LCD\_SPI\_DO](#a02d15016a20227a7470db3ce37b32ae9)   46 |
| #define | [SMARTBOND\_FUNC\_LCD\_SPI\_CLK](#ae17f0095eb1536bf0f477618d7f7d074)   47 |
| #define | [SMARTBOND\_FUNC\_LCD\_SPI\_EN](#af7e0123b209509f766bdee6fd5473456)   48 |
| #define | [SMARTBOND\_FUNC\_TIM\_PWM](#afe4022d7379a973034954b15e838f90c)   49 |
| #define | [SMARTBOND\_FUNC\_TIM2\_PWM](#a107f8c0c3a54d5fb01efa35f31edc6f9)   50 |
| #define | [SMARTBOND\_FUNC\_TIM\_1SHOT](#aa569b7d607bb41d6cc856e177aa2aff9)   51 |
| #define | [SMARTBOND\_FUNC\_TIM2\_1SHOT](#af9ed3f5a6c23379de2cdc58ce2856e66)   52 |
| #define | [SMARTBOND\_FUNC\_TIM3\_PWM](#a5a613b7538c4ae1252375f36f71128c4)   53 |
| #define | [SMARTBOND\_FUNC\_TIM4\_PWM](#a4aee45714b4104a48e1bebbcae2a1660)   54 |
| #define | [SMARTBOND\_PINMUX\_PIN\_POS](#a50e52287199ec82f928e24e9d12fa97b)   0 |
|  | Definitions of bit positions and bit masks in pinmux. |
| #define | [SMARTBOND\_PINMUX\_PIN\_MASK](#ae48f1167f7190d6acc13d1890ec6f141)   0x1f |
| #define | [SMARTBOND\_PINMUX\_PORT\_POS](#ab4cec4ecf671814e804cb3ad18236ac4)   5 |
| #define | [SMARTBOND\_PINMUX\_PORT\_MASK](#a8e82ad973c84c8b36240821fda17c07b)   0x01 |
| #define | [SMARTBOND\_PINMUX\_FUNC\_POS](#a0ed3e3f31e62d585a48fdfa04decf854)   6 |
| #define | [SMARTBOND\_PINMUX\_FUNC\_MASK](#a4dae490f035db9e564d95cb62ceb101c)   0xff |
| #define | [SMARTBOND\_PINMUX](#a66c942c39b093b0dbd3d174d6265600c)(func, port, pin) |
|  | Utility macro to create pinmux. |

## Macro Definition Documentation

## [◆ ](#a93ae4c46ba7233a074cae8a9750e3246)SMARTBOND\_FUNC\_ADC

| #define SMARTBOND\_FUNC\_ADC   26 |
| --- |

## [◆ ](#adf15b25b1e76a63945454870bf8a5880)SMARTBOND\_FUNC\_CLOCK

| #define SMARTBOND\_FUNC\_CLOCK   42 |
| --- |

## [◆ ](#a10e19e7f0d69a912341211e18d88d9fb)SMARTBOND\_FUNC\_COEX\_EXT\_ACT

| #define SMARTBOND\_FUNC\_COEX\_EXT\_ACT   34 |
| --- |

## [◆ ](#a7e470cb7f8deb22199ac0fb2ec7e6867)SMARTBOND\_FUNC\_COEX\_SMART\_ACT

| #define SMARTBOND\_FUNC\_COEX\_SMART\_ACT   35 |
| --- |

## [◆ ](#a17ad842b2c1dfa9f7d2cf8ec9ec67589)SMARTBOND\_FUNC\_COEX\_SMART\_PRI

| #define SMARTBOND\_FUNC\_COEX\_SMART\_PRI   36 |
| --- |

## [◆ ](#a7089e1e95fff22ba99344704b7f731b7)SMARTBOND\_FUNC\_GPIO

| #define SMARTBOND\_FUNC\_GPIO   0 |
| --- |

Definitions of pin functions.

## [◆ ](#ada4dba2404b4f79eb57ad2a8865c94e4)SMARTBOND\_FUNC\_I2C2\_SCL

| #define SMARTBOND\_FUNC\_I2C2\_SCL   23 |
| --- |

## [◆ ](#ac456dcf0d16f720e6f19459eb11f7ef3)SMARTBOND\_FUNC\_I2C2\_SDA

| #define SMARTBOND\_FUNC\_I2C2\_SDA   24 |
| --- |

## [◆ ](#a5b5f41a1016d0430196ee473cbc7a2c5)SMARTBOND\_FUNC\_I2C\_SCL

| #define SMARTBOND\_FUNC\_I2C\_SCL   21 |
| --- |

## [◆ ](#a3a8535069c0b427b0f970248563739fe)SMARTBOND\_FUNC\_I2C\_SDA

| #define SMARTBOND\_FUNC\_I2C\_SDA   22 |
| --- |

## [◆ ](#acf912059ad7e32d8241f6c7881c4cb28)SMARTBOND\_FUNC\_ISO\_CLK

| #define SMARTBOND\_FUNC\_ISO\_CLK   11 |
| --- |

## [◆ ](#aac93ef7075ed12f86b829bd705c7400a)SMARTBOND\_FUNC\_ISO\_DATA

| #define SMARTBOND\_FUNC\_ISO\_DATA   12 |
| --- |

## [◆ ](#a7131a57cb82a1fc7dff9e626dfaed3fa)SMARTBOND\_FUNC\_LCD

| #define SMARTBOND\_FUNC\_LCD   44 |
| --- |

## [◆ ](#ae17f0095eb1536bf0f477618d7f7d074)SMARTBOND\_FUNC\_LCD\_SPI\_CLK

| #define SMARTBOND\_FUNC\_LCD\_SPI\_CLK   47 |
| --- |

## [◆ ](#ac101bc374eb5a717b7bf8188683c2f2e)SMARTBOND\_FUNC\_LCD\_SPI\_DC

| #define SMARTBOND\_FUNC\_LCD\_SPI\_DC   45 |
| --- |

## [◆ ](#a02d15016a20227a7470db3ce37b32ae9)SMARTBOND\_FUNC\_LCD\_SPI\_DO

| #define SMARTBOND\_FUNC\_LCD\_SPI\_DO   46 |
| --- |

## [◆ ](#af7e0123b209509f766bdee6fd5473456)SMARTBOND\_FUNC\_LCD\_SPI\_EN

| #define SMARTBOND\_FUNC\_LCD\_SPI\_EN   48 |
| --- |

## [◆ ](#ab966d361e29c0a4bec64edb8f1f13fcd)SMARTBOND\_FUNC\_PCM\_CLK

| #define SMARTBOND\_FUNC\_PCM\_CLK   31 |
| --- |

## [◆ ](#aa8f8d6b30ff693e02863aebce0fda1f7)SMARTBOND\_FUNC\_PCM\_DI

| #define SMARTBOND\_FUNC\_PCM\_DI   28 |
| --- |

## [◆ ](#a8d2af85827bae92e3323ae7af6795d39)SMARTBOND\_FUNC\_PCM\_DO

| #define SMARTBOND\_FUNC\_PCM\_DO   29 |
| --- |

## [◆ ](#a0350a10a2a18f35042eb1d1380d06e71)SMARTBOND\_FUNC\_PCM\_FSC

| #define SMARTBOND\_FUNC\_PCM\_FSC   30 |
| --- |

## [◆ ](#a9c6dc0a72667b6659761fb900e6cb74e)SMARTBOND\_FUNC\_PDM\_CLK

| #define SMARTBOND\_FUNC\_PDM\_CLK   33 |
| --- |

## [◆ ](#a41038d013590b0fa06e0009071e77913)SMARTBOND\_FUNC\_PDM\_DATA

| #define SMARTBOND\_FUNC\_PDM\_DATA   32 |
| --- |

## [◆ ](#a2710985bfb03536edebe925e42701372)SMARTBOND\_FUNC\_PG

| #define SMARTBOND\_FUNC\_PG   43 |
| --- |

## [◆ ](#ada643666dd9d0e7423c01b1852d01e08)SMARTBOND\_FUNC\_PORT0\_DCF

| #define SMARTBOND\_FUNC\_PORT0\_DCF   37 |
| --- |

## [◆ ](#a633ffca67ab63d296c82588a16717ecd)SMARTBOND\_FUNC\_PORT1\_DCF

| #define SMARTBOND\_FUNC\_PORT1\_DCF   38 |
| --- |

## [◆ ](#ae269c4303f7cbb595d015805870d489a)SMARTBOND\_FUNC\_PORT2\_DCF

| #define SMARTBOND\_FUNC\_PORT2\_DCF   39 |
| --- |

## [◆ ](#aee13677eb591c737d9aa87a56d5ab60e)SMARTBOND\_FUNC\_PORT3\_DCF

| #define SMARTBOND\_FUNC\_PORT3\_DCF   40 |
| --- |

## [◆ ](#a575776c065bdf0795f03931ef32a8014)SMARTBOND\_FUNC\_PORT4\_DCF

| #define SMARTBOND\_FUNC\_PORT4\_DCF   41 |
| --- |

## [◆ ](#abb67eca8ba3b48ab5436a4609f1a633f)SMARTBOND\_FUNC\_SPI2\_CLK

| #define SMARTBOND\_FUNC\_SPI2\_CLK   19 |
| --- |

## [◆ ](#acab6331b3ee09ed93b7963c9e3c4e0e7)SMARTBOND\_FUNC\_SPI2\_DI

| #define SMARTBOND\_FUNC\_SPI2\_DI   17 |
| --- |

## [◆ ](#ae0282ae5f03793c9c8af9d7affeefe23)SMARTBOND\_FUNC\_SPI2\_DO

| #define SMARTBOND\_FUNC\_SPI2\_DO   18 |
| --- |

## [◆ ](#abe46de2948d1c93a938511a78f7a762f)SMARTBOND\_FUNC\_SPI2\_EN

| #define SMARTBOND\_FUNC\_SPI2\_EN   20 |
| --- |

## [◆ ](#a7b9f3eec74e21b5b2aaef12c234bea64)SMARTBOND\_FUNC\_SPI\_CLK

| #define SMARTBOND\_FUNC\_SPI\_CLK   15 |
| --- |

## [◆ ](#a43277e708883b30efd1fa2360801c9ea)SMARTBOND\_FUNC\_SPI\_DI

| #define SMARTBOND\_FUNC\_SPI\_DI   13 |
| --- |

## [◆ ](#a64d7cd483d90e3b1102243c191d189eb)SMARTBOND\_FUNC\_SPI\_DO

| #define SMARTBOND\_FUNC\_SPI\_DO   14 |
| --- |

## [◆ ](#a41d2f9824fb7d591b61482431b39d049)SMARTBOND\_FUNC\_SPI\_EN

| #define SMARTBOND\_FUNC\_SPI\_EN   16 |
| --- |

## [◆ ](#af9ed3f5a6c23379de2cdc58ce2856e66)SMARTBOND\_FUNC\_TIM2\_1SHOT

| #define SMARTBOND\_FUNC\_TIM2\_1SHOT   52 |
| --- |

## [◆ ](#a107f8c0c3a54d5fb01efa35f31edc6f9)SMARTBOND\_FUNC\_TIM2\_PWM

| #define SMARTBOND\_FUNC\_TIM2\_PWM   50 |
| --- |

## [◆ ](#a5a613b7538c4ae1252375f36f71128c4)SMARTBOND\_FUNC\_TIM3\_PWM

| #define SMARTBOND\_FUNC\_TIM3\_PWM   53 |
| --- |

## [◆ ](#a4aee45714b4104a48e1bebbcae2a1660)SMARTBOND\_FUNC\_TIM4\_PWM

| #define SMARTBOND\_FUNC\_TIM4\_PWM   54 |
| --- |

## [◆ ](#aa569b7d607bb41d6cc856e177aa2aff9)SMARTBOND\_FUNC\_TIM\_1SHOT

| #define SMARTBOND\_FUNC\_TIM\_1SHOT   51 |
| --- |

## [◆ ](#afe4022d7379a973034954b15e838f90c)SMARTBOND\_FUNC\_TIM\_PWM

| #define SMARTBOND\_FUNC\_TIM\_PWM   49 |
| --- |

## [◆ ](#a28291720995487ed1909701d27bb6608)SMARTBOND\_FUNC\_UART2\_CTSN

| #define SMARTBOND\_FUNC\_UART2\_CTSN   5 |
| --- |

## [◆ ](#aea2618531f8eca9f53a66df1c2e40cbe)SMARTBOND\_FUNC\_UART2\_RTSN

| #define SMARTBOND\_FUNC\_UART2\_RTSN   6 |
| --- |

## [◆ ](#ad9b9d93fd00717dba1a32feac99a760a)SMARTBOND\_FUNC\_UART2\_RX

| #define SMARTBOND\_FUNC\_UART2\_RX   3 |
| --- |

## [◆ ](#ab8dc0782b4c39f9f04bffbd68e201b07)SMARTBOND\_FUNC\_UART2\_TX

| #define SMARTBOND\_FUNC\_UART2\_TX   4 |
| --- |

## [◆ ](#ab78ba1d4ce9f4551480a8245439607f2)SMARTBOND\_FUNC\_UART3\_CTSN

| #define SMARTBOND\_FUNC\_UART3\_CTSN   9 |
| --- |

## [◆ ](#a34305c8d6c03afebd72736e274f34c86)SMARTBOND\_FUNC\_UART3\_RTSN

| #define SMARTBOND\_FUNC\_UART3\_RTSN   10 |
| --- |

## [◆ ](#a5b3943d551d13bdd36407145262a56f9)SMARTBOND\_FUNC\_UART3\_RX

| #define SMARTBOND\_FUNC\_UART3\_RX   7 |
| --- |

## [◆ ](#aa0d293e2a1c45c9f4a8b33b81d0efe09)SMARTBOND\_FUNC\_UART3\_TX

| #define SMARTBOND\_FUNC\_UART3\_TX   8 |
| --- |

## [◆ ](#a6ed07d7b66f1b82356a972237319ac9b)SMARTBOND\_FUNC\_UART\_RX

| #define SMARTBOND\_FUNC\_UART\_RX   1 |
| --- |

## [◆ ](#a5dfe9979613105acf742ea4c64afb8f2)SMARTBOND\_FUNC\_UART\_TX

| #define SMARTBOND\_FUNC\_UART\_TX   2 |
| --- |

## [◆ ](#af55696a1a2c476841085901eb030bf06)SMARTBOND\_FUNC\_USB

| #define SMARTBOND\_FUNC\_USB   27 |
| --- |

## [◆ ](#a5613a9d97ed91227f724e632cd3a995a)SMARTBOND\_FUNC\_USB\_SOF

| #define SMARTBOND\_FUNC\_USB\_SOF   25 |
| --- |

## [◆ ](#a66c942c39b093b0dbd3d174d6265600c)SMARTBOND\_PINMUX

| #define SMARTBOND\_PINMUX | ( |  | *func*, |
| --- | --- | --- | --- |
|  |  |  | *port*, |
|  |  |  | *pin* ) |

**Value:**

(((SMARTBOND\_FUNC\_ ## func) << [SMARTBOND\_PINMUX\_FUNC\_POS](#a0ed3e3f31e62d585a48fdfa04decf854)) | \

((port) << [SMARTBOND\_PINMUX\_PORT\_POS](#ab4cec4ecf671814e804cb3ad18236ac4)) | \

(pin) << [SMARTBOND\_PINMUX\_PIN\_POS](#a50e52287199ec82f928e24e9d12fa97b))

[SMARTBOND\_PINMUX\_FUNC\_POS](#a0ed3e3f31e62d585a48fdfa04decf854)

#define SMARTBOND\_PINMUX\_FUNC\_POS

**Definition** smartbond-pinctrl.h:72

[SMARTBOND\_PINMUX\_PIN\_POS](#a50e52287199ec82f928e24e9d12fa97b)

#define SMARTBOND\_PINMUX\_PIN\_POS

Definitions of bit positions and bit masks in pinmux.

**Definition** smartbond-pinctrl.h:68

[SMARTBOND\_PINMUX\_PORT\_POS](#ab4cec4ecf671814e804cb3ad18236ac4)

#define SMARTBOND\_PINMUX\_PORT\_POS

**Definition** smartbond-pinctrl.h:70

Utility macro to create pinmux.

## [◆ ](#a4dae490f035db9e564d95cb62ceb101c)SMARTBOND\_PINMUX\_FUNC\_MASK

| #define SMARTBOND\_PINMUX\_FUNC\_MASK   0xff |
| --- |

## [◆ ](#a0ed3e3f31e62d585a48fdfa04decf854)SMARTBOND\_PINMUX\_FUNC\_POS

| #define SMARTBOND\_PINMUX\_FUNC\_POS   6 |
| --- |

## [◆ ](#ae48f1167f7190d6acc13d1890ec6f141)SMARTBOND\_PINMUX\_PIN\_MASK

| #define SMARTBOND\_PINMUX\_PIN\_MASK   0x1f |
| --- |

## [◆ ](#a50e52287199ec82f928e24e9d12fa97b)SMARTBOND\_PINMUX\_PIN\_POS

| #define SMARTBOND\_PINMUX\_PIN\_POS   0 |
| --- |

Definitions of bit positions and bit masks in pinmux.

## [◆ ](#a8e82ad973c84c8b36240821fda17c07b)SMARTBOND\_PINMUX\_PORT\_MASK

| #define SMARTBOND\_PINMUX\_PORT\_MASK   0x01 |
| --- |

## [◆ ](#ab4cec4ecf671814e804cb3ad18236ac4)SMARTBOND\_PINMUX\_PORT\_POS

| #define SMARTBOND\_PINMUX\_PORT\_POS   5 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [smartbond-pinctrl.h](smartbond-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
