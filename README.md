# AI Phishing Email Detection — Senior Research Project
**Regan Cunningham | Eastern Connecticut State University**
*Presented at the CCSNE Conference and CREATE Conference — April 2026*

---

## Overview

Phishing emails remain one of the most prevalent and effective attack vectors in cybersecurity. This project investigates whether modern large language models (LLMs) can reliably detect phishing emails — and which one does it best.

Three popular LLMs were evaluated using a structured prompt designed to guide each model toward a binary phishing/not-phishing classification decision, along with a natural language explanation of its reasoning. Models were tested against a labeled dataset of real phishing and legitimate emails, and performance was measured using accuracy and confusion matrix analysis.

---

## Models Evaluated

- **ChatGPT-4** (OpenAI)
- **Gemini 1.5 Flash** (Google)
- **Microsoft Copilot**

---

## Methodology

Each model received the same structured prompt for every email sample, instructing it to classify the email as phishing or not phishing and provide a justification. No fine-tuning or additional training was applied — this study evaluates the models' out-of-the-box capability using prompt engineering alone.

### Prompt

The following prompt was used consistently across all three models:

<img width="608" height="376" alt="Figure 1 - Accuracy of LLMs in Detecting Phishing Emails" src="https://github.com/user-attachments/assets/11b1c2b1-dd5e-40db-97e8-368b673f9b21" />



---

## Datasets

| Dataset | Purpose | Source |
|---|---|---|
| **EPVME Dataset** | Phishing emails | [EPVME_1.zip on GitHub](https://github.com/sunknighteric/EPVME-Dataset/blob/main/EPVME_1.zip) |
| **Seven Phishing Email Datasets** | Legitimate (non-phishing) emails | [Figshare](https://figshare.com/articles/dataset/Seven_Phishing_Email_Datasets/25432108) |

---

## Results

### Accuracy

**Figure 1.** Accuracy of each LLM in detecting phishing emails. The bar chart below compares each model's overall classification accuracy.

<img width="738" height="474" alt="Prompt used for each LLM" src="https://github.com/user-attachments/assets/0edcddea-5f43-4de3-8a8c-ae2d79d56337" />

---

### Confusion Matrices

**Table 1.** Confusion matrix for each LLM, showing true positives, false positives, true negatives, and false negatives across all classifications.

<img width="383" height="564" alt="Table 1 - Confusion Matrices" src="https://github.com/user-attachments/assets/0d539b85-56a3-421b-a5f1-e5e78e209a42" />

---

### Example Output

**Figure 2.** A sample phishing email from the dataset alongside an example model explanation, illustrating how the LLMs reason through their classifications.

<img width="608" height="642" alt="Figure 2 - Example Screenshots" src="https://github.com/user-attachments/assets/19b0f788-9186-4820-87c8-78df07bb61bb" />

---

## Key Findings

- All three models demonstrated measurable ability (>90%) to identify phishing emails without any task-specific training.
- Performance varied across models, with differences visible in both accuracy rates and false positive/negative distributions.
- Prompt design played a significant role in eliciting consistent, structured responses from each model.

---

## Conference Presentations

This research was presented at two academic conferences in April 2026:

- **CCSNE** — Computing Conference for Students in New England
- **CREATE** — Conference for Research, Exploration, and Academic Transformation at ECSU

---

## Acknowledgments

Research conducted under the mentorship of **Prof. Garrett Dancik**, Department of Computer Science, Eastern Connecticut State University.
