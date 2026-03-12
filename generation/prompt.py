def build_prompt(question,contexts):
    context_text="\n".join(contexts)
    prompt=f"""Answer the question using the context.

Context:
{context_text}

Question:
{question}

Answer:"""
    return prompt