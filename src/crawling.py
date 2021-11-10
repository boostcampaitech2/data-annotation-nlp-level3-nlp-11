import wikipediaapi
import argparse
import re
import ast
import os

from bs4 import BeautifulSoup


class Crawling:
    def __init__(self, args, page_names) -> None:
        self.args = args
        self.wiki_html_ko = wikipediaapi.Wikipedia(
            language="ko", extract_format=wikipediaapi.ExtractFormat.HTML
        )
        for i in page_names:
            self.run_crawling(i)

    def reg_replace(self, str):
        pattern = r"""<(?:"[^"]*"['"]*|'[^']*'['"]*|[^'">])+>"""
        str = re.sub(pattern, "", str)
        return str

    def run_crawling(self, page_name):
        p_html_ko = self.wiki_html_ko.page(page_name)
        soup = BeautifulSoup(p_html_ko.text)
        sentence_array = []
        p_result = []
        for i in soup.find_all("p"):
            p_result.append(self.reg_replace(str(i)))
        sentence_array.extend(p_result)
        for i in soup.find_all("li"):
            sub_str = self.reg_replace(str(i))
            sentence_array.append(sub_str)

        result = "\n".join(sentence_array)
        with open(f"{self.args.data_path}{page_name}.txt", "w") as f:
            f.write(result)
