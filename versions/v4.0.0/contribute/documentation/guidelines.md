---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/contribute/documentation/guidelines.html
original_path: contribute/documentation/guidelines.html
---

# Documentation Guidelines

Note

For instructions on building the documentation, see [Documentation Generation](generation.md#zephyr-doc).

Zephyr Project content is written using the [reStructuredText](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html) [[2]](#id6) markup
language (.rst file extension) with Sphinx extensions, and processed
using Sphinx to create a formatted standalone website. Developers can
view this content either in its raw form as .rst markup files, or (with
Sphinx installed) they can [build the documentation](generation.md#zephyr-doc) locally
to generate the documentation in HTML or PDF format. The HTML content can
then be viewed using a web browser. This same .rst content is served by the
[Zephyr documentation](https://docs.zephyrproject.org) [[4]](#id11) website.

You can read details about [reStructuredText](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html) [[2]](#id6)
and about [Sphinx extensions](http://www.sphinx-doc.org/en/stable/contents.html) [[1]](#id4) from their respective websites.

This document provides a quick reference for commonly used reST and
Sphinx-defined directives and roles used to create the documentation
you’re reading.

## Content Structure

### Tabs, spaces, and indenting

Indenting is significant in reST file content, and using spaces is
preferred. Extra indenting can (unintentionally) change the way content
is rendered too. For lists and directives, indent the content text to
the first non-white space in the preceding line. For example:

```rst
* List item that spans multiple lines of text
  showing where to indent the continuation line.

1. And for numbered list items, the continuation
   line should align with the text of the line above.

.. code-block::

   The text within a directive block should align with the
   first character of the directive name.
```

Refer to the Zephyr [Coding Style](../guidelines.md#coding-style) for additional requirements.

### Headings

While reST allows use of both an overline and matching underline to
indicate a heading, we only use an underline indicator for headings.

- Document title (h1) use `#` for the underline character
- First section heading level (h2) use `*`
- Second section heading level (h3) use `=`
- Third section heading level (h4) use `-`

The heading underline must be the same length as the heading text.

For example:

```rst
This is a title heading
#######################

some content goes here

First section heading
*********************
```

### Lists

For bullet lists, place an asterisk (`*`) or hyphen (`-`) at
the start of a paragraph and indent continuation lines with two
spaces.

The first item in a list (or sublist) must have a blank line before it
and should be indented at the same level as the preceding paragraph
(and not indented itself).

For numbered lists
start with a 1. or a. for example, and continue with autonumbering by
using a `#` sign. Indent continuation lines with three spaces:

```rst
* This is a bulleted list.
* It has two items, the second
  item and has more than one line of reST text.  Additional lines
  are indented to the first character of the
  text of the bullet list.

1. This is a new numbered list. If the wasn't a blank line before it,
   it would be a continuation of the previous list (or paragraph).
#. It has two items too.

a. This is a numbered list using alphabetic list headings
#. It has three items (and uses autonumbering for the rest of the list)
#. Here's the third item

#. This is an autonumbered list (default is to use numbers starting
   with 1).

   #. This is a second-level list under the first item (also
      autonumbered).  Notice the indenting.
   #. And a second item in the nested list.
#. And a second item back in the containing list.  No blank line
   needed, but it wouldn't hurt for readability.
```

Definition lists (with a term and its definition) are a convenient way
to document a word or phrase with an explanation. For example this reST
content:

```rst
The Makefile has targets that include:

html
   Build the HTML output for the project

clean
   Remove all generated output, restoring the folders to a
   clean state.
```

Would be rendered as:

> The Makefile has targets that include:
>
> html
> :   Build the HTML output for the project
>
> clean
> :   Remove all generated output, restoring the folders to a
>     clean state.

### Multi-column lists

If you have a long bullet list of items, where each item is short, you
can indicate the list items should be rendered in multiple columns with
a special `.. rst-class:: rst-columns` directive. The directive will
apply to the next non-comment element (e.g., paragraph), or to content
indented under the directive. For example, this unordered list:

```rst
.. rst-class:: rst-columns

* A list of
* short items
* that should be
* displayed
* horizontally
* so it doesn't
* use up so much
* space on
* the page
```

would be rendered as:

- A list of
- short items
- that should be
- displayed
- horizontally
- so it doesn’t
- use up so much
- space on
- the page

A maximum of three columns will be displayed, and change based on the
available width of the display window, reducing to one column on narrow
(phone) screens if necessary. We’ve deprecated use of the `hlist`
directive because it misbehaves on smaller screens.

### Tables

There are a few ways to create tables, each with their limitations or
quirks. [Grid tables](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#grid-tables)
offer the most capability for defining merged rows and columns, but are
hard to maintain:

```rst
+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      | you can  |
+------------------------+------------+----------+ easily   +
| body row 3 with a two column span   | ...      | span     |
+------------------------+------------+----------+ rows     +
| body row 4             | ...        | ...      | too      |
+------------------------+------------+----------+----------+
```

This example would render as:

| Header row, column 1 (header rows optional) | Header 2 | Header 3 | Header 4 |
| --- | --- | --- | --- |
| body row 1, column 1 | column 2 | column 3 | column 4 |
| body row 2 | … | … | you can easily span rows too |
| body row 3 with a two column span | | … |
| body row 4 | … | … |

[List tables](http://docutils.sourceforge.net/docs/ref/rst/directives.html#list-table)
are much easier to maintain, but don’t support row or column spans:

```rst
.. list-table:: Table title
   :widths: 15 20 40
   :header-rows: 1

   * - Heading 1
     - Heading 2
     - Heading 3
   * - body row 1, column 1
     - body row 1, column 2
     - body row 1, column 3
   * - body row 2, column 1
     - body row 2, column 2
     - body row 2, column 3
```

This example would render as:

Table title

| Heading 1 | Heading 2 | Heading 3 |
| --- | --- | --- |
| body row 1, column 1 | body row 1, column 2 | body row 1, column 3 |
| body row 2, column 1 | body row 2, column 2 | body row 2, column 3 |

The `:widths:` parameter lets you define relative column widths. The
default is equal column widths. If you have a three-column table and you
want the first column to be half as wide as the other two equal-width
columns, you can specify `:widths: 1 2 2`. If you’d like the browser
to set the column widths automatically based on the column contents, you
can use `:widths: auto`.

### Tabbed Content

As introduced in the [Getting Started Guide](../../develop/getting_started/index.md#getting-started), you can provide alternative
content to the reader via a tabbed interface. When the reader clicks on
a tab, the content for that tab is displayed, for example:

```rst
.. tabs::

   .. tab:: Apples

      Apples are green, or sometimes red.

   .. tab:: Pears

      Pears are green.

   .. tab:: Oranges

      Oranges are orange.
```

will display as:

ApplesPearsOranges

Apples are green, or sometimes red.

Pears are green.

Oranges are orange.

Tabs can also be grouped, so that changing the current tab in one area
changes all tabs with the same name throughout the page. For example:

LinuxmacOSWindows

Linux Line 1

macOS Line 1

Windows Line 1

LinuxmacOSWindows

Linux Line 2

macOS Line 2

Windows Line 2

In this latter case, we’re using `.. group-tab::` instead of simply
`.. tab::`. Under the hood, we’re using the [sphinx-tabs](https://github.com/executablebooks/sphinx-tabs) extension that’s included
in the Zephyr setup. Within a tab, you can have most any content *other
than a heading* (code-blocks, ordered and unordered lists, pictures,
paragraphs, and such). You can read more about sphinx-tabs from the
link above.

## Text Formatting

ReSTructuredText supports a variety of text formatting options. This section provides a quick
reference for some of the most commonly used text formatting options in Zephyr documentation. For an
exhaustive list, refer to the [reStructuredText Quick Reference](http://docutils.sourceforge.io/docs/user/rst/quickref.html) [[5]](#id13),
[reStructuredText Interpreted Text Roles](https://docutils.sourceforge.io/docs/ref/rst/roles.html) [[6]](#id15) as well as the [additional roles provided by Sphinx](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html) [[7]](#id17).

### Content Highlighting

Some common reST inline markup samples:

- one asterisk: `*text*` for emphasis (*italics*),
- two asterisks: `**text**` for strong emphasis (**boldface**), and
- two backquotes: ``` ``text`` ``` for `inline code` samples.

If asterisks or backquotes appear in running text and could be confused with
inline markup delimiters, you can eliminate the confusion by adding a
backslash (`\`) before it.

### File Names and Commands

Sphinx extends reST by supporting additional inline markup elements (called
“roles”) used to tag text with special
meanings and allow style output formatting. (You can refer to the [Sphinx Inline Markup](http://sphinx-doc.org/markup/inline.html#inline-markup) [[3]](#id9)
documentation for the full list).

While double quotes can be used for rendering text as “code”, you are encouraged to use the
following roles for marking up file names, command names, and other “special” text.

- `file` for file names, e.g., `` :file:`CMakeLists.txt` `` will render as
  `CMakeLists.txt`

  Note

  In case you want to indicate a “variable” file path, you may use curly braces to enclose the
  variable part of the path, e.g., `` :file:`{boardname}_defconfig` `` will render as
  `boardname_defconfig`.
- `command` for command names, e.g., `` :command:`make` `` will render as **make**
- `envvar` for environment variables, e.g., `` :envvar:`ZEPHYR_BASE` `` will render as
  [`ZEPHYR_BASE`](../../develop/env_vars.md#envvar-ZEPHYR_BASE)

For creating references to files that are hosted in the Zephyr organization on GitHub, refer to
[Cross-referencing files in the Zephyr tree](#linking-to-zephyr-files) section below.

### User Interaction

When documenting user interactions, such as key combinations or GUI interactions, use the following
roles to highlight the commands in a meaningful way:

- `kbd` for keyboard input, e.g., `` :kbd:`Ctrl-C` `` will render as `Ctrl`-`C`
- `menuselection` for menu selections, e.g., `` :menuselection:`File --> Open` `` will render
  as File ‣ Open
- `guilabel` for GUI labels, e.g., `` :guilabel:`Cancel` `` will render as Cancel

### Mathematical Formulas

You can include mathematical formulas using either the `math` role or `math`
directive. The directive provides more flexibility in case you have a more complex formula.

The input language for mathematics is LaTeX markup. Example:

```rst
The answer to life, the universe, and everything is :math:`30 + 2^2 + \sqrt{64} = 42`.
```

This would render as:

> The answer to life, the universe, and everything is \(30 + 2^2 + \sqrt{64} = 42\).

### Non-ASCII Characters

You can insert non-ASCII characters such as a Trademark symbol (™),
by using the notation `|trade|`.
Available replacement names are defined in an include file used during the Sphinx processing
of the reST files. The names of these replacement characters are the same as used in HTML
entities used to insert characters in HTML, e.g., `\&trade;` and are defined in the
file [doc/substitutions.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/substitutions.txt) as listed below:

```rst
.. |br|     raw:: html        .. force a line break in HTML output (blank lines needed here)

   <br />

.. |p|     raw:: html        .. force a blank line in HTML output (blank lines needed here)

   <p></p>

.. These are replacement strings for non-ASCII characters used within the project
   using the same name as the html entity names (e.g., &copy;) for that character

.. |copy|   unicode:: U+000A9 .. COPYRIGHT SIGN
   :ltrim:
.. |trade|  unicode:: U+02122 .. TRADEMARK SIGN
   :ltrim:
.. |reg|    unicode:: U+000AE .. REGISTERED TRADEMARK SIGN
   :ltrim:
.. |deg|    unicode:: U+000B0 .. DEGREE SIGN
   :ltrim:
.. |plusminus|  unicode:: U+000B1 .. PLUS-MINUS SIGN
   :rtrim:
.. |micro|  unicode:: U+000B5 .. MICRO SIGN
   :rtrim:
.. |sup2|  unicode:: U+00B2 .. SUPERSCRIPT TWO
   :ltrim:
```

We’ve kept the substitutions list small but others can be added as
needed by submitting a change to the [doc/substitutions.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/substitutions.txt) file.

### Code Blocks and Command Examples

Use the reST `code-block` directive to create a highlighted block of
fixed-width text, typically used for showing formatted code or console
commands and output. Smart syntax highlighting is also supported (using the
Pygments package). You can also directly specify the highlighting language.
For example:

```rst
.. code-block:: c

   struct k_object {
      char *name;
      uint8_t perms[CONFIG_MAX_THREAD_BYTES];
      uint8_t type;
      uint8_t flags;
      uint32_t data;
   } __packed;
```

Note the blank line between the `code-block` directive and the first
line of the code-block body, and the body content is indented three
spaces (to the first non-white space of the directive name).

This would be rendered as:

> ```c
> struct k_object {
>    char *name;
>    uint8_t perms[CONFIG_MAX_THREAD_BYTES];
>    uint8_t type;
>    uint8_t flags;
>    uint32_t data;
> } __packed;
> ```

Other languages are of course supported (see [languages supported by Pygments](http://pygments.org/languages/) [[8]](#id19)), and in particular,
you are encouraged to make use of the following when appropriate:

- `c` for C code
- `cpp` for C++ code
- `python` for Python code
- `console` for console output, i.e. interactive shell sessions where commands are prefixed by a
  prompt (ex. `$` for Linux, or `uart:~$` for Zephyr’s shell), and where the output is also
  shown. The commands will be highlighted, and the output will not. What’s more, copying code block
  using the “copy” button will automatically copy just the commands, excluding the prompt and the
  outputs of the commands.
- `shell` or `bash` for shell commands. Both languages get highlighted the same but you may use
  `bash` for conveying that the commands are bash-specific, and `shell` for generic shell
  commands.

  Note

  Do not use `bash` or `shell` if your code block includes a prompt, use `console` instead.

  Reciprocally, do not use `console` if your code block does not include a prompt and is not
  showcasing an interactive session with command(s) and their output.

  When to use `bash`/`shell` vs. `console`

  | Use case | `code-block` snippet | Expected output |
  | --- | --- | --- |
  | One or several commands, no output | ```rst .. code-block:: shell     echo "Hello World!" ``` | ```shell echo "Hello World!" ``` |
  | An interactive shell session with command(s) and their output | ```rst .. code-block:: console     $ echo "Hello World!"    Hello World! ``` | ```shell $ echo "Hello World!" Hello World! ``` |
  | An interactive Zephyr shell session, with commands and their outputs | ```rst .. code-block:: console     uart:~$ version    Zephyr version 3.5.99    uart:~$ kernel uptime    Uptime: 20970 ms ``` | ```shell uart:~$ version Zephyr version 3.5.99 uart:~$ kernel uptime Uptime: 20970 ms ``` |
- `bat` for Windows batch files
- `cfg` for config files with “KEY=value” entries (ex. Kconfig `.conf` files)
- `cmake` for CMake
- `devicetree` for Devicetree
- `kconfig` for Kconfig
- `yaml` for YAML
- `rst` for reStructuredText

When no language is specified, the language is set to `none` and the code block is not
highlighted. You may also use `none` explicitly to achieve the same result; for example:

```rst
.. code-block:: none

   This would be a block of text styled with a background
   and box, but with no syntax highlighting.
```

Would display as:

> ```text
> This would be a block of text styled with a background
> and box, but with no syntax highlighting.
> ```

There’s a shorthand for writing code blocks too: end the introductory paragraph with a double colon
(`::`) and indent the code block content that follows it by three spaces. On output, only one
colon will be shown. The code block will have no highlighting (i.e. `none`). You may however use
the `highlight` directive to customize the default language used in your document (see for
example how this is done at the beginning of this very document).

## Links and Cross-References

### Cross-referencing internal content

Traditional ReST links are only supported within the current file using the
notation:

```rst
Refer to the `internal-linking`_ page
```

which renders as,

> Refer to the [internal-linking](#internal-linking) page

Note the use of a trailing
underscore to indicate an outbound link. In this example, the label was
added immediately before a heading, so the text that’s displayed is the
heading text itself. You can change the text that’s displayed as the
link writing this as:

```rst
Refer to the `show this text instead <internal-linking_>`_ page
```

which renders as,

> Refer to the [show this text instead](#internal-linking) page

### Cross-referencing external content

With Sphinx’s help, we can create
link-references to any tagged text within the Zephyr Project documentation.

Target locations in a document are defined with a label directive:

```rst
.. _my label name:

Heading
=======
```

Note the leading underscore indicating an inbound link.
The content immediately following
this label must be a heading, and is the target for a `` :ref:`my label name` ``
reference from anywhere within the Zephyr documentation.
The heading text is shown when referencing this label.
You can also change the text that’s displayed for this link, such as:

```rst
:ref:`some other text <my label name>`
```

To enable easy cross-page linking within the site, each file should have
a reference label before its title so it can
be referenced from another file. These reference labels must be unique
across the whole site, so generic names such as “samples” should be
avoided. For example the top of this document’s .rst file is:

```rst
.. _doc_guidelines:

Documentation Guidelines for the Zephyr Project
###############################################
```

Other .rst documents can link to this document using the `` :ref:`doc_guidelines` `` tag and
it will show up as [Documentation Guidelines](#doc-guidelines). This type of internal cross reference works across
multiple files, and the link text is obtained from the document source so if the title changes,
the link text will update as well.

You can also define links to any URL and then reference it in your document.
For example, with this label definition in the document:

```rst
.. _Zephyr Wikipedia Page:
   https://en.wikipedia.org/wiki/Zephyr_(operating_system)
```

you can reference it with:

```rst
Read the `Zephyr Wikipedia Page`_ for more information about the
project.
```

Tip

When a document contains many external links, it can be useful to list them in a single
“References” section at the end of the document. This can be done using the
`target-notes` directive. Example:

```rst
References
==========

.. target-notes::

.. _external_link1: https://example.com
.. _external_link2: https://example.org
```

### Cross-referencing C documentation

:c:member:

:c:data:

:c:var:

:c:func:

:c:macro:

:c:struct:

:c:union:

:c:enum:

:c:enumerator:

:c:type:
:   You may use these roles to cross-reference the Doxygen documentation of C functions, macros,
    types, etc.

    They are rendered in the HTML output as links to the corresponding Doxygen documentation for the
    item. For example:

    ```rst
    Check out :c:function:`gpio_pin_configure` for more information.
    ```

    Will render as:

    > Check out [`gpio_pin_configure()`](../../doxygen/html/group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33) for more information.

    You may provide a custom link text, similar to the built-in `ref` role.

## Visual Elements

### Images

Images are included in the documentation by using an `image` directive:

```rst
.. image:: ../../../../images/doc-gen-flow.png
   :align: center
   :alt: alt text for the image
```

or if you’d like to add an image caption, use:

```rst
.. figure:: ../../../../images/doc-gen-flow.png
   :alt: image description

   Caption for the figure
```

The file name specified is relative to the document source file,
and we recommend putting images into an `images` folder where the document
source is found.

The usual image formats handled by a web browser are supported: WebP, PNG, GIF,
JPEG, and SVG.

Keep the image size only as large as needed, generally at least 500 px wide but
no more than 1000 px, and no more than 100 KB unless a particularly large image
is needed for clarity.

#### Recommended image formats based on content

- **Screenshots**: WebP or PNG.
- **Diagrams**: Consider using Graphviz for simple diagrams (see
  [dedicated section](graphviz_diagrams) below. If using an external tool, SVG is preferred.
- **Photos** (ex. boards): WebP. Use transparency if possible/available.

### Graphviz

[Graphviz](https://graphviz.org) [[9]](#id21) is a tool for creating diagrams specified in a simple text language. As it’s important
to allow for diagrams used in the documentation to be easily maintained, we encourage the use of
Graphviz for creating diagrams. Graphviz is particularly well suited for creating state diagrams, flow
charts, and other types of diagrams that can be expressed as a graph.

To include a Graphviz diagram in a document, use the `graphviz` directive. For example:

```rst
.. graphviz::

   digraph G {
      rankdir=LR;
      A -> B;
      B -> C;
      C -> D;
   }
```

Would render as:

> digraph G {
> rankdir=LR;
> A -> B;
> B -> C;
> C -> D;
> }

Please refer to the [Graphviz documentation](https://graphviz.org/documentation) [[10]](#id23) for more information on how to create diagrams using
Graphviz’s DOT language.

## Custom Sphinx Roles and Directives

The Zephyr documentation uses custom Sphinx roles and directives to provide additional functionality
and to make it easier to write and maintain consistent documentation.

### Application build commands

.. zephyr-app-commands::
:   Generate consistent documentation of the shell commands needed to manage (build, flash, etc.) an
    application

    For example, to generate commands to build `samples/hello_world` for `qemu_x86` use:

    ```rst
    .. zephyr-app-commands::
       :zephyr-app: samples/hello_world
       :board: qemu_x86
       :goals: build
    ```

    This will render as:

    > ```shell
    > # From the root of the zephyr repository
    > west build -b qemu_x86 samples/hello_world
    > ```

    Options

    :tool: (string)
    :   Which tool to use. Valid options are currently `cmake`, `west` and `all`.
        The default is `west`.

    :app: (string)
    :   Path to the application to build.

    :zephyr-app: (string)
    :   Path to the application to build, this is an app present in the upstream zephyr repository.
        Mutually exclusive with `:app:`.

    :cd-into: (no value)
    :   If set, build instructions are given from within the `:app:` folder, instead of outside of
        it.

    :generator: (string)
    :   Which build system to generate.

        Valid options are currently `ninja` and `make`. The default is `ninja`. This option is
        not case sensitive.

    :host-os:
    :   Which host OS the instructions are for.

        Valid options are `unix`, `win` and `all`. The default is `all`.

    :board: (string)
    :   If set, build commands will target the given board.

    :shield: (string)
    :   If set, build commands will target the given shield.

        Multiple shields can be provided in a comma separated list.

    :conf:
    :   If set, build commands will use the given configuration file(s).

        If multiple configuration files are provided, enclose the space-separated list of files with
        double quotes, e.g., “a.conf b.conf”.

    :gen-args: (string)
    :   If set, indicates additional arguments to the CMake invocation.

    :build-args: (string)
    :   If set, indicates additional arguments to the build invocation.

    :west-args: (string)
    :   If set, additional arguments to the west invocation (ignored for `:tool: cmake`).

    :flash-args: (string)
    :   If set, additional arguments to the flash invocation.

    :snippets: (string)
    :   If set, indicates the application should be compiled with the listed snippets.

        Multiple snippets can be provided in a comma separated list.

    :build-dir: (string)
    :   If set, the application build directory will *APPEND* this relative, Unix-separated, path to
        the standard build directory. This is mostly useful for distinguishing builds for one
        application within a single page.

    :build-dir-fmt: (string)
    :   If set, assume that west config build.dir-fmt` has been set to this path.

        Exclusive with `:build-dir:` and depends on `:tool: west`.

    :goals: (string)
    :   A whitespace-separated list of what to do with the app (any of `build`, `flash`,
        `debug`, `debugserver`, `run`).

        Commands to accomplish these tasks will be generated in the right order.

    :maybe-skip-config: (no value)
    :   If set, this indicates the reader may have already created a build directory and changed
        there, and will tweak the text to note that doing so again is not necessary.

    :compact: (no value)
    :   If set, the generated output is a single code block with no additional comment lines.

### Cross-referencing files in the Zephyr tree

Special roles are available to reference files in the Zephyr tree. For example, referencing this
very file can be done using the [`zephyr_file`](#role-zephyr_file) role, like this:

```rst
Check out :zephyr_file:`doc/contribute/documentation/guidelines.rst` for more information.
```

This would render as:

> Check out [doc/contribute/documentation/guidelines.rst](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/contribute/documentation/guidelines.rst) for more information.

You may use the [`zephyr_raw`](#role-zephyr_raw) role instead if you want to reference the “raw” content.

:zephyr\_file:
:   This role is used to reference a file in the Zephyr tree. For example:

    ```rst
    Check out :zephyr_file:`doc/contribute/documentation/guidelines.rst` for more information.
    ```

    Will render as:

    > Check out [doc/contribute/documentation/guidelines.rst](https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/contribute/documentation/guidelines.rst) for more information.

:zephyr\_raw:
:   This role is used to reference the raw content of a file in the Zephyr tree. For example:

    ```rst
    Check out :zephyr_raw:`doc/contribute/documentation/guidelines.rst` for more information.
    ```

    Will render as:

    > Check out [doc/contribute/documentation/guidelines.rst](https://github.com/zephyrproject-rtos/zephyr/raw/main/doc/contribute/documentation/guidelines.rst) for more information.

:module\_file:
:   This role is used to reference a module in the Zephyr tree. For example:

    ```rst
    Check out :module_file:`hal_stm32:CMakeLists.txt` for more information.
    ```

    Will render as:

    > Check out [hal\_stm32:CMakeLists.txt](https://github.com/zephyrproject-rtos/hal_stm32/blob/019d8255333f96bdd47d26b44049bd3e7af8ef55/CMakeLists.txt) for more information.

### Cross-referencing GitHub issues and pull requests

:github:
:   This role is used to reference a GitHub issue or pull request.

    For example, to reference issue #1234:

    ```rst
    Check out :github:`1234` for more background about this known issue.
    ```

    This will render as:

    > Check out [GitHub #1234](https://github.com/zephyrproject-rtos/zephyr/issues/1234) for more background about this known issue.

### Doxygen API documentation

.. doxygengroup:: name
:   This directive is used to output a short description of a Doxygen group and a link to the
    corresponding Doxygen-generated documentation.

    All the code samples (declared using the [`zephyr:code-sample`](#directive-zephyr-code-sample) directive) indicating the
    group as relevant will automatically be list and referenced in the rendered output.

    For example:

    ```rst
    .. doxygengroup:: can_interface
    ```

    Will render as:

    > [CAN Interface](../../doxygen/html/group__can__interface.md)
    >
    > Related code samples
    >
    > - [Controller Area Network (CAN) babbling node](../../samples/drivers/can/babbling/README.md#can-babbling "Simulate a babbling CAN node.")Simulate a babbling CAN node.
    > - [Controller Area Network (CAN) counter](../../samples/drivers/can/counter/README.md#can-counter "Send and receive CAN messages.")Send and receive CAN messages.

:c:group:
:   This role is used to reference a Doxygen group in the Zephyr tree. In the HTML documentation,
    they are rendered as links to the corresponding Doxygen-generated documentation for the group.
    For example:

    ```rst
    Check out :c:group:`gpio_interface` for more information.
    ```

    Will render as:

    > Check out [GPIO Driver APIs](../../doxygen/html/group__gpio__interface.md) for more information.

    You may provide a custom link text, similar to the built-in `ref` role.

### Kconfig options

If you want to reference a Kconfig option from a document, you can use the
[`kconfig:option`](#role-kconfig-option) role and provide the name of the option you want to reference. The role
will automatically generate a link to the documentation of the Kconfig option when building HTML
output.

Make sure to use the full name of the Kconfig option, including the `CONFIG_` prefix.

:kconfig:option:
:   This role is used to reference a Kconfig option in the Zephyr tree. For example:

    ```rst
    Check out :kconfig:option:`CONFIG_GPIO` for more information.
    ```

    Will render as:

    > Check out [`CONFIG_GPIO`](../../kconfig.md#CONFIG_GPIO "CONFIG_GPIO") for more information.

### Devicetree bindings

If you want to reference a Devicetree binding from a document, you can use the
[`dtcompatible`](#role-dtcompatible) role and provide the compatible string of the binding you want to
reference. The role will automatically generate a link to the documentation of the binding when
building HTML output.

:dtcompatible:
:   This role can be used inline to make a reference to the generated documentation for the
    Devicetree compatible given as argument.

    There may be more than one page for a single compatible. For example, that happens if a binding
    behaves differently depending on the bus the node is on. If that occurs, the reference points at
    a “disambiguation” page which links out to all the possibilities, similarly to how Wikipedia
    disambiguation pages work. Example:

    ```rst
    Check out :dtcompatible:`zephyr,input-longpress` for more information.
    ```

    Will render as:

    > Check out [`zephyr,input-longpress`](../../build/dts/api/bindings/input/zephyr%2Cinput-longpress.md#std-dtcompatible-zephyr-input-longpress) for more information.

### Code samples

.. zephyr:code-sample:: id
:   This directive is used to describe a code sample, including which noteworthy APIs it may be
    exercising.

    For example:

    ```rst
    .. zephyr:code-sample:: blinky
       :name: Blinky
       :relevant-api: gpio_interface

       Blink an LED forever using the GPIO API.
    ```

    The content of the directive is used as the description of the code sample.

    Options

    :name: (text)
    :   Indicates the human-readable short name of the sample.

    :relevant-api: (text)
    :   Optional space-separated list of Doxygen group names that correspond to the APIs exercised
        by the code sample.

:zephyr:code-sample:
:   This role is used to reference a code sample described using [`zephyr:code-sample`](#directive-zephyr-code-sample).

    For example:

    ```rst
    Check out :zephyr:code-sample:`blinky` for more information.
    ```

    Will render as:

    > Check out [Blinky](../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") for more information.

    This can be used exactly like the built-in `ref` role, i.e. you may provide a custom
    link text. For example:

    ```rst
    Check out :zephyr:code-sample:`blinky code sample <blinky>` for more information.
    ```

    Will render as:

    > Check out [blinky code sample](../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") for more information.

.. zephyr:code-sample-category:: id
:   This directive is used to define a category for grouping code samples.

    For example:

    ```rst
    .. zephyr:code-sample-category:: gpio
       :name: GPIO
       :show-listing:

       Samples related to the GPIO subsystem.
    ```

    The contents of the directive is used as the description of the category. It can contain any
    valid reStructuredText content.

    Options

    :name: (text)
    :   Indicates the human-readable name of the category.

    :show-listing: (flag)
    :   If set, a listing of code samples in the category will be shown. The listing is automatically
        generated based on all code samples found in the subdirectories of the current document.

    :glob: (text)
    :   A glob pattern to match the files to include in the listing. The default is \*/\* but it can
        be overridden e.g. when samples may be found in directories not sitting directly under the
        category directory.

:zephyr:code-sample-category:
:   This role is used to reference a code sample category described using
    [`zephyr:code-sample-category`](#directive-zephyr-code-sample-category).

    For example:

    ```rst
    Check out :zephyr:code-sample-category:`cloud` samples for more information.
    ```

    Will render as:

    > Check out [IoT Cloud](../../samples/net/cloud/README.md#cloud) samples for more information.

.. zephyr:code-sample-listing::
:   This directive is used to show a listing of all code samples found in one or more categories.

    For example:

    ```rst
    .. zephyr:code-sample-listing::
       :categories: cloud
    ```

    Will render as:

    > - [AWS IoT Core MQTT](../../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")Connect to AWS IoT Core and publish messages using MQTT.
    > - [Microsoft Azure IoT Hub MQTT](../../samples/net/cloud/mqtt_azure/README.md#mqtt-azure "Connect to Azure IoT Hub and publish messages using MQTT.")Connect to Azure IoT Hub and publish messages using MQTT.
    > - [TagoIO HTTP Post](../../samples/net/cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")Send random temperature values to TagoIO IoT Cloud Platform using HTTP.

    Options

    :categories: (text)
    :   A space-separated list of category IDs for which to show the listing.

    :live-search: (flag)
    :   A flag to include a search box right above the listing. The search box allows users to filter
        the listing by code sample name/description, which can be useful for categories with a large
        number of samples. This option is only available in the HTML builder.

### Boards

.. zephyr:board:: name
:   This directive is used at the beginning of a document to indicate it is the main documentation
    page for a board whose name is given as the directive argument.

    For example:

    ```rst
    .. zephyr:board:: wio_terminal
    ```

    The metadata for the board is read from various config files and used to automatically populate
    some sections of the board documentation. A board documentation page that uses this directive
    can be linked to using the [`zephyr:board`](#role-zephyr-board) role.

:zephyr:board:
:   This role is used to reference a board documented using [`zephyr:board`](#directive-zephyr-board).

    For example:

    ```rst
    Check out :zephyr:board:`wio_terminal` for more information.
    ```

    Will render as:

    > Check out [Wio Terminal](../../boards/seeed/wio_terminal/doc/index.md#wio_terminal) for more information.

.. zephyr:board-catalog::
:   This directive is used to generate a catalog of Zephyr-supported boards that can be used to
    quickly browse the list of all supported boards and filter them according to various criteria.

## References

[[1](#id5)]

[http://www.sphinx-doc.org/en/stable/contents.html](http://www.sphinx-doc.org/en/stable/contents.html)

[2]
([1](#id7),[2](#id8))

[http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html)

[[3](#id10)]

[http://sphinx-doc.org/markup/inline.html#inline-markup](http://sphinx-doc.org/markup/inline.html#inline-markup)

[[4](#id12)]

[https://docs.zephyrproject.org](https://docs.zephyrproject.org)

[[5](#id14)]

[http://docutils.sourceforge.io/docs/user/rst/quickref.html](http://docutils.sourceforge.io/docs/user/rst/quickref.html)

[[6](#id16)]

[https://docutils.sourceforge.io/docs/ref/rst/roles.html](https://docutils.sourceforge.io/docs/ref/rst/roles.html)

[[7](#id18)]

[https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html)

[[8](#id20)]

[http://pygments.org/languages/](http://pygments.org/languages/)

[[9](#id22)]

[https://graphviz.org](https://graphviz.org)

[[10](#id24)]

[https://graphviz.org/documentation](https://graphviz.org/documentation)
