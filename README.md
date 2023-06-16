# Facebook/Bart-Large-CNN

Facebook's Bart-Large-CNN is a state-of-the-art model for performing the task for **text-summarization**. You can use this template to import and run a test summarization using Bart-Large-CNN model in the Inferless platform.

---
## Prerequisites
- **Git**. You would need git installed on your system if you wish to customize the repo after forking.
- **Python>=3.8**. You would need Python to customize the code in the `app.py` according to your needs.
- **Curl**. You would need Curl if you want to make API calls from the terminal itself.

---
##  Quick Start
Here is a quick start to help you get up and running with Bart-Large-CNN on Inferless.

### STEP 1: Fork the repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.
This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### STEP 2: Import the Model in Inverness

Log in to your inferless account https://console.inferless.com/  and click the Add Model button.

Select the model's training framework(Pytorch/Tensorflow/ONNX) and choose **Repo(custom code)** as your model source.

Then use the forked repo URL as the **Model URL**.

The following is a sample Input and Output JSON for this model which you can use while importing this model on Inferless.

### Input
```json
{
  "inputs": [
    {
      "data": [
        "Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken words in much the same way human beings can. NLP combines computational linguistics—rule-based modeling of human language—with statistical, machine learning, and deep learning models. Together, these technologies enable computers to process human language in the form of text or voice data and to ‘understand’ its full meaning, complete with the speaker or writer’s intent and sentiment."
      ],
      "name": "text",
      "shape": [
        1
      ],
      "datatype": "BYTES"
    }
  ]
}
```

### Output
```json
{
  "outputs": [
    {
      "name": "summary_text",
      "shape": [
        1
      ],
      "datatype": "BYTES"
    }
  ]
}
```

Refer to [this link](https://docs.inferless.com/integrations/github-custom-code) for more information on model import.

### STEP 3 Call the Model using Inferless Endpoint 

Following is an example of the curl command you can use to make inferences. You can find the exact curl command in the Model's API page in Inferless.

```bash
curl --location '<your_inference_url>' \
          --header 'Content-Type: application/json' \
          --header 'Authorization: Bearer <your_api_key>' \
          --data '{
                    "inputs": [
                        {
                            "data": [
                                "Enter the content here..."
                            ],
                            "name": "text",
                            "shape": [
                                1
                            ],
                            "datatype": "BYTES"
                        }
                    ]
                }'
```

---
## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in the inputs. Refer to [input](#input) for more.

```python
def infer(self, inputs):
    prompt = inputs["prompt"]
```

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the gpu by setting `self.pipe = None`.




For more information refer to the [Inferless docs](https://docs.inferless.com/).
