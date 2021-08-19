%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-filesystem
Version:        %{tl_version}
Release:        26
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1346:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etex.doc.tar.xz
Source2347:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontname.doc.tar.xz
Source7036:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-latex.tar.xz
Source7043:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-binextra.tar.xz
Source7101:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-context.tar.xz
Source7105:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-fontsextra.tar.xz
Source7106:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-fontsrecommended.tar.xz
Source7107:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-fontutils.tar.xz
Source7118:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-formatsextra.tar.xz
Source7123:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-games.tar.xz
Source7131:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-humanities.tar.xz
Source7134:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langarabic.tar.xz
Source7135:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langchinese.tar.xz
Source7136:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langcjk.tar.xz
Source7137:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langcyrillic.tar.xz
Source7139:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langczechslovak.tar.xz
Source7143:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langenglish.tar.xz
Source7144:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langeuropean.tar.xz
Source7145:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langfrench.tar.xz
Source7146:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langgerman.tar.xz
Source7147:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langgreek.tar.xz
Source7152:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langitalian.tar.xz
Source7153:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langjapanese.tar.xz
Source7159:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langkorean.tar.xz
Source7162:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langpolish.tar.xz
Source7164:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langportuguese.tar.xz
Source7165:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langspanish.tar.xz
Source7166:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-latexextra.tar.xz
Source7167:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-latexrecommended.tar.xz
Source7169:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-pictures.tar.xz
Source7184:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-luatex.tar.xz
Source7188:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-metapost.tar.xz
Source7189:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-music.tar.xz
Source7199:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-pstricks.tar.xz
Source7202:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-publishers.tar.xz
Source7206:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-xetex.tar.xz
Source7207:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-basic.tar.xz
Source7208:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-context.tar.xz
Source7210:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-gust.tar.xz
Source7211:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-medium.tar.xz
Source7212:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-minimal.tar.xz
Source7213:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/scheme-small.tar.xz
Source7613:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-plaingeneric.tar.xz
Source7614:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-mathscience.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-scheme-basic
Summary:        basic scheme (plain and latex)
Version:        svn25923.0
Requires:       texlive-base, texlive-collection-basic, texlive-collection-latex

%description -n  texlive-scheme-basic
This is the basic TeX Live scheme: it is a small set of files
sufficient to typeset plain TeX or LaTeX documents in
PostScript or PDF, using the Computer Modern fonts.  This
scheme corresponds to collection-basic and collection-latex.

%package -n texlive-scheme-context
Summary:        ConTeXt scheme
Version:        svn35799.0
Requires:       texlive-base, texlive-collection-context
Requires:       texlive-collection-metapost, tex-tex-gyre
Requires:       tex-tex-gyre-math, tex-antt, tex-iwona, tex-kurier
Requires:       tex-poltawski, tex-xits, tex-asana-math, tex-gentium-tug
Requires:       tex-pxfonts, tex-txfonts, tex-ccicons, tex-eulervm
Requires:       tex-manfnt-font, tex-marvosym, tex-mflogo-font, tex-wasy
Requires:       tex-ly1
Provides:       tex(context) = %{tl_version}
Obsoletes:      texlive-texmf-context < %{tl_version}

%description -n texlive-scheme-context
This is the TeX Live scheme for installing ConTeXt.

%package -n texlive-scheme-gust
Summary:        GUST TeX Live scheme
Version:        svn44177
Requires:       texlive-base, texlive-FAQ-en-doc, texlive-Type1fonts-doc, texlive-amslatex-primer-doc
Requires:       texlive-amstex, texlive-antt, texlive-bibtex8, texlive-comment
Requires:       texlive-comprehensive-doc, texlive-concrete
Requires:       texlive-cyklop, texlive-dvidvi, texlive-dviljk, texlive-gustprog-doc
Requires:       texlive-impatient-doc, texlive-iwona, texlive-metafont-beginners-doc, texlive-metapost-examples-doc
Requires:       texlive-poltawski, texlive-seetexk, texlive-seminar, texlive-tds-doc
Requires:       texlive-tex4ht, texlive-texdoc, texlive-collection-basic, texlive-collection-context
Requires:       texlive-collection-fontutils, texlive-collection-fontsrecommended
Requires:       texlive-collection-langpolish, texlive-collection-latex
Requires:       texlive-collection-latexrecommended, texlive-collection-metapost
Requires:       texlive-collection-plaingeneric, texlive-collection-texworks
Requires:       texlive-collection-xetex

%description -n texlive-scheme-gust
This is the GUST TeX Live scheme: it is a set of files
sufficient to typeset Polish plain TeX, LaTeX and ConTeXt
documents in PostScript or PDF.

%package -n texlive-scheme-medium
Summary:        medium scheme (small + more packages and languages)
Version:        svn44177
Requires:       texlive-base, texlive-collection-basic, texlive-collection-binextra, texlive-collection-context
Requires:       texlive-collection-fontsrecommended, texlive-collection-fontutils
Requires:       texlive-collection-langczechslovak, texlive-collection-langenglish
Requires:       texlive-collection-langeuropean, texlive-collection-langfrench
Requires:       texlive-collection-langgerman, texlive-collection-langitalian
Requires:       texlive-collection-langpolish, texlive-collection-langportuguese
Requires:       texlive-collection-langspanish, texlive-collection-latex
Requires:       texlive-collection-latexrecommended, texlive-collection-luatex
Requires:       texlive-collection-mathscience, texlive-collection-metapost
Requires:       texlive-collection-plaingeneric, texlive-collection-texworks
Requires:       texlive-collection-xetex

%description -n texlive-scheme-medium
This is the medium TeX Live collection: it contains plain TeX,
LaTeX, many recommended packages, and support for most European
languages.

%package -n texlive-scheme-minimal
Summary:        minimal scheme (plain only)
Version:        svn13822.0
Requires:       texlive-base, texlive-collection-basic

%description -n texlive-scheme-minimal
This is the minimal TeX Live scheme, with support for only
plain TeX. (No LaTeX macros.)  LuaTeX is included because Lua
scripts are used in TeX Live infrastructure.  This scheme
corresponds exactly to collection-basic.

%package -n texlive-scheme-small
Summary:        small scheme (basic + xetex, metapost, a few languages)
Version:        svn41825
Requires:       texlive-base, texlive-collection-basic, texlive-collection-latex, texlive-collection-latexrecommended
Requires:       texlive-collection-metapost, texlive-collection-xetex
Requires:       texlive-ec, texlive-eurosym, texlive-lm, texlive-lualibs
Requires:       texlive-luaotfload, texlive-luatexbase, texlive-revtex, texlive-synctex
Requires:       texlive-times, texlive-tipa, texlive-ulem, texlive-upquote
Requires:       texlive-zapfding, texlive-babel-basque, texlive-hyphen-basque, texlive-babel-czech
Requires:       texlive-hyphen-czech, texlive-babel-danish
Requires:       texlive-hyphen-danish, texlive-babel-dutch
Requires:       texlive-hyphen-dutch, texlive-babel-english
Requires:       texlive-hyphen-english, texlive-babel-finnish
Requires:       texlive-hyphen-finnish, texlive-babel-french
Requires:       texlive-hyphen-french, texlive-babel-german
Requires:       texlive-hyphen-german, texlive-babel-hungarian
Requires:       texlive-hyphen-hungarian, texlive-babel-italian
Requires:       texlive-hyphen-italian, texlive-babel-norsk
Requires:       texlive-hyphen-norwegian, texlive-babel-polish
Requires:       texlive-hyphen-polish, texlive-babel-portuges
Requires:       texlive-hyphen-portuguese, texlive-babel-spanish
Requires:       texlive-hyphen-spanish, texlive-babel-swedish
Requires:       texlive-hyphen-swedish

%description -n texlive-scheme-small
This is a small TeX Live scheme, corresponding to MacTeX's
BasicTeX variant.  It adds XeTeX, MetaPost, various
hyphenations, and some recommended packages to scheme-basic.

%package -n texlive-collection-basic
Summary:        Essential programs and files
Version:        svn45851
Requires:       texlive-base, texlive-texlive.infra, texlive-amsfonts, texlive-bibtex
Requires:       texlive-cm, texlive-dvipdfmx, texlive-dvips, texlive-enctex
Requires:       texlive-etex, texlive-etex-pkg, texlive-glyphlist, texlive-graphics-def
Requires:       texlive-gsftopk, texlive-hyph-utf8, texlive-hyphen-base, texlive-ifluatex
Requires:       texlive-ifxetex, texlive-knuth-lib, texlive-knuth-local, texlive-kpathsea
Requires:       texlive-lua-alt-getopt, texlive-luatex, texlive-makeindex, texlive-metafont
Requires:       texlive-mflogo, texlive-mfware, texlive-pdftex, texlive-plain
Requires:       texlive-tetex, texlive-tex, texlive-tex-ini-files, texlive-texlive-common-doc
Requires:       texlive-texlive-docindex, texlive-texlive-en
Requires:       texlive-texlive-msg-translations, texlive-texlive-scripts
Requires:       texlive-unicode-data, texlive-updmap-map
Requires:       texlive-xdvi
Provides:       tex(tex) = %{tl_version}, tex = %{tl_version}
Requires:       dvipdfmx, xdvik

%description -n texlive-collection-basic
These files are regarded as basic for any TeX system, covering
plain TeX macros, Computer Modern fonts, and configuration for
common drivers; no LaTeX.

%package -n texlive-collection-bibtexextra
Summary:        BibTeX additional styles
Version:        svn47839
Requires:       texlive-base, texlive-collection-latex, texlive-aichej, texlive-ajl
Requires:       texlive-amsrefs, texlive-apacite, texlive-apalike2, texlive-archaeologie
Requires:       texlive-beebe, texlive-besjournals, texlive-bestpapers, texlive-bib2gls
Requires:       texlive-bibarts, texlive-bibexport, texlive-bibhtml, texlive-biblatex
Requires:       texlive-biblatex-abnt, texlive-biblatex-anonymous
Requires:       texlive-biblatex-archaeology, texlive-biblatex-arthistory-bonn
Requires:       texlive-biblatex-apa, texlive-biblatex-bookinarticle
Requires:       texlive-biblatex-bookinother, texlive-biblatex-bwl
Requires:       texlive-biblatex-caspervector, texlive-biblatex-chem
Requires:       texlive-biblatex-chicago, texlive-biblatex-claves
Requires:       texlive-biblatex-dw, texlive-biblatex-enc
Requires:       texlive-biblatex-fiwi, texlive-biblatex-gb7714-2015
Requires:       texlive-biblatex-gost, texlive-biblatex-historian
Requires:       texlive-biblatex-ieee, texlive-biblatex-ijsra
Requires:       texlive-biblatex-iso690, texlive-biblatex-juradiss
Requires:       texlive-biblatex-lni, texlive-biblatex-luh-ipw
Requires:       texlive-biblatex-manuscripts-philology, texlive-biblatex-mla
Requires:       texlive-biblatex-morenames, texlive-biblatex-multiple-dm
Requires:       texlive-biblatex-musuos, texlive-biblatex-nature
Requires:       texlive-biblatex-nejm, texlive-biblatex-nottsclassic
Requires:       texlive-biblatex-opcit-booktitle, texlive-biblatex-oxref
Requires:       texlive-biblatex-philosophy, texlive-biblatex-phys
Requires:       texlive-biblatex-publist, texlive-biblatex-realauthor
Requires:       texlive-biblatex-sbl, texlive-biblatex-science
Requires:       texlive-biblatex-shortfields, texlive-biblatex-socialscienceshuberlin
Requires:       texlive-biblatex-source-division, texlive-biblatex-subseries
Requires:       texlive-biblatex-swiss-legal, texlive-biblatex-trad
Requires:       texlive-biblatex-true-citepages-omit, texlive-biblist
Requires:       texlive-bibtexperllibs, texlive-bibtopic
Requires:       texlive-bibtopicprefix, texlive-bibunits
Requires:       texlive-biolett-bst, texlive-bookdb, texlive-breakcites, texlive-cell
Requires:       texlive-chbibref, texlive-chicago, texlive-chicago-annote, texlive-chembst
Requires:       texlive-chscite, texlive-citeall, texlive-citeref, texlive-collref
Requires:       texlive-compactbib, texlive-crossrefware
Requires:       texlive-custom-bib, texlive-din1505, texlive-dk-bib, texlive-doipubmed
Requires:       texlive-ecobiblatex, texlive-economic, texlive-fbs, texlive-figbib
Requires:       texlive-footbib, texlive-francais-bst, texlive-gbt7714, texlive-geschichtsfrkl
Requires:       texlive-harvard, texlive-harvmac, texlive-historische-zeitschrift, texlive-ietfbibs-doc
Requires:       texlive-ijqc, texlive-inlinebib, texlive-iopart-num, texlive-jneurosci
Requires:       texlive-jurabib, texlive-ksfh_nat, texlive-ltb2bib, texlive-listbib
Requires:       texlive-logreq, texlive-luabibentry, texlive-margbib, texlive-multibib
Requires:       texlive-multibibliography, texlive-munich
Requires:       texlive-nar, texlive-nmbib, texlive-notes2bib, texlive-notex-bst
Requires:       texlive-oscola, texlive-perception, texlive-pnas2009, texlive-rsc
Requires:       texlive-showtags, texlive-sort-by-letters
Requires:       texlive-splitbib, texlive-turabian-formatting
Requires:       texlive-uni-wtal-ger, texlive-uni-wtal-lin
Requires:       texlive-urlbst, texlive-usebib, texlive-vak, texlive-xcite

%description -n texlive-collection-bibtexextra
Additional BibTeX styles and bibliography data(bases), notably
including BibLaTeX.

