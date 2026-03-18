---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gsm__ppp_8h.html
original_path: doxygen/html/gsm__ppp_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gsm\_ppp.h File Reference

[Go to the source code of this file.](gsm__ppp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [gsm\_ppp\_modem\_info](structgsm__ppp__modem__info.md) |

| Macros | |
| --- | --- |
| #define | [GSM\_PPP\_MDM\_MANUFACTURER\_LENGTH](#a7d0d3d4004541ce125417fedc3775db9)   10 |
| #define | [GSM\_PPP\_MDM\_MODEL\_LENGTH](#a6ec9ad653ae610a1c6064bd235235539)   16 |
| #define | [GSM\_PPP\_MDM\_REVISION\_LENGTH](#a9e74ec96ba8289513c69712579226315)   64 |
| #define | [GSM\_PPP\_MDM\_IMEI\_LENGTH](#a3a04d8d88f1ee163b1ddcda94813e1c1)   16 |
| #define | [GSM\_PPP\_MDM\_IMSI\_LENGTH](#a5bacf7668c8757af18e28b6da9ee03f4)   16 |
| #define | [GSM\_PPP\_MDM\_ICCID\_LENGTH](#a44b2e41f36621fd5d6485a339ff10c33)   32 |

| Functions | |
| --- | --- |
| void | [gsm\_ppp\_register\_modem\_power\_callback](#af9dc2fb4a09aa887c2046ca3b029d2e6) (const struct [device](structdevice.md) \*dev, gsm\_modem\_power\_cb modem\_on, gsm\_modem\_power\_cb modem\_off, void \*user\_data) |
|  | Register functions callbacks for power modem on/off. |
| const struct gsm\_ppp\_modem\_info \* | [gsm\_ppp\_modem\_info](#a5b991701916b3094e06d962d95331969) (const struct [device](structdevice.md) \*dev) |
|  | Get GSM modem information. |

## Macro Definition Documentation

## [◆ ](#a44b2e41f36621fd5d6485a339ff10c33)GSM\_PPP\_MDM\_ICCID\_LENGTH

| #define GSM\_PPP\_MDM\_ICCID\_LENGTH   32 |
| --- |

## [◆ ](#a3a04d8d88f1ee163b1ddcda94813e1c1)GSM\_PPP\_MDM\_IMEI\_LENGTH

| #define GSM\_PPP\_MDM\_IMEI\_LENGTH   16 |
| --- |

## [◆ ](#a5bacf7668c8757af18e28b6da9ee03f4)GSM\_PPP\_MDM\_IMSI\_LENGTH

| #define GSM\_PPP\_MDM\_IMSI\_LENGTH   16 |
| --- |

## [◆ ](#a7d0d3d4004541ce125417fedc3775db9)GSM\_PPP\_MDM\_MANUFACTURER\_LENGTH

| #define GSM\_PPP\_MDM\_MANUFACTURER\_LENGTH   10 |
| --- |

## [◆ ](#a6ec9ad653ae610a1c6064bd235235539)GSM\_PPP\_MDM\_MODEL\_LENGTH

| #define GSM\_PPP\_MDM\_MODEL\_LENGTH   16 |
| --- |

## [◆ ](#a9e74ec96ba8289513c69712579226315)GSM\_PPP\_MDM\_REVISION\_LENGTH

| #define GSM\_PPP\_MDM\_REVISION\_LENGTH   64 |
| --- |

## Function Documentation

## [◆ ](#a5b991701916b3094e06d962d95331969)gsm\_ppp\_modem\_info()

| const struct gsm\_ppp\_modem\_info \* gsm\_ppp\_modem\_info | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get GSM modem information.

Parameters
:   | dev | GSM modem device. |
    | --- | --- |

Return values
:   | struct | [gsm\_ppp\_modem\_info](structgsm__ppp__modem__info.md) \* pointer to modem information structure. |
    | --- | --- |

## [◆ ](#af9dc2fb4a09aa887c2046ca3b029d2e6)gsm\_ppp\_register\_modem\_power\_callback()

| void gsm\_ppp\_register\_modem\_power\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | gsm\_modem\_power\_cb | *modem\_on*, |
|  |  | gsm\_modem\_power\_cb | *modem\_off*, |
|  |  | void \* | *user\_data* ) |

Register functions callbacks for power modem on/off.

Parameters
:   | dev | gsm modem device |
    | --- | --- |
    | modem\_on | callback function to execute during gsm ppp configuring. |
    | modem\_off | callback function to execute during gsm ppp stopping. |
    | user\_data | user specified data |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [modem](dir_921fc901d44f7fec5fdbf8b941e64fce.md)
- [gsm\_ppp.h](gsm__ppp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
