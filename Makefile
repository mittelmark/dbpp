##-*- makefile -*-############################################################
#
#  System        : 
#  Module        : 
#  Object Name   : $RCSfile$
#  Revision      : $Revision$
#  Date          : $Date$
#  Author        : $Author$
#  Created By    : Detlef Groth
#  Created       : Mon Jan 23 04:05:41 2023
#  Last Modified : <230123.0739>
#
#  Description	
#
#  Notes
#
#  History
#	
#  $Log$
#
##############################################################################
#
#  Copyright (c) 2023 Detlef Groth.
# 
#  All Rights Reserved.
# 
#  This  document  may  not, in  whole  or in  part, be  copied,  photocopied,
#  reproduced,  translated,  or  reduced to any  electronic  medium or machine
#  readable form without prior written consent from Detlef Groth.
#
##############################################################################


SOURCES = $(shell ls dbpp/widgets/*.py)
MKDOWN1 = $(patsubst %.py,%.md,$(SOURCES))
MKDOWN2 = $(shell echo $(MKDOWN1) | perl -pe 's/\//./g; ')
HTML    = $(patsubst %.md,%.html,$(MKDOWN2))


default: 
	echo $(SOURCES)
	echo $(MKDOWN2)
docs2: 
	rm -f docs/*.md docs/*.html
	pandoc header.md -o docs/header.html --lua-filter=lua-filters/links-to-html.lua
	lazydocs dbpp
	cd docs && for file in `ls *.md`; do cat ../header.md $$file > temp.md && mv temp.md dbpp.$$file && rm $$file; done
	cd docs && for file in `ls dbpp*.md` ; do pandoc $$file -o `basename $$file .md`.html -s -t HTML \
		--css pydoc.css --metadata title="Documentation `basename $$file .md`" \
		--lua-filter ../lua-filters/filter-kroki.lua \
		--lua-filter ../lua-filters/links-to-html.lua ; done
	cd docs && perl -i -pe 's/(img.+flat-square.)>/$$1 \/>/' *.md
	cd docs && perl -i -pe 's/(img.+flat-square.)>/$$1 \/>/' *.html
	cd docs && for file in `ls dbpp*.html`; do htmlark $$file -o temp.html && mv temp.html $$file; done

docs: docs/dbpp.widgets.TextMixins.html \
	  docs/dbpp.widgets.BaseClass.html \
	  docs/dbpp.widgets.StatusBar.html \
  	  docs/dbpp.widgets.Balloon.html \
  	  docs/dbpp.widgets.AutoScrollbar.html \
  	  docs/dbpp.widgets.Scrolled.html \
  	  docs/dbpp.widgets.LabEntry.html \
  	  docs/dbpp.widgets.TableView.html \
    	  docs/dbpp.widgets.TreeView.html \
    	  docs/dbpp.widgets.XTableView.html \
	  docs/dbpp.widgets.Ctext.html 
	  docs/SqlText.html	  

docs/dbpp.widgets.%.md: docs/dbpp/widgets/%.py header.md
	echo here
	echo $<	  

#docs/dbpp.widgets.TextMixins.html: dbpp/widgets/TextMixings.py header.md

#docs/dbpp.widgets.StatusBar.html: dbpp/widgets/StatusBar.py header.md

%.html: %.py header.md
	lazydocs $<
	cd docs && perl -ne '/img align.+right.+flat/ and next; print' $<.md > temp.md
	cd docs && pandoc temp.md -o `basename $< .py`.html --metadata title="`basename $< .py` documentation" \
		--metadata author="Detlef Groth, University of Potsdam" \
		--metadata date=`date +%Y-%m-%d` --css pydoc.css -s \
		-B ../header.html \
		--lua-filter ../../kroki/filter-kroki.lua \
		--lua-filter ../../kroki/filter-python.lua
	rm docs/$<.md
	rm docs/temp.md
