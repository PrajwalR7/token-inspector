# TOKEN_INSPECTOR

Token inspector is a web app, using which you can get to know the number of tokens your data is generating even before making a call to openAI. This is useful when you are working with large data and want to know the number of tokens it is generating. This is also useful when you are working with openAI's paid services like Azure and want to calculate the cost.

## How to use
Make a `POST` request to this API - `https://token-inspector.herokuapp.com/` with the following body:
```json
{
    "model": "gpt-3.5-turbo",
    "data": [
      {"role": "system", "content": "You are a helpful, pattern-following assistant that translates corporate jargon into plain English."},
      {"role": "system", "name":"example_user", "content": "New synergies will help drive top-line growth."},
    ]
}
```
The response body will contain an object which will denote the number of tokens generated
```json
{
    "num_token": 8959
}
```