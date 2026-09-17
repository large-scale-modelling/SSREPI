# SSREPI

**S**ocial **S**imulation **REP**ository **I**nterface (SSREPI)

This is the specification document for the SSREPI metadata. An implentation of this specification can be found at [https://github.Acom/large-scale-modelling/miracle](https://github.com/large-scale-modelling/RECORD), once a working version has been released. This is the:

**R**eproducible
**E**xecution
**C**ollection and
**O**notological
**R**epresentation of
**D**ata

provenance recording framework. This is platform agnostic framework for recording the provenance of data generated, particularly by social simulation models, but can used by other modelling frameworks. 

The markdown version of the standard is [here](https://github.com/large-scale-modelling/SSREPI/blob/main/miracle-specification.md), and the pdf version of the standard is [here](https://github.com/large-scale-modelling/SSREPI/blob/main/miracle-specification.pdf).

If you want a word version of this specification, then `pandoc` can produce documents compatible with Microsoft Word. Please note we are trying to stay away from effectively proprietary formats.

Suggested citation:

[Polhill, G.](https://orcid.org/0000-0002-8596-0590), 
[Milazzo, L.](https://orcid.org/0000-0002-9451-8964), 
[Parker D.](https://orcid.org/0000-0001-8988-193X), 
Jin, X., 
[Pritchard C.](https://orcid.org/0000-0002-4557-8602), 
[Lee, J.-S.](https://orcid.org/0000-0002-4158-2700), 
[Filatova, T.](https://orcid.org/0000-0002-3546-6930),
[Voinov, A.](https://orcid.org/0009-0000-8002-2813),
[Dawson T.](https://orcid.org/0000-0002-4314-1378) and
[Salt, D.](https://orcid.org/0000-0001-5186-9388) 
(2022) MIRACLE simulation outputs metadata specification, _Technical Report, The James Hutton Institute, Aberdeen, September 2023_ (version 3.0.0). 

```BibTeX
@techreport{polhill2022ssrepi,
  author      = {Polhill, Gary and Milazzo, Lorenzo and Parker, Dawn and Jin, Xiongbing and Pritchard, Calvin and Lee, Ju-Sung and Filatova, Tatiana and Voinov, Alexey and Dawson, Terry and Salt, Doug},
  title       = {MIRACLE simulation outputs metadata specification (Formerly: Social Simulation Repository Interface (SSREPI))},
  institution = {The James Hutton Institute},
  year        = {2026},
  number      = {version 3.0.0},
  type        = {Specification},
  address     = {Aberdeen},
  month       = {September},
  url         = {https://github.com/large-scale-modelling/SSREPI/blob/main/miracle-specification.pdf},
}
```
<!--  doi         = {10.5281/zenodo.15234672} -->

## Notes.

The large part of the documentation is created by the code itself in RECORD. This is done in the following manner

```
record-documentation.py > miracle-specification-body.md
```

This, in conjunction with 

+ `miracle-specification-start.md` and
+ `miracle-specification-end.md`

can be used to provide 

+ miracle-specification-full.md, which is the specification in a single file. This can be converted to a pdf in two ways:

1. make-specification.(ps1|sh) - which uses pandoc to convert the markdown to pdf, or
2. make-latex-specification.(ps1|sh) - which produces a tex file for input to `pdflatex`.

The latter is for preparation of a manuscript for submission to arxiv or a journal. The former is for general use.

Note to use either of these you need to install the pandoc-crossref filter,
which is used to generate the references section of the specification. This is
done by downloading the relevant binary from
[here](https://github.com/lierdakil/pandoc-crossref/releases), unzipping it and
placing it in this directory.

```
## Manifest

+ `arxiv-version` - The directory containing the version that is being published on Arxiv. This is a copy of the files in the root directory and the `img` directory. This has been flattened to a single directory as per the instructions from Arxiv.
+ `img` - the images in both mermaid and png format used in the specification. The mermaid files are used to generate the png files. The png files are used in the pdf version of the specification. Pandoc can process mermaid files directly, but the pandoc is quite picky about the version of mermaid that it uses, so the png files are used to ensure that the diagrams are rendered correctly.
+ `previous-versions` - older versions of the specification, which are not maintained. These are provided for reference only.
+ `citations.bib` -  a list of citations used in the specification, in bibtex format. This is used to generate the references section of the specification.
+ `LICENSE.md` -  A copy of the GPLv3 license under which this specification is released.
+ `make-latex-specification.ps1` - Makes a full latex version of the specification, which can used by `pdflatex` to produce a pdf version of the specification. This is for submission to journals or arxiv.
+ `make-specification.ps1|sh` - Makes a full pdf version of the specification, which can be used for general use. This uses pandoc to convert the markdown to pdf. 
+ `miracle-specification-body.md` - Start of the specification in markdown format.
+ `miracle-specification-end.md` - End of the specification in mardown format
+ `miracle-specification-full.pdf` - pdflatex version of specification produced by `pdflatex` and `make-latex-specification.(sh|ps1)`. 
+ `miracle-specification-full.tex` - text file produced by `make-latex-specification.(sh|ps1)` for use with `pdflatex` to produce a pdf version of the specification. This is for submission to journals or arxiv.
+ `miracle-specification-start.md` - End of the specification in mardown format
+ `miracle-specification.md` - full markdown version of the standard produced by `make-specification.(sh|ps1)`.
+ `miracle-specification.pdf` - pdflatex version of the specification produced by `make-specification.(sh|ps1)`.
+ `README.md` - 


## Further reading

Jin, X., Robinson, K., Lee, A., Polhill, J. G., Pritchard, C. and Parker, D. (2017) [MIRACLE: A prototype cloud-based reproducible data analysis and visualization platform for outputs of agent-based models](https://doi.org/10.1016/j.envsoft.2017.06.010). Environmental Modelling and Software 96, 172-180.

Polhill, G., Dawson, T., Parker, D., Jin, X., Robinson, K., Filatova, T., Voinov, A., Barton, M., Pignotti, E. and Edwards, P. (2014) [Towards metadata standards for sharing simulation outputs](https://core.ac.uk/download/pdf/78523531.pdf). In Miguel, F. J., Amblard, F., Barceló, J. A., and Madella, M. (eds.) _Advances in Computational Social Science and Social Simulation: Proceedings of the Social Simulation Conference 2014, Barcelona, Catalunya (Spain), September 15_ Barcelona: Autònoma University of Barcelona, 2014, [DDD repository record 125597](http://ddd.uab.cat/record/125597), pp. 624-627

Polhill G., Milazzo L., Dawson T., Gimona A. and Parker D. (2017) [Lessons learned replicating the analysis of outputs from a social simulation of biodiversity incentivisation](https://doi.org/10.1007/978-3-319-47253-9_32). In: Jager W., Verbrugge R., Flache A., de Roo G., Hoogduin L. and Hemelrijk C. (eds.) Advances in Social Simulation 2015. Advances in Intelligent Systems and Computing 528. Cham: Springer. pp. 355-365.

## Acknowledgements

Earlier work on this specification was funded by the [Third Round](https://diggingintodata.org/awards/2013) of the [Digging into Data Challenge](https://diggingintodata.org/), in a project named [MIRACLE](https://diggingintodata.org/awards/2013/project/mining-relationships-among-variables-large-datasets-complex-systems-miracle). 

Further work has been funded by the Scottish Government Rural and Environment Science and Analytical Services Division (project reference [JHI-C5-1](https://large-scale-modelling.hutton.ac.uk/))
