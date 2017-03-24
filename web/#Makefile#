###
### This Makefile is for making the website only!
###

GITHUB_PAGES_BRANCH=gh-pages
THEME = hyde-y

MARKDOWN = python3 -m markdown
BASEDIR = .
LATEXDIR = $(BASEDIR)/../latex
DOCSDIR = $(BASEDIR)/content/docs
PAGEDIR = $(BASEDIR)/content/
LATEXIFY = python3 $(LATEXDIR)/utils/latexify.py

%.pdf: $(PAGEDIR)/ps/%.md
	$(LATEXIFY) $< > $(LATEXDIR)/temp-latex.md
	pandoc --read=markdown+raw_tex --template=$(LATEXDIR)/tlseminar.template $(LATEXDIR)/temp-latex.md -o $(DOCSDIR)/$@

%.pdf: $(PAGEDIR)/%.md
	$(LATEXIFY) $< > $(LATEXDIR)/temp-latex.md
	pandoc --read=markdown+raw_tex --template=$(LATEXDIR)/tlseminar.template $(LATEXDIR)/temp-latex.md -o $(DOCSDIR)/$@

%.pdf: $(PAGEDIR)/post/%.md
	$(LATEXIFY) $< > $(LATEXDIR)/temp-latex.md
	pandoc --read=markdown+raw_tex --template=$(LATEXDIR)/tlseminar.template $(LATEXDIR)/temp-latex.md -o $(DOCSDIR)/$@


html:
	hugo --theme=$(THEME)

develop:
	hugo server --theme=$(THEME) --buildDrafts --watch

github: html
	cp -r public/* ../
	git add -A; git commit -m "Rebuilt site" ; git push

.PHONY: html clean develop
