---
title: "Show HN: Edky, a CLI to convert Ed25519 public keys from one encoding to another"
url: "https://github.com/artob/edky"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-21T19:57:34Z"
metadata:
  score: "5"
---

# Show HN: Edky, a CLI to convert Ed25519 public keys from one encoding to another

> Source: hackernews | Category: news | 2026-07-21T19:57:34Z

Score: 5 | Comments: 2

Everything increasingly runs on Ed25519 keypairs, but Ed25519 public keys can be encoded as text in dozens of surface-incompatible different ways: hexadecimal, Base64 (OpenSSH), Base32z (iroh, pkdns), Base58 (NEAR), and Multibase (IPFS, libp2p), just for starters.<p>Edky is a command-line tool and Rust library that converts between these Ed25519 surface encodings, aiding use of the same underlying keypair across e.g. an iroh endpoint, a libp2p peer, or a NEAR Protocol account. (Surprisingly, a conversion utility like this didn&#x27;t yet exist!)<p><pre><code>    $ cargo binstall -y edky

    $ edky convert -f iroh -t libp2p 47pjoycnsrfmxikm95jh13y88e8qnhzu5kungjpxyepgt7a8krpy
    z6MktwupdmLXVVqTzCw4i46r4uGyosGXRnR3XjN4Zq7oMMsw

    $ edky convert -f libp2p -t iroh z6MktwupdmLXVVqTzCw4i46r4uGyosGXRnR3XjN4Zq7oMMsw
    47pjoycnsrfmxikm95jh13y88e8qnhzu5kungjpxyepgt7a8krpy

    $ edky convert -f near -t hex ed25519:FVen3X669xLzsi6N2V91DoiyzHzg1uAgqiT8jZ9nS96Z
    d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a

    $ edky convert -f hex -t near d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a
    ed25519:FVen3X669xLzsi6N2V91DoiyzHzg1uAgqiT8jZ9nS96Z</code></pre>
