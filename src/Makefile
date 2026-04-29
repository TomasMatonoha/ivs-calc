KEEP_ITEMS = ../.git \
../.gitignore \
../debugging.png \
../hodnoceni.txt \
../manual.pdf \
../mockup \
../mockup/mockup-b.png \
../mockup/mockup-w.png \
../plan \
../plan/xschabt00_xpaterm00_xsubrtj00_xsamelm00_plan.txt \
../profiling \
../profiling/zprava.pdf \
../README.md \
../screenshot.png \
../xschabt00_xpaterm00_xsubrtj00_xsamelm00.zip \
../src \
calc_library.py \
Doxyfile \
gui_cal.py \
Makefile \
stddev \
data10.txt \
data1000.txt \
data1000000.txt \
tests_calc_library.py
ALL_ITEMS = $(filter-out ../. ../.. ../mockup/. ../mockup/.. ../plan/. ../plan/.. ../profiling/. ../profiling/.. . .., \
$(wildcard ../* ../.* ../mockup/* ../mockup/.* ../plan/*../plan/.* ../profiling/* ../profiling/.* * .*))
DELETE_ITEMS = $(filter-out $(KEEP_ITEMS), $(ALL_ITEMS))

PYTHON = python
PYTEST = .venv/bin/pytest

.PHONY: all pack clean test doc run stddev help
all: run
pack: clean
	@tar -cf ../repo.tar ..
	@mkdir -p ../repo
	@tar -xf ../repo.tar -C ../repo
	@rm ../repo.tar
	@$(MAKE) doc
	@$(PYTHON) -m venv .packvenv
	@.packvenv/bin/pip install -q pyinstaller
	@mkdir -p ../install
	@.packvenv/bin/pyinstaller --clean -y --onefile --name=ivs_calc --distpath ../install gui_cal.py
	@zip -rq "../xschabt00_xpaterm00_xsubrtj00_xsamelm00.zip" doc/ ../install/ ../repo/
	@$(MAKE) clean

clean:
	@echo $(DELETE_ITEMS)
	@rm -rf $(DELETE_ITEMS)
test: $(PYTEST)
	@$(PYTEST) tests_calc_library.py


$(PYTEST):
	@$(PYTHON) -m venv .venv
	@.venv/bin/pip install -q pytest

doc:
	@doxygen -q

run: gui_cal.py calc_library.py
	$(PYTHON) gui_cal.py

stddev:
	@(./stddev < data10.txt) > ../profiling/vystup.txt
	@(./stddev < data1000.txt) >> ../profiling/vystup.txt
	@(./stddev < data1000000.txt) >> ../profiling/vystup.txt
help:
	@echo "make { all pack clean test doc run stddev help }"
