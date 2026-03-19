---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/shell__websocket_8h_source.html
original_path: doxygen/html/shell__websocket_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_websocket.h

[Go to the documentation of this file.](shell__websocket_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SHELL\_WEBSOCKET\_H\_

8#define ZEPHYR\_INCLUDE\_SHELL\_WEBSOCKET\_H\_

9

10#include <[zephyr/net/socket.h](net_2socket_8h.md)>

11#include <[zephyr/net/http/server.h](server_8h.md)>

12#include <[zephyr/net/http/service.h](service_8h.md)>

13#include <[zephyr/shell/shell.h](shell_2shell_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 19](shell__websocket_8h.md#af8728c90d47a7b1b5f161ebe20d2139f)#define SHELL\_WEBSOCKET\_SERVICE\_COUNT CONFIG\_SHELL\_WEBSOCKET\_BACKEND\_COUNT

20

[ 22](structshell__websocket__line__buf.md)struct [shell\_websocket\_line\_buf](structshell__websocket__line__buf.md) {

[ 24](structshell__websocket__line__buf.md#a10a756bb4194410962dfffa59338664c) char [buf](structshell__websocket__line__buf.md#a10a756bb4194410962dfffa59338664c)[CONFIG\_SHELL\_WEBSOCKET\_LINE\_BUF\_SIZE];

25

[ 27](structshell__websocket__line__buf.md#a336e882343a970379b95fcf8d8998f59) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structshell__websocket__line__buf.md#a336e882343a970379b95fcf8d8998f59);

28};

29

[ 31](structshell__websocket.md)struct [shell\_websocket](structshell__websocket.md) {

[ 33](structshell__websocket.md#a747ef2882612e8fe15942df4458f9216) [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) [shell\_handler](structshell__websocket.md#a747ef2882612e8fe15942df4458f9216);

34

[ 36](structshell__websocket.md#a00741fbfef55e28a7016f34152aa3779) void \*[shell\_context](structshell__websocket.md#a00741fbfef55e28a7016f34152aa3779);

37

[ 39](structshell__websocket.md#a01ef6e378e2b07f41d32c4bb5ae55d9d) struct [shell\_websocket\_line\_buf](structshell__websocket__line__buf.md) [line\_out](structshell__websocket.md#a01ef6e378e2b07f41d32c4bb5ae55d9d);

40

[ 42](structshell__websocket.md#a3d8706b299743959341501b42c7d67bf) struct [zsock\_pollfd](structzsock__pollfd.md) [fds](structshell__websocket.md#a3d8706b299743959341501b42c7d67bf)[1];

43

[ 45](structshell__websocket.md#ab2458014f7c0ae75ffaf8c3e483d8c4f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_buf](structshell__websocket.md#ab2458014f7c0ae75ffaf8c3e483d8c4f)[[CONFIG\_SHELL\_CMD\_BUFF\_SIZE](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)];

46

[ 48](structshell__websocket.md#a3b5c1356b3557631902ad1ce518b28ff) size\_t [rx\_len](structshell__websocket.md#a3b5c1356b3557631902ad1ce518b28ff);

49

[ 51](structshell__websocket.md#a775f4d94edd129f2d0902fcbc9cbf80d) struct [k\_mutex](structk__mutex.md) [rx\_lock](structshell__websocket.md#a775f4d94edd129f2d0902fcbc9cbf80d);

52

[ 57](structshell__websocket.md#a6ee67d20a4d76e21fc0f953cfcfd6d0b) struct [k\_work\_delayable](structk__work__delayable.md) [send\_work](structshell__websocket.md#a6ee67d20a4d76e21fc0f953cfcfd6d0b);

[ 58](structshell__websocket.md#a3881d0824985c9b06911b60ca17dc220) struct [k\_work\_sync](structk__work__sync.md) [work\_sync](structshell__websocket.md#a3881d0824985c9b06911b60ca17dc220);

59

[ 61](structshell__websocket.md#aa2ba4d7ab718bb988a4adf1eebe30430) bool [output\_lock](structshell__websocket.md#aa2ba4d7ab718bb988a4adf1eebe30430);

62};

63

64extern const struct [shell\_transport\_api](structshell__transport__api.md) [shell\_websocket\_transport\_api](shell__websocket_8h.md#afd54f1b32a1516cd786320957222356b);

[ 65](shell__websocket_8h.md#a3b510cbaf4d17fc6aa4202a692c89627)int [shell\_websocket\_setup](shell__websocket_8h.md#a3b510cbaf4d17fc6aa4202a692c89627)(int ws\_socket, struct [http\_request\_ctx](structhttp__request__ctx.md) \*request\_ctx, void \*user\_data);

[ 66](shell__websocket_8h.md#a773f4275294a28b9a25364c5a7d50cab)int [shell\_websocket\_enable](shell__websocket_8h.md#a773f4275294a28b9a25364c5a7d50cab)(const struct [shell](structshell.md) \*sh);

67

[ 68](shell__websocket_8h.md#a0e99a36ec4e51975f1129680e480f898)#define GET\_WS\_NAME(\_service) ws\_ctx\_##\_service

[ 69](shell__websocket_8h.md#a279d727996e63e02ac28e0c94c429938)#define GET\_WS\_SHELL\_NAME(\_name) shell\_websocket\_##\_name

[ 70](shell__websocket_8h.md#a520876fc32f62533585a1d56c09267ff)#define GET\_WS\_TRANSPORT\_NAME(\_service) transport\_shell\_ws\_##\_service

[ 71](shell__websocket_8h.md#ae81e574d5e40193417675353a0221cb0)#define GET\_WS\_DETAIL\_NAME(\_service) ws\_res\_detail\_##\_service

72

[ 73](shell__websocket_8h.md#a14fb3497eb5b736b8eea2dbb99c63a10)#define SHELL\_WEBSOCKET\_DEFINE(\_service) \

74 static struct shell\_websocket GET\_WS\_NAME(\_service); \

75 static struct shell\_transport GET\_WS\_TRANSPORT\_NAME(\_service) = { \

76 .api = &shell\_websocket\_transport\_api, \

77 .ctx = &GET\_WS\_NAME(\_service), \

78 }

79

[ 80](shell__websocket_8h.md#a57a0335bfab8ac4a9d9c4a49a45e4166)#define SHELL\_WS\_PORT\_NAME(\_service) http\_service\_##\_service

[ 81](shell__websocket_8h.md#ac2c72690650e352b91c6aab106fa45dd)#define SHELL\_WS\_BUF\_NAME(\_service) ws\_recv\_buffer\_##\_service

[ 82](shell__websocket_8h.md#a870da69234857ceb1966d54d4ee2f278)#define SHELL\_WS\_TEMP\_RECV\_BUF\_SIZE 256

83

[ 84](shell__websocket_8h.md#af32434fee39da58ad013d9b2f2670ddc)#define DEFINE\_WEBSOCKET\_HTTP\_SERVICE(\_service) \

85 uint8\_t SHELL\_WS\_BUF\_NAME(\_service)[SHELL\_WS\_TEMP\_RECV\_BUF\_SIZE]; \

86 struct http\_resource\_detail\_websocket \

87 GET\_WS\_DETAIL\_NAME(\_service) = { \

88 .common = { \

89 .type = HTTP\_RESOURCE\_TYPE\_WEBSOCKET, \

90 \

91 /\* We need HTTP/1.1 GET method for upgrading \*/ \

92 .bitmask\_of\_supported\_http\_methods = BIT(HTTP\_GET), \

93 }, \

94 .cb = shell\_websocket\_setup, \

95 .data\_buffer = SHELL\_WS\_BUF\_NAME(\_service), \

96 .data\_buffer\_len = sizeof(SHELL\_WS\_BUF\_NAME(\_service)), \

97 .user\_data = &GET\_WS\_NAME(\_service), \

98 }; \

99 HTTP\_RESOURCE\_DEFINE(ws\_resource\_##\_service, \_service, \

100 "/" CONFIG\_SHELL\_WEBSOCKET\_ENDPOINT\_URL, \

101 &GET\_WS\_DETAIL\_NAME(\_service))

102

[ 103](shell__websocket_8h.md#aba77cc40652e7aed5f1203cfea2ecd91)#define DEFINE\_WEBSOCKET\_SERVICE(\_service) \

104 SHELL\_WEBSOCKET\_DEFINE(\_service); \

105 SHELL\_DEFINE(shell\_websocket\_##\_service, \

106 CONFIG\_SHELL\_WEBSOCKET\_PROMPT, \

107 &GET\_WS\_TRANSPORT\_NAME(\_service), \

108 CONFIG\_SHELL\_WEBSOCKET\_LOG\_MESSAGE\_QUEUE\_SIZE, \

109 CONFIG\_SHELL\_WEBSOCKET\_LOG\_MESSAGE\_QUEUE\_TIMEOUT, \

110 SHELL\_FLAG\_OLF\_CRLF); \

111 DEFINE\_WEBSOCKET\_HTTP\_SERVICE(\_service)

112

113#if defined(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)

114/\* Use a secure connection only for Websocket. \*/

115#define WEBSOCKET\_CONSOLE\_DEFINE(\_service, \_sec\_tag\_list, \_sec\_tag\_list\_size) \

116 static uint16\_t SHELL\_WS\_PORT\_NAME(\_service) = \

117 CONFIG\_SHELL\_WEBSOCKET\_PORT; \

118 HTTPS\_SERVICE\_DEFINE(\_service, \

119 CONFIG\_SHELL\_WEBSOCKET\_IP\_ADDR, \

120 &SHELL\_WS\_PORT\_NAME(\_service), \

121 SHELL\_WEBSOCKET\_SERVICE\_COUNT, \

122 SHELL\_WEBSOCKET\_SERVICE\_COUNT, \

123 NULL, \

124 NULL, \

125 \_sec\_tag\_list, \

126 \_sec\_tag\_list\_size); \

127 DEFINE\_WEBSOCKET\_SERVICE(\_service); \

128

129

130#else /\* CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS \*/

131/\* TLS not possible so define only normal HTTP service \*/

[ 132](shell__websocket_8h.md#a726a23776948ff246176c1ac2c88daa6)#define WEBSOCKET\_CONSOLE\_DEFINE(\_service, \_sec\_tag\_list, \_sec\_tag\_list\_size) \

133 static uint16\_t SHELL\_WS\_PORT\_NAME(\_service) = \

134 CONFIG\_SHELL\_WEBSOCKET\_PORT; \

135 HTTP\_SERVICE\_DEFINE(\_service, \

136 CONFIG\_SHELL\_WEBSOCKET\_IP\_ADDR, \

137 &SHELL\_WS\_PORT\_NAME(\_service), \

138 SHELL\_WEBSOCKET\_SERVICE\_COUNT, \

139 SHELL\_WEBSOCKET\_SERVICE\_COUNT, \

140 NULL, NULL); \

141 DEFINE\_WEBSOCKET\_SERVICE(\_service)

142

143#endif /\* CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS \*/

144

[ 145](shell__websocket_8h.md#a134a7de93ded994b49fd781fb289e876)#define WEBSOCKET\_CONSOLE\_ENABLE(\_service) \

146 (void)shell\_websocket\_enable(&GET\_WS\_SHELL\_NAME(\_service))

147

148#ifdef \_\_cplusplus

149}

150#endif

151

152#endif /\* ZEPHYR\_INCLUDE\_SHELL\_WEBSOCKET\_H\_ \*/

[shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d)

void(\* shell\_transport\_handler\_t)(enum shell\_transport\_evt evt, void \*context)

**Definition** shell.h:646

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[server.h](server_8h.md)

HTTP server API.

[service.h](service_8h.md)

HTTP service API.

[shell.h](shell_2shell_8h.md)

[CONFIG\_SHELL\_CMD\_BUFF\_SIZE](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)

#define CONFIG\_SHELL\_CMD\_BUFF\_SIZE

**Definition** shell.h:34

[shell\_websocket\_setup](shell__websocket_8h.md#a3b510cbaf4d17fc6aa4202a692c89627)

int shell\_websocket\_setup(int ws\_socket, struct http\_request\_ctx \*request\_ctx, void \*user\_data)

[shell\_websocket\_enable](shell__websocket_8h.md#a773f4275294a28b9a25364c5a7d50cab)

int shell\_websocket\_enable(const struct shell \*sh)

[shell\_websocket\_transport\_api](shell__websocket_8h.md#afd54f1b32a1516cd786320957222356b)

const struct shell\_transport\_api shell\_websocket\_transport\_api

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[http\_request\_ctx](structhttp__request__ctx.md)

HTTP request context.

**Definition** server.h:187

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4034

[k\_work\_sync](structk__work__sync.md)

A structure holding internal state for a pending synchronous operation on a work item or queue.

**Definition** kernel.h:4117

[shell\_transport\_api](structshell__transport__api.md)

Unified shell transport interface.

**Definition** shell.h:668

[shell\_websocket\_line\_buf](structshell__websocket__line__buf.md)

Line buffer structure.

**Definition** shell\_websocket.h:22

[shell\_websocket\_line\_buf::buf](structshell__websocket__line__buf.md#a10a756bb4194410962dfffa59338664c)

char buf[CONFIG\_SHELL\_WEBSOCKET\_LINE\_BUF\_SIZE]

Line buffer.

**Definition** shell\_websocket.h:24

[shell\_websocket\_line\_buf::len](structshell__websocket__line__buf.md#a336e882343a970379b95fcf8d8998f59)

uint16\_t len

Current line length.

**Definition** shell\_websocket.h:27

[shell\_websocket](structshell__websocket.md)

WEBSOCKET-based shell transport.

**Definition** shell\_websocket.h:31

[shell\_websocket::shell\_context](structshell__websocket.md#a00741fbfef55e28a7016f34152aa3779)

void \* shell\_context

Context registered by shell.

**Definition** shell\_websocket.h:36

[shell\_websocket::line\_out](structshell__websocket.md#a01ef6e378e2b07f41d32c4bb5ae55d9d)

struct shell\_websocket\_line\_buf line\_out

Buffer for outgoing line.

**Definition** shell\_websocket.h:39

[shell\_websocket::work\_sync](structshell__websocket.md#a3881d0824985c9b06911b60ca17dc220)

struct k\_work\_sync work\_sync

**Definition** shell\_websocket.h:58

[shell\_websocket::rx\_len](structshell__websocket.md#a3b5c1356b3557631902ad1ce518b28ff)

size\_t rx\_len

Number of data bytes within the input buffer.

**Definition** shell\_websocket.h:48

[shell\_websocket::fds](structshell__websocket.md#a3d8706b299743959341501b42c7d67bf)

struct zsock\_pollfd fds[1]

Array for sockets used by the websocket service.

**Definition** shell\_websocket.h:42

[shell\_websocket::send\_work](structshell__websocket.md#a6ee67d20a4d76e21fc0f953cfcfd6d0b)

struct k\_work\_delayable send\_work

The delayed work is used to send non-lf terminated output that has been around for "too long".

**Definition** shell\_websocket.h:57

[shell\_websocket::shell\_handler](structshell__websocket.md#a747ef2882612e8fe15942df4458f9216)

shell\_transport\_handler\_t shell\_handler

Handler function registered by shell.

**Definition** shell\_websocket.h:33

[shell\_websocket::rx\_lock](structshell__websocket.md#a775f4d94edd129f2d0902fcbc9cbf80d)

struct k\_mutex rx\_lock

Mutex protecting the input buffer access.

**Definition** shell\_websocket.h:51

[shell\_websocket::output\_lock](structshell__websocket.md#aa2ba4d7ab718bb988a4adf1eebe30430)

bool output\_lock

If set, no output is sent to the WEBSOCKET client.

**Definition** shell\_websocket.h:61

[shell\_websocket::rx\_buf](structshell__websocket.md#ab2458014f7c0ae75ffaf8c3e483d8c4f)

uint8\_t rx\_buf[CONFIG\_SHELL\_CMD\_BUFF\_SIZE]

Input buffer.

**Definition** shell\_websocket.h:45

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:912

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket\_poll.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_websocket.h](shell__websocket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
