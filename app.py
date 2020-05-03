from database import init_db
from flask import Flask, jsonify
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.debug = True
init_db()

default_query = '''
{
    allEmployees {
        edges {
            node {
                id,
                name,
                department {
                    id,
                    name
                },
                role {
                    id,
                    name
                }
            }
        }
    }
}'''.strip()


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)


@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World!"})


if __name__ == '__main__':
    app.run()
