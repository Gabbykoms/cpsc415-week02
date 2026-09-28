# Verification Checks

| Check | Expected | Observed | Pass/fail |
|---|---|---|---|
| Question through OpenRouter | Answer + usage line | Got answer with model name, token counts, and thinking effort label | Pass |
| Usage record matches | Same model; same or close token counts | Dashboard token counts matched program output exactly | Pass |
| System prompt changed | Answer style changes accordingly | Changed from prose paragraphs to bullet points | Pass |
| `max_tokens` = 20 | Truncated or empty answer; tokens still billed | Answer truncated mid-sentence at 16 output tokens; tokens still billed on dashboard | Pass |
| Model swapped | Different model name in usage; answer may differ | Swapped from `openai/gpt-4o-mini` to `google/gemini-3.1-flash-lite`; dashboard reflected new model | Pass |
| Local model (optional) | Answer from localhost; no OpenRouter entry | Not tested | N/A |
