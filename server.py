"""Serve the GraphQL interface using flask

Adapted from:
https://codeburst.io/how-to-build-a-graphql-wrapper-for-a-restful-api-in-python-b49767676630

"""
import os
from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema
from schema import Query


def run_graphqli_app():
    """Make a flask app exposing the GraphQLi interface as a route"""
    view_func = GraphQLView.as_view(
        "graphql", schema=Schema(query=Query), graphiql=True
    )

    app = Flask(__name__)
    app.add_url_rule("/graphql", view_func=view_func)

    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))


if __name__ == "__main__":
    run_graphqli_app()
