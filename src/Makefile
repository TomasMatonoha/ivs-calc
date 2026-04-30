KEEP_ITEMS = ../.git \
../.gitignore \
../debugging.png \
../hodnoceni.txt \
../skutecnost.txt \
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
	@mkdir -p ../install/usr/bin ../install/debian
	@.packvenv/bin/pyinstaller --clean -y --onefile --name=ivs-calc --distpath ../install/usr/bin gui_cal.py

	@echo "Package: ivs-calc"          >  ../install/debian/control
	@echo "Section: utils"             >> ../install/debian/control
	@echo "Priority: optional"         >> ../install/debian/control
	@echo "Architecture: all"	>> ../install/debian/control
	@echo "Maintainer: Marek Samel <xsamelm00@fit.vut.cz>" >> ../install/debian/control
	@echo "Build-Depends: debhelper-compat (= 13), python3, python3-tk, zip" >> ../install/debian/control
	@echo "Standards-Version: 4.6.0" >> ../install/debian/control
	@echo "Description: GUI Calculator" >> ../install/debian/control
	@echo " A calculator application"   >> ../install/debian/control

	@echo "#!/usr/bin/make -f"         >  ../install/debian/rules
	@echo "%:"                        >> ../install/debian/rules
	@echo "	dh $$@"                  >> ../install/debian/rules
	@chmod +x ../install/debian/rules

	@echo "ivs-calc usr/bin/"         >  ../install/debian/install

	@zip -rq "../xschabt00_xpaterm00_xsubrtj00_xsamelm00.zip" doc/ ../install/ ../repo/
	@$(MAKE) clean

clean:
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
