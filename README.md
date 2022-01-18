# apartment-research

# Hey

# New


[I'm an inline-style link](https://www.google.com)

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
class Learn:
    def happy(self, run):
	print(run)
```
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```


Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

> Test

> Blockquotes are very handy in email to emulate reply text.

> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 


Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.


# Navigating

The repo is laid out as follows.

- `app/` is where the top-level binary crates for applications live, e.g.
  `app/gimlet` contains the firmware crate for Gimlet. Generally speaking, if
  you want to build an image for something, look here.


- [libfdti1](https://www.intra2net.com/en/developer/libftdi/), found
  as `libftdi1-dev` or similar.

## Build

**We do not use `cargo build` or `cargo run` directly because they are too
inflexible for our purposes.** We have a complex multi-architecture build, which
is a bit beyond them.

Instead, the repo includes a Cargo extension called `xtask` that namespaces our
custom build commands.

```console
$ pyocd list
  #   Probe                                           Unique ID
-----------------------------------------------------------------
  0   NXP Semiconductors LPC-LINK2 CMSIS-DAP V5.361   JSAQCQIQ
```



```console
$ cargo xtask build app/gimletlet/app.toml ping
```
