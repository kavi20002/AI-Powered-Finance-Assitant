from __future__ import annotations

from typing import Optional, Any

try:
    from langchain_community.chat_models import ChatOllama
except Exception:
    try:
        from langchain_community.chat_models.ollama import ChatOllama  # type: ignore
    except Exception:
        ChatOllama = None  # type: ignore


def get_llm(model: str = "llama3") -> Any | None:
    if ChatOllama is None:
        return None

    try:
        return ChatOllama(model=model, temperature=0.2)
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
        return getattr(response, "content", str(response)).strip()
    except Exception:
        return None