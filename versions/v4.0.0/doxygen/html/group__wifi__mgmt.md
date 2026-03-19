---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__wifi__mgmt.html
original_path: doxygen/html/group__wifi__mgmt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Wi-Fi Management

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Wi-Fi Management API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [wifi\_cipher\_desc](structwifi__cipher__desc.md) |
| struct | [wifi\_eap\_cipher\_config](structwifi__eap__cipher__config.md) |
| struct | [wifi\_eap\_config](structwifi__eap__config.md) |
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
| struct | [wifi\_enterprise\_creds\_params](structwifi__enterprise__creds__params.md) |
|  | Wi-Fi enterprise mode credentials. [More...](structwifi__enterprise__creds__params.md#details) |
| struct | [wifi\_ps\_config](structwifi__ps__config.md) |
|  | Wi-Fi power save configuration. [More...](structwifi__ps__config.md#details) |
| struct | [wifi\_11k\_params](structwifi__11k__params.md) |
|  | Wi-Fi 11k parameters. [More...](structwifi__11k__params.md#details) |
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
| struct | [wifi\_wps\_config\_params](structwifi__wps__config__params.md) |
|  | Wi-Fi wps setup. [More...](structwifi__wps__config__params.md#details) |
| struct | [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) |
|  | Wi-Fi management API. [More...](structwifi__mgmt__ops.md#details) |
| struct | [net\_wifi\_mgmt\_offload](structnet__wifi__mgmt__offload.md) |
|  | Wi-Fi management offload API. [More...](structnet__wifi__mgmt__offload.md#details) |

| Macros | |
| --- | --- |
| #define | [WIFI\_COUNTRY\_CODE\_LEN](#ga6766ef7bcb001f1fb526a4083b6cd8bc)   2 |
|  | Length of the country code string. |
| #define | [WIFI\_SSID\_MAX\_LEN](#gad62c60666c9fdffe2e0e9c4388f87886)   32 |
|  | Max SSID length. |
| #define | [WIFI\_PSK\_MIN\_LEN](#gaa8e19abf8c85f237ba5033740ceff553)   8 |
|  | Minimum PSK length. |
| #define | [WIFI\_PSK\_MAX\_LEN](#gad7c3b99c974b342935180a28fdc5ddfc)   64 |
|  | Maximum PSK length. |
| #define | [WIFI\_SAE\_PSWD\_MAX\_LEN](#gab63fa744cc2e049cfd635ab0a187971f)   128 |
|  | Max SAW password length. |
| #define | [WIFI\_MAC\_ADDR\_LEN](#ga29409ff83a53c6464decdde9bdd04de6)   6 |
|  | MAC address length. |
| #define | [WIFI\_ENT\_IDENTITY\_MAX\_LEN](#gac6904487661f157274b0b60833f6684a)   64 |
|  | Max enterprise identity length. |
| #define | [WIFI\_ENT\_PSWD\_MAX\_LEN](#gae2fd55924f4078187431f7a1184f217f)   128 |
|  | Max enterprise password length. |
| #define | [WIFI\_CHANNEL\_MIN](#ga260e473dac1e823fd298a2c982470e0b)   1 |
|  | Minimum channel number. |
| #define | [WIFI\_CHANNEL\_MAX](#ga8ea9141108f93b419f6a6530bf67bd95)   233 |
|  | Maximum channel number. |
| #define | [WIFI\_CHANNEL\_ANY](#ga3876cd718af9f8a7b3682546da854544)   255 |
|  | Any channel number. |
| #define | [WIFI\_INTERFACE\_INDEX\_MIN](#gaa1a74ef94af57a7ea966c691c065a46d)   1 |
|  | Network interface index min value. |
| #define | [WIFI\_INTERFACE\_INDEX\_MAX](#gaa6cbecd7d4197d453038d3da7ef6be7b)   255 |
|  | Network interface index max value. |
| #define | [NET\_REQUEST\_WIFI\_SCAN](#ga1c277da90986fa52dca182c4d922646f)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_SCAN](#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)) |
|  | Request a Wi-Fi scan. |
| #define | [NET\_REQUEST\_WIFI\_CONNECT](#gaa7ab2a97950a22736bb69f60b459f0f6)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_CONNECT](#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)) |
|  | Request a Wi-Fi connect. |
| #define | [NET\_REQUEST\_WIFI\_DISCONNECT](#ga90afd8d4e83056463ec6e667ed8ea60a)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)) |
|  | Request a Wi-Fi disconnect. |
| #define | [NET\_REQUEST\_WIFI\_AP\_ENABLE](#ga638d2eb0a5029c1af46a91b523ed8589)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)) |
|  | Request a Wi-Fi access point enable. |
| #define | [NET\_REQUEST\_WIFI\_AP\_DISABLE](#gaf81f62bf4c9e331a095acbf0d24ca1a2)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)) |
|  | Request a Wi-Fi access point disable. |
| #define | [NET\_REQUEST\_WIFI\_IFACE\_STATUS](#ga3e45f6ee3801553619d8eb7d0af506eb)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)) |
|  | Request a Wi-Fi network interface status. |
| #define | [NET\_REQUEST\_WIFI\_11K\_CONFIG](#gadd9b5b206c7ee2e40c30a37c7b4fc002)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6)) |
| #define | [NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST](#ga4a2b1e8befd7376749b1d4fbcf98376f)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST](#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede)) |
| #define | [NET\_REQUEST\_WIFI\_PS](#ga68aaced888f98e1ba4e6b61b53e5e2ba)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_PS](#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)) |
|  | Request a Wi-Fi power save. |
| #define | [NET\_REQUEST\_WIFI\_TWT](#gab84fd7e9ca0bf0b2b9d08889dda26aad)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_TWT](#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)) |
|  | Request a Wi-Fi TWT. |
| #define | [NET\_REQUEST\_WIFI\_PS\_CONFIG](#ga1032f3773cfe6130da4d4d498b044ee2)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)) |
|  | Request a Wi-Fi power save configuration. |
| #define | [NET\_REQUEST\_WIFI\_REG\_DOMAIN](#ga2b27d102b779a6d846b375854768fb7f)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)) |
|  | Request a Wi-Fi regulatory domain. |
| #define | [NET\_REQUEST\_WIFI\_MODE](#ga9b4da60a8108b0cc431ac1eecfca0cd0)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_MODE](#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)) |
|  | Request current Wi-Fi mode. |
| #define | [NET\_REQUEST\_WIFI\_PACKET\_FILTER](#ga3098e817d12bf4619c9fd2698508fb4e)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)) |
|  | Request Wi-Fi packet filter. |
| #define | [NET\_REQUEST\_WIFI\_CHANNEL](#gad9614d2368f8399850aaec05e40bdc78)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_CHANNEL](#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)) |
|  | Request a Wi-Fi channel. |
| #define | [NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT](#gaa3e52e08d89a1104f07207e52b81d503)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)) |
|  | Request a Wi-Fi access point to disconnect a station. |
| #define | [NET\_REQUEST\_WIFI\_VERSION](#ga3e60c29ca9ce95d17a7fff087290f7f1)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_VERSION](#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)) |
|  | Request a Wi-Fi version. |
| #define | [NET\_REQUEST\_WIFI\_CONN\_PARAMS](#gac6483341435ff380a2d4a69430899c1a)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS](#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a)) |
|  | Request a Wi-Fi connection parameters. |
| #define | [NET\_REQUEST\_WIFI\_RTS\_THRESHOLD](#ga22d80ef0ffb15e4286d7b1c3325d5334)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD](#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)) |
|  | Request a Wi-Fi RTS threshold. |
| #define | [NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM](#gaf4a78d230f5e0743a6aaf152ddda1c67)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM](#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)) |
|  | Request a Wi-Fi AP parameters configuration. |
| #define | [NET\_REQUEST\_WIFI\_PMKSA\_FLUSH](#ga9070995249eb35de37e2b60c4426f840)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH](#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad)) |
|  | Request a Wi-Fi PMKSA cache entries flush. |
| #define | [NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS](#gae5dc7835e11487187663dfe65a15f22b)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS](#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb)) |
|  | Set Wi-Fi enterprise mode CA/client Cert and key. |
| #define | [NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG](#ga2678ea372335af008d9bd3333f7a7de1)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89)) |
|  | Request a Wi-Fi RTS threshold configuration. |
| #define | [NET\_REQUEST\_WIFI\_WPS\_CONFIG](#ga649a63bc7d315ebdd89464ff48b3fada)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7)) |
| #define | [NET\_REQUEST\_WIFI\_START\_ROAMING](#ga89cc123bb5c30140d2ce0a8b741b1086)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING](#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676)) |
| #define | [NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE](#ga373031970a29331bf1b30d1654c128f0)   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55)) |
| #define | [NET\_EVENT\_WIFI\_SCAN\_RESULT](#ga436a927d47eb9abe683b89f2b128cd6e)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e)) |
|  | Event emitted for Wi-Fi scan result. |
| #define | [NET\_EVENT\_WIFI\_SCAN\_DONE](#ga8ce35a12e5338e9a65970382b4a26b88)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018)) |
|  | Event emitted when Wi-Fi scan is done. |
| #define | [NET\_EVENT\_WIFI\_CONNECT\_RESULT](#ga0e8feafcc5efd85d04be91f407c0b7c4)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c)) |
|  | Event emitted for Wi-Fi connect result. |
| #define | [NET\_EVENT\_WIFI\_DISCONNECT\_RESULT](#ga8cbbe69bd60f42fdbb06f4f1e15410c8)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb)) |
|  | Event emitted for Wi-Fi disconnect result. |
| #define | [NET\_EVENT\_WIFI\_IFACE\_STATUS](#ga99e11fc15582b94d4243de7733e47ebb)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14)) |
|  | Event emitted for Wi-Fi network interface status. |
| #define | [NET\_EVENT\_WIFI\_TWT](#gaeb968a5d2a8d68a8c634cca18dbcf9c6)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_TWT](#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18)) |
|  | Event emitted for Wi-Fi TWT information. |
| #define | [NET\_EVENT\_WIFI\_TWT\_SLEEP\_STATE](#ga682d95b5d06a9b175c10d712acca8a49)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750)) |
|  | Event emitted for Wi-Fi TWT sleep state. |
| #define | [NET\_EVENT\_WIFI\_RAW\_SCAN\_RESULT](#gaea8d222282ddef6992330763afc759a4)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac)) |
|  | Event emitted for Wi-Fi raw scan result. |
| #define | [NET\_EVENT\_WIFI\_DISCONNECT\_COMPLETE](#ga40027feb7ec42c846fd99b56bbd2256d)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f)) |
|  | Event emitted Wi-Fi disconnect is completed. |
| #define | [NET\_EVENT\_WIFI\_SIGNAL\_CHANGE](#ga8da47e9d3e594840fb7a7d59f45ea9ce)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE](#ggac2638308cbb0d268831f1618cf8e1fa8acc9d8a16d99e4006b915b3686522a8e0)) |
|  | Event signal change of connected AP. |
| #define | [NET\_EVENT\_WIFI\_NEIGHBOR\_REP\_COMP](#ga7ed4bc9f25055f5a35270a4c6a0bedcc)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](#ggac2638308cbb0d268831f1618cf8e1fa8a86b6811a06f6158ae9ea4687e219e5af)) |
|  | Event Neighbor Report Completed. |
| #define | [NET\_EVENT\_WIFI\_AP\_ENABLE\_RESULT](#ga1d678fbae0f092814392c0ab4087cb73)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b)) |
|  | Event emitted for Wi-Fi access point enable result. |
| #define | [NET\_EVENT\_WIFI\_AP\_DISABLE\_RESULT](#ga104296fdb38edf868bea1a46f572d101)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d)) |
|  | Event emitted for Wi-Fi access point disable result. |
| #define | [NET\_EVENT\_WIFI\_AP\_STA\_CONNECTED](#gacc392179948bfd5bed6702dc8fb5cd9d)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb)) |
|  | Event emitted when Wi-Fi station is connected in AP mode. |
| #define | [NET\_EVENT\_WIFI\_AP\_STA\_DISCONNECTED](#ga3e8154ce1808665dd165f793ddec1673)   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e)) |
|  | Event emitted Wi-Fi station is disconnected from AP. |
| #define | [MAX\_REG\_CHAN\_NUM](#ga3a6bfa37bd7850342279d304df20977d)   42 |
|  | Max regulatory channel number. |
| #define | [WIFI\_WPS\_PIN\_MAX\_LEN](#ga234d72d7c881e67ff49fb6c474c622e3)   8 |

| Typedefs | |
| --- | --- |
| typedef void(\* | [scan\_result\_cb\_t](#gad34b366f1c315207ce0da587ca96d8d8)) (struct [net\_if](structnet__if.md) \*iface, int status, struct [wifi\_scan\_result](structwifi__scan__result.md) \*entry) |
|  | Scan result callback. |

| Enumerations | |
| --- | --- |
| enum | [wifi\_security\_type](#gadde31a04fa25ed805115c6b31854cd9c) {     [WIFI\_SECURITY\_TYPE\_NONE](#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e) = 0 , [WIFI\_SECURITY\_TYPE\_PSK](#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368) , [WIFI\_SECURITY\_TYPE\_PSK\_SHA256](#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e) , [WIFI\_SECURITY\_TYPE\_SAE](#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f) ,     [WIFI\_SECURITY\_TYPE\_SAE\_HNP](#ggadde31a04fa25ed805115c6b31854cd9caab329c818e10cbe98aac1f9c30849c91) = WIFI\_SECURITY\_TYPE\_SAE , [WIFI\_SECURITY\_TYPE\_SAE\_H2E](#ggadde31a04fa25ed805115c6b31854cd9ca1e45d14be678d0693b3f03f73fc5b0df) , [WIFI\_SECURITY\_TYPE\_SAE\_AUTO](#ggadde31a04fa25ed805115c6b31854cd9ca4beacdae98f8ca155609d2fd660c5ed0) , [WIFI\_SECURITY\_TYPE\_WAPI](#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d) ,     [WIFI\_SECURITY\_TYPE\_EAP](#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80) , [WIFI\_SECURITY\_TYPE\_EAP\_TLS](#ggadde31a04fa25ed805115c6b31854cd9ca85bcce61e75c01eb95083523e8925a40) = WIFI\_SECURITY\_TYPE\_EAP , [WIFI\_SECURITY\_TYPE\_WEP](#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724) , [WIFI\_SECURITY\_TYPE\_WPA\_PSK](#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a) ,     [WIFI\_SECURITY\_TYPE\_WPA\_AUTO\_PERSONAL](#ggadde31a04fa25ed805115c6b31854cd9ca275483ee9bced209eb2d131825f599ff) , [WIFI\_SECURITY\_TYPE\_DPP](#ggadde31a04fa25ed805115c6b31854cd9ca6cf0bd5db90deaa6b35f7afe122e8b5f) , [WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_MSCHAPV2](#ggadde31a04fa25ed805115c6b31854cd9caaa1dbea0100af80ca48ad594cddb4212) , [WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_GTC](#ggadde31a04fa25ed805115c6b31854cd9ca0c9db910757c5a715a5e88089362fab5) ,     [WIFI\_SECURITY\_TYPE\_EAP\_TTLS\_MSCHAPV2](#ggadde31a04fa25ed805115c6b31854cd9ca3a20bf15c1e51313629789e6abe0273d) , [WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_TLS](#ggadde31a04fa25ed805115c6b31854cd9ca6d2e5f72b8bf76f093ab79be2a4b9477) , [WIFI\_SECURITY\_TYPE\_EAP\_TLS\_SHA256](#ggadde31a04fa25ed805115c6b31854cd9ca64ddf5be1aabce875fc66e39ff63be9b) , [WIFI\_SECURITY\_TYPE\_FT\_PSK](#ggadde31a04fa25ed805115c6b31854cd9ca42e49ccccfed285d32aa9f36bcfd5fc5) ,     [WIFI\_SECURITY\_TYPE\_FT\_SAE](#ggadde31a04fa25ed805115c6b31854cd9cab7bcc9437586d4940126a2ae1efdb092) , [WIFI\_SECURITY\_TYPE\_FT\_EAP](#ggadde31a04fa25ed805115c6b31854cd9ca00d759c3332700100ca7be612abeeda5) , [WIFI\_SECURITY\_TYPE\_FT\_EAP\_SHA384](#ggadde31a04fa25ed805115c6b31854cd9ca52aa23f908a4fae0864f2e187b89af93)   } |
|  | IEEE 802.11 security types. [More...](#gadde31a04fa25ed805115c6b31854cd9c) |
| enum | [wifi\_eap\_type](#ga92b6fa6755491c3bd61f895213d07331) {     [WIFI\_EAP\_TYPE\_NONE](#gga92b6fa6755491c3bd61f895213d07331a39edcc7a267ce608a1e818948b5d172b) = 0 , [WIFI\_EAP\_TYPE\_GTC](#gga92b6fa6755491c3bd61f895213d07331a64daad77662868322e638da6531a5c0f) = 6 , [WIFI\_EAP\_TYPE\_TLS](#gga92b6fa6755491c3bd61f895213d07331a505b4b888231dd1fbc169d612d8f0c38) = 13 , [WIFI\_EAP\_TYPE\_TTLS](#gga92b6fa6755491c3bd61f895213d07331a35fce37fccb3d27596c4e0a531109dac) = 21 ,     [WIFI\_EAP\_TYPE\_PEAP](#gga92b6fa6755491c3bd61f895213d07331a8e619153aa3dad398c6ced36605f5e3f) = 25 , [WIFI\_EAP\_TYPE\_MSCHAPV2](#gga92b6fa6755491c3bd61f895213d07331a37f7681b1fb5d7165010ec941018882f) = 26   } |
|  | EPA method Types. [More...](#ga92b6fa6755491c3bd61f895213d07331) |
| enum | [wifi\_suiteb\_type](#ga168e7affe48d72d7d1e3ccddb63fe5a7) { [WIFI\_SUITEB](#gga168e7affe48d72d7d1e3ccddb63fe5a7aa8e819a5bbe3bb65e98c69709c086d89) = 1 , [WIFI\_SUITEB\_192](#gga168e7affe48d72d7d1e3ccddb63fe5a7a6fdf84ffa5fcca7371bf2da06be6c30d) } |
|  | Enterprise security WPA3 suiteb types. [More...](#ga168e7affe48d72d7d1e3ccddb63fe5a7) |
| enum | [wifi\_cipher\_type](#ga7f7b23ac019ca504a2006f0376735645) { [WPA\_CAPA\_ENC\_CCMP](#gga7f7b23ac019ca504a2006f0376735645ac0af8c48884381d3be7e9a2b7f3b54e1) , [WPA\_CAPA\_ENC\_GCMP](#gga7f7b23ac019ca504a2006f0376735645a88fe5cd8b7777b931d869cb76ae65b1d) , [WPA\_CAPA\_ENC\_GCMP\_256](#gga7f7b23ac019ca504a2006f0376735645a60599a3fdfad99c6ec1471d4973556c4) } |
|  | Group cipher and pairwise cipher types. [More...](#ga7f7b23ac019ca504a2006f0376735645) |
| enum | [wifi\_group\_mgmt\_cipher\_type](#gaf84d5e1a68393483fc6063c06b8f26e0) { [WPA\_CAPA\_ENC\_BIP](#ggaf84d5e1a68393483fc6063c06b8f26e0a7d5bfccaca027a00e834a8db03f8b8f8) , [WPA\_CAPA\_ENC\_BIP\_GMAC\_128](#ggaf84d5e1a68393483fc6063c06b8f26e0ab15e42ab1ba05c1296b19cbfff2ccf70) , [WPA\_CAPA\_ENC\_BIP\_GMAC\_256](#ggaf84d5e1a68393483fc6063c06b8f26e0ae437a3b3abd043b184e545a4ec40c096) } |
|  | group mgmt cipher types. [More...](#gaf84d5e1a68393483fc6063c06b8f26e0) |
| enum | [wifi\_mfp\_options](#ga1f252da47d9650023d7fff6d08e49c76) { [WIFI\_MFP\_DISABLE](#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969) = 0 , [WIFI\_MFP\_OPTIONAL](#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf) , [WIFI\_MFP\_REQUIRED](#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840) } |
|  | IEEE 802.11w - Management frame protection. [More...](#ga1f252da47d9650023d7fff6d08e49c76) |
| enum | [wifi\_frequency\_bands](#ga1e2f0439a322355fa7368ea880c9c15d) {     [WIFI\_FREQ\_BAND\_2\_4\_GHZ](#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11) = 0 , [WIFI\_FREQ\_BAND\_5\_GHZ](#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895) , [WIFI\_FREQ\_BAND\_6\_GHZ](#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0) , **\_\_WIFI\_FREQ\_BAND\_AFTER\_LAST** ,     [WIFI\_FREQ\_BAND\_MAX](#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5) = \_\_WIFI\_FREQ\_BAND\_AFTER\_LAST - 1 , [WIFI\_FREQ\_BAND\_UNKNOWN](#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)   } |
|  | IEEE 802.11 operational frequency bands (not exhaustive). [More...](#ga1e2f0439a322355fa7368ea880c9c15d) |
| enum | [wifi\_iface\_state](#ga981961f747b919d61d3ccbd41e4508b4) {     [WIFI\_STATE\_DISCONNECTED](#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f) = 0 , [WIFI\_STATE\_INTERFACE\_DISABLED](#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c) , [WIFI\_STATE\_INACTIVE](#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598) , [WIFI\_STATE\_SCANNING](#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b) ,     [WIFI\_STATE\_AUTHENTICATING](#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba) , [WIFI\_STATE\_ASSOCIATING](#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b) , [WIFI\_STATE\_ASSOCIATED](#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc) , [WIFI\_STATE\_4WAY\_HANDSHAKE](#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969) ,     [WIFI\_STATE\_GROUP\_HANDSHAKE](#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e) , [WIFI\_STATE\_COMPLETED](#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f)   } |
|  | Wi-Fi interface states. [More...](#ga981961f747b919d61d3ccbd41e4508b4) |
| enum | [wifi\_iface\_mode](#ga584f6239ac14e2bedc5e6bd72756423b) {     [WIFI\_MODE\_INFRA](#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813) = 0 , [WIFI\_MODE\_IBSS](#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b) = 1 , [WIFI\_MODE\_AP](#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8) = 2 , [WIFI\_MODE\_P2P\_GO](#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889) = 3 ,     [WIFI\_MODE\_P2P\_GROUP\_FORMATION](#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521) = 4 , [WIFI\_MODE\_MESH](#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68) = 5   } |
|  | Wi-Fi interface modes. [More...](#ga584f6239ac14e2bedc5e6bd72756423b) |
| enum | [wifi\_link\_mode](#gabdb2a784d4727b71ab44cca04e422c62) {     [WIFI\_0](#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8) = 0 , [WIFI\_1](#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c) , [WIFI\_2](#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9) , [WIFI\_3](#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362) ,     [WIFI\_4](#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2) , [WIFI\_5](#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824) , [WIFI\_6](#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe) , [WIFI\_6E](#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6) ,     [WIFI\_7](#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934)   } |
|  | Wi-Fi link operating modes. [More...](#gabdb2a784d4727b71ab44cca04e422c62) |
| enum | [wifi\_scan\_type](#gad30e29eda65ccafdbd7f11865937b8ea) { [WIFI\_SCAN\_TYPE\_ACTIVE](#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9) = 0 , [WIFI\_SCAN\_TYPE\_PASSIVE](#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f) } |
|  | Wi-Fi scanning types. [More...](#gad30e29eda65ccafdbd7f11865937b8ea) |
| enum | [wifi\_ps](#ga0fffeb57b68fb8cdef9d3d571368b8ca) { [WIFI\_PS\_DISABLED](#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82) = 0 , [WIFI\_PS\_ENABLED](#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47) } |
|  | Wi-Fi power save states. [More...](#ga0fffeb57b68fb8cdef9d3d571368b8ca) |
| enum | [wifi\_ps\_mode](#gaffae7d2a754be5eb952ad2b83edad54c) { [WIFI\_PS\_MODE\_LEGACY](#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd) = 0 , [WIFI\_PS\_MODE\_WMM](#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5) } |
|  | Wi-Fi power save modes. [More...](#gaffae7d2a754be5eb952ad2b83edad54c) |
| enum | [wifi\_operational\_modes](#ga4a9243eeb974111d6047fd3d8d9cbf35) {     [WIFI\_STA\_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7) = BIT(0) , [WIFI\_MONITOR\_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696) = BIT(1) , [WIFI\_TX\_INJECTION\_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74) = BIT(2) , [WIFI\_PROMISCUOUS\_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56) = BIT(3) ,     [WIFI\_AP\_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd) = BIT(4) , [WIFI\_SOFTAP\_MODE](#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623) = BIT(5)   } |
|  | Wifi operational mode. [More...](#ga4a9243eeb974111d6047fd3d8d9cbf35) |
| enum | [wifi\_filter](#gaa60495242c66a3fac294886856121c1f) { [WIFI\_PACKET\_FILTER\_ALL](#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b) = BIT(0) , [WIFI\_PACKET\_FILTER\_MGMT](#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc) = BIT(1) , [WIFI\_PACKET\_FILTER\_DATA](#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244) = BIT(2) , [WIFI\_PACKET\_FILTER\_CTRL](#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de) = BIT(3) } |
|  | Mode filter settings. [More...](#gaa60495242c66a3fac294886856121c1f) |
| enum | [wifi\_twt\_operation](#gad0e998aeb1b27c4f203ca76339d323a3) { [WIFI\_TWT\_SETUP](#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45) = 0 , [WIFI\_TWT\_TEARDOWN](#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f) } |
|  | Wi-Fi Target Wake Time (TWT) operations. [More...](#gad0e998aeb1b27c4f203ca76339d323a3) |
| enum | [wifi\_twt\_negotiation\_type](#ga695123cd534e2499f516a07fdc5cafa8) { [WIFI\_TWT\_INDIVIDUAL](#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0) = 0 , [WIFI\_TWT\_BROADCAST](#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa) , [WIFI\_TWT\_WAKE\_TBTT](#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978) } |
|  | Wi-Fi Target Wake Time (TWT) negotiation types. [More...](#ga695123cd534e2499f516a07fdc5cafa8) |
| enum | [wifi\_twt\_setup\_cmd](#ga31c78afc89bfdc4b54cee177843f8022) {     [WIFI\_TWT\_SETUP\_CMD\_REQUEST](#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd) = 0 , [WIFI\_TWT\_SETUP\_CMD\_SUGGEST](#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648) , [WIFI\_TWT\_SETUP\_CMD\_DEMAND](#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e) , [WIFI\_TWT\_SETUP\_CMD\_GROUPING](#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279) ,     [WIFI\_TWT\_SETUP\_CMD\_ACCEPT](#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a) , [WIFI\_TWT\_SETUP\_CMD\_ALTERNATE](#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1) , [WIFI\_TWT\_SETUP\_CMD\_DICTATE](#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3) , [WIFI\_TWT\_SETUP\_CMD\_REJECT](#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565)   } |
|  | Wi-Fi Target Wake Time (TWT) setup commands. [More...](#ga31c78afc89bfdc4b54cee177843f8022) |
| enum | [wifi\_twt\_setup\_resp\_status](#ga4d03aedac13ee4512d7717ac624f319a) { [WIFI\_TWT\_RESP\_RECEIVED](#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286) = 0 , [WIFI\_TWT\_RESP\_NOT\_RECEIVED](#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72) } |
|  | Wi-Fi Target Wake Time (TWT) negotiation status. [More...](#ga4d03aedac13ee4512d7717ac624f319a) |
| enum | [wifi\_twt\_fail\_reason](#ga97fa304f9a1db2294a93cccd4c93bcf6) {     [WIFI\_TWT\_FAIL\_UNSPECIFIED](#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13) , [WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL](#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556) , [WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED](#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d) , [WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef) ,     [WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED](#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831) , [WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB](#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860) , [WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB](#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce) , [WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS](#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7) ,     [WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID](#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6) , [WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED](#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee) , [WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS](#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)   } |
|  | Target Wake Time (TWT) error codes. [More...](#ga97fa304f9a1db2294a93cccd4c93bcf6) |
| enum | [wifi\_twt\_teardown\_status](#gad3709d07aaa3ed59b48f9dd7bd181989) { [WIFI\_TWT\_TEARDOWN\_SUCCESS](#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965) = 0 , [WIFI\_TWT\_TEARDOWN\_FAILED](#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d) } |
|  | Wi-Fi Target Wake Time (TWT) teradown status. [More...](#gad3709d07aaa3ed59b48f9dd7bd181989) |
| enum | [wifi\_ps\_param\_type](#gabe45d132797047c098041331c8f6f912) {     [WIFI\_PS\_PARAM\_STATE](#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d) , [WIFI\_PS\_PARAM\_LISTEN\_INTERVAL](#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90) , [WIFI\_PS\_PARAM\_WAKEUP\_MODE](#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8) , [WIFI\_PS\_PARAM\_MODE](#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab) ,     [WIFI\_PS\_PARAM\_EXIT\_STRATEGY](#ggabe45d132797047c098041331c8f6f912a8eb7bd5dbe14f9262980dfeb5bd85e03) , [WIFI\_PS\_PARAM\_TIMEOUT](#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29)   } |
|  | Wi-Fi power save parameters. [More...](#gabe45d132797047c098041331c8f6f912) |
| enum | [wifi\_ps\_wakeup\_mode](#gac7f907644847e905d67c709fa4afae7f) { [WIFI\_PS\_WAKEUP\_MODE\_DTIM](#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6) = 0 , [WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL](#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30) } |
|  | Wi-Fi power save modes. [More...](#gac7f907644847e905d67c709fa4afae7f) |
| enum | [wifi\_ps\_exit\_strategy](#ga2d424d1711389fb784e916a87ff854b7) { [WIFI\_PS\_EXIT\_CUSTOM\_ALGO](#gga2d424d1711389fb784e916a87ff854b7aa8e9097d5c86dfc078fa230ca3b41ce5) = 0 , [WIFI\_PS\_EXIT\_EVERY\_TIM](#gga2d424d1711389fb784e916a87ff854b7a9aa2663512a5fd0dec84807c4f2db832) } |
|  | Wi-Fi power save exit strategy. [More...](#ga2d424d1711389fb784e916a87ff854b7) |
| enum | [wifi\_config\_ps\_param\_fail\_reason](#gad98099584d2222ede93aba42b1fbaff0) {     [WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED](#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38) , [WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL](#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394) , [WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED](#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093) , [WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3) ,     [WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED](#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a) , [WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED](#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486) , [WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID](#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f) , [WIFI\_PS\_PARAM\_FAIL\_INVALID\_EXIT\_STRATEGY](#ggad98099584d2222ede93aba42b1fbaff0adda816053e0d9a00f243b93b5b7178ce)   } |
|  | Wi-Fi power save error codes. [More...](#gad98099584d2222ede93aba42b1fbaff0) |
| enum | [wifi\_ap\_config\_param](#ga83546cf946a9123c563609e8903d9642) { [WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY](#gga83546cf946a9123c563609e8903d9642a2ab06f57b7e2b75b18e919e7777e6a7c) = BIT(0) , [WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA](#gga83546cf946a9123c563609e8903d9642abdcec2dcf5a23339b90d5da94fd19958) = BIT(1) } |
|  | Wi-Fi AP mode configuration parameter. [More...](#ga83546cf946a9123c563609e8903d9642) |
| enum | [net\_request\_wifi\_cmd](#ga99a55137188119f65f9d2bb4f57cac77) {     [NET\_REQUEST\_WIFI\_CMD\_SCAN](#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a) = 1 , [NET\_REQUEST\_WIFI\_CMD\_CONNECT](#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a) , [NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7) , [NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c) ,     [NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf) , [NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de) , [NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6) , [NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST](#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede) ,     [NET\_REQUEST\_WIFI\_CMD\_PS](#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a) , [NET\_REQUEST\_WIFI\_CMD\_TWT](#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09) , [NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9) , [NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456) ,     [NET\_REQUEST\_WIFI\_CMD\_MODE](#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899) , [NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5) , [NET\_REQUEST\_WIFI\_CMD\_CHANNEL](#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2) , [NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a) ,     [NET\_REQUEST\_WIFI\_CMD\_VERSION](#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb) , [NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS](#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a) , [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD](#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b) , [NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM](#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813) ,     [NET\_REQUEST\_WIFI\_CMD\_DPP](#gga99a55137188119f65f9d2bb4f57cac77a6fc4d3aca344dc551dd62ae1d6072104) , [NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH](#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad) , [NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS](#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb) , [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89) ,     [NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7) , [NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING](#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676) , [NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55) , [NET\_REQUEST\_WIFI\_CMD\_CANDIDATE\_SCAN](#gga99a55137188119f65f9d2bb4f57cac77ab7bc479691f88138972d0d8e1e2179ed)   } |
|  | Wi-Fi management commands. [More...](#ga99a55137188119f65f9d2bb4f57cac77) |
| enum | [net\_event\_wifi\_cmd](#gac2638308cbb0d268831f1618cf8e1fa8) {     [NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e) = 1 , [NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018) , [NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c) , [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb) ,     [NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14) , [NET\_EVENT\_WIFI\_CMD\_TWT](#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18) , [NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750) , [NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac) ,     [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f) , [NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE](#ggac2638308cbb0d268831f1618cf8e1fa8acc9d8a16d99e4006b915b3686522a8e0) , [NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_RECEIVED](#ggac2638308cbb0d268831f1618cf8e1fa8a75a0a093f32fa2577286c92c2525df91) , [NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](#ggac2638308cbb0d268831f1618cf8e1fa8a86b6811a06f6158ae9ea4687e219e5af) ,     [NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b) , [NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d) , [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb) , [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e) ,     [NET\_EVENT\_WIFI\_CMD\_SUPPLICANT](#ggac2638308cbb0d268831f1618cf8e1fa8a4ec52c22e23502421077e46e94facf08)   } |
|  | Wi-Fi management events. [More...](#gac2638308cbb0d268831f1618cf8e1fa8) |
| enum | [wifi\_conn\_status](#ga86a5741e54aeb3e290142b0de217b8a8) {     [WIFI\_STATUS\_CONN\_SUCCESS](#gga86a5741e54aeb3e290142b0de217b8a8a380410b02b1e12599f37d1dcb844f5bd) = 0 , [WIFI\_STATUS\_CONN\_FAIL](#gga86a5741e54aeb3e290142b0de217b8a8ab80ec4b70c75695fbe698034e2cb6a44) , [WIFI\_STATUS\_CONN\_WRONG\_PASSWORD](#gga86a5741e54aeb3e290142b0de217b8a8a90d91f96a35c9f6847cbc7abd8c20bf8) , [WIFI\_STATUS\_CONN\_TIMEOUT](#gga86a5741e54aeb3e290142b0de217b8a8abb8783b92aec2ed1ffc6331979888563) ,     [WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND](#gga86a5741e54aeb3e290142b0de217b8a8a2ae79fa389bb447fa108e0107aeff2f4) , [WIFI\_STATUS\_CONN\_LAST\_STATUS](#gga86a5741e54aeb3e290142b0de217b8a8aeee5fb8d8c3e7905554d08331f06191f) , [WIFI\_STATUS\_DISCONN\_FIRST\_STATUS](#gga86a5741e54aeb3e290142b0de217b8a8abe1401e5d516c0d63291add15e558b18) = WIFI\_STATUS\_CONN\_LAST\_STATUS   } |
|  | Wi-Fi connect result codes. [More...](#ga86a5741e54aeb3e290142b0de217b8a8) |
| enum | [wifi\_disconn\_reason](#gac782af0a60b202fd19597cabb7bd3a9a) {     [WIFI\_REASON\_DISCONN\_SUCCESS](#ggac782af0a60b202fd19597cabb7bd3a9aa5c894399db8949a789ca4f5750b6f042) = 0 , [WIFI\_REASON\_DISCONN\_UNSPECIFIED](#ggac782af0a60b202fd19597cabb7bd3a9aa87f5d64a9fd3acf8d67c698199779e5c) , [WIFI\_REASON\_DISCONN\_USER\_REQUEST](#ggac782af0a60b202fd19597cabb7bd3a9aaee75adafb52bd6ecaa547a76c6ccd0a7) , [WIFI\_REASON\_DISCONN\_AP\_LEAVING](#ggac782af0a60b202fd19597cabb7bd3a9aa34e3f78ce43db3daeaf32038e0baf204) ,     [WIFI\_REASON\_DISCONN\_INACTIVITY](#ggac782af0a60b202fd19597cabb7bd3a9aa05fe2f87de30de47ee48f7615c2206e6)   } |
|  | Wi-Fi disconnect reason codes. [More...](#gac782af0a60b202fd19597cabb7bd3a9a) |
| enum | [wifi\_ap\_status](#gaaf730bf76adc06434c7ac63bf0417884) {     [WIFI\_STATUS\_AP\_SUCCESS](#ggaaf730bf76adc06434c7ac63bf0417884a0df52848da8735892d0eb1e381b2cd7c) = 0 , [WIFI\_STATUS\_AP\_FAIL](#ggaaf730bf76adc06434c7ac63bf0417884a6c6801381caa3862004662169202fa9a) , [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED](#ggaaf730bf76adc06434c7ac63bf0417884a5acb85a2361ca72ed10966b829c5753b) , [WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED](#ggaaf730bf76adc06434c7ac63bf0417884a0b1cb592c54c16e8a54defee71c5fd15) ,     [WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED](#ggaaf730bf76adc06434c7ac63bf0417884ac18a7b551f8c6bb7737b0e8e60c323ce) , [WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED](#ggaaf730bf76adc06434c7ac63bf0417884abe5a626d22051522255d98fdfdfbfcc8) , [WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED](#ggaaf730bf76adc06434c7ac63bf0417884a2105e6c49b3bcb5f7dcacbc1e5ce9cca) , [WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED](#ggaaf730bf76adc06434c7ac63bf0417884a36a58980bdc7877c910441590137ddbe)   } |
|  | Wi-Fi AP mode result codes. [More...](#gaaf730bf76adc06434c7ac63bf0417884) |
| enum | [wifi\_mgmt\_op](#gae129d0783276e662575af2314eef86cd) { [WIFI\_MGMT\_GET](#ggae129d0783276e662575af2314eef86cda6b8183a773e0cdfa85bc4b41ae70fdcd) = 0 , [WIFI\_MGMT\_SET](#ggae129d0783276e662575af2314eef86cdaa0d5931c8275a8d3288ab668b6dfb5a1) = 1 } |
|  | Generic get/set operation for any command. [More...](#gae129d0783276e662575af2314eef86cd) |
| enum | [wifi\_twt\_sleep\_state](#ga38c184ea35c02f304cccdf389ca6d552) { [WIFI\_TWT\_STATE\_SLEEP](#gga38c184ea35c02f304cccdf389ca6d552a37a7aba20723b6614e39e1c417f3113c) = 0 , [WIFI\_TWT\_STATE\_AWAKE](#gga38c184ea35c02f304cccdf389ca6d552a7b7b45f85d9644f897ca00bd7864e1b0) = 1 } |
|  | Wi-Fi TWT sleep states. [More...](#ga38c184ea35c02f304cccdf389ca6d552) |
| enum | [wifi\_wps\_op](#ga4c36ae1a5171d3fbaeebf95c16be496d) { [WIFI\_WPS\_PBC](#gga4c36ae1a5171d3fbaeebf95c16be496da093f5b3ef95d9e571ea169430da57e88) = 0 , [WIFI\_WPS\_PIN\_GET](#gga4c36ae1a5171d3fbaeebf95c16be496da75bd5067903c2bba8a06732f0431393d) = 1 , [WIFI\_WPS\_PIN\_SET](#gga4c36ae1a5171d3fbaeebf95c16be496da58120620fd2fca80bdac7990ed0e7552) = 2 } |
|  | Operation for WPS. [More...](#ga4c36ae1a5171d3fbaeebf95c16be496d) |
| enum | [wifi\_hostapd\_iface\_state](#gafb2e8c10f596da3527abf9e227c3001b) {     [WIFI\_HAPD\_IFACE\_UNINITIALIZED](#ggafb2e8c10f596da3527abf9e227c3001ba7b4af20b16fb8881b963d4f2ebdad11a) , [WIFI\_HAPD\_IFACE\_DISABLED](#ggafb2e8c10f596da3527abf9e227c3001ba21e99c5fff612afd417c0d4511a9c135) , [WIFI\_HAPD\_IFACE\_COUNTRY\_UPDATE](#ggafb2e8c10f596da3527abf9e227c3001badd81c06c029edaa9ac973e03136d4ff4) , [WIFI\_HAPD\_IFACE\_ACS](#ggafb2e8c10f596da3527abf9e227c3001ba762c44f87b3dd9a08d2442b86ad06168) ,     [WIFI\_HAPD\_IFACE\_HT\_SCAN](#ggafb2e8c10f596da3527abf9e227c3001ba66a141b5b317ac3dc0ca383886458a00) , [WIFI\_HAPD\_IFACE\_DFS](#ggafb2e8c10f596da3527abf9e227c3001ba2bcdccb48ba12b2561e08292365801a0) , [WIFI\_HAPD\_IFACE\_ENABLED](#ggafb2e8c10f596da3527abf9e227c3001ba82333796edc42607754281a400f07b2a)   } |
|  | Wi-Fi AP status. [More...](#gafb2e8c10f596da3527abf9e227c3001b) |

| Functions | |
| --- | --- |
| const char \* | [wifi\_security\_txt](#ga9bb9f658d7806e42b3ee351fb3e7dfa0) (enum [wifi\_security\_type](#gadde31a04fa25ed805115c6b31854cd9c) security) |
|  | Helper function to get user-friendly security type name. |
| const char \* | [wifi\_mfp\_txt](#ga22354241197a9227fdba77e67d471f5c) (enum [wifi\_mfp\_options](#ga1f252da47d9650023d7fff6d08e49c76) mfp) |
|  | Helper function to get user-friendly MFP name. |
| const char \* | [wifi\_band\_txt](#ga44f875bf0d931b66d582f5dca2d65ed5) (enum [wifi\_frequency\_bands](#ga1e2f0439a322355fa7368ea880c9c15d) band) |
|  | Helper function to get user-friendly frequency band name. |
| const char \* | [wifi\_state\_txt](#ga03d306912dc96178e21d3c82c104582f) (enum [wifi\_iface\_state](#ga981961f747b919d61d3ccbd41e4508b4) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Helper function to get user-friendly interface state name. |
| const char \* | [wifi\_mode\_txt](#gad78536ce1f30accfa45f258b6bf8c73d) (enum [wifi\_iface\_mode](#ga584f6239ac14e2bedc5e6bd72756423b) mode) |
|  | Helper function to get user-friendly interface mode name. |
| const char \* | [wifi\_link\_mode\_txt](#ga0d9d6e2150fb187025300904357f7b4d) (enum [wifi\_link\_mode](#gabdb2a784d4727b71ab44cca04e422c62) link\_mode) |
|  | Helper function to get user-friendly link mode name. |
| const char \* | [wifi\_ps\_txt](#gafbeb5f7fa97fd2ba0c691da0f8853ef2) (enum [wifi\_ps](#ga0fffeb57b68fb8cdef9d3d571368b8ca) ps\_name) |
|  | Helper function to get user-friendly ps name. |
| const char \* | [wifi\_ps\_mode\_txt](#gadb21d49f64e04fba59433e51d5b3481c) (enum [wifi\_ps\_mode](#gaffae7d2a754be5eb952ad2b83edad54c) ps\_mode) |
|  | Helper function to get user-friendly ps mode name. |
| const char \* | [wifi\_twt\_operation\_txt](#gadb125925e851bf7569424cd4295e7712) (enum [wifi\_twt\_operation](#gad0e998aeb1b27c4f203ca76339d323a3) twt\_operation) |
|  | Helper function to get user-friendly twt operation name. |
| const char \* | [wifi\_twt\_negotiation\_type\_txt](#ga6a74e999d63ee491df68447219ef2a0d) (enum [wifi\_twt\_negotiation\_type](#ga695123cd534e2499f516a07fdc5cafa8) twt\_negotiation) |
|  | Helper function to get user-friendly twt negotiation type name. |
| const char \* | [wifi\_twt\_setup\_cmd\_txt](#gae3ca047cc6ef6b6a2e44ba6574d41a44) (enum [wifi\_twt\_setup\_cmd](#ga31c78afc89bfdc4b54cee177843f8022) twt\_setup) |
|  | Helper function to get user-friendly twt setup cmd name. |
| static const char \* | [wifi\_twt\_get\_err\_code\_str](#gab2e6a6e1d8358a8f34d67bd632709b3d) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) err\_no) |
|  | Helper function to get user-friendly TWT error code name. |
| const char \* | [wifi\_ps\_wakeup\_mode\_txt](#ga6fd645f891234136b3028574a0af9666) (enum [wifi\_ps\_wakeup\_mode](#gac7f907644847e905d67c709fa4afae7f) ps\_wakeup\_mode) |
|  | Helper function to get user-friendly ps wakeup mode name. |
| const char \*const | [wifi\_ps\_exit\_strategy\_txt](#gade667a55793caef820b570a248052327) (enum [wifi\_ps\_exit\_strategy](#ga2d424d1711389fb784e916a87ff854b7) ps\_exit\_strategy) |
|  | Helper function to get user-friendly ps exit strategy name. |
| static const char \* | [wifi\_ps\_get\_config\_err\_code\_str](#ga8b72e7989964963a25f42ed1dba240a0) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) err\_no) |
|  | Helper function to get user-friendly power save error code name. |
| void | [wifi\_mgmt\_raise\_connect\_result\_event](#ga036416696b1e3bc458ddbaf07a08d69d) (struct [net\_if](structnet__if.md) \*iface, int status) |
|  | Wi-Fi management connect result event. |
| void | [wifi\_mgmt\_raise\_disconnect\_result\_event](#ga3b6edcf9b51afbf7a327d1a344bd7b87) (struct [net\_if](structnet__if.md) \*iface, int status) |
|  | Wi-Fi management disconnect result event. |
| void | [wifi\_mgmt\_raise\_iface\_status\_event](#ga7da6af0747bcba85f8afab30c92b5b43) (struct [net\_if](structnet__if.md) \*iface, struct [wifi\_iface\_status](structwifi__iface__status.md) \*iface\_status) |
|  | Wi-Fi management interface status event. |
| void | [wifi\_mgmt\_raise\_twt\_event](#ga39404d15243ca084b253cae8fc07e374) (struct [net\_if](structnet__if.md) \*iface, struct [wifi\_twt\_params](structwifi__twt__params.md) \*twt\_params) |
|  | Wi-Fi management TWT event. |
| void | [wifi\_mgmt\_raise\_twt\_sleep\_state](#ga18f09a3196588b51d6c0644f82f639d7) (struct [net\_if](structnet__if.md) \*iface, int twt\_sleep\_state) |
|  | Wi-Fi management TWT sleep state event. |
| void | [wifi\_mgmt\_raise\_raw\_scan\_result\_event](#ga71c99913bded844c4ca32ed9155bc470) (struct [net\_if](structnet__if.md) \*iface, struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \*raw\_scan\_info) |
|  | Wi-Fi management raw scan result event. |
| void | [wifi\_mgmt\_raise\_disconnect\_complete\_event](#gaa75246d6dc55dada389c9d31e2607d5c) (struct [net\_if](structnet__if.md) \*iface, int status) |
|  | Wi-Fi management disconnect complete event. |
| void | [wifi\_mgmt\_raise\_ap\_enable\_result\_event](#ga67b52edeff76c2211b038f4aa90b8982) (struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](#gaaf730bf76adc06434c7ac63bf0417884) status) |
|  | Wi-Fi management AP mode enable result event. |
| void | [wifi\_mgmt\_raise\_ap\_disable\_result\_event](#gadee15c6a492a8ee13bea43812debb5d9) (struct [net\_if](structnet__if.md) \*iface, enum [wifi\_ap\_status](#gaaf730bf76adc06434c7ac63bf0417884) status) |
|  | Wi-Fi management AP mode disable result event. |
| void | [wifi\_mgmt\_raise\_ap\_sta\_connected\_event](#gac8f17f0aa3e426a5cdb731727b9b9ce3) (struct [net\_if](structnet__if.md) \*iface, struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info) |
|  | Wi-Fi management AP mode STA connected event. |
| void | [wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event](#ga49fb9c3908be61d847b31c99be6afc42) (struct [net\_if](structnet__if.md) \*iface, struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \*sta\_info) |
|  | Wi-Fi management AP mode STA disconnected event. |

| Wi-Fi utility functions. | |
| --- | --- |
| Utility functions for the Wi-Fi subsystem. | |
| int | [wifi\_utils\_parse\_scan\_bands](#ga4c91cd7dff0fd9e5402970f3222dc20d) (char \*scan\_bands\_str, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*band\_map) |
|  | Convert a band specification string to a bitmap representing the bands. |
| int | [wifi\_utils\_parse\_scan\_ssids](#ga471a96d3fb6d610a591508b52d4c05a4) (char \*scan\_ssids\_str, const char \*ssids[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_ssids) |
|  | Append a string containing an SSID to an array of SSID strings. |
| int | [wifi\_utils\_parse\_scan\_chan](#gaba9f3117bcef9da1efc1841d3bd9adfd) (char \*scan\_chan\_str, struct [wifi\_band\_channel](structwifi__band__channel.md) \*chan, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_channels) |
|  | Convert a string containing a specification of scan channels to an array. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_utils\_validate\_chan](#gaf1872d0ed2efd3737a36dcc0ab13f18e) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) band, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan) |
|  | Validate a channel against a band. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_utils\_validate\_chan\_2g](#gaf408ba9f75354d3eca735b4804fdf199) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan) |
|  | Validate a channel against the 2.4 GHz band. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_utils\_validate\_chan\_5g](#gae013eee6d6b74126c29d6ca7b2036310) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan) |
|  | Validate a channel against the 5 GHz band. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_utils\_validate\_chan\_6g](#ga2606742e23f48da5ca1660aeac47888b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan) |
|  | Validate a channel against the 6 GHz band. |
| #define | [WIFI\_UTILS\_MAX\_BAND\_STR\_LEN](#ga1104c3c97b460f9f3e15a7a9c56e80af)   3 |
|  | Maximum length of the band specification string. |
| #define | [WIFI\_UTILS\_MAX\_CHAN\_STR\_LEN](#gaacc3c661affda7b376a4024efd645f0b)   4 |
|  | Maximum length of the channel specification string. |

## Detailed Description

Wi-Fi Management API.

Since
:   1.12

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga3a6bfa37bd7850342279d304df20977d)MAX\_REG\_CHAN\_NUM

| #define MAX\_REG\_CHAN\_NUM   42 |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Max regulatory channel number.

## [◆ ](#ga104296fdb38edf868bea1a46f572d101)NET\_EVENT\_WIFI\_AP\_DISABLE\_RESULT

| #define NET\_EVENT\_WIFI\_AP\_DISABLE\_RESULT   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8aeec3d7a9191280c2326034a17555308d)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted for Wi-Fi access point disable result.

## [◆ ](#ga1d678fbae0f092814392c0ab4087cb73)NET\_EVENT\_WIFI\_AP\_ENABLE\_RESULT

| #define NET\_EVENT\_WIFI\_AP\_ENABLE\_RESULT   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8abd1797564427886eeb14dd293ae86a9b)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted for Wi-Fi access point enable result.

## [◆ ](#gacc392179948bfd5bed6702dc8fb5cd9d)NET\_EVENT\_WIFI\_AP\_STA\_CONNECTED

| #define NET\_EVENT\_WIFI\_AP\_STA\_CONNECTED   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED](#ggac2638308cbb0d268831f1618cf8e1fa8abd4269b2cd1302ce61da4f8d7bb9d5fb)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted when Wi-Fi station is connected in AP mode.

## [◆ ](#ga3e8154ce1808665dd165f793ddec1673)NET\_EVENT\_WIFI\_AP\_STA\_DISCONNECTED

| #define NET\_EVENT\_WIFI\_AP\_STA\_DISCONNECTED   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED](#ggac2638308cbb0d268831f1618cf8e1fa8a3678a39f9542968958b5575d571d4e2e)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted Wi-Fi station is disconnected from AP.

## [◆ ](#ga0e8feafcc5efd85d04be91f407c0b7c4)NET\_EVENT\_WIFI\_CONNECT\_RESULT

| #define NET\_EVENT\_WIFI\_CONNECT\_RESULT   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8af76f28777b91b365dc3f97028bc18e3c)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted for Wi-Fi connect result.

## [◆ ](#ga40027feb7ec42c846fd99b56bbd2256d)NET\_EVENT\_WIFI\_DISCONNECT\_COMPLETE

| #define NET\_EVENT\_WIFI\_DISCONNECT\_COMPLETE   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE](#ggac2638308cbb0d268831f1618cf8e1fa8af1c42bd59f01260c64ede07da436c18f)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted Wi-Fi disconnect is completed.

## [◆ ](#ga8cbbe69bd60f42fdbb06f4f1e15410c8)NET\_EVENT\_WIFI\_DISCONNECT\_RESULT

| #define NET\_EVENT\_WIFI\_DISCONNECT\_RESULT   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8a3a3b0387f83d8fb24a0e27312468b0eb)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted for Wi-Fi disconnect result.

## [◆ ](#ga99e11fc15582b94d4243de7733e47ebb)NET\_EVENT\_WIFI\_IFACE\_STATUS

| #define NET\_EVENT\_WIFI\_IFACE\_STATUS   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS](#ggac2638308cbb0d268831f1618cf8e1fa8af4b3f1969b96f63253851c26c3882a14)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted for Wi-Fi network interface status.

## [◆ ](#ga7ed4bc9f25055f5a35270a4c6a0bedcc)NET\_EVENT\_WIFI\_NEIGHBOR\_REP\_COMP

| #define NET\_EVENT\_WIFI\_NEIGHBOR\_REP\_COMP   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](#ggac2638308cbb0d268831f1618cf8e1fa8a86b6811a06f6158ae9ea4687e219e5af)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event Neighbor Report Completed.

## [◆ ](#gaea8d222282ddef6992330763afc759a4)NET\_EVENT\_WIFI\_RAW\_SCAN\_RESULT

| #define NET\_EVENT\_WIFI\_RAW\_SCAN\_RESULT   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8addf15c69512be7ab4957e7c0b3fde0ac)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted for Wi-Fi raw scan result.

## [◆ ](#ga8ce35a12e5338e9a65970382b4a26b88)NET\_EVENT\_WIFI\_SCAN\_DONE

| #define NET\_EVENT\_WIFI\_SCAN\_DONE   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE](#ggac2638308cbb0d268831f1618cf8e1fa8ad753b7e4588257815f4a60a539ca2018)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted when Wi-Fi scan is done.

## [◆ ](#ga436a927d47eb9abe683b89f2b128cd6e)NET\_EVENT\_WIFI\_SCAN\_RESULT

| #define NET\_EVENT\_WIFI\_SCAN\_RESULT   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT](#ggac2638308cbb0d268831f1618cf8e1fa8a37e9ab2a6832153fa968337d920e587e)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted for Wi-Fi scan result.

## [◆ ](#ga8da47e9d3e594840fb7a7d59f45ea9ce)NET\_EVENT\_WIFI\_SIGNAL\_CHANGE

| #define NET\_EVENT\_WIFI\_SIGNAL\_CHANGE   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE](#ggac2638308cbb0d268831f1618cf8e1fa8acc9d8a16d99e4006b915b3686522a8e0)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event signal change of connected AP.

## [◆ ](#gaeb968a5d2a8d68a8c634cca18dbcf9c6)NET\_EVENT\_WIFI\_TWT

| #define NET\_EVENT\_WIFI\_TWT   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_TWT](#ggac2638308cbb0d268831f1618cf8e1fa8adad71603ed829ed92d06f8c40efa9b18)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted for Wi-Fi TWT information.

## [◆ ](#ga682d95b5d06a9b175c10d712acca8a49)NET\_EVENT\_WIFI\_TWT\_SLEEP\_STATE

| #define NET\_EVENT\_WIFI\_TWT\_SLEEP\_STATE   (\_NET\_WIFI\_EVENT | [NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE](#ggac2638308cbb0d268831f1618cf8e1fa8a78838bf7ce80cee5e803712cd0286750)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Event emitted for Wi-Fi TWT sleep state.

## [◆ ](#gadd9b5b206c7ee2e40c30a37c7b4fc002)NET\_REQUEST\_WIFI\_11K\_CONFIG

| #define NET\_REQUEST\_WIFI\_11K\_CONFIG   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77aa86fb7193245593dd84b3a4376bc25d6)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

## [◆ ](#ga4a2b1e8befd7376749b1d4fbcf98376f)NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST

| #define NET\_REQUEST\_WIFI\_11K\_NEIGHBOR\_REQUEST   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST](#gga99a55137188119f65f9d2bb4f57cac77a48b3f0ec6647fb30d3b6456822c2dede)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

## [◆ ](#gaf4a78d230f5e0743a6aaf152ddda1c67)NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM

| #define NET\_REQUEST\_WIFI\_AP\_CONFIG\_PARAM   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM](#gga99a55137188119f65f9d2bb4f57cac77a14a0428720818c79df825d758e83f813)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi AP parameters configuration.

## [◆ ](#gaf81f62bf4c9e331a095acbf0d24ca1a2)NET\_REQUEST\_WIFI\_AP\_DISABLE

| #define NET\_REQUEST\_WIFI\_AP\_DISABLE   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE](#gga99a55137188119f65f9d2bb4f57cac77a6fe9d7137b4cd20de880955b27382ccf)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi access point disable.

## [◆ ](#ga638d2eb0a5029c1af46a91b523ed8589)NET\_REQUEST\_WIFI\_AP\_ENABLE

| #define NET\_REQUEST\_WIFI\_AP\_ENABLE   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE](#gga99a55137188119f65f9d2bb4f57cac77a28267d33b555433271cb121d62194a4c)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi access point enable.

## [◆ ](#gaa3e52e08d89a1104f07207e52b81d503)NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT

| #define NET\_REQUEST\_WIFI\_AP\_STA\_DISCONNECT   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT](#gga99a55137188119f65f9d2bb4f57cac77a6f3865aa6a4d7633e241ee2b002c1b5a)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi access point to disconnect a station.

## [◆ ](#gad9614d2368f8399850aaec05e40bdc78)NET\_REQUEST\_WIFI\_CHANNEL

| #define NET\_REQUEST\_WIFI\_CHANNEL   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_CHANNEL](#gga99a55137188119f65f9d2bb4f57cac77aade3d7a43c730a52f7876c6486170bb2)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi channel.

## [◆ ](#gac6483341435ff380a2d4a69430899c1a)NET\_REQUEST\_WIFI\_CONN\_PARAMS

| #define NET\_REQUEST\_WIFI\_CONN\_PARAMS   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS](#gga99a55137188119f65f9d2bb4f57cac77aa150f53621941796082e00090bde6a5a)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi connection parameters.

## [◆ ](#gaa7ab2a97950a22736bb69f60b459f0f6)NET\_REQUEST\_WIFI\_CONNECT

| #define NET\_REQUEST\_WIFI\_CONNECT   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_CONNECT](#gga99a55137188119f65f9d2bb4f57cac77a78c958877ee60c90803c925b6b2f057a)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi connect.

## [◆ ](#ga90afd8d4e83056463ec6e667ed8ea60a)NET\_REQUEST\_WIFI\_DISCONNECT

| #define NET\_REQUEST\_WIFI\_DISCONNECT   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_DISCONNECT](#gga99a55137188119f65f9d2bb4f57cac77ac33941da138b993f7a1158d91469bcb7)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi disconnect.

## [◆ ](#gae5dc7835e11487187663dfe65a15f22b)NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS

| #define NET\_REQUEST\_WIFI\_ENTERPRISE\_CREDS   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS](#gga99a55137188119f65f9d2bb4f57cac77a94b7fb7a8c529082e1d0458298b6c3fb)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Set Wi-Fi enterprise mode CA/client Cert and key.

## [◆ ](#ga3e45f6ee3801553619d8eb7d0af506eb)NET\_REQUEST\_WIFI\_IFACE\_STATUS

| #define NET\_REQUEST\_WIFI\_IFACE\_STATUS   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS](#gga99a55137188119f65f9d2bb4f57cac77a6af9d52df8f9db6393044e42e10ff0de)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi network interface status.

## [◆ ](#ga9b4da60a8108b0cc431ac1eecfca0cd0)NET\_REQUEST\_WIFI\_MODE

| #define NET\_REQUEST\_WIFI\_MODE   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_MODE](#gga99a55137188119f65f9d2bb4f57cac77ab7183584bdf5fe673d39fa0d090e3899)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request current Wi-Fi mode.

## [◆ ](#ga373031970a29331bf1b30d1654c128f0)NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE

| #define NET\_REQUEST\_WIFI\_NEIGHBOR\_REP\_COMPLETE   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE](#gga99a55137188119f65f9d2bb4f57cac77ad950aa5b87408793f4df9c39fe84cc55)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

## [◆ ](#ga3098e817d12bf4619c9fd2698508fb4e)NET\_REQUEST\_WIFI\_PACKET\_FILTER

| #define NET\_REQUEST\_WIFI\_PACKET\_FILTER   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER](#gga99a55137188119f65f9d2bb4f57cac77a2579ace546bf6954c111eb5951e894f5)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request Wi-Fi packet filter.

## [◆ ](#ga9070995249eb35de37e2b60c4426f840)NET\_REQUEST\_WIFI\_PMKSA\_FLUSH

| #define NET\_REQUEST\_WIFI\_PMKSA\_FLUSH   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH](#gga99a55137188119f65f9d2bb4f57cac77a1fec11ed98f0a9411eefda9e55ee9aad)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi PMKSA cache entries flush.

## [◆ ](#ga68aaced888f98e1ba4e6b61b53e5e2ba)NET\_REQUEST\_WIFI\_PS

| #define NET\_REQUEST\_WIFI\_PS   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_PS](#gga99a55137188119f65f9d2bb4f57cac77abf9fb93c205fa36f74a9ef19d3d0351a)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi power save.

## [◆ ](#ga1032f3773cfe6130da4d4d498b044ee2)NET\_REQUEST\_WIFI\_PS\_CONFIG

| #define NET\_REQUEST\_WIFI\_PS\_CONFIG   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77ae6ce1c605d1bf7c09650ec15d74e77e9)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi power save configuration.

## [◆ ](#ga2b27d102b779a6d846b375854768fb7f)NET\_REQUEST\_WIFI\_REG\_DOMAIN

| #define NET\_REQUEST\_WIFI\_REG\_DOMAIN   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN](#gga99a55137188119f65f9d2bb4f57cac77a367cc44caefd313e0c7ad3badc081456)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi regulatory domain.

## [◆ ](#ga22d80ef0ffb15e4286d7b1c3325d5334)NET\_REQUEST\_WIFI\_RTS\_THRESHOLD

| #define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD](#gga99a55137188119f65f9d2bb4f57cac77a7852cff28fc18ddd7af0f8224c840e7b)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi RTS threshold.

## [◆ ](#ga2678ea372335af008d9bd3333f7a7de1)NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG

| #define NET\_REQUEST\_WIFI\_RTS\_THRESHOLD\_CONFIG   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77ab7a4215540d2e6cda0d522dc621e9d89)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi RTS threshold configuration.

## [◆ ](#ga1c277da90986fa52dca182c4d922646f)NET\_REQUEST\_WIFI\_SCAN

| #define NET\_REQUEST\_WIFI\_SCAN   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_SCAN](#gga99a55137188119f65f9d2bb4f57cac77a4aadf9114010c09bd7420c99a2049d5a)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi scan.

## [◆ ](#ga89cc123bb5c30140d2ce0a8b741b1086)NET\_REQUEST\_WIFI\_START\_ROAMING

| #define NET\_REQUEST\_WIFI\_START\_ROAMING   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING](#gga99a55137188119f65f9d2bb4f57cac77a286205d961a77e44cd98e7894c48e676)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

## [◆ ](#gab84fd7e9ca0bf0b2b9d08889dda26aad)NET\_REQUEST\_WIFI\_TWT

| #define NET\_REQUEST\_WIFI\_TWT   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_TWT](#gga99a55137188119f65f9d2bb4f57cac77a1c9dc2d698326d987ffe5bfd35a9ed09)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi TWT.

## [◆ ](#ga3e60c29ca9ce95d17a7fff087290f7f1)NET\_REQUEST\_WIFI\_VERSION

| #define NET\_REQUEST\_WIFI\_VERSION   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_VERSION](#gga99a55137188119f65f9d2bb4f57cac77a7d9596f2cce54c9e050d89469e86eccb)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Request a Wi-Fi version.

## [◆ ](#ga649a63bc7d315ebdd89464ff48b3fada)NET\_REQUEST\_WIFI\_WPS\_CONFIG

| #define NET\_REQUEST\_WIFI\_WPS\_CONFIG   (\_NET\_WIFI\_BASE | [NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG](#gga99a55137188119f65f9d2bb4f57cac77aec78bf6196abee310e06a8454d27eed7)) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

## [◆ ](#ga3876cd718af9f8a7b3682546da854544)WIFI\_CHANNEL\_ANY

| #define WIFI\_CHANNEL\_ANY   255 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Any channel number.

## [◆ ](#ga8ea9141108f93b419f6a6530bf67bd95)WIFI\_CHANNEL\_MAX

| #define WIFI\_CHANNEL\_MAX   233 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Maximum channel number.

## [◆ ](#ga260e473dac1e823fd298a2c982470e0b)WIFI\_CHANNEL\_MIN

| #define WIFI\_CHANNEL\_MIN   1 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Minimum channel number.

## [◆ ](#ga6766ef7bcb001f1fb526a4083b6cd8bc)WIFI\_COUNTRY\_CODE\_LEN

| #define WIFI\_COUNTRY\_CODE\_LEN   2 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Length of the country code string.

## [◆ ](#gac6904487661f157274b0b60833f6684a)WIFI\_ENT\_IDENTITY\_MAX\_LEN

| #define WIFI\_ENT\_IDENTITY\_MAX\_LEN   64 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Max enterprise identity length.

## [◆ ](#gae2fd55924f4078187431f7a1184f217f)WIFI\_ENT\_PSWD\_MAX\_LEN

| #define WIFI\_ENT\_PSWD\_MAX\_LEN   128 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Max enterprise password length.

## [◆ ](#gaa6cbecd7d4197d453038d3da7ef6be7b)WIFI\_INTERFACE\_INDEX\_MAX

| #define WIFI\_INTERFACE\_INDEX\_MAX   255 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Network interface index max value.

## [◆ ](#gaa1a74ef94af57a7ea966c691c065a46d)WIFI\_INTERFACE\_INDEX\_MIN

| #define WIFI\_INTERFACE\_INDEX\_MIN   1 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Network interface index min value.

## [◆ ](#ga29409ff83a53c6464decdde9bdd04de6)WIFI\_MAC\_ADDR\_LEN

| #define WIFI\_MAC\_ADDR\_LEN   6 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

MAC address length.

## [◆ ](#gad7c3b99c974b342935180a28fdc5ddfc)WIFI\_PSK\_MAX\_LEN

| #define WIFI\_PSK\_MAX\_LEN   64 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Maximum PSK length.

## [◆ ](#gaa8e19abf8c85f237ba5033740ceff553)WIFI\_PSK\_MIN\_LEN

| #define WIFI\_PSK\_MIN\_LEN   8 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Minimum PSK length.

## [◆ ](#gab63fa744cc2e049cfd635ab0a187971f)WIFI\_SAE\_PSWD\_MAX\_LEN

| #define WIFI\_SAE\_PSWD\_MAX\_LEN   128 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Max SAW password length.

## [◆ ](#gad62c60666c9fdffe2e0e9c4388f87886)WIFI\_SSID\_MAX\_LEN

| #define WIFI\_SSID\_MAX\_LEN   32 |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Max SSID length.

## [◆ ](#ga1104c3c97b460f9f3e15a7a9c56e80af)WIFI\_UTILS\_MAX\_BAND\_STR\_LEN

| #define WIFI\_UTILS\_MAX\_BAND\_STR\_LEN   3 |
| --- |

`#include <[wifi_utils.h](wifi__utils_8h.md)>`

Maximum length of the band specification string.

## [◆ ](#gaacc3c661affda7b376a4024efd645f0b)WIFI\_UTILS\_MAX\_CHAN\_STR\_LEN

| #define WIFI\_UTILS\_MAX\_CHAN\_STR\_LEN   4 |
| --- |

`#include <[wifi_utils.h](wifi__utils_8h.md)>`

Maximum length of the channel specification string.

## [◆ ](#ga234d72d7c881e67ff49fb6c474c622e3)WIFI\_WPS\_PIN\_MAX\_LEN

| #define WIFI\_WPS\_PIN\_MAX\_LEN   8 |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

## Typedef Documentation

## [◆ ](#gad34b366f1c315207ce0da587ca96d8d8)scan\_result\_cb\_t

| typedef void(\* scan\_result\_cb\_t) (struct [net\_if](structnet__if.md) \*iface, int status, struct [wifi\_scan\_result](structwifi__scan__result.md) \*entry) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Scan result callback.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | status | Scan result status |
    | entry | Scan result entry |

## Enumeration Type Documentation

## [◆ ](#gac2638308cbb0d268831f1618cf8e1fa8)net\_event\_wifi\_cmd

| enum [net\_event\_wifi\_cmd](#gac2638308cbb0d268831f1618cf8e1fa8) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management events.

| Enumerator | |
| --- | --- |
| NET\_EVENT\_WIFI\_CMD\_SCAN\_RESULT | Scan results available. |
| NET\_EVENT\_WIFI\_CMD\_SCAN\_DONE | Scan done. |
| NET\_EVENT\_WIFI\_CMD\_CONNECT\_RESULT | Connect result. |
| NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_RESULT | Disconnect result. |
| NET\_EVENT\_WIFI\_CMD\_IFACE\_STATUS | Interface status. |
| NET\_EVENT\_WIFI\_CMD\_TWT | TWT events. |
| NET\_EVENT\_WIFI\_CMD\_TWT\_SLEEP\_STATE | TWT sleep status: awake or sleeping, can be used by application to determine if it can send data or not. |
| NET\_EVENT\_WIFI\_CMD\_RAW\_SCAN\_RESULT | Raw scan results available. |
| NET\_EVENT\_WIFI\_CMD\_DISCONNECT\_COMPLETE | Disconnect complete. |
| NET\_EVENT\_WIFI\_CMD\_SIGNAL\_CHANGE | Signal change event. |
| NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_RECEIVED | Neighbor Report. |
| NET\_EVENT\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE | Neighbor Report complete. |
| NET\_EVENT\_WIFI\_CMD\_AP\_ENABLE\_RESULT | AP mode enable result. |
| NET\_EVENT\_WIFI\_CMD\_AP\_DISABLE\_RESULT | AP mode disable result. |
| NET\_EVENT\_WIFI\_CMD\_AP\_STA\_CONNECTED | STA connected to AP. |
| NET\_EVENT\_WIFI\_CMD\_AP\_STA\_DISCONNECTED | STA disconnected from AP. |
| NET\_EVENT\_WIFI\_CMD\_SUPPLICANT | Supplicant specific event. |

## [◆ ](#ga99a55137188119f65f9d2bb4f57cac77)net\_request\_wifi\_cmd

| enum [net\_request\_wifi\_cmd](#ga99a55137188119f65f9d2bb4f57cac77) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management commands.

| Enumerator | |
| --- | --- |
| NET\_REQUEST\_WIFI\_CMD\_SCAN | Scan for Wi-Fi networks. |
| NET\_REQUEST\_WIFI\_CMD\_CONNECT | Connect to a Wi-Fi network. |
| NET\_REQUEST\_WIFI\_CMD\_DISCONNECT | Disconnect from a Wi-Fi network. |
| NET\_REQUEST\_WIFI\_CMD\_AP\_ENABLE | Enable AP mode. |
| NET\_REQUEST\_WIFI\_CMD\_AP\_DISABLE | Disable AP mode. |
| NET\_REQUEST\_WIFI\_CMD\_IFACE\_STATUS | Get interface status. |
| NET\_REQUEST\_WIFI\_CMD\_11K\_CONFIG | Set or get 11k status. |
| NET\_REQUEST\_WIFI\_CMD\_11K\_NEIGHBOR\_REQUEST | Send 11k neighbor request. |
| NET\_REQUEST\_WIFI\_CMD\_PS | Set power save status. |
| NET\_REQUEST\_WIFI\_CMD\_TWT | Setup or teardown TWT flow. |
| NET\_REQUEST\_WIFI\_CMD\_PS\_CONFIG | Get power save config. |
| NET\_REQUEST\_WIFI\_CMD\_REG\_DOMAIN | Set or get regulatory domain. |
| NET\_REQUEST\_WIFI\_CMD\_MODE | Set or get Mode of operation. |
| NET\_REQUEST\_WIFI\_CMD\_PACKET\_FILTER | Set or get packet filter setting for current mode. |
| NET\_REQUEST\_WIFI\_CMD\_CHANNEL | Set or get Wi-Fi channel for Monitor or TX-Injection mode. |
| NET\_REQUEST\_WIFI\_CMD\_AP\_STA\_DISCONNECT | Disconnect a STA from AP. |
| NET\_REQUEST\_WIFI\_CMD\_VERSION | Get Wi-Fi driver and Firmware versions. |
| NET\_REQUEST\_WIFI\_CMD\_CONN\_PARAMS | Get Wi-Fi latest connection parameters. |
| NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD | Set RTS threshold. |
| NET\_REQUEST\_WIFI\_CMD\_AP\_CONFIG\_PARAM | Configure AP parameter. |
| NET\_REQUEST\_WIFI\_CMD\_DPP | DPP actions. |
| NET\_REQUEST\_WIFI\_CMD\_PMKSA\_FLUSH | Flush PMKSA cache entries. |
| NET\_REQUEST\_WIFI\_CMD\_ENTERPRISE\_CREDS | Set enterprise mode credential. |
| NET\_REQUEST\_WIFI\_CMD\_RTS\_THRESHOLD\_CONFIG | Get RTS threshold. |
| NET\_REQUEST\_WIFI\_CMD\_WPS\_CONFIG | WPS config. |
| NET\_REQUEST\_WIFI\_CMD\_START\_ROAMING | Start roaming. |
| NET\_REQUEST\_WIFI\_CMD\_NEIGHBOR\_REP\_COMPLETE | Neighbor report complete. |
| NET\_REQUEST\_WIFI\_CMD\_CANDIDATE\_SCAN | Specific scan. |

## [◆ ](#ga83546cf946a9123c563609e8903d9642)wifi\_ap\_config\_param

| enum [wifi\_ap\_config\_param](#ga83546cf946a9123c563609e8903d9642) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi AP mode configuration parameter.

| Enumerator | |
| --- | --- |
| WIFI\_AP\_CONFIG\_PARAM\_MAX\_INACTIVITY | Used for AP mode configuration parameter ap\_max\_inactivity. |
| WIFI\_AP\_CONFIG\_PARAM\_MAX\_NUM\_STA | Used for AP mode configuration parameter max\_num\_sta. |

## [◆ ](#gaaf730bf76adc06434c7ac63bf0417884)wifi\_ap\_status

| enum [wifi\_ap\_status](#gaaf730bf76adc06434c7ac63bf0417884) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi AP mode result codes.

To be overlaid on top of [wifi\_status](structwifi__status.md "wifi_status") in the AP mode enable or disable result event for detailed status.

| Enumerator | |
| --- | --- |
| WIFI\_STATUS\_AP\_SUCCESS | AP mode enable or disable successful. |
| WIFI\_STATUS\_AP\_FAIL | AP mode enable or disable failed - generic failure. |
| WIFI\_STATUS\_AP\_CHANNEL\_NOT\_SUPPORTED | AP mode enable failed - channel not supported. |
| WIFI\_STATUS\_AP\_CHANNEL\_NOT\_ALLOWED | AP mode enable failed - channel not allowed. |
| WIFI\_STATUS\_AP\_SSID\_NOT\_ALLOWED | AP mode enable failed - SSID not allowed. |
| WIFI\_STATUS\_AP\_AUTH\_TYPE\_NOT\_SUPPORTED | AP mode enable failed - authentication type not supported. |
| WIFI\_STATUS\_AP\_OP\_NOT\_SUPPORTED | AP mode enable failed - operation not supported. |
| WIFI\_STATUS\_AP\_OP\_NOT\_PERMITTED | AP mode enable failed - operation not permitted. |

## [◆ ](#ga7f7b23ac019ca504a2006f0376735645)wifi\_cipher\_type

| enum [wifi\_cipher\_type](#ga7f7b23ac019ca504a2006f0376735645) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Group cipher and pairwise cipher types.

| Enumerator | |
| --- | --- |
| WPA\_CAPA\_ENC\_CCMP | AES in counter mode with CBC-MAC (CCMP-128). |
| WPA\_CAPA\_ENC\_GCMP | 128-bit Galois/Counter Mode Protocol. |
| WPA\_CAPA\_ENC\_GCMP\_256 | 256-bit Galois/Counter Mode Protocol. |

## [◆ ](#gad98099584d2222ede93aba42b1fbaff0)wifi\_config\_ps\_param\_fail\_reason

| enum [wifi\_config\_ps\_param\_fail\_reason](#gad98099584d2222ede93aba42b1fbaff0) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi power save error codes.

| Enumerator | |
| --- | --- |
| WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED | Unspecified error. |
| WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL | Command execution failed. |
| WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED | Parameter not supported. |
| WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS | Unable to get interface status. |
| WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED | Device not connected to AP. |
| WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED | Device already connected to AP. |
| WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID | Listen interval out of range. |
| WIFI\_PS\_PARAM\_FAIL\_INVALID\_EXIT\_STRATEGY | Invalid exit strategy. |

## [◆ ](#ga86a5741e54aeb3e290142b0de217b8a8)wifi\_conn\_status

| enum [wifi\_conn\_status](#ga86a5741e54aeb3e290142b0de217b8a8) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi connect result codes.

To be overlaid on top of [wifi\_status](structwifi__status.md "wifi_status") in the connect result event for detailed status.

| Enumerator | |
| --- | --- |
| WIFI\_STATUS\_CONN\_SUCCESS | Connection successful. |
| WIFI\_STATUS\_CONN\_FAIL | Connection failed - generic failure. |
| WIFI\_STATUS\_CONN\_WRONG\_PASSWORD | Connection failed - wrong password Few possible reasons for 4-way handshake failure that we can guess are as follows: 1) Incorrect key 2) EAPoL frames lost causing timeout.  #1 is the likely cause, so, we convey to the user that it is due to Wrong passphrase/password. |
| WIFI\_STATUS\_CONN\_TIMEOUT | Connection timed out. |
| WIFI\_STATUS\_CONN\_AP\_NOT\_FOUND | Connection failed - AP not found. |
| WIFI\_STATUS\_CONN\_LAST\_STATUS | Last connection status. |
| WIFI\_STATUS\_DISCONN\_FIRST\_STATUS | Connection disconnected status. |

## [◆ ](#gac782af0a60b202fd19597cabb7bd3a9a)wifi\_disconn\_reason

| enum [wifi\_disconn\_reason](#gac782af0a60b202fd19597cabb7bd3a9a) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi disconnect reason codes.

To be overlaid on top of [wifi\_status](structwifi__status.md "wifi_status") in the disconnect result event for detailed reason.

| Enumerator | |
| --- | --- |
| WIFI\_REASON\_DISCONN\_SUCCESS | Success, overload status as reason. |
| WIFI\_REASON\_DISCONN\_UNSPECIFIED | Unspecified reason. |
| WIFI\_REASON\_DISCONN\_USER\_REQUEST | Disconnected due to user request. |
| WIFI\_REASON\_DISCONN\_AP\_LEAVING | Disconnected due to AP leaving. |
| WIFI\_REASON\_DISCONN\_INACTIVITY | Disconnected due to inactivity. |

## [◆ ](#ga92b6fa6755491c3bd61f895213d07331)wifi\_eap\_type

| enum [wifi\_eap\_type](#ga92b6fa6755491c3bd61f895213d07331) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

EPA method Types.

| Enumerator | |
| --- | --- |
| WIFI\_EAP\_TYPE\_NONE | No EPA security. |
| WIFI\_EAP\_TYPE\_GTC | EPA GTC security, refer to rfc3748 chapter 5. |
| WIFI\_EAP\_TYPE\_TLS | EPA TLS security, refer to rfc5216. |
| WIFI\_EAP\_TYPE\_TTLS | EPA TTLS security, refer to rfc5281. |
| WIFI\_EAP\_TYPE\_PEAP | EPA PEAP security, refer to draft-josefsson-pppext-eap-tls-eap-06.txt. |
| WIFI\_EAP\_TYPE\_MSCHAPV2 | EPA MSCHAPV2 security, refer to draft-kamath-pppext-eap-mschapv2-00.txt. |

## [◆ ](#gaa60495242c66a3fac294886856121c1f)wifi\_filter

| enum [wifi\_filter](#gaa60495242c66a3fac294886856121c1f) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Mode filter settings.

| Enumerator | |
| --- | --- |
| WIFI\_PACKET\_FILTER\_ALL | Support management, data and control packet sniffing. |
| WIFI\_PACKET\_FILTER\_MGMT | Support only sniffing of management packets. |
| WIFI\_PACKET\_FILTER\_DATA | Support only sniffing of data packets. |
| WIFI\_PACKET\_FILTER\_CTRL | Support only sniffing of control packets. |

## [◆ ](#ga1e2f0439a322355fa7368ea880c9c15d)wifi\_frequency\_bands

| enum [wifi\_frequency\_bands](#ga1e2f0439a322355fa7368ea880c9c15d) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

IEEE 802.11 operational frequency bands (not exhaustive).

| Enumerator | |
| --- | --- |
| WIFI\_FREQ\_BAND\_2\_4\_GHZ | 2.4 GHz band. |
| WIFI\_FREQ\_BAND\_5\_GHZ | 5 GHz band. |
| WIFI\_FREQ\_BAND\_6\_GHZ | 6 GHz band (Wi-Fi 6E, also extends to 7GHz). |
| WIFI\_FREQ\_BAND\_MAX | Highest frequency band available. |
| WIFI\_FREQ\_BAND\_UNKNOWN | Invalid frequency band. |

## [◆ ](#gaf84d5e1a68393483fc6063c06b8f26e0)wifi\_group\_mgmt\_cipher\_type

| enum [wifi\_group\_mgmt\_cipher\_type](#gaf84d5e1a68393483fc6063c06b8f26e0) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

group mgmt cipher types.

| Enumerator | |
| --- | --- |
| WPA\_CAPA\_ENC\_BIP | 128-bit Broadcast/Multicast Integrity Protocol Cipher-based Message Authentication Code . |
| WPA\_CAPA\_ENC\_BIP\_GMAC\_128 | 128-bit Broadcast/Multicast Integrity Protocol Galois Message Authentication Code . |
| WPA\_CAPA\_ENC\_BIP\_GMAC\_256 | 256-bit Broadcast/Multicast Integrity Protocol Galois Message Authentication Code . |

## [◆ ](#gafb2e8c10f596da3527abf9e227c3001b)wifi\_hostapd\_iface\_state

| enum [wifi\_hostapd\_iface\_state](#gafb2e8c10f596da3527abf9e227c3001b) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi AP status.

| Enumerator | |
| --- | --- |
| WIFI\_HAPD\_IFACE\_UNINITIALIZED |  |
| WIFI\_HAPD\_IFACE\_DISABLED |  |
| WIFI\_HAPD\_IFACE\_COUNTRY\_UPDATE |  |
| WIFI\_HAPD\_IFACE\_ACS |  |
| WIFI\_HAPD\_IFACE\_HT\_SCAN |  |
| WIFI\_HAPD\_IFACE\_DFS |  |
| WIFI\_HAPD\_IFACE\_ENABLED |  |

## [◆ ](#ga584f6239ac14e2bedc5e6bd72756423b)wifi\_iface\_mode

| enum [wifi\_iface\_mode](#ga584f6239ac14e2bedc5e6bd72756423b) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi interface modes.

Based on [https://w1.fi/wpa\_supplicant/devel/defs\_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc](https://w1.fi/wpa_supplicant/devel/defs_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc)

| Enumerator | |
| --- | --- |
| WIFI\_MODE\_INFRA | Infrastructure station mode. |
| WIFI\_MODE\_IBSS | IBSS (ad-hoc) station mode. |
| WIFI\_MODE\_AP | AP mode. |
| WIFI\_MODE\_P2P\_GO | P2P group owner mode. |
| WIFI\_MODE\_P2P\_GROUP\_FORMATION | P2P group formation mode. |
| WIFI\_MODE\_MESH | 802.11s Mesh mode. |

## [◆ ](#ga981961f747b919d61d3ccbd41e4508b4)wifi\_iface\_state

| enum [wifi\_iface\_state](#ga981961f747b919d61d3ccbd41e4508b4) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi interface states.

Based on [https://w1.fi/wpa\_supplicant/devel/defs\_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc](https://w1.fi/wpa_supplicant/devel/defs_8h.html#a4aeb27c1e4abd046df3064ea9756f0bc)

| Enumerator | |
| --- | --- |
| WIFI\_STATE\_DISCONNECTED | Interface is disconnected. |
| WIFI\_STATE\_INTERFACE\_DISABLED | Interface is disabled (administratively). |
| WIFI\_STATE\_INACTIVE | No enabled networks in the configuration. |
| WIFI\_STATE\_SCANNING | Interface is scanning for networks. |
| WIFI\_STATE\_AUTHENTICATING | Authentication with a network is in progress. |
| WIFI\_STATE\_ASSOCIATING | Association with a network is in progress. |
| WIFI\_STATE\_ASSOCIATED | Association with a network completed. |
| WIFI\_STATE\_4WAY\_HANDSHAKE | 4-way handshake with a network is in progress. |
| WIFI\_STATE\_GROUP\_HANDSHAKE | Group Key exchange with a network is in progress. |
| WIFI\_STATE\_COMPLETED | All authentication completed, ready to pass data. |

## [◆ ](#gabdb2a784d4727b71ab44cca04e422c62)wifi\_link\_mode

| enum [wifi\_link\_mode](#gabdb2a784d4727b71ab44cca04e422c62) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi link operating modes.

As per [https://en.wikipedia.org/wiki/Wi-Fi#Versions\_and\_generations](https://en.wikipedia.org/wiki/Wi-Fi#Versions_and_generations).

| Enumerator | |
| --- | --- |
| WIFI\_0 | 802.11 (legacy). |
| WIFI\_1 | 802.11b. |
| WIFI\_2 | 802.11a. |
| WIFI\_3 | 802.11g. |
| WIFI\_4 | 802.11n. |
| WIFI\_5 | 802.11ac. |
| WIFI\_6 | 802.11ax. |
| WIFI\_6E | 802.11ax 6GHz. |
| WIFI\_7 | 802.11be. |

## [◆ ](#ga1f252da47d9650023d7fff6d08e49c76)wifi\_mfp\_options

| enum [wifi\_mfp\_options](#ga1f252da47d9650023d7fff6d08e49c76) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

IEEE 802.11w - Management frame protection.

| Enumerator | |
| --- | --- |
| WIFI\_MFP\_DISABLE | MFP disabled. |
| WIFI\_MFP\_OPTIONAL | MFP optional. |
| WIFI\_MFP\_REQUIRED | MFP required. |

## [◆ ](#gae129d0783276e662575af2314eef86cd)wifi\_mgmt\_op

| enum [wifi\_mgmt\_op](#gae129d0783276e662575af2314eef86cd) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Generic get/set operation for any command.

| Enumerator | |
| --- | --- |
| WIFI\_MGMT\_GET | Get operation. |
| WIFI\_MGMT\_SET | Set operation. |

## [◆ ](#ga4a9243eeb974111d6047fd3d8d9cbf35)wifi\_operational\_modes

| enum [wifi\_operational\_modes](#ga4a9243eeb974111d6047fd3d8d9cbf35) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wifi operational mode.

| Enumerator | |
| --- | --- |
| WIFI\_STA\_MODE | STA mode setting enable. |
| WIFI\_MONITOR\_MODE | Monitor mode setting enable. |
| WIFI\_TX\_INJECTION\_MODE | TX injection mode setting enable. |
| WIFI\_PROMISCUOUS\_MODE | Promiscuous mode setting enable. |
| WIFI\_AP\_MODE | AP mode setting enable. |
| WIFI\_SOFTAP\_MODE | Softap mode setting enable. |

## [◆ ](#ga0fffeb57b68fb8cdef9d3d571368b8ca)wifi\_ps

| enum [wifi\_ps](#ga0fffeb57b68fb8cdef9d3d571368b8ca) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi power save states.

| Enumerator | |
| --- | --- |
| WIFI\_PS\_DISABLED | Power save disabled. |
| WIFI\_PS\_ENABLED | Power save enabled. |

## [◆ ](#ga2d424d1711389fb784e916a87ff854b7)wifi\_ps\_exit\_strategy

| enum [wifi\_ps\_exit\_strategy](#ga2d424d1711389fb784e916a87ff854b7) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi power save exit strategy.

| Enumerator | |
| --- | --- |
| WIFI\_PS\_EXIT\_CUSTOM\_ALGO | PS-Poll frame based. |
| WIFI\_PS\_EXIT\_EVERY\_TIM | QoS NULL frame based. |

## [◆ ](#gaffae7d2a754be5eb952ad2b83edad54c)wifi\_ps\_mode

| enum [wifi\_ps\_mode](#gaffae7d2a754be5eb952ad2b83edad54c) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi power save modes.

| Enumerator | |
| --- | --- |
| WIFI\_PS\_MODE\_LEGACY | Legacy power save mode. |
| WIFI\_PS\_MODE\_WMM | WMM power save mode. |

## [◆ ](#gabe45d132797047c098041331c8f6f912)wifi\_ps\_param\_type

| enum [wifi\_ps\_param\_type](#gabe45d132797047c098041331c8f6f912) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi power save parameters.

| Enumerator | |
| --- | --- |
| WIFI\_PS\_PARAM\_STATE | Power save state. |
| WIFI\_PS\_PARAM\_LISTEN\_INTERVAL | Power save listen interval. |
| WIFI\_PS\_PARAM\_WAKEUP\_MODE | Power save wakeup mode. |
| WIFI\_PS\_PARAM\_MODE | Power save mode. |
| WIFI\_PS\_PARAM\_EXIT\_STRATEGY | Power save exit strategy. |
| WIFI\_PS\_PARAM\_TIMEOUT | Power save timeout. |

## [◆ ](#gac7f907644847e905d67c709fa4afae7f)wifi\_ps\_wakeup\_mode

| enum [wifi\_ps\_wakeup\_mode](#gac7f907644847e905d67c709fa4afae7f) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi power save modes.

| Enumerator | |
| --- | --- |
| WIFI\_PS\_WAKEUP\_MODE\_DTIM | DTIM based wakeup. |
| WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL | Listen interval based wakeup. |

## [◆ ](#gad30e29eda65ccafdbd7f11865937b8ea)wifi\_scan\_type

| enum [wifi\_scan\_type](#gad30e29eda65ccafdbd7f11865937b8ea) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi scanning types.

| Enumerator | |
| --- | --- |
| WIFI\_SCAN\_TYPE\_ACTIVE | Active scanning (default). |
| WIFI\_SCAN\_TYPE\_PASSIVE | Passive scanning. |

## [◆ ](#gadde31a04fa25ed805115c6b31854cd9c)wifi\_security\_type

| enum [wifi\_security\_type](#gadde31a04fa25ed805115c6b31854cd9c) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

IEEE 802.11 security types.

| Enumerator | |
| --- | --- |
| WIFI\_SECURITY\_TYPE\_NONE | No security. |
| WIFI\_SECURITY\_TYPE\_PSK | WPA2-PSK security. |
| WIFI\_SECURITY\_TYPE\_PSK\_SHA256 | WPA2-PSK-SHA256 security. |
| WIFI\_SECURITY\_TYPE\_SAE | WPA3-SAE security. |
| WIFI\_SECURITY\_TYPE\_SAE\_HNP | WPA3-SAE security with hunting-and-pecking loop. |
| WIFI\_SECURITY\_TYPE\_SAE\_H2E | WPA3-SAE security with hash-to-element. |
| WIFI\_SECURITY\_TYPE\_SAE\_AUTO | WPA3-SAE security with both hunting-and-pecking loop and hash-to-element enabled. |
| WIFI\_SECURITY\_TYPE\_WAPI | GB 15629.11-2003 WAPI security. |
| WIFI\_SECURITY\_TYPE\_EAP | EAP security - Enterprise. |
| WIFI\_SECURITY\_TYPE\_EAP\_TLS | EAP TLS security - Enterprise. |
| WIFI\_SECURITY\_TYPE\_WEP | WEP security. |
| WIFI\_SECURITY\_TYPE\_WPA\_PSK | WPA-PSK security. |
| WIFI\_SECURITY\_TYPE\_WPA\_AUTO\_PERSONAL | WPA/WPA2/WPA3 PSK security. |
| WIFI\_SECURITY\_TYPE\_DPP | DPP security. |
| WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_MSCHAPV2 | EAP PEAP MSCHAPV2 security - Enterprise. |
| WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_GTC | EAP PEAP GTC security - Enterprise. |
| WIFI\_SECURITY\_TYPE\_EAP\_TTLS\_MSCHAPV2 | EAP TTLS MSCHAPV2 security - Enterprise. |
| WIFI\_SECURITY\_TYPE\_EAP\_PEAP\_TLS | EAP PEAP security - Enterprise. |
| WIFI\_SECURITY\_TYPE\_EAP\_TLS\_SHA256 | EAP TLS SHA256 security - Enterprise. |
| WIFI\_SECURITY\_TYPE\_FT\_PSK | FT-PSK security. |
| WIFI\_SECURITY\_TYPE\_FT\_SAE | FT-SAE security. |
| WIFI\_SECURITY\_TYPE\_FT\_EAP | FT-EAP security. |
| WIFI\_SECURITY\_TYPE\_FT\_EAP\_SHA384 | FT-EAP-SHA384 security. |

## [◆ ](#ga168e7affe48d72d7d1e3ccddb63fe5a7)wifi\_suiteb\_type

| enum [wifi\_suiteb\_type](#ga168e7affe48d72d7d1e3ccddb63fe5a7) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Enterprise security WPA3 suiteb types.

| Enumerator | |
| --- | --- |
| WIFI\_SUITEB | suiteb. |
| WIFI\_SUITEB\_192 | suiteb-192. |

## [◆ ](#ga97fa304f9a1db2294a93cccd4c93bcf6)wifi\_twt\_fail\_reason

| enum [wifi\_twt\_fail\_reason](#ga97fa304f9a1db2294a93cccd4c93bcf6) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Target Wake Time (TWT) error codes.

| Enumerator | |
| --- | --- |
| WIFI\_TWT\_FAIL\_UNSPECIFIED | Unspecified error. |
| WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL | Command execution failed. |
| WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED | Operation not supported. |
| WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS | Unable to get interface status. |
| WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED | Device not connected to AP. |
| WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB | Peer not HE (802.11ax/Wi-Fi 6) capable. |
| WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB | Peer not TWT capable. |
| WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS | A TWT flow is already in progress. |
| WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID | Invalid negotiated flow id. |
| WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED | IP address not assigned or configured. |
| WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS | Flow already exists. |

## [◆ ](#ga695123cd534e2499f516a07fdc5cafa8)wifi\_twt\_negotiation\_type

| enum [wifi\_twt\_negotiation\_type](#ga695123cd534e2499f516a07fdc5cafa8) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi Target Wake Time (TWT) negotiation types.

| Enumerator | |
| --- | --- |
| WIFI\_TWT\_INDIVIDUAL | TWT individual negotiation. |
| WIFI\_TWT\_BROADCAST | TWT broadcast negotiation. |
| WIFI\_TWT\_WAKE\_TBTT | TWT wake TBTT negotiation. |

## [◆ ](#gad0e998aeb1b27c4f203ca76339d323a3)wifi\_twt\_operation

| enum [wifi\_twt\_operation](#gad0e998aeb1b27c4f203ca76339d323a3) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi Target Wake Time (TWT) operations.

| Enumerator | |
| --- | --- |
| WIFI\_TWT\_SETUP | TWT setup operation. |
| WIFI\_TWT\_TEARDOWN | TWT teardown operation. |

## [◆ ](#ga31c78afc89bfdc4b54cee177843f8022)wifi\_twt\_setup\_cmd

| enum [wifi\_twt\_setup\_cmd](#ga31c78afc89bfdc4b54cee177843f8022) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi Target Wake Time (TWT) setup commands.

| Enumerator | |
| --- | --- |
| WIFI\_TWT\_SETUP\_CMD\_REQUEST | TWT setup request. |
| WIFI\_TWT\_SETUP\_CMD\_SUGGEST | TWT setup suggest (parameters can be changed by AP). |
| WIFI\_TWT\_SETUP\_CMD\_DEMAND | TWT setup demand (parameters can not be changed by AP). |
| WIFI\_TWT\_SETUP\_CMD\_GROUPING | TWT setup grouping (grouping of TWT flows). |
| WIFI\_TWT\_SETUP\_CMD\_ACCEPT | TWT setup accept (parameters accepted by AP). |
| WIFI\_TWT\_SETUP\_CMD\_ALTERNATE | TWT setup alternate (alternate parameters suggested by AP). |
| WIFI\_TWT\_SETUP\_CMD\_DICTATE | TWT setup dictate (parameters dictated by AP). |
| WIFI\_TWT\_SETUP\_CMD\_REJECT | TWT setup reject (parameters rejected by AP). |

## [◆ ](#ga4d03aedac13ee4512d7717ac624f319a)wifi\_twt\_setup\_resp\_status

| enum [wifi\_twt\_setup\_resp\_status](#ga4d03aedac13ee4512d7717ac624f319a) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi Target Wake Time (TWT) negotiation status.

| Enumerator | |
| --- | --- |
| WIFI\_TWT\_RESP\_RECEIVED | TWT response received for TWT request. |
| WIFI\_TWT\_RESP\_NOT\_RECEIVED | TWT response not received for TWT request. |

## [◆ ](#ga38c184ea35c02f304cccdf389ca6d552)wifi\_twt\_sleep\_state

| enum [wifi\_twt\_sleep\_state](#ga38c184ea35c02f304cccdf389ca6d552) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi TWT sleep states.

| Enumerator | |
| --- | --- |
| WIFI\_TWT\_STATE\_SLEEP | TWT sleep state: sleeping. |
| WIFI\_TWT\_STATE\_AWAKE | TWT sleep state: awake. |

## [◆ ](#gad3709d07aaa3ed59b48f9dd7bd181989)wifi\_twt\_teardown\_status

| enum [wifi\_twt\_teardown\_status](#gad3709d07aaa3ed59b48f9dd7bd181989) |
| --- |

`#include <[wifi.h](wifi_8h.md)>`

Wi-Fi Target Wake Time (TWT) teradown status.

| Enumerator | |
| --- | --- |
| WIFI\_TWT\_TEARDOWN\_SUCCESS | TWT teardown success. |
| WIFI\_TWT\_TEARDOWN\_FAILED | TWT teardown failure. |

## [◆ ](#ga4c36ae1a5171d3fbaeebf95c16be496d)wifi\_wps\_op

| enum [wifi\_wps\_op](#ga4c36ae1a5171d3fbaeebf95c16be496d) |
| --- |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Operation for WPS.

| Enumerator | |
| --- | --- |
| WIFI\_WPS\_PBC | WPS pbc. |
| WIFI\_WPS\_PIN\_GET | Get WPS pin number. |
| WIFI\_WPS\_PIN\_SET | Set WPS pin number. |

## Function Documentation

## [◆ ](#ga44f875bf0d931b66d582f5dca2d65ed5)wifi\_band\_txt()

| const char \* wifi\_band\_txt | ( | enum [wifi\_frequency\_bands](#ga1e2f0439a322355fa7368ea880c9c15d) | *band* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly frequency band name.

## [◆ ](#ga0d9d6e2150fb187025300904357f7b4d)wifi\_link\_mode\_txt()

| const char \* wifi\_link\_mode\_txt | ( | enum [wifi\_link\_mode](#gabdb2a784d4727b71ab44cca04e422c62) | *link\_mode* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly link mode name.

## [◆ ](#ga22354241197a9227fdba77e67d471f5c)wifi\_mfp\_txt()

| const char \* wifi\_mfp\_txt | ( | enum [wifi\_mfp\_options](#ga1f252da47d9650023d7fff6d08e49c76) | *mfp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly MFP name.

## [◆ ](#gadee15c6a492a8ee13bea43812debb5d9)wifi\_mgmt\_raise\_ap\_disable\_result\_event()

| void wifi\_mgmt\_raise\_ap\_disable\_result\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | enum [wifi\_ap\_status](#gaaf730bf76adc06434c7ac63bf0417884) | *status* ) |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management AP mode disable result event.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | status | AP mode disable result status |

## [◆ ](#ga67b52edeff76c2211b038f4aa90b8982)wifi\_mgmt\_raise\_ap\_enable\_result\_event()

| void wifi\_mgmt\_raise\_ap\_enable\_result\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | enum [wifi\_ap\_status](#gaaf730bf76adc06434c7ac63bf0417884) | *status* ) |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management AP mode enable result event.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | status | AP mode enable result status |

## [◆ ](#gac8f17f0aa3e426a5cdb731727b9b9ce3)wifi\_mgmt\_raise\_ap\_sta\_connected\_event()

| void wifi\_mgmt\_raise\_ap\_sta\_connected\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \* | *sta\_info* ) |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management AP mode STA connected event.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | sta\_info | STA information |

## [◆ ](#ga49fb9c3908be61d847b31c99be6afc42)wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event()

| void wifi\_mgmt\_raise\_ap\_sta\_disconnected\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [wifi\_ap\_sta\_info](structwifi__ap__sta__info.md) \* | *sta\_info* ) |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management AP mode STA disconnected event.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | sta\_info | STA information |

## [◆ ](#ga036416696b1e3bc458ddbaf07a08d69d)wifi\_mgmt\_raise\_connect\_result\_event()

| void wifi\_mgmt\_raise\_connect\_result\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | int | *status* ) |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management connect result event.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | status | Connect result status |

## [◆ ](#gaa75246d6dc55dada389c9d31e2607d5c)wifi\_mgmt\_raise\_disconnect\_complete\_event()

| void wifi\_mgmt\_raise\_disconnect\_complete\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | int | *status* ) |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management disconnect complete event.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | status | Disconnect complete status |

## [◆ ](#ga3b6edcf9b51afbf7a327d1a344bd7b87)wifi\_mgmt\_raise\_disconnect\_result\_event()

| void wifi\_mgmt\_raise\_disconnect\_result\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | int | *status* ) |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management disconnect result event.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | status | Disconnect result status |

## [◆ ](#ga7da6af0747bcba85f8afab30c92b5b43)wifi\_mgmt\_raise\_iface\_status\_event()

| void wifi\_mgmt\_raise\_iface\_status\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [wifi\_iface\_status](structwifi__iface__status.md) \* | *iface\_status* ) |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management interface status event.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | iface\_status | Interface status |

## [◆ ](#ga71c99913bded844c4ca32ed9155bc470)wifi\_mgmt\_raise\_raw\_scan\_result\_event()

| void wifi\_mgmt\_raise\_raw\_scan\_result\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [wifi\_raw\_scan\_result](structwifi__raw__scan__result.md) \* | *raw\_scan\_info* ) |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management raw scan result event.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | raw\_scan\_info | Raw scan result |

## [◆ ](#ga39404d15243ca084b253cae8fc07e374)wifi\_mgmt\_raise\_twt\_event()

| void wifi\_mgmt\_raise\_twt\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [wifi\_twt\_params](structwifi__twt__params.md) \* | *twt\_params* ) |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management TWT event.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | twt\_params | TWT parameters |

## [◆ ](#ga18f09a3196588b51d6c0644f82f639d7)wifi\_mgmt\_raise\_twt\_sleep\_state()

| void wifi\_mgmt\_raise\_twt\_sleep\_state | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | int | *twt\_sleep\_state* ) |

`#include <[wifi_mgmt.h](wifi__mgmt_8h.md)>`

Wi-Fi management TWT sleep state event.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | twt\_sleep\_state | TWT sleep state |

## [◆ ](#gad78536ce1f30accfa45f258b6bf8c73d)wifi\_mode\_txt()

| const char \* wifi\_mode\_txt | ( | enum [wifi\_iface\_mode](#ga584f6239ac14e2bedc5e6bd72756423b) | *mode* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly interface mode name.

## [◆ ](#gade667a55793caef820b570a248052327)wifi\_ps\_exit\_strategy\_txt()

| const char \*const wifi\_ps\_exit\_strategy\_txt | ( | enum [wifi\_ps\_exit\_strategy](#ga2d424d1711389fb784e916a87ff854b7) | *ps\_exit\_strategy* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly ps exit strategy name.

## [◆ ](#ga8b72e7989964963a25f42ed1dba240a0)wifi\_ps\_get\_config\_err\_code\_str()

| | const char \* wifi\_ps\_get\_config\_err\_code\_str | ( | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *err\_no* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly power save error code name.

## [◆ ](#gadb21d49f64e04fba59433e51d5b3481c)wifi\_ps\_mode\_txt()

| const char \* wifi\_ps\_mode\_txt | ( | enum [wifi\_ps\_mode](#gaffae7d2a754be5eb952ad2b83edad54c) | *ps\_mode* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly ps mode name.

## [◆ ](#gafbeb5f7fa97fd2ba0c691da0f8853ef2)wifi\_ps\_txt()

| const char \* wifi\_ps\_txt | ( | enum [wifi\_ps](#ga0fffeb57b68fb8cdef9d3d571368b8ca) | *ps\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly ps name.

## [◆ ](#ga6fd645f891234136b3028574a0af9666)wifi\_ps\_wakeup\_mode\_txt()

| const char \* wifi\_ps\_wakeup\_mode\_txt | ( | enum [wifi\_ps\_wakeup\_mode](#gac7f907644847e905d67c709fa4afae7f) | *ps\_wakeup\_mode* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly ps wakeup mode name.

## [◆ ](#ga9bb9f658d7806e42b3ee351fb3e7dfa0)wifi\_security\_txt()

| const char \* wifi\_security\_txt | ( | enum [wifi\_security\_type](#gadde31a04fa25ed805115c6b31854cd9c) | *security* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly security type name.

## [◆ ](#ga03d306912dc96178e21d3c82c104582f)wifi\_state\_txt()

| const char \* wifi\_state\_txt | ( | enum [wifi\_iface\_state](#ga981961f747b919d61d3ccbd41e4508b4) | *state* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly interface state name.

## [◆ ](#gab2e6a6e1d8358a8f34d67bd632709b3d)wifi\_twt\_get\_err\_code\_str()

| | const char \* wifi\_twt\_get\_err\_code\_str | ( | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *err\_no* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly TWT error code name.

## [◆ ](#ga6a74e999d63ee491df68447219ef2a0d)wifi\_twt\_negotiation\_type\_txt()

| const char \* wifi\_twt\_negotiation\_type\_txt | ( | enum [wifi\_twt\_negotiation\_type](#ga695123cd534e2499f516a07fdc5cafa8) | *twt\_negotiation* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly twt negotiation type name.

## [◆ ](#gadb125925e851bf7569424cd4295e7712)wifi\_twt\_operation\_txt()

| const char \* wifi\_twt\_operation\_txt | ( | enum [wifi\_twt\_operation](#gad0e998aeb1b27c4f203ca76339d323a3) | *twt\_operation* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly twt operation name.

## [◆ ](#gae3ca047cc6ef6b6a2e44ba6574d41a44)wifi\_twt\_setup\_cmd\_txt()

| const char \* wifi\_twt\_setup\_cmd\_txt | ( | enum [wifi\_twt\_setup\_cmd](#ga31c78afc89bfdc4b54cee177843f8022) | *twt\_setup* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi.h](wifi_8h.md)>`

Helper function to get user-friendly twt setup cmd name.

## [◆ ](#ga4c91cd7dff0fd9e5402970f3222dc20d)wifi\_utils\_parse\_scan\_bands()

| int wifi\_utils\_parse\_scan\_bands | ( | char \* | *scan\_bands\_str*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *band\_map* ) |

`#include <[wifi_utils.h](wifi__utils_8h.md)>`

Convert a band specification string to a bitmap representing the bands.

The function will parse a string which specifies Wi-Fi frequency band values as a comma separated string and convert it to a bitmap. The string can use the following characters to represent the bands:

- 2: 2.4 GHz
- 5: 5 GHz
- 6: 6 GHz

For the bitmap generated refer to [wifi\_frequency\_bands](#ga1e2f0439a322355fa7368ea880c9c15d) for bit position of each band.

E.g. a string "2,5,6" will be converted to a bitmap value of 0x7

Parameters
:   | scan\_bands\_str | String which spe. |
    | --- | --- |
    | band\_map | Pointer to the bitmap variable to be updated. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -errno | value in case of failure. |

## [◆ ](#gaba9f3117bcef9da1efc1841d3bd9adfd)wifi\_utils\_parse\_scan\_chan()

| int wifi\_utils\_parse\_scan\_chan | ( | char \* | *scan\_chan\_str*, |
| --- | --- | --- | --- |
|  |  | struct [wifi\_band\_channel](structwifi__band__channel.md) \* | *chan*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *max\_channels* ) |

`#include <[wifi_utils.h](wifi__utils_8h.md)>`

Convert a string containing a specification of scan channels to an array.

The function will parse a string which specifies channels to be scanned as a string and convert it to an array.

The channel string has to be formatted using the colon (:), comma(,), hyphen (-) and underscore (\_) delimiters as follows:

- A colon identifies the value preceding it as a band. A band value (2: 2.4 GHz, 5: 5 GHz 6: 6 GHz) has to precede the channels in that band (e.g. 2: etc)
- Hyphens (-) are used to identify channel ranges (e.g. 2-7, 32-48 etc)
- Commas are used to separate channel values within a band. Channels can be specified as individual values (2,6,48 etc) or channel ranges using hyphens (1-14, 32-48 etc)
- Underscores (\_) are used to specify multiple band-channel sets (e.g. 2:1,2\_5:36,40 etc)
- No spaces should be used anywhere, i.e. before/after commas, before/after hyphens etc.

An example channel specification specifying channels in the 2.4 GHz and 5 GHz bands is as below: 2:1,5,7,9-11\_5:36-48,100,163-167

Parameters
:   | scan\_chan\_str | List of channels expressed in the format described above. |
    | --- | --- |
    | chan | Pointer to an array where the parsed channels are to be stored. |
    | max\_channels | Maximum number of channels to store |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -errno | value in case of failure. |

## [◆ ](#ga471a96d3fb6d610a591508b52d4c05a4)wifi\_utils\_parse\_scan\_ssids()

| int wifi\_utils\_parse\_scan\_ssids | ( | char \* | *scan\_ssids\_str*, |
| --- | --- | --- | --- |
|  |  | const char \* | *ssids*[], |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_ssids* ) |

`#include <[wifi_utils.h](wifi__utils_8h.md)>`

Append a string containing an SSID to an array of SSID strings.

Parameters
:   | scan\_ssids\_str | string to be appended in the list of scanned SSIDs. |
    | --- | --- |
    | ssids | Pointer to an array where the SSIDs pointers are to be stored. |
    | num\_ssids | Maximum number of SSIDs that can be stored. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -errno | value in case of failure. |

## [◆ ](#gaf1872d0ed2efd3737a36dcc0ab13f18e)wifi\_utils\_validate\_chan()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_utils\_validate\_chan | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *band*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *chan* ) |

`#include <[wifi_utils.h](wifi__utils_8h.md)>`

Validate a channel against a band.

Parameters
:   | band | Band to validate the channel against. |
    | --- | --- |
    | chan | Channel to validate. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the channel is valid for the band. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if the channel is not valid for the band. |

## [◆ ](#gaf408ba9f75354d3eca735b4804fdf199)wifi\_utils\_validate\_chan\_2g()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_utils\_validate\_chan\_2g | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *chan* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_utils.h](wifi__utils_8h.md)>`

Validate a channel against the 2.4 GHz band.

Parameters
:   | chan | Channel to validate. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the channel is valid for the band. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if the channel is not valid for the band. |

## [◆ ](#gae013eee6d6b74126c29d6ca7b2036310)wifi\_utils\_validate\_chan\_5g()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_utils\_validate\_chan\_5g | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *chan* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_utils.h](wifi__utils_8h.md)>`

Validate a channel against the 5 GHz band.

Parameters
:   | chan | Channel to validate. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the channel is valid for the band. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if the channel is not valid for the band. |

## [◆ ](#ga2606742e23f48da5ca1660aeac47888b)wifi\_utils\_validate\_chan\_6g()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_utils\_validate\_chan\_6g | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *chan* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_utils.h](wifi__utils_8h.md)>`

Validate a channel against the 6 GHz band.

Parameters
:   | chan | Channel to validate. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the channel is valid for the band. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if the channel is not valid for the band. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
