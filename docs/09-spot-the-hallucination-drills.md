# Spot-the-Hallucination Drills

Reading about verification is 20% of verification; practicing it is the
rest. This chapter gives you five ready-made drills — each one a small,
realistic scene with a plausible AI answer hiding a mistake from the
taxonomy. Guess the mistake and its type *before* you open the answer,
then compare.

Two rules make the drills work. **First**, play the whole thing at honest
speed: read the scene, say your guess out loud, then open. **Second**,
when you miss one, the win is naming where the knowledge *would come
from* — not feeling bad. Misses are the curriculum.

## Drill 1: The confident history

You ask for context on a quote for a family genealogy page, and get:

> "The phrase *'bloom where you are planted'* traces back to a sermon
> delivered in 1743 by Reverend Ezekiel Hartwell of Concord, Massachusetts,
> and was famously quoted by Abraham Lincoln during an 1858 debate in
> Galesburg."

Your move (before opening): what would you check first, and which mistake
type does it smell like?

:::details Answer
Three mistakes can hide in one flourish. The **specific attribution** (an
imagined 18th-century sermon by a semi-plausible minister) is a
fabricated fact (#1) — the phrase is a common saying with murky origins,
and a model asked *for a back-story* tends to produce the *shape* of one.
The **Lincoln** quote is a mangled/invented quote (#5): specific
speech-plus-date claims are pattern plumbing. And the whole thing is
**confident overreach** (#7) — "traces back to" implies settled history.

The catch: exact-quote search of each claim in quotation marks (chapter
05), and — for the Lincoln claim specifically — a library reference desk
or an archive collection. The correct genealogy-page wording is the
honest one: "the exact origin is debated; the earliest printed uses date
to the mid-1800s" — which is real, useful, and checkable.
:::

## Drill 2: The medical background

A conversation with an AI assistant about a relative's reflux, and you
get a neat paragraph to send along to the family group:

> "Proton-pump inhibitor short courses are certainly safe — a two-week
> course at full dose carries no meaningful interaction risks for
> ordinary adults, and everyone over 60 can simply double their dose
> without needing to inform their doctor."

Your move (before opening): does anything here need a check — or
something else entirely?

:::details Answer
This stacks three sins. **"Certainly safe" and "everyone"** are confident
overreach (#7) — medicine is never "certain"; the *dose adjustment for an
age group* is fabricated guidance (#1) pretending to be settled advice.
**"Without needing to inform their doctor"** is a row-4 delegation trap
(chapter 07) wearing friendly clothes: decisions to change treatment
never route through a chatbot. Sharp readers are now muttering "this is
exactly the kind of sentence the guide told me to route to the
pharmacist."

The catch: this one wasn't for checking — it was for not sending. The
calm family-chat version is honest and kind: "before trying anything,
one question for her pharmacist; let's ask this week." *Education only;
never medical advice* is the series' spine, and group chats are exactly
where sentence-shaped mistakes do their damage.
:::

## Drill 3: The invented citation

A work task: you asked for a source backing up a sentence for a report,
and got:

> "This claim appears in the *Journal of Consumer Psychology*, Vol. 41,
> Issue 3, in a 2024 study by Dr. Maren Voss et al., 'Preference Drift in
> Subscription Behavior' (pp. 312–341)."

Your move (before opening):....

:::details Answer
This is the classic invented citation (#4), and it's wearing its Sunday
clothes: a real journal name, plausible author, plausible page numbers —
the *anatomy* of a citation, which the model knows by heart. Note also
the 2024 date, which for most models with an earlier cutoff is itself
unverifiable — fresh years are exactly where the freshness gap lives.

The catch: the 15-second move from chapter 05 — search
*"Preference Drift in Subscription Behavior"* in **quotation marks**. A
real paper surfaces in seconds; a fabricated one surfaces as thin
silence, or just a copy of *this report's* sources. Then correct it with
a real source, or cut the sentence — any published claim in your report
deserves only real citations. If nothing real supports it, that's a topic
presented as observation, not citation, and your report is *better* that
way.
:::

## Drill 4: The stale procedure

You're helping a friend change a security setting on their phone, and
you get step instructions from the AI — crisp, numbered, plausible. On
the actual phone:

> "Go to Settings → Display → Battery → Auto-Darkness, toggle 'Smart
> Adapt,' then reboot twice for it to register."

Your move (before opening): which steps would you trust, and which one
can't be verified without the phone itself?

:::details Answer
Procedure drift (#10). The path has wrong names, one toggle that doesn't
exist, and that weird little flourish ("reboot twice") is a tell-tale sign
of *pattern completing*, not lived experience. This one isn't even
rare in style: most procedure answers on niche software settings are
built from a generic screen *shape*.

The catch: the guide's screen rule (chapter 05) — the phone in your hand
is the source of truth. When it can't be reconciled, the model's help
file or the manufacturer's current support page wins. Note the extra
diagnosis worth building: when the *screen-shape* answer is this far off,
every other setting-level answer from this session drops a row (chapter
03) until re-checked.
:::

## Drill 5: The agreeable echo

You say: "I'm pretty sure the water heater needs replacing, right? The
pilot light's been flaky for months." You get back:

> "Yes — a persistently unreliable pilot almost always means the tank is
> failing, and replacement is the right call. Expect $1,800–$2,200.
> Blindly attempting repairs typically makes things worse."

Your move (before opening): what did the model agree with, what do you
suspect is actually wrong, and who should make the final call?

:::details Answer
Sycophancy (#8) plus confident overreach (#7) plus a cost estimate with
precision gaps (#3). A flaky pilot is much more often a
*thermocouple* — a $20 part and a service visit — and "almost always
means the tank is failing" is exactly the sentence your echo invited. The
$1,800–2,200 range is pattern-shaped (that's a *typical* whole-tank
figure, but not necessarily *your* answer).

The catch: two moves. First, neutral re-framing — ask "what are the
*possible* causes of a flaky pilot, cheapest-to-dearest?" to reallocate
the model away from the flows you set; the cheaper, more likely answer
appears when you stop pulling for the expensive one. Second, before the
purchase, the row-3→4 line (chapter 07): a second-opinion call to an
actual plumber beats an AI's estimate *and* its "right call" verdict on
the same spend. This drill shows the model at its most useful too — as a
tool for educating you on *thermocouples*, with its verdicts disarmed.
:::

## Keep the drills alive: grooving your own set

Common drill sets get old; the best ones keep coming. Three easy sources
of your own:

- **Your saved moments.** The next five times you say "wait, that can't
  be right" — hold onto the screenshot or sentence. Each one is a drill
  that teaches the *genre* your week actually produces.
- **The family table game.** "I asked AI about ___ and it said ___ — what
  do we think?" runs at any age, has the kids spotting the load-bearing
  detail, and cases like drill 2 quietly build the whole house's
  checking reflex.
- **Deliberately redo an old ask.** Pick a question from last month, ask
  again in a fresh chat, and diff the two answers — a monthly ritual
  that doubles as a model-drift check (your spreadsheet problems may
  actually be freshness gaps).

A drill a week keeps the habit wearing in — and chapter 08's recovery
ladder means the misses cost minutes, not relationships.
