---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp-esp32c3-intmux_8h.html
original_path: doxygen/html/esp-esp32c3-intmux_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp-esp32c3-intmux.h File Reference

[Go to the source code of this file.](esp-esp32c3-intmux_8h_source.md)

| Macros | |
| --- | --- |
| #define | [WIFI\_MAC\_INTR\_SOURCE](#ad000d08efc3e8a5fc56da537973a5cb8)   0 |
| #define | [WIFI\_MAC\_NMI\_SOURCE](#abfc935ef2963ee54b6a1f1279b4887ff)   1 |
| #define | [WIFI\_PWR\_INTR\_SOURCE](#af3cef5f23f39a396dec2a356f395ef69)   2 |
| #define | [WIFI\_BB\_INTR\_SOURCE](#a5383f7fa77bc12a8301c54e0dfb66306)   3 |
| #define | [BT\_MAC\_INTR\_SOURCE](#a0b48425e316b45db6f105daa6f2a0cff)   4 |
| #define | [BT\_BB\_INTR\_SOURCE](#aca3a7357f242a4e91269736de6545470)   5 |
| #define | [BT\_BB\_NMI\_SOURCE](#ab404d2ab995f39616675330f6462dd19)   6 |
| #define | [RWBT\_INTR\_SOURCE](#a14017a5bb9744f9c32138dbdcc09a786)   7 |
| #define | [RWBLE\_INTR\_SOURCE](#a8cf7f44d512a2c0b215397ae4c37a4f1)   8 |
| #define | [RWBT\_NMI\_SOURCE](#a445a79e81929641c372257f4018127f6)   9 |
| #define | [RWBLE\_NMI\_SOURCE](#a3b9cef18112f398bd4ada544f3e2b5a0)   10 |
| #define | [I2C\_MASTER\_SOURCE](#a8b38a0acf3511d0de89607d7eac8f537)   11 |
| #define | [SLC0\_INTR\_SOURCE](#a24b7d137ebb32c58d60d5f84a3ce67db)   12 |
| #define | [SLC1\_INTR\_SOURCE](#a8d8c7fb4a7206356ef7c7b41df4c1b7b)   13 |
| #define | [APB\_CTRL\_INTR\_SOURCE](#ab2acf6e0b0eb1f7ea85f0910f90326dc)   14 |
| #define | [UHCI0\_INTR\_SOURCE](#aa714005c0707aaf1ba5b4a033bcb8f81)   15 |
| #define | [GPIO\_INTR\_SOURCE](#a64020d7c1f6557ef6da375f12acf68de)   16 |
| #define | [GPIO\_NMI\_SOURCE](#a23e7de652ab586c903ec999aa8e77e4e)   17 |
| #define | [SPI1\_INTR\_SOURCE](#a5779abc3d34c94cfad763d9ababebb9f)   18 |
| #define | [SPI2\_INTR\_SOURCE](#ac5d10660472f10fae0d0511f254b696d)   19 |
| #define | [I2S1\_INTR\_SOURCE](#a3b0877aad4fc7995be0cfb71fabb13a6)   20 |
| #define | [UART0\_INTR\_SOURCE](#af4569e6b552e35100134e167cf11c7da)   21 |
| #define | [UART1\_INTR\_SOURCE](#ad6f7d29b71a32716058033727bd01dc2)   22 |
| #define | [LEDC\_INTR\_SOURCE](#a296f3d252d30615dbaea32d61cba9214)   23 |
| #define | [EFUSE\_INTR\_SOURCE](#aaf244ea4b63d912e0ce8d59795c79f9d)   24 |
| #define | [TWAI\_INTR\_SOURCE](#a3a56673ee10a809fb2e75065d84b6f8e)   25 |
| #define | [USB\_INTR\_SOURCE](#a7a020da508049560356d36ab9607bca9)   26 |
| #define | [RTC\_CORE\_INTR\_SOURCE](#a80d2efc475574efe9250d0048a8a8c12)   27 |
| #define | [RMT\_INTR\_SOURCE](#ac6d02a2b0f009553a9e52e7842fa959d)   28 |
| #define | [I2C\_EXT0\_INTR\_SOURCE](#a7a706aa628e14e55247d20c9853d76a9)   29 |
| #define | [TIMER1\_INTR\_SOURCE](#a9f5fed8c34c9b971830ab3e083316271)   30 |
| #define | [TIMER2\_INTR\_SOURCE](#a792de801f5e8339f61a381172782ee06)   31 |
| #define | [TG0\_T0\_LEVEL\_INTR\_SOURCE](#a22bf10410f0b99b9fe398accf66c51b1)   32 |
| #define | [TG0\_WDT\_LEVEL\_INTR\_SOURCE](#afc23d5890e9c8029e7d417291193a559)   33 |
| #define | [TG1\_T0\_LEVEL\_INTR\_SOURCE](#aee34beaabe47713742eb7633bd8430e3)   34 |
| #define | [TG1\_WDT\_LEVEL\_INTR\_SOURCE](#a68616a67d062b7e57dbe6dd59151b85c)   35 |
| #define | [CACHE\_IA\_INTR\_SOURCE](#abc71e0e6d2e6ea7fc39d17297753e72e)   36 |
| #define | [SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE](#a4cb07c15412c22b4939bb5a1e782f6e7)   37 |
| #define | [SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE](#a4ae5acb4be5a37cc87deb29ca61c8034)   38 |
| #define | [SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE](#a3c07aba15f9a2e9bc4a97031a241b512)   39 |
| #define | [SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE](#a36c488ff1605277f2772b1f80552f6ac)   40 |
| #define | [ICACHE\_PRELOAD0\_INTR\_SOURCE](#a83a3ce01a7cc1f3d4095d260f96705d1)   41 |
| #define | [ICACHE\_SYNC0\_INTR\_SOURCE](#ae62a038d99a1fbd095213f05adfd8f0f)   42 |
| #define | [APB\_ADC\_INTR\_SOURCE](#a68b408eb63057838c64c51718c5b1f7f)   43 |
| #define | [DMA\_CH0\_INTR\_SOURCE](#a25d5f4b9fe34b025f0d780e9bafe9d96)   44 |
| #define | [DMA\_CH1\_INTR\_SOURCE](#a7026a776eda63a2aee8b3325dad72791)   45 |
| #define | [DMA\_CH2\_INTR\_SOURCE](#ad09b4d38f016ecc50dbf97f999991120)   46 |
| #define | [RSA\_INTR\_SOURCE](#accd4889d9e375ba16ea00489e7115c30)   47 |
| #define | [AES\_INTR\_SOURCE](#ad793803f54262a4dcf6b14140e9dc22b)   48 |
| #define | [SHA\_INTR\_SOURCE](#a59f92ba6a2f4b3fa9454558f37ff3e24)   49 |
| #define | [FROM\_CPU\_INTR0\_SOURCE](#a47c9d4be8d21b6f389993db5dbe2883d)   50 |
| #define | [FROM\_CPU\_INTR1\_SOURCE](#a2f704a24d6d56f2e13aed56e86e8fb55)   51 |
| #define | [FROM\_CPU\_INTR2\_SOURCE](#a470d4f804a7ddb5d107f1cafe8f19308)   52 |
| #define | [FROM\_CPU\_INTR3\_SOURCE](#a0b8897c96de3f23e794440ef2ef2f523)   53 |
| #define | [ASSIST\_DEBUG\_INTR\_SOURCE](#ab627766f8e6b851882c42596d7df540c)   54 |
| #define | [DMA\_APBPERI\_PMS\_INTR\_SOURCE](#ac1b4f216b241ccb1ee89543a110795ac)   55 |
| #define | [CORE0\_IRAM0\_PMS\_INTR\_SOURCE](#ac01e0a43892a021afe21998a4594bc9c)   56 |
| #define | [CORE0\_DRAM0\_PMS\_INTR\_SOURCE](#a1e105d1f6e499662772ce1b78a6ad027)   57 |
| #define | [CORE0\_PIF\_PMS\_INTR\_SOURCE](#a0562484da17734d4f3848fe28261ceca)   58 |
| #define | [CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE](#a83166cdc662aeb9d1de9c9f0d3e2c330)   59 |
| #define | [BAK\_PMS\_VIOLATE\_INTR\_SOURCE](#a4386805f6a7f861e5f71c9e6b31a106e)   60 |
| #define | [CACHE\_CORE0\_ACS\_INTR\_SOURCE](#acea509fed0c77dfdb5e0f0ea7b5826af)   61 |

