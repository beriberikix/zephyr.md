---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arm-mps3-pinctrl_8h.html
original_path: doxygen/html/arm-mps3-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm-mps3-pinctrl.h File Reference

[Go to the source code of this file.](arm-mps3-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MPS3\_ALT\_FUNC\_POS](#a92d23b008eed86044d67552ec703f2ab)   0 |
| #define | [MPS3\_ALT\_FUNC\_MASK](#af29520fbd24c4ed2559ff1dcefa9c901)   0x7 |
| #define | [MPS3\_EXP\_NUM\_POS](#a271fc39e2ac01cf6973857666445b92a)   3 |
| #define | [MPS3\_EXP\_NUM\_MASK](#a38ff399b3140635abe0858e73ad02b5a)   0x1F8 |
| #define | [MPS3\_PINCTRL\_FUNC\_UART](#a67c22b434c59a2eee7c6b60e2b70ae59)   0 |
| #define | [MPS3\_PINCTRL\_FUNC\_GPIO](#a89a852a0ee4d66c8031b09f6db24331a)   1 |
| #define | [MPS3\_PINCTRL\_FUNC\_I2C](#a23b4c2379a045e9c16bd53d4c5226252)   2 |
| #define | [MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195)   3 |
| #define | [MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9)   4 |
| #define | [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)(alt\_func, exp\_num) |
| #define | [PMOD1\_IO1\_EXP](#a34c7b3c59e141cc0dbae7e0edc2ad129)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 0) |
| #define | [PMOD1\_IO0\_EXP](#a4424b55dd5454cd7fa120a23cd5df6f4)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 1) |
| #define | [PMOD1\_SS\_EXP](#a02b3cca65f1c7756a3ffe36b7987222b)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 3) |
| #define | [PMOD0\_IO2\_EXP](#a0695f557cb8f855300365e2be11bc9bb)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 7) |
| #define | [PMOD0\_IO3\_EXP](#a585aef742cc326eee64903f1fcef6883)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 8) |
| #define | [PMOD1\_SCK\_EXP](#a91e253309b1e5b615c204836c13900da)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 9) |
| #define | [PMOD0\_SS\_EXP](#a4b78ddad746105930ae289c4afd4d4ca)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 10) |
| #define | [PMOD0\_IO0\_EXP](#a1957ed3aa96ccfb786632620782c0f49)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 11) |
| #define | [PMOD0\_IO1\_EXP](#a4284a74f7ee7d951f316a5fa721f5b4c)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 12) |
| #define | [PMOD0\_SCK\_EXP](#a9115e37a39f5044fe5a31dff174fc773)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 13) |
| #define | [PMOD1\_IO3\_EXP](#a8056404e55f29ba58bbd4ea106bccbe0)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 14) |
| #define | [PMOD1\_IO2\_EXP](#a882a514f7c45b8969b030d3e715fd6ab)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 15) |
| #define | [UART3\_RXD\_EXP](#aad1ef19e8c46127baf5ddb680f4a9c2e)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_UART](#a67c22b434c59a2eee7c6b60e2b70ae59), 0) |
| #define | [UART3\_TXD\_EXP](#aab7f8b8584aa06a033aa1e93200eb0d6)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_UART](#a67c22b434c59a2eee7c6b60e2b70ae59), 1) |
| #define | [SPI3\_SS\_EXP](#ae1f9ab03b508c087a9190d742b67fc2a)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 10) |
| #define | [SPI3\_MOSI\_EXP](#a95f2fe6603f5ab5de9c410dfaf87dc52)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 11) |
| #define | [SPI3\_MISO\_EXP](#a14c932b34877e7b1f004bdf3edfdcd4b)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 12) |
| #define | [SPI3\_SCK\_EXP](#ac3801e4481859951369757ac96612165)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 13) |
| #define | [SBCON2\_SDA\_EXP](#a8c2f848c26c691ce333e05fe17c9341d)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_I2C](#a23b4c2379a045e9c16bd53d4c5226252), 14) |
| #define | [SBCON2\_SCL\_EXP](#a301bb93777a77d4fcbed8617edbe319a)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_I2C](#a23b4c2379a045e9c16bd53d4c5226252), 15) |
| #define | [UART4\_RXD\_EXP](#a960b6b4bf5810595c274fab5842189e4)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_UART](#a67c22b434c59a2eee7c6b60e2b70ae59), 16) |
| #define | [UART4\_TXD\_EXP](#a8f2f8e4cb191c641dad8dff6c4753e38)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_UART](#a67c22b434c59a2eee7c6b60e2b70ae59), 17) |
| #define | [SPI4\_SS\_EXP](#a525321e1403275e09014f3ff1fa88d78)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 26) |
| #define | [SPI4\_MOSI\_EXP](#aa73c8c56e661787cc05b131f86a8478c)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 27) |
| #define | [SPI4\_MISO\_EXP](#a9709eee41e54142558c4930f1b034043)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 28) |
| #define | [SPI4\_SCK\_EXP](#aa48a51e34a517797511e7214ad00b7de)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 29) |
| #define | [SBCON3\_SDA\_EXP](#a1f600b98990e17441e52f65cc0dabddb)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_I2C](#a23b4c2379a045e9c16bd53d4c5226252), 30) |
| #define | [SBCON3\_SCL\_EXP](#a42708eb48f46a3dd04242b446389057b)   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_I2C](#a23b4c2379a045e9c16bd53d4c5226252), 31) |

## Macro Definition Documentation

## [◆ ](#af29520fbd24c4ed2559ff1dcefa9c901)MPS3\_ALT\_FUNC\_MASK

| #define MPS3\_ALT\_FUNC\_MASK   0x7 |
| --- |

## [◆ ](#a92d23b008eed86044d67552ec703f2ab)MPS3\_ALT\_FUNC\_POS

| #define MPS3\_ALT\_FUNC\_POS   0 |
| --- |

## [◆ ](#a38ff399b3140635abe0858e73ad02b5a)MPS3\_EXP\_NUM\_MASK

| #define MPS3\_EXP\_NUM\_MASK   0x1F8 |
| --- |

## [◆ ](#a271fc39e2ac01cf6973857666445b92a)MPS3\_EXP\_NUM\_POS

| #define MPS3\_EXP\_NUM\_POS   3 |
| --- |

## [◆ ](#a89a852a0ee4d66c8031b09f6db24331a)MPS3\_PINCTRL\_FUNC\_GPIO

| #define MPS3\_PINCTRL\_FUNC\_GPIO   1 |
| --- |

## [◆ ](#a23b4c2379a045e9c16bd53d4c5226252)MPS3\_PINCTRL\_FUNC\_I2C

| #define MPS3\_PINCTRL\_FUNC\_I2C   2 |
| --- |

## [◆ ](#a7ba2947efe4589c519c8a4531def43a9)MPS3\_PINCTRL\_FUNC\_PMOD

| #define MPS3\_PINCTRL\_FUNC\_PMOD   4 |
| --- |

## [◆ ](#a9a5e1735229d515e14606ba2c5347195)MPS3\_PINCTRL\_FUNC\_SPI

| #define MPS3\_PINCTRL\_FUNC\_SPI   3 |
| --- |

## [◆ ](#a67c22b434c59a2eee7c6b60e2b70ae59)MPS3\_PINCTRL\_FUNC\_UART

| #define MPS3\_PINCTRL\_FUNC\_UART   0 |
| --- |

## [◆ ](#ad10638589bc1eaa0bc10ef0529cb816c)MPS3\_PINMUX

| #define MPS3\_PINMUX | ( |  | *alt\_func*, |
| --- | --- | --- | --- |
|  |  |  | *exp\_num* ) |

