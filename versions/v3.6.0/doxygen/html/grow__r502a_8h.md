---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/grow__r502a_8h.html
original_path: doxygen/html/grow__r502a_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

grow\_r502a.h File Reference

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](grow__r502a_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [sensor\_channel\_grow\_r502a](#a8ff24814059dda20e6b36fe8cc0be30c) { [SENSOR\_CHAN\_FINGERPRINT](#a8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2) = SENSOR\_CHAN\_PRIV\_START } |
| enum | [sensor\_trigger\_type\_grow\_r502a](#a721dcba985d9010bb1f48e82b0027eb4) { [SENSOR\_TRIG\_TOUCH](#a721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4) = SENSOR\_TRIG\_PRIV\_START } |
| enum | [sensor\_attribute\_grow\_r502a](#a638da7a83d9339b17e5d9c8ce92b684b) {     [SENSOR\_ATTR\_R502A\_RECORD\_ADD](#a638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb) = SENSOR\_ATTR\_PRIV\_START , [SENSOR\_ATTR\_R502A\_RECORD\_FIND](#a638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922) , [SENSOR\_ATTR\_R502A\_RECORD\_DEL](#a638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef) , [SENSOR\_ATTR\_R502A\_RECORD\_FREE\_IDX](#a638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df) ,     [SENSOR\_ATTR\_R502A\_RECORD\_EMPTY](#a638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b)   } |

## Enumeration Type Documentation

## [◆ ](#a638da7a83d9339b17e5d9c8ce92b684b)sensor\_attribute\_grow\_r502a

| enum [sensor\_attribute\_grow\_r502a](#a638da7a83d9339b17e5d9c8ce92b684b) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_ATTR\_R502A\_RECORD\_ADD | Add values to the sensor which are having record storage facility. |
| SENSOR\_ATTR\_R502A\_RECORD\_FIND | To find requested data in record storage. |
| SENSOR\_ATTR\_R502A\_RECORD\_DEL | To delete mentioned data from record storage. |
| SENSOR\_ATTR\_R502A\_RECORD\_FREE\_IDX | To get available position to store data on record storage. |
| SENSOR\_ATTR\_R502A\_RECORD\_EMPTY | To empty the storage record. |

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

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [grow\_r502a.h](grow__r502a_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
