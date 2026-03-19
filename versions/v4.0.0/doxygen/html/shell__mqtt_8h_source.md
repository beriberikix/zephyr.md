---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/shell__mqtt_8h_source.html
original_path: doxygen/html/shell__mqtt_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_mqtt.h

[Go to the documentation of this file.](shell__mqtt_8h.md)

1/\*

2 \* Copyright (c) 2022 G-Technologies Sdn. Bhd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SHELL\_MQTT\_H\_

8#define ZEPHYR\_INCLUDE\_SHELL\_MQTT\_H\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/shell/shell.h](shell_2shell_8h.md)>

12#include <[zephyr/net/socket.h](net_2socket_8h.md)>

13#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

14#include <[zephyr/net/net\_event.h](net__event_8h.md)>

15#include <[zephyr/net/conn\_mgr\_monitor.h](conn__mgr__monitor_8h.md)>

16#include <[zephyr/net/mqtt.h](mqtt_8h.md)>

17#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 23](shell__mqtt_8h.md#a5f0b4a9f9b846f6bc3f078ceda7d1202)#define RX\_RB\_SIZE CONFIG\_SHELL\_MQTT\_RX\_BUF\_SIZE

[ 24](shell__mqtt_8h.md#a5d3fb1970e1e98050006978a14b3d95e)#define TX\_BUF\_SIZE CONFIG\_SHELL\_MQTT\_TX\_BUF\_SIZE

[ 25](shell__mqtt_8h.md#af99d398ab2f0c2107110acf3a96b176e)#define SH\_MQTT\_BUFFER\_SIZE 64

[ 26](shell__mqtt_8h.md#a4758c7d32642633d7896438617afcc62)#define DEVICE\_ID\_BIN\_MAX\_SIZE 3

[ 27](shell__mqtt_8h.md#a81607ea00b70580577866be96df54dbd)#define DEVICE\_ID\_HEX\_MAX\_SIZE ((DEVICE\_ID\_BIN\_MAX\_SIZE \* 2) + 1)

[ 28](shell__mqtt_8h.md#a60136c2ef271308ea19e2d1b0971048e)#define SH\_MQTT\_TOPIC\_MAX\_SIZE DEVICE\_ID\_HEX\_MAX\_SIZE + 3

29

30extern const struct [shell\_transport\_api](structshell__transport__api.md) [shell\_mqtt\_transport\_api](shell__mqtt_8h.md#a5f2ae59f251db48e1937b06a96451bbb);

31

[ 32](structshell__mqtt__tx__buf.md)struct [shell\_mqtt\_tx\_buf](structshell__mqtt__tx__buf.md) {

[ 34](structshell__mqtt__tx__buf.md#aa398ab99503f3b24e53fd81fd8aa08e1) char [buf](structshell__mqtt__tx__buf.md#aa398ab99503f3b24e53fd81fd8aa08e1)[[TX\_BUF\_SIZE](shell__mqtt_8h.md#a5d3fb1970e1e98050006978a14b3d95e)];

35

[ 37](structshell__mqtt__tx__buf.md#a7559f53de11c3f211ce05d08615617da) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structshell__mqtt__tx__buf.md#a7559f53de11c3f211ce05d08615617da);

38};

39

[ 41](structshell__mqtt.md)struct [shell\_mqtt](structshell__mqtt.md) {

[ 42](structshell__mqtt.md#a51b8ceee72c5df6a142f06a1d930af45) char [device\_id](structshell__mqtt.md#a51b8ceee72c5df6a142f06a1d930af45)[[DEVICE\_ID\_HEX\_MAX\_SIZE](shell__mqtt_8h.md#a81607ea00b70580577866be96df54dbd)];

[ 43](structshell__mqtt.md#a35965f802271fd1c97247a6f324f9c0e) char [sub\_topic](structshell__mqtt.md#a35965f802271fd1c97247a6f324f9c0e)[[SH\_MQTT\_TOPIC\_MAX\_SIZE](shell__mqtt_8h.md#a60136c2ef271308ea19e2d1b0971048e)];

[ 44](structshell__mqtt.md#a4eb2861d06633f83e4adaf42211d8360) char [pub\_topic](structshell__mqtt.md#a4eb2861d06633f83e4adaf42211d8360)[[SH\_MQTT\_TOPIC\_MAX\_SIZE](shell__mqtt_8h.md#a60136c2ef271308ea19e2d1b0971048e)];

45

[ 47](structshell__mqtt.md#a5887fbed18fce4b9f4fc43ad46ed21d4) [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) [shell\_handler](structshell__mqtt.md#a5887fbed18fce4b9f4fc43ad46ed21d4);

48

[ 49](structshell__mqtt.md#a13909aea8c405ec1f3a4895a764c22ea) struct [ring\_buf](structring__buf.md) [rx\_rb](structshell__mqtt.md#a13909aea8c405ec1f3a4895a764c22ea);

[ 50](structshell__mqtt.md#abc23abb31d323cdee9b9b0f3ebbc9bb6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_rb\_buf](structshell__mqtt.md#abc23abb31d323cdee9b9b0f3ebbc9bb6)[[RX\_RB\_SIZE](shell__mqtt_8h.md#a5f0b4a9f9b846f6bc3f078ceda7d1202)];

[ 51](structshell__mqtt.md#a501e8f5519a7212f3dbf3d5569afe0b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[rx\_rb\_ptr](structshell__mqtt.md#a501e8f5519a7212f3dbf3d5569afe0b1);

52

[ 53](structshell__mqtt.md#a04dbbb8b12567cdabf52be196f201879) struct [shell\_mqtt\_tx\_buf](structshell__mqtt__tx__buf.md) [tx\_buf](structshell__mqtt.md#a04dbbb8b12567cdabf52be196f201879);

54

[ 56](structshell__mqtt.md#a20bd84677bfe92acc1f3d49acdbe5a8a) void \*[shell\_context](structshell__mqtt.md#a20bd84677bfe92acc1f3d49acdbe5a8a);

57

[ 59](structshell__mqtt.md#a74bd401d7ecaf5a31cd28e84a008c042) struct [mqtt\_client](structmqtt__client.md) [mqtt\_cli](structshell__mqtt.md#a74bd401d7ecaf5a31cd28e84a008c042);

60

61 /\* Buffers for MQTT client. \*/

[ 62](structshell__mqtt_1_1buffer.md) struct [buffer](structshell__mqtt_1_1buffer.md) {

[ 63](structshell__mqtt_1_1buffer.md#a95701e4433f999c6cc37b0933a9186df) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx](structshell__mqtt_1_1buffer.md#a95701e4433f999c6cc37b0933a9186df)[[SH\_MQTT\_BUFFER\_SIZE](shell__mqtt_8h.md#af99d398ab2f0c2107110acf3a96b176e)];

[ 64](structshell__mqtt_1_1buffer.md#a3e2595f4553a3864cde9863f4e8295ae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx](structshell__mqtt_1_1buffer.md#a3e2595f4553a3864cde9863f4e8295ae)[[SH\_MQTT\_BUFFER\_SIZE](shell__mqtt_8h.md#af99d398ab2f0c2107110acf3a96b176e)];

[ 65](structshell__mqtt.md#a909c0a7046181f37977355a4e3c1361d) } [buf](structshell__mqtt.md#a909c0a7046181f37977355a4e3c1361d);

66

[ 67](structshell__mqtt.md#aecd5d9972630d81336334e068186c06a) struct [k\_mutex](structk__mutex.md) [lock](structshell__mqtt.md#aecd5d9972630d81336334e068186c06a);

68

[ 70](structshell__mqtt.md#ab874f817ad4424fb1fd8f2ad193c0949) struct sockaddr\_storage [broker](structshell__mqtt.md#ab874f817ad4424fb1fd8f2ad193c0949);

71

[ 72](structshell__mqtt.md#a44ebb7d1a6e567cc20f8ca2a7b0552c0) struct [zsock\_addrinfo](structzsock__addrinfo.md) \*[haddr](structshell__mqtt.md#a44ebb7d1a6e567cc20f8ca2a7b0552c0);

[ 73](structshell__mqtt.md#adbd55a6fbbe67d1492cb5fe5e51c75f8) struct [zsock\_pollfd](structzsock__pollfd.md) [fds](structshell__mqtt.md#adbd55a6fbbe67d1492cb5fe5e51c75f8)[1];

[ 74](structshell__mqtt.md#ae9f4fa6246332166441f77b1074af8c3) int [nfds](structshell__mqtt.md#ae9f4fa6246332166441f77b1074af8c3);

75

[ 76](structshell__mqtt.md#ab8549c45225a7d24338804cf4517e43f) struct [mqtt\_publish\_param](structmqtt__publish__param.md) [pub\_data](structshell__mqtt.md#ab8549c45225a7d24338804cf4517e43f);

77

[ 78](structshell__mqtt.md#a40c04efce79d8bfc559ccaebcb6b8020) struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) [mgmt\_cb](structshell__mqtt.md#a40c04efce79d8bfc559ccaebcb6b8020);

79

[ 81](structshell__mqtt.md#af08ea1a0bbea6cbc64d91a6ccaf6e44c) struct [k\_work\_q](structk__work__q.md) [workq](structshell__mqtt.md#af08ea1a0bbea6cbc64d91a6ccaf6e44c);

[ 82](structshell__mqtt.md#a0b77ec93fb43b67f395842e807c0b58c) struct [k\_work](structk__work.md) [net\_disconnected\_work](structshell__mqtt.md#a0b77ec93fb43b67f395842e807c0b58c);

[ 83](structshell__mqtt.md#a289ae146135f3bc886a0be0f1cb6b69f) struct [k\_work\_delayable](structk__work__delayable.md) [connect\_dwork](structshell__mqtt.md#a289ae146135f3bc886a0be0f1cb6b69f);

[ 84](structshell__mqtt.md#a0b01da2449ac6a4c610642929bf2b7dc) struct [k\_work\_delayable](structk__work__delayable.md) [subscribe\_dwork](structshell__mqtt.md#a0b01da2449ac6a4c610642929bf2b7dc);

[ 85](structshell__mqtt.md#a4a80256d43a0f73431f2f90a5b47eca8) struct [k\_work\_delayable](structk__work__delayable.md) [process\_dwork](structshell__mqtt.md#a4a80256d43a0f73431f2f90a5b47eca8);

[ 86](structshell__mqtt.md#a160a56cfd0ea524f771ed48454d11177) struct [k\_work\_delayable](structk__work__delayable.md) [publish\_dwork](structshell__mqtt.md#a160a56cfd0ea524f771ed48454d11177);

87

[ 89](structshell__mqtt.md#ae8805bd53bffb3c001b0be13e9da68a2) enum [sh\_mqtt\_transport\_state](structshell__mqtt.md#ae8805bd53bffb3c001b0be13e9da68a2) {

[ 90](structshell__mqtt.md#ae8805bd53bffb3c001b0be13e9da68a2a4567083cf7063eff87d35b20590f9337) [SHELL\_MQTT\_TRANSPORT\_DISCONNECTED](structshell__mqtt.md#ae8805bd53bffb3c001b0be13e9da68a2a4567083cf7063eff87d35b20590f9337),

[ 91](structshell__mqtt.md#ae8805bd53bffb3c001b0be13e9da68a2a9c19b6924cec88a03480ed8f84944586) [SHELL\_MQTT\_TRANSPORT\_CONNECTED](structshell__mqtt.md#ae8805bd53bffb3c001b0be13e9da68a2a9c19b6924cec88a03480ed8f84944586),

[ 92](structshell__mqtt.md#a5b991d58788207a99986f26aa0ea8961) } [transport\_state](structshell__mqtt.md#a5b991d58788207a99986f26aa0ea8961);

93

[ 95](structshell__mqtt.md#adea25e747457658ebf35665951949466) enum [sh\_mqtt\_subscribe\_state](structshell__mqtt.md#adea25e747457658ebf35665951949466) {

[ 96](structshell__mqtt.md#adea25e747457658ebf35665951949466a03d85db8ae66843ee6d10d03c6bfa11f) [SHELL\_MQTT\_NOT\_SUBSCRIBED](structshell__mqtt.md#adea25e747457658ebf35665951949466a03d85db8ae66843ee6d10d03c6bfa11f),

[ 97](structshell__mqtt.md#adea25e747457658ebf35665951949466a991a46252c8798c4cf5e21c8622332a8) [SHELL\_MQTT\_SUBSCRIBED](structshell__mqtt.md#adea25e747457658ebf35665951949466a991a46252c8798c4cf5e21c8622332a8),

[ 98](structshell__mqtt.md#ad25a7c092ce351fa7fa7f1a43d2a1ee6) } [subscribe\_state](structshell__mqtt.md#ad25a7c092ce351fa7fa7f1a43d2a1ee6);

99

[ 101](structshell__mqtt.md#a71d26e0999b931528af231243f70ad13) enum [sh\_mqtt\_network\_state](structshell__mqtt.md#a71d26e0999b931528af231243f70ad13) {

[ 102](structshell__mqtt.md#a71d26e0999b931528af231243f70ad13a56e20a76049ca54dbbe25f4e925fc66b) [SHELL\_MQTT\_NETWORK\_DISCONNECTED](structshell__mqtt.md#a71d26e0999b931528af231243f70ad13a56e20a76049ca54dbbe25f4e925fc66b),

[ 103](structshell__mqtt.md#a71d26e0999b931528af231243f70ad13a8f7feb300421797e162715a89cf8c2c4) [SHELL\_MQTT\_NETWORK\_CONNECTED](structshell__mqtt.md#a71d26e0999b931528af231243f70ad13a8f7feb300421797e162715a89cf8c2c4),

[ 104](structshell__mqtt.md#a87304bd3916d7393425d89ef57132b45) } [network\_state](structshell__mqtt.md#a87304bd3916d7393425d89ef57132b45);

105};

106

[ 107](shell__mqtt_8h.md#ad9508e0c183f9ec9aa08448e48b2082c)#define SHELL\_MQTT\_DEFINE(\_name) \

108 static struct shell\_mqtt \_name##\_shell\_mqtt; \

109 struct shell\_transport \_name = { .api = &shell\_mqtt\_transport\_api, \

110 .ctx = (struct shell\_mqtt \*)&\_name##\_shell\_mqtt }

111

[ 120](shell__mqtt_8h.md#ac3adcf640952f93e747c303724fc31bb)const struct [shell](structshell.md) \*[shell\_backend\_mqtt\_get\_ptr](shell__mqtt_8h.md#ac3adcf640952f93e747c303724fc31bb)(void);

121

[ 134](shell__mqtt_8h.md#a96c08138bf623c1b6ddabfb3742f6f18)bool [shell\_mqtt\_get\_devid](shell__mqtt_8h.md#a96c08138bf623c1b6ddabfb3742f6f18)(char \*id, int id\_max\_len);

135

136#ifdef \_\_cplusplus

137}

138#endif

139

140#endif /\* ZEPHYR\_INCLUDE\_SHELL\_MQTT\_H\_ \*/

[conn\_mgr\_monitor.h](conn__mgr__monitor_8h.md)

API for monitoring network connections and interfaces.

[shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d)

void(\* shell\_transport\_handler\_t)(enum shell\_transport\_evt evt, void \*context)

**Definition** shell.h:624

[kernel.h](kernel_8h.md)

Public kernel APIs.

[mqtt.h](mqtt_8h.md)

MQTT Client Implementation.

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[net\_event.h](net__event_8h.md)

Network Events code public header.

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[ring\_buffer.h](ring__buffer_8h.md)

[shell.h](shell_2shell_8h.md)

[TX\_BUF\_SIZE](shell__mqtt_8h.md#a5d3fb1970e1e98050006978a14b3d95e)

#define TX\_BUF\_SIZE

**Definition** shell\_mqtt.h:24

[RX\_RB\_SIZE](shell__mqtt_8h.md#a5f0b4a9f9b846f6bc3f078ceda7d1202)

#define RX\_RB\_SIZE

**Definition** shell\_mqtt.h:23

[shell\_mqtt\_transport\_api](shell__mqtt_8h.md#a5f2ae59f251db48e1937b06a96451bbb)

const struct shell\_transport\_api shell\_mqtt\_transport\_api

[SH\_MQTT\_TOPIC\_MAX\_SIZE](shell__mqtt_8h.md#a60136c2ef271308ea19e2d1b0971048e)

#define SH\_MQTT\_TOPIC\_MAX\_SIZE

**Definition** shell\_mqtt.h:28

[DEVICE\_ID\_HEX\_MAX\_SIZE](shell__mqtt_8h.md#a81607ea00b70580577866be96df54dbd)

#define DEVICE\_ID\_HEX\_MAX\_SIZE

**Definition** shell\_mqtt.h:27

[shell\_mqtt\_get\_devid](shell__mqtt_8h.md#a96c08138bf623c1b6ddabfb3742f6f18)

bool shell\_mqtt\_get\_devid(char \*id, int id\_max\_len)

Function to define the device ID (devid) for which the shell mqtt backend uses as a client ID when it...

[shell\_backend\_mqtt\_get\_ptr](shell__mqtt_8h.md#ac3adcf640952f93e747c303724fc31bb)

const struct shell \* shell\_backend\_mqtt\_get\_ptr(void)

This function provides pointer to shell mqtt backend instance.

[SH\_MQTT\_BUFFER\_SIZE](shell__mqtt_8h.md#af99d398ab2f0c2107110acf3a96b176e)

#define SH\_MQTT\_BUFFER\_SIZE

**Definition** shell\_mqtt.h:25

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2994

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3985

[k\_work\_q](structk__work__q.md)

A structure used to hold work until it can be processed.

**Definition** kernel.h:4109

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3957

[mqtt\_client](structmqtt__client.md)

MQTT Client definition to maintain information relevant to the client.

**Definition** mqtt.h:494

[mqtt\_publish\_param](structmqtt__publish__param.md)

Parameters for a publish message (PUBLISH).

**Definition** mqtt.h:249

[net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md)

Network Management event callback structure Used to register a callback into the network management e...

**Definition** net\_mgmt.h:145

[ring\_buf](structring__buf.md)

A structure to represent a ring buffer.

**Definition** ring\_buffer.h:41

[shell\_mqtt::buffer](structshell__mqtt_1_1buffer.md)

**Definition** shell\_mqtt.h:62

[shell\_mqtt::buffer::tx](structshell__mqtt_1_1buffer.md#a3e2595f4553a3864cde9863f4e8295ae)

uint8\_t tx[64]

**Definition** shell\_mqtt.h:64

[shell\_mqtt::buffer::rx](structshell__mqtt_1_1buffer.md#a95701e4433f999c6cc37b0933a9186df)

uint8\_t rx[64]

**Definition** shell\_mqtt.h:63

[shell\_mqtt\_tx\_buf](structshell__mqtt__tx__buf.md)

**Definition** shell\_mqtt.h:32

[shell\_mqtt\_tx\_buf::len](structshell__mqtt__tx__buf.md#a7559f53de11c3f211ce05d08615617da)

uint16\_t len

Current tx buf length.

**Definition** shell\_mqtt.h:37

[shell\_mqtt\_tx\_buf::buf](structshell__mqtt__tx__buf.md#aa398ab99503f3b24e53fd81fd8aa08e1)

char buf[CONFIG\_SHELL\_MQTT\_TX\_BUF\_SIZE]

tx buffer.

**Definition** shell\_mqtt.h:34

[shell\_mqtt](structshell__mqtt.md)

MQTT-based shell transport.

**Definition** shell\_mqtt.h:41

[shell\_mqtt::tx\_buf](structshell__mqtt.md#a04dbbb8b12567cdabf52be196f201879)

struct shell\_mqtt\_tx\_buf tx\_buf

**Definition** shell\_mqtt.h:53

[shell\_mqtt::subscribe\_dwork](structshell__mqtt.md#a0b01da2449ac6a4c610642929bf2b7dc)

struct k\_work\_delayable subscribe\_dwork

**Definition** shell\_mqtt.h:84

[shell\_mqtt::net\_disconnected\_work](structshell__mqtt.md#a0b77ec93fb43b67f395842e807c0b58c)

struct k\_work net\_disconnected\_work

**Definition** shell\_mqtt.h:82

[shell\_mqtt::rx\_rb](structshell__mqtt.md#a13909aea8c405ec1f3a4895a764c22ea)

struct ring\_buf rx\_rb

**Definition** shell\_mqtt.h:49

[shell\_mqtt::publish\_dwork](structshell__mqtt.md#a160a56cfd0ea524f771ed48454d11177)

struct k\_work\_delayable publish\_dwork

**Definition** shell\_mqtt.h:86

[shell\_mqtt::shell\_context](structshell__mqtt.md#a20bd84677bfe92acc1f3d49acdbe5a8a)

void \* shell\_context

Context registered by shell.

**Definition** shell\_mqtt.h:56

[shell\_mqtt::connect\_dwork](structshell__mqtt.md#a289ae146135f3bc886a0be0f1cb6b69f)

struct k\_work\_delayable connect\_dwork

**Definition** shell\_mqtt.h:83

[shell\_mqtt::sub\_topic](structshell__mqtt.md#a35965f802271fd1c97247a6f324f9c0e)

char sub\_topic[((3 \*2)+1)+3]

**Definition** shell\_mqtt.h:43

[shell\_mqtt::mgmt\_cb](structshell__mqtt.md#a40c04efce79d8bfc559ccaebcb6b8020)

struct net\_mgmt\_event\_callback mgmt\_cb

**Definition** shell\_mqtt.h:78

[shell\_mqtt::haddr](structshell__mqtt.md#a44ebb7d1a6e567cc20f8ca2a7b0552c0)

struct zsock\_addrinfo \* haddr

**Definition** shell\_mqtt.h:72

[shell\_mqtt::process\_dwork](structshell__mqtt.md#a4a80256d43a0f73431f2f90a5b47eca8)

struct k\_work\_delayable process\_dwork

**Definition** shell\_mqtt.h:85

[shell\_mqtt::pub\_topic](structshell__mqtt.md#a4eb2861d06633f83e4adaf42211d8360)

char pub\_topic[((3 \*2)+1)+3]

**Definition** shell\_mqtt.h:44

[shell\_mqtt::rx\_rb\_ptr](structshell__mqtt.md#a501e8f5519a7212f3dbf3d5569afe0b1)

uint8\_t \* rx\_rb\_ptr

**Definition** shell\_mqtt.h:51

[shell\_mqtt::device\_id](structshell__mqtt.md#a51b8ceee72c5df6a142f06a1d930af45)

char device\_id[((3 \*2)+1)]

**Definition** shell\_mqtt.h:42

[shell\_mqtt::shell\_handler](structshell__mqtt.md#a5887fbed18fce4b9f4fc43ad46ed21d4)

shell\_transport\_handler\_t shell\_handler

Handler function registered by shell.

**Definition** shell\_mqtt.h:47

[shell\_mqtt::transport\_state](structshell__mqtt.md#a5b991d58788207a99986f26aa0ea8961)

enum shell\_mqtt::sh\_mqtt\_transport\_state transport\_state

[shell\_mqtt::sh\_mqtt\_network\_state](structshell__mqtt.md#a71d26e0999b931528af231243f70ad13)

sh\_mqtt\_network\_state

Network states.

**Definition** shell\_mqtt.h:101

[shell\_mqtt::SHELL\_MQTT\_NETWORK\_DISCONNECTED](structshell__mqtt.md#a71d26e0999b931528af231243f70ad13a56e20a76049ca54dbbe25f4e925fc66b)

@ SHELL\_MQTT\_NETWORK\_DISCONNECTED

**Definition** shell\_mqtt.h:102

[shell\_mqtt::SHELL\_MQTT\_NETWORK\_CONNECTED](structshell__mqtt.md#a71d26e0999b931528af231243f70ad13a8f7feb300421797e162715a89cf8c2c4)

@ SHELL\_MQTT\_NETWORK\_CONNECTED

**Definition** shell\_mqtt.h:103

[shell\_mqtt::mqtt\_cli](structshell__mqtt.md#a74bd401d7ecaf5a31cd28e84a008c042)

struct mqtt\_client mqtt\_cli

The mqtt client struct.

**Definition** shell\_mqtt.h:59

[shell\_mqtt::network\_state](structshell__mqtt.md#a87304bd3916d7393425d89ef57132b45)

enum shell\_mqtt::sh\_mqtt\_network\_state network\_state

[shell\_mqtt::buf](structshell__mqtt.md#a909c0a7046181f37977355a4e3c1361d)

struct shell\_mqtt::buffer buf

[shell\_mqtt::pub\_data](structshell__mqtt.md#ab8549c45225a7d24338804cf4517e43f)

struct mqtt\_publish\_param pub\_data

**Definition** shell\_mqtt.h:76

[shell\_mqtt::broker](structshell__mqtt.md#ab874f817ad4424fb1fd8f2ad193c0949)

struct sockaddr\_storage broker

MQTT Broker details.

**Definition** shell\_mqtt.h:70

[shell\_mqtt::rx\_rb\_buf](structshell__mqtt.md#abc23abb31d323cdee9b9b0f3ebbc9bb6)

uint8\_t rx\_rb\_buf[CONFIG\_SHELL\_MQTT\_RX\_BUF\_SIZE]

**Definition** shell\_mqtt.h:50

[shell\_mqtt::subscribe\_state](structshell__mqtt.md#ad25a7c092ce351fa7fa7f1a43d2a1ee6)

enum shell\_mqtt::sh\_mqtt\_subscribe\_state subscribe\_state

[shell\_mqtt::fds](structshell__mqtt.md#adbd55a6fbbe67d1492cb5fe5e51c75f8)

struct zsock\_pollfd fds[1]

**Definition** shell\_mqtt.h:73

[shell\_mqtt::sh\_mqtt\_subscribe\_state](structshell__mqtt.md#adea25e747457658ebf35665951949466)

sh\_mqtt\_subscribe\_state

MQTT subscription states.

**Definition** shell\_mqtt.h:95

[shell\_mqtt::SHELL\_MQTT\_NOT\_SUBSCRIBED](structshell__mqtt.md#adea25e747457658ebf35665951949466a03d85db8ae66843ee6d10d03c6bfa11f)

@ SHELL\_MQTT\_NOT\_SUBSCRIBED

**Definition** shell\_mqtt.h:96

[shell\_mqtt::SHELL\_MQTT\_SUBSCRIBED](structshell__mqtt.md#adea25e747457658ebf35665951949466a991a46252c8798c4cf5e21c8622332a8)

@ SHELL\_MQTT\_SUBSCRIBED

**Definition** shell\_mqtt.h:97

[shell\_mqtt::sh\_mqtt\_transport\_state](structshell__mqtt.md#ae8805bd53bffb3c001b0be13e9da68a2)

sh\_mqtt\_transport\_state

MQTT connection states.

**Definition** shell\_mqtt.h:89

[shell\_mqtt::SHELL\_MQTT\_TRANSPORT\_DISCONNECTED](structshell__mqtt.md#ae8805bd53bffb3c001b0be13e9da68a2a4567083cf7063eff87d35b20590f9337)

@ SHELL\_MQTT\_TRANSPORT\_DISCONNECTED

**Definition** shell\_mqtt.h:90

[shell\_mqtt::SHELL\_MQTT\_TRANSPORT\_CONNECTED](structshell__mqtt.md#ae8805bd53bffb3c001b0be13e9da68a2a9c19b6924cec88a03480ed8f84944586)

@ SHELL\_MQTT\_TRANSPORT\_CONNECTED

**Definition** shell\_mqtt.h:91

[shell\_mqtt::nfds](structshell__mqtt.md#ae9f4fa6246332166441f77b1074af8c3)

int nfds

**Definition** shell\_mqtt.h:74

[shell\_mqtt::lock](structshell__mqtt.md#aecd5d9972630d81336334e068186c06a)

struct k\_mutex lock

**Definition** shell\_mqtt.h:67

[shell\_mqtt::workq](structshell__mqtt.md#af08ea1a0bbea6cbc64d91a6ccaf6e44c)

struct k\_work\_q workq

work

**Definition** shell\_mqtt.h:81

[shell\_transport\_api](structshell__transport__api.md)

Unified shell transport interface.

**Definition** shell.h:646

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:890

[zsock\_addrinfo](structzsock__addrinfo.md)

Definition used when querying address information.

**Definition** socket.h:276

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket\_poll.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_mqtt.h](shell__mqtt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
