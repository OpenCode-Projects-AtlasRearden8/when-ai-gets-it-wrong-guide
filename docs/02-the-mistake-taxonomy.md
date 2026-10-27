# The Mistake Taxonomy

Chapter 01 explained *why* models go wrong. This chapter gives the wrongness
a last name. Below is a field guide to the recurring mistake types — the
ones you'll actually meet — with what each one looks like in the wild,
why it happens, and the calm move that catches it.

You will not need all twelve in a given week. But knowing the *shape* of
each mistake is what lets you spot one in three seconds instead of
swallowing it whole.

## The taxonomy

| # | Mistake | What it looks like | Why it happens | The catch |
| --- | --- | --- | --- | --- |
| 1 | **Fabricated fact** | A specific detail that simply is not true — a wrong founding year, an invented ingredient warning, a statute that doesn't exist | The shelf was empty; it filled it with fitting words | Verify any load-bearing detail against a real source (ch. 05) |
| 2 | **Stale fact** | Something that *was* true when the model trained: an old price, a superseded guideline, a menu that changed | Training has a cutoff date the model can't feel | Treat time-sensitive answers as vintage; confirm recency (ch. 03, 05) |
| 3 | **Numeric slip** | Close-but-wrong arithmetic, miscounted lists, backwards date math | Word prediction is not arithmetic | Recompute the numbers yourself; count the list items |
| 4 | **Invented source** | A full citation, quote, court case, or study that does not exist — often with one true anchor (a real author, a real journal) | It knows the *shape* of citations, not their contents | Never trust a citation by format; search the exact title in quotes (ch. 05) |
| 5 | **Mangled quote** | A real person saying words they never said, or a subtly altered version of a real quote | Quotes are pattern; fidelity is luck | Search the exact quoted text in quotation marks |
| 6 | **Entity confusion** | Two similar things blended: the wrong city in the right state, two people with the same name merged, the matrix product confused with its cousin | Overlapping patterns activate together | Check names against the source; ask "which one exactly?" |
| 7 | **Confident overreach** | A sweeping claim far beyond the evidence — "always," "never," "doctors now agree" | Fluency imitates authority; hedging was never rewarded | Read absolutes as flags; downgrade every "always" to "sometimes" and re-ask |
| 8 | **Sycophantic flip** | It agrees with whatever you hint at — and reverses position if you push back again | It was trained to be agreeable; your framing is a strong pull (ch. 01) | Ask neutrally; state "I don't have an opinion yet — what's the evidence?" |
| 9 | **Scope error** | Perfectly right about one thing, stretched to cover yours — general advice applied to your state, your meds, your machine | It can't reliably tell where its answer stops applying | Match the answer to *your* specifics; re-ask with your exact details |
| 10 | **Procedure drift** | Multi-step instructions whose middle steps don't exist — a menu item that was renamed years ago, a button that isn't there | Software changes faster than training data | Confirm each step against the actual screen; fall back to real help pages |
| 11 | **Confident refusal gap** | The subtle one: it doesn't say "I don't know" — it picks the nearest plausible answer instead | Being helpful is a trained-in reflex (ch. 01) | Re-ask as an open question: "what would a careful expert say they *don't* know here?" |
| 12 | **Compounding** | A small wobble early in a long answer becomes a big wrong turn by the end; later details lean on the earlier mistake | Every next word conditions on the words before it | Verify the early facts first; ask it to redo the whole chain if step 1 was wrong |

## Three honesty notes about the table

**First**, these categories overlap, and real mistakes often arrive as
combos — a mangled quote delivered as perfect procedure drift inside a
stale fact. The table is a lens rack, not a set of bins.

**Second**, the model can also exhibit *uncertainty blindness*: when you ask
"are you sure?", a fresh confident reassurance tells you nothing either
direction — "yes, I'm sure" has exactly as much evidentiary value as the
original answer did. Re-asking for comfort is fine; re-asking to verify is
not — the check must land somewhere real (another source, another model,
or arithmetic you do yourself).

**Third**: the taxonomy is complete enough to *catch* mistakes but not to
*end* them. That's not pessimism; that's setting the right job. Nobody,
including the labs, has made a model that flags its own errors reliably —
so the job of catching them is distributed across tools and habits, starting
with yours.

## The catch columns in one sentence each

1. **Fabricated fact** — one load-bearing detail checked against a real
   source; the rest of the answer may be fine.
2. **Stale fact** — "when did this change?" matters more than "what is
   this?"
3. **Numeric slip** — your own brain on the arithmetic, or a calculator,
   beats an AI's fluency every time.
4. **Invented source** — an exact-phrase search takes 20 seconds and
   catches nearly all of them.
5. **Mangled quote** — same: quotation marks around the claimed words.
6. **Entity confusion** — one clarifying question to yourself: "did I ask
   about *this* one or *that* one?"
7. **Confident overreach** — treat every absolute as an invitation to ask
   for the exceptions.
8. **Sycophantic flip** — only neutral framing produces neutral answers.
9. **Scope error** — re-ask with your specifics in the prompt ("for
   Indiana law", "for type 2 diabetes", "for Linux Mint").
10. **Procedure drift** — trust the screen you're looking at over the
    screen it's describing.
11. **The missing "I don't know"** — ask where its answer is thin, not
    whether it is sure.
12. **Compounding** — when step 1 was wrong, stop patching; restart the
    chain.

## Where to worry most

If you remember nothing else from this table, remember the row-shape of
the danger zone:

| High risk | Lower risk |
| --- | --- |
| Rare or niche details | Common knowledge |
| Anything newer than the model cutoff | Old, settled facts |
| Numbers, dates, sums, counts | Narratives and concepts |
| Citations, quotes, "authorities" | Ideas you can test yourself today |
| Anything about *your* specific situation | General background context |

The left column is the checking list from chapter 04. The right column is
what makes AI *worth using*: 90% of its answers don't need a single check.

:::tip The two-second warmup
Before trusting any specific claim, run through three fingertips: is it
**rare**? is it **recent**? is it **numeric**? Any yes — slow down and use
a source-check from chapter 05. All no — enjoy your answer at full speed.
:::
