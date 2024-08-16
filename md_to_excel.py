import os
import re
from io import StringIO

import pandas as pd

PATH_TO_READ = "./pages"
PATH_TO_SAVE = "./tables"


def find_markdown_tables(text):
    find_markdown_tables_regex = re.compile(r"((?:\|.+\|(?:\n|\r))+)", re.MULTILINE)
    return find_markdown_tables_regex.findall(text)


def markdown_to_excel(text, page_number):
    markdown_tables = find_markdown_tables(text)

    if len(markdown_tables) > 0:
        for i, markdown_table in enumerate(markdown_tables):
            table_df = pd.read_csv(
                StringIO(markdown_table), sep="|", encoding="utf-8", engine="python"
            )
            table_df = table_df.dropna(how="all", axis=1)
            table_df = table_df.dropna(how="all", axis=0)
            table_df.to_excel(
                f"{PATH_TO_SAVE}/page_{page_number}_table_{i + 1}.xlsx", index=False
            )


pasta_paginas = ""
lista_paginas = sorted(os.listdir(pasta_paginas), key=len)
for i, page in enumerate(sorted(os.listdir(PATH_TO_READ), key=len)):
    print(page)
    with open(file=f"{PATH_TO_READ}/{page}", mode="r", encoding="utf-8") as f:
        markdown_to_excel(text=f.read(), page_number=i + 1)