## Macro Definition Documentation

## [◆ ](#ad793803f54262a4dcf6b14140e9dc22b)AES\_INTR\_SOURCE

| #define AES\_INTR\_SOURCE   48 |
| --- |

## [◆ ](#a68b408eb63057838c64c51718c5b1f7f)APB\_ADC\_INTR\_SOURCE

| #define APB\_ADC\_INTR\_SOURCE   43 |
| --- |

## [◆ ](#ab2acf6e0b0eb1f7ea85f0910f90326dc)APB\_CTRL\_INTR\_SOURCE

| #define APB\_CTRL\_INTR\_SOURCE   14 |
| --- |

## [◆ ](#ab627766f8e6b851882c42596d7df540c)ASSIST\_DEBUG\_INTR\_SOURCE

| #define ASSIST\_DEBUG\_INTR\_SOURCE   54 |
| --- |

## [◆ ](#a4386805f6a7f861e5f71c9e6b31a106e)BAK\_PMS\_VIOLATE\_INTR\_SOURCE

| #define BAK\_PMS\_VIOLATE\_INTR\_SOURCE   60 |
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

| #define CACHE\_CORE0\_ACS\_INTR\_SOURCE   61 |
| --- |

## [◆ ](#abc71e0e6d2e6ea7fc39d17297753e72e)CACHE\_IA\_INTR\_SOURCE

