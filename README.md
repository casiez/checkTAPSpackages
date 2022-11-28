[![PyPI Version](https://img.shields.io/pypi/v/checkTAPSpackages)](https://pypi.org/project/checkTAPSpackages/)
[![License](https://img.shields.io/github/license/casiez/checkTAPSpackages)](LICENSE)

# checkTAPSpackages

Gets all packages used in a LaTeX document and checks they are in the [list of packages allowed by TAPS](https://www.acm.org/publications/taps/accepted-latex-packages)

Tested on macOS, should work on Linux, could work on Windows.

Install using ```pip install -U checkTAPSpackages```

1. Compile your document by adding ```\listfiles``` below ```\documentclass```
1. Run ```checkTAPSpackages yourGeneratedLogFile.log```

Use ```--all``` option to show all packages used.

Use ```--expand``` to expand the list of subpackages, which produces something like the following:

```
colortbl.sty         => NOT SUPPORTED
eurosym.sty          => NOT SUPPORTED
flushend.sty         => NOT SUPPORTED
macros.sty           => NOT SUPPORTED
   paralist.sty         => NOT SUPPORTED
mathtools.sty        => NOT SUPPORTED
   mhsetup.sty          => NOT SUPPORTED
mhsetup.sty          => NOT SUPPORTED
paralist.sty         => NOT SUPPORTED
submission.sty       => NOT SUPPORTED
   mathtools.sty        => NOT SUPPORTED
   mhsetup.sty          => NOT SUPPORTED
   wasysym.sty          => NOT SUPPORTED
   colortbl.sty         => NOT SUPPORTED
   ulem.sty             => NOT SUPPORTED
   eurosym.sty          => NOT SUPPORTED
   flushend.sty         => NOT SUPPORTED
ulem.sty             => NOT SUPPORTED
wasysym.sty          => NOT SUPPORTED
```

Use ```--diff``` option to list newly supported or not supported packages.
