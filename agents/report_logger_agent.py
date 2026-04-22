from __future__ import annotations

from pathlib import Path
from time import perf_counter

from config.llm import invoke_llm
from config.pipeline_config import DEFAULT_MODEL
from state.shared_state import SharedState, add_trace
from tools.report_writer import build_report_markdown, write_report, write_trace_log

from tools.report_to_image import convert_md_to_image
from tools.report_to_html import convert_md_to_html
from tools.report_to_pdf import convert_html_to_pdf

class ReportLoggerAgent:
    def __init__(
            self,
            report_path: str,
            trace_path: str,
            prompt_path: str,
            model: str = DEFAULT_MODEL,
    ):
        self.report_path = report_path
        self.trace_path = trace_path
        self.prompt_path = prompt_path
        self.model = model

    def _load_prompt(self) -> str:
        return Path(self.prompt_path).read_text(encoding="utf-8").strip()

    def run(self, state: SharedState) -> SharedState:
        start = perf_counter()

        report_file = None
        trace_file = None

        try:
            report_content = build_report_markdown(state)

            prompt = self._load_prompt()
            llm_input = f"{prompt}\n\n{report_content}"
            llm_output = invoke_llm(llm_input, model=self.model)

            if llm_output:
                state["llm_report_refinement"] = llm_output  # just store

            final_report = report_content

            report_file = write_report(self.report_path, final_report)

            html_path = str(self.report_path).replace(".md", ".html")
            convert_md_to_html(report_file, html_path)

            image_path = str(self.report_path).replace(".md", ".png").replace("outputs", "docs")
            convert_md_to_image(report_file, image_path)
            state["report_image"] = image_path

            pdf_path = str(self.report_path).replace(".md", ".pdf").replace("outputs", "docs")
            convert_html_to_pdf(html_path, pdf_path)
            state["report_pdf"] = pdf_path

            add_trace(
                state,
                agent="ReportLoggerAgent",
                event="completed",
                details={
                    "report_path": report_file,
                    "image_path": image_path,
                    "pdf_path": pdf_path,
                    "duration_ms": round((perf_counter() - start) * 1000, 2),
                },
            )

            trace_file = write_trace_log(self.trace_path, state.get("trace", []))

            state["report_path"] = report_file
            state["trace_path"] = trace_file

            state["final_summary"] = (
                "✔ Expense tracking completed\n"
                "✔ Budget analysis completed\n"
                "✔ Savings plan generated\n"
                f"✔ Report created at: {report_file}\n"
                f"✔ Image report: {image_path}\n"
                f"✔ PDF report: {pdf_path}\n"
                "System executed successfully 🚀"
            )

        except Exception as exc:
            add_trace(
                state,
                agent="ReportLoggerAgent",
                event="failed",
                status="error",
                details={"error": str(exc)},
            )

            report_file = write_report(
                self.report_path,
                f"# Error Report\n\nSomething went wrong:\n{exc}",
            )

            trace_file = write_trace_log(self.trace_path, state.get("trace", []))

            state["report_path"] = report_file
            state["trace_path"] = trace_file

            state["final_summary"] = f"⚠️ Report generation failed: {exc}"

        return state