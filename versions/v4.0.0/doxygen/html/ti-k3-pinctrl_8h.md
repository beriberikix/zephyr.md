---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ti-k3-pinctrl_8h.html
original_path: doxygen/html/ti-k3-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ti-k3-pinctrl.h File Reference

[Go to the source code of this file.](ti-k3-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PULLUDEN\_SHIFT](#a0febfbc566c3728115a03bb7f7dc620e)   16 |
| #define | [PULLTYPESEL\_SHIFT](#ad24bec783f5c84d6e82a34141b0d057a)   17 |
| #define | [RXACTIVE\_SHIFT](#aa96a5ff81411950a5661202b443142ca)   18 |
| #define | [PULL\_DISABLE](#a768319530a87153b9804251bdc3b9e4d)   (1 << [PULLUDEN\_SHIFT](#a0febfbc566c3728115a03bb7f7dc620e)) |
| #define | [PULL\_ENABLE](#acaca8fc3aa06bcd710d33c74ec8bff40)   (0 << [PULLUDEN\_SHIFT](#a0febfbc566c3728115a03bb7f7dc620e)) |
| #define | [PULL\_UP](#aca4f67c0077925f24ea1f6b26e313271)   ((1 << [PULLTYPESEL\_SHIFT](#ad24bec783f5c84d6e82a34141b0d057a)) | [PULL\_ENABLE](#acaca8fc3aa06bcd710d33c74ec8bff40)) |
| #define | [PULL\_DOWN](#ab47362632d6cd744f764880731de5704)   ((0 << [PULLTYPESEL\_SHIFT](#ad24bec783f5c84d6e82a34141b0d057a)) | [PULL\_ENABLE](#acaca8fc3aa06bcd710d33c74ec8bff40)) |
| #define | [INPUT\_ENABLE](#a6ad4c7f924e24241629dc10ed6b433f9)   (1 << [RXACTIVE\_SHIFT](#aa96a5ff81411950a5661202b443142ca)) |
| #define | [INPUT\_DISABLE](#a40984b9ac260aa5f3467e55a91cfff30)   (0 << [RXACTIVE\_SHIFT](#aa96a5ff81411950a5661202b443142ca)) |
| #define | [PIN\_OUTPUT](#a16f6fcf4256a279427eb2c243c9e0bd5)   ([INPUT\_DISABLE](#a40984b9ac260aa5f3467e55a91cfff30) | [PULL\_DISABLE](#a768319530a87153b9804251bdc3b9e4d)) |
| #define | [PIN\_OUTPUT\_PULLUP](#abfd6c5cdc843d33ebddee7b244931fc3)   ([INPUT\_DISABLE](#a40984b9ac260aa5f3467e55a91cfff30) | [PULL\_UP](#aca4f67c0077925f24ea1f6b26e313271)) |
| #define | [PIN\_OUTPUT\_PULLDOWN](#a8c5881bfb4d468fa634c8bec1d68595c)   ([INPUT\_DISABLE](#a40984b9ac260aa5f3467e55a91cfff30) | [PULL\_DOWN](#ab47362632d6cd744f764880731de5704)) |
| #define | [PIN\_INPUT](#a5a94a90bd5b33109a2e3832760bc5da1)   ([INPUT\_ENABLE](#a6ad4c7f924e24241629dc10ed6b433f9) | [PULL\_DISABLE](#a768319530a87153b9804251bdc3b9e4d)) |
| #define | [PIN\_INPUT\_PULLUP](#a06f998fe6be04b6a8d278b150790d436)   ([INPUT\_ENABLE](#a6ad4c7f924e24241629dc10ed6b433f9) | [PULL\_UP](#aca4f67c0077925f24ea1f6b26e313271)) |
| #define | [PIN\_INPUT\_PULLDOWN](#a3ce1576f1da81ea2f6c492b8f8cd5350)   ([INPUT\_ENABLE](#a6ad4c7f924e24241629dc10ed6b433f9) | [PULL\_DOWN](#ab47362632d6cd744f764880731de5704)) |
| #define | [MUX\_MODE\_0](#adf2868df9ec8ecdd15e89b8a33a1fdbc)   0 |
| #define | [MUX\_MODE\_1](#a7efdf57cf0a9ef6847bd3e62b42ab771)   1 |
| #define | [MUX\_MODE\_2](#ac2c88f4a9d2752f06cb925ca4993a35e)   2 |
| #define | [MUX\_MODE\_3](#a018dca77be29b23eface983280b1812f)   3 |
| #define | [MUX\_MODE\_4](#ad0ff0ccc1b0b38c49a842c565aa6c0b8)   4 |
| #define | [MUX\_MODE\_5](#a6192dc972d0c7712a06be2d47205c558)   5 |
| #define | [MUX\_MODE\_6](#a9a5bcfce0779373f2ed0f0dd645a9703)   6 |
| #define | [MUX\_MODE\_7](#a97074809f50f00264fd33793d4d0b647)   7 |
| #define | [MUX\_MODE\_8](#a0c6c56a47585b1fe1233139689c519de)   8 |
| #define | [MUX\_MODE\_9](#aa951dab323d11eb1059ed1f278f7730d)   9 |
| #define | [MUX\_MODE\_10](#aebfc9715ee7edf771cb23da2b0028a11)   10 |
| #define | [MUX\_MODE\_11](#a052beac6cdfccce06bb16f447e54db92)   11 |
| #define | [MUX\_MODE\_12](#a1213893060e171293e0484324a6e20ab)   12 |
| #define | [MUX\_MODE\_13](#aa436ee60756d56a9a5f451cdb0dae3c5)   13 |
| #define | [MUX\_MODE\_14](#afa386486189b7027f7ac93a9e2fa2614)   14 |
| #define | [K3\_PINMUX](#a95cac03e59fecc4cb31762747913dddf)(offset, value, mux\_mode) |

## Macro Definition Documentation

## [◆ ](#a40984b9ac260aa5f3467e55a91cfff30)INPUT\_DISABLE

| #define INPUT\_DISABLE   (0 << [RXACTIVE\_SHIFT](#aa96a5ff81411950a5661202b443142ca)) |
| --- |

## [◆ ](#a6ad4c7f924e24241629dc10ed6b433f9)INPUT\_ENABLE

| #define INPUT\_ENABLE   (1 << [RXACTIVE\_SHIFT](#aa96a5ff81411950a5661202b443142ca)) |
| --- |

## [◆ ](#a95cac03e59fecc4cb31762747913dddf)K3\_PINMUX

| #define K3\_PINMUX | ( |  | *offset*, |
| --- | --- | --- | --- |
|  |  |  | *value*, |
|  |  |  | *mux\_mode* ) |

