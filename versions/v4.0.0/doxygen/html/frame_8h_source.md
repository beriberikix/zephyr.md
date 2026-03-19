---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/frame_8h_source.html
original_path: doxygen/html/frame_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

frame.h

[Go to the documentation of this file.](frame_8h.md)

1/\*

2 \* Copyright (c) 2023, Emna Rekik

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVER\_FRAME\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_HTTP\_SERVER\_FRAME\_H\_

14

15#include <[stdint.h](stdint_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 22](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2f)enum [http2\_frame\_type](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2f) {

[ 24](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa02d444bc7da5f9342c8490051494a561) [HTTP2\_DATA\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa02d444bc7da5f9342c8490051494a561) = 0x00,

[ 26](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fabb919f746f9cb550e3d3ed3fbd0aa0fb) [HTTP2\_HEADERS\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fabb919f746f9cb550e3d3ed3fbd0aa0fb) = 0x01,

[ 28](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fab09f251d80dd5475808473a190349d15) [HTTP2\_PRIORITY\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fab09f251d80dd5475808473a190349d15) = 0x02,

[ 30](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2faea35662abfea3d425ca626be3a042e49) [HTTP2\_RST\_STREAM\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2faea35662abfea3d425ca626be3a042e49) = 0x03,

[ 32](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa87d56ac6afcb9d85c8774b190b4f9123) [HTTP2\_SETTINGS\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa87d56ac6afcb9d85c8774b190b4f9123) = 0x04,

[ 34](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fad82d652aee8fd35ce6e2ca0eec717442) [HTTP2\_PUSH\_PROMISE\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fad82d652aee8fd35ce6e2ca0eec717442) = 0x05,

[ 36](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa12949c06e095e808f65bd4fb3cfa69ff) [HTTP2\_PING\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa12949c06e095e808f65bd4fb3cfa69ff) = 0x06,

[ 38](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa9439fea062e3e2d61d8bfadd66e421c8) [HTTP2\_GOAWAY\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa9439fea062e3e2d61d8bfadd66e421c8) = 0x07,

[ 40](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa619d7150ec1e5eff0f7b98a0a228b6b4) [HTTP2\_WINDOW\_UPDATE\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa619d7150ec1e5eff0f7b98a0a228b6b4) = 0x08,

[ 42](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa2baf23cf1cb79f34306edb76f768e822) [HTTP2\_CONTINUATION\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa2baf23cf1cb79f34306edb76f768e822) = 0x09

43};

44

46

47#define HTTP2\_FLAG\_SETTINGS\_ACK 0x01

48#define HTTP2\_FLAG\_END\_HEADERS 0x04

49#define HTTP2\_FLAG\_END\_STREAM 0x01

50#define HTTP2\_FLAG\_PADDED 0x08

51#define HTTP2\_FLAG\_PRIORITY 0x20

52

53#define HTTP2\_FRAME\_HEADER\_SIZE 9

54#define HTTP2\_FRAME\_LENGTH\_OFFSET 0

55#define HTTP2\_FRAME\_TYPE\_OFFSET 3

56#define HTTP2\_FRAME\_FLAGS\_OFFSET 4

57#define HTTP2\_FRAME\_STREAM\_ID\_OFFSET 5

58#define HTTP2\_FRAME\_STREAM\_ID\_MASK 0x7FFFFFFF

59

60#define HTTP2\_HEADERS\_FRAME\_PRIORITY\_LEN 5

61#define HTTP2\_PRIORITY\_FRAME\_LEN 5

62#define HTTP2\_RST\_STREAM\_FRAME\_LEN 4

63

65

