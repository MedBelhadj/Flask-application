from flask import Flask
from flask import jsonify
import numpy as np

applicaition = Flask(__name__)

@applicaition.route('/')
def hello():
    return 'Hello Mohamed Belhadj\n'
    
@applicaition.route('/random/<n>')
def randomvalues(n):
    values = np.random.randint(0,10,int(n))
    result = {'values' : values.tolist()}
    return jsonify(result)
    
if __name__ == '__main__':
    applicaition.run(debug=True)