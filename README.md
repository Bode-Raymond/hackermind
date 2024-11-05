# HackerMind

HackerMind is a document query system that is specifically designed for querying some of the most popular cybersecurity knowledge base wikis. The information in these wikis cover many different topics and techniques in information security. More specifically, the majority of documents on these wikis are focused on offensive security concepts, techniques, and walkthroughs. The purpose of HackerMind is to provide an easily accessible interface for querying all of these information sources at once instead of searching through them individually. The successful implementation of HackerMind will allow for the near instantaneous retrieval of relevant information, which will save time in research allowing for users to spend more time completing tasks instead of researching techniques.

## Installation

1. Clone the repository and navigate to the hackermind directory:

```bash
git clone https://github.com/Bode-Raymond/hackermind.git
cd hackermind
```

2. Update git submodules

```bash
git submodule init
git submodule update
```

3. Create a python virtual environment using `Python 3.12` (Tested with Python 3.12, unknown if <3.12 works):

```bash
python -m venv venv
```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Parsing data from raw data sources:

```bash
python src/hackermind.py parse
```

Note: Raw data can be found in `./data/raw/`. Parsed documents are written to `./data/docs.json`

2. Analyzing parsed data for some basic statistics:

```bash
python src/hackermind.py analyze
```

Note: Graphical results are outputed to `./static/`

3. Run BM25 test:

```bash
python src/hackermind.py bm25
```

Note: Queries that are being tested can be found in `./data/queries.txt`. All output from the test goes to the command line.
