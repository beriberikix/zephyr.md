---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/intc__vim_8h.html
original_path: doxygen/html/intc__vim_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_vim.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/dt-bindings/interrupt-controller/ti-vim.h](ti-vim_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](intc__vim_8h_source.md)

| Macros | |
| --- | --- |
| #define | [VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)   [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)([DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)(0, ti\_vim)) |
| #define | [VIM\_MAX\_IRQ\_PER\_GROUP](#af3def9f38617688929e29eec9651c64b)   (32) |
| #define | [VIM\_MAX\_GROUP\_NUM](#a2520b3f68146858942723fe295c0dae4)   (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))([CONFIG\_NUM\_IRQS](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837) / [VIM\_MAX\_IRQ\_PER\_GROUP](#af3def9f38617688929e29eec9651c64b))) |
| #define | [VIM\_GET\_IRQ\_GROUP\_NUM](#a2bbbdbfa2a3dd00d1bd54d5c804220c1)(n) |
| #define | [VIM\_GET\_IRQ\_BIT\_NUM](#a765f1dd48172c22f4fb9cb5eb2c0ecfc)(n) |
| #define | [VIM\_PRI\_INT\_MAX](#aba7671d7f7dee14d87f7feff8a3451f7)   (15) |
| #define | [VIM\_PID](#a378ef153f705928fff529e02838d50af)   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0000) |
| #define | [VIM\_INFO](#adf312872ea552e35a0e9fed4ef69ae11)   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0004) |
| #define | [VIM\_PRIIRQ](#ab4ee6967e7149c07a2690978e7a2f97b)   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0008) |
| #define | [VIM\_PRIFIQ](#a17ea1cd9d06d003bbc094bffbefb47c4)   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x000C) |
| #define | [VIM\_IRQGSTS](#a7bcbdd8241d466014361b13baf43d81b)   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0010) |
| #define | [VIM\_FIQGSTS](#a6c2b44a4cabf058542f9663f48d1bc07)   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0014) |
| #define | [VIM\_IRQVEC](#a893a5e8467a3e5417272dedc098e42b5)   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0018) |
| #define | [VIM\_FIQVEC](#aba9caef8adb052c353f54679b95f4001)   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x001C) |
| #define | [VIM\_ACTIRQ](#a814d881a2f50b7b47ab25084f59587f5)   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0020) |
| #define | [VIM\_ACTFIQ](#a48bda38b33fc5dfc695dfdbe627f4984)   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0024) |
| #define | [VIM\_DEDVEC](#ac77876e0bfdd3a9382e28728d9e2ebd3)   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0030) |
| #define | [VIM\_RAW](#a0b86c01e8e3844c71a74380c2392a847)(n) |
| #define | [VIM\_STS](#ae714f8162f5840ab2eb655d48c92ac99)(n) |
| #define | [VIM\_INTR\_EN\_SET](#a0d2b404f0483d09a32b6a4914cd660ef)(n) |
| #define | [VIM\_INTR\_EN\_CLR](#a313eefa1e7b90c3988c8d15c1dfb2aae)(n) |
| #define | [VIM\_IRQSTS](#a6a07b16389503e1131e9b46e84545c4e)(n) |
| #define | [VIM\_FIQSTS](#ac20f6ab045eb4c7193c94252d4ee26a5)(n) |
| #define | [VIM\_INTMAP](#adbf1801e1f7dfa45f19f20e91ccbf1e2)(n) |
| #define | [VIM\_INTTYPE](#a28965b8d5ed95f9bd0322e95d41aa65c)(n) |
| #define | [VIM\_PRI\_INT](#ad7c36f8650ff847544a550a31235193b)(n) |
| #define | [VIM\_VEC\_INT](#abb38d6437a3f25c193c2506fe97cf89c)(n) |
| #define | [VIM\_GRP\_RAW\_STS\_MASK](#acd62766b3379b5baf178a33b6ff3d905)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_RAW\_STS\_SHIFT](#ad28eafc29daa6e59de34e62f1493cfca)   (0x00000000U) |
| #define | [VIM\_GRP\_RAW\_STS\_RESETVAL](#aa82ed994598088a4a39bf628d78dc747)   (0x00000000U) |
| #define | [VIM\_GRP\_RAW\_STS\_MAX](#a2842ee6521e5115eb85dd2b591aebd9b)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_RAW\_RESETVAL](#a4817d3ad8ab3b557b19882b272d67d1b)   (0x00000000U) |
| #define | [VIM\_GRP\_STS\_MSK\_MASK](#a7f4d55def9ac847ff1c2f6739f09a636)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_STS\_MSK\_SHIFT](#a79f980ac35a193b154853fd35aa8bcaf)   (0x00000000U) |
| #define | [VIM\_GRP\_STS\_MSK\_RESETVAL](#aec03c90df4149318acb41f1feacd4392)   (0x00000000U) |
| #define | [VIM\_GRP\_STS\_MSK\_MAX](#a1c452655a919216d7ba809d96e1b0287)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_STS\_RESETVAL](#a229308ab7f2cd16ce15cbe0dd8c0197b)   (0x00000000U) |
| #define | [VIM\_GRP\_INTR\_EN\_SET\_MSK\_MASK](#a339c2737a2eb9180b78305a058b6aa90)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_INTR\_EN\_SET\_MSK\_SHIFT](#a9c5eb8d20f8de659ca970cd69c4cd193)   (0x00000000U) |
| #define | [VIM\_GRP\_INTR\_EN\_SET\_MSK\_RESETVAL](#a81eb2356267a972232177b893bc41fb7)   (0x00000000U) |
| #define | [VIM\_GRP\_INTR\_EN\_SET\_MSK\_MAX](#a61e07bf8b299223d8d4767aaa2e718b2)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_INTR\_EN\_SET\_RESETVAL](#a23b0f2ce857795c9e6c6faf35f124d02)   (0x00000000U) |
| #define | [VIM\_GRP\_INTR\_EN\_CLR\_MSK\_MASK](#a5b0397e530cdcc0ae4f88796a9ef86ef)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_INTR\_EN\_CLR\_MSK\_SHIFT](#ae3fde9d57f6e6328a7f88f6889d91c3a)   (0x00000000U) |
| #define | [VIM\_GRP\_INTR\_EN\_CLR\_MSK\_RESETVAL](#a5617ad614b65e9341c5f9b4a3405fce6)   (0x00000000U) |
| #define | [VIM\_GRP\_INTR\_EN\_CLR\_MSK\_MAX](#a1af7c911da646796d1091c4da9f45bf9)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_INTR\_EN\_CLR\_RESETVAL](#a1113d705a90dd04e9af1999c37f9cb8e)   (0x00000000U) |
| #define | [VIM\_GRP\_IRQSTS\_MSK\_MASK](#a13abe76418c094499d537b7fad5a171c)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_IRQSTS\_MSK\_SHIFT](#a24299da38556f543de8e12ff36a81d38)   (0x00000000U) |
| #define | [VIM\_GRP\_IRQSTS\_MSK\_RESETVAL](#ac4d5bf5d6ee09462f4254a12db2bad44)   (0x00000000U) |
| #define | [VIM\_GRP\_IRQSTS\_MSK\_MAX](#aa3a16c92d1f55aff8a9b750990a7daf1)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_IRQSTS\_RESETVAL](#a308a20f9e29c85ece314a6a005b6a4dd)   (0x00000000U) |
| #define | [VIM\_GRP\_FIQSTS\_MSK\_MASK](#a374962357620f5b6ea7f3938158f52c9)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_FIQSTS\_MSK\_SHIFT](#a3b5c2839ef08c51d8163048023bec7bc)   (0x00000000U) |
| #define | [VIM\_GRP\_FIQSTS\_MSK\_RESETVAL](#a75f2aa2343da1e6f1577189911c685ce)   (0x00000000U) |
| #define | [VIM\_GRP\_FIQSTS\_MSK\_MAX](#a7698addaef1b0850b538b508762da567)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_FIQSTS\_RESETVAL](#aff2481d09e0ed29c7206d28c098a0d14)   (0x00000000U) |
| #define | [VIM\_GRP\_INTMAP\_MSK\_MASK](#a0259713478ab1f5930d1b303450d9b72)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_INTMAP\_MSK\_SHIFT](#aea4c913d99500c4b3cb1c60b5b514c2f)   (0x00000000U) |
| #define | [VIM\_GRP\_INTMAP\_MSK\_RESETVAL](#ac5d9e9e42d0c203c22a357ccec802c72)   (0x00000000U) |
| #define | [VIM\_GRP\_INTMAP\_MSK\_MAX](#ad64d7f6045a420d2ed78f6bb0446294f)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_INTMAP\_RESETVAL](#a104e9c67c35b9656d451efbe5045cb78)   (0x00000000U) |
| #define | [VIM\_GRP\_INTTYPE\_MSK\_MASK](#a29cdb963486249ff8d87c1bf4ceeeb74)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_INTTYPE\_MSK\_SHIFT](#a6c1cd189c9e5426b8a79b97b1f860753)   (0x00000000U) |
| #define | [VIM\_GRP\_INTTYPE\_MSK\_RESETVAL](#a5d3443ac8213a8c02c364c9e6f37690c)   (0x00000000U) |
| #define | [VIM\_GRP\_INTTYPE\_MSK\_MAX](#a37f2063ecf4acdd91ab16a8941a9c51c)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_GRP\_INTTYPE\_RESETVAL](#a35adc119bb4371fe8cf7070336935720)   (0x00000000U) |
| #define | [VIM\_PRI\_INT\_VAL\_MASK](#a996fc01313c3b05b298f32b7691a0ba1)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| #define | [VIM\_PRI\_INT\_VAL\_SHIFT](#ad9d91c69c20c243578aea8028d4635a2)   (0x00000000U) |
| #define | [VIM\_PRI\_INT\_VAL\_RESETVAL](#a413968f03758ca53b005bfe7c5e3023b)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| #define | [VIM\_PRI\_INT\_VAL\_MAX](#af8297a7ca4b4b0cddb3703312fb858bb)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| #define | [VIM\_PRI\_INT\_RESETVAL](#a72fa57b55ef32e7c7db63932c28d65da)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| #define | [VIM\_VEC\_INT\_VAL\_MASK](#a8076a54316cec3fc0de52079bd4cd598)   (0xFFFFFFFCU) |
| #define | [VIM\_VEC\_INT\_VAL\_SHIFT](#a3024d3c80cdc3db66954fa83541ca389)   (0x00000002U) |
| #define | [VIM\_VEC\_INT\_VAL\_RESETVAL](#a3dd1401816579e5d07876b87b34e2177)   (0x00000000U) |
| #define | [VIM\_VEC\_INT\_VAL\_MAX](#a769edf746fb1ef704f85bfdee55fb136)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(30)) |
| #define | [VIM\_VEC\_INT\_RESETVAL](#a16bd2873cba17ebd29acd3aeb58b2df4)   (0x00000000U) |
| #define | [VIM\_INFO\_INTERRUPTS\_MASK](#adeba4e94c9d68665820fd13483d24b85)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(11)) |
| #define | [VIM\_INFO\_INTERRUPTS\_SHIFT](#ace1cb4b9d2de191575a9bba21882a025)   (0x00000000U) |
| #define | [VIM\_INFO\_INTERRUPTS\_RESETVAL](#ad37820d3013c0ed4867a7235ee16444f)   (0x00000400U) |
| #define | [VIM\_INFO\_INTERRUPTS\_MAX](#aca715ba5a23516302a6c1a648fbbdeea)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(11)) |
| #define | [VIM\_INFO\_RESETVAL](#a3fc8c50f54bc3a158dbfef51fb96ee5b)   (0x00000400U) |
| #define | [VIM\_PRIIRQ\_VALID\_MASK](#a4d4d0d285eabeccb6418c442a7b3453b)   (0x80000000U) |
| #define | [VIM\_PRIIRQ\_VALID\_SHIFT](#acaca01cbd74088f455f8345472424339)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(5)) |
| #define | [VIM\_PRIIRQ\_VALID\_RESETVAL](#a7026e741d660e4d893ac1457c12ef827)   (0x00000000U) |
| #define | [VIM\_PRIIRQ\_VALID\_MAX](#aacbd1281fb54586fa48c6ed3d49d62cd)   (0x00000001U) |
| #define | [VIM\_PRIIRQ\_VALID\_VAL\_TRUE](#adc2729dd6329da29bac1ac4942003f7d)   (0x1U) |
| #define | [VIM\_PRIIRQ\_VALID\_VAL\_FALSE](#a0966b95628413d1efdf9e572783865bd)   (0x0U) |
| #define | [VIM\_PRIIRQ\_PRI\_MASK](#ad952cdc46228507194a3b19baf6d71e7)   (0x000F0000U) |
| #define | [VIM\_PRIIRQ\_PRI\_SHIFT](#a31ed4fa3d085d39863d0da6b657ca0df)   (0x00000010U) |
| #define | [VIM\_PRIIRQ\_PRI\_RESETVAL](#a810037874c898a7c0f738096406b9148)   (0x00000000U) |
| #define | [VIM\_PRIIRQ\_PRI\_MAX](#ac3f1624d169a99edb836f3a3ba82acfa)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| #define | [VIM\_PRIIRQ\_NUM\_MASK](#a236930837a36a72e4b29f81175537543)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| #define | [VIM\_PRIIRQ\_NUM\_SHIFT](#ac7956ab58b6223b8e511892ff35d9375)   (0x00000000U) |
| #define | [VIM\_PRIIRQ\_NUM\_RESETVAL](#a4376b256f168336b45108b8255a0f92f)   (0x00000000U) |
| #define | [VIM\_PRIIRQ\_NUM\_MAX](#a610e6f20d550a0cc5e90f31f7ce9f065)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| #define | [VIM\_PRIIRQ\_RESETVAL](#a13826544f2e9cd4ce4164b62d8e82d7e)   (0x00000000U) |
| #define | [VIM\_PRIFIQ\_VALID\_MASK](#aba90d57af70816d9b58dc8851f6da004)   (0x80000000U) |
| #define | [VIM\_PRIFIQ\_VALID\_SHIFT](#a3c93252a9eae445243cd8a9c39d79f82)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(5)) |
| #define | [VIM\_PRIFIQ\_VALID\_RESETVAL](#a322fe75f392fb162f1c04330990ed2d7)   (0x00000000U) |
| #define | [VIM\_PRIFIQ\_VALID\_MAX](#ac8173b6b098e38ea9eebbf79e8f8a1da)   (0x00000001U) |
| #define | [VIM\_PRIFIQ\_VALID\_VAL\_TRUE](#ac5ced3000f18ecfc7fc5ea07e3473f78)   (0x1U) |
| #define | [VIM\_PRIFIQ\_VALID\_VAL\_FALSE](#a6bdf3d9847f3ccad759874bb5b09cfb4)   (0x0U) |
| #define | [VIM\_PRIFIQ\_PRI\_MASK](#a6de77b9058d6b58314097adebe045a86)   (0x000F0000U) |
| #define | [VIM\_PRIFIQ\_PRI\_SHIFT](#a3d61188f8ce9b07ac1bcb708c0a28619)   (0x00000010U) |
| #define | [VIM\_PRIFIQ\_PRI\_RESETVAL](#aa810609b09640d548c56bdfb09b9868c)   (0x00000000U) |
| #define | [VIM\_PRIFIQ\_PRI\_MAX](#a67922050c7eb81575c1b7b1e227b6839)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| #define | [VIM\_PRIFIQ\_NUM\_MASK](#aad509ed553a5e15f893390481ac739fa)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| #define | [VIM\_PRIFIQ\_NUM\_SHIFT](#af8b15089bdd21a468168c1d5e8fc7dad)   (0x00000000U) |
| #define | [VIM\_PRIFIQ\_NUM\_RESETVAL](#a608c0a95598b701c377351bdab275df4)   (0x00000000U) |
| #define | [VIM\_PRIFIQ\_NUM\_MAX](#ac27797438659455e527d82e9fb586b5a)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| #define | [VIM\_PRIFIQ\_RESETVAL](#adf127d9e139beb74e65b88741d82013a)   (0x00000000U) |
| #define | [VIM\_IRQGSTS\_STS\_MASK](#a4497e08f4d565ace708e50c84f0f51b6)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_IRQGSTS\_STS\_SHIFT](#a03180f0120311298a518f8f109fa2dee)   (0x00000000U) |
| #define | [VIM\_IRQGSTS\_STS\_RESETVAL](#af7d810589915de14ab7cff616fdb0b5f)   (0x00000000U) |
| #define | [VIM\_IRQGSTS\_STS\_MAX](#a82828e470cbcd1df782ed463c61ecfee)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_IRQGSTS\_RESETVAL](#a674113c74daca28dc3a3777cf2a33917)   (0x00000000U) |
| #define | [VIM\_FIQGSTS\_STS\_MASK](#a4047a2f3c251c623a7bb4f03e2c80aa9)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_FIQGSTS\_STS\_SHIFT](#a0cf8b2290a847eccb9206368c36d84d3)   (0x00000000U) |
| #define | [VIM\_FIQGSTS\_STS\_RESETVAL](#ac814862811ec1cf1d1e240c03fa5220a)   (0x00000000U) |
| #define | [VIM\_FIQGSTS\_STS\_MAX](#a06d51cb097cedabe76ab25fb2336be2b)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| #define | [VIM\_FIQGSTS\_RESETVAL](#ada89357c38ffaa43681b7e874aaddd6a)   (0x00000000U) |
| #define | [VIM\_IRQVEC\_ADDR\_MASK](#a854706bcbaeb0764d2dac7a325734b20)   (0xFFFFFFFCU) |
| #define | [VIM\_IRQVEC\_ADDR\_SHIFT](#a692248d3c771837c934b2057573511f7)   (0x00000002U) |
| #define | [VIM\_IRQVEC\_ADDR\_RESETVAL](#ad0643477818df3a01ec0aad56be04cb1)   (0x00000000U) |
| #define | [VIM\_IRQVEC\_ADDR\_MAX](#abb959b8bcc866cc955ae998ae62a2feb)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(30)) |
| #define | [VIM\_IRQVEC\_RESETVAL](#a5c92254c2655c9a73f13eba43e50a398)   (0x00000000U) |
| #define | [VIM\_FIQVEC\_ADDR\_MASK](#a88ff3e766b092657a21fdf7ae2e93564)   (0xFFFFFFFCU) |
| #define | [VIM\_FIQVEC\_ADDR\_SHIFT](#a0db8828c7c1b359335220d80cf6fcb6f)   (0x00000002U) |
| #define | [VIM\_FIQVEC\_ADDR\_RESETVAL](#a5694973ce948cb75ec95b457b58544a5)   (0x00000000U) |
| #define | [VIM\_FIQVEC\_ADDR\_MAX](#a9e15f36e9494b3f69bbf49d962c38590)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(30)) |
| #define | [VIM\_FIQVEC\_RESETVAL](#a972fd2da90560b549d4eacc367643367)   (0x00000000U) |
| #define | [VIM\_ACTIRQ\_VALID\_MASK](#a9740e75023b8bf6ddc87f2aabc234a5c)   (0x80000000U) |
| #define | [VIM\_ACTIRQ\_VALID\_SHIFT](#ab80c58ab4e04413ec1108ab4899758e4)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(5)) |
| #define | [VIM\_ACTIRQ\_VALID\_RESETVAL](#ad41b0eebaa403614473d6d91b3c54708)   (0x00000000U) |
| #define | [VIM\_ACTIRQ\_VALID\_MAX](#a8c0cf47b8dca0ed71e45a0d2cf791cf9)   (0x00000001U) |
| #define | [VIM\_ACTIRQ\_VALID\_VAL\_TRUE](#a67149d8156c8c49e50ffd974ff541be8)   (0x1U) |
| #define | [VIM\_ACTIRQ\_VALID\_VAL\_FALSE](#a4755bb481e7b635fb78a1ed1645fd65f)   (0x0U) |
| #define | [VIM\_ACTIRQ\_PRI\_MASK](#aa67330dfd1a07514b6aefb175688f6a2)   (0x000F0000U) |
| #define | [VIM\_ACTIRQ\_PRI\_SHIFT](#aa7f7b505e9f67ef073b27eecfd2e24dd)   (0x00000010U) |
| #define | [VIM\_ACTIRQ\_PRI\_RESETVAL](#a407ec18db62cdab6fc03e2e91d8f7a48)   (0x00000000U) |
| #define | [VIM\_ACTIRQ\_PRI\_MAX](#af5af969746c802c3fcc54624cc8fc1c5)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| #define | [VIM\_ACTIRQ\_NUM\_MASK](#af37fe4204363b131433c08e144b706c0)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| #define | [VIM\_ACTIRQ\_NUM\_SHIFT](#a1fb7025bd77510c4aa4735205a5e0119)   (0x00000000U) |
| #define | [VIM\_ACTIRQ\_NUM\_RESETVAL](#a891dc381e24ccef01b7ddc3004e68f72)   (0x00000000U) |
| #define | [VIM\_ACTIRQ\_NUM\_MAX](#ac1e4050ca8a6f725df77e3066fb75577)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| #define | [VIM\_ACTIRQ\_RESETVAL](#afe3be53299ab4dd7f158cb887d2a71af)   (0x00000000U) |
| #define | [VIM\_ACTFIQ\_VALID\_MASK](#a5f654648e1fceddc473017f5c69ebfde)   (0x80000000U) |
| #define | [VIM\_ACTFIQ\_VALID\_SHIFT](#a8891923ca180a27349b5ac4c50b75624)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(5)) |
| #define | [VIM\_ACTFIQ\_VALID\_RESETVAL](#adde70d87d3232e8cebd56058a0ba11c0)   (0x00000000U) |
| #define | [VIM\_ACTFIQ\_VALID\_MAX](#a4c3805e9372e278fa041f29b1cc79be0)   (0x00000001U) |
| #define | [VIM\_ACTFIQ\_VALID\_VAL\_TRUE](#a89a2a0626470f6d4efe41ea9790d6dfb)   (0x1U) |
| #define | [VIM\_ACTFIQ\_VALID\_VAL\_FALSE](#ad931b8267aa9895fb907f83b9bcab0a8)   (0x0U) |
| #define | [VIM\_ACTFIQ\_PRI\_MASK](#a53c9c40d87a7f364b61a6e2f626ec289)   (0x000F0000U) |
| #define | [VIM\_ACTFIQ\_PRI\_SHIFT](#afd741827c49d9ab22ef4982061e48867)   (0x00000010U) |
| #define | [VIM\_ACTFIQ\_PRI\_RESETVAL](#a51ccd75970e116bac2e1a35c6de1170f)   (0x00000000U) |
| #define | [VIM\_ACTFIQ\_PRI\_MAX](#a22d18ac005433d054a6a15dff39c6e68)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| #define | [VIM\_ACTFIQ\_NUM\_MASK](#a6245859896c6fcaf000ce56a04d30d5f)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| #define | [VIM\_ACTFIQ\_NUM\_SHIFT](#adc5bba8d5dd9a72a6db1b5ed51145159)   (0x00000000U) |
| #define | [VIM\_ACTFIQ\_NUM\_RESETVAL](#a09b7e2ffd6b9e526bb3088a421e5efc4)   (0x00000000U) |
| #define | [VIM\_ACTFIQ\_NUM\_MAX](#a6e1d51c6b92462e9789ba0dcc2d3bd53)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| #define | [VIM\_ACTFIQ\_RESETVAL](#a29431d2fd28113d56f66531593876580)   (0x00000000U) |
| #define | [VIM\_DEDVEC\_ADDR\_MASK](#a29b50c725ad2f701fb0c324f178579fb)   (0xFFFFFFFCU) |
| #define | [VIM\_DEDVEC\_ADDR\_SHIFT](#aa2d21a760a0307ad49b55880652ad2de)   (0x00000002U) |
| #define | [VIM\_DEDVEC\_ADDR\_RESETVAL](#a549218cf3d2c3031ad08a2c2cc0138b0)   (0x00000000U) |
| #define | [VIM\_DEDVEC\_ADDR\_MAX](#a4d3ae5e999ff96654cd472211788f203)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(30)) |
| #define | [VIM\_DEDVEC\_RESETVAL](#a8245d6946648411610d113a2c85a9e91)   (0x00000000U) |

