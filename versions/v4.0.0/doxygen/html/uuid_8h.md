---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/uuid_8h.html
original_path: doxygen/html/uuid_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uuid.h File Reference

Bluetooth UUID handling.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/bluetooth/byteorder.h](bluetooth_2byteorder_8h_source.md)>`

[Go to the source code of this file.](uuid_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_uuid](structbt__uuid.md) |
|  | This is a 'tentative' type and should be used as a pointer only. [More...](structbt__uuid.md#details) |
| struct | [bt\_uuid\_16](structbt__uuid__16.md) |
| struct | [bt\_uuid\_32](structbt__uuid__32.md) |
| struct | [bt\_uuid\_128](structbt__uuid__128.md) |

| Macros | |
| --- | --- |
| #define | [BT\_UUID\_SIZE\_16](group__bt__uuid.md#ga9d3506fd135b5cd8763446f572c161da)   2 |
|  | Size in octets of a 16-bit UUID. |
| #define | [BT\_UUID\_SIZE\_32](group__bt__uuid.md#gaf35f2e5054bfcc81985e90b8ef659fd9)   4 |
|  | Size in octets of a 32-bit UUID. |
| #define | [BT\_UUID\_SIZE\_128](group__bt__uuid.md#ga86fdce8e63c0f8208bea6b0f2584eb67)   16 |
|  | Size in octets of a 128-bit UUID. |
| #define | [BT\_UUID\_INIT\_16](group__bt__uuid.md#gab7c9f80628c5fb1b5d1c09d18a1baff7)(value) |
|  | Initialize a 16-bit UUID. |
| #define | [BT\_UUID\_INIT\_32](group__bt__uuid.md#ga207ff52ebf1eea1c487fff3d840a38f8)(value) |
|  | Initialize a 32-bit UUID. |
| #define | [BT\_UUID\_INIT\_128](group__bt__uuid.md#ga1a840adf4bc06cf2cd5dbeb0c868374b)(value...) |
|  | Initialize a 128-bit UUID. |
| #define | [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)(value) |
|  | Helper to declare a 16-bit UUID inline. |
| #define | [BT\_UUID\_DECLARE\_32](group__bt__uuid.md#ga945448449c57b4800e25a363e7d4d1cc)(value) |
|  | Helper to declare a 32-bit UUID inline. |
| #define | [BT\_UUID\_DECLARE\_128](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)(value...) |
|  | Helper to declare a 128-bit UUID inline. |
| #define | [BT\_UUID\_16](group__bt__uuid.md#ga7466cf356741d6348f332653a385fd01)(\_\_u) |
|  | Helper macro to access the 16-bit UUID from a generic UUID. |
| #define | [BT\_UUID\_32](group__bt__uuid.md#gacc77f082e8dac620672676ed8d005504)(\_\_u) |
|  | Helper macro to access the 32-bit UUID from a generic UUID. |
| #define | [BT\_UUID\_128](group__bt__uuid.md#ga931a0d5eb23537be31408c787fd8b48d)(\_\_u) |
|  | Helper macro to access the 128-bit UUID from a generic UUID. |
| #define | [BT\_UUID\_128\_ENCODE](group__bt__uuid.md#gac3973b66e992cbc0940752b77b378f43)(w32, w1, w2, w3, w48) |
|  | Encode 128 bit UUID into array values in little-endian format. |
| #define | [BT\_UUID\_16\_ENCODE](group__bt__uuid.md#ga16e057af1bb2f1c11e74b50bfd490586)(w16) |
|  | Encode 16-bit UUID into array values in little-endian format. |
| #define | [BT\_UUID\_32\_ENCODE](group__bt__uuid.md#gad5294c1c19c66b20321c88939a8849bf)(w32) |
|  | Encode 32-bit UUID into array values in little-endian format. |
| #define | [BT\_UUID\_STR\_LEN](group__bt__uuid.md#gaf9a36381128454102c558568dfd5d029)   37 |
|  | Recommended length of user string buffer for Bluetooth UUID. |
| #define | [BT\_UUID\_GAP\_VAL](group__bt__uuid.md#gaaf6715d89ba70a057949e636fb2368dd)   0x1800 |
|  | Generic Access UUID value. |
| #define | [BT\_UUID\_GAP](group__bt__uuid.md#gae8b61f07e6732ffb876318045b5803c4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GAP\_VAL](group__bt__uuid.md#gaaf6715d89ba70a057949e636fb2368dd)) |
|  | Generic Access. |
| #define | [BT\_UUID\_GATT\_VAL](group__bt__uuid.md#gad893036bda14523c3e35ff66d23bacb2)   0x1801 |
|  | Generic attribute UUID value. |
| #define | [BT\_UUID\_GATT](group__bt__uuid.md#ga18f210e4e60b9fdd80d9d68f007b0728)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_VAL](group__bt__uuid.md#gad893036bda14523c3e35ff66d23bacb2)) |
|  | Generic Attribute. |
| #define | [BT\_UUID\_IAS\_VAL](group__bt__uuid.md#ga637aece6581426d8d5d7b9aeb546a67e)   0x1802 |
|  | Immediate Alert Service UUID value. |
| #define | [BT\_UUID\_IAS](group__bt__uuid.md#ga9d99491d2957912ab80e2636d6ac7416)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_IAS\_VAL](group__bt__uuid.md#ga637aece6581426d8d5d7b9aeb546a67e)) |
|  | Immediate Alert Service. |
| #define | [BT\_UUID\_LLS\_VAL](group__bt__uuid.md#ga1b868ca21fa47aba88601f71eb8ad1d5)   0x1803 |
|  | Link Loss Service UUID value. |
| #define | [BT\_UUID\_LLS](group__bt__uuid.md#ga6bdab3bba88af7187eb50b7817cc317e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_LLS\_VAL](group__bt__uuid.md#ga1b868ca21fa47aba88601f71eb8ad1d5)) |
|  | Link Loss Service. |
| #define | [BT\_UUID\_TPS\_VAL](group__bt__uuid.md#gab8d79e7553b418eae94b9d790d9a422e)   0x1804 |
|  | Tx Power Service UUID value. |
| #define | [BT\_UUID\_TPS](group__bt__uuid.md#ga2e250a6880be716f98e668ab26dcdac3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TPS\_VAL](group__bt__uuid.md#gab8d79e7553b418eae94b9d790d9a422e)) |
|  | Tx Power Service. |
| #define | [BT\_UUID\_CTS\_VAL](group__bt__uuid.md#ga264f3b58d4e3bee6a7533acf0670206d)   0x1805 |
|  | Current Time Service UUID value. |
| #define | [BT\_UUID\_CTS](group__bt__uuid.md#ga8c2c089f4cc458c0f4a5a7506c21a6f9)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CTS\_VAL](group__bt__uuid.md#ga264f3b58d4e3bee6a7533acf0670206d)) |
|  | Current Time Service. |
| #define | [BT\_UUID\_RTUS\_VAL](group__bt__uuid.md#ga13300d9d1074fd90a65233357dd9ad60)   0x1806 |
|  | Reference Time Update Service UUID value. |
| #define | [BT\_UUID\_RTUS](group__bt__uuid.md#ga52c98d18473e61c581f0cab4839defa8)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_RTUS\_VAL](group__bt__uuid.md#ga13300d9d1074fd90a65233357dd9ad60)) |
|  | Reference Time Update Service. |
| #define | [BT\_UUID\_NDSTS\_VAL](group__bt__uuid.md#ga0396837f73209e12bc6d11c64a3a6d67)   0x1807 |
|  | Next DST Change Service UUID value. |
| #define | [BT\_UUID\_NDSTS](group__bt__uuid.md#ga3a4f846cbf5dd4fccec26be00506a61c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_NDSTS\_VAL](group__bt__uuid.md#ga0396837f73209e12bc6d11c64a3a6d67)) |
|  | Next DST Change Service. |
| #define | [BT\_UUID\_GS\_VAL](group__bt__uuid.md#gab31578ab529cf755ec611c491a3676ac)   0x1808 |
|  | Glucose Service UUID value. |
| #define | [BT\_UUID\_GS](group__bt__uuid.md#gac1f5583a48b80fab9d05546d87cb6de0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GS\_VAL](group__bt__uuid.md#gab31578ab529cf755ec611c491a3676ac)) |
|  | Glucose Service. |
| #define | [BT\_UUID\_HTS\_VAL](group__bt__uuid.md#ga3caec4c6564711a2959ffadcf5598011)   0x1809 |
|  | Health Thermometer Service UUID value. |
| #define | [BT\_UUID\_HTS](group__bt__uuid.md#gabffa5a0a0a57cfd330a8bef348c2c2ee)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTS\_VAL](group__bt__uuid.md#ga3caec4c6564711a2959ffadcf5598011)) |
|  | Health Thermometer Service. |
| #define | [BT\_UUID\_DIS\_VAL](group__bt__uuid.md#ga3eaf1d7bfeb9b9375e1e2b4ba7f23aed)   0x180a |
|  | Device Information Service UUID value. |
| #define | [BT\_UUID\_DIS](group__bt__uuid.md#ga03ea74768fa1e69dad54cffe9eeeee31)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DIS\_VAL](group__bt__uuid.md#ga3eaf1d7bfeb9b9375e1e2b4ba7f23aed)) |
|  | Device Information Service. |
| #define | [BT\_UUID\_NAS\_VAL](group__bt__uuid.md#ga66870ecd34acfee828d55f63167b7e67)   0x180b |
|  | Network Availability Service UUID value. |
| #define | [BT\_UUID\_NAS](group__bt__uuid.md#ga92af25a46ae1b534fa248fd0516278cb)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_NAS\_VAL](group__bt__uuid.md#ga66870ecd34acfee828d55f63167b7e67)) |
|  | Network Availability Service. |
| #define | [BT\_UUID\_WDS\_VAL](group__bt__uuid.md#ga110066c42ffc45bf86a9c90528aeb2e7)   0x180c |
|  | Watchdog Service UUID value. |
| #define | [BT\_UUID\_WDS](group__bt__uuid.md#ga7c501f33b29907d48dd31ed70eeb67d4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_WDS\_VAL](group__bt__uuid.md#ga110066c42ffc45bf86a9c90528aeb2e7)) |
|  | Watchdog Service. |
| #define | [BT\_UUID\_HRS\_VAL](group__bt__uuid.md#ga912cb91295d110813a3db0144c95551d)   0x180d |
|  | Heart Rate Service UUID value. |
| #define | [BT\_UUID\_HRS](group__bt__uuid.md#ga17893ceaa9bc20640d4ecdeabe9beb28)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HRS\_VAL](group__bt__uuid.md#ga912cb91295d110813a3db0144c95551d)) |
|  | Heart Rate Service. |
| #define | [BT\_UUID\_PAS\_VAL](group__bt__uuid.md#gaea47ecf9bc957d813312a188a701db54)   0x180e |
|  | Phone Alert Service UUID value. |
| #define | [BT\_UUID\_PAS](group__bt__uuid.md#gadd5233cc3cb516f8b7fb192d6c64bcad)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_PAS\_VAL](group__bt__uuid.md#gaea47ecf9bc957d813312a188a701db54)) |
|  | Phone Alert Service. |
| #define | [BT\_UUID\_BAS\_VAL](group__bt__uuid.md#ga2ff64c18d7f8dae8a328b52f486161c4)   0x180f |
|  | Battery Service UUID value. |
| #define | [BT\_UUID\_BAS](group__bt__uuid.md#gabc55390a1144b556477df555e76848ab)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAS\_VAL](group__bt__uuid.md#ga2ff64c18d7f8dae8a328b52f486161c4)) |
|  | Battery Service. |
| #define | [BT\_UUID\_BPS\_VAL](group__bt__uuid.md#ga2ff98d3bfd27cba7eb99c62dfb31a6fd)   0x1810 |
|  | Blood Pressure Service UUID value. |
| #define | [BT\_UUID\_BPS](group__bt__uuid.md#ga97ed88c10cdc3f1c32c4e53d260eaa3e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BPS\_VAL](group__bt__uuid.md#ga2ff98d3bfd27cba7eb99c62dfb31a6fd)) |
|  | Blood Pressure Service. |
| #define | [BT\_UUID\_ANS\_VAL](group__bt__uuid.md#ga0c6ee900cba57e40f8b3681e1ea404c7)   0x1811 |
|  | Alert Notification Service UUID value. |
| #define | [BT\_UUID\_ANS](group__bt__uuid.md#ga7a208b147e3b35857c72ba8f8db22d62)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ANS\_VAL](group__bt__uuid.md#ga0c6ee900cba57e40f8b3681e1ea404c7)) |
|  | Alert Notification Service. |
| #define | [BT\_UUID\_HIDS\_VAL](group__bt__uuid.md#ga2bf2ec6082e31f397dec6634cda56bbb)   0x1812 |
|  | HID Service UUID value. |
| #define | [BT\_UUID\_HIDS](group__bt__uuid.md#ga74e91eef3e2dcbb4499a0f70f3b479d4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDS\_VAL](group__bt__uuid.md#ga2bf2ec6082e31f397dec6634cda56bbb)) |
|  | HID Service. |
| #define | [BT\_UUID\_SPS\_VAL](group__bt__uuid.md#ga73e7ff27e935868fa86c9d38e186e405)   0x1813 |
|  | Scan Parameters Service UUID value. |
| #define | [BT\_UUID\_SPS](group__bt__uuid.md#ga7599a7a3cdc6a32c60862618b6b70327)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_SPS\_VAL](group__bt__uuid.md#ga73e7ff27e935868fa86c9d38e186e405)) |
|  | Scan Parameters Service. |
| #define | [BT\_UUID\_RSCS\_VAL](group__bt__uuid.md#gad35b23e0814f0f74c3a33587f7922966)   0x1814 |
|  | Running Speed and Cadence Service UUID value. |
| #define | [BT\_UUID\_RSCS](group__bt__uuid.md#ga40a6402510b5c71b0eca5b2f7a914085)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_RSCS\_VAL](group__bt__uuid.md#gad35b23e0814f0f74c3a33587f7922966)) |
|  | Running Speed and Cadence Service. |
| #define | [BT\_UUID\_AIOS\_VAL](group__bt__uuid.md#ga4449d49abf6fed72da52b14a967aec4d)   0x1815 |
|  | Automation IO Service UUID value. |
| #define | [BT\_UUID\_AIOS](group__bt__uuid.md#gaaa73f77971aad79900e18fd58d12ea22)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_AIOS\_VAL](group__bt__uuid.md#ga4449d49abf6fed72da52b14a967aec4d)) |
|  | Automation IO Service. |
| #define | [BT\_UUID\_CSC\_VAL](group__bt__uuid.md#ga4d31b6944d378bcda7c8f7bfc74c5692)   0x1816 |
|  | Cycling Speed and Cadence Service UUID value. |
| #define | [BT\_UUID\_CSC](group__bt__uuid.md#ga6514fa0098d12c02aa34c18e1e5a6396)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CSC\_VAL](group__bt__uuid.md#ga4d31b6944d378bcda7c8f7bfc74c5692)) |
|  | Cycling Speed and Cadence Service. |
| #define | [BT\_UUID\_CPS\_VAL](group__bt__uuid.md#gab063c1e5d2773927ce54c1745c7134d4)   0x1818 |
|  | Cycling Power Service UUID value. |
| #define | [BT\_UUID\_CPS](group__bt__uuid.md#gac3c2895467ba651b8ebad709fdd44f6d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CPS\_VAL](group__bt__uuid.md#gab063c1e5d2773927ce54c1745c7134d4)) |
|  | Cycling Power Service. |
| #define | [BT\_UUID\_LNS\_VAL](group__bt__uuid.md#ga36161c4e68b691cfb6a9f691a8f693dd)   0x1819 |
|  | Location and Navigation Service UUID value. |
| #define | [BT\_UUID\_LNS](group__bt__uuid.md#gac48ea20cb0503dd748862862157e9224)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_LNS\_VAL](group__bt__uuid.md#ga36161c4e68b691cfb6a9f691a8f693dd)) |
|  | Location and Navigation Service. |
| #define | [BT\_UUID\_ESS\_VAL](group__bt__uuid.md#ga8e8d24d0bf0a49713bbfa93cc2bdb0da)   0x181a |
|  | Environmental Sensing Service UUID value. |
| #define | [BT\_UUID\_ESS](group__bt__uuid.md#ga96c5958372c4fdba211b4f74d342a5b3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ESS\_VAL](group__bt__uuid.md#ga8e8d24d0bf0a49713bbfa93cc2bdb0da)) |
|  | Environmental Sensing Service. |
| #define | [BT\_UUID\_BCS\_VAL](group__bt__uuid.md#ga69baa896cd558487733cd575a6193e0d)   0x181b |
|  | Body Composition Service UUID value. |
| #define | [BT\_UUID\_BCS](group__bt__uuid.md#ga08170da6b471e937f64de6943b6e24bb)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BCS\_VAL](group__bt__uuid.md#ga69baa896cd558487733cd575a6193e0d)) |
|  | Body Composition Service. |
| #define | [BT\_UUID\_UDS\_VAL](group__bt__uuid.md#ga035ee545fdd640745b3bcbd8b7e7b3b6)   0x181c |
|  | User Data Service UUID value. |
| #define | [BT\_UUID\_UDS](group__bt__uuid.md#gac6edbd84e5f0b454e130f835a32f1a44)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_UDS\_VAL](group__bt__uuid.md#ga035ee545fdd640745b3bcbd8b7e7b3b6)) |
|  | User Data Service. |
| #define | [BT\_UUID\_WSS\_VAL](group__bt__uuid.md#ga6b6566f914d2c92c9b1bb4efd6efee98)   0x181d |
|  | Weight Scale Service UUID value. |
| #define | [BT\_UUID\_WSS](group__bt__uuid.md#gaa5c518578e2620aafad915a0291dfe8f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_WSS\_VAL](group__bt__uuid.md#ga6b6566f914d2c92c9b1bb4efd6efee98)) |
|  | Weight Scale Service. |
| #define | [BT\_UUID\_BMS\_VAL](group__bt__uuid.md#ga399ffbd6e7d3e50010383f2d521d8089)   0x181e |
|  | Bond Management Service UUID value. |
| #define | [BT\_UUID\_BMS](group__bt__uuid.md#ga0a91114bf5e53c894d10d1e432223714)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BMS\_VAL](group__bt__uuid.md#ga399ffbd6e7d3e50010383f2d521d8089)) |
|  | Bond Management Service. |
| #define | [BT\_UUID\_CGMS\_VAL](group__bt__uuid.md#ga9726266ed3399a646999e19f639457a7)   0x181f |
|  | Continuous Glucose Monitoring Service UUID value. |
| #define | [BT\_UUID\_CGMS](group__bt__uuid.md#ga04767d3a7461b3508bce584704d92c75)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CGMS\_VAL](group__bt__uuid.md#ga9726266ed3399a646999e19f639457a7)) |
|  | Continuous Glucose Monitoring Service. |
| #define | [BT\_UUID\_IPSS\_VAL](group__bt__uuid.md#gad8cc687442abd5eea3e367d2b859e2e8)   0x1820 |
|  | IP Support Service UUID value. |
| #define | [BT\_UUID\_IPSS](group__bt__uuid.md#ga32f10a8bfb452aee43c64eec3c2d5a0f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_IPSS\_VAL](group__bt__uuid.md#gad8cc687442abd5eea3e367d2b859e2e8)) |
|  | IP Support Service. |
| #define | [BT\_UUID\_IPS\_VAL](group__bt__uuid.md#ga8fafd81c36f6b515d2709d5f4efd9d00)   0x1821 |
|  | Indoor Positioning Service UUID value. |
| #define | [BT\_UUID\_IPS](group__bt__uuid.md#ga8dac7b88922315a2af06ad70cdfcfd0c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_IPS\_VAL](group__bt__uuid.md#ga8fafd81c36f6b515d2709d5f4efd9d00)) |
|  | Indoor Positioning Service. |
| #define | [BT\_UUID\_POS\_VAL](group__bt__uuid.md#gabfb8333e3fb8e819f02601ace836687b)   0x1822 |
|  | Pulse Oximeter Service UUID value. |
| #define | [BT\_UUID\_POS](group__bt__uuid.md#gaa713f38e63cfc998559c862f80f2380b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_POS\_VAL](group__bt__uuid.md#gabfb8333e3fb8e819f02601ace836687b)) |
|  | Pulse Oximeter Service. |
| #define | [BT\_UUID\_HPS\_VAL](group__bt__uuid.md#ga5f66d3e11dcde95c3c4e7055734c9aef)   0x1823 |
|  | HTTP Proxy Service UUID value. |
| #define | [BT\_UUID\_HPS](group__bt__uuid.md#gaade9071b49d238d13edf57e90655c41c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HPS\_VAL](group__bt__uuid.md#ga5f66d3e11dcde95c3c4e7055734c9aef)) |
|  | HTTP Proxy Service. |
| #define | [BT\_UUID\_TDS\_VAL](group__bt__uuid.md#gafafc31de7e0d06e831ef13f5ddb88685)   0x1824 |
|  | Transport Discovery Service UUID value. |
| #define | [BT\_UUID\_TDS](group__bt__uuid.md#gaccdb682d8f53c8560bea355a5376d72d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TDS\_VAL](group__bt__uuid.md#gafafc31de7e0d06e831ef13f5ddb88685)) |
|  | Transport Discovery Service. |
| #define | [BT\_UUID\_OTS\_VAL](group__bt__uuid.md#ga0a7a74bbb0c8bbd97d5fd6807deeb4c3)   0x1825 |
|  | Object Transfer Service UUID value. |
| #define | [BT\_UUID\_OTS](group__bt__uuid.md#ga4f18867b63edde824c1a57c0ee354282)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_VAL](group__bt__uuid.md#ga0a7a74bbb0c8bbd97d5fd6807deeb4c3)) |
|  | Object Transfer Service. |
| #define | [BT\_UUID\_FMS\_VAL](group__bt__uuid.md#ga036c6c7b6589a7178851ff7004aa64db)   0x1826 |
|  | Fitness Machine Service UUID value. |
| #define | [BT\_UUID\_FMS](group__bt__uuid.md#ga8935f33e5d388c96e38a172a5831b573)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_FMS\_VAL](group__bt__uuid.md#ga036c6c7b6589a7178851ff7004aa64db)) |
|  | Fitness Machine Service. |
| #define | [BT\_UUID\_MESH\_PROV\_VAL](group__bt__uuid.md#gaa0bf05b5c11a3b6f9f0f8e48298b4776)   0x1827 |
|  | Mesh Provisioning Service UUID value. |
| #define | [BT\_UUID\_MESH\_PROV](group__bt__uuid.md#ga665cc5a42b1b074536ce949fe1853f7b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MESH\_PROV\_VAL](group__bt__uuid.md#gaa0bf05b5c11a3b6f9f0f8e48298b4776)) |
|  | Mesh Provisioning Service. |
| #define | [BT\_UUID\_MESH\_PROXY\_VAL](group__bt__uuid.md#gaa347d1cf40b3eba7052c3e7c80e32a02)   0x1828 |
|  | Mesh Proxy Service UUID value. |
| #define | [BT\_UUID\_MESH\_PROXY](group__bt__uuid.md#ga34de82083c412e280bb585db519d70a2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MESH\_PROXY\_VAL](group__bt__uuid.md#gaa347d1cf40b3eba7052c3e7c80e32a02)) |
|  | Mesh Proxy Service. |
| #define | [BT\_UUID\_MESH\_PROXY\_SOLICITATION\_VAL](group__bt__uuid.md#ga02eaaf8d7ec7981336713d4cb1ea6b6a)   0x1859 |
|  | Proxy Solicitation UUID value. |
| #define | [BT\_UUID\_RCSRV\_VAL](group__bt__uuid.md#ga76f45a959cf7d4bb5b874ba2e2f8c5ad)   0x1829 |
|  | Reconnection Configuration Service UUID value. |
| #define | [BT\_UUID\_RCSRV](group__bt__uuid.md#gafc39274d32d212b7b244f24809d00e15)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_RCSRV\_VAL](group__bt__uuid.md#ga76f45a959cf7d4bb5b874ba2e2f8c5ad)) |
|  | Reconnection Configuration Service. |
| #define | [BT\_UUID\_IDS\_VAL](group__bt__uuid.md#gac1069e0c1a650aa7659942f0533cb384)   0x183a |
|  | Insulin Delivery Service UUID value. |
| #define | [BT\_UUID\_IDS](group__bt__uuid.md#gac3921b7c5c31423d7ac7ed4338ccf980)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_IDS\_VAL](group__bt__uuid.md#gac1069e0c1a650aa7659942f0533cb384)) |
|  | Insulin Delivery Service. |
| #define | [BT\_UUID\_BSS\_VAL](group__bt__uuid.md#gaa75f32c09a7f70c1b79fb7af1b50c0fe)   0x183b |
|  | Binary Sensor Service UUID value. |
| #define | [BT\_UUID\_BSS](group__bt__uuid.md#gacc9ac8d5418e857f70b7836629874296)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BSS\_VAL](group__bt__uuid.md#gaa75f32c09a7f70c1b79fb7af1b50c0fe)) |
|  | Binary Sensor Service. |
| #define | [BT\_UUID\_ECS\_VAL](group__bt__uuid.md#gabd1855b6ede9f8dcfa46b211ad7a33b5)   0x183c |
|  | Emergency Configuration Service UUID value. |
| #define | [BT\_UUID\_ECS](group__bt__uuid.md#ga966e2b5ad06522d4a6e882755fc4dcbf)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ECS\_VAL](group__bt__uuid.md#gabd1855b6ede9f8dcfa46b211ad7a33b5)) |
|  | Emergency Configuration Service. |
| #define | [BT\_UUID\_ACLS\_VAL](group__bt__uuid.md#ga72b1d17c97437e7ced4e1c7c3fb9d0cd)   0x183d |
|  | Authorization Control Service UUID value. |
| #define | [BT\_UUID\_ACLS](group__bt__uuid.md#ga022390a0b44e81e0925e29a87fd4d1e3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ACLS\_VAL](group__bt__uuid.md#ga72b1d17c97437e7ced4e1c7c3fb9d0cd)) |
|  | Authorization Control Service. |
| #define | [BT\_UUID\_PAMS\_VAL](group__bt__uuid.md#gaf85d03a7c42d040559874e6d1a6296a6)   0x183e |
|  | Physical Activity Monitor Service UUID value. |
| #define | [BT\_UUID\_PAMS](group__bt__uuid.md#ga3c5590637fc3c90c4beed23bab9f5eb6)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_PAMS\_VAL](group__bt__uuid.md#gaf85d03a7c42d040559874e6d1a6296a6)) |
|  | Physical Activity Monitor Service. |
| #define | [BT\_UUID\_AICS\_VAL](group__bt__uuid.md#ga67f3c417689d2a7af32e9bacaa274d44)   0x1843 |
|  | Audio Input Control Service UUID value. |
| #define | [BT\_UUID\_AICS](group__bt__uuid.md#ga8e7ec38a733ebe33d9d1d525a7c2c051)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_AICS\_VAL](group__bt__uuid.md#ga67f3c417689d2a7af32e9bacaa274d44)) |
|  | Audio Input Control Service. |
| #define | [BT\_UUID\_VCS\_VAL](group__bt__uuid.md#ga9de8d92b55a644904d5b7257608cba45)   0x1844 |
|  | Volume Control Service UUID value. |
| #define | [BT\_UUID\_VCS](group__bt__uuid.md#gaaf797d6506d5f47e730e5bbf6ff79f7c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_VCS\_VAL](group__bt__uuid.md#ga9de8d92b55a644904d5b7257608cba45)) |
|  | Volume Control Service. |
| #define | [BT\_UUID\_VOCS\_VAL](group__bt__uuid.md#ga78b30023b019279b2b9567d7c3ffeac2)   0x1845 |
|  | Volume Offset Control Service UUID value. |
| #define | [BT\_UUID\_VOCS](group__bt__uuid.md#ga2ab2f92985ca0f65fb066df57c2f1433)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_VOCS\_VAL](group__bt__uuid.md#ga78b30023b019279b2b9567d7c3ffeac2)) |
|  | Volume Offset Control Service. |
| #define | [BT\_UUID\_CSIS\_VAL](group__bt__uuid.md#ga5f2c25e1c3f14fb65f062dc34f56b3ed)   0x1846 |
|  | Coordinated Set Identification Service UUID value. |
| #define | [BT\_UUID\_CSIS](group__bt__uuid.md#ga111f2eb8e186444804b8b3c39f0f00a3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CSIS\_VAL](group__bt__uuid.md#ga5f2c25e1c3f14fb65f062dc34f56b3ed)) |
|  | Coordinated Set Identification Service. |
| #define | [BT\_UUID\_DTS\_VAL](group__bt__uuid.md#gad8fc6ade8cafce1b9461de0a27389c88)   0x1847 |
|  | Device Time Service UUID value. |
| #define | [BT\_UUID\_DTS](group__bt__uuid.md#ga6417c327841fd7317515e394f5ac0089)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DTS\_VAL](group__bt__uuid.md#gad8fc6ade8cafce1b9461de0a27389c88)) |
|  | Device Time Service. |
| #define | [BT\_UUID\_MCS\_VAL](group__bt__uuid.md#ga3cd2f717c107a3e8d65eb958155884fd)   0x1848 |
|  | Media Control Service UUID value. |
| #define | [BT\_UUID\_MCS](group__bt__uuid.md#ga7b84d0b301ce2f565de7eb89165af0cf)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_VAL](group__bt__uuid.md#ga3cd2f717c107a3e8d65eb958155884fd)) |
|  | Media Control Service. |
| #define | [BT\_UUID\_GMCS\_VAL](group__bt__uuid.md#ga35e8dae5a05985c10e3cdd610161ebcc)   0x1849 |
|  | Generic Media Control Service UUID value. |
| #define | [BT\_UUID\_GMCS](group__bt__uuid.md#ga4efbadd4ce5a6fb64a5d9832b4626d0f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GMCS\_VAL](group__bt__uuid.md#ga35e8dae5a05985c10e3cdd610161ebcc)) |
|  | Generic Media Control Service. |
| #define | [BT\_UUID\_CTES\_VAL](group__bt__uuid.md#ga9e7f780e9800abc6fa86fa034482df4b)   0x184a |
|  | Constant Tone Extension Service UUID value. |
| #define | [BT\_UUID\_CTES](group__bt__uuid.md#gaf85f0bff2abbe069d8d64a3eda2a066d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CTES\_VAL](group__bt__uuid.md#ga9e7f780e9800abc6fa86fa034482df4b)) |
|  | Constant Tone Extension Service. |
| #define | [BT\_UUID\_TBS\_VAL](group__bt__uuid.md#gae25bb19fe3d92555a9c2c2de6fae5354)   0x184b |
|  | Telephone Bearer Service UUID value. |
| #define | [BT\_UUID\_TBS](group__bt__uuid.md#ga70c7991e602fa8c87868cac63c838c21)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_VAL](group__bt__uuid.md#gae25bb19fe3d92555a9c2c2de6fae5354)) |
|  | Telephone Bearer Service. |
| #define | [BT\_UUID\_GTBS\_VAL](group__bt__uuid.md#ga1e90e6d7a97ca28b842012f61b76a2cb)   0x184c |
|  | Generic Telephone Bearer Service UUID value. |
| #define | [BT\_UUID\_GTBS](group__bt__uuid.md#gabb0810fa80d5623a5af457a2fb02ca6e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GTBS\_VAL](group__bt__uuid.md#ga1e90e6d7a97ca28b842012f61b76a2cb)) |
|  | Generic Telephone Bearer Service. |
| #define | [BT\_UUID\_MICS\_VAL](group__bt__uuid.md#gac18fe10ee79d240af7c494fab0304d90)   0x184d |
|  | Microphone Control Service UUID value. |
| #define | [BT\_UUID\_MICS](group__bt__uuid.md#ga411a51f52e6e63c905d86ce5b924e69c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MICS\_VAL](group__bt__uuid.md#gac18fe10ee79d240af7c494fab0304d90)) |
|  | Microphone Control Service. |
| #define | [BT\_UUID\_ASCS\_VAL](group__bt__uuid.md#gaedc903cd915524adfa5d4d64fa38cf22)   0x184e |
|  | Audio Stream Control Service UUID value. |
| #define | [BT\_UUID\_ASCS](group__bt__uuid.md#ga7d52614d936753738fb04f124c97fc09)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ASCS\_VAL](group__bt__uuid.md#gaedc903cd915524adfa5d4d64fa38cf22)) |
|  | Audio Stream Control Service. |
| #define | [BT\_UUID\_BASS\_VAL](group__bt__uuid.md#gaa671703a706fc97dcc9a4b1dd7f4fef3)   0x184f |
|  | Broadcast Audio Scan Service UUID value. |
| #define | [BT\_UUID\_BASS](group__bt__uuid.md#ga7d0e06ae7e089098ac9d0c32087d5803)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BASS\_VAL](group__bt__uuid.md#gaa671703a706fc97dcc9a4b1dd7f4fef3)) |
|  | Broadcast Audio Scan Service. |
| #define | [BT\_UUID\_PACS\_VAL](group__bt__uuid.md#ga69dafd580d116dec74b54c818d5c275b)   0x1850 |
|  | Published Audio Capabilities Service UUID value. |
| #define | [BT\_UUID\_PACS](group__bt__uuid.md#ga86720eb2ad6aa3f66a9bf2248cb95383)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_PACS\_VAL](group__bt__uuid.md#ga69dafd580d116dec74b54c818d5c275b)) |
|  | Published Audio Capabilities Service. |
| #define | [BT\_UUID\_BASIC\_AUDIO\_VAL](group__bt__uuid.md#gaa1c0efca17e5b3de3c0fd254181a53db)   0x1851 |
|  | Basic Audio Announcement Service UUID value. |
| #define | [BT\_UUID\_BASIC\_AUDIO](group__bt__uuid.md#ga842f48f68be48c3379161b595fca22a2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BASIC\_AUDIO\_VAL](group__bt__uuid.md#gaa1c0efca17e5b3de3c0fd254181a53db)) |
|  | Basic Audio Announcement Service. |
| #define | [BT\_UUID\_BROADCAST\_AUDIO\_VAL](group__bt__uuid.md#ga0c67f9e1a5fef34fd1fddc539e20119b)   0x1852 |
|  | Broadcast Audio Announcement Service UUID value. |
| #define | [BT\_UUID\_BROADCAST\_AUDIO](group__bt__uuid.md#gafe9b1d539a9c77037e0c8433b702790e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BROADCAST\_AUDIO\_VAL](group__bt__uuid.md#ga0c67f9e1a5fef34fd1fddc539e20119b)) |
|  | Broadcast Audio Announcement Service. |
| #define | [BT\_UUID\_CAS\_VAL](group__bt__uuid.md#gab3f48a2a32b3a2061f3b108350c59ec4)   0x1853 |
|  | Common Audio Service UUID value. |
| #define | [BT\_UUID\_CAS](group__bt__uuid.md#gab69a851e430a0232abb839b0d9fc54e5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CAS\_VAL](group__bt__uuid.md#gab3f48a2a32b3a2061f3b108350c59ec4)) |
|  | Common Audio Service. |
| #define | [BT\_UUID\_HAS\_VAL](group__bt__uuid.md#ga8d937e82611aaa2da305795d00074c93)   0x1854 |
|  | Hearing Access Service UUID value. |
| #define | [BT\_UUID\_HAS](group__bt__uuid.md#gac5acaee5423acd4531768fbf8844676b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HAS\_VAL](group__bt__uuid.md#ga8d937e82611aaa2da305795d00074c93)) |
|  | Hearing Access Service. |
| #define | [BT\_UUID\_TMAS\_VAL](group__bt__uuid.md#ga42f0d2bf3ce4a258a6f9d14a828cf422)   0x1855 |
|  | Telephony and Media Audio Service UUID value. |
| #define | [BT\_UUID\_TMAS](group__bt__uuid.md#ga84ea43f70dee139497be28d90db70104)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TMAS\_VAL](group__bt__uuid.md#ga42f0d2bf3ce4a258a6f9d14a828cf422)) |
|  | Telephony and Media Audio Service. |
| #define | [BT\_UUID\_PBA\_VAL](group__bt__uuid.md#ga06265a1d97c1b734340f9eb0055da913)   0x1856 |
|  | Public Broadcast Announcement Service UUID value. |
| #define | [BT\_UUID\_PBA](group__bt__uuid.md#ga98f4f946c1bca483a7e81cad162ee0b1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_PBA\_VAL](group__bt__uuid.md#ga06265a1d97c1b734340f9eb0055da913)) |
|  | Public Broadcast Announcement Service. |
| #define | [BT\_UUID\_GATT\_PRIMARY\_VAL](group__bt__uuid.md#ga8244f6edaf3a347be1a3bf4e1d8fb4c3)   0x2800 |
|  | GATT Primary Service UUID value. |
| #define | [BT\_UUID\_GATT\_PRIMARY](group__bt__uuid.md#ga6e87ce1575494eb90358e074e8dbe276)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PRIMARY\_VAL](group__bt__uuid.md#ga8244f6edaf3a347be1a3bf4e1d8fb4c3)) |
|  | GATT Primary Service. |
| #define | [BT\_UUID\_GATT\_SECONDARY\_VAL](group__bt__uuid.md#ga764703eec266d58b0ea9e00d02f23d1d)   0x2801 |
|  | GATT Secondary Service UUID value. |
| #define | [BT\_UUID\_GATT\_SECONDARY](group__bt__uuid.md#gad084d3658e663b6b8e200be256c54cdb)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SECONDARY\_VAL](group__bt__uuid.md#ga764703eec266d58b0ea9e00d02f23d1d)) |
|  | GATT Secondary Service. |
| #define | [BT\_UUID\_GATT\_INCLUDE\_VAL](group__bt__uuid.md#gaa493141bce2425fe40f809f151ace673)   0x2802 |
|  | GATT Include Service UUID value. |
| #define | [BT\_UUID\_GATT\_INCLUDE](group__bt__uuid.md#ga995596ff7374ebcb44d4706bc16234e4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_INCLUDE\_VAL](group__bt__uuid.md#gaa493141bce2425fe40f809f151ace673)) |
|  | GATT Include Service. |
| #define | [BT\_UUID\_GATT\_CHRC\_VAL](group__bt__uuid.md#gae8b1af5f3458ca8523db83a3d8ccc62c)   0x2803 |
|  | GATT Characteristic UUID value. |
| #define | [BT\_UUID\_GATT\_CHRC](group__bt__uuid.md#gadcedbbe1c432c4ac737e54b318e01a0f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CHRC\_VAL](group__bt__uuid.md#gae8b1af5f3458ca8523db83a3d8ccc62c)) |
|  | GATT Characteristic. |
| #define | [BT\_UUID\_GATT\_CEP\_VAL](group__bt__uuid.md#ga68b7ae19aad514e4a6731796c34c59da)   0x2900 |
|  | GATT Characteristic Extended Properties UUID value. |
| #define | [BT\_UUID\_GATT\_CEP](group__bt__uuid.md#ga6aa143b721d810f1536d7431a9bf7cc7)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CEP\_VAL](group__bt__uuid.md#ga68b7ae19aad514e4a6731796c34c59da)) |
|  | GATT Characteristic Extended Properties. |
| #define | [BT\_UUID\_GATT\_CUD\_VAL](group__bt__uuid.md#ga2a168fa660bc6c3c3d5a85d99f2c9e60)   0x2901 |
|  | GATT Characteristic User Description UUID value. |
| #define | [BT\_UUID\_GATT\_CUD](group__bt__uuid.md#gaaaf94f5d918a1b6715cf4816b03875a2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CUD\_VAL](group__bt__uuid.md#ga2a168fa660bc6c3c3d5a85d99f2c9e60)) |
|  | GATT Characteristic User Description. |
| #define | [BT\_UUID\_GATT\_CCC\_VAL](group__bt__uuid.md#gaa7807cb9ed1aa19f48c7dc4904f52dbb)   0x2902 |
|  | GATT Client Characteristic Configuration UUID value. |
| #define | [BT\_UUID\_GATT\_CCC](group__bt__uuid.md#ga03a2d3f0ce89508b794d5c87a4303057)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CCC\_VAL](group__bt__uuid.md#gaa7807cb9ed1aa19f48c7dc4904f52dbb)) |
|  | GATT Client Characteristic Configuration. |
| #define | [BT\_UUID\_GATT\_SCC\_VAL](group__bt__uuid.md#ga84cc4d600b5218baf5620b87cb8ddc55)   0x2903 |
|  | GATT Server Characteristic Configuration UUID value. |
| #define | [BT\_UUID\_GATT\_SCC](group__bt__uuid.md#ga82567cdce8c4411cd3daf26711ba9685)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SCC\_VAL](group__bt__uuid.md#ga84cc4d600b5218baf5620b87cb8ddc55)) |
|  | GATT Server Characteristic Configuration. |
| #define | [BT\_UUID\_GATT\_CPF\_VAL](group__bt__uuid.md#ga71924f95ca117ace35e64b0222bb5bf7)   0x2904 |
|  | GATT Characteristic Presentation Format UUID value. |
| #define | [BT\_UUID\_GATT\_CPF](group__bt__uuid.md#ga331a61702ffe9b15bac0de3d60414022)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CPF\_VAL](group__bt__uuid.md#ga71924f95ca117ace35e64b0222bb5bf7)) |
|  | GATT Characteristic Presentation Format. |
| #define | [BT\_UUID\_GATT\_CAF\_VAL](group__bt__uuid.md#ga88dbd0deac028cb0df1a6bd1874aec7f)   0x2905 |
|  | GATT Characteristic Aggregated Format UUID value. |
| #define | [BT\_UUID\_GATT\_CAF](group__bt__uuid.md#gadc590b4039c9f47965e88e57b5589a93)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CAF\_VAL](group__bt__uuid.md#ga88dbd0deac028cb0df1a6bd1874aec7f)) |
|  | GATT Characteristic Aggregated Format. |
| #define | [BT\_UUID\_VALID\_RANGE\_VAL](group__bt__uuid.md#ga6fa0e8a8f2727e4646461ca14247466f)   0x2906 |
|  | Valid Range Descriptor UUID value. |
| #define | [BT\_UUID\_VALID\_RANGE](group__bt__uuid.md#gad53d373df905c4b11c39a3ae4284a6d1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_VALID\_RANGE\_VAL](group__bt__uuid.md#ga6fa0e8a8f2727e4646461ca14247466f)) |
|  | Valid Range Descriptor. |
| #define | [BT\_UUID\_HIDS\_EXT\_REPORT\_VAL](group__bt__uuid.md#gaa8e06b1198ea23a01e892080df88e7f4)   0x2907 |
|  | HID External Report Descriptor UUID value. |
| #define | [BT\_UUID\_HIDS\_EXT\_REPORT](group__bt__uuid.md#gae945ad8eac1b444d92096c76239e106d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDS\_EXT\_REPORT\_VAL](group__bt__uuid.md#gaa8e06b1198ea23a01e892080df88e7f4)) |
|  | HID External Report Descriptor. |
| #define | [BT\_UUID\_HIDS\_REPORT\_REF\_VAL](group__bt__uuid.md#ga4c1f2a0f52f101910f9294b10b5af484)   0x2908 |
|  | HID Report Reference Descriptor UUID value. |
| #define | [BT\_UUID\_HIDS\_REPORT\_REF](group__bt__uuid.md#ga001e019b08f5f88a158ed0861c017609)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDS\_REPORT\_REF\_VAL](group__bt__uuid.md#ga4c1f2a0f52f101910f9294b10b5af484)) |
|  | HID Report Reference Descriptor. |
| #define | [BT\_UUID\_VAL\_TRIGGER\_SETTING\_VAL](group__bt__uuid.md#ga882af0a9286c487c1f108346be9af304)   0x290a |
|  | Value Trigger Setting Descriptor UUID value. |
| #define | [BT\_UUID\_VAL\_TRIGGER\_SETTING](group__bt__uuid.md#ga2601c8bcfd2efae9b20e67f5c95de3f1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_VAL\_TRIGGER\_SETTING\_VAL](group__bt__uuid.md#ga882af0a9286c487c1f108346be9af304)) |
|  | Value Trigger Setting Descriptor. |
| #define | [BT\_UUID\_ES\_CONFIGURATION\_VAL](group__bt__uuid.md#ga85eab7f3dbd2f517d36e750d3c020dec)   0x290b |
|  | Environmental Sensing Configuration Descriptor UUID value. |
| #define | [BT\_UUID\_ES\_CONFIGURATION](group__bt__uuid.md#gae2d7028c5102df6f53765a98b9b729ea)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ES\_CONFIGURATION\_VAL](group__bt__uuid.md#ga85eab7f3dbd2f517d36e750d3c020dec)) |
|  | Environmental Sensing Configuration Descriptor. |
| #define | [BT\_UUID\_ES\_MEASUREMENT\_VAL](group__bt__uuid.md#ga8758259d984c0391feeceb459591e2fb)   0x290c |
|  | Environmental Sensing Measurement Descriptor UUID value. |
| #define | [BT\_UUID\_ES\_MEASUREMENT](group__bt__uuid.md#ga5e738598773234b87a1db746badce304)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ES\_MEASUREMENT\_VAL](group__bt__uuid.md#ga8758259d984c0391feeceb459591e2fb)) |
|  | Environmental Sensing Measurement Descriptor. |
| #define | [BT\_UUID\_ES\_TRIGGER\_SETTING\_VAL](group__bt__uuid.md#ga0da1b874a844e15cdf185c6e7cbc9d64)   0x290d |
|  | Environmental Sensing Trigger Setting Descriptor UUID value. |
| #define | [BT\_UUID\_ES\_TRIGGER\_SETTING](group__bt__uuid.md#gab9daf129a8625853989516032010f1a3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ES\_TRIGGER\_SETTING\_VAL](group__bt__uuid.md#ga0da1b874a844e15cdf185c6e7cbc9d64)) |
|  | Environmental Sensing Trigger Setting Descriptor. |
| #define | [BT\_UUID\_TM\_TRIGGER\_SETTING\_VAL](group__bt__uuid.md#gacacc7a2120d918c46a45cde0b0a8e44b)   0x290e |
|  | Time Trigger Setting Descriptor UUID value. |
| #define | [BT\_UUID\_TM\_TRIGGER\_SETTING](group__bt__uuid.md#ga017b04e00401d50fc33cfd34d218492c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TM\_TRIGGER\_SETTING\_VAL](group__bt__uuid.md#gacacc7a2120d918c46a45cde0b0a8e44b)) |
|  | Time Trigger Setting Descriptor. |
| #define | [BT\_UUID\_GAP\_DEVICE\_NAME\_VAL](group__bt__uuid.md#gac7a400574b6c78638e41eeaf97b7e9f3)   0x2a00 |
|  | GAP Characteristic Device Name UUID value. |
| #define | [BT\_UUID\_GAP\_DEVICE\_NAME](group__bt__uuid.md#ga2bda01c9df904c8d0260ca3c0e3924cb)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GAP\_DEVICE\_NAME\_VAL](group__bt__uuid.md#gac7a400574b6c78638e41eeaf97b7e9f3)) |
|  | GAP Characteristic Device Name. |
| #define | [BT\_UUID\_GAP\_APPEARANCE\_VAL](group__bt__uuid.md#ga8789efbc24ac67479a86c3dfa0379154)   0x2a01 |
|  | GAP Characteristic Appearance UUID value. |
| #define | [BT\_UUID\_GAP\_APPEARANCE](group__bt__uuid.md#ga4354d250e2cfca4fc868134bca4178b0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GAP\_APPEARANCE\_VAL](group__bt__uuid.md#ga8789efbc24ac67479a86c3dfa0379154)) |
|  | GAP Characteristic Appearance. |
| #define | [BT\_UUID\_GAP\_PPF\_VAL](group__bt__uuid.md#ga575ef013a228bb5bb728724c9334347f)   0x2a02 |
|  | GAP Characteristic Peripheral Privacy Flag UUID value. |
| #define | [BT\_UUID\_GAP\_PPF](group__bt__uuid.md#ga4bec5c6656a10756a38ac9a6805f9757)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GAP\_PPF\_VAL](group__bt__uuid.md#ga575ef013a228bb5bb728724c9334347f)) |
|  | GAP Characteristic Peripheral Privacy Flag. |
| #define | [BT\_UUID\_GAP\_RA\_VAL](group__bt__uuid.md#ga739961cc85dd01779228f5054a3c3790)   0x2a03 |
|  | GAP Characteristic Reconnection Address UUID value. |
| #define | [BT\_UUID\_GAP\_RA](group__bt__uuid.md#ga569663025aceabcd964f9c423ab030b5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GAP\_RA\_VAL](group__bt__uuid.md#ga739961cc85dd01779228f5054a3c3790)) |
|  | GAP Characteristic Reconnection Address. |
| #define | [BT\_UUID\_GAP\_PPCP\_VAL](group__bt__uuid.md#ga08be6df54da61393b3fe4efb7ab70b71)   0x2a04 |
|  | GAP Characteristic Peripheral Preferred Connection Parameters UUID value. |
| #define | [BT\_UUID\_GAP\_PPCP](group__bt__uuid.md#gad174f313309b1bbb1208c61769566c77)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GAP\_PPCP\_VAL](group__bt__uuid.md#ga08be6df54da61393b3fe4efb7ab70b71)) |
|  | GAP Characteristic Peripheral Preferred Connection Parameters. |
| #define | [BT\_UUID\_GATT\_SC\_VAL](group__bt__uuid.md#gaf7af098d1487b3e09ded21b4490c50e0)   0x2a05 |
|  | GATT Characteristic Service Changed UUID value. |
| #define | [BT\_UUID\_GATT\_SC](group__bt__uuid.md#gad0609fd8c275c69cd0aabb7ba7c0f628)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SC\_VAL](group__bt__uuid.md#gaf7af098d1487b3e09ded21b4490c50e0)) |
|  | GATT Characteristic Service Changed. |
| #define | [BT\_UUID\_ALERT\_LEVEL\_VAL](group__bt__uuid.md#ga2df4fc4fb971330cb7462911b68f73fd)   0x2a06 |
|  | GATT Characteristic Alert Level UUID value. |
| #define | [BT\_UUID\_ALERT\_LEVEL](group__bt__uuid.md#ga400e07242af41e836dfc250dc41cb010)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ALERT\_LEVEL\_VAL](group__bt__uuid.md#ga2df4fc4fb971330cb7462911b68f73fd)) |
|  | GATT Characteristic Alert Level. |
| #define | [BT\_UUID\_TPS\_TX\_POWER\_LEVEL\_VAL](group__bt__uuid.md#ga07f1f99a8e237304f9415fade56432e4)   0x2a07 |
|  | TPS Characteristic Tx Power Level UUID value. |
| #define | [BT\_UUID\_TPS\_TX\_POWER\_LEVEL](group__bt__uuid.md#gade253bd200b4d2ea9f0463c3911295f1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TPS\_TX\_POWER\_LEVEL\_VAL](group__bt__uuid.md#ga07f1f99a8e237304f9415fade56432e4)) |
|  | TPS Characteristic Tx Power Level. |
| #define | [BT\_UUID\_GATT\_DT\_VAL](group__bt__uuid.md#ga71d42d8e00aa0b388315aeeb68c29839)   0x2a08 |
|  | GATT Characteristic Date Time UUID value. |
| #define | [BT\_UUID\_GATT\_DT](group__bt__uuid.md#ga09cd4c6c81b8393f19b765a01ec556a0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DT\_VAL](group__bt__uuid.md#ga71d42d8e00aa0b388315aeeb68c29839)) |
|  | GATT Characteristic Date Time. |
| #define | [BT\_UUID\_GATT\_DW\_VAL](group__bt__uuid.md#ga952c7341d02dd4bf3cea142b0b41e41c)   0x2a09 |
|  | GATT Characteristic Day of Week UUID value. |
| #define | [BT\_UUID\_GATT\_DW](group__bt__uuid.md#ga442781cffe3da4bff3c8903d46ae07a0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DW\_VAL](group__bt__uuid.md#ga952c7341d02dd4bf3cea142b0b41e41c)) |
|  | GATT Characteristic Day of Week. |
| #define | [BT\_UUID\_GATT\_DDT\_VAL](group__bt__uuid.md#ga02fd005f86fd9995d61f63c3e7735028)   0x2a0a |
|  | GATT Characteristic Day Date Time UUID value. |
| #define | [BT\_UUID\_GATT\_DDT](group__bt__uuid.md#gaee156d97abd11f1422677bbb08cd5193)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DDT\_VAL](group__bt__uuid.md#ga02fd005f86fd9995d61f63c3e7735028)) |
|  | GATT Characteristic Day Date Time. |
| #define | [BT\_UUID\_GATT\_ET256\_VAL](group__bt__uuid.md#ga195fc66b479dec1131ea5e7cf1350afb)   0x2a0c |
|  | GATT Characteristic Exact Time 256 UUID value. |
| #define | [BT\_UUID\_GATT\_ET256](group__bt__uuid.md#ga3d5472767d50ddeabcdc7e2961610b78)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ET256\_VAL](group__bt__uuid.md#ga195fc66b479dec1131ea5e7cf1350afb)) |
|  | GATT Characteristic Exact Time 256. |
| #define | [BT\_UUID\_GATT\_DST\_VAL](group__bt__uuid.md#gad826c92cd28e6eef5651474b611ab093)   0x2a0d |
|  | GATT Characteristic DST Offset UUID value. |
| #define | [BT\_UUID\_GATT\_DST](group__bt__uuid.md#ga4b08c7472ecfe66eb2290fd83772ea24)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DST\_VAL](group__bt__uuid.md#gad826c92cd28e6eef5651474b611ab093)) |
|  | GATT Characteristic DST Offset. |
| #define | [BT\_UUID\_GATT\_TZ\_VAL](group__bt__uuid.md#ga4e7082162bcdc58b385989e955ebb7f9)   0x2a0e |
|  | GATT Characteristic Time Zone UUID value. |
| #define | [BT\_UUID\_GATT\_TZ](group__bt__uuid.md#ga83e5e48b8bd8955dc559b95ec6e73a78)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TZ\_VAL](group__bt__uuid.md#ga4e7082162bcdc58b385989e955ebb7f9)) |
|  | GATT Characteristic Time Zone. |
| #define | [BT\_UUID\_GATT\_LTI\_VAL](group__bt__uuid.md#ga25c6a750b9548144da0e78cca3ad6a59)   0x2a0f |
|  | GATT Characteristic Local Time Information UUID value. |
| #define | [BT\_UUID\_GATT\_LTI](group__bt__uuid.md#ga6524bc40fbada1e558635af6b52283b9)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LTI\_VAL](group__bt__uuid.md#ga25c6a750b9548144da0e78cca3ad6a59)) |
|  | GATT Characteristic Local Time Information. |
| #define | [BT\_UUID\_GATT\_TDST\_VAL](group__bt__uuid.md#ga1bf3703c269e658c0e0e4ef822f14299)   0x2a11 |
|  | GATT Characteristic Time with DST UUID value. |
| #define | [BT\_UUID\_GATT\_TDST](group__bt__uuid.md#gace914257c496dbe17adc0d2b3db8f4c7)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TDST\_VAL](group__bt__uuid.md#ga1bf3703c269e658c0e0e4ef822f14299)) |
|  | GATT Characteristic Time with DST. |
| #define | [BT\_UUID\_GATT\_TA\_VAL](group__bt__uuid.md#gad304e85ca1a4b8f0f53d6068a37ae8d2)   0x2a12 |
|  | GATT Characteristic Time Accuracy UUID value. |
| #define | [BT\_UUID\_GATT\_TA](group__bt__uuid.md#ga75036cc3ceecebccfbfc153a0cc9920f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TA\_VAL](group__bt__uuid.md#gad304e85ca1a4b8f0f53d6068a37ae8d2)) |
|  | GATT Characteristic Time Accuracy. |
| #define | [BT\_UUID\_GATT\_TS\_VAL](group__bt__uuid.md#ga188a456a10d2a44c19a6825bb288294f)   0x2a13 |
|  | GATT Characteristic Time Source UUID value. |
| #define | [BT\_UUID\_GATT\_TS](group__bt__uuid.md#gaaaed25b2d73258322825ca9d2460c1a1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TS\_VAL](group__bt__uuid.md#ga188a456a10d2a44c19a6825bb288294f)) |
|  | GATT Characteristic Time Source. |
| #define | [BT\_UUID\_GATT\_RTI\_VAL](group__bt__uuid.md#ga668e9e73668b1c00a3bac74080ad7bcc)   0x2a14 |
|  | GATT Characteristic Reference Time Information UUID value. |
| #define | [BT\_UUID\_GATT\_RTI](group__bt__uuid.md#ga5b241e9ab9be83919aa99c24da34fa4b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RTI\_VAL](group__bt__uuid.md#ga668e9e73668b1c00a3bac74080ad7bcc)) |
|  | GATT Characteristic Reference Time Information. |
| #define | [BT\_UUID\_GATT\_TUCP\_VAL](group__bt__uuid.md#ga89f6031ef8778c4eb281dcda1afe5688)   0x2a16 |
|  | GATT Characteristic Time Update Control Point UUID value. |
| #define | [BT\_UUID\_GATT\_TUCP](group__bt__uuid.md#gaead8cf75f2bdecf9188272da2b3c5d41)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TUCP\_VAL](group__bt__uuid.md#ga89f6031ef8778c4eb281dcda1afe5688)) |
|  | GATT Characteristic Time Update Control Point. |
| #define | [BT\_UUID\_GATT\_TUS\_VAL](group__bt__uuid.md#ga0511dd52eadfa58395981b621b31c635)   0x2a17 |
|  | GATT Characteristic Time Update State UUID value. |
| #define | [BT\_UUID\_GATT\_TUS](group__bt__uuid.md#gaeef7563b0eb39783afc3c86147262aee)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TUS\_VAL](group__bt__uuid.md#ga0511dd52eadfa58395981b621b31c635)) |
|  | GATT Characteristic Time Update State. |
| #define | [BT\_UUID\_GATT\_GM\_VAL](group__bt__uuid.md#gaa11e9838368e470262efc07f86d12fc7)   0x2a18 |
|  | GATT Characteristic Glucose Measurement UUID value. |
| #define | [BT\_UUID\_GATT\_GM](group__bt__uuid.md#ga804ab92719239778e8328157876fce61)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_GM\_VAL](group__bt__uuid.md#gaa11e9838368e470262efc07f86d12fc7)) |
|  | GATT Characteristic Glucose Measurement. |
| #define | [BT\_UUID\_BAS\_BATTERY\_LEVEL\_VAL](group__bt__uuid.md#ga1961ff80d56b5c06185601cfce941cf1)   0x2a19 |
|  | BAS Characteristic Battery Level UUID value. |
| #define | [BT\_UUID\_BAS\_BATTERY\_LEVEL](group__bt__uuid.md#gae4f41b4e329c728767a8a99a3a89af7e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAS\_BATTERY\_LEVEL\_VAL](group__bt__uuid.md#ga1961ff80d56b5c06185601cfce941cf1)) |
|  | BAS Characteristic Battery Level. |
| #define | [BT\_UUID\_BAS\_BATTERY\_POWER\_STATE\_VAL](group__bt__uuid.md#ga818b6cbee38384f23e1548d49c89e53e)   0x2a1a |
|  | BAS Characteristic Battery Power State UUID value. |
| #define | [BT\_UUID\_BAS\_BATTERY\_POWER\_STATE](group__bt__uuid.md#ga17d4a2ee5c7587ef35013f47dacfb95d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAS\_BATTERY\_POWER\_STATE\_VAL](group__bt__uuid.md#ga818b6cbee38384f23e1548d49c89e53e)) |
|  | BAS Characteristic Battery Power State. |
| #define | [BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATE\_VAL](group__bt__uuid.md#ga7dcdb33b95cc58489343c9591fc0b453)   0x2a1b |
|  | BAS Characteristic Battery Level StateUUID value. |
| #define | [BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATE](group__bt__uuid.md#ga3022242a2bd7ccec5580d007182864dc)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATE\_VAL](group__bt__uuid.md#ga7dcdb33b95cc58489343c9591fc0b453)) |
|  | BAS Characteristic Battery Level State. |
| #define | [BT\_UUID\_HTS\_MEASUREMENT\_VAL](group__bt__uuid.md#ga612376c2ac9b3b21e1fe07aa2c931fad)   0x2a1c |
|  | HTS Characteristic Temperature Measurement UUID value. |
| #define | [BT\_UUID\_HTS\_MEASUREMENT](group__bt__uuid.md#gade726271d11b08b573aec3a1a6794c55)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTS\_MEASUREMENT\_VAL](group__bt__uuid.md#ga612376c2ac9b3b21e1fe07aa2c931fad)) |
|  | HTS Characteristic Temperature Measurement Value. |
| #define | [BT\_UUID\_HTS\_TEMP\_TYP\_VAL](group__bt__uuid.md#ga1e2c9c8bf1c27e0dd3fd37910a349d75)   0x2a1d |
|  | HTS Characteristic Temperature Type UUID value. |
| #define | [BT\_UUID\_HTS\_TEMP\_TYP](group__bt__uuid.md#ga7055bba7158854729f65f76841a32de6)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTS\_TEMP\_TYP\_VAL](group__bt__uuid.md#ga1e2c9c8bf1c27e0dd3fd37910a349d75)) |
|  | HTS Characteristic Temperature Type. |
| #define | [BT\_UUID\_HTS\_TEMP\_INT\_VAL](group__bt__uuid.md#ga4b13a008e37df4a0eb2b4b94bdb15126)   0x2a1e |
|  | HTS Characteristic Intermediate Temperature UUID value. |
| #define | [BT\_UUID\_HTS\_TEMP\_INT](group__bt__uuid.md#ga98f9fe29431766e819b3ea014294431b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTS\_TEMP\_INT\_VAL](group__bt__uuid.md#ga4b13a008e37df4a0eb2b4b94bdb15126)) |
|  | HTS Characteristic Intermediate Temperature. |
| #define | [BT\_UUID\_HTS\_TEMP\_C\_VAL](group__bt__uuid.md#ga67a6e1c0f24628e0cd11a4311de5a6fa)   0x2a1f |
|  | HTS Characteristic Temperature Celsius UUID value. |
| #define | [BT\_UUID\_HTS\_TEMP\_C](group__bt__uuid.md#ga51ef3d61ceffb85824b920fa7b04bd62)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTS\_TEMP\_C\_VAL](group__bt__uuid.md#ga67a6e1c0f24628e0cd11a4311de5a6fa)) |
|  | HTS Characteristic Temperature Celsius. |
| #define | [BT\_UUID\_HTS\_TEMP\_F\_VAL](group__bt__uuid.md#ga002d02e831aa0c3ca24b61b2527ac65b)   0x2a20 |
|  | HTS Characteristic Temperature Fahrenheit UUID value. |
| #define | [BT\_UUID\_HTS\_TEMP\_F](group__bt__uuid.md#ga6835b7816c5dc5bb4453e0b82925bb99)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTS\_TEMP\_F\_VAL](group__bt__uuid.md#ga002d02e831aa0c3ca24b61b2527ac65b)) |
|  | HTS Characteristic Temperature Fahrenheit. |
| #define | [BT\_UUID\_HTS\_INTERVAL\_VAL](group__bt__uuid.md#gac90751f69745ed65ff1739c1b86f3942)   0x2a21 |
|  | HTS Characteristic Measurement Interval UUID value. |
| #define | [BT\_UUID\_HTS\_INTERVAL](group__bt__uuid.md#ga993de0f6c8904f1d1f8527d8a4f31946)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTS\_INTERVAL\_VAL](group__bt__uuid.md#gac90751f69745ed65ff1739c1b86f3942)) |
|  | HTS Characteristic Measurement Interval. |
| #define | [BT\_UUID\_HIDS\_BOOT\_KB\_IN\_REPORT\_VAL](group__bt__uuid.md#gaa842693e29c174601e84feb43098b543)   0x2a22 |
|  | HID Characteristic Boot Keyboard Input Report UUID value. |
| #define | [BT\_UUID\_HIDS\_BOOT\_KB\_IN\_REPORT](group__bt__uuid.md#ga0ef3ddb08d602fcb513d348b1e1f2eb8)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDS\_BOOT\_KB\_IN\_REPORT\_VAL](group__bt__uuid.md#gaa842693e29c174601e84feb43098b543)) |
|  | HID Characteristic Boot Keyboard Input Report. |
| #define | [BT\_UUID\_DIS\_SYSTEM\_ID\_VAL](group__bt__uuid.md#ga4fdfa6e582c6367aea30e9846653ebd3)   0x2a23 |
|  | DIS Characteristic System ID UUID value. |
| #define | [BT\_UUID\_DIS\_SYSTEM\_ID](group__bt__uuid.md#gaac15c93c66cb583c3819036a2bd5ba24)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DIS\_SYSTEM\_ID\_VAL](group__bt__uuid.md#ga4fdfa6e582c6367aea30e9846653ebd3)) |
|  | DIS Characteristic System ID. |
| #define | [BT\_UUID\_DIS\_MODEL\_NUMBER\_VAL](group__bt__uuid.md#ga32a4462aa866ff15bf33046efde8e796)   0x2a24 |
|  | DIS Characteristic Model Number String UUID value. |
| #define | [BT\_UUID\_DIS\_MODEL\_NUMBER](group__bt__uuid.md#ga250d08b7b3de123c866143599975aa41)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DIS\_MODEL\_NUMBER\_VAL](group__bt__uuid.md#ga32a4462aa866ff15bf33046efde8e796)) |
|  | DIS Characteristic Model Number String. |
| #define | [BT\_UUID\_DIS\_SERIAL\_NUMBER\_VAL](group__bt__uuid.md#ga40c84dd8ce10d983596a4f6b9cfea82f)   0x2a25 |
|  | DIS Characteristic Serial Number String UUID value. |
| #define | [BT\_UUID\_DIS\_SERIAL\_NUMBER](group__bt__uuid.md#ga072770347ecf34cb89d293c31f59642d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DIS\_SERIAL\_NUMBER\_VAL](group__bt__uuid.md#ga40c84dd8ce10d983596a4f6b9cfea82f)) |
|  | DIS Characteristic Serial Number String. |
| #define | [BT\_UUID\_DIS\_FIRMWARE\_REVISION\_VAL](group__bt__uuid.md#ga220481d4fb2b498fad4e82637a0d02da)   0x2a26 |
|  | DIS Characteristic Firmware Revision String UUID value. |
| #define | [BT\_UUID\_DIS\_FIRMWARE\_REVISION](group__bt__uuid.md#ga988bb4018b232cb4da64d522703ec5b3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DIS\_FIRMWARE\_REVISION\_VAL](group__bt__uuid.md#ga220481d4fb2b498fad4e82637a0d02da)) |
|  | DIS Characteristic Firmware Revision String. |
| #define | [BT\_UUID\_DIS\_HARDWARE\_REVISION\_VAL](group__bt__uuid.md#ga3db6b3e905dd874c28a7b59c7a2a1b21)   0x2a27 |
|  | DIS Characteristic Hardware Revision String UUID value. |
| #define | [BT\_UUID\_DIS\_HARDWARE\_REVISION](group__bt__uuid.md#ga3842092a747954d24ceef3a0951efac7)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DIS\_HARDWARE\_REVISION\_VAL](group__bt__uuid.md#ga3db6b3e905dd874c28a7b59c7a2a1b21)) |
|  | DIS Characteristic Hardware Revision String. |
| #define | [BT\_UUID\_DIS\_SOFTWARE\_REVISION\_VAL](group__bt__uuid.md#gabef02eec1e667b2b35521a46b355d2e8)   0x2a28 |
|  | DIS Characteristic Software Revision String UUID value. |
| #define | [BT\_UUID\_DIS\_SOFTWARE\_REVISION](group__bt__uuid.md#ga8e9cc11f505e578851155659dc1ab262)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DIS\_SOFTWARE\_REVISION\_VAL](group__bt__uuid.md#gabef02eec1e667b2b35521a46b355d2e8)) |
|  | DIS Characteristic Software Revision String. |
| #define | [BT\_UUID\_DIS\_MANUFACTURER\_NAME\_VAL](group__bt__uuid.md#gac726ebb1cbc1d7ed63df41c232ee4a42)   0x2a29 |
|  | DIS Characteristic Manufacturer Name String UUID Value. |
| #define | [BT\_UUID\_DIS\_MANUFACTURER\_NAME](group__bt__uuid.md#gaefd466120c6923d806cfc4b5beb9899d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DIS\_MANUFACTURER\_NAME\_VAL](group__bt__uuid.md#gac726ebb1cbc1d7ed63df41c232ee4a42)) |
|  | DIS Characteristic Manufacturer Name String. |
| #define | [BT\_UUID\_GATT\_IEEE\_RCDL\_VAL](group__bt__uuid.md#gabf8a181cbe973c985c71aa6eb7d92fe1)   0x2a2a |
|  | GATT Characteristic IEEE Regulatory Certification Data List UUID Value. |
| #define | [BT\_UUID\_GATT\_IEEE\_RCDL](group__bt__uuid.md#ga3d95539bee32ca38ea825aadf85840fb)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IEEE\_RCDL\_VAL](group__bt__uuid.md#gabf8a181cbe973c985c71aa6eb7d92fe1)) |
|  | GATT Characteristic IEEE Regulatory Certification Data List. |
| #define | [BT\_UUID\_CTS\_CURRENT\_TIME\_VAL](group__bt__uuid.md#gae8de32ab38c9e160dc1883c345063855)   0x2a2b |
|  | CTS Characteristic Current Time UUID value. |
| #define | [BT\_UUID\_CTS\_CURRENT\_TIME](group__bt__uuid.md#gae0a920c076eb504b448f390c320ccfb8)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CTS\_CURRENT\_TIME\_VAL](group__bt__uuid.md#gae8de32ab38c9e160dc1883c345063855)) |
|  | CTS Characteristic Current Time. |
| #define | [BT\_UUID\_MAGN\_DECLINATION\_VAL](group__bt__uuid.md#ga6768ade4d8adf925fb52a27cee616e6e)   0x2a2c |
|  | Magnetic Declination Characteristic UUID value. |
| #define | [BT\_UUID\_MAGN\_DECLINATION](group__bt__uuid.md#ga7322a8412c7aaf9e6f06473d3fa5186d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MAGN\_DECLINATION\_VAL](group__bt__uuid.md#ga6768ade4d8adf925fb52a27cee616e6e)) |
|  | Magnetic Declination Characteristic. |
| #define | [BT\_UUID\_GATT\_LLAT\_VAL](group__bt__uuid.md#gabc9b96c541f0711bf5525269c4b3e5b0)   0x2a2d |
|  | GATT Characteristic Legacy Latitude UUID Value. |
| #define | [BT\_UUID\_GATT\_LLAT](group__bt__uuid.md#gaa9187bacfb95b379734ccf89f7eef163)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LLAT\_VAL](group__bt__uuid.md#gabc9b96c541f0711bf5525269c4b3e5b0)) |
|  | GATT Characteristic Legacy Latitude. |
| #define | [BT\_UUID\_GATT\_LLON\_VAL](group__bt__uuid.md#ga5d369d45c15dad30ccf7c3066863401f)   0x2a2e |
|  | GATT Characteristic Legacy Longitude UUID Value. |
| #define | [BT\_UUID\_GATT\_LLON](group__bt__uuid.md#gae090952d14ae3db50edabbdfc4d8ae25)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LLON\_VAL](group__bt__uuid.md#ga5d369d45c15dad30ccf7c3066863401f)) |
|  | GATT Characteristic Legacy Longitude. |
| #define | [BT\_UUID\_GATT\_POS\_2D\_VAL](group__bt__uuid.md#gaca1fdcec43844e0e6afeda46d7d60baf)   0x2a2f |
|  | GATT Characteristic Position 2D UUID Value. |
| #define | [BT\_UUID\_GATT\_POS\_2D](group__bt__uuid.md#ga21220783e6c7079bc9bd2f712b882dc6)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_POS\_2D\_VAL](group__bt__uuid.md#gaca1fdcec43844e0e6afeda46d7d60baf)) |
|  | GATT Characteristic Position 2D. |
| #define | [BT\_UUID\_GATT\_POS\_3D\_VAL](group__bt__uuid.md#ga66b1060fd8eaf94955211b87c9d940c2)   0x2a30 |
|  | GATT Characteristic Position 3D UUID Value. |
| #define | [BT\_UUID\_GATT\_POS\_3D](group__bt__uuid.md#ga56e0a35ad8138b961f68155fa2091ae1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_POS\_3D\_VAL](group__bt__uuid.md#ga66b1060fd8eaf94955211b87c9d940c2)) |
|  | GATT Characteristic Position 3D. |
| #define | [BT\_UUID\_GATT\_SR\_VAL](group__bt__uuid.md#ga862122929d6e4717d21c84efc5869da2)   0x2a31 |
|  | GATT Characteristic Scan Refresh UUID Value. |
| #define | [BT\_UUID\_GATT\_SR](group__bt__uuid.md#ga720d3e1f20d70cffe312f983224c2335)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SR\_VAL](group__bt__uuid.md#ga862122929d6e4717d21c84efc5869da2)) |
|  | GATT Characteristic Scan Refresh. |
| #define | [BT\_UUID\_HIDS\_BOOT\_KB\_OUT\_REPORT\_VAL](group__bt__uuid.md#ga79c18c840c919a2824d7bb84fa2217b5)   0x2a32 |
|  | HID Boot Keyboard Output Report Characteristic UUID value. |
| #define | [BT\_UUID\_HIDS\_BOOT\_KB\_OUT\_REPORT](group__bt__uuid.md#ga67e34824d0d393dcbb401c91690bce00)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDS\_BOOT\_KB\_OUT\_REPORT\_VAL](group__bt__uuid.md#ga79c18c840c919a2824d7bb84fa2217b5)) |
|  | HID Boot Keyboard Output Report Characteristic. |
| #define | [BT\_UUID\_HIDS\_BOOT\_MOUSE\_IN\_REPORT\_VAL](group__bt__uuid.md#ga804ec93e78855249a4a0a692314f4bf9)   0x2a33 |
|  | HID Boot Mouse Input Report Characteristic UUID value. |
| #define | [BT\_UUID\_HIDS\_BOOT\_MOUSE\_IN\_REPORT](group__bt__uuid.md#gae86aedfdbe15939df6384870e883bfa5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDS\_BOOT\_MOUSE\_IN\_REPORT\_VAL](group__bt__uuid.md#ga804ec93e78855249a4a0a692314f4bf9)) |
|  | HID Boot Mouse Input Report Characteristic. |
| #define | [BT\_UUID\_GATT\_GMC\_VAL](group__bt__uuid.md#ga95629cec83007634ec69516be8086d5a)   0x2a34 |
|  | GATT Characteristic Glucose Measurement Context UUID Value. |
| #define | [BT\_UUID\_GATT\_GMC](group__bt__uuid.md#ga1ca1906ee4fc482d5bb83664362c19ae)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_GMC\_VAL](group__bt__uuid.md#ga95629cec83007634ec69516be8086d5a)) |
|  | GATT Characteristic Glucose Measurement Context. |
| #define | [BT\_UUID\_GATT\_BPM\_VAL](group__bt__uuid.md#ga2342a077a10cbf649bb46f64e5fa24cb)   0x2a35 |
|  | GATT Characteristic Blood Pressure Measurement UUID Value. |
| #define | [BT\_UUID\_GATT\_BPM](group__bt__uuid.md#ga53f7809544d80bc8b797dfb0d0761ae2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_BPM\_VAL](group__bt__uuid.md#ga2342a077a10cbf649bb46f64e5fa24cb)) |
|  | GATT Characteristic Blood Pressure Measurement. |
| #define | [BT\_UUID\_GATT\_ICP\_VAL](group__bt__uuid.md#gaf68e5c86b67a8065ca3a1dc8ed0bd9ea)   0x2a36 |
|  | GATT Characteristic Intermediate Cuff Pressure UUID Value. |
| #define | [BT\_UUID\_GATT\_ICP](group__bt__uuid.md#ga33ffcb4cc70f133a29bbbe6c19d6e964)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ICP\_VAL](group__bt__uuid.md#gaf68e5c86b67a8065ca3a1dc8ed0bd9ea)) |
|  | GATT Characteristic Intermediate Cuff Pressure. |
| #define | [BT\_UUID\_HRS\_MEASUREMENT\_VAL](group__bt__uuid.md#ga44d502836331e3ffda5718d719e77ff6)   0x2a37 |
|  | HRS Characteristic Measurement Interval UUID value. |
| #define | [BT\_UUID\_HRS\_MEASUREMENT](group__bt__uuid.md#ga270ace7cd256a5441986d33becbbed05)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HRS\_MEASUREMENT\_VAL](group__bt__uuid.md#ga44d502836331e3ffda5718d719e77ff6)) |
|  | HRS Characteristic Measurement Interval. |
| #define | [BT\_UUID\_HRS\_BODY\_SENSOR\_VAL](group__bt__uuid.md#gafed38fc5d9727fb2b1d009975142ec44)   0x2a38 |
|  | HRS Characteristic Body Sensor Location. |
| #define | [BT\_UUID\_HRS\_BODY\_SENSOR](group__bt__uuid.md#ga6021612c89adac51569a14565f1f6dd2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HRS\_BODY\_SENSOR\_VAL](group__bt__uuid.md#gafed38fc5d9727fb2b1d009975142ec44)) |
|  | HRS Characteristic Control Point. |
| #define | [BT\_UUID\_HRS\_CONTROL\_POINT\_VAL](group__bt__uuid.md#ga83825772db7f9d5c4376a78d44d10a60)   0x2a39 |
|  | HRS Characteristic Control Point UUID value. |
| #define | [BT\_UUID\_HRS\_CONTROL\_POINT](group__bt__uuid.md#gacec1c535fc0d96bbad3083240b5a87a1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HRS\_CONTROL\_POINT\_VAL](group__bt__uuid.md#ga83825772db7f9d5c4376a78d44d10a60)) |
|  | HRS Characteristic Control Point. |
| #define | [BT\_UUID\_GATT\_REM\_VAL](group__bt__uuid.md#gadb260392b00da4d849c03718aaf7d323)   0x2a3a |
|  | GATT Characteristic Removable UUID Value. |
| #define | [BT\_UUID\_GATT\_REM](group__bt__uuid.md#ga92564b1966ed0cacd36b13cdf44b9a04)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_REM\_VAL](group__bt__uuid.md#gadb260392b00da4d849c03718aaf7d323)) |
|  | GATT Characteristic Removable. |
| #define | [BT\_UUID\_GATT\_SRVREQ\_VAL](group__bt__uuid.md#gade09ce0a6c46fc85ada2d38c3240b953)   0x2a3b |
|  | GATT Characteristic Service Required UUID Value. |
| #define | [BT\_UUID\_GATT\_SRVREQ](group__bt__uuid.md#ga66b18ba52088ed23136ffe121d350fa2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SRVREQ\_VAL](group__bt__uuid.md#gade09ce0a6c46fc85ada2d38c3240b953)) |
|  | GATT Characteristic Service Required. |
| #define | [BT\_UUID\_GATT\_SC\_TEMP\_C\_VAL](group__bt__uuid.md#ga2253ec9a6d97865c7408ea4ab18a392e)   0x2a3c |
|  | GATT Characteristic Scientific Temperature in Celsius UUID Value. |
| #define | [BT\_UUID\_GATT\_SC\_TEMP\_C](group__bt__uuid.md#ga2bb1b8f54f9cc4ef40650ad713181b49)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SC\_TEMP\_C\_VAL](group__bt__uuid.md#ga2253ec9a6d97865c7408ea4ab18a392e)) |
|  | GATT Characteristic Scientific Temperature in Celsius. |
| #define | [BT\_UUID\_GATT\_STRING\_VAL](group__bt__uuid.md#ga3b3f44113ca4a89e10d3d84eb02dd847)   0x2a3d |
|  | GATT Characteristic String UUID Value. |
| #define | [BT\_UUID\_GATT\_STRING](group__bt__uuid.md#ga4ca46824207979918b9a668cdf78e19a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_STRING\_VAL](group__bt__uuid.md#ga3b3f44113ca4a89e10d3d84eb02dd847)) |
|  | GATT Characteristic String. |
| #define | [BT\_UUID\_GATT\_NETA\_VAL](group__bt__uuid.md#gabd1aafbeaf157c4d515e5c2bae04823b)   0x2a3e |
|  | GATT Characteristic Network Availability UUID Value. |
| #define | [BT\_UUID\_GATT\_NETA](group__bt__uuid.md#ga98caa54c91df23461cac4b5db6a86330)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_NETA\_VAL](group__bt__uuid.md#gabd1aafbeaf157c4d515e5c2bae04823b)) |
|  | GATT Characteristic Network Availability. |
| #define | [BT\_UUID\_GATT\_ALRTS\_VAL](group__bt__uuid.md#ga11715889e92b0bf1942b3c4d84fa8aea)   0x2a3f |
|  | GATT Characteristic Alert Status UUID Value. |
| #define | [BT\_UUID\_GATT\_ALRTS](group__bt__uuid.md#ga0ef467a1b71b718216f08b21dca1e9b4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ALRTS\_VAL](group__bt__uuid.md#ga11715889e92b0bf1942b3c4d84fa8aea)) |
|  | GATT Characteristic Alert Status. |
| #define | [BT\_UUID\_GATT\_RCP\_VAL](group__bt__uuid.md#gaacbe74b5b9267f2398ea1bbde0300dc6)   0x2a40 |
|  | GATT Characteristic Ringer Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_RCP](group__bt__uuid.md#ga54702c100d46cb9dc358fd511dbc0b7d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RCP\_VAL](group__bt__uuid.md#gaacbe74b5b9267f2398ea1bbde0300dc6)) |
|  | GATT Characteristic Ringer Control Point. |
| #define | [BT\_UUID\_GATT\_RS\_VAL](group__bt__uuid.md#ga1479dc83c76a07d7000d3b53f8dee08d)   0x2a41 |
|  | GATT Characteristic Ringer Setting UUID Value. |
| #define | [BT\_UUID\_GATT\_RS](group__bt__uuid.md#ga5c78797bbe75b3b66cbc0d6ff1b185fa)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RS\_VAL](group__bt__uuid.md#ga1479dc83c76a07d7000d3b53f8dee08d)) |
|  | GATT Characteristic Ringer Setting. |
| #define | [BT\_UUID\_GATT\_ALRTCID\_MASK\_VAL](group__bt__uuid.md#ga46356e3da57646e2a5bf2f6bc13e903f)   0x2a42 |
|  | GATT Characteristic Alert Category ID Bit Mask UUID Value. |
| #define | [BT\_UUID\_GATT\_ALRTCID\_MASK](group__bt__uuid.md#ga7c905ac7003a24680ea6b2d3eeaee801)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ALRTCID\_MASK\_VAL](group__bt__uuid.md#ga46356e3da57646e2a5bf2f6bc13e903f)) |
|  | GATT Characteristic Alert Category ID Bit Mask. |
| #define | [BT\_UUID\_GATT\_ALRTCID\_VAL](group__bt__uuid.md#gab8423dbeb2c21e6c7bc90fcfe34c3a3a)   0x2a43 |
|  | GATT Characteristic Alert Category ID UUID Value. |
| #define | [BT\_UUID\_GATT\_ALRTCID](group__bt__uuid.md#ga207107524e82a8a34dc06263b434325f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ALRTCID\_VAL](group__bt__uuid.md#gab8423dbeb2c21e6c7bc90fcfe34c3a3a)) |
|  | GATT Characteristic Alert Category ID. |
| #define | [BT\_UUID\_GATT\_ALRTNCP\_VAL](group__bt__uuid.md#ga0ef4d1008dcfafce23b10ff3e9f13407)   0x2a44 |
|  | GATT Characteristic Alert Notification Control Point Value. |
| #define | [BT\_UUID\_GATT\_ALRTNCP](group__bt__uuid.md#ga0c0c2f7825242e43ad13c070d1a8c137)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ALRTNCP\_VAL](group__bt__uuid.md#ga0ef4d1008dcfafce23b10ff3e9f13407)) |
|  | GATT Characteristic Alert Notification Control Point. |
| #define | [BT\_UUID\_GATT\_UALRTS\_VAL](group__bt__uuid.md#gacfacfd310975fb4fd6f25c33e658dfaa)   0x2a45 |
|  | GATT Characteristic Unread Alert Status UUID Value. |
| #define | [BT\_UUID\_GATT\_UALRTS](group__bt__uuid.md#gacf608b24c1f0c1d10fdabd8594fe91d4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_UALRTS\_VAL](group__bt__uuid.md#gacfacfd310975fb4fd6f25c33e658dfaa)) |
|  | GATT Characteristic Unread Alert Status. |
| #define | [BT\_UUID\_GATT\_NALRT\_VAL](group__bt__uuid.md#ga61f32ab52c24492cc2a1f0c9ee042987)   0x2a46 |
|  | GATT Characteristic New Alert UUID Value. |
| #define | [BT\_UUID\_GATT\_NALRT](group__bt__uuid.md#gac66637f6bdb5c4efb56739ac3a370032)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_NALRT\_VAL](group__bt__uuid.md#ga61f32ab52c24492cc2a1f0c9ee042987)) |
|  | GATT Characteristic New Alert. |
| #define | [BT\_UUID\_GATT\_SNALRTC\_VAL](group__bt__uuid.md#ga2cc802e286be6c6d97835bc21eaa0433)   0x2a47 |
|  | GATT Characteristic Supported New Alert Category UUID Value. |
| #define | [BT\_UUID\_GATT\_SNALRTC](group__bt__uuid.md#ga30a9d308743e751e56890d48f6ef606b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SNALRTC\_VAL](group__bt__uuid.md#ga2cc802e286be6c6d97835bc21eaa0433)) |
|  | GATT Characteristic Supported New Alert Category. |
| #define | [BT\_UUID\_GATT\_SUALRTC\_VAL](group__bt__uuid.md#ga64a81cfd5ce67cd6c1d27f0a7e7433bd)   0x2a48 |
|  | GATT Characteristic Supported Unread Alert Category UUID Value. |
| #define | [BT\_UUID\_GATT\_SUALRTC](group__bt__uuid.md#ga771c8d083004c4ef49e3334909f3d317)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SUALRTC\_VAL](group__bt__uuid.md#ga64a81cfd5ce67cd6c1d27f0a7e7433bd)) |
|  | GATT Characteristic Supported Unread Alert Category. |
| #define | [BT\_UUID\_GATT\_BPF\_VAL](group__bt__uuid.md#gae5d786f2be340c5f126be0f500ade1f8)   0x2a49 |
|  | GATT Characteristic Blood Pressure Feature UUID Value. |
| #define | [BT\_UUID\_GATT\_BPF](group__bt__uuid.md#ga639e0f8fe154cca9773dd84e21ecc4d5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_BPF\_VAL](group__bt__uuid.md#gae5d786f2be340c5f126be0f500ade1f8)) |
|  | GATT Characteristic Blood Pressure Feature. |
| #define | [BT\_UUID\_HIDS\_INFO\_VAL](group__bt__uuid.md#ga929e50a821031cfb9c0faa3e2b0e9c4a)   0x2a4a |
|  | HID Information Characteristic UUID value. |
| #define | [BT\_UUID\_HIDS\_INFO](group__bt__uuid.md#ga28724b6efade76bfebeca2e8d7f9cdba)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDS\_INFO\_VAL](group__bt__uuid.md#ga929e50a821031cfb9c0faa3e2b0e9c4a)) |
|  | HID Information Characteristic. |
| #define | [BT\_UUID\_HIDS\_REPORT\_MAP\_VAL](group__bt__uuid.md#ga8b3812488738cf6202586b9202403663)   0x2a4b |
|  | HID Report Map Characteristic UUID value. |
| #define | [BT\_UUID\_HIDS\_REPORT\_MAP](group__bt__uuid.md#ga20a3521c85acd563064c5fc7ac022cda)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDS\_REPORT\_MAP\_VAL](group__bt__uuid.md#ga8b3812488738cf6202586b9202403663)) |
|  | HID Report Map Characteristic. |
| #define | [BT\_UUID\_HIDS\_CTRL\_POINT\_VAL](group__bt__uuid.md#gabd625952d5706e851ff40b04e3d86547)   0x2a4c |
|  | HID Control Point Characteristic UUID value. |
| #define | [BT\_UUID\_HIDS\_CTRL\_POINT](group__bt__uuid.md#ga8d867aac6ce50f6196c987438aa34c51)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDS\_CTRL\_POINT\_VAL](group__bt__uuid.md#gabd625952d5706e851ff40b04e3d86547)) |
|  | HID Control Point Characteristic. |
| #define | [BT\_UUID\_HIDS\_REPORT\_VAL](group__bt__uuid.md#gad6eea2097a8432254fd82ce3798869d7)   0x2a4d |
|  | HID Report Characteristic UUID value. |
| #define | [BT\_UUID\_HIDS\_REPORT](group__bt__uuid.md#ga76e590c2499cc6d7540b0bbce20daec9)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDS\_REPORT\_VAL](group__bt__uuid.md#gad6eea2097a8432254fd82ce3798869d7)) |
|  | HID Report Characteristic. |
| #define | [BT\_UUID\_HIDS\_PROTOCOL\_MODE\_VAL](group__bt__uuid.md#ga7de83d3e0472f4edb4821e75fc209aff)   0x2a4e |
|  | HID Protocol Mode Characteristic UUID value. |
| #define | [BT\_UUID\_HIDS\_PROTOCOL\_MODE](group__bt__uuid.md#ga88f780ded3c66387af8825d7a3a1c8ba)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDS\_PROTOCOL\_MODE\_VAL](group__bt__uuid.md#ga7de83d3e0472f4edb4821e75fc209aff)) |
|  | HID Protocol Mode Characteristic. |
| #define | [BT\_UUID\_GATT\_SIW\_VAL](group__bt__uuid.md#gacc5bebeb6cd2fb4c1b0bc7a78a9c67a2)   0x2a4f |
|  | GATT Characteristic Scan Interval Windows UUID Value. |
| #define | [BT\_UUID\_GATT\_SIW](group__bt__uuid.md#ga2bc786ce9acf331708f874261ab457d7)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SIW\_VAL](group__bt__uuid.md#gacc5bebeb6cd2fb4c1b0bc7a78a9c67a2)) |
|  | GATT Characteristic Scan Interval Windows. |
| #define | [BT\_UUID\_DIS\_PNP\_ID\_VAL](group__bt__uuid.md#gab01c14fa28140cae03cae611ee1d32a1)   0x2a50 |
|  | DIS Characteristic PnP ID UUID value. |
| #define | [BT\_UUID\_DIS\_PNP\_ID](group__bt__uuid.md#ga259ece0a5de917da4a497563197bcafe)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DIS\_PNP\_ID\_VAL](group__bt__uuid.md#gab01c14fa28140cae03cae611ee1d32a1)) |
|  | DIS Characteristic PnP ID. |
| #define | [BT\_UUID\_GATT\_GF\_VAL](group__bt__uuid.md#gaea2d0fd8564007e96dcdcab634896fd7)   0x2a51 |
|  | GATT Characteristic Glucose Feature UUID Value. |
| #define | [BT\_UUID\_GATT\_GF](group__bt__uuid.md#ga71ef8682466bc0418dfa848bf83af96c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_GF\_VAL](group__bt__uuid.md#gaea2d0fd8564007e96dcdcab634896fd7)) |
|  | GATT Characteristic Glucose Feature. |
| #define | [BT\_UUID\_RECORD\_ACCESS\_CONTROL\_POINT\_VAL](group__bt__uuid.md#ga413047b20718bddff95b45e1be0b5125)   0x2a52 |
|  | Record Access Control Point Characteristic value. |
| #define | [BT\_UUID\_RECORD\_ACCESS\_CONTROL\_POINT](group__bt__uuid.md#ga8eedb1ff835988f3969a1b38713a6636)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_RECORD\_ACCESS\_CONTROL\_POINT\_VAL](group__bt__uuid.md#ga413047b20718bddff95b45e1be0b5125)) |
|  | Record Access Control Point. |
| #define | [BT\_UUID\_RSC\_MEASUREMENT\_VAL](group__bt__uuid.md#ga68f55222e780136b2c88ed9615c08f4e)   0x2a53 |
|  | RSC Measurement Characteristic UUID value. |
| #define | [BT\_UUID\_RSC\_MEASUREMENT](group__bt__uuid.md#ga14a447a839d13bdc879da42399e39e63)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_RSC\_MEASUREMENT\_VAL](group__bt__uuid.md#ga68f55222e780136b2c88ed9615c08f4e)) |
|  | RSC Measurement Characteristic. |
| #define | [BT\_UUID\_RSC\_FEATURE\_VAL](group__bt__uuid.md#ga9f07e47cd086e3158f637dc2266f7acb)   0x2a54 |
|  | RSC Feature Characteristic UUID value. |
| #define | [BT\_UUID\_RSC\_FEATURE](group__bt__uuid.md#ga4f64ed5b7c06c530320a9fa68794af3a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_RSC\_FEATURE\_VAL](group__bt__uuid.md#ga9f07e47cd086e3158f637dc2266f7acb)) |
|  | RSC Feature Characteristic. |
| #define | [BT\_UUID\_SC\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gad4fd923bb1733c2e9dd993cafa8b5b01)   0x2a55 |
|  | SC Control Point Characteristic UUID value. |
| #define | [BT\_UUID\_SC\_CONTROL\_POINT](group__bt__uuid.md#ga9d6efa914c5a83dcd39ec502e5ac4178)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_SC\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gad4fd923bb1733c2e9dd993cafa8b5b01)) |
|  | SC Control Point Characteristic. |
| #define | [BT\_UUID\_GATT\_DI\_VAL](group__bt__uuid.md#gab1af32d2ba06891961e32b46917b39ab)   0x2a56 |
|  | GATT Characteristic Digital Input UUID Value. |
| #define | [BT\_UUID\_GATT\_DI](group__bt__uuid.md#ga8c4a4fd21416af1be4a0ff2760c48786)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DI\_VAL](group__bt__uuid.md#gab1af32d2ba06891961e32b46917b39ab)) |
|  | GATT Characteristic Digital Input. |
| #define | [BT\_UUID\_GATT\_DO\_VAL](group__bt__uuid.md#gad9c70984dc907efd40e3652603012ada)   0x2a57 |
|  | GATT Characteristic Digital Output UUID Value. |
| #define | [BT\_UUID\_GATT\_DO](group__bt__uuid.md#gab39f19f3e38e8954cac13c4ba6db2234)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DO\_VAL](group__bt__uuid.md#gad9c70984dc907efd40e3652603012ada)) |
|  | GATT Characteristic Digital Output. |
| #define | [BT\_UUID\_GATT\_AI\_VAL](group__bt__uuid.md#ga6b9158a8808fe72710023efac16f8d7e)   0x2a58 |
|  | GATT Characteristic Analog Input UUID Value. |
| #define | [BT\_UUID\_GATT\_AI](group__bt__uuid.md#ga8f60411278ff93a3d590050ed4a87a70)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AI\_VAL](group__bt__uuid.md#ga6b9158a8808fe72710023efac16f8d7e)) |
|  | GATT Characteristic Analog Input. |
| #define | [BT\_UUID\_GATT\_AO\_VAL](group__bt__uuid.md#gae6b9567925c04cde856d656c091540fc)   0x2a59 |
|  | GATT Characteristic Analog Output UUID Value. |
| #define | [BT\_UUID\_GATT\_AO](group__bt__uuid.md#ga3f04b6880bc88de907a3c5b5e1acc10b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AO\_VAL](group__bt__uuid.md#gae6b9567925c04cde856d656c091540fc)) |
|  | GATT Characteristic Analog Output. |
| #define | [BT\_UUID\_GATT\_AGGR\_VAL](group__bt__uuid.md#gadb16be338b14fbd82f7c33b6b92502e8)   0x2a5a |
|  | GATT Characteristic Aggregate UUID Value. |
| #define | [BT\_UUID\_GATT\_AGGR](group__bt__uuid.md#ga7bc66b120e8a90631fe557c9393a7b88)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AGGR\_VAL](group__bt__uuid.md#gadb16be338b14fbd82f7c33b6b92502e8)) |
|  | GATT Characteristic Aggregate. |
| #define | [BT\_UUID\_CSC\_MEASUREMENT\_VAL](group__bt__uuid.md#ga3465d2cfa3704021b137316d04d786b1)   0x2a5b |
|  | CSC Measurement Characteristic UUID value. |
| #define | [BT\_UUID\_CSC\_MEASUREMENT](group__bt__uuid.md#gab3a6cac39fe5370fe4c23f43a165db2d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CSC\_MEASUREMENT\_VAL](group__bt__uuid.md#ga3465d2cfa3704021b137316d04d786b1)) |
|  | CSC Measurement Characteristic. |
| #define | [BT\_UUID\_CSC\_FEATURE\_VAL](group__bt__uuid.md#ga7f697ab76e21d37c62080fe0b5a0e591)   0x2a5c |
|  | CSC Feature Characteristic UUID value. |
| #define | [BT\_UUID\_CSC\_FEATURE](group__bt__uuid.md#gaa4d36cbd23dfb98f8baa5da37f7754ac)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CSC\_FEATURE\_VAL](group__bt__uuid.md#ga7f697ab76e21d37c62080fe0b5a0e591)) |
|  | CSC Feature Characteristic. |
| #define | [BT\_UUID\_SENSOR\_LOCATION\_VAL](group__bt__uuid.md#gae9aec5938fb89ffe510f66af4b330e19)   0x2a5d |
|  | Sensor Location Characteristic UUID value. |
| #define | [BT\_UUID\_SENSOR\_LOCATION](group__bt__uuid.md#gad639330b00b9f8ffcd62c6c1ef7b75d0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_SENSOR\_LOCATION\_VAL](group__bt__uuid.md#gae9aec5938fb89ffe510f66af4b330e19)) |
|  | Sensor Location Characteristic. |
| #define | [BT\_UUID\_GATT\_PLX\_SCM\_VAL](group__bt__uuid.md#ga828a25d5bd3e087a17460a6a0d10c0a9)   0x2a5e |
|  | GATT Characteristic PLX Spot-Check Measurement UUID Value. |
| #define | [BT\_UUID\_GATT\_PLX\_SCM](group__bt__uuid.md#ga0e691d0bdabf3b8df7c986b44eab4c85)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PLX\_SCM\_VAL](group__bt__uuid.md#ga828a25d5bd3e087a17460a6a0d10c0a9)) |
|  | GATT Characteristic PLX Spot-Check Measurement. |
| #define | [BT\_UUID\_GATT\_PLX\_CM\_VAL](group__bt__uuid.md#ga4eb8f3c1d2b33bac3b1e7e1d37cab6a3)   0x2a5f |
|  | GATT Characteristic PLX Continuous Measurement UUID Value. |
| #define | [BT\_UUID\_GATT\_PLX\_CM](group__bt__uuid.md#ga73cf57feba3e1388ad052ffad5832bc1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PLX\_CM\_VAL](group__bt__uuid.md#ga4eb8f3c1d2b33bac3b1e7e1d37cab6a3)) |
|  | GATT Characteristic PLX Continuous Measurement. |
| #define | [BT\_UUID\_GATT\_PLX\_F\_VAL](group__bt__uuid.md#ga8b523306abec9cadcdc742c21d86d702)   0x2a60 |
|  | GATT Characteristic PLX Features UUID Value. |
| #define | [BT\_UUID\_GATT\_PLX\_F](group__bt__uuid.md#ga146ec7d39986333cd3583bbfc8ef27fd)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PLX\_F\_VAL](group__bt__uuid.md#ga8b523306abec9cadcdc742c21d86d702)) |
|  | GATT Characteristic PLX Features. |
| #define | [BT\_UUID\_GATT\_POPE\_VAL](group__bt__uuid.md#gaef6e49a81b4c5a7a32e17ed228a0415a)   0x2a61 |
|  | GATT Characteristic Pulse Oximetry Pulastile Event UUID Value. |
| #define | [BT\_UUID\_GATT\_POPE](group__bt__uuid.md#ga7fa4ae596a22b9fef9db13a830cb8739)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_POPE\_VAL](group__bt__uuid.md#gaef6e49a81b4c5a7a32e17ed228a0415a)) |
|  | GATT Characteristic Pulse Oximetry Pulsatile Event. |
| #define | [BT\_UUID\_GATT\_POCP\_VAL](group__bt__uuid.md#gac98748753db550fcd2bf338f4e11c246)   0x2a62 |
|  | GATT Characteristic Pulse Oximetry Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_POCP](group__bt__uuid.md#ga2ae69ed734761275ae0e4eb09080207a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_POCP\_VAL](group__bt__uuid.md#gac98748753db550fcd2bf338f4e11c246)) |
|  | GATT Characteristic Pulse Oximetry Control Point. |
| #define | [BT\_UUID\_GATT\_CPS\_CPM\_VAL](group__bt__uuid.md#gabab0970b455fb1f0ea87fb3010782ed0)   0x2a63 |
|  | GATT Characteristic Cycling Power Measurement UUID Value. |
| #define | [BT\_UUID\_GATT\_CPS\_CPM](group__bt__uuid.md#ga607c07b67d8af3554e36943cea63d1b5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CPS\_CPM\_VAL](group__bt__uuid.md#gabab0970b455fb1f0ea87fb3010782ed0)) |
|  | GATT Characteristic Cycling Power Measurement. |
| #define | [BT\_UUID\_GATT\_CPS\_CPV\_VAL](group__bt__uuid.md#gac4bde8ba3ccd35dbd94018d40438b8fb)   0x2a64 |
|  | GATT Characteristic Cycling Power Vector UUID Value. |
| #define | [BT\_UUID\_GATT\_CPS\_CPV](group__bt__uuid.md#ga99de832aed97db92213ffe90efd60fd7)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CPS\_CPV\_VAL](group__bt__uuid.md#gac4bde8ba3ccd35dbd94018d40438b8fb)) |
|  | GATT Characteristic Cycling Power Vector. |
| #define | [BT\_UUID\_GATT\_CPS\_CPF\_VAL](group__bt__uuid.md#ga97647d99503cc60a335d6b9bacc693e9)   0x2a65 |
|  | GATT Characteristic Cycling Power Feature UUID Value. |
| #define | [BT\_UUID\_GATT\_CPS\_CPF](group__bt__uuid.md#ga0b7fbbfa7d539676027d0345a3ce5d83)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CPS\_CPF\_VAL](group__bt__uuid.md#ga97647d99503cc60a335d6b9bacc693e9)) |
|  | GATT Characteristic Cycling Power Feature. |
| #define | [BT\_UUID\_GATT\_CPS\_CPCP\_VAL](group__bt__uuid.md#ga1efedae02d29eeca33b7e527506169e8)   0x2a66 |
|  | GATT Characteristic Cycling Power Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_CPS\_CPCP](group__bt__uuid.md#gadc239b7879e9b3a082388331a50392c5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CPS\_CPCP\_VAL](group__bt__uuid.md#ga1efedae02d29eeca33b7e527506169e8)) |
|  | GATT Characteristic Cycling Power Control Point. |
| #define | [BT\_UUID\_GATT\_LOC\_SPD\_VAL](group__bt__uuid.md#gacc581ed161c7d5461b2d420b8b9a88f1)   0x2a67 |
|  | GATT Characteristic Location and Speed UUID Value. |
| #define | [BT\_UUID\_GATT\_LOC\_SPD](group__bt__uuid.md#gae3a4c256c950e72ecb5767b31033bcb8)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LOC\_SPD\_VAL](group__bt__uuid.md#gacc581ed161c7d5461b2d420b8b9a88f1)) |
|  | GATT Characteristic Location and Speed. |
| #define | [BT\_UUID\_GATT\_NAV\_VAL](group__bt__uuid.md#ga28c8f061887f0e0b25dff4d716a65d92)   0x2a68 |
|  | GATT Characteristic Navigation UUID Value. |
| #define | [BT\_UUID\_GATT\_NAV](group__bt__uuid.md#ga6e08e74465bf881a85136d99bec2dc3f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_NAV\_VAL](group__bt__uuid.md#ga28c8f061887f0e0b25dff4d716a65d92)) |
|  | GATT Characteristic Navigation. |
| #define | [BT\_UUID\_GATT\_PQ\_VAL](group__bt__uuid.md#ga26f80b9d40ff1a9e6718150c337a018c)   0x2a69 |
|  | GATT Characteristic Position Quality UUID Value. |
| #define | [BT\_UUID\_GATT\_PQ](group__bt__uuid.md#ga1da56c6bd8423c99aa143756415aebc5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PQ\_VAL](group__bt__uuid.md#ga26f80b9d40ff1a9e6718150c337a018c)) |
|  | GATT Characteristic Position Quality. |
| #define | [BT\_UUID\_GATT\_LNF\_VAL](group__bt__uuid.md#gab3d9abfecb080e73c7f7309cfaa2760e)   0x2a6a |
|  | GATT Characteristic LN Feature UUID Value. |
| #define | [BT\_UUID\_GATT\_LNF](group__bt__uuid.md#gaee45af0edec1f2d7528b03b3d65f37ea)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LNF\_VAL](group__bt__uuid.md#gab3d9abfecb080e73c7f7309cfaa2760e)) |
|  | GATT Characteristic LN Feature. |
| #define | [BT\_UUID\_GATT\_LNCP\_VAL](group__bt__uuid.md#ga2026b24e2189a4fc8292487b7ee94429)   0x2a6b |
|  | GATT Characteristic LN Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_LNCP](group__bt__uuid.md#ga732fde43bbaf6f4c25d824013882089d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LNCP\_VAL](group__bt__uuid.md#ga2026b24e2189a4fc8292487b7ee94429)) |
|  | GATT Characteristic LN Control Point. |
| #define | [BT\_UUID\_ELEVATION\_VAL](group__bt__uuid.md#ga9ee48bd5d6b3ad89252c04861f6d8ff9)   0x2a6c |
|  | Elevation Characteristic UUID value. |
| #define | [BT\_UUID\_ELEVATION](group__bt__uuid.md#ga6a556f695cf7c608b9667ecec3091e32)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ELEVATION\_VAL](group__bt__uuid.md#ga9ee48bd5d6b3ad89252c04861f6d8ff9)) |
|  | Elevation Characteristic. |
| #define | [BT\_UUID\_PRESSURE\_VAL](group__bt__uuid.md#ga9bb13b8b9d9212f8f7ef4559db81ab00)   0x2a6d |
|  | Pressure Characteristic UUID value. |
| #define | [BT\_UUID\_PRESSURE](group__bt__uuid.md#ga3c179c975cfd6f0797e1098d65d59654)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_PRESSURE\_VAL](group__bt__uuid.md#ga9bb13b8b9d9212f8f7ef4559db81ab00)) |
|  | Pressure Characteristic. |
| #define | [BT\_UUID\_TEMPERATURE\_VAL](group__bt__uuid.md#ga9f420dc2ff26a723fe4cbdd467e64d47)   0x2a6e |
|  | Temperature Characteristic UUID value. |
| #define | [BT\_UUID\_TEMPERATURE](group__bt__uuid.md#ga9ce10219c9d9b2f16b9bc101398a5093)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TEMPERATURE\_VAL](group__bt__uuid.md#ga9f420dc2ff26a723fe4cbdd467e64d47)) |
|  | Temperature Characteristic. |
| #define | [BT\_UUID\_HUMIDITY\_VAL](group__bt__uuid.md#gaa1739f28a51d563d6c9b77c2f7cbf081)   0x2a6f |
|  | Humidity Characteristic UUID value. |
| #define | [BT\_UUID\_HUMIDITY](group__bt__uuid.md#gae6d2caca722e06366171b25659798478)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HUMIDITY\_VAL](group__bt__uuid.md#gaa1739f28a51d563d6c9b77c2f7cbf081)) |
|  | Humidity Characteristic. |
| #define | [BT\_UUID\_TRUE\_WIND\_SPEED\_VAL](group__bt__uuid.md#gab89e34d55bd53f075dac53f0720241ba)   0x2a70 |
|  | True Wind Speed Characteristic UUID value. |
| #define | [BT\_UUID\_TRUE\_WIND\_SPEED](group__bt__uuid.md#ga1bf8b992dc79021b1a3f876b2898d25d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TRUE\_WIND\_SPEED\_VAL](group__bt__uuid.md#gab89e34d55bd53f075dac53f0720241ba)) |
|  | True Wind Speed Characteristic. |
| #define | [BT\_UUID\_TRUE\_WIND\_DIR\_VAL](group__bt__uuid.md#ga7d77a45acb17505099602df264b8bb96)   0x2a71 |
|  | True Wind Direction Characteristic UUID value. |
| #define | [BT\_UUID\_TRUE\_WIND\_DIR](group__bt__uuid.md#ga0ba41218ce4954620dfe73f06089fc96)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TRUE\_WIND\_DIR\_VAL](group__bt__uuid.md#ga7d77a45acb17505099602df264b8bb96)) |
|  | True Wind Direction Characteristic. |
| #define | [BT\_UUID\_APPARENT\_WIND\_SPEED\_VAL](group__bt__uuid.md#gad0cff10ce44864db5128c438e4be7c8d)   0x2a72 |
|  | Apparent Wind Speed Characteristic UUID value. |
| #define | [BT\_UUID\_APPARENT\_WIND\_SPEED](group__bt__uuid.md#gaf6a81b9581f029463314fb25dd100e95)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_APPARENT\_WIND\_SPEED\_VAL](group__bt__uuid.md#gad0cff10ce44864db5128c438e4be7c8d)) |
|  | Apparent Wind Speed Characteristic. |
| #define | [BT\_UUID\_APPARENT\_WIND\_DIR\_VAL](group__bt__uuid.md#ga5eb592d6e55ca89ae5cd825edae6d508)   0x2a73 |
|  | Apparent Wind Direction Characteristic UUID value. |
| #define | [BT\_UUID\_APPARENT\_WIND\_DIR](group__bt__uuid.md#ga69adddc8dc981d2b5d02ab604826e42b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_APPARENT\_WIND\_DIR\_VAL](group__bt__uuid.md#ga5eb592d6e55ca89ae5cd825edae6d508)) |
|  | Apparent Wind Direction Characteristic. |
| #define | [BT\_UUID\_GUST\_FACTOR\_VAL](group__bt__uuid.md#ga52857a87ddb7c2df50dcb8436804c7e2)   0x2a74 |
|  | Gust Factor Characteristic UUID value. |
| #define | [BT\_UUID\_GUST\_FACTOR](group__bt__uuid.md#ga0b97427c4d526e544b0fc1b778756941)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GUST\_FACTOR\_VAL](group__bt__uuid.md#ga52857a87ddb7c2df50dcb8436804c7e2)) |
|  | Gust Factor Characteristic. |
| #define | [BT\_UUID\_POLLEN\_CONCENTRATION\_VAL](group__bt__uuid.md#gaececeeeb1976c979aafafe3c892f8a59)   0x2a75 |
|  | Pollen Concentration Characteristic UUID value. |
| #define | [BT\_UUID\_POLLEN\_CONCENTRATION](group__bt__uuid.md#gaa1a189a6d6b23f6983e38124e53aa8be)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_POLLEN\_CONCENTRATION\_VAL](group__bt__uuid.md#gaececeeeb1976c979aafafe3c892f8a59)) |
|  | Pollen Concentration Characteristic. |
| #define | [BT\_UUID\_UV\_INDEX\_VAL](group__bt__uuid.md#gae30333c9b8a0b24f1fa6790872fc7a55)   0x2a76 |
|  | UV Index Characteristic UUID value. |
| #define | [BT\_UUID\_UV\_INDEX](group__bt__uuid.md#gab47898ad86865b6fd514f577e3b7d6f6)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_UV\_INDEX\_VAL](group__bt__uuid.md#gae30333c9b8a0b24f1fa6790872fc7a55)) |
|  | UV Index Characteristic. |
| #define | [BT\_UUID\_IRRADIANCE\_VAL](group__bt__uuid.md#gaa48c2c1a4c75a3b1071b0ef4ca480150)   0x2a77 |
|  | Irradiance Characteristic UUID value. |
| #define | [BT\_UUID\_IRRADIANCE](group__bt__uuid.md#ga1e5254104ebb5ccd9a1e3c0915891aad)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_IRRADIANCE\_VAL](group__bt__uuid.md#gaa48c2c1a4c75a3b1071b0ef4ca480150)) |
|  | Irradiance Characteristic. |
| #define | [BT\_UUID\_RAINFALL\_VAL](group__bt__uuid.md#ga4ed507e7f1ecd49186411efbe4fc26ee)   0x2a78 |
|  | Rainfall Characteristic UUID value. |
| #define | [BT\_UUID\_RAINFALL](group__bt__uuid.md#ga71278019b98dac06d067227ce47320ba)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_RAINFALL\_VAL](group__bt__uuid.md#ga4ed507e7f1ecd49186411efbe4fc26ee)) |
|  | Rainfall Characteristic. |
| #define | [BT\_UUID\_WIND\_CHILL\_VAL](group__bt__uuid.md#ga424993240c213443fc9e95fa9d4ea913)   0x2a79 |
|  | Wind Chill Characteristic UUID value. |
| #define | [BT\_UUID\_WIND\_CHILL](group__bt__uuid.md#ga2bd92aab9da9f594d8a061922c51a137)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_WIND\_CHILL\_VAL](group__bt__uuid.md#ga424993240c213443fc9e95fa9d4ea913)) |
|  | Wind Chill Characteristic. |
| #define | [BT\_UUID\_HEAT\_INDEX\_VAL](group__bt__uuid.md#ga3c0468464a353c37ff4994f49439d27b)   0x2a7a |
|  | Heat Index Characteristic UUID value. |
| #define | [BT\_UUID\_HEAT\_INDEX](group__bt__uuid.md#ga56c812b5eb985ff21f91fb430d89deb3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HEAT\_INDEX\_VAL](group__bt__uuid.md#ga3c0468464a353c37ff4994f49439d27b)) |
|  | Heat Index Characteristic. |
| #define | [BT\_UUID\_DEW\_POINT\_VAL](group__bt__uuid.md#gacf36659263e0a99aece77af08f4ca816)   0x2a7b |
|  | Dew Point Characteristic UUID value. |
| #define | [BT\_UUID\_DEW\_POINT](group__bt__uuid.md#gaf80bc7369817e44102e530371bdf7771)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DEW\_POINT\_VAL](group__bt__uuid.md#gacf36659263e0a99aece77af08f4ca816)) |
|  | Dew Point Characteristic. |
| #define | [BT\_UUID\_GATT\_TREND\_VAL](group__bt__uuid.md#gabb35ed33581726b5eb3bd09abe3bf090)   0x2a7c |
|  | GATT Characteristic Trend UUID Value. |
| #define | [BT\_UUID\_GATT\_TREND](group__bt__uuid.md#ga8b36445adba800c187208c2822a4c0ef)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TREND\_VAL](group__bt__uuid.md#gabb35ed33581726b5eb3bd09abe3bf090)) |
|  | GATT Characteristic Trend. |
| #define | [BT\_UUID\_DESC\_VALUE\_CHANGED\_VAL](group__bt__uuid.md#gadaf24469185095c9a64d09f9494202bd)   0x2a7d |
|  | Descriptor Value Changed Characteristic UUID value. |
| #define | [BT\_UUID\_DESC\_VALUE\_CHANGED](group__bt__uuid.md#ga12ad8a70a766261bd258c5ff96dda1d0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_DESC\_VALUE\_CHANGED\_VAL](group__bt__uuid.md#gadaf24469185095c9a64d09f9494202bd)) |
|  | Descriptor Value Changed Characteristic. |
| #define | [BT\_UUID\_GATT\_AEHRLL\_VAL](group__bt__uuid.md#gad0a8a823d03c2cfd29b330422d909468)   0x2a7e |
|  | GATT Characteristic Aerobic Heart Rate Low Limit UUID Value. |
| #define | [BT\_UUID\_GATT\_AEHRLL](group__bt__uuid.md#ga185e4267f64937fae52a15297df555d0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AEHRLL\_VAL](group__bt__uuid.md#gad0a8a823d03c2cfd29b330422d909468)) |
|  | GATT Characteristic Aerobic Heart Rate Lower Limit. |
| #define | [BT\_UUID\_GATT\_AETHR\_VAL](group__bt__uuid.md#gafe43bdafe5d04b4b5ff205ee9c4efa59)   0x2a7f |
|  | GATT Characteristic Aerobic Threshold UUID Value. |
| #define | [BT\_UUID\_GATT\_AETHR](group__bt__uuid.md#ga81826c45c657d1b6e1ab391776e37d04)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AETHR\_VAL](group__bt__uuid.md#gafe43bdafe5d04b4b5ff205ee9c4efa59)) |
|  | GATT Characteristic Aerobic Threshold. |
| #define | [BT\_UUID\_GATT\_AGE\_VAL](group__bt__uuid.md#ga783cfd994944d68e137d4101943d3665)   0x2a80 |
|  | GATT Characteristic Age UUID Value. |
| #define | [BT\_UUID\_GATT\_AGE](group__bt__uuid.md#ga76fb417fd8e60358ae753d7139be227f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AGE\_VAL](group__bt__uuid.md#ga783cfd994944d68e137d4101943d3665)) |
|  | GATT Characteristic Age. |
| #define | [BT\_UUID\_GATT\_ANHRLL\_VAL](group__bt__uuid.md#gac145e3d9d2b97eb18b059a0146bf4831)   0x2a81 |
|  | GATT Characteristic Anaerobic Heart Rate Lower Limit UUID Value. |
| #define | [BT\_UUID\_GATT\_ANHRLL](group__bt__uuid.md#ga8150d2662f87da3a2175f57236905dbd)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ANHRLL\_VAL](group__bt__uuid.md#gac145e3d9d2b97eb18b059a0146bf4831)) |
|  | GATT Characteristic Anaerobic Heart Rate Lower Limit. |
| #define | [BT\_UUID\_GATT\_ANHRUL\_VAL](group__bt__uuid.md#gaf160fd8971de7dcfd231474e928c20fd)   0x2a82 |
|  | GATT Characteristic Anaerobic Heart Rate Upper Limit UUID Value. |
| #define | [BT\_UUID\_GATT\_ANHRUL](group__bt__uuid.md#gae8c042a675573ca1078b0eacc2041a86)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ANHRUL\_VAL](group__bt__uuid.md#gaf160fd8971de7dcfd231474e928c20fd)) |
|  | GATT Characteristic Anaerobic Heart Rate Upper Limit. |
| #define | [BT\_UUID\_GATT\_ANTHR\_VAL](group__bt__uuid.md#ga21eb08c2a91f869b792b5f71135c2586)   0x2a83 |
|  | GATT Characteristic Anaerobic Threshold UUID Value. |
| #define | [BT\_UUID\_GATT\_ANTHR](group__bt__uuid.md#ga843badc1d786e621ef26b38fa973421a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ANTHR\_VAL](group__bt__uuid.md#ga21eb08c2a91f869b792b5f71135c2586)) |
|  | GATT Characteristic Anaerobic Threshold. |
| #define | [BT\_UUID\_GATT\_AEHRUL\_VAL](group__bt__uuid.md#ga4e2a18435fac380402c890284f4b9cb2)   0x2a84 |
|  | GATT Characteristic Aerobic Heart Rate Upper Limit UUID Value. |
| #define | [BT\_UUID\_GATT\_AEHRUL](group__bt__uuid.md#ga7477670294c4af4a0f55426653d382f6)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AEHRUL\_VAL](group__bt__uuid.md#ga4e2a18435fac380402c890284f4b9cb2)) |
|  | GATT Characteristic Aerobic Heart Rate Upper Limit. |
| #define | [BT\_UUID\_GATT\_DATE\_BIRTH\_VAL](group__bt__uuid.md#gab72ef81ad3ad789c024749d05cf8a132)   0x2a85 |
|  | GATT Characteristic Date of Birth UUID Value. |
| #define | [BT\_UUID\_GATT\_DATE\_BIRTH](group__bt__uuid.md#ga20f4e7f27ff0beae7239be8e69ec6cae)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DATE\_BIRTH\_VAL](group__bt__uuid.md#gab72ef81ad3ad789c024749d05cf8a132)) |
|  | GATT Characteristic Date of Birth. |
| #define | [BT\_UUID\_GATT\_DATE\_THRASS\_VAL](group__bt__uuid.md#ga896c861e50c844d821f571297f9c5e54)   0x2a86 |
|  | GATT Characteristic Date of Threshold Assessment UUID Value. |
| #define | [BT\_UUID\_GATT\_DATE\_THRASS](group__bt__uuid.md#gaf8dbfb3be192a96f6da53a897e853b52)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DATE\_THRASS\_VAL](group__bt__uuid.md#ga896c861e50c844d821f571297f9c5e54)) |
|  | GATT Characteristic Date of Threshold Assessment. |
| #define | [BT\_UUID\_GATT\_EMAIL\_VAL](group__bt__uuid.md#gaf5b2e7bd75c03612409d34874275502b)   0x2a87 |
|  | GATT Characteristic Email Address UUID Value. |
| #define | [BT\_UUID\_GATT\_EMAIL](group__bt__uuid.md#gaf81242da24e4380fcf379cfc0a1bd2d6)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_EMAIL\_VAL](group__bt__uuid.md#gaf5b2e7bd75c03612409d34874275502b)) |
|  | GATT Characteristic Email Address. |
| #define | [BT\_UUID\_GATT\_FBHRLL\_VAL](group__bt__uuid.md#ga1b56739dbd398eede2689af120d2ffab)   0x2a88 |
|  | GATT Characteristic Fat Burn Heart Rate Lower Limit UUID Value. |
| #define | [BT\_UUID\_GATT\_FBHRLL](group__bt__uuid.md#gafe6b60c5aeb090729e901de822a21179)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FBHRLL\_VAL](group__bt__uuid.md#ga1b56739dbd398eede2689af120d2ffab)) |
|  | GATT Characteristic Fat Burn Heart Rate Lower Limit. |
| #define | [BT\_UUID\_GATT\_FBHRUL\_VAL](group__bt__uuid.md#gadaed267d894b3f6637ec65c3ebcaafbe)   0x2a89 |
|  | GATT Characteristic Fat Burn Heart Rate Upper Limit UUID Value. |
| #define | [BT\_UUID\_GATT\_FBHRUL](group__bt__uuid.md#ga499864acace035767c673f7f992fb072)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FBHRUL\_VAL](group__bt__uuid.md#gadaed267d894b3f6637ec65c3ebcaafbe)) |
|  | GATT Characteristic Fat Burn Heart Rate Upper Limit. |
| #define | [BT\_UUID\_GATT\_FIRST\_NAME\_VAL](group__bt__uuid.md#ga05a1552396ae29c2e0e6f23e1e6fe41b)   0x2a8a |
|  | GATT Characteristic First Name UUID Value. |
| #define | [BT\_UUID\_GATT\_FIRST\_NAME](group__bt__uuid.md#ga5668fc0689a92ef812ed7ee1c4bdd2e4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FIRST\_NAME\_VAL](group__bt__uuid.md#ga05a1552396ae29c2e0e6f23e1e6fe41b)) |
|  | GATT Characteristic First Name. |
| #define | [BT\_UUID\_GATT\_5ZHRL\_VAL](group__bt__uuid.md#ga0bf726af2e7015a870cdd67e2e055b48)   0x2a8b |
|  | GATT Characteristic Five Zone Heart Rate Limits UUID Value. |
| #define | [BT\_UUID\_GATT\_5ZHRL](group__bt__uuid.md#ga8c7ec19973ae92bb21e2c13bdc9762e2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_5ZHRL\_VAL](group__bt__uuid.md#ga0bf726af2e7015a870cdd67e2e055b48)) |
|  | GATT Characteristic Five Zone Heart Rate Limits. |
| #define | [BT\_UUID\_GATT\_GENDER\_VAL](group__bt__uuid.md#gac5142588ca57f7c8202dab97e19c47f0)   0x2a8c |
|  | GATT Characteristic Gender UUID Value. |
| #define | [BT\_UUID\_GATT\_GENDER](group__bt__uuid.md#ga5f51ed2cf6d32af22216a9fd2d444ed3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_GENDER\_VAL](group__bt__uuid.md#gac5142588ca57f7c8202dab97e19c47f0)) |
|  | GATT Characteristic Gender. |
| #define | [BT\_UUID\_GATT\_HR\_MAX\_VAL](group__bt__uuid.md#ga8fe65597e6c89ad6fffc3f0c33169ebe)   0x2a8d |
|  | GATT Characteristic Heart Rate Max UUID Value. |
| #define | [BT\_UUID\_GATT\_HR\_MAX](group__bt__uuid.md#ga94b53abaa40569423e0a47428379f42e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_HR\_MAX\_VAL](group__bt__uuid.md#ga8fe65597e6c89ad6fffc3f0c33169ebe)) |
|  | GATT Characteristic Heart Rate Max. |
| #define | [BT\_UUID\_GATT\_HEIGHT\_VAL](group__bt__uuid.md#gaa147b4c9f91f0d0675ffba0c715154ec)   0x2a8e |
|  | GATT Characteristic Height UUID Value. |
| #define | [BT\_UUID\_GATT\_HEIGHT](group__bt__uuid.md#gab80f4d69799421d48ab61a1832a575a7)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_HEIGHT\_VAL](group__bt__uuid.md#gaa147b4c9f91f0d0675ffba0c715154ec)) |
|  | GATT Characteristic Height. |
| #define | [BT\_UUID\_GATT\_HC\_VAL](group__bt__uuid.md#gaedb0d5b971613bd7245c3f632b7a8a13)   0x2a8f |
|  | GATT Characteristic Hip Circumference UUID Value. |
| #define | [BT\_UUID\_GATT\_HC](group__bt__uuid.md#ga3c3e534e884b6b5215a43528a51ff4e3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_HC\_VAL](group__bt__uuid.md#gaedb0d5b971613bd7245c3f632b7a8a13)) |
|  | GATT Characteristic Hip Circumference. |
| #define | [BT\_UUID\_GATT\_LAST\_NAME\_VAL](group__bt__uuid.md#ga242f34d1b3dbb26c0efa62e0d23888ea)   0x2a90 |
|  | GATT Characteristic Last Name UUID Value. |
| #define | [BT\_UUID\_GATT\_LAST\_NAME](group__bt__uuid.md#gabaae49281851c5d6626ef483b90e3d53)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LAST\_NAME\_VAL](group__bt__uuid.md#ga242f34d1b3dbb26c0efa62e0d23888ea)) |
|  | GATT Characteristic Last Name. |
| #define | [BT\_UUID\_GATT\_MRHR\_VAL](group__bt__uuid.md#ga98a0f14a9a0ac32e48280b1ce441a6fd)   0x2a91 |
|  | GATT Characteristic Maximum Recommended Heart Rate> UUID Value. |
| #define | [BT\_UUID\_GATT\_MRHR](group__bt__uuid.md#gac855511d479c0c82971cadfff61a4178)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_MRHR\_VAL](group__bt__uuid.md#ga98a0f14a9a0ac32e48280b1ce441a6fd)) |
|  | GATT Characteristic Maximum Recommended Heart Rate. |
| #define | [BT\_UUID\_GATT\_RHR\_VAL](group__bt__uuid.md#gaed3bfd56abb70c0dff169c1d2813ec18)   0x2a92 |
|  | GATT Characteristic Resting Heart Rate UUID Value. |
| #define | [BT\_UUID\_GATT\_RHR](group__bt__uuid.md#ga4b425ea527897b54a0ed6871ce65b7de)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RHR\_VAL](group__bt__uuid.md#gaed3bfd56abb70c0dff169c1d2813ec18)) |
|  | GATT Characteristic Resting Heart Rate. |
| #define | [BT\_UUID\_GATT\_AEANTHR\_VAL](group__bt__uuid.md#ga5303fd51cf82df81f635cc1213b7e7c8)   0x2a93 |
|  | GATT Characteristic Sport Type for Aerobic and Anaerobic Thresholds UUID Value. |
| #define | [BT\_UUID\_GATT\_AEANTHR](group__bt__uuid.md#gaf80845ed35ef1e841c4805d1a1b346af)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AEANTHR\_VAL](group__bt__uuid.md#ga5303fd51cf82df81f635cc1213b7e7c8)) |
|  | GATT Characteristic Sport Type for Aerobic and Anaerobic Threshold. |
| #define | [BT\_UUID\_GATT\_3ZHRL\_VAL](group__bt__uuid.md#gafddfc45ece5b3f747190bd3de773ebbe)   0x2a94 |
|  | GATT Characteristic Three Zone Heart Rate Limits UUID Value. |
| #define | [BT\_UUID\_GATT\_3ZHRL](group__bt__uuid.md#ga0b303fde7bf69dfb0284034338ae1999)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_3ZHRL\_VAL](group__bt__uuid.md#gafddfc45ece5b3f747190bd3de773ebbe)) |
|  | GATT Characteristic Three Zone Heart Rate Limits. |
| #define | [BT\_UUID\_GATT\_2ZHRL\_VAL](group__bt__uuid.md#gaa252d83bfa77990bc93d98bda035fd9c)   0x2a95 |
|  | GATT Characteristic Two Zone Heart Rate Limits UUID Value. |
| #define | [BT\_UUID\_GATT\_2ZHRL](group__bt__uuid.md#ga5389bd047e5b6769083a59114ed5603b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_2ZHRL\_VAL](group__bt__uuid.md#gaa252d83bfa77990bc93d98bda035fd9c)) |
|  | GATT Characteristic Two Zone Heart Rate Limits. |
| #define | [BT\_UUID\_GATT\_VO2\_MAX\_VAL](group__bt__uuid.md#ga2e3de0e6f3ca1dbad4d7dc559f5bc093)   0x2a96 |
|  | GATT Characteristic VO2 Max UUID Value. |
| #define | [BT\_UUID\_GATT\_VO2\_MAX](group__bt__uuid.md#gaec914c8c808dc5accb82f7c707f8f9c1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_VO2\_MAX\_VAL](group__bt__uuid.md#ga2e3de0e6f3ca1dbad4d7dc559f5bc093)) |
|  | GATT Characteristic VO2 Max. |
| #define | [BT\_UUID\_GATT\_WC\_VAL](group__bt__uuid.md#ga6f843d3c3131abe778d3ec9ce1bcee7d)   0x2a97 |
|  | GATT Characteristic Waist Circumference UUID Value. |
| #define | [BT\_UUID\_GATT\_WC](group__bt__uuid.md#ga06e0730f0abf36dea42a713b22a0082a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_WC\_VAL](group__bt__uuid.md#ga6f843d3c3131abe778d3ec9ce1bcee7d)) |
|  | GATT Characteristic Waist Circumference. |
| #define | [BT\_UUID\_GATT\_WEIGHT\_VAL](group__bt__uuid.md#gabd5f45139136449cac740e99e74a9894)   0x2a98 |
|  | GATT Characteristic Weight UUID Value. |
| #define | [BT\_UUID\_GATT\_WEIGHT](group__bt__uuid.md#ga637f0da0906948ee5b7e40cc602ed167)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_WEIGHT\_VAL](group__bt__uuid.md#gabd5f45139136449cac740e99e74a9894)) |
|  | GATT Characteristic Weight. |
| #define | [BT\_UUID\_GATT\_DBCHINC\_VAL](group__bt__uuid.md#gaa88fbc8a584c60ad025447e72c5b0cb6)   0x2a99 |
|  | GATT Characteristic Database Change Increment UUID Value. |
| #define | [BT\_UUID\_GATT\_DBCHINC](group__bt__uuid.md#gafa555b52c6f195f3d01905a3923db9f3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DBCHINC\_VAL](group__bt__uuid.md#gaa88fbc8a584c60ad025447e72c5b0cb6)) |
|  | GATT Characteristic Database Change Increment. |
| #define | [BT\_UUID\_GATT\_USRIDX\_VAL](group__bt__uuid.md#gadff9aa175bd9b12f9f882e24335aada5)   0x2a9a |
|  | GATT Characteristic User Index UUID Value. |
| #define | [BT\_UUID\_GATT\_USRIDX](group__bt__uuid.md#ga34b014cdec1c5cf41a65e47234eb3f4e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_USRIDX\_VAL](group__bt__uuid.md#gadff9aa175bd9b12f9f882e24335aada5)) |
|  | GATT Characteristic User Index. |
| #define | [BT\_UUID\_GATT\_BCF\_VAL](group__bt__uuid.md#ga4cb5bc721905c8baa78dc25d9738cbad)   0x2a9b |
|  | GATT Characteristic Body Composition Feature UUID Value. |
| #define | [BT\_UUID\_GATT\_BCF](group__bt__uuid.md#ga3d96fa7aafedab4d8b2e9910a8db1029)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_BCF\_VAL](group__bt__uuid.md#ga4cb5bc721905c8baa78dc25d9738cbad)) |
|  | GATT Characteristic Body Composition Feature. |
| #define | [BT\_UUID\_GATT\_BCM\_VAL](group__bt__uuid.md#gafa981b32cb8b6babd737922ba8bf1430)   0x2a9c |
|  | GATT Characteristic Body Composition Measurement UUID Value. |
| #define | [BT\_UUID\_GATT\_BCM](group__bt__uuid.md#ga9ade71ac5e947cc41d5ab6b747232a7d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_BCM\_VAL](group__bt__uuid.md#gafa981b32cb8b6babd737922ba8bf1430)) |
|  | GATT Characteristic Body Composition Measurement. |
| #define | [BT\_UUID\_GATT\_WM\_VAL](group__bt__uuid.md#ga68a0df5e07c31bf5d532c9ef64c1568c)   0x2a9d |
|  | GATT Characteristic Weight Measurement UUID Value. |
| #define | [BT\_UUID\_GATT\_WM](group__bt__uuid.md#gab9a5d321fb5d2854d7edbe66c4d8956c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_WM\_VAL](group__bt__uuid.md#ga68a0df5e07c31bf5d532c9ef64c1568c)) |
|  | GATT Characteristic Weight Measurement. |
| #define | [BT\_UUID\_GATT\_WSF\_VAL](group__bt__uuid.md#gae5fa58f25c54cbb228d816fb58eb5eed)   0x2a9e |
|  | GATT Characteristic Weight Scale Feature UUID Value. |
| #define | [BT\_UUID\_GATT\_WSF](group__bt__uuid.md#ga7c084498045835ca6b9037758ccb437e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_WSF\_VAL](group__bt__uuid.md#gae5fa58f25c54cbb228d816fb58eb5eed)) |
|  | GATT Characteristic Weight Scale Feature. |
| #define | [BT\_UUID\_GATT\_USRCP\_VAL](group__bt__uuid.md#ga0e8380df1c605924bf794974b9a0c811)   0x2a9f |
|  | GATT Characteristic User Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_USRCP](group__bt__uuid.md#ga6cf64ee2a0564da8c5468842d4ccca72)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_USRCP\_VAL](group__bt__uuid.md#ga0e8380df1c605924bf794974b9a0c811)) |
|  | GATT Characteristic User Control Point. |
| #define | [BT\_UUID\_MAGN\_FLUX\_DENSITY\_2D\_VAL](group__bt__uuid.md#ga12df5c55e64d68377b144bbe6afc9fa1)   0x2aa0 |
|  | Magnetic Flux Density - 2D Characteristic UUID value. |
| #define | [BT\_UUID\_MAGN\_FLUX\_DENSITY\_2D](group__bt__uuid.md#ga7c6fe7de55f9167f0deb7e5793683df5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MAGN\_FLUX\_DENSITY\_2D\_VAL](group__bt__uuid.md#ga12df5c55e64d68377b144bbe6afc9fa1)) |
|  | Magnetic Flux Density - 2D Characteristic. |
| #define | [BT\_UUID\_MAGN\_FLUX\_DENSITY\_3D\_VAL](group__bt__uuid.md#ga6eab42e702b2fe2f74ee316b565b6a15)   0x2aa1 |
|  | Magnetic Flux Density - 3D Characteristic UUID value. |
| #define | [BT\_UUID\_MAGN\_FLUX\_DENSITY\_3D](group__bt__uuid.md#ga40845b75cd4b7ec5a561123f58e33f70)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MAGN\_FLUX\_DENSITY\_3D\_VAL](group__bt__uuid.md#ga6eab42e702b2fe2f74ee316b565b6a15)) |
|  | Magnetic Flux Density - 3D Characteristic. |
| #define | [BT\_UUID\_GATT\_LANG\_VAL](group__bt__uuid.md#ga1bf8e2d09646e1340f7195c90e7b53a5)   0x2aa2 |
|  | GATT Characteristic Language UUID Value. |
| #define | [BT\_UUID\_GATT\_LANG](group__bt__uuid.md#ga8738fa7d86325f46ac3560b646afd96c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LANG\_VAL](group__bt__uuid.md#ga1bf8e2d09646e1340f7195c90e7b53a5)) |
|  | GATT Characteristic Language. |
| #define | [BT\_UUID\_BAR\_PRESSURE\_TREND\_VAL](group__bt__uuid.md#ga820b05ac625c07d538697ddda5573b46)   0x2aa3 |
|  | Barometric Pressure Trend Characteristic UUID value. |
| #define | [BT\_UUID\_BAR\_PRESSURE\_TREND](group__bt__uuid.md#ga1fcf3463c69e2974877bfa953c9cbe52)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAR\_PRESSURE\_TREND\_VAL](group__bt__uuid.md#ga820b05ac625c07d538697ddda5573b46)) |
|  | Barometric Pressure Trend Characteristic. |
| #define | [BT\_UUID\_BMS\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gaa3b803e6b55d72d830f0ee01cfc1c1f4)   0x2aa4 |
|  | Bond Management Control Point UUID value. |
| #define | [BT\_UUID\_BMS\_CONTROL\_POINT](group__bt__uuid.md#ga08c91b0e746cce311a0c96bf4347d300)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BMS\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gaa3b803e6b55d72d830f0ee01cfc1c1f4)) |
|  | Bond Management Control Point. |
| #define | [BT\_UUID\_BMS\_FEATURE\_VAL](group__bt__uuid.md#ga666cd38fd2225997e302c0517b7d7070)   0x2aa5 |
|  | Bond Management Feature UUID value. |
| #define | [BT\_UUID\_BMS\_FEATURE](group__bt__uuid.md#ga1d998f7915295eeec0895cfa9d500482)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BMS\_FEATURE\_VAL](group__bt__uuid.md#ga666cd38fd2225997e302c0517b7d7070)) |
|  | Bond Management Feature. |
| #define | [BT\_UUID\_CENTRAL\_ADDR\_RES\_VAL](group__bt__uuid.md#gad7e8753c103960268eafdf4b8fa5710e)   0x2aa6 |
|  | Central Address Resolution Characteristic UUID value. |
| #define | [BT\_UUID\_CENTRAL\_ADDR\_RES](group__bt__uuid.md#gaf3c3da6a9485674f8865764a831e6011)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CENTRAL\_ADDR\_RES\_VAL](group__bt__uuid.md#gad7e8753c103960268eafdf4b8fa5710e)) |
|  | Central Address Resolution Characteristic. |
| #define | [BT\_UUID\_CGM\_MEASUREMENT\_VAL](group__bt__uuid.md#gacec2ac2f394b7d8af60163568581c9ac)   0x2aa7 |
|  | CGM Measurement Characteristic value. |
| #define | [BT\_UUID\_CGM\_MEASUREMENT](group__bt__uuid.md#ga634603e1545a177d0ccfad140103f7e5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CGM\_MEASUREMENT\_VAL](group__bt__uuid.md#gacec2ac2f394b7d8af60163568581c9ac)) |
|  | CGM Measurement Characteristic. |
| #define | [BT\_UUID\_CGM\_FEATURE\_VAL](group__bt__uuid.md#ga693fb44bd4fe9b2da9071b04170bed8a)   0x2aa8 |
|  | CGM Feature Characteristic value. |
| #define | [BT\_UUID\_CGM\_FEATURE](group__bt__uuid.md#ga6be4b6b21e0c5f1dd06f45e309cc4097)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CGM\_FEATURE\_VAL](group__bt__uuid.md#ga693fb44bd4fe9b2da9071b04170bed8a)) |
|  | CGM Feature Characteristic. |
| #define | [BT\_UUID\_CGM\_STATUS\_VAL](group__bt__uuid.md#ga0c2ebf2de8e5f2a83ebc2f11a6a79441)   0x2aa9 |
|  | CGM Status Characteristic value. |
| #define | [BT\_UUID\_CGM\_STATUS](group__bt__uuid.md#ga040dec91474ceaf096c2864eb0f46bff)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CGM\_STATUS\_VAL](group__bt__uuid.md#ga0c2ebf2de8e5f2a83ebc2f11a6a79441)) |
|  | CGM Status Characteristic. |
| #define | [BT\_UUID\_CGM\_SESSION\_START\_TIME\_VAL](group__bt__uuid.md#ga6f646767f25f2d94cb1190ad4acef86f)   0x2aaa |
|  | CGM Session Start Time Characteristic value. |
| #define | [BT\_UUID\_CGM\_SESSION\_START\_TIME](group__bt__uuid.md#ga0f17cfb12a8c4d628a26f7c83c8a7f4b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CGM\_SESSION\_START\_TIME\_VAL](group__bt__uuid.md#ga6f646767f25f2d94cb1190ad4acef86f)) |
|  | CGM Session Start Time. |
| #define | [BT\_UUID\_CGM\_SESSION\_RUN\_TIME\_VAL](group__bt__uuid.md#ga98d88d1b785d3b71b9e3b95864efdbf7)   0x2aab |
|  | CGM Session Run Time Characteristic value. |
| #define | [BT\_UUID\_CGM\_SESSION\_RUN\_TIME](group__bt__uuid.md#ga0f8565339251160fb439d06f5b29b4cf)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CGM\_SESSION\_RUN\_TIME\_VAL](group__bt__uuid.md#ga98d88d1b785d3b71b9e3b95864efdbf7)) |
|  | CGM Session Run Time. |
| #define | [BT\_UUID\_CGM\_SPECIFIC\_OPS\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gaec1bbb364e33912fcc22e63c369e4c77)   0x2aac |
|  | CGM Specific Ops Control Point Characteristic value. |
| #define | [BT\_UUID\_CGM\_SPECIFIC\_OPS\_CONTROL\_POINT](group__bt__uuid.md#ga820aab0acff43919e2710b3d5f93ef4b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CGM\_SPECIFIC\_OPS\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gaec1bbb364e33912fcc22e63c369e4c77)) |
|  | CGM Specific Ops Control Point. |
| #define | [BT\_UUID\_GATT\_IPC\_VAL](group__bt__uuid.md#gafe31f631bf3f9a232214dafa76b35ba6)   0x2aad |
|  | GATT Characteristic Indoor Positioning Configuration UUID Value. |
| #define | [BT\_UUID\_GATT\_IPC](group__bt__uuid.md#ga350bcb39fe9c71f12e5661e4157e95f2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IPC\_VAL](group__bt__uuid.md#gafe31f631bf3f9a232214dafa76b35ba6)) |
|  | GATT Characteristic Indoor Positioning Configuration. |
| #define | [BT\_UUID\_GATT\_LAT\_VAL](group__bt__uuid.md#gadda62951b9abf642684b266f1f073856)   0x2aae |
|  | GATT Characteristic Latitude UUID Value. |
| #define | [BT\_UUID\_GATT\_LAT](group__bt__uuid.md#ga0dcbbd018fd83efcb84721146fa8c47d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LAT\_VAL](group__bt__uuid.md#gadda62951b9abf642684b266f1f073856)) |
|  | GATT Characteristic Latitude. |
| #define | [BT\_UUID\_GATT\_LON\_VAL](group__bt__uuid.md#ga89312e66f25972bced92a8ea1574037a)   0x2aaf |
|  | GATT Characteristic Longitude UUID Value. |
| #define | [BT\_UUID\_GATT\_LON](group__bt__uuid.md#ga59aa1b51e5948c649d0d49d5d7fe45ed)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LON\_VAL](group__bt__uuid.md#ga89312e66f25972bced92a8ea1574037a)) |
|  | GATT Characteristic Longitude. |
| #define | [BT\_UUID\_GATT\_LNCOORD\_VAL](group__bt__uuid.md#gab8183450fa0b94f92709a76f58ce041c)   0x2ab0 |
|  | GATT Characteristic Local North Coordinate UUID Value. |
| #define | [BT\_UUID\_GATT\_LNCOORD](group__bt__uuid.md#gaf1294000d6653870589cd0d4e2d3f05f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LNCOORD\_VAL](group__bt__uuid.md#gab8183450fa0b94f92709a76f58ce041c)) |
|  | GATT Characteristic Local North Coordinate. |
| #define | [BT\_UUID\_GATT\_LECOORD\_VAL](group__bt__uuid.md#ga700e5b0a5be6ba38c882692da43e41f0)   0x2ab1 |
|  | GATT Characteristic Local East Coordinate UUID Value. |
| #define | [BT\_UUID\_GATT\_LECOORD](group__bt__uuid.md#gac7d73c69f971bad67095ee6ad03ed0f2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LECOORD\_VAL](group__bt__uuid.md#ga700e5b0a5be6ba38c882692da43e41f0)) |
|  | GATT Characteristic Local East Coordinate. |
| #define | [BT\_UUID\_GATT\_FN\_VAL](group__bt__uuid.md#ga64e22e58c78f09f8614079bb8cd4092e)   0x2ab2 |
|  | GATT Characteristic Floor Number UUID Value. |
| #define | [BT\_UUID\_GATT\_FN](group__bt__uuid.md#ga7fd58fd3410975a1a66f03bdcebabdc3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FN\_VAL](group__bt__uuid.md#ga64e22e58c78f09f8614079bb8cd4092e)) |
|  | GATT Characteristic Floor Number. |
| #define | [BT\_UUID\_GATT\_ALT\_VAL](group__bt__uuid.md#ga5b30f97c97ee5006390ab895f4bc438e)   0x2ab3 |
|  | GATT Characteristic Altitude UUID Value. |
| #define | [BT\_UUID\_GATT\_ALT](group__bt__uuid.md#ga10bdfef928a7cd1da6bf3b3406121c99)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ALT\_VAL](group__bt__uuid.md#ga5b30f97c97ee5006390ab895f4bc438e)) |
|  | GATT Characteristic Altitude. |
| #define | [BT\_UUID\_GATT\_UNCERTAINTY\_VAL](group__bt__uuid.md#gaeff0f6c7ab86eb8b264d80d579ad4aa5)   0x2ab4 |
|  | GATT Characteristic Uncertainty UUID Value. |
| #define | [BT\_UUID\_GATT\_UNCERTAINTY](group__bt__uuid.md#ga5fc1842a9886deb02cc28887b2e21155)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_UNCERTAINTY\_VAL](group__bt__uuid.md#gaeff0f6c7ab86eb8b264d80d579ad4aa5)) |
|  | GATT Characteristic Uncertainty. |
| #define | [BT\_UUID\_GATT\_LOC\_NAME\_VAL](group__bt__uuid.md#gaa7c22c7d434e3a9b9e2f3f44bd75dad1)   0x2ab5 |
|  | GATT Characteristic Location Name UUID Value. |
| #define | [BT\_UUID\_GATT\_LOC\_NAME](group__bt__uuid.md#gaa5418e610552e13acaa2c675564ae776)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LOC\_NAME\_VAL](group__bt__uuid.md#gaa7c22c7d434e3a9b9e2f3f44bd75dad1)) |
|  | GATT Characteristic Location Name. |
| #define | [BT\_UUID\_URI\_VAL](group__bt__uuid.md#gafb86347f61b0e745bf3b970eb6cf71b0)   0x2ab6 |
|  | URI UUID value. |
| #define | [BT\_UUID\_URI](group__bt__uuid.md#gaee04f3121fa14082ffabc4d705325449)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_URI\_VAL](group__bt__uuid.md#gafb86347f61b0e745bf3b970eb6cf71b0)) |
|  | URI. |
| #define | [BT\_UUID\_HTTP\_HEADERS\_VAL](group__bt__uuid.md#gaf489c9885e90b49b0f072d365c6a7098)   0x2ab7 |
|  | HTTP Headers UUID value. |
| #define | [BT\_UUID\_HTTP\_HEADERS](group__bt__uuid.md#gad88c1b58957bbcc2df817628a6f756db)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTTP\_HEADERS\_VAL](group__bt__uuid.md#gaf489c9885e90b49b0f072d365c6a7098)) |
|  | HTTP Headers. |
| #define | [BT\_UUID\_HTTP\_STATUS\_CODE\_VAL](group__bt__uuid.md#ga257e4213c8e4aa4e6b61dba44e36b268)   0x2ab8 |
|  | HTTP Status Code UUID value. |
| #define | [BT\_UUID\_HTTP\_STATUS\_CODE](group__bt__uuid.md#gaf2e15b1eabca8c810e7f61ee0d650450)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTTP\_STATUS\_CODE\_VAL](group__bt__uuid.md#ga257e4213c8e4aa4e6b61dba44e36b268)) |
|  | HTTP Status Code. |
| #define | [BT\_UUID\_HTTP\_ENTITY\_BODY\_VAL](group__bt__uuid.md#ga84600520548f966e511355ee94edbcde)   0x2ab9 |
|  | HTTP Entity Body UUID value. |
| #define | [BT\_UUID\_HTTP\_ENTITY\_BODY](group__bt__uuid.md#ga2336a53590edbb9ba14c7aacfa36a592)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTTP\_ENTITY\_BODY\_VAL](group__bt__uuid.md#ga84600520548f966e511355ee94edbcde)) |
|  | HTTP Entity Body. |
| #define | [BT\_UUID\_HTTP\_CONTROL\_POINT\_VAL](group__bt__uuid.md#ga37eb19663266e076c35cfa0c73dd0f4f)   0x2aba |
|  | HTTP Control Point UUID value. |
| #define | [BT\_UUID\_HTTP\_CONTROL\_POINT](group__bt__uuid.md#ga996630b67869b95babf5f7b280f26c49)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTTP\_CONTROL\_POINT\_VAL](group__bt__uuid.md#ga37eb19663266e076c35cfa0c73dd0f4f)) |
|  | HTTP Control Point. |
| #define | [BT\_UUID\_HTTPS\_SECURITY\_VAL](group__bt__uuid.md#gacaa02070d2036c0cc76b16437e1cc62b)   0x2abb |
|  | HTTPS Security UUID value. |
| #define | [BT\_UUID\_HTTPS\_SECURITY](group__bt__uuid.md#ga365519de0ab148b5820442eca52ad700)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTTPS\_SECURITY\_VAL](group__bt__uuid.md#gacaa02070d2036c0cc76b16437e1cc62b)) |
|  | HTTPS Security. |
| #define | [BT\_UUID\_GATT\_TDS\_CP\_VAL](group__bt__uuid.md#ga44d037f49e771f08da2381c981fb6ea6)   0x2abc |
|  | GATT Characteristic TDS Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_TDS\_CP](group__bt__uuid.md#ga90f08ee842d221580b036d154417c122)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TDS\_CP\_VAL](group__bt__uuid.md#ga44d037f49e771f08da2381c981fb6ea6)) |
|  | GATT Characteristic TDS Control Point. |
| #define | [BT\_UUID\_OTS\_FEATURE\_VAL](group__bt__uuid.md#ga763bb4a64fa3ba2cd3680858d24dd200)   0x2abd |
|  | OTS Feature Characteristic UUID value. |
| #define | [BT\_UUID\_OTS\_FEATURE](group__bt__uuid.md#ga6bf7967b64150e3bc7f849fa19ddfe7c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_FEATURE\_VAL](group__bt__uuid.md#ga763bb4a64fa3ba2cd3680858d24dd200)) |
|  | OTS Feature Characteristic. |
| #define | [BT\_UUID\_OTS\_NAME\_VAL](group__bt__uuid.md#ga4768610413b66751e9e38eef00bc4516)   0x2abe |
|  | OTS Object Name Characteristic UUID value. |
| #define | [BT\_UUID\_OTS\_NAME](group__bt__uuid.md#gaa6b72769537df80ba5450b6a398b21ff)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_NAME\_VAL](group__bt__uuid.md#ga4768610413b66751e9e38eef00bc4516)) |
|  | OTS Object Name Characteristic. |
| #define | [BT\_UUID\_OTS\_TYPE\_VAL](group__bt__uuid.md#ga1e313ee3c5d5047b8d629d99976c1e32)   0x2abf |
|  | OTS Object Type Characteristic UUID value. |
| #define | [BT\_UUID\_OTS\_TYPE](group__bt__uuid.md#ga94b169c80d3d351c85535d085366086b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_TYPE\_VAL](group__bt__uuid.md#ga1e313ee3c5d5047b8d629d99976c1e32)) |
|  | OTS Object Type Characteristic. |
| #define | [BT\_UUID\_OTS\_SIZE\_VAL](group__bt__uuid.md#ga6072d84794782c93b6c8cb5f30707d9d)   0x2ac0 |
|  | OTS Object Size Characteristic UUID value. |
| #define | [BT\_UUID\_OTS\_SIZE](group__bt__uuid.md#gae24957c8aad49fc0f98570b6b313098a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_SIZE\_VAL](group__bt__uuid.md#ga6072d84794782c93b6c8cb5f30707d9d)) |
|  | OTS Object Size Characteristic. |
| #define | [BT\_UUID\_OTS\_FIRST\_CREATED\_VAL](group__bt__uuid.md#gab0c3ef2ee627f77c46cc78ec1b6e5543)   0x2ac1 |
|  | OTS Object First-Created Characteristic UUID value. |
| #define | [BT\_UUID\_OTS\_FIRST\_CREATED](group__bt__uuid.md#gae5ac09c297a770ebbf7f2a344d24d153)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_FIRST\_CREATED\_VAL](group__bt__uuid.md#gab0c3ef2ee627f77c46cc78ec1b6e5543)) |
|  | OTS Object First-Created Characteristic. |
| #define | [BT\_UUID\_OTS\_LAST\_MODIFIED\_VAL](group__bt__uuid.md#gaa9016cda30f09bd61b38654d87198694)   0x2ac2 |
|  | OTS Object Last-Modified Characteristic UUI value. |
| #define | [BT\_UUID\_OTS\_LAST\_MODIFIED](group__bt__uuid.md#ga06f1570cde6df5e932c72417fe59daef)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_LAST\_MODIFIED\_VAL](group__bt__uuid.md#gaa9016cda30f09bd61b38654d87198694)) |
|  | OTS Object Last-Modified Characteristic. |
| #define | [BT\_UUID\_OTS\_ID\_VAL](group__bt__uuid.md#gad32cdd62e0bead3599de3b3dd6e4e014)   0x2ac3 |
|  | OTS Object ID Characteristic UUID value. |
| #define | [BT\_UUID\_OTS\_ID](group__bt__uuid.md#gaf301617baf5a039c202f0993d80061ce)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_ID\_VAL](group__bt__uuid.md#gad32cdd62e0bead3599de3b3dd6e4e014)) |
|  | OTS Object ID Characteristic. |
| #define | [BT\_UUID\_OTS\_PROPERTIES\_VAL](group__bt__uuid.md#ga0360f97a4f18b56ae3dac4e9b0287602)   0x2ac4 |
|  | OTS Object Properties Characteristic UUID value. |
| #define | [BT\_UUID\_OTS\_PROPERTIES](group__bt__uuid.md#ga215d8088166c529ad1d0024a8f362e3e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_PROPERTIES\_VAL](group__bt__uuid.md#ga0360f97a4f18b56ae3dac4e9b0287602)) |
|  | OTS Object Properties Characteristic. |
| #define | [BT\_UUID\_OTS\_ACTION\_CP\_VAL](group__bt__uuid.md#ga7ebe0c55c503cb82cf4d0ee3838f50fe)   0x2ac5 |
|  | OTS Object Action Control Point Characteristic UUID value. |
| #define | [BT\_UUID\_OTS\_ACTION\_CP](group__bt__uuid.md#ga29c7bec908eeff922e1aaa3043278d2b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_ACTION\_CP\_VAL](group__bt__uuid.md#ga7ebe0c55c503cb82cf4d0ee3838f50fe)) |
|  | OTS Object Action Control Point Characteristic. |
| #define | [BT\_UUID\_OTS\_LIST\_CP\_VAL](group__bt__uuid.md#ga145f367de3db51b96ea6922017380aa3)   0x2ac6 |
|  | OTS Object List Control Point Characteristic UUID value. |
| #define | [BT\_UUID\_OTS\_LIST\_CP](group__bt__uuid.md#ga8acbfefbe1b7cbb5a7aba290d6e7effb)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_LIST\_CP\_VAL](group__bt__uuid.md#ga145f367de3db51b96ea6922017380aa3)) |
|  | OTS Object List Control Point Characteristic. |
| #define | [BT\_UUID\_OTS\_LIST\_FILTER\_VAL](group__bt__uuid.md#ga675bd50dd63de1a13363b041eefc1634)   0x2ac7 |
|  | OTS Object List Filter Characteristic UUID value. |
| #define | [BT\_UUID\_OTS\_LIST\_FILTER](group__bt__uuid.md#gabca5bfb5f6fb4a92f29752cb686c7d88)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_LIST\_FILTER\_VAL](group__bt__uuid.md#ga675bd50dd63de1a13363b041eefc1634)) |
|  | OTS Object List Filter Characteristic. |
| #define | [BT\_UUID\_OTS\_CHANGED\_VAL](group__bt__uuid.md#gaea820a540c02088355739bf6ec6e26ba)   0x2ac8 |
|  | OTS Object Changed Characteristic UUID value. |
| #define | [BT\_UUID\_OTS\_CHANGED](group__bt__uuid.md#ga45dc6f040b210aac136b018c760ac37e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_CHANGED\_VAL](group__bt__uuid.md#gaea820a540c02088355739bf6ec6e26ba)) |
|  | OTS Object Changed Characteristic. |
| #define | [BT\_UUID\_GATT\_RPAO\_VAL](group__bt__uuid.md#ga080af564ef60858fe3ddc0c487f06e97)   0x2ac9 |
|  | GATT Characteristic Resolvable Private Address Only UUID Value. |
| #define | [BT\_UUID\_GATT\_RPAO](group__bt__uuid.md#ga5db6e037e7020b467a5218f828b8a7ea)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RPAO\_VAL](group__bt__uuid.md#ga080af564ef60858fe3ddc0c487f06e97)) |
|  | GATT Characteristic Resolvable Private Address Only. |
| #define | [BT\_UUID\_OTS\_TYPE\_UNSPECIFIED\_VAL](group__bt__uuid.md#ga74f28ba3693c541b909580c4fd262416)   0x2aca |
|  | OTS Unspecified Object Type UUID value. |
| #define | [BT\_UUID\_OTS\_TYPE\_UNSPECIFIED](group__bt__uuid.md#gadc3afb0781f51b2550b077ee24ce9227)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_TYPE\_UNSPECIFIED\_VAL](group__bt__uuid.md#ga74f28ba3693c541b909580c4fd262416)) |
|  | OTS Unspecified Object Type. |
| #define | [BT\_UUID\_OTS\_DIRECTORY\_LISTING\_VAL](group__bt__uuid.md#ga2fee72d19822abcf76cedfbfd96d4cdc)   0x2acb |
|  | OTS Directory Listing UUID value. |
| #define | [BT\_UUID\_OTS\_DIRECTORY\_LISTING](group__bt__uuid.md#ga8f306bef03ca5204c99befc1c6e71225)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_DIRECTORY\_LISTING\_VAL](group__bt__uuid.md#ga2fee72d19822abcf76cedfbfd96d4cdc)) |
|  | OTS Directory Listing. |
| #define | [BT\_UUID\_GATT\_FMF\_VAL](group__bt__uuid.md#ga556cd0fd7d3ff4f862dd3028f0206462)   0x2acc |
|  | GATT Characteristic Fitness Machine Feature UUID Value. |
| #define | [BT\_UUID\_GATT\_FMF](group__bt__uuid.md#ga2aeb2e0aa454feb4438f9527c52780ed)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FMF\_VAL](group__bt__uuid.md#ga556cd0fd7d3ff4f862dd3028f0206462)) |
|  | GATT Characteristic Fitness Machine Feature. |
| #define | [BT\_UUID\_GATT\_TD\_VAL](group__bt__uuid.md#gaedc6e4f493355fe2999e7f1f84bf5d00)   0x2acd |
|  | GATT Characteristic Treadmill Data UUID Value. |
| #define | [BT\_UUID\_GATT\_TD](group__bt__uuid.md#gaa8a7f082cf9b4df21c07ded6a4913b35)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TD\_VAL](group__bt__uuid.md#gaedc6e4f493355fe2999e7f1f84bf5d00)) |
|  | GATT Characteristic Treadmill Data. |
| #define | [BT\_UUID\_GATT\_CTD\_VAL](group__bt__uuid.md#ga235dc61fb231d43a5aaab0b32f398a48)   0x2ace |
|  | GATT Characteristic Cross Trainer Data UUID Value. |
| #define | [BT\_UUID\_GATT\_CTD](group__bt__uuid.md#ga47d30eeb1bb66bb84b8b315fbeb76eea)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CTD\_VAL](group__bt__uuid.md#ga235dc61fb231d43a5aaab0b32f398a48)) |
|  | GATT Characteristic Cross Trainer Data. |
| #define | [BT\_UUID\_GATT\_STPCD\_VAL](group__bt__uuid.md#ga84863f0507404fd9637319c384468808)   0x2acf |
|  | GATT Characteristic Step Climber Data UUID Value. |
| #define | [BT\_UUID\_GATT\_STPCD](group__bt__uuid.md#ga4fd0ee59f5451669a389814d4390c6b5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_STPCD\_VAL](group__bt__uuid.md#ga84863f0507404fd9637319c384468808)) |
|  | GATT Characteristic Step Climber Data. |
| #define | [BT\_UUID\_GATT\_STRCD\_VAL](group__bt__uuid.md#ga222ab56024893f1019af55052f646aca)   0x2ad0 |
|  | GATT Characteristic Stair Climber Data UUID Value. |
| #define | [BT\_UUID\_GATT\_STRCD](group__bt__uuid.md#gae0b7d7316806ee18c4300b399faeb52e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_STRCD\_VAL](group__bt__uuid.md#ga222ab56024893f1019af55052f646aca)) |
|  | GATT Characteristic Stair Climber Data. |
| #define | [BT\_UUID\_GATT\_RD\_VAL](group__bt__uuid.md#gaed2b696b1a2ecbe1e981437ee9e58389)   0x2ad1 |
|  | GATT Characteristic Rower Data UUID Value. |
| #define | [BT\_UUID\_GATT\_RD](group__bt__uuid.md#ga933043dfadcbebbbb2c10a828280c0a0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RD\_VAL](group__bt__uuid.md#gaed2b696b1a2ecbe1e981437ee9e58389)) |
|  | GATT Characteristic Rower Data. |
| #define | [BT\_UUID\_GATT\_IBD\_VAL](group__bt__uuid.md#ga92198d40e1a682c0c7515ba306af2093)   0x2ad2 |
|  | GATT Characteristic Indoor Bike Data UUID Value. |
| #define | [BT\_UUID\_GATT\_IBD](group__bt__uuid.md#gaf6d86dfccb1bf3796b1dbd3c087b8127)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IBD\_VAL](group__bt__uuid.md#ga92198d40e1a682c0c7515ba306af2093)) |
|  | GATT Characteristic Indoor Bike Data. |
| #define | [BT\_UUID\_GATT\_TRSTAT\_VAL](group__bt__uuid.md#ga13e94c01279818ad0ce923051bf4fd1c)   0x2ad3 |
|  | GATT Characteristic Training Status UUID Value. |
| #define | [BT\_UUID\_GATT\_TRSTAT](group__bt__uuid.md#ga5a7f9c7d6d0e93f2d35ff308b875f883)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TRSTAT\_VAL](group__bt__uuid.md#ga13e94c01279818ad0ce923051bf4fd1c)) |
|  | GATT Characteristic Training Status. |
| #define | [BT\_UUID\_GATT\_SSR\_VAL](group__bt__uuid.md#gadad6f8c3d4cf5f40c5f1f27d5ea38ac3)   0x2ad4 |
|  | GATT Characteristic Supported Speed Range UUID Value. |
| #define | [BT\_UUID\_GATT\_SSR](group__bt__uuid.md#gab6ef5e742460fba12f8b974fc4bf735d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SSR\_VAL](group__bt__uuid.md#gadad6f8c3d4cf5f40c5f1f27d5ea38ac3)) |
|  | GATT Characteristic Supported Speed Range. |
| #define | [BT\_UUID\_GATT\_SIR\_VAL](group__bt__uuid.md#ga6339f09bf4e825454fd8c517faf53194)   0x2ad5 |
|  | GATT Characteristic Supported Inclination Range UUID Value. |
| #define | [BT\_UUID\_GATT\_SIR](group__bt__uuid.md#gac69a06d1568114dec01f46df95a3c5ac)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SIR\_VAL](group__bt__uuid.md#ga6339f09bf4e825454fd8c517faf53194)) |
|  | GATT Characteristic Supported Inclination Range. |
| #define | [BT\_UUID\_GATT\_SRLR\_VAL](group__bt__uuid.md#gaf6fae4763a3aa3fe1f04b51b108ca642)   0x2ad6 |
|  | GATT Characteristic Supported Resistance Level Range UUID Value. |
| #define | [BT\_UUID\_GATT\_SRLR](group__bt__uuid.md#ga4141c63e9e7924c8d9e27922ebda4b98)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SRLR\_VAL](group__bt__uuid.md#gaf6fae4763a3aa3fe1f04b51b108ca642)) |
|  | GATT Characteristic Supported Resistance Level Range. |
| #define | [BT\_UUID\_GATT\_SHRR\_VAL](group__bt__uuid.md#ga8516dbe4b6b630f380f9ab3a80bce179)   0x2ad7 |
|  | GATT Characteristic Supported Heart Rate Range UUID Value. |
| #define | [BT\_UUID\_GATT\_SHRR](group__bt__uuid.md#gabe5693829c64f8cd98444c853e0f121c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SHRR\_VAL](group__bt__uuid.md#ga8516dbe4b6b630f380f9ab3a80bce179)) |
|  | GATT Characteristic Supported Heart Rate Range. |
| #define | [BT\_UUID\_GATT\_SPR\_VAL](group__bt__uuid.md#ga1f7f6e8197940264ff921e6dec5c2e81)   0x2ad8 |
|  | GATT Characteristic Supported Power Range UUID Value. |
| #define | [BT\_UUID\_GATT\_SPR](group__bt__uuid.md#gab82bacbce14b886d23f9368db97bb329)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SPR\_VAL](group__bt__uuid.md#ga1f7f6e8197940264ff921e6dec5c2e81)) |
|  | GATT Characteristic Supported Power Range. |
| #define | [BT\_UUID\_GATT\_FMCP\_VAL](group__bt__uuid.md#gaf910e7d5ce12084045e9283b4c5b8b7e)   0x2ad9 |
|  | GATT Characteristic Fitness Machine Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_FMCP](group__bt__uuid.md#ga26b12f1ef3313b7c28328ae22512b277)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FMCP\_VAL](group__bt__uuid.md#gaf910e7d5ce12084045e9283b4c5b8b7e)) |
|  | GATT Characteristic Fitness Machine Control Point. |
| #define | [BT\_UUID\_GATT\_FMS\_VAL](group__bt__uuid.md#gaea596e91c046949687c4331a4841dd07)   0x2ada |
|  | GATT Characteristic Fitness Machine Status UUID Value. |
| #define | [BT\_UUID\_GATT\_FMS](group__bt__uuid.md#ga9ff5045f804b6a2a8cd0b2ec8906e4b3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FMS\_VAL](group__bt__uuid.md#gaea596e91c046949687c4331a4841dd07)) |
|  | GATT Characteristic Fitness Machine Status. |
| #define | [BT\_UUID\_MESH\_PROV\_DATA\_IN\_VAL](group__bt__uuid.md#ga2bde466cfcaeec5c542d5e74f51ddd05)   0x2adb |
|  | Mesh Provisioning Data In UUID value. |
| #define | [BT\_UUID\_MESH\_PROV\_DATA\_IN](group__bt__uuid.md#gaae548e7ca5a9835bd4dcfdf853c43993)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MESH\_PROV\_DATA\_IN\_VAL](group__bt__uuid.md#ga2bde466cfcaeec5c542d5e74f51ddd05)) |
|  | Mesh Provisioning Data In. |
| #define | [BT\_UUID\_MESH\_PROV\_DATA\_OUT\_VAL](group__bt__uuid.md#gafd6e15eb3ae65d5f480706e68aabad8e)   0x2adc |
|  | Mesh Provisioning Data Out UUID value. |
| #define | [BT\_UUID\_MESH\_PROV\_DATA\_OUT](group__bt__uuid.md#gaa003522c72e96e8b2c4b7b724aa2bf2e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MESH\_PROV\_DATA\_OUT\_VAL](group__bt__uuid.md#gafd6e15eb3ae65d5f480706e68aabad8e)) |
|  | Mesh Provisioning Data Out. |
| #define | [BT\_UUID\_MESH\_PROXY\_DATA\_IN\_VAL](group__bt__uuid.md#ga55488739e50c8482da6f4ad0826f0cae)   0x2add |
|  | Mesh Proxy Data In UUID value. |
| #define | [BT\_UUID\_MESH\_PROXY\_DATA\_IN](group__bt__uuid.md#gaebcae07983c397b0771f424d2d890259)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MESH\_PROXY\_DATA\_IN\_VAL](group__bt__uuid.md#ga55488739e50c8482da6f4ad0826f0cae)) |
|  | Mesh Proxy Data In. |
| #define | [BT\_UUID\_MESH\_PROXY\_DATA\_OUT\_VAL](group__bt__uuid.md#ga452dfb3d0f4b62ec327910b9c578ffb0)   0x2ade |
|  | Mesh Proxy Data Out UUID value. |
| #define | [BT\_UUID\_MESH\_PROXY\_DATA\_OUT](group__bt__uuid.md#gaf3fbcbebb0507aec45d94244729f85d8)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MESH\_PROXY\_DATA\_OUT\_VAL](group__bt__uuid.md#ga452dfb3d0f4b62ec327910b9c578ffb0)) |
|  | Mesh Proxy Data Out. |
| #define | [BT\_UUID\_GATT\_NNN\_VAL](group__bt__uuid.md#gab01aec4c2f19b53d919c89b58fd92956)   0x2adf |
|  | GATT Characteristic New Number Needed UUID Value. |
| #define | [BT\_UUID\_GATT\_NNN](group__bt__uuid.md#ga355480e43c9fd2ee1e7fa72a05141c93)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_NNN\_VAL](group__bt__uuid.md#gab01aec4c2f19b53d919c89b58fd92956)) |
|  | GATT Characteristic New Number Needed. |
| #define | [BT\_UUID\_GATT\_AC\_VAL](group__bt__uuid.md#gaf2bc7408a53341478f1b41d54e888478)   0x2ae0 |
|  | GATT Characteristic Average Current UUID Value. |
| #define | [BT\_UUID\_GATT\_AC](group__bt__uuid.md#gadbe14281482e776e87facb9835f522af)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AC\_VAL](group__bt__uuid.md#gaf2bc7408a53341478f1b41d54e888478)) |
|  | GATT Characteristic Average Current. |
| #define | [BT\_UUID\_GATT\_AV\_VAL](group__bt__uuid.md#ga2b5c1eef80844de1d49a70314db91b1d)   0x2ae1 |
|  | GATT Characteristic Average Voltage UUID Value. |
| #define | [BT\_UUID\_GATT\_AV](group__bt__uuid.md#ga3c669e805ea7fc93cade56f2281b10dc)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AV\_VAL](group__bt__uuid.md#ga2b5c1eef80844de1d49a70314db91b1d)) |
|  | GATT Characteristic Average Voltage. |
| #define | [BT\_UUID\_GATT\_BOOLEAN\_VAL](group__bt__uuid.md#ga0e1cbd1ae5c198c0f834802f9d354fb7)   0x2ae2 |
|  | GATT Characteristic Boolean UUID Value. |
| #define | [BT\_UUID\_GATT\_BOOLEAN](group__bt__uuid.md#ga1801b550a1be17bf0bb8c07818749e4e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_BOOLEAN\_VAL](group__bt__uuid.md#ga0e1cbd1ae5c198c0f834802f9d354fb7)) |
|  | GATT Characteristic Boolean. |
| #define | [BT\_UUID\_GATT\_CRDFP\_VAL](group__bt__uuid.md#ga2601e0757464729c789b58deeee15285)   0x2ae3 |
|  | GATT Characteristic Chromatic Distance From Planckian UUID Value. |
| #define | [BT\_UUID\_GATT\_CRDFP](group__bt__uuid.md#gac5bc300a9b31543dc3847990832d78c3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CRDFP\_VAL](group__bt__uuid.md#ga2601e0757464729c789b58deeee15285)) |
|  | GATT Characteristic Chromatic Distance From Planckian. |
| #define | [BT\_UUID\_GATT\_CRCOORDS\_VAL](group__bt__uuid.md#ga8fa1863d2ae7b22462be097308fb5c81)   0x2ae4 |
|  | GATT Characteristic Chromaticity Coordinates UUID Value. |
| #define | [BT\_UUID\_GATT\_CRCOORDS](group__bt__uuid.md#gac43c1fdab4869d79c423399c864f6088)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CRCOORDS\_VAL](group__bt__uuid.md#ga8fa1863d2ae7b22462be097308fb5c81)) |
|  | GATT Characteristic Chromaticity Coordinates. |
| #define | [BT\_UUID\_GATT\_CRCCT\_VAL](group__bt__uuid.md#gac6ef845c60c6d68ad0c3269690e97d51)   0x2ae5 |
|  | GATT Characteristic Chromaticity In CCT And Duv Values UUID Value. |
| #define | [BT\_UUID\_GATT\_CRCCT](group__bt__uuid.md#ga52a4a6bcb91935822f7e21fecbb283bc)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CRCCT\_VAL](group__bt__uuid.md#gac6ef845c60c6d68ad0c3269690e97d51)) |
|  | GATT Characteristic Chromaticity In CCT And Duv Values. |
| #define | [BT\_UUID\_GATT\_CRT\_VAL](group__bt__uuid.md#ga5d65027929bf31cdbdacc167c3f28951)   0x2ae6 |
|  | GATT Characteristic Chromaticity Tolerance UUID Value. |
| #define | [BT\_UUID\_GATT\_CRT](group__bt__uuid.md#ga94c83c03f6cb240374af1bc4ec1b5f32)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CRT\_VAL](group__bt__uuid.md#ga5d65027929bf31cdbdacc167c3f28951)) |
|  | GATT Characteristic Chromaticity Tolerance. |
| #define | [BT\_UUID\_GATT\_CIEIDX\_VAL](group__bt__uuid.md#ga361d00b8be7dc6c3d319a138bf5be1b9)   0x2ae7 |
|  | GATT Characteristic CIE 13.3-1995 Color Rendering Index UUID Value. |
| #define | [BT\_UUID\_GATT\_CIEIDX](group__bt__uuid.md#ga706f4f40760275742a9834d4b94cd1ed)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CIEIDX\_VAL](group__bt__uuid.md#ga361d00b8be7dc6c3d319a138bf5be1b9)) |
|  | GATT Characteristic CIE 13.3-1995 Color Rendering Index. |
| #define | [BT\_UUID\_GATT\_COEFFICIENT\_VAL](group__bt__uuid.md#ga298d1f0c9a48695488c7b211a7de66a9)   0x2ae8 |
|  | GATT Characteristic Coefficient UUID Value. |
| #define | [BT\_UUID\_GATT\_COEFFICIENT](group__bt__uuid.md#ga941228f8812bfda85e86a15185a1270d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_COEFFICIENT\_VAL](group__bt__uuid.md#ga298d1f0c9a48695488c7b211a7de66a9)) |
|  | GATT Characteristic Coefficient. |
| #define | [BT\_UUID\_GATT\_CCTEMP\_VAL](group__bt__uuid.md#ga5533c28dc6bcaad3f66678d0e90a4e88)   0x2ae9 |
|  | GATT Characteristic Correlated Color Temperature UUID Value. |
| #define | [BT\_UUID\_GATT\_CCTEMP](group__bt__uuid.md#ga2562158387beea244d57757e9e87422e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CCTEMP\_VAL](group__bt__uuid.md#ga5533c28dc6bcaad3f66678d0e90a4e88)) |
|  | GATT Characteristic Correlated Color Temperature. |
| #define | [BT\_UUID\_GATT\_COUNT16\_VAL](group__bt__uuid.md#ga2c292a6bf086b695dce4c8a6fcb2e331)   0x2aea |
|  | GATT Characteristic Count 16 UUID Value. |
| #define | [BT\_UUID\_GATT\_COUNT16](group__bt__uuid.md#ga770c5a643468816820bdcc5db2af8d69)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_COUNT16\_VAL](group__bt__uuid.md#ga2c292a6bf086b695dce4c8a6fcb2e331)) |
|  | GATT Characteristic Count 16. |
| #define | [BT\_UUID\_GATT\_COUNT24\_VAL](group__bt__uuid.md#ga360c3c084ac6f8f4ae6c0f8ddb1f2cf3)   0x2aeb |
|  | GATT Characteristic Count 24 UUID Value. |
| #define | [BT\_UUID\_GATT\_COUNT24](group__bt__uuid.md#ga7191613ab08efa46949ecb67d3512180)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_COUNT24\_VAL](group__bt__uuid.md#ga360c3c084ac6f8f4ae6c0f8ddb1f2cf3)) |
|  | GATT Characteristic Count 24. |
| #define | [BT\_UUID\_GATT\_CNTRCODE\_VAL](group__bt__uuid.md#ga77981b5aad0c0424a08c0bbc86c5ca71)   0x2aec |
|  | GATT Characteristic Country Code UUID Value. |
| #define | [BT\_UUID\_GATT\_CNTRCODE](group__bt__uuid.md#gaf83aeabd260ea7d027aafa69beb2b050)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CNTRCODE\_VAL](group__bt__uuid.md#ga77981b5aad0c0424a08c0bbc86c5ca71)) |
|  | GATT Characteristic Country Code. |
| #define | [BT\_UUID\_GATT\_DATEUTC\_VAL](group__bt__uuid.md#gad551c08d84b220342831bbb1d358efd6)   0x2aed |
|  | GATT Characteristic Date UTC UUID Value. |
| #define | [BT\_UUID\_GATT\_DATEUTC](group__bt__uuid.md#ga4151cbfefc334f33800be8fdc853ca34)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DATEUTC\_VAL](group__bt__uuid.md#gad551c08d84b220342831bbb1d358efd6)) |
|  | GATT Characteristic Date UTC. |
| #define | [BT\_UUID\_GATT\_EC\_VAL](group__bt__uuid.md#ga5ae0a7207e95f6aa2d982877057453d2)   0x2aee |
|  | GATT Characteristic Electric Current UUID Value. |
| #define | [BT\_UUID\_GATT\_EC](group__bt__uuid.md#ga9c86c847e1f2bb2deb23dbf4382b003f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_EC\_VAL](group__bt__uuid.md#ga5ae0a7207e95f6aa2d982877057453d2)) |
|  | GATT Characteristic Electric Current. |
| #define | [BT\_UUID\_GATT\_ECR\_VAL](group__bt__uuid.md#ga67e672df782986945ab3103c4ddff412)   0x2aef |
|  | GATT Characteristic Electric Current Range UUID Value. |
| #define | [BT\_UUID\_GATT\_ECR](group__bt__uuid.md#gac2121117e06e8d90448733b7e2ac9b97)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ECR\_VAL](group__bt__uuid.md#ga67e672df782986945ab3103c4ddff412)) |
|  | GATT Characteristic Electric Current Range. |
| #define | [BT\_UUID\_GATT\_ECSPEC\_VAL](group__bt__uuid.md#gafd1eeaf887046c9f2785089a81275153)   0x2af0 |
|  | GATT Characteristic Electric Current Specification UUID Value. |
| #define | [BT\_UUID\_GATT\_ECSPEC](group__bt__uuid.md#gaabdf693ada22d60cb524b501b3203b59)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ECSPEC\_VAL](group__bt__uuid.md#gafd1eeaf887046c9f2785089a81275153)) |
|  | GATT Characteristic Electric Current Specification. |
| #define | [BT\_UUID\_GATT\_ECSTAT\_VAL](group__bt__uuid.md#ga198d44bb45cf18921841e1788aeaa774)   0x2af1 |
|  | GATT Characteristic Electric Current Statistics UUID Value. |
| #define | [BT\_UUID\_GATT\_ECSTAT](group__bt__uuid.md#ga6a1b29e07ffd6240e138c2a0ab1d6525)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ECSTAT\_VAL](group__bt__uuid.md#ga198d44bb45cf18921841e1788aeaa774)) |
|  | GATT Characteristic Electric Current Statistics. |
| #define | [BT\_UUID\_GATT\_ENERGY\_VAL](group__bt__uuid.md#gad6a61da207a152987afcad67fe4633d2)   0x2af2 |
|  | GATT Characteristic Energy UUID Value. |
| #define | [BT\_UUID\_GATT\_ENERGY](group__bt__uuid.md#ga556811cb737ddccf121dda3d65f2d79f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ENERGY\_VAL](group__bt__uuid.md#gad6a61da207a152987afcad67fe4633d2)) |
|  | GATT Characteristic Energy. |
| #define | [BT\_UUID\_GATT\_EPOD\_VAL](group__bt__uuid.md#gab14d5fbaaa0e06c51db1cd41fcc368de)   0x2af3 |
|  | GATT Characteristic Energy In A Period Of Day UUID Value. |
| #define | [BT\_UUID\_GATT\_EPOD](group__bt__uuid.md#ga2c5e6339a8d25083ce8656f02298cc57)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_EPOD\_VAL](group__bt__uuid.md#gab14d5fbaaa0e06c51db1cd41fcc368de)) |
|  | GATT Characteristic Energy In A Period Of Day. |
| #define | [BT\_UUID\_GATT\_EVTSTAT\_VAL](group__bt__uuid.md#gafec2c62ae00f7efb506341edf08b0d9a)   0x2af4 |
|  | GATT Characteristic Event Statistics UUID Value. |
| #define | [BT\_UUID\_GATT\_EVTSTAT](group__bt__uuid.md#gaa8f949e568dce7f639aeb80415674e2a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_EVTSTAT\_VAL](group__bt__uuid.md#gafec2c62ae00f7efb506341edf08b0d9a)) |
|  | GATT Characteristic Event Statistics. |
| #define | [BT\_UUID\_GATT\_FSTR16\_VAL](group__bt__uuid.md#ga5d80019b1543d04e7cc5c7dc0f969c8c)   0x2af5 |
|  | GATT Characteristic Fixed String 16 UUID Value. |
| #define | [BT\_UUID\_GATT\_FSTR16](group__bt__uuid.md#ga8970252d984fd463369baab7445f7bf6)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FSTR16\_VAL](group__bt__uuid.md#ga5d80019b1543d04e7cc5c7dc0f969c8c)) |
|  | GATT Characteristic Fixed String 16. |
| #define | [BT\_UUID\_GATT\_FSTR24\_VAL](group__bt__uuid.md#gafa6970b19301bfc1c5f3dc6392850bd8)   0x2af6 |
|  | GATT Characteristic Fixed String 24 UUID Value. |
| #define | [BT\_UUID\_GATT\_FSTR24](group__bt__uuid.md#ga421bb2147cbf541fed439273ee5f2119)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FSTR24\_VAL](group__bt__uuid.md#gafa6970b19301bfc1c5f3dc6392850bd8)) |
|  | GATT Characteristic Fixed String 24. |
| #define | [BT\_UUID\_GATT\_FSTR36\_VAL](group__bt__uuid.md#ga2b90639839a47260c7f555eec0b8bcd0)   0x2af7 |
|  | GATT Characteristic Fixed String 36 UUID Value. |
| #define | [BT\_UUID\_GATT\_FSTR36](group__bt__uuid.md#ga0a03f71c8d0b616f3a496efe4b5c6561)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FSTR36\_VAL](group__bt__uuid.md#ga2b90639839a47260c7f555eec0b8bcd0)) |
|  | GATT Characteristic Fixed String 36. |
| #define | [BT\_UUID\_GATT\_FSTR8\_VAL](group__bt__uuid.md#gabafdb729c08aae0debace870f6043930)   0x2af8 |
|  | GATT Characteristic Fixed String 8 UUID Value. |
| #define | [BT\_UUID\_GATT\_FSTR8](group__bt__uuid.md#ga7b2a21e708cc13937038a3b88c0ad58b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FSTR8\_VAL](group__bt__uuid.md#gabafdb729c08aae0debace870f6043930)) |
|  | GATT Characteristic Fixed String 8. |
| #define | [BT\_UUID\_GATT\_GENLVL\_VAL](group__bt__uuid.md#ga18a4861ba81ae7f0a9ff0f1de37a6a0b)   0x2af9 |
|  | GATT Characteristic Generic Level UUID Value. |
| #define | [BT\_UUID\_GATT\_GENLVL](group__bt__uuid.md#ga7250c5f01251cf185035c18cf5d087c6)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_GENLVL\_VAL](group__bt__uuid.md#ga18a4861ba81ae7f0a9ff0f1de37a6a0b)) |
|  | GATT Characteristic Generic Level. |
| #define | [BT\_UUID\_GATT\_GTIN\_VAL](group__bt__uuid.md#ga1419411a928165a5cc4a26f0a97358d7)   0x2afa |
|  | GATT Characteristic Global Trade Item Number UUID Value. |
| #define | [BT\_UUID\_GATT\_GTIN](group__bt__uuid.md#ga27ef69db6e19c23b4f735bfbe2c83b7a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_GTIN\_VAL](group__bt__uuid.md#ga1419411a928165a5cc4a26f0a97358d7)) |
|  | GATT Characteristic Global Trade Item Number. |
| #define | [BT\_UUID\_GATT\_ILLUM\_VAL](group__bt__uuid.md#gaf660977f7494cecb5bd2d1d4808b0531)   0x2afb |
|  | GATT Characteristic Illuminance UUID Value. |
| #define | [BT\_UUID\_GATT\_ILLUM](group__bt__uuid.md#gacb727e39a14240931183e4cc608f3114)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ILLUM\_VAL](group__bt__uuid.md#gaf660977f7494cecb5bd2d1d4808b0531)) |
|  | GATT Characteristic Illuminance. |
| #define | [BT\_UUID\_GATT\_LUMEFF\_VAL](group__bt__uuid.md#ga742681175c952de8840c70df64b1562b)   0x2afc |
|  | GATT Characteristic Luminous Efficacy UUID Value. |
| #define | [BT\_UUID\_GATT\_LUMEFF](group__bt__uuid.md#ga3441cb7f9449be2ba9cc5cd73505f894)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LUMEFF\_VAL](group__bt__uuid.md#ga742681175c952de8840c70df64b1562b)) |
|  | GATT Characteristic Luminous Efficacy. |
| #define | [BT\_UUID\_GATT\_LUMNRG\_VAL](group__bt__uuid.md#gade0213130552d2757d74cdc2abe12d65)   0x2afd |
|  | GATT Characteristic Luminous Energy UUID Value. |
| #define | [BT\_UUID\_GATT\_LUMNRG](group__bt__uuid.md#gaa9ad315787bedcd20206b8dc99af4081)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LUMNRG\_VAL](group__bt__uuid.md#gade0213130552d2757d74cdc2abe12d65)) |
|  | GATT Characteristic Luminous Energy. |
| #define | [BT\_UUID\_GATT\_LUMEXP\_VAL](group__bt__uuid.md#ga3f2d4a042fb00481383b7b5e8837f24e)   0x2afe |
|  | GATT Characteristic Luminous Exposure UUID Value. |
| #define | [BT\_UUID\_GATT\_LUMEXP](group__bt__uuid.md#ga38d3dd48f55ebfde06d52310324088d4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LUMEXP\_VAL](group__bt__uuid.md#ga3f2d4a042fb00481383b7b5e8837f24e)) |
|  | GATT Characteristic Luminous Exposure. |
| #define | [BT\_UUID\_GATT\_LUMFLX\_VAL](group__bt__uuid.md#ga26f37ccbd862af70e5fa7516e59da73e)   0x2aff |
|  | GATT Characteristic Luminous Flux UUID Value. |
| #define | [BT\_UUID\_GATT\_LUMFLX](group__bt__uuid.md#gae05c06b201217e919c8493d3245b2f52)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LUMFLX\_VAL](group__bt__uuid.md#ga26f37ccbd862af70e5fa7516e59da73e)) |
|  | GATT Characteristic Luminous Flux. |
| #define | [BT\_UUID\_GATT\_LUMFLXR\_VAL](group__bt__uuid.md#gab1080ef3dffbc5521c8f587766ac22d6)   0x2b00 |
|  | GATT Characteristic Luminous Flux Range UUID Value. |
| #define | [BT\_UUID\_GATT\_LUMFLXR](group__bt__uuid.md#ga93a7fa9b6c9bbd12ef5d9a7169405e59)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LUMFLXR\_VAL](group__bt__uuid.md#gab1080ef3dffbc5521c8f587766ac22d6)) |
|  | GATT Characteristic Luminous Flux Range. |
| #define | [BT\_UUID\_GATT\_LUMINT\_VAL](group__bt__uuid.md#ga00cfabe28348d7a86a54608b8f0ec3de)   0x2b01 |
|  | GATT Characteristic Luminous Intensity UUID Value. |
| #define | [BT\_UUID\_GATT\_LUMINT](group__bt__uuid.md#gaefd8b48d82a4c403e735badb04e812b4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LUMINT\_VAL](group__bt__uuid.md#ga00cfabe28348d7a86a54608b8f0ec3de)) |
|  | GATT Characteristic Luminous Intensity. |
| #define | [BT\_UUID\_GATT\_MASSFLOW\_VAL](group__bt__uuid.md#ga23f13789b3f3f19691dbfdc3a33a506e)   0x2b02 |
|  | GATT Characteristic Mass Flow UUID Value. |
| #define | [BT\_UUID\_GATT\_MASSFLOW](group__bt__uuid.md#ga8670491866b6b62a3834c4f619612a7d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_MASSFLOW\_VAL](group__bt__uuid.md#ga23f13789b3f3f19691dbfdc3a33a506e)) |
|  | GATT Characteristic Mass Flow. |
| #define | [BT\_UUID\_GATT\_PERLGHT\_VAL](group__bt__uuid.md#ga4b8ec7d1538e6655b065a488d8c523af)   0x2b03 |
|  | GATT Characteristic Perceived Lightness UUID Value. |
| #define | [BT\_UUID\_GATT\_PERLGHT](group__bt__uuid.md#ga0f13aca1a13cc11b7e1adf7c1f7e75b1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PERLGHT\_VAL](group__bt__uuid.md#ga4b8ec7d1538e6655b065a488d8c523af)) |
|  | GATT Characteristic Perceived Lightness. |
| #define | [BT\_UUID\_GATT\_PER8\_VAL](group__bt__uuid.md#ga4bc9aee30308246d28eb96152eb686b1)   0x2b04 |
|  | GATT Characteristic Percentage 8 UUID Value. |
| #define | [BT\_UUID\_GATT\_PER8](group__bt__uuid.md#ga60ea8b576b1d3951be45cb928ce841b0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PER8\_VAL](group__bt__uuid.md#ga4bc9aee30308246d28eb96152eb686b1)) |
|  | GATT Characteristic Percentage 8. |
| #define | [BT\_UUID\_GATT\_PWR\_VAL](group__bt__uuid.md#gac70e24a9a91738c615e83e6238c96ed7)   0x2b05 |
|  | GATT Characteristic Power UUID Value. |
| #define | [BT\_UUID\_GATT\_PWR](group__bt__uuid.md#gaa374060d2715bfab9986c1eee2467ed5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PWR\_VAL](group__bt__uuid.md#gac70e24a9a91738c615e83e6238c96ed7)) |
|  | GATT Characteristic Power. |
| #define | [BT\_UUID\_GATT\_PWRSPEC\_VAL](group__bt__uuid.md#ga3db91205384fb559aa9f8865c15356d1)   0x2b06 |
|  | GATT Characteristic Power Specification UUID Value. |
| #define | [BT\_UUID\_GATT\_PWRSPEC](group__bt__uuid.md#gad69a1f73335555e9a7c164ebd2474371)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PWRSPEC\_VAL](group__bt__uuid.md#ga3db91205384fb559aa9f8865c15356d1)) |
|  | GATT Characteristic Power Specification. |
| #define | [BT\_UUID\_GATT\_RRICR\_VAL](group__bt__uuid.md#gac5533a77612f300dd8f1cd8ccd2ee522)   0x2b07 |
|  | GATT Characteristic Relative Runtime In A Current Range UUID Value. |
| #define | [BT\_UUID\_GATT\_RRICR](group__bt__uuid.md#ga7c3534f8bd7b9c662e73cd9d46dc8c79)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RRICR\_VAL](group__bt__uuid.md#gac5533a77612f300dd8f1cd8ccd2ee522)) |
|  | GATT Characteristic Relative Runtime In A Current Range. |
| #define | [BT\_UUID\_GATT\_RRIGLR\_VAL](group__bt__uuid.md#ga41b95788eb3271a8fe87766fe903e8d9)   0x2b08 |
|  | GATT Characteristic Relative Runtime In A Generic Level Range UUID Value. |
| #define | [BT\_UUID\_GATT\_RRIGLR](group__bt__uuid.md#ga2e1c29cac1ece5f3fad29c61ed2b0aa4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RRIGLR\_VAL](group__bt__uuid.md#ga41b95788eb3271a8fe87766fe903e8d9)) |
|  | GATT Characteristic Relative Runtime In A Generic Level Range. |
| #define | [BT\_UUID\_GATT\_RVIVR\_VAL](group__bt__uuid.md#gac3bb5af173f013c8a49227b2920bc107)   0x2b09 |
|  | GATT Characteristic Relative Value In A Voltage Range UUID Value. |
| #define | [BT\_UUID\_GATT\_RVIVR](group__bt__uuid.md#gaac802734c88aac862fcab0599cb2e216)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RVIVR\_VAL](group__bt__uuid.md#gac3bb5af173f013c8a49227b2920bc107)) |
|  | GATT Characteristic Relative Value In A Voltage Range. |
| #define | [BT\_UUID\_GATT\_RVIIR\_VAL](group__bt__uuid.md#ga2866d911411268e5026ef729efa990e9)   0x2b0a |
|  | GATT Characteristic Relative Value In A Illuminance Range UUID Value. |
| #define | [BT\_UUID\_GATT\_RVIIR](group__bt__uuid.md#ga165f79f1dcde1e7359a4c4602dc88c40)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RVIIR\_VAL](group__bt__uuid.md#ga2866d911411268e5026ef729efa990e9)) |
|  | GATT Characteristic Relative Value In A Illuminance Range. |
| #define | [BT\_UUID\_GATT\_RVIPOD\_VAL](group__bt__uuid.md#gab73b24f9941a80fab6423ff85f68aae6)   0x2b0b |
|  | GATT Characteristic Relative Value In A Period Of Day UUID Value. |
| #define | [BT\_UUID\_GATT\_RVIPOD](group__bt__uuid.md#ga9e6b0e6585f2ceb62dd236a0ae3afc6a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RVIPOD\_VAL](group__bt__uuid.md#gab73b24f9941a80fab6423ff85f68aae6)) |
|  | GATT Characteristic Relative Value In A Period Of Day. |
| #define | [BT\_UUID\_GATT\_RVITR\_VAL](group__bt__uuid.md#gaac84e4bcae1a1b83af9124688e01912a)   0x2b0c |
|  | GATT Characteristic Relative Value In A Temperature Range UUID Value. |
| #define | [BT\_UUID\_GATT\_RVITR](group__bt__uuid.md#ga8c8e5e43e2bc8f7c26344fff4127e039)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RVITR\_VAL](group__bt__uuid.md#gaac84e4bcae1a1b83af9124688e01912a)) |
|  | GATT Characteristic Relative Value In A Temperature Range. |
| #define | [BT\_UUID\_GATT\_TEMP8\_VAL](group__bt__uuid.md#gaa7a119bfd7df636f0ed0bf515232e6bb)   0x2b0d |
|  | GATT Characteristic Temperature 8 UUID Value. |
| #define | [BT\_UUID\_GATT\_TEMP8](group__bt__uuid.md#ga146d14e283686a5712c90698fd6a64ad)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TEMP8\_VAL](group__bt__uuid.md#gaa7a119bfd7df636f0ed0bf515232e6bb)) |
|  | GATT Characteristic Temperature 8. |
| #define | [BT\_UUID\_GATT\_TEMP8\_IPOD\_VAL](group__bt__uuid.md#ga616708b903a88a6bb9eabdae60813063)   0x2b0e |
|  | GATT Characteristic Temperature 8 In A Period Of Day UUID Value. |
| #define | [BT\_UUID\_GATT\_TEMP8\_IPOD](group__bt__uuid.md#ga3d28ebdcaa93ed4ccdee512f7ddd979a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TEMP8\_IPOD\_VAL](group__bt__uuid.md#ga616708b903a88a6bb9eabdae60813063)) |
|  | GATT Characteristic Temperature 8 In A Period Of Day. |
| #define | [BT\_UUID\_GATT\_TEMP8\_STAT\_VAL](group__bt__uuid.md#ga3d54ad101d044924da30aa81a6b64111)   0x2b0f |
|  | GATT Characteristic Temperature 8 Statistics UUID Value. |
| #define | [BT\_UUID\_GATT\_TEMP8\_STAT](group__bt__uuid.md#ga071d32c5e9dd24fc179f8cac531e499f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TEMP8\_STAT\_VAL](group__bt__uuid.md#ga3d54ad101d044924da30aa81a6b64111)) |
|  | GATT Characteristic Temperature 8 Statistics. |
| #define | [BT\_UUID\_GATT\_TEMP\_RNG\_VAL](group__bt__uuid.md#gadcdd9e4d2cfa09f6d766b513224ef7bf)   0x2b10 |
|  | GATT Characteristic Temperature Range UUID Value. |
| #define | [BT\_UUID\_GATT\_TEMP\_RNG](group__bt__uuid.md#ga99e73003bde4dac095f198dd7045b297)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TEMP\_RNG\_VAL](group__bt__uuid.md#gadcdd9e4d2cfa09f6d766b513224ef7bf)) |
|  | GATT Characteristic Temperature Range. |
| #define | [BT\_UUID\_GATT\_TEMP\_STAT\_VAL](group__bt__uuid.md#ga035eaed3f130c2222236fdc194f9b1a4)   0x2b11 |
|  | GATT Characteristic Temperature Statistics UUID Value. |
| #define | [BT\_UUID\_GATT\_TEMP\_STAT](group__bt__uuid.md#ga8ae19f54cd4aa1c7ab42c48f33080f52)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TEMP\_STAT\_VAL](group__bt__uuid.md#ga035eaed3f130c2222236fdc194f9b1a4)) |
|  | GATT Characteristic Temperature Statistics. |
| #define | [BT\_UUID\_GATT\_TIM\_DC8\_VAL](group__bt__uuid.md#gae5f1cda9dbc55f77cfbb4c00f4e359f0)   0x2b12 |
|  | GATT Characteristic Time Decihour 8 UUID Value. |
| #define | [BT\_UUID\_GATT\_TIM\_DC8](group__bt__uuid.md#gae9feb929d7a7eb67dc1db02ce26cc82b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TIM\_DC8\_VAL](group__bt__uuid.md#gae5f1cda9dbc55f77cfbb4c00f4e359f0)) |
|  | GATT Characteristic Time Decihour 8. |
| #define | [BT\_UUID\_GATT\_TIM\_EXP8\_VAL](group__bt__uuid.md#ga07a0510f652506225410b1865882d1ea)   0x2b13 |
|  | GATT Characteristic Time Exponential 8 UUID Value. |
| #define | [BT\_UUID\_GATT\_TIM\_EXP8](group__bt__uuid.md#ga5e4aee6898f1ab1f8065c113241c99bd)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TIM\_EXP8\_VAL](group__bt__uuid.md#ga07a0510f652506225410b1865882d1ea)) |
|  | GATT Characteristic Time Exponential 8. |
| #define | [BT\_UUID\_GATT\_TIM\_H24\_VAL](group__bt__uuid.md#ga272a11fc6d56e685243f6507708f8032)   0x2b14 |
|  | GATT Characteristic Time Hour 24 UUID Value. |
| #define | [BT\_UUID\_GATT\_TIM\_H24](group__bt__uuid.md#gac209c86c368f2ed7c20bae2b90f36a0a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TIM\_H24\_VAL](group__bt__uuid.md#ga272a11fc6d56e685243f6507708f8032)) |
|  | GATT Characteristic Time Hour 24. |
| #define | [BT\_UUID\_GATT\_TIM\_MS24\_VAL](group__bt__uuid.md#ga181a187356797362b4a7d9a7d22f7fdc)   0x2b15 |
|  | GATT Characteristic Time Millisecond 24 UUID Value. |
| #define | [BT\_UUID\_GATT\_TIM\_MS24](group__bt__uuid.md#ga941191900854cfed39dae2b5dfba499b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TIM\_MS24\_VAL](group__bt__uuid.md#ga181a187356797362b4a7d9a7d22f7fdc)) |
|  | GATT Characteristic Time Millisecond 24. |
| #define | [BT\_UUID\_GATT\_TIM\_S16\_VAL](group__bt__uuid.md#ga2ad71e9a1912c84f31072edcf3234093)   0x2b16 |
|  | GATT Characteristic Time Second 16 UUID Value. |
| #define | [BT\_UUID\_GATT\_TIM\_S16](group__bt__uuid.md#ga216c5c11e143571c5b40e7554c40ab91)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TIM\_S16\_VAL](group__bt__uuid.md#ga2ad71e9a1912c84f31072edcf3234093)) |
|  | GATT Characteristic Time Second 16. |
| #define | [BT\_UUID\_GATT\_TIM\_S8\_VAL](group__bt__uuid.md#gae7ad9e90132e56a59d3fb3cfaea55faa)   0x2b17 |
|  | GATT Characteristic Time Second 8 UUID Value. |
| #define | [BT\_UUID\_GATT\_TIM\_S8](group__bt__uuid.md#gacf36b122fdeb96d6da4b710506118668)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TIM\_S8\_VAL](group__bt__uuid.md#gae7ad9e90132e56a59d3fb3cfaea55faa)) |
|  | GATT Characteristic Time Second 8. |
| #define | [BT\_UUID\_GATT\_V\_VAL](group__bt__uuid.md#gae727674510a76ca337ea57c4222791ab)   0x2b18 |
|  | GATT Characteristic Voltage UUID Value. |
| #define | [BT\_UUID\_GATT\_V](group__bt__uuid.md#ga1cedb6e5b998d0edf435dd4203fee96c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_V\_VAL](group__bt__uuid.md#gae727674510a76ca337ea57c4222791ab)) |
|  | GATT Characteristic Voltage. |
| #define | [BT\_UUID\_GATT\_V\_SPEC\_VAL](group__bt__uuid.md#ga5bc426767e92938654f24f0158a16b53)   0x2b19 |
|  | GATT Characteristic Voltage Specification UUID Value. |
| #define | [BT\_UUID\_GATT\_V\_SPEC](group__bt__uuid.md#ga23440a5aff26bf0a737d4a48b6ce301d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_V\_SPEC\_VAL](group__bt__uuid.md#ga5bc426767e92938654f24f0158a16b53)) |
|  | GATT Characteristic Voltage Specification. |
| #define | [BT\_UUID\_GATT\_V\_STAT\_VAL](group__bt__uuid.md#gac655949e3c565b8835b099a93a24498f)   0x2b1a |
|  | GATT Characteristic Voltage Statistics UUID Value. |
| #define | [BT\_UUID\_GATT\_V\_STAT](group__bt__uuid.md#gac1d74460417a592cbd4f5b6528c77e28)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_V\_STAT\_VAL](group__bt__uuid.md#gac655949e3c565b8835b099a93a24498f)) |
|  | GATT Characteristic Voltage Statistics. |
| #define | [BT\_UUID\_GATT\_VOLF\_VAL](group__bt__uuid.md#gae37019af7703f5b3abb99bcfbb1d5343)   0x2b1b |
|  | GATT Characteristic Volume Flow UUID Value. |
| #define | [BT\_UUID\_GATT\_VOLF](group__bt__uuid.md#ga8ddcea2b365f55ac647562063ede0f3c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_VOLF\_VAL](group__bt__uuid.md#gae37019af7703f5b3abb99bcfbb1d5343)) |
|  | GATT Characteristic Volume Flow. |
| #define | [BT\_UUID\_GATT\_CRCOORD\_VAL](group__bt__uuid.md#gaf7b547b7f4c6908f601afc33d0d0ebb8)   0x2b1c |
|  | GATT Characteristic Chromaticity Coordinate (not Coordinates) UUID Value. |
| #define | [BT\_UUID\_GATT\_CRCOORD](group__bt__uuid.md#ga53a898269a7f5ab84e9853521f69bc69)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CRCOORD\_VAL](group__bt__uuid.md#gaf7b547b7f4c6908f601afc33d0d0ebb8)) |
|  | GATT Characteristic Chromaticity Coordinate (not Coordinates). |
| #define | [BT\_UUID\_GATT\_RCF\_VAL](group__bt__uuid.md#ga8b2d587922902479e47bd316443e0a56)   0x2b1d |
|  | GATT Characteristic RC Feature UUID Value. |
| #define | [BT\_UUID\_GATT\_RCF](group__bt__uuid.md#gac6961922da80f8c628a35b8855cb788b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RCF\_VAL](group__bt__uuid.md#ga8b2d587922902479e47bd316443e0a56)) |
|  | GATT Characteristic RC Feature. |
| #define | [BT\_UUID\_GATT\_RCSET\_VAL](group__bt__uuid.md#ga47316949dd2eb5571e3b94240a4e6c90)   0x2b1e |
|  | GATT Characteristic RC Settings UUID Value. |
| #define | [BT\_UUID\_GATT\_RCSET](group__bt__uuid.md#ga2af1f07e6e4484476740db5bb6b31b8f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RCSET\_VAL](group__bt__uuid.md#ga47316949dd2eb5571e3b94240a4e6c90)) |
|  | GATT Characteristic RC Settings. |
| #define | [BT\_UUID\_GATT\_RCCP\_VAL](group__bt__uuid.md#gaabe52b93d5ac1e72c468be08fdea35ef)   0x2b1f |
|  | GATT Characteristic Reconnection Configuration Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_RCCP](group__bt__uuid.md#ga48b7a42b204407553262ea68e53f65d7)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RCCP\_VAL](group__bt__uuid.md#gaabe52b93d5ac1e72c468be08fdea35ef)) |
|  | GATT Characteristic Reconnection Configuration Control Point. |
| #define | [BT\_UUID\_GATT\_IDD\_SC\_VAL](group__bt__uuid.md#gadc4e7dcda6314aa68b4165199ddc4123)   0x2b20 |
|  | GATT Characteristic IDD Status Changed UUID Value. |
| #define | [BT\_UUID\_GATT\_IDD\_SC](group__bt__uuid.md#gab36f1fff60a7657844985841bb0350f8)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IDD\_SC\_VAL](group__bt__uuid.md#gadc4e7dcda6314aa68b4165199ddc4123)) |
|  | GATT Characteristic IDD Status Changed. |
| #define | [BT\_UUID\_GATT\_IDD\_S\_VAL](group__bt__uuid.md#gafb1511371c0c19323989961689425d08)   0x2b21 |
|  | GATT Characteristic IDD Status UUID Value. |
| #define | [BT\_UUID\_GATT\_IDD\_S](group__bt__uuid.md#ga560d7cef69190752eb8a5c4f6fed5989)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IDD\_S\_VAL](group__bt__uuid.md#gafb1511371c0c19323989961689425d08)) |
|  | GATT Characteristic IDD Status. |
| #define | [BT\_UUID\_GATT\_IDD\_AS\_VAL](group__bt__uuid.md#ga2e854242941b30552241e1ee3669d669)   0x2b22 |
|  | GATT Characteristic IDD Annunciation Status UUID Value. |
| #define | [BT\_UUID\_GATT\_IDD\_AS](group__bt__uuid.md#ga980781b7142c177ed46b8caca9b8b518)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IDD\_AS\_VAL](group__bt__uuid.md#ga2e854242941b30552241e1ee3669d669)) |
|  | GATT Characteristic IDD Annunciation Status. |
| #define | [BT\_UUID\_GATT\_IDD\_F\_VAL](group__bt__uuid.md#ga7d20cc62ad420b71d299361430005d27)   0x2b23 |
|  | GATT Characteristic IDD Features UUID Value. |
| #define | [BT\_UUID\_GATT\_IDD\_F](group__bt__uuid.md#ga369b0b1ddac085d2812a42f737bdd594)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IDD\_F\_VAL](group__bt__uuid.md#ga7d20cc62ad420b71d299361430005d27)) |
|  | GATT Characteristic IDD Features. |
| #define | [BT\_UUID\_GATT\_IDD\_SRCP\_VAL](group__bt__uuid.md#ga1e817e253f29e03a98327e08c2048e6b)   0x2b24 |
|  | GATT Characteristic IDD Status Reader Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_IDD\_SRCP](group__bt__uuid.md#ga13d829bfcacb036a2271cd09491c1578)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IDD\_SRCP\_VAL](group__bt__uuid.md#ga1e817e253f29e03a98327e08c2048e6b)) |
|  | GATT Characteristic IDD Status Reader Control Point. |
| #define | [BT\_UUID\_GATT\_IDD\_CCP\_VAL](group__bt__uuid.md#ga1dc738c5c564bf05d3c2669a79db6e17)   0x2b25 |
|  | GATT Characteristic IDD Command Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_IDD\_CCP](group__bt__uuid.md#gaf2bc260638bc158b8bfd403bf43de2d9)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IDD\_CCP\_VAL](group__bt__uuid.md#ga1dc738c5c564bf05d3c2669a79db6e17)) |
|  | GATT Characteristic IDD Command Control Point. |
| #define | [BT\_UUID\_GATT\_IDD\_CD\_VAL](group__bt__uuid.md#ga70d6ece9b4d331965c42f0606c0c7526)   0x2b26 |
|  | GATT Characteristic IDD Command Data UUID Value. |
| #define | [BT\_UUID\_GATT\_IDD\_CD](group__bt__uuid.md#gac7dbb4cb283933558699d129928e37d5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IDD\_CD\_VAL](group__bt__uuid.md#ga70d6ece9b4d331965c42f0606c0c7526)) |
|  | GATT Characteristic IDD Command Data. |
| #define | [BT\_UUID\_GATT\_IDD\_RACP\_VAL](group__bt__uuid.md#gab9ef1f54711a8d7d5884c7b3a798f615)   0x2b27 |
|  | GATT Characteristic IDD Record Access Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_IDD\_RACP](group__bt__uuid.md#ga628c153b88ea0f504c234dc44248a237)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IDD\_RACP\_VAL](group__bt__uuid.md#gab9ef1f54711a8d7d5884c7b3a798f615)) |
|  | GATT Characteristic IDD Record Access Control Point. |
| #define | [BT\_UUID\_GATT\_IDD\_HD\_VAL](group__bt__uuid.md#ga26f24abf219ce90fd002d995e3a19d30)   0x2b28 |
|  | GATT Characteristic IDD History Data UUID Value. |
| #define | [BT\_UUID\_GATT\_IDD\_HD](group__bt__uuid.md#ga88e2087b512092d91508f8e878a22f3a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_IDD\_HD\_VAL](group__bt__uuid.md#ga26f24abf219ce90fd002d995e3a19d30)) |
|  | GATT Characteristic IDD History Data. |
| #define | [BT\_UUID\_GATT\_CLIENT\_FEATURES\_VAL](group__bt__uuid.md#ga54537cebc8ce6e7d8d0f377a38765635)   0x2b29 |
|  | GATT Characteristic Client Supported Features UUID value. |
| #define | [BT\_UUID\_GATT\_CLIENT\_FEATURES](group__bt__uuid.md#gae3faa1515f3aae0c71d4face04929dec)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CLIENT\_FEATURES\_VAL](group__bt__uuid.md#ga54537cebc8ce6e7d8d0f377a38765635)) |
|  | GATT Characteristic Client Supported Features. |
| #define | [BT\_UUID\_GATT\_DB\_HASH\_VAL](group__bt__uuid.md#gacead7897f5fed798714a79df2764d95a)   0x2b2a |
|  | GATT Characteristic Database Hash UUID value. |
| #define | [BT\_UUID\_GATT\_DB\_HASH](group__bt__uuid.md#ga6b162958f4f406fd3e3d31a84393fe19)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DB\_HASH\_VAL](group__bt__uuid.md#gacead7897f5fed798714a79df2764d95a)) |
|  | GATT Characteristic Database Hash. |
| #define | [BT\_UUID\_GATT\_BSS\_CP\_VAL](group__bt__uuid.md#gaf609e6663173f4c4bb6ed18274f9931b)   0x2b2b |
|  | GATT Characteristic BSS Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_BSS\_CP](group__bt__uuid.md#gadeabab76545da0de52cc26d48e564730)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_BSS\_CP\_VAL](group__bt__uuid.md#gaf609e6663173f4c4bb6ed18274f9931b)) |
|  | GATT Characteristic BSS Control Point. |
| #define | [BT\_UUID\_GATT\_BSS\_R\_VAL](group__bt__uuid.md#ga73cbe100a043e8f08b87fcfed82107ad)   0x2b2c |
|  | GATT Characteristic BSS Response UUID Value. |
| #define | [BT\_UUID\_GATT\_BSS\_R](group__bt__uuid.md#gae9f0db1cbcc6dfeda9beb96e14350cf6)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_BSS\_R\_VAL](group__bt__uuid.md#ga73cbe100a043e8f08b87fcfed82107ad)) |
|  | GATT Characteristic BSS Response. |
| #define | [BT\_UUID\_GATT\_EMG\_ID\_VAL](group__bt__uuid.md#ga77157df8db39286f6f6edf1dd71f4a5e)   0x2b2d |
|  | GATT Characteristic Emergency ID UUID Value. |
| #define | [BT\_UUID\_GATT\_EMG\_ID](group__bt__uuid.md#ga6fdb1cd7bf1323b27645180ca39ca063)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_EMG\_ID\_VAL](group__bt__uuid.md#ga77157df8db39286f6f6edf1dd71f4a5e)) |
|  | GATT Characteristic Emergency ID. |
| #define | [BT\_UUID\_GATT\_EMG\_TXT\_VAL](group__bt__uuid.md#gabcea55cbf065daab8709e4d36941ad90)   0x2b2e |
|  | GATT Characteristic Emergency Text UUID Value. |
| #define | [BT\_UUID\_GATT\_EMG\_TXT](group__bt__uuid.md#ga1bc6805b2948d3f36af972f2ee34f93a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_EMG\_TXT\_VAL](group__bt__uuid.md#gabcea55cbf065daab8709e4d36941ad90)) |
|  | GATT Characteristic Emergency Text. |
| #define | [BT\_UUID\_GATT\_ACS\_S\_VAL](group__bt__uuid.md#ga7d46292e64c3a8bc9a2ddd71418e56c8)   0x2b2f |
|  | GATT Characteristic ACS Status UUID Value. |
| #define | [BT\_UUID\_GATT\_ACS\_S](group__bt__uuid.md#gad94f7adb29687b460fb7bb860023d890)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ACS\_S\_VAL](group__bt__uuid.md#ga7d46292e64c3a8bc9a2ddd71418e56c8)) |
|  | GATT Characteristic ACS Status. |
| #define | [BT\_UUID\_GATT\_ACS\_DI\_VAL](group__bt__uuid.md#ga0b19f25f01532abb98b63438d55b7683)   0x2b30 |
|  | GATT Characteristic ACS Data In UUID Value. |
| #define | [BT\_UUID\_GATT\_ACS\_DI](group__bt__uuid.md#gabd8886704d8fba31bbb1f9a8aeee9aa3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ACS\_DI\_VAL](group__bt__uuid.md#ga0b19f25f01532abb98b63438d55b7683)) |
|  | GATT Characteristic ACS Data In. |
| #define | [BT\_UUID\_GATT\_ACS\_DON\_VAL](group__bt__uuid.md#ga08ffe10a9e5e1f716581d96dd49bebac)   0x2b31 |
|  | GATT Characteristic ACS Data Out Notify UUID Value. |
| #define | [BT\_UUID\_GATT\_ACS\_DON](group__bt__uuid.md#ga0933ee4e3740e4f6c28522113b84c5b0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ACS\_DON\_VAL](group__bt__uuid.md#ga08ffe10a9e5e1f716581d96dd49bebac)) |
|  | GATT Characteristic ACS Data Out Notify. |
| #define | [BT\_UUID\_GATT\_ACS\_DOI\_VAL](group__bt__uuid.md#ga852f095873bee6c0dec742ea45817294)   0x2b32 |
|  | GATT Characteristic ACS Data Out Indicate UUID Value. |
| #define | [BT\_UUID\_GATT\_ACS\_DOI](group__bt__uuid.md#ga4875b80953686217209dc8a90e705ff2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ACS\_DOI\_VAL](group__bt__uuid.md#ga852f095873bee6c0dec742ea45817294)) |
|  | GATT Characteristic ACS Data Out Indicate. |
| #define | [BT\_UUID\_GATT\_ACS\_CP\_VAL](group__bt__uuid.md#ga492e0766dd16dea9e63e80423c9210cb)   0x2b33 |
|  | GATT Characteristic ACS Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_ACS\_CP](group__bt__uuid.md#gabd2164db62c4f29d2bafc272178312e5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ACS\_CP\_VAL](group__bt__uuid.md#ga492e0766dd16dea9e63e80423c9210cb)) |
|  | GATT Characteristic ACS Control Point. |
| #define | [BT\_UUID\_GATT\_EBPM\_VAL](group__bt__uuid.md#ga3016f0dd266a98f7d88a3198f54caf7e)   0x2b34 |
|  | GATT Characteristic Enhanced Blood Pressure Measurement UUID Value. |
| #define | [BT\_UUID\_GATT\_EBPM](group__bt__uuid.md#gafe7d80c67c7c059c174c2ec8aa6cf92d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_EBPM\_VAL](group__bt__uuid.md#ga3016f0dd266a98f7d88a3198f54caf7e)) |
|  | GATT Characteristic Enhanced Blood Pressure Measurement. |
| #define | [BT\_UUID\_GATT\_EICP\_VAL](group__bt__uuid.md#gad61213ed875c9d0b6bd5a2e7154f80d7)   0x2b35 |
|  | GATT Characteristic Enhanced Intermediate Cuff Pressure UUID Value. |
| #define | [BT\_UUID\_GATT\_EICP](group__bt__uuid.md#gab5032246e17304cb99bb619e6a3d70f1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_EICP\_VAL](group__bt__uuid.md#gad61213ed875c9d0b6bd5a2e7154f80d7)) |
|  | GATT Characteristic Enhanced Intermediate Cuff Pressure. |
| #define | [BT\_UUID\_GATT\_BPR\_VAL](group__bt__uuid.md#ga5b59d10e5d4653ed774a05da55241368)   0x2b36 |
|  | GATT Characteristic Blood Pressure Record UUID Value. |
| #define | [BT\_UUID\_GATT\_BPR](group__bt__uuid.md#gafa84009c324ee2e0a36efd0bbb486d4b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_BPR\_VAL](group__bt__uuid.md#ga5b59d10e5d4653ed774a05da55241368)) |
|  | GATT Characteristic Blood Pressure Record. |
| #define | [BT\_UUID\_GATT\_RU\_VAL](group__bt__uuid.md#ga4ac04b637bed53a51dbf598bd54a827a)   0x2b37 |
|  | GATT Characteristic Registered User UUID Value. |
| #define | [BT\_UUID\_GATT\_RU](group__bt__uuid.md#ga8a00648e37c023bf06be268960071d27)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_RU\_VAL](group__bt__uuid.md#ga4ac04b637bed53a51dbf598bd54a827a)) |
|  | GATT Characteristic Registered User. |
| #define | [BT\_UUID\_GATT\_BR\_EDR\_HD\_VAL](group__bt__uuid.md#gab89358d9db126f1eb9e1df6dc4639b82)   0x2b38 |
|  | GATT Characteristic BR-EDR Handover Data UUID Value. |
| #define | [BT\_UUID\_GATT\_BR\_EDR\_HD](group__bt__uuid.md#ga279da4b9d9aaccd67846d3ff93e25516)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_BR\_EDR\_HD\_VAL](group__bt__uuid.md#gab89358d9db126f1eb9e1df6dc4639b82)) |
|  | GATT Characteristic BR-EDR Handover Data. |
| #define | [BT\_UUID\_GATT\_BT\_SIG\_D\_VAL](group__bt__uuid.md#gaf95bc5640e25a651bb62f474fbdbd0f0)   0x2b39 |
|  | GATT Characteristic Bluetooth SIG Data UUID Value. |
| #define | [BT\_UUID\_GATT\_BT\_SIG\_D](group__bt__uuid.md#ga268e9d8096668ef890f5c17c76c882c5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_BT\_SIG\_D\_VAL](group__bt__uuid.md#gaf95bc5640e25a651bb62f474fbdbd0f0)) |
|  | GATT Characteristic Bluetooth SIG Data. |
| #define | [BT\_UUID\_GATT\_SERVER\_FEATURES\_VAL](group__bt__uuid.md#ga8d23a276e657bccde1385066ce2cd709)   0x2b3a |
|  | GATT Characteristic Server Supported Features UUID value. |
| #define | [BT\_UUID\_GATT\_SERVER\_FEATURES](group__bt__uuid.md#ga261af6f050c6a16d174c80cfce48b13e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SERVER\_FEATURES\_VAL](group__bt__uuid.md#ga8d23a276e657bccde1385066ce2cd709)) |
|  | GATT Characteristic Server Supported Features. |
| #define | [BT\_UUID\_GATT\_PHY\_AMF\_VAL](group__bt__uuid.md#gad94da8852116cc6651c2bb75b8420c95)   0x2b3b |
|  | GATT Characteristic Physical Activity Monitor Features UUID Value. |
| #define | [BT\_UUID\_GATT\_PHY\_AMF](group__bt__uuid.md#ga6d227d76b62bcec99cc8a8b6b8054474)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PHY\_AMF\_VAL](group__bt__uuid.md#gad94da8852116cc6651c2bb75b8420c95)) |
|  | GATT Characteristic Physical Activity Monitor Features. |
| #define | [BT\_UUID\_GATT\_GEN\_AID\_VAL](group__bt__uuid.md#ga8302d0d60c536b9862028633c8155a3a)   0x2b3c |
|  | GATT Characteristic General Activity Instantaneous Data UUID Value. |
| #define | [BT\_UUID\_GATT\_GEN\_AID](group__bt__uuid.md#gacfbd8563c68df3aa15264fc81f0eabb8)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_GEN\_AID\_VAL](group__bt__uuid.md#ga8302d0d60c536b9862028633c8155a3a)) |
|  | GATT Characteristic General Activity Instantaneous Data. |
| #define | [BT\_UUID\_GATT\_GEN\_ASD\_VAL](group__bt__uuid.md#ga4865adb3aadcb01834444e7fda021162)   0x2b3d |
|  | GATT Characteristic General Activity Summary Data UUID Value. |
| #define | [BT\_UUID\_GATT\_GEN\_ASD](group__bt__uuid.md#ga3b068ab73e6c277692a535b81b6e9ae1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_GEN\_ASD\_VAL](group__bt__uuid.md#ga4865adb3aadcb01834444e7fda021162)) |
|  | GATT Characteristic General Activity Summary Data. |
| #define | [BT\_UUID\_GATT\_CR\_AID\_VAL](group__bt__uuid.md#gac82a202322d7ee65130150d09d82b76a)   0x2b3e |
|  | GATT Characteristic CardioRespiratory Activity Instantaneous Data UUID Value. |
| #define | [BT\_UUID\_GATT\_CR\_AID](group__bt__uuid.md#ga35d88cb3312b6867d153780ee3a57be2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CR\_AID\_VAL](group__bt__uuid.md#gac82a202322d7ee65130150d09d82b76a)) |
|  | GATT Characteristic CardioRespiratory Activity Instantaneous Data. |
| #define | [BT\_UUID\_GATT\_CR\_ASD\_VAL](group__bt__uuid.md#ga6606c6d6ac05bbdbbbd27af5c28b825a)   0x2b3f |
|  | GATT Characteristic CardioRespiratory Activity Summary Data UUID Value. |
| #define | [BT\_UUID\_GATT\_CR\_ASD](group__bt__uuid.md#gadac7397ba9891282ef425e05c8161938)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CR\_ASD\_VAL](group__bt__uuid.md#ga6606c6d6ac05bbdbbbd27af5c28b825a)) |
|  | GATT Characteristic CardioRespiratory Activity Summary Data. |
| #define | [BT\_UUID\_GATT\_SC\_ASD\_VAL](group__bt__uuid.md#ga2aed9d07c8f4d552a4d6a5c2b693e97e)   0x2b40 |
|  | GATT Characteristic Step Counter Activity Summary Data UUID Value. |
| #define | [BT\_UUID\_GATT\_SC\_ASD](group__bt__uuid.md#ga9dd42f8966856001425c4bae4f6dc5a5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SC\_ASD\_VAL](group__bt__uuid.md#ga2aed9d07c8f4d552a4d6a5c2b693e97e)) |
|  | GATT Characteristic Step Counter Activity Summary Data. |
| #define | [BT\_UUID\_GATT\_SLP\_AID\_VAL](group__bt__uuid.md#gabb73d22b90482201f9f20d6f89aa6671)   0x2b41 |
|  | GATT Characteristic Sleep Activity Instantaneous Data UUID Value. |
| #define | [BT\_UUID\_GATT\_SLP\_AID](group__bt__uuid.md#gaf0a5a409f91366422f145acbb45e4abd)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SLP\_AID\_VAL](group__bt__uuid.md#gabb73d22b90482201f9f20d6f89aa6671)) |
|  | GATT Characteristic Sleep Activity Instantaneous Data. |
| #define | [BT\_UUID\_GATT\_SLP\_ASD\_VAL](group__bt__uuid.md#gaa309ce83ee85407cc8068aaccec95b94)   0x2b42 |
|  | GATT Characteristic Sleep Activity Summary Data UUID Value. |
| #define | [BT\_UUID\_GATT\_SLP\_ASD](group__bt__uuid.md#ga5232c5aac8c20f23aaadf1a023d91fcb)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SLP\_ASD\_VAL](group__bt__uuid.md#gaa309ce83ee85407cc8068aaccec95b94)) |
|  | GATT Characteristic Sleep Activity Summary Data. |
| #define | [BT\_UUID\_GATT\_PHY\_AMCP\_VAL](group__bt__uuid.md#ga1c2a6903fe19f05e4515122ddd6e454f)   0x2b43 |
|  | GATT Characteristic Physical Activity Monitor Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_PHY\_AMCP](group__bt__uuid.md#ga59ef934ce5ccf5e4ed309319f75c1150)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PHY\_AMCP\_VAL](group__bt__uuid.md#ga1c2a6903fe19f05e4515122ddd6e454f)) |
|  | GATT Characteristic Physical Activity Monitor Control Point. |
| #define | [BT\_UUID\_GATT\_ACS\_VAL](group__bt__uuid.md#gad5ea6f8f92b3679cafed3ac61f5d9128)   0x2b44 |
|  | GATT Characteristic Activity Current Session UUID Value. |
| #define | [BT\_UUID\_GATT\_ACS](group__bt__uuid.md#ga12e8344ffb0ae5d3ff088df56f22d440)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ACS\_VAL](group__bt__uuid.md#gad5ea6f8f92b3679cafed3ac61f5d9128)) |
|  | GATT Characteristic Activity Current Session. |
| #define | [BT\_UUID\_GATT\_PHY\_ASDESC\_VAL](group__bt__uuid.md#ga16b2c15259a5c4d456a43df7be9080d6)   0x2b45 |
|  | GATT Characteristic Physical Activity Session Descriptor UUID Value. |
| #define | [BT\_UUID\_GATT\_PHY\_ASDESC](group__bt__uuid.md#ga3906642c3830a0dff787b6218f502b74)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PHY\_ASDESC\_VAL](group__bt__uuid.md#ga16b2c15259a5c4d456a43df7be9080d6)) |
|  | GATT Characteristic Physical Activity Session Descriptor. |
| #define | [BT\_UUID\_GATT\_PREF\_U\_VAL](group__bt__uuid.md#gae9e12c4297a520b3d626fbd7f4e9c49c)   0x2b46 |
|  | GATT Characteristic Preferred Units UUID Value. |
| #define | [BT\_UUID\_GATT\_PREF\_U](group__bt__uuid.md#ga323afc65d2c3568d9a3267328e46879e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PREF\_U\_VAL](group__bt__uuid.md#gae9e12c4297a520b3d626fbd7f4e9c49c)) |
|  | GATT Characteristic Preferred Units. |
| #define | [BT\_UUID\_GATT\_HRES\_H\_VAL](group__bt__uuid.md#gab74738d5e1fde9be0ae137603d58266a)   0x2b47 |
|  | GATT Characteristic High Resolution Height UUID Value. |
| #define | [BT\_UUID\_GATT\_HRES\_H](group__bt__uuid.md#gaf095ec3ea1b24f184fce737db3b16855)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_HRES\_H\_VAL](group__bt__uuid.md#gab74738d5e1fde9be0ae137603d58266a)) |
|  | GATT Characteristic High Resolution Height. |
| #define | [BT\_UUID\_GATT\_MID\_NAME\_VAL](group__bt__uuid.md#gae44137b7932e5493b66c037b93177f30)   0x2b48 |
|  | GATT Characteristic Middle Name UUID Value. |
| #define | [BT\_UUID\_GATT\_MID\_NAME](group__bt__uuid.md#ga478706893a1e14f1af28928ea7ee3dde)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_MID\_NAME\_VAL](group__bt__uuid.md#gae44137b7932e5493b66c037b93177f30)) |
|  | GATT Characteristic Middle Name. |
| #define | [BT\_UUID\_GATT\_STRDLEN\_VAL](group__bt__uuid.md#ga8ebc62a93e6c323031cd64a4c89bc191)   0x2b49 |
|  | GATT Characteristic Stride Length UUID Value. |
| #define | [BT\_UUID\_GATT\_STRDLEN](group__bt__uuid.md#ga1a05d2cef4e003d8a9f417cfb1915600)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_STRDLEN\_VAL](group__bt__uuid.md#ga8ebc62a93e6c323031cd64a4c89bc191)) |
|  | GATT Characteristic Stride Length. |
| #define | [BT\_UUID\_GATT\_HANDEDNESS\_VAL](group__bt__uuid.md#gaa3a2515dfef7871cb4f2ddaa9b1838bf)   0x2b4a |
|  | GATT Characteristic Handedness UUID Value. |
| #define | [BT\_UUID\_GATT\_HANDEDNESS](group__bt__uuid.md#ga9e0dd2e887dacb08466f63951bdce22c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_HANDEDNESS\_VAL](group__bt__uuid.md#gaa3a2515dfef7871cb4f2ddaa9b1838bf)) |
|  | GATT Characteristic Handedness. |
| #define | [BT\_UUID\_GATT\_DEVICE\_WP\_VAL](group__bt__uuid.md#ga7e3028631b4f17fc6127eb41343f6113)   0x2b4b |
|  | GATT Characteristic Device Wearing Position UUID Value. |
| #define | [BT\_UUID\_GATT\_DEVICE\_WP](group__bt__uuid.md#gaf26f9aa3d7566892cb4d851a212c7a26)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DEVICE\_WP\_VAL](group__bt__uuid.md#ga7e3028631b4f17fc6127eb41343f6113)) |
|  | GATT Characteristic Device Wearing Position. |
| #define | [BT\_UUID\_GATT\_4ZHRL\_VAL](group__bt__uuid.md#gaff4928b6e4a0e7329ab18beed9600f1a)   0x2b4c |
|  | GATT Characteristic Four Zone Heart Rate Limit UUID Value. |
| #define | [BT\_UUID\_GATT\_4ZHRL](group__bt__uuid.md#ga1ead62ac6b72dfafdbe46f3c6a3202a1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_4ZHRL\_VAL](group__bt__uuid.md#gaff4928b6e4a0e7329ab18beed9600f1a)) |
|  | GATT Characteristic Four Zone Heart Rate Limit. |
| #define | [BT\_UUID\_GATT\_HIET\_VAL](group__bt__uuid.md#ga7fcf423cf762d9c9b534c869581ef358)   0x2b4d |
|  | GATT Characteristic High Intensity Exercise Threshold UUID Value. |
| #define | [BT\_UUID\_GATT\_HIET](group__bt__uuid.md#gaa0a5aa82b3eccfc14eef8ce4006899f8)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_HIET\_VAL](group__bt__uuid.md#ga7fcf423cf762d9c9b534c869581ef358)) |
|  | GATT Characteristic High Intensity Exercise Threshold. |
| #define | [BT\_UUID\_GATT\_AG\_VAL](group__bt__uuid.md#ga80d44e488176d215f9da4c531915b9f4)   0x2b4e |
|  | GATT Characteristic Activity Goal UUID Value. |
| #define | [BT\_UUID\_GATT\_AG](group__bt__uuid.md#ga8ab5d539f23fd30b6b44294d52cd148f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AG\_VAL](group__bt__uuid.md#ga80d44e488176d215f9da4c531915b9f4)) |
|  | GATT Characteristic Activity Goal. |
| #define | [BT\_UUID\_GATT\_SIN\_VAL](group__bt__uuid.md#ga9f129bc582093032197016897e86748f)   0x2b4f |
|  | GATT Characteristic Sedentary Interval Notification UUID Value. |
| #define | [BT\_UUID\_GATT\_SIN](group__bt__uuid.md#gaac75b92f8daddb4aecd5b6e0b2a5d33b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SIN\_VAL](group__bt__uuid.md#ga9f129bc582093032197016897e86748f)) |
|  | GATT Characteristic Sedentary Interval Notification. |
| #define | [BT\_UUID\_GATT\_CI\_VAL](group__bt__uuid.md#ga462b52ed2ca39b836e0d7ea3d7a6a609)   0x2b50 |
|  | GATT Characteristic Caloric Intake UUID Value. |
| #define | [BT\_UUID\_GATT\_CI](group__bt__uuid.md#ga61d3e8f34e0f3d466d4a0b64258a6d13)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CI\_VAL](group__bt__uuid.md#ga462b52ed2ca39b836e0d7ea3d7a6a609)) |
|  | GATT Characteristic Caloric Intake. |
| #define | [BT\_UUID\_GATT\_TMAPR\_VAL](group__bt__uuid.md#ga781de482737cfc42662f6e8b1114070f)   0x2b51 |
|  | GATT Characteristic TMAP Role UUID Value. |
| #define | [BT\_UUID\_GATT\_TMAPR](group__bt__uuid.md#ga66395bad8099540561670bd1e588e1e9)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TMAPR\_VAL](group__bt__uuid.md#ga781de482737cfc42662f6e8b1114070f)) |
|  | GATT Characteristic TMAP Role. |
| #define | [BT\_UUID\_AICS\_STATE\_VAL](group__bt__uuid.md#ga95a4d3f8c62782325d2f2bb0df260a97)   0x2b77 |
|  | Audio Input Control Service State value. |
| #define | [BT\_UUID\_AICS\_STATE](group__bt__uuid.md#ga36fff8099e5a7d9c0cbd407b9b261742)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_AICS\_STATE\_VAL](group__bt__uuid.md#ga95a4d3f8c62782325d2f2bb0df260a97)) |
|  | Audio Input Control Service State. |
| #define | [BT\_UUID\_AICS\_GAIN\_SETTINGS\_VAL](group__bt__uuid.md#gaab9ed2f83db5e1ea5c2756b8045ca708)   0x2b78 |
|  | Audio Input Control Service Gain Settings Properties value. |
| #define | [BT\_UUID\_AICS\_GAIN\_SETTINGS](group__bt__uuid.md#ga0b26573f473babc0d4b4d1f817a0e292)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_AICS\_GAIN\_SETTINGS\_VAL](group__bt__uuid.md#gaab9ed2f83db5e1ea5c2756b8045ca708)) |
|  | Audio Input Control Service Gain Settings Properties. |
| #define | [BT\_UUID\_AICS\_INPUT\_TYPE\_VAL](group__bt__uuid.md#ga60250c00a3361316b78e5fa6fef335d7)   0x2b79 |
|  | Audio Input Control Service Input Type value. |
| #define | [BT\_UUID\_AICS\_INPUT\_TYPE](group__bt__uuid.md#gaf9ba49297331bec61b2706ad43a88260)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_AICS\_INPUT\_TYPE\_VAL](group__bt__uuid.md#ga60250c00a3361316b78e5fa6fef335d7)) |
|  | Audio Input Control Service Input Type. |
| #define | [BT\_UUID\_AICS\_INPUT\_STATUS\_VAL](group__bt__uuid.md#ga369eeaa589fbb61fffe8e3dabab5aebf)   0x2b7a |
|  | Audio Input Control Service Input Status value. |
| #define | [BT\_UUID\_AICS\_INPUT\_STATUS](group__bt__uuid.md#ga549930ceca2598871f140ec81778923b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_AICS\_INPUT\_STATUS\_VAL](group__bt__uuid.md#ga369eeaa589fbb61fffe8e3dabab5aebf)) |
|  | Audio Input Control Service Input Status. |
| #define | [BT\_UUID\_AICS\_CONTROL\_VAL](group__bt__uuid.md#gacd6c279c902bb8dfa59e886f52161f9a)   0x2b7b |
|  | Audio Input Control Service Control Point value. |
| #define | [BT\_UUID\_AICS\_CONTROL](group__bt__uuid.md#gae507a2c877c174accb4eb1c18fd7bbc4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_AICS\_CONTROL\_VAL](group__bt__uuid.md#gacd6c279c902bb8dfa59e886f52161f9a)) |
|  | Audio Input Control Service Control Point. |
| #define | [BT\_UUID\_AICS\_DESCRIPTION\_VAL](group__bt__uuid.md#ga0cb5c04f3f8c257d012d9907ba8cde38)   0x2b7c |
|  | Audio Input Control Service Input Description value. |
| #define | [BT\_UUID\_AICS\_DESCRIPTION](group__bt__uuid.md#ga9de23aa540a7e07e4c932d60dd84f7c5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_AICS\_DESCRIPTION\_VAL](group__bt__uuid.md#ga0cb5c04f3f8c257d012d9907ba8cde38)) |
|  | Audio Input Control Service Input Description. |
| #define | [BT\_UUID\_VCS\_STATE\_VAL](group__bt__uuid.md#ga40235c24d4ab2f3c068e8833295bfb89)   0x2b7d |
|  | Volume Control Setting value. |
| #define | [BT\_UUID\_VCS\_STATE](group__bt__uuid.md#gac116f24a102a7b8e6aa80533cc096615)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_VCS\_STATE\_VAL](group__bt__uuid.md#ga40235c24d4ab2f3c068e8833295bfb89)) |
|  | Volume Control Setting. |
| #define | [BT\_UUID\_VCS\_CONTROL\_VAL](group__bt__uuid.md#ga303c174785d397db54c53572c421e6d3)   0x2b7e |
|  | Volume Control Control point value. |
| #define | [BT\_UUID\_VCS\_CONTROL](group__bt__uuid.md#ga24d297c008c9679dcb7078f68affe0a1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_VCS\_CONTROL\_VAL](group__bt__uuid.md#ga303c174785d397db54c53572c421e6d3)) |
|  | Volume Control Control point. |
| #define | [BT\_UUID\_VCS\_FLAGS\_VAL](group__bt__uuid.md#ga7f3385da26bf4cddfe12f48147457baf)   0x2b7f |
|  | Volume Control Flags value. |
| #define | [BT\_UUID\_VCS\_FLAGS](group__bt__uuid.md#ga47ff83b277e87cf0629a633a67567e34)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_VCS\_FLAGS\_VAL](group__bt__uuid.md#ga7f3385da26bf4cddfe12f48147457baf)) |
|  | Volume Control Flags. |
| #define | [BT\_UUID\_VOCS\_STATE\_VAL](group__bt__uuid.md#gae5535cd478c55390fa3c1199584e614d)   0x2b80 |
|  | Volume Offset State value. |
| #define | [BT\_UUID\_VOCS\_STATE](group__bt__uuid.md#ga1d198cbdb65d99eb877fa871f4ac5155)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_VOCS\_STATE\_VAL](group__bt__uuid.md#gae5535cd478c55390fa3c1199584e614d)) |
|  | Volume Offset State. |
| #define | [BT\_UUID\_VOCS\_LOCATION\_VAL](group__bt__uuid.md#ga784c29647d14983b3d3f37f9188b6b6f)   0x2b81 |
|  | Audio Location value. |
| #define | [BT\_UUID\_VOCS\_LOCATION](group__bt__uuid.md#gad3493dcb58547b4108e8ded6e48e8a8c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_VOCS\_LOCATION\_VAL](group__bt__uuid.md#ga784c29647d14983b3d3f37f9188b6b6f)) |
|  | Audio Location. |
| #define | [BT\_UUID\_VOCS\_CONTROL\_VAL](group__bt__uuid.md#gacc2e4a9ac1e93bf6ed1a7001c8038a52)   0x2b82 |
|  | Volume Offset Control Point value. |
| #define | [BT\_UUID\_VOCS\_CONTROL](group__bt__uuid.md#gafb68257cf790e12dab2b888320617de7)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_VOCS\_CONTROL\_VAL](group__bt__uuid.md#gacc2e4a9ac1e93bf6ed1a7001c8038a52)) |
|  | Volume Offset Control Point. |
| #define | [BT\_UUID\_VOCS\_DESCRIPTION\_VAL](group__bt__uuid.md#ga46471ebc019b7c842c0b76efed504625)   0x2b83 |
|  | Volume Offset Audio Output Description value. |
| #define | [BT\_UUID\_VOCS\_DESCRIPTION](group__bt__uuid.md#gad4a8b4af9f5935b86d1541a2086609d3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_VOCS\_DESCRIPTION\_VAL](group__bt__uuid.md#ga46471ebc019b7c842c0b76efed504625)) |
|  | Volume Offset Audio Output Description. |
| #define | [BT\_UUID\_CSIS\_SIRK\_VAL](group__bt__uuid.md#gadaf8b170c1f603f8a61515090558b96c)   0x2b84 |
|  | Set Identity Resolving Key value. |
| #define | [BT\_UUID\_CSIS\_SIRK](group__bt__uuid.md#gac0a3863cf4a928bfaae397b14771622d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CSIS\_SIRK\_VAL](group__bt__uuid.md#gadaf8b170c1f603f8a61515090558b96c)) |
|  | Set Identity Resolving Key. |
| #define | [BT\_UUID\_CSIS\_SET\_SIZE\_VAL](group__bt__uuid.md#ga7b5cf381c0806b01fc91c806588a3cfc)   0x2b85 |
|  | Set size value. |
| #define | [BT\_UUID\_CSIS\_SET\_SIZE](group__bt__uuid.md#ga8995e2ac9173ab613c35f56c5a353d69)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CSIS\_SET\_SIZE\_VAL](group__bt__uuid.md#ga7b5cf381c0806b01fc91c806588a3cfc)) |
|  | Set size. |
| #define | [BT\_UUID\_CSIS\_SET\_LOCK\_VAL](group__bt__uuid.md#ga7f296b9f8b09bc62e639b2e1076894dc)   0x2b86 |
|  | Set lock value. |
| #define | [BT\_UUID\_CSIS\_SET\_LOCK](group__bt__uuid.md#gaf6493077e90f87765c1c1efc044436f0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CSIS\_SET\_LOCK\_VAL](group__bt__uuid.md#ga7f296b9f8b09bc62e639b2e1076894dc)) |
|  | Set lock. |
| #define | [BT\_UUID\_CSIS\_RANK\_VAL](group__bt__uuid.md#ga21db384fb731b1903239a4ecc70138d4)   0x2b87 |
|  | Rank value. |
| #define | [BT\_UUID\_CSIS\_RANK](group__bt__uuid.md#gaa356de4e79779132ed4eeda837b7db57)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CSIS\_RANK\_VAL](group__bt__uuid.md#ga21db384fb731b1903239a4ecc70138d4)) |
|  | Rank. |
| #define | [BT\_UUID\_GATT\_EDKM\_VAL](group__bt__uuid.md#ga31e072f6706b28c309e518cd9449b883)   0x2b88 |
|  | GATT Characteristic Encrypted Data Key Material UUID Value. |
| #define | [BT\_UUID\_GATT\_EDKM](group__bt__uuid.md#ga9b0daac4f03e23c10fca1a40d07e1618)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_EDKM\_VAL](group__bt__uuid.md#ga31e072f6706b28c309e518cd9449b883)) |
|  | GATT Characteristic Encrypted Data Key Material. |
| #define | [BT\_UUID\_GATT\_AE32\_VAL](group__bt__uuid.md#gac74ea8f9e2800086c286c5fa4185a00e)   0x2b89 |
|  | GATT Characteristic Apparent Energy 32 UUID Value. |
| #define | [BT\_UUID\_GATT\_AE32](group__bt__uuid.md#ga646adee056d3097eb180bdea1ad0fd33)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AE32\_VAL](group__bt__uuid.md#gac74ea8f9e2800086c286c5fa4185a00e)) |
|  | GATT Characteristic Apparent Energy 32. |
| #define | [BT\_UUID\_GATT\_AP\_VAL](group__bt__uuid.md#gac3a8b96b59612b0e4ef704afae04e7e3)   0x2b8a |
|  | GATT Characteristic Apparent Power UUID Value. |
| #define | [BT\_UUID\_GATT\_AP](group__bt__uuid.md#ga91eea2c307dfa99632b52d062c2a2645)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_AP\_VAL](group__bt__uuid.md#gac3a8b96b59612b0e4ef704afae04e7e3)) |
|  | GATT Characteristic Apparent Power. |
| #define | [BT\_UUID\_GATT\_CO2CONC\_VAL](group__bt__uuid.md#gaa1edc406495ec9797e153daf1e6cca1f)   0x2b8c |
|  | GATT Characteristic CO2 Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_CO2CONC](group__bt__uuid.md#gab4db18c78e70c6e781dcda022be13276)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CO2CONC\_VAL](group__bt__uuid.md#gaa1edc406495ec9797e153daf1e6cca1f)) |
|  | GATT Characteristic CO2 Concentration. |
| #define | [BT\_UUID\_GATT\_COS\_VAL](group__bt__uuid.md#ga7a568dfc0ac219b16bdd606953b88184)   0x2b8d |
|  | GATT Characteristic Cosine of the Angle UUID Value. |
| #define | [BT\_UUID\_GATT\_COS](group__bt__uuid.md#ga7d456cc3cdf5d6b25a35f6cca08da585)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_COS\_VAL](group__bt__uuid.md#ga7a568dfc0ac219b16bdd606953b88184)) |
|  | GATT Characteristic Cosine of the Angle. |
| #define | [BT\_UUID\_GATT\_DEVTF\_VAL](group__bt__uuid.md#ga7da79c223cdfb3be45607e86f71a6caa)   0x2b8e |
|  | GATT Characteristic Device Time Feature UUID Value. |
| #define | [BT\_UUID\_GATT\_DEVTF](group__bt__uuid.md#ga7e8485b07e0c359964be7b6f8e896546)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DEVTF\_VAL](group__bt__uuid.md#ga7da79c223cdfb3be45607e86f71a6caa)) |
|  | GATT Characteristic Device Time Feature. |
| #define | [BT\_UUID\_GATT\_DEVTP\_VAL](group__bt__uuid.md#ga744f71f5b0c8d2cfe4faf6107f33633b)   0x2b8f |
|  | GATT Characteristic Device Time Parameters UUID Value. |
| #define | [BT\_UUID\_GATT\_DEVTP](group__bt__uuid.md#ga0f22bf31cbe7a58944340b03ccf591c5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DEVTP\_VAL](group__bt__uuid.md#ga744f71f5b0c8d2cfe4faf6107f33633b)) |
|  | GATT Characteristic Device Time Parameters. |
| #define | [BT\_UUID\_GATT\_DEVT\_VAL](group__bt__uuid.md#ga7d0ff38d80780d63e4b43a200be5c7d3)   0x2b90 |
|  | GATT Characteristic Device Time UUID Value. |
| #define | [BT\_UUID\_GATT\_DEVT](group__bt__uuid.md#ga9eb6c84a8ab924deb9fbe5b331d2628a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DEVT\_VAL](group__bt__uuid.md#ga7d0ff38d80780d63e4b43a200be5c7d3)) |
|  | GATT Characteristic String. |
| #define | [BT\_UUID\_GATT\_DEVTCP\_VAL](group__bt__uuid.md#ga111396f18a4d565fabe50e4ab4bb6b01)   0x2b91 |
|  | GATT Characteristic Device Time Control Point UUID Value. |
| #define | [BT\_UUID\_GATT\_DEVTCP](group__bt__uuid.md#ga18de8889aa0297fc80a6fc2846f83da2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_DEVTCP\_VAL](group__bt__uuid.md#ga111396f18a4d565fabe50e4ab4bb6b01)) |
|  | GATT Characteristic Device Time Control Point. |
| #define | [BT\_UUID\_GATT\_TCLD\_VAL](group__bt__uuid.md#ga2aa7a226cd54e1e2435a045cd936c222)   0x2b92 |
|  | GATT Characteristic Time Change Log Data UUID Value. |
| #define | [BT\_UUID\_GATT\_TCLD](group__bt__uuid.md#ga0e38fdb6334c4aa1b3fe8163cad290ea)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TCLD\_VAL](group__bt__uuid.md#ga2aa7a226cd54e1e2435a045cd936c222)) |
|  | GATT Characteristic Time Change Log Data. |
| #define | [BT\_UUID\_MCS\_PLAYER\_NAME\_VAL](group__bt__uuid.md#ga26421e4fde9e424af8318a2a06e55729)   0x2b93 |
|  | Media player name value. |
| #define | [BT\_UUID\_MCS\_PLAYER\_NAME](group__bt__uuid.md#ga25706c3572dd91b223dd7cbea6cc71e2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_PLAYER\_NAME\_VAL](group__bt__uuid.md#ga26421e4fde9e424af8318a2a06e55729)) |
|  | Media player name. |
| #define | [BT\_UUID\_MCS\_ICON\_OBJ\_ID\_VAL](group__bt__uuid.md#gadefa705eae4221748b18f5a088c768ca)   0x2b94 |
|  | Media Icon Object ID value. |
| #define | [BT\_UUID\_MCS\_ICON\_OBJ\_ID](group__bt__uuid.md#ga63ce9edebeebcac1e7344efdabc6519e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_ICON\_OBJ\_ID\_VAL](group__bt__uuid.md#gadefa705eae4221748b18f5a088c768ca)) |
|  | Media Icon Object ID. |
| #define | [BT\_UUID\_MCS\_ICON\_URL\_VAL](group__bt__uuid.md#gad80db7e88bc50944b71ca4c51f6674db)   0x2b95 |
|  | Media Icon URL value. |
| #define | [BT\_UUID\_MCS\_ICON\_URL](group__bt__uuid.md#ga1ff74274cc34b8ba88af2b455109eb98)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_ICON\_URL\_VAL](group__bt__uuid.md#gad80db7e88bc50944b71ca4c51f6674db)) |
|  | Media Icon URL. |
| #define | [BT\_UUID\_MCS\_TRACK\_CHANGED\_VAL](group__bt__uuid.md#ga71cb9b105eb4a581167e09fb293d7dd5)   0x2b96 |
|  | Track Changed value. |
| #define | [BT\_UUID\_MCS\_TRACK\_CHANGED](group__bt__uuid.md#gae7e7b15660158399bd837f10c1380982)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_TRACK\_CHANGED\_VAL](group__bt__uuid.md#ga71cb9b105eb4a581167e09fb293d7dd5)) |
|  | Track Changed. |
| #define | [BT\_UUID\_MCS\_TRACK\_TITLE\_VAL](group__bt__uuid.md#ga8082647831b1da4237b85346f1dca249)   0x2b97 |
|  | Track Title value. |
| #define | [BT\_UUID\_MCS\_TRACK\_TITLE](group__bt__uuid.md#gafb41d75e4bf569b1efeba763fb93722f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_TRACK\_TITLE\_VAL](group__bt__uuid.md#ga8082647831b1da4237b85346f1dca249)) |
|  | Track Title. |
| #define | [BT\_UUID\_MCS\_TRACK\_DURATION\_VAL](group__bt__uuid.md#ga7786188af799df504bcbba1aa007a3eb)   0x2b98 |
|  | Track Duration value. |
| #define | [BT\_UUID\_MCS\_TRACK\_DURATION](group__bt__uuid.md#ga76d4d2c92df6b9d82d60ee7fe835d29c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_TRACK\_DURATION\_VAL](group__bt__uuid.md#ga7786188af799df504bcbba1aa007a3eb)) |
|  | Track Duration. |
| #define | [BT\_UUID\_MCS\_TRACK\_POSITION\_VAL](group__bt__uuid.md#ga6b74c773a708eccb84074cb7ef8c8fe2)   0x2b99 |
|  | Track Position value. |
| #define | [BT\_UUID\_MCS\_TRACK\_POSITION](group__bt__uuid.md#gaa4665539c5027680a843d851bf1b8bfe)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_TRACK\_POSITION\_VAL](group__bt__uuid.md#ga6b74c773a708eccb84074cb7ef8c8fe2)) |
|  | Track Position. |
| #define | [BT\_UUID\_MCS\_PLAYBACK\_SPEED\_VAL](group__bt__uuid.md#gadfe7acf9dbc6ebd3fe21fe469f39e937)   0x2b9a |
|  | Playback Speed value. |
| #define | [BT\_UUID\_MCS\_PLAYBACK\_SPEED](group__bt__uuid.md#ga47629d64d3ed4587089fb8551c4c594c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_PLAYBACK\_SPEED\_VAL](group__bt__uuid.md#gadfe7acf9dbc6ebd3fe21fe469f39e937)) |
|  | Playback Speed. |
| #define | [BT\_UUID\_MCS\_SEEKING\_SPEED\_VAL](group__bt__uuid.md#gaf8ebb66a23e2bed1c7e5b08c79cfe579)   0x2b9b |
|  | Seeking Speed value. |
| #define | [BT\_UUID\_MCS\_SEEKING\_SPEED](group__bt__uuid.md#gac1d6109a86c67555c4b632d6a0563d92)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_SEEKING\_SPEED\_VAL](group__bt__uuid.md#gaf8ebb66a23e2bed1c7e5b08c79cfe579)) |
|  | Seeking Speed. |
| #define | [BT\_UUID\_MCS\_TRACK\_SEGMENTS\_OBJ\_ID\_VAL](group__bt__uuid.md#gafa793d37f3d9c57d1f456a0a9c5dba36)   0x2b9c |
|  | Track Segments Object ID value. |
| #define | [BT\_UUID\_MCS\_TRACK\_SEGMENTS\_OBJ\_ID](group__bt__uuid.md#gaa1e0e61ba28da785308e5dafd72931fd)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_TRACK\_SEGMENTS\_OBJ\_ID\_VAL](group__bt__uuid.md#gafa793d37f3d9c57d1f456a0a9c5dba36)) |
|  | Track Segments Object ID. |
| #define | [BT\_UUID\_MCS\_CURRENT\_TRACK\_OBJ\_ID\_VAL](group__bt__uuid.md#ga884f66865500c127def77f2764b7a322)   0x2b9d |
|  | Current Track Object ID value. |
| #define | [BT\_UUID\_MCS\_CURRENT\_TRACK\_OBJ\_ID](group__bt__uuid.md#gad11916b1a6704ce9cc80a35ddd1b1023)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_CURRENT\_TRACK\_OBJ\_ID\_VAL](group__bt__uuid.md#ga884f66865500c127def77f2764b7a322)) |
|  | Current Track Object ID. |
| #define | [BT\_UUID\_MCS\_NEXT\_TRACK\_OBJ\_ID\_VAL](group__bt__uuid.md#ga791f147766bd7511fdeb98ed9f4e3e05)   0x2b9e |
|  | Next Track Object ID value. |
| #define | [BT\_UUID\_MCS\_NEXT\_TRACK\_OBJ\_ID](group__bt__uuid.md#gaba85414e514d71f1ada3cd32ab7b9857)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_NEXT\_TRACK\_OBJ\_ID\_VAL](group__bt__uuid.md#ga791f147766bd7511fdeb98ed9f4e3e05)) |
|  | Next Track Object ID. |
| #define | [BT\_UUID\_MCS\_PARENT\_GROUP\_OBJ\_ID\_VAL](group__bt__uuid.md#ga06410ca2d5575cb44f3f365c27960487)   0x2b9f |
|  | Parent Group Object ID value. |
| #define | [BT\_UUID\_MCS\_PARENT\_GROUP\_OBJ\_ID](group__bt__uuid.md#ga2dbb766bda1581f49ff331beefdad2c5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_PARENT\_GROUP\_OBJ\_ID\_VAL](group__bt__uuid.md#ga06410ca2d5575cb44f3f365c27960487)) |
|  | Parent Group Object ID. |
| #define | [BT\_UUID\_MCS\_CURRENT\_GROUP\_OBJ\_ID\_VAL](group__bt__uuid.md#ga3873c1d5075d4cb3035509ce57595c28)   0x2ba0 |
|  | Group Object ID value. |
| #define | [BT\_UUID\_MCS\_CURRENT\_GROUP\_OBJ\_ID](group__bt__uuid.md#ga303b89c5ba301bd2c18a3eb48f214ded)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_CURRENT\_GROUP\_OBJ\_ID\_VAL](group__bt__uuid.md#ga3873c1d5075d4cb3035509ce57595c28)) |
|  | Group Object ID. |
| #define | [BT\_UUID\_MCS\_PLAYING\_ORDER\_VAL](group__bt__uuid.md#ga0b17cfa67cdec5722cf51ebc9a616384)   0x2ba1 |
|  | Playing Order value. |
| #define | [BT\_UUID\_MCS\_PLAYING\_ORDER](group__bt__uuid.md#ga7c676d7019e19189cffaf34aefe66c59)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_PLAYING\_ORDER\_VAL](group__bt__uuid.md#ga0b17cfa67cdec5722cf51ebc9a616384)) |
|  | Playing Order. |
| #define | [BT\_UUID\_MCS\_PLAYING\_ORDERS\_VAL](group__bt__uuid.md#ga103cd4f0ae88b27c32ab7854c331de59)   0x2ba2 |
|  | Playing Orders supported value. |
| #define | [BT\_UUID\_MCS\_PLAYING\_ORDERS](group__bt__uuid.md#ga283a2f22a049a6c78221d1186d17e6f5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_PLAYING\_ORDERS\_VAL](group__bt__uuid.md#ga103cd4f0ae88b27c32ab7854c331de59)) |
|  | Playing Orders supported. |
| #define | [BT\_UUID\_MCS\_MEDIA\_STATE\_VAL](group__bt__uuid.md#ga8f62ba6fe627eda5c188151a89d1299f)   0x2ba3 |
|  | Media State value. |
| #define | [BT\_UUID\_MCS\_MEDIA\_STATE](group__bt__uuid.md#gaadaf94fbf0d316505e27fc115998ffd2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_MEDIA\_STATE\_VAL](group__bt__uuid.md#ga8f62ba6fe627eda5c188151a89d1299f)) |
|  | Media State. |
| #define | [BT\_UUID\_MCS\_MEDIA\_CONTROL\_POINT\_VAL](group__bt__uuid.md#ga3b276420dc39941339c3f3bcb3835d3c)   0x2ba4 |
|  | Media Control Point value. |
| #define | [BT\_UUID\_MCS\_MEDIA\_CONTROL\_POINT](group__bt__uuid.md#gae3dc24d21d36349c7af95fe90db6ec91)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_MEDIA\_CONTROL\_POINT\_VAL](group__bt__uuid.md#ga3b276420dc39941339c3f3bcb3835d3c)) |
|  | Media Control Point. |
| #define | [BT\_UUID\_MCS\_MEDIA\_CONTROL\_OPCODES\_VAL](group__bt__uuid.md#ga6eb18372f842f362bb45c93bbefd560b)   0x2ba5 |
|  | Media control opcodes supported value. |
| #define | [BT\_UUID\_MCS\_MEDIA\_CONTROL\_OPCODES](group__bt__uuid.md#ga6ef3d74033d401d7d5fb092485faee16)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_MEDIA\_CONTROL\_OPCODES\_VAL](group__bt__uuid.md#ga6eb18372f842f362bb45c93bbefd560b)) |
|  | Media control opcodes supported. |
| #define | [BT\_UUID\_MCS\_SEARCH\_RESULTS\_OBJ\_ID\_VAL](group__bt__uuid.md#ga337509c52a77206589a8208cf6ac3ac0)   0x2ba6 |
|  | Search result object ID value. |
| #define | [BT\_UUID\_MCS\_SEARCH\_RESULTS\_OBJ\_ID](group__bt__uuid.md#ga2ce71ff006f161cd899fb6b09a98c66f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_SEARCH\_RESULTS\_OBJ\_ID\_VAL](group__bt__uuid.md#ga337509c52a77206589a8208cf6ac3ac0)) |
|  | Search result object ID. |
| #define | [BT\_UUID\_MCS\_SEARCH\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gab89e74c66515dfcdffcb4967b3de4f0d)   0x2ba7 |
|  | Search control point value. |
| #define | [BT\_UUID\_MCS\_SEARCH\_CONTROL\_POINT](group__bt__uuid.md#gab7892abc4201dc18da2bd4a2efca1963)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCS\_SEARCH\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gab89e74c66515dfcdffcb4967b3de4f0d)) |
|  | Search control point. |
| #define | [BT\_UUID\_GATT\_E32\_VAL](group__bt__uuid.md#ga8f238d8197b3293562809916eb667f27)   0x2ba8 |
|  | GATT Characteristic Energy 32 UUID Value. |
| #define | [BT\_UUID\_GATT\_E32](group__bt__uuid.md#ga6419bfcbe6cad1f568b9e212d704e7c7)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_E32\_VAL](group__bt__uuid.md#ga8f238d8197b3293562809916eb667f27)) |
|  | GATT Characteristic Energy 32. |
| #define | [BT\_UUID\_OTS\_TYPE\_MPL\_ICON\_VAL](group__bt__uuid.md#gaeb12a1e806156ec1b7f945dddce3fa24)   0x2ba9 |
|  | Media Player Icon Object Type value. |
| #define | [BT\_UUID\_OTS\_TYPE\_MPL\_ICON](group__bt__uuid.md#ga3b425e5f019ba59d2d76a5d6e9cc16ee)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_TYPE\_MPL\_ICON\_VAL](group__bt__uuid.md#gaeb12a1e806156ec1b7f945dddce3fa24)) |
|  | Media Player Icon Object Type. |
| #define | [BT\_UUID\_OTS\_TYPE\_TRACK\_SEGMENT\_VAL](group__bt__uuid.md#gaf05ecc673eae8b56ce6d5a98e5b22130)   0x2baa |
|  | Track Segments Object Type value. |
| #define | [BT\_UUID\_OTS\_TYPE\_TRACK\_SEGMENT](group__bt__uuid.md#ga5f3fdbd12cc804ed0ca811d4bafe1109)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_TYPE\_TRACK\_SEGMENT\_VAL](group__bt__uuid.md#gaf05ecc673eae8b56ce6d5a98e5b22130)) |
|  | Track Segments Object Type. |
| #define | [BT\_UUID\_OTS\_TYPE\_TRACK\_VAL](group__bt__uuid.md#gaf4094e3381053890f6264d17ff129255)   0x2bab |
|  | Track Object Type value. |
| #define | [BT\_UUID\_OTS\_TYPE\_TRACK](group__bt__uuid.md#gafcf9774a2b6aa1081b6c1a03b31a0c07)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_TYPE\_TRACK\_VAL](group__bt__uuid.md#gaf4094e3381053890f6264d17ff129255)) |
|  | Track Object Type. |
| #define | [BT\_UUID\_OTS\_TYPE\_GROUP\_VAL](group__bt__uuid.md#gafc689c443c46385aefbca0e1db73f877)   0x2bac |
|  | Group Object Type value. |
| #define | [BT\_UUID\_OTS\_TYPE\_GROUP](group__bt__uuid.md#ga7a6fd4221135821cd15a3ba10f33532d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OTS\_TYPE\_GROUP\_VAL](group__bt__uuid.md#gafc689c443c46385aefbca0e1db73f877)) |
|  | Group Object Type. |
| #define | [BT\_UUID\_GATT\_CTEE\_VAL](group__bt__uuid.md#ga6577476ef4d85191e5d5533f6bb99b2d)   0x2bad |
|  | GATT Characteristic Constant Tone Extension Enable UUID Value. |
| #define | [BT\_UUID\_GATT\_CTEE](group__bt__uuid.md#ga985a0ebcc0a61e2c4d9f2f61a7a1afb0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CTEE\_VAL](group__bt__uuid.md#ga6577476ef4d85191e5d5533f6bb99b2d)) |
|  | GATT Characteristic Constant Tone Extension Enable. |
| #define | [BT\_UUID\_GATT\_ACTEML\_VAL](group__bt__uuid.md#gaca4a23a27a2c06eb10da1a64c617cac1)   0x2bae |
|  | GATT Characteristic Advertising Constant Tone Extension Minimum Length UUID Value. |
| #define | [BT\_UUID\_GATT\_ACTEML](group__bt__uuid.md#ga51915bb0637c157a67ce4488e46905a6)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ACTEML\_VAL](group__bt__uuid.md#gaca4a23a27a2c06eb10da1a64c617cac1)) |
|  | GATT Characteristic Advertising Constant Tone Extension Minimum Length. |
| #define | [BT\_UUID\_GATT\_ACTEMTC\_VAL](group__bt__uuid.md#gad3ddda1c88208094616608b178bb27ec)   0x2baf |
|  | GATT Characteristic Advertising Constant Tone Extension Minimum Transmit Count UUID Value. |
| #define | [BT\_UUID\_GATT\_ACTEMTC](group__bt__uuid.md#ga47620598a9365d2fc8d70ada1144c9c1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ACTEMTC\_VAL](group__bt__uuid.md#gad3ddda1c88208094616608b178bb27ec)) |
|  | GATT Characteristic Advertising Constant Tone Extension Minimum Transmit Count. |
| #define | [BT\_UUID\_GATT\_ACTETD\_VAL](group__bt__uuid.md#ga165c63f8c91f61a9930b3c804f7051b7)   0x2bb0 |
|  | GATT Characteristic Advertising Constant Tone Extension Transmit Duration UUID Value. |
| #define | [BT\_UUID\_GATT\_ACTETD](group__bt__uuid.md#ga5a15560d93177634882ff117b35deab4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ACTETD\_VAL](group__bt__uuid.md#ga165c63f8c91f61a9930b3c804f7051b7)) |
|  | GATT Characteristic Advertising Constant Tone Extension Transmit Duration. |
| #define | [BT\_UUID\_GATT\_ACTEI\_VAL](group__bt__uuid.md#ga3be14ce89c7c291cdde2bf1f4ce85808)   0x2bb1 |
|  | GATT Characteristic Advertising Constant Tone Extension Interval UUID Value. |
| #define | [BT\_UUID\_GATT\_ACTEI](group__bt__uuid.md#ga492d6a8c673f4df65d34abad342f4e75)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ACTEI\_VAL](group__bt__uuid.md#ga3be14ce89c7c291cdde2bf1f4ce85808)) |
|  | GATT Characteristic Advertising Constant Tone Extension Interval. |
| #define | [BT\_UUID\_GATT\_ACTEP\_VAL](group__bt__uuid.md#gac32badacbe9099b6f00d5c3d780cdbfe)   0x2bb2 |
|  | GATT Characteristic Advertising Constant Tone Extension PHY UUID Value. |
| #define | [BT\_UUID\_GATT\_ACTEP](group__bt__uuid.md#gaff802fc0d7358acf3bd4bf3209d7aa15)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ACTEP\_VAL](group__bt__uuid.md#gac32badacbe9099b6f00d5c3d780cdbfe)) |
|  | GATT Characteristic Advertising Constant Tone Extension PHY. |
| #define | [BT\_UUID\_TBS\_PROVIDER\_NAME\_VAL](group__bt__uuid.md#gaca347be4dd1f019c5d7421d7c2c0dd29)   0x2bb3 |
|  | Bearer Provider Name value. |
| #define | [BT\_UUID\_TBS\_PROVIDER\_NAME](group__bt__uuid.md#gafaff1ecd49123fab18bce167342a0d3e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_PROVIDER\_NAME\_VAL](group__bt__uuid.md#gaca347be4dd1f019c5d7421d7c2c0dd29)) |
|  | Bearer Provider Name. |
| #define | [BT\_UUID\_TBS\_UCI\_VAL](group__bt__uuid.md#ga361ef37fd71a78544ffcbfd34ecbff6f)   0x2bb4 |
|  | Bearer UCI value. |
| #define | [BT\_UUID\_TBS\_UCI](group__bt__uuid.md#ga2d4349fc96395f603cada574841a90d2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_UCI\_VAL](group__bt__uuid.md#ga361ef37fd71a78544ffcbfd34ecbff6f)) |
|  | Bearer UCI. |
| #define | [BT\_UUID\_TBS\_TECHNOLOGY\_VAL](group__bt__uuid.md#ga066546cd6eb07098643b0fa331b813d3)   0x2bb5 |
|  | Bearer Technology value. |
| #define | [BT\_UUID\_TBS\_TECHNOLOGY](group__bt__uuid.md#ga37ec4aed5afafc2751ef3902f2ef7d73)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_TECHNOLOGY\_VAL](group__bt__uuid.md#ga066546cd6eb07098643b0fa331b813d3)) |
|  | Bearer Technology. |
| #define | [BT\_UUID\_TBS\_URI\_LIST\_VAL](group__bt__uuid.md#ga5e499b3bcb22b0ddd719aba4fed5c644)   0x2bb6 |
|  | Bearer URI Prefixes Supported List value. |
| #define | [BT\_UUID\_TBS\_URI\_LIST](group__bt__uuid.md#ga6c76f72b427694a1e1180b0d2a2adb38)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_URI\_LIST\_VAL](group__bt__uuid.md#ga5e499b3bcb22b0ddd719aba4fed5c644)) |
|  | Bearer URI Prefixes Supported List. |
| #define | [BT\_UUID\_TBS\_SIGNAL\_STRENGTH\_VAL](group__bt__uuid.md#ga44859b71e874ca148e708fde37882c4b)   0x2bb7 |
|  | Bearer Signal Strength value. |
| #define | [BT\_UUID\_TBS\_SIGNAL\_STRENGTH](group__bt__uuid.md#gaf5ebde9e6e4121909d8a165dee7fda3a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_SIGNAL\_STRENGTH\_VAL](group__bt__uuid.md#ga44859b71e874ca148e708fde37882c4b)) |
|  | Bearer Signal Strength. |
| #define | [BT\_UUID\_TBS\_SIGNAL\_INTERVAL\_VAL](group__bt__uuid.md#ga726edee9ad2a92f2a5687a3320f68f99)   0x2bb8 |
|  | Bearer Signal Strength Reporting Interval value. |
| #define | [BT\_UUID\_TBS\_SIGNAL\_INTERVAL](group__bt__uuid.md#ga189f78c9eb6829851ab0497a0e6e3f51)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_SIGNAL\_INTERVAL\_VAL](group__bt__uuid.md#ga726edee9ad2a92f2a5687a3320f68f99)) |
|  | Bearer Signal Strength Reporting Interval. |
| #define | [BT\_UUID\_TBS\_LIST\_CURRENT\_CALLS\_VAL](group__bt__uuid.md#ga1fcc7e36b3ca482eca7572c77fe3bba4)   0x2bb9 |
|  | Bearer List Current Calls value. |
| #define | [BT\_UUID\_TBS\_LIST\_CURRENT\_CALLS](group__bt__uuid.md#gaa5aea84109af0027aae9829169ab7789)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_LIST\_CURRENT\_CALLS\_VAL](group__bt__uuid.md#ga1fcc7e36b3ca482eca7572c77fe3bba4)) |
|  | Bearer List Current Calls. |
| #define | [BT\_UUID\_CCID\_VAL](group__bt__uuid.md#ga01899f1d2f5ec81669b5012ab1448e5b)   0x2bba |
|  | Content Control ID value. |
| #define | [BT\_UUID\_CCID](group__bt__uuid.md#gab76981ff7b5fe1949c606e901daa33d3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CCID\_VAL](group__bt__uuid.md#ga01899f1d2f5ec81669b5012ab1448e5b)) |
|  | Content Control ID. |
| #define | [BT\_UUID\_TBS\_STATUS\_FLAGS\_VAL](group__bt__uuid.md#ga250a14189efd3cc176ae159de0ab03ed)   0x2bbb |
|  | Status flags value. |
| #define | [BT\_UUID\_TBS\_STATUS\_FLAGS](group__bt__uuid.md#ga8f465ca9874ff4889614f13fa7057c87)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_STATUS\_FLAGS\_VAL](group__bt__uuid.md#ga250a14189efd3cc176ae159de0ab03ed)) |
|  | Status flags. |
| #define | [BT\_UUID\_TBS\_INCOMING\_URI\_VAL](group__bt__uuid.md#ga89ec945699c44fbbb220fa6798efa986)   0x2bbc |
|  | Incoming Call Target Caller ID value. |
| #define | [BT\_UUID\_TBS\_INCOMING\_URI](group__bt__uuid.md#gaa11ae7df9db3a1a3576a413db9d70539)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_INCOMING\_URI\_VAL](group__bt__uuid.md#ga89ec945699c44fbbb220fa6798efa986)) |
|  | Incoming Call Target Caller ID. |
| #define | [BT\_UUID\_TBS\_CALL\_STATE\_VAL](group__bt__uuid.md#ga07adb1e98dfdeaa84efeb28a53087286)   0x2bbd |
|  | Call State value. |
| #define | [BT\_UUID\_TBS\_CALL\_STATE](group__bt__uuid.md#gaf3c8e758416d2d7d34adb4be895f1ed0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_CALL\_STATE\_VAL](group__bt__uuid.md#ga07adb1e98dfdeaa84efeb28a53087286)) |
|  | Call State. |
| #define | [BT\_UUID\_TBS\_CALL\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gadc6f999aa7d3ebc821405bac4ed4bf35)   0x2bbe |
|  | Call Control Point value. |
| #define | [BT\_UUID\_TBS\_CALL\_CONTROL\_POINT](group__bt__uuid.md#ga9870653514120a07d85e4ea4f0a83f6e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_CALL\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gadc6f999aa7d3ebc821405bac4ed4bf35)) |
|  | Call Control Point. |
| #define | [BT\_UUID\_TBS\_OPTIONAL\_OPCODES\_VAL](group__bt__uuid.md#ga0e2f14bde4f81d44bdd4171e1bfae68e)   0x2bbf |
|  | Optional Opcodes value. |
| #define | [BT\_UUID\_TBS\_OPTIONAL\_OPCODES](group__bt__uuid.md#ga9c794c63e6c216b9a4a7518207ea7268)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_OPTIONAL\_OPCODES\_VAL](group__bt__uuid.md#ga0e2f14bde4f81d44bdd4171e1bfae68e)) |
|  | Optional Opcodes. |
| #define | [BT\_UUID\_TBS\_TERMINATE\_REASON\_VAL](group__bt__uuid.md#gab146e7f4f8b965634967ea7845a7d875)   0x2bc0 |
|  | BT\_UUID\_TBS\_TERMINATE\_REASON\_VAL. |
| #define | [BT\_UUID\_TBS\_TERMINATE\_REASON](group__bt__uuid.md#ga5eb69cfa65d293421bd2f6797cf1bdd0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_TERMINATE\_REASON\_VAL](group__bt__uuid.md#gab146e7f4f8b965634967ea7845a7d875)) |
|  | BT\_UUID\_TBS\_TERMINATE\_REASON. |
| #define | [BT\_UUID\_TBS\_INCOMING\_CALL\_VAL](group__bt__uuid.md#gaee6b14bcbd32f18efc4d7f805455deb1)   0x2bc1 |
|  | Incoming Call value. |
| #define | [BT\_UUID\_TBS\_INCOMING\_CALL](group__bt__uuid.md#ga4ec4bdf60129003573b79f8ffe993f20)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_INCOMING\_CALL\_VAL](group__bt__uuid.md#gaee6b14bcbd32f18efc4d7f805455deb1)) |
|  | Incoming Call. |
| #define | [BT\_UUID\_TBS\_FRIENDLY\_NAME\_VAL](group__bt__uuid.md#ga598672b6e2aa0bc58c62ac9755aaf64c)   0x2bc2 |
|  | Incoming Call Friendly name value. |
| #define | [BT\_UUID\_TBS\_FRIENDLY\_NAME](group__bt__uuid.md#ga32682d7390ccb0aafd82b57255007749)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TBS\_FRIENDLY\_NAME\_VAL](group__bt__uuid.md#ga598672b6e2aa0bc58c62ac9755aaf64c)) |
|  | Incoming Call Friendly name. |
| #define | [BT\_UUID\_MICS\_MUTE\_VAL](group__bt__uuid.md#ga24667ed9a87ae7f1b529cfea8515b7f3)   0x2bc3 |
|  | Microphone Control Service Mute value. |
| #define | [BT\_UUID\_MICS\_MUTE](group__bt__uuid.md#gada38c5574c186c19c71788d612bb7987)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MICS\_MUTE\_VAL](group__bt__uuid.md#ga24667ed9a87ae7f1b529cfea8515b7f3)) |
|  | Microphone Control Service Mute. |
| #define | [BT\_UUID\_ASCS\_ASE\_SNK\_VAL](group__bt__uuid.md#ga780a810da56da9b9dbba775305f70c69)   0x2bc4 |
|  | Audio Stream Endpoint Sink Characteristic value. |
| #define | [BT\_UUID\_ASCS\_ASE\_SNK](group__bt__uuid.md#ga6542839cbcda51b512d04f1039840964)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ASCS\_ASE\_SNK\_VAL](group__bt__uuid.md#ga780a810da56da9b9dbba775305f70c69)) |
|  | Audio Stream Endpoint Sink Characteristic. |
| #define | [BT\_UUID\_ASCS\_ASE\_SRC\_VAL](group__bt__uuid.md#gace1bd537f3ecee4715efde2b68ebce70)   0x2bc5 |
|  | Audio Stream Endpoint Source Characteristic value. |
| #define | [BT\_UUID\_ASCS\_ASE\_SRC](group__bt__uuid.md#gae520d2f81b0ee284d42e80854217c209)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ASCS\_ASE\_SRC\_VAL](group__bt__uuid.md#gace1bd537f3ecee4715efde2b68ebce70)) |
|  | Audio Stream Endpoint Source Characteristic. |
| #define | [BT\_UUID\_ASCS\_ASE\_CP\_VAL](group__bt__uuid.md#ga6eeb6b573908fe77254894cf3efc5378)   0x2bc6 |
|  | Audio Stream Endpoint Control Point Characteristic value. |
| #define | [BT\_UUID\_ASCS\_ASE\_CP](group__bt__uuid.md#ga79416b6f0e79ee43bf9b495ec94cca4b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ASCS\_ASE\_CP\_VAL](group__bt__uuid.md#ga6eeb6b573908fe77254894cf3efc5378)) |
|  | Audio Stream Endpoint Control Point Characteristic. |
| #define | [BT\_UUID\_BASS\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gad66cb5c49c932d3546fb549c6febeaa0)   0x2bc7 |
|  | Broadcast Audio Scan Service Scan State value. |
| #define | [BT\_UUID\_BASS\_CONTROL\_POINT](group__bt__uuid.md#ga4d8a9467cf5fce4f6be36d160075984c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BASS\_CONTROL\_POINT\_VAL](group__bt__uuid.md#gad66cb5c49c932d3546fb549c6febeaa0)) |
|  | Broadcast Audio Scan Service Scan State. |
| #define | [BT\_UUID\_BASS\_RECV\_STATE\_VAL](group__bt__uuid.md#ga6c69b13ecbcca8121e6bbe49b58eb799)   0x2bc8 |
|  | Broadcast Audio Scan Service Receive State value. |
| #define | [BT\_UUID\_BASS\_RECV\_STATE](group__bt__uuid.md#ga384b5b68bff445f353762e1e15d85aa4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BASS\_RECV\_STATE\_VAL](group__bt__uuid.md#ga6c69b13ecbcca8121e6bbe49b58eb799)) |
|  | Broadcast Audio Scan Service Receive State. |
| #define | [BT\_UUID\_PACS\_SNK\_VAL](group__bt__uuid.md#gac27fec8eb7a757709f647cbaf5b9735f)   0x2bc9 |
|  | Sink PAC Characteristic value. |
| #define | [BT\_UUID\_PACS\_SNK](group__bt__uuid.md#gaf103bb8e2866a7ab7df90f8b62d4edcd)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_PACS\_SNK\_VAL](group__bt__uuid.md#gac27fec8eb7a757709f647cbaf5b9735f)) |
|  | Sink PAC Characteristic. |
| #define | [BT\_UUID\_PACS\_SNK\_LOC\_VAL](group__bt__uuid.md#ga3df681f24778459df49c4f2e8cae6c4b)   0x2bca |
|  | Sink PAC Locations Characteristic value. |
| #define | [BT\_UUID\_PACS\_SNK\_LOC](group__bt__uuid.md#gab54021bccf67751069b0cf5eaef8c61c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_PACS\_SNK\_LOC\_VAL](group__bt__uuid.md#ga3df681f24778459df49c4f2e8cae6c4b)) |
|  | Sink PAC Locations Characteristic. |
| #define | [BT\_UUID\_PACS\_SRC\_VAL](group__bt__uuid.md#gaa7c87310bea3593a8097fa20ec4c2c88)   0x2bcb |
|  | Source PAC Characteristic value. |
| #define | [BT\_UUID\_PACS\_SRC](group__bt__uuid.md#ga958e64cfd0f6b21095b2de28f3b4a0ee)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_PACS\_SRC\_VAL](group__bt__uuid.md#gaa7c87310bea3593a8097fa20ec4c2c88)) |
|  | Source PAC Characteristic. |
| #define | [BT\_UUID\_PACS\_SRC\_LOC\_VAL](group__bt__uuid.md#ga13eee95752b5b248888ad0328c2c7f99)   0x2bcc |
|  | Source PAC Locations Characteristic value. |
| #define | [BT\_UUID\_PACS\_SRC\_LOC](group__bt__uuid.md#ga0c89cb848378466beba18c389286cac7)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_PACS\_SRC\_LOC\_VAL](group__bt__uuid.md#ga13eee95752b5b248888ad0328c2c7f99)) |
|  | Source PAC Locations Characteristic. |
| #define | [BT\_UUID\_PACS\_AVAILABLE\_CONTEXT\_VAL](group__bt__uuid.md#ga64798749d367c63e3d9ed2d07a236e37)   0x2bcd |
|  | Available Audio Contexts Characteristic value. |
| #define | [BT\_UUID\_PACS\_AVAILABLE\_CONTEXT](group__bt__uuid.md#ga0017f4e6621ba40e51062b8f7c77a634)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_PACS\_AVAILABLE\_CONTEXT\_VAL](group__bt__uuid.md#ga64798749d367c63e3d9ed2d07a236e37)) |
|  | Available Audio Contexts Characteristic. |
| #define | [BT\_UUID\_PACS\_SUPPORTED\_CONTEXT\_VAL](group__bt__uuid.md#ga63588c6624da5cba5b53e07c869c16ff)   0x2bce |
|  | Supported Audio Context Characteristic value. |
| #define | [BT\_UUID\_PACS\_SUPPORTED\_CONTEXT](group__bt__uuid.md#ga4f61367e2c6aeac35f2054759389306b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_PACS\_SUPPORTED\_CONTEXT\_VAL](group__bt__uuid.md#ga63588c6624da5cba5b53e07c869c16ff)) |
|  | Supported Audio Context Characteristic. |
| #define | [BT\_UUID\_GATT\_NH4CONC\_VAL](group__bt__uuid.md#ga68bf0922cd7486337b912f8cce89140d)   0x2bcf |
|  | GATT Characteristic Ammonia Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_NH4CONC](group__bt__uuid.md#ga7204a371be3fb10d382ea00bc76b5102)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_NH4CONC\_VAL](group__bt__uuid.md#ga68bf0922cd7486337b912f8cce89140d)) |
|  | GATT Characteristic Ammonia Concentration. |
| #define | [BT\_UUID\_GATT\_COCONC\_VAL](group__bt__uuid.md#ga397cccc077652fe327b7ceab3ccc1f4d)   0x2bd0 |
|  | GATT Characteristic Carbon Monoxide Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_COCONC](group__bt__uuid.md#gab599f83b69654c1b3be91429d9f7bf32)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_COCONC\_VAL](group__bt__uuid.md#ga397cccc077652fe327b7ceab3ccc1f4d)) |
|  | GATT Characteristic Carbon Monoxide Concentration. |
| #define | [BT\_UUID\_GATT\_CH4CONC\_VAL](group__bt__uuid.md#ga13ecd6003180e0ed73d7aa80542dddd6)   0x2bd1 |
|  | GATT Characteristic Methane Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_CH4CONC](group__bt__uuid.md#gad0496cbb8cf296852fe85b7694c1e3a8)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_CH4CONC\_VAL](group__bt__uuid.md#ga13ecd6003180e0ed73d7aa80542dddd6)) |
|  | GATT Characteristic Methane Concentration. |
| #define | [BT\_UUID\_GATT\_NO2CONC\_VAL](group__bt__uuid.md#ga37fdb9197c3003175875337df66c0937)   0x2bd2 |
|  | GATT Characteristic Nitrogen Dioxide Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_NO2CONC](group__bt__uuid.md#ga1a0f1553bbf70517af224fd32a5842f6)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_NO2CONC\_VAL](group__bt__uuid.md#ga37fdb9197c3003175875337df66c0937)) |
|  | GATT Characteristic Nitrogen Dioxide Concentration. |
| #define | [BT\_UUID\_GATT\_NONCH4CONC\_VAL](group__bt__uuid.md#ga2023c3c8c4fdf714a66dc64984a9f198)   0x2bd3 |
|  | GATT Characteristic Non-Methane Volatile Organic Compounds Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_NONCH4CONC](group__bt__uuid.md#ga6770e5f7e2f46c604ada573dd8b950e9)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_NONCH4CONC\_VAL](group__bt__uuid.md#ga2023c3c8c4fdf714a66dc64984a9f198)) |
|  | GATT Characteristic Non-Methane Volatile Organic Compounds Concentration. |
| #define | [BT\_UUID\_GATT\_O3CONC\_VAL](group__bt__uuid.md#ga4a022ea0079ebc09dedf5f472a8755ee)   0x2bd4 |
|  | GATT Characteristic Ozone Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_O3CONC](group__bt__uuid.md#ga23054b696f62c03afb73a0f5286dc2d5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_O3CONC\_VAL](group__bt__uuid.md#ga4a022ea0079ebc09dedf5f472a8755ee)) |
|  | GATT Characteristic Ozone Concentration. |
| #define | [BT\_UUID\_GATT\_PM1CONC\_VAL](group__bt__uuid.md#ga8dde1677ff60c1970c427e9b984e24d9)   0x2bd5 |
|  | GATT Characteristic Particulate Matter - PM1 Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_PM1CONC](group__bt__uuid.md#ga9c39a445bab4603148d4256bcce23a5b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PM1CONC\_VAL](group__bt__uuid.md#ga8dde1677ff60c1970c427e9b984e24d9)) |
|  | GATT Characteristic Particulate Matter - PM1 Concentration. |
| #define | [BT\_UUID\_GATT\_PM25CONC\_VAL](group__bt__uuid.md#ga055b7900ffda40c9ec4e1870abc1d855)   0x2bd6 |
|  | GATT Characteristic Particulate Matter - PM2.5 Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_PM25CONC](group__bt__uuid.md#ga88d2f1f4afcb89267c713144f84f4f7f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PM25CONC\_VAL](group__bt__uuid.md#ga055b7900ffda40c9ec4e1870abc1d855)) |
|  | GATT Characteristic Particulate Matter - PM2.5 Concentration. |
| #define | [BT\_UUID\_GATT\_PM10CONC\_VAL](group__bt__uuid.md#gaebebc238d90e667f33d2c95690d67376)   0x2bd7 |
|  | GATT Characteristic Particulate Matter - PM10 Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_PM10CONC](group__bt__uuid.md#ga9668baee783462813c530f411da07890)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_PM10CONC\_VAL](group__bt__uuid.md#gaebebc238d90e667f33d2c95690d67376)) |
|  | GATT Characteristic Particulate Matter - PM10 Concentration. |
| #define | [BT\_UUID\_GATT\_SO2CONC\_VAL](group__bt__uuid.md#gaf7ee2d08cd80e1d4afc777457217508d)   0x2bd8 |
|  | GATT Characteristic Sulfur Dioxide Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_SO2CONC](group__bt__uuid.md#ga3c7b7be6268bb748f7406737eaa129e2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SO2CONC\_VAL](group__bt__uuid.md#gaf7ee2d08cd80e1d4afc777457217508d)) |
|  | GATT Characteristic Sulfur Dioxide Concentration. |
| #define | [BT\_UUID\_GATT\_SF6CONC\_VAL](group__bt__uuid.md#gaba0853f84e9e33dd4d7d71ecebc31bb6)   0x2bd9 |
|  | GATT Characteristic Sulfur Hexafluoride Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_SF6CONC](group__bt__uuid.md#gaf17d7037cdaed65e208df3792f1fd2d3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SF6CONC\_VAL](group__bt__uuid.md#gaba0853f84e9e33dd4d7d71ecebc31bb6)) |
|  | GATT Characteristic Sulfur Hexafluoride Concentration. |
| #define | [BT\_UUID\_HAS\_HEARING\_AID\_FEATURES\_VAL](group__bt__uuid.md#gad4967e4904cd371940af8b135da21f47)   0x2bda |
|  | Hearing Aid Features Characteristic value. |
| #define | [BT\_UUID\_HAS\_HEARING\_AID\_FEATURES](group__bt__uuid.md#gaebd2bbb103e6928059f1a76eac55916b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HAS\_HEARING\_AID\_FEATURES\_VAL](group__bt__uuid.md#gad4967e4904cd371940af8b135da21f47)) |
|  | Hearing Aid Features Characteristic. |
| #define | [BT\_UUID\_HAS\_PRESET\_CONTROL\_POINT\_VAL](group__bt__uuid.md#ga6fdc731a19072629917ce6ebf28c7fee)   0x2bdb |
|  | Hearing Aid Preset Control Point Characteristic value. |
| #define | [BT\_UUID\_HAS\_PRESET\_CONTROL\_POINT](group__bt__uuid.md#ga7f3a8eea9e7ee68d8865809a061a0e96)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HAS\_PRESET\_CONTROL\_POINT\_VAL](group__bt__uuid.md#ga6fdc731a19072629917ce6ebf28c7fee)) |
|  | Hearing Aid Preset Control Point Characteristic. |
| #define | [BT\_UUID\_HAS\_ACTIVE\_PRESET\_INDEX\_VAL](group__bt__uuid.md#gae9b2bf949e992c7cd6f1aaaa49888189)   0x2bdc |
|  | Active Preset Index Characteristic value. |
| #define | [BT\_UUID\_HAS\_ACTIVE\_PRESET\_INDEX](group__bt__uuid.md#ga9ef9b65a7c9a105798691a2cdffbaf7a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HAS\_ACTIVE\_PRESET\_INDEX\_VAL](group__bt__uuid.md#gae9b2bf949e992c7cd6f1aaaa49888189)) |
|  | Active Preset Index Characteristic. |
| #define | [BT\_UUID\_GATT\_FSTR64\_VAL](group__bt__uuid.md#gac18b9e325ef1db22774f8da35b888223)   0x2bde |
|  | GATT Characteristic Fixed String 64 UUID Value. |
| #define | [BT\_UUID\_GATT\_FSTR64](group__bt__uuid.md#gac617c317945f2b6d45de15eca1190823)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_FSTR64\_VAL](group__bt__uuid.md#gac18b9e325ef1db22774f8da35b888223)) |
|  | GATT Characteristic Fixed String 64. |
| #define | [BT\_UUID\_GATT\_HITEMP\_VAL](group__bt__uuid.md#ga2a3928912a6eed082deac4893fb4f980)   0x2bdf |
|  | GATT Characteristic High Temperature UUID Value. |
| #define | [BT\_UUID\_GATT\_HITEMP](group__bt__uuid.md#ga8d9bad6c04ea4cf096d0d010208e1d2a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_HITEMP\_VAL](group__bt__uuid.md#ga2a3928912a6eed082deac4893fb4f980)) |
|  | GATT Characteristic High Temperature. |
| #define | [BT\_UUID\_GATT\_HV\_VAL](group__bt__uuid.md#ga2b707ca8b876eded6b3adf9bb7132479)   0x2be0 |
|  | GATT Characteristic High Voltage UUID Value. |
| #define | [BT\_UUID\_GATT\_HV](group__bt__uuid.md#ga1104d7e9d1571aacdb77693c64a15edc)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_HV\_VAL](group__bt__uuid.md#ga2b707ca8b876eded6b3adf9bb7132479)) |
|  | GATT Characteristic High Voltage. |
| #define | [BT\_UUID\_GATT\_LD\_VAL](group__bt__uuid.md#ga67e534b02154fd7ff94b5ed21616f5f2)   0x2be1 |
|  | GATT Characteristic Light Distribution UUID Value. |
| #define | [BT\_UUID\_GATT\_LD](group__bt__uuid.md#ga5f68a688a1347d84bd28aa3df7252be9)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LD\_VAL](group__bt__uuid.md#ga67e534b02154fd7ff94b5ed21616f5f2)) |
|  | GATT Characteristic Light Distribution. |
| #define | [BT\_UUID\_GATT\_LO\_VAL](group__bt__uuid.md#gaa127fa12de6d6a641183641853439708)   0x2be2 |
|  | GATT Characteristic Light Output UUID Value. |
| #define | [BT\_UUID\_GATT\_LO](group__bt__uuid.md#gacc7b122d7a849291a5c9c877acfbd50a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LO\_VAL](group__bt__uuid.md#gaa127fa12de6d6a641183641853439708)) |
|  | GATT Characteristic Light Output. |
| #define | [BT\_UUID\_GATT\_LST\_VAL](group__bt__uuid.md#ga34f9f97b35397e713f655b888845d443)   0x2be3 |
|  | GATT Characteristic Light Source Type UUID Value. |
| #define | [BT\_UUID\_GATT\_LST](group__bt__uuid.md#ga2794fa8a9e1030826b4d382cc59f835a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_LST\_VAL](group__bt__uuid.md#ga34f9f97b35397e713f655b888845d443)) |
|  | GATT Characteristic Light Source Type. |
| #define | [BT\_UUID\_GATT\_NOISE\_VAL](group__bt__uuid.md#gab3b7b78bfb8b5dfd30a1751ce9ffaee7)   0x2be4 |
|  | GATT Characteristic Noise UUID Value. |
| #define | [BT\_UUID\_GATT\_NOISE](group__bt__uuid.md#gaeb4d264b70d6d6c87a34f0da320f8e7a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_NOISE\_VAL](group__bt__uuid.md#gab3b7b78bfb8b5dfd30a1751ce9ffaee7)) |
|  | GATT Characteristic Noise. |
| #define | [BT\_UUID\_GATT\_RRCCTP\_VAL](group__bt__uuid.md#ga8cbc0843565303e78f564517c21feb0f)   0x2be5 |
|  | GATT Characteristic Relative Runtime in a Correlated Color Temperature Range UUID Value. |
| #define | [BT\_UUID\_GATT\_RRCCTR](group__bt__uuid.md#ga0f5bffe28d45d35fa2dc6680bc52476d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)(BT\_UUID\_GATT\_RRCCTR\_VAL) |
|  | GATT Characteristic Relative Runtime in a Correlated Color Temperature Range. |
| #define | [BT\_UUID\_GATT\_TIM\_S32\_VAL](group__bt__uuid.md#ga9fd1550589d248be145b120c446181ee)   0x2be6 |
|  | GATT Characteristic Time Second 32 UUID Value. |
| #define | [BT\_UUID\_GATT\_TIM\_S32](group__bt__uuid.md#gac76fc378354bcd1a8c706f7438a90ebb)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_TIM\_S32\_VAL](group__bt__uuid.md#ga9fd1550589d248be145b120c446181ee)) |
|  | GATT Characteristic Time Second 32. |
| #define | [BT\_UUID\_GATT\_VOCCONC\_VAL](group__bt__uuid.md#gabf10e337b78be1ab371fbef771109c53)   0x2be7 |
|  | GATT Characteristic VOC Concentration UUID Value. |
| #define | [BT\_UUID\_GATT\_VOCCONC](group__bt__uuid.md#ga7181f9f1dfaae6cfe3fd8cedd8c20917)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_VOCCONC\_VAL](group__bt__uuid.md#gabf10e337b78be1ab371fbef771109c53)) |
|  | GATT Characteristic VOC Concentration. |
| #define | [BT\_UUID\_GATT\_VF\_VAL](group__bt__uuid.md#ga4c57416ae5e84133339e3fab0ba31918)   0x2be8 |
|  | GATT Characteristic Voltage Frequency UUID Value. |
| #define | [BT\_UUID\_GATT\_VF](group__bt__uuid.md#gae8500640959d58da51aee03fa75c85ba)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_VF\_VAL](group__bt__uuid.md#ga4c57416ae5e84133339e3fab0ba31918)) |
|  | GATT Characteristic Voltage Frequency. |
| #define | [BT\_UUID\_BAS\_BATTERY\_CRIT\_STATUS\_VAL](group__bt__uuid.md#gaad27c84d46c85c4fc436e2d57249e562)   0x2be9 |
|  | BAS Characteristic Battery Critical Status UUID Value. |
| #define | [BT\_UUID\_BAS\_BATTERY\_CRIT\_STATUS](group__bt__uuid.md#ga678d5e47dee2070ce9208538c529460b)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAS\_BATTERY\_CRIT\_STATUS\_VAL](group__bt__uuid.md#gaad27c84d46c85c4fc436e2d57249e562)) |
|  | BAS Characteristic Battery Critical Status. |
| #define | [BT\_UUID\_BAS\_BATTERY\_HEALTH\_STATUS\_VAL](group__bt__uuid.md#ga0dd78641b14fa1affa283f3f53a5f194)   0x2bea |
|  | BAS Characteristic Battery Health Status UUID Value. |
| #define | [BT\_UUID\_BAS\_BATTERY\_HEALTH\_STATUS](group__bt__uuid.md#gaa442c41b04c72f1a7a983e0c6561b90d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAS\_BATTERY\_HEALTH\_STATUS\_VAL](group__bt__uuid.md#ga0dd78641b14fa1affa283f3f53a5f194)) |
|  | BAS Characteristic Battery Health Status. |
| #define | [BT\_UUID\_BAS\_BATTERY\_HEALTH\_INF\_VAL](group__bt__uuid.md#ga3324d4b7047cab8fb2c033c4c92c5793)   0x2beb |
|  | BAS Characteristic Battery Health Information UUID Value. |
| #define | [BT\_UUID\_BAS\_BATTERY\_HEALTH\_INF](group__bt__uuid.md#ga62ad5685a1fcbb18afd57c7ded6463a0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAS\_BATTERY\_HEALTH\_INF\_VAL](group__bt__uuid.md#ga3324d4b7047cab8fb2c033c4c92c5793)) |
|  | BAS Characteristic Battery Health Information. |
| #define | [BT\_UUID\_BAS\_BATTERY\_INF\_VAL](group__bt__uuid.md#ga04f0ff51790e2c759b401f36a989f6b7)   0x2bec |
|  | BAS Characteristic Battery Information UUID Value. |
| #define | [BT\_UUID\_BAS\_BATTERY\_INF](group__bt__uuid.md#gad6dffe9e9e9684b2a943471e0a6c0918)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAS\_BATTERY\_INF\_VAL](group__bt__uuid.md#ga04f0ff51790e2c759b401f36a989f6b7)) |
|  | BAS Characteristic Battery Information. |
| #define | [BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATUS\_VAL](group__bt__uuid.md#gaf14fdc69148ba65b5fb7fe9d42706787)   0x2bed |
|  | BAS Characteristic Battery Level Status UUID Value. |
| #define | [BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATUS](group__bt__uuid.md#ga54a26381c17065abbda1eb4c2a35c244)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAS\_BATTERY\_LEVEL\_STATUS\_VAL](group__bt__uuid.md#gaf14fdc69148ba65b5fb7fe9d42706787)) |
|  | BAS Characteristic Battery Level Status. |
| #define | [BT\_UUID\_BAS\_BATTERY\_TIME\_STATUS\_VAL](group__bt__uuid.md#ga8a1d978914a8cb9c3744b4b333e38f46)   0x2bee |
|  | BAS Characteristic Battery Time Status UUID Value. |
| #define | [BT\_UUID\_BAS\_BATTERY\_TIME\_STATUS](group__bt__uuid.md#ga25e2b1b84d5b9dd46ae79ab26752a02f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAS\_BATTERY\_TIME\_STATUS\_VAL](group__bt__uuid.md#ga8a1d978914a8cb9c3744b4b333e38f46)) |
|  | BAS Characteristic Battery Time Status. |
| #define | [BT\_UUID\_GATT\_ESD\_VAL](group__bt__uuid.md#gaff547b9ef568ae7ae70fdb18cbced21b)   0x2bef |
|  | GATT Characteristic Estimated Service Date UUID Value. |
| #define | [BT\_UUID\_GATT\_ESD](group__bt__uuid.md#ga432ba40acfbe03c50b4a3ede80b972c1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_ESD\_VAL](group__bt__uuid.md#gaff547b9ef568ae7ae70fdb18cbced21b)) |
|  | GATT Characteristic Estimated Service Date. |
| #define | [BT\_UUID\_BAS\_BATTERY\_ENERGY\_STATUS\_VAL](group__bt__uuid.md#ga7af8620512a789611a3c6c96bcbd6c06)   0x2bf0 |
|  | BAS Characteristic Battery Energy Status UUID Value. |
| #define | [BT\_UUID\_BAS\_BATTERY\_ENERGY\_STATUS](group__bt__uuid.md#gadc442a139fff871f63d5e11be37c8231)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BAS\_BATTERY\_ENERGY\_STATUS\_VAL](group__bt__uuid.md#ga7af8620512a789611a3c6c96bcbd6c06)) |
|  | BAS Characteristic Battery Energy Status. |
| #define | [BT\_UUID\_GATT\_SL\_VAL](group__bt__uuid.md#ga87e7a8d4ea7c2f0b4345c3ddd83e2bcc)   0x2bf5 |
|  | GATT Characteristic LE GATT Security Levels UUID Value. |
| #define | [BT\_UUID\_GATT\_SL](group__bt__uuid.md#ga07c07b64d8d06b76b64c71109dd39bc4)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GATT\_SL\_VAL](group__bt__uuid.md#ga87e7a8d4ea7c2f0b4345c3ddd83e2bcc)) |
|  | GATT Characteristic LE GATT Security Levels. |
| #define | [BT\_UUID\_UDI\_FOR\_MEDICAL\_DEVICES\_VAL](group__bt__uuid.md#ga1904b4b736c5949b544cfd3cf270b9a1)   0x2bff |
|  | GATT Characteristic UDI for Medical Devices UUID Value. |
| #define | [BT\_UUID\_UDI\_FOR\_MEDICAL\_DEVICES](group__bt__uuid.md#ga1d0210d3557a3838a4b04bedf413e80c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_UDI\_FOR\_MEDICAL\_DEVICES\_VAL](group__bt__uuid.md#ga1904b4b736c5949b544cfd3cf270b9a1)) |
|  | GATT Characteristic UDI for Medical Devices. |
| #define | [BT\_UUID\_GMAS\_VAL](group__bt__uuid.md#ga791ebaadcc3fac61cda4001d1dadc044)   0x1858 |
|  | Gaming Service UUID value. |
| #define | [BT\_UUID\_GMAS](group__bt__uuid.md#gae48cde28242dd2813cb9259a3db4cd0f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GMAS\_VAL](group__bt__uuid.md#ga791ebaadcc3fac61cda4001d1dadc044)) |
|  | Common Audio Service. |
| #define | [BT\_UUID\_GMAP\_ROLE\_VAL](group__bt__uuid.md#ga8a9ca3e7c352dcc5c6b4834f1c1b188c)   0x2C00 |
|  | Gaming Audio Profile Role UUID value. |
| #define | [BT\_UUID\_GMAP\_ROLE](group__bt__uuid.md#gacb7897b761dc608e7814a2ad103e47a2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GMAP\_ROLE\_VAL](group__bt__uuid.md#ga8a9ca3e7c352dcc5c6b4834f1c1b188c)) |
|  | Gaming Audio Profile Role. |
| #define | [BT\_UUID\_GMAP\_UGG\_FEAT\_VAL](group__bt__uuid.md#ga9a79627722acfc4c93b2d251aefd8b83)   0x2C01 |
|  | Gaming Audio Profile Unicast Game Gateway Features UUID value. |
| #define | [BT\_UUID\_GMAP\_UGG\_FEAT](group__bt__uuid.md#gafcdc548a86c976b07fa57bd0ccaee9c9)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GMAP\_UGG\_FEAT\_VAL](group__bt__uuid.md#ga9a79627722acfc4c93b2d251aefd8b83)) |
|  | Gaming Audio Profile Unicast Game Gateway Features. |
| #define | [BT\_UUID\_GMAP\_UGT\_FEAT\_VAL](group__bt__uuid.md#ga24f317039700e33d09f6244d74e4c024)   0x2C02 |
|  | Gaming Audio Profile Unicast Game Terminal Features UUID value. |
| #define | [BT\_UUID\_GMAP\_UGT\_FEAT](group__bt__uuid.md#gaf3b064865efb4e566ea3d00b1de932e1)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GMAP\_UGT\_FEAT\_VAL](group__bt__uuid.md#ga24f317039700e33d09f6244d74e4c024)) |
|  | Gaming Audio Profile Unicast Game Terminal Features. |
| #define | [BT\_UUID\_GMAP\_BGS\_FEAT\_VAL](group__bt__uuid.md#ga5aa7be5ea8b74329c07f7de879e9ab2f)   0x2C03 |
|  | Gaming Audio Profile Broadcast Game Sender Features UUID value. |
| #define | [BT\_UUID\_GMAP\_BGS\_FEAT](group__bt__uuid.md#ga0aa83932e08ed22c1d75464b77e23b0c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GMAP\_BGS\_FEAT\_VAL](group__bt__uuid.md#ga5aa7be5ea8b74329c07f7de879e9ab2f)) |
|  | Gaming Audio Profile Broadcast Game Sender Features. |
| #define | [BT\_UUID\_GMAP\_BGR\_FEAT\_VAL](group__bt__uuid.md#ga5b7fcf7e18179190c3cd3ec2289ebcd5)   0x2C04 |
|  | Gaming Audio Profile Broadcast Game Receiver Features UUID value. |
| #define | [BT\_UUID\_GMAP\_BGR\_FEAT](group__bt__uuid.md#ga0d13271568a11aceb9a6d169cdb6474c)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_GMAP\_BGR\_FEAT\_VAL](group__bt__uuid.md#ga5b7fcf7e18179190c3cd3ec2289ebcd5)) |
|  | Gaming Audio Profile Broadcast Game Receiver Features. |
| #define | [BT\_UUID\_SDP\_VAL](group__bt__uuid.md#gaa82cf709aaa5986ada534ac4c24aa407)   0x0001 |
| #define | [BT\_UUID\_SDP](group__bt__uuid.md#ga82f35da766ed6acfe18de8d119d19859)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_SDP\_VAL](group__bt__uuid.md#gaa82cf709aaa5986ada534ac4c24aa407)) |
| #define | [BT\_UUID\_UDP\_VAL](group__bt__uuid.md#gab0d4e8012eef2d067b63e8e538d6317c)   0x0002 |
| #define | [BT\_UUID\_UDP](group__bt__uuid.md#ga51e5cf4018099907c64eabf219a193c8)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_UDP\_VAL](group__bt__uuid.md#gab0d4e8012eef2d067b63e8e538d6317c)) |
| #define | [BT\_UUID\_RFCOMM\_VAL](group__bt__uuid.md#ga71dd44d6977cc000c00a6176f71053c9)   0x0003 |
| #define | [BT\_UUID\_RFCOMM](group__bt__uuid.md#gafce3f7dd2fbd02c3a549f46395253cde)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_RFCOMM\_VAL](group__bt__uuid.md#ga71dd44d6977cc000c00a6176f71053c9)) |
| #define | [BT\_UUID\_TCP\_VAL](group__bt__uuid.md#gab4dac3d360e3428cc0b66e34bea75285)   0x0004 |
| #define | [BT\_UUID\_TCP](group__bt__uuid.md#ga419519758947e29b8ded5209b1c47743)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TCP\_VAL](group__bt__uuid.md#gab4dac3d360e3428cc0b66e34bea75285)) |
| #define | [BT\_UUID\_TCS\_BIN\_VAL](group__bt__uuid.md#gab7f9b345cb85f922840e6e21722c3373)   0x0005 |
| #define | [BT\_UUID\_TCS\_BIN](group__bt__uuid.md#ga5c9bd29f560d84a30c0cb009ccfdc36a)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TCS\_BIN\_VAL](group__bt__uuid.md#gab7f9b345cb85f922840e6e21722c3373)) |
| #define | [BT\_UUID\_TCS\_AT\_VAL](group__bt__uuid.md#ga09236e2cc7267043f47445e7b233bc38)   0x0006 |
| #define | [BT\_UUID\_TCS\_AT](group__bt__uuid.md#ga7c31eb642d9cb8231de38f25c43ef23f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_TCS\_AT\_VAL](group__bt__uuid.md#ga09236e2cc7267043f47445e7b233bc38)) |
| #define | [BT\_UUID\_ATT\_VAL](group__bt__uuid.md#ga675b73753e13c6c6dbbc5f655b23e466)   0x0007 |
| #define | [BT\_UUID\_ATT](group__bt__uuid.md#gaa91cf6c6639156a4b5c67041d479d555)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_ATT\_VAL](group__bt__uuid.md#ga675b73753e13c6c6dbbc5f655b23e466)) |
| #define | [BT\_UUID\_OBEX\_VAL](group__bt__uuid.md#gab63382153f97c79f7cdcdfa0a264d6e7)   0x0008 |
| #define | [BT\_UUID\_OBEX](group__bt__uuid.md#ga8f660c1d39057815d0420d2dce00639e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_OBEX\_VAL](group__bt__uuid.md#gab63382153f97c79f7cdcdfa0a264d6e7)) |
| #define | [BT\_UUID\_IP\_VAL](group__bt__uuid.md#ga5bd66bfdd6ee1f68dd2447aed448d860)   0x0009 |
| #define | [BT\_UUID\_IP](group__bt__uuid.md#gad0469b885ffe7be0ff1bef7feb2395d5)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_IP\_VAL](group__bt__uuid.md#ga5bd66bfdd6ee1f68dd2447aed448d860)) |
| #define | [BT\_UUID\_FTP\_VAL](group__bt__uuid.md#gad8ecc3b05eb61d0a3da8daa38deb3887)   0x000a |
| #define | [BT\_UUID\_FTP](group__bt__uuid.md#gada757111154b60d3dbb375192ec48a0f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_FTP\_VAL](group__bt__uuid.md#gad8ecc3b05eb61d0a3da8daa38deb3887)) |
| #define | [BT\_UUID\_HTTP\_VAL](group__bt__uuid.md#gafd11ab75ca80c343f894db89779419d4)   0x000c |
| #define | [BT\_UUID\_HTTP](group__bt__uuid.md#ga34afe0fe521f95f82f0c86e0de8c1d93)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HTTP\_VAL](group__bt__uuid.md#gafd11ab75ca80c343f894db89779419d4)) |
| #define | [BT\_UUID\_WSP\_VAL](group__bt__uuid.md#gac095fdb1bc8d0a07737061b428e12071)   0x000e |
| #define | [BT\_UUID\_WSP](group__bt__uuid.md#ga8f0f3c9e5ef2b6a313ed742a8f7ed0bd)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_WSP\_VAL](group__bt__uuid.md#gac095fdb1bc8d0a07737061b428e12071)) |
| #define | [BT\_UUID\_BNEP\_VAL](group__bt__uuid.md#gacf6c5a3e20d50500cca56daf5802faf5)   0x000f |
| #define | [BT\_UUID\_BNEP](group__bt__uuid.md#ga9bd1756830328cacd40fc8bf80ee176d)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_BNEP\_VAL](group__bt__uuid.md#gacf6c5a3e20d50500cca56daf5802faf5)) |
| #define | [BT\_UUID\_UPNP\_VAL](group__bt__uuid.md#ga0dac826a9f670d1eba071603723fd3f5)   0x0010 |
| #define | [BT\_UUID\_UPNP](group__bt__uuid.md#ga3f7ade885937ba780b0074516c180c42)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_UPNP\_VAL](group__bt__uuid.md#ga0dac826a9f670d1eba071603723fd3f5)) |
| #define | [BT\_UUID\_HIDP\_VAL](group__bt__uuid.md#gac30ff318ffebd4a6793a0267de6b84e9)   0x0011 |
| #define | [BT\_UUID\_HIDP](group__bt__uuid.md#ga9cbd452d2c4fa9fae46cd39bb8133ea2)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HIDP\_VAL](group__bt__uuid.md#gac30ff318ffebd4a6793a0267de6b84e9)) |
| #define | [BT\_UUID\_HCRP\_CTRL\_VAL](group__bt__uuid.md#gaccdbcd9b4ab68185c4ba213d2b83fcf2)   0x0012 |
| #define | [BT\_UUID\_HCRP\_CTRL](group__bt__uuid.md#ga731221f8f6711a400aa0e7c39c8520ea)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HCRP\_CTRL\_VAL](group__bt__uuid.md#gaccdbcd9b4ab68185c4ba213d2b83fcf2)) |
| #define | [BT\_UUID\_HCRP\_DATA\_VAL](group__bt__uuid.md#ga61619a474d5278d79bf66fcda77076f6)   0x0014 |
| #define | [BT\_UUID\_HCRP\_DATA](group__bt__uuid.md#ga0bd9a371c57ecc22cfb40b31025cc69e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HCRP\_DATA\_VAL](group__bt__uuid.md#ga61619a474d5278d79bf66fcda77076f6)) |
| #define | [BT\_UUID\_HCRP\_NOTE\_VAL](group__bt__uuid.md#ga99a3d8dfd8f46ece85f3fa5be8c94a64)   0x0016 |
| #define | [BT\_UUID\_HCRP\_NOTE](group__bt__uuid.md#ga85372fbf20b7d83fdf5e780487f14974)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_HCRP\_NOTE\_VAL](group__bt__uuid.md#ga99a3d8dfd8f46ece85f3fa5be8c94a64)) |
| #define | [BT\_UUID\_AVCTP\_VAL](group__bt__uuid.md#ga07ce8ad97e49eb94eb08a75b8fa555ca)   0x0017 |
| #define | [BT\_UUID\_AVCTP](group__bt__uuid.md#ga1b172e9a094474f5d7fe6b1b46dbc93e)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_AVCTP\_VAL](group__bt__uuid.md#ga07ce8ad97e49eb94eb08a75b8fa555ca)) |
| #define | [BT\_UUID\_AVDTP\_VAL](group__bt__uuid.md#ga2e2934e79054324cec077903c07108ad)   0x0019 |
| #define | [BT\_UUID\_AVDTP](group__bt__uuid.md#ga926c1d29d7655320c3b89558ec5b3d2f)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_AVDTP\_VAL](group__bt__uuid.md#ga2e2934e79054324cec077903c07108ad)) |
| #define | [BT\_UUID\_CMTP\_VAL](group__bt__uuid.md#gae83a731e34ef81a8340f9c5919ad0c6f)   0x001b |
| #define | [BT\_UUID\_CMTP](group__bt__uuid.md#gaa70481ddcb90e8232b3397580c5927a0)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_CMTP\_VAL](group__bt__uuid.md#gae83a731e34ef81a8340f9c5919ad0c6f)) |
| #define | [BT\_UUID\_UDI\_VAL](group__bt__uuid.md#ga477f7e4e7baffa502a0d8ded852ec2e7)   0x001d |
| #define | [BT\_UUID\_UDI](group__bt__uuid.md#gaae2132eeff69adb594365a0af0419695)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_UDI\_VAL](group__bt__uuid.md#ga477f7e4e7baffa502a0d8ded852ec2e7)) |
| #define | [BT\_UUID\_MCAP\_CTRL\_VAL](group__bt__uuid.md#ga9a893aa35fe599d26b6dcfd9bd0fcb2e)   0x001e |
| #define | [BT\_UUID\_MCAP\_CTRL](group__bt__uuid.md#ga1f576ec8576152a951d44a87b8406514)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCAP\_CTRL\_VAL](group__bt__uuid.md#ga9a893aa35fe599d26b6dcfd9bd0fcb2e)) |
| #define | [BT\_UUID\_MCAP\_DATA\_VAL](group__bt__uuid.md#gabc9726eea06d6f3cea2de134f62fb4f1)   0x001f |
| #define | [BT\_UUID\_MCAP\_DATA](group__bt__uuid.md#gab5607157844471d48d2d1db3e295cee3)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_MCAP\_DATA\_VAL](group__bt__uuid.md#gabc9726eea06d6f3cea2de134f62fb4f1)) |
| #define | [BT\_UUID\_L2CAP\_VAL](group__bt__uuid.md#ga64e0b2fde8593ae40dfc0d661240abb4)   0x0100 |
| #define | [BT\_UUID\_L2CAP](group__bt__uuid.md#ga17007ef5a1e355f912af78f909a1d971)   [BT\_UUID\_DECLARE\_16](group__bt__uuid.md#ga66ea8148e444e163a936ebd79a63eb55)([BT\_UUID\_L2CAP\_VAL](group__bt__uuid.md#ga64e0b2fde8593ae40dfc0d661240abb4)) |

| Enumerations | |
| --- | --- |
| enum | { [BT\_UUID\_TYPE\_16](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a8a5a0c5b6310aff10b182daec0e452ba) , [BT\_UUID\_TYPE\_32](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a27382df27b8098bf6144021c1b23c4c8) , [BT\_UUID\_TYPE\_128](group__bt__uuid.md#ggabec48a57ba2d88c9e6006d9996a0fb43a786cbb74a1d74c77cb31ff3c4da45517) } |
|  | Bluetooth UUID types. [More...](group__bt__uuid.md#gabec48a57ba2d88c9e6006d9996a0fb43) |

| Functions | |
| --- | --- |
| int | [bt\_uuid\_cmp](group__bt__uuid.md#gafe17513c1f91cb3f3e61648b71620c6b) (const struct [bt\_uuid](structbt__uuid.md) \*u1, const struct [bt\_uuid](structbt__uuid.md) \*u2) |
|  | Compare Bluetooth UUIDs. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_uuid\_create](group__bt__uuid.md#ga9e260584efcc111eb3ee02bf78f01881) (struct [bt\_uuid](structbt__uuid.md) \*uuid, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data\_len) |
|  | Create a [bt\_uuid](structbt__uuid.md "This is a 'tentative' type and should be used as a pointer only.") from a little-endian data buffer. |
| void | [bt\_uuid\_to\_str](group__bt__uuid.md#gab5ef78dd2263f08de16a0f1e764df657) (const struct [bt\_uuid](structbt__uuid.md) \*uuid, char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Convert Bluetooth UUID to string. |

## Detailed Description

Bluetooth UUID handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [uuid.h](uuid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
