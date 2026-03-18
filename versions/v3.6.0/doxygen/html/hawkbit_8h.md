---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hawkbit_8h.html
original_path: doxygen/html/hawkbit_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hawkbit.h File Reference

[Go to the source code of this file.](hawkbit_8h_source.md)

| Macros | |
| --- | --- |
| #define | [HAWKBIT\_JSON\_URL](group__hawkbit.md#gae2550864ddf596fe544052af73dc1dba)   "/default/controller/v1" |

| Enumerations | |
| --- | --- |
| enum | [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) {     [HAWKBIT\_NETWORKING\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba5a36eadcadc43c1fd0936a8546fb15e8) , [HAWKBIT\_UNCONFIRMED\_IMAGE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bad4b0587da0bdfd829d0d08ed2407357d) , [HAWKBIT\_PERMISSION\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba1d79e6fe8487cc4dc36c6c91bcabd124) , [HAWKBIT\_METADATA\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba2b7d188d8c28a3373d9b8a7f831b1e3a) ,     [HAWKBIT\_DOWNLOAD\_ERROR](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220baf1a448b0addfc769515c725ce5b1bab9) , [HAWKBIT\_OK](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba6af6cd1b834d74a5298f4b3626b48ad3) , [HAWKBIT\_UPDATE\_INSTALLED](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9f5a200928474863a88d170c11594048) , [HAWKBIT\_NO\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220bac73c46deb3e54dba690f814a2fb9db71) ,     [HAWKBIT\_CANCEL\_UPDATE](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba9d677899d5ff00957dfeab70f484863f) , [HAWKBIT\_PROBE\_IN\_PROGRESS](group__hawkbit.md#gga96c59c754178451d8dbd08b32813220ba28ccbb4060d41592884829cf205414f6)   } |
|  | Response message from hawkBit. [More...](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) |

| Functions | |
| --- | --- |
| int | [hawkbit\_init](group__hawkbit.md#ga0ef6151f205088405de242e012984ca6) (void) |
|  | Init the flash partition. |
| void | [hawkbit\_autohandler](group__hawkbit.md#gac077f546d8947d6b55dcb9276ce98283) (void) |
|  | Runs hawkBit probe and hawkBit update automatically. |
| enum [hawkbit\_response](group__hawkbit.md#ga96c59c754178451d8dbd08b32813220b) | [hawkbit\_probe](group__hawkbit.md#ga525173f0c3d0ca4e26124a34d098d0b9) (void) |
|  | The hawkBit probe verify if there is some update to be performed. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [hawkbit.h](hawkbit_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
