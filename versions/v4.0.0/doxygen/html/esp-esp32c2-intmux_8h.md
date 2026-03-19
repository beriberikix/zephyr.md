---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/esp-esp32c2-intmux_8h.html
original_path: doxygen/html/esp-esp32c2-intmux_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp-esp32c2-intmux.h File Reference

[Go to the source code of this file.](esp-esp32c2-intmux_8h_source.md)

| Macros | |
| --- | --- |
| #define | [WIFI\_MAC\_INTR\_SOURCE](#ad000d08efc3e8a5fc56da537973a5cb8)   0 |
| #define | [WIFI\_MAC\_NMI\_SOURCE](#abfc935ef2963ee54b6a1f1279b4887ff)   1 |
| #define | [WIFI\_PWR\_INTR\_SOURCE](#af3cef5f23f39a396dec2a356f395ef69)   2 |
| #define | [WIFI\_BB\_INTR\_SOURCE](#a5383f7fa77bc12a8301c54e0dfb66306)   3 |
| #define | [BT\_MAC\_INTR\_SOURCE](#a0b48425e316b45db6f105daa6f2a0cff)   4 |
| #define | [BT\_BB\_INTR\_SOURCE](#aca3a7357f242a4e91269736de6545470)   5 |
| #define | [BT\_BB\_NMI\_SOURCE](#ab404d2ab995f39616675330f6462dd19)   6 |
| #define | [LP\_TIMER\_SOURCE](#a2e2ebcd69706fcd8908616ba9d2eadee)   7 |
| #define | [COEX\_SOURCE](#a994eca8b87e9db761ea2a93786c201df)   8 |
| #define | [BLE\_TIMER\_SOURCE](#aef8edd6dcae7c2f3e07c89dbe3450a1c)   9 |
| #define | [BLE\_SEC\_SOURCE](#a30434b162fa1be66196eb0eb2aae4521)   10 |
| #define | [I2C\_MASTER\_SOURCE](#a8b38a0acf3511d0de89607d7eac8f537)   11 |
| #define | [APB\_CTRL\_INTR\_SOURCE](#ab2acf6e0b0eb1f7ea85f0910f90326dc)   12 |
| #define | [GPIO\_INTR\_SOURCE](#a64020d7c1f6557ef6da375f12acf68de)   13 |
| #define | [GPIO\_NMI\_SOURCE](#a23e7de652ab586c903ec999aa8e77e4e)   14 |
| #define | [SPI1\_INTR\_SOURCE](#a5779abc3d34c94cfad763d9ababebb9f)   15 |
| #define | [SPI2\_INTR\_SOURCE](#ac5d10660472f10fae0d0511f254b696d)   16 |
| #define | [UART0\_INTR\_SOURCE](#af4569e6b552e35100134e167cf11c7da)   17 |
| #define | [UART1\_INTR\_SOURCE](#ad6f7d29b71a32716058033727bd01dc2)   18 |
| #define | [LEDC\_INTR\_SOURCE](#a296f3d252d30615dbaea32d61cba9214)   19 |
| #define | [EFUSE\_INTR\_SOURCE](#aaf244ea4b63d912e0ce8d59795c79f9d)   20 |
| #define | [RTC\_CORE\_INTR\_SOURCE](#a80d2efc475574efe9250d0048a8a8c12)   21 |
| #define | [I2C\_EXT0\_INTR\_SOURCE](#a7a706aa628e14e55247d20c9853d76a9)   22 |
| #define | [TG0\_T0\_LEVEL\_INTR\_SOURCE](#a22bf10410f0b99b9fe398accf66c51b1)   23 |
| #define | [TG0\_WDT\_LEVEL\_INTR\_SOURCE](#afc23d5890e9c8029e7d417291193a559)   24 |
| #define | [CACHE\_IA\_INTR\_SOURCE](#abc71e0e6d2e6ea7fc39d17297753e72e)   25 |
| #define | [SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE](#a4cb07c15412c22b4939bb5a1e782f6e7)   26 |
| #define | [SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE](#a4ae5acb4be5a37cc87deb29ca61c8034)   27 |
| #define | [SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE](#a3c07aba15f9a2e9bc4a97031a241b512)   28 |
| #define | [SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE](#a36c488ff1605277f2772b1f80552f6ac)   29 |
| #define | [ICACHE\_PRELOAD0\_INTR\_SOURCE](#a83a3ce01a7cc1f3d4095d260f96705d1)   30 |
| #define | [ICACHE\_SYNC0\_INTR\_SOURCE](#ae62a038d99a1fbd095213f05adfd8f0f)   31 |
| #define | [APB\_ADC\_INTR\_SOURCE](#a68b408eb63057838c64c51718c5b1f7f)   32 |
| #define | [DMA\_CH0\_INTR\_SOURCE](#a25d5f4b9fe34b025f0d780e9bafe9d96)   33 |
| #define | [SHA\_INTR\_SOURCE](#a59f92ba6a2f4b3fa9454558f37ff3e24)   34 |
| #define | [ECC\_INTR\_SOURCE](#aa471b47ba3f4e7a17dac9702e250acf4)   35 |
| #define | [FROM\_CPU\_INTR0\_SOURCE](#a47c9d4be8d21b6f389993db5dbe2883d)   36 |
| #define | [FROM\_CPU\_INTR1\_SOURCE](#a2f704a24d6d56f2e13aed56e86e8fb55)   37 |
| #define | [FROM\_CPU\_INTR2\_SOURCE](#a470d4f804a7ddb5d107f1cafe8f19308)   38 |
| #define | [FROM\_CPU\_INTR3\_SOURCE](#a0b8897c96de3f23e794440ef2ef2f523)   39 |
| #define | [ASSIST\_DEBUG\_INTR\_SOURCE](#ab627766f8e6b851882c42596d7df540c)   40 |
| #define | [CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE](#a83166cdc662aeb9d1de9c9f0d3e2c330)   41 |
| #define | [CACHE\_CORE0\_ACS\_INTR\_SOURCE](#acea509fed0c77dfdb5e0f0ea7b5826af)   42 |
| #define | [IRQ\_DEFAULT\_PRIORITY](#a2dbeaa0c017cdff0982b381cc96f0a6c)   3 |
| #define | [ESP\_INTR\_FLAG\_SHARED](#afc7bfcea2e621d81336ea6dd23310363)   (1<<8) /\* Interrupt can be shared between ISRs \*/ |

