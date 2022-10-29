c = get_config()

c.NbConvertApp.recursive_glob = True
c.NbConvertApp.notebooks = ["**/*.ipynb"]
c.NbConvertApp.export_format = "markdown"

c.ExecutePreprocessor.enabled = True

c.TagRemovePreprocessor.enabled = True
c.TagRemovePreprocessor.remove_cell_tags = ("hide_cell",)
c.TagRemovePreprocessor.remove_input_tags = ("hide_input",)
c.TagRemovePreprocessor.remove_all_outputs_tags = ("hide_output",)