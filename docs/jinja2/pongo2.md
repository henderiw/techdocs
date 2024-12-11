## builtin

https://github.com/flosch/pongo2/blob/master/filters_builtin.go

```go
    RegisterFilter("escape", filterEscape)
	RegisterFilter("e", filterEscape) // alias of `escape`
	RegisterFilter("safe", filterSafe)
	RegisterFilter("escapejs", filterEscapejs)

	RegisterFilter("add", filterAdd)
	RegisterFilter("addslashes", filterAddslashes)
	RegisterFilter("capfirst", filterCapfirst)
	RegisterFilter("center", filterCenter)
	RegisterFilter("cut", filterCut)
	RegisterFilter("date", filterDate)
	RegisterFilter("default", filterDefault)
	RegisterFilter("default_if_none", filterDefaultIfNone)
	RegisterFilter("divisibleby", filterDivisibleby)
	RegisterFilter("first", filterFirst)
	RegisterFilter("floatformat", filterFloatformat)
	RegisterFilter("get_digit", filterGetdigit)
	RegisterFilter("iriencode", filterIriencode)
	RegisterFilter("join", filterJoin)
	RegisterFilter("last", filterLast)
	RegisterFilter("length", filterLength)
	RegisterFilter("length_is", filterLengthis)
	RegisterFilter("linebreaks", filterLinebreaks)
	RegisterFilter("linebreaksbr", filterLinebreaksbr)
	RegisterFilter("linenumbers", filterLinenumbers)
	RegisterFilter("ljust", filterLjust)
	RegisterFilter("lower", filterLower)
	RegisterFilter("make_list", filterMakelist)
	RegisterFilter("phone2numeric", filterPhone2numeric)
	RegisterFilter("pluralize", filterPluralize)
	RegisterFilter("random", filterRandom)
	RegisterFilter("removetags", filterRemovetags)
	RegisterFilter("rjust", filterRjust)
	RegisterFilter("slice", filterSlice)
	RegisterFilter("split", filterSplit)
	RegisterFilter("stringformat", filterStringformat)
	RegisterFilter("striptags", filterStriptags)
	RegisterFilter("time", filterDate) // time uses filterDate (same golang-format)
	RegisterFilter("title", filterTitle)
	RegisterFilter("truncatechars", filterTruncatechars)
	RegisterFilter("truncatechars_html", filterTruncatecharsHTML)
	RegisterFilter("truncatewords", filterTruncatewords)
	RegisterFilter("truncatewords_html", filterTruncatewordsHTML)
	RegisterFilter("upper", filterUpper)
	RegisterFilter("urlencode", filterUrlencode)
	RegisterFilter("urlize", filterUrlize)
	RegisterFilter("urlizetrunc", filterUrlizetrunc)
	RegisterFilter("wordcount", filterWordcount)
	RegisterFilter("wordwrap", filterWordwrap)
	RegisterFilter("yesno", filterYesno)

	RegisterFilter("float", filterFloat)     // pongo-specific
	RegisterFilter("integer", filterInteger) // pongo-specific
```