[ 67](structhttp2__settings__field.md)struct [http2\_settings\_field](structhttp2__settings__field.md) {

[ 68](structhttp2__settings__field.md#a66561355ba380a09c0ca8df583c085b8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structhttp2__settings__field.md#a66561355ba380a09c0ca8df583c085b8);

[ 69](structhttp2__settings__field.md#a3093b8f2b69ae06972fecbe89a18c342) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [value](structhttp2__settings__field.md#a3093b8f2b69ae06972fecbe89a18c342);

70} \_\_packed;

71

[ 73](frame_8h.md#ac0e63ce922141d8043318ed40da4b559)enum [http2\_settings](frame_8h.md#ac0e63ce922141d8043318ed40da4b559) {

[ 75](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a0dcdd60d4c429d558c4cebc9c1527e06) [HTTP2\_SETTINGS\_HEADER\_TABLE\_SIZE](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a0dcdd60d4c429d558c4cebc9c1527e06) = 1,

[ 77](frame_8h.md#ac0e63ce922141d8043318ed40da4b559ad1c9118f459a93bce47b0ad1546b50b4) [HTTP2\_SETTINGS\_ENABLE\_PUSH](frame_8h.md#ac0e63ce922141d8043318ed40da4b559ad1c9118f459a93bce47b0ad1546b50b4) = 2,

[ 79](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a844c0af59b8b254301d47b0888886304) [HTTP2\_SETTINGS\_MAX\_CONCURRENT\_STREAMS](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a844c0af59b8b254301d47b0888886304) = 3,

[ 81](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a1152ff63cb965c24f05419e92112d6f0) [HTTP2\_SETTINGS\_INITIAL\_WINDOW\_SIZE](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a1152ff63cb965c24f05419e92112d6f0) = 4,

[ 83](frame_8h.md#ac0e63ce922141d8043318ed40da4b559af09a348b42a97e9d8ae57bff5e252a9e) [HTTP2\_SETTINGS\_MAX\_FRAME\_SIZE](frame_8h.md#ac0e63ce922141d8043318ed40da4b559af09a348b42a97e9d8ae57bff5e252a9e) = 5,

[ 85](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a763095cc59fc3a905a4612e9a2843705) [HTTP2\_SETTINGS\_MAX\_HEADER\_LIST\_SIZE](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a763095cc59fc3a905a4612e9a2843705) = 6,

86};

87

88#ifdef \_\_cplusplus

89}

90#endif

91

92#endif

[http2\_frame\_type](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2f)

http2\_frame\_type

HTTP2 frame types.

**Definition** frame.h:22

[HTTP2\_DATA\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa02d444bc7da5f9342c8490051494a561)

@ HTTP2\_DATA\_FRAME

Data frame.

**Definition** frame.h:24

[HTTP2\_PING\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa12949c06e095e808f65bd4fb3cfa69ff)

@ HTTP2\_PING\_FRAME

Ping frame.

**Definition** frame.h:36

[HTTP2\_CONTINUATION\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa2baf23cf1cb79f34306edb76f768e822)

@ HTTP2\_CONTINUATION\_FRAME

Continuation frame.

**Definition** frame.h:42

[HTTP2\_WINDOW\_UPDATE\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa619d7150ec1e5eff0f7b98a0a228b6b4)

@ HTTP2\_WINDOW\_UPDATE\_FRAME

Window update frame.

**Definition** frame.h:40

[HTTP2\_SETTINGS\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa87d56ac6afcb9d85c8774b190b4f9123)

@ HTTP2\_SETTINGS\_FRAME

Settings frame.

**Definition** frame.h:32

[HTTP2\_GOAWAY\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fa9439fea062e3e2d61d8bfadd66e421c8)

@ HTTP2\_GOAWAY\_FRAME

Goaway frame.

**Definition** frame.h:38

[HTTP2\_PRIORITY\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fab09f251d80dd5475808473a190349d15)

@ HTTP2\_PRIORITY\_FRAME

Priority frame.

**Definition** frame.h:28

[HTTP2\_HEADERS\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fabb919f746f9cb550e3d3ed3fbd0aa0fb)

@ HTTP2\_HEADERS\_FRAME

Headers frame.

**Definition** frame.h:26

[HTTP2\_PUSH\_PROMISE\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2fad82d652aee8fd35ce6e2ca0eec717442)

@ HTTP2\_PUSH\_PROMISE\_FRAME

Push promise frame.

**Definition** frame.h:34

[HTTP2\_RST\_STREAM\_FRAME](frame_8h.md#a3017b7bf771b2502f76e1d8bb672bb2faea35662abfea3d425ca626be3a042e49)

@ HTTP2\_RST\_STREAM\_FRAME

Reset stream frame.

**Definition** frame.h:30

[http2\_settings](frame_8h.md#ac0e63ce922141d8043318ed40da4b559)

http2\_settings

HTTP2 settings.

**Definition** frame.h:73

[HTTP2\_SETTINGS\_HEADER\_TABLE\_SIZE](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a0dcdd60d4c429d558c4cebc9c1527e06)

@ HTTP2\_SETTINGS\_HEADER\_TABLE\_SIZE

Header table size.

**Definition** frame.h:75

[HTTP2\_SETTINGS\_INITIAL\_WINDOW\_SIZE](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a1152ff63cb965c24f05419e92112d6f0)

@ HTTP2\_SETTINGS\_INITIAL\_WINDOW\_SIZE

Initial window size.

**Definition** frame.h:81

[HTTP2\_SETTINGS\_MAX\_HEADER\_LIST\_SIZE](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a763095cc59fc3a905a4612e9a2843705)

@ HTTP2\_SETTINGS\_MAX\_HEADER\_LIST\_SIZE

Max header list size.

**Definition** frame.h:85

[HTTP2\_SETTINGS\_MAX\_CONCURRENT\_STREAMS](frame_8h.md#ac0e63ce922141d8043318ed40da4b559a844c0af59b8b254301d47b0888886304)

@ HTTP2\_SETTINGS\_MAX\_CONCURRENT\_STREAMS

Maximum number of concurrent streams.

**Definition** frame.h:79

[HTTP2\_SETTINGS\_ENABLE\_PUSH](frame_8h.md#ac0e63ce922141d8043318ed40da4b559ad1c9118f459a93bce47b0ad1546b50b4)

@ HTTP2\_SETTINGS\_ENABLE\_PUSH

Enable push.

**Definition** frame.h:77

[HTTP2\_SETTINGS\_MAX\_FRAME\_SIZE](frame_8h.md#ac0e63ce922141d8043318ed40da4b559af09a348b42a97e9d8ae57bff5e252a9e)

@ HTTP2\_SETTINGS\_MAX\_FRAME\_SIZE

Max frame size.

**Definition** frame.h:83

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[http2\_settings\_field](structhttp2__settings__field.md)

HTTP2 settings field.

**Definition** frame.h:67

[http2\_settings\_field::value](structhttp2__settings__field.md#a3093b8f2b69ae06972fecbe89a18c342)

uint32\_t value

Field value.

**Definition** frame.h:69

[http2\_settings\_field::id](structhttp2__settings__field.md#a66561355ba380a09c0ca8df583c085b8)

uint16\_t id

Field id.

**Definition** frame.h:68

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [frame.h](frame_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
