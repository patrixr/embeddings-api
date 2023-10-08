# Embedding Generation Service

This FastAPI application provides an HTTP API for generating embeddings. The
service accepts POST requests at the endpoint `/generate_embedding/`, taking a
JSON body with two fields: `instruction` and `sentence`.

## Requirements

The application requires an environment variable `API_KEY` to be set before
running. This will be used for client authorization on each request.

## API Endpoint

### POST `/generate_embedding/`

Generates embeddings based on the provided instruction and sentence.

#### Request Body

The request body should be a JSON object with the following properties:

- `instruction` (string): The instruction string.
- `sentence` (string): The sentence string.

Example:

```json
{
  "instruction": "Example instruction",
  "sentence": "Example sentence"
}
```

#### Response

The response will be a JSON object with the following properties:

- `embedding`` (array): The generated embedding.

Example

```json
{
  "embedding": [0.1, 0.2, 0.3, 0.4, 0.5]
}
```

## Authorization

The API requires an API key for authorization. The API key should be included in
the authorization header in the format Bearer {API_KEY}.

Example: `Authorization: Bearer your_api_key`

Please replace `your_api_key` with your actual API key in the `Authorization`
header when making requests to the API.
