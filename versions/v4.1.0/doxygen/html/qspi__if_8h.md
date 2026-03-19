---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/qspi__if_8h.html
original_path: doxygen/html/qspi__if_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

qspi\_if.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](qspi__if_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [qspi\_config](structqspi__config.md) |
| struct | [qspi\_dev](structqspi__dev.md) |

| Macros | |
| --- | --- |
| #define | [RPU\_WAKEUP\_NOW](#a84e11529cde7bba98bc0e612c4dec8a7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* WAKEUP RPU - RW \*/ |
|  | Header containing QSPI device interface specific declarations for the Zephyr OS layer of the Wi-Fi driver. |
| #define | [RPU\_AWAKE\_BIT](#a4d4c792a7693d161e62fd7ea78f3ac33)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* RPU AWAKE FROM SLEEP - [RO](arm__mpu__v7m_8h.md#a628642b04c07236ae1e986c248a79ae5) \*/ |
| #define | [RPU\_READY\_BIT](#adf0f3cc72222e245bec2922f9d48d7b9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\* RPU IS READY - [RO](arm__mpu__v7m_8h.md#a628642b04c07236ae1e986c248a79ae5)\*/ |
| #define | [QSPI\_KEY\_LEN\_BYTES](#aaab62367cf18acc6c77435eac0e84d1c)   16 |

| Functions | |
| --- | --- |
| int | [qspi\_cmd\_wakeup\_rpu](#a5ee3cedbf2fe79babdbb5268874a6e93) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
| int | [qspi\_init](#a424155de82df701be9706afae24e920d) (struct [qspi\_config](structqspi__config.md) \*config) |
| int | [qspi\_write](#aa277c292d448168861400c43d8f75b92) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int addr, const void \*data, int len) |
| int | [qspi\_read](#a1b48dfac997cc62e27f54304cc3c0bfc) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int addr, void \*data, int len) |
| int | [qspi\_hl\_read](#ab44ab165657864085e9a747f198b7eec) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int addr, void \*data, int len) |
| int | [qspi\_deinit](#a31827628f36adae2af395c906a118d40) (void) |
| void | [gpio\_free\_irq](#aa73129b0b275e974361fa5a0ef252c2f) (int pin, struct [gpio\_callback](structgpio__callback.md) \*button\_cb\_data) |
| int | [gpio\_request\_irq](#a8bed70457c6dfbb6fe7dd1540390cfb7) (int pin, struct [gpio\_callback](structgpio__callback.md) \*button\_cb\_data, void(\*irq\_handler)()) |
| struct [qspi\_config](structqspi__config.md) \* | [qspi\_defconfig](#a01aa4b1df13cf07ea545c14e0bd82828) (void) |
| struct qspi\_dev \* | [qspi\_dev](#ae7e8a05b3fcc5e483398493e2a7d7e93) (void) |
| struct [qspi\_config](structqspi__config.md) \* | [qspi\_get\_config](#a8d943d5376b6cf3c9d4f37bcf5fc306a) (void) |
| int | [qspi\_cmd\_sleep\_rpu](#ade1b91ab08c431e4a884013b87fda0a4) (const struct [device](structdevice.md) \*dev) |
| void | [hard\_reset](#afb4a6c00361cf7109799350d3b27ad83) (void) |
| void | [get\_sleep\_stats](#a14aeaefb2884e2dd7b2000c724069f31) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wrd\_len) |
| int | [qspi\_validate\_rpu\_wake\_writecmd](#afba5e08a80ba35ed4860f244ca177364) (const struct [device](structdevice.md) \*dev) |
| int | [qspi\_wait\_while\_rpu\_awake](#aa48981a0dad166b00a07a7fd724ea899) (const struct [device](structdevice.md) \*dev) |
| int | [qspi\_RDSR1](#a5d234f9a705746b4406d587437de92ed) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rdsr1) |
| int | [qspi\_RDSR2](#af5b8aea6ccbe60b83c5b10c05f197b41) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rdsr2) |
| int | [qspi\_WRSR2](#a88ab9dead7c0272b233dfb6d941b4a85) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wrsr2) |
| int | [qspi\_enable\_encryption](#ae1f2810d7be515acbb2944f600dbf765) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*key) |
|  | Enable encryption. |

| Variables | |
| --- | --- |
| struct [device](structdevice.md) | [qspi\_perip](#a1814c557c5e1a14b180cdb96ffdc6efc) |

## Macro Definition Documentation

## [◆ ](#aaab62367cf18acc6c77435eac0e84d1c)QSPI\_KEY\_LEN\_BYTES

| #define QSPI\_KEY\_LEN\_BYTES   16 |
| --- |

## [◆ ](#a4d4c792a7693d161e62fd7ea78f3ac33)RPU\_AWAKE\_BIT

| #define RPU\_AWAKE\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* RPU AWAKE FROM SLEEP - [RO](arm__mpu__v7m_8h.md#a628642b04c07236ae1e986c248a79ae5) \*/ |
| --- |

## [◆ ](#adf0f3cc72222e245bec2922f9d48d7b9)RPU\_READY\_BIT

| #define RPU\_READY\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\* RPU IS READY - [RO](arm__mpu__v7m_8h.md#a628642b04c07236ae1e986c248a79ae5)\*/ |
| --- |

## [◆ ](#a84e11529cde7bba98bc0e612c4dec8a7)RPU\_WAKEUP\_NOW

| #define RPU\_WAKEUP\_NOW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* WAKEUP RPU - RW \*/ |
| --- |

Header containing QSPI device interface specific declarations for the Zephyr OS layer of the Wi-Fi driver.

## Function Documentation

## [◆ ](#a14aeaefb2884e2dd7b2000c724069f31)get\_sleep\_stats()

| void get\_sleep\_stats | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *addr*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *buff*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *wrd\_len* ) |

## [◆ ](#aa73129b0b275e974361fa5a0ef252c2f)gpio\_free\_irq()

| void gpio\_free\_irq | ( | int | *pin*, |
| --- | --- | --- | --- |
|  |  | struct [gpio\_callback](structgpio__callback.md) \* | *button\_cb\_data* ) |

## [◆ ](#a8bed70457c6dfbb6fe7dd1540390cfb7)gpio\_request\_irq()

| int gpio\_request\_irq | ( | int | *pin*, |
| --- | --- | --- | --- |
|  |  | struct [gpio\_callback](structgpio__callback.md) \* | *button\_cb\_data*, |
|  |  | void(\* | *irq\_handler*)() ) |

## [◆ ](#afb4a6c00361cf7109799350d3b27ad83)hard\_reset()

| void hard\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ade1b91ab08c431e4a884013b87fda0a4)qspi\_cmd\_sleep\_rpu()

| int qspi\_cmd\_sleep\_rpu | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a5ee3cedbf2fe79babdbb5268874a6e93)qspi\_cmd\_wakeup\_rpu()

| int qspi\_cmd\_wakeup\_rpu | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data* ) |

## [◆ ](#a01aa4b1df13cf07ea545c14e0bd82828)qspi\_defconfig()

| struct [qspi\_config](structqspi__config.md) \* qspi\_defconfig | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a31827628f36adae2af395c906a118d40)qspi\_deinit()

| int qspi\_deinit | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ae7e8a05b3fcc5e483398493e2a7d7e93)qspi\_dev()

| struct qspi\_dev \* qspi\_dev | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ae1f2810d7be515acbb2944f600dbf765)qspi\_enable\_encryption()

| int qspi\_enable\_encryption | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *key* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable encryption.

Parameters
:   | key | Pointer to the 128-bit key |
    | --- | --- |

Returns
:   0 on success, negative errno code on failure.

## [◆ ](#a8d943d5376b6cf3c9d4f37bcf5fc306a)qspi\_get\_config()

| struct [qspi\_config](structqspi__config.md) \* qspi\_get\_config | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ab44ab165657864085e9a747f198b7eec)qspi\_hl\_read()

| int qspi\_hl\_read | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *addr*, |
| --- | --- | --- | --- |
|  |  | void \* | *data*, |
|  |  | int | *len* ) |

## [◆ ](#a424155de82df701be9706afae24e920d)qspi\_init()

| int qspi\_init | ( | struct [qspi\_config](structqspi__config.md) \* | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a5d234f9a705746b4406d587437de92ed)qspi\_RDSR1()

| int qspi\_RDSR1 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rdsr1* ) |

## [◆ ](#af5b8aea6ccbe60b83c5b10c05f197b41)qspi\_RDSR2()

| int qspi\_RDSR2 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rdsr2* ) |

## [◆ ](#a1b48dfac997cc62e27f54304cc3c0bfc)qspi\_read()

| int qspi\_read | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *addr*, |
| --- | --- | --- | --- |
|  |  | void \* | *data*, |
|  |  | int | *len* ) |

## [◆ ](#afba5e08a80ba35ed4860f244ca177364)qspi\_validate\_rpu\_wake\_writecmd()

| int qspi\_validate\_rpu\_wake\_writecmd | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aa48981a0dad166b00a07a7fd724ea899)qspi\_wait\_while\_rpu\_awake()

| int qspi\_wait\_while\_rpu\_awake | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aa277c292d448168861400c43d8f75b92)qspi\_write()

| int qspi\_write | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *addr*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data*, |
|  |  | int | *len* ) |

## [◆ ](#a88ab9dead7c0272b233dfb6d941b4a85)qspi\_WRSR2()

| int qspi\_WRSR2 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *wrsr2* ) |

## Variable Documentation

## [◆ ](#a1814c557c5e1a14b180cdb96ffdc6efc)qspi\_perip

| | struct [device](structdevice.md) qspi\_perip | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [wifi](dir_478165533ab14baf575002d17a842a12.md)
- [nrf\_wifi](dir_827a5ceb820ded32f2709b259acb2436.md)
- [bus](dir_a8af871e2af95a2ae463c0a62cb13e77.md)
- [qspi\_if.h](qspi__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
