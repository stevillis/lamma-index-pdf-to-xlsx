from llama_parse import LlamaParse

pages = LlamaParse(
    result_type="markdown",
    parsing_instruction="""This file contains both images and tables. Please extract only the tables from each page.
    Note that each page may contain one or more tables.
    Keep in mind that page 1 does not contain any tables.
""",
).load_data("./DesempenhoFinanceiroPetrobras1T24.pdf")


for i, page in enumerate(pages):
    with open(f"pages/page{i+1}.md", "w", encoding="utf-8") as f:
        f.write(page.text)
