#!/usr/bin/env python3
"""Execute course notebooks in place, keeping their outputs.

    python3 tools/run_notebook.py Course_2_*/notebooks/s01_*.ipynb [more.ipynb ...]

Rules, matching the course conventions:
- A code cell whose first line contains "NOT RUN" is tagged "skip-execution" and is
  not executed (it needs a GPU, a download, an account or a library not installed).
- Every other code cell is executed top to bottom on the CPU. Any error stops the run
  and is reported with the cell number, so the notebook is never saved half-broken.
- The executed notebook must pass nbformat validation.

Exit status is non-zero if any notebook failed.
"""
from __future__ import annotations

import sys
import time

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

SKIP_TAG = "skip-execution"


def tag_not_run(nb) -> int:
    n = 0
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        first = cell.source.lstrip().splitlines()[0] if cell.source.strip() else ""
        tags = cell.metadata.setdefault("tags", [])
        if "NOT RUN" in first:
            if SKIP_TAG not in tags:
                tags.append(SKIP_TAG)
            cell.outputs = []
            cell.execution_count = None
            n += 1
        elif SKIP_TAG in tags:
            tags.remove(SKIP_TAG)
        if not tags:
            del cell.metadata["tags"]
    return n


def run(path: str, timeout: int = 900) -> bool:
    nb = nbformat.read(path, as_version=4)
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    skipped = tag_not_run(nb)
    client = NotebookClient(nb, timeout=timeout, kernel_name="python3",
                            skip_cells_with_tag=SKIP_TAG, allow_errors=False,
                            resources={"metadata": {"path": "."}})
    t0 = time.time()
    try:
        client.execute()
    except CellExecutionError as e:
        msg = str(e).strip().splitlines()
        print(f"FAIL {path} after {time.time() - t0:.0f}s\n  " + "\n  ".join(msg[-15:]))
        return False
    nbformat.validate(nb)
    nbformat.write(nb, path)
    code = sum(1 for c in nb.cells if c.cell_type == "code")
    print(f"OK   {path}: {code} code cells, {skipped} NOT RUN, {time.time() - t0:.0f}s")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    results = [run(p) for p in sys.argv[1:]]
    sys.exit(0 if all(results) else 1)
