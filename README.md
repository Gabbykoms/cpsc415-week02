# Chat Client

A command-line Python chat client that sends questions to an AI model via OpenRouter and prints the answer, model name, token counts, and thinking effort label.

## How to run

Set your environment variables, then run:

```bash
export OPENROUTER_API_KEY=your-key-here
export CHAT_BASE_URL=https://openrouter.ai/api/v1   # optional
export CHAT_MODEL=openai/gpt-4o-mini                # optional
python3 chat.py
```

If `CHAT_BASE_URL` or `CHAT_MODEL` are not set, the program prints a notice and falls back to hardcoded defaults. `OPENROUTER_API_KEY` is required — requests will fail without it.

Type `quit` or press Ctrl+C to exit.

## Two corrections made to the intent draft

1. **Interaction style:** The draft described a single question-and-answer interaction. I changed it to a continuous conversation loop that keeps prompting until the user types `quit` or hits Ctrl+C.

2. **Thinking effort:** The draft did not include thinking effort at all. I added it because I'm used to setting thinking effort when running models locally in VS Code. The program asks the model to return a thinking effort label; if the model or API doesn't provide one, it honestly reports "No thinking effort label available" rather than guessing.

## One line explained

```python
thinking_effort = data["choices"][0]["message"].get("thinking_effort")
```

This reads the `thinking_effort` field directly from the model's response message. If the field is absent (most models don't return it), `.get()` returns `None` and the program falls back to the honest message.

## Model comparison

| Model | Answer style | Output tokens | Observed cost |
|---|---|---|---|
| `openai/gpt-4o-mini` | Prose paragraphs, conversational | 411 | $0.000249 |
| `google/gemini-3.1-flash-lite` | Structured bullet points, more concise | 839 | $0.00126 |

Both models answered the question "How good is an AI model for learning?" correctly, but Gemini leaned toward lists while GPT-4o-mini wrote in full sentences. Gemini used roughly twice as many output tokens and cost about 5x more for this question.

## Note on local models

A local model was not tested in this lab.
