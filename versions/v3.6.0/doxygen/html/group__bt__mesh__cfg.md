---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__mesh__cfg.html
original_path: doxygen/html/group__bt__mesh__cfg.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Runtime Configuration

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Runtime Configuration.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Application Configuration](group__bt__mesh__cfg__app.md) |
|  | Application Configuration. |
|  | [Subnet Configuration](group__bt__mesh__cfg__subnet.md) |
|  | Subnet Configuration. |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_KR\_NORMAL](#ga5b3af48dfe15948654b7791d7a684ba8)   0x00 |
| #define | [BT\_MESH\_KR\_PHASE\_1](#ga139d621ce45ea87b4d8a15fc2b29dbe3)   0x01 |
| #define | [BT\_MESH\_KR\_PHASE\_2](#gaff6e8f59719f341ab681268e421b1612)   0x02 |
| #define | [BT\_MESH\_KR\_PHASE\_3](#gab0e65cdc2b152d3b84615223fdaebb2e)   0x03 |
| #define | [BT\_MESH\_RELAY\_DISABLED](#gaafd10319da7d2f938207b8fd6de02dbc)   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_RELAY\_ENABLED](#gae5d235a7c182a8add961d7ce344f87aa)   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_RELAY\_NOT\_SUPPORTED](#gabbbbddd31c2a92256fe2f7a7520e76f7)   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| #define | [BT\_MESH\_BEACON\_DISABLED](#ga8fa3d0ac3cb9f69464c4068ca61689b9)   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_BEACON\_ENABLED](#ga01235217559423b93d7e6cf2236278f0)   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_PRIV\_BEACON\_DISABLED](#ga2645fd9e2aed6de7806e7ac5afd1af10)   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_PRIV\_BEACON\_ENABLED](#ga1f72ffadff83f30943df88cd1ddcbee8)   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_GATT\_PROXY\_DISABLED](#ga3fe3e68efd25a3a03a041b978435fd7b)   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_GATT\_PROXY\_ENABLED](#ga77f4438624aae49ea2bb66437c9623f7)   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_GATT\_PROXY\_NOT\_SUPPORTED](#gaecec3747198a29dd10185e3755e660f8)   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| #define | [BT\_MESH\_PRIV\_GATT\_PROXY\_DISABLED](#ga475302ad8ba5589c7ea95da36f18948e)   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_PRIV\_GATT\_PROXY\_ENABLED](#gac73cdadfd9c9417a051739bce59960a7)   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_PRIV\_GATT\_PROXY\_NOT\_SUPPORTED](#ga66b4ed203ecbc9a70620b5adff04110f)   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| #define | [BT\_MESH\_FRIEND\_DISABLED](#ga29fe48989e760438f2c5241110134c8c)   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_FRIEND\_ENABLED](#gaa23bba212dc1b322651723ca20f497a3)   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_FRIEND\_NOT\_SUPPORTED](#ga35f85e6a9c085cdad4f70b8e60d0b027)   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| #define | [BT\_MESH\_NODE\_IDENTITY\_STOPPED](#ga9a83214cdbd34ac1d4bc644136523bd9)   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| #define | [BT\_MESH\_NODE\_IDENTITY\_RUNNING](#ga86e88acc6fdcc26a9cea4415daad016c)   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| #define | [BT\_MESH\_NODE\_IDENTITY\_NOT\_SUPPORTED](#ga7ffe6722b12a8663518b4e17349e4da5)   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) { [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) , [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) , [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) } |
|  | Bluetooth Mesh feature states. [More...](#ga0a3557a71597885a31cf209c6b83cedb) |

| Functions | |
| --- | --- |
| void | [bt\_mesh\_beacon\_set](#ga15de1cdc964628b6f001ef893021ce6e) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) beacon) |
|  | Enable or disable sending of the Secure Network Beacon. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_beacon\_enabled](#ga479c14f6b0d4a08ddf5b160fa9267844) (void) |
|  | Get the current Secure Network Beacon state. |
| int | [bt\_mesh\_priv\_beacon\_set](#ga1afc5ec210bbc6090ada922ddf75e284) (enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) priv\_beacon) |
|  | Enable or disable sending of the Mesh Private beacon. |
| enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) | [bt\_mesh\_priv\_beacon\_get](#ga2c8dc9ee5c3862790efd2a74a1ef6873) (void) |
|  | Get the current Mesh Private beacon state. |
| void | [bt\_mesh\_priv\_beacon\_update\_interval\_set](#ga01abb07d27edef40ffff4da968065c1d) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval) |
|  | Set the current Mesh Private beacon update interval. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_priv\_beacon\_update\_interval\_get](#gafe3d54c1546b03cebbecaf762ae87781) (void) |
|  | Get the current Mesh Private beacon update interval. |
| int | [bt\_mesh\_default\_ttl\_set](#gaafea57625c9fdba535431cc92dadd162) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) default\_ttl) |
|  | Set the default TTL value. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_default\_ttl\_get](#gaa97f63f5b3167c672fa1a0d8c8fe9ab7) (void) |
|  | Get the current default TTL value. |
| int | [bt\_mesh\_od\_priv\_proxy\_get](#ga256d00139ca40eb99303fef766a3add7) (void) |
|  | Get the current Mesh On-Demand Private Proxy state. |
| int | [bt\_mesh\_od\_priv\_proxy\_set](#ga26023b727e1b180263b22d0ade145f81) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) on\_demand\_proxy) |
|  | Set state of Mesh On-Demand Private Proxy. |
| void | [bt\_mesh\_net\_transmit\_set](#gaa652e4f1460f62252065ac21854ab3f6) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xmit) |
|  | Set the Network Transmit parameters. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_net\_transmit\_get](#ga08b336fa1a4a721ac9b10fbb75e4af6b) (void) |
|  | Get the current Network Transmit parameters. |
| int | [bt\_mesh\_relay\_set](#gad8d6773753b80540b2aaa982c1ec8c03) (enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) relay, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xmit) |
|  | Configure the Relay feature. |
| enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) | [bt\_mesh\_relay\_get](#gadb41d2f78a490aa81b5640bb7ff5a5ce) (void) |
|  | Get the current Relay feature state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_relay\_retransmit\_get](#gaf9abf4bcba55d273a7e6e8ee42c521a9) (void) |
|  | Get the current Relay Retransmit parameters. |
| int | [bt\_mesh\_gatt\_proxy\_set](#gaac543b57580f9ac8dff36c0ce1196144) (enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) gatt\_proxy) |
|  | Enable or disable the GATT Proxy feature. |
| enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) | [bt\_mesh\_gatt\_proxy\_get](#ga8457f222211bc812106b2dccc87b1abe) (void) |
|  | Get the current GATT Proxy state. |
| int | [bt\_mesh\_priv\_gatt\_proxy\_set](#ga346244dcc70afe3a85e85c28c56b4f49) (enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) priv\_gatt\_proxy) |
|  | Enable or disable the Private GATT Proxy feature. |
| enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) | [bt\_mesh\_priv\_gatt\_proxy\_get](#ga037375c99abb492d30378deca183071d) (void) |
|  | Get the current Private GATT Proxy state. |
| int | [bt\_mesh\_friend\_set](#ga74b79bc6a15c35ef399e7d5f7c4d26e6) (enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) friendship) |
|  | Enable or disable the Friend feature. |
| enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) | [bt\_mesh\_friend\_get](#gac7b1f1208659c80956e6dab6ac0ebc47) (void) |
|  | Get the current Friend state. |

## Detailed Description

Runtime Configuration.

## Macro Definition Documentation

## [◆ ](#ga8fa3d0ac3cb9f69464c4068ca61689b9)BT\_MESH\_BEACON\_DISABLED

| #define BT\_MESH\_BEACON\_DISABLED   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga01235217559423b93d7e6cf2236278f0)BT\_MESH\_BEACON\_ENABLED

| #define BT\_MESH\_BEACON\_ENABLED   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga29fe48989e760438f2c5241110134c8c)BT\_MESH\_FRIEND\_DISABLED

| #define BT\_MESH\_FRIEND\_DISABLED   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#gaa23bba212dc1b322651723ca20f497a3)BT\_MESH\_FRIEND\_ENABLED

| #define BT\_MESH\_FRIEND\_ENABLED   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga35f85e6a9c085cdad4f70b8e60d0b027)BT\_MESH\_FRIEND\_NOT\_SUPPORTED

| #define BT\_MESH\_FRIEND\_NOT\_SUPPORTED   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga3fe3e68efd25a3a03a041b978435fd7b)BT\_MESH\_GATT\_PROXY\_DISABLED

| #define BT\_MESH\_GATT\_PROXY\_DISABLED   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga77f4438624aae49ea2bb66437c9623f7)BT\_MESH\_GATT\_PROXY\_ENABLED

| #define BT\_MESH\_GATT\_PROXY\_ENABLED   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#gaecec3747198a29dd10185e3755e660f8)BT\_MESH\_GATT\_PROXY\_NOT\_SUPPORTED

| #define BT\_MESH\_GATT\_PROXY\_NOT\_SUPPORTED   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga5b3af48dfe15948654b7791d7a684ba8)BT\_MESH\_KR\_NORMAL

| #define BT\_MESH\_KR\_NORMAL   0x00 |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga139d621ce45ea87b4d8a15fc2b29dbe3)BT\_MESH\_KR\_PHASE\_1

| #define BT\_MESH\_KR\_PHASE\_1   0x01 |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#gaff6e8f59719f341ab681268e421b1612)BT\_MESH\_KR\_PHASE\_2

| #define BT\_MESH\_KR\_PHASE\_2   0x02 |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#gab0e65cdc2b152d3b84615223fdaebb2e)BT\_MESH\_KR\_PHASE\_3

| #define BT\_MESH\_KR\_PHASE\_3   0x03 |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga7ffe6722b12a8663518b4e17349e4da5)BT\_MESH\_NODE\_IDENTITY\_NOT\_SUPPORTED

| #define BT\_MESH\_NODE\_IDENTITY\_NOT\_SUPPORTED   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga86e88acc6fdcc26a9cea4415daad016c)BT\_MESH\_NODE\_IDENTITY\_RUNNING

| #define BT\_MESH\_NODE\_IDENTITY\_RUNNING   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga9a83214cdbd34ac1d4bc644136523bd9)BT\_MESH\_NODE\_IDENTITY\_STOPPED

| #define BT\_MESH\_NODE\_IDENTITY\_STOPPED   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga2645fd9e2aed6de7806e7ac5afd1af10)BT\_MESH\_PRIV\_BEACON\_DISABLED

| #define BT\_MESH\_PRIV\_BEACON\_DISABLED   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga1f72ffadff83f30943df88cd1ddcbee8)BT\_MESH\_PRIV\_BEACON\_ENABLED

| #define BT\_MESH\_PRIV\_BEACON\_ENABLED   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga475302ad8ba5589c7ea95da36f18948e)BT\_MESH\_PRIV\_GATT\_PROXY\_DISABLED

| #define BT\_MESH\_PRIV\_GATT\_PROXY\_DISABLED   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#gac73cdadfd9c9417a051739bce59960a7)BT\_MESH\_PRIV\_GATT\_PROXY\_ENABLED

| #define BT\_MESH\_PRIV\_GATT\_PROXY\_ENABLED   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#ga66b4ed203ecbc9a70620b5adff04110f)BT\_MESH\_PRIV\_GATT\_PROXY\_NOT\_SUPPORTED

| #define BT\_MESH\_PRIV\_GATT\_PROXY\_NOT\_SUPPORTED   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#gaafd10319da7d2f938207b8fd6de02dbc)BT\_MESH\_RELAY\_DISABLED

| #define BT\_MESH\_RELAY\_DISABLED   [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#gae5d235a7c182a8add961d7ce344f87aa)BT\_MESH\_RELAY\_ENABLED

| #define BT\_MESH\_RELAY\_ENABLED   [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## [◆ ](#gabbbbddd31c2a92256fe2f7a7520e76f7)BT\_MESH\_RELAY\_NOT\_SUPPORTED

| #define BT\_MESH\_RELAY\_NOT\_SUPPORTED   [BT\_MESH\_FEATURE\_NOT\_SUPPORTED](#gga0a3557a71597885a31cf209c6b83cedba1e42ee4fce611297ef133bd8260ecdd0) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga0a3557a71597885a31cf209c6b83cedb)bt\_mesh\_feat\_state

| enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) |
| --- |

`#include <[cfg.h](cfg_8h.md)>`

Bluetooth Mesh feature states.

| Enumerator | |
| --- | --- |
| BT\_MESH\_FEATURE\_DISABLED | Feature is supported, but disabled. |
| BT\_MESH\_FEATURE\_ENABLED | Feature is supported and enabled. |
| BT\_MESH\_FEATURE\_NOT\_SUPPORTED | Feature is not supported, and cannot be enabled. |

## Function Documentation

## [◆ ](#ga479c14f6b0d4a08ddf5b160fa9267844)bt\_mesh\_beacon\_enabled()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_beacon\_enabled | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Get the current Secure Network Beacon state.

Returns
:   Whether the Secure Network Beacon feature is enabled.

## [◆ ](#ga15de1cdc964628b6f001ef893021ce6e)bt\_mesh\_beacon\_set()

| void bt\_mesh\_beacon\_set | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *beacon* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Enable or disable sending of the Secure Network Beacon.

Parameters
:   | beacon | New Secure Network Beacon state. |
    | --- | --- |

## [◆ ](#gaa97f63f5b3167c672fa1a0d8c8fe9ab7)bt\_mesh\_default\_ttl\_get()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_default\_ttl\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Get the current default TTL value.

Returns
:   The current default TTL value.

## [◆ ](#gaafea57625c9fdba535431cc92dadd162)bt\_mesh\_default\_ttl\_set()

| int bt\_mesh\_default\_ttl\_set | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *default\_ttl* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Set the default TTL value.

The default TTL value is used when no explicit TTL value is set. Models will use the default TTL value when [bt\_mesh\_msg\_ctx::send\_ttl](structbt__mesh__msg__ctx.md#a43b0ebfdc3c8018a02886d93dfe2f21b "bt_mesh_msg_ctx::send_ttl") is [BT\_MESH\_TTL\_DEFAULT](group__bt__mesh__access.md#ga16516272b42420263b1c47c3ea16c0c8 "BT_MESH_TTL_DEFAULT").

Parameters
:   | default\_ttl | The new default TTL value. Valid values are 0x00 and 0x02 to [BT\_MESH\_TTL\_MAX](group__bt__mesh__access.md#ga071e85e929589d31bf876e2e09cf2f19 "BT_MESH_TTL_MAX"). |
    | --- | --- |

Return values
:   | 0 | Successfully set the default TTL value. |
    | --- | --- |
    | -EINVAL | Invalid TTL value. |

## [◆ ](#gac7b1f1208659c80956e6dab6ac0ebc47)bt\_mesh\_friend\_get()

| enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) bt\_mesh\_friend\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Get the current Friend state.

Returns
:   The Friend feature state.

## [◆ ](#ga74b79bc6a15c35ef399e7d5f7c4d26e6)bt\_mesh\_friend\_set()

| int bt\_mesh\_friend\_set | ( | enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) | *friendship* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Enable or disable the Friend feature.

Any active friendships will be terminated immediately if the Friend feature is disabled.

Support for the Friend feature must be enabled through the `CONFIG_BT_MESH_FRIEND` configuration option.

Parameters
:   | friendship | New Friend feature state. Must be one of [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) and [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729). |
    | --- | --- |

Return values
:   | 0 | Successfully changed the Friend feature state. |
    | --- | --- |
    | -ENOTSUP | The Friend feature is not supported. |
    | -EINVAL | Invalid parameter. |
    | -EALREADY | Already in the given state. |

## [◆ ](#ga8457f222211bc812106b2dccc87b1abe)bt\_mesh\_gatt\_proxy\_get()

| enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) bt\_mesh\_gatt\_proxy\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Get the current GATT Proxy state.

Returns
:   The GATT Proxy feature state.

## [◆ ](#gaac543b57580f9ac8dff36c0ce1196144)bt\_mesh\_gatt\_proxy\_set()

| int bt\_mesh\_gatt\_proxy\_set | ( | enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) | *gatt\_proxy* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Enable or disable the GATT Proxy feature.

Support for the GATT Proxy feature must be enabled through the `CONFIG_BT_MESH_GATT_PROXY` configuration option.

Note
:   The GATT Proxy feature only controls a Proxy node's ability to relay messages to the mesh network. A node that supports GATT Proxy will still advertise Connectable Proxy beacons, even if the feature is disabled. The Proxy feature can only be fully disabled through compile time configuration.

Parameters
:   | gatt\_proxy | New GATT Proxy state. Must be one of [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) and [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729). |
    | --- | --- |

Return values
:   | 0 | Successfully changed the GATT Proxy feature state. |
    | --- | --- |
    | -ENOTSUP | The GATT Proxy feature is not supported. |
    | -EINVAL | Invalid parameter. |
    | -EALREADY | Already in the given state. |

## [◆ ](#ga08b336fa1a4a721ac9b10fbb75e4af6b)bt\_mesh\_net\_transmit\_get()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_net\_transmit\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Get the current Network Transmit parameters.

The [BT\_MESH\_TRANSMIT\_COUNT](group__bt__mesh__access.md#ga62fda0d731241efbaa4827e4eb9d1795 "BT_MESH_TRANSMIT_COUNT") and [BT\_MESH\_TRANSMIT\_INT](group__bt__mesh__access.md#ga2aa21171c5677d23ad0c472291639417 "BT_MESH_TRANSMIT_INT") macros can be used to decode the Network Transmit parameters.

Returns
:   The current Network Transmit parameters.

## [◆ ](#gaa652e4f1460f62252065ac21854ab3f6)bt\_mesh\_net\_transmit\_set()

| void bt\_mesh\_net\_transmit\_set | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *xmit* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Set the Network Transmit parameters.

The Network Transmit parameters determine the parameters local messages are transmitted with.

See also
:   [BT\_MESH\_TRANSMIT](group__bt__mesh__access.md#gaff82bf652232fbce71c31f38a10577a9 "Encode transmission count & interval steps.")

Parameters
:   | xmit | New Network Transmit parameters. Use [BT\_MESH\_TRANSMIT](group__bt__mesh__access.md#gaff82bf652232fbce71c31f38a10577a9 "BT_MESH_TRANSMIT") for encoding. |
    | --- | --- |

## [◆ ](#ga256d00139ca40eb99303fef766a3add7)bt\_mesh\_od\_priv\_proxy\_get()

| int bt\_mesh\_od\_priv\_proxy\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Get the current Mesh On-Demand Private Proxy state.

Return values
:   | 0 | or positive value represents On-Demand Private Proxy feature state |
    | --- | --- |
    | -ENOTSUP | The On-Demand Private Proxy feature is not supported. |

## [◆ ](#ga26023b727e1b180263b22d0ade145f81)bt\_mesh\_od\_priv\_proxy\_set()

| int bt\_mesh\_od\_priv\_proxy\_set | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *on\_demand\_proxy* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Set state of Mesh On-Demand Private Proxy.

Support for the On-Demand Private Proxy state must be enabled with `BT_MESH_OD_PRIV_PROXY_SRV`.

Parameters
:   | on\_demand\_proxy | New Mesh On-Demand Private Proxy state. Value of 0x00 means that advertising with Private Network Identity cannot be enabled on demand. Values in range 0x01 - 0xFF set interval of this advertising after valid Solicitation PDU is received or client disconnects. |
    | --- | --- |

Return values
:   | 0 | Successfully changed the Mesh On-Demand Private Proxy feature state. |
    | --- | --- |
    | -ENOTSUP | The On-Demand Private Proxy feature is not supported. |
    | -EINVAL | Invalid parameter. |
    | -EALREADY | Already in the given state. |

## [◆ ](#ga2c8dc9ee5c3862790efd2a74a1ef6873)bt\_mesh\_priv\_beacon\_get()

| enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) bt\_mesh\_priv\_beacon\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Get the current Mesh Private beacon state.

Returns
:   The Mesh Private beacon feature state.

## [◆ ](#ga1afc5ec210bbc6090ada922ddf75e284)bt\_mesh\_priv\_beacon\_set()

| int bt\_mesh\_priv\_beacon\_set | ( | enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) | *priv\_beacon* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Enable or disable sending of the Mesh Private beacon.

Support for the Private beacon state must be enabled with `CONFIG_BT_MESH_PRIV_BEACONS`.

Parameters
:   | priv\_beacon | New Mesh Private beacon state. Must be one of [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) and [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729). |
    | --- | --- |

Return values
:   | 0 | Successfully changed the Mesh Private beacon feature state. |
    | --- | --- |
    | -ENOTSUP | The Mesh Private beacon feature is not supported. |
    | -EINVAL | Invalid parameter. |
    | -EALREADY | Already in the given state. |

## [◆ ](#gafe3d54c1546b03cebbecaf762ae87781)bt\_mesh\_priv\_beacon\_update\_interval\_get()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_priv\_beacon\_update\_interval\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Get the current Mesh Private beacon update interval.

The Mesh Private beacon's randomization value is updated regularly to maintain the node's privacy. The update interval controls how often the beacon is updated, in 10 second increments.

Returns
:   The Private beacon update interval in 10 second steps, or 0 if the beacon is updated every time it's transmitted.

## [◆ ](#ga01abb07d27edef40ffff4da968065c1d)bt\_mesh\_priv\_beacon\_update\_interval\_set()

| void bt\_mesh\_priv\_beacon\_update\_interval\_set | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *interval* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Set the current Mesh Private beacon update interval.

The Mesh Private beacon's randomization value is updated regularly to maintain the node's privacy. The update interval controls how often the beacon is updated, in 10 second increments.

Parameters
:   | interval | Private beacon update interval in 10 second steps, or 0 to update on every beacon transmission. |
    | --- | --- |

## [◆ ](#ga037375c99abb492d30378deca183071d)bt\_mesh\_priv\_gatt\_proxy\_get()

| enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) bt\_mesh\_priv\_gatt\_proxy\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Get the current Private GATT Proxy state.

Returns
:   The Private GATT Proxy feature state.

## [◆ ](#ga346244dcc70afe3a85e85c28c56b4f49)bt\_mesh\_priv\_gatt\_proxy\_set()

| int bt\_mesh\_priv\_gatt\_proxy\_set | ( | enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) | *priv\_gatt\_proxy* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Enable or disable the Private GATT Proxy feature.

Support for the Private GATT Proxy feature must be enabled through the `CONFIG_BT_MESH_PRIV_BEACONS` and `CONFIG_BT_MESH_GATT_PROXY` configuration options.

Parameters
:   | priv\_gatt\_proxy | New Private GATT Proxy state. Must be one of [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) and [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729). |
    | --- | --- |

Return values
:   | 0 | Successfully changed the Private GATT Proxy feature state. |
    | --- | --- |
    | -ENOTSUP | The Private GATT Proxy feature is not supported. |
    | -EINVAL | Invalid parameter. |
    | -EALREADY | Already in the given state. |

## [◆ ](#gadb41d2f78a490aa81b5640bb7ff5a5ce)bt\_mesh\_relay\_get()

| enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) bt\_mesh\_relay\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Get the current Relay feature state.

Returns
:   The Relay feature state.

## [◆ ](#gaf9abf4bcba55d273a7e6e8ee42c521a9)bt\_mesh\_relay\_retransmit\_get()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_relay\_retransmit\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Get the current Relay Retransmit parameters.

The [BT\_MESH\_TRANSMIT\_COUNT](group__bt__mesh__access.md#ga62fda0d731241efbaa4827e4eb9d1795 "BT_MESH_TRANSMIT_COUNT") and [BT\_MESH\_TRANSMIT\_INT](group__bt__mesh__access.md#ga2aa21171c5677d23ad0c472291639417 "BT_MESH_TRANSMIT_INT") macros can be used to decode the Relay Retransmit parameters.

Returns
:   The current Relay Retransmit parameters, or 0 if relay is not supported.

## [◆ ](#gad8d6773753b80540b2aaa982c1ec8c03)bt\_mesh\_relay\_set()

| int bt\_mesh\_relay\_set | ( | enum [bt\_mesh\_feat\_state](#ga0a3557a71597885a31cf209c6b83cedb) | *relay*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *xmit* ) |

`#include <[cfg.h](cfg_8h.md)>`

Configure the Relay feature.

Enable or disable the Relay feature, and configure the parameters to transmit relayed messages with.

Support for the Relay feature must be enabled through the `CONFIG_BT_MESH_RELAY` configuration option.

See also
:   [BT\_MESH\_TRANSMIT](group__bt__mesh__access.md#gaff82bf652232fbce71c31f38a10577a9 "Encode transmission count & interval steps.")

Parameters
:   | relay | New Relay feature state. Must be one of [BT\_MESH\_FEATURE\_ENABLED](#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275) and [BT\_MESH\_FEATURE\_DISABLED](#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729). |
    | --- | --- |
    | xmit | New Relay retransmit parameters. Use [BT\_MESH\_TRANSMIT](group__bt__mesh__access.md#gaff82bf652232fbce71c31f38a10577a9 "BT_MESH_TRANSMIT") for encoding. |

Return values
:   | 0 | Successfully changed the Relay configuration. |
    | --- | --- |
    | -ENOTSUP | The Relay feature is not supported. |
    | -EINVAL | Invalid parameter. |
    | -EALREADY | Already using the given parameters. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
