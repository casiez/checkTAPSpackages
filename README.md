# checkTAPSpackages

Gets all packages used in a LaTeX document and checks they are in the [list of packages allowed by TAPS](https://www.acm.org/publications/taps/accepted-latex-packages)

Install using ```pip install checkTAPSpackages```

1. Compile your document by adding ```\listfiles``` below ```\documentclass```
1. Run ```checkTAPSpackages yourGeneratedLogFile.log```

Use ```--all``` option to show all packages used.

