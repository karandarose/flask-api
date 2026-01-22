from flask import Flask
import routes

app = Flask(__name__)

app.register_blueprint(routes.product)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8086')






# @app.route('/string')
# def respond_string():
#     return 'Here is a response with a python string'

# @app.route('/html')
# def respond_html():
#     return '<h1 align="center" style="color: blue;">Here is a response with HTML</h1>'

# @app.route('/json/<a>/<b>')
# def resond_json(a, b):
#     # def addition():
#     #     count = 1 + 1
#     #     return count
#     # sum = addition()

#     sum = int(a) + int(b)

#     return jsonify({"message" : f"Here is a response with test and another return {sum}"})