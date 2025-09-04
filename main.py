import time
import base64
from typing import Dict, Any, List
from pathlib import Path

import gradio as gr
from gradio_pdf import PDF
from utils import compile_pandoc_beamer
from bretonwiki import get_page
from llms import generate_slides_for_theme


def _build_payload(themes: List[str]) -> List[Dict[str, Any]]:
    """Build one JSON object per theme.

    Returns a list where each item contains the per-theme results
    (e.g., RI output and slide generation placeholder), along with
    suggested sections.
    """
    themes = [t.strip() for t in themes if (t or "").strip()]
    results: List[Dict[str, Any]] = []
    for theme in themes:
        content: str = get_page(theme, is_only_summary=True)
        slides = generate_slides_for_theme(content.encode("utf-8").decode("utf-8"))
        print(slides)
        results.append(
            {
                "theme": theme,
                "slides": slides,
            }
        )
    return results


def _to_markdown(items: List[Dict[str, Any]]) -> str:
    """Convert per-theme items to a single Markdown document."""
    if not items:
        return "# Aucun thème\n\nAucun thème fourni. Ajoutez au moins un thème."
    lines: List[str] = []
    for i, item in enumerate(items, start=1):
        theme = item.get("theme", f"Thème {i}")
        slides_raw = item.get("slides", "")
        # # Parse content inside ```markdown {CONTENT}```
        # if "```markdown" in slides_raw:
        #     start_marker = "```markdown"
        #     end_marker = "```"
        #     start_idx = slides_raw.find(start_marker)
        #     if start_idx != -1:
        #         start_idx += len(start_marker)
        #         end_idx = slides_raw.find(end_marker, start_idx)
        #         if end_idx != -1:
        #             slides = slides_raw[start_idx:end_idx].strip()
        #         else:
        #             slides = slides_raw[start_idx:].strip()
        #     else:
        #         slides = slides_raw
        # else:
        #     slides = slides_raw

        lines.append(f"## {theme}")
        lines.append("")
        lines.append(str())
        lines.append("")
        # Separator between themes
        lines.append("---")
        lines.append("")
    return "\n".join(lines).strip()


def generate_from_list(count: int, *themes: str) -> str:
    """Simulate a slow call returning a Markdown document for themes."""
    time.sleep(3)
    used = list(themes)[: max(1, int(count))]
    items = _build_payload(used)
    return _to_markdown(items)


ICON = (
    "https://openmoji.org/data/color/svg/1F3F4-E0066-E0072-E0062-E0072-E0065-E007F.svg"
)


ETAL_LOGO = "assets/ETAL_LOGO.png"


def get_image_as_base64(image_path: str) -> str:
    """Convert image to base64 string for embedding in HTML."""
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded_string}"
    except Exception as e:
        print(f"Error loading image: {e}")
        return ""


def build(md: str):
    pdf = compile_pandoc_beamer(md)
    return pdf, pdf  # (viewer path, download path)


# Set up static file serving for assets
gr.set_static_paths(paths=[Path.cwd() / "assets"])

