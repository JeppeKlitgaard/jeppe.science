---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "😬 I Now Respect Your Privacy"
subtitle: "As I always should have!"
summary: ""

authors: ["jeppe"]

date: 2021-07-24T17:46:11+01:00
lastmod: 2021-07-24T17:46:11+01:00

tags:
- Privacy
- jeppe.science
- Meta
- Plausible
- Google Analytics
- Self-hosted

categories:
- Privacy
- Technology
- Website


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
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

When I first set this up, I wanted to have an idea of whether anyone was actually tuning in (spoiler alert: most people aren't), so I set up Google Analytics on my site. It was easy, free, and the de facto choice for most blogs. My software package even had support for it out of the box.

I should add that this was also before I had my recent adventure into trying to claw back a bit more privacy, so at the time I felt fine about using Google Analytics.

Truthfully, writing {{< thought "privacy-for-non-fanatics" >}} made me realise that using Google Analytics on my site was a tad hypocritical for my liking and I wanted to move away from it at my first opportunity - which was now!

## Choice of software

There seemed to be a surprising amount of well-made open source self-hosted analytics tools that take user privacy seriously — I want to be able to get some basic analytics and numbers from people visiting my site, but I decidedly do not want to contribute to them being tracked and profiled across the internet!

Honourable mentions go to [Matomo] and [Shynet], but I ended up settling on [Plausible], which is super light-weight and provides basic analytics tools while not making any compromises on user privacy.

[Plausible] has a paid plan where they take care of hosting for you, but given the size of my site and my budget, it wasn't really an option for me. Fortunately they also offer a neatly dockerized option for free that you can self-host. Initially I didn't have anywhere to host it, but I recently gave up and bought a cheap 3€/mo VPS, which also hosts the [Remark42]-based comment section. I chose Remark42 over something like [Disqus] for much the same reason I ended up with [Plausible] over something like [Google Analytics].

[Remark42] is great, but does require some tricky reverse-proxy modifications to get working the way I wanted. There might be a post about that in the future.

Anyway, I just wanted to let you know that your privacy is (now) safe with me!


[Matomo]: https://matomo.org/
[Shynet]: https://github.com/milesmcc/shynet
[Plausible]: https://plausible.io/
[Remark42]: https://remark42.com/
[Disqus]: https://disqus.com/
[Google Analytics]: https://marketingplatform.google.com/about/analytics/
