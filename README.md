# textcat

#### Text classification models learn to assign one or more labels to text. You can use text classification over short pieces of text like sentences or headlines, or longer texts like paragraphs or even whole documents. One of our top tips for practical NLP is to break down complicated NLP tasks into text classification problems whenever possible. Text classification problems tend to be easier to annotate consistently, and the models need fewer examples to reach high accuracy.

## textcat.manual

#### Manually annotate categories that apply to a text. If only one label is set, the  classification interface is used. If more than one label is specified, the  choice interface is used and categories are added as multiple choice options. If the --exclusive flag is set, categories become mutually exclusive, meaning that only one can be selected during annotation.
``` 
prodigy textcat.manual dataset source --loader --label --exclusive --exclude 
```

## textcat.correct

#### Create training data for an existing trained text classification model by correcting the model’s suggestions. The --threshold is used to determine whether a label should be pre-selected, e.g. if it’s set to 0.5 (default), all labels with a score of 0.5 and above will be checked automatically. Prodigy will automatically infer whether the categories are mutually exclusive, based on the component configuration.
```
prodigy textcat.correct dataset spacy_model source --loader --label --update --threshold --component --exclude
```

## textcat.teach


#### Collect the best possible training data for a text classification model by using a model in the loop. Based on your annotations, Prodigy will decide which questions to ask next. All annotations will be stored in the database. If a patterns file is supplied via the --patterns argument, the matches will be included in the stream and the matched spans are highlighted, so you’re able to tell which words or phrases the selection was based on. Note that the exact pattern matches have no influence when updating the model – they’re only used to help pre-select examples for annotation.
```
prodigy textcat.teach dataset spacy_model source --loader --label --patterns --exclude
```
