from tiktoken import encoding_for_model, get_encoding


def get_num_token(body):
    try:
        encoding = encoding_for_model(body.model)
    except KeyError:
        print('Key error')
        # If model name provided is wrong, falling back to gpt-3.5-turbo's encoding model
        encoding = get_encoding("cl100k_base")
    num_token = 0
    for message in body.data:
        num_token += 4
        if (message['role'] == "name"):
            num_token -= 1
        num_token += len(encoding.encode(message['content']))

    num_token += 2
    return num_token