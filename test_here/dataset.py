from torch.utils.data import DataLoader
from torch.utils.data import Dataset
from pathlib import Path
from typing import Any,Dict
import json

datasetPath=Path(__file__).parent.parent.joinpath("datasets")
fileName = "alpaca.json"

class DeliusDataset(Dataset):
    def __init__(self) -> None:
        super().__init__()
        with datasetPath.joinpath(fileName).open(
            'r',encoding='utf8'
        ) as jsn:
            self.data=json.load(jsn)
        self.instructions=self.data['instruction']
        self.inputs=self.data['input']
        self.outputs=self.data['output']
        self.texts=self.data['text']

    def __getitem__(self, index) -> Dict[str,str]:
        _instruction=self.instructions[str(index)]
        _input=self.inputs[str(index)]
        _output=self.outputs[str(index)]
        _text=self.texts[str(index)]
        return {
            "instruction":_instruction,
            "input":_input,
            "output":_output,
            "text":_text,
        }

    def __len__(self):
        return len(self.instructions)
    