%package -n texlive-collection-binextra
Summary:        TeX auxiliary programs
Version:        svn47945
Requires:       texlive-base, texlive-collection-basic, texlive-a2ping, texlive-adhocfilelist
Requires:       texlive-arara, asymptote, texlive-bibtex8, texlive-bibtexu
Requires:       texlive-bundledoc, texlive-checklistings
Requires:       texlive-chktex, texlive-ctan-o-mat, texlive-ctan_chk-doc, texlive-ctanify
Requires:       texlive-ctanupload, texlive-ctie, texlive-cweb, texlive-de-macro
Requires:       texlive-detex, texlive-dtl, texlive-dtxgen, texlive-dvi2tty
Requires:       texlive-dviasm, texlive-dvicopy, texlive-dvidvi, texlive-dviinfox
Requires:       texlive-dviljk, texlive-dvipng, texlive-dvipos, texlive-dvisvgm
Requires:       texlive-findhyph, texlive-fragmaster, texlive-hook-pre-commit-pkg-doc, texlive-hyphenex
Requires:       texlive-installfont, texlive-lacheck, texlive-latex-git-log, texlive-latex-papersize
Requires:       texlive-latex2man, texlive-latex2nemeth, texlive-latexdiff, texlive-latexfileversion
Requires:       latexmk, texlive-latexpand, texlive-latexindent, texlive-ltxfileinfo
Requires:       texlive-ltximg, texlive-listings-ext, texlive-make4ht, texlive-match_parens
Requires:       texlive-mflua, texlive-mkjobtexmf, texlive-patgen, texlive-pdfbook2
Requires:       texlive-pdfcrop, texlive-pdfjam, texlive-pdflatexpicscale, texlive-pdftools
Requires:       texlive-pdfxup, texlive-pfarrei, texlive-pkfix, texlive-pkfix-helper
Requires:       texlive-purifyeps, texlive-pythontex, texlive-seetexk, texlive-srcredact
Requires:       texlive-sty2dtx, texlive-synctex, texlive-tex4ebook, texlive-texcount
Requires:       texlive-texdef, texlive-texdiff, texlive-texdirflatten, texlive-texdoc
Requires:       texlive-texdoctk, texlive-texfot, texlive-texliveonfly, texlive-texloganalyser
Requires:       texlive-texosquery, texlive-texware, texlive-tie, texlive-tpic2pdftex
Requires:       texlive-typeoutfileinfo, texlive-web, dvipng
Obsoletes:      texlive-utils < %{tl_version}

%description -n texlive-collection-binextra
Various useful, but non-essential, support programs. Includes
programs and macros for DVI file manipulation, literate
programming, patgen, and the TeX Works Editor.

%package -n texlive-collection-context
Summary:        ConTeXt and packages
Version:        svn47139
Requires:       texlive-base, texlive-collection-basic, texlive-context, texlive-jmn
Requires:       texlive-context-account, texlive-context-algorithmic
Requires:       texlive-context-animation, texlive-context-annotation
Requires:       texlive-context-bnf, texlive-context-chromato
Requires:       texlive-context-cmscbf, texlive-context-cmttbf
Requires:       texlive-context-construction-plan, texlive-context-cyrillicnumbers
Requires:       texlive-context-degrade, texlive-context-fancybreak
Requires:       texlive-context-filter, texlive-context-french
Requires:       texlive-context-fullpage, texlive-context-gantt
Requires:       texlive-context-gnuplot, texlive-context-handlecsv
Requires:       texlive-context-inifile, texlive-context-layout
Requires:       texlive-context-letter, texlive-context-lettrine
Requires:       texlive-context-mathsets, texlive-context-notes-zh-cn
Requires:       texlive-context-rst, texlive-context-ruby
Requires:       texlive-context-simplefonts, texlive-context-simpleslides
Requires:       texlive-context-title, texlive-context-transliterator
Requires:       texlive-context-typearea, texlive-context-typescripts
Requires:       texlive-context-vim, texlive-context-visualcounter

%description -n texlive-collection-context
Hans Hagen's powerful ConTeXt system, http://pragma-ade.com.
Also includes third-party ConTeXt packages.

%package -n texlive-collection-fontsextra
Summary:        Additional fonts
Version:        svn47656
Requires:       texlive-base, texlive-collection-basic, texlive-asana-math, texlive-academicons
Requires:       texlive-accanthis, texlive-adforn, texlive-adfsymbols, texlive-aecc
Requires:       texlive-alegreya, texlive-algolrevived, texlive-allrunes, texlive-almfixed
Requires:       texlive-anonymouspro, texlive-antiqua, texlive-antt, texlive-archaic
Requires:       texlive-arev, texlive-arimo, texlive-asapsym, texlive-ascii-font
Requires:       texlive-aspectratio, texlive-astro, texlive-augie, texlive-auncial-new
Requires:       texlive-aurical, texlive-b1encoding, texlive-barcodes, texlive-baskervald
Requires:       texlive-baskervaldx, texlive-baskervillef
Requires:       texlive-bbding, texlive-bbm, texlive-bbm-macros, texlive-bbold
Requires:       texlive-bbold-type1, texlive-belleek, texlive-bera, texlive-berenisadf
Requires:       texlive-beuron, texlive-bguq, texlive-blacklettert1, texlive-boisik
Requires:       texlive-bookhands, texlive-boondox, texlive-braille, texlive-brushscr
Requires:       texlive-cabin, texlive-caladea, texlive-calligra, texlive-calligra-type1
Requires:       texlive-cantarell, texlive-carlito, texlive-carolmin-ps, texlive-ccicons
Requires:       texlive-cfr-initials, texlive-cfr-lm, texlive-cherokee, texlive-chivo
Requires:       texlive-cinzel, texlive-clearsans, texlive-cm-lgc, texlive-cm-mf-extra-bold
Requires:       texlive-cm-unicode, texlive-cmbright, texlive-cmexb, texlive-cmll
Requires:       texlive-cmpica, texlive-cmsrb, texlive-cmtiup, texlive-cochineal
Requires:       texlive-comfortaa, texlive-comicneue, texlive-concmath-fonts, texlive-cookingsymbols
Requires:       texlive-cormorantgaramond, texlive-countriesofeurope
Requires:       texlive-courier-scaled, texlive-crimson, texlive-cryst, texlive-cyklop
Requires:       texlive-dancers, texlive-dantelogo, texlive-dejavu, texlive-dejavu-otf
Requires:       texlive-dice, texlive-dictsym, texlive-dingbat, texlive-doublestroke
Requires:       texlive-dozenal, texlive-drm, texlive-droid, texlive-dsserif
Requires:       texlive-duerer, texlive-duerer-latex, texlive-dutchcal, texlive-ean
Requires:       texlive-ebgaramond, texlive-ebgaramond-maths
Requires:       texlive-ecc, texlive-eco, texlive-eiad, texlive-eiad-ltx
Requires:       texlive-electrum, texlive-elvish, texlive-epigrafica, texlive-epsdice
Requires:       texlive-erewhon, texlive-esrelation, texlive-esstix, texlive-esvect
Requires:       texlive-eulervm, texlive-euxm, texlive-fbb, texlive-fdsymbol
Requires:       texlive-fetamont, texlive-feyn, texlive-fge, texlive-fira
Requires:       texlive-foekfont, texlive-fonetika, texlive-fontawesome, texlive-fontawesome5
Requires:       texlive-fontmfizz, texlive-fonts-churchslavonic
Requires:       texlive-fourier, texlive-fouriernc, texlive-frcursive, texlive-frederika2016
Requires:       texlive-genealogy, texlive-gentium-tug, texlive-gfsartemisia, texlive-gfsbodoni
Requires:       texlive-gfscomplutum, texlive-gfsdidot, texlive-gfsneohellenic, texlive-gfsneohellenicmath
Requires:       texlive-gfssolomos, texlive-gillcm, texlive-gillius, texlive-gnu-freefont
Requires:       texlive-gofonts, texlive-gothic, texlive-greenpoint, texlive-grotesq
Requires:       texlive-hacm, texlive-hands, texlive-heuristica, texlive-hfbright
Requires:       texlive-hfoldsty, texlive-ifsym, texlive-imfellenglish, texlive-inconsolata
Requires:       texlive-initials, texlive-ipaex-type1, texlive-iwona, texlive-jablantile
Requires:       texlive-jamtimes, texlive-junicode, texlive-kixfont, texlive-kpfonts
Requires:       texlive-kurier, texlive-lato, texlive-lfb, texlive-libertine
Requires:       texlive-libertinegc, texlive-libertinus, texlive-libertinus-otf, texlive-libertinust1math
Requires:       texlive-librebaskerville, texlive-librebodoni
Requires:       texlive-librecaslon, texlive-libris, texlive-lineara, texlive-lobster2
Requires:       texlive-lxfonts, texlive-ly1, texlive-mathabx, texlive-mathabx-type1
Requires:       texlive-mathdesign, texlive-mdputu, texlive-mdsymbol, texlive-merriweather
Requires:       texlive-miama, texlive-mintspirit, texlive-missaali, texlive-mnsymbol
Requires:       texlive-montserrat, texlive-mweights, texlive-newpx, texlive-newtx
Requires:       texlive-newtxsf, texlive-newtxtt, texlive-niceframe-type1, texlive-nimbus15
Requires:       texlive-nkarta, texlive-noto, texlive-obnov, texlive-ocherokee
Requires:       texlive-ocr-b, texlive-ocr-b-outline, texlive-ogham, texlive-oinuit
Requires:       texlive-old-arrows, texlive-oldlatin, texlive-oldstandard, texlive-opensans
Requires:       texlive-orkhun, texlive-overlock, texlive-pacioli, texlive-paratype
Requires:       texlive-phaistos, texlive-phonetic, texlive-pigpen, texlive-playfair
Requires:       texlive-plex, texlive-plex-otf, texlive-poltawski, texlive-prodint
Requires:       texlive-punk, texlive-punk-latex, texlive-punknova, texlive-pxtxalfa
Requires:       texlive-quattrocento, texlive-raleway, texlive-recycle, texlive-roboto
Requires:       texlive-romande, texlive-rosario, texlive-rsfso, texlive-sansmathaccent
Requires:       texlive-sansmathfonts, texlive-sauter, texlive-sauterfonts, texlive-schulschriften
Requires:       texlive-semaphor, texlive-shobhika, texlive-skull, texlive-sourcecodepro
Requires:       texlive-sourcesanspro, texlive-sourceserifpro
Requires:       texlive-starfont, texlive-staves, texlive-stickstoo, texlive-stix
Requires:       texlive-stix2-otf, texlive-stix2-type1, texlive-superiors, texlive-svrsymbols
Requires:       texlive-tapir, texlive-tempora, texlive-tengwarscript, texlive-tfrupee
Requires:       texlive-tinos, texlive-tpslifonts, texlive-trajan, texlive-txfontsb
Requires:       texlive-txuprcal, texlive-typicons, texlive-umtypewriter, texlive-universa
Requires:       texlive-universalis, texlive-uppunctlm, texlive-urwchancal
Requires:       texlive-xcharter, texlive-xits, texlive-yfonts
Requires:       texlive-yfonts-t1, texlive-yinit-otf, texlive-zlmtt

%description -n texlive-collection-fontsextra
collection-fontsextra package

%package -n texlive-collection-fontsrecommended
Summary:        Recommended fonts
Version:        svn35830.0
Requires:       texlive-base, texlive-collection-basic, tex-avantgar, tex-bookman
Requires:       tex-charter, tex-cm-super, tex-cmextra, tex-courier
Requires:       tex-ec, tex-euro, texlive-euro-ce, tex-eurosym
Requires:       tex-fpl, tex-helvetic, tex-lm, tex-lm-math
Requires:       tex-marvosym, tex-mathpazo, tex-manfnt-font, tex-mflogo-font
Requires:       tex-ncntrsbk, tex-palatino, tex-pxfonts, tex-rsfs
Requires:       tex-symbol, tex-tex-gyre, tex-tex-gyre-math, tex-times
Requires:       tex-tipa, tex-txfonts, tex-utopia, tex-wasy
Requires:       tex-wasy2-ps, tex-wasysym, tex-zapfchan, tex-zapfding
Provides:       tetex-fonts = 3.1-99
Obsoletes:      tetex-fonts < 3.1-99
Provides:       texlive-texmf-fonts = %{tl_version}
Obsoletes:      texlive-texmf-fonts < %{tl_version}

%description -n texlive-collection-fontsrecommended
Recommended fonts, including the base 35 PostScript fonts,
Latin Modern, TeX Gyre, and T1 and other encoding support for
Computer Modern, in outline form.

%package -n texlive-collection-fontutils
Summary:        Graphics and font utilities
Version:        svn37105.0
Requires:       texlive-base, texlive-collection-basic, tex-accfonts, tex-afm2pl
Requires:       tex-dosepsbin, tex-epstopdf, tex-fontware, tex-lcdftypetools
Requires:       tex-ps2pk, tex-pstools, tex-dvipsconfig, tex-fontinst
Requires:       tex-fontools, tex-mf2pt1, tex-ttfutils, t1utils, psutils

%description -n texlive-collection-fontutils
Programs for conversion between font formats, testing fonts,
virtual fonts, .gf and .pk manipulation, mft, fontinst, etc.
Manipulating OpenType, TrueType, Type 1,and for manipulation of
PostScript and other image formats.

%package -n texlive-collection-formatsextra
Summary:        Additional formats
Version:        svn44177
Provides:       texlive-collection-htmlxml = %{epoch}:svn35743.0.obsolete
Obsoletes:      texlive-collection-htmlxml <= 6:svn35743.0
Provides:       texlive-collection-omega = %{epoch}:svn30388.0.obsolete
Obsoletes:      texlive-collection-omega <= 6:svn30388.0
Requires:       texlive-aleph, texlive-antomega, texlive-base, texlive-collection-basic
Requires:       texlive-collection-latex, texlive-edmac, texlive-eplain, texlive-jadetex
Requires:       texlive-lambda, texlive-lollipop, texlive-mltex, texlive-mxedruli
Requires:       texlive-omega, texlive-omegaware, texlive-otibet, texlive-passivetex
Requires:       texlive-psizzl, texlive-startex, texlive-texsis, texlive-xmltex
Requires:       texlive-xmltexconfig