| #define CACHE\_IA\_INTR\_SOURCE   36 |
| --- |

## [◆ ](#a1e105d1f6e499662772ce1b78a6ad027)CORE0\_DRAM0\_PMS\_INTR\_SOURCE

| #define CORE0\_DRAM0\_PMS\_INTR\_SOURCE   57 |
| --- |

## [◆ ](#ac01e0a43892a021afe21998a4594bc9c)CORE0\_IRAM0\_PMS\_INTR\_SOURCE

| #define CORE0\_IRAM0\_PMS\_INTR\_SOURCE   56 |
| --- |

## [◆ ](#a0562484da17734d4f3848fe28261ceca)CORE0\_PIF\_PMS\_INTR\_SOURCE

| #define CORE0\_PIF\_PMS\_INTR\_SOURCE   58 |
| --- |

## [◆ ](#a83166cdc662aeb9d1de9c9f0d3e2c330)CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE

| #define CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE   59 |
| --- |

## [◆ ](#ac1b4f216b241ccb1ee89543a110795ac)DMA\_APBPERI\_PMS\_INTR\_SOURCE

| #define DMA\_APBPERI\_PMS\_INTR\_SOURCE   55 |
| --- |

## [◆ ](#a25d5f4b9fe34b025f0d780e9bafe9d96)DMA\_CH0\_INTR\_SOURCE

| #define DMA\_CH0\_INTR\_SOURCE   44 |
| --- |

## [◆ ](#a7026a776eda63a2aee8b3325dad72791)DMA\_CH1\_INTR\_SOURCE

| #define DMA\_CH1\_INTR\_SOURCE   45 |
| --- |

## [◆ ](#ad09b4d38f016ecc50dbf97f999991120)DMA\_CH2\_INTR\_SOURCE

| #define DMA\_CH2\_INTR\_SOURCE   46 |
| --- |

