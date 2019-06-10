"""Serve the GraphQL interface using flask

Adapted from:
https://codeburst.io/how-to-build-a-graphql-wrapper-for-a-restful-api-in-python-b49767676630

"""
import os
from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from graphene import Schema
from schema import Query


def run_graphqli_app():
    """Make a flask app exposing the GraphQLi interface as a route"""
    main_schema = Schema(query=Query)
    view_func = GraphQLView.as_view(
        "graphql", schema=main_schema, graphiql=True, batch=True
    )

    app = Flask(__name__)
    CORS(app)
    app.add_url_rule("/graphql", view_func=view_func)
    # used by apollo client
    # app.add_url_rule(
    #     "/graphql/batch",
    #     view_func=GraphQLView.as_view("graphql", schema=main_schema, batch=True),
    # )

    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))


if __name__ == "__main__":
    run_graphqli_app()
