---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structarch__esf.html
original_path: doxygen/html/structarch__esf.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch\_esf Struct Reference

Exception Stack Frame.
[More...](#details)

`#include <[exception.h](arm_2cortex__a__r_2exception_8h_source.md)>`

| Data Structures | |
| --- | --- |
| struct | [\_\_basic\_sf](structarch__esf_1_1____basic__sf.md) |

| Data Fields | |
| --- | --- |
| struct \_\_fpu\_sf | [fpu](#a89304485b8d99aa30facbddf22465170) |
| struct [arch\_esf::\_\_basic\_sf](structarch__esf_1_1____basic__sf.md) | [basic](#a0b4a5972bfeab496a9a0cf0ab7821d63) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x0](#a2eac86aa1bfe72c5382555ac7c4da87a) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x1](#a0306fa0bf609c4b555c94e7c0b261389) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x2](#a7673457760d24a5d3559642ac89fc815) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x3](#a6b194085ef2a4649361f86c78070061a) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x4](#a69fe42719d302c62ba05c08c8548451a) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x5](#a565c8f1b98b8bb4920ed54447559bbe7) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x6](#af3b381fa07e8cc809422f759e03e526b) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x7](#a8c7d66e7eb8a30e76c588ac07c242446) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x8](#ad38f2f48dedc67706db4a78a6c16a74a) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x9](#af84d11e6ca50633cd6a1449df29f9853) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x10](#aeeb737c86d1e14ebe89d908586b21213) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x11](#a041472053798550ecc0ed1641aad0a36) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x12](#afe82dc7299245360c215d874ab6e4fc5) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x13](#aa7a17c78c884e3e76ac20efce28cc07b) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x14](#a6d1deb8481db2cb4b16a4227eeb7156b) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x15](#a9e244148142ac2ddced13d6f4adad723) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x16](#ad14eaf73e5ef14e5e47bed09ddd8fae8) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x17](#aa8e0bd15d3fae88ef7afa2e122b23287) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [x18](#a29dbefef813eba8c1cb9e8d97ddff060) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [lr](#ad9047b114956222cd07503fe9339b43d) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [spsr](#ae587b84ee192f1b4f3bc3649b9358931) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [elr](#a28e161a6b7203eb0abe91c1970a9bd89) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [ra](#a22241917474aaf5718780c55c65be33f) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [gp](#a0256d0bf331458b345ea25e1862e1bf1) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [t0](#a3669d6b58ca5da0dd89a904186ad74ba) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [t1](#ae96b6de3f7fe95b12a5590b68cfca40e) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [t2](#aba3b4051cbac23bbadfaa262b83de953) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [t3](#af280445d5be52877f9a7d48787bd5604) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [t4](#a81163becab1b4d7c244f0b5af3accae9) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [t5](#ad01a8b2c465aead38705b0b6cbb4af96) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [t6](#a7247ee9003b3c26a6bab8c82ab61786b) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [t7](#a8e98b1d9dffeb236db5f4df952842b78) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [t8](#a41e3b393531a98223054e525bd18237e) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [t9](#a91f025811139eb2ed9f9d6f3a1ee482f) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a0](#a0186f8ac5c6949fea58d1da9061fa419) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a1](#a62a1feb37b8724ada83d70caae38a673) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a2](#adc1040e4224662f77875db24635ceb84) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a3](#a3f2e9029daddabeefd2b2c253efd6c83) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [v0](#ac2e9705feb9d23a650939cb42efb0ed7) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [v1](#a53bcb9b20c29225952fa15ed94fc56ff) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [at](#a84c6de4138983cb180f6d8f1faa30e3b) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [epc](#a2c97b72603f596d88e2b01367a230a4c) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [badvaddr](#a1094f36597a23bf73c6574b4457049c5) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [hi](#af249e64a0c2755e2bdab36cc5af721e1) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [lo](#a5c608ad064989abef5fb69fcd422d617) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [status](#abe2ac128675534aa53d4434b32e39fb4) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [cause](#aa0f0105b2ae3986c3b8f1f8927064568) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ra](#af925780dd5a600bcc9741aa588ae3c32) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r1](#a74f77230b78880d1aca123886d7786af) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r2](#a53a4e45913aba2541648c0be71f53e67) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r3](#a613182d7fc3c3ed0f5680fa382eee82b) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r4](#a247b2b132e00b25c58770323da69e5f1) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r5](#accb4010250c2c4abedb4b7877878915e) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r6](#a47c73f90f7d944cd1c8463c7dd4a5fcf) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r7](#a8e1a7067a6c8046ba7d190812582441a) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r8](#a3db521d02db9c611954ea76718e3ee99) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r9](#a9887069365ebcd852ab8d78c19854927) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r10](#a44ea57b6f2ae62b30809394843076290) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r11](#a2f561242c8a2415ec7de7848ee946677) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r12](#ab946ef0b8ded450d16c72ef0733e5229) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r13](#a252de1dd78f9ea00aeae7c8cbe7280ef) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r14](#af1b616f3b2c30abcdf83f0e1956e8fca) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [r15](#a897e6a5360058ae85ae12a074083f18a) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [estatus](#abe51f26556e845597e495628ed653ca0) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [instr](#ac79618cfb2d8d57f995b29ef81ff7f60) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dummy](#ae44a189aed30d7bd9cbb860f7c177d4d) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a4](#a2a794aaedfc9c499f5f98a0bb62936ad) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a5](#abab1419a6c1fd7b294f997f0e58bcc45) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a6](#a463bd3c45ff943e618c9dd628918b520) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a7](#a7fcc14965783e368cd0f3ecc33517147) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [mepc](#a62c66377b82031f09d6e1ec6591b3b86) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [mstatus](#a6e1afae6a77e6eb0624aa982a07813c3) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [s0](#a8138142006da6c5abd397faac0379cfa) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [sp](#a9c3e060a48caeb59d2625e921f1f6d15) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [out](#a25d416d377e446b577945a71ff0cd02a) [8] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [global](#a29a4fe6ed5b2f8c892f0378be0babd78) [8] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [psr](#ae0487ae046fbd1544bd04bf8fab1a300) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pc](#a5547d9c022e6c4a6492df49f11f21493) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [npc](#a0d5ee2c404dc3322ae7c0350d5d6e02f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [wim](#abcb68c0ffad3c9d44c353b7d6cdb1a50) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tbr](#a07426991d80b58a64b1fed1d00c88e8f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [y](#aacb0e92d3b12a154085994040402103e) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ss](#a25aae07c91f6946596f92f0069d6729a) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [gs](#a353cd21036946b829a01ab9e247bf72d) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [fs](#a1f127199573607f22a4c0e95d3b5ce74) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [es](#aac9b040d864214b71afb15e618a300da) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ds](#adbdb731abf4be35509eec853ecddc601) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [esp](#a6c501100e54db4c1e4685090b0785889) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ebp](#aa66aa75f640c3f5c1455b3c185fa92a0) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ebx](#a7dee4cd6c1c3fe496754c1e9c37d6e5e) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [esi](#a260832877afcad7ae2be72244a6c30a4) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [edi](#a7247267fa4d4771bc389bef8ba38e820) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [edx](#ace05744212c1665a672b2ced419f9bfc) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [eax](#a56d08dbd84879425ec2e905c03929048) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ecx](#a899ead638078796464d40e4f67702df8) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [errorCode](#a7f8bfa097d38019069d787f15fa535dc) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [eip](#a9053fc737ec314b9c97095e0267a92f7) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [cs](#ad8b1433dc80019463acefab616d74782) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [eflags](#ac64b0d4af1e920f75c7c844725a84c7c) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [rbp](#ac1bbb2fd72747cf2ea9bd7cc8eed27a1) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [rax](#ab974edf6b86dd1581d6bc64d5cdc7354) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [rcx](#af38fea881164e3eff76e817ba4ebe29d) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [rdx](#a91e33c2d6f590b16f5ceadbcb7376050) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [rsi](#a9c41a02d0cba8682e066f795917c89b8) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [rdi](#ab2c8bd5415a3f97db6b6f408d422f241) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [r8](#ad0dd8c99a9ce48010e9e08d7e383b7d2) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [r9](#acf7d3578d1b0344973a8523d50dbc8fe) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [r10](#ae7cb9f1cc93e72f962065db1dbb2f5ed) |
| char | [fxsave](#af27c45a02ae939f203f260e21c5efdb5) [[X86\_FXSAVE\_SIZE](arch_2x86_2intel64_2thread_8h.md#ace21a6c2662fc989b5a51a2ebb53d129)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [r11](#a924e670be0130045943471415b674374) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [vector](#a70ca625eb2771d9abc1de78184fbdf25) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [code](#a18518c240b772ead3b8a28a033ec3ae4) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [rip](#a6a21373c121cd99b781d68e86fde8331) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [cs](#a935e9363a31d9b3bc2f68bcd6504e977) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [rflags](#a9c69a89af9fd87b41bec751bfc8e35d8) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [rsp](#a3e343e90ea93e32ce86a1c53e68c420a) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [ss](#ab38d5d4230fb79c87259a72b0f18ee50) |
| int | [dummy](#a8b96563526cec43c5b37bdacd3e3e065) |

## Detailed Description

Exception Stack Frame.

A pointer to an "exception stack frame" (ESF) is passed as an argument to exception handlers registered via nanoCpuExcConnect(). As the system always operates at ring 0, only the EIP, CS and EFLAGS registers are pushed onto the stack when an exception occurs.

The exception stack frame includes the volatile registers (EAX, ECX, and EDX) as well as the 5 non-volatile registers (EDI, ESI, EBX, EBP and ESP). Those registers are pushed onto the stack by \_ExcEnt().

## Field Documentation

## [◆ ](#a0186f8ac5c6949fea58d1da9061fa419)a0

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::a0 |
| --- |

## [◆ ](#a62a1feb37b8724ada83d70caae38a673)a1

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::a1 |
| --- |

## [◆ ](#adc1040e4224662f77875db24635ceb84)a2

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::a2 |
| --- |

## [◆ ](#a3f2e9029daddabeefd2b2c253efd6c83)a3

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::a3 |
| --- |

## [◆ ](#a2a794aaedfc9c499f5f98a0bb62936ad)a4

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::a4 |
| --- |

## [◆ ](#abab1419a6c1fd7b294f997f0e58bcc45)a5

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::a5 |
| --- |

## [◆ ](#a463bd3c45ff943e618c9dd628918b520)a6

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::a6 |
| --- |

## [◆ ](#a7fcc14965783e368cd0f3ecc33517147)a7

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::a7 |
| --- |

## [◆ ](#a84c6de4138983cb180f6d8f1faa30e3b)at

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::at |
| --- |

## [◆ ](#a1094f36597a23bf73c6574b4457049c5)badvaddr

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::badvaddr |
| --- |

## [◆ ](#a0b4a5972bfeab496a9a0cf0ab7821d63)basic

| struct [arch\_esf::\_\_basic\_sf](structarch__esf_1_1____basic__sf.md) arch\_esf::basic |
| --- |

## [◆ ](#aa0f0105b2ae3986c3b8f1f8927064568)cause

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::cause |
| --- |

## [◆ ](#a18518c240b772ead3b8a28a033ec3ae4)code

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::code |
| --- |

## [◆ ](#ad8b1433dc80019463acefab616d74782)cs [1/2]

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::cs |
| --- |

## [◆ ](#a935e9363a31d9b3bc2f68bcd6504e977)cs [2/2]

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::cs |
| --- |

## [◆ ](#adbdb731abf4be35509eec853ecddc601)ds

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::ds |
| --- |

## [◆ ](#ae44a189aed30d7bd9cbb860f7c177d4d)dummy [1/2]

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::dummy |
| --- |

## [◆ ](#a8b96563526cec43c5b37bdacd3e3e065)dummy [2/2]

| int arch\_esf::dummy |
| --- |

## [◆ ](#a56d08dbd84879425ec2e905c03929048)eax

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::eax |
| --- |

## [◆ ](#aa66aa75f640c3f5c1455b3c185fa92a0)ebp

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::ebp |
| --- |

## [◆ ](#a7dee4cd6c1c3fe496754c1e9c37d6e5e)ebx

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::ebx |
| --- |

## [◆ ](#a899ead638078796464d40e4f67702df8)ecx

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::ecx |
| --- |

## [◆ ](#a7247267fa4d4771bc389bef8ba38e820)edi

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::edi |
| --- |

## [◆ ](#ace05744212c1665a672b2ced419f9bfc)edx

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::edx |
| --- |

## [◆ ](#ac64b0d4af1e920f75c7c844725a84c7c)eflags

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::eflags |
| --- |

## [◆ ](#a9053fc737ec314b9c97095e0267a92f7)eip

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::eip |
| --- |

## [◆ ](#a28e161a6b7203eb0abe91c1970a9bd89)elr

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::elr |
| --- |

## [◆ ](#a2c97b72603f596d88e2b01367a230a4c)epc

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::epc |
| --- |

## [◆ ](#a7f8bfa097d38019069d787f15fa535dc)errorCode

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::errorCode |
| --- |

## [◆ ](#aac9b040d864214b71afb15e618a300da)es

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::es |
| --- |

## [◆ ](#a260832877afcad7ae2be72244a6c30a4)esi

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::esi |
| --- |

## [◆ ](#a6c501100e54db4c1e4685090b0785889)esp

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::esp |
| --- |

## [◆ ](#abe51f26556e845597e495628ed653ca0)estatus

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::estatus |
| --- |

## [◆ ](#a89304485b8d99aa30facbddf22465170)fpu

| struct \_\_fpu\_sf arch\_esf::fpu |
| --- |

## [◆ ](#a1f127199573607f22a4c0e95d3b5ce74)fs

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::fs |
| --- |

## [◆ ](#af27c45a02ae939f203f260e21c5efdb5)fxsave

| char arch\_esf::fxsave[[X86\_FXSAVE\_SIZE](arch_2x86_2intel64_2thread_8h.md#ace21a6c2662fc989b5a51a2ebb53d129)] |
| --- |

## [◆ ](#a29a4fe6ed5b2f8c892f0378be0babd78)global

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::global[8] |
| --- |

## [◆ ](#a0256d0bf331458b345ea25e1862e1bf1)gp

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::gp |
| --- |

## [◆ ](#a353cd21036946b829a01ab9e247bf72d)gs

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::gs |
| --- |

## [◆ ](#af249e64a0c2755e2bdab36cc5af721e1)hi

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::hi |
| --- |

## [◆ ](#ac79618cfb2d8d57f995b29ef81ff7f60)instr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::instr |
| --- |

## [◆ ](#a5c608ad064989abef5fb69fcd422d617)lo

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::lo |
| --- |

## [◆ ](#ad9047b114956222cd07503fe9339b43d)lr

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::lr |
| --- |

## [◆ ](#a62c66377b82031f09d6e1ec6591b3b86)mepc

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::mepc |
| --- |

## [◆ ](#a6e1afae6a77e6eb0624aa982a07813c3)mstatus

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::mstatus |
| --- |

## [◆ ](#a0d5ee2c404dc3322ae7c0350d5d6e02f)npc

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::npc |
| --- |

## [◆ ](#a25d416d377e446b577945a71ff0cd02a)out

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::out[8] |
| --- |

## [◆ ](#a5547d9c022e6c4a6492df49f11f21493)pc

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::pc |
| --- |

## [◆ ](#ae0487ae046fbd1544bd04bf8fab1a300)psr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::psr |
| --- |

## [◆ ](#a74f77230b78880d1aca123886d7786af)r1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r1 |
| --- |

## [◆ ](#a44ea57b6f2ae62b30809394843076290)r10 [1/2]

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r10 |
| --- |

## [◆ ](#ae7cb9f1cc93e72f962065db1dbb2f5ed)r10 [2/2]

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::r10 |
| --- |

## [◆ ](#a2f561242c8a2415ec7de7848ee946677)r11 [1/2]

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r11 |
| --- |

## [◆ ](#a924e670be0130045943471415b674374)r11 [2/2]

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::r11 |
| --- |

## [◆ ](#ab946ef0b8ded450d16c72ef0733e5229)r12

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r12 |
| --- |

## [◆ ](#a252de1dd78f9ea00aeae7c8cbe7280ef)r13

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r13 |
| --- |

## [◆ ](#af1b616f3b2c30abcdf83f0e1956e8fca)r14

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r14 |
| --- |

## [◆ ](#a897e6a5360058ae85ae12a074083f18a)r15

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r15 |
| --- |

## [◆ ](#a53a4e45913aba2541648c0be71f53e67)r2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r2 |
| --- |

## [◆ ](#a613182d7fc3c3ed0f5680fa382eee82b)r3

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r3 |
| --- |

## [◆ ](#a247b2b132e00b25c58770323da69e5f1)r4

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r4 |
| --- |

## [◆ ](#accb4010250c2c4abedb4b7877878915e)r5

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r5 |
| --- |

## [◆ ](#a47c73f90f7d944cd1c8463c7dd4a5fcf)r6

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r6 |
| --- |

## [◆ ](#a8e1a7067a6c8046ba7d190812582441a)r7

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r7 |
| --- |

## [◆ ](#a3db521d02db9c611954ea76718e3ee99)r8 [1/2]

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r8 |
| --- |

## [◆ ](#ad0dd8c99a9ce48010e9e08d7e383b7d2)r8 [2/2]

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::r8 |
| --- |

## [◆ ](#a9887069365ebcd852ab8d78c19854927)r9 [1/2]

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::r9 |
| --- |

## [◆ ](#acf7d3578d1b0344973a8523d50dbc8fe)r9 [2/2]

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::r9 |
| --- |

## [◆ ](#a22241917474aaf5718780c55c65be33f)ra [1/2]

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::ra |
| --- |

## [◆ ](#af925780dd5a600bcc9741aa588ae3c32)ra [2/2]

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::ra |
| --- |

## [◆ ](#ab974edf6b86dd1581d6bc64d5cdc7354)rax

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::rax |
| --- |

## [◆ ](#ac1bbb2fd72747cf2ea9bd7cc8eed27a1)rbp

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::rbp |
| --- |

## [◆ ](#af38fea881164e3eff76e817ba4ebe29d)rcx

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::rcx |
| --- |

## [◆ ](#ab2c8bd5415a3f97db6b6f408d422f241)rdi

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::rdi |
| --- |

## [◆ ](#a91e33c2d6f590b16f5ceadbcb7376050)rdx

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::rdx |
| --- |

## [◆ ](#a9c69a89af9fd87b41bec751bfc8e35d8)rflags

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::rflags |
| --- |

## [◆ ](#a6a21373c121cd99b781d68e86fde8331)rip

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::rip |
| --- |

## [◆ ](#a9c41a02d0cba8682e066f795917c89b8)rsi

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::rsi |
| --- |

## [◆ ](#a3e343e90ea93e32ce86a1c53e68c420a)rsp

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::rsp |
| --- |

## [◆ ](#a8138142006da6c5abd397faac0379cfa)s0

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::s0 |
| --- |

## [◆ ](#a9c3e060a48caeb59d2625e921f1f6d15)sp

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::sp |
| --- |

## [◆ ](#ae587b84ee192f1b4f3bc3649b9358931)spsr

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::spsr |
| --- |

## [◆ ](#a25aae07c91f6946596f92f0069d6729a)ss [1/2]

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arch\_esf::ss |
| --- |

## [◆ ](#ab38d5d4230fb79c87259a72b0f18ee50)ss [2/2]

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::ss |
| --- |

## [◆ ](#abe2ac128675534aa53d4434b32e39fb4)status

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::status |
| --- |

## [◆ ](#a3669d6b58ca5da0dd89a904186ad74ba)t0

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::t0 |
| --- |

## [◆ ](#ae96b6de3f7fe95b12a5590b68cfca40e)t1

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::t1 |
| --- |

## [◆ ](#aba3b4051cbac23bbadfaa262b83de953)t2

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::t2 |
| --- |

## [◆ ](#af280445d5be52877f9a7d48787bd5604)t3

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::t3 |
| --- |

## [◆ ](#a81163becab1b4d7c244f0b5af3accae9)t4

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::t4 |
| --- |

## [◆ ](#ad01a8b2c465aead38705b0b6cbb4af96)t5

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::t5 |
| --- |

## [◆ ](#a7247ee9003b3c26a6bab8c82ab61786b)t6

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::t6 |
| --- |

## [◆ ](#a8e98b1d9dffeb236db5f4df952842b78)t7

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::t7 |
| --- |

## [◆ ](#a41e3b393531a98223054e525bd18237e)t8

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::t8 |
| --- |

## [◆ ](#a91f025811139eb2ed9f9d6f3a1ee482f)t9

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::t9 |
| --- |

## [◆ ](#a07426991d80b58a64b1fed1d00c88e8f)tbr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::tbr |
| --- |

## [◆ ](#ac2e9705feb9d23a650939cb42efb0ed7)v0

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::v0 |
| --- |

## [◆ ](#a53bcb9b20c29225952fa15ed94fc56ff)v1

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::v1 |
| --- |

## [◆ ](#a70ca625eb2771d9abc1de78184fbdf25)vector

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arch\_esf::vector |
| --- |

## [◆ ](#abcb68c0ffad3c9d44c353b7d6cdb1a50)wim

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::wim |
| --- |

## [◆ ](#a2eac86aa1bfe72c5382555ac7c4da87a)x0

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x0 |
| --- |

## [◆ ](#a0306fa0bf609c4b555c94e7c0b261389)x1

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x1 |
| --- |

## [◆ ](#aeeb737c86d1e14ebe89d908586b21213)x10

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x10 |
| --- |

## [◆ ](#a041472053798550ecc0ed1641aad0a36)x11

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x11 |
| --- |

## [◆ ](#afe82dc7299245360c215d874ab6e4fc5)x12

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x12 |
| --- |

## [◆ ](#aa7a17c78c884e3e76ac20efce28cc07b)x13

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x13 |
| --- |

## [◆ ](#a6d1deb8481db2cb4b16a4227eeb7156b)x14

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x14 |
| --- |

## [◆ ](#a9e244148142ac2ddced13d6f4adad723)x15

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x15 |
| --- |

## [◆ ](#ad14eaf73e5ef14e5e47bed09ddd8fae8)x16

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x16 |
| --- |

## [◆ ](#aa8e0bd15d3fae88ef7afa2e122b23287)x17

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x17 |
| --- |

## [◆ ](#a29dbefef813eba8c1cb9e8d97ddff060)x18

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x18 |
| --- |

## [◆ ](#a7673457760d24a5d3559642ac89fc815)x2

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x2 |
| --- |

## [◆ ](#a6b194085ef2a4649361f86c78070061a)x3

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x3 |
| --- |

## [◆ ](#a69fe42719d302c62ba05c08c8548451a)x4

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x4 |
| --- |

## [◆ ](#a565c8f1b98b8bb4920ed54447559bbe7)x5

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x5 |
| --- |

## [◆ ](#af3b381fa07e8cc809422f759e03e526b)x6

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x6 |
| --- |

## [◆ ](#a8c7d66e7eb8a30e76c588ac07c242446)x7

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x7 |
| --- |

## [◆ ](#ad38f2f48dedc67706db4a78a6c16a74a)x8

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x8 |
| --- |

## [◆ ](#af84d11e6ca50633cd6a1449df29f9853)x9

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_esf::x9 |
| --- |

## [◆ ](#aacb0e92d3b12a154085994040402103e)y

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_esf::y |
| --- |

---

The documentation for this struct was generated from the following files:

- zephyr/arch/arm/cortex\_a\_r/[exception.h](arm_2cortex__a__r_2exception_8h_source.md)
- zephyr/arch/arm/cortex\_m/[exception.h](arm_2cortex__m_2exception_8h_source.md)
- zephyr/arch/arm64/[exception.h](arm64_2exception_8h_source.md)
- zephyr/arch/mips/[exception.h](mips_2exception_8h_source.md)
- zephyr/arch/nios2/[exception.h](nios2_2exception_8h_source.md)
- zephyr/arch/posix/[exception.h](posix_2exception_8h_source.md)
- zephyr/arch/riscv/[exception.h](riscv_2exception_8h_source.md)
- zephyr/arch/sparc/[exception.h](sparc_2exception_8h_source.md)
- zephyr/arch/x86/ia32/[exception.h](x86_2ia32_2exception_8h_source.md)
- zephyr/arch/x86/intel64/[exception.h](x86_2intel64_2exception_8h_source.md)
- zephyr/arch/xtensa/[exception.h](xtensa_2exception_8h_source.md)

- [arch\_esf](structarch__esf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
