# Data Structures & Algorithms Notebooks

This directory provides a systematic home for data structures, algorithms, and practice problems. Use one Notebook per topic instead of one file per problem: begin each topic with its concepts, reusable patterns, and common pitfalls, then collect related problems, solutions, and tests in the same Notebook.

## Directory Convention

```text
notebooks/
├── README.md
├── _templates/
│   └── topic_template.ipynb
└── binary_search/
    └── binary_search.ipynb
```

Future topic directories may include `arrays/`, `linked_lists/`, `stacks_and_queues/`, `trees/`, `graphs/`, `sorting/`, and `dynamic_programming/`. Each topic Notebook should contain learning goals, core concepts, reusable patterns, a problem index, problem summaries, key observations, solutions, complexity analysis, executable code, tests, mistake reviews, and a topic summary.

## Usage

Run `jupyter lab` or `jupyter notebook` from the repository root and open the relevant `.ipynb` file. Copy `_templates/topic_template.ipynb` when starting a new topic. To add a problem to an existing topic, copy the problem cell group from the template and append it to that topic's Notebook.

`binary_search/binary_search.ipynb` contains the Binary Search learning path, concise problem summaries, personal key questions, saved solutions, and executable tests.

## Answer and Practice Workflow

`binary_search/binary_search.ipynb` is the answer notebook. Its cells tagged `solution` retain completed implementations and are collapsed by default, while cells tagged `tests` remain separate.

Run the following command from the repository root whenever you want a clean practice copy:

```bash
make practice
```

This generates `binary_search/binary_search_practice.ipynb`. Every saved method implementation is replaced by `# TODO` and `pass`, while problem summaries, the key-question table, class and method signatures, and tests are preserved. Regeneration always overwrites the practice copy, never the answer notebook. Complete a problem in the practice copy, verify it with the following test cell, and then copy the final implementation back into the answer notebook before regenerating.
