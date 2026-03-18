---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__lwm2m__api.html
original_path: doxygen/html/group__lwm2m__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

LwM2M high-level API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

| Topics | |
| --- | --- |
|  | [LwM2M path helper macros](group__lwm2m__path__helpers.md) |

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
| struct | [lwm2m\_res\_item](structlwm2m__res__item.md) |
|  | LwM2M resource item structure. [More...](structlwm2m__res__item.md#details) |

| Macros | |
| --- | --- |
| #define | [LWM2M\_OBJLNK\_MAX\_ID](#ga34febb0c6fb1c68b0963a6e4dd721763)   USHRT\_MAX |
|  | Maximum value for Objlnk resource fields. |
| #define | [LWM2M\_RES\_DATA\_READ\_ONLY](#ga12c2e0af3d3fc6dd5785e08c0d831a67)   0 |
|  | Resource read-only value bit. |
| #define | [LWM2M\_RES\_DATA\_FLAG\_RO](#ga1bfa5b7d83e3560828a1fb61a4d07355)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([LWM2M\_RES\_DATA\_READ\_ONLY](#ga12c2e0af3d3fc6dd5785e08c0d831a67)) |
|  | Resource read-only flag. |
| #define | [LWM2M\_HAS\_RES\_FLAG](#ga49f4117dfec8cd1abe9f827e235f55b0)(res, f) |
|  | Read resource flags helper macro. |
| #define | [LWM2M\_RD\_CLIENT\_FLAG\_BOOTSTRAP](#ga3a3669237762fa8c23686e5e00b7809f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Run bootstrap procedure in current session. |
| #define | [LWM2M\_MAX\_PATH\_STR\_SIZE](#gab97329844cd411195add5d72ad6aa4b7)   [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("/65535/65535/65535/65535") |
|  | LwM2M path maximum length. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [lwm2m\_socket\_fault\_cb\_t](#gae7bf50f9abf1b82b76ac3e9175e685ac)) (int error) |
|  | Callback function called when a socket error is encountered. |
| typedef void(\* | [lwm2m\_observe\_cb\_t](#gad7bea67e16e1e831e0f949dbf83d5afe)) (enum [lwm2m\_observe\_event](#gac8d63952ec94ca6cfb1dbe12a6c53bfb) event, struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*user\_data) |
|  | Observe callback indicating observer adds and deletes, and notification ACKs and timeouts. |
| typedef void(\* | [lwm2m\_ctx\_event\_cb\_t](#ga38dbaf038426efc75d889c4a0666dac9)) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx, enum [lwm2m\_rd\_client\_event](#gaca90ab8960a4ff01d44735dbc0405862) event) |
|  | Asynchronous RD client event callback. |
| typedef void \*(\* | [lwm2m\_engine\_get\_data\_cb\_t](#ga5e531aade0537eb5e3f5756e9287e384)) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_inst\_id, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*data\_len) |
|  | Asynchronous callback to get a resource buffer and length. |
| typedef int(\* | [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585)) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_inst\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) total\_size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Asynchronous callback when data has been set to a resource buffer. |
| typedef int(\* | [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf)) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id) |
|  | Asynchronous event notification callback. |
| typedef int(\* | [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe)) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*args, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) args\_len) |
|  | Asynchronous execute notification callback. |
| typedef void(\* | [lwm2m\_send\_cb\_t](#gaf5394884da53edb28fe4afc92bf40e6a)) (enum [lwm2m\_send\_status](#ga20848e0942882e8c2cc40ee8a48b7bfd) status) |
|  | Callback returning send status. |

| Enumerations | |
| --- | --- |
| enum | [lwm2m\_observe\_event](#gac8d63952ec94ca6cfb1dbe12a6c53bfb) { [LWM2M\_OBSERVE\_EVENT\_OBSERVER\_ADDED](#ggac8d63952ec94ca6cfb1dbe12a6c53bfba22f4341d713417110d9866b0cbd318e3) , [LWM2M\_OBSERVE\_EVENT\_OBSERVER\_REMOVED](#ggac8d63952ec94ca6cfb1dbe12a6c53bfbae3f4af98b52ee191229c660748c7dd6c) , [LWM2M\_OBSERVE\_EVENT\_NOTIFY\_ACK](#ggac8d63952ec94ca6cfb1dbe12a6c53bfbaab4e1cf0451ba926b90ea21152cac885) , [LWM2M\_OBSERVE\_EVENT\_NOTIFY\_TIMEOUT](#ggac8d63952ec94ca6cfb1dbe12a6c53bfba55494fd6e76f585894e34dc9004fbc9e) } |
|  | Observe callback events. [More...](#gac8d63952ec94ca6cfb1dbe12a6c53bfb) |
| enum | [lwm2m\_socket\_states](#ga7611c1aebb0309ee8340e06dd8ee234d) { [LWM2M\_SOCKET\_STATE\_ONGOING](#gga7611c1aebb0309ee8340e06dd8ee234daa0f06bc70659598b0f51b3ce8094c6ab) , [LWM2M\_SOCKET\_STATE\_ONE\_RESPONSE](#gga7611c1aebb0309ee8340e06dd8ee234da76aa03f71f44096d9413b1f5718d9711) , [LWM2M\_SOCKET\_STATE\_LAST](#gga7611c1aebb0309ee8340e06dd8ee234daed676a6deffe2de7c916bb6eb2906100) , [LWM2M\_SOCKET\_STATE\_NO\_DATA](#gga7611c1aebb0309ee8340e06dd8ee234da2487ae8e93929bf62fd333cd04c5b915) } |
|  | Different traffic states of the LwM2M socket. [More...](#ga7611c1aebb0309ee8340e06dd8ee234d) |
| enum | [lwm2m\_rd\_client\_event](#gaca90ab8960a4ff01d44735dbc0405862) {     [LWM2M\_RD\_CLIENT\_EVENT\_NONE](#ggaca90ab8960a4ff01d44735dbc0405862aca4ebc8d550af02f1891eed1a7b1afcc) , [LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_FAILURE](#ggaca90ab8960a4ff01d44735dbc0405862ac089b900494522de565e36d31ea3b0c4) , [LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_COMPLETE](#ggaca90ab8960a4ff01d44735dbc0405862ac30dd8520e591c8e51c74ce1a53cd524) , [LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_TRANSFER\_COMPLETE](#ggaca90ab8960a4ff01d44735dbc0405862a7c7c3115b6ff16dfa722b6b82c2cd1bc) ,     [LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_FAILURE](#ggaca90ab8960a4ff01d44735dbc0405862ae89498cad338b1dc9cbd3b23838bf0b6) , [LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_COMPLETE](#ggaca90ab8960a4ff01d44735dbc0405862a8994ea8c025cbbd56adcc050a7e86541) , [LWM2M\_RD\_CLIENT\_EVENT\_REG\_TIMEOUT](#ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404) , [LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_COMPLETE](#ggaca90ab8960a4ff01d44735dbc0405862a9f53175c5e935f061a83aa1fcfe9f683) ,     [LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER\_FAILURE](#ggaca90ab8960a4ff01d44735dbc0405862a32552b56152f9a714675fc6bba3b3d5f) , [LWM2M\_RD\_CLIENT\_EVENT\_DISCONNECT](#ggaca90ab8960a4ff01d44735dbc0405862ac6703e7d0809cc9cfcdd1cbd48e2318b) , [LWM2M\_RD\_CLIENT\_EVENT\_QUEUE\_MODE\_RX\_OFF](#ggaca90ab8960a4ff01d44735dbc0405862a7c7853536c452da2f74e9f43a024fcbe) , [LWM2M\_RD\_CLIENT\_EVENT\_ENGINE\_SUSPENDED](#ggaca90ab8960a4ff01d44735dbc0405862afd4eda5dee31b18b1da5414481e33525) ,     [LWM2M\_RD\_CLIENT\_EVENT\_NETWORK\_ERROR](#ggaca90ab8960a4ff01d44735dbc0405862aff939a86c623ab8258c707361b95aef4) , [LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE](#ggaca90ab8960a4ff01d44735dbc0405862ab48772aeed0ead72f3a9289a618af1cd) , [LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER](#ggaca90ab8960a4ff01d44735dbc0405862aac3938a209800a0de0a05b21fab02c13) , [LWM2M\_RD\_CLIENT\_EVENT\_SERVER\_DISABLED](#ggaca90ab8960a4ff01d44735dbc0405862a873a4a3190dc7c24d2518dc8d7268763)   } |
|  | LwM2M RD client events. [More...](#gaca90ab8960a4ff01d44735dbc0405862) |
| enum | [lwm2m\_send\_status](#ga20848e0942882e8c2cc40ee8a48b7bfd) { [LWM2M\_SEND\_STATUS\_SUCCESS](#gga20848e0942882e8c2cc40ee8a48b7bfda127cca7752ab3f00d5a4705f815b14b4) , [LWM2M\_SEND\_STATUS\_FAILURE](#gga20848e0942882e8c2cc40ee8a48b7bfda7a7f1720f39bedba28110fad09939dcd) , [LWM2M\_SEND\_STATUS\_TIMEOUT](#gga20848e0942882e8c2cc40ee8a48b7bfda7c0144cafd4f91a76d229b40df9cb82a) } |
|  | LwM2M send status. [More...](#ga20848e0942882e8c2cc40ee8a48b7bfd) |
| enum | [lwm2m\_security\_mode\_e](#ga11de8078091631cb88b26a9a460097ab) {     [LWM2M\_SECURITY\_PSK](#gga11de8078091631cb88b26a9a460097aba0d4e9d5160e91fc93e062dfb812edb25) = 0 , [LWM2M\_SECURITY\_RAW\_PK](#gga11de8078091631cb88b26a9a460097aba431ac48d7f0fed72ce5ab2c8ea823716) = 1 , [LWM2M\_SECURITY\_CERT](#gga11de8078091631cb88b26a9a460097aba6eef062c9f54bc9698a050c8bb2915ba) = 2 , [LWM2M\_SECURITY\_NOSEC](#gga11de8078091631cb88b26a9a460097abaf6bb17f06d89124076810c132005f8d7) = 3 ,     [LWM2M\_SECURITY\_CERT\_EST](#gga11de8078091631cb88b26a9a460097abaefb45683a68002dab267c3fb2e876824) = 4   } |
|  | Security modes as defined in LwM2M Security object. [More...](#ga11de8078091631cb88b26a9a460097ab) |

| Functions | |
| --- | --- |
| int | [lwm2m\_device\_add\_err](#gabf8726f0438477863423947a7bb77ce2) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) error\_code) |
|  | Register a new error code with LwM2M Device object. |
| void | [lwm2m\_firmware\_set\_write\_cb](#ga6878ea0ebb512b19a4fb0859756f51d0) ([lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) cb) |
|  | Set data callback for firmware block transfer. |
| [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) | [lwm2m\_firmware\_get\_write\_cb](#ga4bf0bbedf5573ac18a11ac4fced11284) (void) |
|  | Get the data callback for firmware block transfer writes. |
| void | [lwm2m\_firmware\_set\_write\_cb\_inst](#gac4e4a819e54344657d70ec479eb6ec8d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) cb) |
|  | Set data callback for firmware block transfer. |
| [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) | [lwm2m\_firmware\_get\_write\_cb\_inst](#gad7334f06c3bdb14485597794a417152d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id) |
|  | Get the data callback for firmware block transfer writes. |
| void | [lwm2m\_firmware\_set\_cancel\_cb](#ga3955dca5cd6d67807ed75e61a4d84d84) ([lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) cb) |
|  | Set callback for firmware update cancel. |
| [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) | [lwm2m\_firmware\_get\_cancel\_cb](#ga9561c1b8407d888f6fbe1e0ceab1c235) (void) |
|  | Get a callback for firmware update cancel. |
| void | [lwm2m\_firmware\_set\_cancel\_cb\_inst](#gaa200b524e505f64247f1e7472c5f36d4) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) cb) |
|  | Set data callback for firmware update cancel. |
| [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) | [lwm2m\_firmware\_get\_cancel\_cb\_inst](#ga6f4b3e08c7e03cff4bf31e2f2999971e) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id) |
|  | Get the callback for firmware update cancel. |
| void | [lwm2m\_firmware\_set\_update\_cb](#ga61eb38e42d9e1b3f467c43a324f2fc65) ([lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set data callback to handle firmware update execute events. |
| [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) | [lwm2m\_firmware\_get\_update\_cb](#ga1e4b8ba1b19ac9025dca3c4799bba84a) (void) |
|  | Get the event callback for firmware update execute events. |
| void | [lwm2m\_firmware\_set\_update\_cb\_inst](#ga31d0f3e40b5e3d608d16a4268b2f1b29) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set data callback to handle firmware update execute events. |
| [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) | [lwm2m\_firmware\_get\_update\_cb\_inst](#ga34995e902b63c4d7d37ebd709d88a72a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id) |
|  | Get the event callback for firmware update execute events. |
| int | [lwm2m\_swmgmt\_set\_activate\_cb](#gac374d0559056ddb9cf43deae932fd128) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set callback to handle software activation requests. |
| int | [lwm2m\_swmgmt\_set\_deactivate\_cb](#ga7a2b93b918257bece819dc44804f27f5) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set callback to handle software deactivation requests. |
| int | [lwm2m\_swmgmt\_set\_install\_package\_cb](#gadfc00060c0b538ed576b5e3edd7dac80) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set callback to handle software install requests. |
| int | [lwm2m\_swmgmt\_set\_delete\_package\_cb](#gacf209563efdc5f3201152088c52d05c3) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set callback to handle software uninstall requests. |
| int | [lwm2m\_swmgmt\_set\_read\_package\_version\_cb](#gab59370ce4fdc94adb4903f22ab1f95b2) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_get\_data\_cb\_t](#ga5e531aade0537eb5e3f5756e9287e384) cb) |
|  | Set callback to read software package. |
| int | [lwm2m\_swmgmt\_set\_write\_package\_cb](#ga293904118f972ae387c8aa85a1028b54) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) cb) |
|  | Set data callback for software management block transfer. |
| int | [lwm2m\_swmgmt\_install\_completed](#ga573e128348fb2f43a33bd09332dd677f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, int error\_code) |
|  | Function to be called when a Software Management object instance completed the Install operation. |
| void | [lwm2m\_event\_log\_set\_read\_log\_data\_cb](#ga950557bce8c510bcc8b0704e7bc4a9dc) ([lwm2m\_engine\_get\_data\_cb\_t](#ga5e531aade0537eb5e3f5756e9287e384) cb) |
|  | Set callback to read log data. |
| int | [lwm2m\_update\_observer\_min\_period](#gadd163806d70713d8349a9db484ba88bf) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s) |
|  | Change an observer's pmin value. |
| int | [lwm2m\_update\_observer\_max\_period](#ga6acccbcd879901574aceab53a21800fc) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s) |
|  | Change an observer's pmax value. |
| int | [lwm2m\_create\_object\_inst](#ga53f5b4c5967e93c7dd224fce8f416265) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Create an LwM2M object instance. |
| int | [lwm2m\_delete\_object\_inst](#gaf921d4bc96090ef8735d90d173feab94) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Delete an LwM2M object instance. |
| void | [lwm2m\_registry\_lock](#ga9a0cdcc9fc6d37462eddeb54e5d1f87a) (void) |
|  | Locks the registry for this thread. |
| void | [lwm2m\_registry\_unlock](#gab09b62982c34887cdd16c30659d3349a) (void) |
|  | Unlocks the registry previously locked by [lwm2m\_registry\_lock()](#ga9a0cdcc9fc6d37462eddeb54e5d1f87a). |
| int | [lwm2m\_set\_opaque](#gaaef33bdf3f48fd91abdb50db4d5460f9) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const char \*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len) |
|  | Set resource (instance) value (opaque buffer). |
| int | [lwm2m\_set\_string](#ga7217f33bf705011d91ba66c86a4d5747) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const char \*data\_ptr) |
|  | Set resource (instance) value (string). |
| int | [lwm2m\_set\_u8](#ga1aa3ff424b7190d0fbd9366626b2685c) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Set resource (instance) value (u8). |
| int | [lwm2m\_set\_u16](#ga1f06bb65571efee18db5d061f95399c3) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value) |
|  | Set resource (instance) value (u16). |
| int | [lwm2m\_set\_u32](#ga9481e570b121404dc1be1ce23d904894) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Set resource (instance) value (u32). |
| int | [lwm2m\_set\_u64](#ga8a751dc8384cc47f9c14d916e20ae19d) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value) |
|  | Set resource (instance) value (u64). |
| int | [lwm2m\_set\_s8](#ga37261a4b9e54eab3d1d855a084d082aa) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) value) |
|  | Set resource (instance) value (s8). |
| int | [lwm2m\_set\_s16](#gad548ffedcb8328b23eb32476a97be6ee) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) value) |
|  | Set resource (instance) value (s16). |
| int | [lwm2m\_set\_s32](#ga327e086959fc5649a5ef14f1f2943e88) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value) |
|  | Set resource (instance) value (s32). |
| int | [lwm2m\_set\_s64](#ga18fcee379640c0dda32d6e3d14827260) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) value) |
|  | Set resource (instance) value (s64). |
| int | [lwm2m\_set\_bool](#ga9ef21d06bef8a97b7666c0aa7fa753b4) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
|  | Set resource (instance) value (bool). |
| int | [lwm2m\_set\_f64](#ga3386d3f2ad8d9713fc2283ed6921c2fc) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const double value) |
|  | Set resource (instance) value (double). |
| int | [lwm2m\_set\_objlnk](#ga04a18bd8a4eeea41a47803c16567d67b) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \*value) |
|  | Set resource (instance) value (Objlnk). |
| int | [lwm2m\_set\_time](#ga7194ad24842e35130d8af7f5104c0844) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) value) |
|  | Set resource (instance) value (Time). |
| int | [lwm2m\_set\_bulk](#ga41b673986e11748b2ded8e1f8f05e0a7) (const struct [lwm2m\_res\_item](structlwm2m__res__item.md) res\_list[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) res\_list\_size) |
|  | Set multiple resource (instance) values. |
| int | [lwm2m\_get\_opaque](#gae245a9a1d9456af7e6283b1074944606) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen) |
|  | Get resource (instance) value (opaque buffer). |
| int | [lwm2m\_get\_string](#ga20fc58b25468bf309175db59d67b820b) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*str, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen) |
|  | Get resource (instance) value (string). |
| int | [lwm2m\_get\_u8](#gac56e804962e529799c771d81ac1fd027) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Get resource (instance) value (u8). |
| int | [lwm2m\_get\_u16](#ga1b96848f96bdab9939bb2619d3e1059b) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value) |
|  | Get resource (instance) value (u16). |
| int | [lwm2m\_get\_u32](#ga0bc84cb39a7a537925ec7d62e54b8b48) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value) |
|  | Get resource (instance) value (u32). |
| int | [lwm2m\_get\_u64](#ga831d229d9a4b983223dff626bbde7a66) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get resource (instance) value (u64). |
| int | [lwm2m\_get\_s8](#ga12817bfbf0a0cbb742568ee974a1c337) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*value) |
|  | Get resource (instance) value (s8). |
| int | [lwm2m\_get\_s16](#ga2426db6720b3f3e15e63022cabae5ece) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*value) |
|  | Get resource (instance) value (s16). |
| int | [lwm2m\_get\_s32](#ga99d7189efa25881dbcddd99e2a795f1b) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value) |
|  | Get resource (instance) value (s32). |
| int | [lwm2m\_get\_s64](#gaaffe06ca9ee5302fb6e26164f250653e) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*value) |
|  | Get resource (instance) value (s64). |
| int | [lwm2m\_get\_bool](#gafdc72844ce0ca417e297d76288155aa4) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*value) |
|  | Get resource (instance) value (bool). |
| int | [lwm2m\_get\_f64](#ga03b72e96a67fcbf85feb5bf0b9df81ce) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, double \*value) |
|  | Get resource (instance) value (double). |
| int | [lwm2m\_get\_objlnk](#ga4de941c36cf678e12da6e05c378a92e5) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \*buf) |
|  | Get resource (instance) value (Objlnk). |
| int | [lwm2m\_get\_time](#ga2e1d41866b5ea35c5aa29bca9bb43812) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*buf) |
|  | Get resource (instance) value (Time). |
| int | [lwm2m\_register\_read\_callback](#gaf33bd6a527b6d399f3d92b666ac77dfb) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_get\_data\_cb\_t](#ga5e531aade0537eb5e3f5756e9287e384) cb) |
|  | Set resource (instance) read callback. |
| int | [lwm2m\_register\_pre\_write\_callback](#ga6f775837e07ba9b0032be8917a593e16) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_get\_data\_cb\_t](#ga5e531aade0537eb5e3f5756e9287e384) cb) |
|  | Set resource (instance) pre-write callback. |
| int | [lwm2m\_register\_validate\_callback](#gad6e5fd4815f409ad59ad631b03199333) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) cb) |
|  | Set resource (instance) validation callback. |
| int | [lwm2m\_register\_post\_write\_callback](#ga3dd8b38e797173dae902404fb5b7a3f4) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) cb) |
|  | Set resource (instance) post-write callback. |
| int | [lwm2m\_register\_exec\_callback](#ga29cc5cdd697e94d7379b1fb178487916) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb) |
|  | Set resource execute event callback. |
| int | [lwm2m\_register\_create\_callback](#ga346d547e02bd53ee83f83b2248449e98) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id, [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) cb) |
|  | Set object instance create event callback. |
| int | [lwm2m\_register\_delete\_callback](#ga92d7e6d81ef674a6c311e1717c6bf373) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id, [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) cb) |
|  | Set object instance delete event callback. |
| int | [lwm2m\_set\_res\_buf](#ga56a2aecd38baedb5dc17258610c4780d) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buffer\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data\_flags) |
|  | Set data buffer for a resource. |
| int | [lwm2m\_set\_res\_data\_len](#ga0f2b115d231bea6622135d72b51f55ca) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len) |
|  | Update data size for a resource. |
| int | [lwm2m\_get\_res\_buf](#gac0b6669d8a19b03eb8b08cbbcdb0c192) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*\*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buffer\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_flags) |
|  | Get data buffer for a resource. |
| int | [lwm2m\_create\_res\_inst](#gac69c40474180fe14c3761185b2db1c0c) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Create a resource instance. |
| int | [lwm2m\_delete\_res\_inst](#gacfeb63db0423e6730ffaa826a87eb262) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Delete a resource instance. |
| int | [lwm2m\_update\_device\_service\_period](#gab45cebf6f0b6b70974367ca453d16aeb) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_ms) |
|  | Update the period of the device service. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [lwm2m\_path\_is\_observed](#ga1065c729d5caa8ca13de7766fce77953) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Check whether a path is observed. |
| int | [lwm2m\_engine\_stop](#ga077e1abd612d31dd33fab52b7d205c39) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx) |
|  | Stop the LwM2M engine. |
| int | [lwm2m\_engine\_start](#ga9f72fbd0163b15c48ea09cf7d511e444) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx) |
|  | Start the LwM2M engine. |
| void | [lwm2m\_acknowledge](#ga919c7d6f418cda99c77fdaf54ae1a7b0) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx) |
|  | Acknowledge the currently processed request with an empty ACK. |
| int | [lwm2m\_rd\_client\_start](#ga9dfd46b8a535b1f28e644dc18f57fd79) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, const char \*ep\_name, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [lwm2m\_ctx\_event\_cb\_t](#ga38dbaf038426efc75d889c4a0666dac9) event\_cb, [lwm2m\_observe\_cb\_t](#gad7bea67e16e1e831e0f949dbf83d5afe) observe\_cb) |
|  | Start the LwM2M RD (Registration / Discovery) Client. |
| int | [lwm2m\_rd\_client\_stop](#gafd87e5d975c4d88973ac3e95e4d156ac) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, [lwm2m\_ctx\_event\_cb\_t](#ga38dbaf038426efc75d889c4a0666dac9) event\_cb, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) deregister) |
|  | Stop the LwM2M RD (De-register) Client. |
| int | [lwm2m\_engine\_pause](#ga1a4dadb822a8241c5bdf339c21cc57a4) (void) |
|  | Suspend the LwM2M engine Thread. |
| int | [lwm2m\_engine\_resume](#ga178fea0407a5e98c4f5d5ad69688853a) (void) |
|  | Resume the LwM2M engine thread. |
| void | [lwm2m\_rd\_client\_update](#gab4ec7a22d01259b6ba9d3a7b6681e6f0) (void) |
|  | Trigger a Registration Update of the LwM2M RD Client. |
| char \* | [lwm2m\_path\_log\_buf](#ga971c0636c19fe7f0a6e918622560a750) (char \*buf, struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path) |
|  | Helper function to print path objects' contents to log. |
| int | [lwm2m\_send\_cb](#ga026cc9288d2de17ec557e08b9b987ebc) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx, const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) path\_list[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) path\_list\_size, [lwm2m\_send\_cb\_t](#gaf5394884da53edb28fe4afc92bf40e6a) reply\_cb) |
|  |  |
| struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | [lwm2m\_rd\_client\_ctx](#ga896caab5473eadff860872023d13b6c0) (void) |
|  |  |
| int | [lwm2m\_enable\_cache](#ga6975c5c4825afaccc52741eb54aca4cb) (const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, struct [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md) \*data\_cache, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cache\_len) |
|  |  |
| int | [lwm2m\_security\_mode](#ga6c05640737cfc4da71841a77de128be0) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx) |
|  | Read security mode from selected security object instance. |
| int | [lwm2m\_set\_default\_sockopt](#ga956c4fc742a588b7b8b95ce8481f09bf) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx) |
|  | Set default socket options for DTLS connections. |

| LwM2M Objects managed by OMA for LwM2M tech specification. | |
| --- | --- |
| Objects in this range have IDs from 0 to 1023. | |
| #define | [LWM2M\_OBJECT\_SECURITY\_ID](#ga785e4a647a2cf93194a249537223ab0f)   0 |
|  | Security object. |
| #define | [LWM2M\_OBJECT\_SERVER\_ID](#gace7b2f0a1f97b6e99c0958a8382ca0d2)   1 |
|  | Server object. |
| #define | [LWM2M\_OBJECT\_ACCESS\_CONTROL\_ID](#gaa8387c8838f952c7c60602e2952c7f55)   2 |
|  | Access Control object. |
| #define | [LWM2M\_OBJECT\_DEVICE\_ID](#ga699f585b320ab5b259d4fb2bda10eb78)   3 |
|  | Device object. |
| #define | [LWM2M\_OBJECT\_CONNECTIVITY\_MONITORING\_ID](#ga73db8616cc7dbbd04267d97a743b8ec0)   4 |
|  | Connectivity Monitoring object. |
| #define | [LWM2M\_OBJECT\_FIRMWARE\_ID](#ga442cc51c7d0807a752ce4affe9221c5b)   5 |
|  | Firmware object. |
| #define | [LWM2M\_OBJECT\_LOCATION\_ID](#ga1046ec68deab3d812d7e5921fb718028)   6 |
|  | Location object. |
| #define | [LWM2M\_OBJECT\_CONNECTIVITY\_STATISTICS\_ID](#gaa6c374c401dd36b6e121ac48c91ca9cf)   7 |
|  | Connectivity Statistics object. |
| #define | [LWM2M\_OBJECT\_SOFTWARE\_MANAGEMENT\_ID](#gac2d140b4a36d6010fe93bca443a658c0)   9 |
|  | Software Management object. |
| #define | [LWM2M\_OBJECT\_PORTFOLIO\_ID](#ga4b4ce912a4554923974461ea3c76007e)   16 |
|  | Portfolio object. |
| #define | [LWM2M\_OBJECT\_BINARYAPPDATACONTAINER\_ID](#ga85eabde1900ef052064d34cf5e3a4afe)   19 |
|  | Binary App Data Container object. |
| #define | [LWM2M\_OBJECT\_EVENT\_LOG\_ID](#ga4f0455fb0271c2fcbb7dadb944431ff0)   20 |
|  | Event Log object. |
| #define | [LWM2M\_OBJECT\_OSCORE\_ID](#gab13a1600a662ed1dbd8845c6d7d4549a)   21 |
|  | OSCORE object. |
| #define | [LWM2M\_OBJECT\_GATEWAY\_ID](#ga3505e9ddcd54afe86e8bd5fbc03fb565)   25 |
|  | Gateway object. |

| LwM2M Objects produced by 3rd party Standards Development | |
| --- | --- |
| Organizations.  Refer to the OMA LightweightM2M (LwM2M) Object and Resource Registry: [http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html](http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html) | |
| #define | [IPSO\_OBJECT\_GENERIC\_SENSOR\_ID](#gaeef485c23d306c93fc0f45dd58766ad9)   3300 |
|  | IPSO Generic Sensor object. |
| #define | [IPSO\_OBJECT\_TEMP\_SENSOR\_ID](#ga3b0c046d93c7bcee9d4da121dd574ff0)   3303 |
|  | IPSO Temperature Sensor object. |
| #define | [IPSO\_OBJECT\_HUMIDITY\_SENSOR\_ID](#ga8075d8b7eb3b4c98f621efef673bb11f)   3304 |
|  | IPSO Humidity Sensor object. |
| #define | [IPSO\_OBJECT\_LIGHT\_CONTROL\_ID](#ga56ebac5260ee467b3763abe49ff3b8ff)   3311 |
|  | IPSO Light Control object. |
| #define | [IPSO\_OBJECT\_ACCELEROMETER\_ID](#ga0b3b9db806e5fe47cc08de34b5fb35fe)   3313 |
|  | IPSO Accelerometer object. |
| #define | [IPSO\_OBJECT\_VOLTAGE\_SENSOR\_ID](#ga270a1b5a576d72099287633b32ce909f)   3316 |
|  | IPSO Voltage Sensor object. |
| #define | [IPSO\_OBJECT\_CURRENT\_SENSOR\_ID](#gae511fd54112829e63c691776750893c2)   3317 |
|  | IPSO Current Sensor object. |
| #define | [IPSO\_OBJECT\_PRESSURE\_ID](#ga752f81e91d0965a50ecfb0679bdea6ba)   3323 |
|  | IPSO Pressure Sensor object. |
| #define | [IPSO\_OBJECT\_BUZZER\_ID](#ga15d664ddbfbf4d5b25dde34a5c650e6b)   3338 |
|  | IPSO Buzzer object. |
| #define | [IPSO\_OBJECT\_TIMER\_ID](#ga6c7bd5880fa22050748c2cb01981cbcb)   3340 |
|  | IPSO Timer object. |
| #define | [IPSO\_OBJECT\_ONOFF\_SWITCH\_ID](#ga776a6a5e1eab3a8de0a39382f94b663a)   3342 |
|  | IPSO On/Off Switch object. |
| #define | [IPSO\_OBJECT\_PUSH\_BUTTON\_ID](#ga6e3119bc8f0b9143ab384e82a5bccf7c)   3347 |
|  | IPSO Push Button object. |
| #define | [UCIFI\_OBJECT\_BATTERY\_ID](#gacdd09a26ce52f36c644a89a8b89f7d32)   3411 |
|  | uCIFI Battery object |
| #define | [IPSO\_OBJECT\_FILLING\_LEVEL\_SENSOR\_ID](#ga21f6bc6255f5f5ed28881fa797d026ca)   3435 |
|  | IPSO Filling Level Sensor object. |

| Power source types used for the "Available Power Sources" resource of | |
| --- | --- |
| the LwM2M Device object (3/0/6). | |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_DC\_POWER](#gae154ca2e54ec7759dd43f2a7a275077e)   0 |
|  | DC power. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_INT](#ga04ca8ac536eed7d411c1b1ea2b2a59ac)   1 |
|  | Internal battery. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_EXT](#gaf12052f903a688712928d036b782f621)   2 |
|  | External battery. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_FUEL\_CELL](#ga10c4633c97881ca7d87c748aaeec68c9)   3 |
|  | Fuel cell. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_PWR\_OVER\_ETH](#ga72352523996e61ea93caff0bb80c42ba)   4 |
|  | Power over Ethernet. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_USB](#ga4877877be75d3dd3c8f600b438b7ea8e)   5 |
|  | USB. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_AC\_POWER](#ga97b9d38ec402478f10642f1f83a4f88a)   6 |
|  | AC (mains) power. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_SOLAR](#gaa41ec1d2ca43e1385cfb11204aff729d)   7 |
|  | Solar. |
| #define | [LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_MAX](#gae7a580aac1804abbcf3feb57a5a30a02)   8 |
|  | Max value for Available Power Source type. |

| Error codes used for the "Error Code" resource of the LwM2M Device | |
| --- | --- |
| object.  An LwM2M client can register one of the following error codes via the [lwm2m\_device\_add\_err()](#gabf8726f0438477863423947a7bb77ce2) function. | |
| #define | [LWM2M\_DEVICE\_ERROR\_NONE](#gad54ec75eb2843d5eed199ddedca6ef4f)   0 |
|  | No error. |
| #define | [LWM2M\_DEVICE\_ERROR\_LOW\_POWER](#ga53a9ee1ae09dd32a8dc2df6018798f9f)   1 |
|  | Low battery power. |
| #define | [LWM2M\_DEVICE\_ERROR\_EXT\_POWER\_SUPPLY\_OFF](#ga33152ea4ef497b02a12d1218d470a5a6)   2 |
|  | External power supply off. |
| #define | [LWM2M\_DEVICE\_ERROR\_GPS\_FAILURE](#ga3c1b7693167ff517c5cbd7bbdbfd1ea0)   3 |
|  | GPS module failure. |
| #define | [LWM2M\_DEVICE\_ERROR\_LOW\_SIGNAL\_STRENGTH](#ga78048382d8bc85bbabbff58f0a9860f2)   4 |
|  | Low received signal strength. |
| #define | [LWM2M\_DEVICE\_ERROR\_OUT\_OF\_MEMORY](#ga94ce0177c066dd43ef660b85afc83485)   5 |
|  | Out of memory. |
| #define | [LWM2M\_DEVICE\_ERROR\_SMS\_FAILURE](#gabcb39cd3757ea60859984f6ad0df9e31)   6 |
|  | SMS failure. |
| #define | [LWM2M\_DEVICE\_ERROR\_NETWORK\_FAILURE](#ga2110d71a0c58087ff877e66b7500ba66)   7 |
|  | IP Connectivity failure. |
| #define | [LWM2M\_DEVICE\_ERROR\_PERIPHERAL\_FAILURE](#ga77e6352eace8116576c880bf7e416ba3)   8 |
|  | Peripheral malfunction. |

| Battery status codes used for the "Battery Status" resource (3/0/20) | |
| --- | --- |
| of the LwM2M Device object.  As the battery status changes, an LwM2M client can set one of the following codes via: lwm2m\_set\_u8("3/0/20", [battery status]) | |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_NORMAL](#ga4329c971f95f1c345381d1c864a9f334)   0 |
|  | The battery is operating normally and not on power. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGING](#gaf19da3a566782aeebebfb6ff110a9152)   1 |
|  | The battery is currently charging. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGE\_COMP](#ga5f7e88b52d8e6029467a2ed10585e6d4)   2 |
|  | The battery is fully charged and the charger is still connected. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_DAMAGED](#gaa3f81df5e4d45838922eb20a15ee3153)   3 |
|  | The battery has some problem. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_LOW](#ga578f6446ec1b70d2a32917abf1f5aad7)   4 |
|  | The battery is low on charge. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_NOT\_INST](#gacc3dfc99fc2cd9ef7048b1a0a0fd55c8)   5 |
|  | The battery is not installed. |
| #define | [LWM2M\_DEVICE\_BATTERY\_STATUS\_UNKNOWN](#ga174e118b07982b87c6c083236b79c3b7)   6 |
|  | The battery information is not available. |

| LWM2M Firmware Update object states | |
| --- | --- |
| An LwM2M client or the LwM2M Firmware Update object use the following codes to represent the LwM2M Firmware Update state (5/0/3). | |
| #define | [STATE\_IDLE](#gaafff27c7165f059a969fe60fee51f683)   0 |
|  | Idle. |
| #define | [STATE\_DOWNLOADING](#gaeb34e88a0da4ac1274ae6b2cef010086)   1 |
|  | Downloading. |
| #define | [STATE\_DOWNLOADED](#ga009085120be71a28c1f6ebdaf7503365)   2 |
|  | Downloaded. |
| #define | [STATE\_UPDATING](#gaac1dab8d1ac28bf13faeee39d1df47c5)   3 |
|  | Updating. |

| LWM2M Firmware Update object result codes | |
| --- | --- |
| After processing a firmware update, the client sets the result via one of the following codes via lwm2m\_set\_u8("5/0/5", [result code]) | |
| #define | [RESULT\_DEFAULT](#ga391b47507468bbc1005903a56f80b1ea)   0 |
|  | Initial value. |
| #define | [RESULT\_SUCCESS](#ga7cc1753a05a0821f6c70dd2bccfbab5c)   1 |
|  | Firmware updated successfully. |
| #define | [RESULT\_NO\_STORAGE](#ga829f7bc83b67dcf16ea4775addd87343)   2 |
|  | Not enough flash memory for the new firmware package. |
| #define | [RESULT\_OUT\_OF\_MEM](#gab5446111a8969aa2c66dae49f04c93cf)   3 |
|  | Out of RAM during downloading process. |
| #define | [RESULT\_CONNECTION\_LOST](#ga0655ba8c402d8b6c8bbd84fb36447bd4)   4 |
|  | Connection lost during downloading process. |
| #define | [RESULT\_INTEGRITY\_FAILED](#gadfd0ac7b6a3fededa2b4471dfe52d3d2)   5 |
|  | Integrity check failure for new downloaded package. |
| #define | [RESULT\_UNSUP\_FW](#gab06dbfdac0c95f8100908a1177f3a62a)   6 |
|  | Unsupported package type. |
| #define | [RESULT\_INVALID\_URI](#ga268204053d7e23737283523224699979)   7 |
|  | Invalid URI. |
| #define | [RESULT\_UPDATE\_FAILED](#ga2dfdd95c2c03ccca25d855b6d6f96ed3)   8 |
|  | Firmware update failed. |
| #define | [RESULT\_UNSUP\_PROTO](#gade3da37a44ee40292ec6344403db8d8d)   9 |
|  | Unsupported protocol. |

## Detailed Description

Since
:   1.9

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga0b3b9db806e5fe47cc08de34b5fb35fe)IPSO\_OBJECT\_ACCELEROMETER\_ID

| #define IPSO\_OBJECT\_ACCELEROMETER\_ID   3313 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Accelerometer object.

## [◆ ](#ga15d664ddbfbf4d5b25dde34a5c650e6b)IPSO\_OBJECT\_BUZZER\_ID

| #define IPSO\_OBJECT\_BUZZER\_ID   3338 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Buzzer object.

## [◆ ](#gae511fd54112829e63c691776750893c2)IPSO\_OBJECT\_CURRENT\_SENSOR\_ID

| #define IPSO\_OBJECT\_CURRENT\_SENSOR\_ID   3317 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Current Sensor object.

## [◆ ](#ga21f6bc6255f5f5ed28881fa797d026ca)IPSO\_OBJECT\_FILLING\_LEVEL\_SENSOR\_ID

| #define IPSO\_OBJECT\_FILLING\_LEVEL\_SENSOR\_ID   3435 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Filling Level Sensor object.

## [◆ ](#gaeef485c23d306c93fc0f45dd58766ad9)IPSO\_OBJECT\_GENERIC\_SENSOR\_ID

| #define IPSO\_OBJECT\_GENERIC\_SENSOR\_ID   3300 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Generic Sensor object.

## [◆ ](#ga8075d8b7eb3b4c98f621efef673bb11f)IPSO\_OBJECT\_HUMIDITY\_SENSOR\_ID

| #define IPSO\_OBJECT\_HUMIDITY\_SENSOR\_ID   3304 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Humidity Sensor object.

## [◆ ](#ga56ebac5260ee467b3763abe49ff3b8ff)IPSO\_OBJECT\_LIGHT\_CONTROL\_ID

| #define IPSO\_OBJECT\_LIGHT\_CONTROL\_ID   3311 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Light Control object.

## [◆ ](#ga776a6a5e1eab3a8de0a39382f94b663a)IPSO\_OBJECT\_ONOFF\_SWITCH\_ID

| #define IPSO\_OBJECT\_ONOFF\_SWITCH\_ID   3342 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO On/Off Switch object.

## [◆ ](#ga752f81e91d0965a50ecfb0679bdea6ba)IPSO\_OBJECT\_PRESSURE\_ID

| #define IPSO\_OBJECT\_PRESSURE\_ID   3323 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Pressure Sensor object.

## [◆ ](#ga6e3119bc8f0b9143ab384e82a5bccf7c)IPSO\_OBJECT\_PUSH\_BUTTON\_ID

| #define IPSO\_OBJECT\_PUSH\_BUTTON\_ID   3347 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Push Button object.

## [◆ ](#ga3b0c046d93c7bcee9d4da121dd574ff0)IPSO\_OBJECT\_TEMP\_SENSOR\_ID

| #define IPSO\_OBJECT\_TEMP\_SENSOR\_ID   3303 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Temperature Sensor object.

## [◆ ](#ga6c7bd5880fa22050748c2cb01981cbcb)IPSO\_OBJECT\_TIMER\_ID

| #define IPSO\_OBJECT\_TIMER\_ID   3340 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Timer object.

## [◆ ](#ga270a1b5a576d72099287633b32ce909f)IPSO\_OBJECT\_VOLTAGE\_SENSOR\_ID

| #define IPSO\_OBJECT\_VOLTAGE\_SENSOR\_ID   3316 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IPSO Voltage Sensor object.

## [◆ ](#ga5f7e88b52d8e6029467a2ed10585e6d4)LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGE\_COMP

| #define LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGE\_COMP   2 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

The battery is fully charged and the charger is still connected.

## [◆ ](#gaf19da3a566782aeebebfb6ff110a9152)LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGING

| #define LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGING   1 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

The battery is currently charging.

## [◆ ](#gaa3f81df5e4d45838922eb20a15ee3153)LWM2M\_DEVICE\_BATTERY\_STATUS\_DAMAGED

| #define LWM2M\_DEVICE\_BATTERY\_STATUS\_DAMAGED   3 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

The battery has some problem.

## [◆ ](#ga578f6446ec1b70d2a32917abf1f5aad7)LWM2M\_DEVICE\_BATTERY\_STATUS\_LOW

| #define LWM2M\_DEVICE\_BATTERY\_STATUS\_LOW   4 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

The battery is low on charge.

## [◆ ](#ga4329c971f95f1c345381d1c864a9f334)LWM2M\_DEVICE\_BATTERY\_STATUS\_NORMAL

| #define LWM2M\_DEVICE\_BATTERY\_STATUS\_NORMAL   0 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

The battery is operating normally and not on power.

## [◆ ](#gacc3dfc99fc2cd9ef7048b1a0a0fd55c8)LWM2M\_DEVICE\_BATTERY\_STATUS\_NOT\_INST

| #define LWM2M\_DEVICE\_BATTERY\_STATUS\_NOT\_INST   5 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

The battery is not installed.

## [◆ ](#ga174e118b07982b87c6c083236b79c3b7)LWM2M\_DEVICE\_BATTERY\_STATUS\_UNKNOWN

| #define LWM2M\_DEVICE\_BATTERY\_STATUS\_UNKNOWN   6 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

The battery information is not available.

## [◆ ](#ga33152ea4ef497b02a12d1218d470a5a6)LWM2M\_DEVICE\_ERROR\_EXT\_POWER\_SUPPLY\_OFF

| #define LWM2M\_DEVICE\_ERROR\_EXT\_POWER\_SUPPLY\_OFF   2 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

External power supply off.

## [◆ ](#ga3c1b7693167ff517c5cbd7bbdbfd1ea0)LWM2M\_DEVICE\_ERROR\_GPS\_FAILURE

| #define LWM2M\_DEVICE\_ERROR\_GPS\_FAILURE   3 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

GPS module failure.

## [◆ ](#ga53a9ee1ae09dd32a8dc2df6018798f9f)LWM2M\_DEVICE\_ERROR\_LOW\_POWER

| #define LWM2M\_DEVICE\_ERROR\_LOW\_POWER   1 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Low battery power.

## [◆ ](#ga78048382d8bc85bbabbff58f0a9860f2)LWM2M\_DEVICE\_ERROR\_LOW\_SIGNAL\_STRENGTH

| #define LWM2M\_DEVICE\_ERROR\_LOW\_SIGNAL\_STRENGTH   4 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Low received signal strength.

## [◆ ](#ga2110d71a0c58087ff877e66b7500ba66)LWM2M\_DEVICE\_ERROR\_NETWORK\_FAILURE

| #define LWM2M\_DEVICE\_ERROR\_NETWORK\_FAILURE   7 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

IP Connectivity failure.

## [◆ ](#gad54ec75eb2843d5eed199ddedca6ef4f)LWM2M\_DEVICE\_ERROR\_NONE

| #define LWM2M\_DEVICE\_ERROR\_NONE   0 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

No error.

## [◆ ](#ga94ce0177c066dd43ef660b85afc83485)LWM2M\_DEVICE\_ERROR\_OUT\_OF\_MEMORY

| #define LWM2M\_DEVICE\_ERROR\_OUT\_OF\_MEMORY   5 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Out of memory.

## [◆ ](#ga77e6352eace8116576c880bf7e416ba3)LWM2M\_DEVICE\_ERROR\_PERIPHERAL\_FAILURE

| #define LWM2M\_DEVICE\_ERROR\_PERIPHERAL\_FAILURE   8 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Peripheral malfunction.

## [◆ ](#gabcb39cd3757ea60859984f6ad0df9e31)LWM2M\_DEVICE\_ERROR\_SMS\_FAILURE

| #define LWM2M\_DEVICE\_ERROR\_SMS\_FAILURE   6 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

SMS failure.

## [◆ ](#ga97b9d38ec402478f10642f1f83a4f88a)LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_AC\_POWER

| #define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_AC\_POWER   6 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

AC (mains) power.

## [◆ ](#gaf12052f903a688712928d036b782f621)LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_EXT

| #define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_EXT   2 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

External battery.

## [◆ ](#ga04ca8ac536eed7d411c1b1ea2b2a59ac)LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_INT

| #define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_INT   1 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Internal battery.

## [◆ ](#gae154ca2e54ec7759dd43f2a7a275077e)LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_DC\_POWER

| #define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_DC\_POWER   0 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

DC power.

## [◆ ](#ga10c4633c97881ca7d87c748aaeec68c9)LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_FUEL\_CELL

| #define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_FUEL\_CELL   3 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Fuel cell.

## [◆ ](#gae7a580aac1804abbcf3feb57a5a30a02)LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_MAX

| #define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_MAX   8 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Max value for Available Power Source type.

## [◆ ](#ga72352523996e61ea93caff0bb80c42ba)LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_PWR\_OVER\_ETH

| #define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_PWR\_OVER\_ETH   4 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Power over Ethernet.

## [◆ ](#gaa41ec1d2ca43e1385cfb11204aff729d)LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_SOLAR

| #define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_SOLAR   7 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Solar.

## [◆ ](#ga4877877be75d3dd3c8f600b438b7ea8e)LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_USB

| #define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_USB   5 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

USB.

## [◆ ](#ga49f4117dfec8cd1abe9f827e235f55b0)LWM2M\_HAS\_RES\_FLAG

| #define LWM2M\_HAS\_RES\_FLAG | ( |  | *res*, |
| --- | --- | --- | --- |
|  |  |  | *f* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

**Value:**

((res->data\_flags & f) == f)

Read resource flags helper macro.

## [◆ ](#gab97329844cd411195add5d72ad6aa4b7)LWM2M\_MAX\_PATH\_STR\_SIZE

| #define LWM2M\_MAX\_PATH\_STR\_SIZE   [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("/65535/65535/65535/65535") |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

LwM2M path maximum length.

## [◆ ](#gaa8387c8838f952c7c60602e2952c7f55)LWM2M\_OBJECT\_ACCESS\_CONTROL\_ID

| #define LWM2M\_OBJECT\_ACCESS\_CONTROL\_ID   2 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Access Control object.

## [◆ ](#ga85eabde1900ef052064d34cf5e3a4afe)LWM2M\_OBJECT\_BINARYAPPDATACONTAINER\_ID

| #define LWM2M\_OBJECT\_BINARYAPPDATACONTAINER\_ID   19 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Binary App Data Container object.

## [◆ ](#ga73db8616cc7dbbd04267d97a743b8ec0)LWM2M\_OBJECT\_CONNECTIVITY\_MONITORING\_ID

| #define LWM2M\_OBJECT\_CONNECTIVITY\_MONITORING\_ID   4 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Connectivity Monitoring object.

## [◆ ](#gaa6c374c401dd36b6e121ac48c91ca9cf)LWM2M\_OBJECT\_CONNECTIVITY\_STATISTICS\_ID

| #define LWM2M\_OBJECT\_CONNECTIVITY\_STATISTICS\_ID   7 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Connectivity Statistics object.

## [◆ ](#ga699f585b320ab5b259d4fb2bda10eb78)LWM2M\_OBJECT\_DEVICE\_ID

| #define LWM2M\_OBJECT\_DEVICE\_ID   3 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Device object.

## [◆ ](#ga4f0455fb0271c2fcbb7dadb944431ff0)LWM2M\_OBJECT\_EVENT\_LOG\_ID

| #define LWM2M\_OBJECT\_EVENT\_LOG\_ID   20 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Event Log object.

## [◆ ](#ga442cc51c7d0807a752ce4affe9221c5b)LWM2M\_OBJECT\_FIRMWARE\_ID

| #define LWM2M\_OBJECT\_FIRMWARE\_ID   5 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Firmware object.

## [◆ ](#ga3505e9ddcd54afe86e8bd5fbc03fb565)LWM2M\_OBJECT\_GATEWAY\_ID

| #define LWM2M\_OBJECT\_GATEWAY\_ID   25 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Gateway object.

## [◆ ](#ga1046ec68deab3d812d7e5921fb718028)LWM2M\_OBJECT\_LOCATION\_ID

| #define LWM2M\_OBJECT\_LOCATION\_ID   6 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Location object.

## [◆ ](#gab13a1600a662ed1dbd8845c6d7d4549a)LWM2M\_OBJECT\_OSCORE\_ID

| #define LWM2M\_OBJECT\_OSCORE\_ID   21 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

OSCORE object.

## [◆ ](#ga4b4ce912a4554923974461ea3c76007e)LWM2M\_OBJECT\_PORTFOLIO\_ID

| #define LWM2M\_OBJECT\_PORTFOLIO\_ID   16 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Portfolio object.

## [◆ ](#ga785e4a647a2cf93194a249537223ab0f)LWM2M\_OBJECT\_SECURITY\_ID

| #define LWM2M\_OBJECT\_SECURITY\_ID   0 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Security object.

## [◆ ](#gace7b2f0a1f97b6e99c0958a8382ca0d2)LWM2M\_OBJECT\_SERVER\_ID

| #define LWM2M\_OBJECT\_SERVER\_ID   1 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Server object.

## [◆ ](#gac2d140b4a36d6010fe93bca443a658c0)LWM2M\_OBJECT\_SOFTWARE\_MANAGEMENT\_ID

| #define LWM2M\_OBJECT\_SOFTWARE\_MANAGEMENT\_ID   9 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Software Management object.

## [◆ ](#ga34febb0c6fb1c68b0963a6e4dd721763)LWM2M\_OBJLNK\_MAX\_ID

| #define LWM2M\_OBJLNK\_MAX\_ID   USHRT\_MAX |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Maximum value for Objlnk resource fields.

## [◆ ](#ga3a3669237762fa8c23686e5e00b7809f)LWM2M\_RD\_CLIENT\_FLAG\_BOOTSTRAP

| #define LWM2M\_RD\_CLIENT\_FLAG\_BOOTSTRAP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Run bootstrap procedure in current session.

## [◆ ](#ga1bfa5b7d83e3560828a1fb61a4d07355)LWM2M\_RES\_DATA\_FLAG\_RO

| #define LWM2M\_RES\_DATA\_FLAG\_RO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([LWM2M\_RES\_DATA\_READ\_ONLY](#ga12c2e0af3d3fc6dd5785e08c0d831a67)) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Resource read-only flag.

## [◆ ](#ga12c2e0af3d3fc6dd5785e08c0d831a67)LWM2M\_RES\_DATA\_READ\_ONLY

| #define LWM2M\_RES\_DATA\_READ\_ONLY   0 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Resource read-only value bit.

## [◆ ](#ga0655ba8c402d8b6c8bbd84fb36447bd4)RESULT\_CONNECTION\_LOST

| #define RESULT\_CONNECTION\_LOST   4 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Connection lost during downloading process.

## [◆ ](#ga391b47507468bbc1005903a56f80b1ea)RESULT\_DEFAULT

| #define RESULT\_DEFAULT   0 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Initial value.

## [◆ ](#gadfd0ac7b6a3fededa2b4471dfe52d3d2)RESULT\_INTEGRITY\_FAILED

| #define RESULT\_INTEGRITY\_FAILED   5 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Integrity check failure for new downloaded package.

## [◆ ](#ga268204053d7e23737283523224699979)RESULT\_INVALID\_URI

| #define RESULT\_INVALID\_URI   7 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Invalid URI.

## [◆ ](#ga829f7bc83b67dcf16ea4775addd87343)RESULT\_NO\_STORAGE

| #define RESULT\_NO\_STORAGE   2 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Not enough flash memory for the new firmware package.

## [◆ ](#gab5446111a8969aa2c66dae49f04c93cf)RESULT\_OUT\_OF\_MEM

| #define RESULT\_OUT\_OF\_MEM   3 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Out of RAM during downloading process.

## [◆ ](#ga7cc1753a05a0821f6c70dd2bccfbab5c)RESULT\_SUCCESS

| #define RESULT\_SUCCESS   1 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Firmware updated successfully.

## [◆ ](#gab06dbfdac0c95f8100908a1177f3a62a)RESULT\_UNSUP\_FW

| #define RESULT\_UNSUP\_FW   6 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Unsupported package type.

## [◆ ](#gade3da37a44ee40292ec6344403db8d8d)RESULT\_UNSUP\_PROTO

| #define RESULT\_UNSUP\_PROTO   9 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Unsupported protocol.

## [◆ ](#ga2dfdd95c2c03ccca25d855b6d6f96ed3)RESULT\_UPDATE\_FAILED

| #define RESULT\_UPDATE\_FAILED   8 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Firmware update failed.

## [◆ ](#ga009085120be71a28c1f6ebdaf7503365)STATE\_DOWNLOADED

| #define STATE\_DOWNLOADED   2 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Downloaded.

The whole data sequence has been downloaded.

## [◆ ](#gaeb34e88a0da4ac1274ae6b2cef010086)STATE\_DOWNLOADING

| #define STATE\_DOWNLOADING   1 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Downloading.

The data sequence is being downloaded.

## [◆ ](#gaafff27c7165f059a969fe60fee51f683)STATE\_IDLE

| #define STATE\_IDLE   0 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Idle.

Before downloading or after successful updating.

## [◆ ](#gaac1dab8d1ac28bf13faeee39d1df47c5)STATE\_UPDATING

| #define STATE\_UPDATING   3 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Updating.

The device is being updated.

## [◆ ](#gacdd09a26ce52f36c644a89a8b89f7d32)UCIFI\_OBJECT\_BATTERY\_ID

| #define UCIFI\_OBJECT\_BATTERY\_ID   3411 |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

uCIFI Battery object

## Typedef Documentation

## [◆ ](#ga38dbaf038426efc75d889c4a0666dac9)lwm2m\_ctx\_event\_cb\_t

| typedef void(\* lwm2m\_ctx\_event\_cb\_t) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx, enum [lwm2m\_rd\_client\_event](#gaca90ab8960a4ff01d44735dbc0405862) event) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Asynchronous RD client event callback.

Parameters
:   | [in] | ctx | LwM2M context generating the event |
    | --- | --- | --- |
    | [in] | event | LwM2M RD client event code |

## [◆ ](#gaeb32bcd4981b4c7bd891f99668ebc0fe)lwm2m\_engine\_execute\_cb\_t

| typedef int(\* lwm2m\_engine\_execute\_cb\_t) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*args, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) args\_len) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Asynchronous execute notification callback.

Resource executes trigger a callback of this type.

Register a function of this type via: [lwm2m\_register\_exec\_callback()](#ga29cc5cdd697e94d7379b1fb178487916)

Parameters
:   | [in] | obj\_inst\_id | Object instance ID generating the callback. |
    | --- | --- | --- |
    | [in] | args | Pointer to execute arguments payload. (This can be NULL if no arguments are provided) |
    | [in] | args\_len | Length of argument payload in bytes. |

Returns
:   Callback returns a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure or 0 for success.

## [◆ ](#ga5e531aade0537eb5e3f5756e9287e384)lwm2m\_engine\_get\_data\_cb\_t

| typedef void \*(\* lwm2m\_engine\_get\_data\_cb\_t) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_inst\_id, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*data\_len) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Asynchronous callback to get a resource buffer and length.

Prior to accessing the data buffer of a resource, the engine can use this callback to get the buffer pointer and length instead of using the resource's data buffer.

The client or LwM2M objects can register a function of this type via: [lwm2m\_register\_read\_callback()](#gaf33bd6a527b6d399f3d92b666ac77dfb) [lwm2m\_register\_pre\_write\_callback()](#ga6f775837e07ba9b0032be8917a593e16)

Parameters
:   | [in] | obj\_inst\_id | Object instance ID generating the callback. |
    | --- | --- | --- |
    | [in] | res\_id | Resource ID generating the callback. |
    | [in] | res\_inst\_id | Resource instance ID generating the callback (typically 0 for non-multi instance resources). |
    | [out] | data\_len | Length of the data buffer. |

Returns
:   Callback returns a pointer to the data buffer or NULL for failure.

## [◆ ](#ga3afac013b0cf731f9c86dc3791131585)lwm2m\_engine\_set\_data\_cb\_t

| typedef int(\* lwm2m\_engine\_set\_data\_cb\_t) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_inst\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) total\_size, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Asynchronous callback when data has been set to a resource buffer.

After changing the data of a resource buffer, the LwM2M engine can make use of this callback to pass the data back to the client or LwM2M objects.

On a block-wise transfers the handler is called multiple times with the data blocks and increasing offset. The last block has the last\_block flag set to true. Beginning of the block transfer has the offset set to 0.

A function of this type can be registered via: [lwm2m\_register\_validate\_callback()](#gad6e5fd4815f409ad59ad631b03199333) [lwm2m\_register\_post\_write\_callback()](#ga3dd8b38e797173dae902404fb5b7a3f4)

Parameters
:   | [in] | obj\_inst\_id | Object instance ID generating the callback. |
    | --- | --- | --- |
    | [in] | res\_id | Resource ID generating the callback. |
    | [in] | res\_inst\_id | Resource instance ID generating the callback (typically 0 for non-multi instance resources). |
    | [in] | data | Pointer to data. |
    | [in] | data\_len | Length of the data. |
    | [in] | last\_block | Flag used during block transfer to indicate the last block of data. For non-block transfers this is always false. |
    | [in] | total\_size | Expected total size of data for a block transfer. For non-block transfers this is 0. |
    | [in] | offset | Offset of the data block. For non-block transfers this is always 0. |

Returns
:   Callback returns a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure or 0 for success.

## [◆ ](#gabcbca483b310e0c4cd68aef2d9cda0bf)lwm2m\_engine\_user\_cb\_t

| typedef int(\* lwm2m\_engine\_user\_cb\_t) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Asynchronous event notification callback.

Various object instance and resource-based events in the LwM2M engine can trigger a callback of this function type: object instance create, and object instance delete.

Register a function of this type via: [lwm2m\_register\_create\_callback()](#ga346d547e02bd53ee83f83b2248449e98) [lwm2m\_register\_delete\_callback()](#ga92d7e6d81ef674a6c311e1717c6bf373)

Parameters
:   | [in] | obj\_inst\_id | Object instance ID generating the callback. |
    | --- | --- | --- |

Returns
:   Callback returns a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure or 0 for success.

## [◆ ](#gad7bea67e16e1e831e0f949dbf83d5afe)lwm2m\_observe\_cb\_t

| typedef void(\* lwm2m\_observe\_cb\_t) (enum [lwm2m\_observe\_event](#gac8d63952ec94ca6cfb1dbe12a6c53bfb) event, struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*user\_data) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Observe callback indicating observer adds and deletes, and notification ACKs and timeouts.

Parameters
:   | [in] | event | Observer add/delete or notification ack/timeout |
    | --- | --- | --- |
    | [in] | path | LwM2M path |
    | [in] | user\_data | Pointer to user\_data buffer, as provided in send\_traceable\_notification(). Used to determine for which data the ACKed/timed out notification was. |

## [◆ ](#gaf5394884da53edb28fe4afc92bf40e6a)lwm2m\_send\_cb\_t

| typedef void(\* lwm2m\_send\_cb\_t) (enum [lwm2m\_send\_status](#ga20848e0942882e8c2cc40ee8a48b7bfd) status) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Callback returning send status.

## [◆ ](#gae7bf50f9abf1b82b76ac3e9175e685ac)lwm2m\_socket\_fault\_cb\_t

| typedef void(\* lwm2m\_socket\_fault\_cb\_t) (int error) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Callback function called when a socket error is encountered.

Parameters
:   | error | Error code |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#gac8d63952ec94ca6cfb1dbe12a6c53bfb)lwm2m\_observe\_event

| enum [lwm2m\_observe\_event](#gac8d63952ec94ca6cfb1dbe12a6c53bfb) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Observe callback events.

| Enumerator | |
| --- | --- |
| LWM2M\_OBSERVE\_EVENT\_OBSERVER\_ADDED | Observer added. |
| LWM2M\_OBSERVE\_EVENT\_OBSERVER\_REMOVED | Observer removed. |
| LWM2M\_OBSERVE\_EVENT\_NOTIFY\_ACK | Notification ACKed. |
| LWM2M\_OBSERVE\_EVENT\_NOTIFY\_TIMEOUT | Notification timed out. |

## [◆ ](#gaca90ab8960a4ff01d44735dbc0405862)lwm2m\_rd\_client\_event

| enum [lwm2m\_rd\_client\_event](#gaca90ab8960a4ff01d44735dbc0405862) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

LwM2M RD client events.

LwM2M client events are passed back to the event\_cb function in [lwm2m\_rd\_client\_start()](#ga9dfd46b8a535b1f28e644dc18f57fd79)

| Enumerator | |
| --- | --- |
| LWM2M\_RD\_CLIENT\_EVENT\_NONE | Invalid event. |
| LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_FAILURE | Bootstrap registration failure. |
| LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_COMPLETE | Bootstrap registration complete. |
| LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_TRANSFER\_COMPLETE | Bootstrap transfer complete. |
| LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_FAILURE | Registration failure. |
| LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_COMPLETE | Registration complete. |
| LWM2M\_RD\_CLIENT\_EVENT\_REG\_TIMEOUT | Registration timeout. |
| LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_COMPLETE | Registration update complete. |
| LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER\_FAILURE | De-registration failure. |
| LWM2M\_RD\_CLIENT\_EVENT\_DISCONNECT | Disconnected. |
| LWM2M\_RD\_CLIENT\_EVENT\_QUEUE\_MODE\_RX\_OFF | Queue mode RX off. |
| LWM2M\_RD\_CLIENT\_EVENT\_ENGINE\_SUSPENDED | Engine suspended. |
| LWM2M\_RD\_CLIENT\_EVENT\_NETWORK\_ERROR | Network error. |
| LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE | Registration update. |
| LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER | De-register. |
| LWM2M\_RD\_CLIENT\_EVENT\_SERVER\_DISABLED | Server disabled. |

## [◆ ](#ga11de8078091631cb88b26a9a460097ab)lwm2m\_security\_mode\_e

| enum [lwm2m\_security\_mode\_e](#ga11de8078091631cb88b26a9a460097ab) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Security modes as defined in LwM2M Security object.

| Enumerator | |
| --- | --- |
| LWM2M\_SECURITY\_PSK | Pre-Shared Key mode. |
| LWM2M\_SECURITY\_RAW\_PK | Raw Public Key mode. |
| LWM2M\_SECURITY\_CERT | Certificate mode. |
| LWM2M\_SECURITY\_NOSEC | NoSec mode. |
| LWM2M\_SECURITY\_CERT\_EST | Certificate mode with EST. |

## [◆ ](#ga20848e0942882e8c2cc40ee8a48b7bfd)lwm2m\_send\_status

| enum [lwm2m\_send\_status](#ga20848e0942882e8c2cc40ee8a48b7bfd) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

LwM2M send status.

LwM2M send status are generated back to the [lwm2m\_send\_cb\_t](#gaf5394884da53edb28fe4afc92bf40e6a) function in [lwm2m\_send\_cb()](#ga026cc9288d2de17ec557e08b9b987ebc)

| Enumerator | |
| --- | --- |
| LWM2M\_SEND\_STATUS\_SUCCESS | Succeed. |
| LWM2M\_SEND\_STATUS\_FAILURE | Failure. |
| LWM2M\_SEND\_STATUS\_TIMEOUT | Timeout. |

## [◆ ](#ga7611c1aebb0309ee8340e06dd8ee234d)lwm2m\_socket\_states

| enum [lwm2m\_socket\_states](#ga7611c1aebb0309ee8340e06dd8ee234d) |
| --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Different traffic states of the LwM2M socket.

This information can be used to give hints for the network interface that can decide what kind of power management should be used.

These hints are given from CoAP layer messages, so usage of DTLS might affect the actual number of expected datagrams.

| Enumerator | |
| --- | --- |
| LWM2M\_SOCKET\_STATE\_ONGOING | Ongoing traffic is expected. |
| LWM2M\_SOCKET\_STATE\_ONE\_RESPONSE | One response is expected for the next message. |
| LWM2M\_SOCKET\_STATE\_LAST | Next message is the last one. |
| LWM2M\_SOCKET\_STATE\_NO\_DATA | No more data is expected. |

## Function Documentation

## [◆ ](#ga919c7d6f418cda99c77fdaf54ae1a7b0)lwm2m\_acknowledge()

| void lwm2m\_acknowledge | ( | struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | *client\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Acknowledge the currently processed request with an empty ACK.

LwM2M engine by default sends piggybacked responses for requests. This function allows to send an empty ACK for a request earlier (from the application callback). The LwM2M engine will then send the actual response as a separate CON message after all callbacks are executed.

Parameters
:   | [in] | client\_ctx | LwM2M context |
    | --- | --- | --- |

## [◆ ](#ga53f5b4c5967e93c7dd224fce8f416265)lwm2m\_create\_object\_inst()

| int lwm2m\_create\_object\_inst | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Create an LwM2M object instance.

LwM2M clients use this function to create non-default LwM2M objects: Example to create first temperature sensor object: lwm2m\_create\_obj\_inst(&LWM2M\_OBJ(3303, 0));

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gac69c40474180fe14c3761185b2db1c0c)lwm2m\_create\_res\_inst()

| int lwm2m\_create\_res\_inst | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Create a resource instance.

LwM2M clients use this function to create multi-resource instances: Example to create 0 instance of device available power sources: lwm2m\_create\_res\_inst(&LWM2M\_OBJ(3, 0, 6, 0));

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gaf921d4bc96090ef8735d90d173feab94)lwm2m\_delete\_object\_inst()

| int lwm2m\_delete\_object\_inst | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Delete an LwM2M object instance.

LwM2M clients use this function to delete LwM2M objects.

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gacfeb63db0423e6730ffaa826a87eb262)lwm2m\_delete\_res\_inst()

| int lwm2m\_delete\_res\_inst | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Delete a resource instance.

Use this function to remove an existing resource instance

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gabf8726f0438477863423947a7bb77ce2)lwm2m\_device\_add\_err()

| int lwm2m\_device\_add\_err | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *error\_code* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Register a new error code with LwM2M Device object.

Parameters
:   | [in] | error\_code | New error code. |
    | --- | --- | --- |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga6975c5c4825afaccc52741eb54aca4cb)lwm2m\_enable\_cache()

| int lwm2m\_enable\_cache | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | struct [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md) \* | *data\_cache*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *cache\_len* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

 Enable data cache for a resource.

Application may enable caching of resource data by allocating buffer for LwM2M engine to use. Buffer must be size of struct [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md "lwm2m_time_series_elem") times cache\_len

Parameters
:   | path | LwM2M path to resource as a struct |
    | --- | --- |
    | data\_cache | Pointer to Data cache array |
    | cache\_len | number of cached entries |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga1a4dadb822a8241c5bdf339c21cc57a4)lwm2m\_engine\_pause()

| int lwm2m\_engine\_pause | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Suspend the LwM2M engine Thread.

Suspend LwM2M engine. Use case could be when network connection is down. LwM2M Engine indicate before it suspend by LWM2M\_RD\_CLIENT\_EVENT\_ENGINE\_SUSPENDED event.

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga178fea0407a5e98c4f5d5ad69688853a)lwm2m\_engine\_resume()

| int lwm2m\_engine\_resume | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Resume the LwM2M engine thread.

Resume suspended LwM2M engine. After successful resume call engine will do full registration or registration update based on suspended time. Event's LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_COMPLETE or LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_COMPLETE indicate that client is connected to server.

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga9f72fbd0163b15c48ea09cf7d511e444)lwm2m\_engine\_start()

| int lwm2m\_engine\_start | ( | struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | *client\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Start the LwM2M engine.

LwM2M clients normally do not need to call this function as it is called by [lwm2m\_rd\_client\_start()](#ga9dfd46b8a535b1f28e644dc18f57fd79). However, if the client does not use the RD client implementation, it will need to be called manually.

Parameters
:   | [in] | client\_ctx | LwM2M context |
    | --- | --- | --- |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga077e1abd612d31dd33fab52b7d205c39)lwm2m\_engine\_stop()

| int lwm2m\_engine\_stop | ( | struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | *client\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Stop the LwM2M engine.

LwM2M clients normally do not need to call this function as it is called within lwm2m\_rd\_client. However, if the client does not use the RD client implementation, it will need to be called manually.

Parameters
:   | [in] | client\_ctx | LwM2M context |
    | --- | --- | --- |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga950557bce8c510bcc8b0704e7bc4a9dc)lwm2m\_event\_log\_set\_read\_log\_data\_cb()

| void lwm2m\_event\_log\_set\_read\_log\_data\_cb | ( | [lwm2m\_engine\_get\_data\_cb\_t](#ga5e531aade0537eb5e3f5756e9287e384) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set callback to read log data.

The callback will be executed when the LWM2M read operation gets called on the corresponding object.

Parameters
:   | [in] | cb | A callback function for handling the read event. |
    | --- | --- | --- |

## [◆ ](#ga9561c1b8407d888f6fbe1e0ceab1c235)lwm2m\_firmware\_get\_cancel\_cb()

| [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) lwm2m\_firmware\_get\_cancel\_cb | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get a callback for firmware update cancel.

Returns
:   A registered callback function perform actions on firmware update cancel.

## [◆ ](#ga6f4b3e08c7e03cff4bf31e2f2999971e)lwm2m\_firmware\_get\_cancel\_cb\_inst()

| [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) lwm2m\_firmware\_get\_cancel\_cb\_inst | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get the callback for firmware update cancel.

Parameters
:   | [in] | obj\_inst\_id | Object instance ID |
    | --- | --- | --- |

Returns
:   A registered callback function perform actions on firmware update cancel.

## [◆ ](#ga1e4b8ba1b19ac9025dca3c4799bba84a)lwm2m\_firmware\_get\_update\_cb()

| [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) lwm2m\_firmware\_get\_update\_cb | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get the event callback for firmware update execute events.

Returns
:   A registered callback function to receive the execute event.

## [◆ ](#ga34995e902b63c4d7d37ebd709d88a72a)lwm2m\_firmware\_get\_update\_cb\_inst()

| [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) lwm2m\_firmware\_get\_update\_cb\_inst | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get the event callback for firmware update execute events.

Parameters
:   | [in] | obj\_inst\_id | Object instance ID |
    | --- | --- | --- |

Returns
:   A registered callback function to receive the execute event.

## [◆ ](#ga4bf0bbedf5573ac18a11ac4fced11284)lwm2m\_firmware\_get\_write\_cb()

| [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) lwm2m\_firmware\_get\_write\_cb | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get the data callback for firmware block transfer writes.

Returns
:   A registered callback function to receive the block transfer data

## [◆ ](#gad7334f06c3bdb14485597794a417152d)lwm2m\_firmware\_get\_write\_cb\_inst()

| [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) lwm2m\_firmware\_get\_write\_cb\_inst | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get the data callback for firmware block transfer writes.

Parameters
:   | [in] | obj\_inst\_id | Object instance ID |
    | --- | --- | --- |

Returns
:   A registered callback function to receive the block transfer data

## [◆ ](#ga3955dca5cd6d67807ed75e61a4d84d84)lwm2m\_firmware\_set\_cancel\_cb()

| void lwm2m\_firmware\_set\_cancel\_cb | ( | [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set callback for firmware update cancel.

LwM2M clients use this function to register a callback to perform actions on firmware update cancel.

Parameters
:   | [in] | cb | A callback function perform actions on firmware update cancel. |
    | --- | --- | --- |

## [◆ ](#gaa200b524e505f64247f1e7472c5f36d4)lwm2m\_firmware\_set\_cancel\_cb\_inst()

| void lwm2m\_firmware\_set\_cancel\_cb\_inst | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set data callback for firmware update cancel.

LwM2M clients use this function to register a callback to perform actions on firmware update cancel.

Parameters
:   | [in] | obj\_inst\_id | Object instance ID |
    | --- | --- | --- |
    | [in] | cb | A callback function perform actions on firmware update cancel. |

## [◆ ](#ga61eb38e42d9e1b3f467c43a324f2fc65)lwm2m\_firmware\_set\_update\_cb()

| void lwm2m\_firmware\_set\_update\_cb | ( | [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set data callback to handle firmware update execute events.

LwM2M clients use this function to register a callback for receiving the update resource "execute" operation on the LwM2M Firmware Update object.

Parameters
:   | [in] | cb | A callback function to receive the execute event. |
    | --- | --- | --- |

## [◆ ](#ga31d0f3e40b5e3d608d16a4268b2f1b29)lwm2m\_firmware\_set\_update\_cb\_inst()

| void lwm2m\_firmware\_set\_update\_cb\_inst | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set data callback to handle firmware update execute events.

LwM2M clients use this function to register a callback for receiving the update resource "execute" operation on the LwM2M Firmware Update object.

Parameters
:   | [in] | obj\_inst\_id | Object instance ID |
    | --- | --- | --- |
    | [in] | cb | A callback function to receive the execute event. |

## [◆ ](#ga6878ea0ebb512b19a4fb0859756f51d0)lwm2m\_firmware\_set\_write\_cb()

| void lwm2m\_firmware\_set\_write\_cb | ( | [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set data callback for firmware block transfer.

LwM2M clients use this function to register a callback for receiving the block transfer data when performing a firmware update.

Parameters
:   | [in] | cb | A callback function to receive the block transfer data |
    | --- | --- | --- |

## [◆ ](#gac4e4a819e54344657d70ec479eb6ec8d)lwm2m\_firmware\_set\_write\_cb\_inst()

| void lwm2m\_firmware\_set\_write\_cb\_inst | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set data callback for firmware block transfer.

LwM2M clients use this function to register a callback for receiving the block transfer data when performing a firmware update.

Parameters
:   | [in] | obj\_inst\_id | Object instance ID |
    | --- | --- | --- |
    | [in] | cb | A callback function to receive the block transfer data |

## [◆ ](#gafdc72844ce0ca417e297d76288155aa4)lwm2m\_get\_bool()

| int lwm2m\_get\_bool | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (bool).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | value | bool buffer to copy data into |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga03b72e96a67fcbf85feb5bf0b9df81ce)lwm2m\_get\_f64()

| int lwm2m\_get\_f64 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | double \* | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (double).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | value | double buffer to copy data into |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga4de941c36cf678e12da6e05c378a92e5)lwm2m\_get\_objlnk()

| int lwm2m\_get\_objlnk | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \* | *buf* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (Objlnk).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | buf | [lwm2m\_objlnk](structlwm2m__objlnk.md "LWM2M Objlnk resource type structure.") buffer to copy data into |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gae245a9a1d9456af7e6283b1074944606)lwm2m\_get\_opaque()

| int lwm2m\_get\_opaque | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | void \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *buflen* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (opaque buffer).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | buf | Data buffer to copy data into |
    | [in] | buflen | Length of buffer |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gac0b6669d8a19b03eb8b08cbbcdb0c192)lwm2m\_get\_res\_buf()

| int lwm2m\_get\_res\_buf | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | void \*\* | *buffer\_ptr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *buffer\_len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *data\_len*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data\_flags* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get data buffer for a resource.

Use this function to get the data buffer information for the specified LwM2M resource.

If you directly write into the buffer, you must use [lwm2m\_set\_res\_data\_len()](#ga0f2b115d231bea6622135d72b51f55ca) function to update the new size of the written data.

All parameters, except for the pathstr, can be NULL if you don't want to read those values.

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | buffer\_ptr | Data buffer pointer |
    | [out] | buffer\_len | Length of buffer |
    | [out] | data\_len | Length of existing data in the buffer |
    | [out] | data\_flags | Data buffer flags (such as read-only, etc) |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga2426db6720b3f3e15e63022cabae5ece)lwm2m\_get\_s16()

| int lwm2m\_get\_s16 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \* | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (s16).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | value | s16 buffer to copy data into |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga99d7189efa25881dbcddd99e2a795f1b)lwm2m\_get\_s32()

| int lwm2m\_get\_s32 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (s32).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | value | s32 buffer to copy data into |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gaaffe06ca9ee5302fb6e26164f250653e)lwm2m\_get\_s64()

| int lwm2m\_get\_s64 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \* | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (s64).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | value | s64 buffer to copy data into |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga12817bfbf0a0cbb742568ee974a1c337)lwm2m\_get\_s8()

| int lwm2m\_get\_s8 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \* | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (s8).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | value | s8 buffer to copy data into |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga20fc58b25468bf309175db59d67b820b)lwm2m\_get\_string()

| int lwm2m\_get\_string | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | void \* | *str*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *buflen* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (string).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | str | String buffer to copy data into |
    | [in] | buflen | Length of buffer |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga2e1d41866b5ea35c5aa29bca9bb43812)lwm2m\_get\_time()

| int lwm2m\_get\_time | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \* | *buf* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (Time).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | buf | [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) pointer to copy data |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga1b96848f96bdab9939bb2619d3e1059b)lwm2m\_get\_u16()

| int lwm2m\_get\_u16 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (u16).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | value | u16 buffer to copy data into |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga0bc84cb39a7a537925ec7d62e54b8b48)lwm2m\_get\_u32()

| int lwm2m\_get\_u32 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (u32).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | value | u32 buffer to copy data into |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga831d229d9a4b983223dff626bbde7a66)lwm2m\_get\_u64()

| int lwm2m\_get\_u64 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (u64).

**[Deprecated](deprecated.md#_deprecated000023)**
:   Unsigned 64bit value type does not exits. This is internally handled as a [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b). Use [lwm2m\_get\_s64()](#gaaffe06ca9ee5302fb6e26164f250653e) instead.

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | value | u64 buffer to copy data into |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gac56e804962e529799c771d81ac1fd027)lwm2m\_get\_u8()

| int lwm2m\_get\_u8 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Get resource (instance) value (u8).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [out] | value | u8 buffer to copy data into |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga1065c729d5caa8ca13de7766fce77953)lwm2m\_path\_is\_observed()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) lwm2m\_path\_is\_observed | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Check whether a path is observed.

Parameters
:   | [in] | path | LwM2M path as a struct to check |
    | --- | --- | --- |

Returns
:   true when there exists an observation of the same level or lower as the given path, false if it doesn't or path is not a valid LwM2M-path. E.g. true if path refers to a resource and the parent object has an observation, false for the inverse.

## [◆ ](#ga971c0636c19fe7f0a6e918622560a750)lwm2m\_path\_log\_buf()

| char \* lwm2m\_path\_log\_buf | ( | char \* | *buf*, |
| --- | --- | --- | --- |
|  |  | struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Helper function to print path objects' contents to log.

Parameters
:   | [in] | buf | The buffer to use for formatting the string |
    | --- | --- | --- |
    | [in] | path | The path to stringify |

Returns
:   Resulting formatted path string

## [◆ ](#ga896caab5473eadff860872023d13b6c0)lwm2m\_rd\_client\_ctx()

| struct [lwm2m\_ctx](structlwm2m__ctx.md) \* lwm2m\_rd\_client\_ctx | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

 Returns LwM2M client context

Returns
:   ctx LwM2M context

## [◆ ](#ga9dfd46b8a535b1f28e644dc18f57fd79)lwm2m\_rd\_client\_start()

| int lwm2m\_rd\_client\_start | ( | struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | *client\_ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *ep\_name*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | [lwm2m\_ctx\_event\_cb\_t](#ga38dbaf038426efc75d889c4a0666dac9) | *event\_cb*, |
|  |  | [lwm2m\_observe\_cb\_t](#gad7bea67e16e1e831e0f949dbf83d5afe) | *observe\_cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Start the LwM2M RD (Registration / Discovery) Client.

The RD client sits just above the LwM2M engine and performs the necessary actions to implement the "Registration interface". For more information see Section "Client Registration Interface" of LwM2M Technical Specification.

NOTE: [lwm2m\_engine\_start()](#ga9f72fbd0163b15c48ea09cf7d511e444) is called automatically by this function.

Parameters
:   | [in] | client\_ctx | LwM2M context |
    | --- | --- | --- |
    | [in] | ep\_name | Registered endpoint name |
    | [in] | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags used to configure current LwM2M session. |
    | [in] | event\_cb | Client event callback function |
    | [in] | observe\_cb | Observe callback function called when an observer was added or deleted, and when a notification was acked or has timed out |

Returns
:   0 for success, -EINPROGRESS when client is already running or negative error codes in case of failure.

## [◆ ](#gafd87e5d975c4d88973ac3e95e4d156ac)lwm2m\_rd\_client\_stop()

| int lwm2m\_rd\_client\_stop | ( | struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | *client\_ctx*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_ctx\_event\_cb\_t](#ga38dbaf038426efc75d889c4a0666dac9) | *event\_cb*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *deregister* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Stop the LwM2M RD (De-register) Client.

The RD client sits just above the LwM2M engine and performs the necessary actions to implement the "Registration interface". For more information see Section "Client Registration Interface" of the LwM2M Technical Specification.

Parameters
:   | [in] | client\_ctx | LwM2M context |
    | --- | --- | --- |
    | [in] | event\_cb | Client event callback function |
    | [in] | deregister | True to deregister the client if registered. False to force close the connection. |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gab4ec7a22d01259b6ba9d3a7b6681e6f0)lwm2m\_rd\_client\_update()

| void lwm2m\_rd\_client\_update | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Trigger a Registration Update of the LwM2M RD Client.

## [◆ ](#ga346d547e02bd53ee83f83b2248449e98)lwm2m\_register\_create\_callback()

| int lwm2m\_register\_create\_callback | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_id*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set object instance create event callback.

This event is triggered when an object instance is created.

Parameters
:   | [in] | obj\_id | LwM2M object id |
    | --- | --- | --- |
    | [in] | cb | Create object instance callback |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga92d7e6d81ef674a6c311e1717c6bf373)lwm2m\_register\_delete\_callback()

| int lwm2m\_register\_delete\_callback | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_id*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_user\_cb\_t](#gabcbca483b310e0c4cd68aef2d9cda0bf) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set object instance delete event callback.

This event is triggered when an object instance is deleted.

Parameters
:   | [in] | obj\_id | LwM2M object id |
    | --- | --- | --- |
    | [in] | cb | Delete object instance callback |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga29cc5cdd697e94d7379b1fb178487916)lwm2m\_register\_exec\_callback()

| int lwm2m\_register\_exec\_callback | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource execute event callback.

This event is triggered when the execute method of a resource is enabled.

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | cb | Execute resource callback |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga3dd8b38e797173dae902404fb5b7a3f4)lwm2m\_register\_post\_write\_callback()

| int lwm2m\_register\_post\_write\_callback | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) post-write callback.

This callback is triggered after setting the value of a resource to the resource data buffer.

It allows an LwM2M client or object to post-process the value of a resource or trigger other related resource calculations.

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | cb | Post-write resource callback |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga6f775837e07ba9b0032be8917a593e16)lwm2m\_register\_pre\_write\_callback()

| int lwm2m\_register\_pre\_write\_callback | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_get\_data\_cb\_t](#ga5e531aade0537eb5e3f5756e9287e384) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) pre-write callback.

This callback is triggered before setting the value of a resource. It can pass a special data buffer to the engine so that the actual resource value can be calculated later, etc.

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | cb | Pre-write resource callback |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gaf33bd6a527b6d399f3d92b666ac77dfb)lwm2m\_register\_read\_callback()

| int lwm2m\_register\_read\_callback | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_get\_data\_cb\_t](#ga5e531aade0537eb5e3f5756e9287e384) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) read callback.

LwM2M clients can use this to set the callback function for resource reads when data handling in the LwM2M engine needs to be bypassed. For example reading back opaque binary data from external storage.

This callback should not generally be used for any data that might be observed as engine does not have any knowledge of data changes.

When separate buffer for data should be used, use [lwm2m\_set\_res\_buf()](#ga56a2aecd38baedb5dc17258610c4780d) instead to set the storage.

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | cb | Read resource callback |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gad6e5fd4815f409ad59ad631b03199333)lwm2m\_register\_validate\_callback()

| int lwm2m\_register\_validate\_callback | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) validation callback.

This callback is triggered before setting the value of a resource to the resource data buffer.

The callback allows an LwM2M client or object to validate the data before writing and notify an error if the data should be discarded for any reason (by returning a negative error code).

Note
:   All resources that have a validation callback registered are initially decoded into a temporary validation buffer. Make sure that CONFIG\_LWM2M\_ENGINE\_VALIDATION\_BUFFER\_SIZE is large enough to store each of the validated resources (individually).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | cb | Validate resource data callback |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga9a0cdcc9fc6d37462eddeb54e5d1f87a)lwm2m\_registry\_lock()

| void lwm2m\_registry\_lock | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Locks the registry for this thread.

Use this function before writing to multiple resources. This halts the lwm2m main thread until all the write-operations are finished.

## [◆ ](#gab09b62982c34887cdd16c30659d3349a)lwm2m\_registry\_unlock()

| void lwm2m\_registry\_unlock | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Unlocks the registry previously locked by [lwm2m\_registry\_lock()](#ga9a0cdcc9fc6d37462eddeb54e5d1f87a).

## [◆ ](#ga6c05640737cfc4da71841a77de128be0)lwm2m\_security\_mode()

| int lwm2m\_security\_mode | ( | struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Read security mode from selected security object instance.

This data is valid only if RD client is running.

Parameters
:   | ctx | Pointer to client context. |
    | --- | --- |

Returns
:   int Positive values are [lwm2m\_security\_mode\_e](#ga11de8078091631cb88b26a9a460097ab), negative error codes otherwise.

## [◆ ](#ga026cc9288d2de17ec557e08b9b987ebc)lwm2m\_send\_cb()

| int lwm2m\_send\_cb | ( | struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) | *path\_list*[], |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *path\_list\_size*, |
|  |  | [lwm2m\_send\_cb\_t](#gaf5394884da53edb28fe4afc92bf40e6a) | *reply\_cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

 LwM2M SEND operation to given path list asynchronously with confirmation callback

Parameters
:   | ctx | LwM2M context |
    | --- | --- |
    | path\_list | LwM2M path struct list |
    | path\_list\_size | Length of path list. Max size is CONFIG\_LWM2M\_COMPOSITE\_PATH\_LIST\_SIZE |
    | reply\_cb | Callback triggered with confirmation state or NULL if not used |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga9ef21d06bef8a97b7666c0aa7fa753b4)lwm2m\_set\_bool()

| int lwm2m\_set\_bool | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (bool).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | bool value |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga41b673986e11748b2ded8e1f8f05e0a7)lwm2m\_set\_bulk()

| int lwm2m\_set\_bulk | ( | const struct [lwm2m\_res\_item](structlwm2m__res__item.md) | *res\_list*[], |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *res\_list\_size* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set multiple resource (instance) values.

NOTE: Value type must match the target resource as this function does not do any type conversion. See struct [lwm2m\_res\_item](structlwm2m__res__item.md "lwm2m_res_item") for list of resource types.

Parameters
:   | [in] | res\_list | LwM2M resource item list |
    | --- | --- | --- |
    | [in] | res\_list\_size | Length of resource list |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga956c4fc742a588b7b8b95ce8481f09bf)lwm2m\_set\_default\_sockopt()

| int lwm2m\_set\_default\_sockopt | ( | struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set default socket options for DTLS connections.

The engine calls this when [lwm2m\_ctx::set\_socketoptions](structlwm2m__ctx.md#a746c578cf1d2c5eb606d0b592f419317 "lwm2m_ctx::set_socketoptions") is not overwritten. You can call this from the overwritten callback to set extra options after or before defaults.

Parameters
:   | ctx | Client context |
    | --- | --- |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga3386d3f2ad8d9713fc2283ed6921c2fc)lwm2m\_set\_f64()

| int lwm2m\_set\_f64 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | const double | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (double).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | double value |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga04a18bd8a4eeea41a47803c16567d67b)lwm2m\_set\_objlnk()

| int lwm2m\_set\_objlnk | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | const struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \* | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (Objlnk).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | pointer to the [lwm2m\_objlnk](structlwm2m__objlnk.md "LWM2M Objlnk resource type structure.") structure |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gaaef33bdf3f48fd91abdb50db4d5460f9)lwm2m\_set\_opaque()

| int lwm2m\_set\_opaque | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | const char \* | *data\_ptr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data\_len* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (opaque buffer).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | data\_ptr | Data buffer |
    | [in] | data\_len | Length of buffer |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga56a2aecd38baedb5dc17258610c4780d)lwm2m\_set\_res\_buf()

| int lwm2m\_set\_res\_buf | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | void \* | *buffer\_ptr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *buffer\_len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data\_len*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data\_flags* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set data buffer for a resource.

Use this function to set the data buffer and flags for the specified LwM2M resource.

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | buffer\_ptr | Data buffer pointer |
    | [in] | buffer\_len | Length of buffer |
    | [in] | data\_len | Length of existing data in the buffer |
    | [in] | data\_flags | Data buffer flags (such as read-only, etc) |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga0f2b115d231bea6622135d72b51f55ca)lwm2m\_set\_res\_data\_len()

| int lwm2m\_set\_res\_data\_len | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data\_len* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Update data size for a resource.

Use this function to set the new size of data in the buffer if you write to a buffer received by [lwm2m\_get\_res\_buf()](#gac0b6669d8a19b03eb8b08cbbcdb0c192).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | data\_len | Length of data |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gad548ffedcb8328b23eb32476a97be6ee)lwm2m\_set\_s16()

| int lwm2m\_set\_s16 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (s16).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | s16 value |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga327e086959fc5649a5ef14f1f2943e88)lwm2m\_set\_s32()

| int lwm2m\_set\_s32 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (s32).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | s32 value |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga18fcee379640c0dda32d6e3d14827260)lwm2m\_set\_s64()

| int lwm2m\_set\_s64 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (s64).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | s64 value |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga37261a4b9e54eab3d1d855a084d082aa)lwm2m\_set\_s8()

| int lwm2m\_set\_s8 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (s8).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | s8 value |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga7217f33bf705011d91ba66c86a4d5747)lwm2m\_set\_string()

| int lwm2m\_set\_string | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | const char \* | *data\_ptr* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (string).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | data\_ptr | NULL terminated char buffer |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga7194ad24842e35130d8af7f5104c0844)lwm2m\_set\_time()

| int lwm2m\_set\_time | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (Time).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | Epoch timestamp |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga1f06bb65571efee18db5d061f95399c3)lwm2m\_set\_u16()

| int lwm2m\_set\_u16 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (u16).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | u16 value |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga9481e570b121404dc1be1ce23d904894)lwm2m\_set\_u32()

| int lwm2m\_set\_u32 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (u32).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | u32 value |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga8a751dc8384cc47f9c14d916e20ae19d)lwm2m\_set\_u64()

| int lwm2m\_set\_u64 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (u64).

**[Deprecated](deprecated.md#_deprecated000022)**
:   Unsigned 64bit value type does not exits. This is internally handled as a [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b). Use [lwm2m\_set\_s64()](#ga18fcee379640c0dda32d6e3d14827260) instead.

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | u64 value |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga1aa3ff424b7190d0fbd9366626b2685c)lwm2m\_set\_u8()

| int lwm2m\_set\_u8 | ( | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set resource (instance) value (u8).

Parameters
:   | [in] | path | LwM2M path as a struct |
    | --- | --- | --- |
    | [in] | value | u8 value |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga573e128348fb2f43a33bd09332dd677f)lwm2m\_swmgmt\_install\_completed()

| int lwm2m\_swmgmt\_install\_completed | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id*, |
| --- | --- | --- | --- |
|  |  | int | *error\_code* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Function to be called when a Software Management object instance completed the Install operation.

Parameters
:   | [in] | obj\_inst\_id | The Software Management object instance |
    | --- | --- | --- |
    | [in] | error\_code | The result code of the operation. Zero on success otherwise it should be a negative integer. |

return 0 on success, otherwise a negative integer.

## [◆ ](#gac374d0559056ddb9cf43deae932fd128)lwm2m\_swmgmt\_set\_activate\_cb()

| int lwm2m\_swmgmt\_set\_activate\_cb | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set callback to handle software activation requests.

The callback will be executed when the LWM2M execute operation gets called on the corresponding object's Activate resource instance.

Parameters
:   | [in] | obj\_inst\_id | The instance number to set the callback for. |
    | --- | --- | --- |
    | [in] | cb | A callback function to receive the execute event. |

Returns
:   0 on success, otherwise a negative integer.

## [◆ ](#ga7a2b93b918257bece819dc44804f27f5)lwm2m\_swmgmt\_set\_deactivate\_cb()

| int lwm2m\_swmgmt\_set\_deactivate\_cb | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set callback to handle software deactivation requests.

The callback will be executed when the LWM2M execute operation gets called on the corresponding object's Deactivate resource instance.

Parameters
:   | [in] | obj\_inst\_id | The instance number to set the callback for. |
    | --- | --- | --- |
    | [in] | cb | A callback function to receive the execute event. |

Returns
:   0 on success, otherwise a negative integer.

## [◆ ](#gacf209563efdc5f3201152088c52d05c3)lwm2m\_swmgmt\_set\_delete\_package\_cb()

| int lwm2m\_swmgmt\_set\_delete\_package\_cb | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set callback to handle software uninstall requests.

The callback will be executed when the LWM2M execute operation gets called on the corresponding object's Uninstall resource instance.

Parameters
:   | [in] | obj\_inst\_id | The instance number to set the callback for. |
    | --- | --- | --- |
    | [in] | cb | A callback function for handling the execute event. |

Returns
:   0 on success, otherwise a negative integer.

## [◆ ](#gadfc00060c0b538ed576b5e3edd7dac80)lwm2m\_swmgmt\_set\_install\_package\_cb()

| int lwm2m\_swmgmt\_set\_install\_package\_cb | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_execute\_cb\_t](#gaeb32bcd4981b4c7bd891f99668ebc0fe) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set callback to handle software install requests.

The callback will be executed when the LWM2M execute operation gets called on the corresponding object's Install resource instance.

Parameters
:   | [in] | obj\_inst\_id | The instance number to set the callback for. |
    | --- | --- | --- |
    | [in] | cb | A callback function to receive the execute event. |

Returns
:   0 on success, otherwise a negative integer.

## [◆ ](#gab59370ce4fdc94adb4903f22ab1f95b2)lwm2m\_swmgmt\_set\_read\_package\_version\_cb()

| int lwm2m\_swmgmt\_set\_read\_package\_version\_cb | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_get\_data\_cb\_t](#ga5e531aade0537eb5e3f5756e9287e384) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set callback to read software package.

The callback will be executed when the LWM2M read operation gets called on the corresponding object.

Parameters
:   | [in] | obj\_inst\_id | The instance number to set the callback for. |
    | --- | --- | --- |
    | [in] | cb | A callback function for handling the read event. |

Returns
:   0 on success, otherwise a negative integer.

## [◆ ](#ga293904118f972ae387c8aa85a1028b54)lwm2m\_swmgmt\_set\_write\_package\_cb()

| int lwm2m\_swmgmt\_set\_write\_package\_cb | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *obj\_inst\_id*, |
| --- | --- | --- | --- |
|  |  | [lwm2m\_engine\_set\_data\_cb\_t](#ga3afac013b0cf731f9c86dc3791131585) | *cb* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Set data callback for software management block transfer.

The callback will be executed when the LWM2M block write operation gets called on the corresponding object's resource instance.

Parameters
:   | [in] | obj\_inst\_id | The instance number to set the callback for. |
    | --- | --- | --- |
    | [in] | cb | A callback function for handling the block write event. |

Returns
:   0 on success, otherwise a negative integer.

## [◆ ](#gab45cebf6f0b6b70974367ca453d16aeb)lwm2m\_update\_device\_service\_period()

| int lwm2m\_update\_device\_service\_period | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *period\_ms* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Update the period of the device service.

Change the duration of the periodic device service that notifies the current time.

Parameters
:   | [in] | period\_ms | New period for the device service (in milliseconds) |
    | --- | --- | --- |

Returns
:   0 for success or negative in case of error.

## [◆ ](#ga6acccbcd879901574aceab53a21800fc)lwm2m\_update\_observer\_max\_period()

| int lwm2m\_update\_observer\_max\_period | ( | struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | *client\_ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *period\_s* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Change an observer's pmax value.

LwM2M clients use this function to modify the pmax attribute for an observation being made. Example to update the pmax of a temperature sensor value being observed: lwm2m\_\_update\_observer\_max\_period(client\_ctx, &LWM2M\_OBJ(3303, 0, 5700), 5);

Parameters
:   | [in] | client\_ctx | LwM2M context |
    | --- | --- | --- |
    | [in] | path | LwM2M path as a struct |
    | [in] | period\_s | Value of pmax to be given (in seconds). |

Returns
:   0 for success or negative in case of error.

## [◆ ](#gadd163806d70713d8349a9db484ba88bf)lwm2m\_update\_observer\_min\_period()

| int lwm2m\_update\_observer\_min\_period | ( | struct [lwm2m\_ctx](structlwm2m__ctx.md) \* | *client\_ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \* | *path*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *period\_s* ) |

`#include <[lwm2m.h](lwm2m_8h.md)>`

Change an observer's pmin value.

LwM2M clients use this function to modify the pmin attribute for an observation being made. Example to update the pmin of a temperature sensor value being observed: lwm2m\_update\_observer\_min\_period(client\_ctx, &LWM2M\_OBJ(3303, 0, 5700), 5);

Parameters
:   | [in] | client\_ctx | LwM2M context |
    | --- | --- | --- |
    | [in] | path | LwM2M path as a struct |
    | [in] | period\_s | Value of pmin to be given (in seconds). |

Returns
:   0 for success or negative in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
