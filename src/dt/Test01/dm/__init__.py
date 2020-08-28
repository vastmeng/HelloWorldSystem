
import digital_machine
import digital_machine.templates as tmpl
from digital_machine import dmCompile

from .Furnace_Blast import Furnace_Blast
from .computer_room import computer_room
from .workshop import workshop


try:
    from ._legacy import models as legacy_models
except ModuleNotFoundError:
    legacy_models = {}

py_model_collection = tmpl.PyModelCollection()



Furnace_Blast().generate_model(digital_machine.digital_twin_model("Test01", "Furnace_Blast"), py_model_collection)
computer_room().generate_model(digital_machine.digital_twin_model("Test01", "computer_room"), py_model_collection)
workshop().generate_model(digital_machine.digital_twin_model("Test01", "workshop"), py_model_collection)


models = py_model_collection.models
models.update(legacy_models)
