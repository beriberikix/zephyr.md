---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/asm-macro-64-bit-mwdt_8h.html
original_path: doxygen/html/asm-macro-64-bit-mwdt_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

asm-macro-64-bit-mwdt.h File Reference

[Go to the source code of this file.](asm-macro-64-bit-mwdt_8h_source.md)

| Variables | |
| --- | --- |
| macro | [MOVR](#a62c92c2e7e269b0afb80256c5207da7b) |
| macro | [d](#a115a46bcc971f5b76b0c10997a1902e9) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro | [LDR](#a4bfaf9dfe8fddd7526716c9007a7cd87) |
| macro s movl &$suffix s endm macro | [s](#a8592182fba37f6a5ad2e67576130f9df) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if | [$narg](#ad1385b31668df52491c21319ebd92fd9) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro | [STR](#ae60b8dec93a8b22478b4a3c0e5e3041e) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro | [PUSHR](#a816d3dff509e4fbd6f919c24ea6baa00) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro | [POPR](#ae0f954f282eaa7ea513662f4c6f5b86b) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro | [LRR](#a917ec782be0164288e0437198ff99026) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro | [SRR](#a72534d5417fa70333c420b0b6e4b014f) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro | [ADDR](#abdb73303312677832377cec11ddbcfb2) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro | [ADD2R](#abae854c7c1e2bbdf09afd83e4a2f931b) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro | [ADD3R](#addcee75a0f02e7c0e6509a645faef441) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro | [SUBR](#aae8940805d698ecb34d3e7f37a4c4f34) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro | [BMSKNR](#aa5f8df7d6794de4e8b999d6f27eb26cd) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro | [LSRR](#aeb496276f0b24fe5026aa43a92ec6be1) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro | [ASLR](#a2029c0d417dae61e19843d312739a317) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro | [ANDR](#a77faee894232464d5aebec81651b4ec2) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro | [ORR](#aed2483697c78bf1e9bef39e9d9d4c11d) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro | [BRR](#a669b40b4c5c00c6c38d327ca6f8fb9f5) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro lbl br &$suffix l lbl endm macro | [BREQR](#af7748ddc29f3b0f94995b1b0393a7089) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro lbl br &$suffix l lbl endm macro lbl breql lbl endm macro | [CMPR](#a112901bfa2cae27eead5f1b117b276e6) |
| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl &$suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl &$suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl &$suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl &$suffix v endm macro v add2l &$suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro lbl br &$suffix l lbl endm macro lbl breql lbl endm macro | [op1](#a1aab4b8f06d98e34b6f619d279e48194) |

## Variable Documentation

## [◆ ](#ad1385b31668df52491c21319ebd92fd9)$narg

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if $narg |
| --- |

**Initial value:**

== 2

ldl\&$suffix [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

## [◆ ](#abae854c7c1e2bbdf09afd83e4a2f931b)ADD2R

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro ADD2R |
| --- |

## [◆ ](#addcee75a0f02e7c0e6509a645faef441)ADD3R

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro ADD3R |
| --- |

## [◆ ](#abdb73303312677832377cec11ddbcfb2)ADDR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro ADDR |
| --- |

## [◆ ](#a77faee894232464d5aebec81651b4ec2)ANDR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro ANDR |
| --- |

## [◆ ](#a2029c0d417dae61e19843d312739a317)ASLR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro ASLR |
| --- |

## [◆ ](#aa5f8df7d6794de4e8b999d6f27eb26cd)BMSKNR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro v subl v endm macro BMSKNR |
| --- |

## [◆ ](#af7748ddc29f3b0f94995b1b0393a7089)BREQR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro lbl br& $suffix l lbl endm macro BREQR |
| --- |

## [◆ ](#a669b40b4c5c00c6c38d327ca6f8fb9f5)BRR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro BRR |
| --- |

## [◆ ](#a112901bfa2cae27eead5f1b117b276e6)CMPR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro lbl br& $suffix l lbl endm macro lbl breql lbl endm macro CMPR |
| --- |

## [◆ ](#a115a46bcc971f5b76b0c10997a1902e9)d

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro lbl br& $suffix l lbl endm macro lbl breql d |
| --- |

## [◆ ](#a4bfaf9dfe8fddd7526716c9007a7cd87)LDR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro LDR |
| --- |

## [◆ ](#a917ec782be0164288e0437198ff99026)LRR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro LRR |
| --- |

## [◆ ](#aeb496276f0b24fe5026aa43a92ec6be1)LSRR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro LSRR |
| --- |

## [◆ ](#a62c92c2e7e269b0afb80256c5207da7b)MOVR

| macro MOVR |
| --- |

## [◆ ](#a1aab4b8f06d98e34b6f619d279e48194)op1

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro lbl br& $suffix l lbl endm macro lbl breql lbl endm macro op2 cmpl op1 |
| --- |

## [◆ ](#aed2483697c78bf1e9bef39e9d9d4c11d)ORR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro ORR |
| --- |

## [◆ ](#ae0f954f282eaa7ea513662f4c6f5b86b)POPR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro POPR |
| --- |

## [◆ ](#a816d3dff509e4fbd6f919c24ea6baa00)PUSHR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro PUSHR |
| --- |

## [◆ ](#a8592182fba37f6a5ad2e67576130f9df)s

| macro s movl& $suffix s endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro v subl v endm macro v bmsknl v endm macro v lsrl v endm macro v asll v endm macro v andl v endm macro v orl v endm macro lbl br& $suffix l lbl endm macro lbl breql s |
| --- |

## [◆ ](#a72534d5417fa70333c420b0b6e4b014f)SRR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro SRR |
| --- |

## [◆ ](#ae60b8dec93a8b22478b4a3c0e5e3041e)STR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro STR |
| --- |

## [◆ ](#aae8940805d698ecb34d3e7f37a4c4f34)SUBR

| macro [s](#a8592182fba37f6a5ad2e67576130f9df) movl& $suffix [s](#a8592182fba37f6a5ad2e67576130f9df) endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else ldl& $suffix endif endm macro [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) if else stl& $suffix endif endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) pushl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) popl [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) endm macro aux lrl aux endm macro aux srl aux endm macro v addl& $suffix v endm macro v add2l& $suffix v endm macro v add3l v endm macro SUBR |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [asm-compat](dir_728f9cb61d4414cdda9196b7386075ee.md)
- [asm-macro-64-bit-mwdt.h](asm-macro-64-bit-mwdt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
