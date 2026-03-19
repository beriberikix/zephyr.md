---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwifi__connect__req__params.html
original_path: doxygen/html/structwifi__connect__req__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_connect\_req\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi connect request parameters.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [ssid](#ac260c2cd17a3f36ea101edaf23d41083) |
|  | SSID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ssid\_length](#a547dddf6be5dd77eda74b1085a798400) |
|  | SSID length. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [psk](#aa7743f0ecbc27a9595720ce13ce57c1d) |
|  | Pre-shared key. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [psk\_length](#aaf7455a65590d19f047214b459a2dcb9) |
|  | Pre-shared key length. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [sae\_password](#a469fac5758b78fc425911837930b2060) |
|  | SAE password (same as PSK but with no length restrictions), optional. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sae\_password\_length](#a74f0819e7a546ffb8bfb0ec587eccf20) |
|  | SAE password length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [band](#aa2fea1881a8ffdf5d7093ae295867f3e) |
|  | Frequency band. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel](#a52b6d0323c35d03ec239f40be35cae72) |
|  | Channel. |
| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) | [security](#a18dce6bb021086877a30e7a04f5b24b9) |
|  | Security type. |
| enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) | [mfp](#a745b3416172672a7e5b12bcc5b55e88c) |
|  | MFP options. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bssid](#aa8081b9075ff9244cefd0ac1ef3f42cb) [[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)] |
|  | BSSID. |
| int | [timeout](#a56183ba7f4d8eaf5fc5b495856adecfd) |
|  | Connect timeout in seconds, SYS\_FOREVER\_MS for no timeout. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [anon\_id](#a781456e079357e2e1096218af3bd218c) |
|  | anonymous identity |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [aid\_length](#a2892253024b70e5cb8eb2166b17ebe22) |
|  | anon\_id length, max 64 |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [key\_passwd](#a4946647659a347667ee49bb6990bba66) |
|  | Private key passwd for enterprise mode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [key\_passwd\_length](#a9f913fc0ccecafaba488e444d701fd68) |
|  | Private key passwd length, max 128. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [key2\_passwd](#a020fc58d7e5350cc803cd5d6fa575e6a) |
|  | private key2 passwd |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [key2\_passwd\_length](#af7b163cc2bffc59f7fa31f47c5e52062) |
|  | key2 passwd length, max 128 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [suiteb\_type](#ac8eaaecd8227e5500bdaf8cddf05a065) |
|  | suiteb or suiteb-192 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [eap\_ver](#aa903297e7ee4801b350b2e3a3a89f28a) |
|  | eap version |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [eap\_identity](#ab9c65599409387af65a3c2895c3116da) |
|  | Identity for EAP. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [eap\_id\_length](#a4da02ff112c09f55dc5bddcda27d16a3) |
|  | eap identity length, max 64 |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [eap\_password](#afd046e702739c4a0d89322ee41b37acd) |
|  | Password string for EAP. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [eap\_passwd\_length](#aeab22e95a04a1831b87beda1772d3db7) |
|  | eap passwd length, max 128 |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ft\_used](#a047b11e703fb646d778785dfcb14257b) |
|  | Fast BSS Transition used. |

## Detailed Description

Wi-Fi connect request parameters.

## Field Documentation

## [◆ ](#a2892253024b70e5cb8eb2166b17ebe22)aid\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::aid\_length |
| --- |

anon\_id length, max 64

## [◆ ](#a781456e079357e2e1096218af3bd218c)anon\_id

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_connect\_req\_params::anon\_id |
| --- |

anonymous identity

## [◆ ](#aa2fea1881a8ffdf5d7093ae295867f3e)band

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::band |
| --- |

Frequency band.

## [◆ ](#aa8081b9075ff9244cefd0ac1ef3f42cb)bssid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::bssid[[WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)] |
| --- |

BSSID.

## [◆ ](#a52b6d0323c35d03ec239f40be35cae72)channel

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::channel |
| --- |

Channel.

## [◆ ](#a4da02ff112c09f55dc5bddcda27d16a3)eap\_id\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::eap\_id\_length |
| --- |

eap identity length, max 64

## [◆ ](#ab9c65599409387af65a3c2895c3116da)eap\_identity

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_connect\_req\_params::eap\_identity |
| --- |

Identity for EAP.

## [◆ ](#aeab22e95a04a1831b87beda1772d3db7)eap\_passwd\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::eap\_passwd\_length |
| --- |

eap passwd length, max 128

## [◆ ](#afd046e702739c4a0d89322ee41b37acd)eap\_password

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_connect\_req\_params::eap\_password |
| --- |

Password string for EAP.

## [◆ ](#aa903297e7ee4801b350b2e3a3a89f28a)eap\_ver

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::eap\_ver |
| --- |

eap version

## [◆ ](#a047b11e703fb646d778785dfcb14257b)ft\_used

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_connect\_req\_params::ft\_used |
| --- |

Fast BSS Transition used.

## [◆ ](#a020fc58d7e5350cc803cd5d6fa575e6a)key2\_passwd

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_connect\_req\_params::key2\_passwd |
| --- |

private key2 passwd

## [◆ ](#af7b163cc2bffc59f7fa31f47c5e52062)key2\_passwd\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::key2\_passwd\_length |
| --- |

key2 passwd length, max 128

## [◆ ](#a4946647659a347667ee49bb6990bba66)key\_passwd

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_connect\_req\_params::key\_passwd |
| --- |

Private key passwd for enterprise mode.

## [◆ ](#a9f913fc0ccecafaba488e444d701fd68)key\_passwd\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::key\_passwd\_length |
| --- |

Private key passwd length, max 128.

## [◆ ](#a745b3416172672a7e5b12bcc5b55e88c)mfp

| enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) wifi\_connect\_req\_params::mfp |
| --- |

MFP options.

## [◆ ](#aa7743f0ecbc27a9595720ce13ce57c1d)psk

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_connect\_req\_params::psk |
| --- |

Pre-shared key.

## [◆ ](#aaf7455a65590d19f047214b459a2dcb9)psk\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::psk\_length |
| --- |

Pre-shared key length.

## [◆ ](#a469fac5758b78fc425911837930b2060)sae\_password

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_connect\_req\_params::sae\_password |
| --- |

SAE password (same as PSK but with no length restrictions), optional.

## [◆ ](#a74f0819e7a546ffb8bfb0ec587eccf20)sae\_password\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::sae\_password\_length |
| --- |

SAE password length.

## [◆ ](#a18dce6bb021086877a30e7a04f5b24b9)security

| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) wifi\_connect\_req\_params::security |
| --- |

Security type.

## [◆ ](#ac260c2cd17a3f36ea101edaf23d41083)ssid

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_connect\_req\_params::ssid |
| --- |

SSID.

## [◆ ](#a547dddf6be5dd77eda74b1085a798400)ssid\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::ssid\_length |
| --- |

SSID length.

## [◆ ](#ac8eaaecd8227e5500bdaf8cddf05a065)suiteb\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_connect\_req\_params::suiteb\_type |
| --- |

suiteb or suiteb-192

## [◆ ](#a56183ba7f4d8eaf5fc5b495856adecfd)timeout

| int wifi\_connect\_req\_params::timeout |
| --- |

Connect timeout in seconds, SYS\_FOREVER\_MS for no timeout.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_connect\_req\_params](structwifi__connect__req__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
