---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2mfd_2npm13xx_8h.html
original_path: doxygen/html/drivers_2mfd_2npm13xx_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm13xx.h File Reference

`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](drivers_2mfd_2npm13xx_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [mfd\_npm13xx\_event\_t](group__mfd__interface__npm13xx.md#ga4ac9f47283f10ea1d847cbd0038aad7a) {     [NPM13XX\_EVENT\_CHG\_COMPLETED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa713b4881ca37b1b536fb32dbbb45f858) , [NPM13XX\_EVENT\_CHG\_ERROR](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa7c34f84901995115cf03399a7c0cf0a6) , [NPM13XX\_EVENT\_BATTERY\_DETECTED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa81b8d1ebbebd90a6c80063cfcd52983c) , [NPM13XX\_EVENT\_BATTERY\_REMOVED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa0e3ee9c58a2cd04e105c829faf72a50d) ,     [NPM13XX\_EVENT\_SHIPHOLD\_PRESS](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa958cb58b437567915ccf9c54b20fe646) , [NPM13XX\_EVENT\_SHIPHOLD\_RELEASE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa285ae1257239be4145f7ff036cfd88e5) , [NPM13XX\_EVENT\_WATCHDOG\_WARN](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa044e675f8f58f27318071be0cc315ba7) , [NPM13XX\_EVENT\_VBUS\_DETECTED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aaed62a7ab4cab4ae1110fe08bf425fa6b) ,     [NPM13XX\_EVENT\_VBUS\_REMOVED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aab2d73d88655a4a3cf0803bc4ac40179e) , [NPM13XX\_EVENT\_GPIO0\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa04af5688f6422ed5f7e37285f0fa98e8) , [NPM13XX\_EVENT\_GPIO1\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aae0fad2bbb85cca6b6e5a3cb43d859e9c) , [NPM13XX\_EVENT\_GPIO2\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa4216711d8a06182068932fef1d542e25) ,     [NPM13XX\_EVENT\_GPIO3\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa439a506f9314c64f78c87244edf8c15b) , [NPM13XX\_EVENT\_GPIO4\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa66c1f49b682bc96fdb186f24834cdb35) , [NPM13XX\_EVENT\_MAX](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa7b92b922aedb16e55c330254e6df0cfa)   } |

| Functions | |
| --- | --- |
| int | [mfd\_npm13xx\_reg\_read\_burst](group__mfd__interface__npm13xx.md#gabba0559ce29b71e1ce7065bf5d36f8d8) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read multiple registers from npm13xx. |
| int | [mfd\_npm13xx\_reg\_read](group__mfd__interface__npm13xx.md#ga154c4c48888ff1587d157b16e38d2584) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Read single register from npm13xx. |
| int | [mfd\_npm13xx\_reg\_write](group__mfd__interface__npm13xx.md#gac1c7815a4bcfb2262fd4f02d28f2f781) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | Write single register to npm13xx. |
| int | [mfd\_npm13xx\_reg\_write2](group__mfd__interface__npm13xx.md#gaeb317a7b4aa2ad37e69c2fda77dbbd0e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data1, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data2) |
|  | Write two registers to npm13xx. |
| int | [mfd\_npm13xx\_reg\_update](group__mfd__interface__npm13xx.md#ga239cfcef1ab91e3ccc8fb7f39f11dfd2) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | Update selected bits in npm13xx register. |
| int | [mfd\_npm13xx\_set\_timer](group__mfd__interface__npm13xx.md#ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms) |
|  | Write npm13xx timer register. |
| int | [mfd\_npm13xx\_reset](group__mfd__interface__npm13xx.md#ga43c5a5225a0cc2738506d5556ecb06ba) (const struct [device](structdevice.md) \*dev) |
|  | npm13xx full power reset |
| int | [mfd\_npm13xx\_hibernate](group__mfd__interface__npm13xx.md#gaf23758d56ac58f814bc2f093ebfa1282) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms) |
|  | npm13xx hibernate |
| int | [mfd\_npm13xx\_add\_callback](group__mfd__interface__npm13xx.md#ga3cac4a85cee20242d3a988d9830ea547) (const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Add npm13xx event callback. |
| int | [mfd\_npm13xx\_remove\_callback](group__mfd__interface__npm13xx.md#ga35fbc854545b9113f6ec36677491b151) (const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Remove npm13xx event callback. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [npm13xx.h](drivers_2mfd_2npm13xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
