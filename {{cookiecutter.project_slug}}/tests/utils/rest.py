class RestMixin:

    @staticmethod
    def get(client, url, headers=None):

        if headers:
            result = client.get(
                url,
                content_type='application/json',
                headers=headers
            )
        else:
            result = client.get(
                url,
                content_type='application/json',
            )
        return result

    @staticmethod
    def post(client, url, data, headers=None):

        if headers:
            result = client.post(
                url,
                data=data,
                content_type='application/json',
                headers=headers
            )
        else:
            result = client.post(
                url,
                data=data,
                content_type='application/json',
            )
        return result
