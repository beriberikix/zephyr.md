---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/osdp_8h.html
original_path: doxygen/html/osdp_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp.h File Reference

Open Supervised Device Protocol (OSDP) public API header file.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](osdp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [osdp\_cmd\_output](structosdp__cmd__output.md) |
|  | Command sent from CP to Control digital output of PD. [More...](structosdp__cmd__output.md#details) |
| struct | [osdp\_cmd\_led\_params](structosdp__cmd__led__params.md) |
|  | LED params sub-structure. [More...](structosdp__cmd__led__params.md#details) |
| struct | [osdp\_cmd\_led](structosdp__cmd__led.md) |
|  | Sent from CP to PD to control the behaviour of it's on-board LEDs. [More...](structosdp__cmd__led.md#details) |
| struct | [osdp\_cmd\_buzzer](structosdp__cmd__buzzer.md) |
|  | Sent from CP to control the behaviour of a buzzer in the PD. [More...](structosdp__cmd__buzzer.md#details) |
| struct | [osdp\_cmd\_text](structosdp__cmd__text.md) |
|  | Command to manipulate any display units that the PD supports. [More...](structosdp__cmd__text.md#details) |
| struct | [osdp\_cmd\_comset](structosdp__cmd__comset.md) |
|  | Sent in response to a COMSET command. [More...](structosdp__cmd__comset.md#details) |
| struct | [osdp\_cmd\_keyset](structosdp__cmd__keyset.md) |
|  | This command transfers an encryption key from the CP to a PD. [More...](structosdp__cmd__keyset.md#details) |
| struct | [osdp\_cmd](structosdp__cmd.md) |
|  | OSDP Command Structure. [More...](structosdp__cmd.md#details) |
| struct | [osdp\_event\_cardread](structosdp__event__cardread.md) |
|  | OSDP event cardread. [More...](structosdp__event__cardread.md#details) |
| struct | [osdp\_event\_keypress](structosdp__event__keypress.md) |
|  | OSDP Event Keypad. [More...](structosdp__event__keypress.md#details) |
| struct | [osdp\_event](structosdp__event.md) |
|  | OSDP Event structure. [More...](structosdp__event.md#details) |

| Macros | |
| --- | --- |
| #define | [OSDP\_CMD\_TEXT\_MAX\_LEN](#acfd9e52e3ca23e6ef3d1cb55a0fa5714)   32 |
|  | Max length of text for text command. |
| #define | [OSDP\_CMD\_KEYSET\_KEY\_MAX\_LEN](#a04a0aa00cbe34e1723be1a4763f63e94)   32 |
|  | Max length of key data for keyset command. |
| #define | [OSDP\_EVENT\_MAX\_DATALEN](#af531800483155468768b89d20c3377d6)   64 |
|  | Max length of event data. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [pd\_command\_callback\_t](#a6a71149ab51996f345c20ad34d725803)) (void \*arg, struct [osdp\_cmd](structosdp__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Callback for PD command notifications. |
| typedef int(\* | [cp\_event\_callback\_t](#aa02ec1fa8d7da5d694d5c2ae163e03cd)) (void \*arg, int pd, struct [osdp\_event](structosdp__event.md) \*ev) |
|  | Callback for CP event notifications. |

| Enumerations | |
| --- | --- |
| enum | [osdp\_led\_color\_e](#a97ee0d8eb19e4e37ac89b2b6d338b84e) {     [OSDP\_LED\_COLOR\_NONE](#a97ee0d8eb19e4e37ac89b2b6d338b84ea72a45fa8f0b48a165c5507e456b4b1e7) , [OSDP\_LED\_COLOR\_RED](#a97ee0d8eb19e4e37ac89b2b6d338b84ea6832c2b25f228213022d0dbb5f5e1584) , [OSDP\_LED\_COLOR\_GREEN](#a97ee0d8eb19e4e37ac89b2b6d338b84eac4024077b8804580d2480708e0b14ae4) , [OSDP\_LED\_COLOR\_AMBER](#a97ee0d8eb19e4e37ac89b2b6d338b84eadd22879185802d0705d7195e1d9bd42c) ,     [OSDP\_LED\_COLOR\_BLUE](#a97ee0d8eb19e4e37ac89b2b6d338b84eadc9d0a41de52b0aa20e428e79e7c6b66) , [OSDP\_LED\_COLOR\_SENTINEL](#a97ee0d8eb19e4e37ac89b2b6d338b84ea0a80ccbb26b42ebc2cca602c7be3117a)   } |
|  | LED Colors as specified in OSDP for the on\_color/off\_color parameters. [More...](#a97ee0d8eb19e4e37ac89b2b6d338b84e) |
| enum | [osdp\_cmd\_e](#abd8555e895d9370da1400f76c931ba21) {     [OSDP\_CMD\_OUTPUT](#abd8555e895d9370da1400f76c931ba21ac59ca019a8253de6e662cd0a09adae1b) = 1 , [OSDP\_CMD\_LED](#abd8555e895d9370da1400f76c931ba21a652b1ddc2ecbf295ef20e7f896a45c42) , [OSDP\_CMD\_BUZZER](#abd8555e895d9370da1400f76c931ba21a876b0be45c76196699326ac80f05fc03) , [OSDP\_CMD\_TEXT](#abd8555e895d9370da1400f76c931ba21ae7da10f0f9c405838264d475b92b4c01) ,     [OSDP\_CMD\_KEYSET](#abd8555e895d9370da1400f76c931ba21a3abb5eec417c6889734c7f91b34b7a8f) , [OSDP\_CMD\_COMSET](#abd8555e895d9370da1400f76c931ba21a008614ac1abea52942de74ffd33ce289) , [OSDP\_CMD\_SENTINEL](#abd8555e895d9370da1400f76c931ba21a80e5942403acbd058d52dd5d58a3aeea)   } |
|  | OSDP application exposed commands. [More...](#abd8555e895d9370da1400f76c931ba21) |
| enum | [osdp\_event\_cardread\_format\_e](#a976512dfb1a4dc3ea9326d72a0abb5e7) { [OSDP\_CARD\_FMT\_RAW\_UNSPECIFIED](#a976512dfb1a4dc3ea9326d72a0abb5e7a8ae3a81c63d022a674e9282a770b8471) , [OSDP\_CARD\_FMT\_RAW\_WIEGAND](#a976512dfb1a4dc3ea9326d72a0abb5e7ab051b59f26c70ea48f7c353fae16b29e) , [OSDP\_CARD\_FMT\_ASCII](#a976512dfb1a4dc3ea9326d72a0abb5e7a5e654daacf0c0c084bac2ea4886bb059) , [OSDP\_CARD\_FMT\_SENTINEL](#a976512dfb1a4dc3ea9326d72a0abb5e7a6b7fa6ec118b9602fd68eceb6b4959d1) } |
|  | Various card formats that a PD can support. [More...](#a976512dfb1a4dc3ea9326d72a0abb5e7) |
| enum | [osdp\_event\_type](#a81548fab575d89f66b45a5d4ac85984d) { [OSDP\_EVENT\_CARDREAD](#a81548fab575d89f66b45a5d4ac85984da0e5b42ad610675190f1d32a736a51250) , [OSDP\_EVENT\_KEYPRESS](#a81548fab575d89f66b45a5d4ac85984da7c51d3f04f97758a6fb24eb4fc69a05c) , [OSDP\_EVENT\_SENTINEL](#a81548fab575d89f66b45a5d4ac85984da34bf34919ee65fe9a943856df65c5e47) } |
|  | OSDP PD Events. [More...](#a81548fab575d89f66b45a5d4ac85984d) |

| Functions | |
| --- | --- |
| Peripheral Device mode APIs | |
| Note  These are only available when  ``` CONFIG_OSDP_MODE_PD ```  is enabled. | |
| void | [osdp\_pd\_set\_command\_callback](#aa79d4fde3ae007e6c829d56daf8c3e49) ([pd\_command\_callback\_t](#a6a71149ab51996f345c20ad34d725803) cb, void \*arg) |
|  | Set callback method for PD command notification. |
| int | [osdp\_pd\_notify\_event](#ac097208c2b197ec4ebe567d59831a29f) (const struct [osdp\_event](structosdp__event.md) \*event) |
|  | API to notify PD events to CP. |
| OSDP Secure Channel APIs | |
| Note  These are only available when  ``` CONFIG_OSDP_SC_ENABLED ```  is enabled. | |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [osdp\_get\_sc\_status\_mask](#ab1335ca06ebddff18873971e4dc03c40) (void) |
|  | Get the current SC status mask. |

## Detailed Description

Open Supervised Device Protocol (OSDP) public API header file.

## Macro Definition Documentation

## [◆ ](#a04a0aa00cbe34e1723be1a4763f63e94)OSDP\_CMD\_KEYSET\_KEY\_MAX\_LEN

| #define OSDP\_CMD\_KEYSET\_KEY\_MAX\_LEN   32 |
| --- |

Max length of key data for keyset command.

## [◆ ](#acfd9e52e3ca23e6ef3d1cb55a0fa5714)OSDP\_CMD\_TEXT\_MAX\_LEN

| #define OSDP\_CMD\_TEXT\_MAX\_LEN   32 |
| --- |

Max length of text for text command.

## [◆ ](#af531800483155468768b89d20c3377d6)OSDP\_EVENT\_MAX\_DATALEN

| #define OSDP\_EVENT\_MAX\_DATALEN   64 |
| --- |

Max length of event data.

## Typedef Documentation

## [◆ ](#aa02ec1fa8d7da5d694d5c2ae163e03cd)cp\_event\_callback\_t

| typedef int(\* cp\_event\_callback\_t) (void \*arg, int pd, struct [osdp\_event](structosdp__event.md) \*ev) |
| --- |

Callback for CP event notifications.

After it has been registered with osdp\_cp\_set\_event\_callback, this method is invoked when the CP receives an event from the PD.

Parameters
:   | arg | Opaque pointer provided by the application during callback registration. |
    | --- | --- |
    | pd | the offset (0-indexed) of this PD in kconfig OSDP\_PD\_ADDRESS\_LIST |
    | ev | pointer to [osdp\_event](structosdp__event.md "OSDP Event structure.") struct (filled by libosdp). |

Return values
:   | 0 | on handling the event successfully. |
    | --- | --- |
    | -ve | on errors. |

## [◆ ](#a6a71149ab51996f345c20ad34d725803)pd\_command\_callback\_t

| typedef int(\* pd\_command\_callback\_t) (void \*arg, struct [osdp\_cmd](structosdp__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
| --- |

Callback for PD command notifications.

After it has been registered with [osdp\_pd\_set\_command\_callback](#aa79d4fde3ae007e6c829d56daf8c3e49), this method is invoked when the PD receives a command from the CP.

Parameters
:   | arg | pointer that will was passed to the arg param of [osdp\_pd\_set\_command\_callback](#aa79d4fde3ae007e6c829d56daf8c3e49). |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | pointer to the received command. |

Return values
:   | 0 | if LibOSDP must send a osdp\_ACK response |
    | --- | --- |
    | -ve | if LibOSDP must send a osdp\_NAK response |
    | +ve | and modify the passed struct [osdp\_cmd](structosdp__cmd.md "OSDP Command Structure.") \*cmd if LibOSDP must send a specific response. This is useful for sending manufacturer specific reply osdp\_MFGREP. |

## Enumeration Type Documentation

## [◆ ](#abd8555e895d9370da1400f76c931ba21)osdp\_cmd\_e

| enum [osdp\_cmd\_e](#abd8555e895d9370da1400f76c931ba21) |
| --- |

OSDP application exposed commands.

| Enumerator | |
| --- | --- |
| OSDP\_CMD\_OUTPUT | Output control command. |
| OSDP\_CMD\_LED | Reader LED control command. |
| OSDP\_CMD\_BUZZER | Reader buzzer control command. |
| OSDP\_CMD\_TEXT | Reader text output command. |
| OSDP\_CMD\_KEYSET | Encryption Key Set Command. |
| OSDP\_CMD\_COMSET | PD Communication Configuration Command. |
| OSDP\_CMD\_SENTINEL | Max command value. |

## [◆ ](#a976512dfb1a4dc3ea9326d72a0abb5e7)osdp\_event\_cardread\_format\_e

| enum [osdp\_event\_cardread\_format\_e](#a976512dfb1a4dc3ea9326d72a0abb5e7) |
| --- |

Various card formats that a PD can support.

This is sent to CP when a PD must report a card read.

| Enumerator | |
| --- | --- |
| OSDP\_CARD\_FMT\_RAW\_UNSPECIFIED | Unspecified card format. |
| OSDP\_CARD\_FMT\_RAW\_WIEGAND | Wiegand card format. |
| OSDP\_CARD\_FMT\_ASCII | ASCII card format. |
| OSDP\_CARD\_FMT\_SENTINEL | Max card format value. |

## [◆ ](#a81548fab575d89f66b45a5d4ac85984d)osdp\_event\_type

| enum [osdp\_event\_type](#a81548fab575d89f66b45a5d4ac85984d) |
| --- |

OSDP PD Events.

| Enumerator | |
| --- | --- |
| OSDP\_EVENT\_CARDREAD | Card read event. |
| OSDP\_EVENT\_KEYPRESS | Keypad press event. |
| OSDP\_EVENT\_SENTINEL | Max event value. |

## [◆ ](#a97ee0d8eb19e4e37ac89b2b6d338b84e)osdp\_led\_color\_e

| enum [osdp\_led\_color\_e](#a97ee0d8eb19e4e37ac89b2b6d338b84e) |
| --- |

LED Colors as specified in OSDP for the on\_color/off\_color parameters.

| Enumerator | |
| --- | --- |
| OSDP\_LED\_COLOR\_NONE | No color. |
| OSDP\_LED\_COLOR\_RED | Red. |
| OSDP\_LED\_COLOR\_GREEN | Green. |
| OSDP\_LED\_COLOR\_AMBER | Amber. |
| OSDP\_LED\_COLOR\_BLUE | Blue. |
| OSDP\_LED\_COLOR\_SENTINEL | Max value. |

## Function Documentation

## [◆ ](#ab1335ca06ebddff18873971e4dc03c40)osdp\_get\_sc\_status\_mask()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) osdp\_get\_sc\_status\_mask | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the current SC status mask.

Returns
:   SC status mask

## [◆ ](#ac097208c2b197ec4ebe567d59831a29f)osdp\_pd\_notify\_event()

| int osdp\_pd\_notify\_event | ( | const struct [osdp\_event](structosdp__event.md) \* | *event* | ) |  |
| --- | --- | --- | --- | --- | --- |

API to notify PD events to CP.

These events are sent to the CP as an alternate response to a POLL command.

Parameters
:   | event | pointer to event struct. Must be filled by application. |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -1 | on failure |

## [◆ ](#aa79d4fde3ae007e6c829d56daf8c3e49)osdp\_pd\_set\_command\_callback()

| void osdp\_pd\_set\_command\_callback | ( | [pd\_command\_callback\_t](#a6a71149ab51996f345c20ad34d725803) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *arg* ) |

Set callback method for PD command notification.

This callback is invoked when the PD receives a command from the CP.

Parameters
:   | cb | The callback function's pointer |
    | --- | --- |
    | arg | A pointer that will be passed as the first argument of cb |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [osdp.h](osdp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
