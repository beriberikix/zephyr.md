---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ots_8h.html
original_path: doxygen/html/ots_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ots.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/sys/crc.h](crc_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/bluetooth/uuid.h](uuid_8h_source.md)>`  
`#include <[zephyr/bluetooth/gatt.h](gatt_8h_source.md)>`

[Go to the source code of this file.](ots_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_ots\_obj\_type](structbt__ots__obj__type.md) |
|  | Type of an OTS object. [More...](structbt__ots__obj__type.md#details) |
| struct | [bt\_ots\_obj\_size](structbt__ots__obj__size.md) |
|  | Descriptor for OTS Object Size parameter. [More...](structbt__ots__obj__size.md#details) |
| struct | [bt\_ots\_feat](structbt__ots__feat.md) |
|  | Features of the OTS. [More...](structbt__ots__feat.md#details) |
| struct | [bt\_ots\_date\_time](structbt__ots__date__time.md) |
|  | Date and Time structure. [More...](structbt__ots__date__time.md#details) |
| struct | [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) |
|  | Metadata of an OTS object. [More...](structbt__ots__obj__metadata.md#details) |
| struct | [bt\_ots\_obj\_add\_param](structbt__ots__obj__add__param.md) |
|  | Descriptor for OTS object addition. [More...](structbt__ots__obj__add__param.md#details) |
| struct | [bt\_ots\_obj\_created\_desc](structbt__ots__obj__created__desc.md) |
|  | Descriptor for OTS created object. [More...](structbt__ots__obj__created__desc.md#details) |
| struct | [bt\_ots\_cb](structbt__ots__cb.md) |
|  | OTS callback structure. [More...](structbt__ots__cb.md#details) |
| struct | [bt\_ots\_init\_param](structbt__ots__init__param.md) |
|  | Descriptor for OTS initialization. [More...](structbt__ots__init__param.md#details) |
| struct | [bt\_ots\_client](structbt__ots__client.md) |
|  | OTS client instance. [More...](structbt__ots__client.md#details) |
| struct | [bt\_ots\_client\_cb](structbt__ots__client__cb.md) |
|  | OTS client callback structure. [More...](structbt__ots__client__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_OTS\_OBJ\_ID\_SIZE](group__bt__ots.md#gad5e4a66f017facc2a185ee0a55a0c3ee)   6 |
|  | Size of OTS object ID (in bytes). |
| #define | [BT\_OTS\_OBJ\_ID\_MIN](group__bt__ots.md#ga79110fa56a524754d74bf20ac6a766aa)   0x000000000100ULL |
|  | Minimum allowed value for object ID (except ID for directory listing). |
| #define | [BT\_OTS\_OBJ\_ID\_MAX](group__bt__ots.md#gabd777e7a1b7adaaacfec3e084c3a9bfe)   0xFFFFFFFFFFFFULL |
|  | Maximum allowed value for object ID (except ID for directory listing). |
| #define | [OTS\_OBJ\_ID\_DIR\_LIST](group__bt__ots.md#ga4a6a0b0a3c8d10f3668e61c9dee0e05e)   0x000000000000ULL |
|  | ID of the Directory Listing Object. |
| #define | [BT\_OTS\_OBJ\_ID\_MASK](group__bt__ots.md#gabe3d54a6dfa0d52a97826c140c603d78)   [BIT64\_MASK](group__sys-util.md#ga1a138896caafcb2429a6483ea7412d12)(48) |
|  | Mask for OTS object IDs, preserving the 48 bits. |
| #define | [BT\_OTS\_OBJ\_ID\_STR\_LEN](group__bt__ots.md#ga2754eeb7418ed762a3119fc56871d37e)   15 |
|  | Length of OTS object ID string (in bytes). |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_DELETE](group__bt__ots.md#ga6ad37ee172d6518e7316b4e0ec8f27c7)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_DELETE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10 "BT_OTS_OBJ_PROP_DELETE") property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_EXECUTE](group__bt__ots.md#ga2342f00ef480b279d737bcddc8e2faf0)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_EXECUTE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad "BT_OTS_OBJ_PROP_EXECUTE") property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_READ](group__bt__ots.md#gaba26016beff74b1b6ec75ba083cf808d)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_READ](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102 "BT_OTS_OBJ_PROP_READ") property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_WRITE](group__bt__ots.md#gaeb1a5a907478fd668199a27e20fc2173)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_WRITE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2 "BT_OTS_OBJ_PROP_WRITE") property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_APPEND](group__bt__ots.md#gaa1eff1b4ee05fb91d87dcb85dd7469e1)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_APPEND](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775 "BT_OTS_OBJ_PROP_APPEND") property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_TRUNCATE](group__bt__ots.md#ga8f99514414958d031a4e9985c8cc976b)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_TRUNCATE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446 "BT_OTS_OBJ_PROP_TRUNCATE") property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_PATCH](group__bt__ots.md#gac36c68dfeb21bf705f87f11e847c5aed)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_PATCH](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed "BT_OTS_OBJ_PROP_PATCH") property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_MARKED](group__bt__ots.md#gae21e599a85549d5cd4462c0f36c291ac)(prop) |
|  | Set [BT\_OTS\_OBJ\_SET\_PROP\_MARKED](group__bt__ots.md#gae21e599a85549d5cd4462c0f36c291ac "BT_OTS_OBJ_SET_PROP_MARKED") property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_DELETE](group__bt__ots.md#ga7a735cf89c9986624e34b183282a65ee)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_DELETE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10 "BT_OTS_OBJ_PROP_DELETE") property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_EXECUTE](group__bt__ots.md#ga90619bdcf5ec9a942f7d81f6c87465fc)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_EXECUTE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad "BT_OTS_OBJ_PROP_EXECUTE") property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_READ](group__bt__ots.md#gae846afdc9f6c40b2bf6d2ae67deb8eef)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_READ](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102 "BT_OTS_OBJ_PROP_READ") property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_WRITE](group__bt__ots.md#ga9769628cbe2c81161607c6518d3d4798)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_WRITE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2 "BT_OTS_OBJ_PROP_WRITE") property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_APPEND](group__bt__ots.md#gaccbf81f9a9ebcc70801739a4a8fafcd8)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_APPEND](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775 "BT_OTS_OBJ_PROP_APPEND") property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_TRUNCATE](group__bt__ots.md#gac7b6632aac554db5b4d5b9f3e8bf78b4)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_TRUNCATE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446 "BT_OTS_OBJ_PROP_TRUNCATE") property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_PATCH](group__bt__ots.md#ga6c8ccb5f8919f062b1b44e1b4981907d)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_PATCH](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed "BT_OTS_OBJ_PROP_PATCH") property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_MARKED](group__bt__ots.md#gaeffab993f4fbe15090a7a626cd56f034)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_MARKED](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3 "BT_OTS_OBJ_PROP_MARKED") property. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_CREATE](group__bt__ots.md#ga8cc851f268de24fe3445a9a0c3af6abf)(feat) |
|  | Set [BT\_OTS\_OACP\_SET\_FEAT\_CREATE](group__bt__ots.md#ga8cc851f268de24fe3445a9a0c3af6abf "BT_OTS_OACP_SET_FEAT_CREATE") feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_DELETE](group__bt__ots.md#ga9306e9a2b8ea468f28eb73b7d412032e)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_DELETE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee "BT_OTS_OACP_FEAT_DELETE") feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_CHECKSUM](group__bt__ots.md#gaba4d7e446212dc6c2139c324d22edc10)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_CHECKSUM](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f "BT_OTS_OACP_FEAT_CHECKSUM") feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_EXECUTE](group__bt__ots.md#ga4b19d199947053e7b2f93b64ea83c29a)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_EXECUTE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c "BT_OTS_OACP_FEAT_EXECUTE") feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_READ](group__bt__ots.md#ga5508cf6698e2927333f31cb0cffce831)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_READ](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465 "BT_OTS_OACP_FEAT_READ") feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_WRITE](group__bt__ots.md#gac035cb71a2caabd16bb64d27b56e32c7)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_WRITE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab "BT_OTS_OACP_FEAT_WRITE") feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_APPEND](group__bt__ots.md#gaabae304227bed27796ad2a346963fa86)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_APPEND](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b "BT_OTS_OACP_FEAT_APPEND") feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_TRUNCATE](group__bt__ots.md#gae5f0e14f685d40782952345ebe50eb3d)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_TRUNCATE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225 "BT_OTS_OACP_FEAT_TRUNCATE") feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_PATCH](group__bt__ots.md#gabca8354bc176bd819005ca213a148b87)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_PATCH](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf "BT_OTS_OACP_FEAT_PATCH") feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_ABORT](group__bt__ots.md#ga3bb8eb9f732947daf289dfe40e171248)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_ABORT](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440 "BT_OTS_OACP_FEAT_ABORT") feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_CREATE](group__bt__ots.md#ga058d8d1fb255ca66057c1edfc547def4)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_CREATE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9 "BT_OTS_OACP_FEAT_CREATE") feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_DELETE](group__bt__ots.md#ga815632fc160921a074bec60250df47f2)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_DELETE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee "BT_OTS_OACP_FEAT_DELETE") feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_CHECKSUM](group__bt__ots.md#gabbc141c9a7d5614971b87b727cbf01af)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_CHECKSUM](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f "BT_OTS_OACP_FEAT_CHECKSUM") feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_EXECUTE](group__bt__ots.md#ga2ac0d82e8fab9fa22b5dc3396c8641ad)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_EXECUTE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c "BT_OTS_OACP_FEAT_EXECUTE") feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_READ](group__bt__ots.md#gac53739b9fd65124f601e92b29b9123cd)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_READ](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465 "BT_OTS_OACP_FEAT_READ") feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_WRITE](group__bt__ots.md#ga390d957c514b2f182ff3d1d0c2221822)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_WRITE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab "BT_OTS_OACP_FEAT_WRITE") feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_APPEND](group__bt__ots.md#ga36f5cc04fce18390bf1cde3e0e8a6184)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_APPEND](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b "BT_OTS_OACP_FEAT_APPEND") feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_TRUNCATE](group__bt__ots.md#ga9ca79d43292354f1558943f944dd53a7)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_TRUNCATE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225 "BT_OTS_OACP_FEAT_TRUNCATE") feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_PATCH](group__bt__ots.md#gaca6591a0c7e8650fa827a7a43fcca81e)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_PATCH](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf "BT_OTS_OACP_FEAT_PATCH") feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_ABORT](group__bt__ots.md#ga196a2aceeecd620baacf0727e1427341)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_ABORT](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440 "BT_OTS_OACP_FEAT_ABORT") feature. |
| #define | [BT\_OTS\_OLCP\_SET\_FEAT\_GO\_TO](group__bt__ots.md#gafe219709f2bd318af66cad4e118df658)(feat) |
|  | Set [BT\_OTS\_OLCP\_FEAT\_GO\_TO](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713 "BT_OTS_OLCP_FEAT_GO_TO") feature. |
| #define | [BT\_OTS\_OLCP\_SET\_FEAT\_ORDER](group__bt__ots.md#ga1248c694ff2d9ded862f37d03d98e2f0)(feat) |
|  | Set [BT\_OTS\_OLCP\_FEAT\_ORDER](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d "BT_OTS_OLCP_FEAT_ORDER") feature. |
| #define | [BT\_OTS\_OLCP\_SET\_FEAT\_NUM\_REQ](group__bt__ots.md#ga1cee6e1affdff27aa0ba6a655c9bf09c)(feat) |
|  | Set [BT\_OTS\_OLCP\_FEAT\_NUM\_REQ](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660 "BT_OTS_OLCP_FEAT_NUM_REQ") feature. |
| #define | [BT\_OTS\_OLCP\_SET\_FEAT\_CLEAR](group__bt__ots.md#ga7a3f8d3b725c8c31d5e3062d46db4438)(feat) |
|  | Set [BT\_OTS\_OLCP\_FEAT\_CLEAR](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af "BT_OTS_OLCP_FEAT_CLEAR") feature. |
| #define | [BT\_OTS\_OLCP\_GET\_FEAT\_GO\_TO](group__bt__ots.md#ga7ec49843849613ee3f8f72209cae68c2)(feat) |
|  | Get [BT\_OTS\_OLCP\_GET\_FEAT\_GO\_TO](group__bt__ots.md#ga7ec49843849613ee3f8f72209cae68c2 "BT_OTS_OLCP_GET_FEAT_GO_TO") feature. |
| #define | [BT\_OTS\_OLCP\_GET\_FEAT\_ORDER](group__bt__ots.md#gad4393e56c94c2484cd344b48cb54b255)(feat) |
|  | Get [BT\_OTS\_OLCP\_GET\_FEAT\_ORDER](group__bt__ots.md#gad4393e56c94c2484cd344b48cb54b255 "BT_OTS_OLCP_GET_FEAT_ORDER") feature. |
| #define | [BT\_OTS\_OLCP\_GET\_FEAT\_NUM\_REQ](group__bt__ots.md#ga2a1a62e410586b1117fd3571e42363d8)(feat) |
|  | Get [BT\_OTS\_OLCP\_GET\_FEAT\_NUM\_REQ](group__bt__ots.md#ga2a1a62e410586b1117fd3571e42363d8 "BT_OTS_OLCP_GET_FEAT_NUM_REQ") feature. |
| #define | [BT\_OTS\_OLCP\_GET\_FEAT\_CLEAR](group__bt__ots.md#ga0f57d172615d1c6ea857506dc0c10e55)(feat) |
|  | Get [BT\_OTS\_OLCP\_GET\_FEAT\_CLEAR](group__bt__ots.md#ga0f57d172615d1c6ea857506dc0c10e55 "BT_OTS_OLCP_GET_FEAT_CLEAR") feature. |
| #define | [BT\_OTS\_DATE\_TIME\_FIELD\_SIZE](group__bt__ots.md#ga56cd1131414fa19e3ec30e2a1a241689)   7 |
| #define | [BT\_OTS\_STOP](group__bt__ots.md#ga4f18ea10855379414dd8a70b6c119d6b)   0 |
| #define | [BT\_OTS\_CONTINUE](group__bt__ots.md#ga8ccd0dec55069aa01bb9740a6520fd51)   1 |

| Typedefs | |
| --- | --- |
| typedef int(\* | [bt\_ots\_client\_dirlisting\_cb](group__bt__ots.md#gaa1a9db6e8aa6ee716e4fdd2e34157f46)) (struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) \*meta) |
|  | Directory listing object metadata callback. |

| Enumerations | |
| --- | --- |
| enum | {     [BT\_OTS\_OBJ\_PROP\_DELETE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10) = 0 , [BT\_OTS\_OBJ\_PROP\_EXECUTE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad) = 1 , [BT\_OTS\_OBJ\_PROP\_READ](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102) = 2 , [BT\_OTS\_OBJ\_PROP\_WRITE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2) = 3 ,     [BT\_OTS\_OBJ\_PROP\_APPEND](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775) = 4 , [BT\_OTS\_OBJ\_PROP\_TRUNCATE](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446) = 5 , [BT\_OTS\_OBJ\_PROP\_PATCH](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed) = 6 , [BT\_OTS\_OBJ\_PROP\_MARKED](group__bt__ots.md#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3) = 7   } |
|  | Properties of an OTS object. [More...](group__bt__ots.md#gaea054a2be05dca63c0cd0375649af26b) |
| enum | {     [BT\_OTS\_OACP\_FEAT\_CREATE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9) = 0 , [BT\_OTS\_OACP\_FEAT\_DELETE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee) = 1 , [BT\_OTS\_OACP\_FEAT\_CHECKSUM](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f) = 2 , [BT\_OTS\_OACP\_FEAT\_EXECUTE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c) = 3 ,     [BT\_OTS\_OACP\_FEAT\_READ](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465) = 4 , [BT\_OTS\_OACP\_FEAT\_WRITE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab) = 5 , [BT\_OTS\_OACP\_FEAT\_APPEND](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b) = 6 , [BT\_OTS\_OACP\_FEAT\_TRUNCATE](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225) = 7 ,     [BT\_OTS\_OACP\_FEAT\_PATCH](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf) = 8 , [BT\_OTS\_OACP\_FEAT\_ABORT](group__bt__ots.md#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440) = 9   } |
|  | Object Action Control Point Feature bits. [More...](group__bt__ots.md#ga141f5762339600942eb229bfdc183ebb) |
| enum | [bt\_ots\_oacp\_write\_op\_mode](group__bt__ots.md#gaebdd2b8a80948d1050d42fa3963cc863) { [BT\_OTS\_OACP\_WRITE\_OP\_MODE\_NONE](group__bt__ots.md#ggaebdd2b8a80948d1050d42fa3963cc863a1c2d68fccd8f252b54a11879a6dd53ab) = 0 , [BT\_OTS\_OACP\_WRITE\_OP\_MODE\_TRUNCATE](group__bt__ots.md#ggaebdd2b8a80948d1050d42fa3963cc863a91d201f7f01809e2af10e10008d4eb8a) = BIT(1) } |
| enum | { [BT\_OTS\_OLCP\_FEAT\_GO\_TO](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713) = 0 , [BT\_OTS\_OLCP\_FEAT\_ORDER](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d) = 1 , [BT\_OTS\_OLCP\_FEAT\_NUM\_REQ](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660) = 2 , [BT\_OTS\_OLCP\_FEAT\_CLEAR](group__bt__ots.md#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af) = 3 } |
|  | Object List Control Point Feature bits. [More...](group__bt__ots.md#ga39716a5c8e5097ad2ddeaf8db407024e) |
| enum | {     [BT\_OTS\_METADATA\_REQ\_NAME](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45ada06e9d807f7c197bd332c0e7ca21ffb) = BIT(0) , [BT\_OTS\_METADATA\_REQ\_TYPE](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45aff8f3ce21a85b397b64b5d03a5fe8af9) = BIT(1) , [BT\_OTS\_METADATA\_REQ\_SIZE](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45aca9770dfa7fbec3a6bc0bccb4e9e41e5) = BIT(2) , [BT\_OTS\_METADATA\_REQ\_CREATED](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45ac47367e5e775fa6690ac5bc03e187095) = BIT(3) ,     [BT\_OTS\_METADATA\_REQ\_MODIFIED](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a35a3d25b637ac80e658102f27aeb7f5e) = BIT(4) , [BT\_OTS\_METADATA\_REQ\_ID](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a44cb8e7804c86fce7c2eab3f3f0743c2) = BIT(5) , [BT\_OTS\_METADATA\_REQ\_PROPS](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45af7c08a3c53273ac6452f607a23826e2f) = BIT(6) , [BT\_OTS\_METADATA\_REQ\_ALL](group__bt__ots.md#gga9bbade1b48363f0f486968723afefb45a04e4ab3e722a23370a63288c3eba8cdf) = 0x7F   } |
|  | Object metadata request bit field values. [More...](group__bt__ots.md#ga9bbade1b48363f0f486968723afefb45) |

| Functions | |
| --- | --- |
| int | [bt\_ots\_obj\_add](group__bt__ots.md#gabf59844edd0ffd434acd94bad9a7b52c) (struct bt\_ots \*ots, const struct [bt\_ots\_obj\_add\_param](structbt__ots__obj__add__param.md) \*param) |
|  | Add an object to the OTS instance. |
| int | [bt\_ots\_obj\_delete](group__bt__ots.md#ga872ba5a73fa4e617b9d48e7361af74c7) (struct bt\_ots \*ots, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Delete an object from the OTS instance. |
| void \* | [bt\_ots\_svc\_decl\_get](group__bt__ots.md#gabe637ba9febb514f7346d71696b70c73) (struct bt\_ots \*ots) |
|  | Get the service declaration attribute. |
| int | [bt\_ots\_init](group__bt__ots.md#ga1c9dcb35c8f07432fd9249a34e597819) (struct bt\_ots \*ots, struct [bt\_ots\_init\_param](structbt__ots__init__param.md) \*ots\_init) |
|  | Initialize the OTS instance. |
| struct bt\_ots \* | [bt\_ots\_free\_instance\_get](group__bt__ots.md#gafc71de8fd65212045fa26b2a81e3876d) (void) |
|  | Get a free instance of OTS from the pool. |
| int | [bt\_ots\_client\_register](group__bt__ots.md#gadefd2ccb46a686a4aa2999da5851184b) (struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst) |
|  | Register an Object Transfer Service Instance. |
| int | [bt\_ots\_client\_unregister](group__bt__ots.md#gabba031c38c7503c1f434a761d9f65df4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Unregister an Object Transfer Service Instance. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_ots\_client\_indicate\_handler](group__bt__ots.md#gac270137f15596777287f68b3d6a6a11c) (struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
|  | OTS Indicate Handler function. |
| int | [bt\_ots\_client\_read\_feature](group__bt__ots.md#gaf11589afc37efe18dcac122835a4c95d) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Read the OTS feature characteristic. |
| int | [bt\_ots\_client\_select\_id](group__bt__ots.md#ga5f2d0b0e4d54e00a1a96157fcfaf172b) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) obj\_id) |
|  | Select an object by its Object ID. |
| int | [bt\_ots\_client\_select\_first](group__bt__ots.md#ga70cae251cf40a5c3c8d2a8c7e1f1e181) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Select the first object. |
| int | [bt\_ots\_client\_select\_last](group__bt__ots.md#ga89fc03d68725de0b5f306c899452b1a8) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Select the last object. |
| int | [bt\_ots\_client\_select\_next](group__bt__ots.md#ga81997ab2f1718c6856e676eb9b3f72bb) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Select the next object. |
| int | [bt\_ots\_client\_select\_prev](group__bt__ots.md#gac84ed7f16fa86d87531d04e2957568f9) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Select the previous object. |
| int | [bt\_ots\_client\_read\_object\_metadata](group__bt__ots.md#ga936f392c880c9d1a73f2bd632e5b63e0) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) metadata) |
|  | Read the metadata of the current object. |
| int | [bt\_ots\_client\_read\_object\_data](group__bt__ots.md#ga8ad1c53325c1b77271307507317a5965) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Read the data of the current selected object. |
| int | [bt\_ots\_client\_write\_object\_data](group__bt__ots.md#ga9444b064c616718dae1577b21540fb9a) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, enum [bt\_ots\_oacp\_write\_op\_mode](group__bt__ots.md#gaebdd2b8a80948d1050d42fa3963cc863) mode) |
|  | Write the data of the current selected object. |
| int | [bt\_ots\_client\_get\_object\_checksum](group__bt__ots.md#ga9cfd057d39ce3fe9bbecaa103ec44f77) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Get the checksum of the current selected object. |
| int | [bt\_ots\_client\_decode\_dirlisting](group__bt__ots.md#gabe485816a2e536758a7ce85c593ea486) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [bt\_ots\_client\_dirlisting\_cb](group__bt__ots.md#gaa1a9db6e8aa6ee716e4fdd2e34157f46) cb) |
|  | Decode Directory Listing object into object metadata. |
| static int | [bt\_ots\_obj\_id\_to\_str](group__bt__ots.md#gac9be2770fc7f2932ea2e31392d956f0a) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) obj\_id, char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Converts binary OTS Object ID to string. |
| void | [bt\_ots\_metadata\_display](group__bt__ots.md#ga8324cc14e8812648cc3663144591af89) (struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) \*metadata, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) count) |
|  | Displays one or more object metadata as text with LOG\_INF. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [ots.h](ots_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
