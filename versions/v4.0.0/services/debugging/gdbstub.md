---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/debugging/gdbstub.html
original_path: services/debugging/gdbstub.html
---

# GDB stub

## [Overview](#id2)

The gdbstub feature provides an implementation of the GDB Remote
Serial Protocol (RSP) that allows you to remotely debug Zephyr
using GDB.

The protocol supports different connection types: serial, UDP/IP and
TCP/IP. Zephyr currently supports only serial device communication.

The GDB program acts as a client while the Zephyr gdbstub acts as a
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
  property of the chosen node to the spare UART device so that [`printk()`](../../doxygen/html/printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)
  and log messages are not being printed to the same UART device used for GDB.
- For boards with only one UART device, [`printk()`](../../doxygen/html/printk_8h.md#a768a7dff8592b69f327a08f96b00fa54) and logging
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

There is a test application [tests/subsys/debug/gdbstub](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/debug/gdbstub) with one of its
test cases `debug.gdbstub.breakpoints` demonstrating how the Zephyr GDB stub can be used.
The test also has a case to connect to the QEMU’s GDB stub implementation (at a custom
port `tcp:1235`) as a reference to validate the test script itself.

Run the test with the following command from your [`ZEPHYR_BASE`](../../develop/env_vars.md#envvar-ZEPHYR_BASE) directory:

> ```shell
> ./scripts/twister -p qemu_x86 -T tests/subsys/debug/gdbstub
> ```

The test should run successfully, and now let’s do something similar step-by-step
to demonstrate how the Zephyr GDB stub works from the GDB user’s perspective.

In the snippets below use and expect your appropriate directories instead of
`<SDK install directory>`, `<build_directory>`, `<ZEPHYR_BASE>`.

1. Open two terminal windows.
2. On the first terminal, build and run the test application:

   ```shell
   # From the root of the zephyr repository
   west build -b qemu_x86 tests/subsys/debug/gdbstub -- '-DCONFIG_QEMU_EXTRA_FLAGS="-serial tcp:localhost:5678,server"'
   west build -t run
   ```

   Note how we set [`CONFIG_QEMU_EXTRA_FLAGS`](../../kconfig.md#CONFIG_QEMU_EXTRA_FLAGS "CONFIG_QEMU_EXTRA_FLAGS") to direct QEMU serial
   console port to the `localhost` TCP port `5678` to wait for a connection
   from the GDB `remote` command we are going to do on the next steps.
3. On the second terminal, start GDB:

   ```shell
   <SDK install directory>/x86_64-zephyr-elf/bin/x86_64-zephyr-elf-gdb
   ```

   1. Tell GDB where to look for the built ELF file:

      ```text
      (gdb) symbol-file <build directory>/zephyr/zephyr.elf
      ```

      Response from GDB:

      ```text
      Reading symbols from <build directory>/zephyr/zephyr.elf...
      ```
   2. Tell GDB to connect to the Zephyr gdbstub serial backend which is exposed
      earlier as a server through the TCP port `-serial` redirection at QEMU.

      ```text
      (gdb) target remote localhost:5678
      ```

      Response from GDB:

      ```text
      Remote debugging using localhost:5678
      arch_gdb_init () at <ZEPHYR_BASE>/arch/x86/core/ia32/gdbstub.c:252
      252     }
      ```

      GDB also shows where the code execution is stopped. In this case,
      it is at [arch/x86/core/ia32/gdbstub.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/x86/core/ia32/gdbstub.c), line 252.
   3. Use command `bt` or `backtrace` to show the backtrace of stack frames.

      ```text
      (gdb) bt
      #0  arch_gdb_init () at <ZEPHYR_BASE>/arch/x86/core/ia32/gdbstub.c:252
      #1  0x00104140 in gdb_init () at <ZEPHYR_BASE>/zephyr/subsys/debug/gdbstub.c:852
      #2  0x00109c13 in z_sys_init_run_level (level=INIT_LEVEL_PRE_KERNEL_2) at <ZEPHYR_BASE>/kernel/init.c:360
      #3  0x00109e73 in z_cstart () at <ZEPHYR_BASE>/kernel/init.c:630
      #4  0x00104422 in z_prep_c (arg=0x1245bc <x86_cpu_boot_arg>) at <ZEPHYR_BASE>/arch/x86/core/prep_c.c:80
      #5  0x001000c9 in __csSet () at <ZEPHYR_BASE>/arch/x86/core/ia32/crt0.S:290
      #6  0x001245bc in uart_dev ()
      #7  0x00134988 in z_interrupt_stacks ()
      #8  0x00000000 in ?? ()
      ```
   4. Use command `list` to show the source code and surroundings where
      code execution is stopped.

      ```text
      (gdb) list
      247             __asm__ volatile ("int3");
      248
      249     #ifdef CONFIG_GDBSTUB_TRACE
      250             printk("gdbstub:%s GDB is connected\n", __func__);
      251     #endif
      252     }
      253
      254     /* Hook current IDT. */
      255     _EXCEPTION_CONNECT_NOCODE(z_gdb_debug_isr, IV_DEBUG, 3);
      256     _EXCEPTION_CONNECT_NOCODE(z_gdb_break_isr, IV_BREAKPOINT, 3);
      ```
   5. Use command `s` or `step` to step through program until it reaches
      a different source line. Now that it finished executing [`arch_gdb_init()`](../../doxygen/html/group__arch-gdbstub.md#ga21c8a32d35c4d267b8306d595ff1d726)
      and is continuing in `gdb_init()`.

      ```text
      (gdb) s
      gdb_init () at <ZEPHYR_BASE>/subsys/debug/gdbstub.c:857
      857     return 0;
      ```

      ```text
      (gdb) list
      852             arch_gdb_init();
      853
      854     #ifdef CONFIG_GDBSTUB_TRACE
      855             printk("gdbstub:%s exit\n", __func__);
      856     #endif
      857             return 0;
      858     }
      859
      860     #ifdef CONFIG_XTENSA
      861     /*
      ```
   6. Use command `br` or `break` to setup a breakpoint. For this example
      set up a breakpoint at `main()`, and let code execution continue
      without any intervention using command `c` (or `continue`).

      ```text
      (gdb) break main
      Breakpoint 1 at 0x10064d: file <ZEPHYR_BASE>/tests/subsys/debug/gdbstub/src/main.c, line 27.
      ```

      ```text
      (gdb) continue
      Continuing.
      ```

      Once code execution reaches `main()`, execution will be stopped
      and GDB prompt returns.

      ```text
      Breakpoint 1, main () at <ZEPHYR_BASE>/tests/subsys/debug/gdbstub/src/main.c:27
      27              printk("%s():enter\n", __func__);
      ```

      Now GDB is waiting at the beginning of `main()`:

      ```text
      (gdb) list
      22
      23      int main(void)
      24      {
      25              int ret;
      26
      27              printk("%s():enter\n", __func__);
      28              ret = test();
      29              printk("ret=%d\n", ret);
      30              return 0;
      31      }
      ```
   7. To examine the value of `ret`, the command `p` or `print`
      can be used.

      ```text
      (gdb) p ret
      $1 = 1273788
      ```

      Since `ret` has not been initialized, it contains some random value.
   8. If step (`s` or `step`) is used here, it will continue execution
      skipping the interior of `test()`.
      To examine code execution inside `test()`,
      a breakpoint can be set for `test()`, or simply using
      `si` (or `stepi`) to execute one machine instruction, where it has
      the side effect of going into the function. The GDB command `finish`
      can be used to continue execution without intervention until the function
      returns.

      ```text
      (gdb) finish
      Run till exit from #0  test () at <ZEPHYR_BASE>/tests/subsys/debug/gdbstub/src/main.c:17
      0x00100667 in main () at <ZEPHYR_BASE>/tests/subsys/debug/gdbstub/src/main.c:28
      28              ret = test();
      Value returned is $2 = 30
      ```
   9. Examine `ret` again which should have the return value from
      `test()`. Sometimes, the assignment is not done until another
      `step` is issued, as in this case. This is due to the assignment
      code is done after returning from function. The assignment code is
      generated by the toolchain as machine instructions which are not
      visible when viewing the corresponding C source file.

      ```text
      (gdb) p ret
      $3 = 1273788
      (gdb) step
      29              printk("ret=%d\n", ret);
      (gdb) p ret
      $4 = 30
      ```
   10. If `continue` is issued here, code execution will continue indefinitely
       as there are no breakpoints to further stop execution. Breaking execution
       in GDB via `Ctrl`-`C` does not currently work as the Zephyr gdbstub does
       not support this functionality yet. Switch to the first console with QEMU
       running the Zephyr image and stop it manually with `Ctrl`+`a` `x`.
       When the same test is executed by Twister, it automatically takes care of
       stopping the QEMU instance.
