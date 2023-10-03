# Multi-Modal Text/Image search using CLIP

This project's origin is [here](https://github.com/weaviate/weaviate-examples/tree/main/clip-multi-modal-text-image-search).

## Description

The Multi-Modal Text/Image Search using CLIP project revolutionizes search capabilities by integrating CLIP technology, allowing users to search for images using natural language descriptions. Built on Weaviate, it supports multi-modal searches, combining text and images effortlessly. Users can describe images or provide images directly for contextual searches. The system is user-friendly, with a customizable interface and support for various image formats, ensuring a seamless and intuitive experience.

![Weaviate Multi-Modal Search](./weaviate-multi-modal-clip-search-demo.png)
(TODO: Add demo video)

This example application spins up a Weaviate instance using the
[multi2vec-clip](https://www.semi.technology/developers/weaviate/current/modules/multi2vec-clip.html)
module, imports a few sample images (you can add your own images, too!) and
provides a very simple search frontend in [React](https://reactjs.org/) using
the [Weaviate JS Client
](https://www.semi.technology/developers/weaviate/current/client-libraries/javascript.html)

Model Credits: This demo uses the [ckip-ViT-B32-multilingual-v1](https://huggingface.co/sentence-transformers/clip-ViT-B-32-multilingual-v1) model from [SBERT.net](https://sbert.net). Shoutout to Nils Reimers and his colleagues for the great Sentence Transformers models. 

## Prerequisites
- Docker & Docker-Compose: Required to set up the Weaviate instance
- Bash: Necessary for executing the provided setup scripts.
- Node.js and npm/yarn: Optional for running the frontend locally.

## Setup instructions

1. Start up Weaviate using `docker-compose up -d`
2. Import the schema (the script will wait for Weaviate to be ready) using `bash ./import/curl/create_schema.sh`
3. Import the images using `bash ./import/curl/import.sh`
4. To run the frontend navigate to the `./frontend` folder and run `yarn && yarn start`. Wait for your browser to open at `http://localhost:3000`

## Usage instructions

### How to run with your own images

Simply add your images to the `./images` folder prior to running the import
script. The script looks for `.jpg` file ending, but Weaviate supports other
image types as well, you can adopt those if you like.


## Dataset license

The images used in this demo are licensed as follows:


* Photo by <a href="https://unsplash.com/@michael75?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Michael</a> on <a href="https://unsplash.com/s/photos/golden-retriever-puppy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
* Photo by <a href="https://unsplash.com/@bastroloog?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Bas Peperzak</a> on <a href="https://unsplash.com/s/photos/fresh-bread?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
* Photo by <a href="https://unsplash.com/@davidkhlr?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">David Köhler</a> on <a href="https://unsplash.com/s/photos/wine-grapes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
* Photo by <a href="https://unsplash.com/@eggbank?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">eggbank</a> on <a href="https://unsplash.com/s/photos/car-city?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
* Photo by <a href="https://unsplash.com/@snowjam?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">John McArthur</a> on <a href="https://unsplash.com/s/photos/airplane?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
          
It is a minimal example using only 5 images, but you can add any amount of
images yourself!


