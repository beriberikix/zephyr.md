---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gsm__ppp_8h_source.html
original_path: doxygen/html/gsm__ppp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gsm\_ppp.h

[Go to the documentation of this file.](gsm__ppp_8h.md)

1/\*

2 \* Copyright (c) 2020 Endian Technologies AB

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MODEM\_GSM\_PPP\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_MODEM\_GSM\_PPP\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

[ 14](gsm__ppp_8h.md#a7d0d3d4004541ce125417fedc3775db9)#define GSM\_PPP\_MDM\_MANUFACTURER\_LENGTH 10

[ 15](gsm__ppp_8h.md#a6ec9ad653ae610a1c6064bd235235539)#define GSM\_PPP\_MDM\_MODEL\_LENGTH 16

[ 16](gsm__ppp_8h.md#a9e74ec96ba8289513c69712579226315)#define GSM\_PPP\_MDM\_REVISION\_LENGTH 64

[ 17](gsm__ppp_8h.md#a3a04d8d88f1ee163b1ddcda94813e1c1)#define GSM\_PPP\_MDM\_IMEI\_LENGTH 16

[ 18](gsm__ppp_8h.md#a5bacf7668c8757af18e28b6da9ee03f4)#define GSM\_PPP\_MDM\_IMSI\_LENGTH 16

[ 19](gsm__ppp_8h.md#a44b2e41f36621fd5d6485a339ff10c33)#define GSM\_PPP\_MDM\_ICCID\_LENGTH 32

20

[ 21](structgsm__ppp__modem__info.md)struct [gsm\_ppp\_modem\_info](structgsm__ppp__modem__info.md) {

[ 22](structgsm__ppp__modem__info.md#a1ee0ab3da77cd27c35943733bbfbdee5) char [mdm\_manufacturer](structgsm__ppp__modem__info.md#a1ee0ab3da77cd27c35943733bbfbdee5)[[GSM\_PPP\_MDM\_MANUFACTURER\_LENGTH](gsm__ppp_8h.md#a7d0d3d4004541ce125417fedc3775db9)];

[ 23](structgsm__ppp__modem__info.md#a877ee65c1b52784bc4d534d792850fae) char [mdm\_model](structgsm__ppp__modem__info.md#a877ee65c1b52784bc4d534d792850fae)[[GSM\_PPP\_MDM\_MODEL\_LENGTH](gsm__ppp_8h.md#a6ec9ad653ae610a1c6064bd235235539)];

[ 24](structgsm__ppp__modem__info.md#a1b8ce6d86bce0a6b083530af0e059a2c) char [mdm\_revision](structgsm__ppp__modem__info.md#a1b8ce6d86bce0a6b083530af0e059a2c)[[GSM\_PPP\_MDM\_REVISION\_LENGTH](gsm__ppp_8h.md#a9e74ec96ba8289513c69712579226315)];

[ 25](structgsm__ppp__modem__info.md#a72281846471c898bf2c11b5a9264feaa) char [mdm\_imei](structgsm__ppp__modem__info.md#a72281846471c898bf2c11b5a9264feaa)[[GSM\_PPP\_MDM\_IMEI\_LENGTH](gsm__ppp_8h.md#a3a04d8d88f1ee163b1ddcda94813e1c1)];

26#if defined(CONFIG\_MODEM\_SIM\_NUMBERS)

27 char mdm\_imsi[[GSM\_PPP\_MDM\_IMSI\_LENGTH](gsm__ppp_8h.md#a5bacf7668c8757af18e28b6da9ee03f4)];

28 char mdm\_iccid[[GSM\_PPP\_MDM\_ICCID\_LENGTH](gsm__ppp_8h.md#a44b2e41f36621fd5d6485a339ff10c33)];

29#endif

[ 30](structgsm__ppp__modem__info.md#a26bc7f1bcf865591cccbd5af97b67dfd) int [mdm\_rssi](structgsm__ppp__modem__info.md#a26bc7f1bcf865591cccbd5af97b67dfd);

31};

32

34struct [device](structdevice.md);

35typedef void (\*gsm\_modem\_power\_cb)(const struct [device](structdevice.md) \*, void \*);

36

37void gsm\_ppp\_start(const struct [device](structdevice.md) \*dev);

38void gsm\_ppp\_stop(const struct [device](structdevice.md) \*dev);

40

[ 51](gsm__ppp_8h.md#af9dc2fb4a09aa887c2046ca3b029d2e6)void [gsm\_ppp\_register\_modem\_power\_callback](gsm__ppp_8h.md#af9dc2fb4a09aa887c2046ca3b029d2e6)(const struct [device](structdevice.md) \*dev,

52 gsm\_modem\_power\_cb modem\_on,

53 gsm\_modem\_power\_cb modem\_off,

54 void \*user\_data);

55

[ 63](gsm__ppp_8h.md#a5b991701916b3094e06d962d95331969)const struct [gsm\_ppp\_modem\_info](structgsm__ppp__modem__info.md) \*[gsm\_ppp\_modem\_info](gsm__ppp_8h.md#a5b991701916b3094e06d962d95331969)(const struct [device](structdevice.md) \*dev);

64

65#ifdef \_\_cplusplus

66}

67#endif

68

69#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MODEM\_GSM\_PPP\_H\_ \*/

[GSM\_PPP\_MDM\_IMEI\_LENGTH](gsm__ppp_8h.md#a3a04d8d88f1ee163b1ddcda94813e1c1)

#define GSM\_PPP\_MDM\_IMEI\_LENGTH

**Definition** gsm\_ppp.h:17

[GSM\_PPP\_MDM\_ICCID\_LENGTH](gsm__ppp_8h.md#a44b2e41f36621fd5d6485a339ff10c33)

#define GSM\_PPP\_MDM\_ICCID\_LENGTH

**Definition** gsm\_ppp.h:19

[gsm\_ppp\_modem\_info](gsm__ppp_8h.md#a5b991701916b3094e06d962d95331969)

const struct gsm\_ppp\_modem\_info \* gsm\_ppp\_modem\_info(const struct device \*dev)

Get GSM modem information.

[GSM\_PPP\_MDM\_IMSI\_LENGTH](gsm__ppp_8h.md#a5bacf7668c8757af18e28b6da9ee03f4)

#define GSM\_PPP\_MDM\_IMSI\_LENGTH

**Definition** gsm\_ppp.h:18

[GSM\_PPP\_MDM\_MODEL\_LENGTH](gsm__ppp_8h.md#a6ec9ad653ae610a1c6064bd235235539)

#define GSM\_PPP\_MDM\_MODEL\_LENGTH

**Definition** gsm\_ppp.h:15

[GSM\_PPP\_MDM\_MANUFACTURER\_LENGTH](gsm__ppp_8h.md#a7d0d3d4004541ce125417fedc3775db9)

#define GSM\_PPP\_MDM\_MANUFACTURER\_LENGTH

**Definition** gsm\_ppp.h:14

[GSM\_PPP\_MDM\_REVISION\_LENGTH](gsm__ppp_8h.md#a9e74ec96ba8289513c69712579226315)

#define GSM\_PPP\_MDM\_REVISION\_LENGTH

**Definition** gsm\_ppp.h:16

[gsm\_ppp\_register\_modem\_power\_callback](gsm__ppp_8h.md#af9dc2fb4a09aa887c2046ca3b029d2e6)

void gsm\_ppp\_register\_modem\_power\_callback(const struct device \*dev, gsm\_modem\_power\_cb modem\_on, gsm\_modem\_power\_cb modem\_off, void \*user\_data)

Register functions callbacks for power modem on/off.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[gsm\_ppp\_modem\_info](structgsm__ppp__modem__info.md)

**Definition** gsm\_ppp.h:21

[gsm\_ppp\_modem\_info::mdm\_revision](structgsm__ppp__modem__info.md#a1b8ce6d86bce0a6b083530af0e059a2c)

char mdm\_revision[64]

**Definition** gsm\_ppp.h:24

[gsm\_ppp\_modem\_info::mdm\_manufacturer](structgsm__ppp__modem__info.md#a1ee0ab3da77cd27c35943733bbfbdee5)

char mdm\_manufacturer[10]

**Definition** gsm\_ppp.h:22

[gsm\_ppp\_modem\_info::mdm\_rssi](structgsm__ppp__modem__info.md#a26bc7f1bcf865591cccbd5af97b67dfd)

int mdm\_rssi

**Definition** gsm\_ppp.h:30

[gsm\_ppp\_modem\_info::mdm\_imei](structgsm__ppp__modem__info.md#a72281846471c898bf2c11b5a9264feaa)

char mdm\_imei[16]

**Definition** gsm\_ppp.h:25

[gsm\_ppp\_modem\_info::mdm\_model](structgsm__ppp__modem__info.md#a877ee65c1b52784bc4d534d792850fae)

char mdm\_model[16]

**Definition** gsm\_ppp.h:23

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [modem](dir_921fc901d44f7fec5fdbf8b941e64fce.md)
- [gsm\_ppp.h](gsm__ppp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
