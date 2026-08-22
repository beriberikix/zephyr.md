---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arm-mps2-pinctrl_8h_source.html
original_path: doxygen/html/arm-mps2-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm-mps2-pinctrl.h

[Go to the documentation of this file.](arm-mps2-pinctrl_8h.md)

1/\*

2 \* Copyright 2025 Arm Limited and/or its affiliates <open-source-office@arm.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

[ 7](arm-mps2-pinctrl_8h.md#ad565796e43c28185243be8c71f910e3f)#define MPS2\_ALT\_FUNC\_POS 0

[ 8](arm-mps2-pinctrl_8h.md#a6ba3abb5ab20065ea59cb44a2b12f09e)#define MPS2\_ALT\_FUNC\_MASK 0x3

9

[ 10](arm-mps2-pinctrl_8h.md#a8fc17b69bcffa4039b207b6a4ab7475d)#define MPS2\_EXP\_NUM\_POS 2

[ 11](arm-mps2-pinctrl_8h.md#a98780dae8c8964bbcce2007cf5186b64)#define MPS2\_EXP\_NUM\_MASK 0x3F

12

[ 13](arm-mps2-pinctrl_8h.md#a793e19909cf9cdd9fb1aa0a34f835c65)#define MPS2\_PINCTRL\_FUNC\_UART 0

[ 14](arm-mps2-pinctrl_8h.md#af7cfe8556e424a3018d0e62e62f1b210)#define MPS2\_PINCTRL\_FUNC\_GPIO 1

[ 15](arm-mps2-pinctrl_8h.md#a33857f12895ab4ffb8bac15a226d9e44)#define MPS2\_PINCTRL\_FUNC\_I2C 2

[ 16](arm-mps2-pinctrl_8h.md#a459cfc88b65ae738b2a94be1fbe6df46)#define MPS2\_PINCTRL\_FUNC\_SPI 3

17

18

[ 19](arm-mps2-pinctrl_8h.md#affba791a0c60352a28b3d8f122534540)#define MPS2\_PINMUX(alt\_func, exp\_num) (exp\_num << MPS2\_EXP\_NUM\_POS | \

20 alt\_func << MPS2\_ALT\_FUNC\_POS)

21

22

23

24/\*

25 \* This is the mapping from the ARM MPS2 Board pins to GPIO

26 \* controllers.

27 \*

28 \* D0 : EXT\_0

29 \* D1 : EXT\_4

30 \* D2 : EXT\_2

31 \* D3 : EXT\_3

32 \* D4 : EXT\_1

33 \* D5 : EXT\_6

34 \* D6 : EXT\_7

35 \* D7 : EXT\_8

36 \* D8 : EXT\_9

37 \* D9 : EXT\_10

38 \* D10 : EXT\_12

39 \* D11 : EXT\_13

40 \* D12 : EXT\_14

41 \* D13 : EXT\_11

42 \* D14 : EXT\_15

43 \* D15 : EXT\_5

44 \* D16 : EXT\_16

45 \* D17 : EXT\_17

46 \* D18 : EXT\_18

47 \* D19 : EXT\_19

48 \* D20 : EXT\_20

49 \* D21 : EXT\_21

50 \* D22 : EXT\_22

51 \* D23 : EXT\_23

52 \* D24 : EXT\_24

53 \* D25 : EXT\_25

54 \* D26 : EXT\_26

55 \* D27 : EXT\_30

56 \* D28 : EXT\_28

57 \* D29 : EXT\_29

58 \* D30 : EXT\_27

59 \* D31 : EXT\_32

60 \* D32 : EXT\_33

61 \* D33 : EXT\_34

62 \* D34 : EXT\_35

63 \* D35 : EXT\_36

64 \* D36 : EXT\_38

65 \* D37 : EXT\_39

66 \* D38 : EXT\_40

67 \* D39 : EXT\_44

68 \* D40 : EXT\_41

69 \* D41 : EXT\_31

70 \* D42 : EXT\_37

71 \* D43 : EXT\_42

72 \* D44 : EXT\_43

73 \* D45 : EXT\_45

74 \* D46 : EXT\_46

75 \* D47 : EXT\_47

76 \* D48 : EXT\_48

77 \* D49 : EXT\_49

78 \* D50 : EXT\_50

79 \* D51 : EXT\_51

80 \*

81 \* UART\_3\_RX : D0

82 \* UART\_3\_TX : D1

83 \* SPI\_3\_CS : D10

84 \* SPI\_3\_MOSI : D11

85 \* SPI\_3\_MISO : D12

86 \* SPI\_3\_SCLK : D13

87 \* I2C\_3\_SDA : D14

88 \* I2C\_3\_SCL : D15

89 \* UART\_4\_RX : D26

90 \* UART\_4\_TX : D30

91 \* SPI\_4\_CS : D36

92 \* SPI\_4\_MOSI : D37

93 \* SPI\_4\_MISO : D38

94 \* SPI\_4\_SCK : D39

95 \* I2C\_4\_SDA : D40

96 \* I2C\_4\_SCL : D41

97 \*

98 \*/

99

100/\* GPIO 0 \*/

[ 101](arm-mps2-pinctrl_8h.md#aad1ef19e8c46127baf5ddb680f4a9c2e)#define UART3\_RXD\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_UART, 0)

[ 102](arm-mps2-pinctrl_8h.md#aab7f8b8584aa06a033aa1e93200eb0d6)#define UART3\_TXD\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_UART, 4)

[ 103](arm-mps2-pinctrl_8h.md#a301bb93777a77d4fcbed8617edbe319a)#define SBCON2\_SCL\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_I2C, 5)

[ 104](arm-mps2-pinctrl_8h.md#a8c2f848c26c691ce333e05fe17c9341d)#define SBCON2\_SDA\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_I2C, 15)

[ 105](arm-mps2-pinctrl_8h.md#ac3801e4481859951369757ac96612165)#define SPI3\_SCK\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 11)

[ 106](arm-mps2-pinctrl_8h.md#ae1f9ab03b508c087a9190d742b67fc2a)#define SPI3\_SS\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 12)

[ 107](arm-mps2-pinctrl_8h.md#a95f2fe6603f5ab5de9c410dfaf87dc52)#define SPI3\_MOSI\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 13)

[ 108](arm-mps2-pinctrl_8h.md#a14c932b34877e7b1f004bdf3edfdcd4b)#define SPI3\_MISO\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 14)

109

110/\* GPIO 1 \*/

[ 111](arm-mps2-pinctrl_8h.md#af8e71afd57806fbe85b504ac68879fa6)#define SPI2\_SS\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 16)

[ 112](arm-mps2-pinctrl_8h.md#af0e38d71c2b6d7cb6f1238e17e8fff6f)#define SPI2\_MISO\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 17)

[ 113](arm-mps2-pinctrl_8h.md#a32eff7bbffdfc00975ff1b5f3281eaa1)#define SPI2\_MOSI\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 18)

[ 114](arm-mps2-pinctrl_8h.md#a6fbdf386063229b64599d3c2071ebffd)#define SPI2\_SCK\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 19)

[ 115](arm-mps2-pinctrl_8h.md#a960b6b4bf5810595c274fab5842189e4)#define UART4\_RXD\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_UART, 26)

[ 116](arm-mps2-pinctrl_8h.md#a8f2f8e4cb191c641dad8dff6c4753e38)#define UART4\_TXD\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_UART, 30)

[ 117](arm-mps2-pinctrl_8h.md#a42708eb48f46a3dd04242b446389057b)#define SBCON3\_SCL\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_I2C, 31)

118

119/\* GPIO 2 \*/

[ 120](arm-mps2-pinctrl_8h.md#a1f600b98990e17441e52f65cc0dabddb)#define SBCON3\_SDA\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_I2C, 41)

[ 121](arm-mps2-pinctrl_8h.md#a525321e1403275e09014f3ff1fa88d78)#define SPI4\_SS\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 38)

[ 122](arm-mps2-pinctrl_8h.md#aa73c8c56e661787cc05b131f86a8478c)#define SPI4\_MOSI\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 39)

[ 123](arm-mps2-pinctrl_8h.md#a9709eee41e54142558c4930f1b034043)#define SPI4\_MISO\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 40)

[ 124](arm-mps2-pinctrl_8h.md#aa48a51e34a517797511e7214ad00b7de)#define SPI4\_SCK\_EXP MPS2\_PINMUX(MPS2\_PINCTRL\_FUNC\_SPI, 44)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [arm-mps2-pinctrl.h](arm-mps2-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
