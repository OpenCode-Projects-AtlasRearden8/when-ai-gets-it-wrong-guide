# A Second Local Opinion

The fastest independent check on a shaky answer isn't another tab of
searching — it's asking a *different* model the same question and
comparing. And the most reliable way to do that is to run a model on your
own computer: **local AI**. This chapter covers what a second opinion can
honestly catch, how to run one locally without spending money or sending
your data anywhere, and the one blindness two models can never fix for
you.

## Why a second model, of two minds about it

Two models disagreeing is high-value information. Two agreeing is not
proof — and that nuance is the whole point of this chapter:

- **Agreement tells you** the answer is the mainstream pattern — two
  independent engines, trained on different mixtures of writing, both
  producing the same detail.
- **Disagreement tells you** the detail was never solid — that's exactly
  the signature of a fabrication, entity confusion, or other mistake from
  the taxonomy, and it tells you *which load-bearing detail* to go check
  by hand (chapter 05).

The asymmetry is important: use the pair as a *smoke detector*, never as
an *alarm-clearing seal*. When both models say the same surprising thing
about your medication or the law, go to the professional anyway. When
they differ, your answer needs a real source check — you just got told
where.

## What local means (in two sentences)

A local model is the same kind of AI as the cloud chatbots, but the
model file lives on your own computer and answers run entirely on it:
no internet connection needed, no account, no data leaving the machine.
You can literally turn your Wi-Fi off and it keeps working.

## The honest policy trade-offs

| Option | What you gain | What you trade |
| --- | --- | --- |
| A second **cloud** assistant | Bigger models, often better quality, zero setup | Your prompt goes to another company; internet required; usually free tiers have limits |
| A **local** model | Privacy (stays on your machine), offline, no per-use cost, no accounts | Needs your hardware; smaller models give less polished answers; first setup takes an evening |

For the checking habit, both count as a second opinion. Local shines
when the content is private (your finances, health details, work
documents) or when your connection doesn't care to cooperate — and it is
*local-first* friendly: an old laptop is a perfectly good second-opinion
machine.

## Getting a local model running — the friendly path

You need three things: a small downloader app, a model file, and a
question. Beginner-approved configs for a low-spend start:

| Step | What to do | Time |
| --- | --- | --- |
| 1 | Install a local-AI app like **Ollama**, **LM Studio**, or **Jan** (each is free; pick one) | 10 minutes |
| 2 | From inside the app, download a small general model — start with a "7B"-ish model if you have 8–16 GB of RAM | 10–40 minutes for the download |
| 3 | Turn your Wi-Fi off and ask it a question you already asked the cloud chatbot | 0 minutes |

Tips worth their weight:

- **Use a model family different from your main tool.** If your main
  assistant is one lineage, pick a model from a different lineage for the
  second opinion. Related models inherit related holes.
- **Small models write worse and still know facts.** The second-opinion
  job doesn't need poetry. It needs one honest factual answer you can
  compare word-for-word against the first model's *load-bearing
  details* only.
- Ask **the same neutral question** to both. Leading phrases ("isn't it
  true that...") can bend both models the same way, which destroys the
  value of the comparison (chapter 01's sycophancy section).

## The comparison ritual (three minutes)

1. **Ask both models the same neutral question**, in separate windows.
2. **Compare the load-bearing details only** — the names, numbers, dates,
   instruction steps. Skip prose differences entirely; two models will
   always write differently, and style mismatch means nothing.
3. **Sort the details into three bins:** *both same* (solid pattern, use
   at your stakes-level), *differ* (needs a source check, chapter 05),
   *one answered and one refused* (that's gold — the refusal is often the
   weak corner).
4. **Run the source check on the diff**, and let both answers keep the
   parts that survived.

The diff list you compare against is almost always tiny — three to six
details. This entire ritual is a coffee break, and it catches the class
of errors hardest to catch alone: confident, fluent, one-model wobble.

## What a second model cannot fix

Run the honesty check on the ritual:

- **Correlated error.** Models read overlapping samples of the same
  internet. Their blind spots can overlap, and two agreement-boxes
  checked on the same wrong fact is still wrong. Every "source" chapter
  move (05) stays mandatory for anything high-stakes.
- **Recency.** A local model you downloaded last month has that
  month's knowledge edge. Neither local nor cloud has knowledge of
  *tomorrow* — the freshness trap applies to both.
- **The row 4 floors.** If chapter 06 belongs in a chain that ends in a
  licensed human, two models shorten nothing: the human stays at the end
  of the chain, the models just make your questions better.

:::note Privacy is the other half of the win
If you're checking answers that contain your family's paperwork, your
numbers, or your work drafts — a local second opinion means that material
never leaves your machine. Free, offline, and private: the same reasons
this whole guide series stays local-first. Chapter 05's search checks
*do* send your query to a search engine; scrub personal details before
searching (a skill its sibling, *The AI Scam Safety Guide*, exercises
fully).
:::

## When the second opinion is worth its minutes

- The answer is **row 3** (you'll repeat it or act on it).
- It is **fact-dense** — names, numbers, dates, rules.
- It **surprises you** — the fact that "that doesn't sound right" pulled
  your eyebrow? That motion was worth doing again with a different engine.
- It's about something **local and specific** (your state, your machine,
  your situation), where scope errors (#9) and procedure drift (#10)
  live.

When *not* to bother: row 1 and 2 asks, pure creative play, emotional
processing, and anything where the first answer was clearly good. The
second opinion is a tool for specific moments, not a daily tax.

## The calm summary

Agreement is mild evidence, disagreement is a pointer, and neither
replaces the real-world check. Local means private, offline, free, and on
hardware you already own. Three minutes per high-stakes answer, never as
a final word on anything that can hurt.