## [◆ ](#aaf244ea4b63d912e0ce8d59795c79f9d)EFUSE\_INTR\_SOURCE

| #define EFUSE\_INTR\_SOURCE   24 |
| --- |

## [◆ ](#a47c9d4be8d21b6f389993db5dbe2883d)FROM\_CPU\_INTR0\_SOURCE

| #define FROM\_CPU\_INTR0\_SOURCE   50 |
| --- |

## [◆ ](#a2f704a24d6d56f2e13aed56e86e8fb55)FROM\_CPU\_INTR1\_SOURCE

| #define FROM\_CPU\_INTR1\_SOURCE   51 |
| --- |

## [◆ ](#a470d4f804a7ddb5d107f1cafe8f19308)FROM\_CPU\_INTR2\_SOURCE

| #define FROM\_CPU\_INTR2\_SOURCE   52 |
| --- |

## [◆ ](#a0b8897c96de3f23e794440ef2ef2f523)FROM\_CPU\_INTR3\_SOURCE

| #define FROM\_CPU\_INTR3\_SOURCE   53 |
| --- |

## [◆ ](#a64020d7c1f6557ef6da375f12acf68de)GPIO\_INTR\_SOURCE

| #define GPIO\_INTR\_SOURCE   16 |
| --- |

## [◆ ](#a23e7de652ab586c903ec999aa8e77e4e)GPIO\_NMI\_SOURCE

| #define GPIO\_NMI\_SOURCE   17 |
| --- |

## [◆ ](#a7a706aa628e14e55247d20c9853d76a9)I2C\_EXT0\_INTR\_SOURCE

| #define I2C\_EXT0\_INTR\_SOURCE   29 |
| --- |

## [◆ ](#a8b38a0acf3511d0de89607d7eac8f537)I2C\_MASTER\_SOURCE

| #define I2C\_MASTER\_SOURCE   11 |
| --- |

## [◆ ](#a3b0877aad4fc7995be0cfb71fabb13a6)I2S1\_INTR\_SOURCE

| #define I2S1\_INTR\_SOURCE   20 |
| --- |

## [◆ ](#a83a3ce01a7cc1f3d4095d260f96705d1)ICACHE\_PRELOAD0\_INTR\_SOURCE

| #define ICACHE\_PRELOAD0\_INTR\_SOURCE   41 |
| --- |

## [◆ ](#ae62a038d99a1fbd095213f05adfd8f0f)ICACHE\_SYNC0\_INTR\_SOURCE

| #define ICACHE\_SYNC0\_INTR\_SOURCE   42 |
| --- |

## [◆ ](#a296f3d252d30615dbaea32d61cba9214)LEDC\_INTR\_SOURCE

| #define LEDC\_INTR\_SOURCE   23 |
| --- |

## [◆ ](#ac6d02a2b0f009553a9e52e7842fa959d)RMT\_INTR\_SOURCE

| #define RMT\_INTR\_SOURCE   28 |
| --- |

## [◆ ](#accd4889d9e375ba16ea00489e7115c30)RSA\_INTR\_SOURCE

| #define RSA\_INTR\_SOURCE   47 |
| --- |

## [◆ ](#a80d2efc475574efe9250d0048a8a8c12)RTC\_CORE\_INTR\_SOURCE

| #define RTC\_CORE\_INTR\_SOURCE   27 |
| --- |

## [◆ ](#a8cf7f44d512a2c0b215397ae4c37a4f1)RWBLE\_INTR\_SOURCE

| #define RWBLE\_INTR\_SOURCE   8 |
| --- |

## [◆ ](#a3b9cef18112f398bd4ada544f3e2b5a0)RWBLE\_NMI\_SOURCE

| #define RWBLE\_NMI\_SOURCE   10 |
| --- |

## [◆ ](#a14017a5bb9744f9c32138dbdcc09a786)RWBT\_INTR\_SOURCE

| #define RWBT\_INTR\_SOURCE   7 |
| --- |

