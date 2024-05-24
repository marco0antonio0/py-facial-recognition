# API Flask de Reconhecimento Facial

Este projeto é uma API desenvolvida em Flask para reconhecimento facial. A API permite fazer upload de uma imagem e comparar com uma imagem de referência para verificar se há uma correspondência facial.

## Funcionalidades

- Receber uma imagem via upload.
- Comparar a imagem recebida com uma imagem de referência pré-definida.
- Retornar um resultado booleano indicando se houve uma correspondência ou não.

## Estrutura do Projeto

```
├── app.py
├── controller.py
├── service.py
└── images
└── pessoa1
└── WhatsApp Image 2024-05-24 at 13.27.41 (1).jpeg
```

- **app.py**: Inicializa o aplicativo Flask e configura as rotas.
- **controller.py**: Define as rotas e o comportamento da API ao receber uma requisição.
- **service.py**: Contém a lógica de comparação facial usando a biblioteca `face_recognition`.
- **images/pessoa1**: Diretório onde a imagem de referência é armazenada.

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual e ative-o:

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

4. Certifique-se de que a imagem de referência está no caminho correto definido no `service.py` (por padrão: `images/pessoa1/WhatsApp Image 2024-05-24 at 13.27.41 (1).jpeg`).

## Uso

1. Inicie o servidor Flask:

    ```sh
    python app.py
    ```

2. Faça uma requisição POST para o endpoint `/compare` com a imagem que deseja comparar. Você pode usar ferramentas como `curl` ou Postman para testar.

    Exemplo usando `curl`:

    ```sh
    curl -X POST -F "image=@caminho/para/sua/imagem.jpeg" http://127.0.0.1:5000/compare
    ```

3. A resposta será um JSON indicando se houve uma correspondência:

    ```json
    {
        "match": true
    }
    ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
