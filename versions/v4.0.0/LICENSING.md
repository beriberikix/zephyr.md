---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/LICENSING.html
original_path: LICENSING.html
---

# Licensing of Zephyr Project components

The Zephyr kernel tree imports or reuses packages, scripts and other files that
are not covered by the [Apache 2.0 License](https://github.com/zephyrproject-rtos/zephyr/blob/main/LICENSE). In some places
there is no LICENSE file or way to put a LICENSE file there, so we describe the
licensing in this document.

*scripts/{checkpatch.pl,checkstack.pl,spelling.txt}*
:   *Origin:* Linux Kernel

    *Licensing:* [GPLv2 License](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/COPYING)

*scripts/{coccicheck,coccinelle/array\_size.cocci,coccinelle/deref\_null.cocci,coccinelle/deref\_null.cocci,coccinelle/deref\_null.cocci,coccinelle/mini\_lock.cocci,coccinelle/mini\_lock.cocci,coccinelle/mini\_lock.cocci,coccinelle/noderef.cocci,coccinelle/noderef.cocci,coccinelle/returnvar.cocci,coccinelle/semicolon.cocci}*
:   *Origin:* Coccinelle

    *Licensing:* [GPLv2 License](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/COPYING)

*subsys/testsuite/coverage/coverage.h*
:   *Origin:* GCC, the GNU Compiler Collection

    *Licensing:* [GPLv2 License](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/COPYING) with Runtime Library Exception

*boards/ene/kb1200\_evb/support/openocd.cfg*
:   *Licensing:* [GPLv2 License](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/plain/COPYING)
