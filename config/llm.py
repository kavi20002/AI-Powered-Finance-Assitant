from __future__ import annotations

from typing import Optional

try:
    from langchain_ollama import ChatOllama
except ImportError:
    ChatOllama = None


def get_llm(model: str = "llama3"):
    if ChatOllama is None:
        return None

    try:
        return ChatOllama(
            model=model,
            temperature=0.2,
            timeout=10,  # ✅ prevent hanging
        )
    except Exception:
        return None


def invoke_llm(prompt: str, model: str = "llama3") -> Optional[str]:
    llm = get_llm(model)

    if llm is None:
        return None

    try:
        response = llm.invoke(prompt)

        if isinstance(response, str):
            return response.strip()

        if hasattr(response, "content"):
            return response.content.strip()

        return str(response).strip()

    except Exception:
        return None