## Macro Definition Documentation

## [◆ ](#a48bda38b33fc5dfc695dfdbe627f4984)VIM\_ACTFIQ

| #define VIM\_ACTFIQ   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0024) |
| --- |

## [◆ ](#a6245859896c6fcaf000ce56a04d30d5f)VIM\_ACTFIQ\_NUM\_MASK

| #define VIM\_ACTFIQ\_NUM\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| --- |

## [◆ ](#a6e1d51c6b92462e9789ba0dcc2d3bd53)VIM\_ACTFIQ\_NUM\_MAX

| #define VIM\_ACTFIQ\_NUM\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| --- |

## [◆ ](#a09b7e2ffd6b9e526bb3088a421e5efc4)VIM\_ACTFIQ\_NUM\_RESETVAL

| #define VIM\_ACTFIQ\_NUM\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#adc5bba8d5dd9a72a6db1b5ed51145159)VIM\_ACTFIQ\_NUM\_SHIFT

| #define VIM\_ACTFIQ\_NUM\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a53c9c40d87a7f364b61a6e2f626ec289)VIM\_ACTFIQ\_PRI\_MASK

| #define VIM\_ACTFIQ\_PRI\_MASK   (0x000F0000U) |
| --- |

## [◆ ](#a22d18ac005433d054a6a15dff39c6e68)VIM\_ACTFIQ\_PRI\_MAX

