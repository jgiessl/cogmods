import os
import sys

import ccobra

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..")))
from modular_models.models.basic_models import VerbalModels
from modular_models.models.ccobra_models.interface import CCobraWrapper


class CCobraVerbalModels(CCobraWrapper, ccobra.CCobraModel):
    def __init__(self):
        CCobraWrapper.__init__(self, model=VerbalModels)
        ccobra.CCobraModel.__init__(self, "Verbal Models", ["syllogistic"], ["single-choice"])

