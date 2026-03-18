---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/develop/west/moving-to-west.html
original_path: develop/west/moving-to-west.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Moving to West

To convert a “pre-west” Zephyr setup on your computer to west, follow these
steps. If you are starting from scratch, use the [Getting Started Guide](../getting_started/index.md#getting-started)
instead. See [Troubleshooting West](troubleshooting.md#west-troubleshooting) for advice on common issues.

1. Install west.

   On Linux:

   ```text
   pip3 install --user -U west
   ```

   On Windows and macOS:

   ```text
   pip3 install -U west
   ```

   For details, see [Installing west](install.md#west-install).
2. Move your zephyr repository to a new `zephyrproject` parent directory,
   and change directory there.

   On Linux and macOS:

   ```text
   mkdir zephyrproject
   mv zephyr zephyrproject
   cd zephyrproject
   ```

   On Windows `cmd.exe`:

   ```text
   mkdir zephyrproject
   move zephyr zephyrproject
   chdir zephyrproject
   ```

   The name `zephyrproject` is recommended, but you can choose any name
   with no spaces anywhere in the path.
3. Create a [west workspace](basics.md#west-workspace) using the zephyr
   repository as a local manifest repository:

   ```text
   west init -l zephyr
   ```

   This creates `zephyrproject/.west`, marking the root of your
   workspace, and does some other setup. It will not change the contents of
   the zephyr repository in any way.
4. Clone the rest of the repositories used by zephyr:

   ```text
   west update
   ```

   **Make sure to run this command whenever you pull zephyr.** Otherwise, your
   local repositories will get out of sync. (Run `west list` for current
   information on these repositories.)

You are done: `zephyrproject` is now set up to use west.