## Macro Definition Documentation

## [◆ ](#a68b408eb63057838c64c51718c5b1f7f)APB\_ADC\_INTR\_SOURCE

| #define APB\_ADC\_INTR\_SOURCE   32 |
| --- |

## [◆ ](#ab2acf6e0b0eb1f7ea85f0910f90326dc)APB\_CTRL\_INTR\_SOURCE

| #define APB\_CTRL\_INTR\_SOURCE   12 |
| --- |

## [◆ ](#ab627766f8e6b851882c42596d7df540c)ASSIST\_DEBUG\_INTR\_SOURCE

| #define ASSIST\_DEBUG\_INTR\_SOURCE   40 |
| --- |

## [◆ ](#a30434b162fa1be66196eb0eb2aae4521)BLE\_SEC\_SOURCE

| #define BLE\_SEC\_SOURCE   10 |
| --- |

## [◆ ](#aef8edd6dcae7c2f3e07c89dbe3450a1c)BLE\_TIMER\_SOURCE

| #define BLE\_TIMER\_SOURCE   9 |
| --- |

## [◆ ](#aca3a7357f242a4e91269736de6545470)BT\_BB\_INTR\_SOURCE

| #define BT\_BB\_INTR\_SOURCE   5 |
| --- |

## [◆ ](#ab404d2ab995f39616675330f6462dd19)BT\_BB\_NMI\_SOURCE