| #define VIM\_ACTFIQ\_PRI\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| --- |

## [◆ ](#a51ccd75970e116bac2e1a35c6de1170f)VIM\_ACTFIQ\_PRI\_RESETVAL

| #define VIM\_ACTFIQ\_PRI\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#afd741827c49d9ab22ef4982061e48867)VIM\_ACTFIQ\_PRI\_SHIFT

| #define VIM\_ACTFIQ\_PRI\_SHIFT   (0x00000010U) |
| --- |

## [◆ ](#a29431d2fd28113d56f66531593876580)VIM\_ACTFIQ\_RESETVAL

| #define VIM\_ACTFIQ\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a5f654648e1fceddc473017f5c69ebfde)VIM\_ACTFIQ\_VALID\_MASK

| #define VIM\_ACTFIQ\_VALID\_MASK   (0x80000000U) |
| --- |

## [◆ ](#a4c3805e9372e278fa041f29b1cc79be0)VIM\_ACTFIQ\_VALID\_MAX

| #define VIM\_ACTFIQ\_VALID\_MAX   (0x00000001U) |
| --- |

## [◆ ](#adde70d87d3232e8cebd56058a0ba11c0)VIM\_ACTFIQ\_VALID\_RESETVAL

| #define VIM\_ACTFIQ\_VALID\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a8891923ca180a27349b5ac4c50b75624)VIM\_ACTFIQ\_VALID\_SHIFT

