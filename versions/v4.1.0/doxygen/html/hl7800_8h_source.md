---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hl7800_8h_source.html
original_path: doxygen/html/hl7800_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hl7800.h

[Go to the documentation of this file.](hl7800_8h.md)

1

10

11#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MODEM\_HL7800\_H\_

12#define ZEPHYR\_INCLUDE\_DRIVERS\_MODEM\_HL7800\_H\_

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19

20#include <time.h>

21

22/\* The size includes the NUL character, the strlen doesn't \*/

[ 23](hl7800_8h.md#a2a9d979df7a39d049f341ce3706343a1)#define MDM\_HL7800\_REVISION\_MAX\_SIZE 29

[ 24](hl7800_8h.md#a506266d9f3df21657fa27c92e2a4b3a9)#define MDM\_HL7800\_REVISION\_MAX\_STRLEN (MDM\_HL7800\_REVISION\_MAX\_SIZE - 1)

25

[ 26](hl7800_8h.md#aadb01caea83021e2a32f863372e0bc40)#define MDM\_HL7800\_IMEI\_SIZE 16

[ 27](hl7800_8h.md#aec5666644e15e4bfb8970815488c273e)#define MDM\_HL7800\_IMEI\_STRLEN (MDM\_HL7800\_IMEI\_SIZE - 1)

28

[ 29](hl7800_8h.md#a633ec3cdd878098287fea81ee7b02b43)#define MDM\_HL7800\_ICCID\_MAX\_SIZE 21

[ 30](hl7800_8h.md#a32865364e6fd4641b9be897bfd6c293f)#define MDM\_HL7800\_ICCID\_MAX\_STRLEN (MDM\_HL7800\_ICCID\_MAX\_SIZE - 1)

31

[ 32](hl7800_8h.md#ae842bbecef777b83225577189205e085)#define MDM\_HL7800\_SERIAL\_NUMBER\_SIZE 15

[ 33](hl7800_8h.md#a10594faa869ccfdcd9d51309cf52d7c7)#define MDM\_HL7800\_SERIAL\_NUMBER\_STRLEN (MDM\_HL7800\_SERIAL\_NUMBER\_SIZE - 1)

34

[ 35](hl7800_8h.md#a5cc5aad6ab04405999246790dd850046)#define MDM\_HL7800\_APN\_MAX\_SIZE 64

[ 36](hl7800_8h.md#acb5d0f96845b17b84c746dcea6bd732a)#define MDM\_HL7800\_APN\_USERNAME\_MAX\_SIZE 65

[ 37](hl7800_8h.md#abc1a2d9744225bc82f3f4b14d365a0fe)#define MDM\_HL7800\_APN\_PASSWORD\_MAX\_SIZE 65

38

[ 39](hl7800_8h.md#af58865f84686e963f5c3fdff2eaea26a)#define MDM\_HL7800\_APN\_MAX\_STRLEN (MDM\_HL7800\_APN\_MAX\_SIZE - 1)

[ 40](hl7800_8h.md#a80f2f5814be64d8ad75b5ced8017ca0d)#define MDM\_HL7800\_APN\_USERNAME\_MAX\_STRLEN \

41 (MDM\_HL7800\_APN\_USERNAME\_MAX\_SIZE - 1)

[ 42](hl7800_8h.md#a2e0973dd337183b6df1209df6a70e017)#define MDM\_HL7800\_APN\_PASSWORD\_MAX\_STRLEN \

43 (MDM\_HL7800\_APN\_PASSWORD\_MAX\_SIZE - 1)

44

[ 45](hl7800_8h.md#a893cc0edcd292a5663439d20fb56a083)#define MDM\_HL7800\_APN\_CMD\_MAX\_SIZE \

46 (32 + MDM\_HL7800\_APN\_USERNAME\_MAX\_STRLEN + \

47 MDM\_HL7800\_APN\_PASSWORD\_MAX\_STRLEN)

48

[ 49](hl7800_8h.md#ab0c04e84f9d80302d1e25c3df6d4bd21)#define MDM\_HL7800\_APN\_CMD\_MAX\_STRLEN (MDM\_HL7800\_APN\_CMD\_MAX\_SIZE - 1)

50

[ 51](structmdm__hl7800__apn.md)struct [mdm\_hl7800\_apn](structmdm__hl7800__apn.md) {

[ 52](structmdm__hl7800__apn.md#a37f48ac1e950f0df59d07a6a83bb5cc9) char [value](structmdm__hl7800__apn.md#a37f48ac1e950f0df59d07a6a83bb5cc9)[[MDM\_HL7800\_APN\_MAX\_SIZE](hl7800_8h.md#a5cc5aad6ab04405999246790dd850046)];

[ 53](structmdm__hl7800__apn.md#abfe087e7989513937c43a28dd83deb21) char [username](structmdm__hl7800__apn.md#abfe087e7989513937c43a28dd83deb21)[[MDM\_HL7800\_APN\_USERNAME\_MAX\_SIZE](hl7800_8h.md#acb5d0f96845b17b84c746dcea6bd732a)];

[ 54](structmdm__hl7800__apn.md#a876db3a5fdf4ce805536d84b96213495) char [password](structmdm__hl7800__apn.md#a876db3a5fdf4ce805536d84b96213495)[[MDM\_HL7800\_APN\_PASSWORD\_MAX\_SIZE](hl7800_8h.md#abc1a2d9744225bc82f3f4b14d365a0fe)];

55};

56

[ 57](hl7800_8h.md#a8364e415a31bdce35ce76039de657b36)#define MDM\_HL7800\_LTE\_BAND\_STR\_SIZE 21

[ 58](hl7800_8h.md#a3381c94afeaabed84e2027d4b947df2d)#define MDM\_HL7800\_LTE\_BAND\_STRLEN (MDM\_HL7800\_LTE\_BAND\_STR\_SIZE - 1)

59

[ 60](hl7800_8h.md#a0384f58773f79651bbb66104c90aa050)#define MDM\_HL7800\_OPERATOR\_INDEX\_SIZE 3

[ 61](hl7800_8h.md#ab52244c336043aa7458ba26a2b6dcf5e)#define MDM\_HL7800\_OPERATOR\_INDEX\_STRLEN (MDM\_HL7800\_OPERATOR\_INDEX\_SIZE - 1)

62

[ 63](hl7800_8h.md#a523acdbfa564f3e83d93f7fbc50b8bc8)#define MDM\_HL7800\_IMSI\_MIN\_STR\_SIZE 15

[ 64](hl7800_8h.md#ac93538b6d4666aed22cef92b71e63df7)#define MDM\_HL7800\_IMSI\_MAX\_STR\_SIZE 16

[ 65](hl7800_8h.md#a645750b25f14ccfb2b6137243081a7ad)#define MDM\_HL7800\_IMSI\_MAX\_STRLEN (MDM\_HL7800\_IMSI\_MAX\_STR\_SIZE - 1)

66

[ 67](hl7800_8h.md#a1a0b40a992ae234953283d27dbeda438)#define MDM\_HL7800\_MODEM\_FUNCTIONALITY\_SIZE 2

[ 68](hl7800_8h.md#acdc8b7fa76054fa28cc1fa3ddd2543eb)#define MDM\_HL7800\_MODEM\_FUNCTIONALITY\_STRLEN \

69 (MDM\_HL7800\_MODEM\_FUNCTIONALITY\_SIZE - 1)

70

[ 71](hl7800_8h.md#af4840e7a40163477ccd00601467a8e8f)#define MDM\_HL7800\_MAX\_GPS\_STR\_SIZE 33

72

[ 73](hl7800_8h.md#a10db6322599d499eccf8116f692a42e1)#define MDM\_HL7800\_MAX\_POLTE\_USER\_ID\_SIZE 16

[ 74](hl7800_8h.md#a781329540d46b975eb8d6bf9870cf4a8)#define MDM\_HL7800\_MAX\_POLTE\_PASSWORD\_SIZE 16

[ 75](hl7800_8h.md#a060fccbbb60656b655abb3a8ad59f428)#define MDM\_HL7800\_MAX\_POLTE\_LOCATION\_STR\_SIZE 33

76

77/\* Assign the server error code (location response) to a value

78 \* that isn't used by locate response so that a single status

79 \* callback can be used.

80 \*/

[ 81](hl7800_8h.md#afbafa9aa28ebfdca72e19fca6cb944ea)#define MDM\_HL7800\_POLTE\_SERVER\_ERROR 10

82

[ 83](hl7800_8h.md#a6bc676bde1502d266c710b729b61182c)#define MDM\_HL7800\_SET\_POLTE\_USER\_AND\_PASSWORD\_FMT\_STR "AT%%POLTECMD=\"SERVERAUTH\",\"%s\",\"%s\""

84

[ 85](structmdm__hl7800__site__survey.md)struct [mdm\_hl7800\_site\_survey](structmdm__hl7800__site__survey.md) {

[ 86](structmdm__hl7800__site__survey.md#aa22e2191ac864718a097fa674dc1adc8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [earfcn](structmdm__hl7800__site__survey.md#aa22e2191ac864718a097fa674dc1adc8); /\* EUTRA Absolute Radio Frequency Channel Number \*/

[ 87](structmdm__hl7800__site__survey.md#a9e8ec0ba55bc7686e0b4b093d9057179) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cell\_id](structmdm__hl7800__site__survey.md#a9e8ec0ba55bc7686e0b4b093d9057179);

[ 88](structmdm__hl7800__site__survey.md#a725a5a647c999bbae2da828eaee481cf) int [rsrp](structmdm__hl7800__site__survey.md#a725a5a647c999bbae2da828eaee481cf);

[ 89](structmdm__hl7800__site__survey.md#a4517603844797cc6e46d96b1773c78c7) int [rsrq](structmdm__hl7800__site__survey.md#a4517603844797cc6e46d96b1773c78c7);

90};

91

[ 92](hl7800_8h.md#a2d26759e8ea3aca2e8e4a6cccac2361a)enum [mdm\_hl7800\_radio\_mode](hl7800_8h.md#a2d26759e8ea3aca2e8e4a6cccac2361a) { [MDM\_RAT\_CAT\_M1](hl7800_8h.md#a2d26759e8ea3aca2e8e4a6cccac2361aac95a4a3318b0683972336c1036f0548e) = 0, [MDM\_RAT\_CAT\_NB1](hl7800_8h.md#a2d26759e8ea3aca2e8e4a6cccac2361aa30bba3902918ea11995cd3db20319d61) };

93

[ 94](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9)enum [mdm\_hl7800\_event](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9) {

[ 95](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a7147e1d7ea1df5eb7604c3246a94ec0a) [HL7800\_EVENT\_RESERVED](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a7147e1d7ea1df5eb7604c3246a94ec0a) = 0,

[ 96](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a08a58f10e3d58022ac945b2e68d4145a) [HL7800\_EVENT\_NETWORK\_STATE\_CHANGE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a08a58f10e3d58022ac945b2e68d4145a),

[ 97](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a4cf6f0344fa2348f378756e77d5f2804) [HL7800\_EVENT\_APN\_UPDATE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a4cf6f0344fa2348f378756e77d5f2804),

[ 98](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9abb822dfaec7e96462be791857f9b3fba) [HL7800\_EVENT\_RSSI](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9abb822dfaec7e96462be791857f9b3fba),

[ 99](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9ac76f3fec60d1ffeca58405cf38bd50fe) [HL7800\_EVENT\_SINR](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9ac76f3fec60d1ffeca58405cf38bd50fe),

[ 100](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a0d25a89cd39d581c82ae73fe0a85ba21) [HL7800\_EVENT\_STARTUP\_STATE\_CHANGE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a0d25a89cd39d581c82ae73fe0a85ba21),

[ 101](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a7bd6e3e3c19ed2c5ac138c16e03b2562) [HL7800\_EVENT\_SLEEP\_STATE\_CHANGE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a7bd6e3e3c19ed2c5ac138c16e03b2562),

[ 102](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9ac22e246ac6bc5794ae0772bf3dbf5086) [HL7800\_EVENT\_RAT](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9ac22e246ac6bc5794ae0772bf3dbf5086),

[ 103](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a327cd78d882a1a36716236f2cdf28c31) [HL7800\_EVENT\_BANDS](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a327cd78d882a1a36716236f2cdf28c31),

[ 104](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9aad01f254032296551f621c888530e9d1) [HL7800\_EVENT\_ACTIVE\_BANDS](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9aad01f254032296551f621c888530e9d1),

[ 105](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9aedd9ae54dfa7a007c18e2a345d0cb0c5) [HL7800\_EVENT\_FOTA\_STATE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9aedd9ae54dfa7a007c18e2a345d0cb0c5),

[ 106](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a3848abb978d465bd0a831fc0b66a33c3) [HL7800\_EVENT\_FOTA\_COUNT](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a3848abb978d465bd0a831fc0b66a33c3),

[ 107](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a8a3b921d5bdb205f44576852467c38e2) [HL7800\_EVENT\_REVISION](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a8a3b921d5bdb205f44576852467c38e2),

[ 108](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9af3410e6ff2caa844c3b6f9963df485d1) [HL7800\_EVENT\_GPS](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9af3410e6ff2caa844c3b6f9963df485d1),

[ 109](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a0b9e7d1fcb8f043c5ac0b242e4c6c772) [HL7800\_EVENT\_GPS\_POSITION\_STATUS](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a0b9e7d1fcb8f043c5ac0b242e4c6c772),

[ 110](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9aead019c4cd55d1f54fb16ddef7f8277c) [HL7800\_EVENT\_POLTE\_REGISTRATION](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9aead019c4cd55d1f54fb16ddef7f8277c),

[ 111](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a7ee246b282ac147aafa45969060c5280) [HL7800\_EVENT\_POLTE\_LOCATE\_STATUS](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a7ee246b282ac147aafa45969060c5280),

[ 112](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a1fb1cd6b652c52ebf12e9741649f8630) [HL7800\_EVENT\_POLTE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a1fb1cd6b652c52ebf12e9741649f8630),

[ 113](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a37463d52131771a296fb141c797b3e14) [HL7800\_EVENT\_SITE\_SURVEY](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a37463d52131771a296fb141c797b3e14),

[ 114](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a9189ebbdcf3175881a0e55ac9867acbf) [HL7800\_EVENT\_STATE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a9189ebbdcf3175881a0e55ac9867acbf),

115};

116

[ 117](hl7800_8h.md#a4b00cc03cc14b3812bed4a57aeea822c)enum [mdm\_hl7800\_state](hl7800_8h.md#a4b00cc03cc14b3812bed4a57aeea822c) {

[ 118](hl7800_8h.md#a4b00cc03cc14b3812bed4a57aeea822caccfc2361ab2bea50b510c428786a9a07) [HL7800\_STATE\_NOT\_READY](hl7800_8h.md#a4b00cc03cc14b3812bed4a57aeea822caccfc2361ab2bea50b510c428786a9a07) = 0,

[ 119](hl7800_8h.md#a4b00cc03cc14b3812bed4a57aeea822ca44858cd6e73be2697e39f60aa54565be) [HL7800\_STATE\_INITIALIZED](hl7800_8h.md#a4b00cc03cc14b3812bed4a57aeea822ca44858cd6e73be2697e39f60aa54565be),

120};

121

[ 122](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99)enum [mdm\_hl7800\_startup\_state](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99) {

[ 123](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99aac2ef169e3273dd11331acae3abb9c6e) [HL7800\_STARTUP\_STATE\_READY](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99aac2ef169e3273dd11331acae3abb9c6e) = 0,

[ 124](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a60dd736ae85eeafaefce839b623c530f) [HL7800\_STARTUP\_STATE\_WAITING\_FOR\_ACCESS\_CODE](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a60dd736ae85eeafaefce839b623c530f),

[ 125](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a92593373e0efcb87471c6d0325f1c2e6) [HL7800\_STARTUP\_STATE\_SIM\_NOT\_PRESENT](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a92593373e0efcb87471c6d0325f1c2e6),

[ 126](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a098e678b80c7148972d572f6dac763d6) [HL7800\_STARTUP\_STATE\_SIMLOCK](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a098e678b80c7148972d572f6dac763d6),

[ 127](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a1b88f9edf57f6fe1b9f4b31ecb196632) [HL7800\_STARTUP\_STATE\_UNRECOVERABLE\_ERROR](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a1b88f9edf57f6fe1b9f4b31ecb196632),

[ 128](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a9d2a5fd088822989fc109cb3add31393) [HL7800\_STARTUP\_STATE\_UNKNOWN](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a9d2a5fd088822989fc109cb3add31393),

[ 129](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a9999f1a90165d5996a7a2ff415db53d6) [HL7800\_STARTUP\_STATE\_INACTIVE\_SIM](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a9999f1a90165d5996a7a2ff415db53d6)

130};

131

[ 132](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773)enum [mdm\_hl7800\_network\_state](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773) {

[ 133](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a94fe4bdd729ba6df15d9e9aa53998599) [HL7800\_NOT\_REGISTERED](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a94fe4bdd729ba6df15d9e9aa53998599) = 0,

[ 134](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a7e5bdc7f85c2d2f6ec62beee156e887d) [HL7800\_HOME\_NETWORK](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a7e5bdc7f85c2d2f6ec62beee156e887d),

[ 135](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a1ad9a81e5ce65dc6eee98a87f880f86a) [HL7800\_SEARCHING](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a1ad9a81e5ce65dc6eee98a87f880f86a),

[ 136](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a4eeb75667b400acaff56ad282bfe6a7c) [HL7800\_REGISTRATION\_DENIED](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a4eeb75667b400acaff56ad282bfe6a7c),

[ 137](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773ae3f6d693bbe0d0c09a41a0e013fe5a82) [HL7800\_OUT\_OF\_COVERAGE](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773ae3f6d693bbe0d0c09a41a0e013fe5a82),

[ 138](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a9d7e014131f399f000965803ccb5e889) [HL7800\_ROAMING](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a9d7e014131f399f000965803ccb5e889),

[ 139](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a04cac2efa21c949edeefc105effa4a39) [HL7800\_EMERGENCY](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a04cac2efa21c949edeefc105effa4a39) = 8,

140 /\* Laird defined states \*/

[ 141](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a2502129bf7729cce4b1b96ac66dfdd86) [HL7800\_UNABLE\_TO\_CONFIGURE](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a2502129bf7729cce4b1b96ac66dfdd86) = 0xf0

142};

143

[ 144](hl7800_8h.md#a3396149e553c32a597739096efe2aff7)enum [mdm\_hl7800\_sleep](hl7800_8h.md#a3396149e553c32a597739096efe2aff7) {

[ 145](hl7800_8h.md#a3396149e553c32a597739096efe2aff7af81cd0793c7faded881246c6a44b099a) [HL7800\_SLEEP\_UNINITIALIZED](hl7800_8h.md#a3396149e553c32a597739096efe2aff7af81cd0793c7faded881246c6a44b099a) = 0,

[ 146](hl7800_8h.md#a3396149e553c32a597739096efe2aff7af1253aa2135a3c1fb0f3a47a1f0265a4) [HL7800\_SLEEP\_HIBERNATE](hl7800_8h.md#a3396149e553c32a597739096efe2aff7af1253aa2135a3c1fb0f3a47a1f0265a4),

[ 147](hl7800_8h.md#a3396149e553c32a597739096efe2aff7ac7bf9c4685d31858b98d4188747387ba) [HL7800\_SLEEP\_AWAKE](hl7800_8h.md#a3396149e553c32a597739096efe2aff7ac7bf9c4685d31858b98d4188747387ba),

[ 148](hl7800_8h.md#a3396149e553c32a597739096efe2aff7a58c8b0b7a63a3f85b14d0cd0eea4b452) [HL7800\_SLEEP\_LITE\_HIBERNATE](hl7800_8h.md#a3396149e553c32a597739096efe2aff7a58c8b0b7a63a3f85b14d0cd0eea4b452),

[ 149](hl7800_8h.md#a3396149e553c32a597739096efe2aff7a37e4283b77e32e890f7cc3eca3985289) [HL7800\_SLEEP\_SLEEP](hl7800_8h.md#a3396149e553c32a597739096efe2aff7a37e4283b77e32e890f7cc3eca3985289),

150};

151

[ 152](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3)enum [mdm\_hl7800\_fota\_state](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3) {

[ 153](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3ab7d67051e56e05be47da306377bb8801) [HL7800\_FOTA\_IDLE](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3ab7d67051e56e05be47da306377bb8801),

[ 154](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3ae6b160137651a7375551760f938b9da8) [HL7800\_FOTA\_START](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3ae6b160137651a7375551760f938b9da8),

[ 155](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a722b66bd586cc4375253341f1df8d189) [HL7800\_FOTA\_WIP](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a722b66bd586cc4375253341f1df8d189),

[ 156](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a481fdc3814098383af7b593d4f61ea7b) [HL7800\_FOTA\_PAD](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a481fdc3814098383af7b593d4f61ea7b),

[ 157](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3aa78ef13656312bb81aa957a515b337d7) [HL7800\_FOTA\_SEND\_EOT](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3aa78ef13656312bb81aa957a515b337d7),

[ 158](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3aaf2423203fdb79510efa9550e2a09bf9) [HL7800\_FOTA\_FILE\_ERROR](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3aaf2423203fdb79510efa9550e2a09bf9),

[ 159](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a6761ef6c52c40786c8b595950499851e) [HL7800\_FOTA\_INSTALL](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a6761ef6c52c40786c8b595950499851e),

[ 160](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a5e517d07a386297b5d80110cabc1864b) [HL7800\_FOTA\_REBOOT\_AND\_RECONFIGURE](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a5e517d07a386297b5d80110cabc1864b),

[ 161](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3abd185b07f408b4b7ecb292f31aa6d19a) [HL7800\_FOTA\_COMPLETE](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3abd185b07f408b4b7ecb292f31aa6d19a),

162};

163

[ 164](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2)enum [mdm\_hl7800\_functionality](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2) {

[ 165](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2ae2c5fac661bdf514debc98b3e248cea4) [HL7800\_FUNCTIONALITY\_MINIMUM](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2ae2c5fac661bdf514debc98b3e248cea4) = 0,

[ 166](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2ad1e22b662121c8c71b9d34810958b6c2) [HL7800\_FUNCTIONALITY\_FULL](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2ad1e22b662121c8c71b9d34810958b6c2) = 1,

[ 167](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2a2aca52c7dc8ade5db478f8eaebc4bc33) [HL7800\_FUNCTIONALITY\_AIRPLANE](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2a2aca52c7dc8ade5db478f8eaebc4bc33) = 4

168};

169

170/\* The modem reports state values as an enumeration and a string.

171 \* GPS values are reported with a type of value and string.

172 \*/

[ 173](structmdm__hl7800__compound__event.md)struct [mdm\_hl7800\_compound\_event](structmdm__hl7800__compound__event.md) {

[ 174](structmdm__hl7800__compound__event.md#abf3581062c802a15f71c250c56609aaf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [code](structmdm__hl7800__compound__event.md#abf3581062c802a15f71c250c56609aaf);

[ 175](structmdm__hl7800__compound__event.md#a014d5de10c32177e4dd3fb011a0793d5) char \*[string](structmdm__hl7800__compound__event.md#a014d5de10c32177e4dd3fb011a0793d5);

176};

177

[ 178](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043b)enum [mdm\_hl7800\_gnss\_event](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043b) {

[ 179](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba3349e6599deabd375c68bb3688bd9bfd) [HL7800\_GNSS\_EVENT\_INVALID](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba3349e6599deabd375c68bb3688bd9bfd) = -1,

[ 180](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba3b0b73d5b585d4ed44e00504be60c8ef) [HL7800\_GNSS\_EVENT\_INIT](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba3b0b73d5b585d4ed44e00504be60c8ef),

[ 181](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba689418f8d35440fe71507ee871f20de1) [HL7800\_GNSS\_EVENT\_START](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba689418f8d35440fe71507ee871f20de1),

[ 182](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043bae83741a25baa0ffc3837b0653b01c318) [HL7800\_GNSS\_EVENT\_STOP](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043bae83741a25baa0ffc3837b0653b01c318),

[ 183](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba2df7e19144b20afb4bf3566804729db1) [HL7800\_GNSS\_EVENT\_POSITION](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba2df7e19144b20afb4bf3566804729db1),

184};

185

[ 186](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625)enum [mdm\_hl7800\_gnss\_status](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625) {

[ 187](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625aadc2b5c2e8b257e8b12ae7c4f5f35d76) [HL7800\_GNSS\_STATUS\_INVALID](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625aadc2b5c2e8b257e8b12ae7c4f5f35d76) = -1,

[ 188](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625a830898a215c51c8a17aab3fb175083b3) [HL7800\_GNSS\_STATUS\_FAILURE](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625a830898a215c51c8a17aab3fb175083b3),

[ 189](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625ab989ec2e119be4f23a37cac5203225ab) [HL7800\_GNSS\_STATUS\_SUCCESS](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625ab989ec2e119be4f23a37cac5203225ab),

190};

191

[ 192](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696b)enum [mdm\_hl7800\_gnss\_position\_event](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696b) {

[ 193](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696babf5377809190c648e6f3624b4b0b82ee) [HL7800\_GNSS\_POSITION\_EVENT\_INVALID](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696babf5377809190c648e6f3624b4b0b82ee) = -1,

[ 194](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696bac41b513dd45d2d038b9d7a4a9bae8fe3) [HL7800\_GNSS\_POSITION\_EVENT\_LOST\_OR\_NOT\_AVAILABLE\_YET](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696bac41b513dd45d2d038b9d7a4a9bae8fe3),

[ 195](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696bad41adce29331d1917c97e94b6409a9b5) [HL7800\_GNSS\_POSITION\_EVENT\_PREDICTION\_AVAILABLE](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696bad41adce29331d1917c97e94b6409a9b5),

[ 196](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696ba1cf9c2fe042ab784450451f36b83818d) [HL7800\_GNSS\_POSITION\_EVENT\_2D\_AVAILABLE](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696ba1cf9c2fe042ab784450451f36b83818d),

[ 197](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696ba6bd45fa147597e9c278ec0f27c42efc7) [HL7800\_GNSS\_POSITION\_EVENT\_3D\_AVAILABLE](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696ba6bd45fa147597e9c278ec0f27c42efc7),

[ 198](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696ba9822e7c1f4a238658592a539d18d0c6d) [HL7800\_GNSS\_POSITION\_EVENT\_FIXED\_TO\_INVALID](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696ba9822e7c1f4a238658592a539d18d0c6d),

199};

200

[ 201](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038)enum [mdm\_hl7800\_gps\_string\_types](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038) {

[ 202](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a5faac685b9958871cc3feb990e593b8b) [HL7800\_GPS\_STR\_LATITUDE](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a5faac685b9958871cc3feb990e593b8b),

[ 203](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a56f4e3a1a3b2eaacb2c34ec486165de8) [HL7800\_GPS\_STR\_LONGITUDE](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a56f4e3a1a3b2eaacb2c34ec486165de8),

[ 204](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a17989267e59a5169abb7f4d4c8bb3694) [HL7800\_GPS\_STR\_GPS\_TIME](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a17989267e59a5169abb7f4d4c8bb3694),

[ 205](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a7cd77b6bf81380fdaba8cdad863a60be) [HL7800\_GPS\_STR\_FIX\_TYPE](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a7cd77b6bf81380fdaba8cdad863a60be),

[ 206](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038aca3dac785dc09cc6d0780c2ce1956de4) [HL7800\_GPS\_STR\_HEPE](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038aca3dac785dc09cc6d0780c2ce1956de4),

[ 207](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a1eac295eb05a3c4617d35c9fd29aebf6) [HL7800\_GPS\_STR\_ALTITUDE](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a1eac295eb05a3c4617d35c9fd29aebf6),

[ 208](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a39502c1243b0df6765d6025e8173f214) [HL7800\_GPS\_STR\_ALT\_UNC](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a39502c1243b0df6765d6025e8173f214),

[ 209](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038af5bef33ea67240657038a288f600ec25) [HL7800\_GPS\_STR\_DIRECTION](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038af5bef33ea67240657038a288f600ec25),

[ 210](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038ac7f6f8e1d00b25b551a1560b7d998fc8) [HL7800\_GPS\_STR\_HOR\_SPEED](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038ac7f6f8e1d00b25b551a1560b7d998fc8),

[ 211](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a40e32118c8039cfd3c6ef72c8a4d7f85) [HL7800\_GPS\_STR\_VER\_SPEED](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a40e32118c8039cfd3c6ef72c8a4d7f85)

212};

213

214/\* status: negative errno, 0 on success

215 \* user and password aren't valid if status is non-zero.

216 \*/

[ 217](structmdm__hl7800__polte__registration__event__data.md)struct [mdm\_hl7800\_polte\_registration\_event\_data](structmdm__hl7800__polte__registration__event__data.md) {

[ 218](structmdm__hl7800__polte__registration__event__data.md#a1d591b3a469fb6fed674fb07455ed8d0) int [status](structmdm__hl7800__polte__registration__event__data.md#a1d591b3a469fb6fed674fb07455ed8d0);

[ 219](structmdm__hl7800__polte__registration__event__data.md#adc8d2cee46aae9ed0736d85ab5805cb0) char \*[user](structmdm__hl7800__polte__registration__event__data.md#adc8d2cee46aae9ed0736d85ab5805cb0);

[ 220](structmdm__hl7800__polte__registration__event__data.md#ad551f94f2488544e69f622d7d26f87d9) char \*[password](structmdm__hl7800__polte__registration__event__data.md#ad551f94f2488544e69f622d7d26f87d9);

221};

222

223/\* status: negative errno, 0 on success, non-zero error code

224 \* Data is not valid if status is non-zero.

225 \*/

[ 226](structmdm__hl7800__polte__location__data.md)struct [mdm\_hl7800\_polte\_location\_data](structmdm__hl7800__polte__location__data.md) {

[ 227](structmdm__hl7800__polte__location__data.md#aaae6d4f0ff600f595bad143166f5605c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp](structmdm__hl7800__polte__location__data.md#aaae6d4f0ff600f595bad143166f5605c);

[ 228](structmdm__hl7800__polte__location__data.md#a3a95fb87ddf47eb9d447b9dd0da92cf3) int [status](structmdm__hl7800__polte__location__data.md#a3a95fb87ddf47eb9d447b9dd0da92cf3);

[ 229](structmdm__hl7800__polte__location__data.md#adc4a7aee1014c0290294240bd968e232) char [latitude](structmdm__hl7800__polte__location__data.md#adc4a7aee1014c0290294240bd968e232)[[MDM\_HL7800\_MAX\_POLTE\_LOCATION\_STR\_SIZE](hl7800_8h.md#a060fccbbb60656b655abb3a8ad59f428)];

[ 230](structmdm__hl7800__polte__location__data.md#a5114024090c7d039d63219495d9fd343) char [longitude](structmdm__hl7800__polte__location__data.md#a5114024090c7d039d63219495d9fd343)[[MDM\_HL7800\_MAX\_POLTE\_LOCATION\_STR\_SIZE](hl7800_8h.md#a060fccbbb60656b655abb3a8ad59f428)];

[ 231](structmdm__hl7800__polte__location__data.md#a479ebd4268c0138138d62818b96a1593) char [confidence\_in\_meters](structmdm__hl7800__polte__location__data.md#a479ebd4268c0138138d62818b96a1593)[[MDM\_HL7800\_MAX\_POLTE\_LOCATION\_STR\_SIZE](hl7800_8h.md#a060fccbbb60656b655abb3a8ad59f428)];

232};

233

[ 257](hl7800_8h.md#afa044d03d9bfbc2f63088da4f094edfc)typedef void (\*[mdm\_hl7800\_event\_callback\_t](hl7800_8h.md#afa044d03d9bfbc2f63088da4f094edfc))(enum [mdm\_hl7800\_event](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9) event,

258 void \*event\_data);

259

[ 260](structmdm__hl7800__callback__agent.md)struct [mdm\_hl7800\_callback\_agent](structmdm__hl7800__callback__agent.md) {

[ 261](structmdm__hl7800__callback__agent.md#a5b69a3952ee320ee88fd99220bac3ef5) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structmdm__hl7800__callback__agent.md#a5b69a3952ee320ee88fd99220bac3ef5);

[ 262](structmdm__hl7800__callback__agent.md#adb1eb808c084c9afb6077b04aa1bb026) [mdm\_hl7800\_event\_callback\_t](hl7800_8h.md#afa044d03d9bfbc2f63088da4f094edfc) [event\_callback](structmdm__hl7800__callback__agent.md#adb1eb808c084c9afb6077b04aa1bb026);

263};

264

[ 270](hl7800_8h.md#ae270849872a22823512cc87b0bbf877e)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_power\_off](hl7800_8h.md#ae270849872a22823512cc87b0bbf877e)(void);

271

[ 277](hl7800_8h.md#a956932a3c7d45f5ab0c3c99aa1decfb4)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_reset](hl7800_8h.md#a956932a3c7d45f5ab0c3c99aa1decfb4)(void);

278

[ 285](hl7800_8h.md#a430e2a1e2e8173dab93cf7b1e1fcb24d)void [mdm\_hl7800\_wakeup](hl7800_8h.md#a430e2a1e2e8173dab93cf7b1e1fcb24d)(bool awake);

286

[ 299](hl7800_8h.md#a41a1f8f29c6ac8b53e5ef05f156a64a9)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_send\_at\_cmd](hl7800_8h.md#a41a1f8f29c6ac8b53e5ef05f156a64a9)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) resp\_timeout, char \*resp,

300 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*resp\_len);

301

[ 314](hl7800_8h.md#ad7d20cde62d5e7c987672cc9c10b152e)void [mdm\_hl7800\_get\_signal\_quality](hl7800_8h.md#ad7d20cde62d5e7c987672cc9c10b152e)(int \*rsrp, int \*sinr);

315

[ 320](hl7800_8h.md#af84e782e572faf543a37a40147660eb0)char \*[mdm\_hl7800\_get\_iccid](hl7800_8h.md#af84e782e572faf543a37a40147660eb0)(void);

321

[ 326](hl7800_8h.md#a1f3a7b2dd7654941006c4a8d5a46af01)char \*[mdm\_hl7800\_get\_sn](hl7800_8h.md#a1f3a7b2dd7654941006c4a8d5a46af01)(void);

327

[ 332](hl7800_8h.md#a4278b7f58b77048b8e833d9215183a5f)char \*[mdm\_hl7800\_get\_imei](hl7800_8h.md#a4278b7f58b77048b8e833d9215183a5f)(void);

333

[ 338](hl7800_8h.md#ac65dc452be996e5366360abb314a4d98)char \*[mdm\_hl7800\_get\_fw\_version](hl7800_8h.md#ac65dc452be996e5366360abb314a4d98)(void);

339

[ 344](hl7800_8h.md#a581582e3f7b07f04e6b33e481e2d6e42)char \*[mdm\_hl7800\_get\_imsi](hl7800_8h.md#a581582e3f7b07f04e6b33e481e2d6e42)(void);

345

[ 351](hl7800_8h.md#a3bf4e149e475d8a7c1f462c7de2dda80)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_update\_apn](hl7800_8h.md#a3bf4e149e475d8a7c1f462c7de2dda80)(char \*access\_point\_name);

352

[ 358](hl7800_8h.md#a9d295b105e71346fcb283959d2641079)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_update\_rat](hl7800_8h.md#a9d295b105e71346fcb283959d2641079)(enum [mdm\_hl7800\_radio\_mode](hl7800_8h.md#a2d26759e8ea3aca2e8e4a6cccac2361a) value);

359

[ 363](hl7800_8h.md#a0b3822e97cbb77f4edab74e8bf2c903e)bool [mdm\_hl7800\_valid\_rat](hl7800_8h.md#a0b3822e97cbb77f4edab74e8bf2c903e)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

364

[ 373](hl7800_8h.md#afab74f2bd3806a23192cae18f65226ad)int [mdm\_hl7800\_register\_event\_callback](hl7800_8h.md#afab74f2bd3806a23192cae18f65226ad)(struct [mdm\_hl7800\_callback\_agent](structmdm__hl7800__callback__agent.md) \*agent);

374

[ 382](hl7800_8h.md#ae2015e7399a17a862048eed89b036c6d)int [mdm\_hl7800\_unregister\_event\_callback](hl7800_8h.md#ae2015e7399a17a862048eed89b036c6d)(struct [mdm\_hl7800\_callback\_agent](structmdm__hl7800__callback__agent.md) \*agent);

383

[ 390](hl7800_8h.md#aaac620a4653d772f4d44a73834a8b4cc)void [mdm\_hl7800\_generate\_status\_events](hl7800_8h.md#aaac620a4653d772f4d44a73834a8b4cc)(void);

391

[ 399](hl7800_8h.md#afa95fa49240c3412521bade1245bc573)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_get\_local\_time](hl7800_8h.md#afa95fa49240c3412521bade1245bc573)(struct [tm](structtm.md) \*[tm](structtm.md), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*offset);

400

401#ifdef CONFIG\_MODEM\_HL7800\_FW\_UPDATE

410[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) mdm\_hl7800\_update\_fw(char \*file\_path);

411#endif

412

[ 418](hl7800_8h.md#a2bb74593dea9486754af21e50f4a6291)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_get\_operator\_index](hl7800_8h.md#a2bb74593dea9486754af21e50f4a6291)(void);

419

[ 425](hl7800_8h.md#a32dc9651acf319448da38709fc488d16)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_get\_functionality](hl7800_8h.md#a32dc9651acf319448da38709fc488d16)(void);

426

[ 437](hl7800_8h.md#a1ca397e9e9db680dc6083ba2b4c08a70)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_set\_functionality](hl7800_8h.md#a1ca397e9e9db680dc6083ba2b4c08a70)(enum [mdm\_hl7800\_functionality](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2) mode);

438

[ 449](hl7800_8h.md#a2946b1d49c63084188f5f6c5dcebaaf2)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_set\_gps\_rate](hl7800_8h.md#a2946b1d49c63084188f5f6c5dcebaaf2)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rate);

450

[ 461](hl7800_8h.md#a8501f6d4883ee8577b5cda0f76d2a3dc)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_polte\_register](hl7800_8h.md#a8501f6d4883ee8577b5cda0f76d2a3dc)(void);

462

[ 470](hl7800_8h.md#a22eb248b7aeb36a1c9895c8de6808f08)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_polte\_enable](hl7800_8h.md#a22eb248b7aeb36a1c9895c8de6808f08)(char \*user, char \*password);

471

[ 482](hl7800_8h.md#a1708f077ddb438f93b246b223e52a80d)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_polte\_locate](hl7800_8h.md#a1708f077ddb438f93b246b223e52a80d)(void);

483

[ 492](hl7800_8h.md#a975a4cd75d9d89dd23b182af2376ef91)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_perform\_site\_survey](hl7800_8h.md#a975a4cd75d9d89dd23b182af2376ef91)(void);

493

[ 500](hl7800_8h.md#a2388ecc33d15263091c63185ccda3ea3)int [mdm\_hl7800\_set\_desired\_sleep\_level](hl7800_8h.md#a2388ecc33d15263091c63185ccda3ea3)(enum [mdm\_hl7800\_sleep](hl7800_8h.md#a3396149e553c32a597739096efe2aff7) level);

501

[ 510](hl7800_8h.md#a16ac0447c88a9f025fc13009e63f46ef)void [mdm\_hl7800\_register\_wake\_test\_point\_callback](hl7800_8h.md#a16ac0447c88a9f025fc13009e63f46ef)(void (\*func)(int [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)));

511

[ 521](hl7800_8h.md#a0e5213411b27b4c5eeffd746464332a8)void [mdm\_hl7800\_register\_gpio6\_callback](hl7800_8h.md#a0e5213411b27b4c5eeffd746464332a8)(void (\*func)(int [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)));

522

[ 531](hl7800_8h.md#aead5a1419d87676f13fdea12f705b125)void [mdm\_hl7800\_register\_cts\_callback](hl7800_8h.md#aead5a1419d87676f13fdea12f705b125)(void (\*func)(int [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)));

532

[ 542](hl7800_8h.md#a935e3010e0a2d633e366711c09f634f1)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [mdm\_hl7800\_set\_bands](hl7800_8h.md#a935e3010e0a2d633e366711c09f634f1)(const char \*bands);

543

[ 554](hl7800_8h.md#a838f6aab78e6f41028d381823cb6b118)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mdm\_hl7800\_log\_filter\_set](hl7800_8h.md#a838f6aab78e6f41028d381823cb6b118)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level);

555

556#ifdef \_\_cplusplus

557}

558#endif

559

560#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MODEM\_HL7800\_H\_ \*/

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[MDM\_HL7800\_MAX\_POLTE\_LOCATION\_STR\_SIZE](hl7800_8h.md#a060fccbbb60656b655abb3a8ad59f428)

#define MDM\_HL7800\_MAX\_POLTE\_LOCATION\_STR\_SIZE

**Definition** hl7800.h:75

[mdm\_hl7800\_valid\_rat](hl7800_8h.md#a0b3822e97cbb77f4edab74e8bf2c903e)

bool mdm\_hl7800\_valid\_rat(uint8\_t value)

[mdm\_hl7800\_register\_gpio6\_callback](hl7800_8h.md#a0e5213411b27b4c5eeffd746464332a8)

void mdm\_hl7800\_register\_gpio6\_callback(void(\*func)(int state))

Allows mapping of P1.12\_GPIO6 signal to a user accessible test point on the development board.

[mdm\_hl7800\_register\_wake\_test\_point\_callback](hl7800_8h.md#a16ac0447c88a9f025fc13009e63f46ef)

void mdm\_hl7800\_register\_wake\_test\_point\_callback(void(\*func)(int state))

Allows mapping of WAKE\_UP signal to a user accessible test point on the development board.

[mdm\_hl7800\_polte\_locate](hl7800_8h.md#a1708f077ddb438f93b246b223e52a80d)

int32\_t mdm\_hl7800\_polte\_locate(void)

Locate device using PoLTE.

[mdm\_hl7800\_set\_functionality](hl7800_8h.md#a1ca397e9e9db680dc6083ba2b4c08a70)

int32\_t mdm\_hl7800\_set\_functionality(enum mdm\_hl7800\_functionality mode)

Set airplane, normal, or reduced functionality mode.

[mdm\_hl7800\_get\_sn](hl7800_8h.md#a1f3a7b2dd7654941006c4a8d5a46af01)

char \* mdm\_hl7800\_get\_sn(void)

Get the HL7800 serial number.

[mdm\_hl7800\_polte\_enable](hl7800_8h.md#a22eb248b7aeb36a1c9895c8de6808f08)

int32\_t mdm\_hl7800\_polte\_enable(char \*user, char \*password)

Enable PoLTE.

[mdm\_hl7800\_set\_desired\_sleep\_level](hl7800_8h.md#a2388ecc33d15263091c63185ccda3ea3)

int mdm\_hl7800\_set\_desired\_sleep\_level(enum mdm\_hl7800\_sleep level)

Set desired sleep level.

[mdm\_hl7800\_set\_gps\_rate](hl7800_8h.md#a2946b1d49c63084188f5f6c5dcebaaf2)

int32\_t mdm\_hl7800\_set\_gps\_rate(uint32\_t rate)

When rate is non-zero: Put modem into Airplane mode.

[mdm\_hl7800\_get\_operator\_index](hl7800_8h.md#a2bb74593dea9486754af21e50f4a6291)

int32\_t mdm\_hl7800\_get\_operator\_index(void)

Read the operator index from the modem.

[mdm\_hl7800\_radio\_mode](hl7800_8h.md#a2d26759e8ea3aca2e8e4a6cccac2361a)

mdm\_hl7800\_radio\_mode

**Definition** hl7800.h:92

[MDM\_RAT\_CAT\_NB1](hl7800_8h.md#a2d26759e8ea3aca2e8e4a6cccac2361aa30bba3902918ea11995cd3db20319d61)

@ MDM\_RAT\_CAT\_NB1

**Definition** hl7800.h:92

[MDM\_RAT\_CAT\_M1](hl7800_8h.md#a2d26759e8ea3aca2e8e4a6cccac2361aac95a4a3318b0683972336c1036f0548e)

@ MDM\_RAT\_CAT\_M1

**Definition** hl7800.h:92

[mdm\_hl7800\_get\_functionality](hl7800_8h.md#a32dc9651acf319448da38709fc488d16)

int32\_t mdm\_hl7800\_get\_functionality(void)

Get modem functionality.

[mdm\_hl7800\_sleep](hl7800_8h.md#a3396149e553c32a597739096efe2aff7)

mdm\_hl7800\_sleep

**Definition** hl7800.h:144

[HL7800\_SLEEP\_SLEEP](hl7800_8h.md#a3396149e553c32a597739096efe2aff7a37e4283b77e32e890f7cc3eca3985289)

@ HL7800\_SLEEP\_SLEEP

**Definition** hl7800.h:149

[HL7800\_SLEEP\_LITE\_HIBERNATE](hl7800_8h.md#a3396149e553c32a597739096efe2aff7a58c8b0b7a63a3f85b14d0cd0eea4b452)

@ HL7800\_SLEEP\_LITE\_HIBERNATE

**Definition** hl7800.h:148

[HL7800\_SLEEP\_AWAKE](hl7800_8h.md#a3396149e553c32a597739096efe2aff7ac7bf9c4685d31858b98d4188747387ba)

@ HL7800\_SLEEP\_AWAKE

**Definition** hl7800.h:147

[HL7800\_SLEEP\_HIBERNATE](hl7800_8h.md#a3396149e553c32a597739096efe2aff7af1253aa2135a3c1fb0f3a47a1f0265a4)

@ HL7800\_SLEEP\_HIBERNATE

**Definition** hl7800.h:146

[HL7800\_SLEEP\_UNINITIALIZED](hl7800_8h.md#a3396149e553c32a597739096efe2aff7af81cd0793c7faded881246c6a44b099a)

@ HL7800\_SLEEP\_UNINITIALIZED

**Definition** hl7800.h:145

[mdm\_hl7800\_update\_apn](hl7800_8h.md#a3bf4e149e475d8a7c1f462c7de2dda80)

int32\_t mdm\_hl7800\_update\_apn(char \*access\_point\_name)

Update the Access Point Name in the modem.

[mdm\_hl7800\_event](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9)

mdm\_hl7800\_event

**Definition** hl7800.h:94

[HL7800\_EVENT\_NETWORK\_STATE\_CHANGE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a08a58f10e3d58022ac945b2e68d4145a)

@ HL7800\_EVENT\_NETWORK\_STATE\_CHANGE

**Definition** hl7800.h:96

[HL7800\_EVENT\_GPS\_POSITION\_STATUS](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a0b9e7d1fcb8f043c5ac0b242e4c6c772)

@ HL7800\_EVENT\_GPS\_POSITION\_STATUS

**Definition** hl7800.h:109

[HL7800\_EVENT\_STARTUP\_STATE\_CHANGE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a0d25a89cd39d581c82ae73fe0a85ba21)

@ HL7800\_EVENT\_STARTUP\_STATE\_CHANGE

**Definition** hl7800.h:100

[HL7800\_EVENT\_POLTE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a1fb1cd6b652c52ebf12e9741649f8630)

@ HL7800\_EVENT\_POLTE

**Definition** hl7800.h:112

[HL7800\_EVENT\_BANDS](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a327cd78d882a1a36716236f2cdf28c31)

@ HL7800\_EVENT\_BANDS

**Definition** hl7800.h:103

[HL7800\_EVENT\_SITE\_SURVEY](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a37463d52131771a296fb141c797b3e14)

@ HL7800\_EVENT\_SITE\_SURVEY

**Definition** hl7800.h:113

[HL7800\_EVENT\_FOTA\_COUNT](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a3848abb978d465bd0a831fc0b66a33c3)

@ HL7800\_EVENT\_FOTA\_COUNT

**Definition** hl7800.h:106

[HL7800\_EVENT\_APN\_UPDATE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a4cf6f0344fa2348f378756e77d5f2804)

@ HL7800\_EVENT\_APN\_UPDATE

**Definition** hl7800.h:97

[HL7800\_EVENT\_RESERVED](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a7147e1d7ea1df5eb7604c3246a94ec0a)

@ HL7800\_EVENT\_RESERVED

**Definition** hl7800.h:95

[HL7800\_EVENT\_SLEEP\_STATE\_CHANGE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a7bd6e3e3c19ed2c5ac138c16e03b2562)

@ HL7800\_EVENT\_SLEEP\_STATE\_CHANGE

**Definition** hl7800.h:101

[HL7800\_EVENT\_POLTE\_LOCATE\_STATUS](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a7ee246b282ac147aafa45969060c5280)

@ HL7800\_EVENT\_POLTE\_LOCATE\_STATUS

**Definition** hl7800.h:111

[HL7800\_EVENT\_REVISION](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a8a3b921d5bdb205f44576852467c38e2)

@ HL7800\_EVENT\_REVISION

**Definition** hl7800.h:107

[HL7800\_EVENT\_STATE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9a9189ebbdcf3175881a0e55ac9867acbf)

@ HL7800\_EVENT\_STATE

**Definition** hl7800.h:114

[HL7800\_EVENT\_ACTIVE\_BANDS](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9aad01f254032296551f621c888530e9d1)

@ HL7800\_EVENT\_ACTIVE\_BANDS

**Definition** hl7800.h:104

[HL7800\_EVENT\_RSSI](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9abb822dfaec7e96462be791857f9b3fba)

@ HL7800\_EVENT\_RSSI

**Definition** hl7800.h:98

[HL7800\_EVENT\_RAT](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9ac22e246ac6bc5794ae0772bf3dbf5086)

@ HL7800\_EVENT\_RAT

**Definition** hl7800.h:102

[HL7800\_EVENT\_SINR](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9ac76f3fec60d1ffeca58405cf38bd50fe)

@ HL7800\_EVENT\_SINR

**Definition** hl7800.h:99

[HL7800\_EVENT\_POLTE\_REGISTRATION](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9aead019c4cd55d1f54fb16ddef7f8277c)

@ HL7800\_EVENT\_POLTE\_REGISTRATION

**Definition** hl7800.h:110

[HL7800\_EVENT\_FOTA\_STATE](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9aedd9ae54dfa7a007c18e2a345d0cb0c5)

@ HL7800\_EVENT\_FOTA\_STATE

**Definition** hl7800.h:105

[HL7800\_EVENT\_GPS](hl7800_8h.md#a3f7b0647d9ff01328e5536478a73aaf9af3410e6ff2caa844c3b6f9963df485d1)

@ HL7800\_EVENT\_GPS

**Definition** hl7800.h:108

[mdm\_hl7800\_send\_at\_cmd](hl7800_8h.md#a41a1f8f29c6ac8b53e5ef05f156a64a9)

int32\_t mdm\_hl7800\_send\_at\_cmd(const uint8\_t \*data, uint8\_t resp\_timeout, char \*resp, uint16\_t \*resp\_len)

Send an AT command to the HL7800.

[mdm\_hl7800\_get\_imei](hl7800_8h.md#a4278b7f58b77048b8e833d9215183a5f)

char \* mdm\_hl7800\_get\_imei(void)

Get the HL7800 IMEI.

[mdm\_hl7800\_wakeup](hl7800_8h.md#a430e2a1e2e8173dab93cf7b1e1fcb24d)

void mdm\_hl7800\_wakeup(bool awake)

Control the wake signals to the HL7800.

[mdm\_hl7800\_gps\_string\_types](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038)

mdm\_hl7800\_gps\_string\_types

**Definition** hl7800.h:201

[HL7800\_GPS\_STR\_GPS\_TIME](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a17989267e59a5169abb7f4d4c8bb3694)

@ HL7800\_GPS\_STR\_GPS\_TIME

**Definition** hl7800.h:204

[HL7800\_GPS\_STR\_ALTITUDE](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a1eac295eb05a3c4617d35c9fd29aebf6)

@ HL7800\_GPS\_STR\_ALTITUDE

**Definition** hl7800.h:207

[HL7800\_GPS\_STR\_ALT\_UNC](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a39502c1243b0df6765d6025e8173f214)

@ HL7800\_GPS\_STR\_ALT\_UNC

**Definition** hl7800.h:208

[HL7800\_GPS\_STR\_VER\_SPEED](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a40e32118c8039cfd3c6ef72c8a4d7f85)

@ HL7800\_GPS\_STR\_VER\_SPEED

**Definition** hl7800.h:211

[HL7800\_GPS\_STR\_LONGITUDE](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a56f4e3a1a3b2eaacb2c34ec486165de8)

@ HL7800\_GPS\_STR\_LONGITUDE

**Definition** hl7800.h:203

[HL7800\_GPS\_STR\_LATITUDE](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a5faac685b9958871cc3feb990e593b8b)

@ HL7800\_GPS\_STR\_LATITUDE

**Definition** hl7800.h:202

[HL7800\_GPS\_STR\_FIX\_TYPE](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038a7cd77b6bf81380fdaba8cdad863a60be)

@ HL7800\_GPS\_STR\_FIX\_TYPE

**Definition** hl7800.h:205

[HL7800\_GPS\_STR\_HOR\_SPEED](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038ac7f6f8e1d00b25b551a1560b7d998fc8)

@ HL7800\_GPS\_STR\_HOR\_SPEED

**Definition** hl7800.h:210

[HL7800\_GPS\_STR\_HEPE](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038aca3dac785dc09cc6d0780c2ce1956de4)

@ HL7800\_GPS\_STR\_HEPE

**Definition** hl7800.h:206

[HL7800\_GPS\_STR\_DIRECTION](hl7800_8h.md#a45fd97039bb3add8ddb09f803ce9b038af5bef33ea67240657038a288f600ec25)

@ HL7800\_GPS\_STR\_DIRECTION

**Definition** hl7800.h:209

[mdm\_hl7800\_state](hl7800_8h.md#a4b00cc03cc14b3812bed4a57aeea822c)

mdm\_hl7800\_state

**Definition** hl7800.h:117

[HL7800\_STATE\_INITIALIZED](hl7800_8h.md#a4b00cc03cc14b3812bed4a57aeea822ca44858cd6e73be2697e39f60aa54565be)

@ HL7800\_STATE\_INITIALIZED

**Definition** hl7800.h:119

[HL7800\_STATE\_NOT\_READY](hl7800_8h.md#a4b00cc03cc14b3812bed4a57aeea822caccfc2361ab2bea50b510c428786a9a07)

@ HL7800\_STATE\_NOT\_READY

**Definition** hl7800.h:118

[mdm\_hl7800\_gnss\_status](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625)

mdm\_hl7800\_gnss\_status

**Definition** hl7800.h:186

[HL7800\_GNSS\_STATUS\_FAILURE](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625a830898a215c51c8a17aab3fb175083b3)

@ HL7800\_GNSS\_STATUS\_FAILURE

**Definition** hl7800.h:188

[HL7800\_GNSS\_STATUS\_INVALID](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625aadc2b5c2e8b257e8b12ae7c4f5f35d76)

@ HL7800\_GNSS\_STATUS\_INVALID

**Definition** hl7800.h:187

[HL7800\_GNSS\_STATUS\_SUCCESS](hl7800_8h.md#a5253bceab7f3da57f9a2d3918ee72625ab989ec2e119be4f23a37cac5203225ab)

@ HL7800\_GNSS\_STATUS\_SUCCESS

**Definition** hl7800.h:189

[mdm\_hl7800\_get\_imsi](hl7800_8h.md#a581582e3f7b07f04e6b33e481e2d6e42)

char \* mdm\_hl7800\_get\_imsi(void)

Get the IMSI.

[mdm\_hl7800\_gnss\_event](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043b)

mdm\_hl7800\_gnss\_event

**Definition** hl7800.h:178

[HL7800\_GNSS\_EVENT\_POSITION](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba2df7e19144b20afb4bf3566804729db1)

@ HL7800\_GNSS\_EVENT\_POSITION

**Definition** hl7800.h:183

[HL7800\_GNSS\_EVENT\_INVALID](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba3349e6599deabd375c68bb3688bd9bfd)

@ HL7800\_GNSS\_EVENT\_INVALID

**Definition** hl7800.h:179

[HL7800\_GNSS\_EVENT\_INIT](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba3b0b73d5b585d4ed44e00504be60c8ef)

@ HL7800\_GNSS\_EVENT\_INIT

**Definition** hl7800.h:180

[HL7800\_GNSS\_EVENT\_START](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043ba689418f8d35440fe71507ee871f20de1)

@ HL7800\_GNSS\_EVENT\_START

**Definition** hl7800.h:181

[HL7800\_GNSS\_EVENT\_STOP](hl7800_8h.md#a5b6a53d0353ae153f715163ca4e6043bae83741a25baa0ffc3837b0653b01c318)

@ HL7800\_GNSS\_EVENT\_STOP

**Definition** hl7800.h:182

[MDM\_HL7800\_APN\_MAX\_SIZE](hl7800_8h.md#a5cc5aad6ab04405999246790dd850046)

#define MDM\_HL7800\_APN\_MAX\_SIZE

**Definition** hl7800.h:35

[mdm\_hl7800\_network\_state](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773)

mdm\_hl7800\_network\_state

**Definition** hl7800.h:132

[HL7800\_EMERGENCY](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a04cac2efa21c949edeefc105effa4a39)

@ HL7800\_EMERGENCY

**Definition** hl7800.h:139

[HL7800\_SEARCHING](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a1ad9a81e5ce65dc6eee98a87f880f86a)

@ HL7800\_SEARCHING

**Definition** hl7800.h:135

[HL7800\_UNABLE\_TO\_CONFIGURE](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a2502129bf7729cce4b1b96ac66dfdd86)

@ HL7800\_UNABLE\_TO\_CONFIGURE

**Definition** hl7800.h:141

[HL7800\_REGISTRATION\_DENIED](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a4eeb75667b400acaff56ad282bfe6a7c)

@ HL7800\_REGISTRATION\_DENIED

**Definition** hl7800.h:136

[HL7800\_HOME\_NETWORK](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a7e5bdc7f85c2d2f6ec62beee156e887d)

@ HL7800\_HOME\_NETWORK

**Definition** hl7800.h:134

[HL7800\_NOT\_REGISTERED](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a94fe4bdd729ba6df15d9e9aa53998599)

@ HL7800\_NOT\_REGISTERED

**Definition** hl7800.h:133

[HL7800\_ROAMING](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773a9d7e014131f399f000965803ccb5e889)

@ HL7800\_ROAMING

**Definition** hl7800.h:138

[HL7800\_OUT\_OF\_COVERAGE](hl7800_8h.md#a65c8ed3a7c2a2aee39ca65e57f33b773ae3f6d693bbe0d0c09a41a0e013fe5a82)

@ HL7800\_OUT\_OF\_COVERAGE

**Definition** hl7800.h:137

[mdm\_hl7800\_log\_filter\_set](hl7800_8h.md#a838f6aab78e6f41028d381823cb6b118)

uint32\_t mdm\_hl7800\_log\_filter\_set(uint32\_t level)

Set the log level for the modem.

[mdm\_hl7800\_polte\_register](hl7800_8h.md#a8501f6d4883ee8577b5cda0f76d2a3dc)

int32\_t mdm\_hl7800\_polte\_register(void)

Register modem/SIM with polte.io.

[mdm\_hl7800\_fota\_state](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3)

mdm\_hl7800\_fota\_state

**Definition** hl7800.h:152

[HL7800\_FOTA\_PAD](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a481fdc3814098383af7b593d4f61ea7b)

@ HL7800\_FOTA\_PAD

**Definition** hl7800.h:156

[HL7800\_FOTA\_REBOOT\_AND\_RECONFIGURE](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a5e517d07a386297b5d80110cabc1864b)

@ HL7800\_FOTA\_REBOOT\_AND\_RECONFIGURE

**Definition** hl7800.h:160

[HL7800\_FOTA\_INSTALL](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a6761ef6c52c40786c8b595950499851e)

@ HL7800\_FOTA\_INSTALL

**Definition** hl7800.h:159

[HL7800\_FOTA\_WIP](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3a722b66bd586cc4375253341f1df8d189)

@ HL7800\_FOTA\_WIP

**Definition** hl7800.h:155

[HL7800\_FOTA\_SEND\_EOT](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3aa78ef13656312bb81aa957a515b337d7)

@ HL7800\_FOTA\_SEND\_EOT

**Definition** hl7800.h:157

[HL7800\_FOTA\_FILE\_ERROR](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3aaf2423203fdb79510efa9550e2a09bf9)

@ HL7800\_FOTA\_FILE\_ERROR

**Definition** hl7800.h:158

[HL7800\_FOTA\_IDLE](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3ab7d67051e56e05be47da306377bb8801)

@ HL7800\_FOTA\_IDLE

**Definition** hl7800.h:153

[HL7800\_FOTA\_COMPLETE](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3abd185b07f408b4b7ecb292f31aa6d19a)

@ HL7800\_FOTA\_COMPLETE

**Definition** hl7800.h:161

[HL7800\_FOTA\_START](hl7800_8h.md#a8ed2ea65436083a9b1a49bb1f64574f3ae6b160137651a7375551760f938b9da8)

@ HL7800\_FOTA\_START

**Definition** hl7800.h:154

[mdm\_hl7800\_set\_bands](hl7800_8h.md#a935e3010e0a2d633e366711c09f634f1)

int32\_t mdm\_hl7800\_set\_bands(const char \*bands)

Set the bands available for the LTE connection.

[mdm\_hl7800\_reset](hl7800_8h.md#a956932a3c7d45f5ab0c3c99aa1decfb4)

int32\_t mdm\_hl7800\_reset(void)

Reset the HL7800 (and allow it to reconfigure).

[mdm\_hl7800\_perform\_site\_survey](hl7800_8h.md#a975a4cd75d9d89dd23b182af2376ef91)

int32\_t mdm\_hl7800\_perform\_site\_survey(void)

Perform a site survey.

[mdm\_hl7800\_update\_rat](hl7800_8h.md#a9d295b105e71346fcb283959d2641079)

int32\_t mdm\_hl7800\_update\_rat(enum mdm\_hl7800\_radio\_mode value)

Update the Radio Access Technology (mode).

[mdm\_hl7800\_generate\_status\_events](hl7800_8h.md#aaac620a4653d772f4d44a73834a8b4cc)

void mdm\_hl7800\_generate\_status\_events(void)

Force modem module to generate status events.

[MDM\_HL7800\_APN\_PASSWORD\_MAX\_SIZE](hl7800_8h.md#abc1a2d9744225bc82f3f4b14d365a0fe)

#define MDM\_HL7800\_APN\_PASSWORD\_MAX\_SIZE

**Definition** hl7800.h:37

[mdm\_hl7800\_get\_fw\_version](hl7800_8h.md#ac65dc452be996e5366360abb314a4d98)

char \* mdm\_hl7800\_get\_fw\_version(void)

Get the HL7800 firmware version.

[MDM\_HL7800\_APN\_USERNAME\_MAX\_SIZE](hl7800_8h.md#acb5d0f96845b17b84c746dcea6bd732a)

#define MDM\_HL7800\_APN\_USERNAME\_MAX\_SIZE

**Definition** hl7800.h:36

[mdm\_hl7800\_get\_signal\_quality](hl7800_8h.md#ad7d20cde62d5e7c987672cc9c10b152e)

void mdm\_hl7800\_get\_signal\_quality(int \*rsrp, int \*sinr)

Get the signal quality of the HL7800.

[mdm\_hl7800\_unregister\_event\_callback](hl7800_8h.md#ae2015e7399a17a862048eed89b036c6d)

int mdm\_hl7800\_unregister\_event\_callback(struct mdm\_hl7800\_callback\_agent \*agent)

Unregister a callback event function.

[mdm\_hl7800\_power\_off](hl7800_8h.md#ae270849872a22823512cc87b0bbf877e)

int32\_t mdm\_hl7800\_power\_off(void)

Power off the HL7800.

[mdm\_hl7800\_register\_cts\_callback](hl7800_8h.md#aead5a1419d87676f13fdea12f705b125)

void mdm\_hl7800\_register\_cts\_callback(void(\*func)(int state))

Allows mapping of UART1\_CTS signal to a user accessible test point on the development board.

[mdm\_hl7800\_gnss\_position\_event](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696b)

mdm\_hl7800\_gnss\_position\_event

**Definition** hl7800.h:192

[HL7800\_GNSS\_POSITION\_EVENT\_2D\_AVAILABLE](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696ba1cf9c2fe042ab784450451f36b83818d)

@ HL7800\_GNSS\_POSITION\_EVENT\_2D\_AVAILABLE

**Definition** hl7800.h:196

[HL7800\_GNSS\_POSITION\_EVENT\_3D\_AVAILABLE](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696ba6bd45fa147597e9c278ec0f27c42efc7)

@ HL7800\_GNSS\_POSITION\_EVENT\_3D\_AVAILABLE

**Definition** hl7800.h:197

[HL7800\_GNSS\_POSITION\_EVENT\_FIXED\_TO\_INVALID](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696ba9822e7c1f4a238658592a539d18d0c6d)

@ HL7800\_GNSS\_POSITION\_EVENT\_FIXED\_TO\_INVALID

**Definition** hl7800.h:198

[HL7800\_GNSS\_POSITION\_EVENT\_INVALID](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696babf5377809190c648e6f3624b4b0b82ee)

@ HL7800\_GNSS\_POSITION\_EVENT\_INVALID

**Definition** hl7800.h:193

[HL7800\_GNSS\_POSITION\_EVENT\_LOST\_OR\_NOT\_AVAILABLE\_YET](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696bac41b513dd45d2d038b9d7a4a9bae8fe3)

@ HL7800\_GNSS\_POSITION\_EVENT\_LOST\_OR\_NOT\_AVAILABLE\_YET

**Definition** hl7800.h:194

[HL7800\_GNSS\_POSITION\_EVENT\_PREDICTION\_AVAILABLE](hl7800_8h.md#aec06e58e1c79e23577d424806b6e696bad41adce29331d1917c97e94b6409a9b5)

@ HL7800\_GNSS\_POSITION\_EVENT\_PREDICTION\_AVAILABLE

**Definition** hl7800.h:195

[mdm\_hl7800\_startup\_state](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99)

mdm\_hl7800\_startup\_state

**Definition** hl7800.h:122

[HL7800\_STARTUP\_STATE\_SIMLOCK](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a098e678b80c7148972d572f6dac763d6)

@ HL7800\_STARTUP\_STATE\_SIMLOCK

**Definition** hl7800.h:126

[HL7800\_STARTUP\_STATE\_UNRECOVERABLE\_ERROR](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a1b88f9edf57f6fe1b9f4b31ecb196632)

@ HL7800\_STARTUP\_STATE\_UNRECOVERABLE\_ERROR

**Definition** hl7800.h:127

[HL7800\_STARTUP\_STATE\_WAITING\_FOR\_ACCESS\_CODE](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a60dd736ae85eeafaefce839b623c530f)

@ HL7800\_STARTUP\_STATE\_WAITING\_FOR\_ACCESS\_CODE

**Definition** hl7800.h:124

[HL7800\_STARTUP\_STATE\_SIM\_NOT\_PRESENT](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a92593373e0efcb87471c6d0325f1c2e6)

@ HL7800\_STARTUP\_STATE\_SIM\_NOT\_PRESENT

**Definition** hl7800.h:125

[HL7800\_STARTUP\_STATE\_INACTIVE\_SIM](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a9999f1a90165d5996a7a2ff415db53d6)

@ HL7800\_STARTUP\_STATE\_INACTIVE\_SIM

**Definition** hl7800.h:129

[HL7800\_STARTUP\_STATE\_UNKNOWN](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99a9d2a5fd088822989fc109cb3add31393)

@ HL7800\_STARTUP\_STATE\_UNKNOWN

**Definition** hl7800.h:128

[HL7800\_STARTUP\_STATE\_READY](hl7800_8h.md#aefcf9c39983d8f3f58bcd1a24ca04e99aac2ef169e3273dd11331acae3abb9c6e)

@ HL7800\_STARTUP\_STATE\_READY

**Definition** hl7800.h:123

[mdm\_hl7800\_get\_iccid](hl7800_8h.md#af84e782e572faf543a37a40147660eb0)

char \* mdm\_hl7800\_get\_iccid(void)

Get the SIM card ICCID.

[mdm\_hl7800\_functionality](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2)

mdm\_hl7800\_functionality

**Definition** hl7800.h:164

[HL7800\_FUNCTIONALITY\_AIRPLANE](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2a2aca52c7dc8ade5db478f8eaebc4bc33)

@ HL7800\_FUNCTIONALITY\_AIRPLANE

**Definition** hl7800.h:167

[HL7800\_FUNCTIONALITY\_FULL](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2ad1e22b662121c8c71b9d34810958b6c2)

@ HL7800\_FUNCTIONALITY\_FULL

**Definition** hl7800.h:166

[HL7800\_FUNCTIONALITY\_MINIMUM](hl7800_8h.md#af999018ef3ca438a9d3cb7b6611300d2ae2c5fac661bdf514debc98b3e248cea4)

@ HL7800\_FUNCTIONALITY\_MINIMUM

**Definition** hl7800.h:165

[mdm\_hl7800\_event\_callback\_t](hl7800_8h.md#afa044d03d9bfbc2f63088da4f094edfc)

void(\* mdm\_hl7800\_event\_callback\_t)(enum mdm\_hl7800\_event event, void \*event\_data)

event - The type of event event\_data - Pointer to event specific data structure: HL7800\_EVENT\_NETWORK...

**Definition** hl7800.h:257

[mdm\_hl7800\_get\_local\_time](hl7800_8h.md#afa95fa49240c3412521bade1245bc573)

int32\_t mdm\_hl7800\_get\_local\_time(struct tm \*tm, int32\_t \*offset)

Get the local time from the modem's real time clock.

[mdm\_hl7800\_register\_event\_callback](hl7800_8h.md#afab74f2bd3806a23192cae18f65226ad)

int mdm\_hl7800\_register\_event\_callback(struct mdm\_hl7800\_callback\_agent \*agent)

Register a function that is called when a modem event occurs.

[types.h](include_2zephyr_2types_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[mdm\_hl7800\_apn](structmdm__hl7800__apn.md)

**Definition** hl7800.h:51

[mdm\_hl7800\_apn::value](structmdm__hl7800__apn.md#a37f48ac1e950f0df59d07a6a83bb5cc9)

char value[64]

**Definition** hl7800.h:52

[mdm\_hl7800\_apn::password](structmdm__hl7800__apn.md#a876db3a5fdf4ce805536d84b96213495)

char password[65]

**Definition** hl7800.h:54

[mdm\_hl7800\_apn::username](structmdm__hl7800__apn.md#abfe087e7989513937c43a28dd83deb21)

char username[65]

**Definition** hl7800.h:53

[mdm\_hl7800\_callback\_agent](structmdm__hl7800__callback__agent.md)

**Definition** hl7800.h:260

[mdm\_hl7800\_callback\_agent::node](structmdm__hl7800__callback__agent.md#a5b69a3952ee320ee88fd99220bac3ef5)

sys\_snode\_t node

**Definition** hl7800.h:261

[mdm\_hl7800\_callback\_agent::event\_callback](structmdm__hl7800__callback__agent.md#adb1eb808c084c9afb6077b04aa1bb026)

mdm\_hl7800\_event\_callback\_t event\_callback

**Definition** hl7800.h:262

[mdm\_hl7800\_compound\_event](structmdm__hl7800__compound__event.md)

**Definition** hl7800.h:173

[mdm\_hl7800\_compound\_event::string](structmdm__hl7800__compound__event.md#a014d5de10c32177e4dd3fb011a0793d5)

char \* string

**Definition** hl7800.h:175

[mdm\_hl7800\_compound\_event::code](structmdm__hl7800__compound__event.md#abf3581062c802a15f71c250c56609aaf)

uint8\_t code

**Definition** hl7800.h:174

[mdm\_hl7800\_polte\_location\_data](structmdm__hl7800__polte__location__data.md)

**Definition** hl7800.h:226

[mdm\_hl7800\_polte\_location\_data::status](structmdm__hl7800__polte__location__data.md#a3a95fb87ddf47eb9d447b9dd0da92cf3)

int status

**Definition** hl7800.h:228

[mdm\_hl7800\_polte\_location\_data::confidence\_in\_meters](structmdm__hl7800__polte__location__data.md#a479ebd4268c0138138d62818b96a1593)

char confidence\_in\_meters[33]

**Definition** hl7800.h:231

[mdm\_hl7800\_polte\_location\_data::longitude](structmdm__hl7800__polte__location__data.md#a5114024090c7d039d63219495d9fd343)

char longitude[33]

**Definition** hl7800.h:230

[mdm\_hl7800\_polte\_location\_data::timestamp](structmdm__hl7800__polte__location__data.md#aaae6d4f0ff600f595bad143166f5605c)

uint32\_t timestamp

**Definition** hl7800.h:227

[mdm\_hl7800\_polte\_location\_data::latitude](structmdm__hl7800__polte__location__data.md#adc4a7aee1014c0290294240bd968e232)

char latitude[33]

**Definition** hl7800.h:229

[mdm\_hl7800\_polte\_registration\_event\_data](structmdm__hl7800__polte__registration__event__data.md)

**Definition** hl7800.h:217

[mdm\_hl7800\_polte\_registration\_event\_data::status](structmdm__hl7800__polte__registration__event__data.md#a1d591b3a469fb6fed674fb07455ed8d0)

int status

**Definition** hl7800.h:218

[mdm\_hl7800\_polte\_registration\_event\_data::password](structmdm__hl7800__polte__registration__event__data.md#ad551f94f2488544e69f622d7d26f87d9)

char \* password

**Definition** hl7800.h:220

[mdm\_hl7800\_polte\_registration\_event\_data::user](structmdm__hl7800__polte__registration__event__data.md#adc8d2cee46aae9ed0736d85ab5805cb0)

char \* user

**Definition** hl7800.h:219

[mdm\_hl7800\_site\_survey](structmdm__hl7800__site__survey.md)

**Definition** hl7800.h:85

[mdm\_hl7800\_site\_survey::rsrq](structmdm__hl7800__site__survey.md#a4517603844797cc6e46d96b1773c78c7)

int rsrq

**Definition** hl7800.h:89

[mdm\_hl7800\_site\_survey::rsrp](structmdm__hl7800__site__survey.md#a725a5a647c999bbae2da828eaee481cf)

int rsrp

**Definition** hl7800.h:88

[mdm\_hl7800\_site\_survey::cell\_id](structmdm__hl7800__site__survey.md#a9e8ec0ba55bc7686e0b4b093d9057179)

uint32\_t cell\_id

**Definition** hl7800.h:87

[mdm\_hl7800\_site\_survey::earfcn](structmdm__hl7800__site__survey.md#aa22e2191ac864718a097fa674dc1adc8)

uint32\_t earfcn

**Definition** hl7800.h:86

[tm](structtm.md)

**Definition** time.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [modem](dir_921fc901d44f7fec5fdbf8b941e64fce.md)
- [hl7800.h](hl7800_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
