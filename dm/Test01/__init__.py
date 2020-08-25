
import digital_machine
import digital_machine.templates as tmpl
from digital_machine import dmCompile

from .computer_root import computer_root
from .Furnace_Blast import Furnace_Blast
from .workshop import workshop


try:
    from ._legacy import models as legacy_models
except ModuleNotFoundError:
    legacy_models = {}

py_model_collection = tmpl.PyModelCollection()



computer_root().generate_model(digital_machine.digital_twin_model("Test01", "computer_root"), py_model_collection)
Furnace_Blast().generate_model(digital_machine.digital_twin_model("Test01", "Furnace_Blast"), py_model_collection)
workshop().generate_model(digital_machine.digital_twin_model("Test01", "workshop"), py_model_collection)


models = py_model_collection.models
models.update(legacy_models)
