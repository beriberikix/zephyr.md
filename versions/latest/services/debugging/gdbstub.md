---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/debugging/gdbstub.html
original_path: services/debugging/gdbstub.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# GDB stub

## [Overview](#id2)

The gdbstub feature provides an implementation of the GDB Remote
Serial Protocol (RSP) that allows you to remotely debug Zephyr
using GDB.

The protocol supports different connection types: serial, UDP/IP and
TCP/IP. Zephyr currently supports only serial device communication.

The GDB program acts as the client while Zephyr acts as the
server. When this feature is enabled, Zephyr stops its execution after
`gdb_init()` starts gdbstub service and waits for a GDB
connection. Once a connection is established it is possible to
synchronously interact with Zephyr. Note that currently it is not
possible to asynchronously send commands to the target.

## [Features](#id3)

The following features are supported:

- Add and remove breakpoints
- Continue and step the target
- Print backtrace
- Read or write general registers
- Read or write the memory

## [Enabling GDB Stub](#id4)

GDB stub can be enabled with the [`CONFIG_GDBSTUB`](../../kconfig.md#CONFIG_GDBSTUB "CONFIG_GDBSTUB") option.

### [Using Serial Backend](#id5)

The serial backend for GDB stub can be enabled with
the [`CONFIG_GDBSTUB_SERIAL_BACKEND`](../../kconfig.md#CONFIG_GDBSTUB_SERIAL_BACKEND "CONFIG_GDBSTUB_SERIAL_BACKEND") option.

Since serial backend utilizes UART devices to send and receive GDB commands,

- If there are spare UART devices on the board, set `zephyr,gdbstub-uart`
  property of the chosen node to the spare UART device so that `printk()`
  and log messages are not being printed to the same UART device used for GDB.
- For boards with only one UART device, `printk()` and logging
  must be disabled if they are also using the same UART device for output.
  GDB related messages may interleave with log messages which may have
  unintended consequences. Usually this can be done by disabling
  [`CONFIG_PRINTK`](../../kconfig.md#CONFIG_PRINTK "CONFIG_PRINTK") and [`CONFIG_LOG`](../../kconfig.md#CONFIG_LOG "CONFIG_LOG").

## [Debugging](#id6)

### [Using Serial Backend](#id7)

1. Build with GDB stub and serial backend enabled.
2. Flash built image onto board and reset the board.

   - Execution should now be paused at `gdb_init()`.
3. Execute GDB on development machine and connect to the GDB stub.

   ```shell
   target remote <serial device>
   ```

   For example,

   ```shell
   target remote /dev/ttyUSB1
   ```
4. GDB commands can be used to start debugging.

## [Example](#id8)

This is an example to demonstrate how GDB stub works.
You can also refer to `tests/subsys/debug/gdbstub`
for its implementation as a Twister test.

1. Open two terminal windows.
2. On the first terminal, build and run the sample:

   ```shell
   # From the root of the zephyr repository
   west build -b qemu_x86 samples/subsys/debug/gdbstub
   west build -t run
   ```
3. On the second terminal, start GDB:

   ```shell
   <SDK install directory>/x86_64-zephyr-elf/bin/x86_64-zephyr-elf-gdb
   ```

   1. Tell GDB where to look for the built ELF file:

      ```text
      (gdb) file <build directory>/zephyr/zephyr.elf
      ```

      Response from GDB:

      ```text
      Reading symbols from <build directory>/zephyr/zephyr.elf...
      ```
   2. Tell GDB to connect to the server:

      ```text
      (gdb) target remote localhost:5678
      ```

      Note that QEMU is setup to redirect the serial used for GDB stub in
      the Zephyr image to a networking port. Hence the connection to
      localhost, port 5678.

      Response from GDB:

      ```text
      Remote debugging using :5678
      arch_gdb_init () at <ZEPHYR_BASE>/arch/x86/core/ia32/gdbstub.c:232
      232     }
      ```

      GDB also shows where the code execution is stopped. In this case,
      it is at `arch/x86/core/ia32/gdbstub.c`, line 232.
   3. Use command `bt` or `backtrace` to show the backtrace of stack frames.

      ```text
      (gdb) bt
      #0  arch_gdb_init () at <ZEPHYR_BASE>/arch/x86/core/ia32/gdbstub.c:232
      #1  0x00105068 in gdb_init (arg=0x0) at <ZEPHYR_BASE>/subsys/debug/gdbstub.c:833
      #2  0x00109d6f in z_sys_init_run_level (level=0x1) at <ZEPHYR_BASE>/kernel/device.c:72
      #3  0x0010a40b in z_cstart () at <ZEPHYR_BASE>/kernel/init.c:423
      #4  0x00105383 in z_prep_c (arg=0x9500) at <ZEPHYR_BASE>/arch/x86/core/prep_c.c:58
      #5  0x001000a9 in __csSet () at <ZEPHYR_BASE>/arch/x86/core/ia32/crt0.S:273
      ```
   4. Use command `list` to show the source code and surroundings where
      code execution is stopped.

      ```text
      (gdb) list
      227     }
      228
      229     void arch_gdb_init(void)
      230     {
      231             __asm__ volatile ("int3");
      232     }
      233
      234     /* Hook current IDT. */
      235     _EXCEPTION_CONNECT_NOCODE(z_gdb_debug_isr, IV_DEBUG, 3);
      236     _EXCEPTION_CONNECT_NOCODE(z_gdb_break_isr, IV_BREAKPOINT, 3);
      ```
   5. Use command `s` or `step` to step through program until it reaches
      a different source line. Now that it finished executing [`arch_gdb_init()`](../../hardware/porting/arch.md#c.arch_gdb_init "arch_gdb_init")
      and is continuing in `gdb_init()`.

      ```text
      (gdb) s
      gdb_init (arg=0x0) at /home/dleung5/zephyr/rtos/zephyr/subsys/debug/gdbstub.c:834
      834     return 0;
      ```

      ```text
      (gdb) list
      829                     LOG_ERR("Could not initialize gdbstub backend.");
      830                     return -1;
      831             }
      832
      833             arch_gdb_init();
      834             return 0;
      835     }
      836
      837     #ifdef CONFIG_XTENSA
      838     /*
      ```
   6. Use command `br` or `break` to setup a breakpoint. This example
      sets up a breakpoint at `main()`, and let code execution continue
      without any intervention using command `c` (or `continue`).

      ```text
      (gdb) break main
      Breakpoint 1 at 0x1005a9: file <ZEPHYR_BASE>/samples/subsys/debug/gdbstub/src/main.c, line 32.
      (gdb) continue
      Continuing.
      ```

      Once code execution reaches `main()`, execution will be stopped
      and GDB prompt returns.

      ```text
      Breakpoint 1, main () at <ZEPHYR_BASE>/samples/subsys/debug/gdbstub/src/main.c:32
      32           ret = test();
      ```

      Now GDB is waiting at the beginning of `main()`:

      ```text
      (gdb) list
      27
      28     int main(void)
      29     {
      30             int ret;
      31
      32             ret = test();
      33             printk("%d\n", ret);
      34     }
      35
      36     K_THREAD_DEFINE(thread, STACKSIZE, thread_entry, NULL, NULL, NULL,
      ```
   7. To examine the value of `ret`, the command `p` or `print`
      can be used.

      ```text
      (gdb) p ret
      $1 = 0x11318c
      ```

      Since `ret` has not been assigned a value yet, what it contains is
      simply a random value.
   8. If step (`s` or `step`) is used here, it will continue execution
      until `printk()` is reached, thus skipping the interior of
      `test()`. To examine code execution inside `test()`,
      a breakpoint can be set for `test()`, or simply using
      `si` (or `stepi`) to execute one machine instruction, where it has
      the side effect of going into the function.

      ```text
      (gdb) si
      test () at <ZEPHYR_BASE>/samples/subsys/debug/gdbstub/src/main.c:13
      13     {
      (gdb) list
      8      #include <zephyr/sys/printk.h>
      9
      10     #define STACKSIZE 512
      11
      12     static int test(void)
      13     {
      14             int a;
      15             int b;
      16
      17             a = 10;
      ```
   9. Here, `step` can be used to go through all code inside `test()`
      until it returns. Or the command `finish` can be used to continue
      execution without intervention until the function returns.

      ```text
      (gdb) finish
      Run till exit from #0  test () at <ZEPHYR_BASE>/samples/subsys/debug/gdbstub/src/main.c:13
      0x001005ae in main () at <ZEPHYR_BASE>/samples/subsys/debug/gdbstub/src/main.c:32
      32             ret = test();
      Value returned is $2 = 0x1e
      ```

      And now, execution is back to `main()`.
   10. Examine `ret` again which should have the return value from
       `test()`. Sometimes, the assignment is not done until another
       `step` is issued, as in this case. This is due to the assignment
       code is done after returning from function. The assignment code is
       generated by the toolchain as machine instructions which are not
       visible when viewing the corresponding C source file.

       ```text
       (gdb) p ret
       $3 = 0x11318c
       (gdb) s
       33              printk("%d\n", ret);
       (gdb) p ret
       $4 = 0x1e
       ```
   11. If `continue` is issued here, code execution will continue indefinitely
       as there are no breakpoints to further stop execution. Breaking execution
       in GDB via Ctrl-C does not currently work as the GDB stub does not
       support this functionality (yet).
