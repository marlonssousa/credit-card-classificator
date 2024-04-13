from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class Model:
    def __init__(self) -> None:
        # Criar o modelo sequencial
        self.model = Sequential()
        # Adicionar camadas densas (fully connected)
        self.model.add(Dense(64, activation='relu', input_dim=19))  # Defina NUM_FEATURES como o número de features de entrada
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))  # Camada de saída com ativação sigmoid para classificação binária
        # Compilar o modelo
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        self.model.load_weights("models/credit-card-weights.h5")

    def predict(self, value):
        return self.model.predict(value)