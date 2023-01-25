##-*- makefile -*-############################################################

# pandoc and lazydocs required install it with:
#    sudo apt|dnf install pandoc
#    pip3 install lazydocs --user

AUTHOR="Detlef Groth, University of Potsdam"
HTMLS      := $(wildcard dbpp/kroki/*.py dbpp/widgets/*.py)
FILENAME   := "dbpp/widgets/GuiBaseClass.py"
BASENAME   := $(shell basename $(FILENAME))
MDFILEIN   := $(shell echo $(BASENAME).md)
MDFILEOUT  := $(shell echo $(FILENAME) | perl -pe 's/\//./g; s/.py/.md/')
HTMLFILE   := $(shell basename $(MDFILEOUT) .md).html
docu: 
	rm -f docs/*.md docs/*.html
	pandoc header.md -o docs/header.html --lua-filter=lua-filters/links-to-html.lua
	lazydocs dbpp
	cd docs && for file in `ls *.md`; do cat ../header.md $$file > temp.md && mv temp.md dbpp.$$file && rm $$file; done
	cd docs && for file in `ls dbpp*.md` ; do pandoc $$file -o `basename $$file .md`.html -s -t HTML \
		--css pydoc.css --metadata title="Documentation `basename $$file .md`" \
		--lua-filter ../lua-filters/filter-kroki.lua \
		--lua-filter ../lua-filters/links-to-html.lua ; done
	cd docs && perl -i -pe 's/(img.+flat-square.)>/$$1 \/>/' *.md
	cd docs && perl -i -pe 's/.+(img.+flat-square.)>//' *.html
	cd docs && for file in `ls dbpp*.html`; do htmlark $$file -o temp.html && mv temp.html $$file; done

lua-readme:
	cd lua-filters && pandoc README.md -o README.html --css pydoc.css -s \
		--lua-filter filter-python.lua --lua-filter filter-kroki.lua
	cd lua-filters && htmlark README.html -o temp.html
	cd lua-filters && mv temp.html README.html

single: docs/header.html header.md
	lazydocs $(FILENAME)
	cd docs && cat ../header.md $(MDFILEIN) > $(MDFILEOUT) && rm $(MDFILEIN)
	cd docs &&  pandoc $(MDFILEOUT) -o `basename $(MDFILEOUT) .md`.html -s -t HTML \
		--css pydoc.css --metadata title="Documentation `basename $(MDFILEOUT) .md`" \
		--metadata author=$(AUTHOR) \
		--metadata date="`date +%Y-%m-%d`" \
		--lua-filter ../lua-filters/filter-kroki.lua \
		--lua-filter ../lua-filters/links-to-html.lua 
	cd docs && perl -i -pe 's/(img.+flat-square.)>/$$1 \/>/' $(MDFILEOUT)
	cd docs && perl -i -pe 's/.+(img.+flat-square.)>.+//' $(HTMLFILE)
	
		
docs/header.html:
	pandoc header.md -o docs/header.html --lua-filter=lua-filters/links-to-html.lua
