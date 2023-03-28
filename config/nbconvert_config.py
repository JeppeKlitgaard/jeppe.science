c = get_config()

c.NbConvertApp.recursive_glob = True
c.NbConvertApp.notebooks = ["**/*.ipynb"]
c.NbConvertApp.export_format = "markdown"
c.NbConvertApp.output_files_dir = "{notebook_name}"
c.NbConvertApp.output_base = "{notebook_name}.generated"
c.NbConvertApp.use_output_suffix = True

# c.ExecutePreprocessor.enabled = True
# c.ExecutePreprocessor.skip_cells_with_tag = "skip_cell"

c.TagRemovePreprocessor.remove_cell_tags = ("hide_cell", "hc", )
c.TagRemovePreprocessor.remove_input_tags = ("hide_input", "hi",)
c.TagRemovePreprocessor.remove_all_outputs_tags = ("hide_output", "ho",)
c.TagRemovePreprocessor.enabled = True

# Put ExecutePreprocessor before TagRemovePreprocessor to make
# remove_all_outputs_tags work
# https://github.com/jupyter/nbconvert/issues/1300
c.Exporter.preprocessors = [
    # "nbconvert.preprocessors.ExecutePreprocessor",
    "nbconvert.preprocessors.TagRemovePreprocessor",
    # "nbconvert.preprocessors.RegexRemovePreprocessor",
    # "nbconvert.preprocessors.ClearOutputPreprocessor",
    # "nbconvert.preprocessors.coalesce_streams",
    # "nbconvert.preprocessors.SVG2PDFPreprocessor",
    # "nbconvert.preprocessors.LatexPreprocessor",
    # "nbconvert.preprocessors.HighlightMagicsPreprocessor",
    # "nbconvert.preprocessors.ExtractOutputPreprocessor",
    # "nbconvert.preprocessors.ClearMetadataPreprocessor",
]