**Value:**

(((offset) & 0x1fff)) ((value) | (mux\_mode))

## [◆ ](#adf2868df9ec8ecdd15e89b8a33a1fdbc)MUX\_MODE\_0

| #define MUX\_MODE\_0   0 |
| --- |

## [◆ ](#a7efdf57cf0a9ef6847bd3e62b42ab771)MUX\_MODE\_1

| #define MUX\_MODE\_1   1 |
| --- |

## [◆ ](#aebfc9715ee7edf771cb23da2b0028a11)MUX\_MODE\_10

| #define MUX\_MODE\_10   10 |
| --- |

## [◆ ](#a052beac6cdfccce06bb16f447e54db92)MUX\_MODE\_11

| #define MUX\_MODE\_11   11 |
| --- |

## [◆ ](#a1213893060e171293e0484324a6e20ab)MUX\_MODE\_12

| #define MUX\_MODE\_12   12 |
| --- |

## [◆ ](#aa436ee60756d56a9a5f451cdb0dae3c5)MUX\_MODE\_13

| #define MUX\_MODE\_13   13 |
| --- |

## [◆ ](#afa386486189b7027f7ac93a9e2fa2614)MUX\_MODE\_14

| #define MUX\_MODE\_14   14 |
| --- |

## [◆ ](#ac2c88f4a9d2752f06cb925ca4993a35e)MUX\_MODE\_2

| #define MUX\_MODE\_2   2 |
| --- |

## [◆ ](#a018dca77be29b23eface983280b1812f)MUX\_MODE\_3

| #define MUX\_MODE\_3   3 |
| --- |

## [◆ ](#ad0ff0ccc1b0b38c49a842c565aa6c0b8)MUX\_MODE\_4

| #define MUX\_MODE\_4   4 |
| --- |

## [◆ ](#a6192dc972d0c7712a06be2d47205c558)MUX\_MODE\_5

| #define MUX\_MODE\_5   5 |
| --- |

## [◆ ](#a9a5bcfce0779373f2ed0f0dd645a9703)MUX\_MODE\_6

| #define MUX\_MODE\_6   6 |
| --- |

## [◆ ](#a97074809f50f00264fd33793d4d0b647)MUX\_MODE\_7

