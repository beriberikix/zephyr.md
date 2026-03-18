---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/segmentation_8h_source.html
original_path: doxygen/html/segmentation_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

segmentation.h

[Go to the documentation of this file.](segmentation_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_SEGMENTATION\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_SEGMENTATION\_H\_

9

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11

12/\* Host gen\_idt uses this header as well, don't depend on toolchain.h \*/

13#ifndef \_\_packed

14#define \_\_packed \_\_attribute\_\_((packed))

15#endif

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21/\* NOTE: We currently do not have definitions for 16-bit segment, currently

22 \* assume everything we are working with is 32-bit

23 \*/

24

[ 25](segmentation_8h.md#a1123609025ff8c35fcebbeefc627fe40)#define SEG\_TYPE\_LDT 0x2

[ 26](segmentation_8h.md#a09b28d129d4935e1ac79010ad2ed845c)#define SEG\_TYPE\_TASK\_GATE 0x5

[ 27](segmentation_8h.md#a9526fd354b043f1d989133fb51584ca5)#define SEG\_TYPE\_TSS 0x9

[ 28](segmentation_8h.md#a358e9557d55f44b1e0c48f56e9bb8eb8)#define SEG\_TYPE\_TSS\_BUSY 0xB

[ 29](segmentation_8h.md#a06659cf84f44e085e88adf1f249ea958)#define SEG\_TYPE\_CALL\_GATE 0xC

[ 30](segmentation_8h.md#a62c20d09a1f35aadbffc000ce695aca5)#define SEG\_TYPE\_IRQ\_GATE 0xE

[ 31](segmentation_8h.md#a24ba226f5d7c4a2d0e73d129b811d009)#define SEG\_TYPE\_TRAP\_GATE 0xF

32

[ 33](segmentation_8h.md#a93b8e20c30316e0b31ce2d72ee429267)#define DT\_GRAN\_BYTE 0

[ 34](segmentation_8h.md#abd17be4fcc2b1627fdd9fce4f2616034)#define DT\_GRAN\_PAGE 1

35

[ 36](segmentation_8h.md#adb3a30ddf8c9e70de7f2f4e9532012c2)#define DT\_READABLE 1

[ 37](segmentation_8h.md#a440b0121a23eaee4a6da138464598332)#define DT\_NON\_READABLE 0

38

[ 39](segmentation_8h.md#a9fed0f1041479b83a2177ce758026e01)#define DT\_WRITABLE 1

[ 40](segmentation_8h.md#a06578eef93a325c17c431c4e30358f68)#define DT\_NON\_WRITABLE 0

41

[ 42](segmentation_8h.md#aafd044e471668a2ad5d65d375fcb037b)#define DT\_EXPAND\_DOWN 1

[ 43](segmentation_8h.md#a42725696f61f6c208aad358e0ef99521)#define DT\_EXPAND\_UP 0

44

[ 45](segmentation_8h.md#a1bf28de4d983377685927df65ada05fc)#define DT\_CONFORM 1

[ 46](segmentation_8h.md#a829d7ba32b7ff93ee11394e198412fb6)#define DT\_NONCONFORM 0

47

[ 48](segmentation_8h.md#a7e6ddc88924ea43b4d89f367cee558d4)#define DT\_TYPE\_SYSTEM 0

[ 49](segmentation_8h.md#adde93db381ef8fc598457a3cef782aa1)#define DT\_TYPE\_CODEDATA 1

50

51#ifndef \_ASMLANGUAGE

52

53/\* Section 7.2.1 of IA architecture SW developer manual, Vol 3. \*/

[ 54](structtask__state__segment.md)struct \_\_packed [task\_state\_segment](structtask__state__segment.md) {

[ 55](structtask__state__segment.md#a6dca0f6680e373545f31490cb4667a1e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [backlink](structtask__state__segment.md#a6dca0f6680e373545f31490cb4667a1e);

[ 56](structtask__state__segment.md#ace0a346f5ca56fc785d17a8cb76c3f00) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_1](structtask__state__segment.md#ace0a346f5ca56fc785d17a8cb76c3f00);

[ 57](structtask__state__segment.md#ae613a01ad49d8aaa43fb955cf95e1de1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esp0](structtask__state__segment.md#ae613a01ad49d8aaa43fb955cf95e1de1);

[ 58](structtask__state__segment.md#a74e85e53e171c23d5f29f1efe0131b0a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ss0](structtask__state__segment.md#a74e85e53e171c23d5f29f1efe0131b0a);

[ 59](structtask__state__segment.md#a93ce3a1140962ce0bb74cb6101b5d696) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_2](structtask__state__segment.md#a93ce3a1140962ce0bb74cb6101b5d696);

[ 60](structtask__state__segment.md#a9f656f69a3e9cd7d74e2e5c27a0c4d79) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esp1](structtask__state__segment.md#a9f656f69a3e9cd7d74e2e5c27a0c4d79);

[ 61](structtask__state__segment.md#a1e8cf1eb785cd0cebfab53c6b6f55922) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ss1](structtask__state__segment.md#a1e8cf1eb785cd0cebfab53c6b6f55922);

[ 62](structtask__state__segment.md#a6790bfb30732ab246b20827fd5d26834) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_3](structtask__state__segment.md#a6790bfb30732ab246b20827fd5d26834);

[ 63](structtask__state__segment.md#a1cb20df4a49a73a2d0b88a8df19621c2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esp2](structtask__state__segment.md#a1cb20df4a49a73a2d0b88a8df19621c2);

[ 64](structtask__state__segment.md#ac8b023be5e2cd2d50ec55d15f7510c15) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ss2](structtask__state__segment.md#ac8b023be5e2cd2d50ec55d15f7510c15);

[ 65](structtask__state__segment.md#a354f74ae39ffff533dfe18693fc813d4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_4](structtask__state__segment.md#a354f74ae39ffff533dfe18693fc813d4);

[ 66](structtask__state__segment.md#a3de57a3414f018da7b074a8c0b38ee98) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cr3](structtask__state__segment.md#a3de57a3414f018da7b074a8c0b38ee98);

[ 67](structtask__state__segment.md#aa1992e03e583070d318adb554f28b8e8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [eip](structtask__state__segment.md#aa1992e03e583070d318adb554f28b8e8);

[ 68](structtask__state__segment.md#ab5e6713aa56576ebf4b4f15bff800993) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [eflags](structtask__state__segment.md#ab5e6713aa56576ebf4b4f15bff800993);

[ 69](structtask__state__segment.md#aca6436062f7e47e63b364aa331498a9c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [eax](structtask__state__segment.md#aca6436062f7e47e63b364aa331498a9c);

[ 70](structtask__state__segment.md#a3bd54264357890c87cfc6ebf12ffa8eb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ecx](structtask__state__segment.md#a3bd54264357890c87cfc6ebf12ffa8eb);

[ 71](structtask__state__segment.md#a36275826a694fb98a7e3d68253991eb3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [edx](structtask__state__segment.md#a36275826a694fb98a7e3d68253991eb3);

[ 72](structtask__state__segment.md#a80e9653cc996ae57e33e263773493058) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ebx](structtask__state__segment.md#a80e9653cc996ae57e33e263773493058);

[ 73](structtask__state__segment.md#af439750f77fd6067776fd24c13443fde) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esp](structtask__state__segment.md#af439750f77fd6067776fd24c13443fde);

[ 74](structtask__state__segment.md#a1b9505b29bba1d91c92457f898e29175) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ebp](structtask__state__segment.md#a1b9505b29bba1d91c92457f898e29175);

[ 75](structtask__state__segment.md#a23f6ba3c3c80d83eabb3e4981a684f86) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esi](structtask__state__segment.md#a23f6ba3c3c80d83eabb3e4981a684f86);

[ 76](structtask__state__segment.md#a305dc05c6ce45b06d5c08886fbc629d2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [edi](structtask__state__segment.md#a305dc05c6ce45b06d5c08886fbc629d2);

[ 77](structtask__state__segment.md#a6fa263ba438e73c765619549082a9c6b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [es](structtask__state__segment.md#a6fa263ba438e73c765619549082a9c6b);

[ 78](structtask__state__segment.md#acae3c67be6cf9f776db8dbe60a13e192) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_5](structtask__state__segment.md#acae3c67be6cf9f776db8dbe60a13e192);

[ 79](structtask__state__segment.md#a14fc9b3472e8ba0b02e1a74576d83ded) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cs](structtask__state__segment.md#a14fc9b3472e8ba0b02e1a74576d83ded);

[ 80](structtask__state__segment.md#ad1a611412a5057e35d8c7fd88cb502fa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_6](structtask__state__segment.md#ad1a611412a5057e35d8c7fd88cb502fa);

[ 81](structtask__state__segment.md#a007494cfabe3da5e7ae4fc17a57cb33d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ss](structtask__state__segment.md#a007494cfabe3da5e7ae4fc17a57cb33d);

[ 82](structtask__state__segment.md#ade71f2bdd6c3866243823ccf4dfc92ef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_7](structtask__state__segment.md#ade71f2bdd6c3866243823ccf4dfc92ef);

[ 83](structtask__state__segment.md#ac04302ea0ad115bbc792ae40396ce78c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ds](structtask__state__segment.md#ac04302ea0ad115bbc792ae40396ce78c);

[ 84](structtask__state__segment.md#aa643892a3d4af08cf265349a67cb5a45) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_8](structtask__state__segment.md#aa643892a3d4af08cf265349a67cb5a45);

[ 85](structtask__state__segment.md#a8954360b2c87c2de06c3ed56437f9a32) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [fs](structtask__state__segment.md#a8954360b2c87c2de06c3ed56437f9a32);

[ 86](structtask__state__segment.md#a12e6373361b91eb6d1895f9567eb6d08) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_9](structtask__state__segment.md#a12e6373361b91eb6d1895f9567eb6d08);

[ 87](structtask__state__segment.md#ac0a81528e661c91b158f030b6766fd7b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [gs](structtask__state__segment.md#ac0a81528e661c91b158f030b6766fd7b);

[ 88](structtask__state__segment.md#a302eaf04a2515f8683dd306cc2448272) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_10](structtask__state__segment.md#a302eaf04a2515f8683dd306cc2448272);

[ 89](structtask__state__segment.md#ab6dfdcda415383ef97b8d1363c202f7b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ldt\_ss](structtask__state__segment.md#ab6dfdcda415383ef97b8d1363c202f7b);

[ 90](structtask__state__segment.md#aeeff71878d4552cf204e882170afe2bf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_11](structtask__state__segment.md#aeeff71878d4552cf204e882170afe2bf);

[ 91](structtask__state__segment.md#ad26eb9b45acb4b97fecd6a9654b32b07) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [t](structtask__state__segment.md#ad26eb9b45acb4b97fecd6a9654b32b07):1; /\* Trap bit \*/

[ 92](structtask__state__segment.md#a1518afb7acfda8e8c15b2750b726a900) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_12](structtask__state__segment.md#a1518afb7acfda8e8c15b2750b726a900):15;

[ 93](structtask__state__segment.md#a4d0ac1ee16bf85562c7af4de080ecf43) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iomap](structtask__state__segment.md#a4d0ac1ee16bf85562c7af4de080ecf43);

94};

95

[ 96](segmentation_8h.md#a7ac21eabd74b9b1e132d0925841a162d)#define SEG\_SELECTOR(index, table, dpl) (index << 3 | table << 2 | dpl)

97

98/\* References

99 \*

100 \* Section 5.8.3 (Call gates)

101 \* Section 7.2.2 (TSS Descriptor)

102 \* Section 3.4.5 (Segment descriptors)

103 \* Section 6.11 (IDT Descriptors)

104 \*

105 \* IA architecture SW developer manual, Vol 3.

106 \*/

[ 107](structsegment__descriptor.md)struct \_\_packed [segment\_descriptor](structsegment__descriptor.md) {

108

109 /\* First DWORD: 0-15 \*/

110 union {

111 /\* IRQ, call, trap gates \*/

[ 112](structsegment__descriptor.md#aaec62c0ab8bb3ce1c01887ec2bc3579c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [limit\_low](structsegment__descriptor.md#aaec62c0ab8bb3ce1c01887ec2bc3579c);

113

114 /\* Task gates \*/

[ 115](structsegment__descriptor.md#acb81ff32dbec3821c9ba1cb423c5bb4d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_task\_gate\_0](structsegment__descriptor.md#acb81ff32dbec3821c9ba1cb423c5bb4d);

116

117 /\* Everything else \*/

[ 118](structsegment__descriptor.md#aacf357093163d9cb7c29de2cd4d74af1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [offset\_low](structsegment__descriptor.md#aacf357093163d9cb7c29de2cd4d74af1);

119 };

120

121 /\* First DWORD: 16-31 \*/

122 union {

123 /\* Call/Task/Interrupt/Trap gates \*/

[ 124](structsegment__descriptor.md#ada9905938c5214787bb9a235658582dd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [segment\_selector](structsegment__descriptor.md#ada9905938c5214787bb9a235658582dd);

125

126 /\* TSS/LDT/Segments \*/

[ 127](structsegment__descriptor.md#a22d9a7e9718d670507a0555b131079aa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [base\_low](structsegment__descriptor.md#a22d9a7e9718d670507a0555b131079aa); /\* Bits 0-15 \*/

128 };

129

130 /\* Second DWORD: 0-7 \*/

131 union {

132 /\* TSS/LDT/Segments \*/

[ 133](structsegment__descriptor.md#a9bc044fe835300da74561089217ae3b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [base\_mid](structsegment__descriptor.md#a9bc044fe835300da74561089217ae3b2); /\* Bits 16-23 \*/

134

135 /\* Task gates \*/

[ 136](structsegment__descriptor.md#a28e1c069a7afe06119ff057ecf388bd2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved\_task\_gate\_1](structsegment__descriptor.md#a28e1c069a7afe06119ff057ecf388bd2);

137

138 /\* IRQ/Trap/Call Gates \*/

139 struct {

140 /\* Reserved except in case of call gates \*/

[ 141](structsegment__descriptor.md#a6edf9d47468d11d8bbc2c3525217b42d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved\_or\_param](structsegment__descriptor.md#a6edf9d47468d11d8bbc2c3525217b42d):5;

142

143 /\* Bits 5-7 0 0 0 per CPU manual \*/

[ 144](structsegment__descriptor.md#a17006cb3ba7efd21a951e882e34b088d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [always\_0\_0](structsegment__descriptor.md#a17006cb3ba7efd21a951e882e34b088d):3;

145 };

146 };

147

148 /\* Second DWORD: 8-15 \*/

149 union {

150 /\* Code or data Segments \*/

151 struct {

152 /\* Set by the processor, init to 0 \*/

[ 153](structsegment__descriptor.md#aaa5b961b21b18d1efd9987dbfc42ad95) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [accessed](structsegment__descriptor.md#aaa5b961b21b18d1efd9987dbfc42ad95):1;

154

155 /\* executable ? readable : writable \*/

[ 156](structsegment__descriptor.md#a598e508bbfbb9ed317bf6b91fd80b0e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rw](structsegment__descriptor.md#a598e508bbfbb9ed317bf6b91fd80b0e9):1;

157 /\* executable ? conforming : direction \*/

[ 158](structsegment__descriptor.md#a25407a6f10ee04a42832238639e4d4ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cd](structsegment__descriptor.md#a25407a6f10ee04a42832238639e4d4ac):1;

159 /\* 1=code 0=data \*/

[ 160](structsegment__descriptor.md#a45ebb67e9b54d4780ec42861e13531fd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [executable](structsegment__descriptor.md#a45ebb67e9b54d4780ec42861e13531fd):1;

161

162 /\* Next 3 fields actually common to all \*/

163

164 /\* 1=code or data, 0=system type \*/

[ 165](structsegment__descriptor.md#a95674f043c616032bf416facd6ac0469) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [descriptor\_type](structsegment__descriptor.md#a95674f043c616032bf416facd6ac0469):1;

166

[ 167](structsegment__descriptor.md#af9c72e8bd49845bf9c9bc16c2b788adf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dpl](structsegment__descriptor.md#af9c72e8bd49845bf9c9bc16c2b788adf):2;

[ 168](structsegment__descriptor.md#a61eda78022c10db647ce9e76a62a27a6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [present](structsegment__descriptor.md#a61eda78022c10db647ce9e76a62a27a6):1;

169 };

170

171 /\* System types \*/

172 struct {

173 /\* One of the SEG\_TYPE\_\* macros above \*/

[ 174](structsegment__descriptor.md#a88f41f8cda2177a6d70b9cf7c315053c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structsegment__descriptor.md#a88f41f8cda2177a6d70b9cf7c315053c):4;

175

176 /\* Alas, C doesn't let you do a union of the first

177 \* 4 bits of a bitfield and put the rest outside of it,

178 \* it ends up getting padded.

179 \*/

[ 180](structsegment__descriptor.md#ac9f594b7ca9e04d5a7cf8a246c73c7d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [use\_other\_union](structsegment__descriptor.md#ac9f594b7ca9e04d5a7cf8a246c73c7d5):4;

181 };

182 };

183

184 /\* Second DWORD: 16-31 \*/

185 union {

186 /\* Call/IRQ/trap gates \*/

[ 187](structsegment__descriptor.md#a86d61b5de39020e207f567a5909aeaba) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [offset\_hi](structsegment__descriptor.md#a86d61b5de39020e207f567a5909aeaba);

188

189 /\* Task Gates \*/

[ 190](structsegment__descriptor.md#a1a8678d1406de90c691a243a4562997d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved\_task\_gate\_2](structsegment__descriptor.md#a1a8678d1406de90c691a243a4562997d);

191

192 /\* segment/LDT/TSS \*/

193 struct {

[ 194](structsegment__descriptor.md#ad233fd87d891ca5f44b7e414c8766b05) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [limit\_hi](structsegment__descriptor.md#ad233fd87d891ca5f44b7e414c8766b05):4;

195

196 /\* flags \*/

[ 197](structsegment__descriptor.md#a59e97c4fc79505fd8095d02edc01480f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [avl](structsegment__descriptor.md#a59e97c4fc79505fd8095d02edc01480f):1; /\* CPU ignores this \*/

198

199 /\* 1=Indicates 64-bit code segment in IA-32e mode \*/

[ 200](structsegment__descriptor.md#aa62f29b11de78f55aa7a829d69a07939) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags\_l](structsegment__descriptor.md#aa62f29b11de78f55aa7a829d69a07939):1; /\* L field \*/

201

[ 202](structsegment__descriptor.md#a3b59b1ec549510eae9c3c2772d782e1a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [db](structsegment__descriptor.md#a3b59b1ec549510eae9c3c2772d782e1a):1; /\* D/B field 1=32-bit 0=16-bit\*/

[ 203](structsegment__descriptor.md#aebd148eac6d6e78c0a028531a76d22a8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [granularity](structsegment__descriptor.md#aebd148eac6d6e78c0a028531a76d22a8):1;

204

[ 205](structsegment__descriptor.md#a37dcfdc6eea1021d6be4f18aa26d4030) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [base\_hi](structsegment__descriptor.md#a37dcfdc6eea1021d6be4f18aa26d4030); /\* Bits 24-31 \*/

206 };

207 };

208

209};

210

211

212/\* Address of this passed to lidt/lgdt.

213 \* IA manual calls this a 'pseudo descriptor'.

214 \*/

[ 215](structpseudo__descriptor.md)struct \_\_packed [pseudo\_descriptor](structpseudo__descriptor.md) {

[ 216](structpseudo__descriptor.md#ac20c21d8d985238e7b83c08ea735ca27) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [size](structpseudo__descriptor.md#ac20c21d8d985238e7b83c08ea735ca27);

[ 217](structpseudo__descriptor.md#ad21f2391c31085657551eabf92249b8c) struct [segment\_descriptor](structsegment__descriptor.md) \*[entries](structpseudo__descriptor.md#ad21f2391c31085657551eabf92249b8c);

218};

219

220

221/\*

222 \* Full linear address (segment selector+offset), for far jumps/calls

223 \*/

[ 224](structfar__ptr.md)struct \_\_packed [far\_ptr](structfar__ptr.md) {

[ 226](structfar__ptr.md#a348a66049c5a1cf56e86743c03ce568b) void \*[offset](structfar__ptr.md#a348a66049c5a1cf56e86743c03ce568b);

[ 228](structfar__ptr.md#a756bf5b1059a1d637556aadbf687df31) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sel](structfar__ptr.md#a756bf5b1059a1d637556aadbf687df31);

229};

230

231

[ 232](segmentation_8h.md#abe841886ae3cb0d59ceb52885d1283c7)#define DT\_ZERO\_ENTRY { { 0 } }

233

234/\* NOTE: the below macros only work for fixed addresses provided at build time.

235 \* Base addresses or offsets cannot be &some\_variable, as pointer values are not

236 \* known until link time and the compiler has to split the address into various

237 \* fields in the segment selector well before that.

238 \*

239 \* If you really need to put &some\_variable as the base address in some

240 \* segment descriptor, you will either need to do the assignment at runtime

241 \* or implement some tool to populate values post-link like gen\_idt does.

242 \*/

243#define \_LIMIT\_AND\_BASE(base\_p, limit\_p, granularity\_p) \

244 .base\_low = (((uint32\_t)base\_p) & 0xFFFF), \

245 .base\_mid = (((base\_p) >> 16) & 0xFF), \

246 .base\_hi = (((base\_p) >> 24) & 0xFF), \

247 .limit\_low = ((limit\_p) & 0xFFFF), \

248 .limit\_hi = (((limit\_p) >> 16) & 0xF), \

249 .granularity = (granularity\_p), \

250 .flags\_l = 0, \

251 .db = 1, \

252 .avl = 0

253

254#define \_SEGMENT\_AND\_OFFSET(segment\_p, offset\_p) \

255 .segment\_selector = (segment\_p), \

256 .offset\_low = ((offset\_p) & 0xFFFF), \

257 .offset\_hi = ((offset\_p) >> 16)

258

259#define \_DESC\_COMMON(dpl\_p) \

260 .dpl = (dpl\_p), \

261 .present = 1

262

263#define \_SYS\_DESC(type\_p) \

264 .type = type\_p, \

265 .descriptor\_type = 0

266

[ 267](segmentation_8h.md#ab5c6bcde7b78dff38fcb2c4f3933e976)#define DT\_CODE\_SEG\_ENTRY(base\_p, limit\_p, granularity\_p, dpl\_p, readable\_p, \

268 conforming\_p) \

269 { \

270 \_DESC\_COMMON(dpl\_p), \

271 \_LIMIT\_AND\_BASE(base\_p, limit\_p, granularity\_p), \

272 .accessed = 0, \

273 .rw = (readable\_p), \

274 .cd = (conforming\_p), \

275 .executable = 1, \

276 .descriptor\_type = 1 \

277 }

278

[ 279](segmentation_8h.md#a91d1151f098e25c090d23d837c7aab05)#define DT\_DATA\_SEG\_ENTRY(base\_p, limit\_p, granularity\_p, dpl\_p, writable\_p, \

280 direction\_p) \

281 { \

282 \_DESC\_COMMON(dpl\_p), \

283 \_LIMIT\_AND\_BASE(base\_p, limit\_p, granularity\_p), \

284 .accessed = 0, \

285 .rw = (writable\_p), \

286 .cd = (direction\_p), \

287 .executable = 0, \

288 .descriptor\_type = 1 \

289 }

290

[ 291](segmentation_8h.md#af27ff503d122d2da7548544833ec8549)#define DT\_LDT\_ENTRY(base\_p, limit\_p, granularity\_p, dpl\_p) \

292 { \

293 \_DESC\_COMMON(dpl\_p), \

294 \_LIMIT\_AND\_BASE(base\_p, limit\_p, granularity\_p), \

295 \_SYS\_DESC(SEG\_TYPE\_LDT) \

296 }

297

[ 298](segmentation_8h.md#ae5739136f793ed325e29441584ea65a5)#define DT\_TSS\_ENTRY(base\_p, limit\_p, granularity\_p, dpl\_p) \

299 { \

300 \_DESC\_COMMON(dpl\_p), \

301 \_LIMIT\_AND\_BASE(base\_p, limit\_p, granularity\_p), \

302 \_SYS\_DESC(SEG\_TYPE\_TSS) \

303 }

304

305/\* "standard" TSS segments that don't stuff extra data past the end of the

306 \* TSS struct

307 \*/

[ 308](segmentation_8h.md#a80cfbaa5c30032fafa5507255a2910e4)#define DT\_TSS\_STD\_ENTRY(base\_p, dpl\_p) \

309 DT\_TSS\_ENTRY(base\_p, sizeof(struct task\_state\_segment), DT\_GRAN\_BYTE, \

310 dpl\_p)

311

[ 312](segmentation_8h.md#a3d598069efca9fad4537f5184f65a1a4)#define DT\_TASK\_GATE\_ENTRY(segment\_p, dpl\_p) \

313 { \

314 \_DESC\_COMMON(dpl\_p), \

315 \_SYS\_DESC(SEG\_TYPE\_TASK\_GATE), \

316 .segment\_selector = (segment\_p) \

317 }

318

[ 319](segmentation_8h.md#a75b12840f3c26ab2de1240874c6ffc82)#define DT\_IRQ\_GATE\_ENTRY(segment\_p, offset\_p, dpl\_p) \

320 { \

321 \_DESC\_COMMON(dpl\_p), \

322 \_SEGMENT\_AND\_OFFSET(segment\_p, offset\_p), \

323 \_SYS\_DESC(SEG\_TYPE\_IRQ\_GATE), \

324 .always\_0\_0 = 0 \

325 }

326

[ 327](segmentation_8h.md#a21a76c871381dce14ff5f35520db7cf0)#define DT\_TRAP\_GATE\_ENTRY(segment\_p, offset\_p, dpl\_p) \

328 { \

329 \_DESC\_COMMON(dpl\_p), \

330 \_SEGMENT\_AND\_OFFSET(segment\_p, offset\_p), \

331 \_SYS\_DESC(SEG\_TYPE\_TRAP\_GATE), \

332 .always\_0\_0 = 0 \

333 }

334

[ 335](segmentation_8h.md#a275e217de9e845c8c9ac717120883796)#define DT\_CALL\_GATE\_ENTRY(segment\_p, offset\_p, dpl\_p, param\_count\_p) \

336 { \

337 \_DESC\_COMMON(dpl\_p), \

338 \_SEGMENT\_AND\_OFFSET(segment\_p, offset\_p), \

339 \_SYS\_DESC(SEG\_TYPE\_TRAP\_GATE), \

340 .reserved\_or\_param = (param\_count\_p), \

341 .always\_0\_0 = 0 \

342 }

343

[ 344](segmentation_8h.md#a1ea5335d043ecfb349e0a97da0734a51)#define DTE\_BASE(dt\_entry) ((dt\_entry)->base\_low | \

345 ((dt\_entry)->base\_mid << 16) | \

346 ((dt\_entry)->base\_hi << 24))

347

[ 348](segmentation_8h.md#a0f68ae723f072069a290b322aee9a133)#define DTE\_LIMIT(dt\_entry) ((dt\_entry)->limit\_low | \

349 ((dt\_entry)->limit\_hi << 16))

350

[ 351](segmentation_8h.md#a1539f29629508325e28796d3226630cc)#define DTE\_OFFSET(dt\_entry) ((dt\_entry)->offset\_low | \

352 ((dt\_entry)->offset\_hi << 16))

353

[ 354](segmentation_8h.md#a76e349fa3b5b4263cf2fbe93e11ece50)#define DT\_INIT(entries) { sizeof(entries) - 1, &entries[0] }

355

356#ifdef CONFIG\_SET\_GDT

357/\* This is either the ROM-based GDT in crt0.S or generated by gen\_gdt.py,

358 \* depending on CONFIG\_GDT\_DYNAMIC

359 \*/

360extern struct [pseudo\_descriptor](structpseudo__descriptor.md) \_gdt;

361#endif

362

363extern const struct [pseudo\_descriptor](structpseudo__descriptor.md) z\_idt;

364

374static inline void z\_sd\_set\_seg\_offset(struct [segment\_descriptor](structsegment__descriptor.md) \*sd,

375 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) segment\_selector,

376 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset)

377{

378 sd->[offset\_low](structsegment__descriptor.md#aacf357093163d9cb7c29de2cd4d74af1) = offset & 0xFFFFU;

379 sd->[offset\_hi](structsegment__descriptor.md#a86d61b5de39020e207f567a5909aeaba) = offset >> 16U;

380 sd->[segment\_selector](structsegment__descriptor.md#ada9905938c5214787bb9a235658582dd) = segment\_selector;

381 sd->[always\_0\_0](structsegment__descriptor.md#a17006cb3ba7efd21a951e882e34b088d) = 0U;

382}

383

384

393static inline void z\_init\_irq\_gate(struct [segment\_descriptor](structsegment__descriptor.md) \*sd,

394 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seg\_selector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset,

395 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dpl)

396{

397 z\_sd\_set\_seg\_offset(sd, seg\_selector, offset);

398 sd->[dpl](structsegment__descriptor.md#af9c72e8bd49845bf9c9bc16c2b788adf) = dpl;

399 sd->[descriptor\_type](structsegment__descriptor.md#a95674f043c616032bf416facd6ac0469) = [DT\_TYPE\_SYSTEM](segmentation_8h.md#a7e6ddc88924ea43b4d89f367cee558d4);

400 sd->[present](structsegment__descriptor.md#a61eda78022c10db647ce9e76a62a27a6) = 1U;

401 sd->[type](structsegment__descriptor.md#a88f41f8cda2177a6d70b9cf7c315053c) = [SEG\_TYPE\_IRQ\_GATE](segmentation_8h.md#a62c20d09a1f35aadbffc000ce695aca5);

402}

403

409static inline void \_set\_tss([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sel)

410{

411 \_\_asm\_\_ \_\_volatile\_\_ ("ltr %0" :: "r" (sel));

412}

413

414

420static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_get\_tss(void)

421{

422 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sel;

423

424 \_\_asm\_\_ \_\_volatile\_\_ ("str %0" : "=r" (sel));

425 return sel;

426}

427

428

434static inline void \_get\_gdt(struct [pseudo\_descriptor](structpseudo__descriptor.md) \*gdt)

435{

436 \_\_asm\_\_ \_\_volatile\_\_ ("sgdt %0" : "=m" (\*gdt));

437}

438

439

445static inline void \_get\_idt(struct [pseudo\_descriptor](structpseudo__descriptor.md) \*idt)

446{

447 \_\_asm\_\_ \_\_volatile\_\_ ("sidt %0" : "=m" (\*idt));

448}

449

450

456static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_get\_ldt(void)

457{

458 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ret;

459

460 \_\_asm\_\_ \_\_volatile\_\_ ("sldt %0" : "=m" (ret));

461 return ret;

462}

463

464

470static inline void \_set\_ldt([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ldt)

471{

472 \_\_asm\_\_ \_\_volatile\_\_ ("lldt %0" :: "m" (ldt));

473

474}

475

484static inline void \_set\_gdt(const struct [pseudo\_descriptor](structpseudo__descriptor.md) \*gdt)

485{

486 \_\_asm\_\_ \_\_volatile\_\_ ("lgdt %0" :: "m" (\*gdt));

487}

488

489

495static inline void z\_set\_idt(const struct [pseudo\_descriptor](structpseudo__descriptor.md) \*idt)

496{

497 \_\_asm\_\_ \_\_volatile\_\_ ("lidt %0" :: "m" (\*idt));

498}

499

500

506static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_get\_cs(void)

507{

508 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cs = 0U;

509

510 \_\_asm\_\_ \_\_volatile\_\_ ("mov %%cs, %0" : "=r" (cs));

511 return cs;

512}

513

514

520static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_get\_ds(void)

521{

522 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ds = 0U;

523

524 \_\_asm\_\_ \_\_volatile\_\_ ("mov %%ds, %0" : "=r" (ds));

525 return ds;

526}

527

528

529#endif /\* \_ASMLANGUAGE \*/

530

531#ifdef \_\_cplusplus

532}

533#endif

534

535#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_SEGMENTATION\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[SEG\_TYPE\_IRQ\_GATE](segmentation_8h.md#a62c20d09a1f35aadbffc000ce695aca5)

#define SEG\_TYPE\_IRQ\_GATE

**Definition** segmentation.h:30

[DT\_TYPE\_SYSTEM](segmentation_8h.md#a7e6ddc88924ea43b4d89f367cee558d4)

#define DT\_TYPE\_SYSTEM

**Definition** segmentation.h:48

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[far\_ptr](structfar__ptr.md)

**Definition** segmentation.h:224

[far\_ptr::offset](structfar__ptr.md#a348a66049c5a1cf56e86743c03ce568b)

void \* offset

Far pointer offset, unused when invoking a task.

**Definition** segmentation.h:226

[far\_ptr::sel](structfar__ptr.md#a756bf5b1059a1d637556aadbf687df31)

uint16\_t sel

Far pointer segment/gate selector.

**Definition** segmentation.h:228

[pseudo\_descriptor](structpseudo__descriptor.md)

**Definition** segmentation.h:215

[pseudo\_descriptor::size](structpseudo__descriptor.md#ac20c21d8d985238e7b83c08ea735ca27)

uint16\_t size

**Definition** segmentation.h:216

[pseudo\_descriptor::entries](structpseudo__descriptor.md#ad21f2391c31085657551eabf92249b8c)

struct segment\_descriptor \* entries

**Definition** segmentation.h:217

[segment\_descriptor](structsegment__descriptor.md)

**Definition** segmentation.h:107

[segment\_descriptor::always\_0\_0](structsegment__descriptor.md#a17006cb3ba7efd21a951e882e34b088d)

uint8\_t always\_0\_0

**Definition** segmentation.h:144

[segment\_descriptor::reserved\_task\_gate\_2](structsegment__descriptor.md#a1a8678d1406de90c691a243a4562997d)

uint16\_t reserved\_task\_gate\_2

**Definition** segmentation.h:190

[segment\_descriptor::base\_low](structsegment__descriptor.md#a22d9a7e9718d670507a0555b131079aa)

uint16\_t base\_low

**Definition** segmentation.h:127

[segment\_descriptor::cd](structsegment__descriptor.md#a25407a6f10ee04a42832238639e4d4ac)

uint8\_t cd

**Definition** segmentation.h:158

[segment\_descriptor::reserved\_task\_gate\_1](structsegment__descriptor.md#a28e1c069a7afe06119ff057ecf388bd2)

uint8\_t reserved\_task\_gate\_1

**Definition** segmentation.h:136

[segment\_descriptor::base\_hi](structsegment__descriptor.md#a37dcfdc6eea1021d6be4f18aa26d4030)

uint8\_t base\_hi

**Definition** segmentation.h:205

[segment\_descriptor::db](structsegment__descriptor.md#a3b59b1ec549510eae9c3c2772d782e1a)

uint8\_t db

**Definition** segmentation.h:202

[segment\_descriptor::executable](structsegment__descriptor.md#a45ebb67e9b54d4780ec42861e13531fd)

uint8\_t executable

**Definition** segmentation.h:160

[segment\_descriptor::rw](structsegment__descriptor.md#a598e508bbfbb9ed317bf6b91fd80b0e9)

uint8\_t rw

**Definition** segmentation.h:156

[segment\_descriptor::avl](structsegment__descriptor.md#a59e97c4fc79505fd8095d02edc01480f)

uint8\_t avl

**Definition** segmentation.h:197

[segment\_descriptor::present](structsegment__descriptor.md#a61eda78022c10db647ce9e76a62a27a6)

uint8\_t present

**Definition** segmentation.h:168

[segment\_descriptor::reserved\_or\_param](structsegment__descriptor.md#a6edf9d47468d11d8bbc2c3525217b42d)

uint8\_t reserved\_or\_param

**Definition** segmentation.h:141

[segment\_descriptor::offset\_hi](structsegment__descriptor.md#a86d61b5de39020e207f567a5909aeaba)

uint16\_t offset\_hi

**Definition** segmentation.h:187

[segment\_descriptor::type](structsegment__descriptor.md#a88f41f8cda2177a6d70b9cf7c315053c)

uint8\_t type

**Definition** segmentation.h:174

[segment\_descriptor::descriptor\_type](structsegment__descriptor.md#a95674f043c616032bf416facd6ac0469)

uint8\_t descriptor\_type

**Definition** segmentation.h:165

[segment\_descriptor::base\_mid](structsegment__descriptor.md#a9bc044fe835300da74561089217ae3b2)

uint8\_t base\_mid

**Definition** segmentation.h:133

[segment\_descriptor::flags\_l](structsegment__descriptor.md#aa62f29b11de78f55aa7a829d69a07939)

uint8\_t flags\_l

**Definition** segmentation.h:200

[segment\_descriptor::accessed](structsegment__descriptor.md#aaa5b961b21b18d1efd9987dbfc42ad95)

uint8\_t accessed

**Definition** segmentation.h:153

[segment\_descriptor::offset\_low](structsegment__descriptor.md#aacf357093163d9cb7c29de2cd4d74af1)

uint16\_t offset\_low

**Definition** segmentation.h:118

[segment\_descriptor::limit\_low](structsegment__descriptor.md#aaec62c0ab8bb3ce1c01887ec2bc3579c)

uint16\_t limit\_low

**Definition** segmentation.h:112

[segment\_descriptor::use\_other\_union](structsegment__descriptor.md#ac9f594b7ca9e04d5a7cf8a246c73c7d5)

uint8\_t use\_other\_union

**Definition** segmentation.h:180

[segment\_descriptor::reserved\_task\_gate\_0](structsegment__descriptor.md#acb81ff32dbec3821c9ba1cb423c5bb4d)

uint16\_t reserved\_task\_gate\_0

**Definition** segmentation.h:115

[segment\_descriptor::limit\_hi](structsegment__descriptor.md#ad233fd87d891ca5f44b7e414c8766b05)

uint8\_t limit\_hi

**Definition** segmentation.h:194

[segment\_descriptor::segment\_selector](structsegment__descriptor.md#ada9905938c5214787bb9a235658582dd)

uint16\_t segment\_selector

**Definition** segmentation.h:124

[segment\_descriptor::granularity](structsegment__descriptor.md#aebd148eac6d6e78c0a028531a76d22a8)

uint8\_t granularity

**Definition** segmentation.h:203

[segment\_descriptor::dpl](structsegment__descriptor.md#af9c72e8bd49845bf9c9bc16c2b788adf)

uint8\_t dpl

**Definition** segmentation.h:167

[task\_state\_segment](structtask__state__segment.md)

**Definition** segmentation.h:54

[task\_state\_segment::ss](structtask__state__segment.md#a007494cfabe3da5e7ae4fc17a57cb33d)

uint16\_t ss

**Definition** segmentation.h:81

[task\_state\_segment::reserved\_9](structtask__state__segment.md#a12e6373361b91eb6d1895f9567eb6d08)

uint16\_t reserved\_9

**Definition** segmentation.h:86

[task\_state\_segment::cs](structtask__state__segment.md#a14fc9b3472e8ba0b02e1a74576d83ded)

uint16\_t cs

**Definition** segmentation.h:79

[task\_state\_segment::reserved\_12](structtask__state__segment.md#a1518afb7acfda8e8c15b2750b726a900)

uint16\_t reserved\_12

**Definition** segmentation.h:92

[task\_state\_segment::ebp](structtask__state__segment.md#a1b9505b29bba1d91c92457f898e29175)

uint32\_t ebp

**Definition** segmentation.h:74

[task\_state\_segment::esp2](structtask__state__segment.md#a1cb20df4a49a73a2d0b88a8df19621c2)

uint32\_t esp2

**Definition** segmentation.h:63

[task\_state\_segment::ss1](structtask__state__segment.md#a1e8cf1eb785cd0cebfab53c6b6f55922)

uint16\_t ss1

**Definition** segmentation.h:61

[task\_state\_segment::esi](structtask__state__segment.md#a23f6ba3c3c80d83eabb3e4981a684f86)

uint32\_t esi

**Definition** segmentation.h:75

[task\_state\_segment::reserved\_10](structtask__state__segment.md#a302eaf04a2515f8683dd306cc2448272)

uint16\_t reserved\_10

**Definition** segmentation.h:88

[task\_state\_segment::edi](structtask__state__segment.md#a305dc05c6ce45b06d5c08886fbc629d2)

uint32\_t edi

**Definition** segmentation.h:76

[task\_state\_segment::reserved\_4](structtask__state__segment.md#a354f74ae39ffff533dfe18693fc813d4)

uint16\_t reserved\_4

**Definition** segmentation.h:65

[task\_state\_segment::edx](structtask__state__segment.md#a36275826a694fb98a7e3d68253991eb3)

uint32\_t edx

**Definition** segmentation.h:71

[task\_state\_segment::ecx](structtask__state__segment.md#a3bd54264357890c87cfc6ebf12ffa8eb)

uint32\_t ecx

**Definition** segmentation.h:70

[task\_state\_segment::cr3](structtask__state__segment.md#a3de57a3414f018da7b074a8c0b38ee98)

uint32\_t cr3

**Definition** segmentation.h:66

[task\_state\_segment::iomap](structtask__state__segment.md#a4d0ac1ee16bf85562c7af4de080ecf43)

uint16\_t iomap

**Definition** segmentation.h:93

[task\_state\_segment::reserved\_3](structtask__state__segment.md#a6790bfb30732ab246b20827fd5d26834)

uint16\_t reserved\_3

**Definition** segmentation.h:62

[task\_state\_segment::backlink](structtask__state__segment.md#a6dca0f6680e373545f31490cb4667a1e)

uint16\_t backlink

**Definition** segmentation.h:55

[task\_state\_segment::es](structtask__state__segment.md#a6fa263ba438e73c765619549082a9c6b)

uint16\_t es

**Definition** segmentation.h:77

[task\_state\_segment::ss0](structtask__state__segment.md#a74e85e53e171c23d5f29f1efe0131b0a)

uint16\_t ss0

**Definition** segmentation.h:58

[task\_state\_segment::ebx](structtask__state__segment.md#a80e9653cc996ae57e33e263773493058)

uint32\_t ebx

**Definition** segmentation.h:72

[task\_state\_segment::fs](structtask__state__segment.md#a8954360b2c87c2de06c3ed56437f9a32)

uint16\_t fs

**Definition** segmentation.h:85

[task\_state\_segment::reserved\_2](structtask__state__segment.md#a93ce3a1140962ce0bb74cb6101b5d696)

uint16\_t reserved\_2

**Definition** segmentation.h:59

[task\_state\_segment::esp1](structtask__state__segment.md#a9f656f69a3e9cd7d74e2e5c27a0c4d79)

uint32\_t esp1

**Definition** segmentation.h:60

[task\_state\_segment::eip](structtask__state__segment.md#aa1992e03e583070d318adb554f28b8e8)

uint32\_t eip

**Definition** segmentation.h:67

[task\_state\_segment::reserved\_8](structtask__state__segment.md#aa643892a3d4af08cf265349a67cb5a45)

uint16\_t reserved\_8

**Definition** segmentation.h:84

[task\_state\_segment::eflags](structtask__state__segment.md#ab5e6713aa56576ebf4b4f15bff800993)

uint32\_t eflags

**Definition** segmentation.h:68

[task\_state\_segment::ldt\_ss](structtask__state__segment.md#ab6dfdcda415383ef97b8d1363c202f7b)

uint16\_t ldt\_ss

**Definition** segmentation.h:89

[task\_state\_segment::ds](structtask__state__segment.md#ac04302ea0ad115bbc792ae40396ce78c)

uint16\_t ds

**Definition** segmentation.h:83

[task\_state\_segment::gs](structtask__state__segment.md#ac0a81528e661c91b158f030b6766fd7b)

uint16\_t gs

**Definition** segmentation.h:87

[task\_state\_segment::ss2](structtask__state__segment.md#ac8b023be5e2cd2d50ec55d15f7510c15)

uint16\_t ss2

**Definition** segmentation.h:64

[task\_state\_segment::eax](structtask__state__segment.md#aca6436062f7e47e63b364aa331498a9c)

uint32\_t eax

**Definition** segmentation.h:69

[task\_state\_segment::reserved\_5](structtask__state__segment.md#acae3c67be6cf9f776db8dbe60a13e192)

uint16\_t reserved\_5

**Definition** segmentation.h:78

[task\_state\_segment::reserved\_1](structtask__state__segment.md#ace0a346f5ca56fc785d17a8cb76c3f00)

uint16\_t reserved\_1

**Definition** segmentation.h:56

[task\_state\_segment::reserved\_6](structtask__state__segment.md#ad1a611412a5057e35d8c7fd88cb502fa)

uint16\_t reserved\_6

**Definition** segmentation.h:80

[task\_state\_segment::t](structtask__state__segment.md#ad26eb9b45acb4b97fecd6a9654b32b07)

uint8\_t t

**Definition** segmentation.h:91

[task\_state\_segment::reserved\_7](structtask__state__segment.md#ade71f2bdd6c3866243823ccf4dfc92ef)

uint16\_t reserved\_7

**Definition** segmentation.h:82

[task\_state\_segment::esp0](structtask__state__segment.md#ae613a01ad49d8aaa43fb955cf95e1de1)

uint32\_t esp0

**Definition** segmentation.h:57

[task\_state\_segment::reserved\_11](structtask__state__segment.md#aeeff71878d4552cf204e882170afe2bf)

uint16\_t reserved\_11

**Definition** segmentation.h:90

[task\_state\_segment::esp](structtask__state__segment.md#af439750f77fd6067776fd24c13443fde)

uint32\_t esp

**Definition** segmentation.h:73

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [segmentation.h](segmentation_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
