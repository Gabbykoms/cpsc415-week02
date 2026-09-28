# Intent: Python Chat Client

## Goal
A command-line Python program that prompts the user to type one question, sends it to an AI model via OpenRouter, and prints the answer, the model name, token counts, and a thinking effort label returned by the model.

## Who it is for
A developer or student who wants to query an AI model from the terminal without a web interface. Today they would have to open a browser or use a third-party app.

## Constraints
- Language: Python 3, standard library only — no pip install, no third-party packages.
- API: OpenRouter (base URL and model name from environment variables; key from `OPENROUTER_API_KEY`).
- Configuration: if any environment variable is missing, the program uses a hardcoded default and reports that it fell back to the default.
- Conversation loop: the program keeps prompting for questions and printing answers until the user quits (e.g. types "quit" or hits Ctrl+C).

## Not in scope
No explicit exclusions defined at this time.

## Success looks like
1. The program prompts for a question interactively, sends it, and prints the answer.
2. The model name and token counts printed by the program match what appears in the OpenRouter Activity dashboard for the same request.
3. If the model does not return a thinking effort label, the program honestly reports that no thinking effort label is available rather than guessing.

## Open questions
- What specific environment variable names should be used for the base URL and model? (Suggested: `CHAT_BASE_URL`, `CHAT_MODEL`, `OPENROUTER_API_KEY`.)
- What are the default values to fall back to if variables are missing?
- Does the thinking effort label come back in a standard response field, or does it vary by model?

**Approved by:** Gabriel Koomson, 09/28/26
