# Facebook/Bart-Large-CNN

Facebook's Bart-Large-CNN is a state of the art model for performing summarization. You can use this template to import and run a Bart-Large-CNN model in the Inferless platform.

## Prerequisites
- **Git**. You would need git installed on your system if you wish to customize the repo after forking.
- **Python>=3.8**. You would need Python to customize the code in the `app.py` according to your needs.
- **Curl**. You would need Curl if you want to make API calls from the terminal itself.

## Quick Start
Here is a quick start to help you get up and running with Bart-Large-CNN on Inferless.

### Step 1: Fork the repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### Step 2: Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the Add Model button.

In the Step 2, Choose the source, select the github repo option and give the repo url in the third step, create model.

Enter all the required details and you've successfully imported the model!

## Curl Command
Following is an example of the CURL command you can use to make inference. You can find the exact curl command in the Model's API page in Inferless.

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

## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in inputs. Refer to [input](#input) for more.

```python
def infer(self, inputs):
    prompt = inputs["prompt"]
```

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the gpu by setting `self.pipe = None`.


## Input
This is an example input json to make the request. The "inputs" will be a key refering to list of dictionaries, each representing a differnet input type.
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

## Output
Following is the json format of the output produced for the inference request.
```json
{
  "outputs": [
    {
      "data": [
        "Natural language processing (NLP) aims to give computers the ability to understand text and spoken words. NLP combines computational linguistics with statistical, machine learning, and deep learning models. Together, these technologies enable computers to process human language in the form of text or voice data and to ‘understand’ its full meaning."
      ],
      "name": "summary_text",
      "shape": [
        1
      ],
      "datatype": "BYTES"
    }
  ]
}
```

For more information refer to the [Inferless docs](https://docs.inferless.com/).
