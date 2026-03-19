---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/frame_8h.html
original_path: doxygen/html/frame_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

frame.h File Reference

HTTP2 frame information.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](frame_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [http2\_settings\_field](structhttp2__settings__field.md) |
|  | HTTP2 settings field. [More...](structhttp2__settings__field.md#details) |

| Enumerations | |
| --- | --- |
| enum | [http2\_frame\_type](#a3017b7bf771b2502f76e1d8bb672bb2f) {     [HTTP2\_DATA\_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa02d444bc7da5f9342c8490051494a561) = 0x00 , [HTTP2\_HEADERS\_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fabb919f746f9cb550e3d3ed3fbd0aa0fb) = 0x01 , [HTTP2\_PRIORITY\_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fab09f251d80dd5475808473a190349d15) = 0x02 , [HTTP2\_RST\_STREAM\_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2faea35662abfea3d425ca626be3a042e49) = 0x03 ,     [HTTP2\_SETTINGS\_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa87d56ac6afcb9d85c8774b190b4f9123) = 0x04 , [HTTP2\_PUSH\_PROMISE\_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fad82d652aee8fd35ce6e2ca0eec717442) = 0x05 , [HTTP2\_PING\_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa12949c06e095e808f65bd4fb3cfa69ff) = 0x06 , [HTTP2\_GOAWAY\_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa9439fea062e3e2d61d8bfadd66e421c8) = 0x07 ,     [HTTP2\_WINDOW\_UPDATE\_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa619d7150ec1e5eff0f7b98a0a228b6b4) = 0x08 , [HTTP2\_CONTINUATION\_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa2baf23cf1cb79f34306edb76f768e822) = 0x09   } |
|  | HTTP2 frame types. [More...](#a3017b7bf771b2502f76e1d8bb672bb2f) |
| enum | [http2\_settings](#ac0e63ce922141d8043318ed40da4b559) {     [HTTP2\_SETTINGS\_HEADER\_TABLE\_SIZE](#ac0e63ce922141d8043318ed40da4b559a0dcdd60d4c429d558c4cebc9c1527e06) = 1 , [HTTP2\_SETTINGS\_ENABLE\_PUSH](#ac0e63ce922141d8043318ed40da4b559ad1c9118f459a93bce47b0ad1546b50b4) = 2 , [HTTP2\_SETTINGS\_MAX\_CONCURRENT\_STREAMS](#ac0e63ce922141d8043318ed40da4b559a844c0af59b8b254301d47b0888886304) = 3 , [HTTP2\_SETTINGS\_INITIAL\_WINDOW\_SIZE](#ac0e63ce922141d8043318ed40da4b559a1152ff63cb965c24f05419e92112d6f0) = 4 ,     [HTTP2\_SETTINGS\_MAX\_FRAME\_SIZE](#ac0e63ce922141d8043318ed40da4b559af09a348b42a97e9d8ae57bff5e252a9e) = 5 , [HTTP2\_SETTINGS\_MAX\_HEADER\_LIST\_SIZE](#ac0e63ce922141d8043318ed40da4b559a763095cc59fc3a905a4612e9a2843705) = 6   } |
|  | HTTP2 settings. [More...](#ac0e63ce922141d8043318ed40da4b559) |

## Detailed Description

HTTP2 frame information.

## Enumeration Type Documentation

## [◆ ](#a3017b7bf771b2502f76e1d8bb672bb2f)http2\_frame\_type

| enum [http2\_frame\_type](#a3017b7bf771b2502f76e1d8bb672bb2f) |
| --- |

HTTP2 frame types.

| Enumerator | |
| --- | --- |
| HTTP2\_DATA\_FRAME | Data frame. |
| HTTP2\_HEADERS\_FRAME | Headers frame. |
| HTTP2\_PRIORITY\_FRAME | Priority frame. |
| HTTP2\_RST\_STREAM\_FRAME | Reset stream frame. |
| HTTP2\_SETTINGS\_FRAME | Settings frame. |
| HTTP2\_PUSH\_PROMISE\_FRAME | Push promise frame. |
| HTTP2\_PING\_FRAME | Ping frame. |
| HTTP2\_GOAWAY\_FRAME | Goaway frame. |
| HTTP2\_WINDOW\_UPDATE\_FRAME | Window update frame. |
| HTTP2\_CONTINUATION\_FRAME | Continuation frame. |

## [◆ ](#ac0e63ce922141d8043318ed40da4b559)http2\_settings

| enum [http2\_settings](#ac0e63ce922141d8043318ed40da4b559) |
| --- |

HTTP2 settings.

| Enumerator | |
| --- | --- |
| HTTP2\_SETTINGS\_HEADER\_TABLE\_SIZE | Header table size. |
| HTTP2\_SETTINGS\_ENABLE\_PUSH | Enable push. |
| HTTP2\_SETTINGS\_MAX\_CONCURRENT\_STREAMS | Maximum number of concurrent streams. |
| HTTP2\_SETTINGS\_INITIAL\_WINDOW\_SIZE | Initial window size. |
| HTTP2\_SETTINGS\_MAX\_FRAME\_SIZE | Max frame size. |
| HTTP2\_SETTINGS\_MAX\_HEADER\_LIST\_SIZE | Max header list size. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [frame.h](frame_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
