---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/grow__r502a_8h.html
original_path: doxygen/html/grow__r502a_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

grow\_r502a.h File Reference

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](grow__r502a_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [r502a\_sys\_param](structr502a__sys__param.md) |
| struct | [r502a\_template](structr502a__template.md) |

| Macros | |
| --- | --- |
| #define | [R502A\_BAUD\_9600](#aaab815dc7de2a1ff5596ad6fdc1e28c2)   1 |
| #define | [R502A\_BAUD\_19200](#a102611233e481e26c8cdafe97efe77b0)   2 |
| #define | [R502A\_BAUD\_38400](#aab799d94bd0dd10ea55c47cd66ba74fb)   4 |
| #define | [R502A\_BAUD\_57600](#a19ab94871e6e51660432c29130c183fb)   6 |
| #define | [R502A\_BAUD\_115200](#aa0f6b1beacb3a3e57f1bd6ab3951ba6b)   12 |

| Enumerations | |
| --- | --- |
| enum | [r502a\_led\_color\_idx](#a843fa88a16ab6b47c4e517ddbc01b4a8) { [R502A\_LED\_COLOR\_RED](#a843fa88a16ab6b47c4e517ddbc01b4a8a667a844dde544590ab7b6e3defd4016c) = 0x01 , [R502A\_LED\_COLOR\_BLUE](#a843fa88a16ab6b47c4e517ddbc01b4a8a0685eb3e0e4de6faa0577fb5f7d0f845) , [R502A\_LED\_COLOR\_PURPLE](#a843fa88a16ab6b47c4e517ddbc01b4a8ad477284ea70fb76c43a386ed3537be6c) } |
| enum | [r502a\_sec\_level](#a48154de53541aced1e78537f10f2f3d1) {     [R502A\_SEC\_LEVEL\_1](#a48154de53541aced1e78537f10f2f3d1a2220c963d396a7d6604ff0b47e3b6db7) = 1 , [R502A\_SEC\_LEVEL\_2](#a48154de53541aced1e78537f10f2f3d1a9fbe3bed318932b9fab282aee7e823ef) , [R502A\_SEC\_LEVEL\_3](#a48154de53541aced1e78537f10f2f3d1adb0e8b2e0242be58c32cf1fb8c3c00fa) , [R502A\_SEC\_LEVEL\_4](#a48154de53541aced1e78537f10f2f3d1a1e579d5283fb984a555f918828b3e1e9) ,     [R502A\_SEC\_LEVEL\_5](#a48154de53541aced1e78537f10f2f3d1abcb8f9a6447757b0fcb8ef4f63979dc1)   } |
| enum | [r502a\_data\_len](#a3298eb4d591ba56131bae8137888dcd8) { [R502A\_PKG\_LEN\_32](#a3298eb4d591ba56131bae8137888dcd8a6be1d185636994b69006b14188d003cf) , [R502A\_PKG\_LEN\_64](#a3298eb4d591ba56131bae8137888dcd8a61ab7cac6d6613f3465157f1ee09b2ee) , [R502A\_PKG\_LEN\_128](#a3298eb4d591ba56131bae8137888dcd8ad5a47c82dd3733cad5a2da69f33735fe) , [R502A\_PKG\_LEN\_256](#a3298eb4d591ba56131bae8137888dcd8a4fa6ae11c8e8f44101a729c4149a1101) } |
| enum | [r502a\_sys\_param\_set](#a16242f27a53b430ea3cf165fbc7ce70b) { [R502A\_BAUD\_RATE](#a16242f27a53b430ea3cf165fbc7ce70bacef6f845b078fffb0f5f10a93cba3721) = 4 , [R502A\_SECURITY\_LEVEL](#a16242f27a53b430ea3cf165fbc7ce70ba2795f5eb1ee8feeba7f57d0bdc4ec519) , [R502A\_DATA\_PKG\_LEN](#a16242f27a53b430ea3cf165fbc7ce70baa356f4aea69d118b8283d347b816bca1) } |
| enum | [sensor\_channel\_grow\_r502a](#a8ff24814059dda20e6b36fe8cc0be30c) { [SENSOR\_CHAN\_FINGERPRINT](#a8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2) = SENSOR\_CHAN\_PRIV\_START } |
| enum | [sensor\_trigger\_type\_grow\_r502a](#a721dcba985d9010bb1f48e82b0027eb4) { [SENSOR\_TRIG\_TOUCH](#a721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4) = SENSOR\_TRIG\_PRIV\_START } |
| enum | [sensor\_attribute\_grow\_r502a](#a638da7a83d9339b17e5d9c8ce92b684b) {     [SENSOR\_ATTR\_R502A\_CAPTURE](#a638da7a83d9339b17e5d9c8ce92b684baa499ad10253a3f3e1ad571c3a149dadd) = SENSOR\_ATTR\_PRIV\_START , [SENSOR\_ATTR\_R502A\_TEMPLATE\_CREATE](#a638da7a83d9339b17e5d9c8ce92b684ba773495d23834e9fd2eb9ee02909be965) , [SENSOR\_ATTR\_R502A\_RECORD\_ADD](#a638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb) , [SENSOR\_ATTR\_R502A\_RECORD\_FIND](#a638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922) ,     [SENSOR\_ATTR\_R502A\_RECORD\_DEL](#a638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef) , [SENSOR\_ATTR\_R502A\_RECORD\_FREE\_IDX](#a638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df) , [SENSOR\_ATTR\_R502A\_RECORD\_EMPTY](#a638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b) , [SENSOR\_ATTR\_R502A\_RECORD\_LOAD](#a638da7a83d9339b17e5d9c8ce92b684ba2edb55a7c3ece4a382d19a951f5cbe13) ,     [SENSOR\_ATTR\_R502A\_COMPARE](#a638da7a83d9339b17e5d9c8ce92b684ba7258864588bd700f50f9572d5532c689) , [SENSOR\_ATTR\_R502A\_SYS\_PARAM](#a638da7a83d9339b17e5d9c8ce92b684ba8e7d9545ee722f94e33af5335b52f3e0)   } |

| Functions | |
| --- | --- |
| int | [r502a\_read\_sys\_param](#a3dbc5cd5f5295741e99735ec0279b48d) (const struct [device](structdevice.md) \*dev, struct [r502a\_sys\_param](structr502a__sys__param.md) \*val) |
| int | [fps\_upload\_char\_buf](#ad16b787e54f20627c4bf15b1732c05ae) (const struct [device](structdevice.md) \*dev, struct [r502a\_template](structr502a__template.md) \*temp) |
| int | [fps\_download\_char\_buf](#a3b6f1ea1024c0d855a7bbf05f79c19c8) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) char\_buf\_id, const struct [r502a\_template](structr502a__template.md) \*temp) |

## Macro Definition Documentation

## [◆ ](#aa0f6b1beacb3a3e57f1bd6ab3951ba6b)R502A\_BAUD\_115200

| #define R502A\_BAUD\_115200   12 |
| --- |

## [◆ ](#a102611233e481e26c8cdafe97efe77b0)R502A\_BAUD\_19200

| #define R502A\_BAUD\_19200   2 |
| --- |

## [◆ ](#aab799d94bd0dd10ea55c47cd66ba74fb)R502A\_BAUD\_38400

| #define R502A\_BAUD\_38400   4 |
| --- |

## [◆ ](#a19ab94871e6e51660432c29130c183fb)R502A\_BAUD\_57600

| #define R502A\_BAUD\_57600   6 |
| --- |

## [◆ ](#aaab815dc7de2a1ff5596ad6fdc1e28c2)R502A\_BAUD\_9600

| #define R502A\_BAUD\_9600   1 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a3298eb4d591ba56131bae8137888dcd8)r502a\_data\_len

| enum [r502a\_data\_len](#a3298eb4d591ba56131bae8137888dcd8) |
| --- |

| Enumerator | |
| --- | --- |
| R502A\_PKG\_LEN\_32 |  |
| R502A\_PKG\_LEN\_64 |  |
| R502A\_PKG\_LEN\_128 |  |
| R502A\_PKG\_LEN\_256 |  |

## [◆ ](#a843fa88a16ab6b47c4e517ddbc01b4a8)r502a\_led\_color\_idx

| enum [r502a\_led\_color\_idx](#a843fa88a16ab6b47c4e517ddbc01b4a8) |
| --- |

| Enumerator | |
| --- | --- |
| R502A\_LED\_COLOR\_RED |  |
| R502A\_LED\_COLOR\_BLUE |  |
| R502A\_LED\_COLOR\_PURPLE |  |

## [◆ ](#a48154de53541aced1e78537f10f2f3d1)r502a\_sec\_level

| enum [r502a\_sec\_level](#a48154de53541aced1e78537f10f2f3d1) |
| --- |

| Enumerator | |
| --- | --- |
| R502A\_SEC\_LEVEL\_1 |  |
| R502A\_SEC\_LEVEL\_2 |  |
| R502A\_SEC\_LEVEL\_3 |  |
| R502A\_SEC\_LEVEL\_4 |  |
| R502A\_SEC\_LEVEL\_5 |  |

## [◆ ](#a16242f27a53b430ea3cf165fbc7ce70b)r502a\_sys\_param\_set

| enum [r502a\_sys\_param\_set](#a16242f27a53b430ea3cf165fbc7ce70b) |
| --- |

| Enumerator | |
| --- | --- |
| R502A\_BAUD\_RATE |  |
| R502A\_SECURITY\_LEVEL |  |
| R502A\_DATA\_PKG\_LEN |  |

## [◆ ](#a638da7a83d9339b17e5d9c8ce92b684b)sensor\_attribute\_grow\_r502a

| enum [sensor\_attribute\_grow\_r502a](#a638da7a83d9339b17e5d9c8ce92b684b) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_ATTR\_R502A\_CAPTURE | To capture finger and store as feature file in RAM buffers char\_buf\_1 and char\_buf\_2. |
| SENSOR\_ATTR\_R502A\_TEMPLATE\_CREATE | create template from feature files at RAM buffers char\_buf\_1 & char\_buf\_2 and store a template data back in both RAM buffers char\_buf\_1 and char\_buf\_2. |
| SENSOR\_ATTR\_R502A\_RECORD\_ADD | Add template to the sensor record storage.  Parameters  | val->val1 | record index for template to be stored in the sensor device's flash library. | | --- | --- | |
| SENSOR\_ATTR\_R502A\_RECORD\_FIND | To find requested data in record storage.  Returns  val->val1 matched record index. val->val2 matching score. |
| SENSOR\_ATTR\_R502A\_RECORD\_DEL | To delete mentioned data from record storage.  Parameters  | val->val1 | record start index to be deleted. | | --- | --- | | val->val2 | number of records to be deleted. | |
| SENSOR\_ATTR\_R502A\_RECORD\_FREE\_IDX | To get available position to store data on record storage. |
| SENSOR\_ATTR\_R502A\_RECORD\_EMPTY | To empty the storage record. |
| SENSOR\_ATTR\_R502A\_RECORD\_LOAD | To load template from storage to RAM buffer of sensor.  Parameters  | val->val1 | record start index to be loaded in device internal RAM buffer. | | --- | --- | |
| SENSOR\_ATTR\_R502A\_COMPARE | To template data stored in sensor's RAM buffer.  Returns  val->val1 match result. [R502A\_FINGER\_MATCH\_FOUND or R502A\_FINGER\_MATCH\_NOT\_FOUND] val->val2 matching score. |
| SENSOR\_ATTR\_R502A\_SYS\_PARAM | To read and write device's system parameters.  sensor\_attr\_set  Parameters  | val->val1 | parameter number from enum [r502a\_sys\_param\_set](#a16242f27a53b430ea3cf165fbc7ce70b). | | --- | --- | | val->val2 | content to be written for the respective parameter. sensor\_attr\_get |  Returns  val->ex.data buffer holds the system parameter values. |

## [◆ ](#a8ff24814059dda20e6b36fe8cc0be30c)sensor\_channel\_grow\_r502a

| enum [sensor\_channel\_grow\_r502a](#a8ff24814059dda20e6b36fe8cc0be30c) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_CHAN\_FINGERPRINT | Fingerprint template count, ID number for enrolling and searching. |

## [◆ ](#a721dcba985d9010bb1f48e82b0027eb4)sensor\_trigger\_type\_grow\_r502a

| enum [sensor\_trigger\_type\_grow\_r502a](#a721dcba985d9010bb1f48e82b0027eb4) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_TRIG\_TOUCH | Trigger fires when a touch is detected. |

## Function Documentation

## [◆ ](#a3b6f1ea1024c0d855a7bbf05f79c19c8)fps\_download\_char\_buf()

| int fps\_download\_char\_buf | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *char\_buf\_id*, |
|  |  | const struct [r502a\_template](structr502a__template.md) \* | *temp* ) |

## [◆ ](#ad16b787e54f20627c4bf15b1732c05ae)fps\_upload\_char\_buf()

| int fps\_upload\_char\_buf | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [r502a\_template](structr502a__template.md) \* | *temp* ) |

## [◆ ](#a3dbc5cd5f5295741e99735ec0279b48d)r502a\_read\_sys\_param()

| int r502a\_read\_sys\_param | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [r502a\_sys\_param](structr502a__sys__param.md) \* | *val* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [grow\_r502a.h](grow__r502a_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
