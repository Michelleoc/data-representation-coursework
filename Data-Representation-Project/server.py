from flask import Flask, jsonify, request, abort
### from bookDAO import bookDAO

app = Flask(__name__, static_url_path='', static_folder='static')

teams = [
    {'team':'England'},
    {'team':'Wales'},
    {'team':'United States'},
    {'team':'Iran'},
    ]

@app.route('/teams', methods=['GET'])
def getAllTeams():
    return jsonify(teams)

@app.route('/vote/<teamname>', methods=['POST'])
def voteForTeams(teamname):
    return jsonify({'teams':teamname})

@app.route('/vote/<teamname>', methods=['GET'])
def getCountForTeams(teamname):
    return '999'

@app.route('/vote', methods=['GET'])
def getAllCount():
    return jsonify({'teams':'test', 'count':999})

@app.route('/vote/all', methods=['delete'])
def deleteAllVote():
    return jsonify({'done':True})


''' 

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/books"
@app.route('/books')
def getAll():
    #print("in getall")
    results = bookDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/books/<int:id>')
def findById(id):
    foundBook = bookDAO.findByID(id)

    return jsonify(foundBook)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    book = {
        "title": request.json['title'],
        "author": request.json['author'],
        "price": request.json['price'],
    }
    values =(book['title'],book['author'],book['price'])
    newId = bookDAO.create(values)
    book['id'] = newId
    return jsonify(book)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBook = bookDAO.findByID(id)
    if not foundBook:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'title' in reqJson:
        foundBook['title'] = reqJson['title']
    if 'Author' in reqJson:
        foundBook['author'] = reqJson['author']
    if 'price' in reqJson:
        foundBook['price'] = reqJson['price']
    values = (foundBook['title'],foundBook['author'],foundBook['price'],foundBook['id'])
    bookDAO.update(values)
    return jsonify(foundBook)
        

    

@app.route('/books/<int:id>' , methods=['DELETE'])
def delete(id):
    bookDAO.delete(id)
    return jsonify({"done":True})


'''

if __name__ == '__main__' :
    app.run(debug= True)