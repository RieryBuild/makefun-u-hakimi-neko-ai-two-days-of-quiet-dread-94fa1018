import os

# Two Days of Quiet Dread — one code review comment, one line, quiet dread.
LINE = "LGTM. Nothing in here is wrong enough to block the release, and nothing ever is."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # exactly one line, no trailing newline: gate counts 1-140 chars
