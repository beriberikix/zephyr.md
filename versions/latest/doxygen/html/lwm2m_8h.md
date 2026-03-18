---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/lwm2m_8h.html
original_path: doxygen/html/lwm2m_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lwm2m.h File Reference

`#include <time.h>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/sys/mutex.h](mutex_8h_source.md)>`  
`#include <[zephyr/net/coap.h](coap_8h_source.md)>`  
`#include <[zephyr/net/lwm2m_path.h](lwm2m__path_8h_source.md)>`

[Go to the source code of this file.](lwm2m_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [lwm2m\_obj\_path](structlwm2m__obj__path.md) |
|  | LwM2M object path structure. [More...](structlwm2m__obj__path.md#details) |
| struct | [lwm2m\_ctx](structlwm2m__ctx.md) |
|  | LwM2M context structure to maintain information for a single LwM2M connection. [More...](structlwm2m__ctx.md#details) |
| struct | [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md) |
|  | LwM2M Time series data structure. [More...](structlwm2m__time__series__elem.md#details) |
| struct | [lwm2m\_objlnk](structlwm2m__objlnk.md) |
|  | LWM2M Objlnk resource type structure. [More...](structlwm2m__objlnk.md#details) |

| Macros | |
| --- | --- |
| #define | [LWM2M\_OBJLNK\_MAX\_ID](group__lwm2m__api.md#ga34febb0c6fb1c68b0963a6e4dd721763)   USHRT\_MAX |
|  | Maximum value for Objlnk resource fields. |
| #define | [LWM2M\_RES\_DATA\_READ\_ONLY](group__lwm2m__api.md#ga12c2e0af3d3fc6dd5785e08c0d831a67)   0 |
|  | Resource read-only value bit. |
| #define | [LWM2M\_RES\_DATA\_FLAG\_RO](group__lwm2m__api.md#ga1bfa5b7d83e3560828a1fb61a4d07355)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([LWM2M\_RES\_DATA\_READ\_ONLY](group__lwm2m__api.md#ga12c2e0af3d3fc6dd5785e08c0d831a67)) |
|  | Resource read-only flag. |
| #define | [LWM2M\_HAS\_RES\_FLAG](group__lwm2m__api.md#ga49f4117dfec8cd1abe9f827e235f55b0)(res, f) |
|  | Read resource flags helper macro. |
| #define | [LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_FAILURE](group__lwm2m__api.md#ga19c025d7df4dec8069ed59ffc788b00c)   [LWM2M\_RD\_CLIENT\_EVENT\_REG\_TIMEOUT](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404) \_\_DEPRECATED\_MACRO |
|  | Define for old event name keeping backward compatibility. |
| #define | [LWM2M\_RD\_CLIENT\_FLAG\_BOOTSTRAP](group__lwm2m__api.md#ga3a3669237762fa8c23686e5e00b7809f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Run bootstrap procedure in current session. |
| #define | [LWM2M\_MAX\_PATH\_STR\_SIZE](group__lwm2m__api.md#gab97329844cd411195add5d72ad6aa4b7)   [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("/65535/65535/65535/65535") |
|  | LwM2M path maximum length. |
| LwM2M Objects managed by OMA for LwM2M tech specification. | |
| Objects in this range have IDs from 0 to 1023. | |
| #define | [LWM2M\_OBJECT\_SECURITY\_ID](group__lwm2m__api.md#ga785e4a647a2cf93194a249537223ab0f)   0 |
|  | Security object. |
| #define | [LWM2M\_OBJECT\_SERVER\_ID](group__lwm2m__api.md#gace7b2f0a1f97b6e99c0958a8382ca0d2)   1 |
|  | Server object. |
| #define | [LWM2M\_OBJECT\_ACCESS\_CONTROL\_ID](group__lwm2m__api.md#gaa8387c8838f952c7c60602e2952c7f55)   2 |
|  | Access Control object. |
| #define | [LWM2M\_OBJECT\_DEVICE\_ID](group__lwm2m__api.md#ga699f585b320ab5b259d4fb2bda10eb78)   3 |
|  | Device object. |
| #define | [LWM2M\_OBJECT\_CONNECTIVITY\_MONITORING\_ID](group__lwm2m__api.md#ga73db8616cc7dbbd04267d97a743b8ec0)   4 |
|  | Connectivity Monitoring object. |
| #define | [LWM2M\_OBJECT\_FIRMWARE\_ID](group__lwm2m__api.md#ga442cc51c7d0807a752ce4affe9221c5b)   5 |
|  | Firmware object. |
| #define | [LWM2M\_OBJECT\_LOCATION\_ID](group__lwm2m__api.md#ga1046ec68deab3d812d7e5921fb718028)   6 |
|  | Location object. |
| #define | [LWM2M\_OBJECT\_CONNECTIVITY\_STATISTICS\_ID](group__lwm2m__api.md#gaa6c374c401dd36b6e121ac48c91ca9cf)   7 |
|  | Connectivity Statistics object. |
| #define | [LWM2M\_OBJECT\_SOFTWARE\_MANAGEMENT\_ID](group__lwm2m__api.md#gac2d140b4a36d6010fe93bca443a658c0)   9 |
|  | Software Management object. |
| #define | [LWM2M\_OBJECT\_PORTFOLIO\_ID](group__lwm2m__api.md#ga4b4ce912a4554923974461ea3c76007e)   16 |
|  | Portfolio object. |
| #define | [LWM2M\_OBJECT\_BINARYAPPDATACONTAINER\_ID](group__lwm2m__api.md#ga85eabde1900ef052064d34cf5e3a4afe)   19 |
|  | Binary App Data Container object. |
| #define | [LWM2M\_OBJECT\_EVENT\_LOG\_ID](group__lwm2m__api.md#ga4f0455fb0271c2fcbb7dadb944431ff0)   20 |
|  | Event Log object. |
| #define | [LWM2M\_OBJECT\_OSCORE\_ID](group__lwm2m__api.md#gab13a1600a662ed1dbd8845c6d7d4549a)   21 |
|  | OSCORE object. |
| #define | [LWM2M\_OBJECT\_GATEWAY\_ID](group__lwm2m__api.md#ga3505e9ddcd54afe86e8bd5fbc03fb565)   25 |
|  | Gateway object. |
| LwM2M Objects produced by 3rd party Standards Development | |
| Organizations.  Refer to the OMA LightweightM2M (LwM2M) Object and Resource Registry: [http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html](http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html) | |
| #define | [IPSO\_OBJECT\_GENERIC\_SENSOR\_ID](group__lwm2m__api.md#gaeef485c23d306c93fc0f45dd58766ad9)   3300 |
|  | IPSO Generic Sensor object. |
| #define | [IPSO\_OBJECT\_TEMP\_SENSOR\_ID](group__lwm2m__api.md#ga3b0c046d93c7bcee9d4da121dd574ff0)   3303 |
|  | IPSO Temperature Sensor object. |
| #define | [IPSO\_OBJECT\_HUMIDITY\_SENSOR\_ID](group__lwm2m__api.md#ga8075d8b7eb3b4c98f621efef673bb11f)   3304 |
|  | IPSO Humidity Sensor object. |
| #define | [IPSO\_OBJECT\_LIGHT\_CONTROL\_ID](group__lwm2m__api.md#ga56ebac5260ee467b3763abe49ff3b8ff)   3311 |
|  | IPSO Light Control object. |
| #define | [IPSO\_OBJECT\_ACCELEROMETER\_ID](group__lwm2m__api.md#ga0b3b9db806e5fe47cc08de34b5fb35fe)   3313 |
|  | IPSO Accelerometer object. |
| #define | [IPSO\_OBJECT\_VOLTAGE\_SENSOR\_ID](group__lwm2m__api.md#ga270a1b5a576d72099287633b32ce909f)   3316 |
|  | IPSO Voltage Sensor object. |
| #define | [IPSO\_OBJECT\_CURRENT\_SENSOR\_ID](group__lwm2m__api.md#gae511fd54112829e63c691776750893c2)   3317 |
|  | IPSO Current Sensor object. |
| #define | [IPSO\_OBJECT\_PRESSURE\_ID](group__lwm2m__api.md#ga752f81e91d0965a50ecfb0679bdea6ba)   3323 |
|  | IPSO Pressure Sensor object. |
| #define | [IPSO\_OBJECT\_BUZZER\_ID](group__lwm2m__api.md#ga15d664ddbfbf4d5b25dde34a5c650e6b)   3338 |
|  | IPSO Buzzer object. |
| #define | [IPSO\_OBJECT\_TIMER\_ID](group__lwm2m__api.md#ga6c7bd5880fa22050748c2cb01981cbcb)   3340 |
|  | IPSO Timer object. |
| #define | [IPSO\_OBJECT\_ONOFF\_SWITCH\_ID](group__lwm2m__api.md#ga776a6a5e1eab3a8de0a39382f94b663a)   3342 |
|  | IPSO On/Off Switch object. |
| #define | [IPSO\_OBJECT\_PUSH\_BUTTON\_ID](group__lwm2m__api.md#ga6e3119bc8f0b9143ab384e82a5bccf7c)   3347 |
|  | IPSO Push Button object. |
| #define | [UCIFI\_OBJECT\_BATTERY\_ID](group__lwm2m__api.md#gacdd09a26ce52f36c644a89a8b89f7d32)   3411 |
|  | uCIFI Battery object |
| #define | [IPSO\_OBJECT\_FILLING\_LEVEL\_SENSOR\_ID](group__lwm2m__api.md#ga21f6bc6255f5f5ed28881fa797d026ca)   3435 |
|  | IPSO Filling Level Sensor object. |
| Power source types used for the "Available Power Sources" resource of | |
| the LwM2M Device object (3/0/6). | |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_DC\_POWER](group__lwm2m__api.md#gae154ca2e54ec7759dd43f2a7a275077e)   0 |
|  | DC power. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_INT](group__lwm2m__api.md#ga04ca8ac536eed7d411c1b1ea2b2a59ac)   1 |
|  | Internal battery. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_EXT](group__lwm2m__api.md#gaf12052f903a688712928d036b782f621)   2 |
|  | External battery. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_FUEL\_CELL](group__lwm2m__api.md#ga10c4633c97881ca7d87c748aaeec68c9)   3 |
|  | Fuel cell. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_PWR\_OVER\_ETH](group__lwm2m__api.md#ga72352523996e61ea93caff0bb80c42ba)   4 |
|  | Power over Ethernet. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_USB](group__lwm2m__api.md#ga4877877be75d3dd3c8f600b438b7ea8e)   5 |
|  | USB. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_AC\_POWER](group__lwm2m__api.md#ga97b9d38ec402478f10642f1f83a4f88a)   6 |
|  | AC (mains) power. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_SOLAR](group__lwm2m__api.md#gaa41ec1d2ca43e1385cfb11204aff729d)   7 |
|  | Solar. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_MAX](group__lwm2m__api.md#gae7a580aac1804abbcf3feb57a5a30a02)   8 |
|  | Max value for Available Power Source type. |
| Error codes used for the "Error Code" resource of the LwM2M Device | |
| object.  An LwM2M client can register one of the following error codes via the [lwm2m\_device\_add\_err()](group__lwm2m__api.md#gabf8726f0438477863423947a7bb77ce2 "Register a new error code with LwM2M Device object.") function. | |
| #define | [LWM2M\_DEVICE\_ERROR\_NONE](group__lwm2m__api.md#gad54ec75eb2843d5eed199ddedca6ef4f)   0 |
|  | No error. |
| #define | [LWM2M\_DEVICE\_ERROR\_LOW\_POWER](group__lwm2m__api.md#ga53a9ee1ae09dd32a8dc2df6018798f9f)   1 |
|  | Low battery power. |
| #define | [LWM2M\_DEVICE\_ERROR\_EXT\_POWER\_SUPPLY\_OFF](group__lwm2m__api.md#ga33152ea4ef497b02a12d1218d470a5a6)   2 |
|  | External power supply off. |
| #define | [LWM2M\_DEVICE\_ERROR\_GPS\_FAILURE](group__lwm2m__api.md#ga3c1b7693167ff517c5cbd7bbdbfd1ea0)   3 |
|  | GPS module failure. |
| #define | [LWM2M\_DEVICE\_ERROR\_LOW\_SIGNAL\_STRENGTH](group__lwm2m__api.md#ga78048382d8bc85bbabbff58f0a9860f2)   4 |
|  | Low received signal strength. |
| #define | [LWM2M\_DEVICE\_ERROR\_OUT\_OF\_MEMORY](group__lwm2m__api.md#ga94ce0177c066dd43ef660b85afc83485)   5 |
|  | Out of memory. |
| #define | [LWM2M\_DEVICE\_ERROR\_SMS\_FAILURE](group__lwm2m__api.md#gabcb39cd3757ea60859984f6ad0df9e31)   6 |
|  | SMS failure. |
| #define | [LWM2M\_DEVICE\_ERROR\_NETWORK\_FAILURE](group__lwm2m__api.md#ga2110d71a0c58087ff877e66b7500ba66)   7 |
|  | IP Connectivity failure. |
| #define | [LWM2M\_DEVICE\_ERROR\_PERIPHERAL\_FAILURE](group__lwm2m__api.md#ga77e6352eace8116576c880bf7e416ba3)   8 |
|  | Peripheral malfunction. |
| Battery status codes used for the "Battery Status" resource (3/0/20) | |
| of the LwM2M Device object.  As the battery status changes, an LwM2M client can set one of the following codes via: lwm2m\_engine\_set\_u8("3/0/20", [battery status]) | |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_NORMAL](group__lwm2m__api.md#ga4329c971f95f1c345381d1c864a9f334)   0 |
|  | The battery is operating normally and not on power. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGING](group__lwm2m__api.md#gaf19da3a566782aeebebfb6ff110a9152)   1 |
|  | The battery is currently charging. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGE\_COMP](group__lwm2m__api.md#ga5f7e88b52d8e6029467a2ed10585e6d4)   2 |
|  | The battery is fully charged and the charger is still connected. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_DAMAGED](group__lwm2m__api.md#gaa3f81df5e4d45838922eb20a15ee3153)   3 |
|  | The battery has some problem. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_LOW](group__lwm2m__api.md#ga578f6446ec1b70d2a32917abf1f5aad7)   4 |
|  | The battery is low on charge. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_NOT\_INST](group__lwm2m__api.md#gacc3dfc99fc2cd9ef7048b1a0a0fd55c8)   5 |
|  | The battery is not installed. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_UNKNOWN](group__lwm2m__api.md#ga174e118b07982b87c6c083236b79c3b7)   6 |
|  | The battery information is not available. |
| LWM2M Firmware Update object states | |
| An LwM2M client or the LwM2M Firmware Update object use the following codes to represent the LwM2M Firmware Update state (5/0/3). | |
| #define | [STATE\_IDLE](group__lwm2m__api.md#gaafff27c7165f059a969fe60fee51f683)   0 |
|  | Idle. |
| #define | [STATE\_DOWNLOADING](group__lwm2m__api.md#gaeb34e88a0da4ac1274ae6b2cef010086)   1 |
|  | Downloading. |
| #define | [STATE\_DOWNLOADED](group__lwm2m__api.md#ga009085120be71a28c1f6ebdaf7503365)   2 |
|  | Downloaded. |
| #define | [STATE\_UPDATING](group__lwm2m__api.md#gaac1dab8d1ac28bf13faeee39d1df47c5)   3 |
|  | Updating. |
| LWM2M Firmware Update object result codes | |
| After processing a firmware update, the client sets the result via one of the following codes via lwm2m\_engine\_set\_u8("5/0/5", [result code]) | |
| #define | [RESULT\_DEFAULT](group__lwm2m__api.md#ga391b47507468bbc1005903a56f80b1ea)   0 |
|  | Initial value. |
| #define | [RESULT\_SUCCESS](group__lwm2m__api.md#ga7cc1753a05a0821f6c70dd2bccfbab5c)   1 |
|  | Firmware updated successfully. |
| #define | [RESULT\_NO\_STORAGE](group__lwm2m__api.md#ga829f7bc83b67dcf16ea4775addd87343)   2 |
|  | Not enough flash memory for the new firmware package. |
| #define | [RESULT\_OUT\_OF\_MEM](group__lwm2m__api.md#gab5446111a8969aa2c66dae49f04c93cf)   3 |
|  | Out of RAM during downloading process. |
| #define | [RESULT\_CONNECTION\_LOST](group__lwm2m__api.md#ga0655ba8c402d8b6c8bbd84fb36447bd4)   4 |
|  | Connection lost during downloading process. |
| #define | [RESULT\_INTEGRITY\_FAILED](group__lwm2m__api.md#gadfd0ac7b6a3fededa2b4471dfe52d3d2)   5 |
|  | Integrity check failure for new downloaded package. |
| #define | [RESULT\_UNSUP\_FW](group__lwm2m__api.md#gab06dbfdac0c95f8100908a1177f3a62a)   6 |
|  | Unsupported package type. |
| #define | [RESULT\_INVALID\_URI](group__lwm2m__api.md#ga268204053d7e23737283523224699979)   7 |
|  | Invalid URI. |
| #define | [RESULT\_UPDATE\_FAILED](group__lwm2m__api.md#ga2dfdd95c2c03ccca25d855b6d6f96ed3)   8 |
|  | Firmware update failed. |
| #define | [RESULT\_UNSUP\_PROTO](group__lwm2m__api.md#gade3da37a44ee40292ec6344403db8d8d)   9 |
|  | Unsupported protocol. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [lwm2m\_socket\_fault\_cb\_t](group__lwm2m__api.md#gae7bf50f9abf1b82b76ac3e9175e685ac)) (int error) |
|  | Callback function called when a socket error is encountered. |
| typedef void(\* | [lwm2m\_observe\_cb\_t](group__lwm2m__api.md#gad7bea67e16e1e831e0f949dbf83d5afe)) (enum [lwm2m\_observe\_event](group__lwm2m__api.md#gac8d63952ec94ca6cfb1dbe12a6c53bfb) event, struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*user\_data) |
|  | Observe callback indicating observer adds and deletes, and notification ACKs and timeouts. |
| typedef void(\* | [lwm2m\_ctx\_event\_cb\_t](group__lwm2m__api.md#ga38dbaf038426efc75d889c4a0666dac9)) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx, enum [lwm2m\_rd\_client\_event](group__lwm2m__api.md#gaca90ab8960a4ff01d44735dbc0405862) event) |
|  | Asynchronous RD client event callback. |
| typedef void \*(\* | [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384)) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_inst\_id, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*data\_len) |
|  | Asynchronous callback to get a resource buffer and length. |
| typedef int(\* | [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9)) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_inst\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) total\_size) |
|  | Asynchronous callback when data has been set to a resource buffer. |
| typedef int(\* | [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf)) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id) |
|  | Asynchronous event notification callback. |
| typedef int(\* | [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe)) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*args, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) args\_len) |
|  | Asynchronous execute notification callback. |
| typedef void(\* | [lwm2m\_send\_cb\_t](group__lwm2m__api.md#gaf5394884da53edb28fe4afc92bf40e6a)) (enum [lwm2m\_send\_status](group__lwm2m__api.md#ga20848e0942882e8c2cc40ee8a48b7bfd) status) |
|  | Callback returning send status. |

| Enumerations | |
| --- | --- |
| enum | [lwm2m\_observe\_event](group__lwm2m__api.md#gac8d63952ec94ca6cfb1dbe12a6c53bfb) { [LWM2M\_OBSERVE\_EVENT\_OBSERVER\_ADDED](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfba22f4341d713417110d9866b0cbd318e3) , [LWM2M\_OBSERVE\_EVENT\_OBSERVER\_REMOVED](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfbae3f4af98b52ee191229c660748c7dd6c) , [LWM2M\_OBSERVE\_EVENT\_NOTIFY\_ACK](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfbaab4e1cf0451ba926b90ea21152cac885) , [LWM2M\_OBSERVE\_EVENT\_NOTIFY\_TIMEOUT](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfba55494fd6e76f585894e34dc9004fbc9e) } |
|  | Observe callback events. [More...](group__lwm2m__api.md#gac8d63952ec94ca6cfb1dbe12a6c53bfb) |
| enum | [lwm2m\_socket\_states](group__lwm2m__api.md#ga7611c1aebb0309ee8340e06dd8ee234d) { [LWM2M\_SOCKET\_STATE\_ONGOING](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234daa0f06bc70659598b0f51b3ce8094c6ab) , [LWM2M\_SOCKET\_STATE\_ONE\_RESPONSE](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234da76aa03f71f44096d9413b1f5718d9711) , [LWM2M\_SOCKET\_STATE\_LAST](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234daed676a6deffe2de7c916bb6eb2906100) , [LWM2M\_SOCKET\_STATE\_NO\_DATA](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234da2487ae8e93929bf62fd333cd04c5b915) } |
|  | Different traffic states of the LwM2M socket. [More...](group__lwm2m__api.md#ga7611c1aebb0309ee8340e06dd8ee234d) |
| enum | [lwm2m\_rd\_client\_event](group__lwm2m__api.md#gaca90ab8960a4ff01d44735dbc0405862) {     [LWM2M\_RD\_CLIENT\_EVENT\_NONE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aca4ebc8d550af02f1891eed1a7b1afcc) , [LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_FAILURE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac089b900494522de565e36d31ea3b0c4) , [LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac30dd8520e591c8e51c74ce1a53cd524) , [LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_TRANSFER\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a7c7c3115b6ff16dfa722b6b82c2cd1bc) ,     [LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_FAILURE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ae89498cad338b1dc9cbd3b23838bf0b6) , [LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a8994ea8c025cbbd56adcc050a7e86541) , [LWM2M\_RD\_CLIENT\_EVENT\_REG\_TIMEOUT](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404) , [LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a9f53175c5e935f061a83aa1fcfe9f683) ,     [LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER\_FAILURE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a32552b56152f9a714675fc6bba3b3d5f) , [LWM2M\_RD\_CLIENT\_EVENT\_DISCONNECT](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac6703e7d0809cc9cfcdd1cbd48e2318b) , [LWM2M\_RD\_CLIENT\_EVENT\_QUEUE\_MODE\_RX\_OFF](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a7c7853536c452da2f74e9f43a024fcbe) , [LWM2M\_RD\_CLIENT\_EVENT\_ENGINE\_SUSPENDED](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862afd4eda5dee31b18b1da5414481e33525) ,     [LWM2M\_RD\_CLIENT\_EVENT\_NETWORK\_ERROR](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aff939a86c623ab8258c707361b95aef4) , [LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ab48772aeed0ead72f3a9289a618af1cd) , [LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aac3938a209800a0de0a05b21fab02c13) , [LWM2M\_RD\_CLIENT\_EVENT\_SERVER\_DISABLED](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a873a4a3190dc7c24d2518dc8d7268763)   } |
|  | LwM2M RD client events. [More...](group__lwm2m__api.md#gaca90ab8960a4ff01d44735dbc0405862) |
| enum | [lwm2m\_send\_status](group__lwm2m__api.md#ga20848e0942882e8c2cc40ee8a48b7bfd) { [LWM2M\_SEND\_STATUS\_SUCCESS](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda127cca7752ab3f00d5a4705f815b14b4) , [LWM2M\_SEND\_STATUS\_FAILURE](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda7a7f1720f39bedba28110fad09939dcd) , [LWM2M\_SEND\_STATUS\_TIMEOUT](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda7c0144cafd4f91a76d229b40df9cb82a) } |
|  | LwM2M send status. [More...](group__lwm2m__api.md#ga20848e0942882e8c2cc40ee8a48b7bfd) |
| enum | [lwm2m\_security\_mode\_e](group__lwm2m__api.md#ga11de8078091631cb88b26a9a460097ab) {     [LWM2M\_SECURITY\_PSK](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba0d4e9d5160e91fc93e062dfb812edb25) = 0 , [LWM2M\_SECURITY\_RAW\_PK](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba431ac48d7f0fed72ce5ab2c8ea823716) = 1 , [LWM2M\_SECURITY\_CERT](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba6eef062c9f54bc9698a050c8bb2915ba) = 2 , [LWM2M\_SECURITY\_NOSEC](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097abaf6bb17f06d89124076810c132005f8d7) = 3 ,     [LWM2M\_SECURITY\_CERT\_EST](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097abaefb45683a68002dab267c3fb2e876824) = 4   } |
|  | Security modes as defined in LwM2M Security object. [More...](group__lwm2m__api.md#ga11de8078091631cb88b26a9a460097ab) |

| Functions | |
| --- | --- |
| int | [lwm2m\_device\_add\_err](group__lwm2m__api.md#gabf8726f0438477863423947a7bb77ce2) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) error\_code) |
|  | Register a new error code with LwM2M Device object. |
| void | [lwm2m\_firmware\_set\_write\_cb](group__lwm2m__api.md#ga6878ea0ebb512b19a4fb0859756f51d0) ([lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb) |
|  | Set data callback for firmware block transfer. |
| [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) | [lwm2m\_firmware\_get\_write\_cb](group__lwm2m__api.md#ga4bf0bbedf5573ac18a11ac4fced11284) (void) |
|  | Get the data callback for firmware block transfer writes. |
| void | [lwm2m\_firmware\_set\_write\_cb\_inst](group__lwm2m__api.md#gac4e4a819e54344657d70ec479eb6ec8d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb) |
|  | Set data callback for firmware block transfer. |
| [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) | [lwm2m\_firmware\_get\_write\_cb\_inst](group__lwm2m__api.md#gad7334f06c3bdb14485597794a417152d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id) |
|  | Get the data callback for firmware block transfer writes. |
| void | [lwm2m\_firmware\_set\_cancel\_cb](group__lwm2m__api.md#ga3955dca5cd6d67807ed75e61a4d84d84) ([lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb) |
|  | Set callback for firmware update cancel. |
| [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) | [lwm2m\_firmware\_get\_cancel\_cb](group__lwm2m__api.md#ga9561c1b8407d888f6fbe1e0ceab1c235) (void) |
|  | Get a callback for firmware update cancel. |
| void | [lwm2m\_firmware\_set\_cancel\_cb\_inst](group__lwm2m__api.md#gaa200b524e505f64247f1e7472c5f36d4) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb) |
|  | Set data callback for firmware update cancel. |
| [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) | [lwm2m\_firmware\_get\_cancel\_cb\_inst](group__lwm2m__api.md#ga6f4b3e08c7e03cff4bf31e2f2999971e) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id) |
|  | Get the callback for firmware update cancel. |
| void | [lwm2m\_firmware\_set\_update\_cb](group__lwm2m__api.md#ga61eb38e42d9e1b3f467c43a324f2fc65) ([lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set data callback to handle firmware update execute events. |
| [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) | [lwm2m\_firmware\_get\_update\_cb](group__lwm2m__api.md#ga1e4b8ba1b19ac9025dca3c4799bba84a) (void) |
|  | Get the event callback for firmware update execute events. |
| void | [lwm2m\_firmware\_set\_update\_cb\_inst](group__lwm2m__api.md#ga31d0f3e40b5e3d608d16a4268b2f1b29) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set data callback to handle firmware update execute events. |
| [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) | [lwm2m\_firmware\_get\_update\_cb\_inst](group__lwm2m__api.md#ga34995e902b63c4d7d37ebd709d88a72a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id) |
|  | Get the event callback for firmware update execute events. |
| int | [lwm2m\_swmgmt\_set\_activate\_cb](group__lwm2m__api.md#gac374d0559056ddb9cf43deae932fd128) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set callback to handle software activation requests. |
| int | [lwm2m\_swmgmt\_set\_deactivate\_cb](group__lwm2m__api.md#ga7a2b93b918257bece819dc44804f27f5) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set callback to handle software deactivation requests. |
| int | [lwm2m\_swmgmt\_set\_install\_package\_cb](group__lwm2m__api.md#gadfc00060c0b538ed576b5e3edd7dac80) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set callback to handle software install requests. |
| int | [lwm2m\_swmgmt\_set\_delete\_package\_cb](group__lwm2m__api.md#gacf209563efdc5f3201152088c52d05c3) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set callback to handle software uninstall requests. |
| int | [lwm2m\_swmgmt\_set\_read\_package\_version\_cb](group__lwm2m__api.md#gab59370ce4fdc94adb4903f22ab1f95b2) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb) |
|  | Set callback to read software package. |
| int | [lwm2m\_swmgmt\_set\_write\_package\_cb](group__lwm2m__api.md#ga293904118f972ae387c8aa85a1028b54) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb) |
|  | Set data callback for software management block transfer. |
| int | [lwm2m\_swmgmt\_install\_completed](group__lwm2m__api.md#ga573e128348fb2f43a33bd09332dd677f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, int error\_code) |
|  | Function to be called when a Software Management object instance completed the Install operation. |
| void | [lwm2m\_event\_log\_set\_read\_log\_data\_cb](group__lwm2m__api.md#ga950557bce8c510bcc8b0704e7bc4a9dc) ([lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb) |
|  | Set callback to read log data. |
| int | [lwm2m\_engine\_update\_observer\_min\_period](group__lwm2m__api.md#ga489c8ea2eb89c7c6dc008002ab2ea836) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, const char \*pathstr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s) |
|  | Change an observer's pmin value. |
| int | [lwm2m\_update\_observer\_min\_period](group__lwm2m__api.md#gadd163806d70713d8349a9db484ba88bf) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s) |
|  | Change an observer's pmin value. |
| int | [lwm2m\_engine\_update\_observer\_max\_period](group__lwm2m__api.md#gacb717ef5a36524e6f0f78b90cc803577) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, const char \*pathstr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s) |
|  | Change an observer's pmax value. |
| int | [lwm2m\_update\_observer\_max\_period](group__lwm2m__api.md#ga6acccbcd879901574aceab53a21800fc) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s) |
|  | Change an observer's pmax value. |
| int | [lwm2m\_engine\_create\_obj\_inst](group__lwm2m__api.md#ga32f393a9e302f1f60839fd2147ebd7e9) (const char \*pathstr) |
|  | Create an LwM2M object instance. |
| int | [lwm2m\_create\_object\_inst](group__lwm2m__api.md#ga53f5b4c5967e93c7dd224fce8f416265) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Create an LwM2M object instance. |
| int | [lwm2m\_engine\_delete\_obj\_inst](group__lwm2m__api.md#ga3849e960b54bcb089ac00476da8fb430) (const char \*pathstr) |
|  | Delete an LwM2M object instance. |
| int | [lwm2m\_delete\_object\_inst](group__lwm2m__api.md#gaf921d4bc96090ef8735d90d173feab94) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Delete an LwM2M object instance. |
| void | [lwm2m\_registry\_lock](group__lwm2m__api.md#ga9a0cdcc9fc6d37462eddeb54e5d1f87a) (void) |
|  | Locks the registry for this thread. |
| void | [lwm2m\_registry\_unlock](group__lwm2m__api.md#gab09b62982c34887cdd16c30659d3349a) (void) |
|  | Unlocks the registry previously locked by [lwm2m\_registry\_lock()](group__lwm2m__api.md#ga9a0cdcc9fc6d37462eddeb54e5d1f87a "Locks the registry for this thread."). |
| int | [lwm2m\_engine\_set\_opaque](group__lwm2m__api.md#ga2a891e26440f732b77ab90b979c8cb49) (const char \*pathstr, const char \*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len) |
|  | Set resource (instance) value (opaque buffer). |
| int | [lwm2m\_set\_opaque](group__lwm2m__api.md#gaaef33bdf3f48fd91abdb50db4d5460f9) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const char \*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len) |
|  | Set resource (instance) value (opaque buffer). |
| int | [lwm2m\_engine\_set\_string](group__lwm2m__api.md#ga28911733660e7ce2f2f73c8eeb87de59) (const char \*pathstr, const char \*data\_ptr) |
|  | Set resource (instance) value (string). |
| int | [lwm2m\_set\_string](group__lwm2m__api.md#ga7217f33bf705011d91ba66c86a4d5747) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const char \*data\_ptr) |
|  | Set resource (instance) value (string). |
| int | [lwm2m\_engine\_set\_u8](group__lwm2m__api.md#ga00a61b227bae53a70b0092bb94801ea8) (const char \*pathstr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Set resource (instance) value (u8). |
| int | [lwm2m\_set\_u8](group__lwm2m__api.md#ga1aa3ff424b7190d0fbd9366626b2685c) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Set resource (instance) value (u8). |
| int | [lwm2m\_engine\_set\_u16](group__lwm2m__api.md#ga4fcea78d9506822ee76df465cf71ffdf) (const char \*pathstr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value) |
|  | Set resource (instance) value (u16). |
| int | [lwm2m\_set\_u16](group__lwm2m__api.md#ga1f06bb65571efee18db5d061f95399c3) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value) |
|  | Set resource (instance) value (u16). |
| int | [lwm2m\_engine\_set\_u32](group__lwm2m__api.md#ga326c722de4ecdcbc09adb52c83cf6400) (const char \*pathstr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Set resource (instance) value (u32). |
| int | [lwm2m\_set\_u32](group__lwm2m__api.md#ga9481e570b121404dc1be1ce23d904894) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Set resource (instance) value (u32). |
| int | [lwm2m\_engine\_set\_u64](group__lwm2m__api.md#ga7d04c579284369233156a0597f09ab83) (const char \*pathstr, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value) |
|  | Set resource (instance) value (u64). |
| int | [lwm2m\_set\_u64](group__lwm2m__api.md#ga8a751dc8384cc47f9c14d916e20ae19d) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value) |
|  | Set resource (instance) value (u64). |
| int | [lwm2m\_engine\_set\_s8](group__lwm2m__api.md#gae665c8bb81c0aef3b960b087ff0f97f8) (const char \*pathstr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) value) |
|  | Set resource (instance) value (s8). |
| int | [lwm2m\_set\_s8](group__lwm2m__api.md#ga37261a4b9e54eab3d1d855a084d082aa) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) value) |
|  | Set resource (instance) value (s8). |
| int | [lwm2m\_engine\_set\_s16](group__lwm2m__api.md#ga1dd4952af0029c94a71f74734ae3a16c) (const char \*pathstr, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) value) |
|  | Set resource (instance) value (s16). |
| int | [lwm2m\_set\_s16](group__lwm2m__api.md#gad548ffedcb8328b23eb32476a97be6ee) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) value) |
|  | Set resource (instance) value (s16). |
| int | [lwm2m\_engine\_set\_s32](group__lwm2m__api.md#ga4f45dc38b5e6a55633474ff5d5447ecb) (const char \*pathstr, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value) |
|  | Set resource (instance) value (s32). |
| int | [lwm2m\_set\_s32](group__lwm2m__api.md#ga327e086959fc5649a5ef14f1f2943e88) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value) |
|  | Set resource (instance) value (s32). |
| int | [lwm2m\_engine\_set\_s64](group__lwm2m__api.md#ga11619cc0907010018217b8d67e9e9f7e) (const char \*pathstr, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) value) |
|  | Set resource (instance) value (s64). |
| int | [lwm2m\_set\_s64](group__lwm2m__api.md#ga18fcee379640c0dda32d6e3d14827260) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) value) |
|  | Set resource (instance) value (s64). |
| int | [lwm2m\_engine\_set\_bool](group__lwm2m__api.md#ga8c82346313a9bf1234f72d71a5db34f5) (const char \*pathstr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
|  | Set resource (instance) value (bool). |
| int | [lwm2m\_set\_bool](group__lwm2m__api.md#ga9ef21d06bef8a97b7666c0aa7fa753b4) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
|  | Set resource (instance) value (bool). |
| int | [lwm2m\_engine\_set\_float](group__lwm2m__api.md#gae85eb5da495b7d42b10cf01c0d826632) (const char \*pathstr, const double \*value) |
|  | Set resource (instance) value (double). |
| int | [lwm2m\_set\_f64](group__lwm2m__api.md#ga3386d3f2ad8d9713fc2283ed6921c2fc) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const double value) |
|  | Set resource (instance) value (double). |
| int | [lwm2m\_engine\_set\_objlnk](group__lwm2m__api.md#gada5007c34ce2ee72017065b32f1cee58) (const char \*pathstr, const struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \*value) |
|  | Set resource (instance) value (Objlnk). |
| int | [lwm2m\_set\_objlnk](group__lwm2m__api.md#ga04a18bd8a4eeea41a47803c16567d67b) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \*value) |
|  | Set resource (instance) value (Objlnk). |
| int | [lwm2m\_engine\_set\_time](group__lwm2m__api.md#gad3621c4a9ddfdc2a9e8fe2df058aefd7) (const char \*pathstr, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) value) |
|  | Set resource (instance) value (Time). |
| int | [lwm2m\_set\_time](group__lwm2m__api.md#ga7194ad24842e35130d8af7f5104c0844) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) value) |
|  | Set resource (instance) value (Time). |
| int | [lwm2m\_engine\_get\_opaque](group__lwm2m__api.md#ga3439a579648c15bfe8883337c4618095) (const char \*pathstr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen) |
|  | Get resource (instance) value (opaque buffer). |
| int | [lwm2m\_get\_opaque](group__lwm2m__api.md#gae245a9a1d9456af7e6283b1074944606) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen) |
|  | Get resource (instance) value (opaque buffer). |
| int | [lwm2m\_engine\_get\_string](group__lwm2m__api.md#ga72e27dfaf0881561245d01d6f800f0dc) (const char \*pathstr, void \*str, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen) |
|  | Get resource (instance) value (string). |
| int | [lwm2m\_get\_string](group__lwm2m__api.md#ga20fc58b25468bf309175db59d67b820b) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*str, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen) |
|  | Get resource (instance) value (string). |
| int | [lwm2m\_engine\_get\_u8](group__lwm2m__api.md#ga50ee578c777c7b8a1b0fbe028c8342ec) (const char \*pathstr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Get resource (instance) value (u8). |
| int | [lwm2m\_get\_u8](group__lwm2m__api.md#gac56e804962e529799c771d81ac1fd027) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Get resource (instance) value (u8). |
| int | [lwm2m\_engine\_get\_u16](group__lwm2m__api.md#ga68986109d78b60f83f9cd85742ed80fb) (const char \*pathstr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value) |
|  | Get resource (instance) value (u16). |
| int | [lwm2m\_get\_u16](group__lwm2m__api.md#ga1b96848f96bdab9939bb2619d3e1059b) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value) |
|  | Get resource (instance) value (u16). |
| int | [lwm2m\_engine\_get\_u32](group__lwm2m__api.md#gafddb717b3f43619e03a240660f65eb03) (const char \*pathstr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value) |
|  | Get resource (instance) value (u32). |
| int | [lwm2m\_get\_u32](group__lwm2m__api.md#ga0bc84cb39a7a537925ec7d62e54b8b48) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value) |
|  | Get resource (instance) value (u32). |
| int | [lwm2m\_engine\_get\_u64](group__lwm2m__api.md#ga8d9068217afe09b0930996e5796b8aac) (const char \*pathstr, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get resource (instance) value (u64). |
| int | [lwm2m\_get\_u64](group__lwm2m__api.md#ga831d229d9a4b983223dff626bbde7a66) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get resource (instance) value (u64). |
| int | [lwm2m\_engine\_get\_s8](group__lwm2m__api.md#ga701d36c7b7a63c8214bfa30c0c19c946) (const char \*pathstr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*value) |
|  | Get resource (instance) value (s8). |
| int | [lwm2m\_get\_s8](group__lwm2m__api.md#ga12817bfbf0a0cbb742568ee974a1c337) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*value) |
|  | Get resource (instance) value (s8). |
| int | [lwm2m\_engine\_get\_s16](group__lwm2m__api.md#ga96f29e6d897b96fedc7f3e19bd906f7c) (const char \*pathstr, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*value) |
|  | Get resource (instance) value (s16). |
| int | [lwm2m\_get\_s16](group__lwm2m__api.md#ga2426db6720b3f3e15e63022cabae5ece) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*value) |
|  | Get resource (instance) value (s16). |
| int | [lwm2m\_engine\_get\_s32](group__lwm2m__api.md#ga40895289c1c8b778b6bf30d444dda63a) (const char \*pathstr, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value) |
|  | Get resource (instance) value (s32). |
| int | [lwm2m\_get\_s32](group__lwm2m__api.md#ga99d7189efa25881dbcddd99e2a795f1b) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value) |
|  | Get resource (instance) value (s32). |
| int | [lwm2m\_engine\_get\_s64](group__lwm2m__api.md#ga7ad1a482074d033ad1def72882efd245) (const char \*pathstr, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*value) |
|  | Get resource (instance) value (s64). |
| int | [lwm2m\_get\_s64](group__lwm2m__api.md#gaaffe06ca9ee5302fb6e26164f250653e) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*value) |
|  | Get resource (instance) value (s64). |
| int | [lwm2m\_engine\_get\_bool](group__lwm2m__api.md#ga606e281a1146f930d7c0675d5881c7d6) (const char \*pathstr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*value) |
|  | Get resource (instance) value (bool). |
| int | [lwm2m\_get\_bool](group__lwm2m__api.md#gafdc72844ce0ca417e297d76288155aa4) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*value) |
|  | Get resource (instance) value (bool). |
| int | [lwm2m\_engine\_get\_float](group__lwm2m__api.md#ga0a272643082347fe6044bddbd7e5cebf) (const char \*pathstr, double \*buf) |
|  | Get resource (instance) value (double). |
| int | [lwm2m\_get\_f64](group__lwm2m__api.md#ga03b72e96a67fcbf85feb5bf0b9df81ce) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, double \*value) |
|  | Get resource (instance) value (double). |
| int | [lwm2m\_engine\_get\_objlnk](group__lwm2m__api.md#gaf4b23e412fcff5f2838f3e232a3cd224) (const char \*pathstr, struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \*buf) |
|  | Get resource (instance) value (Objlnk). |
| int | [lwm2m\_get\_objlnk](group__lwm2m__api.md#ga4de941c36cf678e12da6e05c378a92e5) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \*buf) |
|  | Get resource (instance) value (Objlnk). |
| int | [lwm2m\_engine\_get\_time](group__lwm2m__api.md#ga273fa47b65309b46aa1b73b224d0dfce) (const char \*pathstr, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*buf) |
|  | Get resource (instance) value (Time). |
| int | [lwm2m\_get\_time](group__lwm2m__api.md#ga2e1d41866b5ea35c5aa29bca9bb43812) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*buf) |
|  | Get resource (instance) value (Time). |
| int | [lwm2m\_engine\_register\_read\_callback](group__lwm2m__api.md#ga21d15060cce1c039a11106d71d681f4c) (const char \*pathstr, [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb) |
|  | Set resource (instance) read callback. |
| int | [lwm2m\_register\_read\_callback](group__lwm2m__api.md#gaf33bd6a527b6d399f3d92b666ac77dfb) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb) |
|  | Set resource (instance) read callback. |
| int | [lwm2m\_engine\_register\_pre\_write\_callback](group__lwm2m__api.md#ga1354bc59163db5b3435e8e86c8feafd8) (const char \*pathstr, [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb) |
|  | Set resource (instance) pre-write callback. |
| int | [lwm2m\_register\_pre\_write\_callback](group__lwm2m__api.md#ga6f775837e07ba9b0032be8917a593e16) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb) |
|  | Set resource (instance) pre-write callback. |
| int | [lwm2m\_engine\_register\_validate\_callback](group__lwm2m__api.md#gac1c92e1ee3a804b325aacfe116bad096) (const char \*pathstr, [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb) |
|  | Set resource (instance) validation callback. |
| int | [lwm2m\_register\_validate\_callback](group__lwm2m__api.md#gad6e5fd4815f409ad59ad631b03199333) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb) |
|  | Set resource (instance) validation callback. |
| int | [lwm2m\_engine\_register\_post\_write\_callback](group__lwm2m__api.md#ga5c43bcdb0575f8c56354d6b4e30641a3) (const char \*pathstr, [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb) |
|  | Set resource (instance) post-write callback. |
| int | [lwm2m\_register\_post\_write\_callback](group__lwm2m__api.md#ga3dd8b38e797173dae902404fb5b7a3f4) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb) |
|  | Set resource (instance) post-write callback. |
| int | [lwm2m\_engine\_register\_exec\_callback](group__lwm2m__api.md#gad213063b7e68bd7b4f3ce3de3736a237) (const char \*pathstr, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set resource execute event callback. |
| int | [lwm2m\_register\_exec\_callback](group__lwm2m__api.md#ga29cc5cdd697e94d7379b1fb178487916) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set resource execute event callback. |
| int | [lwm2m\_engine\_register\_create\_callback](group__lwm2m__api.md#gaa198bfb55f98183cbd33169468ae0bcc) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id, [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb) |
|  | Set object instance create event callback. |
| int | [lwm2m\_register\_create\_callback](group__lwm2m__api.md#ga346d547e02bd53ee83f83b2248449e98) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id, [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb) |
|  | Set object instance create event callback. |
| int | [lwm2m\_engine\_register\_delete\_callback](group__lwm2m__api.md#ga6a5dfdd29055bed245bf16ecc5829f95) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id, [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb) |
|  | Set object instance delete event callback. |
| int | [lwm2m\_register\_delete\_callback](group__lwm2m__api.md#ga92d7e6d81ef674a6c311e1717c6bf373) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id, [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb) |
|  | Set object instance delete event callback. |
| int | [lwm2m\_engine\_set\_res\_buf](group__lwm2m__api.md#ga66bdc3f3a4d0e88b036c9704abfbcafc) (const char \*pathstr, void \*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buffer\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data\_flags) |
|  | Set data buffer for a resource. |
| int | [lwm2m\_set\_res\_buf](group__lwm2m__api.md#ga56a2aecd38baedb5dc17258610c4780d) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buffer\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data\_flags) |
|  | Set data buffer for a resource. |
| int | [lwm2m\_engine\_set\_res\_data](group__lwm2m__api.md#gabf56a29aec75675099df2d45ca802718) (const char \*pathstr, void \*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data\_flags) |
|  | Set data buffer for a resource. |
| int | [lwm2m\_engine\_set\_res\_data\_len](group__lwm2m__api.md#ga87833da93894dc5df45b91dfaebf3f91) (const char \*pathstr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len) |
|  | Update data size for a resource. |
| int | [lwm2m\_set\_res\_data\_len](group__lwm2m__api.md#ga0f2b115d231bea6622135d72b51f55ca) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len) |
|  | Update data size for a resource. |
| int | [lwm2m\_engine\_get\_res\_buf](group__lwm2m__api.md#gaff5e10bc0fa34c1fe72a0b4e1ed2bc39) (const char \*pathstr, void \*\*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buffer\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_flags) |
|  | Get data buffer for a resource. |
| int | [lwm2m\_get\_res\_buf](group__lwm2m__api.md#gac0b6669d8a19b03eb8b08cbbcdb0c192) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*\*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buffer\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_flags) |
|  | Get data buffer for a resource. |
| int | [lwm2m\_engine\_get\_res\_data](group__lwm2m__api.md#ga630079a8d2f2acae1c313297cfdbada9) (const char \*pathstr, void \*\*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_flags) |
|  | Get data buffer for a resource. |
| int | [lwm2m\_engine\_create\_res\_inst](group__lwm2m__api.md#ga64b0427f36b6d2d2f8af8cc2e35cdb89) (const char \*pathstr) |
|  | Create a resource instance. |
| int | [lwm2m\_create\_res\_inst](group__lwm2m__api.md#gac69c40474180fe14c3761185b2db1c0c) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Create a resource instance. |
| int | [lwm2m\_engine\_delete\_res\_inst](group__lwm2m__api.md#gac188cd5fdd226dd105d73a4e391c601b) (const char \*pathstr) |
|  | Delete a resource instance. |
| int | [lwm2m\_delete\_res\_inst](group__lwm2m__api.md#gacfeb63db0423e6730ffaa826a87eb262) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Delete a resource instance. |
| int | [lwm2m\_update\_device\_service\_period](group__lwm2m__api.md#gab45cebf6f0b6b70974367ca453d16aeb) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_ms) |
|  | Update the period of the device service. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [lwm2m\_engine\_path\_is\_observed](group__lwm2m__api.md#ga07149d4b624a7294f4508df8c1681b1b) (const char \*pathstr) |
|  | Check whether a path is observed. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [lwm2m\_path\_is\_observed](group__lwm2m__api.md#ga1065c729d5caa8ca13de7766fce77953) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Check whether a path is observed. |
| int | [lwm2m\_engine\_stop](group__lwm2m__api.md#ga077e1abd612d31dd33fab52b7d205c39) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx) |
|  | Stop the LwM2M engine. |
| int | [lwm2m\_engine\_start](group__lwm2m__api.md#ga9f72fbd0163b15c48ea09cf7d511e444) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx) |
|  | Start the LwM2M engine. |
| void | [lwm2m\_acknowledge](group__lwm2m__api.md#ga919c7d6f418cda99c77fdaf54ae1a7b0) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx) |
|  | Acknowledge the currently processed request with an empty ACK. |
| int | [lwm2m\_rd\_client\_start](group__lwm2m__api.md#ga9dfd46b8a535b1f28e644dc18f57fd79) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, const char \*ep\_name, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [lwm2m\_ctx\_event\_cb\_t](group__lwm2m__api.md#ga38dbaf038426efc75d889c4a0666dac9) event\_cb, [lwm2m\_observe\_cb\_t](group__lwm2m__api.md#gad7bea67e16e1e831e0f949dbf83d5afe) observe\_cb) |
|  | Start the LwM2M RD (Registration / Discovery) Client. |
| int | [lwm2m\_rd\_client\_stop](group__lwm2m__api.md#gafd87e5d975c4d88973ac3e95e4d156ac) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, [lwm2m\_ctx\_event\_cb\_t](group__lwm2m__api.md#ga38dbaf038426efc75d889c4a0666dac9) event\_cb, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) deregister) |
|  | Stop the LwM2M RD (De-register) Client. |
| int | [lwm2m\_engine\_pause](group__lwm2m__api.md#ga1a4dadb822a8241c5bdf339c21cc57a4) (void) |
|  | Suspend the LwM2M engine Thread. |
| int | [lwm2m\_engine\_resume](group__lwm2m__api.md#ga178fea0407a5e98c4f5d5ad69688853a) (void) |
|  | Resume the LwM2M engine thread. |
| void | [lwm2m\_rd\_client\_update](group__lwm2m__api.md#gab4ec7a22d01259b6ba9d3a7b6681e6f0) (void) |
|  | Trigger a Registration Update of the LwM2M RD Client. |
| char \* | [lwm2m\_path\_log\_buf](group__lwm2m__api.md#ga971c0636c19fe7f0a6e918622560a750) (char \*buf, struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Helper function to print path objects' contents to log. |
| int | [lwm2m\_engine\_send](group__lwm2m__api.md#ga5a0eed7bf3593f698194e5e047b07fa8) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx, char const \*path\_list[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) path\_list\_size, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) confirmation\_request) |
|  |  |
| int | [lwm2m\_send](group__lwm2m__api.md#gae6358ef4b4e3a1e342828ad9c429ff72) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx, const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) path\_list[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) path\_list\_size, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) confirmation\_request) |
|  |  |
| int | [lwm2m\_send\_cb](group__lwm2m__api.md#ga026cc9288d2de17ec557e08b9b987ebc) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx, const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) path\_list[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) path\_list\_size, [lwm2m\_send\_cb\_t](group__lwm2m__api.md#gaf5394884da53edb28fe4afc92bf40e6a) reply\_cb) |
|  |  |
| struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | [lwm2m\_rd\_client\_ctx](group__lwm2m__api.md#ga896caab5473eadff860872023d13b6c0) (void) |
|  |  |
| int | [lwm2m\_engine\_enable\_cache](group__lwm2m__api.md#gaea2d9f740dd6d6152143be0360f19308) (char const \*resource\_path, struct [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md) \*data\_cache, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cache\_len) |
|  |  |
| int | [lwm2m\_enable\_cache](group__lwm2m__api.md#ga6975c5c4825afaccc52741eb54aca4cb) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, struct [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md) \*data\_cache, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cache\_len) |
|  |  |
| int | [lwm2m\_security\_mode](group__lwm2m__api.md#ga6c05640737cfc4da71841a77de128be0) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx) |
|  | Read security mode from selected security object instance. |
| int | [lwm2m\_set\_default\_sockopt](group__lwm2m__api.md#ga956c4fc742a588b7b8b95ce8481f09bf) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx) |
|  | Set default socket options for DTLS connections. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [lwm2m.h](lwm2m_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
