from flask import Flask, request, jsonify, make_response
import joblib
import pandas as pd
import mapper
import requests

app = Flask(__name__)
lda = joblib.load("model_v5.pkl")
label_encoders = joblib.load("label_encoders.pkl")

@app.route("/predict", methods=["POST"])
def predict():
  try:
    print(request.json)
    requestData = mapper.MapperData.mapper(request.json);
    data = requestData["dados"]
    sample = pd.DataFrame([data])
    for col, le in label_encoders.items():
        if col != "class":
            sample[col] = sample[col]

    # Certifique-se de que a amostra tem a forma correta
    if len(sample.shape) == 1:
        sample = pd.DataFrame([sample])
    else:
        sample = pd.DataFrame(sample)
    prediction = lda.predict(sample)
    if prediction[0] == "Aprovado":
        resposta = "Digno de Crédito"
    elif prediction[0] == "Reprovado":
        resposta = "Não é digno de Crédito"

    result = requestData["conta"]
    result["resposta"] = resposta
    print(result)
    return make_response(jsonify(result))
  except Exception as e:
    return make_response(jsonify({"error": str(e)}), 500)


if __name__ == "__main__":
    app.run(host="0.0.0.0")