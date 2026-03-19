---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/x86_2intel64_2exception_8h_source.html
original_path: doxygen/html/x86_2intel64_2exception_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exception.h

[Go to the documentation of this file.](x86_2intel64_2exception_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corp.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_EXPCEPTION\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_EXPCEPTION\_H\_

8

9#ifndef \_ASMLANGUAGE

10#include <[zephyr/arch/x86/intel64/thread.h](arch_2x86_2intel64_2thread_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

16/\*

17 \* the exception stack frame

18 \*/

19

20struct [arch\_esf](structarch__esf.md) {

21#ifdef CONFIG\_EXCEPTION\_DEBUG

22 /\* callee-saved \*/

23 unsigned long rbx;

24 unsigned long [r12](structarch__esf.md#ab946ef0b8ded450d16c72ef0733e5229);

25 unsigned long [r13](structarch__esf.md#a252de1dd78f9ea00aeae7c8cbe7280ef);

26 unsigned long [r14](structarch__esf.md#af1b616f3b2c30abcdf83f0e1956e8fca);

27 unsigned long [r15](structarch__esf.md#a897e6a5360058ae85ae12a074083f18a);

28#endif /\* CONFIG\_EXCEPTION\_DEBUG \*/

[ 29](structarch__esf.md#ac1bbb2fd72747cf2ea9bd7cc8eed27a1) unsigned long [rbp](structarch__esf.md#ac1bbb2fd72747cf2ea9bd7cc8eed27a1);

30

31 /\* Caller-saved regs \*/

[ 32](structarch__esf.md#ab974edf6b86dd1581d6bc64d5cdc7354) unsigned long [rax](structarch__esf.md#ab974edf6b86dd1581d6bc64d5cdc7354);

[ 33](structarch__esf.md#af38fea881164e3eff76e817ba4ebe29d) unsigned long [rcx](structarch__esf.md#af38fea881164e3eff76e817ba4ebe29d);

[ 34](structarch__esf.md#a91e33c2d6f590b16f5ceadbcb7376050) unsigned long [rdx](structarch__esf.md#a91e33c2d6f590b16f5ceadbcb7376050);

[ 35](structarch__esf.md#a9c41a02d0cba8682e066f795917c89b8) unsigned long [rsi](structarch__esf.md#a9c41a02d0cba8682e066f795917c89b8);

[ 36](structarch__esf.md#ab2c8bd5415a3f97db6b6f408d422f241) unsigned long [rdi](structarch__esf.md#ab2c8bd5415a3f97db6b6f408d422f241);

[ 37](structarch__esf.md#ad0dd8c99a9ce48010e9e08d7e383b7d2) unsigned long [r8](structarch__esf.md#a3db521d02db9c611954ea76718e3ee99);

[ 38](structarch__esf.md#acf7d3578d1b0344973a8523d50dbc8fe) unsigned long [r9](structarch__esf.md#a9887069365ebcd852ab8d78c19854927);

[ 39](structarch__esf.md#ae7cb9f1cc93e72f962065db1dbb2f5ed) unsigned long [r10](structarch__esf.md#a44ea57b6f2ae62b30809394843076290);

40 /\* Must be aligned 16 bytes from the end of this struct due to

41 \* requirements of 'fxsave (%rsp)'

42 \*/

[ 43](structarch__esf.md#af27c45a02ae939f203f260e21c5efdb5) char [fxsave](structarch__esf.md#af27c45a02ae939f203f260e21c5efdb5)[[X86\_FXSAVE\_SIZE](arch_2x86_2intel64_2thread_8h.md#ace21a6c2662fc989b5a51a2ebb53d129)];

[ 44](structarch__esf.md#a924e670be0130045943471415b674374) unsigned long [r11](structarch__esf.md#a2f561242c8a2415ec7de7848ee946677);

45

46 /\* Pushed by CPU or assembly stub \*/

[ 47](structarch__esf.md#a70ca625eb2771d9abc1de78184fbdf25) unsigned long [vector](structarch__esf.md#a70ca625eb2771d9abc1de78184fbdf25);

[ 48](structarch__esf.md#a18518c240b772ead3b8a28a033ec3ae4) unsigned long [code](structarch__esf.md#a18518c240b772ead3b8a28a033ec3ae4);

[ 49](structarch__esf.md#a6a21373c121cd99b781d68e86fde8331) unsigned long [rip](structarch__esf.md#a6a21373c121cd99b781d68e86fde8331);

[ 50](structarch__esf.md#a935e9363a31d9b3bc2f68bcd6504e977) unsigned long [cs](structarch__esf.md#ad8b1433dc80019463acefab616d74782);

[ 51](structarch__esf.md#a9c69a89af9fd87b41bec751bfc8e35d8) unsigned long [rflags](structarch__esf.md#a9c69a89af9fd87b41bec751bfc8e35d8);

[ 52](structarch__esf.md#a3e343e90ea93e32ce86a1c53e68c420a) unsigned long [rsp](structarch__esf.md#a3e343e90ea93e32ce86a1c53e68c420a);

[ 53](structarch__esf.md#ab38d5d4230fb79c87259a72b0f18ee50) unsigned long [ss](structarch__esf.md#a25aae07c91f6946596f92f0069d6729a);

54};

55

[ 56](structx86__ssf.md)struct [x86\_ssf](structx86__ssf.md) {

[ 57](structx86__ssf.md#ab184936f5e61bd1d131930343999e7e1) unsigned long [rip](structx86__ssf.md#ab184936f5e61bd1d131930343999e7e1);

[ 58](structx86__ssf.md#a437b96d8a4918fac172debb55d2c4767) unsigned long [rflags](structx86__ssf.md#a437b96d8a4918fac172debb55d2c4767);

[ 59](structx86__ssf.md#a284dbdfac8e9d81b4a076b631f9267ec) unsigned long [r10](structx86__ssf.md#a284dbdfac8e9d81b4a076b631f9267ec);

[ 60](structx86__ssf.md#a2512b589af2b9c0f0dfbb908428ff21b) unsigned long [r9](structx86__ssf.md#a2512b589af2b9c0f0dfbb908428ff21b);

[ 61](structx86__ssf.md#a0f9f74e4f2790197819babea4c9c5e7e) unsigned long [r8](structx86__ssf.md#a0f9f74e4f2790197819babea4c9c5e7e);

[ 62](structx86__ssf.md#a29bf7a38c8fc2347a2930a71d1b724ec) unsigned long [rdx](structx86__ssf.md#a29bf7a38c8fc2347a2930a71d1b724ec);

[ 63](structx86__ssf.md#adec257b785157623eb9932bb3ff62932) unsigned long [rsi](structx86__ssf.md#adec257b785157623eb9932bb3ff62932);

[ 64](structx86__ssf.md#a50e764f5066662238d2b3b117d199db2) char [fxsave](structx86__ssf.md#a50e764f5066662238d2b3b117d199db2)[[X86\_FXSAVE\_SIZE](arch_2x86_2intel64_2thread_8h.md#ace21a6c2662fc989b5a51a2ebb53d129)];

[ 65](structx86__ssf.md#a9afd12452d8f44c1c4b391bc77afbaec) unsigned long [rdi](structx86__ssf.md#a9afd12452d8f44c1c4b391bc77afbaec);

[ 66](structx86__ssf.md#a080aae764546e381f6455abf18fb6853) unsigned long [rsp](structx86__ssf.md#a080aae764546e381f6455abf18fb6853);

67};

68

69#ifdef \_\_cplusplus

70}

71#endif

72

73#endif /\* \_ASMLANGUAGE \*/

74

75#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_EXPCEPTION\_H\_ \*/

[thread.h](arch_2x86_2intel64_2thread_8h.md)

[X86\_FXSAVE\_SIZE](arch_2x86_2intel64_2thread_8h.md#ace21a6c2662fc989b5a51a2ebb53d129)

#define X86\_FXSAVE\_SIZE

**Definition** thread.h:37

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[arch\_esf::code](structarch__esf.md#a18518c240b772ead3b8a28a033ec3ae4)

unsigned long code

**Definition** exception.h:48

[arch\_esf::r13](structarch__esf.md#a252de1dd78f9ea00aeae7c8cbe7280ef)

uint32\_t r13

**Definition** exception.h:31

[arch\_esf::ss](structarch__esf.md#a25aae07c91f6946596f92f0069d6729a)

unsigned int ss

**Definition** exception.h:32

[arch\_esf::r11](structarch__esf.md#a2f561242c8a2415ec7de7848ee946677)

uint32\_t r11

**Definition** exception.h:29

[arch\_esf::r8](structarch__esf.md#a3db521d02db9c611954ea76718e3ee99)

uint32\_t r8

**Definition** exception.h:26

[arch\_esf::rsp](structarch__esf.md#a3e343e90ea93e32ce86a1c53e68c420a)

unsigned long rsp

**Definition** exception.h:52

[arch\_esf::r10](structarch__esf.md#a44ea57b6f2ae62b30809394843076290)

uint32\_t r10

**Definition** exception.h:28

[arch\_esf::rip](structarch__esf.md#a6a21373c121cd99b781d68e86fde8331)

unsigned long rip

**Definition** exception.h:49

[arch\_esf::vector](structarch__esf.md#a70ca625eb2771d9abc1de78184fbdf25)

unsigned long vector

**Definition** exception.h:47

[arch\_esf::r15](structarch__esf.md#a897e6a5360058ae85ae12a074083f18a)

uint32\_t r15

**Definition** exception.h:33

[arch\_esf::rdx](structarch__esf.md#a91e33c2d6f590b16f5ceadbcb7376050)

unsigned long rdx

**Definition** exception.h:34

[arch\_esf::r9](structarch__esf.md#a9887069365ebcd852ab8d78c19854927)

uint32\_t r9

**Definition** exception.h:27

[arch\_esf::rsi](structarch__esf.md#a9c41a02d0cba8682e066f795917c89b8)

unsigned long rsi

**Definition** exception.h:35

[arch\_esf::rflags](structarch__esf.md#a9c69a89af9fd87b41bec751bfc8e35d8)

unsigned long rflags

**Definition** exception.h:51

[arch\_esf::rdi](structarch__esf.md#ab2c8bd5415a3f97db6b6f408d422f241)

unsigned long rdi

**Definition** exception.h:36

[arch\_esf::r12](structarch__esf.md#ab946ef0b8ded450d16c72ef0733e5229)

uint32\_t r12

**Definition** exception.h:30

[arch\_esf::rax](structarch__esf.md#ab974edf6b86dd1581d6bc64d5cdc7354)

unsigned long rax

**Definition** exception.h:32

[arch\_esf::rbp](structarch__esf.md#ac1bbb2fd72747cf2ea9bd7cc8eed27a1)

unsigned long rbp

**Definition** exception.h:29

[arch\_esf::cs](structarch__esf.md#ad8b1433dc80019463acefab616d74782)

unsigned int cs

**Definition** exception.h:48

[arch\_esf::r14](structarch__esf.md#af1b616f3b2c30abcdf83f0e1956e8fca)

uint32\_t r14

**Definition** exception.h:32

[arch\_esf::fxsave](structarch__esf.md#af27c45a02ae939f203f260e21c5efdb5)

char fxsave[X86\_FXSAVE\_SIZE]

**Definition** exception.h:43

[arch\_esf::rcx](structarch__esf.md#af38fea881164e3eff76e817ba4ebe29d)

unsigned long rcx

**Definition** exception.h:33

[x86\_ssf](structx86__ssf.md)

**Definition** exception.h:56

[x86\_ssf::rsp](structx86__ssf.md#a080aae764546e381f6455abf18fb6853)

unsigned long rsp

**Definition** exception.h:66

[x86\_ssf::r8](structx86__ssf.md#a0f9f74e4f2790197819babea4c9c5e7e)

unsigned long r8

**Definition** exception.h:61

[x86\_ssf::r9](structx86__ssf.md#a2512b589af2b9c0f0dfbb908428ff21b)

unsigned long r9

**Definition** exception.h:60

[x86\_ssf::r10](structx86__ssf.md#a284dbdfac8e9d81b4a076b631f9267ec)

unsigned long r10

**Definition** exception.h:59

[x86\_ssf::rdx](structx86__ssf.md#a29bf7a38c8fc2347a2930a71d1b724ec)

unsigned long rdx

**Definition** exception.h:62

[x86\_ssf::rflags](structx86__ssf.md#a437b96d8a4918fac172debb55d2c4767)

unsigned long rflags

**Definition** exception.h:58

[x86\_ssf::fxsave](structx86__ssf.md#a50e764f5066662238d2b3b117d199db2)

char fxsave[X86\_FXSAVE\_SIZE]

**Definition** exception.h:64

[x86\_ssf::rdi](structx86__ssf.md#a9afd12452d8f44c1c4b391bc77afbaec)

unsigned long rdi

**Definition** exception.h:65

[x86\_ssf::rip](structx86__ssf.md#ab184936f5e61bd1d131930343999e7e1)

unsigned long rip

**Definition** exception.h:57

[x86\_ssf::rsi](structx86__ssf.md#adec257b785157623eb9932bb3ff62932)

unsigned long rsi

**Definition** exception.h:63

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [intel64](dir_1abf87bed33eaf4508c3178cbd4d6168.md)
- [exception.h](x86_2intel64_2exception_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
