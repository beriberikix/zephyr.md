---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gnttab_8h_source.html
original_path: doxygen/html/gnttab_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnttab.h

[Go to the documentation of this file.](gnttab_8h.md)

1/\*

2 \* Copyright (c) 2021-2022 EPAM Systems

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef \_\_XEN\_GNTTAB\_H\_\_

7#define \_\_XEN\_GNTTAB\_H\_\_

8

9#include <[zephyr/xen/public/grant\_table.h](grant__table_8h.md)>

10

11/\*

12 \* Assigns gref and permits access to 4K page for specific domain.

13 \*

14 \* @param domid - id of the domain you sharing gref with

15 \* @param gfn - guest frame number of page, where grant will be located

16 \* @param readonly - permit readonly access to shared grant

17 \* @return - gref assigned to shared grant

18 \*/

[ 19](gnttab_8h.md#aa36d64f2cd70dedabc2c7a67ddb497a9)[grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e) [gnttab\_grant\_access](gnttab_8h.md#aa36d64f2cd70dedabc2c7a67ddb497a9)([domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) domid, unsigned long gfn,

20 bool readonly);

21

22/\*

23 \* Finished access for previously shared grant. Does NOT

24 \* free memory, if it was previously allocated by

25 \* gnttab\_alloc\_and\_grant().

26 \*

27 \* @param gref - grant reference that need to be closed

28 \* @return - zero on success, non-zero on failure

29 \*/

[ 30](gnttab_8h.md#a16013267f3a28da2b672e9d8961b0d9d)int [gnttab\_end\_access](gnttab_8h.md#a16013267f3a28da2b672e9d8961b0d9d)([grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e) gref);

31

32/\*

33 \* Allocates 4K page for grant and share it via returned

34 \* gref. Need to k\_free memory, which was allocated in

35 \* @map parameter after grant releasing.

36 \*

37 \* @param map - double pointer to memory, where grant will be allocated

38 \* @param readonly - permit readonly access to allocated grant

39 \* @return - grant ref on success or negative errno on failure

40 \*/

[ 41](gnttab_8h.md#afedf9bc092852f2fd9f7461b89482634)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [gnttab\_alloc\_and\_grant](gnttab_8h.md#afedf9bc092852f2fd9f7461b89482634)(void \*\*map, bool readonly);

42

43/\*

44 \* Provides interface to acquire free page, that can be used for

45 \* mapping of foreign frames. Should be freed by gnttab\_put\_page()

46 \* after usage.

47 \*

48 \* @return - pointer to page start address, that can be used as host\_addr

49 \* in struct gnttab\_map\_grant\_ref, NULL on error.

50 \*/

[ 51](gnttab_8h.md#a920eb0f010b62517d0eabd46c0b6becc)void \*[gnttab\_get\_page](gnttab_8h.md#a920eb0f010b62517d0eabd46c0b6becc)(void);

52

53/\*

54 \* Releases provided page, that was used for mapping foreign grant frame,

55 \* should be called after unmaping.

56 \*

57 \* @param page\_addr - pointer to start address of used page.

58 \*/

[ 59](gnttab_8h.md#a3f354536f151d40ee0732b880f775bb5)void [gnttab\_put\_page](gnttab_8h.md#a3f354536f151d40ee0732b880f775bb5)(void \*page\_addr);

60

61/\*

62 \* Maps foreign grant ref to Zephyr address space.

63 \*

64 \* @param map\_ops - array of prepared gnttab\_map\_grant\_ref's for mapping

65 \* @param count - number of grefs in map\_ops array

66 \* @return - zero on success or negative errno on failure

67 \* also per-page status will be set in map\_ops[i].status (GNTST\_\*)

68 \*

69 \* To map foreign frame you need 4K-aligned 4K memory page, which will be

70 \* used as host\_addr for grant mapping - it should be acquired by gnttab\_get\_page()

71 \* function.

72 \*/

[ 73](gnttab_8h.md#a64d478848b93048af3e7de5474cc3c0b)int [gnttab\_map\_refs](gnttab_8h.md#a64d478848b93048af3e7de5474cc3c0b)(struct [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md) \*map\_ops, unsigned int count);

74

75/\*

76 \* Unmap foreign grant refs. The gnttab\_put\_page() should be used after this for

77 \* each page, that was successfully unmapped.

78 \*

79 \* @param unmap\_ops - array of prepared gnttab\_map\_grant\_ref's for unmapping

80 \* @param count - number of grefs in unmap\_ops array

81 \* @return - @count on success or negative errno on failure

82 \* also per-page status will be set in unmap\_ops[i].status (GNTST\_\*)

83 \*/

[ 84](gnttab_8h.md#a00a2b9fd5f480b3943d9c0ec164c7fed)int [gnttab\_unmap\_refs](gnttab_8h.md#a00a2b9fd5f480b3943d9c0ec164c7fed)(struct [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md) \*unmap\_ops, unsigned int count);

85

86/\*

87 \* Convert grant ref status codes (GNTST\_\*) to text messages.

88 \*

89 \* @param status - negative GNTST\_\* code, that needs to be converted

90 \* @return - constant pointer to text message, associated with @status

91 \*/

[ 92](gnttab_8h.md#afe3ff541ac6015e39922f34940154724)const char \*[gnttabop\_error](gnttab_8h.md#afe3ff541ac6015e39922f34940154724)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) status);

93

94#endif /\* \_\_XEN\_GNTTAB\_H\_\_ \*/

[gnttab\_unmap\_refs](gnttab_8h.md#a00a2b9fd5f480b3943d9c0ec164c7fed)

int gnttab\_unmap\_refs(struct gnttab\_map\_grant\_ref \*unmap\_ops, unsigned int count)

[gnttab\_end\_access](gnttab_8h.md#a16013267f3a28da2b672e9d8961b0d9d)

int gnttab\_end\_access(grant\_ref\_t gref)

[gnttab\_put\_page](gnttab_8h.md#a3f354536f151d40ee0732b880f775bb5)

void gnttab\_put\_page(void \*page\_addr)

[gnttab\_map\_refs](gnttab_8h.md#a64d478848b93048af3e7de5474cc3c0b)

int gnttab\_map\_refs(struct gnttab\_map\_grant\_ref \*map\_ops, unsigned int count)

[gnttab\_get\_page](gnttab_8h.md#a920eb0f010b62517d0eabd46c0b6becc)

void \* gnttab\_get\_page(void)

[gnttab\_grant\_access](gnttab_8h.md#aa36d64f2cd70dedabc2c7a67ddb497a9)

grant\_ref\_t gnttab\_grant\_access(domid\_t domid, unsigned long gfn, bool readonly)

[gnttabop\_error](gnttab_8h.md#afe3ff541ac6015e39922f34940154724)

const char \* gnttabop\_error(int16\_t status)

[gnttab\_alloc\_and\_grant](gnttab_8h.md#afedf9bc092852f2fd9f7461b89482634)

int32\_t gnttab\_alloc\_and\_grant(void \*\*map, bool readonly)

[grant\_table.h](grant__table_8h.md)

[grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e)

uint32\_t grant\_ref\_t

**Definition** grant\_table.h:116

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md)

**Definition** grant\_table.h:266

[domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)

uint16\_t domid\_t

**Definition** xen.h:217

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [gnttab.h](gnttab_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
