---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structshell__mqtt.html
original_path: doxygen/html/structshell__mqtt.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_mqtt Struct Reference

MQTT-based shell transport.
[More...](#details)

`#include <[shell_mqtt.h](shell__mqtt_8h_source.md)>`

| Data Structures | |
| --- | --- |
| struct | [buffer](structshell__mqtt_1_1buffer.md) |

| Public Types | |
| --- | --- |
| enum | [sh\_mqtt\_transport\_state](#ae8805bd53bffb3c001b0be13e9da68a2) { [SHELL\_MQTT\_TRANSPORT\_DISCONNECTED](#ae8805bd53bffb3c001b0be13e9da68a2a4567083cf7063eff87d35b20590f9337) , [SHELL\_MQTT\_TRANSPORT\_CONNECTED](#ae8805bd53bffb3c001b0be13e9da68a2a9c19b6924cec88a03480ed8f84944586) } |
|  | MQTT connection states. [More...](#ae8805bd53bffb3c001b0be13e9da68a2) |
| enum | [sh\_mqtt\_subscribe\_state](#adea25e747457658ebf35665951949466) { [SHELL\_MQTT\_NOT\_SUBSCRIBED](#adea25e747457658ebf35665951949466a03d85db8ae66843ee6d10d03c6bfa11f) , [SHELL\_MQTT\_SUBSCRIBED](#adea25e747457658ebf35665951949466a991a46252c8798c4cf5e21c8622332a8) } |
|  | MQTT subscription states. [More...](#adea25e747457658ebf35665951949466) |
| enum | [sh\_mqtt\_network\_state](#a71d26e0999b931528af231243f70ad13) { [SHELL\_MQTT\_NETWORK\_DISCONNECTED](#a71d26e0999b931528af231243f70ad13a56e20a76049ca54dbbe25f4e925fc66b) , [SHELL\_MQTT\_NETWORK\_CONNECTED](#a71d26e0999b931528af231243f70ad13a8f7feb300421797e162715a89cf8c2c4) } |
|  | Network states. [More...](#a71d26e0999b931528af231243f70ad13) |

| Data Fields | |
| --- | --- |
| char | [device\_id](#a51b8ceee72c5df6a142f06a1d930af45) [((3 \*2)+1)] |
| char | [sub\_topic](#a35965f802271fd1c97247a6f324f9c0e) [((3 \*2)+1)+3] |
| char | [pub\_topic](#a4eb2861d06633f83e4adaf42211d8360) [((3 \*2)+1)+3] |
| [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) | [shell\_handler](#a5887fbed18fce4b9f4fc43ad46ed21d4) |
|  | Handler function registered by shell. |
| struct [ring\_buf](structring__buf.md) | [rx\_rb](#a13909aea8c405ec1f3a4895a764c22ea) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_rb\_buf](#abc23abb31d323cdee9b9b0f3ebbc9bb6) [CONFIG\_SHELL\_MQTT\_RX\_BUF\_SIZE] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [rx\_rb\_ptr](#a501e8f5519a7212f3dbf3d5569afe0b1) |
| struct [shell\_mqtt\_tx\_buf](structshell__mqtt__tx__buf.md) | [tx\_buf](#a04dbbb8b12567cdabf52be196f201879) |
| void \* | [shell\_context](#a20bd84677bfe92acc1f3d49acdbe5a8a) |
|  | Context registered by shell. |
| struct [mqtt\_client](structmqtt__client.md) | [mqtt\_cli](#a74bd401d7ecaf5a31cd28e84a008c042) |
|  | The mqtt client struct. |
| struct [shell\_mqtt::buffer](structshell__mqtt_1_1buffer.md) | [buf](#a909c0a7046181f37977355a4e3c1361d) |
| struct [k\_mutex](structk__mutex.md) | [lock](#aecd5d9972630d81336334e068186c06a) |
| struct sockaddr\_storage | [broker](#ab874f817ad4424fb1fd8f2ad193c0949) |
|  | MQTT Broker details. |
| struct [zsock\_addrinfo](structzsock__addrinfo.md) \* | [haddr](#a44ebb7d1a6e567cc20f8ca2a7b0552c0) |
| struct [zsock\_pollfd](structzsock__pollfd.md) | [fds](#adbd55a6fbbe67d1492cb5fe5e51c75f8) [1] |
| int | [nfds](#ae9f4fa6246332166441f77b1074af8c3) |
| struct [mqtt\_publish\_param](structmqtt__publish__param.md) | [pub\_data](#ab8549c45225a7d24338804cf4517e43f) |
| struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) | [mgmt\_cb](#a40c04efce79d8bfc559ccaebcb6b8020) |
| struct [k\_work\_q](structk__work__q.md) | [workq](#af08ea1a0bbea6cbc64d91a6ccaf6e44c) |
|  | work |
| struct [k\_work](structk__work.md) | [net\_disconnected\_work](#a0b77ec93fb43b67f395842e807c0b58c) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [connect\_dwork](#a289ae146135f3bc886a0be0f1cb6b69f) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [subscribe\_dwork](#a0b01da2449ac6a4c610642929bf2b7dc) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [process\_dwork](#a4a80256d43a0f73431f2f90a5b47eca8) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [publish\_dwork](#a160a56cfd0ea524f771ed48454d11177) |
| enum [shell\_mqtt::sh\_mqtt\_transport\_state](#ae8805bd53bffb3c001b0be13e9da68a2) | [transport\_state](#a5b991d58788207a99986f26aa0ea8961) |
| enum [shell\_mqtt::sh\_mqtt\_subscribe\_state](#adea25e747457658ebf35665951949466) | [subscribe\_state](#ad25a7c092ce351fa7fa7f1a43d2a1ee6) |
| enum [shell\_mqtt::sh\_mqtt\_network\_state](#a71d26e0999b931528af231243f70ad13) | [network\_state](#a87304bd3916d7393425d89ef57132b45) |

## Detailed Description

MQTT-based shell transport.

## Member Enumeration Documentation

## [◆ ](#a71d26e0999b931528af231243f70ad13)sh\_mqtt\_network\_state

| enum [shell\_mqtt::sh\_mqtt\_network\_state](#a71d26e0999b931528af231243f70ad13) |
| --- |

Network states.

| Enumerator | |
| --- | --- |
| SHELL\_MQTT\_NETWORK\_DISCONNECTED |  |
| SHELL\_MQTT\_NETWORK\_CONNECTED |  |

## [◆ ](#adea25e747457658ebf35665951949466)sh\_mqtt\_subscribe\_state

| enum [shell\_mqtt::sh\_mqtt\_subscribe\_state](#adea25e747457658ebf35665951949466) |
| --- |

MQTT subscription states.

| Enumerator | |
| --- | --- |
| SHELL\_MQTT\_NOT\_SUBSCRIBED |  |
| SHELL\_MQTT\_SUBSCRIBED |  |

## [◆ ](#ae8805bd53bffb3c001b0be13e9da68a2)sh\_mqtt\_transport\_state

| enum [shell\_mqtt::sh\_mqtt\_transport\_state](#ae8805bd53bffb3c001b0be13e9da68a2) |
| --- |

MQTT connection states.

| Enumerator | |
| --- | --- |
| SHELL\_MQTT\_TRANSPORT\_DISCONNECTED |  |
| SHELL\_MQTT\_TRANSPORT\_CONNECTED |  |

## Field Documentation

## [◆ ](#ab874f817ad4424fb1fd8f2ad193c0949)broker

| struct sockaddr\_storage shell\_mqtt::broker |
| --- |

MQTT Broker details.

## [◆ ](#a909c0a7046181f37977355a4e3c1361d)buf

| struct [shell\_mqtt::buffer](structshell__mqtt_1_1buffer.md) shell\_mqtt::buf |
| --- |

## [◆ ](#a289ae146135f3bc886a0be0f1cb6b69f)connect\_dwork

| struct [k\_work\_delayable](structk__work__delayable.md) shell\_mqtt::connect\_dwork |
| --- |

## [◆ ](#a51b8ceee72c5df6a142f06a1d930af45)device\_id

| char shell\_mqtt::device\_id[((3 \*2)+1)] |
| --- |

## [◆ ](#adbd55a6fbbe67d1492cb5fe5e51c75f8)fds

| struct [zsock\_pollfd](structzsock__pollfd.md) shell\_mqtt::fds[1] |
| --- |

## [◆ ](#a44ebb7d1a6e567cc20f8ca2a7b0552c0)haddr

| struct [zsock\_addrinfo](structzsock__addrinfo.md)\* shell\_mqtt::haddr |
| --- |

## [◆ ](#aecd5d9972630d81336334e068186c06a)lock

| struct [k\_mutex](structk__mutex.md) shell\_mqtt::lock |
| --- |

## [◆ ](#a40c04efce79d8bfc559ccaebcb6b8020)mgmt\_cb

| struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) shell\_mqtt::mgmt\_cb |
| --- |

## [◆ ](#a74bd401d7ecaf5a31cd28e84a008c042)mqtt\_cli

| struct [mqtt\_client](structmqtt__client.md) shell\_mqtt::mqtt\_cli |
| --- |

The mqtt client struct.

## [◆ ](#a0b77ec93fb43b67f395842e807c0b58c)net\_disconnected\_work

| struct [k\_work](structk__work.md) shell\_mqtt::net\_disconnected\_work |
| --- |

## [◆ ](#a87304bd3916d7393425d89ef57132b45)network\_state

| enum [shell\_mqtt::sh\_mqtt\_network\_state](#a71d26e0999b931528af231243f70ad13) shell\_mqtt::network\_state |
| --- |

## [◆ ](#ae9f4fa6246332166441f77b1074af8c3)nfds

| int shell\_mqtt::nfds |
| --- |

## [◆ ](#a4a80256d43a0f73431f2f90a5b47eca8)process\_dwork

| struct [k\_work\_delayable](structk__work__delayable.md) shell\_mqtt::process\_dwork |
| --- |

## [◆ ](#ab8549c45225a7d24338804cf4517e43f)pub\_data

| struct [mqtt\_publish\_param](structmqtt__publish__param.md) shell\_mqtt::pub\_data |
| --- |

## [◆ ](#a4eb2861d06633f83e4adaf42211d8360)pub\_topic

| char shell\_mqtt::pub\_topic[((3 \*2)+1)+3] |
| --- |

## [◆ ](#a160a56cfd0ea524f771ed48454d11177)publish\_dwork

| struct [k\_work\_delayable](structk__work__delayable.md) shell\_mqtt::publish\_dwork |
| --- |

## [◆ ](#a13909aea8c405ec1f3a4895a764c22ea)rx\_rb

| struct [ring\_buf](structring__buf.md) shell\_mqtt::rx\_rb |
| --- |

## [◆ ](#abc23abb31d323cdee9b9b0f3ebbc9bb6)rx\_rb\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shell\_mqtt::rx\_rb\_buf[CONFIG\_SHELL\_MQTT\_RX\_BUF\_SIZE] |
| --- |

## [◆ ](#a501e8f5519a7212f3dbf3d5569afe0b1)rx\_rb\_ptr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* shell\_mqtt::rx\_rb\_ptr |
| --- |

## [◆ ](#a20bd84677bfe92acc1f3d49acdbe5a8a)shell\_context

| void\* shell\_mqtt::shell\_context |
| --- |

Context registered by shell.

## [◆ ](#a5887fbed18fce4b9f4fc43ad46ed21d4)shell\_handler

| [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) shell\_mqtt::shell\_handler |
| --- |

Handler function registered by shell.

## [◆ ](#a35965f802271fd1c97247a6f324f9c0e)sub\_topic

| char shell\_mqtt::sub\_topic[((3 \*2)+1)+3] |
| --- |

## [◆ ](#a0b01da2449ac6a4c610642929bf2b7dc)subscribe\_dwork

| struct [k\_work\_delayable](structk__work__delayable.md) shell\_mqtt::subscribe\_dwork |
| --- |

## [◆ ](#ad25a7c092ce351fa7fa7f1a43d2a1ee6)subscribe\_state

| enum [shell\_mqtt::sh\_mqtt\_subscribe\_state](#adea25e747457658ebf35665951949466) shell\_mqtt::subscribe\_state |
| --- |

## [◆ ](#a5b991d58788207a99986f26aa0ea8961)transport\_state

| enum [shell\_mqtt::sh\_mqtt\_transport\_state](#ae8805bd53bffb3c001b0be13e9da68a2) shell\_mqtt::transport\_state |
| --- |

## [◆ ](#a04dbbb8b12567cdabf52be196f201879)tx\_buf

| struct [shell\_mqtt\_tx\_buf](structshell__mqtt__tx__buf.md) shell\_mqtt::tx\_buf |
| --- |

## [◆ ](#af08ea1a0bbea6cbc64d91a6ccaf6e44c)workq

| struct [k\_work\_q](structk__work__q.md) shell\_mqtt::workq |
| --- |

work

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_mqtt.h](shell__mqtt_8h_source.md)

- [shell\_mqtt](structshell__mqtt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
