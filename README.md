# Facebook/Bart-Large-CNN

Facebook AI's facebook/bart-large-cnn model is a pre-trained Seq2Seq model that uses the BERT architecture to perform various NLP tasks, such as summarization, text generation, question answering, and machine translation. It has over 400 million trainable parameters, requiring substantial computational resources to train and fine-tune. Despite this, it's a powerful tool for NLP applications once pre-trained and fine-tuned on smaller datasets.

The model's ability to generate high-quality summaries of longer texts stands out, making it particularly well-suited for summarization tasks. However, it also excels in other NLP tasks, making it a versatile tool for different applications in the field of NLP.

Overall, the facebook/bart-large-cnn model is a highly sophisticated and versatile NLP model that can be used for a wide range of applications. Its potential lies in its ability to generate high-quality summaries and perform various NLP tasks with high accuracy once fine-tuned on a specific dataset.# Facebook/Bart-Large-Cnn

## Input
---
Following is the json format of the input required to make request to the inference server.
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
---
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