# shop-monorepo

brew install poetry

##for each microservice##
see structure as in `catalogue`

 - create poetry.toml with `poetry init`
 - fill in requirements
 - than in microservice's directory run `poetry install`

 open each microservice in it's own window in ide so you can create a separate env for each of them
 to create env run `poetry shell`

 then run it via python

 keep in mind that each folder in shop-monorepo is a python package