| #define VIM\_ACTFIQ\_VALID\_SHIFT   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(5)) |
| --- |

## [◆ ](#ad931b8267aa9895fb907f83b9bcab0a8)VIM\_ACTFIQ\_VALID\_VAL\_FALSE

| #define VIM\_ACTFIQ\_VALID\_VAL\_FALSE   (0x0U) |
| --- |

## [◆ ](#a89a2a0626470f6d4efe41ea9790d6dfb)VIM\_ACTFIQ\_VALID\_VAL\_TRUE

| #define VIM\_ACTFIQ\_VALID\_VAL\_TRUE   (0x1U) |
| --- |

## [◆ ](#a814d881a2f50b7b47ab25084f59587f5)VIM\_ACTIRQ

| #define VIM\_ACTIRQ   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0020) |
| --- |

## [◆ ](#af37fe4204363b131433c08e144b706c0)VIM\_ACTIRQ\_NUM\_MASK

| #define VIM\_ACTIRQ\_NUM\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| --- |

## [◆ ](#ac1e4050ca8a6f725df77e3066fb75577)VIM\_ACTIRQ\_NUM\_MAX

| #define VIM\_ACTIRQ\_NUM\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| --- |

## [◆ ](#a891dc381e24ccef01b7ddc3004e68f72)VIM\_ACTIRQ\_NUM\_RESETVAL

| #define VIM\_ACTIRQ\_NUM\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a1fb7025bd77510c4aa4735205a5e0119)VIM\_ACTIRQ\_NUM\_SHIFT

| #define VIM\_ACTIRQ\_NUM\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#aa67330dfd1a07514b6aefb175688f6a2)VIM\_ACTIRQ\_PRI\_MASK

| #define VIM\_ACTIRQ\_PRI\_MASK   (0x000F0000U) |
| --- |

## [◆ ](#af5af969746c802c3fcc54624cc8fc1c5)VIM\_ACTIRQ\_PRI\_MAX

| #define VIM\_ACTIRQ\_PRI\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| --- |

## [◆ ](#a407ec18db62cdab6fc03e2e91d8f7a48)VIM\_ACTIRQ\_PRI\_RESETVAL

