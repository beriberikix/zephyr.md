---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__ots.html
original_path: doxygen/html/group__bt__ots.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Object Transfer Service (OTS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Object Transfer Service (OTS).
[More...](#details)

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
| #define | [BT\_OTS\_OBJ\_ID\_SIZE](#gad5e4a66f017facc2a185ee0a55a0c3ee)   6 |
|  | Size of OTS object ID (in bytes). |
| #define | [BT\_OTS\_OBJ\_ID\_MIN](#ga79110fa56a524754d74bf20ac6a766aa)   0x000000000100ULL |
|  | Minimum allowed value for object ID (except ID for directory listing). |
| #define | [BT\_OTS\_OBJ\_ID\_MAX](#gabd777e7a1b7adaaacfec3e084c3a9bfe)   0xFFFFFFFFFFFFULL |
|  | Maximum allowed value for object ID (except ID for directory listing). |
| #define | [OTS\_OBJ\_ID\_DIR\_LIST](#ga4a6a0b0a3c8d10f3668e61c9dee0e05e)   0x000000000000ULL |
|  | ID of the Directory Listing Object. |
| #define | [BT\_OTS\_OBJ\_ID\_MASK](#gabe3d54a6dfa0d52a97826c140c603d78)   [BIT64\_MASK](group__sys-util.md#ga1a138896caafcb2429a6483ea7412d12)(48) |
|  | Mask for OTS object IDs, preserving the 48 bits. |
| #define | [BT\_OTS\_OBJ\_ID\_STR\_LEN](#ga2754eeb7418ed762a3119fc56871d37e)   15 |
|  | Length of OTS object ID string (in bytes). |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_DELETE](#ga6ad37ee172d6518e7316b4e0ec8f27c7)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_DELETE](#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10) property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_EXECUTE](#ga2342f00ef480b279d737bcddc8e2faf0)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_EXECUTE](#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad) property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_READ](#gaba26016beff74b1b6ec75ba083cf808d)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_READ](#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102) property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_WRITE](#gaeb1a5a907478fd668199a27e20fc2173)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_WRITE](#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2) property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_APPEND](#gaa1eff1b4ee05fb91d87dcb85dd7469e1)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_APPEND](#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775) property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_TRUNCATE](#ga8f99514414958d031a4e9985c8cc976b)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_TRUNCATE](#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446) property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_PATCH](#gac36c68dfeb21bf705f87f11e847c5aed)(prop) |
|  | Set [BT\_OTS\_OBJ\_PROP\_PATCH](#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed) property. |
| #define | [BT\_OTS\_OBJ\_SET\_PROP\_MARKED](#gae21e599a85549d5cd4462c0f36c291ac)(prop) |
|  | Set [BT\_OTS\_OBJ\_SET\_PROP\_MARKED](#gae21e599a85549d5cd4462c0f36c291ac) property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_DELETE](#ga7a735cf89c9986624e34b183282a65ee)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_DELETE](#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10) property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_EXECUTE](#ga90619bdcf5ec9a942f7d81f6c87465fc)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_EXECUTE](#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad) property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_READ](#gae846afdc9f6c40b2bf6d2ae67deb8eef)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_READ](#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102) property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_WRITE](#ga9769628cbe2c81161607c6518d3d4798)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_WRITE](#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2) property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_APPEND](#gaccbf81f9a9ebcc70801739a4a8fafcd8)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_APPEND](#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775) property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_TRUNCATE](#gac7b6632aac554db5b4d5b9f3e8bf78b4)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_TRUNCATE](#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446) property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_PATCH](#ga6c8ccb5f8919f062b1b44e1b4981907d)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_PATCH](#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed) property. |
| #define | [BT\_OTS\_OBJ\_GET\_PROP\_MARKED](#gaeffab993f4fbe15090a7a626cd56f034)(prop) |
|  | Get [BT\_OTS\_OBJ\_PROP\_MARKED](#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3) property. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_CREATE](#ga8cc851f268de24fe3445a9a0c3af6abf)(feat) |
|  | Set [BT\_OTS\_OACP\_SET\_FEAT\_CREATE](#ga8cc851f268de24fe3445a9a0c3af6abf) feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_DELETE](#ga9306e9a2b8ea468f28eb73b7d412032e)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_DELETE](#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee) feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_CHECKSUM](#gaba4d7e446212dc6c2139c324d22edc10)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_CHECKSUM](#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f) feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_EXECUTE](#ga4b19d199947053e7b2f93b64ea83c29a)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_EXECUTE](#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c) feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_READ](#ga5508cf6698e2927333f31cb0cffce831)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_READ](#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465) feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_WRITE](#gac035cb71a2caabd16bb64d27b56e32c7)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_WRITE](#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab) feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_APPEND](#gaabae304227bed27796ad2a346963fa86)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_APPEND](#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b) feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_TRUNCATE](#gae5f0e14f685d40782952345ebe50eb3d)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_TRUNCATE](#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225) feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_PATCH](#gabca8354bc176bd819005ca213a148b87)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_PATCH](#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf) feature. |
| #define | [BT\_OTS\_OACP\_SET\_FEAT\_ABORT](#ga3bb8eb9f732947daf289dfe40e171248)(feat) |
|  | Set [BT\_OTS\_OACP\_FEAT\_ABORT](#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440) feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_CREATE](#ga058d8d1fb255ca66057c1edfc547def4)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_CREATE](#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9) feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_DELETE](#ga815632fc160921a074bec60250df47f2)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_DELETE](#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee) feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_CHECKSUM](#gabbc141c9a7d5614971b87b727cbf01af)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_CHECKSUM](#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f) feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_EXECUTE](#ga2ac0d82e8fab9fa22b5dc3396c8641ad)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_EXECUTE](#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c) feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_READ](#gac53739b9fd65124f601e92b29b9123cd)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_READ](#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465) feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_WRITE](#ga390d957c514b2f182ff3d1d0c2221822)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_WRITE](#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab) feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_APPEND](#ga36f5cc04fce18390bf1cde3e0e8a6184)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_APPEND](#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b) feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_TRUNCATE](#ga9ca79d43292354f1558943f944dd53a7)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_TRUNCATE](#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225) feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_PATCH](#gaca6591a0c7e8650fa827a7a43fcca81e)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_PATCH](#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf) feature. |
| #define | [BT\_OTS\_OACP\_GET\_FEAT\_ABORT](#ga196a2aceeecd620baacf0727e1427341)(feat) |
|  | Get [BT\_OTS\_OACP\_FEAT\_ABORT](#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440) feature. |
| #define | [BT\_OTS\_OLCP\_SET\_FEAT\_GO\_TO](#gafe219709f2bd318af66cad4e118df658)(feat) |
|  | Set [BT\_OTS\_OLCP\_FEAT\_GO\_TO](#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713) feature. |
| #define | [BT\_OTS\_OLCP\_SET\_FEAT\_ORDER](#ga1248c694ff2d9ded862f37d03d98e2f0)(feat) |
|  | Set [BT\_OTS\_OLCP\_FEAT\_ORDER](#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d) feature. |
| #define | [BT\_OTS\_OLCP\_SET\_FEAT\_NUM\_REQ](#ga1cee6e1affdff27aa0ba6a655c9bf09c)(feat) |
|  | Set [BT\_OTS\_OLCP\_FEAT\_NUM\_REQ](#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660) feature. |
| #define | [BT\_OTS\_OLCP\_SET\_FEAT\_CLEAR](#ga7a3f8d3b725c8c31d5e3062d46db4438)(feat) |
|  | Set [BT\_OTS\_OLCP\_FEAT\_CLEAR](#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af) feature. |
| #define | [BT\_OTS\_OLCP\_GET\_FEAT\_GO\_TO](#ga7ec49843849613ee3f8f72209cae68c2)(feat) |
|  | Get [BT\_OTS\_OLCP\_GET\_FEAT\_GO\_TO](#ga7ec49843849613ee3f8f72209cae68c2) feature. |
| #define | [BT\_OTS\_OLCP\_GET\_FEAT\_ORDER](#gad4393e56c94c2484cd344b48cb54b255)(feat) |
|  | Get [BT\_OTS\_OLCP\_GET\_FEAT\_ORDER](#gad4393e56c94c2484cd344b48cb54b255) feature. |
| #define | [BT\_OTS\_OLCP\_GET\_FEAT\_NUM\_REQ](#ga2a1a62e410586b1117fd3571e42363d8)(feat) |
|  | Get [BT\_OTS\_OLCP\_GET\_FEAT\_NUM\_REQ](#ga2a1a62e410586b1117fd3571e42363d8) feature. |
| #define | [BT\_OTS\_OLCP\_GET\_FEAT\_CLEAR](#ga0f57d172615d1c6ea857506dc0c10e55)(feat) |
|  | Get [BT\_OTS\_OLCP\_GET\_FEAT\_CLEAR](#ga0f57d172615d1c6ea857506dc0c10e55) feature. |
| #define | [BT\_OTS\_DATE\_TIME\_FIELD\_SIZE](#ga56cd1131414fa19e3ec30e2a1a241689)   7 |
| #define | [BT\_OTS\_STOP](#ga4f18ea10855379414dd8a70b6c119d6b)   0 |
| #define | [BT\_OTS\_CONTINUE](#ga8ccd0dec55069aa01bb9740a6520fd51)   1 |

| Typedefs | |
| --- | --- |
| typedef int(\* | [bt\_ots\_client\_dirlisting\_cb](#gaa1a9db6e8aa6ee716e4fdd2e34157f46)) (struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) \*meta) |
|  | Directory listing object metadata callback. |

| Enumerations | |
| --- | --- |
| enum | {     [BT\_OTS\_OBJ\_PROP\_DELETE](#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10) = 0 , [BT\_OTS\_OBJ\_PROP\_EXECUTE](#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad) = 1 , [BT\_OTS\_OBJ\_PROP\_READ](#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102) = 2 , [BT\_OTS\_OBJ\_PROP\_WRITE](#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2) = 3 ,     [BT\_OTS\_OBJ\_PROP\_APPEND](#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775) = 4 , [BT\_OTS\_OBJ\_PROP\_TRUNCATE](#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446) = 5 , [BT\_OTS\_OBJ\_PROP\_PATCH](#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed) = 6 , [BT\_OTS\_OBJ\_PROP\_MARKED](#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3) = 7   } |
|  | Properties of an OTS object. [More...](#gaea054a2be05dca63c0cd0375649af26b) |
| enum | {     [BT\_OTS\_OACP\_FEAT\_CREATE](#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9) = 0 , [BT\_OTS\_OACP\_FEAT\_DELETE](#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee) = 1 , [BT\_OTS\_OACP\_FEAT\_CHECKSUM](#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f) = 2 , [BT\_OTS\_OACP\_FEAT\_EXECUTE](#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c) = 3 ,     [BT\_OTS\_OACP\_FEAT\_READ](#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465) = 4 , [BT\_OTS\_OACP\_FEAT\_WRITE](#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab) = 5 , [BT\_OTS\_OACP\_FEAT\_APPEND](#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b) = 6 , [BT\_OTS\_OACP\_FEAT\_TRUNCATE](#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225) = 7 ,     [BT\_OTS\_OACP\_FEAT\_PATCH](#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf) = 8 , [BT\_OTS\_OACP\_FEAT\_ABORT](#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440) = 9   } |
|  | Object Action Control Point Feature bits. [More...](#ga141f5762339600942eb229bfdc183ebb) |
| enum | [bt\_ots\_oacp\_write\_op\_mode](#gaebdd2b8a80948d1050d42fa3963cc863) { [BT\_OTS\_OACP\_WRITE\_OP\_MODE\_NONE](#ggaebdd2b8a80948d1050d42fa3963cc863a1c2d68fccd8f252b54a11879a6dd53ab) = 0 , [BT\_OTS\_OACP\_WRITE\_OP\_MODE\_TRUNCATE](#ggaebdd2b8a80948d1050d42fa3963cc863a91d201f7f01809e2af10e10008d4eb8a) = BIT(1) } |
| enum | { [BT\_OTS\_OLCP\_FEAT\_GO\_TO](#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713) = 0 , [BT\_OTS\_OLCP\_FEAT\_ORDER](#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d) = 1 , [BT\_OTS\_OLCP\_FEAT\_NUM\_REQ](#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660) = 2 , [BT\_OTS\_OLCP\_FEAT\_CLEAR](#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af) = 3 } |
|  | Object List Control Point Feature bits. [More...](#ga39716a5c8e5097ad2ddeaf8db407024e) |
| enum | {     [BT\_OTS\_METADATA\_REQ\_NAME](#gga9bbade1b48363f0f486968723afefb45ada06e9d807f7c197bd332c0e7ca21ffb) = BIT(0) , [BT\_OTS\_METADATA\_REQ\_TYPE](#gga9bbade1b48363f0f486968723afefb45aff8f3ce21a85b397b64b5d03a5fe8af9) = BIT(1) , [BT\_OTS\_METADATA\_REQ\_SIZE](#gga9bbade1b48363f0f486968723afefb45aca9770dfa7fbec3a6bc0bccb4e9e41e5) = BIT(2) , [BT\_OTS\_METADATA\_REQ\_CREATED](#gga9bbade1b48363f0f486968723afefb45ac47367e5e775fa6690ac5bc03e187095) = BIT(3) ,     [BT\_OTS\_METADATA\_REQ\_MODIFIED](#gga9bbade1b48363f0f486968723afefb45a35a3d25b637ac80e658102f27aeb7f5e) = BIT(4) , [BT\_OTS\_METADATA\_REQ\_ID](#gga9bbade1b48363f0f486968723afefb45a44cb8e7804c86fce7c2eab3f3f0743c2) = BIT(5) , [BT\_OTS\_METADATA\_REQ\_PROPS](#gga9bbade1b48363f0f486968723afefb45af7c08a3c53273ac6452f607a23826e2f) = BIT(6) , [BT\_OTS\_METADATA\_REQ\_ALL](#gga9bbade1b48363f0f486968723afefb45a04e4ab3e722a23370a63288c3eba8cdf) = 0x7F   } |
|  | Object metadata request bit field values. [More...](#ga9bbade1b48363f0f486968723afefb45) |

| Functions | |
| --- | --- |
| int | [bt\_ots\_obj\_add](#gabf59844edd0ffd434acd94bad9a7b52c) (struct bt\_ots \*ots, const struct [bt\_ots\_obj\_add\_param](structbt__ots__obj__add__param.md) \*param) |
|  | Add an object to the OTS instance. |
| int | [bt\_ots\_obj\_delete](#ga872ba5a73fa4e617b9d48e7361af74c7) (struct bt\_ots \*ots, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Delete an object from the OTS instance. |
| void \* | [bt\_ots\_svc\_decl\_get](#gabe637ba9febb514f7346d71696b70c73) (struct bt\_ots \*ots) |
|  | Get the service declaration attribute. |
| int | [bt\_ots\_init](#ga1c9dcb35c8f07432fd9249a34e597819) (struct bt\_ots \*ots, struct [bt\_ots\_init\_param](structbt__ots__init__param.md) \*ots\_init) |
|  | Initialize the OTS instance. |
| struct bt\_ots \* | [bt\_ots\_free\_instance\_get](#gafc71de8fd65212045fa26b2a81e3876d) (void) |
|  | Get a free instance of OTS from the pool. |
| int | [bt\_ots\_client\_register](#gadefd2ccb46a686a4aa2999da5851184b) (struct [bt\_ots\_client](structbt__ots__client.md) \*ots\_inst) |
|  | Register an Object Transfer Service Instance. |
| int | [bt\_ots\_client\_unregister](#gabba031c38c7503c1f434a761d9f65df4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Unregister an Object Transfer Service Instance. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_ots\_client\_indicate\_handler](#gac270137f15596777287f68b3d6a6a11c) (struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
|  | OTS Indicate Handler function. |
| int | [bt\_ots\_client\_read\_feature](#gaf11589afc37efe18dcac122835a4c95d) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Read the OTS feature characteristic. |
| int | [bt\_ots\_client\_select\_id](#ga5f2d0b0e4d54e00a1a96157fcfaf172b) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) obj\_id) |
|  | Select an object by its Object ID. |
| int | [bt\_ots\_client\_select\_first](#ga70cae251cf40a5c3c8d2a8c7e1f1e181) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Select the first object. |
| int | [bt\_ots\_client\_select\_last](#ga89fc03d68725de0b5f306c899452b1a8) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Select the last object. |
| int | [bt\_ots\_client\_select\_next](#ga81997ab2f1718c6856e676eb9b3f72bb) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Select the next object. |
| int | [bt\_ots\_client\_select\_prev](#gac84ed7f16fa86d87531d04e2957568f9) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Select the previous object. |
| int | [bt\_ots\_client\_read\_object\_metadata](#ga936f392c880c9d1a73f2bd632e5b63e0) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) metadata) |
|  | Read the metadata of the current object. |
| int | [bt\_ots\_client\_read\_object\_data](#ga8ad1c53325c1b77271307507317a5965) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn) |
|  | Read the data of the current selected object. |
| int | [bt\_ots\_client\_write\_object\_data](#ga9444b064c616718dae1577b21540fb9a) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, enum [bt\_ots\_oacp\_write\_op\_mode](#gaebdd2b8a80948d1050d42fa3963cc863) mode) |
|  | Write the data of the current selected object. |
| int | [bt\_ots\_client\_get\_object\_checksum](#ga9cfd057d39ce3fe9bbecaa103ec44f77) (struct [bt\_ots\_client](structbt__ots__client.md) \*otc\_inst, struct bt\_conn \*conn, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Get the checksum of the current selected object. |
| int | [bt\_ots\_client\_decode\_dirlisting](#gabe485816a2e536758a7ce85c593ea486) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [bt\_ots\_client\_dirlisting\_cb](#gaa1a9db6e8aa6ee716e4fdd2e34157f46) cb) |
|  | Decode Directory Listing object into object metadata. |
| static int | [bt\_ots\_obj\_id\_to\_str](#gac9be2770fc7f2932ea2e31392d956f0a) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) obj\_id, char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Converts binary OTS Object ID to string. |
| void | [bt\_ots\_metadata\_display](#ga8324cc14e8812648cc3663144591af89) (struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) \*metadata, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) count) |
|  | Displays one or more object metadata as text with LOG\_INF. |

## Detailed Description

Object Transfer Service (OTS).

[Experimental] Users should note that the APIs can change as a part of ongoing development.

## Macro Definition Documentation

## [◆ ](#ga8ccd0dec55069aa01bb9740a6520fd51)BT\_OTS\_CONTINUE

| #define BT\_OTS\_CONTINUE   1 |
| --- |

`#include <[ots.h](ots_8h.md)>`

## [◆ ](#ga56cd1131414fa19e3ec30e2a1a241689)BT\_OTS\_DATE\_TIME\_FIELD\_SIZE

| #define BT\_OTS\_DATE\_TIME\_FIELD\_SIZE   7 |
| --- |

`#include <[ots.h](ots_8h.md)>`

## [◆ ](#ga196a2aceeecd620baacf0727e1427341)BT\_OTS\_OACP\_GET\_FEAT\_ABORT

| #define BT\_OTS\_OACP\_GET\_FEAT\_ABORT | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OACP\_FEAT\_ABORT](#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440)))

[BT\_OTS\_OACP\_FEAT\_ABORT](#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440)

@ BT\_OTS\_OACP\_FEAT\_ABORT

Bit 9 OACP Abort Op Code Supported.

**Definition** ots.h:253

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

Get [BT\_OTS\_OACP\_FEAT\_ABORT](#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga36f5cc04fce18390bf1cde3e0e8a6184)BT\_OTS\_OACP\_GET\_FEAT\_APPEND

| #define BT\_OTS\_OACP\_GET\_FEAT\_APPEND | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OACP\_FEAT\_APPEND](#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b)))

[BT\_OTS\_OACP\_FEAT\_APPEND](#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b)

@ BT\_OTS\_OACP\_FEAT\_APPEND

Bit 6 Appending Additional Data to Objects Supported.

**Definition** ots.h:244

Get [BT\_OTS\_OACP\_FEAT\_APPEND](#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#gabbc141c9a7d5614971b87b727cbf01af)BT\_OTS\_OACP\_GET\_FEAT\_CHECKSUM

| #define BT\_OTS\_OACP\_GET\_FEAT\_CHECKSUM | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OACP\_FEAT\_CHECKSUM](#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f)))

[BT\_OTS\_OACP\_FEAT\_CHECKSUM](#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f)

@ BT\_OTS\_OACP\_FEAT\_CHECKSUM

Bit 2 OACP Calculate Checksum Op Code Supported.

**Definition** ots.h:232

Get [BT\_OTS\_OACP\_FEAT\_CHECKSUM](#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga058d8d1fb255ca66057c1edfc547def4)BT\_OTS\_OACP\_GET\_FEAT\_CREATE

| #define BT\_OTS\_OACP\_GET\_FEAT\_CREATE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OACP\_FEAT\_CREATE](#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9)))

[BT\_OTS\_OACP\_FEAT\_CREATE](#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9)

@ BT\_OTS\_OACP\_FEAT\_CREATE

Bit 0 OACP Create Op Code Supported.

**Definition** ots.h:226

Get [BT\_OTS\_OACP\_FEAT\_CREATE](#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga815632fc160921a074bec60250df47f2)BT\_OTS\_OACP\_GET\_FEAT\_DELETE

| #define BT\_OTS\_OACP\_GET\_FEAT\_DELETE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OACP\_FEAT\_DELETE](#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee)))

[BT\_OTS\_OACP\_FEAT\_DELETE](#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee)

@ BT\_OTS\_OACP\_FEAT\_DELETE

Bit 1 OACP Delete Op Code Supported.

**Definition** ots.h:229

Get [BT\_OTS\_OACP\_FEAT\_DELETE](#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga2ac0d82e8fab9fa22b5dc3396c8641ad)BT\_OTS\_OACP\_GET\_FEAT\_EXECUTE

| #define BT\_OTS\_OACP\_GET\_FEAT\_EXECUTE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OACP\_FEAT\_EXECUTE](#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c)))

[BT\_OTS\_OACP\_FEAT\_EXECUTE](#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c)

@ BT\_OTS\_OACP\_FEAT\_EXECUTE

Bit 3 OACP Execute Op Code Supported.

**Definition** ots.h:235

Get [BT\_OTS\_OACP\_FEAT\_EXECUTE](#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#gaca6591a0c7e8650fa827a7a43fcca81e)BT\_OTS\_OACP\_GET\_FEAT\_PATCH

| #define BT\_OTS\_OACP\_GET\_FEAT\_PATCH | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OACP\_FEAT\_PATCH](#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf)))

[BT\_OTS\_OACP\_FEAT\_PATCH](#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf)

@ BT\_OTS\_OACP\_FEAT\_PATCH

Bit 8 Patching of Objects Supported.

**Definition** ots.h:250

Get [BT\_OTS\_OACP\_FEAT\_PATCH](#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#gac53739b9fd65124f601e92b29b9123cd)BT\_OTS\_OACP\_GET\_FEAT\_READ

| #define BT\_OTS\_OACP\_GET\_FEAT\_READ | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OACP\_FEAT\_READ](#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465)))

[BT\_OTS\_OACP\_FEAT\_READ](#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465)

@ BT\_OTS\_OACP\_FEAT\_READ

Bit 4 OACP Read Op Code Supported.

**Definition** ots.h:238

Get [BT\_OTS\_OACP\_FEAT\_READ](#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga9ca79d43292354f1558943f944dd53a7)BT\_OTS\_OACP\_GET\_FEAT\_TRUNCATE

| #define BT\_OTS\_OACP\_GET\_FEAT\_TRUNCATE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OACP\_FEAT\_TRUNCATE](#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225)))

[BT\_OTS\_OACP\_FEAT\_TRUNCATE](#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225)

@ BT\_OTS\_OACP\_FEAT\_TRUNCATE

Bit 7 Truncation of Objects Supported.

**Definition** ots.h:247

Get [BT\_OTS\_OACP\_FEAT\_TRUNCATE](#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga390d957c514b2f182ff3d1d0c2221822)BT\_OTS\_OACP\_GET\_FEAT\_WRITE

| #define BT\_OTS\_OACP\_GET\_FEAT\_WRITE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OACP\_FEAT\_WRITE](#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab)))

[BT\_OTS\_OACP\_FEAT\_WRITE](#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab)

@ BT\_OTS\_OACP\_FEAT\_WRITE

Bit 5 OACP Write Op Code Supported.

**Definition** ots.h:241

Get [BT\_OTS\_OACP\_FEAT\_WRITE](#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga3bb8eb9f732947daf289dfe40e171248)BT\_OTS\_OACP\_SET\_FEAT\_ABORT

| #define BT\_OTS\_OACP\_SET\_FEAT\_ABORT | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OACP\_FEAT\_ABORT](#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440), 1)

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)

#define WRITE\_BIT(var, bit, set)

Set or clear a bit depending on a boolean value.

**Definition** util\_macro.h:61

Set [BT\_OTS\_OACP\_FEAT\_ABORT](#gga141f5762339600942eb229bfdc183ebba01ce52dfca5f2682d81d6f2791fc6440) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#gaabae304227bed27796ad2a346963fa86)BT\_OTS\_OACP\_SET\_FEAT\_APPEND

| #define BT\_OTS\_OACP\_SET\_FEAT\_APPEND | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OACP\_FEAT\_APPEND](#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b), 1)

Set [BT\_OTS\_OACP\_FEAT\_APPEND](#gga141f5762339600942eb229bfdc183ebba1b7ba3b2a5ffc32aa859da569ededc6b) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#gaba4d7e446212dc6c2139c324d22edc10)BT\_OTS\_OACP\_SET\_FEAT\_CHECKSUM

| #define BT\_OTS\_OACP\_SET\_FEAT\_CHECKSUM | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OACP\_FEAT\_CHECKSUM](#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f), 1)

Set [BT\_OTS\_OACP\_FEAT\_CHECKSUM](#gga141f5762339600942eb229bfdc183ebba323ed129b63a7e255f6514621241721f) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga8cc851f268de24fe3445a9a0c3af6abf)BT\_OTS\_OACP\_SET\_FEAT\_CREATE

| #define BT\_OTS\_OACP\_SET\_FEAT\_CREATE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OACP\_FEAT\_CREATE](#gga141f5762339600942eb229bfdc183ebbabee225c7d1f55c19e56d7a67aaf117b9), 1)

Set [BT\_OTS\_OACP\_SET\_FEAT\_CREATE](#ga8cc851f268de24fe3445a9a0c3af6abf) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga9306e9a2b8ea468f28eb73b7d412032e)BT\_OTS\_OACP\_SET\_FEAT\_DELETE

| #define BT\_OTS\_OACP\_SET\_FEAT\_DELETE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OACP\_FEAT\_DELETE](#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee), 1)

Set [BT\_OTS\_OACP\_FEAT\_DELETE](#gga141f5762339600942eb229bfdc183ebba09d2e17b58435aff5e4322a1e22ee4ee) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga4b19d199947053e7b2f93b64ea83c29a)BT\_OTS\_OACP\_SET\_FEAT\_EXECUTE

| #define BT\_OTS\_OACP\_SET\_FEAT\_EXECUTE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OACP\_FEAT\_EXECUTE](#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c), 1)

Set [BT\_OTS\_OACP\_FEAT\_EXECUTE](#gga141f5762339600942eb229bfdc183ebba4625c869b8a58d32890b5cf1dd53103c) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#gabca8354bc176bd819005ca213a148b87)BT\_OTS\_OACP\_SET\_FEAT\_PATCH

| #define BT\_OTS\_OACP\_SET\_FEAT\_PATCH | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OACP\_FEAT\_PATCH](#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf), 1)

Set [BT\_OTS\_OACP\_FEAT\_PATCH](#gga141f5762339600942eb229bfdc183ebbabbce2855f3bd45cf53214720aff7c3cf) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga5508cf6698e2927333f31cb0cffce831)BT\_OTS\_OACP\_SET\_FEAT\_READ

| #define BT\_OTS\_OACP\_SET\_FEAT\_READ | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OACP\_FEAT\_READ](#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465), 1)

Set [BT\_OTS\_OACP\_FEAT\_READ](#gga141f5762339600942eb229bfdc183ebba2261328316b24f1b1cf8086931412465) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#gae5f0e14f685d40782952345ebe50eb3d)BT\_OTS\_OACP\_SET\_FEAT\_TRUNCATE

| #define BT\_OTS\_OACP\_SET\_FEAT\_TRUNCATE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OACP\_FEAT\_TRUNCATE](#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225), 1)

Set [BT\_OTS\_OACP\_FEAT\_TRUNCATE](#gga141f5762339600942eb229bfdc183ebba2594f36c56ab5cb471eded4d1dca1225) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#gac035cb71a2caabd16bb64d27b56e32c7)BT\_OTS\_OACP\_SET\_FEAT\_WRITE

| #define BT\_OTS\_OACP\_SET\_FEAT\_WRITE | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OACP\_FEAT\_WRITE](#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab), 1)

Set [BT\_OTS\_OACP\_FEAT\_WRITE](#gga141f5762339600942eb229bfdc183ebba43b4e48d8ec4cd335c1158eec44e2eab) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#gaccbf81f9a9ebcc70801739a4a8fafcd8)BT\_OTS\_OBJ\_GET\_PROP\_APPEND

| #define BT\_OTS\_OBJ\_GET\_PROP\_APPEND | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((prop) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OBJ\_PROP\_APPEND](#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775)))

[BT\_OTS\_OBJ\_PROP\_APPEND](#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775)

@ BT\_OTS\_OBJ\_PROP\_APPEND

Bit 4 Appending data to this object is permitted.

**Definition** ots.h:86

Get [BT\_OTS\_OBJ\_PROP\_APPEND](#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#ga7a735cf89c9986624e34b183282a65ee)BT\_OTS\_OBJ\_GET\_PROP\_DELETE

| #define BT\_OTS\_OBJ\_GET\_PROP\_DELETE | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((prop) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OBJ\_PROP\_DELETE](#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10)))

[BT\_OTS\_OBJ\_PROP\_DELETE](#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10)

@ BT\_OTS\_OBJ\_PROP\_DELETE

Bit 0 Deletion of this object is permitted.

**Definition** ots.h:71

Get [BT\_OTS\_OBJ\_PROP\_DELETE](#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#ga90619bdcf5ec9a942f7d81f6c87465fc)BT\_OTS\_OBJ\_GET\_PROP\_EXECUTE

| #define BT\_OTS\_OBJ\_GET\_PROP\_EXECUTE | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((prop) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OBJ\_PROP\_EXECUTE](#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad)))

[BT\_OTS\_OBJ\_PROP\_EXECUTE](#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad)

@ BT\_OTS\_OBJ\_PROP\_EXECUTE

Bit 1 Execution of this object is permitted.

**Definition** ots.h:74

Get [BT\_OTS\_OBJ\_PROP\_EXECUTE](#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#gaeffab993f4fbe15090a7a626cd56f034)BT\_OTS\_OBJ\_GET\_PROP\_MARKED

| #define BT\_OTS\_OBJ\_GET\_PROP\_MARKED | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((prop) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OBJ\_PROP\_MARKED](#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3)))

[BT\_OTS\_OBJ\_PROP\_MARKED](#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3)

@ BT\_OTS\_OBJ\_PROP\_MARKED

Bit 7 This object is a marked object.

**Definition** ots.h:99

Get [BT\_OTS\_OBJ\_PROP\_MARKED](#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#ga6c8ccb5f8919f062b1b44e1b4981907d)BT\_OTS\_OBJ\_GET\_PROP\_PATCH

| #define BT\_OTS\_OBJ\_GET\_PROP\_PATCH | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((prop) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OBJ\_PROP\_PATCH](#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed)))

[BT\_OTS\_OBJ\_PROP\_PATCH](#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed)

@ BT\_OTS\_OBJ\_PROP\_PATCH

Bit 6 Patching this object is permitted.

**Definition** ots.h:96

Get [BT\_OTS\_OBJ\_PROP\_PATCH](#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#gae846afdc9f6c40b2bf6d2ae67deb8eef)BT\_OTS\_OBJ\_GET\_PROP\_READ

| #define BT\_OTS\_OBJ\_GET\_PROP\_READ | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((prop) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OBJ\_PROP\_READ](#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102)))

[BT\_OTS\_OBJ\_PROP\_READ](#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102)

@ BT\_OTS\_OBJ\_PROP\_READ

Bit 2 Reading this object is permitted.

**Definition** ots.h:77

Get [BT\_OTS\_OBJ\_PROP\_READ](#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#gac7b6632aac554db5b4d5b9f3e8bf78b4)BT\_OTS\_OBJ\_GET\_PROP\_TRUNCATE

| #define BT\_OTS\_OBJ\_GET\_PROP\_TRUNCATE | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((prop) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OBJ\_PROP\_TRUNCATE](#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446)))

[BT\_OTS\_OBJ\_PROP\_TRUNCATE](#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446)

@ BT\_OTS\_OBJ\_PROP\_TRUNCATE

Bit 5 Truncation of this object is permitted.

**Definition** ots.h:89

Get [BT\_OTS\_OBJ\_PROP\_TRUNCATE](#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#ga9769628cbe2c81161607c6518d3d4798)BT\_OTS\_OBJ\_GET\_PROP\_WRITE

| #define BT\_OTS\_OBJ\_GET\_PROP\_WRITE | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((prop) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OBJ\_PROP\_WRITE](#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2)))

[BT\_OTS\_OBJ\_PROP\_WRITE](#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2)

@ BT\_OTS\_OBJ\_PROP\_WRITE

Bit 3 Writing data to this object is permitted.

**Definition** ots.h:80

Get [BT\_OTS\_OBJ\_PROP\_WRITE](#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#gabe3d54a6dfa0d52a97826c140c603d78)BT\_OTS\_OBJ\_ID\_MASK

| #define BT\_OTS\_OBJ\_ID\_MASK   [BIT64\_MASK](group__sys-util.md#ga1a138896caafcb2429a6483ea7412d12)(48) |
| --- |

`#include <[ots.h](ots_8h.md)>`

Mask for OTS object IDs, preserving the 48 bits.

## [◆ ](#gabd777e7a1b7adaaacfec3e084c3a9bfe)BT\_OTS\_OBJ\_ID\_MAX

| #define BT\_OTS\_OBJ\_ID\_MAX   0xFFFFFFFFFFFFULL |
| --- |

`#include <[ots.h](ots_8h.md)>`

Maximum allowed value for object ID (except ID for directory listing).

## [◆ ](#ga79110fa56a524754d74bf20ac6a766aa)BT\_OTS\_OBJ\_ID\_MIN

| #define BT\_OTS\_OBJ\_ID\_MIN   0x000000000100ULL |
| --- |

`#include <[ots.h](ots_8h.md)>`

Minimum allowed value for object ID (except ID for directory listing).

## [◆ ](#gad5e4a66f017facc2a185ee0a55a0c3ee)BT\_OTS\_OBJ\_ID\_SIZE

| #define BT\_OTS\_OBJ\_ID\_SIZE   6 |
| --- |

`#include <[ots.h](ots_8h.md)>`

Size of OTS object ID (in bytes).

## [◆ ](#ga2754eeb7418ed762a3119fc56871d37e)BT\_OTS\_OBJ\_ID\_STR\_LEN

| #define BT\_OTS\_OBJ\_ID\_STR\_LEN   15 |
| --- |

`#include <[ots.h](ots_8h.md)>`

Length of OTS object ID string (in bytes).

## [◆ ](#gaa1eff1b4ee05fb91d87dcb85dd7469e1)BT\_OTS\_OBJ\_SET\_PROP\_APPEND

| #define BT\_OTS\_OBJ\_SET\_PROP\_APPEND | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(prop, [BT\_OTS\_OBJ\_PROP\_APPEND](#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775), 1)

Set [BT\_OTS\_OBJ\_PROP\_APPEND](#ggaea054a2be05dca63c0cd0375649af26baa8d5d51b201d2a597c24b7ded910d775) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#ga6ad37ee172d6518e7316b4e0ec8f27c7)BT\_OTS\_OBJ\_SET\_PROP\_DELETE

| #define BT\_OTS\_OBJ\_SET\_PROP\_DELETE | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(prop, [BT\_OTS\_OBJ\_PROP\_DELETE](#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10), 1)

Set [BT\_OTS\_OBJ\_PROP\_DELETE](#ggaea054a2be05dca63c0cd0375649af26ba67e0f8a5c2bf7c8bf4985244addabb10) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#ga2342f00ef480b279d737bcddc8e2faf0)BT\_OTS\_OBJ\_SET\_PROP\_EXECUTE

| #define BT\_OTS\_OBJ\_SET\_PROP\_EXECUTE | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(prop, [BT\_OTS\_OBJ\_PROP\_EXECUTE](#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad), 1)

Set [BT\_OTS\_OBJ\_PROP\_EXECUTE](#ggaea054a2be05dca63c0cd0375649af26bac6db1a3e594fa023f92dc64bab5d84ad) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#gae21e599a85549d5cd4462c0f36c291ac)BT\_OTS\_OBJ\_SET\_PROP\_MARKED

| #define BT\_OTS\_OBJ\_SET\_PROP\_MARKED | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(prop, [BT\_OTS\_OBJ\_PROP\_MARKED](#ggaea054a2be05dca63c0cd0375649af26ba0bdca2be2e189b42017696450f2866b3), 1)

Set [BT\_OTS\_OBJ\_SET\_PROP\_MARKED](#gae21e599a85549d5cd4462c0f36c291ac) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#gac36c68dfeb21bf705f87f11e847c5aed)BT\_OTS\_OBJ\_SET\_PROP\_PATCH

| #define BT\_OTS\_OBJ\_SET\_PROP\_PATCH | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(prop, [BT\_OTS\_OBJ\_PROP\_PATCH](#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed), 1)

Set [BT\_OTS\_OBJ\_PROP\_PATCH](#ggaea054a2be05dca63c0cd0375649af26bad06eac80b28432e5a1aa7354607982ed) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#gaba26016beff74b1b6ec75ba083cf808d)BT\_OTS\_OBJ\_SET\_PROP\_READ

| #define BT\_OTS\_OBJ\_SET\_PROP\_READ | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(prop, [BT\_OTS\_OBJ\_PROP\_READ](#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102), 1)

Set [BT\_OTS\_OBJ\_PROP\_READ](#ggaea054a2be05dca63c0cd0375649af26baae41b0d5056970dac41c971526ad5102) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#ga8f99514414958d031a4e9985c8cc976b)BT\_OTS\_OBJ\_SET\_PROP\_TRUNCATE

| #define BT\_OTS\_OBJ\_SET\_PROP\_TRUNCATE | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(prop, [BT\_OTS\_OBJ\_PROP\_TRUNCATE](#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446), 1)

Set [BT\_OTS\_OBJ\_PROP\_TRUNCATE](#ggaea054a2be05dca63c0cd0375649af26baa6ecd69675ca00eda24b3af26a80d446) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#gaeb1a5a907478fd668199a27e20fc2173)BT\_OTS\_OBJ\_SET\_PROP\_WRITE

| #define BT\_OTS\_OBJ\_SET\_PROP\_WRITE | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(prop, [BT\_OTS\_OBJ\_PROP\_WRITE](#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2), 1)

Set [BT\_OTS\_OBJ\_PROP\_WRITE](#ggaea054a2be05dca63c0cd0375649af26baddbcc4e3e304491e7f6068cc2705ebb2) property.

Parameters
:   | prop | Object properties. |
    | --- | --- |

## [◆ ](#ga0f57d172615d1c6ea857506dc0c10e55)BT\_OTS\_OLCP\_GET\_FEAT\_CLEAR

| #define BT\_OTS\_OLCP\_GET\_FEAT\_CLEAR | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OLCP\_FEAT\_CLEAR](#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af)))

[BT\_OTS\_OLCP\_FEAT\_CLEAR](#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af)

@ BT\_OTS\_OLCP\_FEAT\_CLEAR

Bit 3 OLCP Clear Marking Op Code Supported.

**Definition** ots.h:417

Get [BT\_OTS\_OLCP\_GET\_FEAT\_CLEAR](#ga0f57d172615d1c6ea857506dc0c10e55) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga7ec49843849613ee3f8f72209cae68c2)BT\_OTS\_OLCP\_GET\_FEAT\_GO\_TO

| #define BT\_OTS\_OLCP\_GET\_FEAT\_GO\_TO | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OLCP\_FEAT\_GO\_TO](#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713)))

[BT\_OTS\_OLCP\_FEAT\_GO\_TO](#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713)

@ BT\_OTS\_OLCP\_FEAT\_GO\_TO

Bit 0 OLCP Go To Op Code Supported.

**Definition** ots.h:408

Get [BT\_OTS\_OLCP\_GET\_FEAT\_GO\_TO](#ga7ec49843849613ee3f8f72209cae68c2) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga2a1a62e410586b1117fd3571e42363d8)BT\_OTS\_OLCP\_GET\_FEAT\_NUM\_REQ

| #define BT\_OTS\_OLCP\_GET\_FEAT\_NUM\_REQ | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OLCP\_FEAT\_NUM\_REQ](#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660)))

[BT\_OTS\_OLCP\_FEAT\_NUM\_REQ](#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660)

@ BT\_OTS\_OLCP\_FEAT\_NUM\_REQ

Bit 2 OLCP Request Number of Objects Op Code Supported.

**Definition** ots.h:414

Get [BT\_OTS\_OLCP\_GET\_FEAT\_NUM\_REQ](#ga2a1a62e410586b1117fd3571e42363d8) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#gad4393e56c94c2484cd344b48cb54b255)BT\_OTS\_OLCP\_GET\_FEAT\_ORDER

| #define BT\_OTS\_OLCP\_GET\_FEAT\_ORDER | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

((feat) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([BT\_OTS\_OLCP\_FEAT\_ORDER](#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d)))

[BT\_OTS\_OLCP\_FEAT\_ORDER](#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d)

@ BT\_OTS\_OLCP\_FEAT\_ORDER

Bit 1 OLCP Order Op Code Supported.

**Definition** ots.h:411

Get [BT\_OTS\_OLCP\_GET\_FEAT\_ORDER](#gad4393e56c94c2484cd344b48cb54b255) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga7a3f8d3b725c8c31d5e3062d46db4438)BT\_OTS\_OLCP\_SET\_FEAT\_CLEAR

| #define BT\_OTS\_OLCP\_SET\_FEAT\_CLEAR | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OLCP\_FEAT\_CLEAR](#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af), 1)

Set [BT\_OTS\_OLCP\_FEAT\_CLEAR](#gga39716a5c8e5097ad2ddeaf8db407024ea823c63fcb7513849433f43f32472d5af) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#gafe219709f2bd318af66cad4e118df658)BT\_OTS\_OLCP\_SET\_FEAT\_GO\_TO

| #define BT\_OTS\_OLCP\_SET\_FEAT\_GO\_TO | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OLCP\_FEAT\_GO\_TO](#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713), 1)

Set [BT\_OTS\_OLCP\_FEAT\_GO\_TO](#gga39716a5c8e5097ad2ddeaf8db407024eafc61637c1a09549edb4152ffb7dbf713) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga1cee6e1affdff27aa0ba6a655c9bf09c)BT\_OTS\_OLCP\_SET\_FEAT\_NUM\_REQ

| #define BT\_OTS\_OLCP\_SET\_FEAT\_NUM\_REQ | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OLCP\_FEAT\_NUM\_REQ](#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660), 1)

Set [BT\_OTS\_OLCP\_FEAT\_NUM\_REQ](#gga39716a5c8e5097ad2ddeaf8db407024ea5a7c5fdfe81fd2e65fe7d259f966c660) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga1248c694ff2d9ded862f37d03d98e2f0)BT\_OTS\_OLCP\_SET\_FEAT\_ORDER

| #define BT\_OTS\_OLCP\_SET\_FEAT\_ORDER | ( |  | *feat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

**Value:**

[WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(feat, [BT\_OTS\_OLCP\_FEAT\_ORDER](#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d), 1)

Set [BT\_OTS\_OLCP\_FEAT\_ORDER](#gga39716a5c8e5097ad2ddeaf8db407024ea327a18e0d3a1bca70b4753c19e7d840d) feature.

Parameters
:   | feat | OTS features. |
    | --- | --- |

## [◆ ](#ga4f18ea10855379414dd8a70b6c119d6b)BT\_OTS\_STOP

| #define BT\_OTS\_STOP   0 |
| --- |

`#include <[ots.h](ots_8h.md)>`

## [◆ ](#ga4a6a0b0a3c8d10f3668e61c9dee0e05e)OTS\_OBJ\_ID\_DIR\_LIST

| #define OTS\_OBJ\_ID\_DIR\_LIST   0x000000000000ULL |
| --- |

`#include <[ots.h](ots_8h.md)>`

ID of the Directory Listing Object.

## Typedef Documentation

## [◆ ](#gaa1a9db6e8aa6ee716e4fdd2e34157f46)bt\_ots\_client\_dirlisting\_cb

| typedef int(\* bt\_ots\_client\_dirlisting\_cb) (struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) \*meta) |
| --- |

`#include <[ots.h](ots_8h.md)>`

Directory listing object metadata callback.

If a directory listing is decoded using [bt\_ots\_client\_decode\_dirlisting()](#gabe485816a2e536758a7ce85c593ea486), this callback will be called for each object in the directory listing.

Parameters
:   | meta | The metadata of the decoded object |
    | --- | --- |

Returns
:   int BT\_OTS\_STOP or BT\_OTS\_CONTINUE. BT\_OTS\_STOP can be used to stop the decoding.

## Enumeration Type Documentation

## [◆ ](#gaea054a2be05dca63c0cd0375649af26b)anonymous enum

| anonymous enum |
| --- |

`#include <[ots.h](ots_8h.md)>`

Properties of an OTS object.

| Enumerator | |
| --- | --- |
| BT\_OTS\_OBJ\_PROP\_DELETE | Bit 0 Deletion of this object is permitted. |
| BT\_OTS\_OBJ\_PROP\_EXECUTE | Bit 1 Execution of this object is permitted. |
| BT\_OTS\_OBJ\_PROP\_READ | Bit 2 Reading this object is permitted. |
| BT\_OTS\_OBJ\_PROP\_WRITE | Bit 3 Writing data to this object is permitted. |
| BT\_OTS\_OBJ\_PROP\_APPEND | Bit 4 Appending data to this object is permitted.  Appending data increases its Allocated Size. |
| BT\_OTS\_OBJ\_PROP\_TRUNCATE | Bit 5 Truncation of this object is permitted. |
| BT\_OTS\_OBJ\_PROP\_PATCH | Bit 6 Patching this object is permitted.  Patching this object overwrites some of the object's existing contents. |
| BT\_OTS\_OBJ\_PROP\_MARKED | Bit 7 This object is a marked object. |

## [◆ ](#ga39716a5c8e5097ad2ddeaf8db407024e)anonymous enum

| anonymous enum |
| --- |

`#include <[ots.h](ots_8h.md)>`

Object List Control Point Feature bits.

| Enumerator | |
| --- | --- |
| BT\_OTS\_OLCP\_FEAT\_GO\_TO | Bit 0 OLCP Go To Op Code Supported. |
| BT\_OTS\_OLCP\_FEAT\_ORDER | Bit 1 OLCP Order Op Code Supported. |
| BT\_OTS\_OLCP\_FEAT\_NUM\_REQ | Bit 2 OLCP Request Number of Objects Op Code Supported. |
| BT\_OTS\_OLCP\_FEAT\_CLEAR | Bit 3 OLCP Clear Marking Op Code Supported. |

## [◆ ](#ga9bbade1b48363f0f486968723afefb45)anonymous enum

| anonymous enum |
| --- |

`#include <[ots.h](ots_8h.md)>`

Object metadata request bit field values.

| Enumerator | |
| --- | --- |
| BT\_OTS\_METADATA\_REQ\_NAME | Request object name. |
| BT\_OTS\_METADATA\_REQ\_TYPE | Request object type. |
| BT\_OTS\_METADATA\_REQ\_SIZE | Request object size. |
| BT\_OTS\_METADATA\_REQ\_CREATED | Request object first created time. |
| BT\_OTS\_METADATA\_REQ\_MODIFIED | Request object last modified time. |
| BT\_OTS\_METADATA\_REQ\_ID | Request object ID. |
| BT\_OTS\_METADATA\_REQ\_PROPS | Request object properties. |
| BT\_OTS\_METADATA\_REQ\_ALL | Request all object metadata. |

## [◆ ](#ga141f5762339600942eb229bfdc183ebb)anonymous enum

| anonymous enum |
| --- |

`#include <[ots.h](ots_8h.md)>`

Object Action Control Point Feature bits.

| Enumerator | |
| --- | --- |
| BT\_OTS\_OACP\_FEAT\_CREATE | Bit 0 OACP Create Op Code Supported. |
| BT\_OTS\_OACP\_FEAT\_DELETE | Bit 1 OACP Delete Op Code Supported. |
| BT\_OTS\_OACP\_FEAT\_CHECKSUM | Bit 2 OACP Calculate Checksum Op Code Supported. |
| BT\_OTS\_OACP\_FEAT\_EXECUTE | Bit 3 OACP Execute Op Code Supported. |
| BT\_OTS\_OACP\_FEAT\_READ | Bit 4 OACP Read Op Code Supported. |
| BT\_OTS\_OACP\_FEAT\_WRITE | Bit 5 OACP Write Op Code Supported. |
| BT\_OTS\_OACP\_FEAT\_APPEND | Bit 6 Appending Additional Data to Objects Supported. |
| BT\_OTS\_OACP\_FEAT\_TRUNCATE | Bit 7 Truncation of Objects Supported. |
| BT\_OTS\_OACP\_FEAT\_PATCH | Bit 8 Patching of Objects Supported. |
| BT\_OTS\_OACP\_FEAT\_ABORT | Bit 9 OACP Abort Op Code Supported. |

## [◆ ](#gaebdd2b8a80948d1050d42fa3963cc863)bt\_ots\_oacp\_write\_op\_mode

| enum [bt\_ots\_oacp\_write\_op\_mode](#gaebdd2b8a80948d1050d42fa3963cc863) |
| --- |

`#include <[ots.h](ots_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_OTS\_OACP\_WRITE\_OP\_MODE\_NONE |  |
| BT\_OTS\_OACP\_WRITE\_OP\_MODE\_TRUNCATE |  |

## Function Documentation

## [◆ ](#gabe485816a2e536758a7ce85c593ea486)bt\_ots\_client\_decode\_dirlisting()

| int bt\_ots\_client\_decode\_dirlisting | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *length*, |
|  |  | [bt\_ots\_client\_dirlisting\_cb](#gaa1a9db6e8aa6ee716e4fdd2e34157f46) | *cb* ) |

`#include <[ots.h](ots_8h.md)>`

Decode Directory Listing object into object metadata.

If the Directory Listing object contains multiple objects, then the callback will be called for each of them.

Parameters
:   | data | The data received for the directory listing object. |
    | --- | --- |
    | length | Length of the data. |
    | cb | The callback that will be called for each object. |

## [◆ ](#ga9cfd057d39ce3fe9bbecaa103ec44f77)bt\_ots\_client\_get\_object\_checksum()

| int bt\_ots\_client\_get\_object\_checksum | ( | struct [bt\_ots\_client](structbt__ots__client.md) \* | *otc\_inst*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \* | *conn*, |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[ots.h](ots_8h.md)>`

Get the checksum of the current selected object.

This will trigger an OACP calculate checksum operation for the current object with a specified offset and length.

The checksum goes to OACP IND and obj\_checksum\_calculated() callback.

Parameters
:   | otc\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | Pointer to the connection object. |
    | offset | Offset to calculate, usually 0. |
    | len | Len of data to calculate checksum for. May be less than the current object's size, but shall not be larger. |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#gac270137f15596777287f68b3d6a6a11c)bt\_ots\_client\_indicate\_handler()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_ots\_client\_indicate\_handler | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \* | *params*, |
|  |  | const void \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *length* ) |

`#include <[ots.h](ots_8h.md)>`

OTS Indicate Handler function.

Set this function as callback for indicate handler when discovering OTS.

Parameters
:   | conn | Connection object. May be NULL, indicating that the peer is being unpaired. |
    | --- | --- |
    | params | Subscription parameters. |
    | data | Attribute value data. If NULL then subscription was removed. |
    | length | Attribute value length. |

## [◆ ](#gaf11589afc37efe18dcac122835a4c95d)bt\_ots\_client\_read\_feature()

| int bt\_ots\_client\_read\_feature | ( | struct [bt\_ots\_client](structbt__ots__client.md) \* | *otc\_inst*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \* | *conn* ) |

`#include <[ots.h](ots_8h.md)>`

Read the OTS feature characteristic.

Parameters
:   | otc\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | Pointer to the connection object. |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#ga8ad1c53325c1b77271307507317a5965)bt\_ots\_client\_read\_object\_data()

| int bt\_ots\_client\_read\_object\_data | ( | struct [bt\_ots\_client](structbt__ots__client.md) \* | *otc\_inst*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \* | *conn* ) |

`#include <[ots.h](ots_8h.md)>`

Read the data of the current selected object.

This will trigger an OACP read operation for the current size of the object with a 0 offset and then expect receiving the content via the L2CAP CoC.

The data of the object are returned in the obj\_data\_read() callback.

Parameters
:   | otc\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | Pointer to the connection object. |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#ga936f392c880c9d1a73f2bd632e5b63e0)bt\_ots\_client\_read\_object\_metadata()

| int bt\_ots\_client\_read\_object\_metadata | ( | struct [bt\_ots\_client](structbt__ots__client.md) \* | *otc\_inst*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \* | *conn*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *metadata* ) |

`#include <[ots.h](ots_8h.md)>`

Read the metadata of the current object.

The metadata are returned in the obj\_metadata\_read() callback.

Parameters
:   | otc\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | Pointer to the connection object. |
    | metadata | Bitfield (BT\_OTS\_METADATA\_REQ\_\*) of the metadata to read. |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#gadefd2ccb46a686a4aa2999da5851184b)bt\_ots\_client\_register()

| int bt\_ots\_client\_register | ( | struct [bt\_ots\_client](structbt__ots__client.md) \* | *ots\_inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

Register an Object Transfer Service Instance.

Register an Object Transfer Service instance discovered on the peer. Call this function when an OTS instance is discovered (discovery is to be handled by the higher layer).

Parameters
:   | [in] | ots\_inst | Discovered OTS instance. |
    | --- | --- | --- |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#ga70cae251cf40a5c3c8d2a8c7e1f1e181)bt\_ots\_client\_select\_first()

| int bt\_ots\_client\_select\_first | ( | struct [bt\_ots\_client](structbt__ots__client.md) \* | *otc\_inst*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \* | *conn* ) |

`#include <[ots.h](ots_8h.md)>`

Select the first object.

Parameters
:   | otc\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | Pointer to the connection object. |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#ga5f2d0b0e4d54e00a1a96157fcfaf172b)bt\_ots\_client\_select\_id()

| int bt\_ots\_client\_select\_id | ( | struct [bt\_ots\_client](structbt__ots__client.md) \* | *otc\_inst*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \* | *conn*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *obj\_id* ) |

`#include <[ots.h](ots_8h.md)>`

Select an object by its Object ID.

Parameters
:   | otc\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | Pointer to the connection object. |
    | obj\_id | Object's ID. |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#ga89fc03d68725de0b5f306c899452b1a8)bt\_ots\_client\_select\_last()

| int bt\_ots\_client\_select\_last | ( | struct [bt\_ots\_client](structbt__ots__client.md) \* | *otc\_inst*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \* | *conn* ) |

`#include <[ots.h](ots_8h.md)>`

Select the last object.

Parameters
:   | otc\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | Pointer to the connection object. |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#ga81997ab2f1718c6856e676eb9b3f72bb)bt\_ots\_client\_select\_next()

| int bt\_ots\_client\_select\_next | ( | struct [bt\_ots\_client](structbt__ots__client.md) \* | *otc\_inst*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \* | *conn* ) |

`#include <[ots.h](ots_8h.md)>`

Select the next object.

Parameters
:   | otc\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | Pointer to the connection object. |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#gac84ed7f16fa86d87531d04e2957568f9)bt\_ots\_client\_select\_prev()

| int bt\_ots\_client\_select\_prev | ( | struct [bt\_ots\_client](structbt__ots__client.md) \* | *otc\_inst*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \* | *conn* ) |

`#include <[ots.h](ots_8h.md)>`

Select the previous object.

Parameters
:   | otc\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | Pointer to the connection object. |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#gabba031c38c7503c1f434a761d9f65df4)bt\_ots\_client\_unregister()

| int bt\_ots\_client\_unregister | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

Unregister an Object Transfer Service Instance.

Unregister an Object Transfer Service instance when disconnect from the peer. Call this function when an ACL using OTS instance is disconnected.

Parameters
:   | [in] | index | Index of OTS instance. |
    | --- | --- | --- |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#ga9444b064c616718dae1577b21540fb9a)bt\_ots\_client\_write\_object\_data()

| int bt\_ots\_client\_write\_object\_data | ( | struct [bt\_ots\_client](structbt__ots__client.md) \* | *otc\_inst*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \* | *conn*, |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | enum [bt\_ots\_oacp\_write\_op\_mode](#gaebdd2b8a80948d1050d42fa3963cc863) | *mode* ) |

`#include <[ots.h](ots_8h.md)>`

Write the data of the current selected object.

This will trigger an OACP write operation for the current object with a specified offset and then expect transferring the content via the L2CAP CoC.

The length of the data written to object is returned in the obj\_data\_written() callback.

Parameters
:   | otc\_inst | Pointer to the OTC instance. |
    | --- | --- |
    | conn | Pointer to the connection object. |
    | buf | Pointer to the data buffer to be written. |
    | len | Size of data. |
    | offset | Offset to write, usually 0. |
    | mode | Mode Parameter for OACP Write Op Code. See [bt\_ots\_oacp\_write\_op\_mode](#gaebdd2b8a80948d1050d42fa3963cc863). |

Returns
:   int 0 if success, ERRNO on failure.

## [◆ ](#gafc71de8fd65212045fa26b2a81e3876d)bt\_ots\_free\_instance\_get()

| struct bt\_ots \* bt\_ots\_free\_instance\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

Get a free instance of OTS from the pool.

Returns
:   OTS instance in case of success or NULL in case of error.

## [◆ ](#ga1c9dcb35c8f07432fd9249a34e597819)bt\_ots\_init()

| int bt\_ots\_init | ( | struct bt\_ots \* | *ots*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_ots\_init\_param](structbt__ots__init__param.md) \* | *ots\_init* ) |

`#include <[ots.h](ots_8h.md)>`

Initialize the OTS instance.

Parameters
:   | ots | OTS instance. |
    | --- | --- |
    | ots\_init | OTS initialization descriptor. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga8324cc14e8812648cc3663144591af89)bt\_ots\_metadata\_display()

| void bt\_ots\_metadata\_display | ( | struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) \* | *metadata*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *count* ) |

`#include <[ots.h](ots_8h.md)>`

Displays one or more object metadata as text with LOG\_INF.

Parameters
:   | metadata | Pointer to the first (or only) metadata in an array. |
    | --- | --- |
    | count | Number of metadata objects to display information of. |

## [◆ ](#gabf59844edd0ffd434acd94bad9a7b52c)bt\_ots\_obj\_add()

| int bt\_ots\_obj\_add | ( | struct bt\_ots \* | *ots*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_ots\_obj\_add\_param](structbt__ots__obj__add__param.md) \* | *param* ) |

`#include <[ots.h](ots_8h.md)>`

Add an object to the OTS instance.

This function adds an object to the OTS database. When the object is being added, a callback obj\_created() is called to notify the user about a new object ID.

Parameters
:   | ots | OTS instance. |
    | --- | --- |
    | param | Object addition parameters. |

Returns
:   ID of created object in case of success.
:   negative value in case of error.

## [◆ ](#ga872ba5a73fa4e617b9d48e7361af74c7)bt\_ots\_obj\_delete()

| int bt\_ots\_obj\_delete | ( | struct bt\_ots \* | *ots*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* ) |

`#include <[ots.h](ots_8h.md)>`

Delete an object from the OTS instance.

This function deletes an object from the OTS database. When the object is deleted a callback obj\_deleted() is called to notify the user about this event. At this point, it is possible to free allocated buffer for object data.

Parameters
:   | ots | OTS instance. |
    | --- | --- |
    | id | ID of the object to be deleted (uint48). |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gac9be2770fc7f2932ea2e31392d956f0a)bt\_ots\_obj\_id\_to\_str()

| | int bt\_ots\_obj\_id\_to\_str | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *obj\_id*, | | --- | --- | --- | --- | |  |  | char \* | *str*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

Converts binary OTS Object ID to string.

Parameters
:   | obj\_id | Object ID. |
    | --- | --- |
    | str | Address of user buffer with enough room to store formatted string containing binary Object ID. |
    | len | Length of data to be copied to user string buffer. Refer to BT\_OTS\_OBJ\_ID\_STR\_LEN about recommended value. |

Returns
:   Number of successfully formatted bytes from binary ID.

## [◆ ](#gabe637ba9febb514f7346d71696b70c73)bt\_ots\_svc\_decl\_get()

| void \* bt\_ots\_svc\_decl\_get | ( | struct bt\_ots \* | *ots* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ots.h](ots_8h.md)>`

Get the service declaration attribute.

This function is enabled for CONFIG\_BT\_OTS\_SECONDARY\_SVC configuration. The first service attribute can be included in any other GATT service.

Parameters
:   | ots | OTS instance. |
    | --- | --- |

Returns
:   The first OTS attribute instance.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
