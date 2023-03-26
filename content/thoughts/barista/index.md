---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "☕ Barista: An Espanso build tool for Unicode connoisseurs"
subtitle: "No coffee beans were harmed in the development of this tool."
summary: ""

date: 2022-01-21T23:43:39+00:00
lastmod: 2022-01-21T23:43:43+00:00

tags:
- Unicode
- Productivity
- Open-Source
- Tooling

categories:
- Technology
- Academia


# Featured image
# To use, place an image named `featured.jpg/png` in your page's folder.
# Placement options: 1 = Full column width, 2 = Out-set, 3 = Screen-width
# Focal point options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
# Set `preview_only` to `true` to just use the image for thumbnails.

image:
  caption: 'Photo by [**Nathan Dumlao**](https://unsplash.com/@nate_dumlao)'
  focal_point: "Center"
  placement: 1
  preview_only: false
---

Gone are the days _(at least almost)_ when we lived under the tyranny of the feared
American Standard Code for Information Interchange, perhaps better known by its acronym __*ASCII*__.
The world has _(again, largely)_ changed to the much revered Unicode,
but all is not well in encoding paradise.

We are still in the expressive bondage imposed upon us by the finite and inadequate layout of
our keyboards. I have a dream that one day, keyboard users will rise up and
live out the true potential of the superior encoding. To find freedom in the kind embrace of Unicode.

Our savior is none other than [Federico Terzi], our Holy Book nothing less than [Espanso].
I hope to convince you that [Barista] may belong in the Gospels,
or whatever the equivalent may be in your chosen faith, belief system or lack thereof. 

[Espanso] is _text expander_ that provides an escape from our ASCII nightmare and manages
to be performant, privacy-focused, cross-platform, and entirely free and open source.
Perhaps the best feature of [Espanso] is it's creator – the diety in the increasingly strenious
analogy of this post. [Federico Terzi] is uniquely friendly and helpful, which is an invaluable
quality that is all too rare in the vast world of open source pet projects.

## 😊 Enough with the flattery

Espanso, like most text expanders, works by replacing certain strings of keyboard
inputs with something else – in Espanso you can actually even run scripts or small forms as well,
but that is beyond the scope of this post.

This is solves our Unicode input problem in a simple, predictable, and configurable way.
With the fair decent unique support of [MathJax].

Below is an example of a few expansions I have set up with my Espanso configuration.
Whenever I type the _match_, [Espanso] automagically replaces it with the replacement.

| Match    | Replacement                                                  |
| -------- | ------------------------------------------------------------ |
| `:isod ` | `2022-01-21` (today's date, calculated at time of expansion) |
| `:oint ` | ∮                                                            |
| `:bbR `  | ℝ                                                            |
| `:@ `    | hi@jeppe.science                                             |
| `;b `    | β                                             |

In fact, my current Espanso setup contains 34015 matches that map to 1666 replacements!
I can type pretty much any accented latinised character easily: ą, ÿ, ŧ and so on.

## 🤔 ¿Why?

I can actually also type all the greek letters (and bold, italicised, bold-and-italicsed, sans-serif, sans-serif-bold, sans-serif bold-italic, blackboard bold greek letters).
One might, very reasonably, argue that this is entirely excessive and goes far beyond what is reasonable.
While this is true to some extent, some physics notation relies on different fonts and bold and italics carry mathematical meaning as well.

One very noticable benefit of using Unicode is that your LaTeX/[MathJax]
source text is infinitely (or should I say: ∞-ly) more readable.
I find math-heavy LaTeX source files to be very disorienting and hard to navigate – no more!

## ☕ So what was this Barista thing again?

As you can imagine, managing 34015 matches is a daunting task and entirely
inappropriate work for a human, which brings us to [Barista].

While still poorly documented, [Barista] is a capable build tool for [Espanso]
configuration files. It allows me to split my matches and replacements across 
85 [Jsonnet] files instead.

### 🎺 Aside: Jsonnet

[Jsonnet] is a templating language that extends `json` and allows us to
write logic and neat functionality directly in our configuration files!
It is super cool, though still fairly immature as a language, and currently
the reference implementation is switching from `C++` to `Go`.

## 🏗 Barista as a build tool

[Barista] is essentially just a handy tool for compiling a bunch of [Jsonnet] files
and placing them in a place for [Espanso] to discover.

Additionally it features some neat functionality like detecting match collisions
(though these are less of an issue with Espanso v2) as well as
a bunch of [Jsonnet] library functions that are aimed at making working with
Unicode sequences more convenient.

Lastly the default configuration for Barista is my personal setup,
but can easily be configured to use different leading and trailing triggers –
something that is not currently supported in the native [Espanso] configuration files.

Currently Barista compiles my 7376 lines [Jsonnet] and `YAML` source files into 41067 lines of rendered `YAML`,
which [Espanso] uses.

## 💃 Example of how Barista and Espanso helps me write math

The following identity for the Laplacian of a vector field is a good example of
how [Espanos] has massively improved my math writing workflow:

$$
∇² \vec F = ∇(∇ ⋅ \vec F) - ∇ × (∇ × \vec F)
$$

With Unicode the source text looks like:

```latex
∇² \vec F = ∇(∇ ⋅ \vec F) - ∇ × (∇ × \vec F)
```

Without, it looks like:
```latex
{\nabla}^2 \vec F =
  \nabla(\nabla \cdot \vec F) -
  \nabla \times (\nabla \times \vec F)
```

$$
{\nabla}^2 \vec F =
  \nabla(\nabla \cdot \vec F) -
  \nabla \times (\nabla \times \vec F)
$$

## ⚠ Cautionary note

[Barista] is still somewhat geared towards my personal setup, but if there is
interest I would be happy to polish it a bit more and put it on [PyPI].

[Federico Terzi]: https://federicoterzi.com/
[Espanso]: https://espanso.org/
[MathJax]: https://www.mathjax.org/
[Barista]: https://github.com/JeppeKlitgaard/barista
[Jsonnet]: https://jsonnet.org/
[PyPI]: https://pypi.org/