| #define BT\_BB\_NMI\_SOURCE   6 |
| --- |

## [◆ ](#a0b48425e316b45db6f105daa6f2a0cff)BT\_MAC\_INTR\_SOURCE

| #define BT\_MAC\_INTR\_SOURCE   4 |
| --- |

## [◆ ](#acea509fed0c77dfdb5e0f0ea7b5826af)CACHE\_CORE0\_ACS\_INTR\_SOURCE

| #define CACHE\_CORE0\_ACS\_INTR\_SOURCE   42 |
| --- |

## [◆ ](#abc71e0e6d2e6ea7fc39d17297753e72e)CACHE\_IA\_INTR\_SOURCE

| #define CACHE\_IA\_INTR\_SOURCE   25 |
| --- |

## [◆ ](#a994eca8b87e9db761ea2a93786c201df)COEX\_SOURCE

| #define COEX\_SOURCE   8 |
| --- |

## [◆ ](#a83166cdc662aeb9d1de9c9f0d3e2c330)CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE

| #define CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE   41 |
| --- |

## [◆ ](#a25d5f4b9fe34b025f0d780e9bafe9d96)DMA\_CH0\_INTR\_SOURCE

| #define DMA\_CH0\_INTR\_SOURCE   33 |
| --- |

## [◆ ](#aa471b47ba3f4e7a17dac9702e250acf4)ECC\_INTR\_SOURCE

| #define ECC\_INTR\_SOURCE   35 |
| --- |

## [◆ ](#aaf244ea4b63d912e0ce8d59795c79f9d)EFUSE\_INTR\_SOURCE

| #define EFUSE\_INTR\_SOURCE   20 |
| --- |

## [◆ ](#afc7bfcea2e621d81336ea6dd23310363)ESP\_INTR\_FLAG\_SHARED

| #define ESP\_INTR\_FLAG\_SHARED   (1<<8) /\* Interrupt can be shared between ISRs \*/ |
| --- |

## [◆ ](#a47c9d4be8d21b6f389993db5dbe2883d)FROM\_CPU\_INTR0\_SOURCE

| #define FROM\_CPU\_INTR0\_SOURCE   36 |
| --- |

## [◆ ](#a2f704a24d6d56f2e13aed56e86e8fb55)FROM\_CPU\_INTR1\_SOURCE

| #define FROM\_CPU\_INTR1\_SOURCE   37 |
| --- |

## [◆ ](#a470d4f804a7ddb5d107f1cafe8f19308)FROM\_CPU\_INTR2\_SOURCE

| #define FROM\_CPU\_INTR2\_SOURCE   38 |
| --- |

## [◆ ](#a0b8897c96de3f23e794440ef2ef2f523)FROM\_CPU\_INTR3\_SOURCE

| #define FROM\_CPU\_INTR3\_SOURCE   39 |
| --- |

## [◆ ](#a64020d7c1f6557ef6da375f12acf68de)GPIO\_INTR\_SOURCE

| #define GPIO\_INTR\_SOURCE   13 |
| --- |

## [◆ ](#a23e7de652ab586c903ec999aa8e77e4e)GPIO\_NMI\_SOURCE

| #define GPIO\_NMI\_SOURCE   14 |
| --- |

## [◆ ](#a7a706aa628e14e55247d20c9853d76a9)I2C\_EXT0\_INTR\_SOURCE

| #define I2C\_EXT0\_INTR\_SOURCE   22 |
| --- |

## [◆ ](#a8b38a0acf3511d0de89607d7eac8f537)I2C\_MASTER\_SOURCE

| #define I2C\_MASTER\_SOURCE   11 |
| --- |

## [◆ ](#a83a3ce01a7cc1f3d4095d260f96705d1)ICACHE\_PRELOAD0\_INTR\_SOURCE

| #define ICACHE\_PRELOAD0\_INTR\_SOURCE   30 |
| --- |

