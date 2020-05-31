# text summarization with BART
from ktrain import text
ts = text.TransformerSummarizer()

some_long_document = ""
ts.summarize(some_long_document)

# NER with BioBERT embeddings
import ktrain
from ktrain import text as txt
x_train= [['IL-2', 'responsiveness', 'requires', 'three', 'distinct', 'elements', 'within', 'the', 'enhancer', '.'], ...]
y_train=[['B-protein', 'O', 'O', 'O', 'O', 'B-DNA', 'O', 'O', 'B-DNA', 'O'], ...]

(trn, val, preproc) = txt.entities_from_array(x_train, y_train)
model = txt.sequence_tagger('bilstm-bert', preproc, bert_model='monologg/biobert_v1.1_pubmed')
learner = ktrain.get_learner(model, train_data=trn, val_data=val, batch_size=128)
learner.fit(0.01, 1, cycle_len=5)