with gr.Blocks(
    css="""
    #title { display:flex; align-items:center; gap:.5rem; margin:0 }
    #title img { height:1.25em; vertical-align:-.2em }
    """,
) as demo:
    gr.Markdown(
        f'''<h2 id="title"><img src="{ICON}" alt="Bretagne"> BrezhonRAG</h2> by SKIP<u>AI</u>LH'''
    )
    gr.Markdown(
        f'''
        <img src="{get_image_as_base64(ETAL_LOGO)}" alt="Logo ETAL 2025" style="display: inline; width: 3%;">

        **ETAL 2026** - École d'été en Traitement Automatique des Langues
        ''',
    )

    with gr.Row():
        with gr.Column(scale=3):
            MAX_ITEMS = 10
            themes_count = gr.State(1)
            theme_inputs = [
                gr.Textbox(
                    label=f"Thème {i + 1}",
                    placeholder="Entrez le thème…",
                    lines=1,
                    visible=(i == 0),
                )
                for i in range(MAX_ITEMS)
            ]

            with gr.Row():
                add_btn = gr.Button("+")
                remove_btn = gr.Button("-")
            with gr.Row():
                submit_btn = gr.Button("Générer les diapositives")

        with gr.Column(scale=1):
            json_in = gr.File(
                label="Importer des diapositives",
                file_types=[".json"],
                interactive=True,
            )
    with gr.Row():
        with gr.Column():
            out_md = gr.Textbox(
                label="Résultat (Markdown éditable)",
                lines=22,
                interactive=True,
                show_copy_button=True,
            )
        with gr.Column():
            viewer = PDF(label="Slides Preview", height=500)  # inline pdf.js viewer
            dl = gr.DownloadButton("Télécharger les diapositives", interactive=False)
            gen_btn = gr.Button("Générer les diapositives", interactive=False)
            gen_btn.click(build, inputs=[out_md], outputs=[viewer, dl])

    def show_uploaded_json(file):
        if not file:
            return gr.update()
        try:
            import json

            with open(file.name, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            # If reading/parsing fails, try to show raw content in a code block
            try:
                with open(file.name, "r", encoding="utf-8") as f:
                    raw = f.read()
                return f"```json\n{raw}\n```"
            except Exception:
                return f"Erreur lors de la lecture du JSON: {e.__class__.__name__}"

        # If the JSON matches our per-theme format, convert to Markdown
        if (
            isinstance(data, list)
            and data
            and isinstance(data[0], dict)
            and "theme" in data[0]
        ):
            try:
                return _to_markdown(data)  # type: ignore[arg-type]
            except Exception:
                pass
        # Fallback: pretty-print as fenced code so user can edit
        try:
            return (
                "```json\n" + json.dumps(data, ensure_ascii=False, indent=2) + "\n```"
            )
        except Exception:
            return str(data)

    def add_item(count: int):
        count = int(count)
        if count >= MAX_ITEMS:
            updates = [gr.update(visible=(i < count)) for i in range(MAX_ITEMS)]
            return count, *updates
        new_count = count + 1
        updates = [gr.update(visible=(i < new_count)) for i in range(MAX_ITEMS)]
        return new_count, *updates

    def remove_last(count: int, *values: str):
        count = int(count)
        if count <= 1:
            updates = [gr.update(visible=(i < count)) for i in range(MAX_ITEMS)]
            return count, *updates
        new_count = count - 1
        # Clear the value of the now-hidden last input
        updates = []
        for i in range(MAX_ITEMS):
            if i < new_count:
                updates.append(gr.update(visible=True))
            elif i == new_count:
                updates.append(gr.update(value="", visible=False))
            else:
                updates.append(gr.update(visible=False))
        return new_count, *updates

    # Enable/disable slide actions based on Markdown content
    def _toggle_slide_actions(md: str):
        enabled = bool((md or "").strip())
        return gr.update(interactive=enabled), gr.update(interactive=enabled)

    # Wire actions
    submit_btn.click(
        fn=generate_from_list,
        inputs=[themes_count, *theme_inputs],
        outputs=[out_md],
    )
    add_btn.click(
        fn=add_item,
        inputs=[themes_count],
        outputs=[themes_count, *theme_inputs],
    )
    remove_btn.click(
        fn=remove_last,
        inputs=[themes_count, *theme_inputs],
        outputs=[themes_count, *theme_inputs],
    )
    json_in.change(fn=show_uploaded_json, inputs=[json_in], outputs=[out_md])
    # Toggle Generate/Download buttons when Markdown changes
    out_md.change(fn=_toggle_slide_actions, inputs=[out_md], outputs=[gen_btn, dl])


if __name__ == "__main__":
    demo.launch(share=True, allowed_paths=[str(Path.cwd() / "assets")])