| #define VIM\_ACTIRQ\_PRI\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#aa7f7b505e9f67ef073b27eecfd2e24dd)VIM\_ACTIRQ\_PRI\_SHIFT

| #define VIM\_ACTIRQ\_PRI\_SHIFT   (0x00000010U) |
| --- |

## [◆ ](#afe3be53299ab4dd7f158cb887d2a71af)VIM\_ACTIRQ\_RESETVAL

| #define VIM\_ACTIRQ\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a9740e75023b8bf6ddc87f2aabc234a5c)VIM\_ACTIRQ\_VALID\_MASK

| #define VIM\_ACTIRQ\_VALID\_MASK   (0x80000000U) |
| --- |

## [◆ ](#a8c0cf47b8dca0ed71e45a0d2cf791cf9)VIM\_ACTIRQ\_VALID\_MAX

| #define VIM\_ACTIRQ\_VALID\_MAX   (0x00000001U) |
| --- |

## [◆ ](#ad41b0eebaa403614473d6d91b3c54708)VIM\_ACTIRQ\_VALID\_RESETVAL

| #define VIM\_ACTIRQ\_VALID\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#ab80c58ab4e04413ec1108ab4899758e4)VIM\_ACTIRQ\_VALID\_SHIFT

| #define VIM\_ACTIRQ\_VALID\_SHIFT   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(5)) |
| --- |

## [◆ ](#a4755bb481e7b635fb78a1ed1645fd65f)VIM\_ACTIRQ\_VALID\_VAL\_FALSE

| #define VIM\_ACTIRQ\_VALID\_VAL\_FALSE   (0x0U) |
| --- |

## [◆ ](#a67149d8156c8c49e50ffd974ff541be8)VIM\_ACTIRQ\_VALID\_VAL\_TRUE

| #define VIM\_ACTIRQ\_VALID\_VAL\_TRUE   (0x1U) |
| --- |

## [◆ ](#a6b442dccdb4e254cac43abd28c0a724d)VIM\_BASE\_ADDR

| #define VIM\_BASE\_ADDR   [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)([DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)(0, ti\_vim)) |
| --- |

## [◆ ](#ac77876e0bfdd3a9382e28728d9e2ebd3)VIM\_DEDVEC

| #define VIM\_DEDVEC   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0030) |
| --- |

## [◆ ](#a29b50c725ad2f701fb0c324f178579fb)VIM\_DEDVEC\_ADDR\_MASK

| #define VIM\_DEDVEC\_ADDR\_MASK   (0xFFFFFFFCU) |
| --- |

## [◆ ](#a4d3ae5e999ff96654cd472211788f203)VIM\_DEDVEC\_ADDR\_MAX

| #define VIM\_DEDVEC\_ADDR\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(30)) |
| --- |

## [◆ ](#a549218cf3d2c3031ad08a2c2cc0138b0)VIM\_DEDVEC\_ADDR\_RESETVAL

| #define VIM\_DEDVEC\_ADDR\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#aa2d21a760a0307ad49b55880652ad2de)VIM\_DEDVEC\_ADDR\_SHIFT

| #define VIM\_DEDVEC\_ADDR\_SHIFT   (0x00000002U) |
| --- |

## [◆ ](#a8245d6946648411610d113a2c85a9e91)VIM\_DEDVEC\_RESETVAL

| #define VIM\_DEDVEC\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a6c2b44a4cabf058542f9663f48d1bc07)VIM\_FIQGSTS

| #define VIM\_FIQGSTS   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0014) |
| --- |

## [◆ ](#ada89357c38ffaa43681b7e874aaddd6a)VIM\_FIQGSTS\_RESETVAL

| #define VIM\_FIQGSTS\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a4047a2f3c251c623a7bb4f03e2c80aa9)VIM\_FIQGSTS\_STS\_MASK

| #define VIM\_FIQGSTS\_STS\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a06d51cb097cedabe76ab25fb2336be2b)VIM\_FIQGSTS\_STS\_MAX

| #define VIM\_FIQGSTS\_STS\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#ac814862811ec1cf1d1e240c03fa5220a)VIM\_FIQGSTS\_STS\_RESETVAL

| #define VIM\_FIQGSTS\_STS\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a0cf8b2290a847eccb9206368c36d84d3)VIM\_FIQGSTS\_STS\_SHIFT

| #define VIM\_FIQGSTS\_STS\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#ac20f6ab045eb4c7193c94252d4ee26a5)VIM\_FIQSTS

| #define VIM\_FIQSTS | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + (0x414) + ((n) \* 0x20))

[VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)

#define VIM\_BASE\_ADDR

**Definition** intc\_vim.h:16

## [◆ ](#aba9caef8adb052c353f54679b95f4001)VIM\_FIQVEC

| #define VIM\_FIQVEC   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x001C) |
| --- |

## [◆ ](#a88ff3e766b092657a21fdf7ae2e93564)VIM\_FIQVEC\_ADDR\_MASK

| #define VIM\_FIQVEC\_ADDR\_MASK   (0xFFFFFFFCU) |
| --- |

## [◆ ](#a9e15f36e9494b3f69bbf49d962c38590)VIM\_FIQVEC\_ADDR\_MAX

| #define VIM\_FIQVEC\_ADDR\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(30)) |
| --- |

## [◆ ](#a5694973ce948cb75ec95b457b58544a5)VIM\_FIQVEC\_ADDR\_RESETVAL

| #define VIM\_FIQVEC\_ADDR\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a0db8828c7c1b359335220d80cf6fcb6f)VIM\_FIQVEC\_ADDR\_SHIFT

| #define VIM\_FIQVEC\_ADDR\_SHIFT   (0x00000002U) |
| --- |

## [◆ ](#a972fd2da90560b549d4eacc367643367)VIM\_FIQVEC\_RESETVAL

| #define VIM\_FIQVEC\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a765f1dd48172c22f4fb9cb5eb2c0ecfc)VIM\_GET\_IRQ\_BIT\_NUM

| #define VIM\_GET\_IRQ\_BIT\_NUM | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))((n) % [VIM\_MAX\_IRQ\_PER\_GROUP](#af3def9f38617688929e29eec9651c64b)))

