# Serving blip image captioning with BentoML

This project is a blip image captioning service built with [BentoML](https://github.com/bentoml/BentoML).

Try it on `BentoCloud`. [Deploy Now](https://money.cloud.bentoml.com/projects/whisperx)

It comes with [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large),
you can easily customize it to try other [image-to-text](https://huggingface.co/models?pipeline_tag=image-to-text) models.

## 🏃 Quick start 🏃

To quickly get started, follow the instructions below or try this [tutorial](https://colab.research.google.com/github/xianml/blip-image-captioning/blob/main/blip_image_captioning.ipynb) in Google Colab.

### 1. Install dependencies

```bash
pip install -U -q -r requirements.txt
```

### 2. Import model

we can download the blip model from huggingface to local BentoML model store using bentoml sdk.

```bash
python import_model.py
```

### 3. Start Server

We can easily start the server locally with just one single command:

```bash
bentoml serve service:svc
```

## 🎯 Try it out 🎯
we have the following ways to interact with the server:

### 1. Web UI

Open http://0.0.0.0:3000 from your browser to send test requests from the Web UI.

### 2. Raw HTTP
Alternatively, test it with curl command. And we can test the image captioning model under conditional or un-conditional by giving it a prompt input or not.

```bash
!curl -X 'POST' \
  'http://127.0.0.1:3000/generate' \
  -H 'accept: text/plain' \
  -H 'Content-Type: multipart/form-data' \
  -F 'img=@three-dog.jpg;type=image/jpeg' \
  -F 'prompt='

!curl -X 'POST' \
  'http://127.0.0.1:3000/generate' \
  -H 'accept: text/plain' \
  -H 'Content-Type: multipart/form-data' \
  -F 'img=@three-dog.jpg;type=image/jpeg' \
  -F 'prompt=this picture is '
```

### 3. BentoML client

you can just simply run the following code to get the result.

```bash
python client.py
```


## 🚀 Production Deployment 🚀

to deploy it to production, we need to build the Bento first.
learn more about [Bento](https://docs.bentoml.com/en/latest/concepts/bento.html).

### Build and push Bento

```bash
> bentoml build

██████╗ ███████╗███╗   ██╗████████╗ ██████╗ ███╗   ███╗██╗
██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║██║
██████╔╝█████╗  ██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║██║
██╔══██╗██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║██║
██████╔╝███████╗██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║███████╗
╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝

Successfully built Bento(tag="image_captioning-svc:virrs2tnskexaasc").
```

BentoML provides a number of [deployment options](https://docs.bentoml.com/en/latest/concepts/deploy.html).
The easiest way to set up a production-ready endpoint of your text embedding service is via BentoCloud,
the serverless cloud platform built for BentoML, by the BentoML team.

Next steps:

1. Sign up for a BentoCloud account [here](https://www.bentoml.com/).
2. Get an API Token, see instructions [here](https://docs.bentoml.com/en/latest/bentocloud/getting-started/ship.html#acquiring-an-api-token).
3. Push your Bento to BentoCloud: `bentoml push image_captioning-svc:virrs2tnskexaasc`
4. Deploy via Web UI, see [Deploying on BentoCloud](https://docs.bentoml.com/en/latest/bentocloud/getting-started/ship.html#deploying-your-bento)

## Community

👉 Join our [AI Application Developer community!](https://l.bentoml.com/join-slack)
