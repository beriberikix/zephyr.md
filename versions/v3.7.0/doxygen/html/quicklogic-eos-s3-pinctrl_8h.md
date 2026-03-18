---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/quicklogic-eos-s3-pinctrl_8h.html
original_path: doxygen/html/quicklogic-eos-s3-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

quicklogic-eos-s3-pinctrl.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](quicklogic-eos-s3-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IO\_MUX\_REG\_MAX\_OFFSET](#a42e8d57fbc0ce7fea27c8e5487008c38)   107 |
| #define | [IO\_MUX\_MAX\_PAD\_NR](#ab345030af28df16546437382d1c935a9)   45 |
| #define | [FUNC\_SEL\_UART\_RX](#a76393e634c1e77ca47d7106c27889936)   (77 << 13) |
| #define | [QUICKLOGIC\_EOS\_S3\_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)(pin, fun) |
| #define | [UART\_TX\_PAD44](#ac3cce2e16d9678b674a6b73e9675cb56)   [QUICKLOGIC\_EOS\_S3\_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)(44, 0x3) |
| #define | [UART\_RX\_PAD45](#a4c89eee6f06d8e99b1d042b385622cae)   [QUICKLOGIC\_EOS\_S3\_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)(45, [FUNC\_SEL\_UART\_RX](#a76393e634c1e77ca47d7106c27889936) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2)) |
| #define | [USB\_PU\_CTRL\_PAD23](#ac8ede25f5a027513c1815e1ecd59f8b7)   [QUICKLOGIC\_EOS\_S3\_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)(23, 0x0) |
| #define | [USB\_DN\_PAD28](#ac9f2cd78de5e93b13ac7683e1439b21d)   [QUICKLOGIC\_EOS\_S3\_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)(28, 0x0) |
| #define | [USB\_DP\_PAD31](#ac814f848b3db7d98dada168dad9e0b74)   [QUICKLOGIC\_EOS\_S3\_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)(31, 0x0) |

## Macro Definition Documentation

## [◆ ](#a76393e634c1e77ca47d7106c27889936)FUNC\_SEL\_UART\_RX

| #define FUNC\_SEL\_UART\_RX   (77 << 13) |
| --- |

## [◆ ](#ab345030af28df16546437382d1c935a9)IO\_MUX\_MAX\_PAD\_NR

| #define IO\_MUX\_MAX\_PAD\_NR   45 |
| --- |

## [◆ ](#a42e8d57fbc0ce7fea27c8e5487008c38)IO\_MUX\_REG\_MAX\_OFFSET

| #define IO\_MUX\_REG\_MAX\_OFFSET   107 |
| --- |

## [◆ ](#a32684ea1b082834fcadc1d17ab2f6ea7)QUICKLOGIC\_EOS\_S3\_PINMUX

| #define QUICKLOGIC\_EOS\_S3\_PINMUX | ( |  | *pin*, |
| --- | --- | --- | --- |
|  |  |  | *fun* ) |

**Value:**

(pin) (fun)

## [◆ ](#a4c89eee6f06d8e99b1d042b385622cae)UART\_RX\_PAD45

| #define UART\_RX\_PAD45   [QUICKLOGIC\_EOS\_S3\_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)(45, [FUNC\_SEL\_UART\_RX](#a76393e634c1e77ca47d7106c27889936) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2)) |
| --- |

## [◆ ](#ac3cce2e16d9678b674a6b73e9675cb56)UART\_TX\_PAD44

| #define UART\_TX\_PAD44   [QUICKLOGIC\_EOS\_S3\_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)(44, 0x3) |
| --- |

## [◆ ](#ac9f2cd78de5e93b13ac7683e1439b21d)USB\_DN\_PAD28

| #define USB\_DN\_PAD28   [QUICKLOGIC\_EOS\_S3\_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)(28, 0x0) |
| --- |

## [◆ ](#ac814f848b3db7d98dada168dad9e0b74)USB\_DP\_PAD31

| #define USB\_DP\_PAD31   [QUICKLOGIC\_EOS\_S3\_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)(31, 0x0) |
| --- |

## [◆ ](#ac8ede25f5a027513c1815e1ecd59f8b7)USB\_PU\_CTRL\_PAD23

| #define USB\_PU\_CTRL\_PAD23   [QUICKLOGIC\_EOS\_S3\_PINMUX](#a32684ea1b082834fcadc1d17ab2f6ea7)(23, 0x0) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [quicklogic-eos-s3-pinctrl.h](quicklogic-eos-s3-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