[VIM\_MAX\_IRQ\_PER\_GROUP](#af3def9f38617688929e29eec9651c64b)

#define VIM\_MAX\_IRQ\_PER\_GROUP

**Definition** intc\_vim.h:18

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

## [◆ ](#a2bbbdbfa2a3dd00d1bd54d5c804220c1)VIM\_GET\_IRQ\_GROUP\_NUM

| #define VIM\_GET\_IRQ\_GROUP\_NUM | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))((n) / [VIM\_MAX\_IRQ\_PER\_GROUP](#af3def9f38617688929e29eec9651c64b)))

## [◆ ](#a374962357620f5b6ea7f3938158f52c9)VIM\_GRP\_FIQSTS\_MSK\_MASK

| #define VIM\_GRP\_FIQSTS\_MSK\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a7698addaef1b0850b538b508762da567)VIM\_GRP\_FIQSTS\_MSK\_MAX

| #define VIM\_GRP\_FIQSTS\_MSK\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a75f2aa2343da1e6f1577189911c685ce)VIM\_GRP\_FIQSTS\_MSK\_RESETVAL

| #define VIM\_GRP\_FIQSTS\_MSK\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a3b5c2839ef08c51d8163048023bec7bc)VIM\_GRP\_FIQSTS\_MSK\_SHIFT

| #define VIM\_GRP\_FIQSTS\_MSK\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#aff2481d09e0ed29c7206d28c098a0d14)VIM\_GRP\_FIQSTS\_RESETVAL

| #define VIM\_GRP\_FIQSTS\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a0259713478ab1f5930d1b303450d9b72)VIM\_GRP\_INTMAP\_MSK\_MASK

| #define VIM\_GRP\_INTMAP\_MSK\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#ad64d7f6045a420d2ed78f6bb0446294f)VIM\_GRP\_INTMAP\_MSK\_MAX

| #define VIM\_GRP\_INTMAP\_MSK\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#ac5d9e9e42d0c203c22a357ccec802c72)VIM\_GRP\_INTMAP\_MSK\_RESETVAL

| #define VIM\_GRP\_INTMAP\_MSK\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#aea4c913d99500c4b3cb1c60b5b514c2f)VIM\_GRP\_INTMAP\_MSK\_SHIFT

| #define VIM\_GRP\_INTMAP\_MSK\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a104e9c67c35b9656d451efbe5045cb78)VIM\_GRP\_INTMAP\_RESETVAL

| #define VIM\_GRP\_INTMAP\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a5b0397e530cdcc0ae4f88796a9ef86ef)VIM\_GRP\_INTR\_EN\_CLR\_MSK\_MASK

| #define VIM\_GRP\_INTR\_EN\_CLR\_MSK\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a1af7c911da646796d1091c4da9f45bf9)VIM\_GRP\_INTR\_EN\_CLR\_MSK\_MAX

| #define VIM\_GRP\_INTR\_EN\_CLR\_MSK\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a5617ad614b65e9341c5f9b4a3405fce6)VIM\_GRP\_INTR\_EN\_CLR\_MSK\_RESETVAL

| #define VIM\_GRP\_INTR\_EN\_CLR\_MSK\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#ae3fde9d57f6e6328a7f88f6889d91c3a)VIM\_GRP\_INTR\_EN\_CLR\_MSK\_SHIFT

| #define VIM\_GRP\_INTR\_EN\_CLR\_MSK\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a1113d705a90dd04e9af1999c37f9cb8e)VIM\_GRP\_INTR\_EN\_CLR\_RESETVAL

| #define VIM\_GRP\_INTR\_EN\_CLR\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a339c2737a2eb9180b78305a058b6aa90)VIM\_GRP\_INTR\_EN\_SET\_MSK\_MASK

| #define VIM\_GRP\_INTR\_EN\_SET\_MSK\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a61e07bf8b299223d8d4767aaa2e718b2)VIM\_GRP\_INTR\_EN\_SET\_MSK\_MAX

| #define VIM\_GRP\_INTR\_EN\_SET\_MSK\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a81eb2356267a972232177b893bc41fb7)VIM\_GRP\_INTR\_EN\_SET\_MSK\_RESETVAL

| #define VIM\_GRP\_INTR\_EN\_SET\_MSK\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a9c5eb8d20f8de659ca970cd69c4cd193)VIM\_GRP\_INTR\_EN\_SET\_MSK\_SHIFT

| #define VIM\_GRP\_INTR\_EN\_SET\_MSK\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a23b0f2ce857795c9e6c6faf35f124d02)VIM\_GRP\_INTR\_EN\_SET\_RESETVAL

| #define VIM\_GRP\_INTR\_EN\_SET\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a29cdb963486249ff8d87c1bf4ceeeb74)VIM\_GRP\_INTTYPE\_MSK\_MASK

| #define VIM\_GRP\_INTTYPE\_MSK\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a37f2063ecf4acdd91ab16a8941a9c51c)VIM\_GRP\_INTTYPE\_MSK\_MAX

| #define VIM\_GRP\_INTTYPE\_MSK\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a5d3443ac8213a8c02c364c9e6f37690c)VIM\_GRP\_INTTYPE\_MSK\_RESETVAL

| #define VIM\_GRP\_INTTYPE\_MSK\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a6c1cd189c9e5426b8a79b97b1f860753)VIM\_GRP\_INTTYPE\_MSK\_SHIFT

| #define VIM\_GRP\_INTTYPE\_MSK\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a35adc119bb4371fe8cf7070336935720)VIM\_GRP\_INTTYPE\_RESETVAL

| #define VIM\_GRP\_INTTYPE\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a13abe76418c094499d537b7fad5a171c)VIM\_GRP\_IRQSTS\_MSK\_MASK

| #define VIM\_GRP\_IRQSTS\_MSK\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#aa3a16c92d1f55aff8a9b750990a7daf1)VIM\_GRP\_IRQSTS\_MSK\_MAX

| #define VIM\_GRP\_IRQSTS\_MSK\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#ac4d5bf5d6ee09462f4254a12db2bad44)VIM\_GRP\_IRQSTS\_MSK\_RESETVAL

| #define VIM\_GRP\_IRQSTS\_MSK\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a24299da38556f543de8e12ff36a81d38)VIM\_GRP\_IRQSTS\_MSK\_SHIFT

| #define VIM\_GRP\_IRQSTS\_MSK\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a308a20f9e29c85ece314a6a005b6a4dd)VIM\_GRP\_IRQSTS\_RESETVAL

| #define VIM\_GRP\_IRQSTS\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a4817d3ad8ab3b557b19882b272d67d1b)VIM\_GRP\_RAW\_RESETVAL

| #define VIM\_GRP\_RAW\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#acd62766b3379b5baf178a33b6ff3d905)VIM\_GRP\_RAW\_STS\_MASK

| #define VIM\_GRP\_RAW\_STS\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a2842ee6521e5115eb85dd2b591aebd9b)VIM\_GRP\_RAW\_STS\_MAX

| #define VIM\_GRP\_RAW\_STS\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#aa82ed994598088a4a39bf628d78dc747)VIM\_GRP\_RAW\_STS\_RESETVAL

| #define VIM\_GRP\_RAW\_STS\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#ad28eafc29daa6e59de34e62f1493cfca)VIM\_GRP\_RAW\_STS\_SHIFT

| #define VIM\_GRP\_RAW\_STS\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a7f4d55def9ac847ff1c2f6739f09a636)VIM\_GRP\_STS\_MSK\_MASK

| #define VIM\_GRP\_STS\_MSK\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a1c452655a919216d7ba809d96e1b0287)VIM\_GRP\_STS\_MSK\_MAX

| #define VIM\_GRP\_STS\_MSK\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#aec03c90df4149318acb41f1feacd4392)VIM\_GRP\_STS\_MSK\_RESETVAL

| #define VIM\_GRP\_STS\_MSK\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a79f980ac35a193b154853fd35aa8bcaf)VIM\_GRP\_STS\_MSK\_SHIFT

| #define VIM\_GRP\_STS\_MSK\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a229308ab7f2cd16ce15cbe0dd8c0197b)VIM\_GRP\_STS\_RESETVAL

| #define VIM\_GRP\_STS\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#adf312872ea552e35a0e9fed4ef69ae11)VIM\_INFO

| #define VIM\_INFO   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0004) |
| --- |

## [◆ ](#adeba4e94c9d68665820fd13483d24b85)VIM\_INFO\_INTERRUPTS\_MASK

| #define VIM\_INFO\_INTERRUPTS\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(11)) |
| --- |

## [◆ ](#aca715ba5a23516302a6c1a648fbbdeea)VIM\_INFO\_INTERRUPTS\_MAX

| #define VIM\_INFO\_INTERRUPTS\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(11)) |
| --- |

## [◆ ](#ad37820d3013c0ed4867a7235ee16444f)VIM\_INFO\_INTERRUPTS\_RESETVAL

| #define VIM\_INFO\_INTERRUPTS\_RESETVAL   (0x00000400U) |
| --- |

## [◆ ](#ace1cb4b9d2de191575a9bba21882a025)VIM\_INFO\_INTERRUPTS\_SHIFT

| #define VIM\_INFO\_INTERRUPTS\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a3fc8c50f54bc3a158dbfef51fb96ee5b)VIM\_INFO\_RESETVAL

| #define VIM\_INFO\_RESETVAL   (0x00000400U) |
| --- |

## [◆ ](#adbf1801e1f7dfa45f19f20e91ccbf1e2)VIM\_INTMAP

| #define VIM\_INTMAP | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + (0x418) + ((n) \* 0x20))

## [◆ ](#a313eefa1e7b90c3988c8d15c1dfb2aae)VIM\_INTR\_EN\_CLR

| #define VIM\_INTR\_EN\_CLR | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + (0x40c) + ((n) \* 0x20))

## [◆ ](#a0d2b404f0483d09a32b6a4914cd660ef)VIM\_INTR\_EN\_SET

| #define VIM\_INTR\_EN\_SET | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + (0x408) + ((n) \* 0x20))

## [◆ ](#a28965b8d5ed95f9bd0322e95d41aa65c)VIM\_INTTYPE

| #define VIM\_INTTYPE | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + (0x41c) + ((n) \* 0x20))

## [◆ ](#a7bcbdd8241d466014361b13baf43d81b)VIM\_IRQGSTS

| #define VIM\_IRQGSTS   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0010) |
| --- |

## [◆ ](#a674113c74daca28dc3a3777cf2a33917)VIM\_IRQGSTS\_RESETVAL

| #define VIM\_IRQGSTS\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a4497e08f4d565ace708e50c84f0f51b6)VIM\_IRQGSTS\_STS\_MASK

| #define VIM\_IRQGSTS\_STS\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#a82828e470cbcd1df782ed463c61ecfee)VIM\_IRQGSTS\_STS\_MAX

| #define VIM\_IRQGSTS\_STS\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(32)) |
| --- |

## [◆ ](#af7d810589915de14ab7cff616fdb0b5f)VIM\_IRQGSTS\_STS\_RESETVAL

| #define VIM\_IRQGSTS\_STS\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a03180f0120311298a518f8f109fa2dee)VIM\_IRQGSTS\_STS\_SHIFT

| #define VIM\_IRQGSTS\_STS\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a6a07b16389503e1131e9b46e84545c4e)VIM\_IRQSTS

| #define VIM\_IRQSTS | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + (0x410) + ((n) \* 0x20))

## [◆ ](#a893a5e8467a3e5417272dedc098e42b5)VIM\_IRQVEC

| #define VIM\_IRQVEC   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0018) |
| --- |

## [◆ ](#a854706bcbaeb0764d2dac7a325734b20)VIM\_IRQVEC\_ADDR\_MASK

| #define VIM\_IRQVEC\_ADDR\_MASK   (0xFFFFFFFCU) |
| --- |

## [◆ ](#abb959b8bcc866cc955ae998ae62a2feb)VIM\_IRQVEC\_ADDR\_MAX

| #define VIM\_IRQVEC\_ADDR\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(30)) |
| --- |

## [◆ ](#ad0643477818df3a01ec0aad56be04cb1)VIM\_IRQVEC\_ADDR\_RESETVAL

| #define VIM\_IRQVEC\_ADDR\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a692248d3c771837c934b2057573511f7)VIM\_IRQVEC\_ADDR\_SHIFT

| #define VIM\_IRQVEC\_ADDR\_SHIFT   (0x00000002U) |
| --- |

## [◆ ](#a5c92254c2655c9a73f13eba43e50a398)VIM\_IRQVEC\_RESETVAL

| #define VIM\_IRQVEC\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a2520b3f68146858942723fe295c0dae4)VIM\_MAX\_GROUP\_NUM

| #define VIM\_MAX\_GROUP\_NUM   (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))([CONFIG\_NUM\_IRQS](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837) / [VIM\_MAX\_IRQ\_PER\_GROUP](#af3def9f38617688929e29eec9651c64b))) |
| --- |

## [◆ ](#af3def9f38617688929e29eec9651c64b)VIM\_MAX\_IRQ\_PER\_GROUP

| #define VIM\_MAX\_IRQ\_PER\_GROUP   (32) |
| --- |

## [◆ ](#a378ef153f705928fff529e02838d50af)VIM\_PID

| #define VIM\_PID   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0000) |
| --- |

## [◆ ](#ad7c36f8650ff847544a550a31235193b)VIM\_PRI\_INT

| #define VIM\_PRI\_INT | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + (0x1000) + ((n) \* 0x4))

## [◆ ](#aba7671d7f7dee14d87f7feff8a3451f7)VIM\_PRI\_INT\_MAX

| #define VIM\_PRI\_INT\_MAX   (15) |
| --- |

## [◆ ](#a72fa57b55ef32e7c7db63932c28d65da)VIM\_PRI\_INT\_RESETVAL

| #define VIM\_PRI\_INT\_RESETVAL   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| --- |

## [◆ ](#a996fc01313c3b05b298f32b7691a0ba1)VIM\_PRI\_INT\_VAL\_MASK

| #define VIM\_PRI\_INT\_VAL\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| --- |

## [◆ ](#af8297a7ca4b4b0cddb3703312fb858bb)VIM\_PRI\_INT\_VAL\_MAX

| #define VIM\_PRI\_INT\_VAL\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| --- |

## [◆ ](#a413968f03758ca53b005bfe7c5e3023b)VIM\_PRI\_INT\_VAL\_RESETVAL

| #define VIM\_PRI\_INT\_VAL\_RESETVAL   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| --- |

## [◆ ](#ad9d91c69c20c243578aea8028d4635a2)VIM\_PRI\_INT\_VAL\_SHIFT

| #define VIM\_PRI\_INT\_VAL\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a17ea1cd9d06d003bbc094bffbefb47c4)VIM\_PRIFIQ

| #define VIM\_PRIFIQ   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x000C) |
| --- |

## [◆ ](#aad509ed553a5e15f893390481ac739fa)VIM\_PRIFIQ\_NUM\_MASK

| #define VIM\_PRIFIQ\_NUM\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| --- |

## [◆ ](#ac27797438659455e527d82e9fb586b5a)VIM\_PRIFIQ\_NUM\_MAX

| #define VIM\_PRIFIQ\_NUM\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| --- |

## [◆ ](#a608c0a95598b701c377351bdab275df4)VIM\_PRIFIQ\_NUM\_RESETVAL

| #define VIM\_PRIFIQ\_NUM\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#af8b15089bdd21a468168c1d5e8fc7dad)VIM\_PRIFIQ\_NUM\_SHIFT

| #define VIM\_PRIFIQ\_NUM\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#a6de77b9058d6b58314097adebe045a86)VIM\_PRIFIQ\_PRI\_MASK

| #define VIM\_PRIFIQ\_PRI\_MASK   (0x000F0000U) |
| --- |

## [◆ ](#a67922050c7eb81575c1b7b1e227b6839)VIM\_PRIFIQ\_PRI\_MAX

| #define VIM\_PRIFIQ\_PRI\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| --- |

## [◆ ](#aa810609b09640d548c56bdfb09b9868c)VIM\_PRIFIQ\_PRI\_RESETVAL

| #define VIM\_PRIFIQ\_PRI\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a3d61188f8ce9b07ac1bcb708c0a28619)VIM\_PRIFIQ\_PRI\_SHIFT

| #define VIM\_PRIFIQ\_PRI\_SHIFT   (0x00000010U) |
| --- |

## [◆ ](#adf127d9e139beb74e65b88741d82013a)VIM\_PRIFIQ\_RESETVAL

| #define VIM\_PRIFIQ\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#aba90d57af70816d9b58dc8851f6da004)VIM\_PRIFIQ\_VALID\_MASK

| #define VIM\_PRIFIQ\_VALID\_MASK   (0x80000000U) |
| --- |

## [◆ ](#ac8173b6b098e38ea9eebbf79e8f8a1da)VIM\_PRIFIQ\_VALID\_MAX

| #define VIM\_PRIFIQ\_VALID\_MAX   (0x00000001U) |
| --- |

## [◆ ](#a322fe75f392fb162f1c04330990ed2d7)VIM\_PRIFIQ\_VALID\_RESETVAL

| #define VIM\_PRIFIQ\_VALID\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a3c93252a9eae445243cd8a9c39d79f82)VIM\_PRIFIQ\_VALID\_SHIFT

| #define VIM\_PRIFIQ\_VALID\_SHIFT   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(5)) |
| --- |

## [◆ ](#a6bdf3d9847f3ccad759874bb5b09cfb4)VIM\_PRIFIQ\_VALID\_VAL\_FALSE

| #define VIM\_PRIFIQ\_VALID\_VAL\_FALSE   (0x0U) |
| --- |

## [◆ ](#ac5ced3000f18ecfc7fc5ea07e3473f78)VIM\_PRIFIQ\_VALID\_VAL\_TRUE

| #define VIM\_PRIFIQ\_VALID\_VAL\_TRUE   (0x1U) |
| --- |

## [◆ ](#ab4ee6967e7149c07a2690978e7a2f97b)VIM\_PRIIRQ

| #define VIM\_PRIIRQ   ([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + 0x0008) |
| --- |

## [◆ ](#a236930837a36a72e4b29f81175537543)VIM\_PRIIRQ\_NUM\_MASK

| #define VIM\_PRIIRQ\_NUM\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| --- |

## [◆ ](#a610e6f20d550a0cc5e90f31f7ce9f065)VIM\_PRIIRQ\_NUM\_MAX

| #define VIM\_PRIIRQ\_NUM\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(10)) |
| --- |

## [◆ ](#a4376b256f168336b45108b8255a0f92f)VIM\_PRIIRQ\_NUM\_RESETVAL

| #define VIM\_PRIIRQ\_NUM\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#ac7956ab58b6223b8e511892ff35d9375)VIM\_PRIIRQ\_NUM\_SHIFT

| #define VIM\_PRIIRQ\_NUM\_SHIFT   (0x00000000U) |
| --- |

## [◆ ](#ad952cdc46228507194a3b19baf6d71e7)VIM\_PRIIRQ\_PRI\_MASK

| #define VIM\_PRIIRQ\_PRI\_MASK   (0x000F0000U) |
| --- |

## [◆ ](#ac3f1624d169a99edb836f3a3ba82acfa)VIM\_PRIIRQ\_PRI\_MAX

| #define VIM\_PRIIRQ\_PRI\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4)) |
| --- |

## [◆ ](#a810037874c898a7c0f738096406b9148)VIM\_PRIIRQ\_PRI\_RESETVAL

| #define VIM\_PRIIRQ\_PRI\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a31ed4fa3d085d39863d0da6b657ca0df)VIM\_PRIIRQ\_PRI\_SHIFT

| #define VIM\_PRIIRQ\_PRI\_SHIFT   (0x00000010U) |
| --- |

## [◆ ](#a13826544f2e9cd4ce4164b62d8e82d7e)VIM\_PRIIRQ\_RESETVAL

| #define VIM\_PRIIRQ\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a4d4d0d285eabeccb6418c442a7b3453b)VIM\_PRIIRQ\_VALID\_MASK

| #define VIM\_PRIIRQ\_VALID\_MASK   (0x80000000U) |
| --- |

## [◆ ](#aacbd1281fb54586fa48c6ed3d49d62cd)VIM\_PRIIRQ\_VALID\_MAX

| #define VIM\_PRIIRQ\_VALID\_MAX   (0x00000001U) |
| --- |

## [◆ ](#a7026e741d660e4d893ac1457c12ef827)VIM\_PRIIRQ\_VALID\_RESETVAL

| #define VIM\_PRIIRQ\_VALID\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#acaca01cbd74088f455f8345472424339)VIM\_PRIIRQ\_VALID\_SHIFT

| #define VIM\_PRIIRQ\_VALID\_SHIFT   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(5)) |
| --- |

## [◆ ](#a0966b95628413d1efdf9e572783865bd)VIM\_PRIIRQ\_VALID\_VAL\_FALSE

| #define VIM\_PRIIRQ\_VALID\_VAL\_FALSE   (0x0U) |
| --- |

## [◆ ](#adc2729dd6329da29bac1ac4942003f7d)VIM\_PRIIRQ\_VALID\_VAL\_TRUE

| #define VIM\_PRIIRQ\_VALID\_VAL\_TRUE   (0x1U) |
| --- |

## [◆ ](#a0b86c01e8e3844c71a74380c2392a847)VIM\_RAW

| #define VIM\_RAW | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + (0x400) + ((n) \* 0x20))

## [◆ ](#ae714f8162f5840ab2eb655d48c92ac99)VIM\_STS

| #define VIM\_STS | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + (0x404) + ((n) \* 0x20))

## [◆ ](#abb38d6437a3f25c193c2506fe97cf89c)VIM\_VEC\_INT

| #define VIM\_VEC\_INT | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([VIM\_BASE\_ADDR](#a6b442dccdb4e254cac43abd28c0a724d) + (0x2000) + ((n) \* 0x4))

## [◆ ](#a16bd2873cba17ebd29acd3aeb58b2df4)VIM\_VEC\_INT\_RESETVAL

| #define VIM\_VEC\_INT\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a8076a54316cec3fc0de52079bd4cd598)VIM\_VEC\_INT\_VAL\_MASK

| #define VIM\_VEC\_INT\_VAL\_MASK   (0xFFFFFFFCU) |
| --- |

## [◆ ](#a769edf746fb1ef704f85bfdee55fb136)VIM\_VEC\_INT\_VAL\_MAX

| #define VIM\_VEC\_INT\_VAL\_MAX   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(30)) |
| --- |

## [◆ ](#a3dd1401816579e5d07876b87b34e2177)VIM\_VEC\_INT\_VAL\_RESETVAL

| #define VIM\_VEC\_INT\_VAL\_RESETVAL   (0x00000000U) |
| --- |

## [◆ ](#a3024d3c80cdc3db66954fa83541ca389)VIM\_VEC\_INT\_VAL\_SHIFT

| #define VIM\_VEC\_INT\_VAL\_SHIFT   (0x00000002U) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_vim.h](intc__vim_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
