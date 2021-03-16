
# tokenizer for DL models
#df is the dataframe with the columns name and labels for training tokenizer
def tokens(df):
    from keras.preprocessing.text import Tokenizer
    token = Tokenizer(num_words = None,char_level = True)
    token.fit_on_texts(df.name)
    return token
#funtion for pad seq
#input train dataframe and test dataframe and tokenizer
def pad_seq(train_df,test_df,token):
    from keras.preprocessing.sequence import pad_sequences
    train_seq = pad_sequences(token.texts_to_sequences(train_df.name),maxlen = 50)
    test_seq = pad_sequences(token.texts_to_sequences(test_df.name),maxlen = 50)
    return train_seq,test_seq
#takes train dataframe and test dataframe as inputs and returns their enoding
def encode_labels(train_df,test_df):
    train_lab = np.array([1 if x == 'person' else 0 for x in train_df.label])
    test_lab = np.array([1 if x == 'person' else 0 for x in test_df.label])
    return train_lab,test_lab
#compile model and train it
def compile_model(train_seq,train_lab,test_seq,test_lab,token):
    emb = Embedding(len(token.word_index)+1,128,input_length = 50)
    dense = Dense(1,activation = 'sigmoid')
    model = Sequential()
    model.add(emb)
    model.add(Flatten())
    model.add(dense)
    model.compile(optimizer = 'sgd',loss = 'binary_crossentropy',metrics = ['accuracy'])
    print(model.summary())
    model.fit(train_seq,train_lab,epochs = 5)
    loss,accuracy = model.evaluate(test_seq,test_lab)
    return round(accuracy * 100,2),model
#function to predict labels
#takes the model, names list and toke as input
def predict(model,names,token):
    name_token = pad_sequences(token.texts_to_sequences(names),maxlen = 50)
    pred = model.predict_classes(name_token)
    predict_label = ['person' if x == 1 else 'other' for x in pred]
    return predict_label
