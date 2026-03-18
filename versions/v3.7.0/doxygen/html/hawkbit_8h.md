---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/hawkbit_8h.html
original_path: doxygen/html/hawkbit_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hawkbit.h File Reference

`#include <[zephyr/net/tls_credentials.h](tls__credentials_8h_source.md)>`

[Go to the source code of this file.](hawkbit_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) |
|  | hawkBit configuration structure. [More...](structhawkbit__runtime__config.md#details) |

| Macros | |
| --- | --- |
| #define | [HAWKBIT\_JSON\_URL](group__hawkbit.md#gae2550864ddf596fe544052af73dc1dba)   "/default/controller/v1" |

| Typedefs | |
| --- | --- |
| typedef int(\* | [hawkbit\_config\_device\_data\_cb\_handler\_t](group__hawkbit.md#ga2774769ec44f2793895b5d783b4dceda)) (const char \*device\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size) |
|  | Callback to provide the custom data to the hawkBit server. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [hawkbit\_get\_device\_identity\_cb\_handler\_t](group__hawkbit.md#ga154220c632a7594c0630cdcd79385055)) (char \*id, int id\_max\_len) |
|  | Callback to get the device identity. |

| Enumerations | |
| --- | --- |
| enum | [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) {     [HAWKBIT\_NETWORKING\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8) , [HAWKBIT\_UNCONFIRMED\_IMAGE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d) , [HAWKBIT\_PERMISSION\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124) , [HAWKBIT\_METADATA\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a) ,     [HAWKBIT\_DOWNLOAD\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9) , [HAWKBIT\_OK](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba6af6cd1b834d74a5298f4b3626b48ad3) , [HAWKBIT\_UPDATE\_INSTALLED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048) , [HAWKBIT\_NO\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71) ,     [HAWKBIT\_CANCEL\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9d677899d5ff00957dfeab70f484863f) , [HAWKBIT\_NOT\_INITIALIZED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac4ba42120229e92b52c82d4a4d4cd708) , [HAWKBIT\_PROBE\_IN\_PROGRESS](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6)   } |
|  | Response message from hawkBit. [More...](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) |

| Functions | |
| --- | --- |
| int | [hawkbit\_set\_custom\_data\_cb](group__hawkbit.md#gad8e83255a969eb61244b1edfd0b95e5d) ([hawkbit\_config\_device\_data\_cb\_handler\_t](group__hawkbit.md#ga2774769ec44f2793895b5d783b4dceda) cb) |
|  | Set the custom data callback. |
| int | [hawkbit\_init](group__hawkbit.md#ga0ef6151f205088405de242e012984ca6) (void) |
|  | Init the flash partition. |
| void | [hawkbit\_autohandler](group__hawkbit.md#gac077f546d8947d6b55dcb9276ce98283) (void) |
|  | Runs hawkBit probe and hawkBit update automatically. |
| enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) | [hawkbit\_probe](group__hawkbit.md#ga525173f0c3d0ca4e26124a34d098d0b9) (void) |
|  | The hawkBit probe verify if there is some update to be performed. |
| void | [hawkbit\_reboot](group__hawkbit.md#ga03631b12a4107d660bac14bfd33bfebd) (void) |
|  | Request system to reboot. |
| int | [hawkbit\_set\_device\_identity\_cb](group__hawkbit.md#ga4ce085b8f2bb46af2c2e9f3f2879d633) ([hawkbit\_get\_device\_identity\_cb\_handler\_t](group__hawkbit.md#ga154220c632a7594c0630cdcd79385055) cb) |
|  | Set the device identity callback. |
| int | [hawkbit\_set\_config](group__hawkbit.md#ga5e6a1e2e49b75a44a9f13f059ed7d3f6) (struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) \*config) |
|  | Set the hawkBit server configuration settings. |
| struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) | [hawkbit\_get\_config](group__hawkbit.md#gaae46014585251b53afe726d42475d739) (void) |
|  | Get the hawkBit server configuration settings. |
| static int | [hawkbit\_set\_server\_addr](group__hawkbit.md#gaa49efdafe94e1d36a537aff962df41d5) (char \*addr\_str) |
|  | Set the hawkBit server address. |
| static int | [hawkbit\_set\_server\_port](group__hawkbit.md#ga78ef6a168132940040ad04498f0b462d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) port) |
|  | Set the hawkBit server port. |
| static int | [hawkbit\_set\_ddi\_security\_token](group__hawkbit.md#gaa2799669246cc817bb8e294a8fbfb3d2) (char \*token) |
|  | Set the hawkBit security token. |
| static int | [hawkbit\_set\_tls\_tag](group__hawkbit.md#ga5c73e9ba4dd9788e22fdb11f1f2b81ee) ([sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) tag) |
|  | Set the hawkBit TLS tag. |
| static char \* | [hawkbit\_get\_server\_addr](group__hawkbit.md#gacbbaed38e2ace7d8dcc78e40b286b5e9) (void) |
|  | Get the hawkBit server address. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [hawkbit\_get\_server\_port](group__hawkbit.md#ga3674fc406aa20fe4770ff0c729817b7c) (void) |
|  | Get the hawkBit server port. |
| static char \* | [hawkbit\_get\_ddi\_security\_token](group__hawkbit.md#gadc4aea2dac4915a434a10e6e055f54f7) (void) |
|  | Get the hawkBit security token. |
| static [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) | [hawkbit\_get\_tls\_tag](group__hawkbit.md#ga694e5f4fbcae451eb90a019f6d1f3b81) (void) |
|  | Get the hawkBit TLS tag. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [hawkbit\_get\_action\_id](group__hawkbit.md#ga0ca5f633e902137ecda068ab312d52db) (void) |
|  | Get the hawkBit action id. |
| int | [hawkbit\_reset\_action\_id](group__hawkbit.md#ga26f0066c87c57b500170ac377b560bb4) (void) |
|  | Resets the hawkBit action id, that is saved in settings. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [hawkbit.h](hawkbit_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
