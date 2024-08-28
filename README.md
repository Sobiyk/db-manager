# DB manager

## Инструкция по запуску

- Склонировать репозиторий
  ```
  git clone git@github.com:Sobiyk/vk_test_assigment.git
  ```

- Заполнить .env файл по шаблону
  ```
  TNT_HOST="tarantool1"
  TNT_PORT='3301'
  ```

- Развернуть docker контейнеры с помощью docker-compose
  ```
  docker-compose up -d --build
  ```

- Доукументация API
  ```
  http://localhost:8000/docs
  ```

## Список эндпоинтов
- POST `/api/login`
- POST `/api/write`
- POST `/api/read`

- ### POST `/api/login` - `Login`
  - #### body: x-www-form-urlencoded
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```
  - #### Successful Response - 200 OK
    ```json
    {
      "access_token": "some_token",
      "token_type": "bearer"
    }
    ```
  - #### Validation Error - 422 Unprocessable Entity
    ```json
    {
      "detail": [
        {
          "loc": [
            "string",
            0
          ],
          "msg": "string",
          "type": "string"
        }
      ]
    }
    ```

- ### POST `/api/read` - `Read Batch`
- #### body: JSON
    ```json
    {
      "keys": ["key1", "key2"]
    }
    ```
  - #### Successful Response - 200 OK
    ```json
    {
      "data": {
        "key1": ["key1", "value1", "value2"],
        "key2": ["key2", "value1"]
      }
    }
    ```
  - #### Validation Error - 422 Unprocessable Entity
    ```json
    {
      "detail": [
        {
          "loc": [
            "string",
            0
          ],
          "msg": "string",
          "type": "string"
        }
      ]
    }
    ```
  - #### Bad Request - 400
    ```json
    {
      "detail": "message"
    }
    ```
  - #### Unauthorized - 401
    ```json
    {
      "detail": "Not authenticated"
    }
    ```

- ### POST `/api/write` - `Write Batch`
- #### body: JSON
    ```json
    {
      "data": {
        "key": "value",
        "key": "value"
      }
    }
    ```
  - #### Successful Response - 201 CREATED
    ```json
    {
      "status": "success"
    }
    ```
  - #### Validation Error - 422 Unprocessable Entity
    ```json
    {
      "detail": [
        {
          "loc": [
            "string",
            0
          ],
          "msg": "string",
          "type": "string"
        }
      ]
    }
    ```
  - #### Bad Request - 400
    ```json
    {
      "detail": "message"
    }
    ```
  - #### Unauthorized - 401
    ```json
    {
      "detail": "Not authenticated"
    }
    ```
