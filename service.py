import face_recognition

REFERENCE_IMAGE_PATH = "images/pessoa1/WhatsApp Image 2024-05-24 at 13.27.41 (1).jpeg"


def compare_faces(uploaded_image):
    # Carregar a imagem de referência e detectar as características do rosto
    reference_image = face_recognition.load_image_file(REFERENCE_IMAGE_PATH)
    reference_encodings = face_recognition.face_encodings(reference_image)
    if not reference_encodings:
        raise ValueError("Nenhum rosto encontrado na imagem de referência")

    # Detectar características no rosto da imagem enviada
    uploaded_encodings = face_recognition.face_encodings(uploaded_image)
    if not uploaded_encodings:
        raise ValueError("Nenhum rosto encontrado na imagem enviada")

    # Comparar o primeiro rosto encontrado
    result = face_recognition.compare_faces(
        [reference_encodings[0]], uploaded_encodings[0]
    )
    return result[0]
