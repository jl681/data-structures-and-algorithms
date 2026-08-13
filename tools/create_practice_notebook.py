#!/usr/bin/env python3
"""Generate a clean practice notebook from the answer notebook."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = REPOSITORY_ROOT / "notebooks/binary_search/binary_search.ipynb"
DEFAULT_OUTPUT = REPOSITORY_ROOT / "notebooks/binary_search/binary_search_practice.ipynb"


def replace_method_bodies_with_stubs(source: str) -> str:
    """Preserve class and method signatures while replacing implementations."""
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)
    methods: list[ast.FunctionDef | ast.AsyncFunctionDef] = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            methods.extend(
                child
                for child in node.body
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
            )

    for method in sorted(methods, key=lambda node: node.lineno, reverse=True):
        first_statement = method.body[0]
        indentation = " " * first_statement.col_offset
        stub = [
            f"{indentation}# TODO: Write your solution here.\n",
            f"{indentation}pass\n",
        ]
        lines[first_statement.lineno - 1 : method.end_lineno] = stub

    return "".join(lines)


def generate_practice_notebook(source_path: Path, output_path: Path) -> int:
    notebook = json.loads(source_path.read_text(encoding="utf-8"))
    replaced = 0

    for cell in notebook["cells"]:
        tags = cell.get("metadata", {}).get("tags", [])
        cell["execution_count"] = None if cell.get("cell_type") == "code" else cell.get("execution_count")
        if cell.get("cell_type") == "code":
            cell["outputs"] = []

        if cell.get("cell_type") != "code" or "solution" not in tags:
            continue

        source = "".join(cell.get("source", []))
        practice_source = replace_method_bodies_with_stubs(source)
        cell["source"] = practice_source.splitlines(keepends=True)
        cell["metadata"].pop("jupyter", None)
        cell["metadata"]["tags"] = ["practice"]
        replaced += 1

    notebook.setdefault("metadata", {})["dsa_notebook_type"] = "practice"
    notebook["metadata"]["generated_from"] = str(source_path.relative_to(REPOSITORY_ROOT))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    return replaced


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a solution-free DSA practice notebook."
    )
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    replaced = generate_practice_notebook(args.source.resolve(), args.output.resolve())
    print(f"Generated {args.output} with {replaced} blank solution cells.")


if __name__ == "__main__":
    main()