%description -n texlive-collection-formatsextra
Collected TeX `formats', i.e., large-scale macro packages
designed to be dumped into .fmt files -- excluding the most
common ones, such as latex and context, which have their own
package(s).

%package -n texlive-collection-games
Summary:        Games typesetting
Version:        svn47828
Requires:       texlive-base, texlive-collection-latex, texlive-bartel-chess-fonts, texlive-chess
Requires:       texlive-chess-problem-diagrams, texlive-chessboard
Requires:       texlive-chessfss, texlive-crossword, texlive-crosswrd, texlive-egameps
Requires:       texlive-gamebook, texlive-go, texlive-hanoi, texlive-havannah
Requires:       texlive-hexgame, texlive-horoscop, texlive-labyrinth, texlive-logicpuzzle
Requires:       texlive-musikui, texlive-onedown, texlive-othello, texlive-othelloboard
Requires:       texlive-pas-crosswords, texlive-psgo, texlive-reverxii-doc, texlive-rubik
Requires:       texlive-schwalbe-chess, texlive-sgame, texlive-skak, texlive-skaknew
Requires:       texlive-soup, texlive-sudoku, texlive-sudokubundle, texlive-xq
Requires:       texlive-xskak

%description -n texlive-collection-games
Setups for typesetting various games, including chess.

%package -n texlive-collection-humanities
Summary:        Humanities packages
Version:        svn45363
Requires:       texlive-base, texlive-collection-latex, texlive-adtrees, texlive-bibleref
Requires:       texlive-bibleref-lds, texlive-bibleref-mouth
Requires:       texlive-bibleref-parse, texlive-covington
Requires:       texlive-diadia, texlive-dramatist, texlive-dvgloss, texlive-ecltree
Requires:       texlive-edfnotes, texlive-ednotes, texlive-eledform, texlive-eledmac
Requires:       texlive-expex, texlive-gb4e, texlive-gmverse, texlive-jura
Requires:       texlive-juraabbrev, texlive-juramisc, texlive-jurarsp, texlive-ledmac
Requires:       texlive-lexikon, texlive-lexref, texlive-ling-macros, texlive-linguex
Requires:       texlive-liturg, texlive-metrix, texlive-parallel, texlive-parrun
Requires:       texlive-phonrule, texlive-plari, texlive-play, texlive-poemscol
Requires:       texlive-poetry, texlive-poetrytex, texlive-qobitree, texlive-qtree
Requires:       texlive-reledmac, texlive-rrgtrees, texlive-rtklage, texlive-screenplay
Requires:       texlive-screenplay-pkg, texlive-sides, texlive-stage, texlive-textglos
Requires:       texlive-thalie, texlive-tree-dvips, texlive-verse, texlive-xyling

%description -n texlive-collection-humanities
Packages for law, linguistics, social sciences, humanities,
etc.

%package -n texlive-collection-langarabic
Summary:        Arabic
Version:        svn47518
Requires:       texlive-base, texlive-collection-basic, texlive-alkalami, texlive-amiri
Requires:       texlive-arabi, texlive-arabi-add, texlive-arabluatex, texlive-arabtex
Requires:       texlive-bidi, texlive-bidihl, texlive-dad, texlive-ghab
Requires:       texlive-hyphen-arabic, texlive-hyphen-farsi
Requires:       texlive-imsproc, texlive-kurdishlipsum, texlive-lshort-persian-doc, texlive-luabidi
Requires:       texlive-na-box, texlive-persian-bib, texlive-sexam, texlive-simurgh
Requires:       texlive-tram, texlive-xepersian

%description -n texlive-collection-langarabic
Support for Arabic and Persian.

%package -n texlive-collection-langchinese
Summary:        Chinese
Version:        svn47408
Requires:       texlive-base, texlive-collection-langcjk
Requires:       texlive-arphic, texlive-arphic-ttf, texlive-asymptote-by-example-zh-cn-doc, texlive-asymptote-faq-zh-cn-doc
Requires:       texlive-asymptote-manual-zh-cn-doc, texlive-cns
Requires:       texlive-ctex, texlive-ctex-faq-doc, texlive-fandol, texlive-fduthesis
Requires:       texlive-hyphen-chinese, texlive-impatient-cn-doc
Requires:       texlive-latex-notes-zh-cn-doc, texlive-lshort-chinese-doc
Requires:       texlive-pgfornament-han, texlive-texlive-zh-cn-doc
Requires:       texlive-texproposal-doc, texlive-upzhkinsoku
Requires:       texlive-xpinyin, texlive-xtuthesis, texlive-zhlipsum, texlive-zhmetrics
Requires:       texlive-zhmetrics-uptex, texlive-zhnumber
Requires:       texlive-zhspacing

%description -n texlive-collection-langchinese
Support for Chinese; additional packages in collection-langcjk.

%package -n texlive-collection-langcjk
Summary:        Chinese/Japanese/Korean (base)
Version:        svn45194
Requires:       texlive-base, texlive-collection-basic, texlive-adobemapping, texlive-c90
Requires:       texlive-cjk, texlive-cjkpunct, texlive-cjkutils, texlive-dnp
Requires:       texlive-fixjfm, texlive-garuda-c90, texlive-jfmutil, texlive-norasi-c90
Requires:       texlive-pxtatescale, texlive-xcjk2uni, texlive-zxjafont
Provides:       tex(japanese) = %{tl_version}, tex(east-asian) = %{tl_version}
Obsoletes:      texlive-east-asian < %{tl_version}, texlive-texmf-east-asian < %{tl_version}

%description -n texlive-collection-langcjk
Packages supporting a combination of Chinese, Japanese, Korean,
including macros, fonts, documentation.  Also Thai in the c90
encoding, since there is some overlap in those fonts; standard
Thai support is in collection-langother.  Additional packages
for CJK are in their individual language collections.

%package -n texlive-collection-langcyrillic
Summary:        Cyrillic
Version:        svn44895
Requires:       texlive-base, texlive-collection-basic, texlive-collection-latex, texlive-babel-belarusian
Requires:       texlive-babel-bulgarian, texlive-babel-russian
Requires:       texlive-babel-serbian, texlive-babel-serbianc
Requires:       texlive-babel-ukrainian, texlive-churchslavonic
Requires:       texlive-cmcyr, texlive-cyrillic, texlive-cyrillic-bin, texlive-cyrplain
Requires:       texlive-disser, texlive-eskd, texlive-eskdx, texlive-gost
Requires:       texlive-hyphen-belarusian, texlive-hyphen-bulgarian
Requires:       texlive-hyphen-churchslavonic, texlive-hyphen-mongolian
Requires:       texlive-hyphen-russian, texlive-hyphen-serbian
Requires:       texlive-hyphen-ukrainian, texlive-lcyw, texlive-lh, texlive-lhcyr
Requires:       texlive-lshort-bulgarian-doc, texlive-lshort-mongol-doc
Requires:       texlive-lshort-russian-doc, texlive-lshort-ukr-doc
Requires:       texlive-mongolian-babel, texlive-montex, texlive-mpman-ru-doc, texlive-numnameru
Requires:       texlive-pst-eucl-translation-bg-doc, texlive-ruhyphen
Requires:       texlive-russ, texlive-serbian-apostrophe
Requires:       texlive-serbian-date-lat, texlive-serbian-def-cyr
Requires:       texlive-serbian-lig, texlive-t2, texlive-texlive-ru-doc, texlive-texlive-sr-doc
Requires:       texlive-ukrhyph

%description -n texlive-collection-langcyrillic
Support for Cyrillic scripts (Bulgarian, Russian, Serbian,
Ukrainian), even if Latin alphabets may also be used.

%package -n texlive-collection-langczechslovak
Summary:        Czech/Slovak
Version:        svn32550.0
Requires:       texlive-base, texlive-collection-basic, texlive-collection-latex, tex-babel-czech
Requires:       tex-babel-slovak, tex-cnbwp, tex-cs, tex-csbulletin
Requires:       tex-cslatex, tex-csplain, texlive-cstex-doc, tex-hyphen-czech
Requires:       tex-hyphen-slovak, tex-vlna, texlive-lshort-czech-doc, texlive-lshort-slovak-doc
Requires:       texlive-texlive-cz-doc

%description -n texlive-collection-langczechslovak
Support for Czech/Slovak.

%package -n texlive-collection-langenglish
Summary:        US and UK English
Version:        svn46126
Requires:       texlive-base, texlive-collection-basic, texlive-hyphen-english, texlive-FAQ-en-doc
Requires:       texlive-MemoirChapStyles-doc, texlive-Type1fonts-doc
Requires:       texlive-amscls-doc, texlive-amslatex-primer-doc
Requires:       texlive-around-the-bend-doc, texlive-ascii-chart-doc
Requires:       texlive-biblatex-cheatsheet-doc, texlive-components-of-TeX-doc
Requires:       texlive-comprehensive-doc, texlive-dickimaw-doc
Requires:       texlive-docsurvey-doc, texlive-dtxtut-doc
Requires:       texlive-first-latex-doc-doc, texlive-forest-quickstart-doc
Requires:       texlive-gentle-doc, texlive-guide-to-latex-doc
Requires:       texlive-happy4th-doc, texlive-impatient-doc
Requires:       texlive-intro-scientific-doc, texlive-knuth-doc
Requires:       texlive-l2tabu-english-doc, texlive-latex-brochure-doc
Requires:       texlive-latex-course-doc, texlive-latex-doc-ptr-doc
Requires:       texlive-latex-graphics-companion-doc, texlive-latex-refsheet-doc
Requires:       texlive-latex-veryshortguide-doc, texlive-latex-web-companion-doc
Requires:       texlive-latex2e-help-texinfo, texlive-latex4wp-doc
Requires:       texlive-latexcheat-doc, texlive-latexcourse-rug-doc
Requires:       texlive-latexfileinfo-pkgs, texlive-lshort-english-doc
Requires:       texlive-macros2e-doc, texlive-math-e-doc
Requires:       texlive-math-into-latex-4-doc, texlive-maths-symbols-doc
Requires:       texlive-memdesign-doc, texlive-metafont-beginners-doc
Requires:       texlive-metapost-examples-doc, texlive-patgen2-tutorial-doc
Requires:       texlive-pictexsum-doc, texlive-plain-doc-doc
Requires:       texlive-presentations-en-doc, texlive-short-math-guide
Requires:       texlive-simplified-latex-doc, texlive-svg-inkscape-doc
Requires:       texlive-tabulars-e-doc, texlive-tamethebeast-doc
Requires:       texlive-tds-doc, texlive-tex-font-errors-cheatsheet-doc
Requires:       texlive-tex-overview-doc, texlive-tex-refs-doc
Requires:       texlive-texbytopic-doc, texlive-titlepages-doc
Requires:       texlive-tlc2-doc, texlive-undergradmath-doc
Requires:       texlive-visualfaq-doc, texlive-webguide-doc
Requires:       texlive-xetexref-doc

%description -n texlive-collection-langenglish
Support for (and documentation in) English.

%package -n texlive-collection-langeuropean
Summary:        Other European languages
Version:        svn46803
Requires:       texlive-base, texlive-collection-basic, texlive-armtex, texlive-babel-albanian
Requires:       texlive-babel-bosnian, texlive-babel-breton
Requires:       texlive-babel-croatian, texlive-babel-danish
Requires:       texlive-babel-dutch, texlive-babel-estonian
Requires:       texlive-babel-finnish, texlive-babel-friulan
Requires:       texlive-babel-hungarian, texlive-babel-icelandic
Requires:       texlive-babel-irish, texlive-babel-kurmanji
Requires:       texlive-babel-latin, texlive-babel-latvian
Requires:       texlive-babel-macedonian, texlive-babel-norsk
Requires:       texlive-babel-occitan, texlive-babel-piedmontese
Requires:       texlive-babel-romanian, texlive-babel-romansh
Requires:       texlive-babel-samin, texlive-babel-scottish
Requires:       texlive-babel-slovenian, texlive-babel-swedish
Requires:       texlive-babel-turkish, texlive-babel-welsh
Requires:       texlive-finbib, texlive-gloss-occitan, texlive-hrlatex, texlive-hulipsum
Requires:       texlive-hyphen-croatian, texlive-hyphen-danish
Requires:       texlive-hyphen-dutch, texlive-hyphen-estonian
Requires:       texlive-hyphen-finnish, texlive-hyphen-friulan
Requires:       texlive-hyphen-hungarian, texlive-hyphen-icelandic
Requires:       texlive-hyphen-irish, texlive-hyphen-kurmanji
Requires:       texlive-hyphen-latin, texlive-hyphen-latvian
Requires:       texlive-hyphen-lithuanian, texlive-hyphen-norwegian
Requires:       texlive-hyphen-occitan, texlive-hyphen-piedmontese
Requires:       texlive-hyphen-romanian, texlive-hyphen-romansh
Requires:       texlive-hyphen-slovenian, texlive-hyphen-swedish
Requires:       texlive-hyphen-turkish, texlive-hyphen-uppersorbian
Requires:       texlive-hyphen-welsh, texlive-lithuanian
Requires:       texlive-lshort-dutch-doc, texlive-lshort-estonian-doc
Requires:       texlive-lshort-finnish-doc, texlive-lshort-slovenian-doc
Requires:       texlive-lshort-turkish-doc, texlive-nevelok
Requires:       texlive-swebib, texlive-turkmen

%description -n texlive-collection-langeuropean
Support for a number of European languages; others (Greek,
German, French, ...) have their own collections, depending
simply on the size of the support.

%package -n texlive-collection-langfrench
Summary:        French
Version:        svn40375
Requires:       texlive-base, texlive-collection-basic, tex-aeguill, texlive-apprends-latex-doc
Requires:       tex-babel-basque, tex-babel-french, tex-basque-book, tex-basque-date
Requires:       tex-bib-fr, tex-bibleref-french, texlive-booktabs-fr-doc, tex-droit-fr
Requires:       tex-e-french, texlive-epslatex-fr-doc, tex-facture, texlive-formation-latex-ul
Requires:       tex-frletter, tex-hyphen-basque, tex-hyphen-french, texlive-impatient-fr-doc
Requires:       tex-impnattypo, texlive-l2tabu-french-doc
Requires:       tex-latex2e-help-texinfo-fr-doc, texlive-lshort-french-doc
Requires:       tex-mafr, tex-tabvar, tex-tdsfrmath, texlive-texlive-fr-doc
Requires:       texlive-translation-array-fr-doc, texlive-translation-dcolumn-fr-doc
Requires:       texlive-translation-natbib-fr-doc, texlive-translation-tabbing-fr-doc
Requires:       tex-variations, tex-visualtikz-doc

%description -n texlive-collection-langfrench
Support for French and Basque.

%package -n texlive-collection-langgerman
Summary:        German
Version:        svn44952
Requires:       texlive-base, texlive-collection-basic, texlive-apalike-german, texlive-babel-german
Requires:       texlive-bibleref-german, texlive-booktabs-de-doc
Requires:       texlive-csquotes-de-doc, texlive-dehyph-exptl
Requires:       texlive-dhua, texlive-einfuehrung-doc, texlive-einfuehrung2-doc, texlive-etdipa-doc
Requires:       texlive-etoolbox-de-doc, texlive-fifinddo-info-doc
Requires:       texlive-geometry-de-doc, texlive-german, texlive-germbib, texlive-germkorr
Requires:       texlive-hausarbeit-jura, texlive-hyphen-german
Requires:       texlive-koma-script-examples-doc, texlive-l2picfaq-doc
Requires:       texlive-l2tabu-doc, texlive-latex-bib-ex-doc
Requires:       texlive-latex-bib2-ex-doc, texlive-latex-referenz-doc
Requires:       texlive-latex-tabellen-doc, texlive-latexcheat-de-doc
Requires:       texlive-lshort-german-doc, texlive-lualatex-doc-de-doc
Requires:       texlive-microtype-de-doc, texlive-milog, texlive-presentations-doc, texlive-r_und_s
Requires:       texlive-templates-fenn-doc, texlive-templates-sommer-doc
Requires:       texlive-termcal-de, texlive-texlive-de-doc
Requires:       texlive-tipa-de-doc, texlive-translation-arsclassica-de-doc
Requires:       texlive-translation-biblatex-de-doc, texlive-translation-chemsym-de-doc
Requires:       texlive-translation-ecv-de-doc, texlive-translation-enumitem-de-doc
Requires:       texlive-translation-europecv-de-doc, texlive-translation-filecontents-de-doc
Requires:       texlive-translation-moreverb-de-doc, texlive-udesoftec
Requires:       texlive-uhrzeit, texlive-umlaute, texlive-voss-mathcol-doc

%description -n texlive-collection-langgerman
Support for German.

%package -n texlive-collection-langgreek
Summary:        Greek
Version:        svn44192
Requires:       texlive-base, texlive-collection-basic, texlive-babel-greek, texlive-begingreek
Requires:       texlive-betababel, texlive-bgreek, texlive-cbfonts, texlive-cbfonts-fd
Requires:       texlive-gfsbaskerville, texlive-gfsporson
Requires:       texlive-greek-fontenc, texlive-greek-inputenc
Requires:       texlive-greekdates, texlive-greektex, texlive-greektonoi, texlive-hyphen-greek
Requires:       texlive-hyphen-ancientgreek, texlive-ibycus-babel
Requires:       texlive-ibygrk, texlive-kerkis, texlive-levy, texlive-lgreek
Requires:       texlive-mkgrkindex, texlive-teubner, texlive-xgreek, texlive-yannisgr

%description -n texlive-collection-langgreek
Support for Greek.

%package -n texlive-collection-langitalian
Summary:        Italian
Version:        svn30372.0
Requires:       texlive-base, texlive-collection-basic, texlive-amsldoc-it-doc, texlive-amsmath-it-doc
Requires:       texlive-amsthdoc-it-doc, tex-babel-italian
Requires:       tex-codicefiscaleitaliano, texlive-fancyhdr-it-doc
Requires:       tex-fixltxhyph, tex-frontespizio, tex-hyphen-italian, tex-itnumpar
Requires:       texlive-l2tabu-italian-doc, texlive-latex4wp-it-doc
Requires:       tex-layaureo, texlive-lshort-italian-doc
Requires:       texlive-psfrag-italian-doc, texlive-texlive-it-doc

%description -n texlive-collection-langitalian
Support for Italian.

%package -n texlive-collection-langjapanese
Summary:        Japanese
Version:        svn47703
Requires:       texlive-base, texlive-collection-langcjk
Requires:       texlive-ascmac, texlive-babel-japanese, texlive-bxbase, texlive-bxcjkjatype
Requires:       texlive-bxjalipsum, texlive-bxjaprnind, texlive-bxjscls, texlive-bxorigcapt
Requires:       texlive-convbkmk, texlive-endnotesj, texlive-gentombow, texlive-ifptex
Requires:       texlive-ifxptex, texlive-ipaex, texlive-japanese-otf, texlive-japanese-otf-uptex
Requires:       texlive-jlreq, texlive-jsclasses, texlive-lshort-japanese-doc, texlive-luatexja
Requires:       texlive-mendex-doc, texlive-morisawa, texlive-pbibtex-base, texlive-platex
Requires:       texlive-platex-tools, texlive-platexcheat-doc
Requires:       texlive-ptex, texlive-ptex-base, texlive-ptex-fonts, texlive-ptex-fontmaps
Requires:       texlive-ptex2pdf, texlive-pxbase, texlive-pxchfon, texlive-pxcjkcat
Requires:       texlive-pxjahyper, texlive-pxrubrica, texlive-pxufont, texlive-uplatex
Requires:       texlive-uptex-bin, texlive-uptex-base, texlive-uptex-fonts, texlive-wadalab
Requires:       texlive-zxjafbfont, texlive-zxjatype

%description -n texlive-collection-langjapanese
Support for Japanese; additional packages in collection-
langcjk.

%package -n texlive-collection-langkorean
Summary:        Korean
Version:        svn42106
Requires:       texlive-base, texlive-baekmuk, texlive-cjk-ko, texlive-collection-langcjk
Requires:       texlive-kotex-oblivoir, texlive-kotex-plain
Requires:       texlive-kotex-utf, texlive-kotex-utils, texlive-lshort-korean-doc, texlive-nanumtype1
Requires:       texlive-uhc, texlive-unfonts-core, texlive-unfonts-extra

%description -n texlive-collection-langkorean
Support for Korean; additional packages in collection-langcjk.

%package -n texlive-collection-langpolish
Summary:        Polish
Version:        svn44371
Requires:       texlive-base, texlive-collection-latex, texlive-collection-basic, texlive-babel-polish
Requires:       texlive-bredzenie, texlive-cc-pl, texlive-gustlib, texlive-gustprog-doc
Requires:       texlive-hyphen-polish, texlive-lshort-polish-doc
Requires:       texlive-mex, texlive-mwcls, texlive-pl, texlive-polski
Requires:       texlive-przechlewski-book, texlive-qpxqtx
Requires:       texlive-tap, texlive-tex-virtual-academy-pl-doc
Requires:       texlive-texlive-pl-doc, texlive-utf8mex

%description -n texlive-collection-langpolish
Support for Polish.

%package -n texlive-collection-langportuguese
Summary:        Portuguese
Version:        svn47524
Requires:       texlive-base, texlive-collection-basic, tex-babel-portuges, texlive-beamer-tut-pt-doc
Requires:       texlive-cursolatex-doc, tex-feupphdteses
Requires:       tex-hyphen-portuguese, texlive-latex-via-exemplos
Requires:       texlive-latexcheat-ptbr-doc, texlive-lshort-portuguese-doc
Requires:       tex-ordinalpt, texlive-xypic-tut-pt-doc

%description -n texlive-collection-langportuguese
Support for Portuguese.

%package -n texlive-collection-langspanish
Summary:        Spanish
Version:        svn40587
Requires:       texlive-base, texlive-collection-basic, tex-babel-catalan, tex-babel-galician
Requires:       tex-babel-spanglish, tex-babel-spanish, texlive-es-tex-faq-doc, tex-hyphen-catalan
Requires:       tex-hyphen-galician, tex-hyphen-spanish, texlive-l2tabu-spanish-doc, tex-latex2e-help-texinfo-spanish
Requires:       texlive-latexcheat-esmx-doc, texlive-lshort-spanish-doc
Requires:       tex-spanish-mx, tex-texlive-es-doc

%description -n texlive-collection-langspanish
Support for Spanish.

%package -n texlive-collection-latex
Summary:        LaTeX fundamental packages
Version:        svn41614
Requires:       texlive-base, texlive-collection-basic, texlive-ae, texlive-amscls
Requires:       texlive-amsmath, texlive-babel, texlive-babel-english, texlive-babelbib
Requires:       texlive-carlisle, texlive-colortbl, texlive-fancyhdr, texlive-fix2col
Requires:       texlive-geometry, texlive-graphics, texlive-graphics-cfg, texlive-hyperref
Requires:       texlive-latex, texlive-latex-bin, texlive-latex-fonts, texlive-latexconfig
Requires:       texlive-ltxmisc, texlive-mfnfss, texlive-mptopdf, texlive-natbib
Requires:       texlive-oberdiek, texlive-pslatex, texlive-psnfss, texlive-pspicture
Requires:       texlive-tools, texlive-url
Provides:       tex(latex-base) = %{tl_version}

%description -n texlive-collection-latex
These packages are either mandated by the core LaTeX team, or
very widely used and strongly recommended in practice.

%package -n texlive-collection-latexextra
Summary:        LaTeX additional packages
Version:        svn48313
Requires:       texlive-base, texlive-collection-latexrecommended
Requires:       texlive-collection-pictures, texlive-2up
Requires:       texlive-ESIEEcv, texlive-GS1, texlive-HA-prosper, texlive-Tabbing
Requires:       texlive-a0poster, texlive-a4wide, texlive-a5comb, texlive-abraces
Requires:       texlive-abstract, texlive-achemso, texlive-acro, texlive-acronym
Requires:       texlive-acroterm, texlive-actuarialangle
Requires:       texlive-actuarialsymbol, texlive-addfont
Requires:       texlive-addlines, texlive-adjmulticol, texlive-adjustbox, texlive-adrconv
Requires:       texlive-advdate, texlive-akktex, texlive-akletter, texlive-alertmessage
Requires:       texlive-alnumsec, texlive-alterqcm, texlive-altfont, texlive-amsaddr
Requires:       texlive-animate, texlive-anonchap, texlive-answers, texlive-anyfontsize
Requires:       texlive-appendix, texlive-appendixnumberbeamer
Requires:       texlive-apptools, texlive-arcs, texlive-arrayjobx, texlive-arraysort
Requires:       texlive-arydshln, texlive-assignment, texlive-assoccnt, texlive-attachfile
Requires:       texlive-aurl, texlive-authoraftertitle, texlive-authorarchive, texlive-authorindex
Requires:       texlive-autonum, texlive-autopdf, texlive-avremu, texlive-background
Requires:       texlive-bankstatement, texlive-bashful, texlive-basicarith, texlive-bchart
Requires:       texlive-beamer2thesis, texlive-beameraudience
Requires:       texlive-beamercolorthemeowl, texlive-beamerdarkthemes
Requires:       texlive-beamerposter, texlive-beamersubframe
Requires:       texlive-beamertheme-cuerna, texlive-beamertheme-detlevcm
Requires:       texlive-beamertheme-epyt, texlive-beamertheme-focus
Requires:       texlive-beamertheme-metropolis, texlive-beamertheme-phnompenh
Requires:       texlive-beamertheme-saintpetersburg, texlive-beamertheme-upenn-bc
Requires:       texlive-beamerthemejltree, texlive-beamerthemenirma
Requires:       texlive-beton, texlive-bewerbung, texlive-bez123, texlive-bezos
Requires:       texlive-bhcexam, texlive-bibletext, texlive-bigfoot, texlive-bigints
Requires:       texlive-biochemistry-colors, texlive-bizcard
Requires:       texlive-blindtext, texlive-blkarray, texlive-block, texlive-bnumexpr
Requires:       texlive-boites, texlive-bold-extra, texlive-bookcover, texlive-bookest
Requires:       texlive-booklet, texlive-boolexpr, texlive-bophook, texlive-boxedminipage
Requires:       texlive-boxedminipage2e, texlive-boxhandler
Requires:       texlive-bracketkey, texlive-braket, texlive-breakurl, texlive-bullcntr
Requires:       texlive-bussproofs, texlive-bxcalc, texlive-bxdpx-beamer, texlive-bxdvidriver
Requires:       texlive-bxenclose, texlive-bxnewfont, texlive-bxpapersize, texlive-bxpdfver
Requires:       texlive-calcage, texlive-calctab, texlive-calculator, texlive-calrsfs
Requires:       texlive-cals, texlive-calxxxx-yyyy, texlive-cancel, texlive-canoniclayout
Requires:       texlive-capt-of, texlive-captcont, texlive-captdef, texlive-carbohydrates
Requires:       texlive-cases, texlive-casyl, texlive-catchfilebetweentags, texlive-catechis
Requires:       texlive-catoptions, texlive-cbcoptic, texlive-ccaption, texlive-cclicenses
Requires:       texlive-cd, texlive-cd-cover, texlive-cdpbundl, texlive-cellprops
Requires:       texlive-cellspace, texlive-censor, texlive-changebar, texlive-changelayout
Requires:       texlive-changepage, texlive-changes, texlive-chappg, texlive-chapterfolder
Requires:       texlive-cheatsheet, texlive-chet, texlive-chextras, texlive-childdoc
Requires:       texlive-chkfloat, texlive-chletter, texlive-chngcntr, texlive-chronology
Requires:       texlive-circ, texlive-classics, texlive-classpack, texlive-clrdblpg
Requires:       texlive-clefval, texlive-cleveref, texlive-clipboard, texlive-clock
Requires:       texlive-cloze, texlive-clrstrip, texlive-cmdstring, texlive-cmdtrack
Requires:       texlive-cmsd, texlive-cnltx, texlive-cntformats, texlive-cntperchap
Requires:       texlive-codedoc, texlive-codepage, texlive-codesection, texlive-collcell
Requires:       texlive-collectbox, texlive-colordoc, texlive-colorinfo, texlive-coloring
Requires:       texlive-colorspace, texlive-colortab, texlive-colorwav, texlive-colorweb
Requires:       texlive-colourchange, texlive-combelow, texlive-combine, texlive-comma
Requires:       texlive-commado, texlive-comment, texlive-competences, texlive-concepts
Requires:       texlive-concprog, texlive-constants, texlive-continue, texlive-contour
Requires:       texlive-contracard, texlive-conv-xkv, texlive-cooking, texlive-cooking-units
Requires:       texlive-cool, texlive-coollist, texlive-coolstr, texlive-coolthms
Requires:       texlive-cooltooltips, texlive-coordsys, texlive-copyedit, texlive-copyrightbox
Requires:       texlive-coseoul, texlive-counttexruns, texlive-courseoutline, texlive-coursepaper
Requires:       texlive-coverpage, texlive-cprotect, texlive-crbox, texlive-crossreference
Requires:       texlive-crossreftools, texlive-csquotes, texlive-css-colors, texlive-csvsimple
Requires:       texlive-cuisine, texlive-currency, texlive-currfile, texlive-currvita
Requires:       texlive-cutwin, texlive-cv, texlive-cv4tw, texlive-cweb-latex
Requires:       texlive-cyber, texlive-cybercic, texlive-dashbox, texlive-dashrule
Requires:       texlive-dashundergaps, texlive-dataref, texlive-datatool, texlive-dateiliste
Requires:       texlive-datenumber, texlive-datetime, texlive-datetime2, texlive-datetime2-bahasai
Requires:       texlive-datetime2-basque, texlive-datetime2-breton
Requires:       texlive-datetime2-bulgarian, texlive-datetime2-catalan
Requires:       texlive-datetime2-croatian, texlive-datetime2-czech
Requires:       texlive-datetime2-danish, texlive-datetime2-dutch
Requires:       texlive-datetime2-en-fulltext, texlive-datetime2-english
Requires:       texlive-datetime2-esperanto, texlive-datetime2-estonian
Requires:       texlive-datetime2-finnish, texlive-datetime2-french
Requires:       texlive-datetime2-galician, texlive-datetime2-german
Requires:       texlive-datetime2-greek, texlive-datetime2-hebrew
Requires:       texlive-datetime2-icelandic, texlive-datetime2-irish
Requires:       texlive-datetime2-italian, texlive-datetime2-it-fulltext
Requires:       texlive-datetime2-latin, texlive-datetime2-lsorbian
Requires:       texlive-datetime2-magyar, texlive-datetime2-norsk
Requires:       texlive-datetime2-polish, texlive-datetime2-portuges
Requires:       texlive-datetime2-romanian, texlive-datetime2-russian
Requires:       texlive-datetime2-samin, texlive-datetime2-scottish
Requires:       texlive-datetime2-serbian, texlive-datetime2-slovak
Requires:       texlive-datetime2-slovene, texlive-datetime2-spanish
Requires:       texlive-datetime2-swedish, texlive-datetime2-turkish
Requires:       texlive-datetime2-ukrainian, texlive-datetime2-usorbian
Requires:       texlive-datetime2-welsh, texlive-dblfloatfix
Requires:       texlive-decimal, texlive-decorule, texlive-delimtxt, texlive-denisbdoc
Requires:       texlive-diagbox, texlive-diagnose, texlive-dialogl, texlive-dichokey
Requires:       texlive-dinbrief, texlive-directory, texlive-dirtytalk, texlive-dlfltxb
Requires:       texlive-dnaseq, texlive-doclicense, texlive-docmfp, texlive-docmute
Requires:       texlive-doctools, texlive-documentation, texlive-doi, texlive-dotarrow
Requires:       texlive-dotseqn, texlive-download, texlive-dox, texlive-dpfloat
Requires:       texlive-dprogress, texlive-drac, texlive-draftcopy, texlive-draftfigure
Requires:       texlive-draftwatermark, texlive-dtk, texlive-dtxdescribe, texlive-dtxgallery-doc
Requires:       texlive-ducksay, texlive-dvdcoll, texlive-dynamicnumber, texlive-dynblocks
Requires:       texlive-ean13isbn, texlive-easy, texlive-easy-todo, texlive-easyfig
Requires:       texlive-easyformat, texlive-easylist, texlive-easyreview, texlive-ebezier
Requires:       texlive-ecclesiastic, texlive-ecv, texlive-ed, texlive-edmargin
Requires:       texlive-eemeir, texlive-efbox, texlive-egplot, texlive-elements
Requires:       texlive-ellipsis, texlive-elmath, texlive-elocalloc, texlive-elpres
Requires:       texlive-elzcards, texlive-emarks, texlive-embedall, texlive-embrac
Requires:       texlive-emptypage, texlive-emulateapj, texlive-endfloat, texlive-endheads
Requires:       texlive-endnotes, texlive-engpron, texlive-engrec, texlive-enotez
Requires:       texlive-enumitem, texlive-enumitem-zref, texlive-envbig, texlive-environ
Requires:       texlive-envlab, texlive-epigraph, texlive-epiolmec, texlive-eqell
Requires:       texlive-eqlist, texlive-eqnalign, texlive-eqname, texlive-eqparbox
Requires:       texlive-errata, texlive-erw-l3, texlive-esami, texlive-esdiff
Requires:       texlive-esint, texlive-esint-type1, texlive-etaremune, texlive-etextools
Requires:       texlive-etoc, texlive-eukdate, texlive-eulerpx, texlive-europasscv
Requires:       texlive-europecv, texlive-everyhook, texlive-everypage, texlive-exam
Requires:       texlive-exam-n, texlive-examdesign, texlive-example, texlive-examplep
Requires:       texlive-exceltex, texlive-excludeonly, texlive-exercise, texlive-exercisebank
Requires:       texlive-exercises, texlive-exp-testopt, texlive-expdlist, texlive-export
Requires:       texlive-exsheets, texlive-exsol, texlive-extract, texlive-facsimile
Requires:       texlive-factura, texlive-fancylabel, texlive-fancynum, texlive-fancypar
Requires:       texlive-fancyslides, texlive-fancytabs, texlive-fancytooltips, texlive-fcolumn
Requires:       texlive-fetchcls, texlive-ffslides, texlive-fgruler, texlive-fibeamer
Requires:       texlive-fifo-stack, texlive-figsize, texlive-filecontents, texlive-filecontentsdef
Requires:       texlive-filedate, texlive-fileinfo, texlive-filemod, texlive-fink
Requires:       texlive-finstrut, texlive-fithesis, texlive-fixcmex, texlive-fixfoot
Requires:       texlive-fixme, texlive-fixmetodonotes, texlive-fjodor, texlive-flabels
Requires:       texlive-flacards, texlive-flagderiv, texlive-flashcards, texlive-flashmovie
Requires:       texlive-flipbook, texlive-flippdf, texlive-floatflt, texlive-floatrow
Requires:       texlive-flowfram, texlive-fmp, texlive-fmtcount, texlive-fn2end
Requires:       texlive-fnbreak, texlive-fncychap, texlive-fncylab, texlive-fnpara
Requires:       texlive-fnpct, texlive-fnumprint, texlive-foilhtml, texlive-fontaxes
Requires:       texlive-fonttable, texlive-footmisc, texlive-footmisx, texlive-footnotebackref
Requires:       texlive-footnotehyper, texlive-footnoterange
Requires:       texlive-footnpag, texlive-forarray, texlive-foreign, texlive-forloop
Requires:       texlive-formlett, texlive-forms16be, texlive-formular, texlive-fragments
Requires:       texlive-frame, texlive-framed, texlive-frankenstein, texlive-frege
Requires:       texlive-ftcap, texlive-ftnxtra, texlive-fullblck, texlive-fullminipage
Requires:       texlive-fullwidth, texlive-fundus-calligra
Requires:       texlive-fundus-cyr, texlive-fundus-sueterlin
Requires:       texlive-fvextra, texlive-fwlw, texlive-g-brief, texlive-gatherenum
Requires:       texlive-gauss, texlive-gcard, texlive-gcite, texlive-gender
Requires:       texlive-genmpage, texlive-getfiledate, texlive-getitems, texlive-ginpenc
Requires:       texlive-gitfile-info, texlive-gitinfo, texlive-gitinfo2, texlive-gitlog
Requires:       texlive-gloss, texlive-glossaries, texlive-glossaries-danish, texlive-glossaries-dutch
Requires:       texlive-glossaries-english, texlive-glossaries-extra
Requires:       texlive-glossaries-finnish, texlive-glossaries-french
Requires:       texlive-glossaries-german, texlive-glossaries-irish
Requires:       texlive-glossaries-italian, texlive-glossaries-magyar
Requires:       texlive-glossaries-polish, texlive-glossaries-portuges
Requires:       texlive-glossaries-serbian, texlive-glossaries-spanish
Requires:       texlive-gmdoc, texlive-gmdoc-enhance, texlive-gmiflink, texlive-gmutils
Requires:       texlive-gmverb, texlive-graphbox, texlive-graphicx-psmin, texlive-graphicxbox
Requires:       texlive-grayhints, texlive-grfpaste, texlive-grid, texlive-grid-system
Requires:       texlive-gridset, texlive-guitlogo, texlive-halloweenmath, texlive-hackthefootline
Requires:       texlive-handin, texlive-handout, texlive-hang, texlive-hanging
Requires:       texlive-hardwrap, texlive-harnon-cv, texlive-harpoon, texlive-hc
Requires:       texlive-he-she, texlive-hhtensor, texlive-histogr, texlive-hitec
Requires:       texlive-hletter, texlive-hpsdiss, texlive-hrefhide, texlive-hvindex
Requires:       texlive-hypdvips, texlive-hyper, texlive-hyperbar, texlive-hypernat
Requires:       texlive-hyperxmp, texlive-hyphenat, texlive-idxcmds, texlive-idxlayout
Requires:       texlive-iffont, texlive-ifmslide, texlive-ifmtarg, texlive-ifnextok
Requires:       texlive-ifoddpage, texlive-ifplatform, texlive-ifthenx, texlive-iitem
Requires:       texlive-image-gallery, texlive-imakeidx, texlive-import, texlive-incgraph
Requires:       texlive-indextools, texlive-inlinedef, texlive-inputtrc, texlive-interactiveworkbook
Requires:       texlive-interfaces, texlive-intopdf, texlive-inversepath, texlive-invoice
Requires:       texlive-invoice2, texlive-iso, texlive-iso10303, texlive-isodate
Requires:       texlive-isodoc, texlive-isonums, texlive-isopt, texlive-isorot
Requires:       texlive-isotope, texlive-issuulinks, texlive-iwhdp, texlive-jlabels
Requires:       texlive-jslectureplanner, texlive-jumplines
Requires:       texlive-jvlisting, texlive-kantlipsum, texlive-kerntest, texlive-keycommand
Requires:       texlive-keyfloat, texlive-keyreader, texlive-keystroke, texlive-keyval2e
Requires:       texlive-keyvaltable, texlive-kix, texlive-knowledge, texlive-koma-moderncvclassic
Requires:       texlive-koma-script-sfs, texlive-komacv, texlive-komacv-rg, texlive-ktv-texdata
Requires:       texlive-l3build, texlive-labbook, texlive-labels, texlive-labelschanged
Requires:       texlive-lastpackage, texlive-lastpage, texlive-latex-tds-doc, texlive-latexdemo
Requires:       texlive-latexgit, texlive-layouts, texlive-lazylist, texlive-lccaps
Requires:       texlive-lcd, texlive-lcg, texlive-leading, texlive-leaflet
Requires:       texlive-leftidx, texlive-leipzig, texlive-lengthconvert, texlive-lettre
Requires:       texlive-lettrine, texlive-lewis, texlive-lhelp, texlive-libgreek
Requires:       texlive-limap, texlive-linegoal, texlive-linop, texlive-lipsum
Requires:       texlive-lisp-on-tex, texlive-listing, texlive-listlbls, texlive-listliketab
Requires:       texlive-listofsymbols, texlive-lkproof, texlive-lmake, texlive-locality
Requires:       texlive-localloc, texlive-logbox, texlive-logical-markup-utils, texlive-logpap
Requires:       texlive-longfbox, texlive-longfigure, texlive-longnamefilelist, texlive-loops
Requires:       texlive-lsc, texlive-lstaddons, texlive-lt3graph, texlive-ltablex
Requires:       texlive-ltabptch, texlive-ltxdockit, texlive-ltxindex, texlive-ltxkeys
Requires:       texlive-ltxnew, texlive-ltxtools, texlive-lua-check-hyphen, texlive-luatodonotes
Requires:       texlive-macroswap, texlive-magaz, texlive-mailing, texlive-mailmerge
Requires:       texlive-makebarcode, texlive-makebase, texlive-makebox, texlive-makecell
Requires:       texlive-makecirc, texlive-makecmds, texlive-makedtx, texlive-makeglos
Requires:       texlive-mandi, texlive-manfnt, texlive-manuscript, texlive-manyind
Requires:       texlive-marginfit, texlive-marginfix, texlive-marginnote, texlive-markdown
Requires:       texlive-mathalfa, texlive-mathastext, texlive-mathexam, texlive-mathfam256
Requires:       texlive-mathfont, texlive-maybemath, texlive-mbenotes, texlive-mcaption
Requires:       texlive-mceinleger, texlive-mcexam, texlive-mcite, texlive-mciteplus
Requires:       texlive-mdframed, texlive-media9, texlive-medstarbeamer, texlive-meetingmins
Requires:       texlive-memexsupp, texlive-memory, texlive-mensa-tex, texlive-menu
Requires:       texlive-menukeys, texlive-method, texlive-metre, texlive-mfirstuc
Requires:       texlive-mftinc, texlive-midpage, texlive-minibox, texlive-minidocument
Requires:       texlive-minifp, texlive-minipage-marginpar
Requires:       texlive-minitoc, texlive-minorrevision, texlive-minted, texlive-minutes
Requires:       texlive-mla-paper, texlive-mlist, texlive-mmap, texlive-mnotes
Requires:       texlive-moderncv, texlive-modernposter, texlive-moderntimeline, texlive-modref
Requires:       texlive-modroman, texlive-modular, texlive-monofill, texlive-moodle
Requires:       texlive-moreenum, texlive-morefloats, texlive-morehype, texlive-moresize
Requires:       texlive-moreverb, texlive-morewrites, texlive-mparhack, texlive-mpostinl
Requires:       texlive-msc, texlive-msg, texlive-mslapa, texlive-mtgreek
Requires:       texlive-multenum, texlive-multiaudience, texlive-multibbl, texlive-multicap
Requires:       texlive-multidef, texlive-multienv, texlive-multiexpand, texlive-multilang
Requires:       texlive-multirow, texlive-mversion, texlive-mwe, texlive-mycv
Requires:       texlive-mylatexformat, texlive-nag, texlive-nameauth, texlive-namespc
Requires:       texlive-ncclatex, texlive-ncctools, texlive-needspace, texlive-nestquot
Requires:       texlive-newcommand-doc, texlive-newenviron
Requires:       texlive-newfile, texlive-newlfm, texlive-newspaper, texlive-newunicodechar
Requires:       texlive-newvbtm, texlive-newverbs, texlive-nextpage, texlive-nfssext-cfr
Requires:       texlive-nicefilelist, texlive-niceframe, texlive-nicetext, texlive-nidanfloat
Requires:       texlive-nlctdoc, texlive-noconflict, texlive-noindentafter, texlive-noitcrul
Requires:       texlive-nolbreaks, texlive-nomencl, texlive-nomentbl, texlive-nonfloat
Requires:       texlive-nonumonpart, texlive-nopageno, texlive-normalcolor, texlive-notes
Requires:       texlive-notespages, texlive-notestex, texlive-notoccite, texlive-nowidow
Requires:       texlive-nox, texlive-ntheorem, texlive-numberedblock, texlive-numname
Requires:       texlive-numprint, texlive-numspell, texlive-ocg-p, texlive-ocgx
Requires:       texlive-ocgx2, texlive-ocr-latex, texlive-octavo, texlive-oldstyle
Requires:       texlive-onlyamsmath, texlive-opcit, texlive-optidef, texlive-optional
Requires:       texlive-options, texlive-outline, texlive-outliner, texlive-outlines
Requires:       texlive-outlining, texlive-overlays, texlive-overpic, texlive-padcount
Requires:       texlive-pagecolor, texlive-pagecont, texlive-pagenote, texlive-pagerange
Requires:       texlive-pageslts, texlive-paper, texlive-papercdcase, texlive-papermas
Requires:       texlive-papertex, texlive-paracol, texlive-parades, texlive-paralist
Requires:       texlive-paresse, texlive-parnotes, texlive-parselines, texlive-pas-cours
Requires:       texlive-pas-cv, texlive-pas-tableur, texlive-patchcmd, texlive-pauldoc
Requires:       texlive-pawpict, texlive-pax, texlive-pbox, texlive-pbsheet
Requires:       texlive-pdf14, texlive-pdfcomment, texlive-pdfcprot, texlive-pdfmarginpar
Requires:       texlive-pdfoverlay, texlive-pdfpagediff, texlive-pdfpc-movie, texlive-pdfprivacy
Requires:       texlive-pdfreview, texlive-pdfscreen, texlive-pdfslide, texlive-pdfsync
Requires:       texlive-pdfwin, texlive-pdfx, texlive-pecha, texlive-perltex
Requires:       texlive-permute, texlive-petiteannonce, texlive-phffullpagefigure, texlive-phfnote
Requires:       texlive-phfparen, texlive-phfqit, texlive-phfquotetext, texlive-phfsvnwatermark
Requires:       texlive-phfthm, texlive-philex, texlive-phonenumbers, texlive-photo
Requires:       texlive-piff, texlive-pkgloader, texlive-placeins, texlive-plantslabels
Requires:       texlive-plates, texlive-plweb, texlive-polynom, texlive-polynomial
Requires:       texlive-polytable, texlive-postcards, texlive-poster-mac, texlive-ppr-prv
Requires:       texlive-preprint, texlive-pressrelease, texlive-prettyref, tex-preview
Requires:       texlive-printlen, texlive-probsoln, texlive-program, texlive-progress
Requires:       texlive-progressbar, texlive-proofread, texlive-properties, texlive-prosper
Requires:       texlive-protex, texlive-protocol, texlive-psfragx, texlive-pstool
Requires:       texlive-pstring, texlive-pxgreeks, texlive-pygmentex, texlive-python
Requires:       texlive-qcm, texlive-qstest, texlive-qsymbols, texlive-quicktype
Requires:       texlive-quotchap, texlive-quoting, texlive-quotmark, texlive-ran_toks
Requires:       texlive-randtext, texlive-rccol, texlive-rcs-multi, texlive-rcsinfo
Requires:       texlive-readarray, texlive-realboxes, texlive-recipe, texlive-recipebook
Requires:       texlive-recipecard, texlive-rectopma, texlive-refcheck, texlive-refenums
Requires:       texlive-reflectgraphics, texlive-refman, texlive-refstyle, texlive-regcount
Requires:       texlive-regexpatch, texlive-register, texlive-regstats, texlive-relenc
Requires:       texlive-relsize, texlive-repeatindex, texlive-repltext, texlive-rjlparshap
Requires:       texlive-rlepsf, texlive-rmpage, texlive-robustcommand, texlive-robustindex
Requires:       texlive-romanbar, texlive-romanbarpagenumber
Requires:       texlive-romanneg, texlive-romannum, texlive-rotfloat, texlive-rotpages
Requires:       texlive-roundbox, texlive-rterface, texlive-rtkinenc, texlive-rulercompass
Requires:       texlive-rvwrite, texlive-sanitize-umlaut
Requires:       texlive-sauerj, texlive-savefnmark, texlive-savesym, texlive-savetrees
Requires:       texlive-scale, texlive-scalebar, texlive-scalerel, texlive-scanpages
Requires:       texlive-scrlttr2copy, texlive-sdrt, texlive-secdot, texlive-sectionbox
Requires:       texlive-sectionbreak, texlive-sectsty, texlive-seealso, texlive-selectp
Requires:       texlive-semantic, texlive-semantic-markup
Requires:       texlive-semioneside, texlive-semproc, texlive-sepfootnotes, texlive-seqsplit
Requires:       texlive-sesstime, texlive-sf298, texlive-sffms, texlive-sfmath
Requires:       texlive-shadethm, texlive-shadow, texlive-shadowtext, texlive-shapepar
Requires:       texlive-shdoc, texlive-shipunov, texlive-shorttoc, texlive-show2e
Requires:       texlive-showcharinbox, texlive-showdim, texlive-showexpl, texlive-showhyphens
Requires:       texlive-showlabels, texlive-sidecap, texlive-sidenotes, texlive-silence
Requires:       texlive-simplecd, texlive-simplecv, texlive-simpleinvoice, texlive-sitem
Requires:       texlive-skb, texlive-skdoc, texlive-skeycommand, texlive-skeyval
Requires:       texlive-skrapport, texlive-slantsc, texlive-smalltableof, texlive-smartunits
Requires:       texlive-smartref, texlive-snapshot, texlive-snotez, texlive-soul
Requires:       texlive-spark-otf, texlive-sparklines, texlive-sphack, texlive-splitindex
Requires:       texlive-spot, texlive-spotcolor, texlive-spreadtab, texlive-spverbatim
Requires:       texlive-srbook-mem, texlive-srcltx, texlive-sseq, texlive-sslides
Requires:       texlive-stack, texlive-stackengine, texlive-standalone, texlive-stdclsdv
Requires:       texlive-stdpage, texlive-stealcaps, texlive-stex, texlive-storebox
Requires:       texlive-storecmd, texlive-stringstrings, texlive-sttools, texlive-stubs
Requires:       texlive-studenthandouts, texlive-subdepth
Requires:       texlive-subeqn, texlive-subeqnarray, texlive-subfigmat, texlive-subfigure
Requires:       texlive-subfiles, texlive-subfloat, texlive-substitutefont, texlive-substr
Requires:       texlive-supertabular, texlive-svg, texlive-svgcolor, texlive-svn
Requires:       texlive-svn-multi, texlive-svn-prov, texlive-svninfo, texlive-syntax
Requires:       texlive-syntrace, texlive-synttree, texlive-tabfigures, texlive-tableaux
Requires:       texlive-tablefootnote, texlive-tableof, texlive-tablestyles, texlive-tablists
Requires:       texlive-tabls, texlive-tabstackengine, texlive-tabto-ltx, texlive-tabu
Requires:       texlive-tabularborder, texlive-tabularcalc
Requires:       texlive-tabularew, texlive-tabulary, texlive-tagging, texlive-tagpair
Requires:       texlive-tagpdf, texlive-talk, texlive-tamefloats, texlive-tasks
Requires:       texlive-tcldoc, texlive-tcolorbox, texlive-tdclock, texlive-technics
Requires:       texlive-ted, texlive-templatetools, texlive-termcal, texlive-termlist
Requires:       texlive-testhyphens, texlive-testidx, texlive-tex-label, texlive-texlogos
Requires:       texlive-texmate, texlive-texments, texlive-texpower, texlive-texshade
Requires:       texlive-textualicomma, texlive-texvc, texlive-textfit, texlive-textmerg
Requires:       texlive-textpos, texlive-theoremref, texlive-thinsp, texlive-thmtools
Requires:       texlive-threadcol, texlive-threeparttable
Requires:       texlive-threeparttablex, texlive-thumb, texlive-thumbs, texlive-thumby
Requires:       texlive-ticket, texlive-titlecaps, texlive-titlefoot, texlive-titlepic
Requires:       texlive-titleref, texlive-titlesec, texlive-titling, texlive-tocbibind
Requires:       texlive-tocdata, texlive-tocloft, texlive-tocvsec2, texlive-todo
Requires:       texlive-todonotes, texlive-tokenizer, texlive-toolbox, texlive-topfloat
Requires:       texlive-totcount, texlive-totpages, texlive-translations, texlive-trfsigns
Requires:       texlive-trimspaces, texlive-trivfloat, texlive-trsym, texlive-truncate
Requires:       texlive-tucv, texlive-turnthepage, texlive-twoinone, texlive-twoup
Requires:       texlive-txgreeks, texlive-type1cm, texlive-typed-checklist, texlive-typeface
Requires:       texlive-typoaid, texlive-typogrid, texlive-uassign, texlive-ucs
Requires:       texlive-uebungsblatt, texlive-umoline, texlive-underlin, texlive-underoverlap
Requires:       texlive-undolabl, texlive-units, texlive-unravel, texlive-upmethodology
Requires:       texlive-upquote, texlive-uri, texlive-ushort, texlive-uspace
Requires:       texlive-variablelm, texlive-varindex, texlive-varsfromjobname, texlive-varwidth
Requires:       texlive-vdmlisting, texlive-verbasef, texlive-verbatimbox, texlive-verbatimcopy
Requires:       texlive-verbdef, texlive-verbments, texlive-version, texlive-versions
Requires:       texlive-versonotes, texlive-vertbars, texlive-vgrid, texlive-vhistory
Requires:       texlive-vmargin, texlive-volumes, texlive-vpe, texlive-vruler
Requires:       texlive-vwcol, texlive-wallcalendar, texlive-wallpaper, texlive-warning
Requires:       texlive-warpcol, texlive-was, texlive-widetable, texlive-williams
Requires:       texlive-withargs, texlive-wordcount, texlive-wordlike, texlive-wrapfig
Requires:       texlive-wtref, texlive-xargs, texlive-xassoccnt, texlive-xcntperchap
Requires:       texlive-xcolor-material, texlive-xcolor-solarized
Requires:       texlive-xcomment, texlive-xdoc, texlive-xellipsis, texlive-xfakebold
Requires:       texlive-xfor, texlive-xhfill, texlive-xifthen, texlive-xint
Requires:       texlive-xltabular, texlive-xmpincl, texlive-xnewcommand, texlive-xoptarg
Requires:       texlive-xpatch, texlive-xpeek, texlive-xprintlen, texlive-xpunctuate
Requires:       texlive-xsavebox, texlive-xsim, texlive-xstring, texlive-xtab
Requires:       texlive-xurl, texlive-xwatermark, texlive-xytree, texlive-yafoot
Requires:       texlive-yagusylo, texlive-yaletter, texlive-ycbook, texlive-ydoc
Requires:       texlive-yplan, texlive-zebra-goodies, texlive-zed-csp, texlive-ziffer
Requires:       texlive-zwgetfdate, texlive-zwpagelayout

%description -n texlive-collection-latexextra
A very large collection of add-on packages for LaTeX.

%package -n texlive-collection-latexrecommended
Summary:        LaTeX recommended packages
Version:        svn45955
Requires:       texlive-base, texlive-collection-latex, texlive-anysize, texlive-beamer
Requires:       texlive-booktabs, texlive-breqn, texlive-caption, texlive-cite
Requires:       texlive-cmap, texlive-crop, texlive-ctable, texlive-eso-pic
Requires:       texlive-euenc, texlive-euler, texlive-etoolbox, texlive-extsizes
Requires:       texlive-fancybox, texlive-fancyref, texlive-fancyvrb, texlive-filehook
Requires:       texlive-float, texlive-fontspec, texlive-fp, texlive-index
Requires:       texlive-jknapltx, texlive-koma-script, texlive-latexbug, texlive-l3experimental
Requires:       texlive-l3kernel, texlive-l3packages, texlive-lineno, texlive-listings
Requires:       texlive-lwarp, texlive-mathspec, texlive-mathtools, texlive-mdwtools
Requires:       texlive-memoir, texlive-metalogo, texlive-microtype, texlive-ms
Requires:       texlive-ntgclass, texlive-parskip, texlive-pdfpages, texlive-polyglossia
Requires:       texlive-powerdot, texlive-psfrag, texlive-rcs, texlive-sansmath
Requires:       texlive-section, texlive-seminar, texlive-sepnum, texlive-setspace
Requires:       texlive-subfig, texlive-textcase, texlive-thumbpdf, texlive-translator
Requires:       texlive-typehtml, texlive-ucharcat, texlive-underscore, texlive-unicode-math
Requires:       texlive-xcolor, texlive-xkeyval, texlive-xltxtra, texlive-xunicode
Provides:       tex(latex) = %{tl_version}, texlive-latex = %{tl_version}
Requires:       texlive-collection-fontsrecommended

%description -n texlive-collection-latexrecommended
A collection of recommended add-on packages for LaTeX which
have widespread use.

%package -n texlive-collection-luatex
Summary:        LuaTeX packages
Version:        svn48052
Requires:       texlive-base, texlive-collection-basic, texlive-auto-pst-pdf-lua, texlive-bezierplot
Requires:       texlive-checkcites, texlive-chickenize, texlive-combofont, texlive-cstypo
Requires:       texlive-ctablestack, texlive-enigma, texlive-fontloader-luaotfload, texlive-interpreter
Requires:       texlive-kanaparser, texlive-lua-visual-debug
Requires:       texlive-lua2dox, texlive-luacode, texlive-luahyphenrules, texlive-luaindex
Requires:       texlive-luainputenc, texlive-luaintro-doc
Requires:       texlive-lualatex-doc-doc, texlive-lualatex-math
Requires:       texlive-lualatex-truncate, texlive-lualibs
Requires:       texlive-luamplib, texlive-luaotfload, texlive-luapackageloader, texlive-luatex85
Requires:       texlive-luatexbase, texlive-luatexko, texlive-luatextra, texlive-luavlna
Requires:       texlive-luaxml, texlive-nodetree, texlive-odsfile, texlive-placeat
Requires:       texlive-plantuml, texlive-selnolig, texlive-spelling, texlive-typewriter

%description -n texlive-collection-luatex
Packages for LuaTeX, a Unicode-aware extension of pdfTeX, using
Lua as an embedded scripting and extension language.
http://luatex.org/

%package -n texlive-collection-mathscience
Summary:        Mathematics, natural sciences, computer science packages
Version:        svn48252
Provides:       texlive-collection-science = %{epoch}:svn39074.obsolete
Obsoletes:      texlive-collection-science <= 6:svn39074
Provides:       texlive-collection-mathextra = %{epoch}:svn40076.obsolete
Obsoletes:      texlive-collection-mathextra <= 6:svn40076
Requires:       texlive-base, texlive-collection-fontsrecommended
Requires:       texlive-collection-latex, texlive-12many
Requires:       texlive-SIstyle, texlive-SIunits, texlive-alg, texlive-algobox
Requires:       texlive-algorithm2e, texlive-algorithmicx
Requires:       texlive-algorithms, texlive-aligned-overset
Requires:       texlive-amstex, texlive-apxproof, texlive-autobreak, texlive-axodraw2
Requires:       texlive-backnaur, texlive-begriff, texlive-binomexp, texlive-biocon
Requires:       texlive-bitpattern, texlive-bohr, texlive-boldtensors, texlive-bosisio
Requires:       texlive-bpchem, texlive-bropd, texlive-bytefield, texlive-calculation
Requires:       texlive-cascade, texlive-ccfonts, texlive-chemarrow, texlive-chemcompounds
Requires:       texlive-chemcono, texlive-chemexec, texlive-chemformula, texlive-chemgreek
Requires:       texlive-chemmacros, texlive-chemnum, texlive-chemschemex, texlive-chemsec
Requires:       texlive-chemstyle, texlive-clrscode, texlive-clrscode3e, texlive-commath
Requires:       texlive-complexity, texlive-computational-complexity
Requires:       texlive-concmath, texlive-concrete, texlive-conteq, texlive-correctmathalign
Requires:       texlive-cryptocode, texlive-delim, texlive-delimset, texlive-delimseasy
Requires:       texlive-diffcoeff, texlive-digiconfigs, texlive-dijkstra, texlive-drawmatrix
Requires:       texlive-drawstack, texlive-dyntree, texlive-ebproof, texlive-econometrics
Requires:       texlive-eltex, texlive-emf, texlive-endiagram, texlive-engtlc
Requires:       texlive-eqnarray, texlive-eqnnumwarn, texlive-extarrows, texlive-extpfeil
Requires:       texlive-faktor, texlive-fnspe, texlive-fouridx, texlive-functan
Requires:       texlive-galois, texlive-gastex, texlive-gene-logic, texlive-ghsystem
Requires:       texlive-gotoh, texlive-grundgesetze, texlive-gu, texlive-hep
Requires:       texlive-hepnames, texlive-hepparticles, texlive-hepthesis, texlive-hepunits
Requires:       texlive-includernw, texlive-interval, texlive-ionumbers, texlive-isomath
Requires:       texlive-karnaugh, texlive-karnaugh-map, texlive-karnaughmap, texlive-logicproof
Requires:       texlive-longdivision, texlive-lpform, texlive-lplfitch, texlive-lstbayes
Requires:       texlive-mathcomp, texlive-mathfixs, texlive-mathpartir, texlive-mathpunctspace
Requires:       texlive-matlab-prettifier, texlive-mattens
Requires:       texlive-mgltex, texlive-mhchem, texlive-mhequ, texlive-miller
Requires:       texlive-multiobjective, texlive-mychemistry
Requires:       texlive-natded, texlive-nath, texlive-nicematrix, texlive-nuc
Requires:       texlive-nucleardata, texlive-objectz, texlive-oplotsymbl, texlive-ot-tableau
Requires:       texlive-oubraces, texlive-perfectcut, texlive-physics, texlive-pm-isomath
Requires:       texlive-polexpr, texlive-prftree, texlive-proba, texlive-prooftrees
Requires:       texlive-pseudocode, texlive-pygmentex, texlive-pythonhighlight, texlive-rec-thy
Requires:       texlive-revquantum, texlive-ribbonproofs
Requires:       texlive-rmathbr, texlive-sasnrdisplay, texlive-sciposter, texlive-sclang-prettifier
Requires:       texlive-scratchx, texlive-sesamanuel, texlive-sfg, texlive-shuffle
Requires:       texlive-simpler-wick, texlive-simplewick
Requires:       texlive-siunitx, texlive-skmath, texlive-spalign, texlive-stanli
Requires:       texlive-statex, texlive-statex2, texlive-statistics, texlive-statistik
Requires:       texlive-statmath, texlive-steinmetz, texlive-stmaryrd, texlive-structmech
Requires:       texlive-struktex, texlive-substances, texlive-subsupscripts, texlive-susy
Requires:       texlive-syllogism, texlive-sympytexpackage
Requires:       texlive-synproof, texlive-t-angles, texlive-tablor, texlive-tensor
Requires:       texlive-tex-ewd, texlive-textgreek, texlive-textopo, texlive-thmbox
Requires:       texlive-turnstile, texlive-ulqda, texlive-unitsdef, texlive-venn
Requires:       texlive-witharrows, texlive-xymtex, texlive-yhmath, texlive-youngtab
Requires:       texlive-ytableau

%description -n texlive-collection-mathscience
Mathematics, natural sciences, computer science packages

%package -n texlive-collection-metapost
Summary:        MetaPost and Metafont packages
Version:        svn44297
Requires:       texlive-base, texlive-collection-basic, tex-automata, tex-bbcard
Requires:       tex-blockdraw_mp, tex-bpolynomial, tex-cmarrows, tex-drv
Requires:       tex-dviincl, tex-emp, tex-epsincl, tex-expressg
Requires:       tex-exteps, tex-featpost, tex-feynmf, tex-feynmp-auto
Requires:       tex-garrigues, tex-gmp, tex-hatching, tex-latexmp
Requires:       tex-mcf2graph, tex-metago, tex-metaobj, tex-metaplot
Requires:       tex-metapost, tex-metauml, tex-mfpic, tex-mfpic4ode
Requires:       tex-mp3d, tex-mparrows, tex-mpcolornames, tex-mpattern
Requires:       tex-mpgraphics, texlive-mptrees, tex-piechartmp, tex-repere
Requires:       tex-roex, tex-roundrect, tex-shapes, tex-slideshow
Requires:       tex-splines, tex-suanpan, tex-textpath, tex-threeddice

%description -n texlive-collection-metapost
collection-metapost package

%package -n texlive-collection-music
Summary:        Music packages
Version:        svn48102
Requires:       texlive-base, texlive-collection-latex, texlive-abc, texlive-autosp
Requires:       texlive-bagpipe, texlive-figbas, texlive-gchords, texlive-gregoriotex
Requires:       texlive-gtrcrd, texlive-guitar, texlive-guitarchordschemes, texlive-harmony
Requires:       texlive-leadsheets, texlive-lilyglyphs, texlive-lyluatex, texlive-m-tx
Requires:       texlive-musicography, texlive-musixguit, texlive-musixtex, texlive-musixtex-fonts
Requires:       texlive-musixtnt, texlive-octave, texlive-piano, texlive-pmx
Requires:       texlive-pmxchords, texlive-songbook, texlive-songs, texlive-xpiano

%description -n texlive-collection-music
Music-related fonts and packages.

%package -n texlive-collection-pictures
Summary:        Graphics, pictures, diagrams
Version:        svn48314
Requires:       texlive-base, texlive-collection-basic, texlive-adigraph, texlive-aobs-tikz
Requires:       texlive-askmaps, texlive-asyfig, texlive-asypictureb, texlive-autoarea
Requires:       texlive-bardiag, texlive-beamerswitch, texlive-binarytree, texlive-blochsphere
Requires:       texlive-bloques, texlive-blox, texlive-bodegraph, texlive-bondgraph
Requires:       texlive-bondgraphs, texlive-braids, texlive-bxeepic, texlive-cachepic
Requires:       texlive-callouts, texlive-celtic, texlive-chemfig, texlive-combinedgraphics
Requires:       texlive-circuitikz, texlive-curve, texlive-curve2e, texlive-curves
Requires:       texlive-dcpic, texlive-diagmac2, texlive-doc-pictex-doc, texlive-dottex
Requires:       texlive-dot2texi, texlive-dratex, texlive-drs, texlive-duotenzor
Requires:       texlive-dynkin-diagrams, texlive-ecgdraw
Requires:       texlive-eepic, texlive-ellipse, texlive-endofproofwd, texlive-epspdf
Requires:       texlive-epspdfconversion, texlive-esk, texlive-fast-diagram, texlive-fig4latex
Requires:       texlive-fitbox, texlive-flowchart, texlive-forest, texlive-genealogytree
Requires:       texlive-getmap, texlive-gincltex, texlive-gnuplottex, texlive-gradientframe
Requires:       texlive-grafcet, texlive-graph35, texlive-graphicxpsd, texlive-graphviz
Requires:       texlive-gtrlib-largetrees, texlive-harveyballs
Requires:       texlive-here, texlive-hf-tikz, texlive-hobby, texlive-hvfloat
Requires:       texlive-istgame, texlive-knitting, texlive-knittingpattern, texlive-ladder
Requires:       texlive-lapdf, texlive-latex-make, texlive-lpic, texlive-lroundrect
Requires:       texlive-luamesh, texlive-luasseq, texlive-maker, texlive-makeshape
Requires:       texlive-mathspic, texlive-milsymb, texlive-miniplot, texlive-mkpic
Requires:       texlive-modiagram, texlive-neuralnetwork
Requires:       texlive-numericplots, texlive-pb-diagram
Requires:       texlive-penrose, texlive-petri-nets, texlive-pgf, texlive-pgf-blur
Requires:       texlive-pgf-soroban, texlive-pgf-spectra
Requires:       texlive-pgf-umlcd, texlive-pgf-umlsd, texlive-pgfgantt, texlive-pgfkeyx
Requires:       texlive-pgfmolbio, texlive-pgfopts, texlive-pgfornament, texlive-pgfplots
Requires:       texlive-picinpar, texlive-pict2e, texlive-pictex, texlive-pictex2
Requires:       texlive-pinlabel, texlive-pixelart, texlive-pmgraph, texlive-postage
Requires:       texlive-prerex, texlive-productbox, texlive-pxpgfmark, texlive-qcircuit
Requires:       texlive-qrcode, texlive-randbild, texlive-randomwalk, texlive-reotex
Requires:       texlive-rviewport, texlive-sa-tikz, texlive-schemabloc, texlive-scsnowman
Requires:       texlive-scratch, texlive-setdeck, texlive-signchart, texlive-smartdiagram
Requires:       texlive-spath3, texlive-spectralsequences
Requires:       texlive-swimgraf, texlive-table-fct, texlive-texdraw, texlive-ticollege
Requires:       texlive-tipfr-doc, texlive-tikz-3dplot, texlive-tikz-bayesnet, texlive-tikz-cd
Requires:       texlive-tikz-dependency, texlive-tikz-dimline
Requires:       texlive-tikz-feynman, texlive-tikz-inet, texlive-tikz-kalender, texlive-tikz-karnaugh
Requires:       texlive-tikz-ladder, texlive-tikz-layers
Requires:       texlive-tikz-nef, texlive-tikz-network, texlive-tikz-opm, texlive-tikz-optics
Requires:       texlive-tikz-page, texlive-tikz-palattice
Requires:       texlive-tikz-qtree, texlive-tikz-relay, texlive-tikz-sfc, texlive-tikz-timing
Requires:       texlive-tikzcodeblocks, texlive-tikzducks
Requires:       texlive-tikzinclude, texlive-tikzmark, texlive-tikzmarmots, texlive-tikzorbital
Requires:       texlive-tikzpagenodes, texlive-tikzpfeile
Requires:       texlive-tikzpeople, texlive-tikzposter, texlive-tikzscale, texlive-tikzsymbols
Requires:       texlive-timing-diagrams, texlive-tqft, texlive-tkz-base, texlive-tkz-berge
Requires:       texlive-tkz-doc, texlive-tkz-euclide, texlive-tkz-fct, texlive-tkz-graph
Requires:       texlive-tkz-kiviat, texlive-tkz-linknodes
Requires:       texlive-tkz-orm, texlive-tkz-tab, texlive-tsemlines, texlive-tufte-latex
Requires:       texlive-venndiagram, texlive-visualpstricks-doc
Requires:       texlive-xpicture, texlive-xypic

%description -n texlive-collection-pictures
Including TikZ, pict, etc., but MetaPost and PStricks are
separate.

%package -n texlive-collection-plaingeneric
Summary:        Plain (La)TeX packages
Version:        svn47878
Provides:       texlive-collection-genericrecommended = svn35655.0.obsolete
Obsoletes:      texlive-collection-genericrecommended <= svn35655.0
Provides:       texlive-collection-genericextra = svn39964.obsolete
Obsoletes:      texlive-collection-genericextra <= svn39964
Provides:       texlive-collection-plainextra = svn37156.0.obsolete
Obsoletes:      texlive-collection-plainextra <= svn37156.0
Requires:       texlive-base, texlive-collection-basic, texlive-abbr, texlive-abstyles
Requires:       texlive-apnum, texlive-autoaligne, texlive-barr, texlive-bitelist
Requires:       texlive-borceux, texlive-c-pascal, texlive-catcodes, texlive-chronosys
Requires:       texlive-colorsep, texlive-dinat, texlive-dirtree, texlive-docbytex
Requires:       texlive-dowith, texlive-eijkhout, texlive-encxvlna, texlive-epigram
Requires:       texlive-epsf, texlive-epsf-dvipdfmx, texlive-fenixpar, texlive-figflow
Requires:       texlive-fixpdfmag, texlive-fltpoint, texlive-fntproof, texlive-font-change
Requires:       texlive-fontch, texlive-fontname, texlive-gates, texlive-genmisc
Requires:       texlive-getoptk, texlive-gfnotation, texlive-gobble, texlive-graphics-pln
Requires:       texlive-gtl, texlive-hlist, texlive-hyplain, texlive-ifetex
Requires:       texlive-iftex, texlive-insbox, texlive-js-misc, texlive-kastrup
Requires:       texlive-lambda-lists, texlive-langcode, texlive-lecturer, texlive-librarian
Requires:       texlive-listofitems, texlive-mathdots, texlive-metatex, texlive-midnight
Requires:       texlive-mkpattern, texlive-modulus, texlive-multido, texlive-navigator
Requires:       texlive-newsletr, texlive-ofs, texlive-olsak-misc, texlive-path
Requires:       texlive-pdf-trans, texlive-pitex, texlive-placeins-plain, texlive-plainpkg
Requires:       texlive-plipsum, texlive-plnfss, texlive-plstmary, texlive-present
Requires:       texlive-randomlist, texlive-resumemac, texlive-schemata, texlive-shade
Requires:       texlive-simplekv, texlive-systeme, texlive-tabto-generic, texlive-termmenu
Requires:       texlive-tex-ps, texlive-tex4ht, texlive-texapi, texlive-texdate
Requires:       texinfo-tex, texlive-timetable, texlive-tracklang, texlive-treetex
Requires:       texlive-trigonometry, texlive-ulem, texlive-upca, texlive-varisize
Requires:       texlive-xii-doc, texlive-xii-lat, texlive-xlop, texlive-yax

%description -n texlive-collection-plaingeneric
Add-on packages and macros that work with plain TeX, often LaTeX, and 
occasionally other formats.

%package -n texlive-collection-pstricks
Summary:        PSTricks
Version:        svn48230
Requires:       texlive-base, texlive-collection-basic, texlive-collection-plaingeneric, texlive-auto-pst-pdf
Requires:       texlive-bclogo, texlive-dsptricks, texlive-makeplot, texlive-pdftricks
Requires:       texlive-pdftricks2, texlive-pedigree-perl
Requires:       texlive-psbao, texlive-pst-2dplot, texlive-pst-3d, texlive-pst-3dplot
Requires:       texlive-pst-abspos, texlive-pst-am, texlive-pst-antiprism, texlive-pst-arrow
Requires:       texlive-pst-asr, texlive-pst-bar, texlive-pst-barcode, texlive-pst-bezier
Requires:       texlive-pst-blur, texlive-pst-bspline, texlive-pst-calculate, texlive-pst-calendar
Requires:       texlive-pst-cie, texlive-pst-circ, texlive-pst-coil, texlive-pst-contourplot
Requires:       texlive-pst-cox, texlive-pst-dart, texlive-pst-dbicons, texlive-pst-diffraction
Requires:       texlive-pst-electricfield, texlive-pst-eps
Requires:       texlive-pst-eucl, texlive-pst-exa, texlive-pst-fill, texlive-pst-fit
Requires:       texlive-pst-fr3d, texlive-pst-fractal, texlive-pst-fun, texlive-pst-func
Requires:       texlive-pst-gantt, texlive-pst-geo, texlive-pst-geometrictools, texlive-pst-ghsb
Requires:       texlive-pst-gr3d, texlive-pst-grad, texlive-pst-graphicx, texlive-pst-infixplot
Requires:       texlive-pst-intersect, texlive-pst-jtree
Requires:       texlive-pst-knot, texlive-pst-labo, texlive-pst-layout, texlive-pst-lens
Requires:       texlive-pst-light3d, texlive-pst-magneticfield
Requires:       texlive-pst-math, texlive-pst-mirror, texlive-pst-node, texlive-pst-ob3d
Requires:       texlive-pst-ode, texlive-pst-optexp, texlive-pst-optic, texlive-pst-osci
Requires:       texlive-pst-ovl, texlive-pst-pad, texlive-pst-pdf, texlive-pst-pdgr
Requires:       texlive-pst-perspective, texlive-pst-platon
Requires:       texlive-pst-plot, texlive-pst-poker, texlive-pst-poly, texlive-pst-pulley
Requires:       texlive-pst-qtree, texlive-pst-rputover, texlive-pst-rubans, texlive-pst-shell
Requires:       texlive-pst-sigsys, texlive-pst-slpe, texlive-pst-solarsystem, texlive-pst-solides3d
Requires:       texlive-pst-soroban, texlive-pst-spectra
Requires:       texlive-pst-spinner, texlive-pst-spirograph
Requires:       texlive-pst-stru, texlive-pst-support-doc
Requires:       texlive-pst-text, texlive-pst-thick, texlive-pst-tools, texlive-pst-tree
Requires:       texlive-pst-tvz, texlive-pst-uml, texlive-pst-vectorian, texlive-pst-vehicle
Requires:       texlive-pst-vowel, texlive-pst-vue3d, texlive-pst2pdf, texlive-pstricks
Requires:       texlive-pstricks-add, texlive-pstricks_calcnotes-doc
Requires:       texlive-uml, texlive-vaucanson-g, texlive-vocaltract

%description -n texlive-collection-pstricks
PSTricks core and all add-on packages.

%package -n texlive-collection-publishers
Summary:        Publisher styles, theses, etc
Version:        svn48360
Requires:       texlive-base, texlive-collection-latex, texlive-IEEEconf, texlive-IEEEtran
Requires:       texlive-aastex, texlive-abnt, texlive-abntex2, texlive-acmart
Requires:       texlive-acmconf, texlive-active-conf, texlive-adfathesis, texlive-afparticle
Requires:       texlive-afthesis, texlive-aguplus, texlive-aiaa, texlive-ametsoc
Requires:       texlive-anufinalexam-doc, texlive-aomart
Requires:       texlive-apa, texlive-apa6, texlive-apa6e, texlive-arsclassica
Requires:       texlive-articleingud, texlive-asaetr, texlive-ascelike, texlive-aucklandthesis
Requires:       texlive-bangorcsthesis, texlive-bangorexam
Requires:       texlive-bath-bst, texlive-beamer-FUBerlin
Requires:       texlive-beamer-verona, texlive-beilstein
Requires:       texlive-bgteubner, texlive-br-lex, texlive-brandeis-dissertation, texlive-cascadilla
Requires:       texlive-cesenaexam, texlive-chem-journal
Requires:       texlive-cje, texlive-classicthesis, texlive-cleanthesis, texlive-cmpj
Requires:       texlive-confproc, texlive-cquthesis, texlive-dccpaper, texlive-dithesis
Requires:       texlive-ebook, texlive-ebsthesis, texlive-ejpecp, texlive-ekaia
Requires:       texlive-elbioimp, texlive-elsarticle, texlive-elteikthesis, texlive-emisa
Requires:       texlive-erdc, texlive-estcpmm, texlive-etsvthor, texlive-fbithesis
Requires:       texlive-fcavtex, texlive-fcltxdoc, texlive-fei, texlive-gaceta
Requires:       texlive-gatech-thesis, texlive-gradstudentresume
Requires:       texlive-grant, texlive-gsemthesis, texlive-gzt, texlive-h2020proposal
Requires:       texlive-hagenberg-thesis, texlive-har2nat
Requires:       texlive-hecthese, texlive-hithesis, texlive-hobete, texlive-hustthesis
Requires:       texlive-icsv, texlive-ieeepes, texlive-ijmart, texlive-ijsra
Requires:       texlive-imac, texlive-imtekda, texlive-iscram, texlive-jacow
Requires:       texlive-jmlr, texlive-jnuexam, texlive-jpsj, texlive-kdgdocs
Requires:       texlive-kluwer, texlive-ksp-thesis, texlive-ku-template, texlive-langsci
Requires:       texlive-limecv, texlive-lion-msc, texlive-llncsconf, texlive-lni
Requires:       texlive-lps, texlive-matc3, texlive-matc3mem, texlive-mcmthesis
Requires:       texlive-mentis, texlive-mnras, texlive-msu-thesis, texlive-mucproc
Requires:       texlive-mugsthesis, texlive-musuos, texlive-muthesis, texlive-mynsfc
Requires:       texlive-nature, texlive-navydocs, texlive-nddiss, texlive-ndsu-thesis
Requires:       texlive-novel, texlive-nwejm, texlive-nih, texlive-nihbiosketch
Requires:       texlive-nostarch, texlive-nrc, texlive-onrannual, texlive-opteng
Requires:       texlive-philosophersimprint, texlive-pittetd
Requires:       texlive-pkuthss, texlive-powerdot-FUBerlin
Requires:       texlive-powerdot-tuliplab, texlive-pracjourn
Requires:       texlive-procIAGssymp, texlive-proposal, texlive-ptptex, texlive-psu-thesis
Requires:       texlive-resphilosophica, texlive-resumecls
Requires:       texlive-revtex, texlive-revtex4, texlive-rutitlepage, texlive-ryethesis
Requires:       texlive-sageep, texlive-sapthesis, texlive-scrjrnl, texlive-schule
Requires:       texlive-scientific-thesis-cover, texlive-sduthesis
Requires:       texlive-seuthesis, texlive-seuthesix, texlive-soton, texlive-sphdthesis
Requires:       texlive-spie, texlive-sr-vorl, texlive-stellenbosch, texlive-suftesi
Requires:       texlive-sugconf, texlive-tabriz-thesis, texlive-texilikechaps, texlive-texilikecover
Requires:       texlive-thesis-ekf, texlive-thesis-gwu, texlive-thesis-titlepage-fhac, texlive-thucoursework
Requires:       texlive-thuthesis, texlive-timbreicmc, texlive-tlc-article, texlive-topletter
Requires:       texlive-toptesi, texlive-tudscr, texlive-tugboat, texlive-tugboat-plain
Requires:       texlive-turabian, texlive-tui, texlive-uaclasses, texlive-uafthesis
Requires:       texlive-uantwerpendocs, texlive-ucbthesis
Requires:       texlive-ucdavisthesis, texlive-ucsmonograph
Requires:       texlive-ucthesis, texlive-uestcthesis, texlive-uhhassignment, texlive-uiucredborder
Requires:       texlive-uiucthesis, texlive-ulthese, texlive-umbclegislation, texlive-umthesis
Requires:       texlive-umich-thesis, texlive-unamth-template-doc
Requires:       texlive-unamthesis, texlive-unitn-bimrep
Requires:       texlive-univie-ling, texlive-unswcover, texlive-uothesis, texlive-urcls
Requires:       texlive-uowthesis, texlive-uowthesistitlepage
Requires:       texlive-uspatent, texlive-ut-thesis, texlive-uwthesis, texlive-vancouver
Requires:       texlive-wsemclassic, texlive-xcookybooky
Requires:       texlive-xduthesis, texlive-yathesis, texlive-york-thesis

%description -n texlive-collection-publishers
collection-publishers package

%package -n texlive-collection-xetex
Summary:        XeTeX and packages
Version:        svn47630
Requires:       texlive-base, texlive-collection-basic, texlive-arabxetex, texlive-awesomebox
Requires:       texlive-bidi-atbegshi, texlive-bidicontour
Requires:       texlive-bidipagegrid, texlive-bidishadowtext
Requires:       texlive-bidipresentation, texlive-cqubeamer
Requires:       texlive-fixlatvian, texlive-font-change-xetex
Requires:       texlive-fontbook, texlive-fontwrap, texlive-interchar, texlive-na-position
Requires:       texlive-philokalia, texlive-ptext, texlive-quran, texlive-realscripts
Requires:       texlive-simple-resume-cv, texlive-simple-thesis-dissertation
Requires:       texlive-ucharclasses, texlive-unicode-bidi
Requires:       texlive-unisugar, texlive-xebaposter, texlive-xechangebar, texlive-xecjk
Requires:       texlive-xecolor, texlive-xecyr, texlive-xeindex, texlive-xesearch
Requires:       texlive-xespotcolor, texlive-xetex, texlive-xetex-itrans, texlive-xetex-pstricks
Requires:       texlive-xetex-tibetan, texlive-xetexconfig
Requires:       texlive-xetexfontinfo, texlive-xetexko, texlive-xevlna
Provides:       tex(xetex) = %{tl_version}
Obsoletes:      texlive-texmf-xetex < %{tl_version}

%description -n texlive-collection-xetex
Packages for XeTeX, the Unicode/OpenType-enabled TeX by
Jonathan Kew, http://tug.org/xetex.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names=""
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}%{_infodir}/
cp -R %{buildroot}/%{_texdir}/texmf-dist/doc/man %{buildroot}%{_datadir}/
mv %{buildroot}/%{_texdir}/texmf-dist/doc/info/* %{buildroot}%{_infodir}/
rm -f %{buildroot}%{_infodir}/fontname.info*
rm -f %{buildroot}%{_datadir}/man/man1/etex.*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/doc/etex/base/*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/doc/fonts/fontname/*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/doc/generic/arrayjobx/*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/doc/latex/arraysort/*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man/man1/etex.*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tex/generic/arrayjobx/*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tex/latex/arraysort/arraysort.sty
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*
install -d %{buildroot}%{_sysconfdir}/texlive/tex/generic/config

%files -n texlive-scheme-basic
%defattr(-,root,root,755)

%files -n texlive-scheme-context
%defattr(-,root,root,755)

%files -n texlive-scheme-gust
%defattr(-,root,root,755)

%files -n texlive-scheme-medium
%defattr(-,root,root,755)

%files -n texlive-scheme-minimal
%defattr(-,root,root,755)

%files -n texlive-scheme-small
%defattr(-,root,root,755)

%files -n texlive-collection-basic
%defattr(-,root,root,755)

%files -n texlive-collection-bibtexextra
%defattr(-,root,root,755)

%files -n texlive-collection-binextra
%defattr(-,root,root,755)

%files -n texlive-collection-context
%defattr(-,root,root,755)

%files -n texlive-collection-fontsextra
%defattr(-,root,root,755)

%files -n texlive-collection-fontsrecommended
%defattr(-,root,root,755)

%files -n texlive-collection-fontutils
%defattr(-,root,root,755)

%files -n texlive-collection-formatsextra
%defattr(-,root,root,755)

%files -n texlive-collection-games
%defattr(-,root,root,755)

%files -n texlive-collection-humanities
%defattr(-,root,root,755)

%files -n texlive-collection-langarabic
%defattr(-,root,root,755)

%files -n texlive-collection-langchinese
%defattr(-,root,root,755)

%files -n texlive-collection-langcjk
%defattr(-,root,root,755)

%files -n texlive-collection-langcyrillic
%defattr(-,root,root,755)

%files -n texlive-collection-langczechslovak
%defattr(-,root,root,755)

%files -n texlive-collection-langenglish
%defattr(-,root,root,755)

%files -n texlive-collection-langeuropean
%defattr(-,root,root,755)

%files -n texlive-collection-langfrench
%defattr(-,root,root,755)

%files -n texlive-collection-langgerman
%defattr(-,root,root,755)

%files -n texlive-collection-langgreek
%defattr(-,root,root,755)

%files -n texlive-collection-langitalian
%defattr(-,root,root,755)

%files -n texlive-collection-langjapanese
%defattr(-,root,root,755)

%files -n texlive-collection-langkorean
%defattr(-,root,root,755)

%files -n texlive-collection-langpolish
%defattr(-,root,root,755)

%files -n texlive-collection-langportuguese
%defattr(-,root,root,755)

%files -n texlive-collection-langspanish
%defattr(-,root,root,755)

%files -n texlive-collection-latex
%defattr(-,root,root,755)

%files -n texlive-collection-latexextra
%defattr(-,root,root,755)

%files -n texlive-collection-latexrecommended
%defattr(-,root,root,755)

%files -n texlive-collection-luatex
%defattr(-,root,root,755)

%files -n texlive-collection-mathscience
%defattr(-,root,root,755)

%files -n texlive-collection-metapost
%defattr(-,root,root,755)

%files -n texlive-collection-music
%defattr(-,root,root,755)

%files -n texlive-collection-pictures
%defattr(-,root,root,755)

%files -n texlive-collection-plaingeneric
%defattr(-,root,root,755)

%files -n texlive-collection-pstricks
%defattr(-,root,root,755)

%files -n texlive-collection-publishers
%defattr(-,root,root,755)

%files -n texlive-collection-xetex
%defattr(-,root,root,755)


%changelog
* Thu Aug 19 2021 sunguoshuai <sunguoshuai@huawei.com> - 8:2018-25
- Remove texlive-collection-langother,texlive-scheme-full,texlive-scheme-tetex
  who requires texlive-vntex

* Mon May 24 2021 maminjie <maminjie1@huawei.com> - 8:2018-25
- Remove the Requires texlive-venturisadf,texlive-wsuipa,texlive-vntex (are dropped)

* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
