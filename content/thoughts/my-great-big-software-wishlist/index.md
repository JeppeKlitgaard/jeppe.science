---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "🎁 My Great Big Software Wishlist"
subtitle: ""
summary: ""

authors: ["jeppe"]

date: 2021-06-06T14:14:18+01:00
lastmod: 2022-01-02T00:53:27+01:00

tags:
- e-mail
- encryption
- privacy
- productivity
- dev

categories:
- Technology


# Featured image
# To use, place an image named `featured.jpg/png` in your page's folder.
# Placement options: 1 = Full column width, 2 = Out-set, 3 = Screen-width
# Focal point options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
# Set `preview_only` to `true` to just use the image for thumbnails.

image:
  caption: 'Photo by [**Kira auf der Heide**](https://unsplash.com/@kadh)'
  focal_point: "Center"
  placement: 1
  preview_only: false

  

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []

toc: true
featured: false
draft: false
---

Having recently switched over a fair portion of my tech setup to more ethical
and/or open source solutions, which often tend to care more about the wishes
of the communities that surround them than their commericial counterparts, I
have amassed a great big wishlist of things I hope to see in the products I have
been using.

## Espanso

I am super excited for the [espanso] 2.0 release, which is a major refactor
of the already excellent espanso software, which has become a real life-saver
for writing LaTeX and in general switching over to using more unicode symbols.

I have transitioned to using a US keyboard layout almost exclusively, as I find
my native Danish layout to be fairly cramped, especially when writing code or
math. As a result, I would need to change back to the Danish keyboard layout
when needing to write æ, ø, å. Instead, I can just use [espanso]!

### Update

Espanso v2 has been released and it is predictably amazing.
Federico Terzi is an amazingly friendly developer and takes great care of the
community he has built.

Wishlist:
- [X] 2.0.0 release ([issue](https://github.com/federico-terzi/espanso/issues/594))
- [ ] More customizable packages
- [ ] Native `jsonnet` support? ([issue](https://github.com/federico-terzi/espanso/issues/679))
- [ ] Scripting ([issue](https://github.com/federico-terzi/espanso/issues/813))
- [ ] Improved Emoji rendering, ideally with [OpenMoji] ([issue](https://github.com/federico-terzi/espanso/issues/790))
- [ ] Additional search terms for matches ([issue](https://github.com/federico-terzi/espanso/issues/789))

## Anki

Anki is a super neat piece of software for spaced repetition.

The internals have been getting an overhaul for a while, which is great,
but what I am really hoping for is a few UX improvements.
Currently the interface feels a bit dated, and I am __really__ not a fan
of the HTML formatting of the cards, which will sometimes include hidden tags
that break MathJax.

Wishlist:
- [ ] Markdown cards
- [ ] More first-class MathJax support and configurability
- [ ] Integration of most popular addons into core of Anki

## MathJax 3

MathJax 3 development is slowly progressing - the contour integral issue, for example, is from 2013.
I much prefer the extensibility and style to KaTeX, and it seems like release 3.2 of MathJax will
finally get it up to par with the 2.7 release (Python deja vu...)

Wishlist:
- [X] 3.2 Release
- [ ] Newline support - ([issue](https://github.com/mathjax/MathJax/issues/2312))
- [ ] Contour integral support - ([issue](https://github.com/mathjax/MathJax/issues/566))
- [X] Better Unicode support - ([issue](https://github.com/mathjax/MathJax/issues/2708))

## Obsidian

Obsidian is great for writing notes and is super customizable.
It is still early days for Obsidian, which hasn't yet reached version 1.0.0.

Wishlist:
- [ ] Documented API
- [ ] Improvements to Graph View
- [X] WYSIWYG (with good MathJax support)
- [ ] Natively customizable MathJax
- [ ] Open source/partial open source (ideally, though as long as devs keep staying awesome, I am happy)

## ProtonCalendar

I am really hoping to switch away from Google Calendar soon, but until
ProtonCalendar supports subscribing to `.ical` calendars, I don't think I'll
be able to 😞.

Wishlist:
- [ ] Calendar subscription

## ProtonMail

Wishlist:
- [X] Full release of ProtonMail 4.0

## Concepts.app

Wishlist:
- [ ] Full subscription sync between Windows and Android
- [ ] Feature parity between Android, Windows, and iOS.
- [ ] Easily copy selection to clipboard as PNG image on Android

## Cryptomator
Link: [Cryptomator]

Wishlist:
- [ ] Document provider on Android ([issue](https://github.com/cryptomator/android/issues/35))
- [ ] PIN protection on Android ([issue](https://github.com/cryptomator/android/issues/301))

## Hugo

Wishlist:
- [ ] Native support for `.ipynb` Jupyter Notebooks ([issue](https://github.com/gohugoio/hugo/issues/6101))

## gWSL

Wishlist:
- [X] Non-insiders release of `gWSL`


## MountainDuck

I use [MountainDuck] for part of my data to store encrypted [Cryptomator] vaults
on Google Drive, but I find that it isn't super stable.
This is a bit frustrating, as the software is not free.

Wishlist:
- [ ] Fix of memory leaks
- [ ] More stable user experience
- [ ] Faster syncs

## OpenMoji

It would be fantastic to be able to use colored [OpenMoji] on this website.
It will likely be a while before sufficient tooling and browser support will enable
that, unfortunately.

Wishlist:
- [ ] Unicode 14.0
- [ ] Usable in modern browsers

## CSS Font Module 4 Specification

I passionately despise the monochrome Unicode 1.1 emojis that seem to crop up everywhere.
[GitLab] made an excellent [blog post](https://about.gitlab.com/blog/2018/05/30/journey-in-native-unicode-emoji/)
about their struggles with it,
yet somehow in 2022 a good solution has yet to be specified and implemented.

There is a very promising property, `font-variation-emoji`, that is part of the
CSS Font Module 4 Specification draft, but even though the [solution was proposed in
2017](https://github.com/w3c/csswg-drafts/issues/352), it still has not made its way
into browsers. Argh!

Wishlist:
- [ ] Finalisation of CSS Font Module 4 Specification -([issue](https://www.w3.org/TR/css-fonts-4/))
- [ ] Implementation of CSS Font Module 4 Specification in major browsers

[Hugo]: https://gohugo.io/
[Cryptomator]: https://cryptomator.org/
[MountainDuck]: https://mountainduck.io/
[espanso]: https://espanso.org/
[OpenMoji]: https://openmoji.org/
[GitLab]: https://about.gitlab.com/
