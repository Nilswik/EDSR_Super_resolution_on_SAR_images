# mandatory for the term project for the course DIL 700 at University West

## EU AI Act Impact on This Project

The EU AI Act classifies AI systems into risk tiers based on their intended use and potential harm.

### Risk Classification

This project in its current form — academic research on a single SAR image — would fall under **minimal risk**. It makes no autonomous decisions affecting people and is not deployed in any real system.

### If Deployed in Practice

SAR imagery is heavily used in:

- Military surveillance and reconnaissance
- Border monitoring
- Disaster response and damage assessment

If this super-resolution model were used to enhance imagery for **automated surveillance or target recognition**, it could be reclassified as **high risk** under the EU AI Act, triggering requirements for:

- Human oversight mechanisms
- Conformity assessments before deployment
- Registration in the EU database of high-risk AI systems

to be noted it won't be used for any if this

### Technical Robustness Requirement

The Act requires AI systems to be technically robust and accurate. The limitations identified in this project — small training dataset, metric ceiling from speckle noise, single-scene generalisation - would need to be fully addressed and documented before any compliant deployment.

### Transparency

The most immediately applicable provision is the **transparency requirement** - developers must document training data, model design and known limitations. The report produced for this project already satisfies this in an academic context.

### Summary

As a research project it is largely unaffected, but any move toward real-world SAR surveillance applications would likely trigger high-risfk classification and signiicant compliance requirements.

### Formal Specifications

what i want to have done

1. **SP-01** — The model shall achieve a PSNR of at least 25 dB
on the validation set.
2. **SP-02** — The model shall achieve an SSIM of at least 0.40
on the validation set.
3. **SP-03** — The model shall produce output images at exactly
4× the spatial resolution of the input.
4. **SP-04** — The system shall process a 32×32 LR patch and
produce a 128×128 HR output without artefacts.
5. **SP-05** — Training shall be completed on a single consumer
GPU with 12 GB VRAM or less.
6. **SP-06** — The system shall handle single-channel SAR
amplitude imagery as input.
7. **SP-07** — Preprocessing shall reduce speckle noise
sufficiently to enable model convergence beyond the SLC baseline.

---

### Acceptance Test Procedures (ATPs)

| ID | Specification | Test | Pass Criteria | Result |
|---|---|---|---|---|
| ATP-01 | SP-01 | Evaluate model on validation set and record PSNR | PSNR ≥ 25 dB | 29.26 dB |
| ATP-02 | SP-02 | Evaluate model on validation set and record SSIM | SSIM ≥ 0.40 |  0.5667 |
| ATP-03 | SP-03 | Pass a 32×32 patch through the model and check output shape | Output shape = 128×128 |  Verified |
| ATP-04 | SP-04 | Visual inspection of output patches for blocking or ringing artefacts | No visible artefacts |  Passed |
| ATP-05 | SP-05 | Monitor VRAM usage during training | Peak VRAM ≤ 12 GB | RTX 4070 12 GB |
| ATP-06 | SP-06 | Confirm model accepts single channel input tensor | No runtime error on (B,1,H,W) input |  Verified |
| ATP-07 | SP-07 | Compare SLC vs multilook val PSNR | Multilook PSNR > SLC PSNR | +5.23 dB |


### Workload

Ive done this project Solo so ive done all the work

### Use of AI in this project

AI has been used in this project for discussing approaches, ides and debugging errors, since im new to PyTorch some help has been had with that but code is written by hand and my words are my own

### How to use

#### Requiremetns

pip install torch torchvision tifffile numpy matplotlib torchmetrics tqdm

Run the import shutil.py file and you'll get the tif files they are to big for github so you'll have to downlaod them your self.
