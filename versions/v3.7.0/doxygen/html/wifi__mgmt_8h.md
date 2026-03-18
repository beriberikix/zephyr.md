---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/wifi__mgmt_8h.html
original_path: doxygen/html/wifi__mgmt_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_mgmt.h File Reference

WiFi L2 stack public header.
[More...](#details)

`#include <[zephyr/net/net_mgmt.h](net__mgmt_8h_source.md)>`  
`#include <[zephyr/net/wifi.h](wifi_8h_source.md)>`  
`#include <[zephyr/net/ethernet.h](ethernet_8h_source.md)>`  
`#include <[zephyr/net/offloaded_netdev.h](offloaded__netdev_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`

[Go to the source code of this file.](wifi__mgmt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [wifi\_version](structwifi__version.md) |
|  | Wi-Fi version. [More...](structwifi__version.md#details) |
| struct | [wifi\_band\_channel](structwifi__band__channel.md) |
|  | Wi-Fi structure to uniquely identify a band-channel pair. [More...](structwifi__band__channel.md#details) |
| struct | [wifi\_scan\_params](structwifi__scan__params.md) |
|  | Wi-Fi scan parameters structure. [More...](structwifi__scan__params.md#details) |
| struct | [wifi\_scan\_result](structwifi__scan__result.md) |
|  | Wi-Fi scan result, each result is provided to the [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md "Network Management event callback structure Used to register a callback into the network management e...") via its info attribute (see [net\_mgmt.h](net__mgmt_8h.md "Network Management API public header.")). [More...](structwifi__scan__result.md#details) |
| struct | [wifi\_connect\_req\_params](structwifi__connect__req__params.md) |
|  | Wi-Fi connect request parameters. [More...](structwifi__connect__req__params.md#details) |
| struct | [wifi\_status](structwifi__status.md) |
|  | Generic Wi-Fi status for commands and events. [More...](structwifi__status.md#details) |
| struct | [wifi\_iface\_status](structwifi__iface__status.md) |
|  | Wi-Fi interface status. [More...](structwifi__iface__status.md#details) |
| struct | [wifi\_ps\_params](structwifi__ps__params.md) |
|  | Wi-Fi power save parameters. [More...](structwifi__ps__params.md#details) |
| struct | [wifi\_twt\_params](structwifi__twt__params.md) |
|  | Wi-Fi TWT parameters. [More...](structwifi__twt__params.md#details) |
| struct | [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) |
|  | Wi-Fi TWT flow information. [More...](structwifi__twt__flow__info.md#details) |
| struct | [wifi\_ps\_config](structwifi__ps__config.md) |
|  | Wi-Fi power save configuration. [More...](structwifi__ps__config.md#details) |
| struct | [wifi\_reg\_chan\_info](structwifi__reg__chan__info.md) |
|  | Per-channel regulatory attributes. [More...](structwifi__reg__chan__info.md#details) |
| struct | [wifi\_reg\_domain](structwifi__reg__domain.md) |
|  | Regulatory domain information or configuration. [More...](structwifi__reg__domain.md#details) |
| struct | [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) |
|  | Wi-Fi raw scan result. [More...](structwifi__raw__scan__result.md#details) |
| struct | [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) |
|  | AP mode - connected STA details. [More...](structwifi__ap__sta__info.md#details) |
| struct | [wifi\_mode\_info](structwifi__mode__info.md) |
|  | Wi-Fi mode setup. [More...](structwifi__mode__info.md#details) |
| struct | [wifi\_filter\_info](structwifi__filter__info.md) |
|  | Wi-Fi filter setting for monitor, prmoiscuous, TX-injection modes. [More...](structwifi__filter__info.md#details) |
| struct | [wifi\_channel\_info](structwifi__channel__info.md) |
|  | Wi-Fi channel setting for monitor and TX-injection modes. [More...](structwifi__channel__info.md#details) |
| struct | [wifi\_ap\_config\_params](structwifi__ap__config__params.md) |
|  | Wi-Fi AP configuration parameter. [More...](structwifi__ap__config__params.md#details) |
| struct | [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) |
|  | Wi-Fi management API. [More...](structwifi__mgmt__ops.md#details) |
| struct | [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md) |
|  | Wi-Fi management offload API. [More...](structnet__wifi__mgmt__offload.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_REQUEST\_WIFI\_SCAN](group__wifi__mgmt.md#ga1c277da90986fa52dca182c4d922646f)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)) |
|  | Request a Wi-Fi scan. |
| #define | [NET\_REQUEST\_WIFI\_CONNECT](group__wifi__mgmt.md#gaa7ab2a97950a22736bb69f60b459f0f6)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_CONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)) |
|  | Request a Wi-Fi connect. |
| #define | [NET\_REQUEST\_WIFI\_DISCONNECT](group__wifi__mgmt.md#ga90afd8d4e83056463ec6e667ed8ea60a)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)) |
|  | Request a Wi-Fi disconnect. |
| #define | [NET\_REQUEST\_WIFI\_AP\_ENABLE](group__wifi__mgmt.md#ga638d2eb0a5029c1af46a91b523ed8589)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)) |
|  | Request a Wi-Fi access point enable. |
| #define | [NET\_REQUEST\_WIFI\_AP\_DISABLE](group__wifi__mgmt.md#gaf81f62bf4c9e331a095acbf0d24ca1a2)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)) |
|  | Request a Wi-Fi access point disable. |
| #define | [NET\_REQUEST\_WIFI\_IFACE\_STATUS](group__wifi__mgmt.md#ga3e45f6ee3801553619d8eb7d0af506eb)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)) |
|  | Request a Wi-Fi network interface status. |
| #define | [NET\_REQUEST\_WIFI\_PS](group__wifi__mgmt.md#ga68aaced888f98e1ba4e6b61b53e5e2ba)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_PS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)) |
|  | Request a Wi-Fi power save. |
| #define | [NET\_REQUEST\_WIFI\_TWT](group__wifi__mgmt.md#gab84fd7e9ca0bf0b2b9d08889dda26aad)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)) |
|  | Request a Wi-Fi TWT. |
| #define | [NET\_REQUEST\_WIFI\_PS\_CONFIG](group__wifi__mgmt.md#ga1032f3773cfe6130da4d4d498b044ee2)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)) |
|  | Request a Wi-Fi power save configuration. |
| #define | [NET\_REQUEST\_WIFI\_REG\_DOMAIN](group__wifi__mgmt.md#ga2b27d102b779a6d846b375854768fb7f)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)) |
|  | Request a Wi-Fi regulatory domain. |
| #define | [NET\_REQUEST\_WIFI\_MODE](group__wifi__mgmt.md#ga9b4da60a8108b0cc431ac1eecfca0cd0)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)) |
|  | Request current Wi-Fi mode. |
| #define | [NET\_REQUEST\_WIFI\_PACKET\_FILTER](group__wifi__mgmt.md#ga3098e817d12bf4619c9fd2698508fb4e)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)) |
|  | Request Wi-Fi packet filter. |
| #define | [NET\_REQUEST\_WIFI\_CHANNEL](group__wifi__mgmt.md#gad9614d2368f8399850aaec05e40bdc78)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_CHANNEL](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)) |
|  | Request a Wi-Fi channel. |
| #define | [NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gaa3e52e08d89a1104f07207e52b81d503)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)) |
|  | Request a Wi-Fi access point to disconnect a station. |
| #define | [NET\_REQUEST\_WIFI\_VERSION](group__wifi__mgmt.md#ga3e60c29ca9ce95d17a7fff087290f7f1)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_VERSION](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)) |
|  | Request a Wi-Fi version. |
| #define | [NET\_REQUEST\_WIFI\_RTS\_THRESHOLD](group__wifi__mgmt.md#ga22d80ef0ffb15e4286d7b1c3325d5334)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)) |
|  | Request a Wi-Fi RTS threshold. |
| #define | [NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gaf4a78d230f5e0743a6aaf152ddda1c67)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)) |
|  | Request a Wi-Fi AP parameters configuration. |
| #define | [NET\_EVENT\_WIFI\_SCAN\_RESULT](group__wifi__mgmt.md#ga436a927d47eb9abe683b89f2b128cd6e)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e)) |
|  | Event emitted for Wi-Fi scan result. |
| #define | [NET\_EVENT\_WIFI\_SCAN\_DONE](group__wifi__mgmt.md#ga8ce35a12e5338e9a65970382b4a26b88)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018)) |
|  | Event emitted when Wi-Fi scan is done. |
| #define | [NET\_EVENT\_WIFI\_CONNECT\_RESULT](group__wifi__mgmt.md#ga0e8feafcc5efd85d04be91f407c0b7c4)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c)) |
|  | Event emitted for Wi-Fi connect result. |
| #define | [NET\_EVENT\_WIFI\_DISCONNECT\_RESULT](group__wifi__mgmt.md#ga8cbbe69bd60f42fdbb06f4f1e15410c8)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb)) |
|  | Event emitted for Wi-Fi disconnect result. |
| #define | [NET\_EVENT\_WIFI\_IFACE\_STATUS](group__wifi__mgmt.md#ga99e11fc15582b94d4243de7733e47ebb)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14)) |
|  | Event emitted for Wi-Fi network interface status. |
| #define | [NET\_EVENT\_WIFI\_TWT](group__wifi__mgmt.md#gaeb968a5d2a8d68a8c634cca18dbcf9c6)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18)) |
|  | Event emitted for Wi-Fi TWT information. |
| #define | [NET\_EVENT\_WIFI\_TWT\_SLEEP\_STATE](group__wifi__mgmt.md#ga682d95b5d06a9b175c10d712acca8a49)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750)) |
|  | Event emitted for Wi-Fi TWT sleep state. |
| #define | [NET\_EVENT\_WIFI\_RAW\_SCAN\_RESULT](group__wifi__mgmt.md#gaea8d222282ddef6992330763afc759a4)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac)) |
|  | Event emitted for Wi-Fi raw scan result. |
| #define | [NET\_EVENT\_WIFI\_DISCONNECT\_COMPLETE](group__wifi__mgmt.md#ga40027feb7ec42c846fd99b56bbd2256d)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f)) |
|  | Event emitted Wi-Fi disconnect is completed. |
| #define | [NET\_EVENT\_WIFI\_AP\_ENABLE\_RESULT](group__wifi__mgmt.md#ga1d678fbae0f092814392c0ab4087cb73)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b)) |
|  | Event emitted for Wi-Fi access point enable result. |
| #define | [NET\_EVENT\_WIFI\_AP\_DISABLE\_RESULT](group__wifi__mgmt.md#ga104296fdb38edf868bea1a46f572d101)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d)) |
|  | Event emitted for Wi-Fi access point disable result. |
| #define | [NET\_EVENT\_WIFI\_AP\_STA\_CONNECTED](group__wifi__mgmt.md#gacc392179948bfd5bed6702dc8fb5cd9d)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb)) |
|  | Event emitted when Wi-Fi station is connected in AP mode. |
| #define | [NET\_EVENT\_WIFI\_AP\_STA\_DISCONNECTED](group__wifi__mgmt.md#ga3e8154ce1808665dd165f793ddec1673)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e)) |
|  | Event emitted Wi-Fi station is disconnected from AP. |
| #define | [MAX\_REG\_CHAN\_NUM](group__wifi__mgmt.md#ga3a6bfa37bd7850342279d304df20977d)   42 |
|  | Max regulatory channel number. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [scan\_result\_cb\_t](group__wifi__mgmt.md#gad34b366f1c315207ce0da587ca96d8d8)) (struct [net\_if](structnet__if.md) \*iface, int status, struct [wifi\_scan\_result](structwifi__scan__result.md) \*entry) |
|  | Scan result callback. |

| Enumerations | |
| --- | --- |
| enum | [net\_request\_wifi\_cmd](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77) {     [NET\_REQUEST\_WIFI\_CMD\_SCAN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a) = 1 , [NET\_REQUEST\_WIFI\_CMD\_CONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a) , [NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7) , [NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c) ,     [NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf) , [NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de) , [NET\_REQUEST\_WIFI\_CMD\_PS](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a) , [NET\_REQUEST\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09) ,     [NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9) , [NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456) , [NET\_REQUEST\_WIFI\_CMD\_MODE](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899) , [NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5) ,     [NET\_REQUEST\_WIFI\_CMD\_CHANNEL](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2) , [NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a) , [NET\_REQUEST\_WIFI\_CMD\_VERSION](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb) , [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b) ,     [NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM](group__wifi__mgmt.md#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)   } |
|  | Wi-Fi management commands. [More...](group__wifi__mgmt.md#ga99a55137188119f65f9d2bb4f57cac77) |
| enum | [net\_event\_wifi\_cmd](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8) {     [NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e) = 1 , [NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018) , [NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c) , [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb) ,     [NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14) , [NET\_EVENT\_WIFI\_CMD\_TWT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18) , [NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750) , [NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac) ,     [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f) , [NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b) , [NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d) , [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb) ,     [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](group__wifi__mgmt.md#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e)   } |
|  | Wi-Fi management events. [More...](group__wifi__mgmt.md#gac2638308cbb0d268831f1618cf8e1fa8) |
| enum | [wifi\_conn\_status](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) {     [WIFI\_STATUS\_CONN\_SUCCESS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd) = 0 , [WIFI\_STATUS\_CONN\_FAIL](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44) , [WIFI\_STATUS\_CONN\_WRONG\_PASSWORD](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8) , [WIFI\_STATUS\_CONN\_TIMEOUT](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563) ,     [WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4) , [WIFI\_STATUS\_CONN\_LAST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f) , [WIFI\_STATUS\_DISCONN\_FIRST\_STATUS](group__wifi__mgmt.md#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18) = WIFI\_STATUS\_CONN\_LAST\_STATUS   } |
|  | Wi-Fi connect result codes. [More...](group__wifi__mgmt.md#ga86a5741e54aeb3e290142b0de217b8a8) |
| enum | [wifi\_disconn\_reason](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) {     [WIFI\_REASON\_DISCONN\_SUCCESS](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042) = 0 , [WIFI\_REASON\_DISCONN\_UNSPECIFIED](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c) , [WIFI\_REASON\_DISCONN\_USER\_REQUEST](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7) , [WIFI\_REASON\_DISCONN\_AP\_LEAVING](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204) ,     [WIFI\_REASON\_DISCONN\_INACTIVITY](group__wifi__mgmt.md#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6)   } |
|  | Wi-Fi disconnect reason codes. [More...](group__wifi__mgmt.md#gac782af0a60b202fd19597cabb7bd3a9a) |
| enum | [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) {     [WIFI\_STATUS\_AP\_SUCCESS](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) = 0 , [WIFI\_STATUS\_AP\_FAIL](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a) , [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b) , [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15) ,     [WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce) , [WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8) , [WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca) , [WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](group__wifi__mgmt.md#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe)   } |
|  | Wi-Fi AP mode result codes. [More...](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) |
| enum | [wifi\_mgmt\_op](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) { [WIFI\_MGMT\_GET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) = 0 , [WIFI\_MGMT\_SET](group__wifi__mgmt.md#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) = 1 } |
|  | Generic get/set operation for any command. [More...](group__wifi__mgmt.md#gae129d0783276e662575af2314eef86cd) |
| enum | [wifi\_twt\_sleep\_state](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552) { [WIFI\_TWT\_STATE\_SLEEP](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) = 0 , [WIFI\_TWT\_STATE\_AWAKE](group__wifi__mgmt.md#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) = 1 } |
|  | Wi-Fi TWT sleep states. [More...](group__wifi__mgmt.md#ga38c184ea35c02f304cccdf389ca6d552) |

| Functions | |
| --- | --- |
| void | [wifi\_mgmt\_raise\_connect\_result\_event](group__wifi__mgmt.md#ga036416696b1e3bc458ddbaf07a08d69d) (struct [net\_if](structnet__if.md) \*iface, int status) |
|  | Wi-Fi management connect result event. |
| void | [wifi\_mgmt\_raise\_disconnect\_result\_event](group__wifi__mgmt.md#ga3b6edcf9b51afbf7a327d1a344bd7b87) (struct [net\_if](structnet__if.md) \*iface, int status) |
|  | Wi-Fi management disconnect result event. |
| void | [wifi\_mgmt\_raise\_iface\_status\_event](group__wifi__mgmt.md#ga7da6af0747bcba85f8afab30c92b5b43) (struct [net\_if](structnet__if.md) \*iface, struct [wifi\_iface\_status](structwifi__iface__status.md) \*iface\_status) |
|  | Wi-Fi management interface status event. |
| void | [wifi\_mgmt\_raise\_twt\_event](group__wifi__mgmt.md#ga39404d15243ca084b253cae8fc07e374) (struct [net\_if](structnet__if.md) \*iface, struct [wifi\_twt\_params](structwifi__twt__params.md) \*twt\_params) |
|  | Wi-Fi management TWT event. |
| void | [wifi\_mgmt\_raise\_twt\_sleep\_state](group__wifi__mgmt.md#ga18f09a3196588b51d6c0644f82f639d7) (struct [net\_if](structnet__if.md) \*iface, int twt\_sleep\_state) |
|  | Wi-Fi management TWT sleep state event. |
| void | [wifi\_mgmt\_raise\_raw\_scan\_result\_event](group__wifi__mgmt.md#ga71c99913bded844c4ca32ed9155bc470) (struct [net\_if](structnet__if.md) \*iface, struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*raw\_scan\_info) |
|  | Wi-Fi management raw scan result event. |
| void | [wifi\_mgmt\_raise\_disconnect\_complete\_event](group__wifi__mgmt.md#gaa75246d6dc55dada389c9d31e2607d5c) (struct [net\_if](structnet__if.md) \*iface, int status) |
|  | Wi-Fi management disconnect complete event. |
| void | [wifi\_mgmt\_raise\_ap\_enable\_result\_event](group__wifi__mgmt.md#ga67b52edeff76c2211b038f4aa90b8982) (struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status) |
|  | Wi-Fi management AP mode enable result event. |
| void | [wifi\_mgmt\_raise\_ap\_disable\_result\_event](group__wifi__mgmt.md#gadee15c6a492a8ee13bea43812debb5d9) (struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](group__wifi__mgmt.md#gaaf730bf76adc06434c7ac63bf0417884) status) |
|  | Wi-Fi management AP mode disable result event. |
| void | [wifi\_mgmt\_raise\_ap\_sta\_connected\_event](group__wifi__mgmt.md#gac8f17f0aa3e426a5cdb731727b9b9ce3) (struct [net\_if](structnet__if.md) \*iface, struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info) |
|  | Wi-Fi management AP mode STA connected event. |
| void | [wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](group__wifi__mgmt.md#ga49fb9c3908be61d847b31c99be6afc42) (struct [net\_if](structnet__if.md) \*iface, struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info) |
|  | Wi-Fi management AP mode STA disconnected event. |

## Detailed Description

WiFi L2 stack public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_mgmt.h](wifi__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
