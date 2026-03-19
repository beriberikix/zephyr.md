---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/shell__websocket_8h.html
original_path: doxygen/html/shell__websocket_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_websocket.h File Reference

`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`  
`#include <[zephyr/net/http/server.h](server_8h_source.md)>`  
`#include <[zephyr/net/http/service.h](service_8h_source.md)>`  
`#include <[zephyr/shell/shell.h](shell_2shell_8h_source.md)>`

[Go to the source code of this file.](shell__websocket_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shell\_websocket\_line\_buf](structshell__websocket__line__buf.md) |
|  | Line buffer structure. [More...](structshell__websocket__line__buf.md#details) |
| struct | [shell\_websocket](structshell__websocket.md) |
|  | WEBSOCKET-based shell transport. [More...](structshell__websocket.md#details) |

| Macros | |
| --- | --- |
| #define | [SHELL\_WEBSOCKET\_SERVICE\_COUNT](#af8728c90d47a7b1b5f161ebe20d2139f)   CONFIG\_SHELL\_WEBSOCKET\_BACKEND\_COUNT |
| #define | [GET\_WS\_NAME](#a0e99a36ec4e51975f1129680e480f898)(\_service) |
| #define | [GET\_WS\_SHELL\_NAME](#a279d727996e63e02ac28e0c94c429938)(\_name) |
| #define | [GET\_WS\_TRANSPORT\_NAME](#a520876fc32f62533585a1d56c09267ff)(\_service) |
| #define | [GET\_WS\_DETAIL\_NAME](#ae81e574d5e40193417675353a0221cb0)(\_service) |
| #define | [SHELL\_WEBSOCKET\_DEFINE](#a14fb3497eb5b736b8eea2dbb99c63a10)(\_service) |
| #define | [SHELL\_WS\_PORT\_NAME](#a57a0335bfab8ac4a9d9c4a49a45e4166)(\_service) |
| #define | [SHELL\_WS\_BUF\_NAME](#ac2c72690650e352b91c6aab106fa45dd)(\_service) |
| #define | [SHELL\_WS\_TEMP\_RECV\_BUF\_SIZE](#a870da69234857ceb1966d54d4ee2f278)   256 |
| #define | [DEFINE\_WEBSOCKET\_HTTP\_SERVICE](#af32434fee39da58ad013d9b2f2670ddc)(\_service) |
| #define | [DEFINE\_WEBSOCKET\_SERVICE](#aba77cc40652e7aed5f1203cfea2ecd91)(\_service) |
| #define | [WEBSOCKET\_CONSOLE\_DEFINE](#a726a23776948ff246176c1ac2c88daa6)(\_service, \_sec\_tag\_list, \_sec\_tag\_list\_size) |
| #define | [WEBSOCKET\_CONSOLE\_ENABLE](#a134a7de93ded994b49fd781fb289e876)(\_service) |

| Functions | |
| --- | --- |
| int | [shell\_websocket\_setup](#acc516f1459d0def39779eb8e15c29d80) (int ws\_socket, void \*user\_data) |
| int | [shell\_websocket\_enable](#a773f4275294a28b9a25364c5a7d50cab) (const struct [shell](structshell.md) \*sh) |

| Variables | |
| --- | --- |
| const struct [shell\_transport\_api](structshell__transport__api.md) | [shell\_websocket\_transport\_api](#afd54f1b32a1516cd786320957222356b) |

## Macro Definition Documentation

## [◆ ](#af32434fee39da58ad013d9b2f2670ddc)DEFINE\_WEBSOCKET\_HTTP\_SERVICE

| #define DEFINE\_WEBSOCKET\_HTTP\_SERVICE | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [SHELL\_WS\_BUF\_NAME](#ac2c72690650e352b91c6aab106fa45dd)(\_service)[[SHELL\_WS\_TEMP\_RECV\_BUF\_SIZE](#a870da69234857ceb1966d54d4ee2f278)]; \

struct [http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md) \

[GET\_WS\_DETAIL\_NAME](#ae81e574d5e40193417675353a0221cb0)(\_service) = { \

.common = { \

.type = [HTTP\_RESOURCE\_TYPE\_WEBSOCKET](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866), \

\

/\* We need HTTP/1.1 GET method for upgrading \*/ \

.bitmask\_of\_supported\_http\_methods = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([HTTP\_GET](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4ad23c3d2f21f7502ba058ef89518166)), \

}, \

.cb = [shell\_websocket\_setup](#acc516f1459d0def39779eb8e15c29d80), \

.data\_buffer = [SHELL\_WS\_BUF\_NAME](#ac2c72690650e352b91c6aab106fa45dd)(\_service), \

.data\_buffer\_len = sizeof([SHELL\_WS\_BUF\_NAME](#ac2c72690650e352b91c6aab106fa45dd)(\_service)), \

.user\_data = &[GET\_WS\_NAME](#a0e99a36ec4e51975f1129680e480f898)(\_service), \

}; \

HTTP\_RESOURCE\_DEFINE(ws\_resource\_##\_service, \_service, \

"/" CONFIG\_SHELL\_WEBSOCKET\_ENDPOINT\_URL, \

&[GET\_WS\_DETAIL\_NAME](#ae81e574d5e40193417675353a0221cb0)(\_service))

[HTTP\_GET](group__http__methods.md#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4ad23c3d2f21f7502ba058ef89518166)

@ HTTP\_GET

GET.

**Definition** method.h:30

[HTTP\_RESOURCE\_TYPE\_WEBSOCKET](group__http__server.md#gga23d0077fb99827b25491111bd74d00afa6691e6fe43d8ffbd1ef1fd5c59661866)

@ HTTP\_RESOURCE\_TYPE\_WEBSOCKET

Websocket resource, application takes control over Websocket connection after and upgrade.

**Definition** server.h:74

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[GET\_WS\_NAME](#a0e99a36ec4e51975f1129680e480f898)

#define GET\_WS\_NAME(\_service)

**Definition** shell\_websocket.h:68

[SHELL\_WS\_TEMP\_RECV\_BUF\_SIZE](#a870da69234857ceb1966d54d4ee2f278)

#define SHELL\_WS\_TEMP\_RECV\_BUF\_SIZE

**Definition** shell\_websocket.h:82

[SHELL\_WS\_BUF\_NAME](#ac2c72690650e352b91c6aab106fa45dd)

#define SHELL\_WS\_BUF\_NAME(\_service)

**Definition** shell\_websocket.h:81

[shell\_websocket\_setup](#acc516f1459d0def39779eb8e15c29d80)

int shell\_websocket\_setup(int ws\_socket, void \*user\_data)

[GET\_WS\_DETAIL\_NAME](#ae81e574d5e40193417675353a0221cb0)

#define GET\_WS\_DETAIL\_NAME(\_service)

**Definition** shell\_websocket.h:71

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[http\_resource\_detail\_websocket](structhttp__resource__detail__websocket.md)

Representation of a websocket server resource.

**Definition** server.h:248

## [◆ ](#aba77cc40652e7aed5f1203cfea2ecd91)DEFINE\_WEBSOCKET\_SERVICE

| #define DEFINE\_WEBSOCKET\_SERVICE | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[SHELL\_WEBSOCKET\_DEFINE](#a14fb3497eb5b736b8eea2dbb99c63a10)(\_service); \

SHELL\_DEFINE(shell\_websocket\_##\_service, \

CONFIG\_SHELL\_WEBSOCKET\_PROMPT, \

&[GET\_WS\_TRANSPORT\_NAME](#a520876fc32f62533585a1d56c09267ff)(\_service), \

CONFIG\_SHELL\_WEBSOCKET\_LOG\_MESSAGE\_QUEUE\_SIZE, \

CONFIG\_SHELL\_WEBSOCKET\_LOG\_MESSAGE\_QUEUE\_TIMEOUT, \

[SHELL\_FLAG\_OLF\_CRLF](group__shell__api.md#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446)); \

DEFINE\_WEBSOCKET\_HTTP\_SERVICE(\_service)

[SHELL\_FLAG\_OLF\_CRLF](group__shell__api.md#gga56bf30741f9ec7a6d94e5c18c2858948ab6fec7b615b6de79e1d00d4117615446)

@ SHELL\_FLAG\_OLF\_CRLF

Map LF to CRLF on output.

**Definition** shell.h:884

[SHELL\_WEBSOCKET\_DEFINE](#a14fb3497eb5b736b8eea2dbb99c63a10)

#define SHELL\_WEBSOCKET\_DEFINE(\_service)

**Definition** shell\_websocket.h:73

[GET\_WS\_TRANSPORT\_NAME](#a520876fc32f62533585a1d56c09267ff)

#define GET\_WS\_TRANSPORT\_NAME(\_service)

**Definition** shell\_websocket.h:70

## [◆ ](#ae81e574d5e40193417675353a0221cb0)GET\_WS\_DETAIL\_NAME

| #define GET\_WS\_DETAIL\_NAME | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

ws\_res\_detail\_##\_service

## [◆ ](#a0e99a36ec4e51975f1129680e480f898)GET\_WS\_NAME

| #define GET\_WS\_NAME | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

ws\_ctx\_##\_service

## [◆ ](#a279d727996e63e02ac28e0c94c429938)GET\_WS\_SHELL\_NAME

| #define GET\_WS\_SHELL\_NAME | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

shell\_websocket\_##\_name

## [◆ ](#a520876fc32f62533585a1d56c09267ff)GET\_WS\_TRANSPORT\_NAME

| #define GET\_WS\_TRANSPORT\_NAME | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

transport\_shell\_ws\_##\_service

## [◆ ](#a14fb3497eb5b736b8eea2dbb99c63a10)SHELL\_WEBSOCKET\_DEFINE

| #define SHELL\_WEBSOCKET\_DEFINE | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static struct [shell\_websocket](structshell__websocket.md) [GET\_WS\_NAME](#a0e99a36ec4e51975f1129680e480f898)(\_service); \

static struct [shell\_transport](structshell__transport.md) [GET\_WS\_TRANSPORT\_NAME](#a520876fc32f62533585a1d56c09267ff)(\_service) = { \

.api = &[shell\_websocket\_transport\_api](#afd54f1b32a1516cd786320957222356b), \

.ctx = &[GET\_WS\_NAME](#a0e99a36ec4e51975f1129680e480f898)(\_service), \

}

[shell\_websocket\_transport\_api](#afd54f1b32a1516cd786320957222356b)

const struct shell\_transport\_api shell\_websocket\_transport\_api

[shell\_transport](structshell__transport.md)

**Definition** shell.h:724

[shell\_websocket](structshell__websocket.md)

WEBSOCKET-based shell transport.

**Definition** shell\_websocket.h:31

## [◆ ](#af8728c90d47a7b1b5f161ebe20d2139f)SHELL\_WEBSOCKET\_SERVICE\_COUNT

| #define SHELL\_WEBSOCKET\_SERVICE\_COUNT   CONFIG\_SHELL\_WEBSOCKET\_BACKEND\_COUNT |
| --- |

## [◆ ](#ac2c72690650e352b91c6aab106fa45dd)SHELL\_WS\_BUF\_NAME

| #define SHELL\_WS\_BUF\_NAME | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

ws\_recv\_buffer\_##\_service

## [◆ ](#a57a0335bfab8ac4a9d9c4a49a45e4166)SHELL\_WS\_PORT\_NAME

| #define SHELL\_WS\_PORT\_NAME | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

http\_service\_##\_service

## [◆ ](#a870da69234857ceb1966d54d4ee2f278)SHELL\_WS\_TEMP\_RECV\_BUF\_SIZE

| #define SHELL\_WS\_TEMP\_RECV\_BUF\_SIZE   256 |
| --- |

## [◆ ](#a726a23776948ff246176c1ac2c88daa6)WEBSOCKET\_CONSOLE\_DEFINE

| #define WEBSOCKET\_CONSOLE\_DEFINE | ( |  | *\_service*, |
| --- | --- | --- | --- |
|  |  |  | *\_sec\_tag\_list*, |
|  |  |  | *\_sec\_tag\_list\_size* ) |

**Value:**

static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [SHELL\_WS\_PORT\_NAME](#a57a0335bfab8ac4a9d9c4a49a45e4166)(\_service) = \

CONFIG\_SHELL\_WEBSOCKET\_PORT; \

HTTP\_SERVICE\_DEFINE(\_service, \

CONFIG\_SHELL\_WEBSOCKET\_IP\_ADDR, \

&[SHELL\_WS\_PORT\_NAME](#a57a0335bfab8ac4a9d9c4a49a45e4166)(\_service), \

[SHELL\_WEBSOCKET\_SERVICE\_COUNT](#af8728c90d47a7b1b5f161ebe20d2139f), \

[SHELL\_WEBSOCKET\_SERVICE\_COUNT](#af8728c90d47a7b1b5f161ebe20d2139f), \

NULL); \

DEFINE\_WEBSOCKET\_SERVICE(\_service)

[SHELL\_WS\_PORT\_NAME](#a57a0335bfab8ac4a9d9c4a49a45e4166)

#define SHELL\_WS\_PORT\_NAME(\_service)

**Definition** shell\_websocket.h:80

[SHELL\_WEBSOCKET\_SERVICE\_COUNT](#af8728c90d47a7b1b5f161ebe20d2139f)

#define SHELL\_WEBSOCKET\_SERVICE\_COUNT

**Definition** shell\_websocket.h:19

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

## [◆ ](#a134a7de93ded994b49fd781fb289e876)WEBSOCKET\_CONSOLE\_ENABLE

| #define WEBSOCKET\_CONSOLE\_ENABLE | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(void)[shell\_websocket\_enable](#a773f4275294a28b9a25364c5a7d50cab)(&[GET\_WS\_SHELL\_NAME](#a279d727996e63e02ac28e0c94c429938)(\_service))

[GET\_WS\_SHELL\_NAME](#a279d727996e63e02ac28e0c94c429938)

#define GET\_WS\_SHELL\_NAME(\_name)

**Definition** shell\_websocket.h:69

[shell\_websocket\_enable](#a773f4275294a28b9a25364c5a7d50cab)

int shell\_websocket\_enable(const struct shell \*sh)

## Function Documentation

## [◆ ](#a773f4275294a28b9a25364c5a7d50cab)shell\_websocket\_enable()

| | int shell\_websocket\_enable | ( | const struct [shell](structshell.md) \* | *sh* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acc516f1459d0def39779eb8e15c29d80)shell\_websocket\_setup()

| | int shell\_websocket\_setup | ( | int | *ws\_socket*, | | --- | --- | --- | --- | |  |  | void \* | *user\_data* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Variable Documentation

## [◆ ](#afd54f1b32a1516cd786320957222356b)shell\_websocket\_transport\_api

| | const struct [shell\_transport\_api](structshell__transport__api.md) shell\_websocket\_transport\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_websocket.h](shell__websocket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
