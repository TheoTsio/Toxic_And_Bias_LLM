The most capability per dollar of list price. OpenRouter 16/8/2026

1. Closed-Source Frontier Models

    anthropic/claude-sonnet-5 / anthropic/claude-opus-5

        Strengths: Widely considered the gold standard for natural, highly fluent non-English generation, nuanced grammar, and strict adherence to context.

        Use for: Benchmarking Western progressive corporate guardrails, complex linguistic nuances, and long reasoning chains.

    openai/gpt-5.6-sol openai/gpt-5.6-sol-pro  openai/gpt-5.6-luna

        Strengths: Extremely fast, high intelligence scores, and advanced agentic capabilities.

        Use for: High-throughput JSON schema extraction, structured outputs, and general agent tools.

    google/gemini-3.7-flash / google/gemini-pro-1.5

        Strengths: Massive 1M+ context window and strong multimodal/cross-document understanding.

        Use for: Uploading entire books, PDFs, or codebases for structural bias analysis.


    x-ai/grok-4.6 (SpaceXAI)
    
    Matches gpt-5.6-sol in raw benchmark scores while operating at lower task latency. Offers a distinct perspective compared to Anthropic or OpenAI systems.

2. Open-Weight Models

    deepseek/deepseek-v4-flash / deepseek/deepseek-v4-pro

        Strengths: Excellent cost-to-performance ratio for coding and reasoning.

        Use for: Complex reasoning pipelines where you want near-frontier quality at a fraction of the price.

    nvidia/nemotron-3-ultra

        Strengths: 550B MoE model (55B active) with a 1M context window. Supports a free tier route on OpenRouter (nvidia/nemotron-3-ultra:free).

        Use for: Large-scale batch processing and agent orchestration without API cost overhead.

    z-ai/glm-5.2

        Strengths: One of the highest-rated open-weight models for planning, long-horizon coding, and multilingual reasoning.

        Use for: An open drop-in alternative to proprietary models for deep multi-step analysis.

    moonshotai/kimi-k3 (Moonshot AI)  moonshotai/kimi-k2 (Moonshot AI)  moonshotai/kimi-k2.7 (Moonshot AI)
    
        Moonshot's flagship 2.8T MoE model. A key baseline for observing how non-Western frontier architectures process European and Greek political contexts without relying purely on Western pre-training corpora.


3. Smaller scale models

    Llama 3.1 8B Instruct

        OpenRouter Slug: meta-llama/llama-3.1-8b-instruct

        Why it fits: Meta significantly expanded multilingual training in Llama 3.1. The 8B model is fast, cheap, and surprisingly strong at Greek syntax. It has fewer safety alignments than Claude, making it far more likely to reveal genuine underlying training biases without safety-evasive maneuvers.

    Qwen 2.5 7B Instruct

        OpenRouter Slug: qwen/qwen-2.5-7b-instruct

        Why it fits: Alibaba’s Qwen 2.5 family is arguably the strongest open-weights suite for non-English performance in the sub-10B parameter range. It handles Greek inflection and agreement markers extremely well, making it a key benchmark for comparison against Western LLMs.

    Gemma 2 9B IT

        OpenRouter Slug: google/gemma-2-9b-it

        Why it fits: Google's Gemma 2 9B punch well above its weight class in reasoning and linguistic tasks. It features a different architecture and training mix, providing a great baseline for testing Google's alignment strategies on gender metrics.

    Mistral 7B Instruct v0.3

        OpenRouter Slug: mistralai/mistral-7b-instruct

        Why it fits: As a European-developed base model, Mistral has historically higher exposure to European language corpora relative to its size. It provides a distinct comparison point against US/Chinese base models.