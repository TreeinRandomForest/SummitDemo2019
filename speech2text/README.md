#### Create and activate a virtualenv
`virtualenv -p python3 $HOME/tmp/deepspeech-venv/`

`source $HOME/tmp/deepspeech-venv/bin/activate`

#### Install DeepSpeech
`pip install deepspeech`

#### OR Install DeepSpeech CUDA enabled package
`pip install deepspeech-gpu`

#### Download pre-trained English model and extract
`curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.1/deepspeech-0.6.1-models.tar.gz`
`tar xvf deepspeech-0.6.1-models.tar.gz`

#### Transcribe audio file and output dollar value
`text=$(deepspeech --model deepspeech-0.6.1-models/output_graph.pbmm --lm deepspeech-0.6.1-models/lm.binary --trie deepspeech-0.6.1-models/trie --audio my_audio_file.wav)` 

`python text2value.py --value="$text"`

