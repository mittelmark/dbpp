##-*- makefile -*-############################################################

# pandoc and lazydocs required install it with:
#    sudo apt|dnf install pandoc
#    pip3 install lazydocs --user

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

