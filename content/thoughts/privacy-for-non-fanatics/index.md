---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "🔏 Privacy for Non-Fanatics"
subtitle: "Striking a balance between convenience, cost, and confidentiality"
summary: ""
authors: ["jeppe"]

toc: true

tags:
- Privacy
- Encryption
- Productivity
- E-Mail
- Cloud Storage
- Google

categories:
- Technology

date: 2021-05-04T17:33:53+01:00
lastmod: 2021-05-04T17:33:53+01:00
featured: false
draft: false

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
---

If you're anything like me, you been meaning to up your privacy-game as some sort of futile
protest against our benevolent data overlords.
It turns out, however, that the services they provide - often for free - are awfully convenient
and crucially don't require much maintainence or effort from their users.
And for the low-low price of nothing more than your privacy, a pound of flesh, and your first-born.

For me, that's a price I have become increasingly unwilling to pay, and I have therefore
started to explore how to find a good balance between:

1. __Convinence__ - I don't want to mess around with PGP keys regularly
2. __Cost__ - I am but a poor student
3. __Confidentiality__ - I want my communication and personal data to be private

## 🤔 Where to start

My primary concerns have been around the data I have been hoarding on my now
abandoned Dropbox account, my photos, and my e-mail communication.

While it was easy to forget and hardly kept me up at night, the thought of storing
all my files unencrypted with a third-party using a free account _should_ be enough to
terrify anyone. I was storing medical details, tax documents, payslips, and all sorts of documents
that were really meant for my 👀 only.

Similarly the thought of Google oogling my photos was a bit disconcerting, innocent though they are.

Lastly, since moving to the UK where you can expect to communicate with your doctor,
employer and the Government over e-mail (which is [a horrible and completely inappropriate way to handle private data](https://security.stackexchange.com/questions/30087/good-simple-list-of-reasons-that-email-is-inherently-insecure)),
I thought I needed to get away from GMail.
In Denmark, any sensitive communication can and should be done via [E-Boks](https://www.e-boks.com/danmark/en/) and [NemID](https://en.wikipedia.org/wiki/NemID),
but sadly there doesn't seem to be a UK equivalent.

## ☁ Cloud Storage

Fortunately, as a student I get literally unlimited cloud storage through my
university Google account. Less fortunately, it doesn't really do much for my goal of
increasing my privacy. Trading in my free Dropbox account with a Google one still
leaves my data unencrypted and readable by a third party.

### Enter Cryptomator

Fortunately, there are software solutions that are designed to solve this issue.
A notable candidate for this is [Cryptomator](https://cryptomator.org/), which
is open source, free, and _fairly_ mature. Effectively it works by implementing a
filesystem that sits on top of a regular folder (called a _vault_), and encrypts/decrypts
your data on the fly. That way, all data at rest is stored encrypted.

By placing your vault in a folder synced by Google Drive, you get to use Google storage,
but without having to worry about them being able to read any data stored in your vault.

The fact that a vault is nothing more than an elaborate folder means that you can store
it nicely next to your other data on a cloud storage service, which you may not want
to have encrypted.

#### Android

The Android client for Cryptomator isn't free, but given the hard work that has gone
into Cryptomator it seems only fair to throw a bit of money at the creators.

__Crucially__, it is a one-time payment and not a recurring subscription.

The Android client could still use a bit of work, and the lack of a Document Provider
can be annoying. As a result, I still store some of my documents unencrypted, such that
apps that work best with a Document Provider can still be used.

Luckily, the client is being [actively developed](https://github.com/cryptomator/android)
and a Document Provider is on [the roadmap](https://cryptomator.org/blog/2021/04/08/roadmap/)

#### Alternatives

A notable alternative would be [Boxcryptor](https://www.boxcryptor.com/en/),
though this has a __recurring__ payment model and is not open source.

Further, it doesn't have a fully-fledged Linux client, which may be a dealbreaker.

### What if we don't have unlimited storage?

After leaving university I suspect I'll end up transitioning to another cloud storage provider.

[Sync.com](https://www.sync.com/pricing/) looks promising with 1TB/5$/month and native end-to-end encryption.
The only problem is a lack of Linux support, which may be a dealbreaker.

## 📷 Pictures

Now that we have mass-storage set up, moving photos from Google Photos to cloud storage
is easy.

For viewing the photos I use [digiKam](https://www.digikam.org/), which seems pretty decent.
It is hardly a show-stopper, UX-wise, but it is free, open-source, and OS-agnostic.

## 📧 E-Mail

For e-mail I eventually settled on just moving off GMail to the privacy-oriented provider [mailbox.org](https://mailbox.org/en/).

While security is probably better when using [ProtonMail](https://protonmail.com/) or [Tutanota](https://tutanota.com/),
I wanted something that _simply works_ and is based on the existing, widely used standards (even if these standards are horrible and inherently insecure).

With a custom domain the price ends up at 3€/mo, which is a bit higher than I was hoping for,
but I guess I'll just forego that one coffee per month and sleep soundly knowing that Google isn't
able to snoop through my mails.

It also has a bunch of other cool features:

1. German based
2. Eco-friendly energy
3. Disposable e-mails
4. Office suite

The UX is a bit old-fashioned and every now and then I'll stumble upon something in German,
which only serves to highlight just how much my German has deteriorated since high school.

Germany being Germany, it doesn't have recurring credit card payments and instead
needs you to 'top up' your credit manually 🙃.

## 💤 TL;DR

It is possible to get some _'easy privacy pickings'_ for less than 10$/mo,
which I am more than happy to pay.
