---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mqtt_8h.html
original_path: doxygen/html/mqtt_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt.h File Reference

MQTT Client Implementation.
[More...](#details)

`#include <stddef.h>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/net/tls_credentials.h](tls__credentials_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/sys/mutex.h](mutex_8h_source.md)>`  
`#include <[zephyr/net/websocket.h](websocket_8h_source.md)>`

[Go to the source code of this file.](mqtt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mqtt\_utf8](structmqtt__utf8.md) |
|  | Abstracts UTF-8 encoded strings. [More...](structmqtt__utf8.md#details) |
| struct | [mqtt\_binstr](structmqtt__binstr.md) |
|  | Abstracts binary strings. [More...](structmqtt__binstr.md#details) |
| struct | [mqtt\_topic\_alias](structmqtt__topic__alias.md) |
|  | Abstracts aliased topic. [More...](structmqtt__topic__alias.md#details) |
| struct | [mqtt\_topic](structmqtt__topic.md) |
|  | Abstracts MQTT UTF-8 encoded topic that can be subscribed to or published. [More...](structmqtt__topic.md#details) |
| struct | [mqtt\_utf8\_pair](structmqtt__utf8__pair.md) |
|  | Abstracts MQTT UTF-8 encoded string pair. [More...](structmqtt__utf8__pair.md#details) |
| struct | [mqtt\_publish\_message](structmqtt__publish__message.md) |
|  | Parameters for a publish message. [More...](structmqtt__publish__message.md#details) |
| struct | [mqtt\_connack\_param](structmqtt__connack__param.md) |
|  | Parameters for a connection acknowledgment (CONNACK). [More...](structmqtt__connack__param.md#details) |
| struct | [mqtt\_common\_ack\_properties](structmqtt__common__ack__properties.md) |
|  | Common MQTT 5.0 properties shared across all ack-type messages. [More...](structmqtt__common__ack__properties.md#details) |
| struct | [mqtt\_puback\_param](structmqtt__puback__param.md) |
|  | Parameters for MQTT publish acknowledgment (PUBACK). [More...](structmqtt__puback__param.md#details) |
| struct | [mqtt\_pubrec\_param](structmqtt__pubrec__param.md) |
|  | Parameters for MQTT publish receive (PUBREC). [More...](structmqtt__pubrec__param.md#details) |
| struct | [mqtt\_pubrel\_param](structmqtt__pubrel__param.md) |
|  | Parameters for MQTT publish release (PUBREL). [More...](structmqtt__pubrel__param.md#details) |
| struct | [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md) |
|  | Parameters for MQTT publish complete (PUBCOMP). [More...](structmqtt__pubcomp__param.md#details) |
| struct | [mqtt\_suback\_param](structmqtt__suback__param.md) |
|  | Parameters for MQTT subscription acknowledgment (SUBACK). [More...](structmqtt__suback__param.md#details) |
| struct | [mqtt\_unsuback\_param](structmqtt__unsuback__param.md) |
|  | Parameters for MQTT unsubscribe acknowledgment (UNSUBACK). [More...](structmqtt__unsuback__param.md#details) |
| struct | [mqtt\_publish\_param](structmqtt__publish__param.md) |
|  | Parameters for a publish message (PUBLISH). [More...](structmqtt__publish__param.md#details) |
| struct | [mqtt\_subscription\_list](structmqtt__subscription__list.md) |
|  | Parameters for subscribe/unsubscribe message. [More...](structmqtt__subscription__list.md#details) |
| struct | [mqtt\_disconnect\_param](structmqtt__disconnect__param.md) |
|  | Parameters for disconnect message. [More...](structmqtt__disconnect__param.md#details) |
| struct | [mqtt\_auth\_param](structmqtt__auth__param.md) |
|  | Parameters for auth message. [More...](structmqtt__auth__param.md#details) |
| union | [mqtt\_evt\_param](unionmqtt__evt__param.md) |
|  | Defines event parameters notified along with asynchronous events to the application. [More...](unionmqtt__evt__param.md#details) |
| struct | [mqtt\_evt](structmqtt__evt.md) |
|  | Defines MQTT asynchronous event notified to the application. [More...](structmqtt__evt.md#details) |
| struct | [mqtt\_sec\_config](structmqtt__sec__config.md) |
|  | TLS configuration for secure MQTT transports. [More...](structmqtt__sec__config.md#details) |
| struct | [mqtt\_transport](structmqtt__transport.md) |
|  | MQTT transport specific data. [More...](structmqtt__transport.md#details) |
| struct | [mqtt\_internal](structmqtt__internal.md) |
|  | MQTT internal state. [More...](structmqtt__internal.md#details) |
| struct | [mqtt\_client](structmqtt__client.md) |
|  | MQTT Client definition to maintain information relevant to the client. [More...](structmqtt__client.md#details) |

| Macros | |
| --- | --- |
| #define | [MQTT\_UTF8\_LITERAL](group__mqtt__socket.md#gaeaa4fcf581c7d6be755f9a053a3b488c)(literal) |
|  | Initialize UTF-8 encoded string from C literal string. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mqtt\_evt\_cb\_t](group__mqtt__socket.md#gabdf01ededb62ceb4c1608a64cb718a8c)) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_evt](structmqtt__evt.md) \*evt) |
|  | Asynchronous event notification callback registered by the application. |

| Enumerations | |
| --- | --- |
| enum | [mqtt\_evt\_type](group__mqtt__socket.md#ga0071fe013b9920711456ef51cc3e6d91) {     [MQTT\_EVT\_CONNACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3) , [MQTT\_EVT\_DISCONNECT](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032) , [MQTT\_EVT\_PUBLISH](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9) , [MQTT\_EVT\_PUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de) ,     [MQTT\_EVT\_PUBREC](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87) , [MQTT\_EVT\_PUBREL](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2) , [MQTT\_EVT\_PUBCOMP](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8) , [MQTT\_EVT\_SUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb) ,     [MQTT\_EVT\_UNSUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2) , [MQTT\_EVT\_PINGRESP](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5) , [MQTT\_EVT\_AUTH](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a4c5645869d17a4f9391999bfb6bbccde)   } |
|  | MQTT Asynchronous Events notified to the application from the module through the callback registered by the application. [More...](group__mqtt__socket.md#ga0071fe013b9920711456ef51cc3e6d91) |
| enum | [mqtt\_version](group__mqtt__socket.md#ga90d152a4b0986e9a07a12c7c56f5e2a0) { [MQTT\_VERSION\_3\_1\_0](group__mqtt__socket.md#gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7) = 3 , [MQTT\_VERSION\_3\_1\_1](group__mqtt__socket.md#gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e) = 4 , [MQTT\_VERSION\_5\_0](group__mqtt__socket.md#gga90d152a4b0986e9a07a12c7c56f5e2a0a6f11ad8ae7114d8c1fdf85bda376b97f) = 5 } |
|  | MQTT version protocol level. [More...](group__mqtt__socket.md#ga90d152a4b0986e9a07a12c7c56f5e2a0) |
| enum | [mqtt\_qos](group__mqtt__socket.md#ga396015e492b0fee8da37c7168d9cdb33) { [MQTT\_QOS\_0\_AT\_MOST\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e) = 0x00 , [MQTT\_QOS\_1\_AT\_LEAST\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d) = 0x01 , [MQTT\_QOS\_2\_EXACTLY\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117) = 0x02 } |
|  | MQTT Quality of Service types. [More...](group__mqtt__socket.md#ga396015e492b0fee8da37c7168d9cdb33) |
| enum | [mqtt\_conn\_return\_code](group__mqtt__socket.md#gaa17b38ed9c7e65f3e01ad906b24bb618) {     [MQTT\_CONNECTION\_ACCEPTED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050) = 0x00 , [MQTT\_UNACCEPTABLE\_PROTOCOL\_VERSION](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744) = 0x01 , [MQTT\_IDENTIFIER\_REJECTED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141) = 0x02 , [MQTT\_SERVER\_UNAVAILABLE](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3) = 0x03 ,     [MQTT\_BAD\_USER\_NAME\_OR\_PASSWORD](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134) = 0x04 , [MQTT\_NOT\_AUTHORIZED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb) = 0x05   } |
|  | MQTT 3.1 CONNACK return codes. [More...](group__mqtt__socket.md#gaa17b38ed9c7e65f3e01ad906b24bb618) |
| enum | [mqtt\_connack\_reason\_code](group__mqtt__socket.md#gae4c3fb5313addb72961ff578113d183a) {     [MQTT\_CONNACK\_SUCCESS](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aabd738258dd4eaabe5c4ebb4bcf69e5d7) = 0 , [MQTT\_CONNACK\_UNSPECIFIED\_ERROR](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa19f93ee28b2b6841289fade02c351989) = 128 , [MQTT\_CONNACK\_MALFORMED\_PACKET](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa04de5af39cb78ef43bb4c8e701287ed0) = 129 , [MQTT\_CONNACK\_PROTOCOL\_ERROR](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa1fd45d6623840524c7af93a4725025cc) = 130 ,     [MQTT\_CONNACK\_IMPL\_SPECIFIC\_ERROR](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa3819f991bd83ec9b4bf55754f7ef93ee) = 131 , [MQTT\_CONNACK\_UNSUPPORTED\_PROTO\_ERROR](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa2d5037f830538b73ea342bcdc24a9816) = 132 , [MQTT\_CONNACK\_CLIENT\_ID\_NOT\_VALID](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aafe38d9cabe4bee5f3f28484a58c5137f) = 133 , [MQTT\_CONNACK\_BAD\_USERNAME\_OR\_PASS](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa7ac5fefe2b6c3e7946dc84628fd560bd) = 134 ,     [MQTT\_CONNACK\_NOT\_AUTHORIZED](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa83ec9ee9dfb3f649d06cf4d5f527ae4e) = 135 , [MQTT\_CONNACK\_SERVER\_UNAVAILABLE](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa76a813a52ed0d4f53b2646176b2fb5aa) = 136 , [MQTT\_CONNACK\_SERVER\_BUSY](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa30546ae5648049fb5c14161b5ae42aa8) = 137 , [MQTT\_CONNACK\_BANNED](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa5838075a9ed66476838a3fcda7eeba33) = 138 ,     [MQTT\_CONNACK\_BAD\_AUTH\_METHOD](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aafae37cc54cb28707b473d20f53c335d4) = 140 , [MQTT\_CONNACK\_TOPIC\_NAME\_INVALID](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa6fc0c79bac3ec08435fbaec3f80a2eb5) = 144 , [MQTT\_CONNACK\_PACKET\_TOO\_LARGE](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa930dc7b029c625730377653165736040) = 149 , [MQTT\_CONNACK\_QUOTA\_EXCEEDED](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aaa9386156438b2f5b71d57324c54c5f7f) = 151 ,     [MQTT\_CONNACK\_PAYLOAD\_FORMAT\_INVALID](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa8ded9dc2d24ca21f67e97217047f876c) = 153 , [MQTT\_CONNACK\_RETAIN\_NOT\_SUPPORTED](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aab152dc910d3c55de3b64f0ac22611956) = 154 , [MQTT\_CONNACK\_QOS\_NOT\_SUPPORTED](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa75f011e782a11c1c594848daf63e2fb0) = 155 , [MQTT\_CONNACK\_USE\_ANOTHER\_SERVER](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aaf5a1f0040353625ff72dee52fb13f75c) = 156 ,     [MQTT\_CONNACK\_SERVER\_MOVED](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aa8eda2ef9f0e7cc719169370e2cdcf8fa) = 157 , [MQTT\_CONNACK\_CONNECTION\_RATE\_EXCEEDED](group__mqtt__socket.md#ggae4c3fb5313addb72961ff578113d183aae84b943ac946b53a1df9ec409746274e) = 159   } |
|  | MQTT 5.0 CONNACK reason codes (MQTT 5.0, chapter 3.2.2.2). [More...](group__mqtt__socket.md#gae4c3fb5313addb72961ff578113d183a) |
| enum | [mqtt\_suback\_return\_code](group__mqtt__socket.md#gaca1e61c8b14b75544e253cea355274a8) { [MQTT\_SUBACK\_SUCCESS\_QoS\_0](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01) = 0x00 , [MQTT\_SUBACK\_SUCCESS\_QoS\_1](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c) = 0x01 , [MQTT\_SUBACK\_SUCCESS\_QoS\_2](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b) = 0x02 , [MQTT\_SUBACK\_FAILURE](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7) = 0x80 } |
|  | MQTT SUBACK return codes. [More...](group__mqtt__socket.md#gaca1e61c8b14b75544e253cea355274a8) |
| enum | [mqtt\_disconnect\_reason\_code](group__mqtt__socket.md#gaaf563f26ca66841145643a657119d780) {     [MQTT\_DISCONNECT\_NORMAL](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780ac1db368d96389b585530954a493bcf9a) = 0 , [MQTT\_DISCONNECT\_WITH\_WILL\_MSG](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780adc4c0e7ee2f8a1ab654f23b8355b878b) = 4 , [MQTT\_DISCONNECT\_UNSPECIFIED\_ERROR](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780ad9f253248e9fecaae14ee37f0c02d87c) = 128 , [MQTT\_DISCONNECT\_MALFORMED\_PACKET](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780abbca5c088ca0392dca55c87469c571fa) = 129 ,     [MQTT\_DISCONNECT\_PROTOCOL\_ERROR](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780aad7106c041af27373d4e3b87faddafec) = 130 , [MQTT\_DISCONNECT\_IMPL\_SPECIFIC\_ERROR](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a27eb2c713ee9957075da608d1da6ce6c) = 131 , [MQTT\_DISCONNECT\_NOT\_AUTHORIZED](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a4d5c4ec55ee517078c47c59d81fadc78) = 135 , [MQTT\_DISCONNECT\_SERVER\_BUSY](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780ae3d9774a0f77be21b670512eb4a40b86) = 137 ,     [MQTT\_DISCONNECT\_SERVER\_SHUTTING\_DOWN](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a625f16227444f6f306de49aa953acd9d) = 139 , [MQTT\_DISCONNECT\_KEEP\_ALIVE\_TIMEOUT](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780af4b7253dac64f072945054d02d9c2603) = 141 , [MQTT\_DISCONNECT\_SESSION\_TAKE\_OVER](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a11c5eb260bb0d16faeca565aef4f79cf) = 142 , [MQTT\_DISCONNECT\_TOPIC\_FILTER\_INVALID](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a9e863b1f7632caa83efdb41f742f7c6a) = 143 ,     [MQTT\_DISCONNECT\_TOPIC\_NAME\_INVALID](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a053e8c2e553308869a31582cd85d1610) = 144 , [MQTT\_DISCONNECT\_RECV\_MAX\_EXCEEDED](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a55857c640fa90478873eed61a27fa2c0) = 147 , [MQTT\_DISCONNECT\_TOPIC\_ALIAS\_INVALID](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a2421954cb46644bc942827fdeb21cb9c) = 148 , [MQTT\_DISCONNECT\_PACKET\_TOO\_LARGE](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a3639eb9318092b7c642001133e21158b) = 149 ,     [MQTT\_DISCONNECT\_MESSAGE\_RATE\_TOO\_HIGH](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780ab86eac24ac0829257a1b11c8b82e8194) = 150 , [MQTT\_DISCONNECT\_QUOTA\_EXCEEDED](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780ac6db698ae6e2d24b480997adcff7e1a5) = 151 , [MQTT\_DISCONNECT\_ADMIN\_ACTION](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780ace998d2c989d41195d40dda31cf19173) = 152 , [MQTT\_DISCONNECT\_PAYLOAD\_FORMAT\_INVALID](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780afb77e6ac6da08c7d21f093c6068bdd5a) = 153 ,     [MQTT\_DISCONNECT\_RETAIN\_NOT\_SUPPORTED](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780acfd3c3a5b146ed10efb32cd7c6e0cb65) = 154 , [MQTT\_DISCONNECT\_QOS\_NOT\_SUPPORTED](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a70754dd31cc50ca8963ecedf52087a0d) = 155 , [MQTT\_DISCONNECT\_USE\_ANOTHER\_SERVER](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a34cce9b17d556ca9d93d01302ec079e6) = 156 , [MQTT\_DISCONNECT\_SERVER\_MOVED](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780adf78c69bb559f2b471ecdf4380fe21d1) = 157 ,     [MQTT\_DISCONNECT\_SHARED\_SUB\_NOT\_SUPPORTED](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a0cdcb8aed8cf188a50ca6094f3280f98) = 158 , [MQTT\_DISCONNECT\_CONNECTION\_RATE\_EXCEEDED](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780ab418f144f1509e91332486a6f4ee9293) = 159 , [MQTT\_DISCONNECT\_MAX\_CONNECT\_TIME](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780af95f658c0b71d44c6aab3dc3b01ac00c) = 160 , [MQTT\_DISCONNECT\_SUB\_ID\_NOT\_SUPPORTED](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a9d383cae65f31d61bdcf1e38db92bbc4) = 161 ,     [MQTT\_DISCONNECT\_WILDCARD\_SUB\_NOT\_SUPPORTED](group__mqtt__socket.md#ggaaf563f26ca66841145643a657119d780a82b2e5d2b8358fe893d5c682093d13c4) = 162   } |
|  | MQTT Disconnect reason codes (MQTT 5.0, chapter 3.14.2.1). [More...](group__mqtt__socket.md#gaaf563f26ca66841145643a657119d780) |
| enum | [mqtt\_auth\_reason\_code](group__mqtt__socket.md#gacdbeff0450bbcd438cdf35cd543fc6d6) { [MQTT\_AUTH\_SUCCESS](group__mqtt__socket.md#ggacdbeff0450bbcd438cdf35cd543fc6d6a609d75c1d9d37d5340ac979c924efa60) = 0 , [MQTT\_AUTH\_CONTINUE\_AUTHENTICATION](group__mqtt__socket.md#ggacdbeff0450bbcd438cdf35cd543fc6d6add4e38c81c8e1a8b79d911c87612f863) = 24 , [MQTT\_AUTH\_RE\_AUTHENTICATE](group__mqtt__socket.md#ggacdbeff0450bbcd438cdf35cd543fc6d6a46e6b7c5ae59f315137cf0df3aec816a) = 25 } |
|  | MQTT Authenticate reason codes (MQTT 5.0, chapter 3.15.2.1). [More...](group__mqtt__socket.md#gacdbeff0450bbcd438cdf35cd543fc6d6) |
| enum | [mqtt\_transport\_type](group__mqtt__socket.md#gaffc2c3078004cf8d24935be086ad63b4) { [MQTT\_TRANSPORT\_NON\_SECURE](group__mqtt__socket.md#ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a) , [MQTT\_TRANSPORT\_NUM](group__mqtt__socket.md#ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df) } |
|  | MQTT transport type. [More...](group__mqtt__socket.md#gaffc2c3078004cf8d24935be086ad63b4) |

| Functions | |
| --- | --- |
| void | [mqtt\_client\_init](group__mqtt__socket.md#gad1376509ae7c946c840d103d8b59e9a1) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | Initializes the client instance. |
| int | [mqtt\_connect](group__mqtt__socket.md#gad936f28553cb2e771a843512b0a315fa) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | API to request new MQTT client connection. |
| int | [mqtt\_publish](group__mqtt__socket.md#ga57745efa1bf6fbdf7eb1b3f01623e4c7) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_publish\_param](structmqtt__publish__param.md) \*param) |
|  | API to publish messages on topics. |
| int | [mqtt\_publish\_qos1\_ack](group__mqtt__socket.md#gae9069fceec2c018e64cc6beb16aa055c) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_puback\_param](structmqtt__puback__param.md) \*param) |
|  | API used by client to send acknowledgment on receiving QoS1 publish message. |
| int | [mqtt\_publish\_qos2\_receive](group__mqtt__socket.md#gacbe41b83d9c0676d0d4cf01dd91765eb) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_pubrec\_param](structmqtt__pubrec__param.md) \*param) |
|  | API used by client to send acknowledgment on receiving QoS2 publish message. |
| int | [mqtt\_publish\_qos2\_release](group__mqtt__socket.md#ga6c952ed014f78774096bfb6099794803) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_pubrel\_param](structmqtt__pubrel__param.md) \*param) |
|  | API used by client to request release of QoS2 publish message. |
| int | [mqtt\_publish\_qos2\_complete](group__mqtt__socket.md#ga2b17999e845d613f5b0b20015b8204f3) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md) \*param) |
|  | API used by client to send acknowledgment on receiving QoS2 publish release message. |
| int | [mqtt\_subscribe](group__mqtt__socket.md#ga40d226b891b8f62f2c486bbb11ce9678) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_subscription\_list](structmqtt__subscription__list.md) \*param) |
|  | API to request subscription of one or more topics on the connection. |
| int | [mqtt\_unsubscribe](group__mqtt__socket.md#ga4ff43a198e93e332b5553a4d0b59261d) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_subscription\_list](structmqtt__subscription__list.md) \*param) |
|  | API to request unsubscription of one or more topics on the connection. |
| int | [mqtt\_ping](group__mqtt__socket.md#gad1d549d37b69a61e1bf8d9d213e02ca8) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | API to send MQTT ping. |
| int | [mqtt\_disconnect](group__mqtt__socket.md#ga0bc7d91da88c2fbc25108d89ce4318c4) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_disconnect\_param](structmqtt__disconnect__param.md) \*param) |
|  | API to disconnect MQTT connection. |
| int | [mqtt\_auth](group__mqtt__socket.md#gad4d870f91a7d594c3a7325ab6de87a02) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_auth\_param](structmqtt__auth__param.md) \*param) |
|  | API to send an authentication packet to the server. |
| int | [mqtt\_abort](group__mqtt__socket.md#gafb2df41fad7c318f9fe75919919139bd) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | API to abort MQTT connection. |
| int | [mqtt\_live](group__mqtt__socket.md#ga8b87710d01076c8e51b1a75634168269) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | This API should be called periodically for the client to be able to keep the connection alive by sending Ping Requests if need be. |
| int | [mqtt\_keepalive\_time\_left](group__mqtt__socket.md#gaa16bf7b0597ad00c4a3943235579e86b) (const struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | Helper function to determine when next keep alive message should be sent. |
| int | [mqtt\_input](group__mqtt__socket.md#ga2dbc3c158d63a6f57b362be94c22660a) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | Receive an incoming MQTT packet. |
| int | [mqtt\_read\_publish\_payload](group__mqtt__socket.md#ga3559cdd6093d75c6fe6792ec2a453172) (struct [mqtt\_client](structmqtt__client.md) \*client, void \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Read the payload of the received PUBLISH message. |
| int | [mqtt\_read\_publish\_payload\_blocking](group__mqtt__socket.md#ga05213aceaa9e9cbbfaa9bab7a78b3d25) (struct [mqtt\_client](structmqtt__client.md) \*client, void \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Blocking version of [mqtt\_read\_publish\_payload](group__mqtt__socket.md#ga3559cdd6093d75c6fe6792ec2a453172 "mqtt_read_publish_payload") function. |
| int | [mqtt\_readall\_publish\_payload](group__mqtt__socket.md#ga31823965ec34a253793b40b50e800417) (struct [mqtt\_client](structmqtt__client.md) \*client, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Blocking version of [mqtt\_read\_publish\_payload](group__mqtt__socket.md#ga3559cdd6093d75c6fe6792ec2a453172 "mqtt_read_publish_payload") function which runs until the required number of bytes are read. |

## Detailed Description

MQTT Client Implementation.

Note
:   The implementation assumes TCP module is enabled.
:   By default the implementation uses MQTT version 3.1.1.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mqtt.h](mqtt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
