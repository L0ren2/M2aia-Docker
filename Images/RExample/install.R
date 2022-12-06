if (!require("Cardinal")) {
	if (!requireNamespace("BiocManager", quietly = TRUE)) {
		install.packages("BiocManager")
	}
	if (!requireNamespace("dbplyr", quietly = TRUE)) {
		install.packages("dbplyr")
	}
       BiocManager::install("Cardinal")
	if (!require("readr"))
		install.packages("readr")
}
