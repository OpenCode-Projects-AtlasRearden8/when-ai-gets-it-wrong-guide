# Why Models Hallucinate

The old word for what AI does when it's wrong is *hallucination*, which is
at once too dramatic and too kind. A hallucination feels like seeing
something that isn't there. What an AI does is more like this: **it fills
an empty shelf with whatever word fits best, then dusts it off.** This
chapter explains that mechanism in plain English, because knowing *why* the
mistakes happen is half of learning to feel them coming.

## The one-sentence explanation

> An AI model has never looked anything up. It writes the words that
> *usually come next* — including when the true words are rare, uneven, or
> missing.

Everything else in this chapter is the equipment around that one sentence.

## A writing engine, not a lookup engine

The model behind a chatbot learned by reading an enormous amount of human
writing and doing one job over and over: predicting what word comes next.
Billions of times. What it got good at is *pattern shaped like knowledge* —
the rhythm of an encyclopedia entry, the cadence of an expert, the structure
of a proper citation.

It then learned a second job: **be helpful**, by being trained on examples
of good answers and coached with your feedback.

Put those two things together and you get the personality you've met: a
fluent, confident, helpful writer that has:

- **No database to check against.** Facts in the output are the words that
  fit, not words retrieved from a reference shelf.
- **No internal signal that says "this bit is shaky."** The made-up detail
  and the true detail come out through the same pipe, polished the same.
- **A strong push away from "I don't know."** An answer — almost any
  answer — scores better than a shrug.

## The four big gap types

Practically everything you'll see is one of these four gaps —
knowledge gaps, freshness gaps, precision gaps, or source gaps:

### 1. Knowledge gaps: rare things

The internet is uneven. Your state's obscure 2021 rule change, the exact
return policy of a mid-size mattress company, the sixth paper by a
little-known professor — the model saw little or nothing about some of
these.
When you ask, it still has to produce *words*, and the words it produces
will sound exactly like a real answer. Rare queries are where fabrication
lives, and the scary thing is that rare queries don't *feel* rare to you.

### 2. Freshness gaps: old or missing facts

The model finished training on a particular day. Everything after that —
new laws, new prices, new menu items, next Tuesday's pharmacy hours, this
year's tax brackets — is invisible to it unless the tool you're using adds
live search. Its answers about these are either stale or quietly invented,
and there's no tone change to tell you which. Ask anything time-sensitive
and cut its confidence score in half automatically.

### 3. Precision gaps: counts, math, dates, digits

Predicting words is not doing arithmetic. Counting something — letters in a
word, numbers in a list, days between dates — is not a word-prediction
task, and the model knows the *shape* of answers more reliably than their
values. So you get "exactly 14 days" when it's 12, total-fee math that's
close but wrong, and confidently specific numbers that shimmer. This is
also why asking the same model the same math question twice sometimes
yields two answers.

### 4. Source gaps: invented citations, quotes, and references

Worst of the family: citations. A model that knows the *shape* of a
citation (author, year, journal, page numbers — all in their neat little
slots) can produce a full-looking one from pure pattern. The journal
exists; the paper doesn't. The author is real; that quote was never said.
You cannot verify by *vibe*. Only chapter 05's source checks catch these.

## Why it never sounds unsure

It has a second job after "write convincing words": **be helpful**. It was
refined on human feedback rewarding confident, complete answers, and the
training examples overwhelmingly did not model gentle hesitation — no
"experts disagree here," no "that data was missing." Its default answer may
be wrong on substance and impossible to tell apart from a right one. You
shouldn't expect reliable tone-shifts when knowledge runs out: an
uncertainty signal that came naturally to humans was never part of the
training. This is a design gap, not malice: a system trained to be useful
is going to fill silence, not decorate it with caveats.

## Sycophancy: it leans toward your framing

One more quirk, and a big one: models tend to agree with how you've framed
the question. If you ask "why is X bad?", the answer drifts toward "here's
why X is bad" — even where experts don't agree with the premise. If you
say "so if I'm right that...", it tends to confirm. Chapter 02 calls
this the sycophantic flip and shows its tell. The counter-habit is simple:
ask neutral questions ("what are reasons for and against?") and correct
premises in the prompt.

:::note Not lying, not stupid
"Hallucinate" is the least useful mental model here, because it implies
something broken inside a person. The model isn't lying and isn't broken;
it's a pattern-completion engine pushed (by design and by training) into
positions where completion sometimes requires invention. The feeling to
have isn't "it's stupid" and isn't "it's alive" — it's "this output came
from somewhere other than the reference shelf; let me check the parts
that matter."
:::

## The implications in one paragraph

Everything in the rest of this guide follows from what you just read:

- The more **rare, recent, or numeric** a question is, the more it needs
  checking (gaps 1–3).
- **Citations and quotes** need checking no matter how elegant they look
  (gap 4).
- **Tone tells you nothing** — confidence is a register the model picked
  up in training, not a knowledge signal (the second job).
- **Your own framing bends it** (sycophancy) — so phrase questions
  neutrally and never let "just checking, right?" flow into the prompt.
- And the trap is never "AI makes mistakes," which you already know. The
  trap is **an AI answer that sounds exactly like your confident coworker
  and is wrong in a specific, load-bearing place**, where you don't
  notice because nothing asked you to look twice.
