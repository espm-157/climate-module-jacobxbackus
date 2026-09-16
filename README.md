[![Reproducibility Check](https://github.com/espm-157/climate-module-jacobxbackus/actions/workflows/main.yml/badge.svg)](https://github.com/espm-157/climate-module-jacobxbackus/actions/workflows/main.yml)

# Climate Data Analysis

Joseph Wong and Jacob Backus. We split the work evenly, used AI for the code, and wrote the explanations ourselves.

The notebook explores Mauna Loa CO₂, Arctic sea ice, EXIOBASE industrial output and emissions, and the Vostok ice-core record. It includes three figures, checks of missing values and units, measured memory comparisons, and a UK emissions comparison.

## Run the notebook

Use the course's Linux Jupyter environment with Python 3.11 and an internet connection. The course workflow uses Python 3.11.9. Keep `climate.ipynb`, `requirements.txt`, and `data/` together.

```bash
python -m pip install -r requirements.txt
```

Open `climate.ipynb`, restart the kernel, and run all cells in order. The large `Z` table is read directly from the public EXIOBASE Parquet source, so a fresh checkout does not need a local copy. The other inputs are stored in `data/` as September 8, 2026 snapshots.

The memory measurement uses Linux's `resource` counter. Run this notebook in the course environment or a Linux environment rather than native Windows Python.

## Files

| File | Purpose |
|---|---|
| `climate.ipynb` | Analysis, figures, verification blocks, and reflection |
| `requirements.txt` | Analysis and course-check dependencies |
| `data/` | Small source snapshots used by the notebook |
| `.github/workflows/main.yml` | Existing course reproducibility check |

Keep the instructor's workflow in place. It checks notebook execution with:

```bash
pytest --nbval-lax *.ipynb
```

Keep only the final assignment notebook at the repository root; put personal backup notebooks outside the repository. A green check confirms execution, while the notebook's source and numerical checks support the scientific results.

## Data and interpretation

| Data | Source |
|---|---|
| Mauna Loa TXT and CSV | [NOAA CO₂ trends](https://gml.noaa.gov/ccgg/trends/data.html) |
| Arctic monthly sea ice, all twelve files | [NSIDC Sea Ice Index v4](https://nsidc.org/data/g02135/versions/4) |
| EXIOBASE 2022: Z, Y, F, x, F_hh | [EXIOBASE 3.8.1](https://zenodo.org/records/4588235), [Parquet distribution](https://source.coop/youssef-harby/exiobase-3) |
| National CO₂ | [Our World in Data](https://github.com/owid/co2-data) |
| Vostok ice-core CO₂ | [Barnola et al., CDIAC record](https://doi.org/10.3334/CDIAC/ATG.009) |

The full-pandas and local Ibis benchmark results are actual measurements from the original run, retained for comparison. The current Ibis query includes remote access and reports this process's lifetime memory peak.

The UK comparison documents different emissions boundaries and EXIOBASE's projected 2022 values. Peat decay is excluded from the headline total, and the remaining UK discrepancy and Estonia outlier are reported explicitly. The ice-core comparison also keeps the sampling differences and gap between records visible.

EXIOBASE uses [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Retain the source credits and the original data terms. Further interpretation sources are linked in the notebook.
