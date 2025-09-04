from mistralai import Mistral

MISTRAL_API_KEY = "Qqd9RUesa31WLSg7zxQ2DnJSlhwKZfRG"
MISTRAL_MODEL = "mistral-small-2506"

CLIENT = Mistral(api_key=MISTRAL_API_KEY)
MODEL = MISTRAL_MODEL


def generate_slides_for_theme(theme: str) -> str:
    # ouvrir le fichier prompts/translate_prompt.txt
    with open("prompts/translate_prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()
    prompt = prompt.format(input=theme)

    chat_response = CLIENT.chat.complete(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "<<<START_SLIDES>>>\n", "prefix": True},
        ],
    )
    ctx = chat_response.choices[0].message.content
    slides = ctx.split("<<<START_SLIDES>>>")
    if len(slides) > 1:
        return slides[1]
    else:
        return ctx
