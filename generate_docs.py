#!/usr/bin/env python3
import os
import yaml
from pathlib import Path

DOCS_PATH = "docs"
AUTO_DOCS_PREFIX = "_"

os.makedirs(DOCS_PATH, exist_ok=True)


def generate_docs_table_of_contents(md_data):
    toc = """
## Table of Contents

"""
    for line in md_data.split("\n"):
        fmts = ["#", "##", "###", "####", "#####", "######"]

        for fmt in fmts:
            if line.startswith(f"{fmt} "):
                title: str = line.split(fmt)[1]
                title_ref = title.replace(" ", "-").lower()
                if title_ref.startswith("-"):
                    title_ref = title_ref[1:]
                # if title_ref.endswith(":"):
                #     title_ref = title_ref[:-1]
                space = len(fmt) - 2
                toc += f"""{"  "*space}- [{title.lower().strip()}](#{title_ref.replace(":","")})\n"""
    return toc


def generate_docs(file):
    filename = f"{file}".split("/")[-1].split(".")[0]
    content = str()

    with open(file, "r") as f:
        data = yaml.safe_load(f)
        if "tasks" not in data:
            return

    for key, value in data["tasks"].items():
        _md = f"""## {key}\n\n"""
        _md += f"""{value["desc"]}\n\n"""

        _md += f"""#### Summary\n\n{value["summary"].strip()}\n"""

        # Add required variables
        if value.get("requires") and value["requires"].get("vars"):
            _md += f"""#### Required Variables\n\n"""
            for var in value["requires"]["vars"]:
                _md += f"""- **{var}**\n"""

        # Add variables
        if value.get("vars"):
            _md += f"""#### Variables\n\n"""
            for var in value["vars"]:
                _value = value["vars"][var]
                if not isinstance(_value, dict):
                    _md += f"""- **{var}**: `{_value}`\n"""
                # else:
                #     _md += f"""- **{var}**: `{_value["default"]}`\n"""
                # _md += f"""- **{var}**: `{value["vars"][var]}`\n"""

        content += _md + "\n\n"

    c = generate_docs_table_of_contents(content) + "\n\n" + content
    with open(f"{DOCS_PATH}/{AUTO_DOCS_PREFIX}{filename}.md", "w") as f:
        f.write(c)


def main():
    templates = Path("templates").rglob("*.yml")
    conf = ["./docs/init.md"]

    for template in templates:
        print(f"Generating docs for {template}...")
        generate_docs(template)

    print("\nGenerating documentation...\n")
    for i in conf:
        print(f"Copying {i}...")
        with open(i, "r") as f:
            init = f.read()

    with open("README.md", "w") as f:
        f.write(init + "\n\n")
        f.write("### Available Templates:\n\n")
        for file in Path(DOCS_PATH).rglob("*.md"):
            if file.stem.startswith(AUTO_DOCS_PREFIX):
                print(f"Adding {file} to README.md...")
                f.write(f"- [{file.stem[1:]}](./{DOCS_PATH}/{file.stem}.md)\n")
        # for file in Path(DOCS_PATH).rglob("*.md"):
        #     print(f"Adding {file} to README.md...")
        #     with open(file, "r") as r:
        #         content = r.read()
        #         f.write(content + "\n\n")


main()
