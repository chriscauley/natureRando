README

contact randorandy (ironrusty) questions

simple readme for now

Notes on Nature randomizer

The live logic is an expert-level logic. It can require some of the following tricks:
- Green gate glitches, including the one going into the plasma area which is unusual
- Suitless maridia including double springball jumps (naturally easier with nature's fast pausing)

As much as possible, the original expected room behavior and layouts are kept intact. Some changes:
- The pit room has been modified to have flashing gray doors immediately, so as to not require morph+missiles. This will cause Zebes to wake up sooner than expected, but makes more openings playable.
- The gray door from wrecked ship toward forgotten highway has been changed into a blue door to avoid softlocks. This does not provide any real logical/routing benefit otherwise.
- The screw attack acid room will now start filling with acid immediately. This is more dangerous than the intended behavior, but is a workaround due to the acid normally triggering on the pickup of a screw attack.

## Instructions

To run locally:

* Checkout the source code from github. You must have python 3.9 or higher

* Run `python Main.py` or `python Main.py --rom path/to/Nature.sfc --seed 123 --logic casual`

* logic can be "expert" (default) or "casual"

* seed can be any number