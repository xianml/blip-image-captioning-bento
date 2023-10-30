if __name__ == "__main__":
    from bentoml.client import Client
    import PIL.Image

    import nest_asyncio

    nest_asyncio.apply()

    client = Client.from_url("http://localhost:3000")
    print(
        client.generate(
            img=PIL.Image.open("./three-dog.jpg"),
            prompt="this picture is",
        )
    )