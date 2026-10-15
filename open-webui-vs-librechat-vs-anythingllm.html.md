# Open WebUI vs LibreChat vs AnythingLLM (self-hosted chat UIs) | SelfHostAI

Source: https://andreiturcea-creator.github.io/selfhost-ai-dir/open-webui-vs-librechat-vs-anythingllm.html
Last updated: 2026-10-15


**Short answer:** Open WebUI is the usual ChatGPT-style UI for Ollama, LibreChat is best for mixing many API providers with agents, and AnythingLLM is built around chatting with your documents (RAG).

Last updated: 15 October 2026 · No tax figures on this site, so no GOV.UK check applies; tool details come from each project's public GitHub repository · [Markdown version](https://andreiturcea-creator.github.io/selfhost-ai-dir/open-webui-vs-librechat-vs-anythingllm.html.md)

|  | [Open WebUI](https://andreiturcea-creator.github.io/selfhost-ai-dir/tool-open-webui.html) | [LibreChat](https://andreiturcea-creator.github.io/selfhost-ai-dir/tool-librechat.html) | [AnythingLLM](https://andreiturcea-creator.github.io/selfhost-ai-dir/tool-anything-llm.html) |
|---|---|---|---|
| Focus | ChatGPT-style UI, Ollama-friendly | Multi-provider chat + agents | All-in-one RAG over documents |
| Licence (as listed) | BSD-3 | MIT | MIT |
| Repo | [open-webui](https://github.com/open-webui/open-webui) | [LibreChat](https://github.com/danny-avila/LibreChat) | [anything-llm](https://github.com/Mintplex-Labs/anything-llm) |

All three run in Docker on a modest VPS. The model runtime is the heavy part: see [runtimes compared](https://andreiturcea-creator.github.io/selfhost-ai-dir/ollama-vs-llama-cpp-vs-vllm.html). For document search at scale add [Qdrant](https://andreiturcea-creator.github.io/selfhost-ai-dir/tool-qdrant.html).

## Frequently asked questions

### Open WebUI or LibreChat?

Open WebUI is the usual choice alongside Ollama for a polished single-team UI. LibreChat is strong when you mix many API providers and want agents.

### What about chatting with my documents?

AnythingLLM is built around RAG over your files. Open WebUI also offers document features. For a vector database, see Qdrant.

### Which is fully MIT licensed?

LibreChat and AnythingLLM are listed as MIT. Open WebUI is listed as BSD-3; check its repository for any branding terms.
