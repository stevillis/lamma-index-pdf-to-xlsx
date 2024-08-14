from llama_parse import LlamaParse

pages = LlamaParse(
    result_type="markdown",
    parsing_instruction="""
    This file contains images and tables. I only want the tables of each page.
    Consider page 1 does not have any table.""",
).load_data("./DesempenhoFinanceiroPetrobras1T24.pdf")


for i, page in enumerate(pages):
    with open(f"pages/page{i+1}.md", "w", encoding="utf-8") as f:
        f.write(page.text)