**Value:**

(exp\_num << [MPS3\_EXP\_NUM\_POS](#a271fc39e2ac01cf6973857666445b92a) | \

alt\_func << [MPS3\_ALT\_FUNC\_POS](#a92d23b008eed86044d67552ec703f2ab))

[MPS3\_EXP\_NUM\_POS](#a271fc39e2ac01cf6973857666445b92a)

#define MPS3\_EXP\_NUM\_POS

**Definition** arm-mps3-pinctrl.h:10

[MPS3\_ALT\_FUNC\_POS](#a92d23b008eed86044d67552ec703f2ab)

#define MPS3\_ALT\_FUNC\_POS

**Definition** arm-mps3-pinctrl.h:7

## [◆ ](#a1957ed3aa96ccfb786632620782c0f49)PMOD0\_IO0\_EXP

| #define PMOD0\_IO0\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 11) |
| --- |

## [◆ ](#a4284a74f7ee7d951f316a5fa721f5b4c)PMOD0\_IO1\_EXP

| #define PMOD0\_IO1\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 12) |
| --- |

## [◆ ](#a0695f557cb8f855300365e2be11bc9bb)PMOD0\_IO2\_EXP

| #define PMOD0\_IO2\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 7) |
| --- |

## [◆ ](#a585aef742cc326eee64903f1fcef6883)PMOD0\_IO3\_EXP

| #define PMOD0\_IO3\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 8) |
| --- |

## [◆ ](#a9115e37a39f5044fe5a31dff174fc773)PMOD0\_SCK\_EXP

| #define PMOD0\_SCK\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 13) |
| --- |

## [◆ ](#a4b78ddad746105930ae289c4afd4d4ca)PMOD0\_SS\_EXP

| #define PMOD0\_SS\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 10) |
| --- |

## [◆ ](#a4424b55dd5454cd7fa120a23cd5df6f4)PMOD1\_IO0\_EXP

| #define PMOD1\_IO0\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 1) |
| --- |

## [◆ ](#a34c7b3c59e141cc0dbae7e0edc2ad129)PMOD1\_IO1\_EXP

| #define PMOD1\_IO1\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 0) |
| --- |

## [◆ ](#a882a514f7c45b8969b030d3e715fd6ab)PMOD1\_IO2\_EXP

| #define PMOD1\_IO2\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 15) |
| --- |

## [◆ ](#a8056404e55f29ba58bbd4ea106bccbe0)PMOD1\_IO3\_EXP

| #define PMOD1\_IO3\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 14) |
| --- |

## [◆ ](#a91e253309b1e5b615c204836c13900da)PMOD1\_SCK\_EXP

| #define PMOD1\_SCK\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 9) |
| --- |

## [◆ ](#a02b3cca65f1c7756a3ffe36b7987222b)PMOD1\_SS\_EXP

| #define PMOD1\_SS\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_PMOD](#a7ba2947efe4589c519c8a4531def43a9), 3) |
| --- |

## [◆ ](#a301bb93777a77d4fcbed8617edbe319a)SBCON2\_SCL\_EXP

| #define SBCON2\_SCL\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_I2C](#a23b4c2379a045e9c16bd53d4c5226252), 15) |
| --- |

## [◆ ](#a8c2f848c26c691ce333e05fe17c9341d)SBCON2\_SDA\_EXP

| #define SBCON2\_SDA\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_I2C](#a23b4c2379a045e9c16bd53d4c5226252), 14) |
| --- |

## [◆ ](#a42708eb48f46a3dd04242b446389057b)SBCON3\_SCL\_EXP

| #define SBCON3\_SCL\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_I2C](#a23b4c2379a045e9c16bd53d4c5226252), 31) |
| --- |

## [◆ ](#a1f600b98990e17441e52f65cc0dabddb)SBCON3\_SDA\_EXP

| #define SBCON3\_SDA\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_I2C](#a23b4c2379a045e9c16bd53d4c5226252), 30) |
| --- |

## [◆ ](#a14c932b34877e7b1f004bdf3edfdcd4b)SPI3\_MISO\_EXP

| #define SPI3\_MISO\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 12) |
| --- |

## [◆ ](#a95f2fe6603f5ab5de9c410dfaf87dc52)SPI3\_MOSI\_EXP

| #define SPI3\_MOSI\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 11) |
| --- |

## [◆ ](#ac3801e4481859951369757ac96612165)SPI3\_SCK\_EXP

| #define SPI3\_SCK\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 13) |
| --- |

## [◆ ](#ae1f9ab03b508c087a9190d742b67fc2a)SPI3\_SS\_EXP

| #define SPI3\_SS\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 10) |
| --- |

## [◆ ](#a9709eee41e54142558c4930f1b034043)SPI4\_MISO\_EXP

| #define SPI4\_MISO\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 28) |
| --- |

## [◆ ](#aa73c8c56e661787cc05b131f86a8478c)SPI4\_MOSI\_EXP

| #define SPI4\_MOSI\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 27) |
| --- |

## [◆ ](#aa48a51e34a517797511e7214ad00b7de)SPI4\_SCK\_EXP

| #define SPI4\_SCK\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 29) |
| --- |

## [◆ ](#a525321e1403275e09014f3ff1fa88d78)SPI4\_SS\_EXP

| #define SPI4\_SS\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_SPI](#a9a5e1735229d515e14606ba2c5347195), 26) |
| --- |

## [◆ ](#aad1ef19e8c46127baf5ddb680f4a9c2e)UART3\_RXD\_EXP

| #define UART3\_RXD\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_UART](#a67c22b434c59a2eee7c6b60e2b70ae59), 0) |
| --- |

## [◆ ](#aab7f8b8584aa06a033aa1e93200eb0d6)UART3\_TXD\_EXP

| #define UART3\_TXD\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_UART](#a67c22b434c59a2eee7c6b60e2b70ae59), 1) |
| --- |

## [◆ ](#a960b6b4bf5810595c274fab5842189e4)UART4\_RXD\_EXP

| #define UART4\_RXD\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_UART](#a67c22b434c59a2eee7c6b60e2b70ae59), 16) |
| --- |

## [◆ ](#a8f2f8e4cb191c641dad8dff6c4753e38)UART4\_TXD\_EXP

| #define UART4\_TXD\_EXP   [MPS3\_PINMUX](#ad10638589bc1eaa0bc10ef0529cb816c)([MPS3\_PINCTRL\_FUNC\_UART](#a67c22b434c59a2eee7c6b60e2b70ae59), 17) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [arm-mps3-pinctrl.h](arm-mps3-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
