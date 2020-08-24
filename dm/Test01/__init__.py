
import digital_machine
import digital_machine.templates as tmpl
from digital_machine import dmCompile

from .abstract_model_0 import abstract_model_0
from .Furnace_Blast import Furnace_Blast
from .workshop import workshop


try:
    from ._legacy import models as legacy_models
except ModuleNotFoundError:
    legacy_models = {}

py_model_collection = tmpl.PyModelCollection()

dmCompile.get_context().put_abstract_model("{Test01}abstract_model_0", abstract_model_0)


Furnace_Blast().generate_model(digital_machine.digital_twin_model("Test01", "Furnace_Blast"), py_model_collection)
workshop().generate_model(digital_machine.digital_twin_model("Test01", "workshop"), py_model_collection)


models = py_model_collection.models
models.update(legacy_models)
