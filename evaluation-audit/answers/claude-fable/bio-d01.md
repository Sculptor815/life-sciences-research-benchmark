# Claude Fable 5 / bio-d01

Original final answer, shared by both scoring rounds.

# Deconvolution study: target inhibition vs. substrate competition vs. reporter interference

## Recommended next action (lead conclusion)

Before any mechanistic kinetics, run two cheap counter-assays that the evidence already flags as decisive: (1) a **reporter-only assay** (coupling enzyme + authentic product + fluorophore, no target enzyme) with the compound, and (2) an **absorbance/fluorescence spectral scan** of the compound alone and spiked into a fixed fluorophore standard. D3 ("the compound absorbs near the excitation wavelength") makes an optical inner-filter artifact a live, high-prior hypothesis; it must be quantified and corrected before any claim of target inhibition can be interpreted. Only after the detection chain is cleared (or corrected) should you proceed to substrate-variation kinetics to separate target inhibition from substrate competition.

Note on terminology: "substrate competition" here is treated as **competitive inhibition at the target's substrate site** (compound and substrate compete), which is a *mode* of target engagement, distinguishable from non-/uncompetitive target inhibition and from reporter interference. If instead you mean the compound is itself an alternative substrate, the same substrate-variation and direct-product-detection arms resolve it (see Arm 4 and Alternatives).

---

## Evidence → inference → conclusion chain

| Evidence | Inference | Consequence for design |
|---|---|---|
| D1: single [S], 30-min endpoint | No information on substrate dependence or linearity; endpoint can hide depletion, lag phases, time-dependent inhibition, and coupling-enzyme saturation | Must determine Km, switch to kinetic (continuous) reads, and verify initial-rate linearity before mechanism can be assigned |
| D2: coupled detection via a second enzyme + fluorophore | Signal loss has ≥3 non-target explanations: inhibition of the coupling enzyme, reaction with/quenching of the fluorophore, or optical filtering | Reporter-only counterscreen and coupling-capacity titration are mandatory; an orthogonal (uncoupled) readout is the confirmatory arm |
| D3: compound absorbs near λ_ex | Primary inner-filter effect (attenuation of excitation light) can lower signal with no biochemistry at all; apparent "IC50" would track absorbance, not Ki | Measure A(λ_ex) and A(λ_em) across the compound titration; apply inner-filter correction or shift wavelengths; include fluorophore-standard + compound control |
| Purified target and reporter enzymes available | Each step of the cascade can be interrogated in isolation | Build the study as a factorial dissection of the cascade: optics → fluorophore → coupling enzyme → target enzyme → substrate site |

**Logical structure:** the fluorescence signal is the output of a chain: *target enzyme → product → coupling enzyme → fluorophore → photons*. A signal decrease is ambiguous among links. The study isolates each link with the compound present, working **backwards from the detector**, because an artifact at a downstream link invalidates all upstream interpretation. Only when downstream links are shown compound-insensitive (or quantitatively corrected) does a signal decrease license the conclusion "target inhibition," and only substrate-variation kinetics then licenses "competitive."

---

## Study design

### Phase 0 — Preparation, calibration and quality checks

Unknown parameters (not reported in evidence) and how to calibrate them — do **not** assume values:

1. **
