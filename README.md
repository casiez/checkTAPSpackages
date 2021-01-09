# checkTAPSpackages

Allows to check an article written in LaTeX only uses standard packages listed on the [TAPS page](https://www.acm.org/publications/taps/accepted-latex-packages)

Install using ```pip install checkTAPSpackages```

1. Compile your document by adding ```\listfiles``` below ```\documentclass```
1. Run ```checkTAPSpackages yourGeneratedLogFile.log```

Use ```--all``` option to show all packages used.

