# backend-api

## Run Locally

Clone the project

```bash
git clone git@github.com:malaysianpaygap/backend-api.git
```

Create the conda environment

```bash
conda create --name api python=3.7
conda activate api
```

## Running Tests

Before running the tests make sure that you have Docker installed and running as the
test will create a dummy postgresql database to run the test on.

To run the tests, run the following command

```bash
make setup-db
make test
```