## [◆ ](#ae62a038d99a1fbd095213f05adfd8f0f)ICACHE\_SYNC0\_INTR\_SOURCE

| #define ICACHE\_SYNC0\_INTR\_SOURCE   31 |
| --- |

## [◆ ](#a2dbeaa0c017cdff0982b381cc96f0a6c)IRQ\_DEFAULT\_PRIORITY

| #define IRQ\_DEFAULT\_PRIORITY   3 |
| --- |

## [◆ ](#a296f3d252d30615dbaea32d61cba9214)LEDC\_INTR\_SOURCE

| #define LEDC\_INTR\_SOURCE   19 |
| --- |

## [◆ ](#a2e2ebcd69706fcd8908616ba9d2eadee)LP\_TIMER\_SOURCE

| #define LP\_TIMER\_SOURCE   7 |
| --- |

## [◆ ](#a80d2efc475574efe9250d0048a8a8c12)RTC\_CORE\_INTR\_SOURCE

| #define RTC\_CORE\_INTR\_SOURCE   21 |
| --- |

## [◆ ](#a59f92ba6a2f4b3fa9454558f37ff3e24)SHA\_INTR\_SOURCE

| #define SHA\_INTR\_SOURCE   34 |
| --- |

## [◆ ](#a5779abc3d34c94cfad763d9ababebb9f)SPI1\_INTR\_SOURCE

| #define SPI1\_INTR\_SOURCE   15 |
| --- |

## [◆ ](#ac5d10660472f10fae0d0511f254b696d)SPI2\_INTR\_SOURCE

| #define SPI2\_INTR\_SOURCE   16 |
| --- |

## [◆ ](#a36c488ff1605277f2772b1f80552f6ac)SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE

| #define SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE   29 |
| --- |

## [◆ ](#a4cb07c15412c22b4939bb5a1e782f6e7)SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE   26 |
| --- |

## [◆ ](#a4ae5acb4be5a37cc87deb29ca61c8034)SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE   27 |
| --- |

## [◆ ](#a3c07aba15f9a2e9bc4a97031a241b512)SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE   28 |
| --- |

## [◆ ](#a22bf10410f0b99b9fe398accf66c51b1)TG0\_T0\_LEVEL\_INTR\_SOURCE

| #define TG0\_T0\_LEVEL\_INTR\_SOURCE   23 |
| --- |

## [◆ ](#afc23d5890e9c8029e7d417291193a559)TG0\_WDT\_LEVEL\_INTR\_SOURCE

| #define TG0\_WDT\_LEVEL\_INTR\_SOURCE   24 |
| --- |

## [◆ ](#af4569e6b552e35100134e167cf11c7da)UART0\_INTR\_SOURCE

| #define UART0\_INTR\_SOURCE   17 |
| --- |

## [◆ ](#ad6f7d29b71a32716058033727bd01dc2)UART1\_INTR\_SOURCE

| #define UART1\_INTR\_SOURCE   18 |
| --- |

## [◆ ](#a5383f7fa77bc12a8301c54e0dfb66306)WIFI\_BB\_INTR\_SOURCE

| #define WIFI\_BB\_INTR\_SOURCE   3 |
| --- |

## [◆ ](#ad000d08efc3e8a5fc56da537973a5cb8)WIFI\_MAC\_INTR\_SOURCE

| #define WIFI\_MAC\_INTR\_SOURCE   0 |
| --- |

## [◆ ](#abfc935ef2963ee54b6a1f1279b4887ff)WIFI\_MAC\_NMI\_SOURCE

| #define WIFI\_MAC\_NMI\_SOURCE   1 |
| --- |

## [◆ ](#af3cef5f23f39a396dec2a356f395ef69)WIFI\_PWR\_INTR\_SOURCE

| #define WIFI\_PWR\_INTR\_SOURCE   2 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [esp-esp32c2-intmux.h](esp-esp32c2-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