| #define MUX\_MODE\_7   7 |
| --- |

## [◆ ](#a0c6c56a47585b1fe1233139689c519de)MUX\_MODE\_8

| #define MUX\_MODE\_8   8 |
| --- |

## [◆ ](#aa951dab323d11eb1059ed1f278f7730d)MUX\_MODE\_9

| #define MUX\_MODE\_9   9 |
| --- |

## [◆ ](#a5a94a90bd5b33109a2e3832760bc5da1)PIN\_INPUT

| #define PIN\_INPUT   ([INPUT\_ENABLE](#a6ad4c7f924e24241629dc10ed6b433f9) | [PULL\_DISABLE](#a768319530a87153b9804251bdc3b9e4d)) |
| --- |

## [◆ ](#a3ce1576f1da81ea2f6c492b8f8cd5350)PIN\_INPUT\_PULLDOWN

| #define PIN\_INPUT\_PULLDOWN   ([INPUT\_ENABLE](#a6ad4c7f924e24241629dc10ed6b433f9) | [PULL\_DOWN](#ab47362632d6cd744f764880731de5704)) |
| --- |

## [◆ ](#a06f998fe6be04b6a8d278b150790d436)PIN\_INPUT\_PULLUP

| #define PIN\_INPUT\_PULLUP   ([INPUT\_ENABLE](#a6ad4c7f924e24241629dc10ed6b433f9) | [PULL\_UP](#aca4f67c0077925f24ea1f6b26e313271)) |
| --- |

## [◆ ](#a16f6fcf4256a279427eb2c243c9e0bd5)PIN\_OUTPUT

| #define PIN\_OUTPUT   ([INPUT\_DISABLE](#a40984b9ac260aa5f3467e55a91cfff30) | [PULL\_DISABLE](#a768319530a87153b9804251bdc3b9e4d)) |
| --- |

## [◆ ](#a8c5881bfb4d468fa634c8bec1d68595c)PIN\_OUTPUT\_PULLDOWN

| #define PIN\_OUTPUT\_PULLDOWN   ([INPUT\_DISABLE](#a40984b9ac260aa5f3467e55a91cfff30) | [PULL\_DOWN](#ab47362632d6cd744f764880731de5704)) |
| --- |

## [◆ ](#abfd6c5cdc843d33ebddee7b244931fc3)PIN\_OUTPUT\_PULLUP

| #define PIN\_OUTPUT\_PULLUP   ([INPUT\_DISABLE](#a40984b9ac260aa5f3467e55a91cfff30) | [PULL\_UP](#aca4f67c0077925f24ea1f6b26e313271)) |
| --- |

## [◆ ](#a768319530a87153b9804251bdc3b9e4d)PULL\_DISABLE

| #define PULL\_DISABLE   (1 << [PULLUDEN\_SHIFT](#a0febfbc566c3728115a03bb7f7dc620e)) |
| --- |

## [◆ ](#ab47362632d6cd744f764880731de5704)PULL\_DOWN

| #define PULL\_DOWN   ((0 << [PULLTYPESEL\_SHIFT](#ad24bec783f5c84d6e82a34141b0d057a)) | [PULL\_ENABLE](#acaca8fc3aa06bcd710d33c74ec8bff40)) |
| --- |

## [◆ ](#acaca8fc3aa06bcd710d33c74ec8bff40)PULL\_ENABLE

| #define PULL\_ENABLE   (0 << [PULLUDEN\_SHIFT](#a0febfbc566c3728115a03bb7f7dc620e)) |
| --- |

## [◆ ](#aca4f67c0077925f24ea1f6b26e313271)PULL\_UP

| #define PULL\_UP   ((1 << [PULLTYPESEL\_SHIFT](#ad24bec783f5c84d6e82a34141b0d057a)) | [PULL\_ENABLE](#acaca8fc3aa06bcd710d33c74ec8bff40)) |
| --- |

## [◆ ](#ad24bec783f5c84d6e82a34141b0d057a)PULLTYPESEL\_SHIFT

| #define PULLTYPESEL\_SHIFT   17 |
| --- |

## [◆ ](#a0febfbc566c3728115a03bb7f7dc620e)PULLUDEN\_SHIFT

| #define PULLUDEN\_SHIFT   16 |
| --- |

## [◆ ](#aa96a5ff81411950a5661202b443142ca)RXACTIVE\_SHIFT

| #define RXACTIVE\_SHIFT   18 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ti-k3-pinctrl.h](ti-k3-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
