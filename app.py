import json
import numpy as np
import torch
from transformers import pipeline


class InferlessPythonModel:
    def initialize(self):
        self.generator = pipeline(
            "##task_type##",
            model="##huggingface_name##",
            device=0,
            use_auth_token="##user_auth_token##",
        )

    def infer(self, text):
        pipeline_output = self.generator(text)
        return pipeline_output[0]["hello"]

    def finalize(self):
        self.pipe = None
