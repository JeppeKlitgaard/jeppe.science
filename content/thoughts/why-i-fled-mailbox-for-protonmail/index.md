---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "🏃‍♂️ Why I Fled Mailbox.org for Protonmail"
subtitle: "A bumpy ride to get privacy-respecting e-mail"
summary: ""

authors: ["jeppe"]

date: 2021-06-06T18:36:33+01:00
lastmod: 2021-06-06T18:36:33+01:00

tags:
- e-mail
- protonmail
- mailfence
- mailbox.org
- encryption
- productivity

categories:
- Technology
- Privacy
- Review


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

## The Goal
As I described in the post [🔏 Privacy for Non-Fanatics]({{< relref "/thoughts/privacy-for-non-fanatics" >}}),
I have recently been on a budget-friendly quest to claw back at least some of my privacy from the ever-expanding silicon giants.

Something that bothered me in particular was e-mail, through which a surprising amount of sensitive information is being
sent in the UK - this would be considered highly inappropriate – if not outright illegal – in Denmark. 🤔

## The Journey
In the end, after being disappointed with the initial look and feel of [MailFence], I went for the Germany-based Mailbox.org.
These are both options that are highly praised in online reviews, but given my experience with [Mailbox.org] I find it hard to believe that
even the more reputable tech sites did a thorough test of the service.

I had wanted to avoid [ProtonMail] out of a concern that they don't offer regular IMAP/SMTP connectivity,
but require the use of "ProtonMail Bridge" to be able to use other mail clients than the ProtonMail web service.

This is important to me, as I currently use 5 e-mail accounts due to different organisational affiliations,
and this would be entirely unmanageable if I were to use individual inboxes on webservices.

### The Problem(s)
As I was setting up SPF and DKIM on Mailbox.org, I had some problems due to an error in their "knowledge database", which suggests
using an SPF-type entry to set up SPF. While this might have made sense at the time of writing that entry (presumable refering to [RFC4408]), this document was made obsolete in 2014 with the introduction of [RFC7208]. [RFC4408] was only ever experimental, and in the [RFC7208] specification SPF-type RR's are no longer valid and should be changed to TXT.

As a result of using the wrong RR type (by following the mailbox.org guide), I couldn't get Google to
accept my SPF record, which was obviously not ideal. Eventually I figured out the issue and wanted to highlight this to [Mailbox.org] and filed a ticket with their support.

After having waited 12 days for a reply from their support team, I sent a quick follow up to their support team,
in which I very politely explained that I was still hoping for a reply and had become worried I was forgotten by them. 😢

After another couple of days, taking the total wait for a simple support ticket up to over 2 weeks,
they finally got back to me. It wasn't quite what I was expecting though – Germans are usually known for their formality and thoroughness,
but I was left with a short, unhelpful reply written in some fairly broken English. No apologies for, or acknowledgement of, my inconvinence.

While I hadn't been impressed with the dated look of the website, the UX issues with their online application, or the fact that you'd suddenly wander into parts of the application still in German, it was my experience with their support that broke the camels back - I simply didn't feel comfortable staying with [Mailbox.org].

Additionally, they don't support recurring payments, nor do they _appear_ to remind you when your balance is running out. I was one day from running out of credits when I finally left them, but hadn't gotten any reminder to add my credits to my balance — I dare not think what happens when you run out credits.


__I really hope people steer clear of [Mailbox.org] in the future.
While their heart might be in the right place, they seem very far from a reliable provider,
especially for something as critical as e-mail.__
It should be noted that I was on the 3€/mo plan.

It appears I am not alone in my experience: [Other frustrated customer](https://www.reddit.com/r/privacytoolsIO/comments/95spme/mailboxorg_sucks_need_a_new_privacy_email_provider/)

Oh, and the guide still has not been fixed! 🤦‍♂️

## The Solution
[ProtonMail]'s paid offering is slightly less featureful than a comparable plan
with [Mailbox.org], but in return you get a solution that works much better and
is far easier to use. Encryption is also enabled out of the box.

Unlike [Mailbox.org], who actively guide you towards an invalid SPF setup,
[ProtonMail] helps you setup SPF, DMARC, and DKIM - further, they even check
that they are setup correctly and their automatic service spotted and alerted me
to a typo in my DMARC setup! Absolutely amazing.

Even the ProtonMail 3.x version, which is due to be replaced with the even snazzier
ProtonMail 4.0 very soon, had an excellent user experience and setting up
ProtonMail Bridge for use with Outlook was easy and reliable.

I do kind of miss having 5 custom domains for the price of 3€, but I only really need
one, which I get for the price of 3.3$/month (≈2.7€/month).

The Android app seems nice and I am really looking forward to using ProtonCalendar,
once that has a couple more features that currently prevent me from switching over from
Google Calendar.

_I should add that this definitely isn't sponsored, I am just really impressed with [ProtonMail]
and really unimpressed with [Mailbox.org]..._

## TL;DR

[Mailbox.org] is a super poor choice for an e-mail provider.

[ProtonMail] is really good, but can be expensive if you need a lot of custom domains.
It also won't work for you if
you need to use a non-Proton client on mobile.

ProtonMail is the king of mail providers, and with very good reason. 👑

[RFC4408]: https://datatracker.ietf.org/doc/html/rfc4408
[RFC7208]: https://datatracker.ietf.org/doc/html/rfc7208
[MailFence]: https://mailfence.com/
[Mailbox.org]: https://mailbox.org/en/
[ProtonMail]: https://protonmail.com/
