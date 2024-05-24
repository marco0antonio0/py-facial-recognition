from flask import request, jsonify
import cv2
import numpy as np
from service import compare_faces


def setup_routes(app):
    @app.route("/compare", methods=["POST"])
    def upload_and_compare():
        if "image" not in request.files:
            return jsonify({"error": "Nenhuma imagem fornecida"}), 400

        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "Nenhum arquivo selecionado"}), 400

        if file:
            try:
                # Converter o arquivo de imagem para um array NumPy
                in_memory_file = file.read()
                nparr = np.frombuffer(in_memory_file, np.uint8)
                img = cv2.imdecode(
                    nparr, cv2.IMREAD_COLOR
                )  # Converter para uma imagem OpenCV

                # Chamar o serviço de comparação de rostos
                match_result = compare_faces(img)

                # Converter numpy bool para bool do Python para ser serializável
                is_match = bool(match_result)

                return jsonify({"match": is_match})
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        return jsonify({"error": "Erro desconhecido"}), 500
