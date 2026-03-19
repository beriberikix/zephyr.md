---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__buf_8h.html
original_path: doxygen/html/net__buf_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_buf.h File Reference

Buffer management.
[More...](#details)

`#include <stddef.h>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](net__buf_8h_source.md)

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
| #define | [NET\_BUF\_SIMPLE\_DEFINE](group__net__buf.md#gaf85aa0b705bb4fbe2630191fde802501)(\_name, \_size) |
|  | Define a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") stack variable. |
| #define | [NET\_BUF\_SIMPLE\_DEFINE\_STATIC](group__net__buf.md#ga21ced8b3082d57bf071008de5fffc0f4)(\_name, \_size) |
|  | Define a static [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") variable. |
| #define | [NET\_BUF\_SIMPLE](group__net__buf.md#ga0b01dc80027d13b1895379d4d1397207)(\_size) |
|  | Define a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") stack variable and get a pointer to it. |
| #define | [NET\_BUF\_EXTERNAL\_DATA](group__net__buf.md#gaaeacbdf3cfda12691c75253015e5c19a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag indicating that the buffer's associated data pointer, points to externally allocated memory. |
| #define | [NET\_BUF\_POOL\_HEAP\_DEFINE](group__net__buf.md#ga61671ac866081d31dfe9eddbf3b6f210)(\_name, \_count, \_ud\_size, \_destroy) |
|  | Define a new pool for buffers using the heap for the data. |
| #define | [NET\_BUF\_POOL\_FIXED\_DEFINE](group__net__buf.md#gacc53824e01db7935bcc9cad564b716cd)(\_name, \_count, \_data\_size, \_ud\_size, \_destroy) |
|  | Define a new pool for buffers based on fixed-size data. |
| #define | [NET\_BUF\_POOL\_VAR\_DEFINE](group__net__buf.md#ga90e691e793c964847d737f5ecf7646ec)(\_name, \_count, \_data\_size, \_ud\_size, \_destroy) |
|  | Define a new pool for buffers with variable size payloads. |
| #define | [NET\_BUF\_POOL\_DEFINE](group__net__buf.md#ga810aba8ba321fd012edc238ea9fe19dc)(\_name, \_count, \_size, \_ud\_size, \_destroy) |
|  | Define a new pool for buffers. |

| Typedefs | |
| --- | --- |
| typedef struct [net\_buf](structnet__buf.md) \*(\* | [net\_buf\_allocator\_cb](group__net__buf.md#ga9b74d094a45daf74cd230eaa4fcbc065)) ([k\_timeout\_t](structk__timeout__t.md) timeout, void \*user\_data) |
|  | Network buffer allocator callback. |

| Functions | |
| --- | --- |
| static void | [net\_buf\_simple\_init](group__net__buf.md#ga040279b601191367dee013bab9916d8d) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) reserve\_head) |
|  | Initialize a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object. |
| void | [net\_buf\_simple\_init\_with\_data](group__net__buf.md#ga7fac47a2a25eaca39c5d14f1f55b485d) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Initialize a [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") object with data. |
| static void | [net\_buf\_simple\_reset](group__net__buf.md#ga4b537e913e132448cbf56976504ddddd) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Reset buffer. |
| void | [net\_buf\_simple\_clone](group__net__buf.md#ga0186c153b72a379affdd3e2e3994b5a7) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*original, struct [net\_buf\_simple](structnet__buf__simple.md) \*clone) |
|  | Clone buffer state, using the same data buffer. |
| void \* | [net\_buf\_simple\_add](group__net__buf.md#ga1906e637c848948f5780428a99b3341e) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Prepare data to be added at the end of the buffer. |
| void \* | [net\_buf\_simple\_add\_mem](group__net__buf.md#gac37209c1e5097e5610860943fb7d0115) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, const void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Copy given number of bytes from memory to the end of the buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [net\_buf\_simple\_add\_u8](group__net__buf.md#ga8ff9344b8d8deba1b72b8fca048a525c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | Add (8-bit) byte at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le16](group__net__buf.md#gaa2daf3b20074ff1a23806ce88becebf5) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Add 16-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be16](group__net__buf.md#ga910f2b9df58fb0706aa40e3b80f235aa) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Add 16-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le24](group__net__buf.md#gaf1a89eb15eed79003412ba5a32a35cf6) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 24-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be24](group__net__buf.md#ga5eb09afeff062af577094d2d3f5fdec8) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 24-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le32](group__net__buf.md#ga3bf1bcff840dddd721f2c49ef0ed7c56) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 32-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be32](group__net__buf.md#gaac5cd20776d8e7bb4db77cbe5366373c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 32-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le40](group__net__buf.md#ga67da71ba5942cc11e95aa5ba02cb8552) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 40-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be40](group__net__buf.md#ga69bdaf4373693bb468cf3876e9edf239) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 40-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le48](group__net__buf.md#ga5be8c9f33df5b31c15df193a7116ce25) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 48-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be48](group__net__buf.md#gadb433fb4a1a61702c0615359a4340171) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 48-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_le64](group__net__buf.md#ga79dc411da328b847dcf1903d71eaf011) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 64-bit value at the end of the buffer. |
| void | [net\_buf\_simple\_add\_be64](group__net__buf.md#ga8e31a7b6537d7634e346236534d2a6d0) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 64-bit value at the end of the buffer. |
| void \* | [net\_buf\_simple\_remove\_mem](group__net__buf.md#ga8473bdffadc05b22335a321df89f4b83) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the end of the buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_buf\_simple\_remove\_u8](group__net__buf.md#gaf508f74e5e050a7294e8a70bd3725fc3) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove a 8-bit value from the end of the buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_simple\_remove\_le16](group__net__buf.md#ga0b57f9ca2f3837e94cd7862e37efc01c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 16 bits from the end of the buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_simple\_remove\_be16](group__net__buf.md#ga93f9f84845601df4ffc118be1ffd2fee) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 16 bits from the end of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_remove\_le24](group__net__buf.md#ga4e2fef883228f7de41af3cf90648c3c5) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 24 bits from the end of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_remove\_be24](group__net__buf.md#ga9b39384162a91d7d07e037a9ada782dd) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 24 bits from the end of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_remove\_le32](group__net__buf.md#ga9e8d016ce384378142fdec6c8dde2457) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 32 bits from the end of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_remove\_be32](group__net__buf.md#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 32 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_le40](group__net__buf.md#ga2c937164e648fe8b854cb1144051b6b9) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 40 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_be40](group__net__buf.md#ga9abd2bccc90cf654556c18322888d131) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 40 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_le48](group__net__buf.md#gac0628bbbe5d9c2b82766d5a17e767696) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 48 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_be48](group__net__buf.md#gab93d22797c3f406179c4c145241d6abb) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 48 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_le64](group__net__buf.md#ga560bd7b181c7f08599ae9241b6ce99fd) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 64 bits from the end of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_remove\_be64](group__net__buf.md#ga602fae83e2ecf47552a11f9282619932) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 64 bits from the end of the buffer. |
| void \* | [net\_buf\_simple\_push](group__net__buf.md#ga64df9754665440370340c6dddde625d1) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Prepare data to be added to the start of the buffer. |
| void \* | [net\_buf\_simple\_push\_mem](group__net__buf.md#gaaa838083c610f7426c509efaae69a511) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, const void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Copy given number of bytes from memory to the start of the buffer. |
| void | [net\_buf\_simple\_push\_le16](group__net__buf.md#ga50cd64438d8f218e3d1ef8b53b7d41a6) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Push 16-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be16](group__net__buf.md#ga827bd85eba0dbd098790d84d22e8e32d) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Push 16-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_u8](group__net__buf.md#ga0f19da70bfc8f597680ee02c21226a77) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | Push 8-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_le24](group__net__buf.md#gabe52d6735d835edc361666bb3413b907) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 24-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be24](group__net__buf.md#gabfddd4956ec1e356002a3122fea74b72) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 24-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_le32](group__net__buf.md#ga8662e6bada476c0d48cebea4661b2ac1) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 32-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be32](group__net__buf.md#gad0c3b8fdeaad6437c3dfcbb03fa52426) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 32-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_le40](group__net__buf.md#ga745ab6f34138b506b42f78e0975a5d2e) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 40-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be40](group__net__buf.md#gad65bcaf8401e6f5ffff81a998cfb8fe5) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 40-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_le48](group__net__buf.md#ga66b44897e336f31e3ecbf4717bec274e) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 48-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be48](group__net__buf.md#ga1ea39c7d7e9ba4e10d31d818e45e192a) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 48-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_le64](group__net__buf.md#ga771634e50e2bf7c291565ce6b2af7e85) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 64-bit value to the beginning of the buffer. |
| void | [net\_buf\_simple\_push\_be64](group__net__buf.md#gafea2201655955ab004b5f77106998ae9) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 64-bit value to the beginning of the buffer. |
| void \* | [net\_buf\_simple\_pull](group__net__buf.md#gaf5ab4a5fe4a6226be72a510fea0ed8a8) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the beginning of the buffer. |
| void \* | [net\_buf\_simple\_pull\_mem](group__net__buf.md#ga9c676fdbd6e999a9eab26b13d3608e0c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the beginning of the buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_buf\_simple\_pull\_u8](group__net__buf.md#ga09a261c615136fd39834cd301fc692e7) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove a 8-bit value from the beginning of the buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_simple\_pull\_le16](group__net__buf.md#gad59d180ae81b55f6d618565a37d25dba) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 16 bits from the beginning of the buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_simple\_pull\_be16](group__net__buf.md#gae36458ba05a4ab89e429be4cfd264440) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 16 bits from the beginning of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_pull\_le24](group__net__buf.md#ga4c9d2ac72a176c49ec224353b5566eb9) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 24 bits from the beginning of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_pull\_be24](group__net__buf.md#ga4c24d445d6b75c850a9e95fb242a50e1) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 24 bits from the beginning of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_pull\_le32](group__net__buf.md#ga38df82e6ba9bc2c75133200f7fa75353) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 32 bits from the beginning of the buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_simple\_pull\_be32](group__net__buf.md#ga1a53892ed75f994bbbb3a2bcf1743d3c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 32 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_le40](group__net__buf.md#gad669c07efe5cb90ebffcc76d9c1029a1) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 40 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_be40](group__net__buf.md#gaa665830dad59ac957f79c7f1cc84aed5) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 40 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_le48](group__net__buf.md#ga69fbfbd72b17783c5ee12b4b2ac9af46) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 48 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_be48](group__net__buf.md#ga19bdefe740fe94a42fba76d71b4ef6e2) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 48 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_le64](group__net__buf.md#ga7e0e2d0adbe9062d08f5d8afc7acd89e) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 64 bits from the beginning of the buffer. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_simple\_pull\_be64](group__net__buf.md#gad07f0d49a7db99063077de493e7b0712) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Remove and convert 64 bits from the beginning of the buffer. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [net\_buf\_simple\_tail](group__net__buf.md#gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Get the tail pointer for a buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_simple\_headroom](group__net__buf.md#gaafcb52db2daf1c4451a600e7b647e55c) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Check buffer headroom. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_simple\_tailroom](group__net__buf.md#ga23e85f8f681fd7617032b4ca40dc62c5) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Check buffer tailroom. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_simple\_max\_len](group__net__buf.md#gabfe255688a80c0abea866762ff4c5a6c) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Check maximum [net\_buf\_simple::len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3 "Length of the data behind the data pointer.") value. |
| static void | [net\_buf\_simple\_save](group__net__buf.md#gabf5b098aa0926d9b7fb88baff8a3e2d8) (const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Save the parsing state of a buffer. |
| static void | [net\_buf\_simple\_restore](group__net__buf.md#gaedd36481657a7a9d108659d56e131721) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Restore the parsing state of a buffer. |
| struct [net\_buf\_pool](structnet__buf__pool.md) \* | [net\_buf\_pool\_get](group__net__buf.md#ga145f4b2de7548814eaa7ba86fb123989) (int id) |
|  | Looks up a pool based on its ID. |
| int | [net\_buf\_id](group__net__buf.md#gacdf048dc0afc7ef67027117e0d51d3a3) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Get a zero-based index for a buffer. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_alloc\_fixed](group__net__buf.md#ga686df794ec6881625b54454a33587bab) (struct [net\_buf\_pool](structnet__buf__pool.md) \*pool, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a new fixed buffer from a pool. |
| static struct [net\_buf](structnet__buf.md) \* | [net\_buf\_alloc](group__net__buf.md#ga534366f3b5c7f41a28372c12149ca005) (struct [net\_buf\_pool](structnet__buf__pool.md) \*pool, [k\_timeout\_t](structk__timeout__t.md) timeout) |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_alloc\_len](group__net__buf.md#ga11d489aedcca82117965fa6ba9d11ca5) (struct [net\_buf\_pool](structnet__buf__pool.md) \*pool, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a new variable length buffer from a pool. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_alloc\_with\_data](group__net__buf.md#ga8c24d0761d6d38facb6cca60c7c13c0c) (struct [net\_buf\_pool](structnet__buf__pool.md) \*pool, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a new buffer from a pool but with external data pointer. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_get](group__net__buf.md#ga014a0e87afc143d06a7eaf6c2f04c742) (struct [k\_fifo](structk__fifo.md) \*fifo, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get a buffer from a FIFO. |
| static void | [net\_buf\_destroy](group__net__buf.md#ga739249547eb37b839b3c1ebdbcb88d28) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Destroy buffer from custom destroy callback. |
| void | [net\_buf\_reset](group__net__buf.md#ga1292f38b096fd80e31889aff44b0c021) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Reset buffer. |
| void | [net\_buf\_simple\_reserve](group__net__buf.md#ga0e5d3d938becfefc4f4b4d083cb467aa) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) reserve) |
|  | Initialize buffer with the given headroom. |
| void | [net\_buf\_slist\_put](group__net__buf.md#ga6d2dfc45e1e5acf21fe08359a4f92a18) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Put a buffer into a list. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_slist\_get](group__net__buf.md#ga218d4a0c160c57a44946154478724cb3) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Get a buffer from a list. |
| void | [net\_buf\_put](group__net__buf.md#ga7e1bcc520b7bffcbd9c1d3d308100047) (struct [k\_fifo](structk__fifo.md) \*fifo, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Put a buffer to the end of a FIFO. |
| void | [net\_buf\_unref](group__net__buf.md#gabedcb728bc2fc0c2b5319a8fd87e8273) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Decrements the reference count of a buffer. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_ref](group__net__buf.md#ga29387b2a672bf2bb8739046a46f3601f) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Increment the reference count of a buffer. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_clone](group__net__buf.md#gaf4d80e2878e3c790fff206bec820f03f) (struct [net\_buf](structnet__buf.md) \*buf, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Clone buffer. |
| static void \* | [net\_buf\_user\_data](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Get a pointer to the user data of a buffer. |
| int | [net\_buf\_user\_data\_copy](group__net__buf.md#ga4d1dd56ca8d32d3cfda114fd36761d0d) (struct [net\_buf](structnet__buf.md) \*dst, const struct [net\_buf](structnet__buf.md) \*src) |
|  | Copy user data from one to another buffer. |
| static void | [net\_buf\_reserve](group__net__buf.md#ga8ac58ad4f73b498bef2ff3ac7e30c6c3) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) reserve) |
|  | Initialize buffer with the given headroom. |
| static void \* | [net\_buf\_add](group__net__buf.md#ga30776d2b21f06d244c083af5c25b0f3e) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Prepare data to be added at the end of the buffer. |
| static void \* | [net\_buf\_add\_mem](group__net__buf.md#gacf4e2eba52975ba6728c79274a769d0f) (struct [net\_buf](structnet__buf.md) \*buf, const void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Copies the given number of bytes to the end of the buffer. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [net\_buf\_add\_u8](group__net__buf.md#ga868ac2bea103fed568b461cbcd45eda2) (struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | Add (8-bit) byte at the end of the buffer. |
| static void | [net\_buf\_add\_le16](group__net__buf.md#gadd6d01a3b1efd0de16f9bef975809404) (struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Add 16-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be16](group__net__buf.md#ga61878a9bd7462ca925eac39181f2972c) (struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Add 16-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_le24](group__net__buf.md#ga32b90364091ade229830686f03b25d4c) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 24-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be24](group__net__buf.md#ga0f3cd9f9b364a2d2125aea19221d3e1e) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 24-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_le32](group__net__buf.md#gae8ba33b6592ef7fd859b35d63b285d87) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 32-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be32](group__net__buf.md#ga5543d00c96f83970f8dbf3670a9dc3fc) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Add 32-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_le40](group__net__buf.md#ga62790f9644102f4952c250f6513a2ada) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 40-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be40](group__net__buf.md#ga70cb98da91de098a92fbd69712c2bde7) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 40-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_le48](group__net__buf.md#gaf19bf75c3d4d645b1eebf9254aa22790) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 48-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be48](group__net__buf.md#ga8fe6feb191ab338e91bd62f44e184deb) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 48-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_le64](group__net__buf.md#gac3f955f8fecc0e5971d2e5e8176e973e) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 64-bit value at the end of the buffer. |
| static void | [net\_buf\_add\_be64](group__net__buf.md#ga055f6eb7d5fbc9a3cf529a9ed00970c4) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Add 64-bit value at the end of the buffer. |
| static void \* | [net\_buf\_remove\_mem](group__net__buf.md#gace5ad98eac4772db3b0fa2181912f1f0) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the end of the buffer. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_buf\_remove\_u8](group__net__buf.md#gad954b9f37790d5e7087db7db7bdedd41) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove a 8-bit value from the end of the buffer. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_remove\_le16](group__net__buf.md#gaaf654110fb6a8bdfc27433945d4d1308) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 16 bits from the end of the buffer. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_remove\_be16](group__net__buf.md#ga5da86c8ea703ab3f01c408cce73b0651) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 16 bits from the end of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_remove\_be24](group__net__buf.md#ga6f346a9af570528d238592851240fd74) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 24 bits from the end of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_remove\_le24](group__net__buf.md#ga903f59c8dea1b2c54969b567fe315041) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 24 bits from the end of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_remove\_le32](group__net__buf.md#gae9321a469cc751c58cfb532afd57d265) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 32 bits from the end of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_remove\_be32](group__net__buf.md#gacce707d646d7008ec3167af1a0b20da8) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 32 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_le40](group__net__buf.md#ga57150a1ba09b28e5c3b04bdefce7ed8e) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 40 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_be40](group__net__buf.md#gae2920eab3c56d0d462811b83961df466) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 40 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_le48](group__net__buf.md#ga0c147d9f95e2224696a8ace26f63a300) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 48 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_be48](group__net__buf.md#gaab0e3bcc21c958c01ef076cd0efe087c) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 48 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_le64](group__net__buf.md#ga447b9c6be3fe04a50eb35dd29f190b6d) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 64 bits from the end of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_remove\_be64](group__net__buf.md#ga8b9edd213da2d48dfb8d70a8d307ba13) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 64 bits from the end of the buffer. |
| static void \* | [net\_buf\_push](group__net__buf.md#ga96a2b1f07f3a7958057d9c7cc1f01b73) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Prepare data to be added at the start of the buffer. |
| static void \* | [net\_buf\_push\_mem](group__net__buf.md#ga7e9daccec8cae1b9bfda52b0758adf0c) (struct [net\_buf](structnet__buf.md) \*buf, const void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Copies the given number of bytes to the start of the buffer. |
| static void | [net\_buf\_push\_u8](group__net__buf.md#ga9093202ba0a22bfa519bbe32d4585186) (struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val) |
|  | Push 8-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le16](group__net__buf.md#gab6c84c6846c06c2b339bc88df35e2655) (struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Push 16-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be16](group__net__buf.md#ga6dd756ff8332d076f5d37c69e6c534b5) (struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Push 16-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le24](group__net__buf.md#ga87524ac50e53ba59c6692af10cf001b9) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 24-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be24](group__net__buf.md#ga87338399d8ecd64a894908ed4a2f710b) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 24-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le32](group__net__buf.md#ga97c9046185d6a1e9235bf6914c72dfc4) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 32-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be32](group__net__buf.md#gae4e64a23708ed910fb6c3ab8ba481a4c) (struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Push 32-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le40](group__net__buf.md#gaefab4a755cf4fb7d2b4a142a9351c189) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 40-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be40](group__net__buf.md#ga512f84e686ff70a5589557575ccda1f8) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 40-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le48](group__net__buf.md#ga852654f7e59951bf3536e3f4e98761bf) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 48-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be48](group__net__buf.md#gabfbcb051019ff210cc2b85adcf4bc821) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 48-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_le64](group__net__buf.md#gad4ee42b023881f80211fbeca53a0f25d) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 64-bit value to the beginning of the buffer. |
| static void | [net\_buf\_push\_be64](group__net__buf.md#ga43ff5faab0b099a355b9b96b7b0e3d8c) (struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
|  | Push 64-bit value to the beginning of the buffer. |
| static void \* | [net\_buf\_pull](group__net__buf.md#gaef433d92734dd8691c292abdb823ba0e) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the beginning of the buffer. |
| static void \* | [net\_buf\_pull\_mem](group__net__buf.md#gaedc5ffe19bb0ec438e633023c3c5de74) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Remove data from the beginning of the buffer. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_buf\_pull\_u8](group__net__buf.md#ga71bb306d2ce459a60a8c3fc6dac54c90) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove a 8-bit value from the beginning of the buffer. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_pull\_le16](group__net__buf.md#gaed64e9f2b969f2c0d99cd281e73c860a) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 16 bits from the beginning of the buffer. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_pull\_be16](group__net__buf.md#ga97909a33c374a5c757fd2faf582139b7) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 16 bits from the beginning of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_pull\_le24](group__net__buf.md#ga85c505321484a50ed9422f24934ed077) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 24 bits from the beginning of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_pull\_be24](group__net__buf.md#ga8de937e8775879712ea0acbf60327a95) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 24 bits from the beginning of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_pull\_le32](group__net__buf.md#ga5f051078f1ffcc40e9ad40e7545a084f) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 32 bits from the beginning of the buffer. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_buf\_pull\_be32](group__net__buf.md#ga5f8f2e2244eb574b3e57d09d85412967) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 32 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_le40](group__net__buf.md#ga36b27c6373eb245f777164065386d100) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 40 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_be40](group__net__buf.md#ga050bdaccaec842482a02b096aa0c999f) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 40 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_le48](group__net__buf.md#ga7eeee45b6639146d1492f92263ee4f51) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 48 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_be48](group__net__buf.md#ga68934e105c4b3a8e27aa61b3ec5526db) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 48 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_le64](group__net__buf.md#ga9a3df35e2287cbcfe1b60e2efa52c64e) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 64 bits from the beginning of the buffer. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [net\_buf\_pull\_be64](group__net__buf.md#ga3c1e80741a49691e69e57c891d3edb05) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Remove and convert 64 bits from the beginning of the buffer. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_tailroom](group__net__buf.md#gaecbc6adf16469e3366c88445ea7a553a) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Check buffer tailroom. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_headroom](group__net__buf.md#gac9a09897f44e708f920064826aa2f703) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Check buffer headroom. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_buf\_max\_len](group__net__buf.md#ga65924b8234c91dfc09069ba06242a6b7) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Check maximum [net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38 "Length of the data behind the data pointer.") value. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [net\_buf\_tail](group__net__buf.md#gaedb10a84b352a3d7716bef979af2ab31) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Get the tail pointer for a buffer. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_frag\_last](group__net__buf.md#ga042ce3f2e7e3fd0948ca2623fff36746) (struct [net\_buf](structnet__buf.md) \*frags) |
|  | Find the last fragment in the fragment list. |
| void | [net\_buf\_frag\_insert](group__net__buf.md#gac032b44db4a845dba8303fecfe1b63e7) (struct [net\_buf](structnet__buf.md) \*parent, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Insert a new fragment to a chain of bufs. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_frag\_add](group__net__buf.md#ga0d7e310802a2bc7b2078f9310827535f) (struct [net\_buf](structnet__buf.md) \*head, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Add a new fragment to the end of a chain of bufs. |
| struct [net\_buf](structnet__buf.md) \* | [net\_buf\_frag\_del](group__net__buf.md#ga602a99833bd401a0ada5bd5defa7a2ff) (struct [net\_buf](structnet__buf.md) \*parent, struct [net\_buf](structnet__buf.md) \*frag) |
|  | Delete existing fragment from a chain of bufs. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_linearize](group__net__buf.md#gaffd49f2de8e72d5f7585b4e5167923d8) (void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dst\_len, const struct [net\_buf](structnet__buf.md) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Copy bytes from [net\_buf](structnet__buf.md "Network buffer representation.") chain starting at offset to linear buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_append\_bytes](group__net__buf.md#ga646d680491753b3ed29fa83c26732d1a) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const void \*value, [k\_timeout\_t](structk__timeout__t.md) timeout, [net\_buf\_allocator\_cb](group__net__buf.md#ga9b74d094a45daf74cd230eaa4fcbc065) allocate\_cb, void \*user\_data) |
|  | Append data to a list of [net\_buf](structnet__buf.md "Network buffer representation."). |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_data\_match](group__net__buf.md#gaef938c3ab676a5bd5bf8338b8d7cb30c) (const struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Match data with a [net\_buf](structnet__buf.md "Network buffer representation.")'s content. |
| static struct [net\_buf](structnet__buf.md) \* | [net\_buf\_skip](group__net__buf.md#ga2d7096280d4fa6f5e32c4674d542889b) (struct [net\_buf](structnet__buf.md) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Skip N number of bytes in a [net\_buf](structnet__buf.md "Network buffer representation."). |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [net\_buf\_frags\_len](group__net__buf.md#gaebb95f08dbd4d38a250170aa78ddeb44) (const struct [net\_buf](structnet__buf.md) \*buf) |
|  | Calculate amount of bytes stored in fragments. |

## Detailed Description

Buffer management.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net\_buf.h](net__buf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
