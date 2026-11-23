from pathlib import Path

LINE = "I didn't miss it. My pet-waste AI flagged your lone Cheeto as a biohazard, so I docked at 12% battery to file a formal incident report."
assert len(LINE) <= 200 and "\n" not in LINE

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(LINE, encoding="utf-8")
