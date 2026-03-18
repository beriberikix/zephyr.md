---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__net__buf.html
original_path: doxygen/html/group__net__buf.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Buffer Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network buffer library.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_buf\_simple](structnet__buf__simple.md) |
|  | Simple network buffer representation. [More...](structnet__buf__simple.md#details) |
| struct | [net\_buf\_simple\_state](structnet__buf__simple__state.md) |
|  | Parsing state of a buffer. [More...](structnet__buf__simple__state.md#details) |
| struct | [net\_buf](structnet__buf.md) |
|  | Network buffer representation. [More...](structnet__buf.md#details) |
| struct | [net\_buf\_pool](structnet__buf__pool.md) |
|  | Network buffer pool representation. [More...](structnet__buf__pool.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_BUF\_SIMPLE\_DEFINE](#gaf85aa0b705bb4fbe2630191fde802501)(\_name, \_size) |
|  | Define a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") stack variable. |
| #define | [NET\_BUF\_SIMPLE\_DEFINE\_STATIC](#ga21ced8b3082d57bf071008de5fffc0f4)(\_name, \_size) |
|  | Define a static [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") variable. |
| #define | [NET\_BUF\_SIMPLE](#ga0b01dc80027d13b1895379d4d1397207)(\_size) |
|  | Define a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") stack variable and get a pointer to it. |
| #define | [NET\_BUF\_EXTERNAL\_DATA](#gaaeacbdf3cfda12691c75253015e5c19a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag indicating that the buffer's associated data pointer, points to externally allocated memory. |
| #define | [NET\_BUF\_POOL\_HEAP\_DEFINE](#ga61671ac866081d31dfe9eddbf3b6f210)(\_name, \_count, \_ud\_size, \_destroy) |
|  | Define a new pool for buffers using the heap for the data. |
| #define | [NET\_BUF\_POOL\_FIXED\_DEFINE](#gacc53824e01db7935bcc9cad564b716cd)(\_name, \_count, \_data\_size, \_ud\_size, \_destroy) |
|  | Define a new pool for buffers based on fixed-size data. |
| #define | [NET\_BUF\_POOL\_VAR\_DEFINE](#ga90e691e793c964847d737f5ecf7646ec)(\_name, \_count, \_data\_size, \_ud\_size, \_destroy) |
|  | Define a new pool for buffers with variable size payloads. |
| #define | [NET\_BUF\_POOL\_DEFINE](#ga810aba8ba321fd012edc238ea9fe19dc)(\_name, \_count, \_size, \_ud\_size, \_destroy) |
|  | Define a new pool for buffers. |

| Typedefs | |
| --- | --- |
| typedef struct [net\_buf](structnet__buf.md) \*(\* | [net\_buf\_allocator\_cb](#ga9b74d094a45daf74cd230eaa4fcbc065)) ([k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Network buffer allocator callback. |

| Functions | |
| --- | --- |
| static void | [net\_buf\_simple\_init](#ga040279b601191367dee013bab9916d8d) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) reserve\_head) |
|  | Initialize a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object. |
| void | [net\_buf\_simple\_init\_with\_data](#ga7fac47a2a25eaca39c5d14f1f55b485d) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Initialize a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object with data. |
| static void | [net\_buf\_simple\_reset](#ga4b537e913e132448cbf56976504ddddd) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Reset buffer. |
| void | [net\_buf\_simple\_clone](#ga0186c153b72a379affdd3e2e3994b5a7) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*original, struct [net\_buf\_simple](structnet__buf__simple.md) \*clone) |
|  | Clone buffer state, using the same data buffer. |
| void \* | [net\_buf\_simple\_add](#ga1906e637c848948f5780428a99b3341e) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Prepare data to be added at the end of the buffer. |
| void \* | [net\_buf\_simple\_add\_mem](#gac37209c1e5097e5610860943fb7d0115) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, const void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Copy given number of bytes from memory to the end of the buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [net\_buf\_simple\_add\_u8](#ga8ff9344b8d8deba1b72b8fca048a525c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | Add (8-bit) byte at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le16](#gaa2daf3b20074ff1a23806ce88becebf5) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Add 16-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be16](#ga910f2b9df58fb0706aa40e3b80f235aa) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Add 16-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le24](#gaf1a89eb15eed79003412ba5a32a35cf6) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 24-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be24](#ga5eb09afeff062af577094d2d3f5fdec8) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 24-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le32](#ga3bf1bcff840dddd721f2c49ef0ed7c56) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 32-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be32](#gaac5cd20776d8e7bb4db77cbe5366373c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 32-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le40](#ga67da71ba5942cc11e95aa5ba02cb8552) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 40-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be40](#ga69bdaf4373693bb468cf3876e9edf239) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 40-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le48](#ga5be8c9f33df5b31c15df193a7116ce25) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 48-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be48](#gadb433fb4a1a61702c0615359a4340171) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 48-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le64](#ga79dc411da328b847dcf1903d71eaf011) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 64-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be64](#ga8e31a7b6537d7634e346236534d2a6d0) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 64-bit value at the end of the buffer. |
| void \* | [net\_buf\_simple\_remove\_mem](#ga8473bdffadc05b22335a321df89f4b83) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the end of the buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_buf\_simple\_remove\_u8](#gaf508f74e5e050a7294e8a70bd3725fc3) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove a 8-bit value from the end of the buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_simple\_remove\_le16](#ga0b57f9ca2f3837e94cd7862e37efc01c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 16 bits from the end of the buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_simple\_remove\_be16](#ga93f9f84845601df4ffc118be1ffd2fee) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 16 bits from the end of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_remove\_le24](#ga4e2fef883228f7de41af3cf90648c3c5) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 24 bits from the end of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_remove\_be24](#ga9b39384162a91d7d07e037a9ada782dd) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 24 bits from the end of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_remove\_le32](#ga9e8d016ce384378142fdec6c8dde2457) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 32 bits from the end of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_remove\_be32](#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 32 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_le40](#ga2c937164e648fe8b854cb1144051b6b9) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 40 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_be40](#ga9abd2bccc90cf654556c18322888d131) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 40 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_le48](#gac0628bbbe5d9c2b82766d5a17e767696) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 48 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_be48](#gab93d22797c3f406179c4c145241d6abb) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 48 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_le64](#ga560bd7b181c7f08599ae9241b6ce99fd) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 64 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_be64](#ga602fae83e2ecf47552a11f9282619932) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 64 bits from the end of the buffer. |
| void \* | [net\_buf\_simple\_push](#ga64df9754665440370340c6dddde625d1) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Prepare data to be added to the start of the buffer. |
| void \* | [net\_buf\_simple\_push\_mem](#gaaa838083c610f7426c509efaae69a511) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, const void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Copy given number of bytes from memory to the start of the buffer. |
| void | [net\_buf\_simple\_push\_le16](#ga50cd64438d8f218e3d1ef8b53b7d41a6) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Push 16-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be16](#ga827bd85eba0dbd098790d84d22e8e32d) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Push 16-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_u8](#ga0f19da70bfc8f597680ee02c21226a77) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | Push 8-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_le24](#gabe52d6735d835edc361666bb3413b907) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 24-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be24](#gabfddd4956ec1e356002a3122fea74b72) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 24-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_le32](#ga8662e6bada476c0d48cebea4661b2ac1) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 32-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be32](#gad0c3b8fdeaad6437c3dfcbb03fa52426) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 32-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_le40](#ga745ab6f34138b506b42f78e0975a5d2e) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 40-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be40](#gad65bcaf8401e6f5ffff81a998cfb8fe5) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 40-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_le48](#ga66b44897e336f31e3ecbf4717bec274e) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 48-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be48](#ga1ea39c7d7e9ba4e10d31d818e45e192a) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 48-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_le64](#ga771634e50e2bf7c291565ce6b2af7e85) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 64-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be64](#gafea2201655955ab004b5f77106998ae9) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 64-bit value to the beginning of the buffer. |
| void \* | [net\_buf\_simple\_pull](#gaf5ab4a5fe4a6226be72a510fea0ed8a8) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the beginning of the buffer. |
| void \* | [net\_buf\_simple\_pull\_mem](#ga9c676fdbd6e999a9eab26b13d3608e0c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the beginning of the buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_buf\_simple\_pull\_u8](#ga09a261c615136fd39834cd301fc692e7) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove a 8-bit value from the beginning of the buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_simple\_pull\_le16](#gad59d180ae81b55f6d618565a37d25dba) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 16 bits from the beginning of the buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_simple\_pull\_be16](#gae36458ba05a4ab89e429be4cfd264440) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 16 bits from the beginning of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_pull\_le24](#ga4c9d2ac72a176c49ec224353b5566eb9) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 24 bits from the beginning of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_pull\_be24](#ga4c24d445d6b75c850a9e95fb242a50e1) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 24 bits from the beginning of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_pull\_le32](#ga38df82e6ba9bc2c75133200f7fa75353) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 32 bits from the beginning of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_pull\_be32](#ga1a53892ed75f994bbbb3a2bcf1743d3c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 32 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_le40](#gad669c07efe5cb90ebffcc76d9c1029a1) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 40 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_be40](#gaa665830dad59ac957f79c7f1cc84aed5) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 40 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_le48](#ga69fbfbd72b17783c5ee12b4b2ac9af46) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 48 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_be48](#ga19bdefe740fe94a42fba76d71b4ef6e2) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 48 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_le64](#ga7e0e2d0adbe9062d08f5d8afc7acd89e) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 64 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_be64](#gad07f0d49a7db99063077de493e7b0712) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 64 bits from the beginning of the buffer. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [net\_buf\_simple\_tail](#gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Get the tail pointer for a buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_simple\_headroom](#gaafcb52db2daf1c4451a600e7b647e55c) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Check buffer headroom. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_simple\_tailroom](#ga23e85f8f681fd7617032b4ca40dc62c5) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Check buffer tailroom. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_simple\_max\_len](#gabfe255688a80c0abea866762ff4c5a6c) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Check maximum [net\_buf\_simple::len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3 "Length of the data behind the data pointer.") value. |
| static void | [net\_buf\_simple\_save](#gabf5b098aa0926d9b7fb88baff8a3e2d8) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Save the parsing state of a buffer. |
| static void | [net\_buf\_simple\_restore](#gaedd36481657a7a9d108659d56e131721) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Restore the parsing state of a buffer. |
| struct [net\_buf\_pool](structnet__buf__pool.md) \* | [net\_buf\_pool\_get](#ga145f4b2de7548814eaa7ba86fb123989) (int id) |
|  | Looks up a pool based on its ID. |
| int | [net\_buf\_id](#gacdf048dc0afc7ef67027117e0d51d3a3) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Get a zero-based index for a buffer. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_alloc\_fixed](#ga686df794ec6881625b54454a33587bab) (struct [net\_buf\_pool](structnet__buf__pool.md) \*pool, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a new fixed buffer from a pool. |
| static struct [net\_buf](structnet__buf.md) \* | [net\_buf\_alloc](#ga534366f3b5c7f41a28372c12149ca005) (struct [net\_buf\_pool](structnet__buf__pool.md) \*pool, [k\_timeout\_t](structk__timeout__t.md) timeout) |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_alloc\_len](#ga11d489aedcca82117965fa6ba9d11ca5) (struct [net\_buf\_pool](structnet__buf__pool.md) \*pool, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a new variable length buffer from a pool. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_alloc\_with\_data](#ga8c24d0761d6d38facb6cca60c7c13c0c) (struct [net\_buf\_pool](structnet__buf__pool.md) \*pool, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a new buffer from a pool but with external data pointer. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_get](#ga014a0e87afc143d06a7eaf6c2f04c742) (struct [k\_fifo](structk__fifo.md) \*fifo, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get a buffer from a FIFO. |
| static void | [net\_buf\_destroy](#ga739249547eb37b839b3c1ebdbcb88d28) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Destroy buffer from custom destroy callback. |
| void | [net\_buf\_reset](#ga1292f38b096fd80e31889aff44b0c021) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Reset buffer. |
| void | [net\_buf\_simple\_reserve](#ga0e5d3d938becfefc4f4b4d083cb467aa) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) reserve) |
|  | Initialize buffer with the given headroom. |
| void | [net\_buf\_slist\_put](#ga6d2dfc45e1e5acf21fe08359a4f92a18) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Put a buffer into a list. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_slist\_get](#ga218d4a0c160c57a44946154478724cb3) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Get a buffer from a list. |
| void | [net\_buf\_put](#ga7e1bcc520b7bffcbd9c1d3d308100047) (struct [k\_fifo](structk__fifo.md) \*fifo, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Put a buffer to the end of a FIFO. |
| void | [net\_buf\_unref](#gabedcb728bc2fc0c2b5319a8fd87e8273) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Decrements the reference count of a buffer. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_ref](#ga29387b2a672bf2bb8739046a46f3601f) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Increment the reference count of a buffer. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_clone](#gaf4d80e2878e3c790fff206bec820f03f) (struct [net\_buf](structnet__buf.md) \*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Clone buffer. |
| static void \* | [net\_buf\_user\_data](#gaf2df457abe3e56d47107b76bdc004756) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Get a pointer to the user data of a buffer. |
| int | [net\_buf\_user\_data\_copy](#ga4d1dd56ca8d32d3cfda114fd36761d0d) (struct [net\_buf](structnet__buf.md) \*dst, const struct [net\_buf](structnet__buf.md) \*src) |
|  | Copy user data from one to another buffer. |
| static void | [net\_buf\_reserve](#ga8ac58ad4f73b498bef2ff3ac7e30c6c3) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) reserve) |
|  | Initialize buffer with the given headroom. |
| static void \* | [net\_buf\_add](#ga30776d2b21f06d244c083af5c25b0f3e) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Prepare data to be added at the end of the buffer. |
| static void \* | [net\_buf\_add\_mem](#gacf4e2eba52975ba6728c79274a769d0f) (struct [net\_buf](structnet__buf.md) \*buf, const void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Copies the given number of bytes to the end of the buffer. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [net\_buf\_add\_u8](#ga868ac2bea103fed568b461cbcd45eda2) (struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | Add (8-bit) byte at the end of the buffer. |
| static void | [net\_buf\_add\_le16](#gadd6d01a3b1efd0de16f9bef975809404) (struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Add 16-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be16](#ga61878a9bd7462ca925eac39181f2972c) (struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Add 16-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_le24](#ga32b90364091ade229830686f03b25d4c) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 24-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be24](#ga0f3cd9f9b364a2d2125aea19221d3e1e) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 24-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_le32](#gae8ba33b6592ef7fd859b35d63b285d87) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 32-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be32](#ga5543d00c96f83970f8dbf3670a9dc3fc) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 32-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_le40](#ga62790f9644102f4952c250f6513a2ada) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 40-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be40](#ga70cb98da91de098a92fbd69712c2bde7) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 40-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_le48](#gaf19bf75c3d4d645b1eebf9254aa22790) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 48-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be48](#ga8fe6feb191ab338e91bd62f44e184deb) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 48-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_le64](#gac3f955f8fecc0e5971d2e5e8176e973e) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 64-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be64](#ga055f6eb7d5fbc9a3cf529a9ed00970c4) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 64-bit value at the end of the buffer. |
| static void \* | [net\_buf\_remove\_mem](#gace5ad98eac4772db3b0fa2181912f1f0) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the end of the buffer. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_buf\_remove\_u8](#gad954b9f37790d5e7087db7db7bdedd41) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove a 8-bit value from the end of the buffer. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_remove\_le16](#gaaf654110fb6a8bdfc27433945d4d1308) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 16 bits from the end of the buffer. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_remove\_be16](#ga5da86c8ea703ab3f01c408cce73b0651) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 16 bits from the end of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_remove\_be24](#ga6f346a9af570528d238592851240fd74) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 24 bits from the end of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_remove\_le24](#ga903f59c8dea1b2c54969b567fe315041) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 24 bits from the end of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_remove\_le32](#gae9321a469cc751c58cfb532afd57d265) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 32 bits from the end of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_remove\_be32](#gacce707d646d7008ec3167af1a0b20da8) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 32 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_le40](#ga57150a1ba09b28e5c3b04bdefce7ed8e) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 40 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_be40](#gae2920eab3c56d0d462811b83961df466) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 40 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_le48](#ga0c147d9f95e2224696a8ace26f63a300) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 48 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_be48](#gaab0e3bcc21c958c01ef076cd0efe087c) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 48 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_le64](#ga447b9c6be3fe04a50eb35dd29f190b6d) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 64 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_be64](#ga8b9edd213da2d48dfb8d70a8d307ba13) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 64 bits from the end of the buffer. |
| static void \* | [net\_buf\_push](#ga96a2b1f07f3a7958057d9c7cc1f01b73) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Prepare data to be added at the start of the buffer. |
| static void \* | [net\_buf\_push\_mem](#ga7e9daccec8cae1b9bfda52b0758adf0c) (struct [net\_buf](structnet__buf.md) \*buf, const void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Copies the given number of bytes to the start of the buffer. |
| static void | [net\_buf\_push\_u8](#ga9093202ba0a22bfa519bbe32d4585186) (struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | Push 8-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le16](#gab6c84c6846c06c2b339bc88df35e2655) (struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Push 16-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be16](#ga6dd756ff8332d076f5d37c69e6c534b5) (struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Push 16-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le24](#ga87524ac50e53ba59c6692af10cf001b9) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 24-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be24](#ga87338399d8ecd64a894908ed4a2f710b) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 24-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le32](#ga97c9046185d6a1e9235bf6914c72dfc4) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 32-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be32](#gae4e64a23708ed910fb6c3ab8ba481a4c) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 32-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le40](#gaefab4a755cf4fb7d2b4a142a9351c189) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 40-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be40](#ga512f84e686ff70a5589557575ccda1f8) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 40-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le48](#ga852654f7e59951bf3536e3f4e98761bf) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 48-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be48](#gabfbcb051019ff210cc2b85adcf4bc821) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 48-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le64](#gad4ee42b023881f80211fbeca53a0f25d) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 64-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be64](#ga43ff5faab0b099a355b9b96b7b0e3d8c) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 64-bit value to the beginning of the buffer. |
| static void \* | [net\_buf\_pull](#gaef433d92734dd8691c292abdb823ba0e) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the beginning of the buffer. |
| static void \* | [net\_buf\_pull\_mem](#gaedc5ffe19bb0ec438e633023c3c5de74) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the beginning of the buffer. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_buf\_pull\_u8](#ga71bb306d2ce459a60a8c3fc6dac54c90) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove a 8-bit value from the beginning of the buffer. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_pull\_le16](#gaed64e9f2b969f2c0d99cd281e73c860a) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 16 bits from the beginning of the buffer. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_pull\_be16](#ga97909a33c374a5c757fd2faf582139b7) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 16 bits from the beginning of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_pull\_le24](#ga85c505321484a50ed9422f24934ed077) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 24 bits from the beginning of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_pull\_be24](#ga8de937e8775879712ea0acbf60327a95) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 24 bits from the beginning of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_pull\_le32](#ga5f051078f1ffcc40e9ad40e7545a084f) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 32 bits from the beginning of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_pull\_be32](#ga5f8f2e2244eb574b3e57d09d85412967) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 32 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_le40](#ga36b27c6373eb245f777164065386d100) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 40 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_be40](#ga050bdaccaec842482a02b096aa0c999f) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 40 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_le48](#ga7eeee45b6639146d1492f92263ee4f51) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 48 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_be48](#ga68934e105c4b3a8e27aa61b3ec5526db) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 48 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_le64](#ga9a3df35e2287cbcfe1b60e2efa52c64e) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 64 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_be64](#ga3c1e80741a49691e69e57c891d3edb05) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 64 bits from the beginning of the buffer. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_tailroom](#gaecbc6adf16469e3366c88445ea7a553a) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Check buffer tailroom. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_headroom](#gac9a09897f44e708f920064826aa2f703) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Check buffer headroom. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_max\_len](#ga65924b8234c91dfc09069ba06242a6b7) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Check maximum [net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38 "Length of the data behind the data pointer.") value. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [net\_buf\_tail](#gaedb10a84b352a3d7716bef979af2ab31) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Get the tail pointer for a buffer. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_frag\_last](#ga042ce3f2e7e3fd0948ca2623fff36746) (struct [net\_buf](structnet__buf.md) \*frags) |
|  | Find the last fragment in the fragment list. |
| void | [net\_buf\_frag\_insert](#gac032b44db4a845dba8303fecfe1b63e7) (struct [net\_buf](structnet__buf.md) \*parent, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Insert a new fragment to a chain of bufs. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_frag\_add](#ga0d7e310802a2bc7b2078f9310827535f) (struct [net\_buf](structnet__buf.md) \*head, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Add a new fragment to the end of a chain of bufs. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_frag\_del](#ga602a99833bd401a0ada5bd5defa7a2ff) (struct [net\_buf](structnet__buf.md) \*parent, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Delete existing fragment from a chain of bufs. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_linearize](#gaffd49f2de8e72d5f7585b4e5167923d8) (void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dst\_len, const struct [net\_buf](structnet__buf.md) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Copy bytes from [net\_buf](structnet__buf.md "Network buffer representation.") chain starting at offset to linear buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_append\_bytes](#ga646d680491753b3ed29fa83c26732d1a) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const void \*value, [k\_timeout\_t](structk__timeout__t.md) timeout, [net\_buf\_allocator\_cb](#ga9b74d094a45daf74cd230eaa4fcbc065) allocate\_cb, void \*user\_data) |
|  | Append data to a list of [net\_buf](structnet__buf.md "Network buffer representation."). |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_data\_match](#gaef938c3ab676a5bd5bf8338b8d7cb30c) (const struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Match data with a [net\_buf](structnet__buf.md "Network buffer representation.")'s content. |
| static struct [net\_buf](structnet__buf.md) \* | [net\_buf\_skip](#ga2d7096280d4fa6f5e32c4674d542889b) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Skip N number of bytes in a [net\_buf](structnet__buf.md "Network buffer representation."). |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_frags\_len](#gaebb95f08dbd4d38a250170aa78ddeb44) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Calculate amount of bytes stored in fragments. |

## Detailed Description

Network buffer library.

## Macro Definition Documentation

## [◆ ](#gaaeacbdf3cfda12691c75253015e5c19a)NET\_BUF\_EXTERNAL\_DATA

| #define NET\_BUF\_EXTERNAL\_DATA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[buf.h](net_2buf_8h.md)>`

Flag indicating that the buffer's associated data pointer, points to externally allocated memory.

Therefore once ref goes down to zero, the pointed data will not need to be deallocated. This never needs to be explicitly set or unset by the [net\_buf](structnet__buf.md "Network buffer representation.") API user. Such [net\_buf](structnet__buf.md "Network buffer representation.") is exclusively instantiated via [net\_buf\_alloc\_with\_data()](#ga8c24d0761d6d38facb6cca60c7c13c0c) function. Reference count mechanism however will behave the same way, and ref count going to 0 will free the [net\_buf](structnet__buf.md "Network buffer representation.") but no the data pointer in it.

## [◆ ](#ga810aba8ba321fd012edc238ea9fe19dc)NET\_BUF\_POOL\_DEFINE

| #define NET\_BUF\_POOL\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_count*, |
|  |  |  | *\_size*, |
|  |  |  | *\_ud\_size*, |
|  |  |  | *\_destroy* ) |

`#include <[buf.h](net_2buf_8h.md)>`

**Value:**

[NET\_BUF\_POOL\_FIXED\_DEFINE](#gacc53824e01db7935bcc9cad564b716cd)(\_name, \_count, \_size, \_ud\_size, \_destroy)

[NET\_BUF\_POOL\_FIXED\_DEFINE](#gacc53824e01db7935bcc9cad564b716cd)

#define NET\_BUF\_POOL\_FIXED\_DEFINE(\_name, \_count, \_data\_size, \_ud\_size, \_destroy)

Define a new pool for buffers based on fixed-size data.

**Definition** buf.h:1219

Define a new pool for buffers.

Defines a [net\_buf\_pool](structnet__buf__pool.md "Network buffer pool representation.") struct and the necessary memory storage (array of structs) for the needed amount of buffers. After this,the buffers can be accessed from the pool through net\_buf\_alloc. The pool is defined as a static variable, so if it needs to be exported outside the current module this needs to happen with the help of a separate pointer rather than an extern declaration.

If provided with a custom destroy callback this callback is responsible for eventually calling [net\_buf\_destroy()](#ga739249547eb37b839b3c1ebdbcb88d28) to complete the process of returning the buffer to the pool.

Parameters
:   | \_name | Name of the pool variable. |
    | --- | --- |
    | \_count | Number of buffers in the pool. |
    | \_size | Maximum data size for each buffer. |
    | \_ud\_size | Amount of user data space to reserve. |
    | \_destroy | Optional destroy callback when buffer is freed. |

## [◆ ](#gacc53824e01db7935bcc9cad564b716cd)NET\_BUF\_POOL\_FIXED\_DEFINE

| #define NET\_BUF\_POOL\_FIXED\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_count*, |
|  |  |  | *\_data\_size*, |
|  |  |  | *\_ud\_size*, |
|  |  |  | *\_destroy* ) |

`#include <[buf.h](net_2buf_8h.md)>`

**Value:**

\_NET\_BUF\_ARRAY\_DEFINE(\_name, \_count, \_ud\_size); \

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_\_noinit net\_buf\_data\_##\_name[\_count][\_data\_size] \_\_net\_buf\_align; \

static const struct net\_buf\_pool\_fixed net\_buf\_fixed\_##\_name = { \

.data\_pool = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)net\_buf\_data\_##\_name, \

}; \

static const struct net\_buf\_data\_alloc net\_buf\_fixed\_alloc\_##\_name = { \

.cb = &net\_buf\_fixed\_cb, \

.alloc\_data = (void \*)&net\_buf\_fixed\_##\_name, \

.max\_alloc\_size = \_data\_size, \

}; \

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(net\_buf\_pool, \_name) = \

NET\_BUF\_POOL\_INITIALIZER(\_name, &net\_buf\_fixed\_alloc\_##\_name, \

\_net\_buf\_##\_name, \_count, \_ud\_size, \

\_destroy)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Define a new pool for buffers based on fixed-size data.

Defines a [net\_buf\_pool](structnet__buf__pool.md "Network buffer pool representation.") struct and the necessary memory storage (array of structs) for the needed amount of buffers. After this, the buffers can be accessed from the pool through net\_buf\_alloc. The pool is defined as a static variable, so if it needs to be exported outside the current module this needs to happen with the help of a separate pointer rather than an extern declaration.

The data payload of the buffers will be allocated from a byte array of fixed sized chunks. This kind of pool does not support blocking on the data allocation, so the timeout passed to net\_buf\_alloc will be always treated as K\_NO\_WAIT when trying to allocate the data. This means that allocation failures, i.e. NULL returns, must always be handled cleanly.

If provided with a custom destroy callback, this callback is responsible for eventually calling [net\_buf\_destroy()](#ga739249547eb37b839b3c1ebdbcb88d28) to complete the process of returning the buffer to the pool.

Parameters
:   | \_name | Name of the pool variable. |
    | --- | --- |
    | \_count | Number of buffers in the pool. |
    | \_data\_size | Maximum data payload per buffer. |
    | \_ud\_size | User data space to reserve per buffer. |
    | \_destroy | Optional destroy callback when buffer is freed. |

## [◆ ](#ga61671ac866081d31dfe9eddbf3b6f210)NET\_BUF\_POOL\_HEAP\_DEFINE

| #define NET\_BUF\_POOL\_HEAP\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_count*, |
|  |  |  | *\_ud\_size*, |
|  |  |  | *\_destroy* ) |

`#include <[buf.h](net_2buf_8h.md)>`

**Value:**

\_NET\_BUF\_ARRAY\_DEFINE(\_name, \_count, \_ud\_size); \

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([net\_buf\_pool](structnet__buf__pool.md), \_name) = \

NET\_BUF\_POOL\_INITIALIZER(\_name, &net\_buf\_heap\_alloc, \

\_net\_buf\_##\_name, \_count, \_ud\_size, \

\_destroy)

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** buf.h:1076

Define a new pool for buffers using the heap for the data.

Defines a [net\_buf\_pool](structnet__buf__pool.md "Network buffer pool representation.") struct and the necessary memory storage (array of structs) for the needed amount of buffers. After this, the buffers can be accessed from the pool through net\_buf\_alloc. The pool is defined as a static variable, so if it needs to be exported outside the current module this needs to happen with the help of a separate pointer rather than an extern declaration.

The data payload of the buffers will be allocated from the heap using k\_malloc, so CONFIG\_HEAP\_MEM\_POOL\_SIZE must be set to a positive value. This kind of pool does not support blocking on the data allocation, so the timeout passed to net\_buf\_alloc will be always treated as K\_NO\_WAIT when trying to allocate the data. This means that allocation failures, i.e. NULL returns, must always be handled cleanly.

If provided with a custom destroy callback, this callback is responsible for eventually calling [net\_buf\_destroy()](#ga739249547eb37b839b3c1ebdbcb88d28) to complete the process of returning the buffer to the pool.

Parameters
:   | \_name | Name of the pool variable. |
    | --- | --- |
    | \_count | Number of buffers in the pool. |
    | \_ud\_size | User data space to reserve per buffer. |
    | \_destroy | Optional destroy callback when buffer is freed. |

## [◆ ](#ga90e691e793c964847d737f5ecf7646ec)NET\_BUF\_POOL\_VAR\_DEFINE

| #define NET\_BUF\_POOL\_VAR\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_count*, |
|  |  |  | *\_data\_size*, |
|  |  |  | *\_ud\_size*, |
|  |  |  | *\_destroy* ) |

`#include <[buf.h](net_2buf_8h.md)>`

**Value:**

\_NET\_BUF\_ARRAY\_DEFINE(\_name, \_count, \_ud\_size); \

K\_HEAP\_DEFINE(net\_buf\_mem\_pool\_##\_name, \_data\_size); \

static const struct net\_buf\_data\_alloc net\_buf\_data\_alloc\_##\_name = { \

.cb = &net\_buf\_var\_cb, \

.alloc\_data = &net\_buf\_mem\_pool\_##\_name, \

.max\_alloc\_size = 0, \

}; \

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([net\_buf\_pool](structnet__buf__pool.md), \_name) = \

NET\_BUF\_POOL\_INITIALIZER(\_name, &net\_buf\_data\_alloc\_##\_name, \

\_net\_buf\_##\_name, \_count, \_ud\_size, \

\_destroy)

Define a new pool for buffers with variable size payloads.

Defines a [net\_buf\_pool](structnet__buf__pool.md "Network buffer pool representation.") struct and the necessary memory storage (array of structs) for the needed amount of buffers. After this, the buffers can be accessed from the pool through net\_buf\_alloc. The pool is defined as a static variable, so if it needs to be exported outside the current module this needs to happen with the help of a separate pointer rather than an extern declaration.

The data payload of the buffers will be based on a memory pool from which variable size payloads may be allocated.

If provided with a custom destroy callback, this callback is responsible for eventually calling [net\_buf\_destroy()](#ga739249547eb37b839b3c1ebdbcb88d28) to complete the process of returning the buffer to the pool.

Parameters
:   | \_name | Name of the pool variable. |
    | --- | --- |
    | \_count | Number of buffers in the pool. |
    | \_data\_size | Total amount of memory available for data payloads. |
    | \_ud\_size | User data space to reserve per buffer. |
    | \_destroy | Optional destroy callback when buffer is freed. |

## [◆ ](#ga0b01dc80027d13b1895379d4d1397207)NET\_BUF\_SIMPLE

| #define NET\_BUF\_SIMPLE | ( |  | *\_size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

**Value:**

((struct [net\_buf\_simple](structnet__buf__simple.md) \*)(&(struct { \

struct [net\_buf\_simple](structnet__buf__simple.md) buf; \

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data[\_size]; \

}) { \

.buf.size = \_size, \

}))

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

Define a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") stack variable and get a pointer to it.

This is a helper macro which is used to define a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object on the stack and the get a pointer to it as follows:

struct [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") \*my\_buf = [NET\_BUF\_SIMPLE(10)](#ga0b01dc80027d13b1895379d4d1397207);

After creating the object it needs to be initialized by calling [net\_buf\_simple\_init()](#ga040279b601191367dee013bab9916d8d).

Parameters
:   | \_size | Maximum data storage for the buffer. |
    | --- | --- |

Returns
:   Pointer to stack-allocated [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object.

## [◆ ](#gaf85aa0b705bb4fbe2630191fde802501)NET\_BUF\_SIMPLE\_DEFINE

| #define NET\_BUF\_SIMPLE\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_size* ) |

`#include <[buf.h](net_2buf_8h.md)>`

**Value:**

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf\_data\_##\_name[\_size]; \

struct [net\_buf\_simple](structnet__buf__simple.md) \_name = { \

.data = net\_buf\_data\_##\_name, \

.[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3) = 0, \

.size = \_size, \

.\_\_buf = net\_buf\_data\_##\_name, \

}

[net\_buf\_simple::len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3)

uint16\_t len

Length of the data behind the data pointer.

**Definition** buf.h:96

Define a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") stack variable.

This is a helper macro which is used to define a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object on the stack.

Parameters
:   | \_name | Name of the [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object. |
    | --- | --- |
    | \_size | Maximum data storage for the buffer. |

## [◆ ](#ga21ced8b3082d57bf071008de5fffc0f4)NET\_BUF\_SIMPLE\_DEFINE\_STATIC

| #define NET\_BUF\_SIMPLE\_DEFINE\_STATIC | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_size* ) |

`#include <[buf.h](net_2buf_8h.md)>`

**Value:**

static \_\_noinit [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf\_data\_##\_name[\_size]; \

static struct [net\_buf\_simple](structnet__buf__simple.md) \_name = { \

.data = net\_buf\_data\_##\_name, \

.[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3) = 0, \

.size = \_size, \

.\_\_buf = net\_buf\_data\_##\_name, \

}

Define a static [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") variable.

This is a helper macro which is used to define a static [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object.

Parameters
:   | \_name | Name of the [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object. |
    | --- | --- |
    | \_size | Maximum data storage for the buffer. |

## Typedef Documentation

## [◆ ](#ga9b74d094a45daf74cd230eaa4fcbc065)net\_buf\_allocator\_cb

| typedef struct [net\_buf](structnet__buf.md) \*(\* net\_buf\_allocator\_cb) ([k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
| --- |

`#include <[buf.h](net_2buf_8h.md)>`

Network buffer allocator callback.

The allocator callback is called when net\_buf\_append\_bytes needs to allocate a new [net\_buf](structnet__buf.md "Network buffer representation.").

Parameters
:   | timeout | Affects the action taken should the net buf pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout. |
    | --- | --- |
    | user\_data | The user data given in net\_buf\_append\_bytes call. |

Returns
:   pointer to allocated [net\_buf](structnet__buf.md "Network buffer representation.") or NULL on error.

## Function Documentation

## [◆ ](#ga30776d2b21f06d244c083af5c25b0f3e)net\_buf\_add()

| | void \* net\_buf\_add | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Prepare data to be added at the end of the buffer.

Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | len | Number of bytes to increment the length with. |

Returns
:   The original tail of the buffer.

## [◆ ](#ga61878a9bd7462ca925eac39181f2972c)net\_buf\_add\_be16()

| | void net\_buf\_add\_be16 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 16-bit value at the end of the buffer.

Adds 16-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 16-bit value to be added. |

## [◆ ](#ga0f3cd9f9b364a2d2125aea19221d3e1e)net\_buf\_add\_be24()

| | void net\_buf\_add\_be24 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 24-bit value at the end of the buffer.

Adds 24-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 24-bit value to be added. |

## [◆ ](#ga5543d00c96f83970f8dbf3670a9dc3fc)net\_buf\_add\_be32()

| | void net\_buf\_add\_be32 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 32-bit value at the end of the buffer.

Adds 32-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 32-bit value to be added. |

## [◆ ](#ga70cb98da91de098a92fbd69712c2bde7)net\_buf\_add\_be40()

| | void net\_buf\_add\_be40 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 40-bit value at the end of the buffer.

Adds 40-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 40-bit value to be added. |

## [◆ ](#ga8fe6feb191ab338e91bd62f44e184deb)net\_buf\_add\_be48()

| | void net\_buf\_add\_be48 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 48-bit value at the end of the buffer.

Adds 48-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 48-bit value to be added. |

## [◆ ](#ga055f6eb7d5fbc9a3cf529a9ed00970c4)net\_buf\_add\_be64()

| | void net\_buf\_add\_be64 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 64-bit value at the end of the buffer.

Adds 64-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 64-bit value to be added. |

## [◆ ](#gadd6d01a3b1efd0de16f9bef975809404)net\_buf\_add\_le16()

| | void net\_buf\_add\_le16 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 16-bit value at the end of the buffer.

Adds 16-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 16-bit value to be added. |

## [◆ ](#ga32b90364091ade229830686f03b25d4c)net\_buf\_add\_le24()

| | void net\_buf\_add\_le24 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 24-bit value at the end of the buffer.

Adds 24-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 24-bit value to be added. |

## [◆ ](#gae8ba33b6592ef7fd859b35d63b285d87)net\_buf\_add\_le32()

| | void net\_buf\_add\_le32 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 32-bit value at the end of the buffer.

Adds 32-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 32-bit value to be added. |

## [◆ ](#ga62790f9644102f4952c250f6513a2ada)net\_buf\_add\_le40()

| | void net\_buf\_add\_le40 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 40-bit value at the end of the buffer.

Adds 40-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 40-bit value to be added. |

## [◆ ](#gaf19bf75c3d4d645b1eebf9254aa22790)net\_buf\_add\_le48()

| | void net\_buf\_add\_le48 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 48-bit value at the end of the buffer.

Adds 48-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 48-bit value to be added. |

## [◆ ](#gac3f955f8fecc0e5971d2e5e8176e973e)net\_buf\_add\_le64()

| | void net\_buf\_add\_le64 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add 64-bit value at the end of the buffer.

Adds 64-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 64-bit value to be added. |

## [◆ ](#gacf4e2eba52975ba6728c79274a769d0f)net\_buf\_add\_mem()

| | void \* net\_buf\_add\_mem | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | const void \* | *mem*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Copies the given number of bytes to the end of the buffer.

Increments the data length of the buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | mem | Location of data to be added. |
    | len | Length of data to be added |

Returns
:   The original tail of the buffer.

## [◆ ](#ga868ac2bea103fed568b461cbcd45eda2)net\_buf\_add\_u8()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* net\_buf\_add\_u8 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Add (8-bit) byte at the end of the buffer.

Increments the data length of the buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | byte value to be added. |

Returns
:   Pointer to the value added

## [◆ ](#ga534366f3b5c7f41a28372c12149ca005)net\_buf\_alloc()

| | struct [net\_buf](structnet__buf.md) \* net\_buf\_alloc | ( | struct [net\_buf\_pool](structnet__buf__pool.md) \* | *pool*, | | --- | --- | --- | --- | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Note
:   Some types of data allocators do not support blocking (such as the HEAP type). In this case it's still possible for [net\_buf\_alloc()](#ga534366f3b5c7f41a28372c12149ca005) to fail (return NULL) even if it was given K\_FOREVER.
:   The timeout value will be overridden to K\_NO\_WAIT if called from the system workqueue.

Parameters
:   | pool | Which pool to allocate the buffer from. |
    | --- | --- |
    | timeout | Affects the action taken should the pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout. |

Returns
:   New buffer or NULL if out of buffers.

## [◆ ](#ga686df794ec6881625b54454a33587bab)net\_buf\_alloc\_fixed()

| struct [net\_buf](structnet__buf.md) \* net\_buf\_alloc\_fixed | ( | struct [net\_buf\_pool](structnet__buf__pool.md) \* | *pool*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Allocate a new fixed buffer from a pool.

Note
:   Some types of data allocators do not support blocking (such as the HEAP type). In this case it's still possible for [net\_buf\_alloc()](#ga534366f3b5c7f41a28372c12149ca005) to fail (return NULL) even if it was given K\_FOREVER.
:   The timeout value will be overridden to K\_NO\_WAIT if called from the system workqueue.

Parameters
:   | pool | Which pool to allocate the buffer from. |
    | --- | --- |
    | timeout | Affects the action taken should the pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout. |

Returns
:   New buffer or NULL if out of buffers.

## [◆ ](#ga11d489aedcca82117965fa6ba9d11ca5)net\_buf\_alloc\_len()

| struct [net\_buf](structnet__buf.md) \* net\_buf\_alloc\_len | ( | struct [net\_buf\_pool](structnet__buf__pool.md) \* | *pool*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Allocate a new variable length buffer from a pool.

Note
:   Some types of data allocators do not support blocking (such as the HEAP type). In this case it's still possible for [net\_buf\_alloc()](#ga534366f3b5c7f41a28372c12149ca005) to fail (return NULL) even if it was given K\_FOREVER.
:   The timeout value will be overridden to K\_NO\_WAIT if called from the system workqueue.

Parameters
:   | pool | Which pool to allocate the buffer from. |
    | --- | --- |
    | size | Amount of data the buffer must be able to fit. |
    | timeout | Affects the action taken should the pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout. |

Returns
:   New buffer or NULL if out of buffers.

## [◆ ](#ga8c24d0761d6d38facb6cca60c7c13c0c)net\_buf\_alloc\_with\_data()

| struct [net\_buf](structnet__buf.md) \* net\_buf\_alloc\_with\_data | ( | struct [net\_buf\_pool](structnet__buf__pool.md) \* | *pool*, |
| --- | --- | --- | --- |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Allocate a new buffer from a pool but with external data pointer.

Allocate a new buffer from a pool, where the data pointer comes from the user and not from the pool.

Note
:   Some types of data allocators do not support blocking (such as the HEAP type). In this case it's still possible for [net\_buf\_alloc()](#ga534366f3b5c7f41a28372c12149ca005) to fail (return NULL) even if it was given K\_FOREVER.
:   The timeout value will be overridden to K\_NO\_WAIT if called from the system workqueue.

Parameters
:   | pool | Which pool to allocate the buffer from. |
    | --- | --- |
    | data | External data pointer |
    | size | Amount of data the pointed data buffer if able to fit. |
    | timeout | Affects the action taken should the pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout. |

Returns
:   New buffer or NULL if out of buffers.

## [◆ ](#ga646d680491753b3ed29fa83c26732d1a)net\_buf\_append\_bytes()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_buf\_append\_bytes | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const void \* | *value*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | [net\_buf\_allocator\_cb](#ga9b74d094a45daf74cd230eaa4fcbc065) | *allocate\_cb*, |
|  |  | void \* | *user\_data* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Append data to a list of [net\_buf](structnet__buf.md "Network buffer representation.").

Append data to a [net\_buf](structnet__buf.md "Network buffer representation."). If there is not enough space in the [net\_buf](structnet__buf.md "Network buffer representation.") then more [net\_buf](structnet__buf.md "Network buffer representation.") will be added, unless there are no free [net\_buf](structnet__buf.md "Network buffer representation.") and timeout occurs. If not allocator is provided it attempts to allocate from the same pool as the original buffer.

Parameters
:   | buf | Network buffer. |
    | --- | --- |
    | len | Total length of input data |
    | value | Data to be added |
    | timeout | Timeout is passed to the [net\_buf](structnet__buf.md "Network buffer representation.") allocator callback. |
    | allocate\_cb | When a new [net\_buf](structnet__buf.md "Network buffer representation.") is required, use this callback. |
    | user\_data | A user data pointer to be supplied to the allocate\_cb. This pointer is can be anything from a mem\_pool or a [net\_pkt](structnet__pkt.md "Network packet."), the logic is left up to the allocate\_cb function. |

Returns
:   Length of data actually added. This may be less than input length if other timeout than K\_FOREVER was used, and there were no free fragments in a pool to accommodate all data.

## [◆ ](#gaf4d80e2878e3c790fff206bec820f03f)net\_buf\_clone()

| struct [net\_buf](structnet__buf.md) \* net\_buf\_clone | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Clone buffer.

Duplicate given buffer including any (user) data and headers currently stored.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |
    | timeout | Affects the action taken should the pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout. |

Returns
:   Cloned buffer or NULL if out of buffers.

## [◆ ](#gaef938c3ab676a5bd5bf8338b8d7cb30c)net\_buf\_data\_match()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_buf\_data\_match | ( | const struct [net\_buf](structnet__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset*, |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Match data with a [net\_buf](structnet__buf.md "Network buffer representation.")'s content.

Compare data with a content of a [net\_buf](structnet__buf.md "Network buffer representation."). Provide information about the number of bytes matching between both. If needed, traverse through multiple buffer fragments.

Parameters
:   | buf | Network buffer |
    | --- | --- |
    | offset | Starting offset to compare from |
    | data | Data buffer for comparison |
    | len | Number of bytes to compare |

Returns
:   The number of bytes compared before the first difference.

## [◆ ](#ga739249547eb37b839b3c1ebdbcb88d28)net\_buf\_destroy()

| | void net\_buf\_destroy | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Destroy buffer from custom destroy callback.

This helper is only intended to be used from custom destroy callbacks. If no custom destroy callback is given to NET\_BUF\_POOL\_\*\_DEFINE() then there is no need to use this API.

Parameters
:   | buf | Buffer to destroy. |
    | --- | --- |

## [◆ ](#ga0d7e310802a2bc7b2078f9310827535f)net\_buf\_frag\_add()

| struct [net\_buf](structnet__buf.md) \* net\_buf\_frag\_add | ( | struct [net\_buf](structnet__buf.md) \* | *head*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *frag* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add a new fragment to the end of a chain of bufs.

Append a new fragment into the buffer fragments list.

Note: This function takes ownership of the fragment reference so the caller is not required to unref.

Parameters
:   | head | Head of the fragment chain. |
    | --- | --- |
    | frag | Fragment to add. |

Returns
:   New head of the fragment chain. Either head (if head was non-NULL) or frag (if head was NULL).

## [◆ ](#ga602a99833bd401a0ada5bd5defa7a2ff)net\_buf\_frag\_del()

| struct [net\_buf](structnet__buf.md) \* net\_buf\_frag\_del | ( | struct [net\_buf](structnet__buf.md) \* | *parent*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *frag* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Delete existing fragment from a chain of bufs.

Parameters
:   | parent | Parent buffer/fragment, or NULL if there is no parent. |
    | --- | --- |
    | frag | Fragment to delete. |

Returns
:   Pointer to the buffer following the fragment, or NULL if it had no further fragments.

## [◆ ](#gac032b44db4a845dba8303fecfe1b63e7)net\_buf\_frag\_insert()

| void net\_buf\_frag\_insert | ( | struct [net\_buf](structnet__buf.md) \* | *parent*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *frag* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Insert a new fragment to a chain of bufs.

Insert a new fragment into the buffer fragments list after the parent.

Note: This function takes ownership of the fragment reference so the caller is not required to unref.

Parameters
:   | parent | Parent buffer/fragment. |
    | --- | --- |
    | frag | Fragment to insert. |

## [◆ ](#ga042ce3f2e7e3fd0948ca2623fff36746)net\_buf\_frag\_last()

| struct [net\_buf](structnet__buf.md) \* net\_buf\_frag\_last | ( | struct [net\_buf](structnet__buf.md) \* | *frags* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Find the last fragment in the fragment list.

Returns
:   Pointer to last fragment in the list.

## [◆ ](#gaebb95f08dbd4d38a250170aa78ddeb44)net\_buf\_frags\_len()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_buf\_frags\_len | ( | const struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Calculate amount of bytes stored in fragments.

Calculates the total amount of data stored in the given buffer and the fragments linked to it.

Parameters
:   | buf | Buffer to start off with. |
    | --- | --- |

Returns
:   Number of bytes in the buffer and its fragments.

## [◆ ](#ga014a0e87afc143d06a7eaf6c2f04c742)net\_buf\_get()

| struct [net\_buf](structnet__buf.md) \* net\_buf\_get | ( | struct [k\_fifo](structk__fifo.md) \* | *fifo*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Get a buffer from a FIFO.

This function is NOT thread-safe if the buffers in the FIFO contain fragments.

Parameters
:   | fifo | Which FIFO to take the buffer from. |
    | --- | --- |
    | timeout | Affects the action taken should the FIFO be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout. |

Returns
:   New buffer or NULL if the FIFO is empty.

## [◆ ](#gac9a09897f44e708f920064826aa2f703)net\_buf\_headroom()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_buf\_headroom | ( | const struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Check buffer headroom.

Check how much free space there is in the beginning of the buffer.

buf A valid pointer on a buffer

Returns
:   Number of bytes available in the beginning of the buffer.

## [◆ ](#gacdf048dc0afc7ef67027117e0d51d3a3)net\_buf\_id()

| int net\_buf\_id | ( | const struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Get a zero-based index for a buffer.

This function will translate a buffer into a zero-based index, based on its placement in its buffer pool. This can be useful if you want to associate an external array of meta-data contexts with the buffers of a pool.

Parameters
:   | buf | Network buffer. |
    | --- | --- |

Returns
:   Zero-based index for the buffer.

## [◆ ](#gaffd49f2de8e72d5f7585b4e5167923d8)net\_buf\_linearize()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_buf\_linearize | ( | void \* | *dst*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *dst\_len*, |
|  |  | const struct [net\_buf](structnet__buf.md) \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Copy bytes from [net\_buf](structnet__buf.md "Network buffer representation.") chain starting at offset to linear buffer.

Copy (extract) *len* bytes from *src* [net\_buf](structnet__buf.md "Network buffer representation.") chain, starting from *offset* in it, to a linear buffer *dst*. Return number of bytes actually copied, which may be less than requested, if [net\_buf](structnet__buf.md "Network buffer representation.") chain doesn't have enough data, or destination buffer is too small.

Parameters
:   | dst | Destination buffer |
    | --- | --- |
    | dst\_len | Destination buffer length |
    | src | Source [net\_buf](structnet__buf.md "Network buffer representation.") chain |
    | offset | Starting offset to copy from |
    | len | Number of bytes to copy |

Returns
:   number of bytes actually copied

## [◆ ](#ga65924b8234c91dfc09069ba06242a6b7)net\_buf\_max\_len()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_max\_len | ( | const struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Check maximum [net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38 "Length of the data behind the data pointer.") value.

This value is depending on the number of bytes being reserved as headroom.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   Number of bytes usable behind the [net\_buf::data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56 "Pointer to the start of data in the buffer.") pointer.

## [◆ ](#ga145f4b2de7548814eaa7ba86fb123989)net\_buf\_pool\_get()

| struct [net\_buf\_pool](structnet__buf__pool.md) \* net\_buf\_pool\_get | ( | int | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Looks up a pool based on its ID.

Parameters
:   | id | Pool ID (e.g. from buf->pool\_id). |
    | --- | --- |

Returns
:   Pointer to pool.

## [◆ ](#gaef433d92734dd8691c292abdb823ba0e)net\_buf\_pull()

| | void \* net\_buf\_pull | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove data from the beginning of the buffer.

Removes data from the beginning of the buffer by modifying the data pointer and buffer length.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | len | Number of bytes to remove. |

Returns
:   New beginning of the buffer data.

## [◆ ](#ga97909a33c374a5c757fd2faf582139b7)net\_buf\_pull\_be16()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_pull\_be16 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 16 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 16-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   16-bit value converted from big endian to host endian.

## [◆ ](#ga8de937e8775879712ea0acbf60327a95)net\_buf\_pull\_be24()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_pull\_be24 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 24 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 24-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   24-bit value converted from big endian to host endian.

## [◆ ](#ga5f8f2e2244eb574b3e57d09d85412967)net\_buf\_pull\_be32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_pull\_be32 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 32 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 32-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   32-bit value converted from big endian to host endian.

## [◆ ](#ga050bdaccaec842482a02b096aa0c999f)net\_buf\_pull\_be40()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_pull\_be40 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 40 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 40-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   40-bit value converted from big endian to host endian.

## [◆ ](#ga68934e105c4b3a8e27aa61b3ec5526db)net\_buf\_pull\_be48()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_pull\_be48 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 48 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 48-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   48-bit value converted from big endian to host endian.

## [◆ ](#ga3c1e80741a49691e69e57c891d3edb05)net\_buf\_pull\_be64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_pull\_be64 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 64 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 64-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   64-bit value converted from big endian to host endian.

## [◆ ](#gaed64e9f2b969f2c0d99cd281e73c860a)net\_buf\_pull\_le16()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_pull\_le16 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 16 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 16-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   16-bit value converted from little endian to host endian.

## [◆ ](#ga85c505321484a50ed9422f24934ed077)net\_buf\_pull\_le24()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_pull\_le24 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 24 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 24-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   24-bit value converted from little endian to host endian.

## [◆ ](#ga5f051078f1ffcc40e9ad40e7545a084f)net\_buf\_pull\_le32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_pull\_le32 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 32 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 32-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   32-bit value converted from little endian to host endian.

## [◆ ](#ga36b27c6373eb245f777164065386d100)net\_buf\_pull\_le40()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_pull\_le40 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 40 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 40-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   40-bit value converted from little endian to host endian.

## [◆ ](#ga7eeee45b6639146d1492f92263ee4f51)net\_buf\_pull\_le48()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_pull\_le48 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 48 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 48-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   48-bit value converted from little endian to host endian.

## [◆ ](#ga9a3df35e2287cbcfe1b60e2efa52c64e)net\_buf\_pull\_le64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_pull\_le64 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 64 bits from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 64-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   64-bit value converted from little endian to host endian.

## [◆ ](#gaedc5ffe19bb0ec438e633023c3c5de74)net\_buf\_pull\_mem()

| | void \* net\_buf\_pull\_mem | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove data from the beginning of the buffer.

Removes data from the beginning of the buffer by modifying the data pointer and buffer length.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | len | Number of bytes to remove. |

Returns
:   Pointer to the old beginning of the buffer data.

## [◆ ](#ga71bb306d2ce459a60a8c3fc6dac54c90)net\_buf\_pull\_u8()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf\_pull\_u8 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove a 8-bit value from the beginning of the buffer.

Same idea as with [net\_buf\_pull()](#gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 8-bit values.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   The 8-bit removed value

## [◆ ](#ga96a2b1f07f3a7958057d9c7cc1f01b73)net\_buf\_push()

| | void \* net\_buf\_push | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Prepare data to be added at the start of the buffer.

Modifies the data pointer and buffer length to account for more data in the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | len | Number of bytes to add to the beginning. |

Returns
:   The new beginning of the buffer data.

## [◆ ](#ga6dd756ff8332d076f5d37c69e6c534b5)net\_buf\_push\_be16()

| | void net\_buf\_push\_be16 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 16-bit value to the beginning of the buffer.

Adds 16-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 16-bit value to be pushed to the buffer. |

## [◆ ](#ga87338399d8ecd64a894908ed4a2f710b)net\_buf\_push\_be24()

| | void net\_buf\_push\_be24 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 24-bit value to the beginning of the buffer.

Adds 24-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 24-bit value to be pushed to the buffer. |

## [◆ ](#gae4e64a23708ed910fb6c3ab8ba481a4c)net\_buf\_push\_be32()

| | void net\_buf\_push\_be32 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 32-bit value to the beginning of the buffer.

Adds 32-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 32-bit value to be pushed to the buffer. |

## [◆ ](#ga512f84e686ff70a5589557575ccda1f8)net\_buf\_push\_be40()

| | void net\_buf\_push\_be40 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 40-bit value to the beginning of the buffer.

Adds 40-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 40-bit value to be pushed to the buffer. |

## [◆ ](#gabfbcb051019ff210cc2b85adcf4bc821)net\_buf\_push\_be48()

| | void net\_buf\_push\_be48 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 48-bit value to the beginning of the buffer.

Adds 48-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 48-bit value to be pushed to the buffer. |

## [◆ ](#ga43ff5faab0b099a355b9b96b7b0e3d8c)net\_buf\_push\_be64()

| | void net\_buf\_push\_be64 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 64-bit value to the beginning of the buffer.

Adds 64-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 64-bit value to be pushed to the buffer. |

## [◆ ](#gab6c84c6846c06c2b339bc88df35e2655)net\_buf\_push\_le16()

| | void net\_buf\_push\_le16 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 16-bit value to the beginning of the buffer.

Adds 16-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 16-bit value to be pushed to the buffer. |

## [◆ ](#ga87524ac50e53ba59c6692af10cf001b9)net\_buf\_push\_le24()

| | void net\_buf\_push\_le24 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 24-bit value to the beginning of the buffer.

Adds 24-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 24-bit value to be pushed to the buffer. |

## [◆ ](#ga97c9046185d6a1e9235bf6914c72dfc4)net\_buf\_push\_le32()

| | void net\_buf\_push\_le32 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 32-bit value to the beginning of the buffer.

Adds 32-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 32-bit value to be pushed to the buffer. |

## [◆ ](#gaefab4a755cf4fb7d2b4a142a9351c189)net\_buf\_push\_le40()

| | void net\_buf\_push\_le40 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 40-bit value to the beginning of the buffer.

Adds 40-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 40-bit value to be pushed to the buffer. |

## [◆ ](#ga852654f7e59951bf3536e3f4e98761bf)net\_buf\_push\_le48()

| | void net\_buf\_push\_le48 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 48-bit value to the beginning of the buffer.

Adds 48-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 48-bit value to be pushed to the buffer. |

## [◆ ](#gad4ee42b023881f80211fbeca53a0f25d)net\_buf\_push\_le64()

| | void net\_buf\_push\_le64 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 64-bit value to the beginning of the buffer.

Adds 64-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 64-bit value to be pushed to the buffer. |

## [◆ ](#ga7e9daccec8cae1b9bfda52b0758adf0c)net\_buf\_push\_mem()

| | void \* net\_buf\_push\_mem | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | const void \* | *mem*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Copies the given number of bytes to the start of the buffer.

Modifies the data pointer and buffer length to account for more data in the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | mem | Location of data to be added. |
    | len | Length of data to be added. |

Returns
:   The new beginning of the buffer data.

## [◆ ](#ga9093202ba0a22bfa519bbe32d4585186)net\_buf\_push\_u8()

| | void net\_buf\_push\_u8 | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Push 8-bit value to the beginning of the buffer.

Adds 8-bit value the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 8-bit value to be pushed to the buffer. |

## [◆ ](#ga7e1bcc520b7bffcbd9c1d3d308100047)net\_buf\_put()

| void net\_buf\_put | ( | struct [k\_fifo](structk__fifo.md) \* | *fifo*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Put a buffer to the end of a FIFO.

If the buffer contains follow-up fragments this function will take care of inserting them as well into the FIFO.

Parameters
:   | fifo | Which FIFO to put the buffer to. |
    | --- | --- |
    | buf | Buffer. |

## [◆ ](#ga29387b2a672bf2bb8739046a46f3601f)net\_buf\_ref()

| struct [net\_buf](structnet__buf.md) \* net\_buf\_ref | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Increment the reference count of a buffer.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   the buffer newly referenced

## [◆ ](#ga5da86c8ea703ab3f01c408cce73b0651)net\_buf\_remove\_be16()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_remove\_be16 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 16 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 16-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   16-bit value converted from big endian to host endian.

## [◆ ](#ga6f346a9af570528d238592851240fd74)net\_buf\_remove\_be24()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_remove\_be24 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 24 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 24-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   24-bit value converted from big endian to host endian.

## [◆ ](#gacce707d646d7008ec3167af1a0b20da8)net\_buf\_remove\_be32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_remove\_be32 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 32 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 32-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   32-bit value converted from big endian to host endian.

## [◆ ](#gae2920eab3c56d0d462811b83961df466)net\_buf\_remove\_be40()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_remove\_be40 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 40 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 40-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   40-bit value converted from big endian to host endian.

## [◆ ](#gaab0e3bcc21c958c01ef076cd0efe087c)net\_buf\_remove\_be48()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_remove\_be48 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 48 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 48-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   48-bit value converted from big endian to host endian.

## [◆ ](#ga8b9edd213da2d48dfb8d70a8d307ba13)net\_buf\_remove\_be64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_remove\_be64 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 64 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 64-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   64-bit value converted from big endian to host endian.

## [◆ ](#gaaf654110fb6a8bdfc27433945d4d1308)net\_buf\_remove\_le16()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_remove\_le16 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 16 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 16-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   16-bit value converted from little endian to host endian.

## [◆ ](#ga903f59c8dea1b2c54969b567fe315041)net\_buf\_remove\_le24()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_remove\_le24 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 24 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 24-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   24-bit value converted from little endian to host endian.

## [◆ ](#gae9321a469cc751c58cfb532afd57d265)net\_buf\_remove\_le32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_remove\_le32 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 32 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 32-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   32-bit value converted from little endian to host endian.

## [◆ ](#ga57150a1ba09b28e5c3b04bdefce7ed8e)net\_buf\_remove\_le40()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_remove\_le40 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 40 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 40-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   40-bit value converted from little endian to host endian.

## [◆ ](#ga0c147d9f95e2224696a8ace26f63a300)net\_buf\_remove\_le48()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_remove\_le48 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 48 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 48-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   48-bit value converted from little endian to host endian.

## [◆ ](#ga447b9c6be3fe04a50eb35dd29f190b6d)net\_buf\_remove\_le64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_remove\_le64 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 64 bits from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 64-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   64-bit value converted from little endian to host endian.

## [◆ ](#gace5ad98eac4772db3b0fa2181912f1f0)net\_buf\_remove\_mem()

| | void \* net\_buf\_remove\_mem | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove data from the end of the buffer.

Removes data from the end of the buffer by modifying the buffer length.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | len | Number of bytes to remove. |

Returns
:   New end of the buffer data.

## [◆ ](#gad954b9f37790d5e7087db7db7bdedd41)net\_buf\_remove\_u8()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf\_remove\_u8 | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove a 8-bit value from the end of the buffer.

Same idea as with [net\_buf\_remove\_mem()](#gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 8-bit values.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   The 8-bit removed value

## [◆ ](#ga8ac58ad4f73b498bef2ff3ac7e30c6c3)net\_buf\_reserve()

| | void net\_buf\_reserve | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *reserve* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Initialize buffer with the given headroom.

The buffer is not expected to contain any data when this API is called.

Parameters
:   | buf | Buffer to initialize. |
    | --- | --- |
    | reserve | How much headroom to reserve. |

## [◆ ](#ga1292f38b096fd80e31889aff44b0c021)net\_buf\_reset()

| void net\_buf\_reset | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Reset buffer.

Reset buffer data and flags so it can be reused for other purposes.

Parameters
:   | buf | Buffer to reset. |
    | --- | --- |

## [◆ ](#ga1906e637c848948f5780428a99b3341e)net\_buf\_simple\_add()

| void \* net\_buf\_simple\_add | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Prepare data to be added at the end of the buffer.

Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | len | Number of bytes to increment the length with. |

Returns
:   The original tail of the buffer.

## [◆ ](#ga910f2b9df58fb0706aa40e3b80f235aa)net\_buf\_simple\_add\_be16()

| void net\_buf\_simple\_add\_be16 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 16-bit value at the end of the buffer.

Adds 16-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 16-bit value to be added. |

## [◆ ](#ga5eb09afeff062af577094d2d3f5fdec8)net\_buf\_simple\_add\_be24()

| void net\_buf\_simple\_add\_be24 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 24-bit value at the end of the buffer.

Adds 24-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 24-bit value to be added. |

## [◆ ](#gaac5cd20776d8e7bb4db77cbe5366373c)net\_buf\_simple\_add\_be32()

| void net\_buf\_simple\_add\_be32 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 32-bit value at the end of the buffer.

Adds 32-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 32-bit value to be added. |

## [◆ ](#ga69bdaf4373693bb468cf3876e9edf239)net\_buf\_simple\_add\_be40()

| void net\_buf\_simple\_add\_be40 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 40-bit value at the end of the buffer.

Adds 40-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 40-bit value to be added. |

## [◆ ](#gadb433fb4a1a61702c0615359a4340171)net\_buf\_simple\_add\_be48()

| void net\_buf\_simple\_add\_be48 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 48-bit value at the end of the buffer.

Adds 48-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 48-bit value to be added. |

## [◆ ](#ga8e31a7b6537d7634e346236534d2a6d0)net\_buf\_simple\_add\_be64()

| void net\_buf\_simple\_add\_be64 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 64-bit value at the end of the buffer.

Adds 64-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 64-bit value to be added. |

## [◆ ](#gaa2daf3b20074ff1a23806ce88becebf5)net\_buf\_simple\_add\_le16()

| void net\_buf\_simple\_add\_le16 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 16-bit value at the end of the buffer.

Adds 16-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 16-bit value to be added. |

## [◆ ](#gaf1a89eb15eed79003412ba5a32a35cf6)net\_buf\_simple\_add\_le24()

| void net\_buf\_simple\_add\_le24 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 24-bit value at the end of the buffer.

Adds 24-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 24-bit value to be added. |

## [◆ ](#ga3bf1bcff840dddd721f2c49ef0ed7c56)net\_buf\_simple\_add\_le32()

| void net\_buf\_simple\_add\_le32 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 32-bit value at the end of the buffer.

Adds 32-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 32-bit value to be added. |

## [◆ ](#ga67da71ba5942cc11e95aa5ba02cb8552)net\_buf\_simple\_add\_le40()

| void net\_buf\_simple\_add\_le40 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 40-bit value at the end of the buffer.

Adds 40-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 40-bit value to be added. |

## [◆ ](#ga5be8c9f33df5b31c15df193a7116ce25)net\_buf\_simple\_add\_le48()

| void net\_buf\_simple\_add\_le48 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 48-bit value at the end of the buffer.

Adds 48-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 48-bit value to be added. |

## [◆ ](#ga79dc411da328b847dcf1903d71eaf011)net\_buf\_simple\_add\_le64()

| void net\_buf\_simple\_add\_le64 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add 64-bit value at the end of the buffer.

Adds 64-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 64-bit value to be added. |

## [◆ ](#gac37209c1e5097e5610860943fb7d0115)net\_buf\_simple\_add\_mem()

| void \* net\_buf\_simple\_add\_mem | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | const void \* | *mem*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Copy given number of bytes from memory to the end of the buffer.

Increments the data length of the buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | mem | Location of data to be added. |
    | len | Length of data to be added |

Returns
:   The original tail of the buffer.

## [◆ ](#ga8ff9344b8d8deba1b72b8fca048a525c)net\_buf\_simple\_add\_u8()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* net\_buf\_simple\_add\_u8 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Add (8-bit) byte at the end of the buffer.

Increments the data length of the buffer to account for more data at the end.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | byte value to be added. |

Returns
:   Pointer to the value added

## [◆ ](#ga0186c153b72a379affdd3e2e3994b5a7)net\_buf\_simple\_clone()

| void net\_buf\_simple\_clone | ( | const struct [net\_buf\_simple](structnet__buf__simple.md) \* | *original*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *clone* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Clone buffer state, using the same data buffer.

Initializes a buffer to point to the same data as an existing buffer. Allows operations on the same data without altering the length and offset of the original.

Parameters
:   | original | Buffer to clone. |
    | --- | --- |
    | clone | The new clone. |

## [◆ ](#gaafcb52db2daf1c4451a600e7b647e55c)net\_buf\_simple\_headroom()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_buf\_simple\_headroom | ( | const struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Check buffer headroom.

Check how much free space there is in the beginning of the buffer.

buf A valid pointer on a buffer

Returns
:   Number of bytes available in the beginning of the buffer.

## [◆ ](#ga040279b601191367dee013bab9916d8d)net\_buf\_simple\_init()

| | void net\_buf\_simple\_init | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *reserve\_head* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Initialize a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object.

This needs to be called after creating a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object using the NET\_BUF\_SIMPLE macro.

Parameters
:   | buf | Buffer to initialize. |
    | --- | --- |
    | reserve\_head | Headroom to reserve. |

## [◆ ](#ga7fac47a2a25eaca39c5d14f1f55b485d)net\_buf\_simple\_init\_with\_data()

| void net\_buf\_simple\_init\_with\_data | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Initialize a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object with data.

Initialized buffer object with external data.

Parameters
:   | buf | Buffer to initialize. |
    | --- | --- |
    | data | External data pointer |
    | size | Amount of data the pointed data buffer if able to fit. |

## [◆ ](#gabfe255688a80c0abea866762ff4c5a6c)net\_buf\_simple\_max\_len()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_simple\_max\_len | ( | const struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Check maximum [net\_buf\_simple::len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3 "Length of the data behind the data pointer.") value.

This value is depending on the number of bytes being reserved as headroom.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   Number of bytes usable behind the [net\_buf\_simple::data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1 "Pointer to the start of data in the buffer.") pointer.

## [◆ ](#gaf5ab4a5fe4a6226be72a510fea0ed8a8)net\_buf\_simple\_pull()

| void \* net\_buf\_simple\_pull | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Remove data from the beginning of the buffer.

Removes data from the beginning of the buffer by modifying the data pointer and buffer length.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | len | Number of bytes to remove. |

Returns
:   New beginning of the buffer data.

## [◆ ](#gae36458ba05a4ab89e429be4cfd264440)net\_buf\_simple\_pull\_be16()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_simple\_pull\_be16 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 16 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 16-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   16-bit value converted from big endian to host endian.

## [◆ ](#ga4c24d445d6b75c850a9e95fb242a50e1)net\_buf\_simple\_pull\_be24()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_simple\_pull\_be24 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 24 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 24-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   24-bit value converted from big endian to host endian.

## [◆ ](#ga1a53892ed75f994bbbb3a2bcf1743d3c)net\_buf\_simple\_pull\_be32()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_simple\_pull\_be32 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 32 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 32-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   32-bit value converted from big endian to host endian.

## [◆ ](#gaa665830dad59ac957f79c7f1cc84aed5)net\_buf\_simple\_pull\_be40()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_pull\_be40 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 40 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 40-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   40-bit value converted from big endian to host endian.

## [◆ ](#ga19bdefe740fe94a42fba76d71b4ef6e2)net\_buf\_simple\_pull\_be48()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_pull\_be48 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 48 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 48-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   48-bit value converted from big endian to host endian.

## [◆ ](#gad07f0d49a7db99063077de493e7b0712)net\_buf\_simple\_pull\_be64()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_pull\_be64 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 64 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 64-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   64-bit value converted from big endian to host endian.

## [◆ ](#gad59d180ae81b55f6d618565a37d25dba)net\_buf\_simple\_pull\_le16()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_simple\_pull\_le16 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 16 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 16-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   16-bit value converted from little endian to host endian.

## [◆ ](#ga4c9d2ac72a176c49ec224353b5566eb9)net\_buf\_simple\_pull\_le24()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_simple\_pull\_le24 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 24 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 24-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   24-bit value converted from little endian to host endian.

## [◆ ](#ga38df82e6ba9bc2c75133200f7fa75353)net\_buf\_simple\_pull\_le32()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_simple\_pull\_le32 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 32 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 32-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   32-bit value converted from little endian to host endian.

## [◆ ](#gad669c07efe5cb90ebffcc76d9c1029a1)net\_buf\_simple\_pull\_le40()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_pull\_le40 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 40 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 40-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   40-bit value converted from little endian to host endian.

## [◆ ](#ga69fbfbd72b17783c5ee12b4b2ac9af46)net\_buf\_simple\_pull\_le48()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_pull\_le48 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 48 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 48-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   48-bit value converted from little endian to host endian.

## [◆ ](#ga7e0e2d0adbe9062d08f5d8afc7acd89e)net\_buf\_simple\_pull\_le64()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_pull\_le64 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 64 bits from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 64-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   64-bit value converted from little endian to host endian.

## [◆ ](#ga9c676fdbd6e999a9eab26b13d3608e0c)net\_buf\_simple\_pull\_mem()

| void \* net\_buf\_simple\_pull\_mem | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Remove data from the beginning of the buffer.

Removes data from the beginning of the buffer by modifying the data pointer and buffer length.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | len | Number of bytes to remove. |

Returns
:   Pointer to the old location of the buffer data.

## [◆ ](#ga09a261c615136fd39834cd301fc692e7)net\_buf\_simple\_pull\_u8()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf\_simple\_pull\_u8 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove a 8-bit value from the beginning of the buffer.

Same idea as with [net\_buf\_simple\_pull()](#gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 8-bit values.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   The 8-bit removed value

## [◆ ](#ga64df9754665440370340c6dddde625d1)net\_buf\_simple\_push()

| void \* net\_buf\_simple\_push | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Prepare data to be added to the start of the buffer.

Modifies the data pointer and buffer length to account for more data in the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | len | Number of bytes to add to the beginning. |

Returns
:   The new beginning of the buffer data.

## [◆ ](#ga827bd85eba0dbd098790d84d22e8e32d)net\_buf\_simple\_push\_be16()

| void net\_buf\_simple\_push\_be16 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 16-bit value to the beginning of the buffer.

Adds 16-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 16-bit value to be pushed to the buffer. |

## [◆ ](#gabfddd4956ec1e356002a3122fea74b72)net\_buf\_simple\_push\_be24()

| void net\_buf\_simple\_push\_be24 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 24-bit value to the beginning of the buffer.

Adds 24-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 24-bit value to be pushed to the buffer. |

## [◆ ](#gad0c3b8fdeaad6437c3dfcbb03fa52426)net\_buf\_simple\_push\_be32()

| void net\_buf\_simple\_push\_be32 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 32-bit value to the beginning of the buffer.

Adds 32-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 32-bit value to be pushed to the buffer. |

## [◆ ](#gad65bcaf8401e6f5ffff81a998cfb8fe5)net\_buf\_simple\_push\_be40()

| void net\_buf\_simple\_push\_be40 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 40-bit value to the beginning of the buffer.

Adds 40-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 40-bit value to be pushed to the buffer. |

## [◆ ](#ga1ea39c7d7e9ba4e10d31d818e45e192a)net\_buf\_simple\_push\_be48()

| void net\_buf\_simple\_push\_be48 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 48-bit value to the beginning of the buffer.

Adds 48-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 48-bit value to be pushed to the buffer. |

## [◆ ](#gafea2201655955ab004b5f77106998ae9)net\_buf\_simple\_push\_be64()

| void net\_buf\_simple\_push\_be64 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 64-bit value to the beginning of the buffer.

Adds 64-bit value in big endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 64-bit value to be pushed to the buffer. |

## [◆ ](#ga50cd64438d8f218e3d1ef8b53b7d41a6)net\_buf\_simple\_push\_le16()

| void net\_buf\_simple\_push\_le16 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 16-bit value to the beginning of the buffer.

Adds 16-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 16-bit value to be pushed to the buffer. |

## [◆ ](#gabe52d6735d835edc361666bb3413b907)net\_buf\_simple\_push\_le24()

| void net\_buf\_simple\_push\_le24 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 24-bit value to the beginning of the buffer.

Adds 24-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 24-bit value to be pushed to the buffer. |

## [◆ ](#ga8662e6bada476c0d48cebea4661b2ac1)net\_buf\_simple\_push\_le32()

| void net\_buf\_simple\_push\_le32 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 32-bit value to the beginning of the buffer.

Adds 32-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 32-bit value to be pushed to the buffer. |

## [◆ ](#ga745ab6f34138b506b42f78e0975a5d2e)net\_buf\_simple\_push\_le40()

| void net\_buf\_simple\_push\_le40 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 40-bit value to the beginning of the buffer.

Adds 40-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 40-bit value to be pushed to the buffer. |

## [◆ ](#ga66b44897e336f31e3ecbf4717bec274e)net\_buf\_simple\_push\_le48()

| void net\_buf\_simple\_push\_le48 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 48-bit value to the beginning of the buffer.

Adds 48-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 48-bit value to be pushed to the buffer. |

## [◆ ](#ga771634e50e2bf7c291565ce6b2af7e85)net\_buf\_simple\_push\_le64()

| void net\_buf\_simple\_push\_le64 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 64-bit value to the beginning of the buffer.

Adds 64-bit value in little endian format to the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 64-bit value to be pushed to the buffer. |

## [◆ ](#gaaa838083c610f7426c509efaae69a511)net\_buf\_simple\_push\_mem()

| void \* net\_buf\_simple\_push\_mem | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | const void \* | *mem*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Copy given number of bytes from memory to the start of the buffer.

Modifies the data pointer and buffer length to account for more data in the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | mem | Location of data to be added. |
    | len | Length of data to be added. |

Returns
:   The new beginning of the buffer data.

## [◆ ](#ga0f19da70bfc8f597680ee02c21226a77)net\_buf\_simple\_push\_u8()

| void net\_buf\_simple\_push\_u8 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *val* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Push 8-bit value to the beginning of the buffer.

Adds 8-bit value the beginning of the buffer.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | val | 8-bit value to be pushed to the buffer. |

## [◆ ](#ga93f9f84845601df4ffc118be1ffd2fee)net\_buf\_simple\_remove\_be16()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_simple\_remove\_be16 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 16 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 16-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   16-bit value converted from big endian to host endian.

## [◆ ](#ga9b39384162a91d7d07e037a9ada782dd)net\_buf\_simple\_remove\_be24()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_simple\_remove\_be24 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 24 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 24-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   24-bit value converted from big endian to host endian.

## [◆ ](#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)net\_buf\_simple\_remove\_be32()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_simple\_remove\_be32 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 32 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 32-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   32-bit value converted from big endian to host endian.

## [◆ ](#ga9abd2bccc90cf654556c18322888d131)net\_buf\_simple\_remove\_be40()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_remove\_be40 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 40 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 40-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   40-bit value converted from big endian to host endian.

## [◆ ](#gab93d22797c3f406179c4c145241d6abb)net\_buf\_simple\_remove\_be48()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_remove\_be48 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 48 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 48-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   48-bit value converted from big endian to host endian.

## [◆ ](#ga602fae83e2ecf47552a11f9282619932)net\_buf\_simple\_remove\_be64()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_remove\_be64 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 64 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 64-bit big endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   64-bit value converted from big endian to host endian.

## [◆ ](#ga0b57f9ca2f3837e94cd7862e37efc01c)net\_buf\_simple\_remove\_le16()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_simple\_remove\_le16 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 16 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 16-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   16-bit value converted from little endian to host endian.

## [◆ ](#ga4e2fef883228f7de41af3cf90648c3c5)net\_buf\_simple\_remove\_le24()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_simple\_remove\_le24 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 24 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 24-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   24-bit value converted from little endian to host endian.

## [◆ ](#ga9e8d016ce384378142fdec6c8dde2457)net\_buf\_simple\_remove\_le32()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_buf\_simple\_remove\_le32 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 32 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 32-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   32-bit value converted from little endian to host endian.

## [◆ ](#ga2c937164e648fe8b854cb1144051b6b9)net\_buf\_simple\_remove\_le40()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_remove\_le40 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 40 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 40-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   40-bit value converted from little endian to host endian.

## [◆ ](#gac0628bbbe5d9c2b82766d5a17e767696)net\_buf\_simple\_remove\_le48()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_remove\_le48 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 48 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 48-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   48-bit value converted from little endian to host endian.

## [◆ ](#ga560bd7b181c7f08599ae9241b6ce99fd)net\_buf\_simple\_remove\_le64()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_buf\_simple\_remove\_le64 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove and convert 64 bits from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 64-bit little endian data.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   64-bit value converted from little endian to host endian.

## [◆ ](#ga8473bdffadc05b22335a321df89f4b83)net\_buf\_simple\_remove\_mem()

| void \* net\_buf\_simple\_remove\_mem | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Remove data from the end of the buffer.

Removes data from the end of the buffer by modifying the buffer length.

Parameters
:   | buf | Buffer to update. |
    | --- | --- |
    | len | Number of bytes to remove. |

Returns
:   New end of the buffer data.

## [◆ ](#gaf508f74e5e050a7294e8a70bd3725fc3)net\_buf\_simple\_remove\_u8()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_buf\_simple\_remove\_u8 | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Remove a 8-bit value from the end of the buffer.

Same idea as with [net\_buf\_simple\_remove\_mem()](#ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 8-bit values.

Parameters
:   | buf | A valid pointer on a buffer. |
    | --- | --- |

Returns
:   The 8-bit removed value

## [◆ ](#ga0e5d3d938becfefc4f4b4d083cb467aa)net\_buf\_simple\_reserve()

| void net\_buf\_simple\_reserve | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *reserve* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Initialize buffer with the given headroom.

The buffer is not expected to contain any data when this API is called.

Parameters
:   | buf | Buffer to initialize. |
    | --- | --- |
    | reserve | How much headroom to reserve. |

## [◆ ](#ga4b537e913e132448cbf56976504ddddd)net\_buf\_simple\_reset()

| | void net\_buf\_simple\_reset | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Reset buffer.

Reset buffer data so it can be reused for other purposes.

Parameters
:   | buf | Buffer to reset. |
    | --- | --- |

## [◆ ](#gaedd36481657a7a9d108659d56e131721)net\_buf\_simple\_restore()

| | void net\_buf\_simple\_restore | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) \* | *state* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Restore the parsing state of a buffer.

Restores the parsing state of a buffer from a state previously stored by [net\_buf\_simple\_save()](#gabf5b098aa0926d9b7fb88baff8a3e2d8).

Parameters
:   | buf | Buffer to which the state should be restored. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Stored state. |

## [◆ ](#gabf5b098aa0926d9b7fb88baff8a3e2d8)net\_buf\_simple\_save()

| | void net\_buf\_simple\_save | ( | const struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) \* | *state* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Save the parsing state of a buffer.

Saves the parsing state of a buffer so it can be restored later.

Parameters
:   | buf | Buffer from which the state should be saved. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Storage for the state. |

## [◆ ](#gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8)net\_buf\_simple\_tail()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* net\_buf\_simple\_tail | ( | const struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Get the tail pointer for a buffer.

Get a pointer to the end of the data in a buffer.

Parameters
:   | buf | Buffer. |
    | --- | --- |

Returns
:   Tail pointer for the buffer.

## [◆ ](#ga23e85f8f681fd7617032b4ca40dc62c5)net\_buf\_simple\_tailroom()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_buf\_simple\_tailroom | ( | const struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Check buffer tailroom.

Check how much free space there is at the end of the buffer.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   Number of bytes available at the end of the buffer.

## [◆ ](#ga2d7096280d4fa6f5e32c4674d542889b)net\_buf\_skip()

| | struct [net\_buf](structnet__buf.md) \* net\_buf\_skip | ( | struct [net\_buf](structnet__buf.md) \* | *buf*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Skip N number of bytes in a [net\_buf](structnet__buf.md "Network buffer representation.").

Skip N number of bytes starting from fragment's offset. If the total length of data is placed in multiple fragments, this function will skip from all fragments until it reaches N number of bytes. Any fully skipped buffers are removed from the [net\_buf](structnet__buf.md "Network buffer representation.") list.

Parameters
:   | buf | Network buffer. |
    | --- | --- |
    | len | Total length of data to be skipped. |

Returns
:   Pointer to the fragment or NULL and pos is 0 after successful skip, NULL and pos is 0xffff otherwise.

## [◆ ](#ga218d4a0c160c57a44946154478724cb3)net\_buf\_slist\_get()

| struct [net\_buf](structnet__buf.md) \* net\_buf\_slist\_get | ( | [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \* | *list* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Get a buffer from a list.

If the buffer had any fragments, these will automatically be recovered from the list as well and be placed to the buffer's fragment list.

Parameters
:   | list | Which list to take the buffer from. |
    | --- | --- |

Returns
:   New buffer or NULL if the FIFO is empty.

## [◆ ](#ga6d2dfc45e1e5acf21fe08359a4f92a18)net\_buf\_slist\_put()

| void net\_buf\_slist\_put | ( | [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \* | *list*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Put a buffer into a list.

If the buffer contains follow-up fragments this function will take care of inserting them as well into the list.

Parameters
:   | list | Which list to append the buffer to. |
    | --- | --- |
    | buf | Buffer. |

## [◆ ](#gaedb10a84b352a3d7716bef979af2ab31)net\_buf\_tail()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* net\_buf\_tail | ( | const struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Get the tail pointer for a buffer.

Get a pointer to the end of the data in a buffer.

Parameters
:   | buf | Buffer. |
    | --- | --- |

Returns
:   Tail pointer for the buffer.

## [◆ ](#gaecbc6adf16469e3366c88445ea7a553a)net\_buf\_tailroom()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_buf\_tailroom | ( | const struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Check buffer tailroom.

Check how much free space there is at the end of the buffer.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   Number of bytes available at the end of the buffer.

## [◆ ](#gabedcb728bc2fc0c2b5319a8fd87e8273)net\_buf\_unref()

| void net\_buf\_unref | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Decrements the reference count of a buffer.

The buffer is put back into the pool if the reference count reaches zero.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

## [◆ ](#gaf2df457abe3e56d47107b76bdc004756)net\_buf\_user\_data()

| | void \* net\_buf\_user\_data | ( | const struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[buf.h](net_2buf_8h.md)>`

Get a pointer to the user data of a buffer.

Parameters
:   | buf | A valid pointer on a buffer |
    | --- | --- |

Returns
:   Pointer to the user data of the buffer.

## [◆ ](#ga4d1dd56ca8d32d3cfda114fd36761d0d)net\_buf\_user\_data\_copy()

| int net\_buf\_user\_data\_copy | ( | struct [net\_buf](structnet__buf.md) \* | *dst*, |
| --- | --- | --- | --- |
|  |  | const struct [net\_buf](structnet__buf.md) \* | *src* ) |

`#include <[buf.h](net_2buf_8h.md)>`

Copy user data from one to another buffer.

Parameters
:   | dst | A valid pointer to a buffer gettings its user data overwritten. |
    | --- | --- |
    | src | A valid pointer to a buffer gettings its user data copied. User data size must be equal to or exceed *dst*. |

Returns
:   0 on success or negative error number on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