## [◆ ](#a445a79e81929641c372257f4018127f6)RWBT\_NMI\_SOURCE

| #define RWBT\_NMI\_SOURCE   9 |
| --- |

## [◆ ](#a59f92ba6a2f4b3fa9454558f37ff3e24)SHA\_INTR\_SOURCE

| #define SHA\_INTR\_SOURCE   49 |
| --- |

## [◆ ](#a24b7d137ebb32c58d60d5f84a3ce67db)SLC0\_INTR\_SOURCE

| #define SLC0\_INTR\_SOURCE   12 |
| --- |

## [◆ ](#a8d8c7fb4a7206356ef7c7b41df4c1b7b)SLC1\_INTR\_SOURCE

| #define SLC1\_INTR\_SOURCE   13 |
| --- |

## [◆ ](#a5779abc3d34c94cfad763d9ababebb9f)SPI1\_INTR\_SOURCE

| #define SPI1\_INTR\_SOURCE   18 |
| --- |

## [◆ ](#ac5d10660472f10fae0d0511f254b696d)SPI2\_INTR\_SOURCE

| #define SPI2\_INTR\_SOURCE   19 |
| --- |

## [◆ ](#a36c488ff1605277f2772b1f80552f6ac)SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE

| #define SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE   40 |
| --- |

## [◆ ](#a4cb07c15412c22b4939bb5a1e782f6e7)SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE   37 |
| --- |

## [◆ ](#a4ae5acb4be5a37cc87deb29ca61c8034)SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE   38 |
| --- |

## [◆ ](#a3c07aba15f9a2e9bc4a97031a241b512)SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE   39 |
| --- |

## [◆ ](#a22bf10410f0b99b9fe398accf66c51b1)TG0\_T0\_LEVEL\_INTR\_SOURCE

| #define TG0\_T0\_LEVEL\_INTR\_SOURCE   32 |
| --- |

## [◆ ](#afc23d5890e9c8029e7d417291193a559)TG0\_WDT\_LEVEL\_INTR\_SOURCE

| #define TG0\_WDT\_LEVEL\_INTR\_SOURCE   33 |
| --- |

## [◆ ](#aee34beaabe47713742eb7633bd8430e3)TG1\_T0\_LEVEL\_INTR\_SOURCE

| #define TG1\_T0\_LEVEL\_INTR\_SOURCE   34 |
| --- |

## [◆ ](#a68616a67d062b7e57dbe6dd59151b85c)TG1\_WDT\_LEVEL\_INTR\_SOURCE

| #define TG1\_WDT\_LEVEL\_INTR\_SOURCE   35 |
| --- |

## [◆ ](#a9f5fed8c34c9b971830ab3e083316271)TIMER1\_INTR\_SOURCE

| #define TIMER1\_INTR\_SOURCE   30 |
| --- |

## [◆ ](#a792de801f5e8339f61a381172782ee06)TIMER2\_INTR\_SOURCE

| #define TIMER2\_INTR\_SOURCE   31 |
| --- |

## [◆ ](#a3a56673ee10a809fb2e75065d84b6f8e)TWAI\_INTR\_SOURCE

| #define TWAI\_INTR\_SOURCE   25 |
| --- |

## [◆ ](#af4569e6b552e35100134e167cf11c7da)UART0\_INTR\_SOURCE

| #define UART0\_INTR\_SOURCE   21 |
| --- |

## [◆ ](#ad6f7d29b71a32716058033727bd01dc2)UART1\_INTR\_SOURCE

| #define UART1\_INTR\_SOURCE   22 |
| --- |

## [◆ ](#aa714005c0707aaf1ba5b4a033bcb8f81)UHCI0\_INTR\_SOURCE

| #define UHCI0\_INTR\_SOURCE   15 |
| --- |

## [◆ ](#a7a020da508049560356d36ab9607bca9)USB\_INTR\_SOURCE

| #define USB\_INTR\_SOURCE   26 |
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
- [esp-esp32c3-intmux.h](esp-esp32c3-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
