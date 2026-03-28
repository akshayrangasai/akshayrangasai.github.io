---
title: 'Getting Started with This Blog'
description: 'A quick look at how this site is built, why I chose Astro, and how to write your first post.'
pubDate: 'Mar 27 2026'
tags: ['meta', 'astro']
---

This site is built with [Astro](https://astro.build) — a static site generator that ships zero JavaScript by default and lets you write content in plain Markdown files.

## Why Astro?

The main reason: **content portability**. Every post on this blog is just a `.md` file sitting in the `src/content/blog/` directory. There's no database, no CMS, no vendor lock-in. If I ever want to switch to a different framework, I take my Markdown files and go.

Other things I like about it:

- **Fast by default** — no client-side JavaScript unless you explicitly add it
- **Framework agnostic** — you can use React, Vue, Svelte, or nothing at all
- **Content collections** — type-safe frontmatter with Zod schemas
- **Built-in RSS** — syndication out of the box

## How to write a post

Create a new `.md` file in `src/content/blog/`. Add frontmatter at the top:

```yaml
---
title: 'Your Post Title'
description: 'A short description for the blog listing.'
pubDate: 'Mar 27 2026'
tags: ['whatever', 'you-want']
---
```

Then write your content in Markdown below the frontmatter. That's it.

## What's next

I'll be using this space to write about whatever I'm working on — tools, projects, ideas, and occasionally something completely unrelated. The goal is to think in public and see where it goes.
