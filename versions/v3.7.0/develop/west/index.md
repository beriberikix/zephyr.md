---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/develop/west/index.html
original_path: develop/west/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# West (Zephyr’s meta-tool)

The Zephyr project includes a swiss-army knife command line tool named
`west`[[1]](#west-name). West is developed in its own [repository](https://github.com/zephyrproject-rtos/west).

West’s built-in commands provide a multiple repository management system with
features inspired by Google’s Repo tool and Git submodules. West is also
“pluggable”: you can write your own west extension commands which add
additional features to west. Zephyr uses this to provide conveniences for
building applications, flashing and debugging them, and more.

Like `git` and `docker`, the top-level `west` command takes some common
options, a sub-command to run, and then options and arguments for that
sub-command:

```text
west [common-opts] <command> [opts] <args>
```

Since west v0.8, you can also run west like this:

```text
python3 -m west [common-opts] <command> [opts] <args>
```

You can run `west --help` (or `west -h` for short) to get top-level help
for available west commands, and `west <command> -h` for detailed help on
each command.

For details on west’s Python APIs, see [West APIs](west-apis.md#west-apis).

Footnotes

[[1](#id1)]

Zephyr is an English name for the Latin [Zephyrus](https://en.wiktionary.org/wiki/Zephyrus), the ancient Greek god of the
west wind.
